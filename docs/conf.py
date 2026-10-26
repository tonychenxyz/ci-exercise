project = "unc"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx_markdown_builder",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

exclude_patterns = ["_build"]
html_theme = "furo"
