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
                "@material-ui/core": "^3.9.4",
                "uuid": "^9.0.1"
            },
            devDependencies={},
            aliases={
                "@mbdb_deposit": "js/mbdb/forms/deposit"
            },
        )
    },
)
