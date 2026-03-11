from invenio_notifications.services.generators import RecipientGenerator
from invenio_notifications.models import Recipient
from invenio_accounts.models import Role


def _extract_entity_email_data(entity):
    return {
        "email": entity.email,
        "id": entity.id,
        "preferences": dict(getattr(entity, "preferences", {}) or {}),  # force plain dict
    }


class RoleRecipient(RecipientGenerator):
    """Recipients based on a SQLAlchemy Role lookup — bypasses OpenSearch."""

    def __init__(self, role_name: str):
        self.role_name = role_name

    def __call__(self, notification=None, recipients=None, **kwargs):
        if recipients is None:
            recipients = {}

        # --- 1) Load role
        role = Role.query.filter_by(name=self.role_name).first()
        if not role:
            return recipients

        # --- 2) Iterate users
        added = 0
        for user in role.users:

            if not user.email:
                continue

            recipients[str(user.id)] = Recipient(data=_extract_entity_email_data(user))
            added += 1

        return recipients


class DynamicReviewerRecipient(RecipientGenerator):
    def __call__(self, notification, recipients):
        ctx = notification.context
        request = ctx.get("request")
        if not request:
            return recipients

        topic = request.get("topic")
        method = None

        if topic and isinstance(topic, dict):
            metadata = topic.get("metadata", {})
            method = (
                metadata.get("general_parameters", {})
                .get("record_information", {})
                .get("resource_type")
            )

        mapping = {
            "MST": "reviewer_mst",
            "SPR": "reviewer_spr",
            "ITC": "reviewer_itc",
            "BLI": "reviewer_bli",
            "MP": "reviewer_mp",
        }

        role_to_fetch = mapping.get(method)

        if not role_to_fetch:
            receiver = request.get("receiver", {})
            role_to_fetch = receiver.get("group", "reviewer")

        return RoleRecipient(role_to_fetch)(notification, recipients)