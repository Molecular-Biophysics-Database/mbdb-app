"""Developer playground (/playground): every PoC form component in isolation.

Design: conversion_docs/poc/design/Playground.md. Registered only when
MBDB_PLAYGROUND_ENABLED is true; when unset, it follows the debug flag, which
is on in the development server only.
"""

from flask import Blueprint
from oarepo_ui.resources import TemplatePageUIResource, TemplatePageUIResourceConfig
from oarepo_ui.resources.components import UIResourceComponent


class MstUiModelComponent(UIResourceComponent):
    """Pass the mst ui_model to the page, so fields get the model labels and help."""

    def before_render(self, *, extra_context, **kwargs):
        from ui.mst import MstUIResourceConfig

        extra_context["ui_model"] = MstUIResourceConfig().model.ui_model


class PlaygroundUIResourceConfig(TemplatePageUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/playground"
    blueprint_name = "playground_ui"
    application_id = "playground"
    pages = {"": "mbdb_playground.Playground"}
    components = (MstUiModelComponent,)


def create_blueprint(app):
    """Register the playground blueprint (an empty one when disabled)."""
    if not app.config.get("MBDB_PLAYGROUND_ENABLED", app.debug):
        return Blueprint(PlaygroundUIResourceConfig.blueprint_name, __name__)
    return TemplatePageUIResource(PlaygroundUIResourceConfig()).as_blueprint()
