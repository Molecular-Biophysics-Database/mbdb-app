from oarepo_published_service.services.config import PublishedServiceConfig
from oarepo_runtime.config.service import PermissionsPresetsConfigMixin


class MbdbBliPublishedServiceConfig(
    PublishedServiceConfig, PermissionsPresetsConfigMixin
):
    service_id = "published_mbdb_bli"
