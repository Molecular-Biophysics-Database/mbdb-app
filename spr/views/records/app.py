from flask import Blueprint


def create_app_blueprint(app):
    blueprint = Blueprint("spr_app", __name__, url_prefix="/records/spr/")
    blueprint.record_once(init_create_app_blueprint)

    # calls record_once for all other functions starting with "init_addons_"
    # https://stackoverflow.com/questions/58785162/how-can-i-call-function-with-string-value-that-equals-to-function-name
    funcs = globals()
    funcs = [
        v for k, v in funcs.items() if k.startswith("init_addons_spr") and callable(v)
    ]
    for func in funcs:
        blueprint.record_once(func)

    return blueprint


def init_create_app_blueprint(state):
    """Init app."""
    app = state.app
    ext = app.extensions["spr"]

    # register service
    sregistry = app.extensions["invenio-records-resources"].registry
    sregistry.register(
        ext.service_records, service_id=ext.service_records.config.service_id
    )

    # Register indexer
    if hasattr(ext.service_records, "indexer"):
        iregistry = app.extensions["invenio-indexer"].registry
        iregistry.register(
            ext.service_records.indexer,
            indexer_id=ext.service_records.config.service_id,
        )


def init_addons_spr_requests(state):
    app = state.app
    requests = app.extensions["invenio-requests"]

    from spr import config

    for rt in getattr(config, "REQUESTS_REGISTERED_TYPES", []):
        requests.request_type_registry.register_type(rt)

    for er in getattr(config, "REQUESTS_ENTITY_RESOLVERS", []):
        requests.entity_resolvers_registry.register_type(er)


def init_addons_spr_published_service(state):
    """Init app."""
    app = state.app
    ext = app.extensions["spr"]

    # register service
    sregistry = app.extensions["invenio-records-resources"].registry
    sregistry.register(
        ext.published_service_records,
        service_id=ext.published_service_records.config.service_id,
    )