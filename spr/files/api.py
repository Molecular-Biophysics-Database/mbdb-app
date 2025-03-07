from invenio_records_resources.records.api import FileRecord
from invenio_records_resources.records.systemfields import IndexField

from spr.files.models import SprFileDraftMetadata, SprFileMetadata


class SprFile(FileRecord):

    model_cls = SprFileMetadata

    index = IndexField(
        "spr_file-spr_file-1.0.0",
    )
    record_cls = None  # is defined inside the parent record


class SprFileDraft(FileRecord):

    model_cls = SprFileDraftMetadata

    index = IndexField(
        "spr_file_draft-spr_file_draft-1.0.0",
    )
    record_cls = None  # is defined inside the parent record
