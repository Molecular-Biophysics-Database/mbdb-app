import logging

from flask import g
from flask_login import current_user
from invenio_requests.proxies import current_requests_service
from invenio_search.engine import dsl, search

from . import review

log = logging.getLogger(__name__)

REVIEW_TYPES = [
    review.ReviewDraftRequestType.type_id,
    review.ReviewNewVersionRequestType.type_id,
    review.ReviewChangedMetadataRequestType.type_id,
]


def count_waiting_requests(identity):
    """Number of review requests waiting for one of the identity's roles."""
    roles = [need.value for need in identity.provides if need.method == "role"]
    if not roles:
        return 0
    return current_requests_service.search(
        identity,
        params={"size": 1},
        extra_filter=dsl.Q("term", status="submitted")
        & dsl.Q("terms", type=REVIEW_TYPES)
        & dsl.Q("terms", **{"receiver.group": roles}),
    ).total


def waiting_requests_count():
    """For templates; the header is on every page, so a search failure must not break it."""
    if not current_user.is_authenticated:
        return 0
    if "waiting_requests_count" not in g:
        try:
            g.waiting_requests_count = count_waiting_requests(g.identity)
        except search.OpenSearchException:
            log.exception("Could not count the waiting requests")
            g.waiting_requests_count = 0
    return g.waiting_requests_count
