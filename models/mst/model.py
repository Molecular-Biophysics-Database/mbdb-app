"""
Microscale thermophoresis


"""
from __future__ import annotations

from invenio_i18n import lazy_gettext as _
from oarepo_model.presets.drafts import drafts_preset
from oarepo_model.presets.relations import relations_preset
from oarepo_model.presets.ui import ui_preset
from oarepo_model.presets.custom_fields import custom_fields_preset
from oarepo_model.api import model
from oarepo_model.customizations import AddMetadataExport
from oarepo_model.datatypes.registry import from_yaml
from oarepo_model.presets.records_resources import records_resources_preset
from oarepo_model.presets.ui_links import ui_links_preset

from .serializers import DataCiteJSONSerializer

# TODO: Consider letting users add an image/icon for the model,
# so that the deposit model selection page is more visually appealing.
mst_model = model(
    "mst",
    version="1.0.0",
    description="Microscale thermophoresis\n\n",
    presets=[
        records_resources_preset,
        # drafts_preset,
        relations_preset,
        ui_preset,
        custom_fields_preset,
        ui_links_preset,

    ],
    types=[
        from_yaml("../general_parameters-definitions.yaml", __file__),
        from_yaml("metadata.yaml", __file__),
        from_yaml("mst-definitions.yaml", __file__),
    ],
    metadata_type="Metadata",
    customizations=[
        # Add your customizations here, such as custom exports and class mixins. 
        # The list of available extensions is at https://github.com/oarepo/oarepo-model.
        # If you do not find a customization that suits your needs or need a
        # help with using customizations, please contact us at support@cesnet.cz and
        # specify the keyword "Invenio repository development" inside the subject or
        # mail body of the request.

        # export for datacite
        AddMetadataExport(
            code="datacite",
            name=_("Datacite export"),
            mimetype="application/vnd.datacite.datacite+json",
            serializer=DataCiteJSONSerializer()
        ),
    ],
    configuration={
        "ui_blueprint_name": "mst_ui"
    }
)
