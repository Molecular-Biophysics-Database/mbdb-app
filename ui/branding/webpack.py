from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    ".",
    default="semantic-ui",
    themes={
        "semantic-ui": {
            "entry": {
                "branding": "./js/branding.js"
            },
            "dependencies": {
                "react-searchkit": "^2.0.0",
                "semantic-ui-less": "^2.5.0",
            },
            "devDependencies": {
                "tailwindcss": "^3.3.5"
            },
            "aliases": {
                "../../theme.config$": "less/theme.config",
                "../../less/site": "less/site",
                "../../less": "less",
                "@less": "less",
            },
        }
    },
)
