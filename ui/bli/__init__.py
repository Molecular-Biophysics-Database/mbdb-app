from oarepo_ui.resources import BabelComponent
from oarepo_ui.resources.components import FilesComponent
from oarepo_ui.resources.config import RecordsUIResourceConfig
from oarepo_ui.resources.resource import RecordsUIResource
from datetime import date
from oarepo_ui.resources.components import UIResourceComponent
from typing import Dict

from common.ui.components import MBDBEditComponent

from oarepo_vocabularies.ui.resources.components import DepositVocabularyOptionsComponent

class BliInitialValuesComponent(UIResourceComponent):
    def empty_record(self, *, resource_requestctx, empty_data: Dict, **kwargs):
        empty_data.update({
          "metadata": {
            "general_parameters": {
              "schema_version": "0.9.21",
              "technique": "BLI measurement of hemoglobin serum elements",
              "record_information": {
                "publisher": "MBDB",
                "resource_type_general": "Dataset",
                "resource_type": "BLI",
                "deposition_date": date.today().isoformat(),
                "date_available": date.today().isoformat(),
                "subject_category": "Biophysics",
              },
            },
            "method_specific_parameters": {
              "schema_version": "0.9.6"
            }
          }
        })

class BliResourceConfig(RecordsUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/bli/"
    blueprint_name = "bli"
    ui_serializer_class = "bli.resources.records.ui.BliUIJSONSerializer"
    api_service = "bli"

    components = [BabelComponent, FilesComponent, DepositVocabularyOptionsComponent, BliInitialValuesComponent]

    # TODO: is this still needed?
    edit_layout = 'edit_layout.json'

    search_component = "bli/search/ResultsListItem.jsx"


    application_id = "bli"

    templates = {
        "detail": "bli.Detail",
        "search": "bli.Search",
        "edit": "bli.Deposit",
        "create": "bli.Deposit",
    }

    # TODO: will be removed when user dashboard gets implemented
    def search_app_config(self, identity, api_config, overrides=None, **kwargs):
        return super().search_app_config(
            identity, api_config,
            overrides=overrides or {}, endpoint='/api/user/records/bli/', **kwargs)


class BliResource(RecordsUIResource):

    # TODO: will be removed when user dashboard gets implemented
    def _get_record(self, resource_requestctx, allow_draft=False):
        try:
            return super()._get_record(resource_requestctx, allow_draft=False)
        except:
            return super()._get_record(resource_requestctx, allow_draft=True)


def create_blueprint(app):
    """Register blueprint for this resource."""
    return BliResource(BliResourceConfig()).as_blueprint()
