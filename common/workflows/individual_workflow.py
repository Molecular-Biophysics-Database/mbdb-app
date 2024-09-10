#
# Roles within the workflow:
#
# administrator == super curator, IBT staff
# curator == scientific curator, IBT staff
#
#
# Synthetic roles:
#
# RecordOwners() == actual owner of the record (person who created it)
#
# Record states:
#
# draft == record is being created
# submitted == record is submitted for approval/publishing but not yet accepted
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
)

from oarepo_requests.services.permissions.workflow_policies import RequestBasedWorkflowPermissions

from .custom_generators import UserWithRole


# TODO: naming issue: DefaultWorkflowPermissions vs DefaultWorkflowPermissionPolicy
class IndividualWorkflowPermissions(RequestBasedWorkflowPermissions):
    can_create = [
        AuthenticatedUser()
    ]

    can_read = [
        RecordOwners(),
        # curator can see the record in any state
        UserWithRole("curator"),
        # administrator can see everything
        UserWithRole("administrator"),
        IfInState(
            "published",
            then_=[
                AnyUser(),
            ],
        )
    ]

    can_update = [
        IfInState(
            "draft",
            then_=[
                RecordOwners(),
                UserWithRole("curator"),
                UserWithRole("administrator"),
            ],
        ),
    ]

    can_delete = [
        # draft can be deleted, published record must be deleted via request
        IfInState(
            "draft",
            then_=[
                RecordOwners(),
                UserWithRole("curator"),
                UserWithRole("administrator"),
            ],
        ),
    ]

    can_publish = [
        IfInState(
            "draft",
            then_=[RecordOwners()]
        )
    ]


class IndividualWorkflowRequests(WorkflowRequestPolicy):
    publish_draft = WorkflowRequest(
        # if the record is in draft state, the owner can publish
        requesters=[
            IfInState(
                "draft",
                then_=[
                    RecordOwners(),
                ]
            ),
        ],
        recipients=[AutoApprove()],
    )

    edit_published_record = WorkflowRequest(
        requesters=[
            IfInState(
                "published",
                then_=[
                    RecordOwners(),
                ],
            )
        ],
        # the request is auto-approve, we do not limit the owner of the record to create a new
        # draft version. It will need to be accepted by the curator though.
        recipients=[AutoApprove()],
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
                ],
            ),
        ],
        # if the requester is the curator of the community or administrator, auto approve the request,
        # otherwise, the request is sent to the curator
        recipients=[
            IfRequestedBy(
                requesters=[
                    UserWithRole("administrator"),
                    UserWithRole("curator"),
                ],
                then_=[AutoApprove()],
                else_=[UserWithRole("administrator")])
        ],
        # the record comes to the state of retracting when the request is submitted. If the request
        # is accepted, the record is deleted, if declined, it is published again.
        transitions=WorkflowTransitions(
            submitted="retracting", declined="published", accepted="deleted"
        ),
    )

