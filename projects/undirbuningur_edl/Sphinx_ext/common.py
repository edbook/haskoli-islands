#!/usr/bin/env pythona
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 The University of Sydney
# This file is part of the Reauthoring toolkit

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor
# Boston, MA  02110-1301, USA.
#
# Author: Abelardo Pardo (abelardo.pardo@sydney.edu.au)
#

import os
import posixpath


def get_relative_path_to_static(document):
    docname = document.get("source")
    srcdir = document.settings.env.srcdir
    # build_suffix = os.path.dirname(docname).replace(srcdir, '')
    build_suffix = os.path.dirname(docname)[len(srcdir) :]
    if build_suffix != "":
        build_suffix = build_suffix[1:]

    builder = document.settings.env.app.builder
    build_dir = os.path.join(builder.outdir, build_suffix)
    static_dir = os.path.join(builder.outdir, "_static")

    # Relpath is to obtain the correct path from one file to the other and it
    # should be OS dependent. However, once we obtain this, we need to
    # translate the relative path to a valid URL, that is why we use
    # posixpath
    return posixpath.join(*os.path.relpath(static_dir, build_dir).split("\\"))


def get_parameter_value(config, options, key, config_key, enforce_set=True):
    value = options.get(key, None)
    if value is None:
        value = config[config_key]
        if enforce_set and value is None:
            raise ValueError("Unset config var " + config_key)
    return value


def get_enclosing_activity_id(node):
    """
    Function that traverses the tree upwards through the parent relationship
    until a node is detected with the "activity" and "section" classes. When
    found, it returns the IDs attribute. None if not found.
    """
    start = node
    while (
        "activity" not in start.attributes["classes"] or start.tagname != "section"
    ) and start.parent is not None:
        start = start.parent

    if "activity" in start.attributes["classes"] and start.tagname == "section":
        return start.attributes["ids"][0]

    return None
