from oarepo_ui.resources import BabelComponent
from oarepo_ui.resources.components import FilesComponent
from oarepo_ui.resources.config import RecordsUIResourceConfig
from oarepo_ui.resources.resource import RecordsUIResource
from datetime import date
from oarepo_ui.resources.components import UIResourceComponent
from typing import Dict

from common.ui.components import MBDBEditComponent

from oarepo_vocabularies.ui.resources.components import DepositVocabularyOptionsComponent

class ItcInitialValuesComponent(UIResourceComponent):
    def empty_record(self, *, resource_requestctx, empty_data: Dict, **kwargs):
        empty_data.update({
          "metadata": {
            "general_parameters": {
              "schema_version": "0.9.21",
              "technique": "ITC measurement of hemoglobin serum elements",
              "record_information": {
                "publisher": "MBDB",
                "resource_type_general": "Dataset",
                "resource_type": "ITC",
                "deposition_date": date.today().isoformat(),
                "date_available": date.today().isoformat(),
                "subject_category": "Biophysics",
              },
            },
            "method_specific_parameters": {
              "schema_version": "0.0.3"
            }
          }
        })

class ItcResourceConfig(RecordsUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/itc/"
    blueprint_name = "itc"
    ui_serializer_class = "itc.resources.records.ui.ItcUIJSONSerializer"
    api_service = "itc"

    components = [BabelComponent, FilesComponent, DepositVocabularyOptionsComponent, ItcInitialValuesComponent]

    # TODO: is this still needed?
    edit_layout = 'edit_layout.json'


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
