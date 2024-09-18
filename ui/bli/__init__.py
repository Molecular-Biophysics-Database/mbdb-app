from oarepo_ui.resources import BabelComponent
from oarepo_ui.resources.components import FilesComponent
from oarepo_ui.resources.config import RecordsUIResourceConfig
from oarepo_ui.resources.resource import RecordsUIResource
from oarepo_ui.resources.components import UIResourceComponent
from oarepo_ui.resources import BabelComponent, PermissionsComponent
from typing import Dict
from common.fixed_record_values import make_fixed_values
from common.ui.components import MBDBEditComponent

from oarepo_vocabularies.ui.resources.components import DepositVocabularyOptionsComponent


class BliInitialValuesComponent(UIResourceComponent):
    def empty_record(self, *, resource_requestctx, empty_data: Dict, **kwargs):
        empty_data.update(
            make_fixed_values(
                technique="Bio-layer interferometry (BLI)",
                schema_version="0.9.7",
                resource_type="BLI",
            )
        )


class BliResourceConfig(RecordsUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/bli/"
    blueprint_name = "bli"
    ui_serializer_class = "bli.resources.records.ui.BliUIJSONSerializer"
    api_service = "bli"

    components = [BabelComponent, FilesComponent, DepositVocabularyOptionsComponent, BliInitialValuesComponent, PermissionsComponent]

    # TODO: is this still needed?
    edit_layout = 'edit_layout.json'

    search_component = "bli/search/ResultsListItem"

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
