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
            dependencies={},
            devDependencies={},
            aliases={
                "@js/itc": "./js/itc"
            },
        )
    },
)
