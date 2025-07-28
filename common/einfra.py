from invenio_accounts.models import User
from invenio_communities.communities.records.models import CommunityMetadata
from invenio_db import db
from oarepo_oidc_einfra.communities import CommunityRole


def transform_community_roles(
    user: User, current_roles: set[CommunityRole], new_roles: set[CommunityRole]
):
    """
    Always add the generic community role to user's communities.
    """
    community_metadata = (
        db.session.query(CommunityMetadata).filter_by(slug="generic").first()
    )
    print("Community metadata: ", community_metadata)
    if not any(
        str(role.community_id) == str(community_metadata.id) for role in new_roles
    ):
        new_roles.add(
            CommunityRole(
                community_id=community_metadata.id,
                role="member",
            )
        )
