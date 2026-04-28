import json
from alembic import op

revision = "mbdb_app_12"
down_revision = "mbdb_app_11"
branch_labels = ()
depends_on = None

TABLES = (
    "bli_metadata",
    "bli_draft_metadata",
)


def patch_record(data):
    metadata = data.setdefault("metadata", {})
    gp = metadata.setdefault("general_parameters", {})
    msp = metadata.setdefault("method_specific_parameters", {})
    ri = gp.setdefault("record_information", {})

    ri.setdefault("title", "Untitled")

    gp.setdefault("entities_of_interest", [])
    gp.setdefault("chemical_environments", [])

    msp.setdefault("plates", [])
    msp.setdefault("sensors", [])
    msp.setdefault("measurements", [])
    msp.setdefault("measurement_protocol", [])

    return data


def migrate_table(table):
    conn = op.get_bind()

    for row in conn.execute("SELECT * FROM " + table):
        js = row["json"]

        if isinstance(js, str):
            js = json.loads(js)

        if not js:
            continue

        new_js = patch_record(js)

        conn.execute(
            "UPDATE " + table + " SET json=%(js)s WHERE id=%(id)s",
            {"js": json.dumps(new_js), "id": row["id"]},
        )


def upgrade():
    for table in TABLES:
        migrate_table(table)


def downgrade():
    pass
