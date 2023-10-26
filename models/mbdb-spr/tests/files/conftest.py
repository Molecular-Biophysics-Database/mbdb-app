
import pytest
from invenio_records_resources.resources import FileResource

from mbdb_spr.resources.files.config import MbdbSprFileResourceConfig
from mbdb_spr.services.files.config import MbdbSprFileServiceConfig
from mbdb_spr.services.files.service import MbdbSprFileService


@pytest.fixture()
def input_data(input_data):
    input_data["files"] = {"enabled": True}
    return input_data


@pytest.fixture(scope="module")
def file_service():
    """File service shared fixture."""
    service = MbdbSprFileService(MbdbSprFileServiceConfig())
    return service


@pytest.fixture(scope="module")
def file_resource(file_service):
    """File Resources."""
    return FileResource(MbdbSprFileResourceConfig(), file_service)
