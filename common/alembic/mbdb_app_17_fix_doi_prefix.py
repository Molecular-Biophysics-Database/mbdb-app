"""fix the DOI prefix mistakenly used in mbdb_app_15's backfill"""

import json

from alembic import op

revision = "mbdb_app_17"
down_revision = "mbdb_app_16"
branch_labels = ()
depends_on = None

# mbdb_app_15 backfilled pids.doi.identifier using the stage DataCite
# prefix by mistake. The correct prefix is:
WRONG_PREFIX = "10.82657"
CORRECT_PREFIX = "10.71479"

AFFECTED_METHODS = ("bli", "itc", "mp", "mst", "spr")


def fix_doi_prefix(table_name):
    conn = op.get_bind()

    for row in conn.execute("SELECT id, json FROM " + table_name):
        json_data = row["json"]

        if not json_data:
            continue

        pids = json_data.get("pids") or {}
        doi = pids.get("doi")
        if not doi:
            continue

        identifier = doi.get("identifier") or ""
        if not identifier.startswith(WRONG_PREFIX + "/"):
            continue

        suffix = identifier[len(WRONG_PREFIX) + 1 :]
        doi["identifier"] = f"{CORRECT_PREFIX}/{suffix}"

        conn.execute(
            "UPDATE " + table_name + " SET json=%(js)s WHERE id=%(rowid)s",
            {"js": json.dumps(json_data), "rowid": row["id"]},
        )


def upgrade():
    """Upgrade database."""
    for method in AFFECTED_METHODS:
        fix_doi_prefix(f"{method}_metadata")


def downgrade():
    """Downgrade database."""
    # Reverting would require distinguishing rows this migration touched
    # from ones that were already correct, which isn't recoverable from
    # the data alone. Nothing to revert automatically.
    pass
