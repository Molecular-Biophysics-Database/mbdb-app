import json
from pathlib import Path
import inspect
from typing import Dict

from oarepo_ui.resources.components import UIResourceComponent


class MBDBEditComponent(UIResourceComponent):
    def form_config(
        self, *, form_config, **kwargs
    ):
        json_location = (
                Path(inspect.getfile(type(self.config))).parent / self.config.edit_layout
        )
        if json_location.exists():
            layout = json.loads(json_location.read_text())
            form_config['editLayout'] = layout
        

    def empty_record(self, *, resource_requestctx, empty_data: Dict, **kwargs):
        """
        Called before an empty record data are returned.

        :param resource_requestctx: invenio request context (see https://github.com/inveniosoftware/flask-resources/blob/master/flask_resources/context.py)
        :param empty_data: empty record data
        """
        empty_data.clear()
