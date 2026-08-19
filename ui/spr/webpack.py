from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    ".",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "spr_search": "./js/spr/search/index.js",
                "spr_deposit_form": "./js/spr/forms/index.js",
            },
            dependencies={},
            devDependencies={},
            aliases={
                "@js/spr": "./js/spr"
            },
        )
    },
)
