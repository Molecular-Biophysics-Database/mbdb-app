from invenio_records_resources.services import RecordLink
from invenio_records_resources.services import (
    RecordServiceConfig as InvenioRecordServiceConfig,
)
from invenio_records_resources.services import pagination_links
from invenio_records_resources.services.records.components import (
    DataComponent,
    FilesOptionsComponent,
)
from oarepo_runtime.config.service import PermissionsPresetsConfigMixin

from mbdb_bli.records.api import MbdbBliRecord
from mbdb_bli.services.records.permissions import MbdbBliPermissionPolicy
from mbdb_bli.services.records.schema import MbdbBliSchema
from mbdb_bli.services.records.search import MbdbBliSearchOptions


class MbdbBliServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordServiceConfig):
    """MbdbBliRecord service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/mbdb-bli/"

    base_permission_policy_cls = MbdbBliPermissionPolicy

    schema = MbdbBliSchema

    search = MbdbBliSearchOptions

    record_cls = MbdbBliRecord

    service_id = "mbdb_bli"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordServiceConfig.components,
        FilesOptionsComponent,
        DataComponent,
    ]

    model = "mbdb_bli"

    @property
    def links_item(self):
        return {
            "files": RecordLink("{self.url_prefix}{id}/files"),
            "self": RecordLink("{self.url_prefix}{id}"),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{self.url_prefix}{?args*}"),
        }
