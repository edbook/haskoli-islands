Markgildi og samfelldni
=======================

.. note:: 
    **Nauðsynleg undirstaða**

    -  Jafna línu, P.2

    -  Jafna hrings, P.3

    -  Hliðrun og skölun grafs, P.3

    -  (Stranglega) minnkandi og (stranglega) vaxandi föll, 2.8

    -  Jafnstæð og oddstæð föll, P.4

    -  Margliður; deiling, þáttun og rætur, P.6

    -  Tölugildisfallið, P.1

    -  Þríhyrningsójafnan, P.1

    -  Formerkjafallið, :math:`sgn(x)`, P.5

.. warning::
	Þessi kafli fjallar um tvö afskaplega mikilvæg og nátengd hugtök,
	markgildi og samfelldni. Það er nauðsynlegt fyrir nemendur að ná 
	góðum tökum á þeim því mörg hugtök í stærðfræði og hagnýtingum á stærðfræði
	sem verða á vegi ykkar í framtíðinni byggja á þessum hugtökum.
 
*I'd take the awe of understanding over the awe of ignorance any day.*

\- Douglas Adams, The Salmon of Doubt

--------

.. _markgildi:

Markgildi
---------

.. index::
    markgildi

Óformleg skilgreining á markgildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Segjum að fall :math:`f(x)` *stefni á tölu* :math:`L` *þegar* :math:`x`
*stefnir á* :math:`a`, og ritum :math:`\lim_{x\rightarrow a} f(x)=L`, ef
við getum tryggt að :math:`f(x)` sé eins nálægt :math:`L` og við
viljum bara með því að velja :math:`x` nógu nálægt :math:`a`.

Skilgreining: Markgildi
~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f` sé skilgreint á opnu bili umhverfis
punktinn :math:`a`, nema hvað hugsanlega er :math:`f(a)` ekki
skilgreint. Við segjum að :math:`f(x)` *stefni á tölu* :math:`L` *þegar*
:math:`x` *stefnir á* :math:`a`, og ritum
:math:`\lim_{x\rightarrow a} f(x)=L`, ef eftirfarandi skilyrði er
uppfyllt:

Fyrir sérhverja tölu :math:`\epsilon>0` er til tala :math:`\delta>0`
sem fullnægir eftirfarandi skilyrði: 

.. math:: \text{fyrir öll $x$ sem uppfylla} \qquad 0 < |x-a| < \delta \qquad \text{gildir} \qquad |f(x)-L| <\epsilon.

Við segjum að talan :math:`L` sé :hover:`markgildi,markgildi` :math:`f(x)` þegar
:math:`x` stefnir á :math:`a`.

.. ggb:: sYHVajyE
    :width: 700
    :height: 400
    :img: 01_markgildi.png
    :imgwidth: 12cm


.. note:: 
    Þegar athugað er hvort markgildið :math:`\lim_{x\rightarrow a} f(x)` er
    til, og þá hvert gildi þess er, þá skiptir ekki máli hvort :math:`f(a)` er
    skilgreint eða ekki.

.. _daemi2.1:

Dæmi
~~~~

(i)   :math:`\lim_{x \to a} c = c`, :math:`c` fasti

(ii)  :math:`\lim_{x \to a} x = a`

(iii) :math:`\lim_{x \to a} |x| = |a|`

.. only:: latex

    Sönnun á lið 2.

.. begin-toggle::
    :label: Sýna sönnun á lið 2

Hér er fallið sem um ræðir :math:`f(x) = x` og :math:`L=a`. 
Látum :math:`\epsilon>0` vera gefið. Við viljum finna 
:math:`\delta >0` þannig að :math:`|x-a|<\delta` hafi í för
með sér :math:`|f(x)-a| < \epsilon`. Þar sem :math:`f(x)=x` þá er seinni
ójafnan jafngild :math:`|x-a|<\epsilon`. Þetta er sama ójafnan og 
:math:`\delta` þarf að uppfylla þannig að okkur nægir að velja 
:math:`\delta = \epsilon`. Þá hefur 

.. math:: 
        |x-a| < \delta 

í för með sér að 

.. math::
        |f(x) -a| < \epsilon.

.. end-toggle::

.. begin-toggle::
    :label: Sýna ábendingar

**Ábendingar fyrir sannanir á liðum 1 og 3**

Til að sanna þetta þá er best að teikna mynd til að átta sig á því hvernig
föllin haga sér. Svo má velja

(i) :math:`\delta` sem hvað sem er.

(iii) :math:`\delta=\epsilon`.


.. end-toggle::

------

Markgildi frá hægri og vinstri
------------------------------

.. index::
    markgildi; frá hægri

Óformleg skilgreining
~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f` sé skilgreint á opnu bili
:math:`(a,b)`. Segjum að :math:`f(x)` *stefni á tölu* :math:`L` *þegar*
:math:`x` *stefnir á* :math:`a` *frá hægri*, og ritum
:math:`\lim_{x\rightarrow a^+} f(x)=L`, ef við getum tryggt að
:math:`f(x)` sé eins nálægt :math:`L` og við viljum bara með því að
velja :math:`x>a` nógu nálægt :math:`a`.

Skilgreining: Markgildi frá hægri
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f` sé skilgreint á opnu bili
:math:`(a,b)`. Við segjum að :math:`f(x)` *stefni á tölu* :math:`L`
*þegar* :math:`x` *stefnir á* :math:`a` *frá hægri*, og ritum
:math:`\lim_{x\rightarrow a^+} f(x)=L`, ef eftirfarandi skilyrði er
uppfyllt.

Fyrir sérhverja tölu :math:`\epsilon>0` er til tala :math:`\delta>0`
þannig að um öll :math:`x` sem eru þannig að

.. math:: a<x<a+\delta,\quad \text{ þá er } \quad |f(x)-L| <\epsilon.

.. ggb:: nDwQJCG2
    :width: 600
    :height: 400
    :img: 02_markfrahaegri.png
    :imgwidth: 12cm


.. index::
    markgildi; frá vinstri

Óformleg skilgreining
~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f` sé skilgreint á opnu bili
:math:`(b,a)`. Segjum að :math:`f(x)` *stefni á tölu* :math:`L` þegar
:math:`x` *stefnir á* :math:`a` *frá vinstri*, og ritum
:math:`\lim_{x\rightarrow a^-} f(x)=L`, ef við getum tryggt að
:math:`f(x)` sé eins nálægt :math:`L` og við viljum bara með því að
velja :math:`x<a` nógu nálægt :math:`a`.

Skilgreining: Markgildi frá vinstri
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f` sé skilgreint á opnu bili
:math:`(b,a)`. Við segjum að :math:`f(x)` *stefni á tölu* :math:`L`
*þegar* :math:`x` *stefnir á* :math:`a` *frá vinstri*, og ritum
:math:`\lim_{x\rightarrow a^-} f(x)=L`, ef eftirfarandi skilyrði er
uppfyllt.

Fyrir sérhverja tölu :math:`\epsilon>0` er til tala :math:`\delta>0`
þannig að um öll :math:`x` sem eru þannig að

.. math:: a-\delta<x<a,\quad \text{ þá er } \quad |f(x)-L| <\epsilon.

.. ggb:: fV63g8mx
    :width: 600
    :height: 400
    :img: 03_markfravinstri.png
    :imgwidth: 12cm

.. _setning-hv_markgildi:

Setning
~~~~~~~

Gerum ráð fyrir að fall :math:`f` sé skilgreint á opnu bili umhverfis
punktinn :math:`a`, nema hvað hugsanlega er :math:`f(a)` ekki
skilgreint. Þá er

.. math:: \lim_{x\rightarrow a} f(x)=L

ef og aðeins ef

.. math:: \lim_{x\rightarrow a^-} f(x)=L=\lim_{x\rightarrow a^+} f(x).

Dæmi: Tölugildisfallið
~~~~~~~~~~~~~~~~~~~~~~~

:hover:`Tölugildisfallið,tölugildi` :math:`|x|` er skilgreint sem :math:`x`
ef :math:`x\geq 0` en :math:`-x` ef :math:`x<0`. Um tölugildisfallið gildir

(i)   

      .. math:: \lim_{x\to 0^+} \frac x{|x|} = 1

(ii)  

      .. math:: \lim_{x\to 0^-} \frac x{|x|} = -1

(iii) 

      .. math:: \lim_{x\to 0} \frac x{|x|} \quad \text{er ekki til}

.. image:: ./myndir/kafli02/02_daemi.png

.. begin-toggle::
        :label: Sýna sönnun

(i)
        Hér skoðum við eingöngu :math:`x>0` og þá gildir að 
        :math:`\frac x{|x|} = \frac xx = 1`. Þar sem
        :math:`\lim_{x \to 0} 1 = 1` samkvæmt :ref:`Dæmi 2.1.3 <daemi2.1>`
        þá gildir einni að :math:`\lim_{x \to 0^+} 1 = 1` samkvæmt 
        :ref:`setningunni <setning-hv_markgildi>` 
        hér á undan. Þannig að 

        .. math::
                \lim_{x \to 0^+} \frac x{|x|} = 
                \lim_{x \to 0^+} 1 = 1

(ii)
        Eins og liður 1 nema ef :math:`x<0` þá er 
        :math:`\frac x{|x|} = \frac x{-x} = -1`

(iii)
        Af liðum 1 og 2 sést að hægri og vinstri markgildin eru ekki þau sömu þannig
        að samkvæmt :ref:`setningunni <setning-hv_markgildi>` hér á undan þá er
        markgildið ekki til.

.. end-toggle::

------

Reiknireglur fyrir markgildi
----------------------------

.. _setning-markgildi:

Setning
~~~~~~~

Gerum ráð fyrir að :math:`\lim_{x\rightarrow a}f(x)=L` og að
:math:`\lim_{x\rightarrow a}g(x)=M`. Þá gildir

(i)   :math:`\lim_{x\rightarrow a}\Big(f(x)+g(x)\Big)=L+M`.

(ii)  :math:`\lim_{x\rightarrow a}\Big(f(x)-g(x)\Big)=L-M`.

(iii) :math:`\lim_{x\rightarrow a}f(x)g(x)=LM`.

(iv)  :math:`\lim_{x\rightarrow a}kf(x)=kL`, þar sem :math:`k` fasti.

(v)   :math:`\lim_{x\rightarrow a}f(x)/g(x)=L/M`, að því gefnu að
      :math:`M\neq 0`.

(vi)  Gerum ráð fyrir að :math:`m` og :math:`n` séu heiltölur þannig að
      :math:`f(x)^{m/n}` sé skilgreint fyrir öll :math:`x` á bili
      :math:`(b,c)` umhverfis :math:`a` (en ekki endilega fyrir
      :math:`x=a`) og að :math:`L^{m/n}` sé skilgreint. Þá er
      :math:`\lim_{x\rightarrow a}f(x)^{m/n}=L^{m/n}`.

(vii) Ef til er bil :math:`(b,c)` sem inniheldur :math:`a` þannig að
      :math:`f(x)\leq g(x)` fyrir öll :math:`x\in (b,c)`, nema kannski
      :math:`x=a`, þá er
      :math:`\lim_{x\rightarrow a}f(x)=L\leq M=\lim_{x\rightarrow a}g(x)`.

.. warning::
    Liður (1) í setningunni á undan segir að ef markgildin
    :math:`\lim_{x\to a} f(x)` og :math:`\lim_{x\to a} g(x)` eru til þá sé
    markgildið :math:`\lim_{x\to a} (f(x)+g(x))` einnig til.

    En hún segir **ekki** að ef :math:`f` og :math:`g` eru föll þannig að
    markgildið :math:`\lim_{x\to a} (f(x)+g(x))` er til, að þá séu
    markgildin :math:`\lim_{x\to a} f(x)` og :math:`\lim_{x\to a} g(x)`
    einnig til.

.. begin-toggle::
    :label: Sýna sönnun á lið 1.

**Sönnun á lið 1** 

Við viljum sýna að fyrir :math:`\epsilon>0` þá sé til :math:`\delta>0`
þannig að ef :math:`|x-a|<\delta` þá sé :math:`|f(x)+g(x) - (L+M)|<\epsilon`.
Látum nú :math:`\epsilon>0` vera gefið, þá fæst af 
:math:`\lim_{x\to a} f(x) = L` að til er :math:`\delta_1>0` þannig að 

.. math::  |f(x)-L| < \frac \epsilon 2 

ef :math:`|x-a|<\delta_1`. Eins fæst af :math:`\lim_{x \to a} g(x)=M`
að til er :math:`\delta_2` þannig að 

.. math::  |g(x)-M| < \frac \epsilon 2 

ef :math:`|x-a|<\delta_2`. 

Ef við setjum :math:`\delta = \min\{\delta_1,\delta_2\}` þá þýðir það að 
öll :math:`x` sem uppfylla :math:`|x-a|<\delta` uppfylla einnig 
:math:`|x-a|<\delta_1` og :math:`|x-a|<\delta_2`. Þá gefur þríhyrningsójafnan 
okkur að fyrir slíkt :math:`x` þá er

.. math:: 
	|f(x)+g(x) - (L+M)| = |f(x)-L + g(x)-M| \\
	< |f(x)-L| + |g(x)-M| < \frac \epsilon 2 + \frac \epsilon 2 = \epsilon,

sem er það sem við vildum sýna.

.. end-toggle::

.. index::
    klemmureglan
    
Setning: Klemmureglan
~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`f(x)\leq
g(x)\leq h(x)` fyrir öll :math:`x` á bili :math:`(b, c)` sem inniheldur
:math:`a`, nema kannski :math:`x=a`. Gerum enn fremur ráð fyrir að

.. math:: \lim_{x\rightarrow a}f(x)=\lim_{x\rightarrow a}h(x)=L.

Þá er :math:`\lim_{x\rightarrow a}g(x)=L`.

.. image:: ./myndir/kafli02/04_03_klemmuregla.png
	:align: center
	:width: 80%

.. begin-toggle:: 
    :label: Sýna sönnun

**Sönnun**
   
Látum :math:`\epsilon>0` vera gefið. Við viljum sýna að þá sé til :math:`\delta>0` þannig
að :math:`|g(x)-L|<\epsilon` fyrir öll :math:`x` sem uppfylla :math:`|x-a|<\delta`.

Þetta má líka skrifa svona: 
Við viljum sýna að þá sé til :math:`\delta>0` þannig
að :math:`L-\epsilon<g(x)<L+\epsilon` fyrir öll :math:`x` sem uppfylla :math:`a-\delta < x<a+\delta`.

Við vitum nú að þar sem :math:`\lim_{x\to a} f(x) = L` þá er til :math:`\delta_1` 
þannig að :math:`L-\epsilon<f(x)<L+\epsilon` fyrir öll :math:`x` sem uppfylla :math:`a-\delta_1 < x<a+\delta_1`.

Eins þá fæst af :math:`\lim_{x\to a} h(x) = L` að til er :math:`\delta_2` 
þannig að :math:`L-\epsilon<g(x)<L+\epsilon` fyrir öll :math:`x` sem uppfylla :math:`a-\delta_2 < x<a+\delta_2`.

Setjum nú :math:`\delta = \min\{\delta_1,\delta_2\}` og athugum að það þýðir að fyrir sérhvert :math:`x` sem
uppfyllir :math:`a-\delta < x < a+\delta` uppfyllir einnig :math:`a-\delta_1 < x<a+\delta_1` 
og :math:`a-\delta_2 < x<a+\delta_2`. Þá gefur :math:`f(x)\leq g(x)\leq h(x)` að 

.. math:: L-\epsilon<f(x) \leq g(x) \leq h(x) < L+\epsilon.

Þar með er :math:`L-\epsilon < g(x) < L+\epsilon` og þá höfum við sýnt að 
:math:`\lim_{x\to a} g(x) = L`. 

.. end-toggle::


Dæmi: Markgildi með sínus
~~~~~~~~~~~~~~~~~~~~~~~~~

(i)   

      .. math:: \lim_{x\to 0} \sin\left(\frac 1x\right) \quad \text{er ekki til}

(ii)  

      .. math:: \lim_{x\to 0} x\sin\left(\frac 1x\right) = 0

(iii) 

      .. math:: \lim_{x \to 0} \frac{\sin(x)}{x} = 1

.. only:: latex

        Sönnun á lið 1.

.. begin-toggle::
        :label: Sýna sönnun á 1.

Sönnum þetta með mótsögn. Gerum ráð fyrir að til sé markgildi :math:`L` þannig að fyrir
sérhvert :math:`\epsilon >0` er til :math:`\delta>0` þannig að 
:math:`|x-0|<\delta` hefur í för með sér að :math:`|\sin(1/x) - L|<\epsilon`. Til þess
að þetta leiði til mótsagnar þurfum við að finna :math:`\epsilon>0` sem er þannig að 
sama hversu lítið :math:`\delta>0` er valið þá er alltaf til :math:`x` þannig að 
:math:`|x-0|<\delta` og 

.. math::
        \left|\sin\left(\frac 1x \right)-L\right| \geq \epsilon.

Veljum :math:`\epsilon = 0,5`. Ástæðan fyrir þessu vali er sú að þar sem 
:math:`\sin(1/x)` sveiflast á milli :math:`-1` og :math:`1` þá er nóg að 
velja tölu sem er þannig að fallið sveiflist út
fyrir bilið :math:`[L-\epsilon,L+\epsilon]`. Í þessu tilviki þýðir það að 
:math:`\epsilon` þarf að vera minna en 1. 

Ef markgildið er til þá er ætti að vera til :math:`\delta>0` þannig að 
:math:`|\sin(1/x)-L|< 0.5` fyrir :math:`x` sem uppfylla :math:`|x-0|<\delta`.
Byrjum á að skoða tilvikið :math:`L\leq 0`. 
Finnum nógu stóra náttúrlega tölu :math:`k`
þannig að :math:`\frac 1{2\pi k + \pi/2} < \delta`. 
Ef við setjum :math:`x=\frac 1{2\pi k + \pi/2}`  
þá fæst að :math:`|x-0|<\delta` en 
        
.. math::
        \left|\sin\left(\frac 1x \right) - L\right| = 
        |\sin(2\pi k +\pi/2) - L|  = |1-L| > 0,5

Tilvikið þegar :math:`L>0` er eins nema þá veljum við :math:`x=\frac 1{2\pi k - \pi/2}` 
sem þýðir að :math:`\sin(x) = -1`.



.. ggb:: yfYAfqtm
        :width: 652
        :height: 352
        :zoom_drag: false
        :img: 03_daemi-sin.png
        :imgwidth: 12cm

.. end-toggle::

Markgildi þegar x stefnir á óendanlegt
--------------------------------------


.. image:: ./myndir/kafli02/06_liminf.png
	:align: center
	:width: 50%

.. index::
    markgildi; þegar x stefnir á óendalegt


Óformleg skilgreining
~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f` sé skilgreint á bili
:math:`(a, \infty)`. Segjum að :math:`f(x)` *stefni á tölu* :math:`L`
*þegar* :math:`x` *stefnir á* :math:`\infty`, og ritum
:math:`\lim_{x\rightarrow \infty} f(x)=L`, ef við getum tryggt að
:math:`f(x)` sé eins nálægt :math:`L` og við viljum bara með því að
velja :math:`x` nógu stórt.

Skilgreining: Markgildi þegar :math:`x \to \infty`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f` sé skilgreint á bili
:math:`(a,\infty)`. Við segjum að :math:`f(x)` *stefni á tölu* :math:`L`
*þegar* :math:`x` *stefnir á* :math:`\infty`, og ritum
:math:`\lim_{x\rightarrow \infty} f(x)=L`, ef eftirfarandi skilyrði er
uppfyllt:

Fyrir sérhverja tölu :math:`\epsilon>0` er til tala :math:`R`
þannig að um öll :math:`x>R` gildir að 

.. math:: |f(x)-L|<\epsilon.

Óformleg skilgreining
~~~~~~~~~~~~~~~~~~~~~~


Fyrir :math:`-\infty` er þetta gert með sama sniði.


Gerum ráð fyrir að fall :math:`f` sé skilgreint á bili
:math:`(-\infty, a)`. Segjum að :math:`f(x)` *stefni á tölu* :math:`L`
*þegar* :math:`x` *stefnir á* :math:`-\infty`, og ritum
:math:`\lim_{x\rightarrow -\infty} f(x)=L`, ef við getum tryggt að
:math:`f(x)` sé eins nálægt :math:`L` og við viljum bara með því að
velja :math:`x` sem nógu stóra neikvæða tölu.

Skilgreining: Markgildi þegar :math:`x \to -\infty`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f` sé skilgreint á bili
:math:`(-\infty,a)`. Við segjum að :math:`f(x)` *stefni á tölu*
:math:`L` *þegar* :math:`x` *stefnir á* :math:`-\infty`, og ritum
:math:`\lim_{x\rightarrow -\infty} f(x)=L`, ef eftirfarandi skilyrði er
uppfyllt:

Fyrir sérhverja tölu :math:`\epsilon>0` er til tala :math:`R`
þannig að um öll :math:`x<R` gildir að 

.. math:: |f(x)-L|<\epsilon.

------

Óendanlegt sem markgildi
------------------------

.. index::
    markgildi; óendanlegt sem markgildi

Óformleg skilgreining
~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f` sé skilgreint á opnu bili umhverfis
punktinn :math:`a`, nema hvað hugsanlega er :math:`f(a)` ekki
skilgreint. Segjum að :math:`f(x)` *stefni á* :math:`\infty` *þegar*
:math:`x` *stefnir á* :math:`a`, og ritum
:math:`\lim_{x\rightarrow a} f(x)=\infty`, ef við getum tryggt að
:math:`f(x)` sé *hversu stórt sem við viljum* bara með því að velja
:math:`x` *nógu nálægt* :math:`a`.

Skilgreining: Markgildið :math:`\infty`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f` sé skilgreint á opnu bili umhverfis
punktinn :math:`a`, nema hvað hugsanlega er :math:`f(a)` ekki
skilgreint. Við segjum að :math:`f(x)` *stefni á* :math:`\infty` *þegar*
:math:`x` *stefnir á* :math:`a`, og ritum
:math:`\lim_{x\rightarrow a} f(x)=\infty`, ef eftirfarandi skilyrði er
uppfyllt.

Fyrir sérhverja tölu :math:`B` er til tala :math:`\delta>0` þannig
að um öll :math:`x` sem eru þannig að 

.. math:: 
        0 < |x-a| <\delta \quad  \text{ gildir að } \quad f(x) > B.

.. warning:: 
    Athugið að :math:`\infty` er **ekki** tala. Þó að
    :math:`\lim_{x\rightarrow a} f(x)=\infty` þá er samt sagt að markgildið
    :math:`\lim_{x\rightarrow a} f(x)` sé ekki til.

Óformleg skilgreining
~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f` sé skilgreint á opnu bili umhverfis
punktinn :math:`a`, nema hvað hugsanlega er :math:`f(a)` ekki
skilgreint. Segjum að :math:`f(x)` *stefni á* :math:`-\infty` *þegar*
:math:`x` *stefnir á* :math:`a`, og ritum
:math:`\lim_{x\rightarrow a} f(x)=-\infty`, ef við getum tryggt að
:math:`f(x)` sé hversu lítið sem við viljum bara með því að velja
:math:`x` nógu nálægt :math:`a`.

Skilgreining: Markgildið :math:`-\infty`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f` sé skilgreint á opnu bili umhverfis
punktinn :math:`a`, nema hvað hugsanlega er :math:`f(a)` ekki
skilgreint. Við segjum að :math:`f(x)` *stefni á* :math:`-\infty`
*þegar* :math:`x` *stefnir á* :math:`a`, og ritum
:math:`\lim_{x\rightarrow a} f(x)=-\infty`, ef eftirfarandi skilyrði er
uppfyllt.

Fyrir sérhverja tölu :math:`B` er til tala :math:`\delta>0` þannig
að um öll :math:`x` sem eru þannig að

.. math:: 0 < |x-a| < \delta \quad \text{ gildir að } \quad f(x)<B.

.. warning:: 
    Athugið að :math:`-\infty` er **ekki** tala. Þó að
    :math:`\lim_{x\rightarrow a} f(x)=-\infty` þá er samt sagt að markgildið
    :math:`\lim_{x\rightarrow a} f(x)` sé ekki til.

.. index:: 
    samfelldni
    samfelldni; í punkti

-------

.. _samfelldni:

Samfelldni
----------

Hér skilgreinum við og skoðum seinna grundvallarhugtakið í þessum kafla, sem er :hover:`samfelldni`.


.. index::
    innri punktur

Skilgreining: Innri punktur
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`A\subseteq {{\mathbb  R}}` og :math:`x\in A`. Við segjum að
:math:`x` sé :hover:`innri punktur` :math:`A` ef :math:`A` inniheldur opið bil
umhverfis :math:`x`, það er að segja til er tala :math:`\delta>0` þannig
að :math:`(x-\delta, x+\delta)\subseteq
A`.

Ef :math:`x` er ekki innri punktur :math:`A` og :math:`x\in A` þá segjum
við að :math:`x` sé :hover:`jaðarpunktur` :math:`A`.


.. index:: 
    samfelldni; í punkti

Skilgreining: Samfelldni í punkti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera fall og :math:`c` innri punkt skilgreiningarsvæðis
:math:`f`. Sagt er að :math:`f` sé *samfellt í punktinum* :math:`c` ef

.. math:: \lim_{x\rightarrow c}f(x)=f(c).

Setning
~~~~~~~

Látum :math:`f` og :math:`g` vera föll. Gerum ráð fyrir að :math:`c` sé
innri punktur skilgreiningarsvæðis beggja fallanna og að bæði föllin séu
samfelld í punktinum :math:`c`. Þá eru eftirfarandi föll samfelld í
:math:`c`:

(i)   :math:`f+g`

(ii)  :math:`f-g`

(iii) :math:`fg`

(iv)  :math:`kf`, þar sem :math:`k` er fasti

(v)   :math:`f/g`, ef :math:`g(c)\neq 0`

(vi)  :math:`\Big(f(x)\Big)^{1/n}`, að því gefnu að :math:`f(c)>0` ef
      :math:`n` er slétt tala og :math:`f(c)\neq 0` ef :math:`n<0`.

Þessi setning er bein afleiðing af :ref:`Setningu 2.3.1 <setning-markgildi>`.

Setning: Samskeyting samfelldra falla
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`g` vera fall sem er skilgreint á opnu bili umhverfis
:math:`c` og samfellt í :math:`c` og látum :math:`f` vera fall sem er
skilgreint á opnu bili umhverfis :math:`g(c)` og samfellt í
:math:`g(c)`. Þá er fallið :math:`f\circ g` skilgreint á opnu bili
umhverfis :math:`c` og er samfellt í :math:`c`.


.. note:: 
    Ef fall er skilgreint með formúlu og skilgreingamengið er ekki tilgreint
    sérstaklega, þá er venjan að líta alla þá punkta þar sem formúlan gildir
    sem skilgreingarmengi fallsins

    
.. index:: 
    samfelldni, samfellt fall

.. _`skilgrsamfellt`:
    
Skilgreining: Samfellt fall
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við segjum að fall :math:`f` sé :hover:`samfellt,samfellt fall` ef það er samfellt í
sérhverjum punkti skilgreingarmengisins.

Óformlega þýðir þetta að hægt er að teikna graf :math:`f` án þess að lyfta pennanum frá blaðinu.

Dæmi
~~~~

Eftirfarandi föll eru samfelld

(i)   margliður

(ii)  ræð föll

(iii) ræð veldi

(iv)  hornaföll; :math:`\sin`, :math:`\cos`, :math:`\tan`

(v)   tölugildisfallið :math:`|x|`

Að búa til samfelld föll
~~~~~~~~~~~~~~~~~~~~~~~~

Með því að nota föllin úr dæminu á undan sem efnivið þá getum við búið
til fjölda samfelldra fall með því að beita aðgerðunum úr Setningu 2.6.4
og Setningu 2.6.3.

.. index::
    samfelldni; frá hægri/vinstri


Dæmi
~~~~

Fallið :math:`\cos(3x+5)` er samfellt. Margliðan :math:`g(x) =3x+5` og 
:math:`f(x) = \cos(x)` eru samfelld föll og þá er samskeytingin
:math:`f\circ g(x) = \cos(3x+5)` einnig samfellt fall.

-------

Hægri/vinstri samfelldni
------------------------

Rifjum upp skilgreininguna á samfelldni.

Skilgreining
~~~~~~~~~~~~

Látum :math:`f` vera fall og :math:`c` innri punkt skilgreiningarsvæðis
:math:`f`. Sagt er að :math:`f` sé *samfellt í punktinum* :math:`c` ef

.. math:: \lim_{x\rightarrow c}f(x)=f(c).

Athugasemd
~~~~~~~~~~

Þessi skilgreining virkar aðeins fyrir innri punkta
skilgreiningarsvæðisins. Þannig að ef ætlunin er að rannsaka samfelldni
í jaðarpunktum þá gengur þessi skilgreining ekki. Hins vegar getum við
útvíkkað skilgreininguna á samfelldni fyrir hægri og vinstri endapunkta
bila með því að einskorða okkur við markgildi frá vinstri og hægri.

Skilgreining: Hægri/vinstri samfelldni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(i)  Fall :math:`f` er *samfellt frá hægri í punkti* :math:`c` ef
     :math:`\lim_{x\rightarrow c^+}f(x)=f(c)`.

     Hér er gert ráð fyrir að fallið :math:`f` sé amk. skilgreint á
     bili :math:`[c, a)`.

(ii) Fall :math:`f` er *samfellt frá vinstri í punkti* :math:`c` ef
     :math:`\lim_{x\rightarrow c^-}f(x)=f(c)`.

     Hér er gert ráð fyrir að fallið :math:`f` sé amk. skilgreint á
     bili :math:`(a, c]`.

Uppfærum nú skilgreininguna á :ref:`samfelldu falli <skilgrsamfellt>`.

.. index:: 
    fall; samfellt

Uppfærð skilgreining: Samfellt fall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`f` sé fall sem er skilgreint á mengi
:math:`A`, þar sem :math:`A` er sammengi endanlega margra bila. Við
segjum að fallið :math:`f` sé *samfellt* ef það er samfellt í öllum
innri punktum skilgreingarmengisins og ef það er samfellt frá
hægri/vinstri í jaðarpunktum skilgreingarmengisins, eftir því sem við á.

.. note::
    Ef fall er samfellt á opnu bili :math:`(a,b)`, og ef :math:`a<c<d<b`, þá
    er fallið einnig samfellt á bilinu :math:`[c,d]`.

-------

Eiginleikar samfelldra falla
----------------------------

.. index::
    há- og lággildislögmálið

.. _`Há- og lággildislögmálið`:

Setning – Há- og lággildislögmálið
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera samfellt fall skilgreint á **lokuðu takmörkuðu bili**
:math:`[a,b]`. Þá eru til tölur :math:`x_1` og :math:`x_2` í
:math:`[a,b]` þannig að fyrir allar tölur :math:`x` í :math:`[a,b]` er

.. math:: f(x_1)\leq f(x)\leq f(x_2).

Þetta þýðir að samfellt fall :math:`f` á lokuðu og takmörkuðu bili
:math:`[a,b]` tekur bæði hæsta og lægsta gildi á bilinu. Hæsta gildið er
þá :math:`f(x_2)` og lægsta gildið er :math:`f(x_1)`.

.. note::
    Það er mögulegt að fallið taki há/lággildi sitt í fleiri en einum
    punkti.

.. index::
    milligildissetningin


Setning: Milligildissetningin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera samfellt fall skilgreint á lokuðu takmörkuðu bili
:math:`[a,b]`. Gerum ráð fyrir að :math:`s` sé tala sem liggur á milli
:math:`f(a)` og :math:`f(b)`. Þá er til tala :math:`c` sem liggur á
milli :math:`a` og :math:`b` þannig að :math:`f(c)=s`.

.. ggb:: zEQQcGcQ
    :width: 700
    :height: 400
    :img: 10_milligildissetn.png
    :imgwidth: 12cm

.. begin-toggle::
    :label: Sýna sönnun

**Sönnun**

Í setningunni þá gerum við ráð fyrir að :math:`s` liggi á milli :math:`f(a)` og
:math:`f(b)`. Til að svona :math:`s` sé til þá þarf :math:`f(a) \neq f(b)`. 

Skoðum tilvikið þegar :math:`f(a) < f(b)`, en þá er :math:`f(a) < s < f(b)`. 
Tilvikið :math:`f(a)>f(b)` er nánast eins.

Skilgreinum mengið :math:`S = \{ x \in [a,b] ; f(x) < s\}`. Þetta mengi er ekki tómt
því :math:`a` er í því og það er takmarkað að ofan af :math:`b`. Samkvæmt 
:ref:`Frumsendunni um efra mark <FrumsendanUmEfraMark>` þá er til efra mark :math:`c \in[a,b]`
fyrir :math:`S`. Við viljum sýna að :math:`f(c)=s`. 

Ef :math:`f(c)>s` þá segir samfelldni :math:`f`
okkur að til sé lítið bil kringum :math:`c` þar sem fallið er stærra en :math:`s`. Sér í lagi er
til tala minni en :math:`c` sem er ekki í menginu :math:`S`. Þetta þýðir að :math:`c` er 
ekki efra mark :math:`S`. Orðum þetta aðeins nákvæmar.

Veljum :math:`0<\epsilon < f(c)-s` þá er til :math:`\delta>0` þannig að ef :math:`x\in ]c-\delta,c+\delta[`
þá er :math:`|f(c)-f(x)|<\epsilon < f(c) -s`. Þetta hefur í för með sér að :math:`f(c) - f(x) < f(c) -s`, 
það er :math:`f(x)>s`. Þetta þýðir að öll :math:`x\in]c-\delta,c[` eru "minni" efri mörk fyrir :math:`S`
en :math:`c` sem gengur ekki og er því mótsögn.

Ef :math:`f(c)<s` þá segir samfelldni :math:`f` okkur að til sé lítið bil kringum :math:`c`
þar sem fallið er minna en :math:`s`. Sér í lagi  er til tala stærri en :math:`c` sem er í menginu
:math:`S`. Þetta þýðir að :math:`c` er ekki efra mark, því efra mark á að vera stærra eða jafnt
og öll stök í :math:`S`. Þetta er einnig mótsögn.

Þá er bara eftir möguleikinn :math:`f(c)=s`, sem er nákvæmlega það sem við vildum.

.. end-toggle::

.. note::
    Það er möguleiki að það séu fleiri en einn punktur á bilinu þar sem fallið tekur
    gildið :math:`s`. Sönnunin hér á undan finnur þann stærsta. 

Fylgisetning
~~~~~~~~~~~~

Ef :math:`P(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0` er margliða af
oddatölu stigi :math:`n`, þá er til rauntala :math:`c` þannig að :math:`P(c)=0`.

.. begin-toggle::
    :label: Sýna sönnun

**Sönnun**

Gerum ráð fyrir að :math:`a_n>0`. Þá er
:math:`\lim_{x\to -\infty} P(x) = -\infty` og
:math:`\lim_{x\to \infty} P(x) = \infty`. Það þýðir að til eru tölur
:math:`a` og :math:`b` þannig að :math:`P(a)<0` og :math:`P(b)>0`. Með
því að beita Milligildissetningunni á fallið :math:`P` á bilinu
:math:`[a,b]` og með :math:`s=0` þá fæst að til er núllstöð á bilinu
:math:`[a,b]`.

Ef :math:`a_n < 0` þá víxlast formerkin á markgildunum hér að ofan en röksemdafærslan er
að öðru leyti eins.

.. end-toggle::

