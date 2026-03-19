from typing import Dict
from oarepo_ui.resources import BabelComponent, PermissionsComponent
from oarepo_ui.resources.components import FilesComponent, UIResourceComponent, AllowedHtmlTagsComponent
from oarepo_ui.resources.config import RecordsUIResourceConfig
from oarepo_ui.resources.resource import RecordsUIResource
from oarepo_vocabularies.ui.resources.config import (
    VocabularyFormDepositVocabularyOptionsComponent,
)
from common.fixed_record_values import make_fixed_values
from common.ui.search_in_all import SearchInAllMixin
from invenio_records_resources.resources.records.resource import request_read_args, request_view_args
from flask import request
from common.utils.pdf_utils import generate_pdf_response
from common.utils.filename_utils import build_pdf_filename
from invenio_rdm_records.services.errors import RecordDeletedException

class BliInitialValuesComponent(UIResourceComponent):
    def empty_record(self, *, resource_requestctx, empty_data: Dict, **kwargs):
        empty_data.update(
            make_fixed_values(
                method="Bio-layer interferometry (BLI)",
                resource_type="BLI",
            )
        )


class BliUIResourceConfig(SearchInAllMixin, RecordsUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/bli/"
    blueprint_name = "bli"
    ui_serializer_class = "bli.resources.records.ui.BliUIJSONSerializer"
    api_service = "bli"

    components = [
        BabelComponent,
        AllowedHtmlTagsComponent,
        FilesComponent,
        VocabularyFormDepositVocabularyOptionsComponent,
        BliInitialValuesComponent,
        PermissionsComponent,
    ]

    # TODO: is this still needed?
    edit_layout = "edit_layout.json"

    search_component = "bli/search/ResultsListItem"

    application_id = "bli"

    templates = {
        "detail": "bli.Detail",
        "search": "bli.Search",
        "edit": "bli.Deposit",
        "create": "bli.Deposit",
    }

    routes = {
        **RecordsUIResourceConfig.routes,
        "pdf": "/<pid_value>/pdf"
    }

class BliResource(RecordsUIResource):

    # TODO: will be removed when user dashboard gets implemented
    def _get_record(self, resource_requestctx, allow_draft=False, include_deleted=False):
        try:
            return super()._get_record(resource_requestctx, allow_draft=False, include_deleted=include_deleted)
        except RecordDeletedException:
            raise
        except:
            return super()._get_record(resource_requestctx, allow_draft=True, include_deleted=include_deleted)

    @request_read_args
    @request_view_args
    def pdf(self):
        base_url = request.url.split("?")[0].replace("/pdf", "")
        url = f"{base_url}?pdf_embedded=true"

        pid_value = request.view_args.get("pid_value", "record")
        record = self._get_record(request, allow_draft=True)

        filename = build_pdf_filename(record.to_dict(), pid_value)

        return generate_pdf_response(url, filename)


def create_blueprint(app):
    """Register blueprint for this resource."""
    from common.utils.tombstone import record_tombstone_error
    blueprint = BliResource(BliUIResourceConfig()).as_blueprint()
    blueprint.register_error_handler(RecordDeletedException, record_tombstone_error)
    return blueprint
