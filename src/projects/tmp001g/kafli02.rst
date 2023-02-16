Extensions
==========

.. ggb:: mkyudgwh

Toggle-block
------------

.. begin-toggle::
  :label: Sýna útleiðslu á hreyfijöfnum
  :starthidden: True

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

.. end-toggle::

Buttons with links
~~~~~~~~~~~~~~~~~~

.. button::
  :text: Edbook home page
  :link: http://edbook.hi.is

Panopto
~~~~~~~
Displays videos hosted on Panopto

.. panopto:: bfb3abf8-891c-4a53-8cee-08640552d8f0
    :width: 100%
    :height: 405

Math - Katex
~~~~~~~~~~~~
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
    :height: 500

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
Þetta er texti um :hover:`stærðfræðigreiningu` og :hover:`afleiðujöfnur, deildajafna`. Fleiri hugtök: :hover:`heildi`, :hover:`ferill`, :hover:`vörpun`.

Auto-generated list of translated terms:

.. hoverlist::

Google Analytics Extension
----------------------------
This extension enables the use of Google Analytics by inserting the tracking code on each page (except the index) and by inserting your tracking ID inside conf.py you should be able to monitor the use of your site.

This extension also tracks how far users have scrolled on the page. When a new section is scrolled into view a Google Analytics event is fired. These events can be seen in real time in the Javascript console (Chrome: CTRL+Shift+I OR Options-> More Tools -> Developer Tools).
