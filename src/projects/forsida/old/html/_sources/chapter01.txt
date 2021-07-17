Chapter
=======

Section
-------

Subsection
~~~~~~~~~~

Text

Extensions
----------

MathJax
~~~~~~~

In text :math:`2` or

.. math::
	4+4+3


Sage-cell extensions 
--------------------

For the pdf-version the applets can be changed for static images.

R
~~~~

.. sagecell::
    :lang: R

    4+4
    
Sage
~~~~

Sage example by `Marshall Hampton <http://wiki.sagemath.org/interact/graphics#Curves_of_Pursuit>`_.

.. sagecell::

    html('<h2>Tangent line grapher</h2>')
    @interact
    def tangent_line(f = input_box(default=sin(x)), xbegin = slider(0,10,1/10,0), xend = slider(0,10,1/10,10), x0 = slider(0, 1, 1/100, 1/2)):
        prange = [xbegin, xend]
        x0i = xbegin + x0*(xend-xbegin)
        var('x')
        df = diff(f)
        tanf = f(x0i) + df(x0i)*(x-x0i)
        fplot = plot(f, prange[0], prange[1])
        print 'Tangent line is y = ' + tanf._repr_()
        tanplot = plot(tanf, prange[0], prange[1], rgbcolor = (1,0,0))
        fmax = f.find_local_maximum(prange[0], prange[1])[0]
        fmin = f.find_local_minimum(prange[0], prange[1])[0]
        show(fplot + tanplot, xmin = prange[0], xmax = prange[1], ymax = fmax, ymin = fmin)

Octave
~~~~~~

.. warning::
	Plotting in Octave is not working at the moment

.. sagecell::
    :lang: octave

    A = [ 1, 1, 2; 3, 5, 8; 13, 21, 34 ]
    B = rand (3, 2)
    A*B

Hoverrole Extension
~~~~~~~~~~~~~~~~~~~
Þetta er texti um :hover:`stærðfræðigreiningu` og :hover:`afleiðujöfnur, deildajafna`. Fleiri hugtök: :hover:`heildi`, :hover:`ferill`, :hover:`vörpun`.

Auto-generated list of translated terms:

.. hoverlist::

    
