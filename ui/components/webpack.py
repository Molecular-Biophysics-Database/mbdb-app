from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    ".",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
            },
            dependencies={
                "@material-ui/core": "^3.9.4"
            },
            devDependencies={},
            aliases={
                "@mbdb_deposit": "js/mbdb/forms/deposit"
            },
        )
    },
)
