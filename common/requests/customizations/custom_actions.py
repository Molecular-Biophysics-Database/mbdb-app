from oarepo_requests.actions.generic import OARepoSubmitAction, OARepoAcceptAction, OARepoDeclineAction
from invenio_notifications.services.uow import NotificationOp
from .custom_builders import *


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
    status_to = "created"
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
