from invenio_drafts_resources.services import (
    RecordServiceConfig as InvenioRecordDraftsServiceConfig,
)
from invenio_drafts_resources.services.records.components import DraftFilesComponent
from invenio_drafts_resources.services.records.config import is_record
from invenio_records_resources.services import ConditionalLink, RecordLink
from invenio_records_resources.services.records.components import DataComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin
from oarepo_runtime.services.files import FilesComponent
from oarepo_runtime.services.results import RecordList

from mbdb_bli.records.api import MbdbBliDraft, MbdbBliRecord
from mbdb_bli.services.records.permissions import MbdbBliPermissionPolicy
from mbdb_bli.services.records.schema import MbdbBliSchema
from mbdb_bli.services.records.search import MbdbBliSearchOptions


class MbdbBliServiceConfig(
    PermissionsPresetsConfigMixin, InvenioRecordDraftsServiceConfig
):
    """MbdbBliRecord service config."""

    result_list_cls = RecordList

    PERMISSIONS_PRESETS = ["authenticated"]

    url_prefix = "/mbdb-bli/"

    base_permission_policy_cls = MbdbBliPermissionPolicy

    schema = MbdbBliSchema

    search = MbdbBliSearchOptions

    record_cls = MbdbBliRecord

    service_id = "mbdb_bli"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordDraftsServiceConfig.components,
        FilesComponent,
        DataComponent,
        DraftFilesComponent,
    ]

    model = "mbdb_bli"
    draft_cls = MbdbBliDraft
    search_drafts = MbdbBliSearchOptions

    @property
    def links_item(self):
        return {
            "draft": RecordLink("{+api}/mbdb-bli/{id}/draft"),
            "files": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+api}/mbdb-bli/{id}/files"),
                else_=RecordLink("{+api}/mbdb-bli/{id}/draft/files"),
            ),
            "latest": RecordLink("{+api}/mbdb-bli/{id}/versions/latest"),
            "latest_html": RecordLink("{+ui}/bli/{id}/latest"),
            "publish": RecordLink("{+api}/mbdb-bli/{id}/draft/actions/publish"),
            "record": RecordLink("{+api}/mbdb-bli/{id}"),
            "self": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+api}/mbdb-bli/{id}"),
                else_=RecordLink("{+api}/mbdb-bli/{id}/draft"),
            ),
            "self_html": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+ui}/bli/{id}"),
                else_=RecordLink("{+ui}/bli/{id}/edit"),
            ),
            "versions": RecordLink("{+api}/mbdb-bli/{id}/versions"),
        }
