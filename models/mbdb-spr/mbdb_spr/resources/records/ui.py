from flask_resources import BaseListSchema, MarshmallowSerializer
from flask_resources.serializers import JSONSerializer

from mbdb_spr.services.records.ui_schema import MbdbSprUISchema


class MbdbSprUIJSONSerializer(MarshmallowSerializer):
    """UI JSON serializer."""

    def __init__(self):
        """Initialise Serializer."""
        super().__init__(
            format_serializer_cls=JSONSerializer,
            object_schema_cls=MbdbSprUISchema,
            list_schema_cls=BaseListSchema,
            schema_context={"object_key": "ui"},
        )