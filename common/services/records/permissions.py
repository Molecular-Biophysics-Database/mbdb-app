from invenio_records_permissions.generators import AuthenticatedUser

from oarepo_workflows.services.permissions.record_permission_policy import WorkflowRecordPermissionPolicy

class MbdbPermissionPreset(WorkflowRecordPermissionPolicy):
    can_view_deposit_page = [
        # TODO: should be removed after this permission is implemented directly on oarepo-communities
        AuthenticatedUser(),
    ]