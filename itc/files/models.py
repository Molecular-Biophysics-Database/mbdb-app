from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin

from itc.records.models import ItcDraftMetadata, ItcMetadata


class ItcFileMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for ItcFile metadata."""

    __tablename__ = "itc_file_metadata"
    __record_model_cls__ = ItcMetadata


class ItcFileDraftMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for ItcFileDraft metadata."""

    __tablename__ = "itc_file_draft_metadata"
    __record_model_cls__ = ItcDraftMetadata
