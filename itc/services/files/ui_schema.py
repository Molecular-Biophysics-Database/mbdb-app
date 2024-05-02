import marshmallow as ma
from marshmallow import fields as ma_fields
from marshmallow.validate import OneOf
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_runtime.services.schema.ui import InvenioUISchema


class ItcFileUISchema(InvenioUISchema):
    class Meta:
        unknown = ma.RAISE

    content_type = ma_fields.String(
        required=True, validate=[OneOf(["text", "binary", "text and binary"])]
    )

    context = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "raw measurement data",
                    "derived measurement data",
                    "quality control report",
                ]
            )
        ],
    )

    description = ma_fields.String()

    name = ma_fields.String(required=True)

    originates_from = ma_fields.String(
        required=True, validate=[OneOf(["Instrument software", "User", "MBDB"])]
    )

    processing_steps = ma_fields.List(
        ma_fields.Nested(lambda: ProcessingStepsItemUISchema()), required=True
    )

    recommended_software = ma_fields.String()

    size = ma_fields.Integer(required=True)


class ProcessingStepsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String(required=True)

    link_to_source_code = ma_fields.String()

    name = ma_fields.String(required=True)

    software_name = ma_fields.String()

    software_version = ma_fields.String()


class ItcFileDraftUISchema(InvenioUISchema):
    class Meta:
        unknown = ma.RAISE
