from oarepo_ui.resources.config import TemplatePageUIResourceConfig
from oarepo_ui.resources.resource import TemplatePageUIResource
from invenio_records_resources.resources.records.resource import request_read_args
import marshmallow as ma
from flask_resources import resource_requestctx

class ChooseMethodPageResourceConfig(TemplatePageUIResourceConfig):
    url_prefix = "/"
    blueprint_name = "choose_method"
    template_folder = "templates"
    pages = {
        "choose-method": "ChooseMethodPage",
        # add a new page here. The key is the URL path, the value is the name of the template
        # then put <name>.jinja into the templates folder
    }
    request_read_args = {
        "community": ma.fields.String()
    }

class ChooseMethodPageResource(TemplatePageUIResource):
    @request_read_args
    def render(self, page, *args, **kwargs):
        return super().render(page, *args, community=resource_requestctx.args.get("community", ""), **kwargs)

def create_blueprint(app):
    """Register blueprint for this resource."""
    return ChooseMethodPageResource(ChooseMethodPageResourceConfig()).as_blueprint()