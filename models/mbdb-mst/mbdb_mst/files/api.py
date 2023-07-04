from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records_resources.records.api import FileRecord
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext

from mbdb_mst.files.models import MbdbMstFileMetadata


class MbdbMstFileIdProvider(RecordIdProviderV2):
    pid_type = "mstfl"


class MbdbMstFile(FileRecord):
    model_cls = MbdbMstFileMetadata

    pid = PIDField(
        provider=MbdbMstFileIdProvider, context_cls=PIDFieldContext, create=True
    )
    dumper_extensions = []
    record_cls = None  # is defined inside the parent record
