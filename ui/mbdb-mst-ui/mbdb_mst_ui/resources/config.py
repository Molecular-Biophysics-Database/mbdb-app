from oarepo_ui.resources.config import RecordsUIResourceConfig
from oarepo_ui.resources import BabelComponent

from mbdb_common.ui.components import MBDBEditComponent
from .mbdb_files_component import MBDBFilesComponent


class MbdbMstUIResourceConfig(RecordsUIResourceConfig):
    template_folder = "../templates"
    url_prefix = "/mst/"
    blueprint_name = "mbdb-mst-ui"
    ui_serializer_class = "mbdb_mst.resources.records.ui.MbdbMstUIJSONSerializer"
    api_service = "mbdb_mst"
    layout = "mbdb_mst"
    edit_layout = 'edit_layout.json'

    components = [BabelComponent, MBDBEditComponent, MBDBFilesComponent]
    try:
        from oarepo_vocabularies.ui.resources.components import DepositVocabularyOptionsComponent
        components.append(DepositVocabularyOptionsComponent)
    except ImportError:
        pass

    templates = {
        "detail": {
            "layout": "mbdb_mst_ui/DetailRoot.jinja",
            "blocks": {
                "record_main_content": "Main",
                "record_sidebar": "Sidebar",
            },
        },
        "search": {"layout": "mbdb_mst_ui/Search.html.jinja", "app_id": "Mbdb_mst_ui.Search"},
        "edit": {"layout": "mbdb_mst_ui/Deposit.html.jinja"},
        "create": {"layout": "mbdb_mst_ui/Deposit.html.jinja"},
    }

    def search_app_config(self, identity, api_config, overrides={}, **kwargs):
        return super().search_app_config(
            identity, api_config,
            overrides=overrides, endpoint='/api/user/mbdb-mst/', **kwargs)
