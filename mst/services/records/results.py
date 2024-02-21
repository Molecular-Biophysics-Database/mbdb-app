from oarepo_requests.services.results import RequestsComponent, RequestTypesComponent
from oarepo_runtime.services.results import RecordItem, RecordList


class MstRecordItem(RecordItem):
    """MstRecord record item."""

    components = [*RecordItem.components, RequestsComponent(), RequestTypesComponent()]


class MstRecordList(RecordList):
    """MstRecord record list."""

    components = [*RecordList.components]
