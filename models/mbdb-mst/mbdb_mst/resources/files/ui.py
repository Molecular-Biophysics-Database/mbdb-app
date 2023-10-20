from flask_resources import BaseListSchema, MarshmallowSerializer
from flask_resources.serializers import JSONSerializer

from mbdb_mst.services.files.ui_schema import (
    MbdbMstFileDraftUISchema,
    MbdbMstFileUISchema,
)


class MbdbMstFileUIJSONSerializer(MarshmallowSerializer):
    """UI JSON serializer."""

    def __init__(self):
        """Initialise Serializer."""
        super().__init__(
            format_serializer_cls=JSONSerializer,
            object_schema_cls=MbdbMstFileUISchema,
            list_schema_cls=BaseListSchema,
            schema_context={"object_key": "ui"},
        )


class MbdbMstFileDraftUIJSONSerializer(MarshmallowSerializer):
    """UI JSON serializer."""

    def __init__(self):
        """Initialise Serializer."""
        super().__init__(
            format_serializer_cls=JSONSerializer,
            object_schema_cls=MbdbMstFileDraftUISchema,
            list_schema_cls=BaseListSchema,
            schema_context={"object_key": "ui"},
        )
