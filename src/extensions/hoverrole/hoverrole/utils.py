import logging
import os
from logging.config import dictConfig
from pathlib import Path
from typing import Optional, Union

import coloredlogs
from jinja2 import (
    Environment,
    FileSystemLoader,
    PackageLoader,
    Template,
    select_autoescape,
)

SEARCH_URL = "https://www.stae.is/os/leita/{}"

jinja2_env = Environment(loader=PackageLoader("hoverrole"), autoescape=select_autoescape())


def configure_logger(name):
    level = os.getenv("LOG_LEVEL", "INFO")
    fmt = "%(name)s(%(lineno)d): [%(levelname)s] %(message)s"
    styles = coloredlogs.DEFAULT_FIELD_STYLES | {
        "levelname": {"bold": True, "color": "blue", "faint": True}
    }
    logger = logging.getLogger(name)
    coloredlogs.install(fmt=fmt, field_styles=styles, level=level, logger=logger)
    return logger


def get_first_term(terms: Union[list, str]) -> str:
    if terms and isinstance(terms, list):
        return terms[0]
    return terms


def serialize(items: list) -> str:
    if items and isinstance(items, list):
        return ", ".join(items)
    return items


def urlify(item: str, split_char: str = "_") -> str:
    term = get_first_term(item).replace(" ", split_char)
    return SEARCH_URL.format(term)


def get_html(
    tpl: str, word: str, terms: list, html_link: bool = False, stae_index: bool = None
) -> str:
    if stae_index == None:
        term: str = serialize(terms)
        url: Optional[str] = urlify(terms) if html_link else None
    else:
        term: str = terms[stae_index]
        url: Optional[str] = SEARCH_URL.format(term) if html_link else None
    template = jinja2_env.get_template(tpl)
    return template.render(word=word, term=term, url=url)


def get_latex(latexIt: bool, latexLink: bool, word: str, term: str) -> str:
    if latexIt:
        return f"\\textit{{{word}}}"
    if latexLink:
        url = urlify(term, "\_")
        return f"\\href{{{url}}}{{{word}}}"
    return word


def get_translations_file():
    # TODO: add to extension config
    return "LIST_OF_HOVER_TERMS.json"
