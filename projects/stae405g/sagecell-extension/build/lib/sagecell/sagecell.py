#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.compat import Directive



class sagecell(nodes.General, nodes.Element): 
    pass


def html_visit_sagecell_node(self, node):
    # the code is either in R, Sage or Octave
    # if auto is True the code is run automatically (without having to press evaluation button)
    # if hidecode is True the code is not displayed 
    if node["lang"] == "r":
        if node["auto"]:
            if node["hidecode"]:
                self.body.append("<div class='rsageAutoHidden'>")
            else:
                self.body.append("<div class='rsageAuto'>")
        else:
            self.body.append("<div class='rsage'>")
    
    elif node["lang"] == "octave":
        if node["auto"]:
            if node["hidecode"]:
                self.body.append("<div class='osageAutoHidden'>")
            else:
                self.body.append("<div class='osageAuto'>")
        else:
            self.body.append("<div class='osage'>")

    else:        
        if node["auto"]:
            if node["hidecode"]:
                self.body.append("<div class='sageAutoHidden'>")
            else:
                self.body.append("<div class='sageAuto'>")
        else:
            self.body.append("<div class='sage'>")

    self.body.append("<script type='text/x-sage'>")	    
    self.body.append(node['code'])    
    self.body.append("</script>")    
    self.body.append("</div>")	


def html_depart_sagecell_node(self, node):
    pass


def latex_visit_sagecell_node(self, node):
    # If "latexcode" is True the code is displayed verbatim, 
    # Then an image of the outcome isi displayed if an image file was given.
    if node["latexcode"]:
        self.body.append("\n\n")
        self.body.append("\\begin{verbatim}\n")
        self.body.append(node['code'])
        self.body.append("\n\end{verbatim}")
        self.body.append("\n\n")

    if node["img"] != None:
        self.body.append("\n\n")
        self.body.append("\\begin{center}\n")
        self.body.append("\\includegraphics[width="+node['imgwidth']+",keepaspectratio=true]{"+node['img']+"}\n")
        self.body.append("\n\end{center}")

def latex_depart_sagecell_node(self, node):
    pass


class SageCell(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 7
    option_spec = {
        "codefile": directives.unchanged,
        "lang": directives.unchanged,
        "auto": directives.unchanged,
        "hidecode": directives.unchanged,
        "latexcode": directives.unchanged,
        "img": directives.unchanged,
        "imgwidth": directives.unchanged,
    }
	
    def run(self):              
 
        if "codefile" in self.options:
            codefile = self.options.get("codefile")
            f = open(codefile,'r')
            code = f.read()
        else:
            code = '\n'.join(self.content)

        if "lang" in self.options:
            lang = self.options.get("lang")
        else: 
            lang = "sage"

        if "auto" in self.options:
            auto = True
        else: 
            auto = False
        
        if "hidecode" in self.options:
            hidecode = True
        else: 
            hidecode = False

        if "latexcode" in self.options:
            latexcode = True
        else: 
            latexcode = False

        if "img" in self.options:
            img = self.options.get("img")
        else:
            img = None

        if "imgwidth" in self.options:
            imgwidth = self.options.get("imgwidth")
        else:
            imgwidth = "8cm"

        content_list = self.content

        node = sagecell()  
        node['code'] = code     
        node['lang'] = lang
        node['auto'] = auto
        node['hidecode'] = hidecode  
        node['latexcode'] = latexcode
        node['img'] = img
        node['imgwidth'] = imgwidth
    
        return [node]		


def setup(app):
    app.add_node(sagecell, html = (html_visit_sagecell_node, html_depart_sagecell_node), latex = (latex_visit_sagecell_node, latex_depart_sagecell_node))
    app.add_directive("sagecell", SageCell)



