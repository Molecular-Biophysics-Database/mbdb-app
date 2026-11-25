import logging
from typing import override

from invenio_records_permissions.generators import Generator
from invenio_search.engine import dsl
from oarepo_runtime import current_runtime
from oarepo_runtime.services.generators import ConditionalGenerator
from oarepo_workflows.requests import RecipientGeneratorMixin
from oarepo_workflows.services.permissions.generators import UserWithRole

log = logging.getLogger(__name__)


def reviewer_role(model):
    return f"reviewer_{model.code}"


class DynamicReviewer(RecipientGeneratorMixin, Generator):
    """Reviewers of the record's method: role `reviewer_<model code>`, e.g. reviewer_mst.

    The method is the record's model, not metadata.resource_type as in rdm-12:
    that is a free text field the depositor can change or leave empty.
    """

    def _role(self, record):
        return UserWithRole(reviewer_role(current_runtime.get_model_for_record(record)))

    @override
    def needs(self, record=None, **context):
        return self._role(record).needs() if record is not None else []

    @override
    def query_filter(self, identity=None, **context):
        query = dsl.Q("match_none")
        for schema, model in current_runtime.rdm_models_by_schema.items():
            role_filter = UserWithRole(reviewer_role(model)).query_filter(identity=identity)
            query |= role_filter & dsl.Q("term", **{"$schema": schema})
        return query

    @override
    def reference_receivers(self, record=None, request_type=None, **context):
        return self._role(record).reference_receivers()


class IfHasReviewerRole(ConditionalGenerator):
    """Without the role the draft would be locked in a request nobody can accept."""

    def __init__(self, then_):
        super().__init__(then_, else_=[])

    @override
    def _condition(self, record=None, **context):
        if record is None:
            return False
        if DynamicReviewer().reference_receivers(record=record):
            return True
        log.error("No reviewer role for %s, run scripts/setup_roles.py", type(record))
        return False

    @override
    def _query_instate(self, **context):
        return dsl.Q("match_none")
