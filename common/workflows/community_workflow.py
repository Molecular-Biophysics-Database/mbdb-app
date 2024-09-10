#
# Roles within the workflow:
#
# administrator == super curator, IBT staff
# curator == scientific curator, IBT staff
#
# Community roles:
#
# CommunityMembers() == member of the community
# DefaultCommunityRole("administrator") == administrator of the community
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

from datetime import timedelta

from oarepo_communities.services.permissions.policy import CommunityDefaultWorkflowPermissions

from invenio_records_permissions.generators import AnyUser
from oarepo_communities.services.permissions.generators import (
    CommunityMembers,
    DefaultCommunityRole,
)
from oarepo_requests.services.permissions.generators import IfRequestedBy
from oarepo_runtime.services.permissions.generators import RecordOwners
from oarepo_workflows import (
    AutoApprove,
    IfInState,
    WorkflowRequest,
    WorkflowRequestEscalation,
    WorkflowRequestPolicy,
    WorkflowTransitions,
)
from .custom_generators import UserWithRole, IfHasPreviousVersion




# TODO: naming issue: DefaultWorkflowPermissions vs DefaultWorkflowPermissionPolicy
class CommunityWorkflowPermissions(CommunityDefaultWorkflowPermissions):
    can_create = [
        CommunityMembers(),
        UserWithRole("administrator"),
        UserWithRole("curator"),
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
        ),
        IfInState(
            "retracting",
            then_=[
                RecordOwners(),
                UserWithRole("curator"),
                UserWithRole("administrator"),
            ],
        ),
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
        # if not draft, can not be directly updated, must use request
        IfInState(
            "submitted",
            then_=[
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


class CommunityWorkflowRequests(WorkflowRequestPolicy):
    publish_draft = WorkflowRequest(
        # if the record is in draft state, the owner or curator can request publishing
        requesters=[
            IfInState(
                "draft",
                then_=[
                    RecordOwners(),
                    DefaultCommunityRole("administrator"),
                ],
            ),
        ],
        recipients=[
            IfRequestedBy(
                requesters=[
                    DefaultCommunityRole("administrator")
                ],
                then_=[UserWithRole("curator")],
                else_=[
                    UserWithRole("curator"),
                    DefaultCommunityRole("administrator"),
                ],
            ),
        ],
        transitions=WorkflowTransitions(
            submitted="submitted", accepted="published", declined="draft"
        ),
        # if the request is not resolved in 21 days, escalate it to the administrator
        escalations=[
            WorkflowRequestEscalation(
                after=timedelta(days=14), recipients=[UserWithRole("administrator")]
            )
        ],
    )

    edit_published_record = WorkflowRequest(
        requesters=[
            IfInState(
                "published",
                then_=[
                    RecordOwners(),
                    UserWithRole("curator"),
                    UserWithRole("administrator"),
                ],
            )
        ],
        # the request is auto-approve, we do not limit the owner of the record to create a new
        # draft version.
        recipients=[AutoApprove()],
    )

    delete_published_record = WorkflowRequest(
        # if the record is draft, it is covered by the delete permission
        # if published, only the owner or curator can request deleting
        requesters=[
            IfInState(
                "published",
                then_=[
                    RecordOwners(),
                    UserWithRole("administrator"),
                ],
            )
        ],
        # if the requester is the curator of the community or administrator, auto approve the request,
        # otherwise, the request is sent to the curator
        recipients=[
            IfRequestedBy(
                requesters=[
                    UserWithRole("administrator"),
                ],
                then_=[AutoApprove()],
                else_=[DefaultCommunityRole("administrator")],
            )
        ],
        # the record comes to the state of retracting when the request is submitted. If the request
        # is accepted, the record is deleted, if declined, it is published again.
        transitions=WorkflowTransitions(
            submitted="retracting", declined="published", accepted="deleted"
        ),
        # if the request is not resolved in 14 days, escalate it to the administrator
        escalations=[
            WorkflowRequestEscalation(
                after=timedelta(days=14), recipients=[UserWithRole("administrator")]
            )
        ],
    )
