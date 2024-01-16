from invenio_db import db
from invenio_drafts_resources.records import (
    DraftMetadataBase,
    ParentRecordMixin,
    ParentRecordStateMixin,
)
from invenio_files_rest.models import Bucket
from invenio_records.models import RecordMetadataBase
from sqlalchemy_utils import UUIDType


class BliParentMetadata(db.Model, RecordMetadataBase):

    __tablename__ = "bli_parent_record_metadata"


class BliMetadata(db.Model, RecordMetadataBase, ParentRecordMixin):
    """Model for BliRecord metadata."""

    __tablename__ = "bli_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}

    __parent_record_model__ = BliParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class BliDraftMetadata(db.Model, DraftMetadataBase, ParentRecordMixin):
    """Model for BliDraft metadata."""

    __tablename__ = "bli_draft_metadata"

    __parent_record_model__ = BliParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class BliParentState(db.Model, ParentRecordStateMixin):
    table_name = "bli_parent_state_metadata"

    __parent_record_model__ = BliParentMetadata
    __record_model__ = BliMetadata
    __draft_model__ = BliDraftMetadata
