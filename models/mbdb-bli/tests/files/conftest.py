
import pytest
from invenio_records_resources.resources import FileResource

from mbdb_bli.resources.files.config import MbdbBliFileResourceConfig
from mbdb_bli.services.files.config import MbdbBliFileServiceConfig
from mbdb_bli.services.files.service import MbdbBliFileService


@pytest.fixture(scope="module")
def file_service():
    """File service shared fixture."""
    service = MbdbBliFileService(MbdbBliFileServiceConfig())
    return service


@pytest.fixture(scope="module")
def file_resource(file_service):
    """File Resources."""
    return FileResource(MbdbBliFileResourceConfig(), file_service)


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
