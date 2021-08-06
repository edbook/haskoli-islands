#!/usr/bin/python
import re
import sys

########## This version of this script is for the book 'Tölfræði frá grunni' only! ###########

# Replace method
def replace_all(text, dic):
    for i, j in dic.items():
        if type(i) == str:
            text = text.replace(i, j)
        else:
            text = i.sub(j, text)
    return text


# Dictionaries with our find:replace values.
reps = {
    # Adding the svg package
    re.compile(r"(\\usepackage\{babel\})"): r"\1\n\\usepackage{svg}",
    # Changing the includegraphics command to one that supports svg files
    # Note: To shrink oversized images, I needed to force the size of ALL svg images
    # to a given size (here: 400pt). This number can be changed as you see fit!
    re.compile(r"sphinxincludegraphics(\{\{.*?\}\.svg\})"): "includesvg[width=400pt]\\1",
    # The '\maketitle' command has been redifined and is messing up the command
    # after it (here: \sphinxtableofcontents). We add a newline so that the next command
    # is merely an empty line and even though pdflatex asks for input, it is safe to continue!
    re.compile(r"(\\maketitle)"): "\\1\n",
    # package 'hyperref' is loaded twice for some reason...? Get rid of the second one!
    re.compile(r"(\\usepackage\{amssymb\})\n\\usepackage\{hyperref\}"): "\\1",
    # 'H' forces images to appear exactly where they are in the text
    re.compile(r"\\begin\{figure\}\[htbp\]"): r"\\begin{figure}[H]",
    ### Issues specifically to do with 'Tölfræði frá grunni' ###
    # One picture is 'side-by-side' with a table, and we must scale it differently
    re.compile(
        r"sphinxincludegraphics\[width=2.000\\linewidth\](\{\{.*?\}\.svg\})"
    ): "includesvg[width=300pt]\\1",
    ### Issues specifically to do with 'R frá grunni' ###
    # pdflatex does not like '"}' at the end of a sphinxupquote command.
    # We add some fluff so that the two symbols are not side by side!
    # re.compile(r'(sphinxupquote\{.*?")(\}\})'): '\\1\\hspace{0 mm}\\2',
    # 'sub': 'dub'
}


f = open(sys.argv[1], encoding="utf8")
filedata = f.read()
f.close()

# Doing the actual replacing
newdata = replace_all(filedata, reps)

# Saving the finished product
f = open(sys.argv[2], "w")
f.write("".join(newdata))
f.close()
