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


class BliResource(RecordsUIResource):

    # TODO: will be removed when user dashboard gets implemented
    def _get_record(self, resource_requestctx, allow_draft=False):
        try:
            return super()._get_record(resource_requestctx, allow_draft=False)
        except:
            return super()._get_record(resource_requestctx, allow_draft=True)


def create_blueprint(app):
    """Register blueprint for this resource."""
    return BliResource(BliUIResourceConfig()).as_blueprint()
