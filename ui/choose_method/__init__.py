from oarepo_ui.resources.config import TemplatePageUIResourceConfig
from oarepo_ui.resources.resource import TemplatePageUIResource


class ChooseMethodPageResourceConfig(TemplatePageUIResourceConfig):
    url_prefix = "/"
    blueprint_name = "choose_method"
    template_folder = "templates"
    pages = {
        "choose-method": "ChooseMethodPage",
        # add a new page here. The key is the URL path, the value is the name of the template
        # then put <name>.jinja into the templates folder
    }


def create_blueprint(app):
    """Register blueprint for this resource."""
    return TemplatePageUIResource(ChooseMethodPageResourceConfig()).as_blueprint()