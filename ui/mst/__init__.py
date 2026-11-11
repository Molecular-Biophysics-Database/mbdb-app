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
from flask import g, redirect, url_for
from flask_menu import current_menu
from flask_security import login_required
from invenio_app_rdm.records_ui.views.decorators import no_cache_response
from invenio_records_resources.services.errors import PermissionDeniedError
from oarepo_ui.resources.decorators import pass_draft_community, pass_query_args
from invenio_i18n import lazy_gettext as _
from oarepo_ui.overrides import UIComponent
from oarepo_ui.overrides.components import UIComponentImportMode
from oarepo_ui.proxies import current_oarepo_ui


class MstUIResourceConfig(RecordsUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/mst"
    blueprint_name = "mst_ui"
    model_name = "mst"
    search_component = UIComponent(
        "MstResultsListItem",
        "@js/mst/search/ResultsListItem",
        UIComponentImportMode.DEFAULT
    )


    components = [
        AllowedHtmlTagsComponent,
        FilesEnabledComponent,
        BabelComponent,
        PermissionsComponent,
        FilesComponent,
    ]


    application_id = "mst"

    # rdm-12 style URLs instead of oarepo-ui's /uploads/... and /records/...
    routes = {
        "search": "",
        "deposit_create": "/new",
        "deposit_edit": "/<pid_value>/edit",
        "record_detail": "/<pid_value>",
        "record_latest": "/<pid_value>/latest",
        "record_export": "/<pid_value>/export/<export_format>",
        "published_file_preview": "/<pid_value>/files/<path:filepath>/preview",
        "draft_file_preview": "/<pid_value>/preview/files/<path:filepath>/preview",
    }


class MstUIResource(RecordsUIResource):
    @login_required
    @no_cache_response
    @pass_query_args("create")
    @pass_draft_community
    def deposit_create(self, community=None, community_ui=None, **kwargs):
        """Create an empty draft right away and redirect to its edit page,
        so the record identifier exists before the form is filled in."""
        if not self.has_deposit_permissions(g.identity):
            raise PermissionDeniedError(_("User does not have permission to create a record."))
        data = {"metadata": {}}
        if community is not None:
            data["parent"] = {"communities": {"default": {"id": community.id}}}
        draft = self.api_service.create(g.identity, data)
        return redirect(url_for(f"{self.config.blueprint_name}.deposit_edit", pid_value=draft.id))


def ui_overrides(app):
    """Register UI overrides."""
    ui_resource_config = MstUIResourceConfig()

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
    ui_resource_config = MstUIResourceConfig()

    with app.app_context():
        current_menu.submenu("plus.create_mst").register(
            f"{ui_resource_config.blueprint_name}.deposit_create",
            _("New MST"),
            order=1,
            visible_when=can_view_deposit_page,
        )

def finalize_app(app):
    """Finalize app"""
    init_menu(app)
    ui_overrides(app)

def create_blueprint(app):
    """Register blueprint for this resource."""
    blueprint = MstUIResource(MstUIResourceConfig()).as_blueprint()
    return blueprint
