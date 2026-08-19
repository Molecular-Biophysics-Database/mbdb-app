from oarepo_ui.resources import BabelComponent
from oarepo_ui.resources.components import (
    AllowedHtmlTagsComponent,
    FilesComponent,
    PermissionsComponent,

)

from oarepo_rdm.ui.components import FilesEnabledComponent

from oarepo_ui.resources.records.config import RecordsUIResourceConfig
from oarepo_ui.resources.records.resource import RecordsUIResource
from oarepo_ui.utils import can_view_deposit_page
from flask_menu import current_menu
from invenio_i18n import lazy_gettext as _
from oarepo_ui.overrides import UIComponent
from oarepo_ui.overrides.components import UIComponentImportMode
from oarepo_ui.proxies import current_oarepo_ui


class SprUIResourceConfig(RecordsUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/spr"
    blueprint_name = "spr_ui"
    model_name = "spr"
    search_component = UIComponent(
        "SprResultsListItem",
        "@js/spr/search/ResultsListItem",
        UIComponentImportMode.DEFAULT
    )


    components = [
        AllowedHtmlTagsComponent,
        FilesEnabledComponent,
        BabelComponent,
        PermissionsComponent,
        FilesComponent,
    ]


    application_id = "spr"


class SprUIResource(RecordsUIResource):
    pass

def ui_overrides(app):
    """Register UI overrides."""
    ui_resource_config = SprUIResourceConfig()

    if (
        current_oarepo_ui is not None
        and ui_resource_config.model
        and ui_resource_config.model.record_json_schema
        and ui_resource_config.search_component
    ):
        current_oarepo_ui.register_result_list_item(
            ui_resource_config.model.record_json_schema, ui_resource_config.search_component
        )


def init_menu(app):
    """Initialize menu before first request."""
    ui_resource_config = SprUIResourceConfig()

    with app.app_context():
        current_menu.submenu("plus.create_spr").register(
            f"{ui_resource_config.blueprint_name}.deposit_create",
            _("New spr"),
            order=1,
            visible_when=can_view_deposit_page,
        )

def finalize_app(app):
    """Finalize app"""
    init_menu(app)
    ui_overrides(app)

def create_blueprint(app):
    """Register blueprint for this resource."""
    blueprint = SprUIResource(SprUIResourceConfig()).as_blueprint()
    return blueprint
