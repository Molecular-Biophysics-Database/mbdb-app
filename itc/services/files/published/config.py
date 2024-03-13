from itc.services.files.config import ItcFileServiceConfig


class ItcFilePublishedServiceConfig(ItcFileServiceConfig):
    service_id = "published_itc_file"

    @property
    def components(self):
        return [*super().components]
