from invenio_records_resources.services import FileServiceConfig
from invenio_records_resources.services.files.components.metadata import FileMetadataComponent
from invenio_records_resources.services.files.components.content import FileContentComponent

from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin

from common.services.files.synchronous_file_processing import SynchronousFileProcessorComponent

class BaseFileServiceConfigWithProcessors(PermissionsPresetsConfigMixin, FileServiceConfig):
    components = [
        *PermissionsPresetsConfigMixin.components,
        FileMetadataComponent,
        FileContentComponent,
        SynchronousFileProcessorComponent,
    ]
