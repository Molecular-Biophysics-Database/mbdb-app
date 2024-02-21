from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin

from bli.records.models import BliDraftMetadata, BliMetadata


class BliFileMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for BliFile metadata."""

    __tablename__ = "bli_file_metadata"
    __record_model_cls__ = BliMetadata


class BliFileDraftMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for BliFileDraft metadata."""

    __tablename__ = "bli_file_draft_metadata"
    __record_model_cls__ = BliDraftMetadata
