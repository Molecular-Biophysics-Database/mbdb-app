from invenio_db import db
from invenio_files_rest.models import Bucket
from invenio_records.models import RecordMetadataBase
from sqlalchemy_utils import UUIDType


class MbdbBliMetadata(db.Model, RecordMetadataBase):
    """Model for MbdbBliRecord metadata."""

    __tablename__ = "mbdbbli_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)
