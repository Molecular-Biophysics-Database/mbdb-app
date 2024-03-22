from oarepo_ui.resources.config import TemplatePageUIResourceConfig
from oarepo_ui.resources.resource import TemplatePageUIResource


class UnderDevelopmentPageResourceConfig(TemplatePageUIResourceConfig):
    url_prefix = "/"
    blueprint_name = "under_development"
    template_folder = "templates"
    pages = {
        "under-development": "UnderDevelopmentPage",
        # add a new page here. The key is the URL path, the value is the name of the template
        # then put <name>.jinja into the templates folder
    }


def create_blueprint(app):
    """Register blueprint for this resource."""
    return TemplatePageUIResource(UnderDevelopmentPageResourceConfig()).as_blueprint()
