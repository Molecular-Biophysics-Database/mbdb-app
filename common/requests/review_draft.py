from oarepo_runtime.i18n import lazy_gettext as _
from oarepo_requests.types import ModelRefTypes
from oarepo_requests.types.generic import NonDuplicableOARepoRequestType


# Request
#
class ReviewDraftRequestType(NonDuplicableOARepoRequestType):
    type_id = "review_draft"
    name = _("Review Draft")

    @classmethod
    @property
    def available_actions(cls):
        return {
            **super().available_actions,
        }

    receiver_can_be_none = False
    creator_can_be_none = False
    topic_can_be_none = False
    # TODO: Should published really be True?
    allowed_topic_ref_types = ModelRefTypes(published=True, draft=True)
