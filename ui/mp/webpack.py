from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    ".",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "mp_search": "./js/mp/search/index.js",
                "mp_deposit_form": "./js/mp/forms/index.js",
            },
            dependencies={
                "@material-ui/core": "^3.9.4"
            },
            devDependencies={},
            aliases={
                "@mp_deposit": "js/mp/forms/deposit"
            },
        )
    },
)
