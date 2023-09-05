from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin

from mbdb_bli.records.models import MbdbBliMetadata


class MbdbBliFileMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for MbdbBliFile metadata."""

    __tablename__ = "mbdbblifile_metadata"
    __record_model_cls__ = MbdbBliMetadata
