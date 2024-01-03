from oarepo_ui.resources.resource import RecordsUIResource

class MbdbMstUIResource(RecordsUIResource):
    def _get_record(self, resource_requestctx, allow_draft=False):
        try:
            return super()._get_record(resource_requestctx, allow_draft=False)
        except:
            return super()._get_record(resource_requestctx, allow_draft=True)

    def empty_record(self, resource_requestctx, **kwargs):
        """Create an empty record with default values. """
        return {}