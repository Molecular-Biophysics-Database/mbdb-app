import json

from alembic import op
from sqlalchemy import text


revision = "mbdb_app_12"
down_revision = "mbdb_app_11"
branch_labels = ()
depends_on = None


METHODS = ("mst", "spr", "bli", "itc", "mp")

RECORD_TABLES = tuple(
    table
    for method in METHODS
    for table in (
        f"{method}_metadata",
        f"{method}_draft_metadata",
    )
)

PARENT_TABLES = tuple(
    f"{method}_parent_record_metadata"
    for method in METHODS
)


def normalize_json(value):
    if isinstance(value, str):
        return json.loads(value)
    return value


def patch_record(data):
    data.setdefault("pids", {})

    metadata = data.setdefault("metadata", {})
    gp = metadata.setdefault("general_parameters", {})
    msp = metadata.setdefault("method_specific_parameters", {})

    gp.setdefault("entities_of_interest", [])
    gp.setdefault("chemical_environments", [])

    msp.setdefault("measurements", [])
    msp.setdefault("measurement_protocol", [])
    msp.setdefault("measurement_positions", [])

    return data


def unpatch_record(data):
    metadata = data.get("metadata", {})
    gp = metadata.get("general_parameters", {})
    msp = metadata.get("method_specific_parameters", {})

    if data.get("pids") == {}:
        data.pop("pids", None)

    if gp.get("entities_of_interest") == []:
        gp.pop("entities_of_interest", None)

    if gp.get("chemical_environments") == []:
        gp.pop("chemical_environments", None)

    for key in (
        "measurements",
        "measurement_protocol",
        "measurement_positions",
    ):
        if msp.get(key) == []:
            msp.pop(key, None)

    if msp == {}:
        metadata.pop("method_specific_parameters", None)

    if gp == {}:
        metadata.pop("general_parameters", None)

    if metadata == {}:
        data.pop("metadata", None)

    return data


def patch_parent(data):
    """
    Fixes:
        "owned_by": { "user": "39" }

    to:
        "owned_by": { "user": 39 }
    """

    try:
        user_id = data["access"]["owned_by"]["user"]
    except KeyError:
        return data

    if isinstance(user_id, str) and user_id.isdigit():
        data["access"]["owned_by"]["user"] = int(user_id)

    return data


def unpatch_parent(data):
    """
    Downgrade back to old legacy form.

    Be careful: this intentionally converts numeric owner id back to string.
    """

    try:
        user_id = data["access"]["owned_by"]["user"]
    except KeyError:
        return data

    if isinstance(user_id, int):
        data["access"]["owned_by"]["user"] = str(user_id)

    return data


def table_exists(conn, table):
    result = conn.execute(
        text("""
            SELECT EXISTS (
                SELECT 1
                FROM information_schema.tables
                WHERE table_schema = 'public'
                  AND table_name = :table
            )
        """),
        {"table": table},
    ).scalar()

    return bool(result)


def migrate_table(table, patch_func):
    conn = op.get_bind()

    if not table_exists(conn, table):
        return

    rows = conn.execute(
        text(f'SELECT id, json FROM "{table}"')
    ).mappings()

    for row in rows:
        js = normalize_json(row["json"])

        if not js:
            continue

        new_js = patch_func(js)

        conn.execute(
            text(f'UPDATE "{table}" SET json = :js WHERE id = :id'),
            {
                "js": json.dumps(new_js),
                "id": row["id"],
            },
        )


def upgrade():
    for table in RECORD_TABLES:
        migrate_table(table, patch_record)

    for table in PARENT_TABLES:
        migrate_table(table, patch_parent)


def downgrade():
    for table in RECORD_TABLES:
        migrate_table(table, unpatch_record)

    for table in PARENT_TABLES:
        migrate_table(table, unpatch_parent)