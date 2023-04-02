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
# Authors: Abelardo Pardo (abelardo.pardo@sydney.edu.au)
#          Xavier Ochoa (xavier@cti.espol.edu.ec)
#

from __future__ import division

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from Sphinx_ext import common


class EmbeddedVideo(nodes.General, nodes.Element):
    pass


#
# TODO: Include event capturing for VIMEO
#       Check https://developer.vimeo.com/player/js-api
#
#
def visit_embedded_video_node(self, node):
    youtube_template = """<script type="text/javascript">
        array_video_embed['{0}'] = {{height: '{1}', width: '{2}',
        videoId: '{3}', playerVars: {{rel: 0{4}{5}}},
        events: {{'onStateChange': onPlayerStateChange}}}};</script>"""

    vimeo_template = """<iframe src="https://player.vimeo.com/video/{0}"
      width="{1}" height="{2}" id="{3}" frameborder="0" webkitallowfullscreen
        mozallowfullscreen allowfullscreen></iframe>"""

    # Initialize variables for start and end of segment
    start_str = ""
    end_str = ""

    # Get the argument
    video_id = node["args"][0]
    # If only start is set
    if len(node["args"]) >= 2:
        start_str = ", start: '{0}'".format(node["args"][1])
    # If start and end are set
    if len(node["args"]) == 3:
        end_str = ", end: '{0}'".format(node["args"][2])

    # Get the params
    elem_id = node["element_id"]
    height = node["height"]
    width = node["width"]
    vformat = node["format"].lower()  # Take the value in all lowercase

    # If it is the instructor guide, print the id
    if hasattr(self.builder.config, "iguide") and self.builder.config.iguide:
        self.body.append('<div class="embedded-video-id">')
        self.body.append("<strong>Video ID: %s</strong>" % video_id)
        self.body.append("</div>")

    # Deploy the div with the script inside
    self.body.append('<div id="%s" class="embedded-video">' % elem_id)

    # Emit code for the different video formats
    if vformat == "youtube":
        #
        # YOUTUBE
        #
        self.body.append(
            youtube_template.format(elem_id, height, width, video_id, start_str, end_str)
        )
    elif vformat == "vimeo":
        #
        # VIMEO
        #
        self.body.append(vimeo_template.format(video_id, width, height, elem_id))
    else:
        # Unknown video format, raise exception.
        raise Exception('Incorrect "format" value in embedded-video directive')

    self.body.append("</div>")


def depart_embedded_video_node(self, node):
    # Unused params
    del self, node


class EmbeddedVideoDirective(Directive):
    """
    Directive to embed a youtube video, deploy the API and track events on the
    video.

    .. embedded-video:: videoId
       :format: [youtube, vimeo]
       :height: value
       :width: value

    """

    has_content = False
    required_arguments = 1  # videoId
    optional_arguments = 2  # start end
    final_argument_whitespace = False
    option_spec = {
        "height": directives.nonnegative_int,
        "width": directives.nonnegative_int,
        "format": directives.unchanged,
    }

    def run(self):
        config = self.state.document.settings.env.config

        height = common.get_parameter_value(config, self.options, "height", "embedded_video_height")
        width = common.get_parameter_value(config, self.options, "width", "embedded_video_width")

        vformat = common.get_parameter_value(
            config, self.options, "format", "embedded_video_format"
        )

        element_id = "embedded-video-%s" % self.state.document.settings.env.new_serialno(
            "embedded-video"
        )

        return [
            EmbeddedVideo(
                args=self.arguments,
                element_id=element_id,
                height=height,
                width=width,
                format=vformat,
            )
        ]


def setup(app):
    app.add_node(EmbeddedVideo, html=(visit_embedded_video_node, depart_embedded_video_node))

    app.add_directive("embedded-video", EmbeddedVideoDirective)

    # Declare the three parameters for the directive. Any changes in any value
    # should fire the rebuild (thus the True as third parameter.
    app.add_config_value("embedded_video_height", 390, True)
    app.add_config_value("embedded_video_width", "100%", True)
    app.add_config_value("embedded_video_format", "youtube", True)
