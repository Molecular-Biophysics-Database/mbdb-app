from bli.files.models import BliFileDraftMetadata, BliFileMetadata
from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records_resources.records.api import FileRecord
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext


class BliFileIdProvider(RecordIdProviderV2):
    pid_type = "blfl"


class BliFile(FileRecord):

    model_cls = BliFileMetadata

    index = IndexField("bli_file-bli_file-1.0.0")

    pid = PIDField(provider=BliFileIdProvider, context_cls=PIDFieldContext, create=True)
    record_cls = None  # is defined inside the parent record


class BliFileDraft(FileRecord):

    model_cls = BliFileDraftMetadata

    index = IndexField("bli_file_draft-bli_file_draft-1.0.0")

    pid = PIDField(provider=BliFileIdProvider, context_cls=PIDFieldContext, create=True)
    record_cls = None  # is defined inside the parent record
