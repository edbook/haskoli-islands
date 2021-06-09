#!/usr/bin/python
import os
import sys
import fileinput



# Replace method 
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text
 
# Dictionary with our find:replace values.
reps = { 
	'\\begin {frame}':'\\begin{frame}',
	'\\begin{frame}{':'\subsection{',  
	'\\end{frame}':'',
	'\\end {frame}':'',
	'\\begin{block}':'\subsubsection',
	'\\begin {block}':'\subsubsection', 
	'\\end{block}':'',
	'\\end {block}':'',
	'\\begin{theorem}':'\subsubsection',
	'\\begin {theorem}':'\subsubsection', 
	'\\end{theorem}':'',
	'\\end {theorem}':'',
	'\\begin{definition}':'\subsubsection',
	'\\begin {definition}':'\subsubsection', 
	'\\end{definition}':'',
	'\\end {definition}':'',
	'\\begin{proof}':'\subsubsection',
	'\\begin {proof}':'\subsubsection', 
	'\\end{proof}':'',
	'\\end {proof}':'',
	'\\begin{proposition}':'\subsubsection',
	'\\begin {proposition}':'\subsubsection', 
	'\\end{proposition}':'',
	'\\end {proposition}':'',
	'\\begin{frame}':'\subsection{}', 
#	'sub':'dub'
}


f = open(sys.argv[1])
filedata = f.read()
f.close()

#newdata = filedata.replace("frame","cra")
newdata = replace_all(filedata,reps)

f = open(sys.argv[2],'w')
f.write(newdata)
f.close()
