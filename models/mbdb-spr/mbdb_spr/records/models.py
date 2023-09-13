from invenio_db import db
from invenio_drafts_resources.records import (
    DraftMetadataBase,
    ParentRecordMixin,
    ParentRecordStateMixin,
)
from invenio_files_rest.models import Bucket
from invenio_records.models import RecordMetadataBase
from sqlalchemy_utils import UUIDType


class MbdbSprParentMetadata(db.Model, RecordMetadataBase):
    __tablename__ = "mbdb_spr_parent_record_metadata"


class MbdbSprMetadata(db.Model, RecordMetadataBase, ParentRecordMixin):
    """Model for MbdbSprRecord metadata."""

    __tablename__ = "mbdb_spr_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}

    __parent_record_model__ = MbdbSprParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class MbdbSprDraftMetadata(db.Model, DraftMetadataBase, ParentRecordMixin):
    """Model for MbdbSprDraft metadata."""

    __tablename__ = "mbdb_spr_draft_metadata"

    __parent_record_model__ = MbdbSprParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class MbdbSprParentState(db.Model, ParentRecordStateMixin):
    table_name = "mbdb_spr_parent_state_metadata"

    __parent_record_model__ = MbdbSprParentMetadata
    __record_model__ = MbdbSprMetadata
    __draft_model__ = MbdbSprDraftMetadata
