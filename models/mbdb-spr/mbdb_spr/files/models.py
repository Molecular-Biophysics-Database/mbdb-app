from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin

from mbdb_spr.records.models import MbdbSprMetadata


class MbdbSprFileMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for MbdbSprFile metadata."""

    __tablename__ = "mbdbsprfile_metadata"
    __record_model_cls__ = MbdbSprMetadata
