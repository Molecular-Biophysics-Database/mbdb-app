from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records_resources.records.api import FileRecord
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext

from mst.files.models import MstFileDraftMetadata, MstFileMetadata


class MstFileIdProvider(RecordIdProviderV2):
    pid_type = "mstfl"


class MstFile(FileRecord):

    model_cls = MstFileMetadata

    index = IndexField("mst_file-mst_file-1.0.0")

    pid = PIDField(provider=MstFileIdProvider, context_cls=PIDFieldContext, create=True)
    record_cls = None  # is defined inside the parent record


class MstFileDraft(FileRecord):

    model_cls = MstFileDraftMetadata

    index = IndexField("mst_file_draft-mst_file_draft-1.0.0")

    pid = PIDField(provider=MstFileIdProvider, context_cls=PIDFieldContext, create=True)
    record_cls = None  # is defined inside the parent record
