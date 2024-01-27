from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin
from mst.records.models import MstDraftMetadata, MstMetadata


class MstFileMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for MstFile metadata."""

    __tablename__ = "mst_file_metadata"
    __record_model_cls__ = MstMetadata


class MstFileDraftMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for MstFileDraft metadata."""

    __tablename__ = "mst_file_draft_metadata"
    __record_model_cls__ = MstDraftMetadata
