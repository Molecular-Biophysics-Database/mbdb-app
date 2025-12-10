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
        if not topic:
            return recipients

        if isinstance(topic, dict) and "$ref" in topic:
            return recipients

        metadata = topic.get("metadata") if isinstance(topic, dict) else None
        if not metadata:
            return recipients

        method = (
            metadata.get("general_parameters", {})
            .get("record_information", {})
            .get("resource_type")
        )

        mapping = {
            "MST": "mst_reviewer",
            "SPR": "spr_reviewer",
            "ITC": "itc_reviewer",
            "BLI": "bli_reviewer",
            "MP": "mp_reviewer",
        }

        role = mapping.get(method, "reviewer")

        return RoleRecipient(role)(notification, recipients)
