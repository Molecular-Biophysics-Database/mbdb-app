from invenio_drafts_resources.records.api import ParentRecord
from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records_resources.records.api import FileRecord
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext

from mbdb_spr.files.models import DraftParentMetadata, MbdbSprFileMetadata, ParentState


class DraftParentRecord(ParentRecord):
    model_cls = DraftParentMetadata

    # schema = ConstantField(
    #    "$schema", "local://parent-v1.0.0.json"
    # )


class MbdbSprFileIdProvider(RecordIdProviderV2):
    pid_type = "sprfl"


class MbdbSprFile(FileRecord):
    model_cls = MbdbSprFileMetadata

    index = IndexField("mbdb_spr_file-mbdb_spr_file-1.0.0")

    pid = PIDField(
        provider=MbdbSprFileIdProvider, context_cls=PIDFieldContext, create=True
    )
    dumper_extensions = []
    record_cls = None  # is defined inside the parent record

    versions_model_cls = ParentState

    parent_record_cls = DraftParentRecord
