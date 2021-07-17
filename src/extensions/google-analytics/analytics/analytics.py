# -*- coding: UTF-8-sig -*-

# google-analytics is a Sphinx Extension which embeds the Google Analytics tracking code and
# appends the Scrolldepth extension code snippet after each section in the document.

# Author: Símon Böðvarsson
# 17.08.2016
# Modified: Arnór Pétur Marteinsson
# 02.08.2018

from docutils import nodes, utils
from docutils.parsers.rst import Directive
from sphinx.application import ExtensionError

class scrolldepth_node(nodes.General, nodes.Element):
	pass

def add_tracking_code(app, pagename, templatename, context, doctree):
	if pagename == 'index':
		return

	analytics_id = app.config.ga_id

	script = context.get('scripttags', '')
	footer = context.get('footerscripttags', '')

	script += """
	<!-- Global site tag (gtag.js) - Google Analytics -->
	<script async src="https://www.googletagmanager.com/gtag/js?id="""+analytics_id+""""></script>
	<script>
		window.dataLayer = window.dataLayer || [];
		function gtag(){dataLayer.push(arguments);}
		gtag('js', new Date());
		gtag('config', '"""+analytics_id+"""');
	</script>
	"""
	script += "<script>top.scrolldepth_tags = []; </script>"

	footer += '<script src="_static/jquery.scrolldepth.js"></script>'
	
	if app.config.enable_custom_scrolldepth:
		footer += """
		<script>
			jQuery.scrollDepth({
			percentage: false,
			userTiming: false,
			pixelDepth: false,
			nonInteraction: false,
			elements: top.scrolldepth_tags
		}); 
		</script>
		"""
	else:
		footer += """
		<script>
			jQuery(function() {
				jQuery.scrollDepth();
			});
		</script>
		"""

	footer += """
	<script>
		function findIndex(proof,linkArray){ return linkArray.indexOf(proof) + 1 }

		$(".admonition-title > a").click(function(){
			var links = [];
			$(".admonition-title > a").each(function(index){
				var hrefArr = $( this ).text().split(" ")
				var hrefLower = hrefArr.map(v => v.toLowerCase())
				if(hrefLower.includes("sönnun")){
					links.push($( this ).attr("href"));
				}
			})

			if(links.includes($( this ).attr("href"))){
				gtag('event', 'click', {
				'event_category' : 'Toggle Proof',
				'event_label' : 'Chapter: '+ 
					$(document).attr('title').split('. ')[0] + ' - Proof: ' +
					findIndex($( this ).attr("href"), links)
				});
			}
		})

	</script>
	"""
	
	context['scripttags'] = script
	context['footerscripttags'] = footer

def html_scrolldepth_visit(self,node):
	pass

def html_scrolldepth_depart(self,node):
	self.body.append(node['snippet'])

def tex_scrolldepth_visit(self,node):
    pass

def tex_scrolldepth_depart(self,node):
	pass

def append_scrolldepth_nodes(app,doctree,fromdocname):
	if not app.builder.name == 'html':
		return

	if not app.config.enable_custom_scrolldepth:
		return

	# Create and insert scrolldepth nodes for each subsection.
	parent =  ""
	subsection_count = 0 
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

def builder_inited(app):
    if not app.config.ga_id:
        raise ExtensionError("'ga_id config value must be set for the "
			"google analytics extension to work'")

def setup(app):
    # Extension setup.
    app.add_node(scrolldepth_node, 
    	html = (html_scrolldepth_visit, html_scrolldepth_depart),
    	latex = (tex_scrolldepth_visit, tex_scrolldepth_depart))
    app.add_config_value('ga_id', '', 'html')
    app.add_config_value('enable_custom_scrolldepth', False, 'html')
    app.connect('builder-inited', builder_inited)
    app.connect('html-page-context', add_tracking_code)
    app.connect('doctree-resolved', append_scrolldepth_nodes)
    return{'version': '1.1'}