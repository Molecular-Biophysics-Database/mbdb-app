from oarepo_ui.resources.config import RecordsUIResourceConfig

class MstUiResourceConfig(RecordsUIResourceConfig):
    template_folder = "../templates"
    url_prefix = "/mst/"
    blueprint_name = "mst-ui"
    ui_serializer_class = "mbdb_mst.resources.records.ui.MbdbMstUIJSONSerializer"
    api_service = "mbdb_mst"
    layout = "mbdb_mst"

    templates = {
        "detail": {
            "layout": "mst_ui/detail.html",
            "blocks": {
                "record_main_content": "mst_ui/main.html",
                "record_sidebar": "mst_ui/sidebar.html"                
            },
        },
        "search": {"layout": "mst_ui/search.html"},
    }
