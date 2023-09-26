from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "mbdb_mst_ui_components": "./js/mbdb_mst_ui/custom-components.js",
                "mbdb_mst_ui_search": "./js/mbdb_mst_ui/search/index.js",
                "mbdb_mst_ui_deposit_form": "./js/mbdb_mst_ui/forms/deposit/index.js",
            },
            dependencies={
                "react-searchkit": "^2.0.0",
                "@mbdb/input-form": "^0.0.7",
            },
            devDependencies={},
            aliases={
                "@translations/mbdb_mst_ui": "translations/mbdb_mst_ui",
            },
        )
    },
)
