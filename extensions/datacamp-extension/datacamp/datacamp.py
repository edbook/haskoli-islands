from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import ExtensionError
try:
    from sphinx.util.compat import Directive
except ImportError:
    from docutils.parsers.rst import Directive

"""
Datacamp extension:

Constructs datacamp nodes while reading through the .rst documents.
Upon finishing, the extension gathers all hidden code that has been written
for each site and constructs the html elements accordingly. That enables users
to declare 'global' variables that can be utilized between datacamp elements.
"""

class datacamp(nodes.General, nodes.Element):
	pass

class hidden_datacamp(nodes.General, nodes.Element):
	pass

def html_visit_datacamp_node(self, node):
	pass

def html_depart_datacamp_node(self, node):
	pass

def html_visit_hidden_datacamp_node(self, node):
	"""
	Construction of html elements while traversing through already created nodes and
	making adjustments accordingly
	"""
	language = node['lang'].lower()
	self.body.append('<div data-datacamp-exercise data-lang="'+language+'">')
	if node['library']:
		self.body.append('<code data-type="pre-exercise-code">')
		if language == 'python':
			for lib in node['library']:
				self.body.append('import ' + lib)
		else:
			for lib in library:
				self.body.append('library('+lib+')')
		if not node['hiddencode']:
			self.body.append('</code>')
	if node['hiddencode']:
		if not node['library']:
			self.body.append('<code data-type="pre-exercise-code">')
		for hid in node['hiddencode']:
			self.body.append(hid+"\n")
		self.body.append('</code>')
	self.body.append('<code data-type="sample-code">')
	self.body.append(node['code'])
	self.body.append('</code>')
	self.body.append('</div>')


def html_depart_hidden_datacamp_node(self, node):
	pass

def append_datacamp_hidden(app, doctree, fromdocname):
	#'Post production' adjustments
	if not app.builder.name == 'html':
		return

	env = app.builder.env
	for section in doctree.traverse(datacamp, ascend = False):
		current_file = section.__dict__['source'].split("\\")[-1]
		ishidden = section['hidden']

		newnode = hidden_datacamp()
		newnode['code'] = section['code']
		newnode['lang'] = section['lang']
		newnode['library'] = section['library']
		newnode['hiddencode'] = []

		if newnode['lang'] == 'python':
			newnode['hiddencode'] = env.datacamp_code_python[current_file]
		else:
			newnode['hiddencode'] = env.datacamp_code_r[current_file]

		if not ishidden:
			section.replace_self(newnode)


class DatacampDirective(Directive):
	has_content = True
	option_spec = {
		"lang": directives.unchanged,
		"library": directives.unchanged,
		"hidden": directives.unchanged
	}

	def run(self):
		env = self.state.document.settings.env

		lang = 'r'
		library = []
		hidden = False
		code = '\n'.join(self.content)
		filename = env.docname + ".rst"
		if not hasattr(env, 'datacamp_code_python'):
			env.datacamp_code_python = {}
		if not filename in env.datacamp_code_python:
			env.datacamp_code_python[filename] = []

		if not hasattr(env, 'datacamp_code_r'):
			env.datacamp_code_r = {}
		if not filename in env.datacamp_code_r:
			env.datacamp_code_r[filename] = []
		
		if 'lang' in self.options:
			lang = self.options.get('lang')
		if 'library' in self.options:
			library = self.options.get('library').split(', ')
		if 'hidden' in self.options:
			hidden = True
			if lang == 'python':
				env.datacamp_code_python[filename].append(code)
			else:
				env.datacamp_code_r[filename].append(code)
			
		node = datacamp()
		node['lang'] = lang
		node['library'] = library
		node['hidden'] = hidden
		node['code'] = code

		return [node]

def builder_inited(app):
	datapath = app.config.datacamp_path
	if not datapath:
		raise ExtensionError('datacamp_path config value must be set for the '
			'datacamp extension to work')
	if datapath:
		app.add_javascript(datapath)

def setup(app):
	app.add_node(datacamp, 
		html=(html_visit_datacamp_node, html_depart_datacamp_node))
	app.add_node(hidden_datacamp, 
		html=(html_visit_hidden_datacamp_node, html_depart_hidden_datacamp_node))
	app.add_config_value('datacamp_path', None, False)
	app.add_directive('datacamp', DatacampDirective)
	app.add_stylesheet('css/datacamp-custom.css')

	app.connect('builder-inited', builder_inited)
	app.connect('doctree-resolved', append_datacamp_hidden)
