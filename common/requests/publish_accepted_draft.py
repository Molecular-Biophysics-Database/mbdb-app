from __future__ import annotations

from typing import TYPE_CHECKING, Any
from typing_extensions import override

from oarepo_runtime.i18n import lazy_gettext as _
from oarepo_requests.utils import (
    is_auto_approved,
    request_identity_matches,
)
from oarepo_requests.types.publish_draft import PublishDraftRequestType

if TYPE_CHECKING:
    from flask_babel.speaklater import LazyString
    from flask_principal import Identity
    from invenio_drafts_resources.records import Record
    from invenio_requests.records.api import Request


class PublishAcceptedDraftRequestType(PublishDraftRequestType):
    type_id = "publish_accepted_draft"
    name = _("Publish")

    # If inputs are needed, e.g. version name, they should be specified in form
    form = {}

    @override
    def stateful_description(
        self,
        identity: Identity,
        *,
        topic: Record,
        request: Request | None = None,
        **kwargs: Any,
    ) -> str | LazyString:
        """Return the stateful description of the request."""
        if is_auto_approved(self, identity=identity, topic=topic):
            return _(
                "By pressing 'Submit' you agree that the MBDB can distribute "
                "your data under the "
                """
                <a 
                  href='https://creativecommons.org/publicdomain/zero/1.0/?ref=chooser-v1' 
                  target='_blank'
                ><u>CCO license.</u></a>
                """
                "This means that <br>"
                "1) You hereby waive all copyright and related or neighboring "
                "rights together with all associated claims and causes of action "
                "with respect to this work to the extent possible under the law.<br>"
                "2) You have read and understand the terms and intended legal effect of CC0, "
                "and hereby voluntarily elect to apply it to this work. " 
                "will be placed in the public domain. <br><br> "
                
                "Furthermore, you hereby agree to MBDB's "
                """
                <a 
                  href='https://molecular-biophysics-database.github.io/mbdb-docs/terms-and-conditions/users' 
                  target='_blank'
                ><u>terms and conditions,</u></a>
                """
                "which, among others, include receiving permissions from all depositors, "
                "and ensuring that all deposited information, to the best of your knowledge, is correct."
            )

        match request.status:
            case "submitted":
                if request_identity_matches(request.created_by, identity):
                    return _(
                        "The draft has been submitted for review. "
                        "It is now locked and no further changes are possible. "
                        "You will be notified about the decision by email."
                    )
                if request_identity_matches(request.receiver, identity):
                    return _(
                        "The draft has been submitted for review. "
                        "You can now accept or decline the request."
                    )
                return _("The draft has been submitted for review.")
            case _:
                if request_identity_matches(request.created_by, identity):
                    return _(
                        "Submit for review. After submitting the draft for review, "
                        "it will be locked and no further modifications will be possible."
                    )
                return _("Request not yet submitted.")