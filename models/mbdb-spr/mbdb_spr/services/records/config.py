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

from mbdb_spr.records.api import MbdbSprDraft, MbdbSprRecord
from mbdb_spr.services.records.permissions import MbdbSprPermissionPolicy
from mbdb_spr.services.records.schema import MbdbSprSchema
from mbdb_spr.services.records.search import MbdbSprSearchOptions


class MbdbSprServiceConfig(
    PermissionsPresetsConfigMixin, InvenioRecordDraftsServiceConfig
):
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
        *InvenioRecordDraftsServiceConfig.components,
        DataComponent,
        FilesOptionsComponent,
        DraftFilesComponent,
    ]

    model = "mbdb_spr"
    draft_cls = MbdbSprDraft
    search_drafts = MbdbSprSearchOptions

    @property
    def links_item(self):
        return {
            "draft": RecordLink("{+api}/mbdb-spr/{id}/draft"),
            "files": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+api}/mbdb-spr/{id}/files"),
                else_=RecordLink("{+api}/mbdb-spr/{id}/draft/files"),
            ),
            "latest": RecordLink("{+api}/mbdb-spr/{id}/versions/latest"),
            "latest_html": RecordLink("{+ui}/mbdb-spr/{id}/latest"),
            "publish": RecordLink("{+api}/mbdb-spr/{id}/draft/actions/publish"),
            "record": RecordLink("{+api}/mbdb-spr/{id}"),
            "self": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+api}/mbdb-spr/{id}"),
                else_=RecordLink("{+api}/mbdb-spr/{id}/draft"),
            ),
            "self_html": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+ui}/mbdb-spr/{id}"),
                else_=RecordLink("{+ui}/uploads/{id}"),
            ),
            "versions": RecordLink("{+api}/mbdb-spr/{id}/versions"),
        }
