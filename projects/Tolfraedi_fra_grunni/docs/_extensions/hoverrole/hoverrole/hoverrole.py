# -*- coding: UTF-8-sig -*-

# The role :hover:`word,term` provides an inline highlight of 'word' with a mouse-over 
# translation from Icelandic to English of 'term' according to the stae.is/os database.
# In the case of :hover:`word`. The string 'term' is assumed to be the same as 'word'

# Author: Símon Böðvarsson
# 1.08.2016

from docutils import nodes, utils
from docutils.parsers.rst.roles import set_classes
from docutils.parsers.rst import Directive
import codecs
import os
import sys
from . import dictlookup

def hover_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    # app lets us access configuration settings and the parser as well as save
    # data for later use.
    app = inliner.document.settings.env.app
    transNum = app.config.hover_numOfTranslations
    htmlLink = app.config.hover_htmlLinkToStae
    latexLink = app.config.hover_latexLinkToStae
    latexIt = app.config.hover_latexItText
    translationList = app.config.hover_translationList

    # for text input of the form: "word,term"
    try:
        [word,term] = text.split(",")
        term = term.lstrip()
    # If no 'term' is provided, it is assumed to be the same as 'word'.
    except ValueError: 
        word=term=text

    node = make_hover_node(word,term,transNum,htmlLink,latexLink,latexIt)

    # Save the translated term to file for later use in hoverlist.
    if translationList:
        save_to_listfile('LIST_OF_HOVER_TERMS',node)        

    return [node],[]

def save_to_listfile(filename, node):
    try:
            newlinecontent = []
            newlinecontent.append(node['word'])
            newlinecontent.append(node['term'])
            newlinecontent.append(node['citationform'])
            for translation in node['translation']:
                newlinecontent.append(translation)
    except KeyError:
        return

    for no,item in enumerate(newlinecontent):
        # Make sure the strings are all str type and not bytes.
        if isinstance(item,bytes):
            newlinecontent[no] = item.decode('utf-8')

    newline = ";".join(newlinecontent)+"\n" 

    try:
        listfile = open(filename,'r')
    except IOError:
    # Create the file if it doesn't exist.
        createfile = open(filename,'w+')
        createfile.close()
        listfile = open(filename,'r')

    listcontents = listfile.readlines()
    listfile.close

    listcontents.insert(0,newline)

    listfile = open(filename,'w+')
    listcontents = "".join(listcontents)
    listfile.write(listcontents)
    listfile.close()
    return

def make_hover_node(word,term,transNum,htmlLink,latexLink,latexIt):
     # Create new hover object.
    hover_node = hover()
    hover_node['word'] = word
    hover_node['term'] = term

    # Get translation and citation form of term.
    dictentry = dictlookup.lookup(term)
    try:
        translation = dictentry[b'enTerm']
        hover_node['translation'] = translation
        hover_node['citationform'] = dictentry[b'isTerm']
    # If translation was not found create error message and code snippets.
    except KeyError:
        errormsg = 'Ekki fannst þýðing á hugtakinu: '
        html =  '<a class="tooltip" target="_blank">'+word+\
                '<span><staelink style="line-height:4px; font-size:80%;">'+errormsg+\
                '<i>'+term+'</i></staelink></span></a>'

        latex = word
        if latexIt:
            latex = '\\textit{' + latex + '}'
        if latexLink:
            searchURL = 'http://www.stae.is/os/leita/'+term.replace(" ","\_")
            latex = '\\href{' + searchURL +'}{' + word +'}'

        # Add the HTML and Latex code snippets to the node.
        hover_node['latexcode'] = latex
        hover_node['htmlcode'] = html
        return hover_node

    # If a translation was found create string with translations and HTML and Latex code snippets.
    tranStr = ''
    for transl in translation:
        tranStr = tranStr + transl.decode('utf-8') + ", "
    all_translations = tranStr[:-2] + "."
    single_translation = translation[0].decode('utf-8') + "."

    # HTML snippet
    html = '<a '
    if htmlLink:
        html = html + 'href="http://www.stae.is/os/leita/'+single_translation.replace(" ","_")
    if transNum == 'single':
        html = html + '" class="tooltip" target="_blank">'+word+'<span>en: <i>'+single_translation+'</i>'
    else: 
        hover_node['translation'] = all_translations
        html = html + '" class="tooltip" target="_blank">'+word+'<span>en: <i>'+all_translations+'</i>'
    if htmlLink:
        html = html + '<staelink style="font-size:80%;"><br><strong>Smelltu</strong> fyrir ítarlegri þýðingu.</staelink>'
    html = html + '</span></a>'

    # Latex snippet
    latex = word
    if latexIt:
        latex = '\\textit{' + latex + '}'
    if latexLink:
        urlTerm = single_translation.rstrip()
        searchURL = 'http://www.stae.is/os/leita/'+urlTerm.replace(" ","\_")
        latex = '\\href{' + searchURL[:-1] +'}{' + word +'}'

    # Add the HTML and Latex code snippets to the node.
    hover_node['latexcode'] = latex
    hover_node['htmlcode'] = html
    
    return hover_node

class hover(nodes.General, nodes.Element):
    pass
    

def html_hover_visit(self,node):
    pass 

def html_hover_depart(self,node):
    self.body.append(node['htmlcode'])

def tex_hover_visit(self,node):
    pass

def tex_hover_depart(self,node):
    self.body.append(node['latexcode'])


class hoverlist(nodes.General, nodes.Element):
    pass


class HoverListDirective(Directive):

    def run(self):
        return[hoverlist('')]

def create_hoverlist(app,doctree, fromdocname):
     # If translationlists are set to not appear, replace them with empty nodes.
    if not app.config.hover_translationList:
        for node in doctree.traverse(hoverlist):
            if not app.config.hover_translationList:
                node.replace_self([])
        return
    
    # Words is a dictionary with translated terms as keys and translations as values.
    words = {}
    content = []

    #with codecs.open("LIST_OF_HOVER_TERMS", encoding = "utf-8") as listfile:
    listfile = open("LIST_OF_HOVER_TERMS",'r')
    listcontents = listfile.readlines()
    listfile.close()

    for line in listcontents:
        # Clean up the strings.
        line = line.split(";")
        for idx,entry in enumerate(line):
            beginindex = entry.find("'")
            newentry = entry[beginindex+1:]
            line[idx] = newentry

        citationform = line[2]
        translation = line[3]

        if citationform in words:
            continue
        words[citationform] = translation

    # Add words and translations (sorted) to nodes.
    for key,value in sorted(words.items()):
        wordnode = nodes.emphasis(key,key)
        translationstring = " : " + value

        # Add linebreak if smaller version of list is used.
        if app.config.hover_miniTranslationList:
            translationstring += "\n"

        translationnode = nodes.Text(translationstring)

        # If the larger version of list is requested, create new paragraph.
        if not app.config.hover_miniTranslationList:
            para = nodes.paragraph()
        # If the smaller version of list is requested, create a new line.
        else:
            para = nodes.line()
        # Append the line/paragraph.
        para += wordnode 
        para += translationnode
        content.append(para)

    # Replace all hoverlist nodes with the translations
    for node in doctree.traverse(hoverlist):
        # If hover_translation userconfig is set to 0 remove all hoverlist nodes.
        if not app.config.hover_translationList:
            node.replace_self([])
            continue 
        node.replace_self(content)
    return 

def delete_hoverlist(app,doctree):
    if app.config.hover_translationList:
        try:
            listfile = open('LIST_OF_HOVER_TERMS','w+')
            emptystring = ""
            listfile.write(emptystring)
            listfile.close()
        except:
            print("Could not write over contents in: 'LIST_OF_HOVER_TERMS'",
                " for unknown reasons. User may need to erase contents manually.")
    else:
        pass
    return

def setup(app):
    # Extension setup.
    
    # Number of translations to be displayed. The default 'single' displays only the first
    # found translation,  'all' displays all.
    app.add_config_value('hover_numOfTranslations','single','html')
    # Set to default ('1') if hover target should link to stae.is search for the translated term.
    # Set to '0' if no link should be attached.
    app.add_config_value('hover_htmlLinkToStae',1,'html')
    app.add_config_value('hover_latexLinkToStae',0,'env')
    # Should the text be italicized in latex output. '1' for on, '0' for off.
    app.add_config_value('hover_latexItText',1,'env')

    # Should a list of translations be created (default '1')
    app.add_config_value('hover_translationList',1,'env')
    # Enable for a smaller version of the list of translations.
    app.add_config_value('hover_miniTranslationList',0,'env')

    app.add_node(hover, html = (html_hover_visit, html_hover_depart), latex = (tex_hover_visit, tex_hover_depart))
    app.add_role('hover',hover_role)

    app.add_node(hoverlist)
    app.add_directive('hoverlist',HoverListDirective)
    app.connect('doctree-resolved', create_hoverlist)
    app.connect('build-finished',delete_hoverlist)
    return{'version': '1'}