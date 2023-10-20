from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records_resources.records.api import FileRecord
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext

from mbdb_mst.files.models import MbdbMstFileDraftMetadata, MbdbMstFileMetadata


class MbdbMstFileIdProvider(RecordIdProviderV2):
    pid_type = "mstfl"


class MbdbMstFile(FileRecord):
    model_cls = MbdbMstFileMetadata

    index = IndexField("mbdb_mst_file-mbdb_mst_file-1.0.0")

    pid = PIDField(
        provider=MbdbMstFileIdProvider, context_cls=PIDFieldContext, create=True
    )
    record_cls = None  # is defined inside the parent record


class MbdbMstFileDraft(FileRecord):
    model_cls = MbdbMstFileDraftMetadata

    index = IndexField("mbdb_mst_file_draft-mbdb_mst_file_draft-1.0.0")

    pid = PIDField(
        provider=MbdbMstFileIdProvider, context_cls=PIDFieldContext, create=True
    )
    record_cls = None  # is defined inside the parent record
