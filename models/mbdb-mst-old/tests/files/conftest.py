
import pytest
from invenio_records_resources.resources import FileResource

from mbdb_mst.resources.files.config import MbdbMstFileResourceConfig
from mbdb_mst.services.files.config import MbdbMstFileServiceConfig
from mbdb_mst.services.files.service import MbdbMstFileService


@pytest.fixture(scope="module")
def file_service():
    """File service shared fixture."""
    service = MbdbMstFileService(MbdbMstFileServiceConfig())
    return service


@pytest.fixture(scope="module")
def file_resource(file_service):
    """File Resources."""
    return FileResource(MbdbMstFileResourceConfig(), file_service)


@pytest.fixture(scope="module")
def headers():
    """Default headers for making requests."""
    return {
        "content-type": "application/json",
        "accept": "application/json",
    }


@pytest.fixture(scope="module")
def app_config(app_config):
    app_config["FILES_REST_STORAGE_CLASS_LIST"] = {
        "L": "Local",
        "F": "Fetch",
        "R": "Remote",
    }
    app_config["FILES_REST_DEFAULT_STORAGE_CLASS"] = "L"

    return app_config
