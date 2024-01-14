from invenio_db import db
from invenio_drafts_resources.records import (
    DraftMetadataBase,
    ParentRecordMixin,
    ParentRecordStateMixin,
)
from invenio_files_rest.models import Bucket
from invenio_records.models import RecordMetadataBase
from sqlalchemy_utils import UUIDType


class MstParentMetadata(db.Model, RecordMetadataBase):

    __tablename__ = "mst_parent_record_metadata"


class MstMetadata(db.Model, RecordMetadataBase, ParentRecordMixin):
    """Model for MstRecord metadata."""

    __tablename__ = "mst_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}

    __parent_record_model__ = MstParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class MstDraftMetadata(db.Model, DraftMetadataBase, ParentRecordMixin):
    """Model for MstDraft metadata."""

    __tablename__ = "mst_draft_metadata"

    __parent_record_model__ = MstParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class MstParentState(db.Model, ParentRecordStateMixin):
    table_name = "mst_parent_state_metadata"

    __parent_record_model__ = MstParentMetadata
    __record_model__ = MstMetadata
    __draft_model__ = MstDraftMetadata
