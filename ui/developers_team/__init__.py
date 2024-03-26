from oarepo_ui.resources.config import TemplatePageUIResourceConfig
from oarepo_ui.resources.resource import TemplatePageUIResource


class DevelopersTeamPageResourceConfig(TemplatePageUIResourceConfig):
    url_prefix = "/"
    blueprint_name = "developers_team"
    template_folder = "templates"
    pages = {
        "developers-team": "DevelopersTeamPage", 
        # add a new page here. The key is the URL path, the value is the name of the template
        # then put <name>.jinja into the templates folder
    }


def create_blueprint(app):
    """Register blueprint for this resource."""
    return TemplatePageUIResource(DevelopersTeamPageResourceConfig()).as_blueprint()