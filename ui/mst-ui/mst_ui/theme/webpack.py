from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "mst_ui_components": "./js/mst_ui/custom-components.js",
                "mst_ui_search": "./js/mst_ui/search/index.js"
            },
            dependencies={
                "react-searchkit": "^2.0.0",
            },
            devDependencies={
            },
            aliases={
                "@translations/mst_ui": "translations/mst_ui",
            },
        )
    },
)
