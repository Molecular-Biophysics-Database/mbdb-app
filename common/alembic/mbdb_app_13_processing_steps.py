import json

from alembic import op

revision = "mbdb_app_13"
down_revision = "mbdb_app_12"
branch_labels = ()
depends_on = None

AFFECTED_METHODS = ("spr", "mst", "bli", "itc", "mp")


def tables_constructor(method):
    return [
        f"{method}_file_metadata",
        f"{method}_file_draft_metadata",
    ]


def rename_processing_step(table_name, old_key, new_key):
    conn = op.get_bind()

    for row in conn.execute("SELECT id, json FROM " + table_name):
        json_data = row["json"]

        if not json_data or "metadata" not in json_data:
            continue

        metadata = json_data["metadata"]

        if old_key not in metadata:
            continue

        metadata[new_key] = metadata.pop(old_key)

        conn.execute(
            "UPDATE " + table_name + " SET json=%(js)s WHERE id=%(rowid)s",
            {"js": json.dumps(json_data), "rowid": row["id"]},
        )


def upgrade():
    for method in AFFECTED_METHODS:
        for table in tables_constructor(method):
            rename_processing_step(
                table,
                old_key="processing_step",
                new_key="processing_steps",
            )


def downgrade():
    for method in AFFECTED_METHODS:
        for table in tables_constructor(method):
            rename_processing_step(
                table,
                old_key="processing_steps",
                new_key="processing_step",
            )