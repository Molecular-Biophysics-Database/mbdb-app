from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "mst_ui_components": "./js/mst_ui/custom-components.js"
            },
            dependencies={
            },
            devDependencies={
            },
            aliases={
            }
        )
    },
)
