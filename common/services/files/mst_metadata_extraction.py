from common.services.files.base_extractor import BaseFileServiceConfigWithProcessors
from mbdb_parsing.mst import MocProcessor, XlxsProcessor

class MstFileServiceConfigWithProcessors(BaseFileServiceConfigWithProcessors):
    components = []
    synchronous_file_processors = [
        MocProcessor(),
        XlxsProcessor(),
    ]
