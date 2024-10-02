from typing import Dict

from oarepo_ui.resources.components import FilesComponent
from oarepo_ui.resources.config import RecordsUIResourceConfig
from oarepo_ui.resources.resource import RecordsUIResource
from oarepo_ui.resources.components import UIResourceComponent
from oarepo_ui.resources import BabelComponent, PermissionsComponent
from oarepo_vocabularies.ui.resources.config import VocabularyFormDepositVocabularyOptionsComponent

from common.fixed_record_values import make_fixed_values


class SprInitialValuesComponent(UIResourceComponent):
    def empty_record(self, *, resource_requestctx, empty_data: Dict, **kwargs):
        empty_data.update(
            make_fixed_values(
                technique="Surface plasmon resonance (SPR)",
                schema_version="0.9.6",
                resource_type="SPR",
            )
        )

class SprResourceConfig(RecordsUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/spr/"
    blueprint_name = "spr"
    ui_serializer_class = "spr.resources.records.ui.SprUIJSONSerializer"
    api_service = "spr"

    components = [
        BabelComponent,
        FilesComponent,
        VocabularyFormDepositVocabularyOptionsComponent,
        SprInitialValuesComponent,
        PermissionsComponent,
    ]

    # TODO: is this still needed?
    edit_layout = 'edit_layout.json'

    search_component = "spr/search/ResultsListItem"

    application_id = "spr"

    templates = {
        "detail": "spr.Detail",
        "search": "spr.Search",
        "edit": "spr.Deposit",
        "create": "spr.Deposit",
    }

    # TODO: will be removed when user dashboard gets implemented
    def search_app_config(self, identity, api_config, overrides=None, **kwargs):
        return super().search_app_config(
            identity, api_config,
            overrides=overrides or {}, endpoint='/api/user/records/spr/', **kwargs)


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
