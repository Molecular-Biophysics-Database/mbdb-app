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
# Record states:
#
# draft == record is being created
# submitted == record is submitted for approval/publishing but not yet accepted (locked)
# accepted == record has been approved for publication, the decision of timing is made by owner (locked)
# published == record is published
# deleting == record is in the process of being deleted (request filed but not yet accepted)
#

from invenio_records_permissions.generators import AnyUser, Disable
from oarepo_communities.services.permissions.generators import (
    CommunityMembers,
    DefaultCommunityRole,
    PrimaryCommunityMembers,
)
from oarepo_communities.services.permissions.policy import (
    CommunityDefaultWorkflowPermissions,
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

from .custom_generators import UserWithRole, DynamicReviewer


# TODO: naming issue: DefaultWorkflowPermissions vs DefaultWorkflowPermissionPolicy
class CommunityWorkflowPermissions(CommunityDefaultWorkflowPermissions):
    can_create = [
        PrimaryCommunityMembers(),
        UserWithRole("editor"),
    ]

    can_read = [
        RecordOwners(),
        CommunityMembers(),
        DefaultCommunityRole("administrator"),
        # editor can see the record in any state
        UserWithRole("editor"),
        # administrator can see everything
        UserWithRole("administrator"),
        IfInState(
            "draft",
            then_=[
                DynamicReviewer(),
            ],
        ),
        IfInState(
            ["published"],
            then_=[
                AnyUser(),
            ],
        ),
        IfInState(
            ["submitted", "accepted"],
            then_=[
                DynamicReviewer(),
            ],
        ),
    ]

    can_search_all_records = CommunityDefaultWorkflowPermissions.can_search
    can_read_all_records = can_read

    can_update = [
        IfInState(
            ["draft"],
            then_=[
                RecordOwners(),
                PrimaryCommunityMembers(),
                DefaultCommunityRole("administrator"),
                UserWithRole("editor"),
                UserWithRole("administrator"),
            ],
        ),
        # if not draft, can not be directly updated, must use request
        IfInState(
            "submitted",
            then_=[
                UserWithRole("editor"),
                UserWithRole("administrator"),
            ],
        ),
    ]

    can_delete = [
        # draft can be deleted, published record must be deleted via request
        IfInState(
            ["draft"],
            then_=[
                RecordOwners(),
                DefaultCommunityRole("administrator"),
                UserWithRole("editor"),
                UserWithRole("administrator"),
            ],
        ),
        IfInState(
            "retracting",
            then_=[
                UserWithRole("administrator"),
            ]
        )
    ]

    can_manage_files = [
        Disable(),
    ]


class CommunityWorkflowRequests(WorkflowRequestPolicy):
    submit_draft = WorkflowRequest(
        # reviewers are notified when a draft is submitted
        requesters=[
            IfInState(
                ["draft"],
                then_=[
                    RecordOwners(),
                    DefaultCommunityRole("administrator"),
                ],
            ),
        ],
        recipients=[DynamicReviewer()],
        transitions=WorkflowTransitions(
            declined="draft", submitted="submitted", accepted="accepted", cancelled="draft"
        ),
    )

    delete_published_record = WorkflowRequest(
        # if the record is draft, it is covered by the delete permission
        # if published, only the owner or editor can request deleting
        requesters=[
            IfInState(
                "published",
                then_=[
                    RecordOwners(),
                    DefaultCommunityRole("administrator"),
                    UserWithRole("editor"),
                    UserWithRole("administrator"),
                ],
            )
        ],
        # if the requester is the editor of the community or administrator, auto approve the request,
        # otherwise, the request is sent to the editor
        recipients=[
            UserWithRole("administrator"),
        ],
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
            IfInState(
                ["draft"],
                then_=[
                    RecordOwners(),
                    DefaultCommunityRole("administrator"),
                ],
            ),
        ],
        recipients=[AutoApprove()],
        transitions=WorkflowTransitions(declined="accepted", accepted="published"),
    )
