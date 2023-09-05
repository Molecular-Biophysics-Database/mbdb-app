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
    __tablename__ = "mbdb_mst_parent_metadata"


class MbdbMstMetadata(db.Model, RecordMetadataBase, ParentRecordMixin):
    """Model for MbdbMstRecord metadata."""

    __tablename__ = "mbdbmst_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}

    __parent_record_model__ = DraftParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class MbdbMstDraftMetadata(db.Model, DraftMetadataBase, ParentRecordMixin):
    """Model for MbdbMstDraft metadata."""

    __tablename__ = "mbdbmstdraft_metadata"

    __parent_record_model__ = DraftParentMetadata


class MbdbMstParentState(db.Model, ParentRecordStateMixin):
    table_name = "mbdbmst_parent_state_metadata"

    __parent_record_model__ = DraftParentMetadata
    __record_model__ = MbdbMstMetadata
    __draft_model__ = MbdbMstDraftMetadata
