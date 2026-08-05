import json

from alembic import op

revision = "mbdb_app_16"
down_revision = "mbdb_app_15"
branch_labels = ()
depends_on = None

AFFECTED_METHODS = ("spr", "mst", "bli", "itc", "mp")

# The instrument relation (see PIDRelation in each method's records/api.py)
# only ever injects id/title/manufacturer/@v. Anything else still present
# on metadata.general_parameters.instrument is a leftover from the old
# deposit form days when InstrumentSchema allowed unknown fields through
# (same root cause as mbdb_app_14, which only handled "created"/"updated").
# Once a stray key like this is baked into a record, invenio_records'
# RelationResult._dereference_one short-circuits on "@v" already being
# present and never re-applies the relation's keys allow-list, so it
# survives indefinitely. In this case the stray "hierarchy" field (a
# vocabulary-only system field: level/title/ancestors/leaf) is dynamically
# mapped by OpenSearch from whatever shape the first-indexed record has,
# and conflicts with the shape on other records, causing
# mapper_parsing_exception on reindex.
ALLOWED_KEYS = {"id", "title", "manufacturer", "@v"}


def tables_constructor(method):
    return [
        f"{method}_metadata",
        f"{method}_draft_metadata",
    ]


def strip_instrument_stray_fields(table_name):
    conn = op.get_bind()

    for row in conn.execute("SELECT id, json FROM " + table_name):
        json_data = row["json"]

        if not json_data or "metadata" not in json_data:
            continue

        instrument = json_data["metadata"].get("general_parameters", {}).get(
            "instrument"
        )

        if not isinstance(instrument, dict):
            continue

        stray_keys = [key for key in instrument if key not in ALLOWED_KEYS]
        if not stray_keys:
            continue

        for key in stray_keys:
            instrument.pop(key, None)

        conn.execute(
            "UPDATE " + table_name + " SET json=%(js)s WHERE id=%(rowid)s",
            {"js": json.dumps(json_data), "rowid": row["id"]},
        )


def upgrade():
    for method in AFFECTED_METHODS:
        for table in tables_constructor(method):
            strip_instrument_stray_fields(table)


def downgrade():
    # The original stray values are not recoverable (and were invalid to
    # begin with), so there is nothing meaningful to restore.
    pass
