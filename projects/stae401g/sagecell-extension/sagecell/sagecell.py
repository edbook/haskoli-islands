#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes
from sphinx.errors import ExtensionError
from docutils.parsers.rst import directives
try:
    from sphinx.util.compat import Directive
except ImportError:
    from docutils.parsers.rst import Directive


class sagecell(nodes.General, nodes.Element): 
    pass

def construct_sage_div(hidden, auto, plang, self, node):
    #constructs opening tags according to programming language inputs
    if node["auto"]:
        if node["hidecode"]:
            self.body.append("<div class='"+hidden+"'>")
        else:
            self.body.append("<div class='"+auto+"'>")
    else:
        self.body.append("<div class='"+plang+"'>")

def html_visit_sagecell_node(self, node):
    # the code is either in R, Sage, Octave or Python
    # if auto is True the code is run automatically (without having to press evaluation button)
    # if hidecode is True the code is not displayed 
    language = node["lang"].lower()
    if language == "r":
        construct_sage_div('rsageAutoHidden','rsageAuto','rsage',self,node)
    
    elif language == "octave":
        construct_sage_div('osageAutoHidden','osageAuto','osage',self,node)

    elif language == "python":
        construct_sage_div('psageAutoHidden','psageAuto','psage',self,node)

    else:
        construct_sage_div('sageAutoHidden','sageAuto','sage',self,node)        

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
        self.body.append("\\includegraphics[width="+node['imgwidth']+
            ",keepaspectratio=true]{"+node['img']+"}\n")
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

def builder_inited(app):
    jquerypath = app.config.sage_jquery_path
    sagepath = app.config.sage_path
    customsagepath = app.config.custom_sage_path
    if not jquerypath:
        raise ExtensionError('sage_jquery_path config value must be set for the '
            'sagecell extension to work')
    elif not sagepath:
        raise ExtensionError('sage_path config value must be set for the '
            'sagecell extension to work')
    elif not customsagepath:
        raise ExtensionError('custom_sage_path config value must be set for the '
            'sagecell extension to work')
    if jquerypath and sagepath and customsagepath:
        app.add_javascript(jquerypath)
        app.add_javascript(sagepath)
        app.add_javascript(customsagepath)

def setup(app):
    app.add_node(sagecell, html = (html_visit_sagecell_node, html_depart_sagecell_node), latex = (latex_visit_sagecell_node, latex_depart_sagecell_node))
    app.add_config_value('sage_jquery_path', None, False)
    app.add_config_value('sage_path', None, False)
    app.add_config_value('custom_sage_path', None, False)
    app.add_directive('sagecell', SageCell)
    app.connect('builder-inited', builder_inited)



