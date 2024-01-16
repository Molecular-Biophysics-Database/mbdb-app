from oarepo_ui.resources.file_resource import S3RedirectFileResource


class BliFileResource(S3RedirectFileResource):
    """BliFile resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules


class BliFileDraftResource(S3RedirectFileResource):
    """BliFileDraft resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules
