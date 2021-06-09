This extension defines a directive 'sagecell' which allows to embedd sage cell inside sphinx doc. To learn more about sage cell server visit: http://aleph.sagemath.org/static/about.html


Installation
=========
   1. Install this extension: 
        'python(3) setup.py build'
        'sudo python(3) setup.py install' OR 'python(3) setup.py install --user'
   2. Move 'layout.html' to your '_templates' directory. Change sagecell paths if necessary. Here you can also change the text on the sagecell evaluation buttons.
   3. Add 'sagecell.sagecell' to your extensions in 'conf.py'


How to use it
===========

Example of usage::

	.. sagecell::

        L = [factor(n) for n in range(1, 20)]
        L[4:9]

Options
======
The lang option is set to 'r' if the code is to be interpreted as R code and 'octave' if the code is to be interpreted as Octave, otherwise the code is interpreted as Sage.

Example:

.. sagecell::
    :lang: r 

    a <- 3
    a+5

.. sagecell::
    :lang: octave

    A = [ 1, 1, 2; 3, 5, 8; 13, 21, 34 ]
    B = rand (3, 2)
    A*B


The codefile option is used to read the code from a file instead of writing it directly in the sphinx rst file.

Example:

.. sagecell::
    :codefile: example.sage

The auto option is used to have the code be evaluated automatically and display results when the page is loaded.

The hidecode option is used to set the display to minimal, so only the results are displayed but not the code. It only works if the auto option is also used.

Examples:

.. sagecell::
    :lang: r
    :codefile: code.R
    :auto:

.. sagecell::
    :auto: 
    :hidecode:   

    a <- 3
    a+5

During latex generation, the code is displayed verbatim if the latexcode option is chosen. If the img option is set to an image file the image will be displayed (beneath the code if the showcode option is also chosen). The width of the image is set with the imgwidth option, if no width is set the default width is 8cm.

.. sagecell::
    :codefile: example.sage
    :img: example.jpg
    :imgwidth: 4cm

.. sagecell::
    :lang: r 
    :latexcode:  
    :img: ex.png 

    a <- 3
    a+5

.. sagecell::
    :latexcode:

    2+3


