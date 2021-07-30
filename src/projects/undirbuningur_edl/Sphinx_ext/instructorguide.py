#!/usr/bin/env python
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

from __future__ import division

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.transforms import misc
from sphinx import addnodes
from sphinx.util.nodes import set_source_info


class InstructorGuideDirective(Directive):
    """
    Directive to insert content only for the instructor guide. The directive has
    two possible versions and relies on already existing nodes:

    .. iguide:: Instructor guide

    which is equivalent to:

    .. only:: iguide

       .. admonition:: Instructor guide
          :class: iguide

          TEXT GIVEN IN THE DIRECTIVE

    """

    has_content = True
    required_arguments = 1
    final_argument_whitespace = True

    def run(self):
        self.assert_has_content()

        node = addnodes.only()
        node.document = self.state.document
        set_source_info(self, node)
        node["expr"] = "iguide"

        text = "\n".join(self.content)
        admonition_node = nodes.admonition(text, **self.options)
        self.add_name(admonition_node)

        title_text = self.arguments[0]
        textnodes, messages = self.state.inline_text(title_text, self.lineno)
        admonition_node += nodes.title(title_text, "", *textnodes)
        admonition_node += messages
        admonition_node["classes"] += ["iguide"]

        self.state.nested_parse(self.content, self.content_offset, admonition_node)
        node += admonition_node

        return [node]


class InstructorGuideSectionDirective(Directive):
    """
    Directive to insert content only for the instructor guide. The directive has
    two possible versions and relies on already existing nodes:

    .. iguide-section:: label

    which is equivalent to:

    .. only:: iguide

       .. rst-class:: iguide objectives

       TEXT GIVEN IN THE DIRECTIVE

    """

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False

    def run(self):
        node = addnodes.only()
        node.document = self.state.document
        set_source_info(self, node)
        node["expr"] = "iguide"

        class_value = ["iguide", self.arguments[0]]

        pending = nodes.pending(
            misc.ClassAttribute, {"class": class_value, "directive": self.name}, self.block_text
        )
        self.state_machine.document.note_pending(pending)
        node += pending

        self.state.nested_parse(self.content, self.content_offset, node, match_titles=1)
        return [node]


def setup(app):
    app.add_directive("iguide", InstructorGuideDirective)
    app.add_directive("iguide-section", InstructorGuideSectionDirective)
