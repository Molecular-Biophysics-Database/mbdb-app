from invenio_communities.records.records.models import CommunityRelationMixin
from invenio_db import db
from invenio_drafts_resources.records import (
    DraftMetadataBase,
    ParentRecordMixin,
    ParentRecordStateMixin,
)
from invenio_files_rest.models import Bucket
from invenio_records.models import RecordMetadataBase
from oarepo_workflows.records.models import RecordWorkflowParentModelMixin
from sqlalchemy_utils import UUIDType


class ItcParentMetadata(RecordWorkflowParentModelMixin, db.Model, RecordMetadataBase):

    __tablename__ = "itc_parent_record_metadata"


class ItcMetadata(db.Model, RecordMetadataBase, ParentRecordMixin):
    """Model for ItcRecord metadata."""

    __tablename__ = "itc_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}

    __parent_record_model__ = ItcParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class ItcDraftMetadata(db.Model, DraftMetadataBase, ParentRecordMixin):
    """Model for ItcDraft metadata."""

    __tablename__ = "itc_draft_metadata"

    __parent_record_model__ = ItcParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class ItcCommunitiesMetadata(db.Model, CommunityRelationMixin):
    __tablename__ = "itc_communities_metadata"
    __record_model__ = ItcParentMetadata


class ItcParentState(db.Model, ParentRecordStateMixin):
    table_name = "itc_parent_state_metadata"

    __parent_record_model__ = ItcParentMetadata
    __record_model__ = ItcMetadata
    __draft_model__ = ItcDraftMetadata
