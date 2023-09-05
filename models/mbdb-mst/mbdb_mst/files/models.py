from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin

from mbdb_mst.records.models import MbdbMstMetadata


class DraftParentMetadata(db.Model, RecordMetadataBase):
    __tablename__ = "mbdb_mst_file_parent_metadata"


class MbdbMstFileMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for MbdbMstFile metadata."""

    __tablename__ = "mbdbmstfile_metadata"
    __record_model_cls__ = MbdbMstMetadata

    __parent_record_model__ = DraftParentMetadata
