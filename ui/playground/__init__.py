"""Developer playground (/playground): every PoC form component in isolation.

Design: conversion_docs/poc/design/Playground.md. Registered only when
MBDB_PLAYGROUND_ENABLED is true; when unset, it follows the debug flag, which
is on in the development server only.
"""

from pathlib import Path

from flask import Blueprint
from oarepo_ui.resources import TemplatePageUIResource, TemplatePageUIResourceConfig
from oarepo_ui.resources.components import UIResourceComponent

# The repository's own static folder: served by the playground blueprint at
# /playground/static/... (the instance static only holds what `invenio collect`
# copies from the packages, so files here would otherwise never be served).
STATIC_FOLDER = str(Path(__file__).resolve().parents[2] / "static")


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
    pages = {"": "mbdb_playground.Playground", "mst-mockup": "mbdb_playground.MstMockup"}
    components = (MstUiModelComponent,)


class PlaygroundUIResource(TemplatePageUIResource):
    """TemplatePageUIResource with more than one page.

    The upstream partial-based page handlers all carry the "render" name, so
    with two pages Flask would see the same endpoint twice; name the endpoints
    after the page paths instead.
    """

    def create_url_rules(self) -> list[dict]:
        """Create the url rules, with one endpoint per page."""
        rules = super().create_url_rules()
        for rule, page_path in zip(rules, self.config.pages, strict=True):
            if not rule.get("endpoint"):
                suffix = page_path.replace("-", "_").replace("/", "_") or "index"
                rule["endpoint"] = f"render_{suffix}"
        return rules

    def create_blueprint(self, **options):
        """Create the blueprint, serving the repository's static folder."""
        options.setdefault("static_folder", STATIC_FOLDER)
        return super().create_blueprint(**options)


def create_blueprint(app):
    """Register the playground blueprint (an empty one when disabled)."""
    if not app.config.get("MBDB_PLAYGROUND_ENABLED", app.debug):
        return Blueprint(
            PlaygroundUIResourceConfig.blueprint_name,
            __name__,
            static_folder=STATIC_FOLDER,
        )
    return PlaygroundUIResource(PlaygroundUIResourceConfig()).as_blueprint()
