from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin

from mbdb_spr.records.models import MbdbSprDraftMetadata, MbdbSprMetadata


class MbdbSprFileMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for MbdbSprFile metadata."""

    __tablename__ = "mbdb_spr_file_metadata"
    __record_model_cls__ = MbdbSprMetadata


class MbdbSprFileDraftMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for MbdbSprFileDraft metadata."""

    __tablename__ = "mbdb_spr_file_draft_metadata"
    __record_model_cls__ = MbdbSprDraftMetadata
