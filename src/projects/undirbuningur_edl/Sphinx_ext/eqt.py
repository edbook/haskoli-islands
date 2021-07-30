# virkar betur

# !/usr/bin/env pythona
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

import posixpath

from docutils import nodes
from docutils.parsers.rst import Directive, roles
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from docutils.parsers.rst.roles import set_classes
from Sphinx_ext import common


class EqtAnswerType(nodes.General, nodes.Element):
    pass


def visit_eqt_answer_type_node(self, node):
    """
    Function executed when the node representing the :eqt:`XXX` is visited
    """
    # Need to check for the MODE!
    if node["type"] == "eqt" or node["type"] == "eqt-mc":
        if node["type"] == "eqt":
            input_type = "radio"
        else:
            input_type = "checkbox"

        is_correct = node["content"] == "C"

        self.body.append(
            '<input type="%s" name="question" value="%s" />' % (input_type, node["content"])
        )

        if is_correct:
            self.body.append('  <img class="result_icon" ')
            self.body.append('style="display: none;"')
            self.body.append(
                '       src="%s"></img>' % posixpath.join(node["p_to_static"], "Correct_20x20.png")
            )
        else:
            self.body.append('  <img class="result_icon" ')
            self.body.append('style="display: none;"')
            self.body.append(
                '       src="%s"></img>'
                % posixpath.join(node["p_to_static"], "Incorrect_20x20.png")
            )

        # If in instructor mode, write the solution of the question
        if hasattr(self.builder.config, "iguide") and self.builder.config.iguide:
            if node["content"] == "C":
                self.body.append("<strong>[Rétt!]</strong>")
            else:
                self.body.append("<strong>[Rangt]</strong>")
        return

    if node["type"] == "eqt-fib":
        self.body.append('<div class="reauthoring_embedded_quiz-fib-answer">')
        self.body.append("Answer")
        self.body.append('<input type="text" name="question" value=""/>')
        self.body.append('<input type="hidden" name="solution" ')
        self.body.append('value="%s"/>' % node["content"])

        # If in instructor mode, write the solution
        if hasattr(self.builder.config, "iguide") and self.builder.config.iguide:
            self.body.append(" <strong>[%s]</strong>" % node["content"])

        self.body.append("</div>")
        return

    # If we reached this point in the function, there is a question type that is
    # new and has no corresponding code here!
    raise ValueError("Directive " + node["type"] + " has not been implemented")


def depart_eqt_answer_type_node(self, node):
    """
    Function executed when the node representing the :eqt:`XXX` is left
    """
    # Unused parameters
    del self, node


class Eqt(nodes.General, nodes.Element):
    pass


def visit_eqt_node(self, node):
    """
    Function executed when the node representing .. eqt:: fff is visited.
    """
    # Need to check for the MODE!

    suffix = ""
    if node["name"] == "eqt-fib":
        suffix = "-fib"
    elif node["name"] == "eqt-mc":
        suffix = "-mc"

    self.body.append(
        '<div class="reauthoring_embedded_quiz%s" id="%s">' % (suffix, node["args"][0])
    )
    self.body.append('<form class="reauthoring_embedded_quiz_questions">')


def depart_eqt_node(self, node):
    """
    Function executed when the node representing .. eqt:: fff is left
    """
    # Need to check for the MODE!

    self.body.append("</form>")
    self.body.append('<div class="reauthoring_embedded_quiz_buttons">')
    self.body.append('<input class="reauthoring_quiz_button reauthoring-grade" ')
    self.body.append('       style="display:none;" ')
    self.body.append('       type="button" value="Athuga svar" />')
    self.body.append('<input class="reauthoring_quiz_button reauthoring-again" ')
    self.body.append('       style="display:none;" ')
    self.body.append('       type="button" value="Reyna aftur" />')
    self.body.append('<input class="reauthoring_quiz_button reauthoring-solution" ')
    self.body.append('       style="display:none;" ')
    self.body.append('       type="button" value="Sýna svör" />')
    self.body.append('  <img class="correct_icon" style="opacity: 0;"')
    self.body.append(
        '       src="%s"></img>' % posixpath.join(node["p_to_static"], "Correct_20x20.png")
    )
    self.body.append('  <img class="incorrect_icon" style="opacity: 0;"')
    self.body.append(
        '       src="%s"></img>' % posixpath.join(node["p_to_static"], "Incorrect_20x20.png")
    )
    self.body.append('<span class="reauthoring-embedded-answer"></span>')
    self.body.append("</div>")

    # If it is the instructor guide, print the id
    if hasattr(self.builder.config, "iguide") and self.builder.config.iguide:
        self.body.append('<div class="reauthoring_embedded_quiz_eqtid">')
        self.body.append("<strong>Question ID: %s </strong>" % node["args"][0])
        self.body.append("</div>")

    self.body.append("</div>")


class EQuestionDirective(Directive):
    """
    Directive to insert a (single answer) multiple choice embedded question.
    The run method is executed when the .. directive is found when parsing.
    The syntax is:

    .. eqt:: question-id

       Text describing the question

       - :eqt:`C` Answer number 1 (which is correct)
       - :eqt:`I` Answer number 2 (which is incorrect)
       - :eqt:`I` Answer number 3 (which is incorrect)
       - :eqt:`I` Answer number 4 (which is incorrect)
    """

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False

    def run(self):
        # Raise an error if the directive does not have contents.
        self.assert_has_content()

        config = self.state.document.settings.env.config

        if config.config_values.get("eqt_question_type") is not None:
            raise ValueError("Embedded questions cannot be nested.")

        # Store the type of question in an additional attribute in the
        # environment.
        config.config_values["eqt-question-type"] = self.name

        p_to_static = common.get_relative_path_to_static(self.state.document)
        result = Eqt(args=self.arguments, name=self.name, p_to_static=p_to_static)

        # Parse the nested content
        self.state.nested_parse(self.content, self.content_offset, result)

        # Remove the question type from the environment
        del config.config_values["eqt-question-type"]

        # If the question is a single MCQ, check that there is an enumerated
        # list and perform some additional tasks.
        if self.name == "eqt" or self.name == "eqt-mc":
            # Loop over the question children to detect which one corresponds to
            # the list of answers and add some additional attributes
            answer_list_node = None
            for question_child in result.children:
                if question_child.__class__.__name__ != "enumerated_list":
                    continue

                # Try ot obtain the eqt_answer_type. If it fails, we are
                # processing a regular node so we keep processing children
                name = question_child.children[0].children[0].children[0].__class__.__name__
                if name == "EqtAnswerType":
                    answer_list_node = question_child
                    break

            if answer_list_node is not None:
                answer_list_node["enumtype"] = answer_list_node["enumtype"] + " eqt-answer-list"
            else:
                raise ValueError("No answer list found in e-question.")

        return [result]


def eqt_answer(name, rawtext, text, lineno, inliner, options=None, content=None):
    """
    Function executed with the role :eqt:`???` is parsed
    """

    # Unused parameters
    del name, rawtext, lineno, content

    # This role has only effect when in HTML mode.
    if inliner.document.settings.env.app.builder.format != "html":
        return

    # Get the question type (if none, raise an exception).
    config = inliner.document.settings.env.config
    question_type = config.config_values.get("eqt-question-type")
    if question_type is None:
        raise ValueError("Role :eqt: must appear inside an embedded question.")

    # Single answer MCQ
    if question_type == "eqt":
        # The value of the role can only be C or I (correct or incorrect)
        if text != "C" and text != "I":
            raise ValueError('Role text must be "C" or "I"')

    # Get the relative path to the static directory
    p_to_static = common.get_relative_path_to_static(inliner.document)

    return [
        EqtAnswerType(args=options, type=question_type, content=text, p_to_static=p_to_static)
    ], []


def explanation_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Function executed with the role :expl: is parsed
    """
    # Unused parameters
    del name, rawtext, lineno, content

    # This role has only effect when in HTML mode.
    if inliner.document.settings.env.app.builder.format != "html":
        return

    # Get the question type (if none, raise an exception).
    config = inliner.document.settings.env.config
    question_type = config.config_values.get("eqt-question-type")
    if question_type is None:
        raise ValueError("Role :expl: must appear inside an embedded question.")

    # Get the relative path to the static directory
    p_to_static = common.get_relative_path_to_static(inliner.document)

    return [Explanation(args=options, content=text, p_to_static=p_to_static)], []


class Explanation(nodes.General, nodes.Element):
    pass


class ESolutionDirective(BaseAdmonition):
    node_class = nodes.admonition

    def run(self):
        set_classes(self.options)
        self.assert_has_content()
        text = "\n".join(self.content)
        admonition_node = self.node_class(text, **self.options)
        self.add_name(admonition_node)
        title_text = "Lausn"
        textnodes, messages = self.state.inline_text(title_text, self.lineno)
        title = nodes.title(title_text, "", *textnodes)
        admonition_node += title
        admonition_node += messages
        admonition_node["classes"] += ["expl", "tip"]
        self.state.nested_parse(self.content, self.content_offset, admonition_node)
        return [admonition_node]


def visit_explanation_node(self, node):
    """
    Function executed when the node representing the :expl:`XXX` is visited
    """
    self.body.append('<div class="tip expl admonition">%s</div>' % node["content"])
    return


def depart_explanation_node(self, node):
    """
    Function executed when the node representing the :expl:`XXX` is left
    """
    # Unused parameters
    del self, node


def setup(app):
    app.add_node(Eqt, html=(visit_eqt_node, depart_eqt_node))

    app.add_directive("eqt", EQuestionDirective)
    app.add_directive("eqt-fib", EQuestionDirective)
    app.add_directive("eqt-mc", EQuestionDirective)
    app.add_directive("eqt-solution", ESolutionDirective)

    roles.register_local_role("eqt", eqt_answer)
    roles.register_local_role("expl", explanation_role)

    app.add_node(EqtAnswerType, html=(visit_eqt_answer_type_node, depart_eqt_answer_type_node))
    app.add_node(Explanation, html=(visit_explanation_node, depart_explanation_node))
