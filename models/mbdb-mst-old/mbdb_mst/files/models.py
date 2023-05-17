from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin

from mbdb_mst.records.models import MbdbMstMetadata


class MbdbMstFileMetadata(db.Model, FileRecordModelMixin, RecordMetadataBase):
    """Model for MbdbMstFile metadata."""

    __tablename__ = "mbdbmstfile_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}
    __record_model_cls__ = MbdbMstMetadata
