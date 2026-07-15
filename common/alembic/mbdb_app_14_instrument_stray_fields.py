import json

from alembic import op

revision = "mbdb_app_14"
down_revision = "mbdb_app_13"
branch_labels = ()
depends_on = None

AFFECTED_METHODS = ("spr", "mst", "bli", "itc", "mp")

# These are vocabulary system fields that leaked into
# metadata.general_parameters.instrument from the deposit form (see
# InstrumentSchema/InstrumentUISchema, which used to allow unknown fields
# through). "created" in particular could be stored as a locale-formatted
# string rather than ISO 8601, which OpenSearch's "date" mapping rejects.
STRAY_KEYS = ("created", "updated")


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

        if not any(key in instrument for key in STRAY_KEYS):
            continue

        for key in STRAY_KEYS:
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
