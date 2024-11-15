from invenio_records_resources.services import FileServiceConfig
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin

from mbdb_parsing.mst import MocProcessor, XlxsProcessor


class MstFileServiceConfigWithProcessors(PermissionsPresetsConfigMixin, FileServiceConfig):
    file_processors = [
        MocProcessor(),
        XlxsProcessor(),
    ]
    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
    ]
