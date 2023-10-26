from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin

from mbdb_mst.records.models import MbdbMstDraftMetadata, MbdbMstMetadata


class MbdbMstFileMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for MbdbMstFile metadata."""

    __tablename__ = "mbdb_mst_file_metadata"
    __record_model_cls__ = MbdbMstMetadata


class MbdbMstFileDraftMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for MbdbMstFileDraft metadata."""

    __tablename__ = "mbdb_mst_file_draft_metadata"
    __record_model_cls__ = MbdbMstDraftMetadata
