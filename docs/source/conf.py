import sys
import os

sys.path.insert(0, os.path.abspath("../../mcsmapi"))

extensions = [
    "sphinx.ext.autodoc",
    "autoapi.extension",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
]

autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
    "imported-members",
]
autoapi_dirs = ["../../mcsmapi"]
