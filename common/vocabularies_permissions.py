from invenio_records_permissions.generators import AuthenticatedUser, SystemProcess
from oarepo_runtime.services.config.permissions_presets import ReadOnlyPermissionPolicy


class FineGrainedVocabularyPermissionPolicy(ReadOnlyPermissionPolicy):
    can_create_affiliations = [SystemProcess()]
    can_create_cell_fractions = [AuthenticatedUser(), SystemProcess()]
    can_create_body_fluids = [AuthenticatedUser(), SystemProcess()]
    can_create_chemicals = [AuthenticatedUser(), SystemProcess()]
    can_create_environment_types = [AuthenticatedUser(), SystemProcess()]
    can_create_instruments = [SystemProcess()]
    can_create_languages = [SystemProcess()]
    can_create_grants = [AuthenticatedUser(), SystemProcess()]
    can_create_organisms = [SystemProcess()]
    can_create_products = [AuthenticatedUser(), SystemProcess()]
    can_create = [AuthenticatedUser(), SystemProcess()]
