"""backfill pids.doi for records published before oarepo_doi was wired in"""

import json

from alembic import op

revision = "mbdb_app_15"
down_revision = "mbdb_app_14"
branch_labels = ()
depends_on = None

# Must match the DataCite prefix configured in invenio.cfg
# (DATACITE_CREDENTIALS_DEFAULT / DATACITE_CREDENTIALS). New records mint
# DOIs as f"{prefix}/{record_id}" (DATACITE_SPECIFIED_ID=True), and these
# old records were already registered at DataCite under that same
# pattern when they were published on the old production version — this
# migration just writes the already-known value into pids.doi so that
# the self_doi/doi links (computed from pids.doi.identifier) appear.
DOI_PREFIX = "10.82657"

AFFECTED_METHODS = ("bli", "itc", "mp", "mst", "spr")


def backfill_doi(table_name):
    conn = op.get_bind()

    for row in conn.execute("SELECT id, json FROM " + table_name):
        json_data = row["json"]

        if not json_data:
            continue

        pids = json_data.get("pids") or {}
        if pids.get("doi"):
            continue  # already has a DOI, nothing to do

        record_id = json_data.get("id")
        if not record_id:
            continue

        pids["doi"] = {
            "provider": "datacite",
            "identifier": f"{DOI_PREFIX}/{record_id}",
        }
        json_data["pids"] = pids

        conn.execute(
            "UPDATE " + table_name + " SET json=%(js)s WHERE id=%(rowid)s",
            {"js": json.dumps(json_data), "rowid": row["id"]},
        )


def upgrade():
    """Upgrade database."""
    for method in AFFECTED_METHODS:
        backfill_doi(f"{method}_metadata")


def downgrade():
    """Downgrade database."""
    # The DOI values written here are indistinguishable from ones minted
    # normally after this migration ran (same f"{prefix}/{record_id}"
    # shape), so blindly clearing pids.doi on downgrade risks stripping
    # real DOIs from records published after the upgrade ran. Nothing to
    # revert automatically.
    pass
