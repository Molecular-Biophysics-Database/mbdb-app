"""Additional views."""

from flask import Blueprint, render_template

def create_blueprint(app):
    """Register blueprint routes on app."""
    blueprint = Blueprint(
        "mbdb_site",
        __name__,
        template_folder="./templates",
    )

    # default endpoint if know page is currently available 
    blueprint.add_url_rule(rule="/under-development", view_func=under_development)

    # testing instructions are temporarily placed here
    blueprint.add_url_rule(rule="/tutorial", view_func=tutorial)

    # contact information
    blueprint.add_url_rule(rule="/contact", view_func=contact_information)


    return blueprint


def under_development():
    return render_template('semantic-ui/mbdb_site/under-development.html')

def tutorial():
    return render_template('semantic-ui/mbdb_site/tutorial.html')

def contact_information():
    return render_template('semantic-ui/mbdb_site/contact-information.html')    