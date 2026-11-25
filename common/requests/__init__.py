"""Two-step publication: a reviewer accepts the draft, then its owner publishes it."""

from .publish_approved import PublishApprovedDraftRequestType
from .review import (
    ReviewAcceptNotificationBuilder,
    ReviewChangedMetadataRequestType,
    ReviewDraftRequestType,
    ReviewNewVersionRequestType,
)

REQUEST_TYPES = [
    ReviewDraftRequestType(),
    ReviewNewVersionRequestType(),
    ReviewChangedMetadataRequestType(),
    PublishApprovedDraftRequestType(),
]

NOTIFICATION_BUILDERS = {
    ReviewAcceptNotificationBuilder.type: ReviewAcceptNotificationBuilder,
}
