# -- General configuration ------------------------------------------------
from pathlib import Path


extensions = [
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx.ext.mathjax",
    # Katex is a substitute for mathjax, renders math much faster
    # Note: katex extension must come before sagecell to work properly
    "sphinxcontrib.katex",
    # Extension for embedding geogebra applets, see README.txt in ggbextension folder
    "sphinxcontrib.geogebra",  # (https://github.com/edbook/sphinxcontrib-geogebra)
    "sphinxcontrib.toggleblock",  # (https://github.com/edbook/sphinxcontrib-toogleblock)
    "sphinxcontrib.questionnaire",  # (https://github.com/edbook/sphinxcontrib-questionnaire)
    # Extension for providing Icelandic to English translation of mathematical terms
    "sphinxcontrib.hoverrole",  # (https://github.com/edbook/sphinxcontrib-hoverrole)
    # Extension for embedding sage cells (https://github.com/edbook/sphinxcontrib-sagecell)
    # Note: sagecell must not be listed before katex.katex
    #    'sphinxcontrib.sagecell',
    # Extension for embedding datacamp-light which enables constructing simple programming exercises
    # in R and python, with much greater package support than sagecell in R
    "sphinxcontrib.datacamp",
    # Extension that allows embedding panopto videos from rec.hi.is
    "sphinxcontrib.panopto",
    "sphinxcontrib.custombutton",
    "sphinxcontrib.youtube",
    #    "sphinx_rtd_dark_mode"
]

vendors = {
    "mathjax_path": (
        "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
    ),
    "katex_path": "https://cdn.jsdelivr.net/npm/katex@latest/dist/katex.min.js",
    "katex_render": "https://cdn.jsdelivr.net/npm/katex@latest/dist/contrib/auto-render.min.js",
    "render_math": "rendermath.js",
    "katex_css": "https://cdn.jsdelivr.net/npm/katex@latest/dist/katex.min.css",
    "datacamp_path": "https://cdn.datacamp.com/datacamp-light-latest.min.js",
    "sage_jquery_path": "http://sagecell.sagemath.org/static/jquery.min.js",
    "sage_path": "http://sagecell.sagemath.org/static/embedded_sagecell.js",
}

# Path for latest datacamp javascript file

# Paths for sagecell javascript files
# custom_sage_path = Path(root, "custom_sage.js")
