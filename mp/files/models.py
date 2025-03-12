from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin

from mp.records.models import MpDraftMetadata, MpMetadata


class MpFileMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for MpFile metadata."""

    __tablename__ = "mp_file_metadata"
    __record_model_cls__ = MpMetadata


class MpFileDraftMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for MpFileDraft metadata."""

    __tablename__ = "mp_file_draft_metadata"
    __record_model_cls__ = MpDraftMetadata
