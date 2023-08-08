import marshmallow as ma
from invenio_records_resources.services.files.schema import (
    FileSchema as InvenioFileSchema,
)
from marshmallow import validate as ma_validate
from oarepo_runtime.validation import validate_date


class MbdbMstFileSchema(InvenioFileSchema):
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

    created = ma.fields.String(dump_only=True, validate=[validate_date("%Y-%m-%d")])

    description = ma.fields.String()

    name = ma.fields.String()

    originates_from = ma.fields.String(
        validate=[ma_validate.OneOf(["Instrument software", "User", "MBDB"])]
    )

    processing_steps = ma.fields.List(
        ma.fields.Nested(lambda: ProcessingStepsItemSchema())
    )

    recommended_software = ma.fields.String()

    size = ma.fields.Integer()

    updated = ma.fields.String(dump_only=True, validate=[validate_date("%Y-%m-%d")])


class ProcessingStepsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    description = ma.fields.String()

    link_to_source_code = ma.fields.String()

    name = ma.fields.String()

    software_name = ma.fields.String()

    software_tool = ma.fields.String()

    software_version = ma.fields.String()
