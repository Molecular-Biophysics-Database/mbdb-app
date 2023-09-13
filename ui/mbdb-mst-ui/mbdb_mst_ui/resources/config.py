from oarepo_ui.resources.config import RecordsUIResourceConfig
from oarepo_ui.resources import BabelComponent


class MbdbMstUIResourceConfig(RecordsUIResourceConfig):
    template_folder = "../templates"
    url_prefix = "/mst/"
    blueprint_name = "mbdb-mst-ui"
    ui_serializer_class = "mbdb_mst.resources.records.ui.MbdbMstUIJSONSerializer"
    api_service = "mbdb_mst"
    layout = "mbdb_mst"

    components = [BabelComponent]
    try:
        from oarepo_vocabularies.ui.resources.components import DepositVocabularyOptionsComponent
        components.append(DepositVocabularyOptionsComponent)
    except ImportError:
        pass

    templates = {
        "detail": {
            "layout": "mbdb_mst_ui/Detail.html.jinja",
            "blocks": {
                "record_main_content": "Main",
                "record_sidebar": "Sidebar",
            },
        },
        "search": {"layout": "mbdb_mst_ui/search.html"},
        "edit": {"layout": "mbdb_mst_ui/deposit.html"},
        "create": {"layout": "mbdb_mst_ui/deposit.html"},
    }

    def search_app_config(self, identity, api_config, overrides={}, **kwargs):
        return super().search_app_config(identity, api_config,
                                         overrides=overrides, endpoint='/api/user/mbdb-mst/', **kwargs)
