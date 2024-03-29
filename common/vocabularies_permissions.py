from invenio_records_permissions.generators import AuthenticatedUser, SystemProcess
from oarepo_runtime.services.config.permissions_presets import ReadOnlyPermissionPolicy, EveryonePermissionPolicy


class FineGrainedVocabularyPermissionPolicy(ReadOnlyPermissionPolicy):
    can_create_chemicals = [AuthenticatedUser(), SystemProcess()]
    can_create_affiliations = [SystemProcess()]
    can_create_grants = [SystemProcess()]
    can_create_organisms = [SystemProcess()]
    can_create_instruments = [SystemProcess()]
    can_create = [AuthenticatedUser(), SystemProcess()]
