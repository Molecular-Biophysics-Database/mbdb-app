from invenio_records_permissions.generators import AuthenticatedUser

from oarepo_workflows.services.permissions.policy import WorkflowPermissionPolicy

class MbdbPermissionPreset(WorkflowPermissionPolicy):
    can_view_deposit_page = [
        # TODO: should be removed after this permission is implemented directly on oarepo-communities
        AuthenticatedUser(),
    ]