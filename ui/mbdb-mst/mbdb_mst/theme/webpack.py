from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "mbdb_mst_components": "./js/mbdb_mst/custom-components.js",
                "mbdb_mst_search": "./js/mbdb_mst/search/index.js",
            },
            dependencies={
                "react-searchkit": "^2.0.0",
            },
            devDependencies={},
            aliases={
                "@translations/mbdb_mst": "translations/mbdb_mst",
            },
        )
    },
)
