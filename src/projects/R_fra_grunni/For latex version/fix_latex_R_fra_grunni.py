# This script was made for python 3.7, other versions might have bugs!
import re
import sys

########## This version of this script is for the book 'R frá grunni' only! ###########

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
    re.compile(r'(\\usepackage\{babel\})'): r'\1\n\\usepackage{svg}',
    # Changing the includegraphics command to one that supports svg files
    # Note: To shrink oversized images, I needed to force the size of ALL svg images
    # to a given size (here: 400pt). This number can be changed as you see fit!
    re.compile(r'sphinxincludegraphics(\{\{.*?\}\.svg\})'): 'includesvg[width=400pt]\\1',
    # The '\maketitle' command has been redifined and is messing up the command
    # after it (here: \sphinxtableofcontents). We add a newline so that the next command
    # is merely an empty line and even though pdflatex asks for input, it is safe to continue!
    re.compile(r'(\\maketitle)'): '\\1\n',
    # package 'hyperref' is loaded twice for some reason...? Get rid of the second one!
    re.compile(r'(\\usepackage\{amssymb\})\n\\usepackage\{hyperref\}'): '\\1',
    # 'H' forces images to appear exactly where they are in the text
    re.compile(r'\\begin\{figure\}\[htbp\]'): r'\\begin{figure}[H]',


    ### Issues specifically to do with 'R frá grunni' ###
    # pdflatex does not like '"}' at the end of a sphinxupquote command.
    # We add some fluff so that the two symbols are not side by side!
    re.compile(r'(sphinxupquote\{.*?")(\}\})'): r'\1\\hspace{0 mm}\2',

    # Adding package to be able to display 'keyboard keys'
    re.compile(r'(\\usepackage\{geometry\})'): r'\1\n\\usepackage{menukeys}',
    # Fixing the unicode characters used to display 'keyboard keys'
    re.compile(r'\\sphinxcode{\\sphinxupquote\{⌘\}\}'): r'\\keys{\\cmd}',
    re.compile(r'\\sphinxcode{\\sphinxupquote\{⏎\}\}'): r'\\keys{\\return}',
    re.compile(r'\\sphinxcode{\\sphinxupquote\{Ctrl\}\}'): r'\\keys{\\ctrl}',

    # Inserting settings for R code chunks
    re.compile(r'( \\fi\n\\fi\n)(\\usepackage\{cmap\})'): r'\1\n% For R syntax highlighting\n\\usepackage[svgnames]{xcolor}\n\\usepackage{listings}\n\\lstset{\n  language=R,                       % the language of the code\n  %basicstyle=\\tiny\\ttfamily,       % the size of the fonts that are used for the code\n  numbers=left,                     % where to put the line-numbers\n  numberstyle=\\color{Blue},         % the style that is used for the line-numbers\n  stepnumber=1,                     % the step between two line-numbers. If it is 1, each line\n                                    % will be numbered\n  numbersep=5pt,                    % how far the line-numbers are from the code\n  backgroundcolor=\\color{white},    % choose the background color. You must add\\usepackage{color}\n  showspaces=false,                 % show spaces adding particular underscores\n  showstringspaces=false,           % underline spaces within strings\n  showtabs=false,                   % show tabs within strings adding particular underscores\n  frame=single,                     % adds a frame around the code\n  rulecolor=\\color{black},          % if not set, the frame-color may be changed on line-breaks\n                                    % within not-black text (e.g. comments (green here))\n  tabsize=2,                        % sets default tabsize to 2 spaces\n  captionpos=b,                     % sets the caption-position to bottom\n  breaklines=true,                  % sets automatic line breaking\n  breakatwhitespace=false,          % sets if automatic breaks should only happen at whitespace\n  keywordstyle=\\color{RoyalBlue},   % keyword style\n  commentstyle=\\color{YellowGreen}, % comment style\n  stringstyle=\\color{ForestGreen}   % string literal style\n}\n\n\2',



    # 'sub': 'dub'
}


f = open(sys.argv[1], encoding='utf8')
filedata = f.read()
f.close()

# Doing the actual replacing
newdata = replace_all(filedata, reps)

# Saving the finished product
f = open(sys.argv[2], 'w')
f.write(''.join(newdata))
f.close()
