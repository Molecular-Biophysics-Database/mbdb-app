#
# Copyright (C) 2024 CESNET z.s.p.o.
#
# oarepo-requests is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.
#
"""Request for deleting published record."""

from invenio_i18n import lazy_gettext as _
from oarepo_requests.types.delete_published_record import DeletePublishedRecordRequestType


class CustomDeletePublishedRecordRequestType(DeletePublishedRecordRequestType):
    form = [
        {
            "section": "",
            "fields": [
                {
                    "field": "removal_reason",
                    "ui_widget": "Input",
                    "props": {
                        "label": _("Removal Reason"),
                        "placeholder": _("Write down the removal reason."),
                        "required": True,
                    },
                },
                {
                    "section": "",
                    "field": "note",
                    "ui_widget": "Input",
                    "props": {
                        "label": _("Note"),
                        "placeholder": _("This note is internal and will not be visible to the public."),
                        "required": False,
                    },
                },
            ],
        }
    ]