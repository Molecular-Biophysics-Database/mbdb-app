"""oarepo's publish requests, except that accepting does not publish the draft.

They keep oarepo's type ids: the deposit form's submit button knows only those.
"""

from typing import override

from invenio_i18n import gettext
from invenio_i18n import lazy_gettext as _
from invenio_notifications.services.uow import NotificationOp
from oarepo_requests.actions.generic import OARepoAcceptAction
from oarepo_requests.actions.publish_changed_metadata import (
    PublishChangedMetadataSubmitAction,
)
from oarepo_requests.actions.publish_draft import (
    MakeTopicDraftMixin,
    PublishDraftDeclineAction,
    PublishDraftSubmitAction,
    PublishMixin,
)
from oarepo_requests.actions.publish_new_version import PublishNewVersionSubmitAction
from oarepo_requests.notifications.builders.publish import (
    PublishDraftRequestAcceptNotificationBuilder,
    PublishDraftRequestDeclineNotificationBuilder,
    PublishDraftRequestSubmitNotificationBuilder,
)
from oarepo_requests.notifications.generators import EntityRecipientGenerator
from oarepo_requests.types import (
    PublishChangedMetadataRequestType,
    PublishDraftRequestType,
    PublishNewVersionRequestType,
)

from .titles import request_title


class ReviewSubmitNotificationBuilder(PublishDraftRequestSubmitNotificationBuilder):
    """For the reviewers."""

    type = "mbdb-review-request-event.submit"


class ReviewSubmitCreatorNotificationBuilder(
    PublishDraftRequestSubmitNotificationBuilder
):
    """The confirmation for the one who submitted the draft."""

    type = "mbdb-review-request-event.submit-creator"
    recipients = (EntityRecipientGenerator(key="request.created_by"),)


class ReviewDeclineNotificationBuilder(PublishDraftRequestDeclineNotificationBuilder):
    type = "mbdb-review-request-event.decline"


class ReviewAcceptNotificationBuilder(PublishDraftRequestAcceptNotificationBuilder):
    type = "mbdb-review-request-event.accept"


class ReviewAcceptAction(MakeTopicDraftMixin, PublishMixin, OARepoAcceptAction):
    name = _("Accept")

    @override
    def apply(self, identity, uow, *args, **kwargs):
        uow.register(
            NotificationOp(ReviewAcceptNotificationBuilder.build(request=self.request))
        )


class ReviewDeclineAction(PublishDraftDeclineAction):
    notification_builder = ReviewDeclineNotificationBuilder


class ReviewSubmitMixin:
    """Names the request after its draft and preselects everyone with the receiving role."""

    notification_builder = ReviewSubmitNotificationBuilder

    @override
    def apply(self, identity, uow, *args, **kwargs):
        self.request["title"] = request_title(self.topic)
        receiver = self.request.receiver
        if receiver is not None and "group" in receiver.reference_dict:
            # shortcut: not limited to REQUESTS_REVIEWERS_MAX_NUMBER (15), raise it if a role
            # gets more members, otherwise the list cannot be edited in the UI
            self.request.reviewers = [
                user for user in receiver.resolve().users if user.active
            ]
        super().apply(identity, uow, *args, **kwargs)
        uow.register(
            NotificationOp(
                ReviewSubmitCreatorNotificationBuilder.build(request=self.request)
            )
        )


class ReviewDraftSubmitAction(ReviewSubmitMixin, PublishDraftSubmitAction):
    pass


class ReviewNewVersionSubmitAction(ReviewSubmitMixin, PublishNewVersionSubmitAction):
    pass


class ReviewChangedMetadataSubmitAction(
    ReviewSubmitMixin, PublishChangedMetadataSubmitAction
):
    pass


class ReviewMixin:
    accept_action = ReviewAcceptAction
    decline_action = ReviewDeclineAction

    @override
    def string_by_state(self, identity, **kwargs):
        # oarepo's text says that the draft has been published
        kwargs["accepted"] = gettext("Accepted, the owner can publish the draft")
        return super().string_by_state(identity, **kwargs)


class ReviewDraftRequestType(ReviewMixin, PublishDraftRequestType):
    submit_action = ReviewDraftSubmitAction


class ReviewNewVersionRequestType(ReviewMixin, PublishNewVersionRequestType):
    submit_action = ReviewNewVersionSubmitAction


class ReviewChangedMetadataRequestType(ReviewMixin, PublishChangedMetadataRequestType):
    submit_action = ReviewChangedMetadataSubmitAction
