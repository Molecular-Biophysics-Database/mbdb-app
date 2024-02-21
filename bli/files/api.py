from invenio_records_resources.records.api import FileRecord
from invenio_records_resources.records.systemfields import IndexField

from bli.files.models import BliFileDraftMetadata, BliFileMetadata


class BliFile(FileRecord):

    model_cls = BliFileMetadata

    index = IndexField("bli_file-bli_file-1.0.0")
    record_cls = None  # is defined inside the parent record


class BliFileDraft(FileRecord):

    model_cls = BliFileDraftMetadata

    index = IndexField("bli_file_draft-bli_file_draft-1.0.0")
    record_cls = None  # is defined inside the parent record
