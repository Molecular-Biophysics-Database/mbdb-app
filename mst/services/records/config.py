from invenio_drafts_resources.services import (
    RecordServiceConfig as InvenioRecordDraftsServiceConfig,
)
from invenio_drafts_resources.services.records.components import DraftFilesComponent
from invenio_drafts_resources.services.records.config import is_record
from invenio_records_resources.services import ConditionalLink, RecordLink
from invenio_records_resources.services.records.components import DataComponent
from oarepo_requests.services.components import PublishDraftComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin
from oarepo_runtime.services.files import FilesComponent
from oarepo_runtime.services.results import RecordList

from mst.records.api import MstDraft, MstRecord
from mst.services.records.permissions import MstPermissionPolicy
from mst.services.records.schema import MstSchema
from mst.services.records.search import MstSearchOptions


class MstServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordDraftsServiceConfig):
    """MstRecord service config."""

    result_list_cls = RecordList

    PERMISSIONS_PRESETS = ["authenticated"]

    url_prefix = "/records/mst/"

    base_permission_policy_cls = MstPermissionPolicy

    schema = MstSchema

    search = MstSearchOptions

    record_cls = MstRecord

    service_id = "mst"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordDraftsServiceConfig.components,
        PublishDraftComponent("publish_draft", "delete_record"),
        FilesComponent,
        DataComponent,
        DraftFilesComponent,
    ]

    model = "mst"
    draft_cls = MstDraft
    search_drafts = MstSearchOptions

    @property
    def links_item(self):
        return {
            "draft": RecordLink("{+api}/records/mst/{id}/draft"),
            "files": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+api}/records/mst/{id}/files"),
                else_=RecordLink("{+api}/records/mst/{id}/draft/files"),
            ),
            "latest": RecordLink("{+api}/records/mst/{id}/versions/latest"),
            "latest_html": RecordLink("{+ui}/mst/{id}/latest"),
            "publish": RecordLink("{+api}/records/mst/{id}/draft/actions/publish"),
            "record": RecordLink("{+api}/records/mst/{id}"),
            "self": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+api}/records/mst/{id}"),
                else_=RecordLink("{+api}/records/mst/{id}/draft"),
            ),
            "self_html": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+ui}/mst/{id}"),
                else_=RecordLink("{+ui}/mst/{id}/edit"),
            ),
            "versions": RecordLink("{+api}/records/mst/{id}/versions"),
        }
