from oarepo_requests.actions.generic import OARepoAcceptAction
from oarepo_requests.types import ModelRefTypes
from oarepo_requests.types.generic import OARepoRequestType
from oarepo_runtime.datastreams.utils import get_record_service_for_record
from oarepo_runtime.i18n import lazy_gettext as _

from oarepo_communities.proxies import current_oarepo_communities


class UserAlreadyIncludedException(Exception):
    """The user is already in the community."""

    description = "The user is already included in this community."


class InviteToCommunityAcceptAction(OARepoAcceptAction):
    """Accept action."""

    def apply(self, identity, request_type, topic, uow, *args, **kwargs):
        community_id = self.request.receiver.resolve().community_id
        service = get_record_service_for_record(topic)
        community_inclusion_service = (
            current_oarepo_communities.community_inclusion_service
        )
        community_inclusion_service.remove(
            topic, community_id, record_service=service, uow=uow
        )


# Request
#
class InviteToCommunityRequestType(OARepoRequestType):
    """Review request for submitting a record to a community."""

    type_id = "invite_to_community"
    name = _("Invite to community")

    creator_can_be_none = False
    topic_can_be_none = False
    allowed_topic_ref_types = ModelRefTypes(published=True, draft=True)

    @classmethod
    @property
    def available_actions(cls):
        return {
            **super().available_actions,
            "accept": InviteToCommunityAcceptAction,
        }

    def can_create(self, identity, data, receiver, topic, creator, *args, **kwargs):
        super().can_create(identity, data, receiver, topic, creator, *args, **kwargs)
        target_community_id = data["payload"]["community"]
        already_included = target_community_id in topic.parent.communities.ids
        if already_included:
            raise UserAlreadyIncludedException(
                "Cannot apply, user is already in target community."
            )

    @classmethod
    def can_possibly_create(self, identity, topic, *args, **kwargs):
        super().can_possibly_create(identity, topic, *args, **kwargs)
        try:
            communities = topic.parent.communities.ids
        except AttributeError:
            return False
        return len(communities) > 1
