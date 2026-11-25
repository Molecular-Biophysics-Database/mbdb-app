"""Metadata of uploaded files.

As in mbdb-app-rdm-12: unlike models/files.yaml, processing steps are optional
and the option values are capitalized.
"""

from __future__ import annotations

import marshmallow as ma
from invenio_i18n import gettext as _
from invenio_records_resources.services.files.schema import FileSchema
from invenio_records_resources.services.records.components import ServiceComponent
from marshmallow import fields as ma_fields
from marshmallow.validate import Length, OneOf


def _not_blank(value):
    if not value.strip():
        raise ma.ValidationError("Missing data for required field.")


class ProcessingStepSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    name = ma_fields.String(required=True, validate=_not_blank)
    description = ma_fields.String(required=True, validate=_not_blank)
    software_name = ma_fields.String()
    software_version = ma_fields.String()
    link_to_source_code = ma_fields.String()


class MstFileMetadataSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    content_type = ma_fields.String(required=True, validate=OneOf(["Text", "Binary", "Text and binary"]))
    context = ma_fields.String(
        required=True,
        validate=OneOf(["Raw measurement data", "Derived measurement data", "Quality control report"]),
    )
    originates_from = ma_fields.String(required=True, validate=OneOf(["Instrument software", "User", "MBDB"]))
    creation_date = ma_fields.String(required=True)
    description = ma_fields.String()
    recommended_software = ma_fields.String()
    processing_steps = ma_fields.List(ma_fields.Nested(ProcessingStepSchema), validate=Length(min=1))
    # written by Invenio's image processor, sent back by the form unchanged
    width = ma_fields.Integer()
    height = ma_fields.Integer()

    @ma.validates("creation_date")
    def _validate_creation_date(self, value, **kwargs):
        ma_fields.Date(format="%Y-%m-%d").deserialize(value)


class MstFileSchema(FileSchema):
    # sent by the deposit form together with the file
    metadata = ma_fields.Nested(MstFileMetadataSchema, required=True)


class MstFileServiceConfigMixin:
    file_schema = MstFileSchema


def file_metadata_error(record):
    """Return an error message when a file of the record has incomplete metadata, None otherwise."""
    schema = MstFileMetadataSchema()
    keys = sorted(key for key, file in record.files.items() if schema.validate(file.metadata or {}))
    if not keys:
        return None
    return _("Required file details are missing or not valid: %(files)s", files=", ".join(keys))


class FileMetadataComponent(ServiceComponent):
    """Report incomplete file metadata when a draft is saved."""

    def update_draft(self, identity, data=None, record=None, errors=None, **kwargs):
        message = file_metadata_error(record)
        if message and errors is not None:
            errors.append({"field": "files.enabled", "messages": [message]})


class FileMetadataServiceMixin:
    """Refuse incomplete file metadata on submit and publish."""

    def _validate_draft(self, identity, draft, *args, **kwargs):
        super()._validate_draft(identity, draft, *args, **kwargs)
        message = file_metadata_error(draft)
        if message:
            raise ma.ValidationError(message, field_name="files.enabled")
