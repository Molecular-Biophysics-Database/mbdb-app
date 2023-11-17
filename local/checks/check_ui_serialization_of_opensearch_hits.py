import json
import sys

from invenio_app.factory import create_app
from mbdb_mst.services.records.ui_schema import MbdbMstUISchema
from babel import Locale
import friendly_traceback as ft


def check_ui_serialization(json_file):
    with open (json_file, "r") as f:
        data = json.load(f)
    hits = data["hits"]["hits"]

    locale = Locale.parse('en')

    for hit in hits:
        ui_schema = MbdbMstUISchema(context={'locale': locale})
        ui_schema.dump(hit["_source"])


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        check_ui_serialization(sys.argv[1])