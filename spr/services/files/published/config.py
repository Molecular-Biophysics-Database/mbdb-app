from spr.services.files.config import SprFileServiceConfig


class SprFilePublishedServiceConfig(SprFileServiceConfig):
    service_id = "published_spr_file"

    @property
    def components(self):
        return [*super().components]
