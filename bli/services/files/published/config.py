from bli.services.files.config import BliFileServiceConfig


class BliFilePublishedServiceConfig(BliFileServiceConfig):
    service_id = "published_bli_file"

    @property
    def components(self):
        return [*super().components]
