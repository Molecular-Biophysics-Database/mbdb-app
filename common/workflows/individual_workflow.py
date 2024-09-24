# Roles within the workflow:
#
# administrator:
#  - IBT staff
#  - has the overall technical responsibility for MBDB (extensive rights except publication related operation)
#  - main tasks include changing records and drafts for technical reasons (e.g. model change, old drafts)
#
# editor:
#  - IBT staff
#  - has the overall scientific responsibility for MBDB
#  - main task include changing published records and drafts on scientific ground
#
# reviewer:
#  - MBDB community (IBT staff initially)
#  - Method specific scientific reviewer
#  - Main task is to scientifically review records durin depositions
#
# Synthetic roles:
#
# RecordOwners() == actual owner of the record (person who created it)
#
# Record states:
#
# draft == record is being created
# submitted == record is submitted for approval/publishing but not yet accepted (locked)
# accepted == record has been approved for publication, the decision of timing is made by owner (locked)
# published == record is published
# deleting == record is in the process of being deleted (request filed but not yet accepted)
#
from invenio_records_permissions.generators import AnyUser, AuthenticatedUser

from oarepo_requests.services.permissions.generators import IfRequestedBy
from oarepo_runtime.services.permissions.generators import RecordOwners
from oarepo_workflows import (
    AutoApprove,
    IfInState,
    WorkflowRequest,
    WorkflowRequestPolicy,
    WorkflowTransitions,
    AutoRequest,
)

from oarepo_requests.services.permissions.workflow_policies import (
    RequestBasedWorkflowPermissions,
)

from .custom_generators import UserWithRole


# TODO: naming issue: DefaultWorkflowPermissions vs DefaultWorkflowPermissionPolicy
class IndividualWorkflowPermissions(RequestBasedWorkflowPermissions):
    can_create = [AuthenticatedUser()]

    can_read = [
        RecordOwners(),
        # administrator and editor can always read
        UserWithRole("administrator"),
        UserWithRole("editor"),
        IfInState(
            "published",
            then_=[
                AnyUser(),
            ],
        ),
    ]

    can_update = [
        # administrator and editor can always update
        UserWithRole("administrator"),
        UserWithRole("editor"),
        # owners can edit drafts before submission
        IfInState(
            "draft",
            then_=[
                RecordOwners(),
            ],
        ),
    ]

    can_delete = [
        # administrator and editor can always delete
        UserWithRole("administrator"),
        UserWithRole("editor"),
        # draft can be deleted, published record must be deleted via request
        IfInState(
            "draft",
            then_=[
                RecordOwners(),
            ],
        ),
    ]

    can_publish = [
        # only accepted drafts can be published
        RecordOwners(),
    ]


class IndividualWorkflowRequests(WorkflowRequestPolicy):
    review_draft = WorkflowRequest(
        # reviewers are notified when a draft is submitted
        requesters=[
            IfInState("submitted", then_=[AutoRequest()]),
        ],
        recipients=[UserWithRole("reviewer")],
        transitions=WorkflowTransitions(declined="draft", accepted="accepted"),
    )

    delete_published_record = WorkflowRequest(
        # if the record is draft, it is covered by the delete permission
        # if published or submitted, only the owner or curator can request deleting
        requesters=[
            IfInState(
                "published",
                then_=[
                    RecordOwners(),
                    UserWithRole("administrator"),
                    UserWithRole("editor"),
                ],
            ),
        ],
        # if the requester is the curator of the community or administrator, auto approve the request,
        # otherwise, the request is sent to the curator
        recipients=[
            IfRequestedBy(
                requesters=[
                    UserWithRole("administrator"),
                ],
                then_=[AutoApprove()],
                else_=[UserWithRole("administrator")],
            )
        ],
        # the record comes to the state of retracting when the request is submitted. If the request
        # is accepted, the record is deleted, if declined, it is published again.
        transitions=WorkflowTransitions(
            submitted="retracting", declined="published", accepted="deleted"
        ),
    )

    assign_doi = WorkflowRequest(
        # Upon publication, a DOI assignment request is automatically generated
        requesters=[
            IfInState("published", then_=[AutoRequest()])
        ],
        recipients=[AutoApprove()],
    )
