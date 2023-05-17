

def create_blueprint_from_app(app):
    """Create MbdbMstFile blueprint."""
    blueprint = app.extensions["mbdb_mst_file"].resource.as_blueprint()
    blueprint.record_once(init_create_blueprint_from_app)

    # calls record_once for all other functions starting with "init_addons_"
    # https://stackoverflow.com/questions/58785162/how-can-i-call-function-with-string-value-that-equals-to-function-name
    funcs = globals()
    funcs = [
        v
        for k, v in funcs.items()
        if k.startswith("init_addons_mbdb_mst_file") and callable(v)
    ]
    for func in funcs:
        blueprint.record_once(func)

    return blueprint


def init_create_blueprint_from_app(state):
    """Init app."""
    app = state.app
    ext = app.extensions["mbdb_mst_file"]

    # register service
    sregistry = app.extensions["invenio-records-resources"].registry
    sregistry.register(ext.service, service_id="mbdb_mst_file")