#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
from datetime import date
from pathlib import Path

sys.path.insert(0, os.path.abspath("."))
sys.path.append(os.path.abspath("../../settings"))

from settings import *
import yaml

with open(Path.joinpath(Path(__file__).parent / "config.yml"), "r") as f:
    config = yaml.safe_load(f)
year = date.today().year

#################### PROJECT ######################
project = config["description"]
projectid = config["name"]
copyright = f"{year}, {config['description']}"
author = f"{config['author']} <{config['email']}>"
year = str(year)
version = year  # The short X.Y version.
release = year  # The full version, including alpha/beta/rc tags.
###################################################

texinfo_documents = [
    (
        "index",
        projectid,
        project,
        author,
        projectid,
        "One line description of project.",
        "Miscellaneous",
    ),
]

latex_documents = [
    (
        "index",
        str(os.path.split(os.getcwd())[1] + ".tex"),
        project,
        author,
        "manual",
    ),
]

# Replace strings in rst files
rst_epilog ="""
.. |author| replace:: {author}
.. |project| replace:: {project}
.. |projectid| replace:: {projectid}
.. |email| replace:: {email}
""".format(author=config['author'],project=project,projectid=projectid.upper(),email=config['email'])
