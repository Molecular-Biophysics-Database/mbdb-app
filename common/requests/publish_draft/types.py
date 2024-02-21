from oarepo_requests.actions.publish_draft import PublishDraftAcceptAction
from oarepo_requests.types.publish_draft import PublishDraftRequestType as BasePublishDraftRequestType
from oarepo_runtime.i18n import lazy_gettext as _


class PublishDraftRequestType(BasePublishDraftRequestType):

    type_id = "publish_draft"
    name = _("Publish-draft")

    available_actions = {
        **BasePublishDraftRequestType.available_actions,
    }

    allowed_topic_ref_types = [
        "bli_draft",
        "mst_draft",
        "spr_draft"
    ]

    @classmethod
    def _update_link_config(cls, **context_values):
        return {}
