#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import inspect
from datetime import date
from typing import List, TypedDict
from pathlib import Path
import yaml
from edbook.lib.utils import get_projects_path

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))
# sys.path.append(os.path.abspath("../../extensions"))
from sphinxcontrib.questionnaire import (
    get_eqt_ext_static_dir,  # Verður að koma eftir að bæta extensions í path
)


# -- Custom extension options and paths --------------------------------------

# user starts in light mode
# default_dark_mode = False

# -- General configuration ------------------------------------------------
extensions = [
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx.ext.mathjax",
    # Katex is a substitute for mathjax, renders math much faster
    # Note: katex extension must come before sagecell to work properly
    #'sphinxcontrib.katex',
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

mathjax_path = (
    "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
)

katex_path = "https://cdn.jsdelivr.net/npm/katex@latest/dist/katex.min.js"
katex_render = (
    "https://cdn.jsdelivr.net/npm/katex@latest/dist/contrib/auto-render.min.js"
)
render_math = "rendermath.js"
katex_css = "https://cdn.jsdelivr.net/npm/katex@latest/dist/katex.min.css"

# Path for latest datacamp javascript file
datacamp_path = "https://cdn.datacamp.com/datacamp-light-latest.min.js"

# Paths for sagecell javascript files
sage_jquery_path = "http://sagecell.sagemath.org/static/jquery.min.js"
sage_path = "http://sagecell.sagemath.org/static/embedded_sagecell.js"
custom_sage_path = "custom_sage.js"

# Google Analytics ID, enable_custom_scrolldepth default value is False if not set
# ga_id = "UA-78633732-4"
# enable_custom_scrolldepth = True

# -- Build options ----------------------------------------------------

todo_include_todos = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = "is"
locale_dirs = ["locale/"]

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

#Enables referencing of figures  
numfig = True


# -- Options for HTML output ----------------------------------------------
# import alabaster
#
# html_theme_path = [alabaster.get_path()]
# extensions = ['alabaster']
# html_theme = 'alabaster'
# html_sidebars = {
#    '**': [
#        'about.html',
#        'navigation.html',
#        'relations.html',
#        'searchbox.html',
#        'donate.html',
#    ]
# }

html_theme = "sphinx_rtd_theme"
# html_theme_path = ["_themes"]

html_context = {
    "display_github": True,
    "github_user": "edbook",
    "github_repo": "haskoli-islands",
    "github_version": str("master/projects/" + os.path.split(os.getcwd())[1] + "/"),
}

html_permalinks = True
## CLOUD
# import cloud_sptheme as csp
# html_theme = "cloud"
# html_theme_path = [csp.get_theme_dir()]
# html_theme_options = {"roottarget": "index" }


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/haskoli_islands-edbook.svg"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon_2.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static", get_eqt_ext_static_dir()]
html_css_files = ["css/edbook.css"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}


# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False
# html_copy_source = False
# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "TMP001G"


# -- Options for HTML Slide output ---------------------------------------------------

slide_theme = "slides2"
slide_theme_options = {"custom_css": "custom.css"}

# slide_link_html_to_slides = not on_rtd
# slide_link_html_sections_to_slides = not on_rtd
# slide_relative_path = "./slides/"
#
# slide_link_to_html = True
# slide_html_relative_path = "../"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    "fncychap": "\\usepackage[Sonny]{fncychap}",
    "papersize": "a4paper",
    "preamble": """\
\\usepackage{amsmath}
\\usepackage{amssymb}
\\usepackage{hyperref}
""",
}

# latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
# }

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "_static/hi_vnvs_horiz_raunvisindadeild.jpg"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
latex_show_urls = "inline"

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        "index",
        id,
        "TMP001G Documentation",
        ["Jónmundur Gunnuson"],
        1,
    )
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
# epub_title = 'Stærðfræðigreining I'
# epub_author = 'Benedikt Steinar Magnússon'
# epub_publisher = 'Benedikt Steinar Magnússon'
# epub_copyright = '2015, Benedikt Steinar Magnússon'

# The basename for the epub file. It defaults to the project name.
# epub_basename = 'Stærðfræðigreining I'

# The HTML theme for the epub output. Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
# epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
# epub_identifier = ''

# A unique identification for the text.
# epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
# epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of ontent.opf.
# epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# The depth of the table of contents in toc.ncx.
# epub_tocdepth = 3

# Allow duplicate toc entries.
# epub_tocdup = True

# Choose between 'default' and 'includehidden'.
# epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
# epub_fix_images = False

# Scale large images.
# epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# epub_show_urls = 'inline'

# If false, no index is generated.
# epub_use_index = True


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'python': ("http://docs.python.org/", None)}


from docutils import nodes
from docutils.nodes import Element

# Hulda bætti mér við. Opna linka í öðrum gluggan.
from sphinx.writers.html import HTMLTranslator


class PatchedHTMLTranslator(HTMLTranslator):
    def visit_reference(self, node: Element) -> None:
        atts = {"class": "reference"}
        if node.get("internal") or "refuri" not in node:
            atts["class"] += " internal"
        else:
            atts["class"] += " external"
            # ---------------------------------------------------------
            # Customize behavior (open in new tab, secure linking site)
            atts["target"] = "_blank"
            atts["rel"] = "noopener noreferrer"
            # ---------------------------------------------------------
        if "refuri" in node:
            atts["href"] = node["refuri"] or "#"
            if self.settings.cloak_email_addresses and atts["href"].startswith(
                "mailto:"
            ):
                atts["href"] = self.cloak_mailto(atts["href"])
                self.in_mailto = True
        else:
            assert (
                "refid" in node
            ), 'References must have "refuri" or "refid" attribute.'
            atts["href"] = "#" + node["refid"]
        if not isinstance(node.parent, nodes.TextElement):
            assert len(node) == 1 and isinstance(node[0], nodes.image)
            atts["class"] += " image-reference"
        if "reftitle" in node:
            atts["title"] = node["reftitle"]
        if "target" in node:
            atts["target"] = node["target"]
        self.body.append(self.starttag(node, "a", "", **atts))


# Ákvarðar textann í sphinx_togglebutton (Default er "Click to show")
hint_indent = (
    r"\00a0" * 12
)  # Staðsetning textans er harðkóðuð í sphinx_togglebutton CSS-ið svo þurfum auka indent
togglebutton_hint = hint_indent + "Sýna" + r"\00a0" * 2


class EdbookAuthors(TypedDict):
    name: str
    email: str


class EdbookConfig(TypedDict):
    name: str
    description: str
    authors: List[EdbookAuthors]


def get_authors(config: EdbookConfig):
    year = date.today().year
    auth = config["authors"]  # Dict of authors and their emails
    print(auth[0]["name"])
    ############################### PROJECT ##############################
    project = config["description"]
    projectid = config["name"]
    # auth_title is the line with authors used in index.rst
    if auth[0]["name"] == None:  # No listed authors
        auth_title = "--"
    elif len(auth) == 1 and auth[0]["email"] != None:
        auth_title = (
            "Höfundur efnis: " + auth[0]["name"] + " <" + auth[0]["email"] + ">."
        )
    elif len(auth) == 1:
        auth_title = (
            "Höfundur efnis: " + auth[0]["name"] + "."
        )
    else:
        auth_title = "Höfundar efnis: "
        for a in auth:
            if a == auth[0]:  # First author
                auth_title += a["name"]
                if a["email"] != None:
                    auth_title += " <" + a["email"] + ">"
            elif a == auth[-1]:  # Last author
                auth_title += " og " + a["name"]
                if a["email"] != None:
                    auth_title += " <" + a["email"] + ">."
            else:  # All other
                auth_title += ", " + a["name"]
                if a["email"] != None:
                    auth_title += " <" + a["email"] + ">"
    copyright = f"{year}, {config['description']}"
    year = str(year)
    version = year  # The short X.Y version.
    release = year  # The full version, including alpha/beta/rc tags.
    return project, projectid, auth_title


def get_caller_path():
    for n in inspect.stack()[0]:
        if type(n) == str and get_projects_path() == Path(n).parent.resolve().parent:
            print(f"{get_projects_path()} | {Path(n).parent.resolve()}")
            return Path(n).parent.resolve()
    raise Exception("This should not happen, call the ambulance")


with open(Path.joinpath(get_caller_path() / "config.yml"), "r") as f:
    config: EdbookConfig = yaml.safe_load(f)
print(config)
project, projectid, auth_title = get_authors(config)

######################################################################

latex_documents = [
    (
        "index",
        str(os.path.split(os.getcwd())[1] + ".tex"),
        project,
        auth_title,
        "manual",
    ),
]

# Replace strings in rst files
rst_epilog = """
.. |auth_title| replace:: {auth_title}
.. |project| replace:: {project}
.. |projectid| replace:: {projectid}
""".format(
    auth_title=auth_title, project=project, projectid=projectid.upper()
)
