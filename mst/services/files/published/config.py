from mst.services.files.config import MstFileServiceConfig


class MstFilePublishedServiceConfig(MstFileServiceConfig):
    service_id = "published_mst_file"

    @property
    def components(self):
        return [*super().components]
