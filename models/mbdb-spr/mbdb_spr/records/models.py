from invenio_db import db
from invenio_files_rest.models import Bucket
from invenio_records.models import RecordMetadataBase
from sqlalchemy_utils import UUIDType


class MbdbSprMetadata(db.Model, RecordMetadataBase):
    """Model for MbdbSprRecord metadata."""

    __tablename__ = "mbdbspr_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)
