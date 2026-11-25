"""Advanced search page: builds a field query and opens the search with it."""

from __future__ import annotations

from flask import Blueprint, render_template

from .fields import FIELDS


def advanced_search():
    return render_template("advanced_search/advanced_search.html", fields=FIELDS)


def create_blueprint(app):
    blueprint = Blueprint("advanced_search", __name__, template_folder="templates/semantic-ui")
    blueprint.add_url_rule("/advanced-search", view_func=advanced_search)
    return blueprint
