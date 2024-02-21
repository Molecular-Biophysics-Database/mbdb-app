from oarepo_requests.services.results import RequestsComponent, RequestTypesComponent
from oarepo_runtime.services.results import RecordItem, RecordList


class BliRecordItem(RecordItem):
    """BliRecord record item."""

    components = [*RecordItem.components, RequestsComponent(), RequestTypesComponent()]


class BliRecordList(RecordList):
    """BliRecord record list."""

    components = [*RecordList.components]
