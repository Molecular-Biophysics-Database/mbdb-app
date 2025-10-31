from marshmallow import Schema, fields, pre_load
from marshmallow.validate import OneOf
from marshmallow.exceptions import ValidationError
from semver import parse_version_info


class VersionUpdateSchema(Schema):
    @pre_load
    def update_version(self, data, **kwargs):
        schema_version_validators = self.fields['schema_version'].validators
        for validator in schema_version_validators:
            if isinstance(validator, OneOf):
                schema_version = validator.choices[0]
                break
        else:
            raise Exception("Version not found in schema")

        data_version = data.get('schema_version')

        if data_version and parse_version_info(data_version) < parse_version_info(schema_version):
            data['schema_version'] = schema_version

        return data

