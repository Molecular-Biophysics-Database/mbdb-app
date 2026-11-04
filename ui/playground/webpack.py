from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    ".",
    default="semantic-ui",
    themes={
        "semantic-ui": {
            "entry": {
                "mbdb_playground": "./js/mbdb_playground/index.js",
                # the full MST form mockup (/playground/mst-mockup)
                "mst_mockup": "./js/mbdb_playground/mst_mockup/index.js",
            },
            "dependencies": {},
            "devDependencies": {},
            "aliases": {
                "@js/mbdb_playground": "./js/mbdb_playground",
            },
        }
    },
)
