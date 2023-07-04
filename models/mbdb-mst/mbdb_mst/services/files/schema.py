import marshmallow as ma
from invenio_records_resources.services.files.schema import (
    FileSchema as InvenioFileSchema,
)
from oarepo_runtime.validation import validate_date


class MbdbMstFileSchema(InvenioFileSchema):
    class Meta:
        unknown = ma.RAISE

    created = ma.fields.String(dump_only=True, validate=[validate_date("%Y-%m-%d")])

    updated = ma.fields.String(dump_only=True, validate=[validate_date("%Y-%m-%d")])
