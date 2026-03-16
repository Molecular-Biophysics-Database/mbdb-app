from oarepo_workflows.requests import RecipientGeneratorMixin
from oarepo_runtime.services.permissions.generators import UserWithRole
from invenio_records_permissions.generators import ConditionalGenerator

class UserWithRole(UserWithRole, RecipientGeneratorMixin):
    def reference_receivers(self, **kwargs):
        return [{"group": self.roles[0]}]

class DynamicReviewer(UserWithRole, RecipientGeneratorMixin):
    """Resolve reviewer group dynamically from record/request metadata."""

    def __init__(self, default_role="reviewer"):
        self.default_role = default_role
        super().__init__(default_role)

    def _resolve_role(self, **kwargs):
        request = kwargs.get("request")
        record = kwargs.get("record")
        topic = kwargs.get("topic")

        # Try to get the topic/record metadata in the most direct way available
        obj = topic or record

        metadata = {}
        if obj is not None:
            metadata = getattr(obj, "metadata", None) or obj.get("metadata", {}) if isinstance(obj, dict) else {}

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

        return mapping.get(method, self.default_role)

    def reference_receivers(self, **kwargs):
        role = self._resolve_role(**kwargs)
        return [{"group": role}]


class IfHasPreviousVersion(ConditionalGenerator):
    def __init__(self, then_):
        super().__init__(then_, else_=[])

    def _condition(self, record, **kwargs):
        try:
            # null if never published (no previous version exists) otherwise
            # it contains the id
            latest = record.communities.latest_id
        except AttributeError:
            return False
        return bool(latest)


class IfInCommunity(ConditionalGenerator):
    def __init__(self, then_):
        super().__init__(then_, else_=[])

    def _condition(self, record, **kwargs):
        try:
            communities = record.communities
        except AttributeError:
            return False
        return bool(communities)