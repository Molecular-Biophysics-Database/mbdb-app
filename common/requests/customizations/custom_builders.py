from invenio_notifications.services.filters import KeyRecipientFilter
from invenio_users_resources.notifications.filters import (
    UserPreferencesRecipientFilter,
)
from invenio_requests.notifications.builders import CommentRequestEventCreateNotificationBuilder
from oarepo_requests.notifications.generators import EntityRecipient
from oarepo_requests.notifications.builders.oarepo import OARepoRequestActionNotificationBuilder
from invenio_requests.notifications.filters import UserRecipientFilter
from invenio_requests.notifications.generators import RequestParticipantsRecipient
from common.requests.customizations.custom_generators import DynamicReviewerRecipient


class CustomCommentRequestEventCreateNotificationBuilder(CommentRequestEventCreateNotificationBuilder):
    # TODO Define notification logic based on the comment creator's role. Implement conditional
    #  notification builders or recipient filters to ensure the Request Creator is notified
    #  only when the Reviewer comments, and vice-versa.
    recipients = [
        RequestParticipantsRecipient(key="request"),
        DynamicReviewerRecipient(),
    ]

    recipient_filters = [
        KeyRecipientFilter(key="request_event.created_by"),
        UserRecipientFilter(key="request_event.created_by"),
        UserPreferencesRecipientFilter(),
    ]

    @classmethod
    def build(cls, request, request_event):
        notif = super().build(request, request_event)
        notif.context["backend_ids"] = ["email"]

        return notif


class DraftRequestSubmitReceiverNotificationBuilder(OARepoRequestActionNotificationBuilder):
    type = "draft-request-receiver.submit"
    recipients = [DynamicReviewerRecipient()]


class DraftRequestSubmitCreatorNotificationBuilder(OARepoRequestActionNotificationBuilder):
    type = "draft-request-creator.submit"
    # User that created/sent the request (author of the record)
    recipients = [EntityRecipient(key="request.created_by")]


class DraftRequestAcceptCreatorNotificationBuilder(OARepoRequestActionNotificationBuilder):
    type = "draft-request-accept-creator.submit"
    # Authors as recipients
    recipients = [EntityRecipient(key="request.created_by")]


class DraftRequestDeclineCreatorNotificationBuilder(OARepoRequestActionNotificationBuilder):
    type = "draft-request-decline-creator.submit"
    recipients = [EntityRecipient(key="request.created_by")]
