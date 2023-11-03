import json
from pathlib import Path
from invenio_records_resources.services.records.components import ServiceComponent
import inspect
from invenio_records_resources.proxies import current_service_registry


class MBDBEditComponent(ServiceComponent):
    def form_config(
        self, *, form_config, resource, record,
            view_args, identity, **kwargs
    ):
        json_location = (
                Path(inspect.getfile(type(resource.config))).parent / resource.config.edit_layout
        )
        if json_location.exists():
            layout = json.loads(json_location.read_text())
            form_config['editLayout'] = layout
    def before_ui_edit(
        self, *, record, resource, extra_context, identity, **kwargs
    ):
        file_service = current_service_registry.get("mbdb_mst_file_draft")
        files = file_service.list_files(identity, record['id'])
        extra_context["files"] = files.to_dict()
        
