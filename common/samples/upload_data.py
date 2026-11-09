"""Upload a sample MST record:

    invenio shell common/samples/upload_data.py <record.json> [owner email]

Without an owner email the draft belongs to the system user, so nobody can edit it in the UI.

Invenio never creates vocabulary items on its own, so chemicals and organisms the record
references but that are not in the vocabularies yet are created first, from the data
embedded in the record (title, formula, weight, ... / title, rank).
"""

import json
import sys

from invenio_access.permissions import system_identity
from invenio_accounts.models import User
from invenio_db import db
from invenio_pidstore.errors import PIDDoesNotExistError
from invenio_vocabularies.proxies import current_service as vocabulary_service
from invenio_vocabularies.records.api import Vocabulary
from oarepo_runtime import current_runtime
from oarepo_runtime.typing import record_from_result


def _chemical(item):
    custom_fields = {
        key: item[key]
        for key in ("chemical_formula", "molecular_weight", "additional_identifiers")
        if key in item
    }
    return {"id": item["id"], "title": item["title"], "custom_fields": custom_fields}


def _organism(item):
    vocabulary_item = {"id": item["id"], "title": item["title"]}
    if item.get("rank"):
        vocabulary_item["props"] = {"rank": item["rank"].lower()}
    return vocabulary_item


# vocabulary type and converter from embedded record data, by vocabulary item id prefix
VOCABULARY_ITEM_BUILDERS = {
    "inchikey:": ("chemicals", _chemical),
    "taxid:": ("organisms", _organism),
}


def referenced_vocabulary_items(data):
    """Yield (vocabulary type, vocabulary item) for every chemical/organism in the record."""
    if isinstance(data, dict):
        item_id = data.get("id")
        if isinstance(item_id, str) and "title" in data:
            for prefix, (vocabulary_type, build) in VOCABULARY_ITEM_BUILDERS.items():
                if item_id.startswith(prefix):
                    yield vocabulary_type, build(data)
        for value in data.values():
            yield from referenced_vocabulary_items(value)
    elif isinstance(data, list):
        for value in data:
            yield from referenced_vocabulary_items(value)


def create_missing_vocabulary_items(data, uow=None):
    """Create referenced chemicals/organisms that are not in the vocabularies yet."""
    created = []
    seen = set()
    for vocabulary_type, item in referenced_vocabulary_items(data):
        key = (vocabulary_type, item["id"])
        if key in seen:
            continue
        seen.add(key)
        try:
            Vocabulary.pid.resolve(key)
        except PIDDoesNotExistError:
            vocabulary_service.create(system_identity, {**item, "type": vocabulary_type}, uow=uow)
            created.append(key)
    return created


def upload(path, owner_email=None, uow=None):
    with open(path) as f:
        data = json.load(f)
    for vocabulary_type, item_id in create_missing_vocabulary_items(data, uow=uow):
        print(f"created {vocabulary_type} vocabulary item {item_id}")
    mst_service = current_runtime.models["mst"].service
    # created by the system (users need a community/workflow to create records),
    # then handed over to the owner so they can edit it in the UI
    result = mst_service.create(system_identity, data, uow=uow)
    if owner_email:
        owner = User.query.filter_by(email=owner_email).one()
        draft = record_from_result(result)
        draft.parent.access.owned_by = owner
        draft.parent.commit()
        db.session.commit()
        mst_service.indexer.index(draft)
    return result


if __name__ == "__main__":
    result = upload(sys.argv[1], owner_email=sys.argv[2] if len(sys.argv) > 2 else None)
    print(result.data["links"]["self_html"])
