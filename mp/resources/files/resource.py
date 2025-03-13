from oarepo_ui.resources.file_resource import S3RedirectFileResource


class MpFileResource(S3RedirectFileResource):
    """MpFile resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules


class MpFileDraftResource(S3RedirectFileResource):
    """MpFileDraft resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules
