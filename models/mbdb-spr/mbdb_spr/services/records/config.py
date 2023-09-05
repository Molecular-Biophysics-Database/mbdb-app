from invenio_drafts_resources.services import (
    RecordServiceConfig as InvenioRecordDraftsServiceConfig,
)
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
        FilesOptionsComponent,
        DataComponent,
    ]

    model = "mbdb_spr"
    draft_cls = MbdbSprDraft

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
