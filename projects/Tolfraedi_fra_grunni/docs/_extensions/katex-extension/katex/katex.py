# -*- coding: utf-8 -*-
from docutils import nodes

import sphinx
from sphinx.locale import _
from sphinx.errors import ExtensionError
from sphinx.ext.mathbase import setup_math as mathbase_setup
from sphinx.ext.mathbase import get_node_equation_number

def get_latex(node):
    if 'latex' in node.attributes:
        return node['latex'] 
    else:
        return node.astext()


def html_visit_math(self, node):
    self.body.append(self.starttag(node, 'span', '', CLASS='math'))
    self.body.append(self.builder.config.katex_inline[0] +
                     self.encode(get_latex(node)) +
                     self.builder.config.katex_inline[1] + '</span>')
    raise nodes.SkipNode


def html_visit_displaymath(self, node):
    self.body.append('<div style="text-align: center;">\n')
    
    if node['number']:
        self.body.append(self.starttag(node, 'div', CLASS='math', STYLE='display:inline-block;'))
    else:
        self.body.append(self.starttag(node, 'div', CLASS='math'))

    if node['nowrap']:
        self.body.append(self.encode(get_latex(node)))
        self.body.append('</div>')
        raise nodes.SkipNode


    self.body.append(self.builder.config.katex_display[0])
    latex = get_latex(node)
    parts = [prt for prt in latex.split('\n\n') if prt.strip()]

    if len(parts) > 1:  # Add alignment if there are more than 1 equation
        self.body.append(r' \begin{aligned}')

    for i, part in enumerate(parts):
        part = self.encode(part)
        aligned = part[7:14] == "aligned"
        if r'\\' in part and not aligned:
            self.body.append(r'\begin{aligned}' + part + r'\end{aligned}')
        else:
            self.body.append(part)
        if i < len(parts) - 1:  # append new line if not the last equation
            self.body.append(r'\\')

    if len(parts) > 1:  # Add alignment if there are more than 1 equation
        self.body.append(r'\end{aligned} ')

    self.body.append(self.builder.config.katex_display[1])
    self.body.append('</div>\n')

    if node['number']:
        number = get_node_equation_number(self, node)
        self.body.append('<h6 class="eqno">(%s)' % number)
        self.add_permalink_ref(node, _('Varanlegur hlekkur'))
        self.body.append('</h6>')

    self.body.append('</div>\n')
    raise nodes.SkipNode

try:
    basestring
except:
    basestring = str
    
def builder_inited(app):
    katexpath = app.config.katex_path
    renderpath = app.config.katex_render
    mathpath = app.config.render_math

    if not katexpath:
        raise ExtensionError('katex_path config value must be set for the '
                             'katex extension to work')
    elif not renderpath:
        raise ExtensionError('katex_render config value must be set for the '
                             'katex extension to work')    
    elif not mathpath:
        raise ExtensionError('render_math config value must be set for the '
                             'katex extension to work')                        

    if katexpath and renderpath and mathpath:
        app.add_javascript(katexpath)
        app.add_javascript(renderpath)
        app.add_javascript(mathpath)
    
    if app.config.katex_css:
        app.add_stylesheet(app.config.katex_css)

      
def setup(app):
    try:
        mathbase_setup(app, (html_visit_math, None), (html_visit_displaymath, None))
    except ExtensionError:
        raise ExtensionError('katex.katex: other math package is already loaded')


    app.add_config_value('katex_path', None, False)
    app.add_config_value('katex_render', None, False)
    app.add_config_value('render_math', None, False)

    app.add_config_value('katex_css', None, 'html')
    app.add_config_value('katex_inline', [r'\(', r'\)'], 'html')
    app.add_config_value('katex_display', [r'\[', r'\]'], 'html')

    app.connect('builder-inited', builder_inited)

    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}