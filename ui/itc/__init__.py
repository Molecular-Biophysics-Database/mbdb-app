from typing import Dict

from oarepo_ui.resources import BabelComponent, PermissionsComponent
from oarepo_ui.resources.components import FilesComponent, UIResourceComponent
from oarepo_ui.resources.config import RecordsUIResourceConfig
from oarepo_ui.resources.resource import RecordsUIResource
from oarepo_vocabularies.ui.resources.config import (
    VocabularyFormDepositVocabularyOptionsComponent,
)

from common.fixed_record_values import make_fixed_values
from common.ui.search_in_all import SearchInAllMixin


class ItcInitialValuesComponent(UIResourceComponent):
    def empty_record(self, *, resource_requestctx, empty_data: Dict, **kwargs):
        empty_data.update(
            make_fixed_values(
                method="Isothermal Titration Calorimetry (ITC)",
                resource_type="ITC",
            )
        )


class ItcResourceConfig(SearchInAllMixin, RecordsUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/itc/"
    blueprint_name = "itc"
    ui_serializer_class = "itc.resources.records.ui.ItcUIJSONSerializer"
    api_service = "itc"

    components = [
        BabelComponent,
        FilesComponent,
        VocabularyFormDepositVocabularyOptionsComponent,
        ItcInitialValuesComponent,
        PermissionsComponent,
    ]

    # TODO: is this still needed?
    edit_layout = "edit_layout.json"

    search_component = "itc/search/ResultsListItem"

    application_id = "itc"

    templates = {
        "detail": "itc.Detail",
        "search": "itc.Search",
        "edit": "itc.Deposit",
        "create": "itc.Deposit",
    }


class ItcResource(RecordsUIResource):

    # TODO: will be removed when user dashboard gets implemented
    def _get_record(self, resource_requestctx, allow_draft=False):
        try:
            return super()._get_record(resource_requestctx, allow_draft=False)
        except:
            return super()._get_record(resource_requestctx, allow_draft=True)


def create_blueprint(app):
    """Register blueprint for this resource."""
    return ItcResource(ItcResourceConfig()).as_blueprint()
