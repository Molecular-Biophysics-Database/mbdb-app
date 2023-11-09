"""Additional views."""

from flask import Blueprint, render_template

def create_blueprint(app):
    """Register blueprint routes on app."""
    blueprint = Blueprint(
        "mbdb_site",
        __name__,
        template_folder="./templates",
    )

    blueprint.add_url_rule(**{"rule": "/under-development", "view_func": under_development})

    return blueprint


def under_development():
    return render_template('semantic-ui/mbdb_site/under-development.html')