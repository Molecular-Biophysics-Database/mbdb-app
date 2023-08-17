
import pytest
from invenio_records_resources.resources import FileResource

from mbdb_spr.resources.files.config import MbdbSprFileResourceConfig
from mbdb_spr.services.files.config import MbdbSprFileServiceConfig
from mbdb_spr.services.files.service import MbdbSprFileService


@pytest.fixture(scope="module")
def file_service():
    """File service shared fixture."""
    service = MbdbSprFileService(MbdbSprFileServiceConfig())
    return service


@pytest.fixture(scope="module")
def file_resource(file_service):
    """File Resources."""
    return FileResource(MbdbSprFileResourceConfig(), file_service)


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
