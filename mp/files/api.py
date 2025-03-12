from invenio_records_resources.records.api import FileRecord
from invenio_records_resources.records.systemfields import IndexField

from mp.files.models import MpFileDraftMetadata, MpFileMetadata


class MpFile(FileRecord):

    model_cls = MpFileMetadata

    index = IndexField(
        "mp_file-mp_file-1.0.0",
    )
    record_cls = None  # is defined inside the parent record


class MpFileDraft(FileRecord):

    model_cls = MpFileDraftMetadata

    index = IndexField(
        "mp_file_draft-mp_file_draft-1.0.0",
    )
    record_cls = None  # is defined inside the parent record
