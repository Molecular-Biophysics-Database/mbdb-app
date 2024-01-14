from oarepo_ui.resources.file_resource import S3RedirectFileResource


class MstFileResource(S3RedirectFileResource):
    """MstFile resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules


class MstFileDraftResource(S3RedirectFileResource):
    """MstFileDraft resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules
