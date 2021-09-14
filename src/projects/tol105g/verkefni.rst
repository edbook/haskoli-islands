.. include:: rst-include

Verkefni
========

1. Annars stigs jafna
~~~~~~~~~~~~~~~~~~~~~
Skrifið forrit sem leysir annars stigs jöfnu

.. math:: y = a x^2 + b x + c

Fallið á að lesa inn :math:`a`, :math:`b` og :math:`c` með ``input``-skipunum
(með viðeigandi beiðnum til notanda). Ef jafnan hefur tvær lausnir á forritið að
skrifa „Lausnirnar eru:“ og síðan lausnirnar, ef hún hefur eina lausn á að
skrifa hana með viðeigandi skýringu og ef engin lausn er skal skrifa skilaboð um
það. Lausn eða lausnir eru gefnar með formúlunni

.. math::
   x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}

Ef stærðin undir kvaðratrótinni er neikvæð þá er engin lausn, ef
hún er núll er ein lausn, annars tvær. Gerið auk þess ráð fyrir
þeim möguleika að :math:`a` sé 0. Ef :math:`b` er ekki líka 0 þá er jafnan fyrsta
stigs og forritið á að skrifa að svo sé, ásamt lausninni (sem er
þá ein). Látið :math:`b` og :math:`c` vera gefin með afmælisdegi ykkar (dagur og mánuður) og prófið forritið fyrir fjórar mismunandi jöfnur, fyrsta
stigs jöfnuna :math:`bx + c = 0` og annars stigs jöfnur sem hafa enga, eina og tvær
lausnir þar á meðal jöfnuna :math:`x^2 + bx + c = 0`. Setjið viðeigandi skjölunarstreng  fremst í forritið.

2. Simpsons-regla
~~~~~~~~~~~~~~~~~
Skrifa skal forrit til að nálga heildi með svonefndri *Simpsons-regla*. Í trapisureglu er heildisbilinu skipt í :math:`n` hlutbil, fallið sem heilda skal nálgað með beinum línustrikum og heildi þess nálgað með flatarmálinu undir þessum línustrikum. Í Simpsonsreglu er fallið hinsvegar nálgað (eða *brúað* eins og það er kallað) með parabólum og heildið nálgað með flatarmálinu undir þeim. Skoðið endilega Wikipedíu-grein `um aðferðina <https://en.wikipedia.org/wiki/Simpson%27s_rule>`_.

Simpsons-formúlan er eftirfarandi:

.. math::
   \int_{a}^{b} f(x) \, dx \approx 
   \frac{\Delta x}{3}\left(f(x_0) + 4f(x_1)+2f(x_2)+
   4f(x_3)+2f(x_4)+\cdots+4f(x_{n-1}) + f(x_{n})\right)

þar sem :math:`\Delta x = \displaystyle{\frac{b-a}{n}}` :math:`x_i=a+i\Delta x`, :math:`i = 0,\ldots, n` og :math:`n` er slétt tala.

Skrifið fall ``simpson(f,a,b,n)`` sem nálgar heildið af ``f`` frá ``a``
til ``b`` með samsettri Simpsons-reglu með ``n`` hlutbilum.

Prófið með heildunum:

.. math::  (*)\quad\int_1^2\frac{\sin(x)}{x} dx
           \qquad\quad\text{og}\qquad\quad
           (**)\quad\int_0^1\exp(x) dx

með 4 hlutbilum. Ef rétt er forritað ætti að fást :math:`(*)` 0.65933 og
:math:`(**)` 1.71832. Rétt gildi eru 0.65933 og 1.71828, og trapisuregla með 4
bilum gefur 0.65863 og 1.72722.

Heildið líka eitthvert sjálfvalið fall þar sem afmælisdagur ykkar kemur við sögu.

3. Viðsnúningur
~~~~~~~~~~~~~~~
a) Skrifið fall ``hausaftast(L)`` sem færir haus L aftast. Ef kallað er með
   :code:`L=[1,2,3,4]` ætti að koma út :code:`L=[2,3,4,1]`. Prófið líka með
   lista búnum til útfrá afmælisdegi (t.d. 3.8.1999 :math:`\to` :code:`[3,8,99]`).

b) Skrifið fall ``snúavið(L)`` sem snýr við lista. Hér er reiknirit:

   .. code::

      fall snúavið(L)
          n := lengd L
          M := tómur listi
          fyrir i = n-1,n-2,...,0:
              setja i-ta stak L afast í M
          skila M
          
   Prófið að snúa við ``L=[1,2,3,4]`` sem ætti að skila ``[4,3,2,1]``
   og líka afmælisdagalistanum úr a-lið.
