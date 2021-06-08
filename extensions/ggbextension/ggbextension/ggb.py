#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import directives
import string
import random
try:
    from sphinx.util.compat import Directive
except ImportError:
    from docutils.parsers.rst import Directive


class ggb(nodes.General, nodes.Element):
    pass

def html_visit_ggb_node(self, node):
    #Construct random ID string 62^30
    lst = [random.choice(string.ascii_letters + string.digits) for n in range(30)]
    ID = "".join(lst)
    self.body.append("<div id=\""+ID+"\"></div>\n")
    self.body.append("<script>\n")
    self.body.append("var ggbApp_"+ID+" = new GGBApplet({\n")
    self.body.append("\"appName\": \"graphing\", \n")
    self.body.append("\"width\": "+node['width']+", \n")
    self.body.append("\"height\": "+node['height']+", \n")
    self.body.append("\"material_id\":\" "+node['id']+"\", \n")
    self.body.append("\"preventFocus\": true, \n")
    self.body.append("\"enableShiftDragZoom\": "+node['zoom_drag']+" \n")
    self.body.append("}, true);\n")
    self.body.append("ggbAppletId[\""+ID+"\"] = ggbApp_"+ID+";\n")
    self.body.append("</script>")

def html_depart_ggb_node(self, node):
    pass

def tex_visit_ggb_node(self, node):
    if node["img"] != None:
        self.body.append("\n\n")
        self.body.append("\\begin{center}\n")
        self.body.append("\\includegraphics[width="+node['imgwidth']+",keepaspectratio=true]{"+node['img']+"}\n")
        self.body.append("\\end{center}")
        self.body.append("\n\n")

def tex_depart_ggb_node(self, node):
    pass

class GGB(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 5
    final_argument_whitespace = False
    option_spec = {
        "width": directives.unchanged,
        "height": directives.unchanged,
        "img": directives.unchanged,
        "imgwidth": directives.unchanged,
        "zoom_drag": directives.unchanged,
    }
    
    def run(self):
        node = ggb()
        node["id"] = self.arguments[0] 
        node["width"] = self.options.get("width", "700")
        node["height"] = self.options.get("height", "400")
        node["img"] = self.options.get("img", None)
        node["imgwidth"] = self.options.get("imgwidth", "8cm") 
        node["zoom_drag"] = self.options.get("zoom_drag", "false")
        
        return [node]

def setup(app):
    app.add_node(ggb,html = (html_visit_ggb_node, html_depart_ggb_node), latex = (tex_visit_ggb_node, tex_depart_ggb_node))
    app.add_directive('ggb',GGB)
