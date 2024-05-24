from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    ".",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "itc_search": "./js/itc/search/index.js",
                "itc_deposit_form": "./js/itc/forms/index.js",
            },
            dependencies={
                "@material-ui/core": "^3.9.4"
            },
            devDependencies={},
            aliases={
                "@itc_deposit": "js/itc/forms/deposit"
            },
        )
    },
)
