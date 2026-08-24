from invenio_access.permissions import system_identity
from oarepo_runtime import current_runtime
import json
import sys

mst_service = current_runtime.models["mst"].service
print(sys.argv)
j = json.load(open(sys.argv[1]))
result = mst_service.create(system_identity, j)
print(result.data)