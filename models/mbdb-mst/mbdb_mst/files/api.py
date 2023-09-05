from invenio_drafts_resources.records.api import ParentRecord
from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records_resources.records.api import FileRecord
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext

from mbdb_mst.files.models import DraftParentMetadata, MbdbMstFileMetadata, ParentState


class DraftParentRecord(ParentRecord):
    model_cls = DraftParentMetadata

    # schema = ConstantField(
    #    "$schema", "local://parent-v1.0.0.json"
    # )


class MbdbMstFileIdProvider(RecordIdProviderV2):
    pid_type = "mstfl"


class MbdbMstFile(FileRecord):
    model_cls = MbdbMstFileMetadata

    index = IndexField("mbdb_mst_file-mbdb_mst_file-1.0.0")

    pid = PIDField(
        provider=MbdbMstFileIdProvider, context_cls=PIDFieldContext, create=True
    )
    dumper_extensions = []
    record_cls = None  # is defined inside the parent record

    versions_model_cls = ParentState

    parent_record_cls = DraftParentRecord
