from oarepo_requests.actions.delete_topic import DeleteTopicSubmitAction
from oarepo_requests.types.delete_record import DeleteRecordRequestType as BaseDeleteRecordRequestType


class DeleteRecordRequestType(BaseDeleteRecordRequestType):

    type_id = "delete_record"
    name = "Delete-record"

    available_actions = {
        **BaseDeleteRecordRequestType.available_actions,
        "submit": DeleteTopicSubmitAction,
    }

    allowed_topic_ref_types = [
        "bli"
        "mst",
        "spr"
    ]

    @classmethod
    def _update_link_config(cls, **context_values):
        return {}
