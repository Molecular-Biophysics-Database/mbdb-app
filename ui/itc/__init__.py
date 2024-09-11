from oarepo_ui.resources import BabelComponent
from oarepo_ui.resources.components import FilesComponent
from oarepo_ui.resources.config import RecordsUIResourceConfig
from oarepo_ui.resources.resource import RecordsUIResource
from oarepo_ui.resources.components import UIResourceComponent
from typing import Dict

from common.fixed_record_values import make_fixed_values

from oarepo_vocabularies.ui.resources.components import DepositVocabularyOptionsComponent


class ItcInitialValuesComponent(UIResourceComponent):
    def empty_record(self, *, resource_requestctx, empty_data: Dict, **kwargs):
        empty_data.update(
            make_fixed_values(
                technique="Isothermal Titration Calorimetry (ITC)",
                schema_version="0.1.0",
                resource_type="ITC",
            )
        )


class ItcResourceConfig(RecordsUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/itc/"
    blueprint_name = "itc"
    ui_serializer_class = "itc.resources.records.ui.ItcUIJSONSerializer"
    api_service = "itc"

    components = [BabelComponent, FilesComponent, DepositVocabularyOptionsComponent, ItcInitialValuesComponent]

    # TODO: is this still needed?
    edit_layout = 'edit_layout.json'

    search_component = "itc/search/ResultsListItem"

    application_id = "itc"

    templates = {
        "detail": "itc.Detail",
        "search": "itc.Search",
        "edit": "itc.Deposit",
        "create": "itc.Deposit",
    }

    # TODO: will be removed when user dashboard gets implemented
    def search_app_config(self, identity, api_config, overrides=None, **kwargs):
        return super().search_app_config(
            identity, api_config,
            overrides=overrides or {}, endpoint='/api/user/records/itc/', **kwargs)


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
