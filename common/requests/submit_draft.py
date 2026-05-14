from marshmallow import ValidationError
from oarepo_runtime.i18n import lazy_gettext as _
from oarepo_requests.types import ModelRefTypes
from oarepo_requests.types.generic import NonDuplicableOARepoRequestType
from oarepo_runtime.datastreams.utils import get_record_service_for_record
from common.requests.customizations.custom_actions import *



# Request
class SubmitDraftRequestType(NonDuplicableOARepoRequestType):
    """
    Custom submit draft request that validates the draft upon submission. The
    request is not created if validation fails.
    """

    type_id = "submit_draft"
    name = _("Submit")

    # Modal popup
    dangerous = True

    @classmethod
    @property
    def available_actions(cls):
        actions = dict(super().available_actions)

        # remove inherited cancel action
        actions.pop("cancel", None)

        # override/add custom actions
        actions.update({
            "submit": SubmitDraftAction,
            "accept": AcceptDraftAction,
            "decline": DeclineDraftAction,
        })
        return actions

    receiver_can_be_none = False
    creator_can_be_none = False
    topic_can_be_none = False
    allowed_topic_ref_types = ModelRefTypes(published=True, draft=True)

    def can_create(self, identity, data, receiver, topic, creator, *args, **kwargs):
        if not topic.is_draft:
            raise ValueError("Trying to create publish request on published record")
        super().can_create(identity, data, receiver, topic, creator, *args, **kwargs)
        draft = topic

        # Enforce required file
        has_files = (
                getattr(draft, "files", None)
                and getattr(draft.files, "entries", None)
                and len(draft.files.entries) > 0
        )
        if not has_files:
            raise ValidationError({"files.enabled": ["Missing uploaded files."]})

        topic_service = get_record_service_for_record(topic)
        errors = topic_service.validate_draft(identity, topic["id"])

        if errors:
            raise ValidationError(errors)

    def stateful_name(self, identity, *, topic, request=None, **kwargs):
        return self.string_by_state(
            identity,
            topic=topic,
            request=request,

            create=_("Submit for review"),
            create_autoapproved=_("Submit for review"),
            cancelled=_("Draft request cancelled"),
            submit=_("Submit for review"),

            submitted_receiver=_("Draft sumbitted for review"),
            submitted_creator=_("Submitted for review"),
            submitted_others=_("Submitted"),

            accepted=_("Accepted"),
            declined=_("Draft declined"),
            created=_("Draft request created"),
        )