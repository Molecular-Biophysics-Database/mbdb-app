from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records_resources.records.api import FileRecord
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from spr.files.models import SprFileDraftMetadata, SprFileMetadata


class SprFileIdProvider(RecordIdProviderV2):
    pid_type = "sprfl"


class SprFile(FileRecord):

    model_cls = SprFileMetadata

    index = IndexField("spr_file-spr_file-1.0.0")

    pid = PIDField(provider=SprFileIdProvider, context_cls=PIDFieldContext, create=True)
    record_cls = None  # is defined inside the parent record


class SprFileDraft(FileRecord):

    model_cls = SprFileDraftMetadata

    index = IndexField("spr_file_draft-spr_file_draft-1.0.0")

    pid = PIDField(provider=SprFileIdProvider, context_cls=PIDFieldContext, create=True)
    record_cls = None  # is defined inside the parent record
