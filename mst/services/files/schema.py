import marshmallow as ma
from invenio_records_resources.services.files.schema import (
    FileSchema as InvenioFileSchema,
)
from marshmallow import fields as ma_fields
from marshmallow.validate import OneOf
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_runtime.services.schema.validation import validate_date


class MstFileSchema(InvenioFileSchema):
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

    created = ma_fields.String(dump_only=True, validate=[validate_date("%Y-%m-%d")])

    description = ma_fields.String()

    name = ma_fields.String(required=True)

    originates_from = ma_fields.String(
        required=True, validate=[OneOf(["Instrument software", "User", "MBDB"])]
    )

    processing_steps = ma_fields.List(
        ma_fields.Nested(lambda: ProcessingStepsItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    recommended_software = ma_fields.String()

    size = ma_fields.Integer(required=True, validate=[ma.validate.Range(min=0)])

    updated = ma_fields.String(dump_only=True, validate=[validate_date("%Y-%m-%d")])


class ProcessingStepsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String(required=True)

    link_to_source_code = ma_fields.String()

    name = ma_fields.String(required=True)

    software_name = ma_fields.String()

    software_version = ma_fields.String()
