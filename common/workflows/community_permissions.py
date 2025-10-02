from invenio_administration.generators import Administration
from invenio_communities.generators import (
    CommunityManagersForRole,
)
from invenio_communities.permissions import CommunityPermissionPolicy
from invenio_records_permissions.generators import Disable, SystemProcess
from oarepo_communities.services.permissions.generators import PrimaryCommunityRole


class CommunitiesPermissionPolicy(CommunityPermissionPolicy):

    can_create = [Administration(), SystemProcess()]
    """Only administrators can create communities, not common users."""

    can_submit_record = [SystemProcess()]
    """Who can submit a record to a community directly. 
       We have a workflow for this, so allow just the system process."""
    #
    # # who can include a record directly, without a review
    can_include_directly = [SystemProcess()]
    """We have a workflow for both including to a secondary community 
       and publishing within primary, so just the system process."""
    #
    can_members_add = [SystemProcess()]
    """In invenio, one can invite a group - we are disabling this behaviour as
    users are handled by AAI and the invitation process targets individual users."""

    can_members_search = [
        PrimaryCommunityRole("administrator"),
        PrimaryCommunityRole("curator"),
        SystemProcess(),
    ]
    # """Who can search for members of a community - only owners and curators."""
    #
    can_members_search_public = [
        PrimaryCommunityRole("administrator"),
        PrimaryCommunityRole("curator"),
        SystemProcess(),
    ]
    can_members_update = [
        CommunityManagersForRole(),
        SystemProcess(),
    ]
    """Who can update a single membership (role, visibility, ...).
    Note: in nr-docs we do not allow users to change their role or visibility,
    just the manager can do that."""

    #
    # # Ability to delete a single membership
    can_members_delete = can_members_update
    """Who can delete a single membership. As with the update, only the manager can do that."""

    can_request_membership = [Disable()]
    """Currently user can not ask for direct inclusion (just invitations), 
    so disable the direct request."""
