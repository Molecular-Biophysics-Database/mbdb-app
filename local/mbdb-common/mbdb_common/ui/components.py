import json
from pathlib import Path
import inspect
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
        
