from typing import override

from invenio_i18n import lazy_gettext as _
from invenio_notifications.services.uow import NotificationOp
from oarepo_requests.actions.generic import OARepoAcceptAction, OARepoSubmitAction
from oarepo_requests.actions.publish_draft import MakeTopicDraftMixin, PublishMixin
from oarepo_requests.notifications.builders.publish import (
    PublishDraftRequestAcceptNotificationBuilder,
)
from oarepo_requests.types import PublishChangedMetadataRequestType
from oarepo_requests.utils import get_draft_record_service
from oarepo_runtime.typing import record_from_result

from .titles import request_title


class PublishApprovedSubmitAction(MakeTopicDraftMixin, PublishMixin, OARepoSubmitAction):
    """No notification, the request is accepted right away."""

    @override
    def apply(self, identity, uow, *args, **kwargs):
        self.request["title"] = request_title(self.topic)


class PublishApprovedAcceptAction(MakeTopicDraftMixin, PublishMixin, OARepoAcceptAction):
    name = _("Publish")

    @override
    def apply(self, identity, uow, *args, **kwargs):
        service = get_draft_record_service(self.topic)
        self.topic = record_from_result(
            service.publish(identity, self.topic["id"], uow=uow, expand=False)
        )
        uow.register(
            NotificationOp(
                PublishDraftRequestAcceptNotificationBuilder.build(request=self.request)
            )
        )


class PublishApprovedDraftRequestType(PublishChangedMetadataRequestType):
    """The owner publishes a draft accepted by a reviewer, be it a new record,
    a new version or changed metadata (whose topic oarepo has to convert to the draft)."""

    type_id = "publish_approved_draft"
    name = _("Publish")
    description = _("Publish the accepted draft")
    topic_type = "draft"
    submit_action = PublishApprovedSubmitAction
    accept_action = PublishApprovedAcceptAction

    @classmethod
    @override
    def get_topic_type(cls, topic):
        return "draft" if topic.is_draft else "published"

    @classmethod
    @override
    def open_request_exists(cls, *args, **kwargs):
        # a request whose submit failed stays open and must not block another attempt
        return False

    @override
    def stateful_name(self, identity, **kwargs):
        return self.name

    @override
    def stateful_description(self, identity, **kwargs):
        return self.description
