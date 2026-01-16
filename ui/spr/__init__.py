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

class SprInitialValuesComponent(UIResourceComponent):
    def empty_record(self, *, resource_requestctx, empty_data: Dict, **kwargs):
        empty_data.update(
            make_fixed_values(
                method="Surface plasmon resonance (SPR)",
                resource_type="SPR",
            )
        )


class SprUIResourceConfig(SearchInAllMixin, RecordsUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/spr/"
    blueprint_name = "spr"
    ui_serializer_class = "spr.resources.records.ui.SprUIJSONSerializer"
    api_service = "spr"

    components = [
        BabelComponent,
        AllowedHtmlTagsComponent,
        FilesComponent,
        VocabularyFormDepositVocabularyOptionsComponent,
        SprInitialValuesComponent,
        PermissionsComponent,
    ]

    # TODO: is this still needed?
    edit_layout = "edit_layout.json"

    search_component = "spr/search/ResultsListItem"

    application_id = "spr"

    templates = {
        "detail": "spr.Detail",
        "search": "spr.Search",
        "edit": "spr.Deposit",
        "create": "spr.Deposit",
    }

    routes = {
        **RecordsUIResourceConfig.routes,
        "pdf": "/<pid_value>/pdf"
    }


class SprResource(RecordsUIResource):

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
    return SprResource(SprUIResourceConfig()).as_blueprint()
