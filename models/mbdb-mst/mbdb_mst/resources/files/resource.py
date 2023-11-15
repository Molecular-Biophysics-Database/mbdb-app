from invenio_records_resources.resources.files.resource import FileResource
from oarepo_runtime.resources import S3RedirectFileResource

class MbdbMstFileResource(S3RedirectFileResource):
    """MbdbMstFile resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules


class MbdbMstFileDraftResource(S3RedirectFileResource):
    """MbdbMstFileDraft resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules
