#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.compat import Directive


class ggb(nodes.General, nodes.Element):
    pass

def html_visit_ggb_node(self, node):
    self.body.append("<figure>")
    # ath gildi a breytum (rc, ai, sdz, ofl.)
    # snyrtilegra að nota % til að setja breytur inn
    self.body.append("<iframe src='https://tube.geogebra.org/material/iframe/id/"+node['id']+"/width/"+node['width']+"/height/"+node['height']+"/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/true/ld/false/sri/true/at/auto' width="+node['width']+" height="+node['height']+" frameborder='0'>")
    self.body.append("</iframe>")
    self.body.append("</figure>")

def html_depart_ggb_node(self, node):
    pass

def tex_visit_ggb_node(self, node):
    self.body.append("\n\n")
    self.body.append("\\begin{center}\n")
    self.body.append("\\includegraphics[width="+node['imgwidth']+",keepaspectratio=true]{"+node['img']+"}\n")
    self.body.append("\\end{center}")
    self.body.append("\n\n")

def tex_depart_ggb_node(self, node):
    pass

class GGB(Directive):
    has_content = True
    # verdum ad hafa 
    # haed, breidd, id, mynd, breidd myndar
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        "width": directives.unchanged,
        "height": directives.unchanged,
        "img": directives.unchanged,
        "imgwidth": directives.unchanged,
    }
    
    def run(self):
        node = ggb()
        node["id"] = self.arguments[0] 
        node["width"] = self.options.get("width")
        node["height"] = self.options.get("height")
        node["img"] = self.options.get("img")
        node["imgwidth"] = self.options.get("imgwidth") 
        
        return [node]

def setup(app):
    app.add_node(ggb,html = (html_visit_ggb_node, html_depart_ggb_node), latex = (tex_visit_ggb_node, tex_depart_ggb_node))
    app.add_directive('ggb',GGB)
    
