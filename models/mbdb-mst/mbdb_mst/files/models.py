from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin

from mbdb_mst.records.models import MbdbMstMetadata


class MbdbMstFileMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for MbdbMstFile metadata."""

    __tablename__ = "mbdbmstfile_metadata"
    __record_model_cls__ = MbdbMstMetadata
