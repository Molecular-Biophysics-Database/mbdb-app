from flask_resources import BaseListSchema
from flask_resources.serializers import JSONSerializer
from oarepo_runtime.resources import LocalizedUIJSONSerializer

from mbdb_bli.services.files.ui_schema import (
    MbdbBliFileDraftUISchema,
    MbdbBliFileUISchema,
)


class MbdbBliFileUIJSONSerializer(LocalizedUIJSONSerializer):
    """UI JSON serializer."""

    def __init__(self):
        """Initialise Serializer."""
        super().__init__(
            format_serializer_cls=JSONSerializer,
            object_schema_cls=MbdbBliFileUISchema,
            list_schema_cls=BaseListSchema,
            schema_context={"object_key": "ui"},
        )


class MbdbBliFileDraftUIJSONSerializer(LocalizedUIJSONSerializer):
    """UI JSON serializer."""

    def __init__(self):
        """Initialise Serializer."""
        super().__init__(
            format_serializer_cls=JSONSerializer,
            object_schema_cls=MbdbBliFileDraftUISchema,
            list_schema_cls=BaseListSchema,
            schema_context={"object_key": "ui"},
        )
