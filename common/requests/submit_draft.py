from marshmallow import ValidationError
from oarepo_runtime.i18n import lazy_gettext as _
from oarepo_requests.types import ModelRefTypes
from oarepo_requests.types.generic import NonDuplicableOARepoRequestType
from oarepo_runtime.datastreams.utils import get_record_service_for_record
from oarepo_requests.actions.generic import OARepoSubmitAction, OARepoAcceptAction, OARepoDeclineAction
from invenio_notifications.services.uow import NotificationOp
from oarepo_requests.notifications.generators import EntityRecipient
from oarepo_requests.notifications.builders.oarepo import OARepoRequestActionNotificationBuilder
from common.requests.custom_generators import DynamicReviewerRecipient


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

class SubmitDraftAction(OARepoSubmitAction):
    """Submit draft action."""

    def apply(
            self,
            identity,
            state,
            uow,
            *args,
            **kwargs,
    ) -> None:
        # Send notification to Receivers
        uow.register(
            NotificationOp(
                DraftRequestSubmitReceiverNotificationBuilder.build(request=self.request)
            )
        )

        # Send notification to Creators
        uow.register(
            NotificationOp(
                DraftRequestSubmitCreatorNotificationBuilder.build(request=self.request)
            )
        )
        return super().apply(identity, state, uow, *args, **kwargs)

class AcceptDraftAction(OARepoAcceptAction):
    """Accept draft action."""

    def apply(
            self,
            identity,
            state,
            uow,
            *args,
            **kwargs,
    ) -> None:
        # Send notification to Creators
        uow.register(
            NotificationOp(
                DraftRequestAcceptCreatorNotificationBuilder.build(request=self.request)
            )
        )
        return super().apply(identity, state, uow, *args, **kwargs)

class DeclineDraftAction(OARepoDeclineAction):
    """Decline draft action."""

    def apply(
            self,
            identity,
            state,
            uow,
            *args,
            **kwargs,
    ) -> None:
        request_event = super().apply(identity, state, uow, *args, **kwargs)
        # Send notification to Creators
        uow.register(
            NotificationOp(
                DraftRequestDeclineCreatorNotificationBuilder.build(request=self.request)
            )
        )
        return super().apply(identity, state, uow, *args, **kwargs)

# Request
class SubmitDraftRequestType(NonDuplicableOARepoRequestType):
    """
    Custom submit draft request that validates the draft upon submission. The
    request is not created if validation fails.
    """

    type_id = "submit_draft"
    name = _("Submit")

    # Modal popup
    dangerous = True

    @classmethod
    @property
    def available_actions(cls):
        return {
            **super().available_actions,
            "submit": SubmitDraftAction,
            "accept": AcceptDraftAction,
            "decline": DeclineDraftAction,
        }

    receiver_can_be_none = False
    creator_can_be_none = False
    topic_can_be_none = False
    allowed_topic_ref_types = ModelRefTypes(published=True, draft=True)

    def can_create(self, identity, data, receiver, topic, creator, *args, **kwargs):
        if not topic.is_draft:
            raise ValueError("Trying to create publish request on published record")
        super().can_create(identity, data, receiver, topic, creator, *args, **kwargs)
        draft = topic

        # Enforce required file
        has_files = (
                getattr(draft, "files", None)
                and getattr(draft.files, "entries", None)
                and len(draft.files.entries) > 0
        )
        if not has_files:
            raise ValidationError({"files.enabled": ["Missing uploaded files."]})

        topic_service = get_record_service_for_record(topic)
        errors = topic_service.validate_draft(identity, topic["id"])

        if errors:
            raise ValidationError(errors)