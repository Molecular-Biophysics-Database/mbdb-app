from invenio_db import db
from invenio_drafts_resources.records import (
    DraftMetadataBase,
    ParentRecordMixin,
    ParentRecordStateMixin,
)
from invenio_files_rest.models import Bucket
from invenio_records.models import RecordMetadataBase
from sqlalchemy_utils import UUIDType


class SprParentMetadata(db.Model, RecordMetadataBase):

    __tablename__ = "spr_parent_record_metadata"


class SprMetadata(db.Model, RecordMetadataBase, ParentRecordMixin):
    """Model for SprRecord metadata."""

    __tablename__ = "spr_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}

    __parent_record_model__ = SprParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class SprDraftMetadata(db.Model, DraftMetadataBase, ParentRecordMixin):
    """Model for SprDraft metadata."""

    __tablename__ = "spr_draft_metadata"

    __parent_record_model__ = SprParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class SprParentState(db.Model, ParentRecordStateMixin):
    table_name = "spr_parent_state_metadata"

    __parent_record_model__ = SprParentMetadata
    __record_model__ = SprMetadata
    __draft_model__ = SprDraftMetadata
