from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    ".",
    default="semantic-ui",
    themes={
        "semantic-ui": {
            "entry": {
                "components": "./js/custom-components.js",
                # Not loaded by any page. `./run.sh jstest` only searches the
                # directories of webpack entries for tests, so without this
                # entry the tests under js/mbdb/forms would never run.
                "mbdb_forms": "./js/mbdb/forms/index.js",
            },
            "dependencies": {},
            "devDependencies": {},
            "aliases": {
                "@js/mbdb": "./js/mbdb",
                "mbdb-semantic-ui-react": "./js/mbdb-semantic-ui-react",
                "mbdb-react-invenio-forms": "./js/mbdb-react-invenio-forms",
            },
        }
    },
)
