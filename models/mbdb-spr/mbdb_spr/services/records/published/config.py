from oarepo_published_service.services.config import PublishedServiceConfig
from oarepo_runtime.config.service import PermissionsPresetsConfigMixin


class MbdbSprPublishedServiceConfig(
    PublishedServiceConfig, PermissionsPresetsConfigMixin
):
    service_id = "published_mbdb_spr"
