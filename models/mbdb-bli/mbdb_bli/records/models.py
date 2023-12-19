from invenio_db import db
from invenio_drafts_resources.records import (
    DraftMetadataBase,
    ParentRecordMixin,
    ParentRecordStateMixin,
)
from invenio_files_rest.models import Bucket
from invenio_records.models import RecordMetadataBase
from sqlalchemy_utils import UUIDType


class MbdbBliParentMetadata(db.Model, RecordMetadataBase):

    __tablename__ = "mbdb_bli_parent_record_metadata"


class MbdbBliMetadata(db.Model, RecordMetadataBase, ParentRecordMixin):
    """Model for MbdbBliRecord metadata."""

    __tablename__ = "mbdb_bli_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}

    __parent_record_model__ = MbdbBliParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class MbdbBliDraftMetadata(db.Model, DraftMetadataBase, ParentRecordMixin):
    """Model for MbdbBliDraft metadata."""

    __tablename__ = "mbdb_bli_draft_metadata"

    __parent_record_model__ = MbdbBliParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class MbdbBliParentState(db.Model, ParentRecordStateMixin):
    table_name = "mbdb_bli_parent_state_metadata"

    __parent_record_model__ = MbdbBliParentMetadata
    __record_model__ = MbdbBliMetadata
    __draft_model__ = MbdbBliDraftMetadata
