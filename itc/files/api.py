from invenio_records_resources.records.api import FileRecord
from invenio_records_resources.records.systemfields import IndexField

from itc.files.models import ItcFileDraftMetadata, ItcFileMetadata


class ItcFile(FileRecord):

    model_cls = ItcFileMetadata

    index = IndexField("itc_file-itc_file-1.0.0", search_alias="itc_file")
    record_cls = None  # is defined inside the parent record


class ItcFileDraft(FileRecord):

    model_cls = ItcFileDraftMetadata

    index = IndexField(
        "itc_file_draft-itc_file_draft-1.0.0", search_alias="itc_file_draft"
    )
    record_cls = None  # is defined inside the parent record
