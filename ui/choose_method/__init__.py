"""Choose method page: the start of a new deposition."""

from __future__ import annotations

from flask import Blueprint, render_template


def choose_method():
    return render_template("choose_method/choose_method.html")


def create_blueprint(app):
    blueprint = Blueprint("choose_method", __name__, template_folder="templates/semantic-ui")
    blueprint.add_url_rule("/choose-method", view_func=choose_method)
    return blueprint
