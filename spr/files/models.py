from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin
from spr.records.models import SprDraftMetadata, SprMetadata


class SprFileMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for SprFile metadata."""

    __tablename__ = "spr_file_metadata"
    __record_model_cls__ = SprMetadata


class SprFileDraftMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for SprFileDraft metadata."""

    __tablename__ = "spr_file_draft_metadata"
    __record_model_cls__ = SprDraftMetadata
