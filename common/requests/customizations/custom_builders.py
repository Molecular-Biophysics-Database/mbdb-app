from invenio_users_resources.notifications.filters import UserPreferencesRecipientFilter
from invenio_requests.notifications.builders import CommentRequestEventCreateNotificationBuilder
from oarepo_requests.notifications.generators import EntityRecipient
from oarepo_requests.notifications.builders.oarepo import OARepoRequestActionNotificationBuilder
from common.requests.customizations.custom_generators import DynamicReviewerRecipient
from invenio_notifications.services.filters import RecipientFilter
from invenio_notifications.services.generators import RecipientGenerator
from invenio_notifications.registry import EntityResolverRegistry


class ForceBackendRecipient(RecipientGenerator):
    """Ensures backend_ids is ALWAYS in the context when this runs."""

    def __call__(self, notification, recipients):
        if "backend_ids" not in notification.context:
            notification.context["backend_ids"] = ["email"]
        return recipients

class CustomCommentRequestEventCreateNotificationBuilder(CommentRequestEventCreateNotificationBuilder):
    type = "comment-request-event.create"

    recipients = [
        ForceBackendRecipient(),
        EntityRecipient(key="request.created_by"),
        DynamicReviewerRecipient(),
    ]

    recipient_filters = [
        UserPreferencesRecipientFilter(),
    ]

    @classmethod
    def build(cls, request, request_event):
        """Build notification matching the base class pattern + backend_ids."""
        return cls.notification_cls(
            type=cls.type,
            context={
                "request": EntityResolverRegistry.reference_entity(request),
                "request_event": EntityResolverRegistry.reference_entity(request_event),
                "backend_ids": ["email"],
            },
        )

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
