from flask.blueprints import Blueprint

def create_api_blueprint(app):
    """Create MbdbMstRecord blueprint."""
    blueprint = app.extensions["mbdb_mst"].resource.as_blueprint()
    blueprint.record_once(init_create_api_blueprint)

    funcs = globals()
    funcs = [
        v
        for k, v in funcs.items()
        if k.startswith("create_api_blueprint_addon_") and callable(v)
    ]
    for func in funcs:
        blueprint.record_once(func)

    return blueprint


def init_create_api_blueprint(state):
    """Init app."""
    app = state.app
    ext = app.extensions["mbdb_mst"]

    # register service
    sregistry = app.extensions["invenio-records-resources"].registry
    sregistry.register(ext.service, service_id="mbdb_mst")

    # Register indexer
    if hasattr(ext.service, "indexer"):
        iregistry = app.extensions["invenio-indexer"].registry
        iregistry.register(ext.service.indexer, indexer_id="mbdb_mst")


def create_app_blueprint(app):
    """Create MbdbMstRecord blueprint."""
    blueprint = Blueprint("mbdb_mst_app", __name__, url_prefix="mbdb-mst")
    blueprint.record_once(init_create_app_blueprint)

    funcs = globals()
    funcs = [
        v
        for k, v in funcs.items()
        if k.startswith("create_app_blueprint_addon_") and callable(v)
    ]
    for func in funcs:
        blueprint.record_once(func)

    return blueprint


def init_create_app_blueprint(state):
    """Init app."""
    app = state.app
    ext = app.extensions["mbdb_mst"]

    # register service
    sregistry = app.extensions["invenio-records-resources"].registry
    sregistry.register(ext.service, service_id="mbdb_mst")

    # Register indexer
    if hasattr(ext.service, "indexer"):
        iregistry = app.extensions["invenio-indexer"].registry
        iregistry.register(ext.service.indexer, indexer_id="mbdb_mst")
