from invenio_drafts_resources.services import (
    RecordServiceConfig as InvenioRecordDraftsServiceConfig,
)
from invenio_drafts_resources.services.records.components import DraftFilesComponent
from invenio_drafts_resources.services.records.config import is_record
from invenio_records_resources.services import (
    ConditionalLink,
    RecordLink,
    pagination_links,
)
from invenio_records_resources.services.records.components import DataComponent
from itc.records.api import ItcDraft, ItcRecord
from itc.services.records.permissions import ItcPermissionPolicy
from itc.services.records.results import ItcRecordItem, ItcRecordList
from itc.services.records.schema import ItcSchema
from itc.services.records.search import ItcSearchOptions
from oarepo_runtime.records import has_draft, is_published_record
from oarepo_runtime.services.components import OwnersComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin
from oarepo_runtime.services.files import FilesComponent

from common.services.records.components import ForeignVocabularyFetcherComponent


class ItcServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordDraftsServiceConfig):
    """ItcRecord service config."""

    result_item_cls = ItcRecordItem

    result_list_cls = ItcRecordList

    PERMISSIONS_PRESETS = ["authenticated"]

    url_prefix = "/records/itc/"

    base_permission_policy_cls = ItcPermissionPolicy

    schema = ItcSchema

    search = ItcSearchOptions

    record_cls = ItcRecord

    service_id = "itc"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordDraftsServiceConfig.components,
        ForeignVocabularyFetcherComponent,
        OwnersComponent,
        DraftFilesComponent,
        DataComponent,
        FilesComponent,
    ]

    model = "itc"
    draft_cls = ItcDraft
    search_drafts = ItcSearchOptions

    @property
    def links_item(self):
        return {
            "draft": RecordLink("{+api}/records/itc/{id}/draft"),
            "edit_html": RecordLink("{+ui}/itc/{id}/edit", when=has_draft),
            "files": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+api}/records/itc/{id}/files"),
                else_=RecordLink("{+api}/records/itc/{id}/draft/files"),
            ),
            "latest": RecordLink("{+api}/records/itc/{id}/versions/latest"),
            "latest_html": RecordLink("{+ui}/itc/{id}/latest"),
            "publish": RecordLink("{+api}/records/itc/{id}/draft/actions/publish"),
            "record": RecordLink("{+api}/records/itc/{id}"),
            "requests": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/itc/{id}/requests"),
                else_=RecordLink("{+api}/records/itc/{id}/draft/requests"),
            ),
            "self": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/itc/{id}"),
                else_=RecordLink("{+api}/records/itc/{id}/draft"),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+ui}/itc/{id}"),
                else_=RecordLink("{+ui}/itc/{id}/preview"),
            ),
            "versions": RecordLink("{+api}/records/itc/{id}/versions"),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/records/itc/{?args*}"),
        }

    @property
    def links_search_drafts(self):
        return {
            **pagination_links("{+api}/user/records/itc/{?args*}"),
        }

    @property
    def links_search_versions(self):
        return {
            **pagination_links("{+api}/records/itc/{id}/versions{?args*}"),
        }
