from pathlib import Path

from flask import Blueprint, redirect


def create_blueprint(app):
    """Register blueprint for this resource."""
    template_folder = Path(__file__).parent.joinpath("templates").resolve()

    # TODO: Hacky solution to avoid error in invenio-communities where link is hardcoded
    # they promised to correct this soon
    app.add_url_rule(
        "/fake-link",
        endpoint="invenio_app_rdm_users.communities",
        view_func=lambda: redirect("/me/communities/"),
    )

    return Blueprint(
        "components",
        __name__,
        url_prefix="/",
        template_folder=str(template_folder),
    )
