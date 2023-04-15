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

# auth_title is the line with authors in index.rst
auth = config["authors"] # Dict of authors and their emails 

if len(auth) == 1:
    auth_title = "Höfundur efnis: " + auth[1]['name'] + " <" + auth[1]['email'] + ">."
else: 
    auth_title = "Höfundar efnis: "
    for a in auth:
        if a == auth[0]: # First author
            auth_title += a['name'] + " <" + a['email'] + ">"
        elif a == auth[-1]:  # Last author
            auth_title += " og " + a['name'] + " <" + a['email'] + ">."
        else: # All other
            auth_title += ", " + a['name'] + " <" + a['email'] + ">"

#################### PROJECT ######################
project = config["description"]
projectid = config["name"]
copyright = f"{year}, {config['description']}"
author = f"{config['author']} <{config['email']}>"
year = str(year)
version = year  # The short X.Y version.
release = year  # The full version, including alpha/beta/rc tags.
###################################################

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
.. |auth_title| replace:: {auth_title}
.. |project| replace:: {project}
.. |projectid| replace:: {projectid}
""".format(auth_title=auth_title,project=project,projectid=projectid.upper())
