from flask import Blueprint

templates_blueprint = Blueprint("mbdb_templates",
                                __name__,
                                template_folder="templates")
