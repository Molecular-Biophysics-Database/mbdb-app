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
from invenio_rdm_records.services.generators import IfRecordDeleted
from invenio_records_permissions.generators import (
    AnyUser,
    AuthenticatedUser,
    Disable,
    SystemProcess,
)
from invenio_users_resources.services.permissions import UserManager
from oarepo_requests.services.permissions.workflow_policies import (
    RequestBasedWorkflowPermissions,
)
from oarepo_runtime.services.permissions.generators import RecordOwners
from oarepo_workflows import (
    AutoApprove,
    AutoRequest,
    IfInState,
    WorkflowRequest,
    WorkflowRequestPolicy,
    WorkflowTransitions,
)

from .custom_generators import UserWithRole
from .custom_generators import DynamicReviewer


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
        IfInState(
            ["submitted", "accepted", "returned_draft"],
            then_=[
                DynamicReviewer(),
            ],
        ),
    ]

    can_read_deleted = [
        IfRecordDeleted(
            then_=[
                UserManager,  # this is strange, but taken from RDM
                UserWithRole("administrator"),
                SystemProcess(),
            ],
            else_=can_read,
        )
    ]

    can_search_all_records = RequestBasedWorkflowPermissions.can_search
    can_read_all_records = can_read

    can_update = [
        # owners can edit drafts before submission
        IfInState(
            ["draft", "returned_draft"],
            then_=[
                RecordOwners(),
                UserWithRole("editor"),
            ],
        ),
    ]

    can_delete = [
        # draft can be directly deleted, published record must be deleted via request
        # TODO Check with JD who is supposed to delete published records
        IfInState(
            ["draft", "returned_draft"],
            then_=[
                RecordOwners(),
                UserWithRole("administrator"),
            ],
        ),
        IfInState(
            "submitted",
            then_=[
                RecordOwners(),
                UserWithRole("administrator"),
            ],
        ),
        IfInState(
            "accepted",
            then_=[
                RecordOwners(),
                UserWithRole("administrator"),
            ],
        ),
        IfInState(
            "retracting",
            then_=[
                UserWithRole("administrator"),
            ]
        )]

    can_manage_files = [
        Disable(),
    ]


class IndividualWorkflowRequests(WorkflowRequestPolicy):
    submit_draft = WorkflowRequest(
        # reviewers are notified when a draft is submitted
        requesters=[
            IfInState(["draft", "returned_draft"], then_=[RecordOwners()]),
        ],
        recipients=[DynamicReviewer()],
        transitions=WorkflowTransitions(
            declined="returned_draft", submitted="submitted", accepted="accepted"
        ),
    )

    # TODO: Currently, new versions are not implemented, when it is,
    #       please uncomment the following
    """
    new_version = WorkflowRequest(
        requesters=[
            IfInState(
                "published",
                then_=[
                    RecordOwners(),
                    UserWithRole("administrator"),
                    UserWithRole("editor")
                ],
            )
        ],
        # the request is auto-approve, we do not limit the owner of the record to create a new
        # draft version. It will need to be accepted by the curator though.
        recipients=[AutoApprove()],
    )
    """

    delete_published_record = WorkflowRequest(
        # if the record is draft, it is covered by the delete permission
        # if published or submitted, only the owner or curator can request deleting
        requesters=[
            IfInState(
                "published",
                then_=[
                    RecordOwners(),
                    UserWithRole("editor"),
                    UserWithRole("administrator"),
                ],
            ),
        ],
        recipients=[UserWithRole("administrator")],
        # the record comes to the state of retracting when the request is submitted. If the request
        # is accepted, the record is deleted, if declined, it is published again.
        transitions=WorkflowTransitions(
            submitted="retracting", declined="published", accepted="deleted"
        ),
    )

    assign_doi = WorkflowRequest(
        # Upon publication, a DOI assignment request is automatically generated
        requesters=[IfInState("published", then_=[AutoRequest()])],
        recipients=[AutoApprove()],
    )

    publish_accepted_draft = WorkflowRequest(
        requesters=[
            IfInState("accepted", then_=[RecordOwners()]),
        ],
        recipients=[AutoApprove()],
        transitions=WorkflowTransitions(declined="accepted", accepted="published"),
    )
