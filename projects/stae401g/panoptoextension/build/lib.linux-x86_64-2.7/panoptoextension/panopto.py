#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.compat import Directive


class panopto(nodes.General, nodes.Element):
    pass

def html_visit_panopto_node(self, node):
    self.body.append("<figure>")
    self.body.append("<iframe src='https://rec.hi.is/Panopto/Pages/Embed.aspx?id="+node['id']+"' width="+node['width']+" height="+node['height']+" style=padding: 0px; border: 1px solid #464646; frameborder='0'>")
    self.body.append("</iframe>")
    self.body.append("</figure>")


def tex_visit_panopto_node(self, node):
    if node["img"] != None:
        self.body.append("\n\n")
        self.body.append("\\begin{center}\n")
        self.body.append("\\includegraphics[width="+node['imgwidth']+",keepaspectratio=true]{"+node['img']+"}\n")
        self.body.append("\\end{center}")
        self.body.append("\n\n")


def html_depart_panopto_node(self, node):
    pass


def tex_depart_panopto_node(self, node):
    pass

class PANOPTO(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 2
    final_argument_whitespace = False
    option_spec = {
        "width": directives.unchanged,
        "height": directives.unchanged,
    }
    
    def run(self):
        node = panopto()
        node["id"] = self.arguments[0] 
        node["width"] = self.options.get("width", "700")
        node["height"] = self.options.get("height", "400")


        
        return [node]

def setup(app):
    app.add_node(panopto,html = (html_visit_panopto_node, html_depart_panopto_node), latex = (tex_visit_panopto_node, tex_depart_panopto_node))
    app.add_directive('panopto',PANOPTO)
