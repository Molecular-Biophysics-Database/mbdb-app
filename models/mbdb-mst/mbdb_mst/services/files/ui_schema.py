import marshmallow as ma
from oarepo_runtime.ui.marshmallow import InvenioUISchema


class MbdbMstFileUISchema(InvenioUISchema):
    class Meta:
        unknown = ma.RAISE
