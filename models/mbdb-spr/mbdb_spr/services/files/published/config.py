from oarepo_published_service.services.config import PublishedServiceConfig
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin


class MbdbSprFilePublishedServiceConfig(
    PublishedServiceConfig, PermissionsPresetsConfigMixin
):
    service_id = "published_mbdb_spr_file"
