from invenio_access.permissions import system_identity
from oarepo_runtime.i18n import lazy_gettext as _
from oarepo_requests.types import ModelRefTypes
from oarepo_requests.types.generic import NonDuplicableOARepoRequestType
from oarepo_runtime.datastreams.utils import get_record_service_for_record

# Request
#
class SubmitDraftRequestType(NonDuplicableOARepoRequestType):
    """
    Custom submit draft request that validates the draft upon submission. The
    request is not created if validation fails.
    """

    type_id = "submit_draft"
    name = _("Submit")

    @classmethod
    @property
    def available_actions(cls):
        return {
            **super().available_actions,
        }

    receiver_can_be_none = False
    creator_can_be_none = False
    topic_can_be_none = False
    allowed_topic_ref_types = ModelRefTypes(published=True, draft=True)

    def can_create(self, identity, data, receiver, topic, creator, *args, **kwargs):
        if not topic.is_draft:
            raise ValueError("Trying to create publish request on published record")
        super().can_create(identity, data, receiver, topic, creator, *args, **kwargs)
        topic_service = get_record_service_for_record(topic)
        topic_service.validate_draft(system_identity, topic["id"])
