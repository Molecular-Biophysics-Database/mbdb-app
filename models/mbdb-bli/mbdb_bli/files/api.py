from invenio_drafts_resources.records.api import ParentRecord
from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records_resources.records.api import FileRecord
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext

from mbdb_bli.files.models import DraftParentMetadata, MbdbBliFileMetadata
from mbdb_bli.records.models import MbdbBliParentState


class DraftParentRecord(ParentRecord):
    model_cls = DraftParentMetadata

    # schema = ConstantField(
    #    "$schema", "local://parent-v1.0.0.json"
    # )


class MbdbBliFileIdProvider(RecordIdProviderV2):
    pid_type = "blfl"


class MbdbBliFile(FileRecord):
    model_cls = MbdbBliFileMetadata

    index = IndexField("mbdb_bli_file-mbdb_bli_file-1.0.0")

    pid = PIDField(
        provider=MbdbBliFileIdProvider, context_cls=PIDFieldContext, create=True
    )
    dumper_extensions = []
    record_cls = None  # is defined inside the parent record

    versions_model_cls = MbdbBliParentState

    parent_record_cls = DraftParentRecord
