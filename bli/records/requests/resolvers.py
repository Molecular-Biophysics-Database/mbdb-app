from oarepo_runtime.records.entity_resolvers import (
    DraftProxy,
    RecordProxy,
    RecordResolver,
)


class BliResolver(RecordResolver):
    # invenio_requests.registry.TypeRegistry
    # requires name of the resolver for the model; needs only to be unique for the model, so use the name of the model
    type_id = "bli"

    proxy_cls = RecordProxy

    def __init__(self, record_cls, service_id, type_key):
        super().__init__(
            record_cls, service_id, type_key=type_key, proxy_cls=self.proxy_cls
        )


class BliDraftResolver(RecordResolver):
    # invenio_requests.registry.TypeRegistry
    # requires name of the resolver for the model; needs only to be unique for the model, so use the name of the model
    type_id = "bli_draft"

    proxy_cls = DraftProxy

    def __init__(self, record_cls, service_id, type_key):
        super().__init__(
            record_cls, service_id, type_key=type_key, proxy_cls=self.proxy_cls
        )
