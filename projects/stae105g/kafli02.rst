Markgildi og samfelldni
=======================

.. admonition:: Nauðsynleg undirstaða
  :class: athugasemd

    -  Jafna línu

    -  Jafna hrings

    -  Hliðrun og skölun grafs

    -  (Stranglega) minnkandi og (stranglega) vaxandi föll

    -  Jafnstæð og oddstæð föll

    -  Margliður; deiling, þáttun og rætur

    -  Tölugildisfallið

    -  Þríhyrningsójafnan

    -  Formerkjafallið, :math:`sgn(x)`


---------

.. epigraph::

  *It is perilous to study too deeply the arts of the Enemy,
  for good or for ill. But such falls and betrayals, alas, have happened before.*

  \-Lord Elrond, The Fellowship of the Ring


---------

.. admonition:: Aðvörun
  :class: advorun

	Þessi kafli fjallar um tvö afskaplega mikilvæg og nátengd hugtök,
	markgildi og samfelldni. Það er nauðsynlegt fyrir nemendur að ná
	góðum tökum á þeim því mörg hugtök í stærðfræði og hagnýtingum á stærðfræði
	sem verða á vegi ykkar í framtíðinni byggja á þessum hugtökum.

--------

.. _markgildi:

Skilgreiningar á markgildi
--------------------------

Óformleg skilgreining á markgildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index::
    markgildi

Segjum að fall :math:`f(x)` *stefni á tölu* :math:`L` *þegar* :math:`x`
*stefnir á* :math:`a`, og ritum :math:`\lim_{x\rightarrow a} f(x)=L`, ef
við getum tryggt að :math:`f(x)` sé eins nálægt :math:`L` og við
viljum bara með því að velja :math:`x` nógu nálægt :math:`a`.

Skilgreining: Markgildi
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

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
      :width: 600
      :height: 400
      :img: 01_markgildi.png
      :imgwidth: 12cm

.. admonition:: Aðvörun
  :class: advorun

  Bókin notar örlítið lauslegri skilgreiningu á markgildi. Ekki er til ein,
  viðtekin skilgreining og er þetta háð túlkun að einhverju leyti. Til að halda
  samræmi við aðra áfanga Háskóla Íslands munum við notast við þessa skilgreiningu
  frekar en þá sem bókin býður upp á.

.. admonition:: Athugasemd
  :class: athugasemd

    Þegar athugað er hvort markgildið :math:`\lim_{x\rightarrow a} f(x)` er
    til, og þá hvert gildi þess er, þá skiptir ekki máli hvort :math:`f(a)` er
    skilgreint eða ekki.

.. _daemi2.1:

Dæmi: Markgildi
~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

    (i)   :math:`\lim_{x \to a} c = c`, :math:`c` fasti

    (ii)  :math:`\lim_{x \to a} x = a`

    (iii) :math:`\lim_{x \to a} |x| = |a|`

------

Markgildi
---------

.. index::
    markgildi; frá hægri

Óformleg skilgreining á markgildi frá hægri
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f` sé skilgreint á opnu bili
:math:`(a,b)`. Segjum að :math:`f(x)` *stefni á tölu* :math:`L` *þegar*
:math:`x` *stefnir á* :math:`a` *frá hægri*, og ritum
:math:`\lim_{x\rightarrow a^+} f(x)=L`, ef við getum tryggt að
:math:`f(x)` sé eins nálægt :math:`L` og við viljum bara með því að
velja :math:`x>a` nógu nálægt :math:`a`.

Skilgreining: Markgildi frá hægri
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

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

Óformleg skilgreining á markgildi frá vinstri
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f` sé skilgreint á opnu bili
:math:`(b,a)`. Segjum að :math:`f(x)` *stefni á tölu* :math:`L` þegar
:math:`x` *stefnir á* :math:`a` *frá vinstri*, og ritum
:math:`\lim_{x\rightarrow a^-} f(x)=L`, ef við getum tryggt að
:math:`f(x)` sé eins nálægt :math:`L` og við viljum bara með því að
velja :math:`x<a` nógu nálægt :math:`a`.


Skilgreining: Markgildi frá vinstri
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

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

Skilgreining: Önnur skilgreining á markgildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
  :class: skilgreining

  Gerum ráð fyrir að fall :math:`f` sé skilgreint á opnu bili umhverfis
  punktinn :math:`a`, nema hvað hugsanlega er :math:`f(a)` ekki
  skilgreint. Þá er

  .. math:: \lim_{x\rightarrow a} f(x)=L

  ef og aðeins ef

  .. math:: \lim_{x\rightarrow a^-} f(x)=L=\lim_{x\rightarrow a^+} f(x).

Dæmi: Tölugildisfallið
~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Lausn
  :class: daemi

  :hover:`Tölugildisfallið,tölugildi` :math:`|x|` er skilgreint sem :math:`x`
  ef :math:`x\geq 0` en :math:`-x` ef :math:`x<0`. Um tölugildisfallið gildir

      (i)

      .. math:: \lim_{x\to 0^+} \frac x{|x|} = 1

      (ii)

      .. math:: \lim_{x\to 0^-} \frac x{|x|} = -1

      (iii)

      .. math:: \lim_{x\to 0} \frac x{|x|} \quad \text{er ekki til}

  .. image:: ./myndir/kafli02/02_daemi.png

------

Reiknireglur fyrir markgildi
----------------------------

.. _setning-markgildi:

.. admonition:: Reiknireglur fyrir markgildi
  :class: setning

    Gerum ráð fyrir að :math:`\lim_{x\rightarrow a}f(x)=L` og að
    :math:`\lim_{x\rightarrow a}g(x)=M`. Þá gildir

    (i)   :math:`\lim_{x\rightarrow a}\Big(f(x)+g(x)\Big)=L+M`.

    (ii)  :math:`\lim_{x\rightarrow a}\Big(f(x)-g(x)\Big)=L-M`.

    (iii) :math:`\lim_{x\rightarrow a}f(x)g(x)=LM`.

    (iv)  :math:`\lim_{x\rightarrow a}kf(x)=kL`, þar sem :math:`k` fasti.

    (v)   :math:`\lim_{x\rightarrow a}f(x)/g(x)=L/M`, að því gefnu að :math:`M\neq 0`.

    (vi)  Gerum ráð fyrir að :math:`m` og :math:`n` séu heiltölur þannig að
          :math:`f(x)^{m/n}` sé skilgreint fyrir öll :math:`x` á bili
          :math:`(b,c)` umhverfis :math:`a` (en ekki endilega fyrir
          :math:`x=a`) og að :math:`L^{m/n}` sé skilgreint. Þá er
          :math:`\lim_{x\rightarrow a}f(x)^{m/n}=L^{m/n}`.

    (vii) Ef til er bil :math:`(b,c)` sem inniheldur :math:`a` þannig að
          :math:`f(x)\leq g(x)` fyrir öll :math:`x\in (b,c)`, nema kannski
          :math:`x=a`, þá er
          :math:`\lim_{x\rightarrow a}f(x)=L\leq M=\lim_{x\rightarrow a}g(x)`.

.. admonition:: Aðvörun
  :class: advorun

    Liður (1) í setningunni á undan segir að ef markgildin
    :math:`\lim_{x\to a} f(x)` og :math:`\lim_{x\to a} g(x)` eru til þá sé
    markgildið :math:`\lim_{x\to a} (f(x)+g(x))` einnig til.

    En hún segir **ekki** að ef :math:`f` og :math:`g` eru föll þannig að
    markgildið :math:`\lim_{x\to a} (f(x)+g(x))` er til, að þá séu
    markgildin :math:`\lim_{x\to a} f(x)` og :math:`\lim_{x\to a} g(x)`
    einnig til.

------

Aðferðir til að meta markgildi
------------------------------

Skilgreining: Sérstöðupunktur og afmáanlegur sérstöðupunktur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Lauslega má skilgreina *sérstöðupunkt* sem þær tölur :math:`a` sem uppfylla að
  fallið :math:`f(x)` er ekki skilgreint í :math:`a`. Sérstöðupunktur
  kallast *afmáanlegur sérstöðupunktur* ef hann uppfyllir að til er tala :math:`L`
  þannig að

  .. math:: \lim_{x \rightarrow a^-} f(x) = L = \lim_{x \rightarrow a^+} f(x).

  .. image:: ./myndir/kafli02/PMA_afmaanlegur1.png
    :width: 75%
    :align: center

Dæmi: Afmáanlegur sérstöðupunktur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Reiknum markgildið

  .. math:: \lim_{x \rightarrow 1} \frac{x-1}{x-1}.

.. admonition:: Lausn
  :class: daemi, dropdown

  Ef við skoðum fallið :math:`h(x)=\frac{x-1}{x-1}` er ljóst að hægt er að stytta
  :math:`x-1` í teljara út fyrir :math:`x-1` í nefnara. Því er :math:`1`
  afmáanlegur sérstöðupunktu. Munum þó, að þetta fall
  hefur skilgreiningarmengið :math:`\mathbb{R} \setminus \{1\}` og það að stytta
  fallið breytir því ekki. Því gildir, að jafnvel þó fallið sé styttanlegt í
  :math:`h(x)=1` að :math:`1` er enn ekki hluti af skilgreiningarmenginu og því
  fallið óskilgreint í punktinum. En þar sem við gátum stytt nefnarann í burtu
  þá gildir að

  .. math:: \lim_{x \rightarrow 1} \frac{x-1}{x-1} = 1.

  .. image:: ./myndir/kafli02/PMA_afmaanlegur.png
      :width: 75 %
      :align: center

.. admonition:: Athugasemd
  :class: athugasemd

  Almennt gildir, ef hægt er að stytta ræða fallið :math:`\frac{P(x)}{Q(x)}` í
  fastann :math:`c`, að

  .. math:: \lim_{x \rightarrow a} \frac{P(x)}{Q(x)} = c

  fyrir öll :math:`a \in \mathbb{R}`, jafnvel þó :math:`a` sé ekki í skilgreiningarmengi
  fallsins. Ef hægt er að stytta einhverjar en ekki allar núllstöðvar nefnara fallsins í burtu
  þá er markgildið einfaldlega gildi nýja, stytta fallsins í punktinum, þ.e.
  ef ræða fallið :math:`f(x)` hefur afmáanlega sérstöðupunktinn :math:`a` svo unnt
  er að stytta það í ræða fallið :math:`\frac{P(x)}{Q(x)}` þá gildir að

  .. math:: \lim_{x \rightarrow a} \frac{P(x)}{Q(x)} = \frac{P(a)}{Q(a)}.

.. index::
    klemmureglan

Klemmureglan
~~~~~~~~~~~~~

Ef við reynum að ákvarða markgildi fallsins :math:`g(x)` þá getur hjálpað ef
okkur tekst að *klemma* fallið milli tveggja annarra falla.

Setning: Klemmureglan
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: klemmureglan
  :class: setning

  Gerum ráð fyrir að :math:`f(x)\leq
  g(x)\leq h(x)` fyrir öll :math:`x` á bili :math:`(b, c)` sem inniheldur
  :math:`a`, nema kannski :math:`x=a`. Gerum enn fremur ráð fyrir að

  .. math:: \lim_{x\rightarrow a}f(x)=\lim_{x\rightarrow a}h(x)=L.

  Þá er :math:`\lim_{x\rightarrow a}g(x)=L`.

  .. image:: ./myndir/kafli02/04_03_klemmuregla.png
   :align: center
   :width: 80%

Dæmi: Klemmureglan
~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Reiknum markgildið

  .. math:: \lim_{x \rightarrow 0} \frac{\sin(x)}{x}.

.. admonition:: Lausn
  :class: daemi, dropdown

  Athugum að bæði teljarinn og nefnarinn taka gildið 0 þegar við stingum inn
  :math:`x=0` og :math:`\frac{0}{0}` er ekki skilgreint. Nú er vitað að fyrir
  öll :math:`x \in \mathbb{R}` gildir að

  .. math:: \sin(x) \leq x \leq \tan(x).

  Auðvelt er að sannfæra sig um með þetta með einfaldri mynd af einingahringnum.

  .. image:: ./myndir/kafli02/PMA_unitcircle.png
    :align: center
    :width: 75%

  Við getum nú deilt í gegnum ójöfnuna með :math:`\sin(x)` til að fá

  .. math:: 1 \leq \frac{x}{\sin(x)} \leq \frac{1}{\cos(x)}

  þar sem við nýttum okkur að :math:`\tan(x)=\frac{\sin(x)}{\cos(x)}`.
  Næst snúum við ójöfnunni við, með því að velta öllum brotunum, til að fá að

  .. math:: \cos(x) \leq \frac{\sin(x)}{x} \leq 1.

  Notum nú klemmuregluna til að ákvarða gildi :math:`\frac{\sin(x)}{x}` þar sem
  það er klemmt á milli :math:`1` og :math:`\frac{1}{\cos(x)}`, því við sjáum að

  .. math:: \lim_{x \rightarrow 0} 1 = 1

  og

  .. math:: \lim_{x \rightarrow 0} \cos(x) = \cos(0) = 1.

  Þá segir klemmureglan að

  .. math:: 1 \leq \lim_{x \rightarrow 0} \frac{\sin(x)}{x} \leq 1.

  Aðeins ein tala uppfyllir að vera bæði stærri eða jöfn 1 og minni eða jöfn 1,
  og það er talan 1. Því fæst að

  .. math::  \lim_{x \rightarrow 0} \frac{\sin(x)}{x} = 1.

Margföldun með samoka
~~~~~~~~~~~~~~~~~~~~~

Í sumum tilfellum getur margföldun með samoka haft þau áhrif að núllstöð nefnarans
verður að afmáanlegum sérstöðupunkti í nýja, lengda brotinu.

Skilgreining: Samoki
~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  *Samoki* er myndaður þegar formerki er víxlað milli liðanna í tvíliðu. Þannig
  er samoki tvíliðunnar :math:`x+y` til að mynda :math:`x-y` og samoki tvíliðunnar
  :math:`\sqrt{x}-1` er :math:`\sqrt{x}+1`.

Dæmi: Samoki
~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Reiknum markgildið

  .. math:: \lim_{x \rightarrow -1} \frac{\sqrt{x+2}-1}{x+1}.

.. admonition:: Lausn
  :class: daemi, dropdown

  Lengjum brotið með samoka teljarans.

  .. math:: =\lim_{x \rightarrow -1} \frac{\sqrt{x+2}-1}{x+1} \cdot \frac{\sqrt{x+2}+1}{\sqrt{x+2}+1} = \lim_{x \rightarrow -1} \frac{x+1}{(x+1)(\sqrt{x+2}+1)}.

  Við getum nú stytt brotið, þar sem :math:`x+1` er sameiginlegur þáttur í bæði
  teljara og nefnara. Fáum því

  .. math:: =\lim_{x \rightarrow -1} \frac{1}{\sqrt{x+2}+1}.

  Tökum eftir því að :math:`-1` er ekki lengur núllstöð nefnarans. Við getum því
  sett :math:`-1` beint inn í fallið til að ákvarða markgildið.

  .. math:: =\lim_{x \rightarrow -1} \frac{1}{\sqrt{x+2}+1} = \frac{1}{\sqrt{-1+2}+1} = \frac{1}{2}.

Einfalda flókið brot
~~~~~~~~~~~~~~~~~~~~

Stundum getur hjálpað að taka brot, sem er óþarflega flókið, og reyna að einfalda það.

Dæmi: Einfalda flókið brot
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Reiknum markgildið

  .. math:: \lim_{x \rightarrow 1} \frac{\frac{1}{x+1}-\frac{1}{2}}{x-1}

.. admonition:: Lausn
  :class: daemi, dropdown

  Ef við stingum 1 inn fyrir :math:`x` fæst :math:`\frac{0}{0}`, sem er óskilgreint.
  Við skulum einfalda brotið með því að lengja það með minnsta samnefnara brota
  teljarans.


  .. math:: =\lim_{x \rightarrow 1} \frac{\frac{1}{x+1}-\frac{1}{2}}{x-1} \cdot \frac{2(x+1)}{2(x+1)} = \lim_{x \rightarrow 1} \frac{-(x-1)}{2(x-1)(x+1)}.

  Tökum eftir því að :math:`x-1` er sameiginlegur þáttur í teljara og nefnara og
  við getum því stytt brotið.

  .. math:: = \lim_{x \rightarrow 1} \frac{-1}{2(x+1)}.

  Þar sem :math:`1` er ekki lengur núllstöð nefnarans, þá getum við metið markgildið
  beint með því að stinga inn :math:`x=1`.

  .. math:: =  \frac{-1}{2(1+1)} = - \frac{1}{4}.

------

Markgildi í óendanleikanum
--------------------------

Óformleg skilgreining á markgildnu :math:`\infty`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef fallið stefnir ekki á eina ákveðna tölu, heldur stefnir fallgildið á að verða annað hvort
óendanlega stórt eða óendanlega lítið (úr báðum áttum), segjum við að markgildið
sé :math:`\pm \infty`, þar sem :math:`+` er notað ef fallið stefnir á að
vera óendanlega stórt en :math:`-` ef það stefnir á að vera óendanlega lítið.

Skilgreining: Markgildið :math:`\infty`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

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

.. admonition:: athugasemd
  :class: athugasemd

    Athugum sérstaklega að það sama verður að gilda fyrir báðar áttir. Ekki dugar að
    markgildið stefni á :math:`-\infty` úr annarri áttinni en :math:`+\infty` úr hinni.

.. admonition:: Athugasemd
  :class: athugasemd

    Stundum er :math:`+`-tákninu sleppt fyrir :math:`+\infty` og aðeins er skrifað
    :math:`\infty`. Þetta er í samræmi við tölur almennt, þar sem jákvæðar tölur
    eru formerkislausar en neikvæðar tölur ávallt táknaðar með :math:`-` fyrir framan.
    Munum þó jafnframt að :math:`\infty` er ekki tala og hegðar sér ekki eins og slík.
    Almennar reiknireglur gilda ekki þegar rætt er um óendanleikann.

.. admonition:: Athugasemd
  :class: athugasemd

  Sumir vilja gera greinarmun á þegar markgildið er einhver tala og þegar
  markgildið er :math:`\pm \infty`. Þá er fyrra tilfellið ýmist kallað *endanlegt markgildi*
  eða *eiginlegt markgildi* en það seinna ýmist *óendanlegt markgildi* eða
  *óeiginlegt markgildi*.

  Mörg föll stefna á :math:`\pm \infty` í einhverjum punkti eða punktum. Það er t.a.m. algeng
  hegðun hjá ræðum föllum sem hafa núllstöð í nefnara sem ekki er hægt að stytta út
  (þ.e. það er ekki afmáanlegur sérstöðupunktur).

Dæmi: Markgildið :math:`\infty`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Lítum á fallið :math:`h(x)=\frac{1}{(x-2)^2}` og veltum því fyrir okkur hvað
  gerist þegar við látum :math:`x \rightarrow 2`.

.. admonition:: Lausn
  :class: daemi, dropdown

  Ef við skoðum hegðun fallsins
  í kringum punktinn :math:`2` getum við séð að því meir sem við nálgumst punktinn,
  úr báðum áttum, þeim mun stærra verður :math:`y`-gildið.

  .. image:: ./myndir/kafli02/PMA_inf_lim.png
      :width: 75 %
      :align: center

  Því er ljóst að

  .. math:: \lim_{x \rightarrow 2} \frac{1}{(x-2)^2} = \infty.

Dæmi: Markgildið :math:`\infty`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Lítum á fallið :math:`h(x)=\frac{1}{x}` og veltum því fyrir okkur hvað
  gerist þegar við látum :math:`x \rightarrow 0`.

.. admonition:: Lausn
  :class: daemi, dropdown

  Ef við skoðum hegðun fallsins
  í kringum punktinn :math:`0` getum við séð að ef við nálgumst punktinn frá hægri
  þá stefnir :math:`y`-gildið á :math:`\infty` en ef við nálgumst puntkinn frá
  vinstri þá stefnir :math:`y`-gildið á :math:`-\infty`, þ.e.

  .. math:: \lim_{x \rightarrow 0^-} \frac{1}{x} = -\infty

  og

  .. math::  \lim_{x \rightarrow 0^+} \frac{1}{x} = \infty

  .. image:: ./myndir/kafli02/PMA_lim_ekki_til.png
      :width: 75 %
      :align: center

  Þar sem :math:`\lim_{x \rightarrow 0^-}  \neq \lim_{x \rightarrow 0^+}` er ljóst
  að markgildið er ekki til.

  .. figure:: ./myndir/kafli02/mean_girls.gif
      :width: 75 %
      :align: center

------

Markgildi þegar x stefnir á óendanlegt
---------------------------------------

.. image:: ./myndir/kafli02/06_liminf.png
	:align: center
	:width: 50%

.. index::
    markgildi; þegar x stefnir á óendalegt


Óformleg skilgreining á markgildnu þegar :math:`x \to \infty`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f` sé skilgreint á bili
:math:`(a, \infty)`. Segjum að :math:`f(x)` *stefni á tölu* :math:`L`
*þegar* :math:`x` *stefnir á* :math:`\infty`, og ritum
:math:`\lim_{x\rightarrow \infty} f(x)=L`, ef við getum tryggt að
:math:`f(x)` sé eins nálægt :math:`L` og við viljum bara með því að
velja :math:`x` nógu stórt.

Skilgreining: Markgildi þegar :math:`x \to \infty`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Gerum ráð fyrir að fall :math:`f` sé skilgreint á bili
  :math:`(a,\infty)`. Við segjum að :math:`f(x)` *stefni á tölu* :math:`L`
  *þegar* :math:`x` *stefnir á* :math:`\infty`, og ritum
  :math:`\lim_{x\rightarrow \infty} f(x)=L`, ef eftirfarandi skilyrði er
  uppfyllt:

  Fyrir sérhverja tölu :math:`\epsilon>0` er til tala :math:`R`
  þannig að um öll :math:`x>R` gildir að

  .. math:: |f(x)-L|<\epsilon.

Óformleg skilgreining á markgildnu þegar :math:`x \to -\infty`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fyrir :math:`-\infty` er þetta gert með sama sniði.

Gerum ráð fyrir að fall :math:`f` sé skilgreint á bili
:math:`(-\infty, a)`. Segjum að :math:`f(x)` *stefni á tölu* :math:`L`
*þegar* :math:`x` *stefnir á* :math:`-\infty`, og ritum
:math:`\lim_{x\rightarrow -\infty} f(x)=L`, ef við getum tryggt að
:math:`f(x)` sé eins nálægt :math:`L` og við viljum bara með því að
velja :math:`x` sem nógu stóra neikvæða tölu.

Skilgreining: Markgildi þegar :math:`x \to -\infty`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Gerum ráð fyrir að fall :math:`f` sé skilgreint á bili
  :math:`(-\infty,a)`. Við segjum að :math:`f(x)` *stefni á tölu*
  :math:`L` *þegar* :math:`x` *stefnir á* :math:`-\infty`, og ritum
  :math:`\lim_{x\rightarrow -\infty} f(x)=L`, ef eftirfarandi skilyrði er
  uppfyllt:

  Fyrir sérhverja tölu :math:`\epsilon>0` er til tala :math:`R`
  þannig að um öll :math:`x<R` gildir að

  .. math:: |f(x)-L|<\epsilon.

Dæmi: Markgildi þegar :math:`x \to -\infty`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Lítum á veldisvísisfallið, þ.e. :math:`f(x)=e^x`. Reiknum markgildið

  .. math:: \lim_{x \rightarrow -\infty} e^x.

.. admonition:: Lausn
  :class: daemi, dropdown

  Samkvæmt því sem sagt var um vísisföll þá gildir að

  .. math:: \lim_{x \rightarrow -\infty} e^x = 0.

  Auðvelt er að sannfæra sig um þetta þegar litið er á graf veldisvísisfallsins.
  Athugum að því minna sem :math:`x` verður, því minna verður :math:`f(x)` án þess
  þó nokkurn tímann að snerta :math:`x`-ásinn.

  .. image:: ./myndir/kafli02/PMA_exp.png
    :width: 75%
    :align: center

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

.. admonition:: Skilgreining
  :class: skilgreining

  Látum :math:`A\subseteq {{\mathbb  R}}` og :math:`x\in A`. Við segjum að
  :math:`x` sé :hover:`innri punktur` :math:`A` ef :math:`A` inniheldur opið bil
  umhverfis :math:`x`, það er að segja til er tala :math:`\delta>0` þannig
  að :math:`(x-\delta, x+\delta)\subseteq A`.

  Ef :math:`x` er ekki innri punktur :math:`A` og :math:`x\in A` þá segjum
  við að :math:`x` sé :hover:`jaðarpunktur` :math:`A`.

Dæmi: Innri punktur
~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Fyrir bilið :math:`A` er punkturinn :math:`C` innri punktur en punkturinn
  :math:`B` jaðarpunktur.

  .. image:: ./myndir/kafli02/PMA_bil.png
   :align: center
   :width: 130%

.. index::
    samfelldni; í punkti

Skilgreining: Samfelldni í punkti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Látum :math:`f` vera fall og :math:`c` innri punkt skilgreiningarmengis
  :math:`f`. Sagt er að :math:`f` sé *samfellt í punktinum* :math:`c` ef

  .. math:: \lim_{x\rightarrow c}f(x)=f(c).

Setning
~~~~~~~

.. admonition:: Setning
  :class: setning

  Látum :math:`f` og :math:`g` vera föll. Gerum ráð fyrir að :math:`c` sé
  innri punktur skilgreiningarmengis beggja fallanna og að bæði föllin séu
  samfelld í punktinum :math:`c`. Þá eru eftirfarandi föll samfelld í
  :math:`c`:

  (i)   :math:`f+g`

  (ii)  :math:`f-g`

  (iii) :math:`fg`

  (iv)  :math:`kf`, þar sem :math:`k` er fasti

  (v)   :math:`f/g`, ef :math:`g(c)\neq 0`

  (vi)  :math:`\Big(f(x)\Big)^{1/n}`, að því gefnu að :math:`f(c)>0` ef
        :math:`n` er slétt tala og :math:`f(c)\neq 0` ef :math:`n<0`.

  Þessi setning er bein afleiðing af :ref:`reiknireglum fyrir markgildi <setning-markgildi>`.

Setning: Samskeyting samfelldra falla
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Látum :math:`g` vera fall sem er skilgreint á opnu bili umhverfis
  :math:`c` og samfellt í :math:`c` og látum :math:`f` vera fall sem er
  skilgreint á opnu bili umhverfis :math:`g(c)` og samfellt í
  :math:`g(c)`. Þá er fallið :math:`f\circ g` skilgreint á opnu bili
  umhverfis :math:`c` og er samfellt í :math:`c`.

.. admonition:: Athugasemd
  :class: athugasemd

    Ef fall er skilgreint með formúlu og skilgreingamengið er ekki tilgreint
    sérstaklega, þá er venjan að líta alla þá punkta þar sem formúlan gildir
    sem skilgreingarmengi fallsins


.. index::
    samfelldni, samfellt fall

.. _`skilgrsamfellt`:

Skilgreining: Samfellt fall
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Við segjum að fall :math:`f` sé :hover:`samfellt,samfellt fall` ef það er samfellt í
  sérhverjum punkti skilgreingarmengisins.

.. admonition:: Athugasemd
  :class: athugasemd

  Athugið að til að fall sé samfellt er einungis gerð krafa um að það sé samfellt
  í öllum punktum skilgreiningarmengi síns. Samkvæmt þessari skilgreiningu er fallið
  :math:`f(x)=\frac{1}{x}` með skilgreiningarmengið :math:`\mathbb{R} \setminus \{0\}`
  samfellt jafnvel þó það taki stökk í kringum :math:`x=0`
  einfaldlega af þeirri ástæðu að 0 er ekki í skilgreiningarmengi fallsins.

  .. image:: ./myndir/kafli02/PMA_1overx.png
	 :align: center
	 :width: 130%

.. admonition:: Aðvörun
  :class: advorun

  Bókin tekur aðeins annan pól í hæðina varðandi samfelldni ræðra falla (sbr. Ex. 2.29).
  Það er bein afleiðing af skilgreiningu þeirra á markgildi, sem er örlítði frábrugðin
  þeirri skilgreiningu sem við notum. Þetta er að vissu leyti túlkunaratriði.

Dæmi: Samfellt fall
~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

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

Fallið :math:`\cos(3x+5)` er samfellt. Margliðan :math:`g(x) =3x+5` og
:math:`f(x) = \cos(x)` eru samfelld föll og þá er samskeytingin
:math:`f\circ g(x) = \cos(3x+5)` einnig samfellt fall.


Rifjum upp skilgreininguna á samfelldni.

.. admonition:: Skilgreining
  :class: skilgreining

  Látum :math:`f` vera fall og :math:`c` innri punkt skilgreiningarmengis
  :math:`f`. Sagt er að :math:`f` sé *samfellt í punktinum* :math:`c` ef

  .. math:: \lim_{x\rightarrow c}f(x)=f(c).

.. admonition:: Athugasemd
  :class: athugasemd

  Þessi skilgreining virkar aðeins fyrir innri punkta
  skilgreiningarmengisins. Þannig að ef ætlunin er að rannsaka samfelldni
  í jaðarpunktum þá gengur þessi skilgreining ekki. Hins vegar getum við
  útvíkkað skilgreininguna á samfelldni fyrir hægri og vinstri endapunkta
  bila með því að einskorða okkur við markgildi frá vinstri og hægri.

Skilgreining: Hægri/vinstri samfelldni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  (i)  Fall :math:`f` er *samfellt frá hægri í punkti* :math:`c` ef
       :math:`\lim_{x\rightarrow c^+}f(x)=f(c)`.

       Hér er gert ráð fyrir að fallið :math:`f` sé amk. skilgreint á
       bili :math:`[c, a[`.

  (ii) Fall :math:`f` er *samfellt frá vinstri í punkti* :math:`c` ef
       :math:`\lim_{x\rightarrow c^-}f(x)=f(c)`.

       Hér er gert ráð fyrir að fallið :math:`f` sé amk. skilgreint á
       bili :math:`]a, c]`.

Uppfærum nú skilgreininguna á :ref:`samfelldu falli <skilgrsamfellt>`.

.. index::
    fall; samfellt

Skilgreining: Uppfærð skilgreining á samfelldu falli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Gerum ráð fyrir að :math:`f` sé fall sem er skilgreint á mengi
  :math:`A`, þar sem :math:`A` er sammengi endanlega margra bila. Við
  segjum að fallið :math:`f` sé *samfellt* ef það er samfellt í öllum
  innri punktum skilgreingarmengisins og ef það er samfellt frá
  hægri/vinstri í jaðarpunktum skilgreingarmengisins, eftir því sem við á.

.. admonition:: Athugasemd
  :class: athugasemd

    Ef fall er samfellt á opnu bili :math:`]a,b[`, og ef :math:`a<c<d<b`, þá
    er fallið einnig samfellt á bilinu :math:`[c,d]`.

-------

Eiginleikar samfelldra falla
----------------------------

.. index::
    há- og lággildislögmálið

.. _`Há- og lággildislögmálið`:

Setninging: Há- og lággildislögmálið
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Há- og lággildislögmálið
  :class: setning

  Látum :math:`f` vera samfellt fall skilgreint á **lokuðu takmörkuðu bili**
  :math:`[a,b]`. Þá eru til tölur :math:`x_1` og :math:`x_2` í
  :math:`[a,b]` þannig að fyrir allar tölur :math:`x` í :math:`[a,b]` er

  .. math:: f(x_1)\leq f(x)\leq f(x_2).

Þetta þýðir að samfellt fall :math:`f` á lokuðu og takmörkuðu bili
:math:`[a,b]` tekur bæði hæsta og lægsta gildi á bilinu. Hæsta gildið er
þá :math:`f(x_2)` og lægsta gildið er :math:`f(x_1)`.

.. admonition:: Athugasemd
  :class: athugasemd

    Það er mögulegt að fallið taki há/lággildi sitt í fleiri en einum
    punkti.

.. index::
    milligildissetningin

Setning: Milligildissetningin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Milligildissetningin
  :class: setning

  Látum :math:`f` vera samfellt fall skilgreint á lokuðu takmörkuðu bili
  :math:`[a,b]`. Gerum ráð fyrir að :math:`s` sé tala sem liggur á milli
  :math:`f(a)` og :math:`f(b)`. Þá er til tala :math:`c` sem liggur á
  milli :math:`a` og :math:`b` þannig að :math:`f(c)=s`.

  .. ggb:: zEQQcGcQ
      :width: 680
      :height: 400
      :img: 10_milligildissetn.png
      :imgwidth: 12cm

.. admonition:: Athugasemd
  :class: athugasemd

    Það er möguleiki að það séu fleiri en einn punktur á bilinu þar sem fallið tekur
    gildið :math:`s`.

Fylgisetning
~~~~~~~~~~~~

.. admonition:: Fylgisetning
  :class: setning

  Ef :math:`P(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0` er margliða af
  oddatölu stigi :math:`n`, þá er til rauntala :math:`c` þannig að :math:`P(c)=0`.
