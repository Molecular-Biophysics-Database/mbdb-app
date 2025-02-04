from invenio_records_resources.records.api import FileRecord
from invenio_records_resources.records.systemfields import IndexField

from mst.files.models import MstFileDraftMetadata, MstFileMetadata


class MstFile(FileRecord):

    model_cls = MstFileMetadata

    index = IndexField("mst_file-mst_file-1.0.0", search_alias="mst_file")
    record_cls = None  # is defined inside the parent record


class MstFileDraft(FileRecord):

    model_cls = MstFileDraftMetadata

    index = IndexField(
        "mst_file_draft-mst_file_draft-1.0.0", search_alias="mst_file_draft"
    )
    record_cls = None  # is defined inside the parent record
