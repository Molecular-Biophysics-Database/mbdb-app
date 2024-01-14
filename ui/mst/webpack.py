from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    ".",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "mst_search": "./js/mst/search/index.js",
                "mst_deposit_form": "./js/mst/forms/deposit/index.js",
            },
            dependencies={
                "@mbdb/input-form": "^0.0.28",
            },
            devDependencies={},
            aliases={},
        )
    },
)
