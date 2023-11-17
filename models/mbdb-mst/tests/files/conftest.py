
import pytest
from invenio_records_resources.resources import FileResource

from mbdb_mst.resources.files.config import MbdbMstFileResourceConfig
from mbdb_mst.services.files.config import MbdbMstFileServiceConfig
from mbdb_mst.services.files.service import MbdbMstFileService


@pytest.fixture()
def input_data(input_data):
    input_data["files"] = {"enabled": True}
    return input_data


@pytest.fixture(scope="module")
def file_service():
    """File service shared fixture."""
    service = MbdbMstFileService(MbdbMstFileServiceConfig())
    return service


@pytest.fixture(scope="module")
def file_resource(file_service):
    """File Resources."""
    return FileResource(MbdbMstFileResourceConfig(), file_service)
