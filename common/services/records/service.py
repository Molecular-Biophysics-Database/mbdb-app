from invenio_records_resources.services.uow import unit_of_work

class AddWorkflowServiceMixin:

    @unit_of_work()
    def create(self, identity, data, uow=None, expand=False, **kwargs):
        parent = data.setdefault("parent", {})
        community = parent.setdefault("communities", {})
        if not community:
            parent["workflow"] = "individual"
        else:
            parent["workflow"] = "community"

        return super().create(identity, data, uow=uow, expand=expand, **kwargs)