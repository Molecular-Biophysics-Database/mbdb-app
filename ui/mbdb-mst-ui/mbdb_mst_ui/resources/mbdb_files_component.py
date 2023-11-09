import json
from pathlib import Path
from invenio_records_resources.services.records.components import ServiceComponent
import inspect
from invenio_records_resources.proxies import current_service_registry


class MBDBFilesComponent(ServiceComponent):
    def before_ui_edit(
        self, *, record, resource, extra_context, identity, **kwargs
    ):
        file_service = current_service_registry.get("mbdb_mst_file_draft")
        files = file_service.list_files(identity, record['id'])
        extra_context["files"] = files.to_dict()

    def before_ui_detail(
        self, **kwargs
    ):
        self.before_ui_edit(**kwargs)