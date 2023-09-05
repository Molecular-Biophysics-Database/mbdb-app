from oarepo_ui.resources.config import RecordsUIResourceConfig
from oarepo_ui.resources import BabelComponent

import jinja2

def is_defined(v):
    return not is_undefined(v)


def is_undefined(v):
    return isinstance(v, jinja2.Undefined)


def undefed():
    return jinja2.Undefined()


def filter_get_data_analysis_for_derived_parameter(data_analyses, derived_parameter_id):
    if is_undefined(data_analyses) or is_undefined(derived_parameter_id):
        return undefed()

    for analysis in data_analyses:
        derived_parameter = analysis['derived_parameter']
        if derived_parameter['id'] == derived_parameter_id:
            return analysis

    return undefed()


def filter_get_entity_involved(derived_parameter, entity_id):
    if is_undefined(derived_parameter) or is_undefined(entity_id) or 'entities_involved' not in derived_parameter:
        return undefed()

    for ei in derived_parameter['entities_involved']:
        if ei['entity']['id'] == entity_id:
            return ei

    return undefed()


def filter_get_ligand_and_target(entities_involved, ligands, targets):
    ligand = undefed()
    target = undefed()

    for ei in entities_involved:
        if is_undefined(ligand):
            for lig in ligands:
                if ei['entity']['id'] == lig['entity']['id']:
                    ligand = lig
                    break

        if is_undefined(target):
            for targ in targets:
                if ei['entity']['id'] == targ['entity']['id']:
                    target = targ
                    break

        if is_defined(target) and is_defined(ligand):
            break

    return { "ligand": ligand, "target": target }


def filter_maybe_get(value, path):
    if is_undefined(value):
        return undefed()

    v = value
    for tok in path.split('.'):
        if is_undefined(v) or tok not in v:
            return undefed()
        v = v[tok]

    return v


NICE_NAME_OVERRIDES = {
    'ph': 'pH',
    'inchi key': 'InChI key',
}
def filter_nice_name(name):
    if name in NICE_NAME_OVERRIDES:
        return NICE_NAME_OVERRIDES[name]
    else:
        return name.replace('_', ' ').capitalize()


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
            "layout": "mbdb_mst_ui/DetailRoot.jinja",
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

    def apply_additional_config(self, catalog):
        catalog.jinja_env.filters["get_data_analysis_for_derived_parameter"] = filter_get_data_analysis_for_derived_parameter
        catalog.jinja_env.filters["get_entity_involved"] = filter_get_entity_involved
        catalog.jinja_env.filters["get_ligand_and_target"] = filter_get_ligand_and_target
        catalog.jinja_env.filters["maybe_get"] = filter_maybe_get
        catalog.jinja_env.filters["nice_name"] = filter_nice_name

        return catalog
