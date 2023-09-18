import jinja2

def is_defined(v):
    return not is_undefined(v)


def is_undefined(v):
    return isinstance(v, jinja2.Undefined)


def undefed():
    return jinja2.Undefined()


def maybe_get(value, path):
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
def nice_name(name):
    if name in NICE_NAME_OVERRIDES:
        return NICE_NAME_OVERRIDES[name]
    else:
        return name.replace('_', ' ').capitalize()
