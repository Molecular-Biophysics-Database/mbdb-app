from typing import Dict

from oarepo_ui.resources.components import FilesComponent
from oarepo_ui.resources.config import RecordsUIResourceConfig
from oarepo_ui.resources.resource import RecordsUIResource
from oarepo_ui.resources.components import UIResourceComponent
from oarepo_ui.resources import BabelComponent, PermissionsComponent
from oarepo_vocabularies.ui.resources.config import (
    VocabularyFormDepositVocabularyOptionsComponent,
)

from common.fixed_record_values import make_fixed_values


class MpInitialValuesComponent(UIResourceComponent):
    def empty_record(self, *, resource_requestctx, empty_data: Dict, **kwargs):
        empty_data.update(
            make_fixed_values(
                technique="Mass photometry (MP)",
                resource_type="MP",
            )
        )


class MpResourceConfig(RecordsUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/mp/"
    blueprint_name = "mp"
    ui_serializer_class = "mp.resources.records.ui.MpUIJSONSerializer"
    api_service = "mp"

    components = [
        BabelComponent,
        FilesComponent,
        VocabularyFormDepositVocabularyOptionsComponent,
        MpInitialValuesComponent,
        PermissionsComponent,
    ]

    # TODO: is this still needed?
    edit_layout = "edit_layout.json"

    search_component = "mp/search/ResultsListItem"

    application_id = "mp"

    templates = {
        "detail": "mp.Detail",
        "search": "mp.Search",
        "edit": "mp.Deposit",
        "create": "mp.Deposit",
    }

    # TODO: will be removed when user dashboard gets implemented
    def search_app_config(self, identity, api_config, overrides=None, **kwargs):
        return super().search_app_config(
            identity,
            api_config,
            overrides=overrides or {},
            endpoint="/api/user/records/mo/",
            **kwargs,
        )


class MpResource(RecordsUIResource):

    # TODO: will be removed when user dashboard gets implemented
    def _get_record(self, resource_requestctx, allow_draft=False):
        try:
            return super()._get_record(resource_requestctx, allow_draft=False)
        except:
            return super()._get_record(resource_requestctx, allow_draft=True)


def create_blueprint(app):
    """Register blueprint for this resource."""
    return MpResource(MpResourceConfig()).as_blueprint()
