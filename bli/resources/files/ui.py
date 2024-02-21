from flask import g
from flask_resources import BaseListSchema
from flask_resources.serializers import JSONSerializer
from oarepo_runtime.resources import LocalizedUIJSONSerializer

from bli.services.files.ui_schema import BliFileDraftUISchema, BliFileUISchema


class BliFileUIJSONSerializer(LocalizedUIJSONSerializer):
    """UI JSON serializer."""

    def __init__(self):
        """Initialise Serializer."""
        super().__init__(
            format_serializer_cls=JSONSerializer,
            object_schema_cls=BliFileUISchema,
            list_schema_cls=BaseListSchema,
            schema_context={"object_key": "ui", "identity": g.identity},
        )


class BliFileDraftUIJSONSerializer(LocalizedUIJSONSerializer):
    """UI JSON serializer."""

    def __init__(self):
        """Initialise Serializer."""
        super().__init__(
            format_serializer_cls=JSONSerializer,
            object_schema_cls=BliFileDraftUISchema,
            list_schema_cls=BaseListSchema,
            schema_context={"object_key": "ui", "identity": g.identity},
        )
