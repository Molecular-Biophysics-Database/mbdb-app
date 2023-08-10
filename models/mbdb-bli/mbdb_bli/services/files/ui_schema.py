import marshmallow as ma
from marshmallow import validate as ma_validate
from oarepo_runtime.ui.marshmallow import InvenioUISchema


class MbdbBliFileUISchema(InvenioUISchema):
    class Meta:
        unknown = ma.RAISE

    content_type = ma.fields.String(
        validate=[ma_validate.OneOf(["text", "binary", "text and binary"])]
    )

    context = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                [
                    "raw measurement data",
                    "derived measurement data",
                    "quality control report",
                    "performance test report",
                ]
            )
        ]
    )

    description = ma.fields.String()

    name = ma.fields.String()

    originates_from = ma.fields.String(
        validate=[ma_validate.OneOf(["Instrument software", "User", "MBDB"])]
    )

    processing_steps = ma.fields.List(
        ma.fields.Nested(lambda: ProcessingStepsItemUISchema())
    )

    recommended_software = ma.fields.String()

    size = ma.fields.Integer()


class ProcessingStepsItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    description = ma.fields.String()

    link_to_source_code = ma.fields.String()

    name = ma.fields.String()

    software_name = ma.fields.String()

    software_tool = ma.fields.String()

    software_version = ma.fields.String()