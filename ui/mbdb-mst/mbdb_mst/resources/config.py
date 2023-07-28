from oarepo_ui.resources.config import RecordsUIResourceConfig


class MbdbMstResourceConfig(RecordsUIResourceConfig):
    template_folder = "../templates"
    url_prefix = "/mbdb-mst/"
    blueprint_name = "mbdb-mst"
    ui_serializer_class = "mbdb_mst.resources.records.ui.MbdbMstUIJSONSerializer"
    api_service = "mbdb_mst"
    layout = "mbdb_mst"

    templates = {
        "detail": {
            "layout": "mbdb_mst/detail.html",
            "blocks": {
                "record_main_content": "mbdb_mst/main.html",
                "record_sidebar": "mbdb_mst/sidebar.html"                
            },
        },
        "search": {"layout": "mbdb_mst/search.html"},
    }
