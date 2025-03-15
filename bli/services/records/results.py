from oarepo_communities.services.results import RecordCommunitiesComponent
from oarepo_requests.services.results import RequestsComponent, RequestTypesComponent
from oarepo_runtime.services.results import RecordItem, RecordList


class BliRecordItem(RecordItem):
    """BliRecord record item."""

    components = [
        *RecordItem.components,
        RecordCommunitiesComponent(),
        RequestsComponent(),
        RequestTypesComponent(),
    ]


class BliRecordList(RecordList):
    """BliRecord record list."""

    components = [*RecordList.components]
