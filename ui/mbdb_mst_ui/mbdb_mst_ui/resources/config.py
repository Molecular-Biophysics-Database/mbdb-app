from oarepo_ui.resources.config import RecordsUIResourceConfig


class MbdbMstUiResourceConfig(RecordsUIResourceConfig):
    template_folder = "../templates"
    url_prefix = "/mst/"
    blueprint_name = "mbdb_mst_ui"
    ui_serializer_class = "mbdb_mst.resources.records.ui.MbdbMstUIJSONSerializer"
    api_service = "mbdb_mst"
    layout = "mbdb_mst"

    templates = {
        "detail": {
            "layout": "mbdb_mst_ui/detail.html",
            "blocks": {
                "record_main_content": "mbdb_mst_ui/main.html",
                "record_sidebar": "mbdb_mst_ui/sidebar.html"                
            },
        },
        "search": {"layout": "mbdb_mst_ui/search.html"},
    }
