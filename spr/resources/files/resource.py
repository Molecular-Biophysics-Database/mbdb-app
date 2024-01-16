from oarepo_ui.resources.file_resource import S3RedirectFileResource


class SprFileResource(S3RedirectFileResource):
    """SprFile resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules


class SprFileDraftResource(S3RedirectFileResource):
    """SprFileDraft resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules
