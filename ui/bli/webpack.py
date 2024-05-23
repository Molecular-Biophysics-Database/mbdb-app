from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    ".",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "bli_search": "./js/bli/search/index.js",
                "bli_deposit_form": "./js/bli/forms/index.js",
            },
            dependencies={
                "@material-ui/core": "^3.9.4"
            },
            devDependencies={},
            aliases={
                "@bli_deposit": "js/bli/forms/deposit"
            },
        )
    },
)
