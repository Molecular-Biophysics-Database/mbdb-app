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


class SprInitialValuesComponent(UIResourceComponent):
    def empty_record(self, *, resource_requestctx, empty_data: Dict, **kwargs):
        empty_data.update(
            make_fixed_values(
                method="Surface plasmon resonance (SPR)",
                resource_type="SPR",
            )
        )


class SprResourceConfig(SearchInAllMixin, RecordsUIResourceConfig):
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


class SprResource(RecordsUIResource):

    # TODO: will be removed when user dashboard gets implemented
    def _get_record(self, resource_requestctx, allow_draft=False):
        try:
            return super()._get_record(resource_requestctx, allow_draft=False)
        except:
            return super()._get_record(resource_requestctx, allow_draft=True)


def create_blueprint(app):
    """Register blueprint for this resource."""
    return SprResource(SprResourceConfig()).as_blueprint()
