from invenio_records_permissions.generators import AuthenticatedUser, SystemProcess
from oarepo_runtime.services.config.permissions_presets import ReadOnlyPermissionPolicy
from common.workflows.custom_generators import UserWithRole

class FineGrainedVocabularyPermissionPolicy(ReadOnlyPermissionPolicy):
    """Permission policy for vocabularies"""
    # Roles that are potentially able to create vocabularies
    can_create = [AuthenticatedUser(), SystemProcess()]
    # Roles which can create specific vocabularies
    can_create_affiliations = [AuthenticatedUser(), SystemProcess()]
    can_create_body_fluids = [AuthenticatedUser(), SystemProcess()]
    can_create_cell_fractions = [AuthenticatedUser(), SystemProcess()]
    can_create_chemicals = [AuthenticatedUser(), SystemProcess()]
    can_create_environment_types = [AuthenticatedUser(), SystemProcess()]
    can_create_grants = [AuthenticatedUser(), SystemProcess()]
    can_create_instruments = [SystemProcess(), UserWithRole("editor")]
    can_create_languages = [SystemProcess()]
    can_create_organisms = [SystemProcess()]
    can_create_products = [AuthenticatedUser(), SystemProcess()]