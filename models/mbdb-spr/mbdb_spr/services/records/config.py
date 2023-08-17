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

from mbdb_spr.records.api import MbdbSprRecord
from mbdb_spr.services.records.permissions import MbdbSprPermissionPolicy
from mbdb_spr.services.records.schema import MbdbSprSchema
from mbdb_spr.services.records.search import MbdbSprSearchOptions


class MbdbSprServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordServiceConfig):
    """MbdbSprRecord service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/mbdb-spr/"

    base_permission_policy_cls = MbdbSprPermissionPolicy

    schema = MbdbSprSchema

    search = MbdbSprSearchOptions

    record_cls = MbdbSprRecord

    service_id = "mbdb_spr"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordServiceConfig.components,
        FilesOptionsComponent,
        DataComponent,
    ]

    model = "mbdb_spr"

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
