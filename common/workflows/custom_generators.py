from oarepo_workflows.requests import RecipientGeneratorMixin
from oarepo_runtime.services.permissions.generators import UserWithRole
from invenio_records_permissions.generators import ConditionalGenerator

class UserWithRole(UserWithRole, RecipientGeneratorMixin):
    def reference_receivers(self, **kwargs):
        return [{"group": self.roles[0]}]


class IfHasPreviousVersion(ConditionalGenerator):
    def __init__(self, then_):
        super().__init__(then_, else_=[])

    def _condition(self, record, **kwargs):
        try:
            # null if never published (no previous version exists) otherwise it contains the id
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