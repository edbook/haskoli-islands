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

from docutils.parsers.rst import Directive, directives
from Sphinx_ext import common, htmlform


class InstructorFeedbackDirective(Directive):
    """
    Directive to insert a form with a text area so that a instructor can submit
    feedback about any material to be considered later.

    .. instructor-feedback: id
       :button_name: default "Submit"
       :rows: Number of rows in the text window (10)
       :columns: same for columns (30)
       :text: Initial text to write in the window (@Your name@)

    Config params and default values:
    instructor_feedback_submit_button_name: 'Submit'
    instructor_feedback_rows: '10'
    instructor_feedback_columns: '30'
    instructor_feedback_text : ''
    """

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        "button_name": directives.unchanged,
        "rows": directives.positive_int,
        "columns": directives.positive_int,
        "text": directives.unchanged,
    }

    def run(self):
        config = self.state.document.settings.env.config

        # Submit button text
        button_name = common.get_parameter_value(
            config, self.options, "button_name", "instructor_feedback_submit_button_name", False
        )

        # Number of rows and columns in the text area
        rows = common.get_parameter_value(
            config, self.options, "rows", "instructor_feedback_rows", False
        )

        columns = common.get_parameter_value(
            config, self.options, "columns", "instructor_feedback_columns", False
        )

        # Get the path to the static directory containing the images
        p_to_static = common.get_relative_path_to_static(self.state.document)

        # Text to include in the form
        text = common.get_parameter_value(
            config, self.options, "text", "instructor_feedback_text", False
        )

        # Create the form node
        result = htmlform.HtmlForm(
            args=self.arguments, button_name=button_name, p_to_static=p_to_static
        )

        # Add an input field containing the event-name
        result += htmlform.HtmlInput(
            args=["event-name"],
            el_type="hidden",
            checked="",
            maxlength="",
            value="instructor-session-feedback",
        )

        # And the default text.
        result += htmlform.HtmlTextarea(args=["msg"], rows=rows, columns=columns, text=text)
        return [result]


def setup(app):
    app.add_directive("instructor-feedback", InstructorFeedbackDirective)

    app.add_config_value("instructor_feedback_submit_button_name", "Submit", True)
    app.add_config_value("instructor_feedback_text", "", True)
    app.add_config_value("instructor_feedback_rows", "10", True)
    app.add_config_value("instructor_feedback_columns", "30", True)
