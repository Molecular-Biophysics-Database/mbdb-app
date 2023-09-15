from .resources.filters import *

MBDB_MST_UI_RESOURCE = "mbdb_mst_ui.resources.resource:MbdbMstUIResource"
MBDB_MST_UI_RESOURCE_CONFIG = "mbdb_mst_ui.resources.config:MbdbMstUIResourceConfig"

OAREPO_UI_JINJAX_FILTERS = {
    'maybe_get': maybe_get,
    'nice_name': nice_name
}
