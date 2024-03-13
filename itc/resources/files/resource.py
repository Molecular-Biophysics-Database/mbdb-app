from oarepo_ui.resources.file_resource import S3RedirectFileResource


class ItcFileResource(S3RedirectFileResource):
    """ItcFile resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules


class ItcFileDraftResource(S3RedirectFileResource):
    """ItcFileDraft resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules
