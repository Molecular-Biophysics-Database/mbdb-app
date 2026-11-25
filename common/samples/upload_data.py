"""Upload a sample MST record:

    invenio shell common/samples/upload_data.py <record.json> [owner email]

Without an owner email the draft belongs to the system user, so nobody can edit it in the UI.

Invenio never creates vocabulary items on its own, so vocabulary items the record references
but that do not exist yet are created first, from the data embedded in the record:
affiliations, funders and awards (id, name/number/title), chemicals (title, formula,
weight, ...) and organisms (title, rank).
"""

import json
import sys

from invenio_access.permissions import system_identity
from invenio_accounts.models import User
from invenio_db import db
from invenio_pidstore.errors import PIDDoesNotExistError
from invenio_records_resources.proxies import current_service_registry
from invenio_vocabularies.proxies import current_service as vocabulary_service
from invenio_vocabularies.records.api import Vocabulary
from oarepo_runtime import current_runtime
from oarepo_runtime.typing import record_from_result
from sqlalchemy.orm.exc import NoResultFound


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


def _ror(ror_id):
    return [{"identifier": ror_id, "scheme": "ror"}]


def referenced_dedicated_items(data, parent_key=None):
    """Yield (service id, item) for affiliations, funders and awards referenced by the record.

    These are Invenio's dedicated vocabularies (own services), referenced as
    {"id", "name"} in "affiliations" lists, and as "funder" / "award" in funding.
    """
    if isinstance(data, dict):
        if parent_key == "affiliations" and "id" in data and "name" in data:
            yield "affiliations", {"id": data["id"], "name": data["name"], "identifiers": _ror(data["id"])}
        if "funder" in data and "id" in data["funder"]:
            funder = data["funder"]
            yield "funders", {"id": funder["id"], "name": funder["name"], "identifiers": _ror(funder["id"])}
            award = data.get("award")
            if award and "id" in award:
                yield "awards", {
                    "id": award["id"],
                    "number": award["number"],
                    "title": award["title"],
                    "funder": {"id": funder["id"]},
                }
        for key, value in data.items():
            yield from referenced_dedicated_items(value, key)
    elif isinstance(data, list):
        for value in data:
            yield from referenced_dedicated_items(value, parent_key)


def create_missing_dedicated_items(data, uow=None):
    """Create referenced affiliations, funders and awards that do not exist yet."""
    created = []
    items = {}
    for service_id, item in referenced_dedicated_items(data):
        items.setdefault((service_id, item["id"]), item)
    # funders before awards: an award must reference an existing funder
    for service_id in ("affiliations", "funders", "awards"):
        service = current_service_registry.get(service_id)
        for (item_service_id, item_id), item in items.items():
            if item_service_id != service_id:
                continue
            try:
                service.read(system_identity, item_id)
            except (PIDDoesNotExistError, NoResultFound):
                service.create(system_identity, item, uow=uow)
                created.append((service_id, item_id))
    return created


def upload(path, owner_email=None, uow=None):
    with open(path) as f:
        data = json.load(f)
    created = create_missing_dedicated_items(data, uow=uow) + create_missing_vocabulary_items(data, uow=uow)
    for vocabulary_type, item_id in created:
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
    links = result.data["links"]
    print(f"record:  {result.id}")
    print(f"edit:    {links['self_html']}")
    print(f"preview: {links['preview_html']}")
    print(f"API:     {links['self']}")
