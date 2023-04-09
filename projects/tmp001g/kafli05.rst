Viðbætur
==========

Geogebra
--------

Hægt er að greypa inn Geogebra-forrit með `sphinxcontrib-geogebra 
<https://github.com/edbook/sphinxcontrib-geogebra>`_ viðbótinni.
Vista þarf Geogebra-skjalið á geogebra.org þar sem það fær auðkenni, en auðkennið 
er aftasti hlutinn af vefslóðinni.
Forritið er svo sett inn með: 

.. code-block::

  .. ggb:: abcdefgh


Sjá https://github.com/edbook/sphinxcontrib-geogebra#options fyrir fleiri stillingar.

Dæmi
~~~~

.. ggb:: mkyudgwh

Togglebutton
------------

.. admonition:: Útleiðasla á hreyfijöfnum
    :class: setning, dropdown

    Hröðun er afleiða hraðans og því má lýsa sem afleiðujöfnu:

    .. math::
      \begin{aligned}
        &\text{Upphaflega jafnan} &    a &=\frac{dv(t)}{dt} \\
        &\text{Umritum} &    dv(t) &=  a\cdot dt \\
        &\text{Heildum beggja vegna} &     \int_0^t dv &= a \cdot \int_0^t dt \\
        &\text{ } &       v(t)-v(0) &= a\cdot (t-0) \\
        &\text{} & v(t) &= a\cdot t +v_0
      \end{aligned}

    sem er einmitt jafnan fyrir hraða sem fall af tíma.


Takkar fyrir hlekki (sphinxcontrib-custombutton)
------------------------------------------------

Viðbótin `sphinxcontrib-custombutton <https://github.com/sphinxcontrib-custombutton>`_ 
er fyrir sérsniðna takka með hlekkjum. Skráin ``_static/button.css`` geymir stillingar
fyrir útlit takkans. 

.. button::
  :text: Edbook home page
  :link: http://edbook.hi.is

Panopto
-------

Hægt er að greypa inn Panopto-myndbönd með 

.. code-block::
    
    .. panopto:: ab027f4b-88b9-4647-af20-afdf0092304d
        :width: 100%
        :height: 400

Hér er `ab027f4b-88b9-4647-af20-afdf0092304d` auðkennið sem myndbandið hefur á 
Panopto-þjóninum. Til að finna það þá er best að fara inn á hi.cloud.panopto.eu
finna myndbandið og smella á `Settings` og undir `Viewer Link` er auðkennið það sem
stendur fyrir aftan `id=`. 

.. panopto:: ab027f4b-88b9-4647-af20-afdf0092304d
    :width: 100%

Youtube
-------



Math - Katex
------------
Math on page is rendered with Katex.
Katex is faster in works for almost all latex syntax, there are documented cases of examples
known to cause troubles in the katex-extension sub-directory

In line: :math:`\lim_{x\to a^-} f(x) = \pm \infty`, or

.. math::
    \overline{x}=\frac{M_{x=0}}{m} = \frac{\sum_{i=1}^n x_im_i}{\sum_{i=1}^n m_i}.


Datacamp extensions
-------------------

Python
~~~~~~

.. datacamp::
    :lang: python

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    fig = plt.figure()

    def f(x, y):
        return np.sin(x) + np.cos(y)

    x = np.linspace(0, 2 * np.pi, 120)
    y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)

    im = plt.imshow(f(x, y), animated=True)

    def updatefig(*args):
        global x, y
        x += np.pi / 15.
        y += np.pi / 20.
        im.set_array(f(x, y))
        return im,

    ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
    plt.show()

R
~~~

.. datacamp::
    :lang: r

    options(scipen=999)  # turn-off scientific notation like 1e+48
    library(ggplot2)
    theme_set(theme_bw())  # pre-set the bw theme.
    data("midwest", package = "ggplot2")

    gg <- ggplot(midwest, aes(x=area, y=poptotal)) +
        geom_point(aes(col=state, size=popdensity)) +
        geom_smooth(method="loess", se=F) +
        xlim(c(0, 0.1)) +
        ylim(c(0, 500000)) +
        labs(subtitle="Area Vs Population",
        y="Population",
        x="Area",
        title="Scatterplot",
        caption = "Source: midwest")

    gg

Hoverrole Extension
-------------------

Þetta er texti um :hover:`stærðfræðigreiningu,stærðfræðigreining` og :hover:`afleiðujöfnur, deildajafna`. Fleiri hugtök: :hover:`heildi`, :hover:`ferill`, :hover:`vörpun`.

Auto-generated list of translated terms:

.. hoverlist::

Google Analytics Extension
----------------------------
This extension enables the use of Google Analytics by inserting the tracking code on each page (except the index) and by inserting your tracking ID inside conf.py you should be able to monitor the use of your site.

This extension also tracks how far users have scrolled on the page. When a new section is scrolled into view a Google Analytics event is fired. These events can be seen in real time in the Javascript console (Chrome: CTRL+Shift+I OR Options-> More Tools -> Developer Tools).
