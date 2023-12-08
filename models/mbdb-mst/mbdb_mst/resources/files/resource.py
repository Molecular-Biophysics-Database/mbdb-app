from oarepo_ui.resources.file_resource import S3RedirectFileResource


class MbdbMstFileResource(S3RedirectFileResource):
    """MbdbMstFile resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules


class MbdbMstFileDraftResource(S3RedirectFileResource):
    """MbdbMstFileDraft resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules
