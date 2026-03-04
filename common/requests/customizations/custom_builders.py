from invenio_users_resources.notifications.filters import UserPreferencesRecipientFilter
from invenio_requests.notifications.builders import CommentRequestEventCreateNotificationBuilder
from oarepo_requests.notifications.generators import EntityRecipient
from oarepo_requests.notifications.builders.oarepo import OARepoRequestActionNotificationBuilder
from common.requests.customizations.custom_generators import DynamicReviewerRecipient
from invenio_notifications.services.filters import RecipientFilter
from invenio_notifications.services.generators import RecipientGenerator


class ExcludeEventCreatorFilter(RecipientFilter):
    """Filter that removes the person who triggered the event from recipients."""

    def __call__(self, notification, recipients):
        event = notification.context.get("request_event", {})
        creator_id = None
        print(event)
        if isinstance(event, dict):
            created_by = event.get("created_by", {})
            creator_id = created_by.get("id") or created_by.get("user")
            print(creator_id)

        else:
            created_by = getattr(event, "created_by", {})
            if isinstance(created_by, dict):
                creator_id = created_by.get("id") or created_by.get("user")
            else:
                creator_id = getattr(created_by, "id", None) or getattr(created_by, "user", None)

        if creator_id:
            recipients.pop(str(creator_id), None)
            print(recipients)

        return recipients




class ForceBackendRecipient(RecipientGenerator):
    """Ensures backend_ids is ALWAYS in the context when this runs."""

    def __call__(self, notification, recipients):
        if "backend_ids" not in notification.context:
            notification.context["backend_ids"] = ["email"]
        return recipients


from invenio_notifications.registry import EntityResolverRegistry


class CustomCommentRequestEventCreateNotificationBuilder(CommentRequestEventCreateNotificationBuilder):
    recipients = [
        EntityRecipient(key="request.created_by"),
        DynamicReviewerRecipient(),
    ]

    recipient_filters = [
        UserPreferencesRecipientFilter(),
        ExcludeEventCreatorFilter(),
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
