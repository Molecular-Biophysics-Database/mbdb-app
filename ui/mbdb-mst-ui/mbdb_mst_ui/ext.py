# Copyright (c) 2022 Miroslav Bauer
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import re

from invenio_base.utils import obj_or_import_string
from mbdb_mst_ui import config as config


class MbdbMstExtension:
    def __init__(self, app=None):
        if app:
            self.init_config(app)
            self.init_app(app)
            self.init_resource(app)

    def init_app(self, app):
        app.extensions["mbdb_mst_ui"] = self

    def init_resource(self, app):
        """Initialize vocabulary resources."""
        self.resource = obj_or_import_string(app.config["MBDB_MST_UI_RESOURCE"])(
            config=obj_or_import_string(app.config["MBDB_MST_UI_RESOURCE_CONFIG"])(),
        )

    def init_config(self, app):
        """Initialize configuration."""
        for identifier in dir(config):
            if re.match("^[A-Z_]*$", identifier) and not identifier.startswith("_"):
                app.config.setdefault(identifier, getattr(config, identifier))
