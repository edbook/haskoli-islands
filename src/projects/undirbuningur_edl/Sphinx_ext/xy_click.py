# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 The University of Sydney
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

import os

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from jinja2 import Template
from Sphinx_ext import common


class XyClickNode(nodes.General, nodes.Element):
    pass


def skip_visit(self, node):
    # Unused parameters
    del self, node


def visit_xy_click_node(self, node):
    # Get the xy_click ID from the enclosing activity or from the given
    # label
    element_id = node["args"][0]

    # Get the parameters
    title = node["title"]
    topleft_label = node["topleft_label"]
    top_label = node["top_label"]
    topright_label = node["topright_label"]
    bottomleft_label = node["bottomleft_label"]
    bottom_label = node["bottom_label"]
    bottomright_label = node["bottomright_label"]
    left_label = node["left_label"]
    right_label = node["right_label"]
    xy_size = node["size"]
    img_src = node["imgsrc"]
    img_path = os.path.join(node["p_to_static"], img_src)
    ok_path = os.path.join(node["p_to_static"], "Correct_20x20.png")

    with open("templates/xy_click.html.j2") as f:
        template = Template(f.read())
    snippet = template.render(
        element_id=element_id,
        title=title,
        topleft_label=topleft_label,
        top_label=top_label,
        topright_label=topright_label,
        left_label=left_label,
        img_path=img_path,
        xy_size=xy_size,
        ok_path=ok_path,
        right_label=right_label,
        bottomleft_label=bottomleft_label,
        bottom_label=bottom_label,
        bottomright_label=bottomright_label,
    )
    self.body.append(snippet)


def depart_xy_click_node(self, node):
    # Unused parameters
    del self, node


class XyClickDirective(Directive):
    """
    Directive to insert an image with a 2D cuadrant with four levels at the
    top, bottom, left and right, detect when the user
    clicks in the cuadrant and emit an event with the coordinates. The syntax
    is:

    .. xy-click:: xy-click-id
       :title: Title to put above the grid
       :top: North Label
       :bottom: South Label
       :left: East Label
       :right: West Label
       :size: 300px

    """

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        "title": directives.unchanged,
        "topleft": directives.unchanged,
        "top": directives.unchanged,
        "topright": directives.unchanged,
        "bottomleft": directives.unchanged,
        "bottom": directives.unchanged,
        "bottomright": directives.unchanged,
        "left": directives.unchanged,
        "right": directives.unchanged,
        "size": directives.unchanged,
        "imgsrc": directives.unchanged,
    }

    def run(self):
        config = self.state.document.settings.env.config

        # Get the labels
        title = common.get_parameter_value(config, self.options, "title", "xy_click_title", False)
        topleft_label = common.get_parameter_value(
            config, self.options, "topleft", "xy_click_topleft_label", False
        )
        top_label = common.get_parameter_value(
            config, self.options, "top", "xy_click_top_label", False
        )
        topright_label = common.get_parameter_value(
            config, self.options, "topright", "xy_click_topright_label", False
        )
        bottomleft_label = common.get_parameter_value(
            config, self.options, "bottomleft", "xy_click_bottomleft_label", False
        )
        bottom_label = common.get_parameter_value(
            config, self.options, "bottom", "xy_click_bottom_label", False
        )
        bottomright_label = common.get_parameter_value(
            config, self.options, "bottomright", "xy_click_bottomright_label", False
        )
        left_label = common.get_parameter_value(
            config, self.options, "left", "xy_click_left_label", False
        )
        right_label = common.get_parameter_value(
            config, self.options, "right", "xy_click_right_label", False
        )

        # Get the size
        grid_size = common.get_parameter_value(
            config, self.options, "size", "xy_click_grid_size", False
        )

        # Get the path to the static directory containing the images
        p_to_static = common.get_relative_path_to_static(self.state.document)

        # Get the path to the static directory containing the images
        imgsrc = common.get_parameter_value(
            config, self.options, "imgsrc", "xy_click_img_src", False
        )

        return [
            XyClickNode(
                args=self.arguments,
                title=title,
                topleft_label=topleft_label,
                top_label=top_label,
                topright_label=topright_label,
                bottomleft_label=bottomleft_label,
                bottom_label=bottom_label,
                bottomright_label=bottomright_label,
                left_label=left_label,
                right_label=right_label,
                size=grid_size,
                p_to_static=p_to_static,
                imgsrc=imgsrc,
            )
        ]


def setup(app):
    app.add_node(
        XyClickNode,
        html=(visit_xy_click_node, depart_xy_click_node),
        latex=(skip_visit, skip_visit),
        text=(skip_visit, skip_visit),
        man=(skip_visit, skip_visit),
        texinfo=(skip_visit, skip_visit),
    )

    # Declaring the directive
    app.add_directive("xy-click", XyClickDirective)

    #
    # CONFIGURATION
    #

    # Title to appear above the grid
    app.add_config_value("xy_click_title", None, True)
    # Labels to show at the top
    app.add_config_value("xy_click_topleft_label", "TOP LEFT LABEL", True)
    app.add_config_value("xy_click_top_label", "TOP LABEL", True)
    app.add_config_value("xy_click_topright_label", "TOP RIGHT LABEL", True)
    # Labels to show in the sides
    app.add_config_value("xy_click_left_label", "LEFT LABEL", True)
    app.add_config_value("xy_click_right_label", "RIGHT LABEL", True)
    # Labels to show at the bottom
    app.add_config_value("xy_click_bottomleft_label", "BOTTOM LEFT LABEL", True)
    app.add_config_value("xy_click_bottom_label", "BOTTOM LABEL", True)
    app.add_config_value("xy_click_bottomright_label", "BOTTOM RIGHT LABEL", True)
    # Grid size
    app.add_config_value("xy_click_grid_size", "400px", True)
    # Image file
    app.add_config_value("xy_click_img_src", "xy_grid_5x5.png", True)
