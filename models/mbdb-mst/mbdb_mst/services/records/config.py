from invenio_records_resources.services import RecordLink
from invenio_records_resources.services import (
    RecordServiceConfig as InvenioRecordServiceConfig,
)
from invenio_records_resources.services import pagination_links
from invenio_records_resources.services.records.components import (
    DataComponent,
)
from oarepo_runtime.config.service import PermissionsPresetsConfigMixin

from mbdb_mst.records.api import MbdbMstRecord
from mbdb_mst.services.records.permissions import MbdbMstPermissionPolicy
from mbdb_mst.services.records.schema import MbdbMstSchema

# TODO: waiting for search
# from mbdb_mst.services.records.search import MbdbMstSearchOptions


class MbdbMstServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordServiceConfig):
    """MbdbMstRecord service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/mbdb-mst/"

    base_permission_policy_cls = MbdbMstPermissionPolicy

    schema = MbdbMstSchema

    # TODO: waiting for search
    # search = MbdbMstSearchOptions

    record_cls = MbdbMstRecord

    service_id = "mbdb_mst"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordServiceConfig.components,
        DataComponent,
    ]

    model = "mbdb_mst"

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
