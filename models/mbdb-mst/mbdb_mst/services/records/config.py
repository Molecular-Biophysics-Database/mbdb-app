from invenio_drafts_resources.services import (
    RecordServiceConfig as InvenioRecordDraftsServiceConfig,
)
from invenio_drafts_resources.services.records.components import DraftFilesComponent
from invenio_drafts_resources.services.records.config import is_record
from invenio_records_resources.services import ConditionalLink, RecordLink
from invenio_records_resources.services.records.components import (
    DataComponent,
    FilesOptionsComponent,
)
from oarepo_runtime.config.service import PermissionsPresetsConfigMixin

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
        DraftFilesComponent,
        FilesOptionsComponent,
        DataComponent,
    ]

    model = "mbdb_mst"
    draft_cls = MbdbMstDraft

    @property
    def links_item(self):
        return {
            "draft": RecordLink("{+api}/mbdb-mst/{id}/draft"),
            "files": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+api}/mbdb-mst/{id}/files"),
                else_=RecordLink("{+api}/mbdb-mst/{id}/draft/files"),
            ),
            "latest": RecordLink("{+api}/mbdb-mst/{id}/versions/latest"),
            "latest_html": RecordLink("{+ui}/mbdb-mst/{id}/latest"),
            "publish": RecordLink("{+api}/mbdb-mst/{id}/draft/actions/publish"),
            "record": RecordLink("{+api}/mbdb-mst/{id}"),
            "self": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+api}/mbdb-mst/{id}"),
                else_=RecordLink("{+api}/mbdb-mst/{id}/draft"),
            ),
            "self_html": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+ui}/mbdb-mst/{id}"),
                else_=RecordLink("{+ui}/uploads/{id}"),
            ),
            "versions": RecordLink("{+api}/mbdb-mst/{id}/versions"),
        }
