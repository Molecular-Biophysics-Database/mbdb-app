from oarepo_workflows.requests import RecipientGeneratorMixin
from oarepo_runtime.services.permissions.generators import UserWithRole
from invenio_records_permissions.generators import ConditionalGenerator
from flask_principal import RoleNeed
from invenio_records_permissions.generators import Generator
from oarepo_runtime.services.permissions.generators import RecordOwners

class UserWithRole(UserWithRole, RecipientGeneratorMixin):
    def reference_receivers(self, **kwargs):
        return [{"group": self.roles[0]}]

class DynamicReviewer(UserWithRole, RecipientGeneratorMixin):
    """Resolve reviewer group dynamically from record/request metadata."""

    def __init__(self):
        # We no longer pass a default role to the parent
        super().__init__()

    def _resolve_role(self, **kwargs):
        # topic is usually the record associated with a request
        obj = kwargs.get("topic") or kwargs.get("record")

        if obj is None:
            return None

        # Handle both record objects and dicts
        metadata = getattr(obj, "metadata", obj.get("metadata", {})) if obj else {}

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

        resolved = mapping.get(method)
        return resolved

    def needs(self, **kwargs):
        """Used for checking permissions (can_read, can_update)."""
        role = self._resolve_role(**kwargs)
        # If no role is resolved, return empty list (access denied)
        return [RoleNeed(role)] if role else []

    def reference_receivers(self, **kwargs):
        """Used for workflow notifications."""
        role = self._resolve_role(**kwargs)
        return [{"group": role}] if role else []

class RecordOwnerWithRequiredSubmissionContent(Generator):
    def needs(self, record=None, **kwargs):
        if not record:
            return []

        metadata = record.get("metadata") or {}
        general = metadata.get("general_parameters") or {}
        msp = metadata.get("method_specific_parameters") or {}
        record_info = general.get("record_information") or {}
        has_title = bool(record_info.get("title"))

        if not has_title:
            return []

        return RecordOwners().needs(record=record, **kwargs)

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