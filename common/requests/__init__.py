"""Two-step publication: a reviewer accepts the draft, then its owner publishes it."""

from .publish_approved import PublishApprovedDraftRequestType
from .review import (
    ReviewAcceptNotificationBuilder,
    ReviewChangedMetadataRequestType,
    ReviewDeclineNotificationBuilder,
    ReviewDraftRequestType,
    ReviewNewVersionRequestType,
    ReviewSubmitCreatorNotificationBuilder,
    ReviewSubmitNotificationBuilder,
)

REQUEST_TYPES = [
    ReviewDraftRequestType(),
    ReviewNewVersionRequestType(),
    ReviewChangedMetadataRequestType(),
    PublishApprovedDraftRequestType(),
]

NOTIFICATION_BUILDERS = {
    builder.type: builder
    for builder in (
        ReviewSubmitNotificationBuilder,
        ReviewSubmitCreatorNotificationBuilder,
        ReviewAcceptNotificationBuilder,
        ReviewDeclineNotificationBuilder,
    )
}
