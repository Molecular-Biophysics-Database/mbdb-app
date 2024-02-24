import jinja2
from oarepo_ui.resources.templating.data import FieldData, EMPTY_FIELD_DATA
from oarepo_ui.resources.templating.filters import ichain


def _is_undefined(v):
    return isinstance(v, jinja2.Undefined)


def maybe_get(value, path):
    """filter: maybe_get"""
    if _is_undefined(value):
        return jinja2.Undefined()

    v = value
    for tok in path.split('.'):
        if _is_undefined(v) or tok not in v:
            return jinja2.Undefined()
        v = v[tok]

    return v


NICE_NAME_OVERRIDES = {
    'ph': 'pH',
    'inchi key': 'InChI key',
}
def nice_name(name):
    """filter: nice_name"""
    name = str(name)

    if name in NICE_NAME_OVERRIDES:
        return NICE_NAME_OVERRIDES[name]
    else:
        return name.replace('_', ' ').capitalize()


def find_reference(parts, part_id):
    if isinstance(part_id, FieldData):
        part_id = part_id.value

    for part in ichain(parts):
        if part.id.value == part_id:
            return part

    return EMPTY_FIELD_DATA
