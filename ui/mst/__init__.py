from oarepo_ui.resources import BabelComponent
from oarepo_ui.resources.components import FilesComponent
from oarepo_ui.resources.config import RecordsUIResourceConfig
from oarepo_ui.resources.resource import RecordsUIResource

from common.ui.components import MBDBEditComponent

from oarepo_vocabularies.ui.resources.components import DepositVocabularyOptionsComponent


class MstResourceConfig(RecordsUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/mst/"
    blueprint_name = "mst"
    ui_serializer_class = "mst.resources.records.ui.MstUIJSONSerializer"
    api_service = "mst"

    # TODO: is MBDBEditComponent still needed?
    components = [BabelComponent, MBDBEditComponent, FilesComponent, DepositVocabularyOptionsComponent]

    # TODO: is this still needed?
    edit_layout = 'edit_layout.json'


    application_id = "mst"

    templates = {
        "detail": "mst.Detail",
        "search": "mst.Search",
        "edit": "mst.Deposit",
        "create": "mst.Deposit",
    }

    # TODO: will be removed when user dashboard gets implemented
    def search_app_config(self, identity, api_config, overrides=None, **kwargs):
        return super().search_app_config(
            identity, api_config,
            overrides=overrides or {}, endpoint='/api/user/records/mst/', **kwargs)


class MstResource(RecordsUIResource):

    # TODO: will be removed when user dashboard gets implemented
    def _get_record(self, resource_requestctx, allow_draft=False):
        try:
            return super()._get_record(resource_requestctx, allow_draft=False)
        except:
            return super()._get_record(resource_requestctx, allow_draft=True)


def create_blueprint(app):
    """Register blueprint for this resource."""
    return MstResource(MstResourceConfig()).as_blueprint()
