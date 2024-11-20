from invenio_records_resources.services import FileServiceConfig
from invenio_records_resources.services.files.components.metadata import FileMetadataComponent
from invenio_records_resources.services.files.components.content import FileContentComponent

from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin

from mbdb_parsing.mst import MocProcessor, XlxsProcessor
from common.services.files.synchronous_file_processing import SynchronousFileProcessorComponent

class MstFileServiceConfigWithProcessors(PermissionsPresetsConfigMixin, FileServiceConfig):
    file_processors = [
        MocProcessor(),
        XlxsProcessor(),
    ]
    components = [
        *PermissionsPresetsConfigMixin.components,
        FileMetadataComponent,
        FileContentComponent,
        SynchronousFileProcessorComponent,
    ]
