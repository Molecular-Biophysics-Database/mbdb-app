class SearchInAllMixin:
    # search in the 'all' endpoint
    def search_endpoint_url(self, identity, api_config, overrides={}, **kwargs):
        return f"/api/all{api_config.url_prefix}"
