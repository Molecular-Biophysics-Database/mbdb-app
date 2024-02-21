from oarepo_requests.services.results import RequestsComponent, RequestTypesComponent
from oarepo_runtime.services.results import RecordItem, RecordList


class SprRecordItem(RecordItem):
    """SprRecord record item."""

    components = [*RecordItem.components, RequestsComponent(), RequestTypesComponent()]


class SprRecordList(RecordList):
    """SprRecord record list."""

    components = [*RecordList.components]
