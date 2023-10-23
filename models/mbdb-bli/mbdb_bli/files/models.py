from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin

from mbdb_bli.records.models import MbdbBliDraftMetadata, MbdbBliMetadata


class MbdbBliFileMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for MbdbBliFile metadata."""

    __tablename__ = "mbdb_bli_file_metadata"
    __record_model_cls__ = MbdbBliMetadata


class MbdbBliFileDraftMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for MbdbBliFileDraft metadata."""

    __tablename__ = "mbdb_bli_file_draft_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}
    __record_model_cls__ = MbdbBliDraftMetadata
