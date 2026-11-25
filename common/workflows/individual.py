"""Individual workflow with method specific reviewers.

Site-wide roles (created by scripts/setup_roles.py):

reviewer_<model> == reads drafts of the method, accepts/declines their publish requests
editor           == reads all drafts and can edit them
administrator    == reads all drafts and can delete them

Record states: draft -> submitted -> approved -> published, or revision_requested when
declined. The owner publishes the approved draft. Submitted and approved drafts are
locked, nobody can edit them.
"""

from invenio_i18n import lazy_gettext as _
from invenio_rdm_records.services.generators import RecordOwners
from invenio_records_permissions.generators import SameAs
from invenio_requests.customizations import CommentEventType
from oarepo_config import IndividualWorkflow
from oarepo_requests.services.permissions.generators import RequestActive
from oarepo_workflows import (
    AutoApprove,
    IfInState,
    WorkflowRequest,
    WorkflowRequestPolicy,
    WorkflowTransitions,
)
from oarepo_workflows.requests.events import WorkflowEvent
from oarepo_workflows.services.permissions.generators import UserWithRole

from .generators import DynamicReviewer, IfHasReviewerRole


def extend_permissions(policy):
    class IndividualWorkflowPermissions(policy):
        can_rdm_preview = (
            *policy.can_rdm_preview,
            UserWithRole("editor"),
            UserWithRole("administrator"),
            DynamicReviewer(),
        )
        can_rdm_review = (*policy.can_rdm_review, UserWithRole("editor"))
        can_update = (
            IfInState(["draft", "revision_requested"], [SameAs("can_rdm_review")]),
        )
        # not limited to the states above: oarepo needs it on published records for sharing
        can_update_draft = (
            IfInState(["submitted", "approved"], [], else_=[SameAs("can_rdm_review")]),
        )
        can_publish = (
            *policy.can_publish,
            IfInState("approved", [RequestActive()]),
        )
        can_delete = (
            *policy.can_delete,
            IfInState(
                ["draft", "submitted", "approved", "revision_requested"],
                [UserWithRole("administrator")],
            ),
        )

    return IndividualWorkflowPermissions


def publish_request():
    return WorkflowRequest(
        requesters=[
            IfInState(
                ["draft", "revision_requested"],
                [IfHasReviewerRole([RecordOwners()])],
            )
        ],
        recipients=[DynamicReviewer()],
        transitions=WorkflowTransitions(
            submitted="submitted",
            accepted="approved",
            declined="revision_requested",
            cancelled="draft",
        ),
        events={
            CommentEventType.type_id: WorkflowEvent(
                submitters=[RecordOwners(), DynamicReviewer()]
            )
        },
    )


class IndividualWorkflowRequests(WorkflowRequestPolicy):
    publish_draft = publish_request()
    publish_new_version = publish_request()
    publish_changed_metadata = publish_request()
    publish_approved_draft = WorkflowRequest(
        requesters=[IfInState("approved", [RecordOwners()])],
        recipients=[AutoApprove()],
        transitions=WorkflowTransitions(accepted="published"),
    )


individual_workflow = IndividualWorkflow(
    label=_("Individual Submission Workflow"),
    review_required=True,
    publish_without_review_roles=["direct-publisher"],
    extra_permissions=extend_permissions,
    extra_requests=IndividualWorkflowRequests,
)
