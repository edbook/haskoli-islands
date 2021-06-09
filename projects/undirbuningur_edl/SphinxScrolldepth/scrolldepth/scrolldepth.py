# -*- coding: UTF-8-sig -*-

# SpinxScrolldepth is a Sphinx Extension which appends the Scrolldepth Google Analytics extension 
# code snippet after each section in the document. See scrolldepth.parsnip.io. 

# Author: Símon Böðvarsson
# 17.08.2016

from docutils import nodes, utils
from docutils.parsers.rst import Directive

class scrolldepth_node(nodes.General, nodes.Element):
	pass

def html_scrolldepth_visit(self,node):
	pass

def html_scrolldepth_depart(self,node):
	self.body.append(node['snippet'])

def tex_scrolldepth_visit(self,node):
    pass

def tex_scrolldepth_depart(self,node):
	pass

def append_scrolldepth_nodes(app,doctree,fromdocname):
	if not app.builder == 'html':
		return
	# Create and insert scrolldepth nodes for each subsection.
	parent =  ""
	subsection_count = 1 
	for section in doctree.traverse(nodes.section, ascend = False):
		if parent == "":
			parent = section
		if section.parent == parent:
			subsection_count +=1
			div_id = 'scrolled_to_section_%d' %subsection_count
			snippet = "<div id='" + div_id + "' > " 
			snippet += "<script> top.scrolldepth_tags.push('#"+div_id+"'); </script>"
			newnode = scrolldepth_node()
			newnode['snippet'] = snippet
			section.append(newnode)

def setup(app):
    # Extension setup.
    app.add_node(scrolldepth_node, 
    	html = (html_scrolldepth_visit, html_scrolldepth_depart),
    	latex = (tex_scrolldepth_visit, tex_scrolldepth_depart))
    app.connect('doctree-resolved', append_scrolldepth_nodes)
    return{'version': '1.0'}