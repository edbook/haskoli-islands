#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
# Copyright (C) 2014 The University of Sydney
# Original author: Abelardo Pardo (abelardo.pardo@sydney.edu.au)
#
# This project is based upon the work on the Reauthoring toolkit
# Author: Naeka
#

from __future__ import unicode_literals

from docutils import nodes
from docutils.parsers.rst import roles, Directive
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from docutils.parsers.rst.roles import set_classes


class EqtAnswerType(nodes.General, nodes.Element):
    pass


def visit_eqt_answer_type_node(self, node):
    """
    Function executed when the node representing the :eqt:`XXX` is visited.
    """
    # Need to check for the MODE!
    if node['type'] == 'eqt' or node['type'] == 'eqt-mc':
        if node['type'] == 'eqt':
            input_type = 'radio'
        else:
            input_type = 'checkbox'

        self.body.append('<label>')
        self.body.append(
            '<input type="{}" name="question" value="{}" />'.format(
                input_type, node['content']))

    if node['type'] == 'eqt-fib':
        self.body.append("""
            <div class="eqt-fib-answer">
                Réponse :
                <input type="text" name="answer" value="" data-answer="{}"/>
            </div>
        """.format(node['content']))
    raise nodes.SkipNode


def non_html_visit_node(self, node):
    raise nodes.SkipNode


class Eqt(nodes.General, nodes.Element):
    pass


def visit_eqt_node(self, node):
    """
    Function executed when the node representing .. eqt:: fff is visited.
    """
    if node['name'] == 'eqt-fib':
        mode = 'fill-in-blank'
    elif node['name'] == 'eqt-mc':
        mode = 'multiple'
    else:
        mode = 'regular'

    self.body.append(
        '<div class="eqt-block" id="{}" data-mode="{}">'.format(
            node["args"][0], mode))
    self.body.append('<form class="eqt-block-questions">')


def depart_eqt_node(self, node):
    """
    Function executed when the node representing .. eqt:: fff is left
    """
    # Need to check for the MODE!

    self.body.append('</form>')
    self.body.append('<div class="eqt-block-actions">')
    self.body.append(
        '<input class="eqt-actions eqt-grade btn btn-neutral" type="button" '
        'value="Évaluer"/>')
    self.body.append(
        '<input class="eqt-actions eqt-again btn btn-neutral" type="button" '
        'value="Réessayer"/>')
    self.body.append(
        '<input class="eqt-actions eqt-solution btn btn-neutral" '
        'type="button" value="Solution"/>')
    self.body.append('<span class="result-icon"></span>')
    self.body.append('</div>')
    self.body.append('</div>')


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

        if config.config_values.get('eqt_question_type') is not None:
            raise ValueError("Embedded questions cannot be nested.")

        # Store the type of question in an additional attribute in the
        # environment.
        config.config_values['eqt-question-type'] = self.name

        p_to_static = ''
        result = Eqt(args=self.arguments,
                     name=self.name,
                     p_to_static=p_to_static)

        # Parse the nested content
        self.state.nested_parse(self.content, self.content_offset, result)

        # Remove the question type from the environment
        del config.config_values['eqt-question-type']

        # If the question is a single MCQ, check that there is an enumerated
        # list and perform some additional tasks.
        if self.name == "eqt" or self.name == "eqt-mc":
            # Loop over the question children to detect which one corresponds
            # to the list of answers and add some additional attributes
            answer_list_node = None
            for question_child in result.children:
                if question_child.__class__.__name__ != 'enumerated_list':
                    continue

                # Try ot obtain the eqt_answer_type. If it fails, we are
                # processing a regular node so we keep processing children
                name = question_child.children[0].children[0].children[
                    0].__class__.__name__
                if name == 'EqtAnswerType':
                    answer_list_node = question_child
                    break

            if answer_list_node is not None:
                answer_list_node['enumtype'] = \
                    answer_list_node['enumtype'] + ' eqt-answer-list'
            else:
                raise ValueError('No answer list found in e-question.')

        return [result]


def eqt_answer(name, rawtext, text, lineno, inliner, options=None,
               content=None):
    """
    Function executed with the role :eqt:`???` is parsed
    """

    # Unused parameters
    del name, rawtext, lineno, content

    # Get the question type (if none, raise an exception).
    config = inliner.document.settings.env.config
    question_type = config.config_values.get('eqt-question-type')
    if question_type is None:
        raise ValueError('Role :eqt: must appear inside an embedded question.')

    # Single answer MCQ
    if question_type == 'eqt':
        # The value of the role can only be C or I (correct or incorrect)
        if text != 'C' and text != 'I':
            raise ValueError('Role text must be "C" or "I"')

    # Get the relative path to the static directory
    p_to_static = ''

    return [
        EqtAnswerType(args=options, type=question_type, content=text,
                      p_to_static=p_to_static)
    ], []


def explanation_role(name, rawtext, text, lineno, inliner, options={},
                     content=[]):
    """
    Function executed with the role :expl: is parsed
    """
    # Unused parameters
    del name, rawtext, lineno, content

    # Get the question type (if none, raise an exception).
    config = inliner.document.settings.env.config
    question_type = config.config_values.get('eqt-question-type')
    if question_type is None:
        raise ValueError(
            'Role :expl: must appear inside an embedded question.')

    # Get the relative path to the static directory
    p_to_static = ''

    return [
        Explanation(args=options, content=text, p_to_static=p_to_static)
    ], []


class Explanation(nodes.General, nodes.Element):
    pass


class ESolutionDirective(BaseAdmonition):
    node_class = nodes.admonition

    def run(self):
        set_classes(self.options)
        self.assert_has_content()
        text = '\n'.join(self.content)
        admonition_node = self.node_class(text, **self.options)
        self.add_name(admonition_node)
        title_text = "Solution"
        textnodes, messages = self.state.inline_text(title_text, self.lineno)
        title = nodes.title(title_text, '', *textnodes)
        admonition_node += title
        admonition_node += messages
        admonition_node['classes'] += ['tip', 'expl']
        self.state.nested_parse(
            self.content, self.content_offset, admonition_node)
        return [admonition_node]


def visit_explanation_node(self, node):
    """
    Function executed when the node representing the :expl:`XXX` is visited
    """
    self.body.append(
        '<div class="admonition tip expl" style="display: none;">'
        '{}</div>'.format(node["content"]))
    raise nodes.SkipNode


def setup(app):
    app.add_node(
        Eqt,
        html=(visit_eqt_node, depart_eqt_node),
        latex=(non_html_visit_node, None),
        text=(non_html_visit_node, None),
        man=(non_html_visit_node, None),
        texinfo=(non_html_visit_node, None)
    )

    app.add_directive("eqt", EQuestionDirective)
    app.add_directive("eqt-fib", EQuestionDirective)
    app.add_directive("eqt-mc", EQuestionDirective)
    app.add_directive("eqt-solution", ESolutionDirective)

    roles.register_local_role('eqt', eqt_answer)
    roles.register_local_role('expl', explanation_role)

    app.add_node(
        EqtAnswerType,
        html=(visit_eqt_answer_type_node, None),
        latex=(non_html_visit_node, None),
        text=(non_html_visit_node, None),
        man=(non_html_visit_node, None),
        texinfo=(non_html_visit_node, None)
    )
    app.add_node(
        Explanation,
        html=(visit_explanation_node, None),
        latex=(non_html_visit_node, None),
        text=(non_html_visit_node, None),
        man=(non_html_visit_node, None),
        texinfo=(non_html_visit_node, None)
    )

    app.add_stylesheet('css/eqt.css')
    app.add_javascript('js/eqt.js')
