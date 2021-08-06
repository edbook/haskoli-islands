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

import os
import sys

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from Sphinx_ext import common


class ActivityDuration(nodes.General, nodes.Element):
    pass


def skip_visit(self, node):
    # Function to skip the processing of the entire directive
    # Unused params
    del self, node


def visit_activity_duration_node(self, node):
    # Get the duration ID either from the enclosing activity or from the given
    # label
    if len(node["args"]) == 2:
        duration_id = node["args"][1]
    else:
        duration_id = common.get_enclosing_activity_id(node)
        if duration_id is None:
            print("Error in file", node.source, "line", node.line)
            print("activity-duration must have an id as second argument")
            print("or be part of a section labeled with the directive")
            print(".. rst-class:: activity")
            sys.exit(1)

    try:
        duration_value = int(node["args"][0])
    except ValueError:
        print("Error in file", node.source, "line", node.line)
        print("The duration directive must have a number as first parameter.")
        sys.exit(1)

    # Get the parameters
    phrase = node["phrase"]

    self.body.append('<div class="reauthoring_duration_select">')
    self.body.append("<form>")

    self.body.append(phrase)

    # Subject and Verb values and activity id
    self.body.append('<input type="hidden" name="duration-id" value="%s"/>' % duration_id)

    # Value of the duration
    self.body.append('<select name="duration-value">')
    value = int(duration_value / 2)
    self.body.append("<option selected disabled>Select a value</option>")
    self.body.append(
        '<option value="LT-%s/%s">Less than %s</option>' % (value, duration_value, value)
    )
    self.body.append('<option value="%s/%s">%s</option>' % (value, duration_value, value))
    value = int(duration_value * 3 / 4)
    self.body.append('<option value="%s/%s">%s</option>' % (value, duration_value, value))

    self.body.append(
        '<option value="%s/%s">%s</option>' % (duration_value, duration_value, duration_value)
    )
    value = int(duration_value * 5 / 4)
    self.body.append('<option value="%s/%s">%s</option>' % (value, duration_value, value))
    value = int(duration_value * 3 / 2)
    self.body.append('<option value="%s/%s">%s</option>' % (value, duration_value, value))
    self.body.append(
        '<option value="GT-%s/%s">More than %s</option>' % (value, duration_value, value)
    )
    self.body.append("<select> mins.")

    # Submit button
    self.body.append('<button class="reauthoring_duration_submit">Ok</button>')
    self.body.append("</form>")
    self.body.append(
        '<img class="duration_ok_icon" style="display: none;" src="%s"></img>'
        % os.path.join(node["p_to_static"], "Correct_20x20.png")
    )
    self.body.append("</div>")


def depart_activity_duration_node(self, node):
    # Unused params
    del self, node


class ActivityDurationDirective(Directive):
    """
    Directive to insert a form to catch the duration of an activity. The syntax
    is:

    .. activity-duration:: id [expected]
       :phrase: phrase to put before the text (default in config var)

    The following configuration variables are also accepted:
    - activity_duration_phrase: phrase to include before the duration
                                default is How long did this activity take you?
    """

    has_content = True
    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = False
    option_spec = {"phrase": directives.unchanged}

    def run(self):
        config = self.state.document.settings.env.config

        # Phrase to prefix the value
        phrase = common.get_parameter_value(
            config, self.options, "phrase", "activity_duration_phrase", False
        )

        # Get the path to the static directory containing the images
        p_to_static = common.get_relative_path_to_static(self.state.document)

        return [ActivityDuration(args=self.arguments, phrase=phrase, p_to_static=p_to_static)]


def setup(app):
    app.add_node(
        ActivityDuration,
        html=(visit_activity_duration_node, depart_activity_duration_node),
        latex=(skip_visit, skip_visit),
        text=(skip_visit, skip_visit),
        man=(skip_visit, skip_visit),
        texinfo=(skip_visit, skip_visit),
    )

    # Declaring the directive
    app.add_directive("activity-duration", ActivityDurationDirective)

    #
    # CONFIGURATION
    #

    # Phrase to precede the value
    app.add_config_value("activity_duration_phrase", "How long did this activity take you?", True)
