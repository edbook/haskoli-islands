# The role :hover:`word,term` provides an inline highlight of 'word' with a mouse-over
# translation from Icelandic to English of 'term' according to the stae.is/os database.
# In the case of :hover:`word`. The string 'term' is assumed to be the same as 'word'

# Author: Símon Böðvarsson
# 1.08.2016

import json
from pathlib import Path
from typing import List, TypedDict

from docutils import nodes
from docutils.parsers.rst import Directive
from jinja2 import Template

from . import dictlookup
from .utils import (
    configure_logger,
    get_html,
    get_latex,
    get_translations_file,
    serialize,
)

logger = configure_logger(__name__)


class HoverType(TypedDict):
    word: str
    term: str
    citationform: str
    translation: str


class hover(nodes.General, nodes.Element):
    pass


class hoverlist(nodes.General, nodes.Element):
    pass


class HoverListDirective(Directive):
    def run(self):
        return [hoverlist("")]


def hover_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    # app lets us access configuration settings and the parser as well as save
    # data for later use.
    app = inliner.document.settings.env.app
    transNum = app.config.hover_numOfTranslations
    htmlLink = app.config.hover_htmlLinkToStae
    latexLink = app.config.hover_latexLinkToStae
    latexIt = app.config.hover_latexItText
    translationList = app.config.hover_translationList

    # for text input of the form: "word,term"
    split_text = text.split(",")
    stae_index = None
    if len(split_text) == 3:
        word, term, stae_index = split_text
        stae_index = int(stae_index) - 1  # indexum frá 1 en ekki 0
        term = term.lstrip()
    elif len(split_text) == 2:
        word, term = split_text
        term = term.lstrip()
    else:
        word = term = text

    node = make_hover_node(word, term, transNum, htmlLink, latexLink, latexIt, stae_index)
    # Save the translated term to file for later use in hoverlist.
    if translationList:
        save_to_listfile(get_translations_file(), node)

    return [node], []


def save_to_listfile(filename: str, node: hover):
    try:
        hover_obj: HoverType = {
            "word": node["word"],
            "term": node["term"],
            "citationform": node["citationform"],
            "translation": node["translation"],
        }
    except KeyError:
        return

    f = Path(filename)
    f.touch(exist_ok=True)
    data = f.read_text(encoding="utf-8")

    if not data:
        data = []
    else:
        data = json.loads(data)
    data.append(hover_obj)
    Path(filename).write_text(
        json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False), encoding="utf-8",
    )
    return


def make_hover_node(word, term, transNum, htmlLink, latexLink, latexIt, stae_index):
    # Create new hover object.
    hover_node = hover()
    hover_node["word"] = word
    hover_node["term"] = term

    # Get translation and citation form of term.
    dictentry = dictlookup.lookup(term)
    try:
        translation = dictentry["enTerm"]
        hover_node["translation"] = translation
        hover_node["citationform"] = dictentry["isTerm"]

    # If translation was not found create error message and code snippets.
    except KeyError:
        hover_node["htmlcode"] = get_html("not_found.html", word, term,)
        hover_node["latexcode"] = get_latex(latexIt, latexLink, word, term)
        return hover_node

    if stae_index == None:
        hover_node["translation"] = serialize(translation)
        hover_node["htmlcode"] = get_html("translation.html", word, translation, htmlLink)
    else:
        hover_node["translation"] = translation[stae_index]
        hover_node["htmlcode"] = get_html(
            "translation.html", word, translation, htmlLink, stae_index
        )
    hover_node["latexcode"] = get_latex(latexIt, latexLink, word, translation)

    return hover_node


def html_hover_visit(self, node):
    pass


def html_hover_depart(self, node):
    self.body.append(node["htmlcode"])


def tex_hover_visit(self, node):
    pass


def tex_hover_depart(self, node):
    self.body.append(node["latexcode"])


def create_hoverlist(app, doctree, fromdocname):
    # If translationlists are set to not appear, replace them with empty nodes.
    if not app.config.hover_translationList:
        for node in doctree.traverse(hoverlist):
            if not app.config.hover_translationList:
                node.replace_self([])
        return

    # Words is a dictionary with translated terms as keys and translations as values.
    words = {}
    content = []
    data: List[HoverType] = json.loads(Path(get_translations_file()).read_text())

    for item in data:
        if item["citationform"] in words:
            continue
        words[item["citationform"]] = item["translation"]

    # Add words and translations (sorted) to nodes.
    for key, value in sorted(words.items()):
        wordnode = nodes.emphasis(key, key)
        translationstring = " : " + value

        # Add linebreak if smaller version of list is used.
        if app.config.hover_miniTranslationList:
            translationstring += "\n"

        translationnode = nodes.Text(translationstring)

        # If the larger version of list is requested, create new paragraph.
        if not app.config.hover_miniTranslationList:
            para = nodes.paragraph()
        # If the smaller version of list is requested, create a new line.
        else:
            para = nodes.line()
        # Append the line/paragraph.
        para += wordnode
        para += translationnode
        content.append(para)

    # Replace all hoverlist nodes with the translations
    for node in doctree.traverse(hoverlist):
        # If hover_translation userconfig is set to 0 remove all hoverlist nodes.
        if not app.config.hover_translationList:
            node.replace_self([])
            continue
        node.replace_self(content)
    return


def delete_hoverlist(app, doctree):
    if app.config.hover_translationList:
        filename = get_translations_file()
        try:
            with open(filename, "a+") as f:
                f.truncate()
        except:
            logger.error(
                f"Could not write over contents in: '{filename}' for unknown"
                " reasons. User may need to erase contents manually.",
            )
    else:
        pass
    return


def setup(app):
    # Extension setup.

    # Number of translations to e displayed. The default 'single' displays only the first
    # found translation,  'all' displays all.
    app.add_config_value("hover_numOfTranslations", "single", "html")
    # Set to default ('1') if hover target should link to stae.is search for the translated term.
    # Set to '0' if no link should e attached.
    app.add_config_value("hover_htmlLinkToStae", 1, "html")
    app.add_config_value("hover_latexLinkToStae", 0, "env")
    # Should the text e italicized in latex output. '1' for on, '0' for off.
    app.add_config_value("hover_latexItText", 1, "env")

    # Should a list of translations e created (default '1')
    app.add_config_value("hover_translationList", 1, "env")
    # Enable for a smaller version of the list of translations.
    app.add_config_value("hover_miniTranslationList", 0, "env")
    app.add_config_value("hover_outputFile", "translations.json", "env")

    app.add_node(
        hover,
        html=(html_hover_visit, html_hover_depart),
        latex=(tex_hover_visit, tex_hover_depart),
    )
    app.add_role("hover", hover_role)

    app.add_node(hoverlist)
    app.add_directive("hoverlist", HoverListDirective)
    app.connect("doctree-resolved", create_hoverlist)
    app.connect("build-finished", delete_hoverlist)
    return {"version": "1"}
