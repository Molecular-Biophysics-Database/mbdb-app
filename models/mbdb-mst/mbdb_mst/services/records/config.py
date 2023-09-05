from invenio_drafts_resources.services import (
    RecordServiceConfig as InvenioRecordDraftsServiceConfig,
)
from invenio_drafts_resources.services.records.config import is_record
from invenio_records_resources.services import ConditionalLink, RecordLink
from invenio_records_resources.services.records.components import (
    DataComponent,
    FilesOptionsComponent,
)

from mbdb_mst.records.api import MbdbMstDraft, MbdbMstRecord
from mbdb_mst.services.records.permissions import MbdbMstPermissionPolicy
from mbdb_mst.services.records.schema import MbdbMstSchema
from mbdb_mst.services.records.search import MbdbMstSearchOptions


class MbdbMstServiceConfig(
    PermissionsPresetsConfigMixin, InvenioRecordDraftsServiceConfig
):
    """MbdbMstRecord service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/mbdb-mst/"

    base_permission_policy_cls = MbdbMstPermissionPolicy

    schema = MbdbMstSchema

    search = MbdbMstSearchOptions

    record_cls = MbdbMstRecord

    service_id = "mbdb_mst"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordDraftsServiceConfig.components,
        FilesOptionsComponent,
        DataComponent,
    ]

    model = "mbdb_mst"
    draft_cls = MbdbMstDraft

    @property
    def links_item(self):
        return {
            "draft": RecordLink("{+api}/{self.url_prefix}{id}/draft"),
            "files": RecordLink("{self.url_prefix}{id}/files"),
            "latest": RecordLink("{+api}/{self.url_prefix}{id}/versions/latest"),
            "latest_html": RecordLink("{+ui}/{self.url_prefix}{id}/latest"),
            "publish": RecordLink("{+api}/{self.url_prefix}{id}/draft/actions/publish"),
            "record": RecordLink("{+api}/{self.url_prefix}{id}"),
            "self": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+api}{self.url_prefix}{id}"),
                else_=RecordLink("{+api}{self.url_prefix}{id}/draft"),
            ),
            "self_html": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+ui}{self.url_prefix}{id}"),
                else_=RecordLink("{+ui}/uploads/{id}"),
            ),
            "versions": RecordLink("{+api}/{self.url_prefix}{id}/versions"),
        }
