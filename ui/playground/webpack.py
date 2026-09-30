from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    ".",
    default="semantic-ui",
    themes={
        "semantic-ui": {
            "entry": {
                "mbdb_playground": "./js/mbdb_playground/index.js",
            },
            "dependencies": {},
            "devDependencies": {},
            "aliases": {
                "@js/mbdb_playground": "./js/mbdb_playground",
            },
        }
    },
)
