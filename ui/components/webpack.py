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
            "dependencies": {
                # vocabularyTitles.js fetches vocabulary items with Invenio's
                # Accept header (VocabularyFields-review F5); declare it so the
                # import resolves via the components package, not by accident
                # of the instance assets entry.
                "axios": "^1.7.7",
            },
            "devDependencies": {},
            "aliases": {
                "@js/mbdb": "./js/mbdb",
                "mbdb-semantic-ui-react": "./js/mbdb-semantic-ui-react",
                "mbdb-react-invenio-forms": "./js/mbdb-react-invenio-forms",
            },
        }
    },
)
