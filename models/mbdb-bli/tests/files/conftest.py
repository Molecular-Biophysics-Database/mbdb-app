
import pytest
from invenio_records_resources.resources import FileResource

from mbdb_bli.resources.files.config import MbdbBliFileResourceConfig
from mbdb_bli.services.files.config import MbdbBliFileServiceConfig
from mbdb_bli.services.files.service import MbdbBliFileService


@pytest.fixture()
def input_data(input_data):
    input_data["files"] = {"enabled": True}
    return input_data


@pytest.fixture(scope="module")
def file_service():
    """File service shared fixture."""
    service = MbdbBliFileService(MbdbBliFileServiceConfig())
    return service


@pytest.fixture(scope="module")
def file_resource(file_service):
    """File Resources."""
    return FileResource(MbdbBliFileResourceConfig(), file_service)
