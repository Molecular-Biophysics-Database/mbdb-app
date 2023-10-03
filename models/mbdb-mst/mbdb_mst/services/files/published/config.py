from oarepo_published_service.services.config import (
    PublishedServiceConfig as PublishedServiceConfig,
)
from oarepo_runtime.config.service import PermissionsPresetsConfigMixin


class MbdbMstFilePublishedServiceConfig(
    PublishedServiceConfig, PermissionsPresetsConfigMixin
):
    service_id = "published_mbdb_mst_file"
