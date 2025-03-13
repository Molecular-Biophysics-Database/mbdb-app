from oarepo_communities.services.results import RecordCommunitiesComponent
from oarepo_requests.services.results import RequestsComponent, RequestTypesComponent
from oarepo_runtime.services.results import RecordItem, RecordList


class ItcRecordItem(RecordItem):
    """ItcRecord record item."""

    components = [
        *RecordItem.components,
        RecordCommunitiesComponent(),
        RequestsComponent(),
        RequestTypesComponent(),
    ]


class ItcRecordList(RecordList):
    """ItcRecord record list."""

    components = [*RecordList.components]
