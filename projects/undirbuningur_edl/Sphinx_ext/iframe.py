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

import sys

from docutils import nodes
from docutils.parsers.rst import Directive


class IFrame(nodes.General, nodes.Element):
    pass


def skip_visit(self, node):
    # Unused parameters
    del self, node


def visit_iframe_node(self, node):
    element = """<iframe class="reauthoring" id="%s" src="%s" width="100%%"
                  height="200px" marginheight="0"></iframe>"""

    # Get the frame ID as first argument and the URL as second argument
    if len(node["args"]) != 2:
        print("Error in file", node.source, "line", node.line)
        print("iframe must have an id and a URL as arguments")
        sys.exit(1)

    self.body.append(element % (node["args"][0], node["args"][1]))


def depart_iframe_node(self, node):
    # Unused parameters
    del self, node


class IFrameDirective(Directive):
    """
    Directive to insert an iframe with an id and a URL. The syntax
    is:

    .. iframe:: id URL

    """

    has_content = False
    required_arguments = 2
    optional_arguments = 0
    final_argument_whitespace = False

    def run(self):
        return [IFrame(args=self.arguments)]


def setup(app):
    app.add_node(
        IFrame,
        html=(visit_iframe_node, depart_iframe_node),
        latex=(skip_visit, skip_visit),
        text=(skip_visit, skip_visit),
        man=(skip_visit, skip_visit),
        texinfo=(skip_visit, skip_visit),
    )

    # Declaring the directive
    app.add_directive("iframe", IFrameDirective)
