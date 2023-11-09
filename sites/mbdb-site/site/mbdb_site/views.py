"""Additional views."""

from flask import Blueprint
from flask import render_template

def create_blueprint(app):
    """Register blueprint routes on app."""
    blueprint = Blueprint(
        "mbdb_site",
        __name__,
        template_folder="./templates",
    )

    @blueprint.route('/templates/mbdb_site/under-development.html')
    def new_page():
        return render_template('under-development.html')

    return blueprint
