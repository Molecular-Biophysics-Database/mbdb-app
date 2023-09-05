from invenio_db import db
from invenio_drafts_resources.records import (
    DraftMetadataBase,
    ParentRecordMixin,
    ParentRecordStateMixin,
)
from invenio_files_rest.models import Bucket
from invenio_records.models import RecordMetadataBase
from sqlalchemy_utils import UUIDType


class DraftParentMetadata(db.Model, RecordMetadataBase):
    __tablename__ = "mbdb_bli_parent_metadata"


class MbdbBliMetadata(db.Model, RecordMetadataBase, ParentRecordMixin):
    """Model for MbdbBliRecord metadata."""

    __tablename__ = "mbdbbli_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}

    __parent_record_model__ = DraftParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class MbdbBliDraftMetadata(db.Model, DraftMetadataBase, ParentRecordMixin):
    """Model for MbdbBliDraft metadata."""

    __tablename__ = "mbdbblidraft_metadata"

    __parent_record_model__ = DraftParentMetadata


class ParentState(db.Model, ParentRecordStateMixin):
    table_name = "mbdbbli_parent_state_metadata"

    __parent_record_model__ = DraftParentMetadata
    __record_model__ = MbdbBliMetadata
    __draft_model__ = MbdbBliDraftMetadata
