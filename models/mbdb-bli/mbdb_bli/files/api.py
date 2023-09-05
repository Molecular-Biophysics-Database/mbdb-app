from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records_resources.records.api import FileRecord
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext

from mbdb_bli.files.models import MbdbBliFileMetadata


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
