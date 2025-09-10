# Configuration file for the Sphinx documentation builder.

project = "Falcoria"
author = "Falcoria Authors"
release = "latest"

extensions = [
    "myst_parser",
]

# Allow both .md and .rst
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

master_doc = "index"

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
