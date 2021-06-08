
Afleiður
========
.. note::
    **Nauðsynleg undirstaða**
    
    - :ref:`markgildi`

    - :ref:`samfelldni`

    - :ref:`samskeyting falla <samskeyting>`

    - :ref:`andhverfur falla <andhverfa>`

    - hornaföll, P7

*He felt that his whole life was some kind of dream and he sometimes wondered whose it was and whether they were enjoying it.*

-- Douglas Adams, The Hitchhiker's Guide to the Galaxy


------
    
.. index::
    afleiða
    
.. _afleidur:

Skilgreining á afleiðu
----------------------

Skilgreining: Afleiða
~~~~~~~~~~~~~~~~~~~~~

Látum :math:`a` vera innri punkt skilgreiningarsvæðis falls :math:`f`.
:hover:`Afleiða falls,afleiða` :math:`f` *í punkti* :math:`a` er skilgreind sem

.. math:: f'(a)=\lim_{h\rightarrow 0}\frac{f(a+h)-f(a)}{h}.

Ef markgildið er til þá er sagt að fallið :math:`f` sé 
:hover:`diffranlegt,diffranlegur` *í
punktinum* :math:`a`, en annars er sagt að fallið sé *ekki diffranlegt í
punktinum* :math:`a`.

Dæmi
~~~~

Fallið :math:`f(x) = x^2` er diffranlegt í sérhverjum punkti :math:`a`.
Það sést af því að

.. math::
    \begin{aligned}
    \lim_{h\to 0} \frac{f(a+h)-f(a)}{h} 
    &= \lim_{h\to 0} \frac{(a+h)^2-a^2}{h}\\ 
    &= \lim_{h\to 0} \frac{a^2+2ah+h^2-a^2}{h}\\
    &= \lim_{h\to 0} \frac{2ah+h^2}{h}\\
    &= \lim_{h\to 0} 2a+h = 2a.\end{aligned}


.. ggb:: SUnNEmTG
    :width: 700
    :height: 500
    :img: ./01_afleida.png
    :imgwidth: 12cm

Setning
~~~~~~~

Ef fall :math:`f` er diffranlegt í punkti :math:`c` þá er :math:`f`
samfellt í punktinum :math:`c`.

.. begin-toggle::
    :label: Sýna sönnun

**Sönnun**

Skoðum markgildið :math:`f'(x)=\lim_{h\to 0} \frac{f(c+h)-f(c)}{h}`. Þar
sem :math:`h\to 0` þá verður teljarinn einnig að stefna á 0. Það er
:math:`\lim_{h \to 0} f(c+h)-f(c) = 0`, eða
:math:`\lim_{h \to 0} f(c+h) = f(c)`. Þetta má einnig rita
:math:`\lim_{x \to c} f(x) = f(c)`, sem þýðir að fallið :math:`f` er
samfellt í :math:`x=c`.

.. end-toggle::

.. warning::
    Fall getur verið samfellt í punkti :math:`c` án þess að það sé
    diffranlegt í :math:`c`.

Dæmi
~~~~

Fallið :math:`f(x) = |x|` er samfellt. En það er ekki diffranlegt í
punktinum :math:`x=0`. Það sést af því að

.. math::
    \lim_{h\to 0^+} \frac{f(0+h)-f(0)}{h} = \lim_{h\to 0^+} \frac{|h|}{h} = 1

en

.. math::
    \lim_{h\to 0^-} \frac{f(0+h)-f(0)}{h} = \lim_{h\to 0^-} \frac{|h|}{h} = -1.

Þannig að markgildið :math:`\lim_{h\to 0} \frac{f(0+h)-f(0)}{h}` er ekki til og því er 
fallið ekki diffranlegt í :math:`x=0`.

.. index::
    snertill
    sniðill
    seealso: snertill; sniðill
    seealso: sniðill; snertill

Snertill
~~~~~~~~

Afleiðu falls :math:`f` í punktinum :math:`a` fæst með því að taka
:hover:`sniðil,sniðill` í gegnum punktana :math:`(a,f(a))` og :math:`(a+h,f(a+h))`, og
láta svo :math:`h` stefna á :math:`0`.

Þetta gefur hallatölu :hover:`snertilsins,snertill` við graf fallsins í punktinum
:math:`(a,f(a))`

Jafna snertils við graf fallsins í punktingum :math:`a` er línan

.. math:: y = f'(a)(x-a) + f(a).

.. ggb:: 1425869
    :width: 700
    :height: 400
    :img: ./01_05_snertill.png
    :imgwidth: 12cm
    :zoom_drag: true 


Athugasemd: Hallatalan :math:`\infty` er ekki leyfð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við leyfum ekki :math:`f'(a) = \infty` eða 
:math:`f'(a) = -\infty`. Samanber
:math:`f(x) = x^{\frac 13}` í :math:`a=0`,

.. math::

   \lim_{h \to 0} \frac{f(0+h)-f(0)}h = 
	\lim_{h \to 0} \frac{h^{\frac 13}}h = 
       \lim_{h \to 0} h^{-\frac 23} = \infty.

Hér ætti því jafna snertilsins að vera :math:`x=0`.

.. image:: ./myndir/kafli03/01_x13.png
	:align: center
	:width: 12cm

Við viljum að snertillinn sé nálgun við graf fallsins fyrir :math:`x` nálægt
:math:`a`, lóðrétt lína er gagnslaus nálgun því hún er ekki skilgreind sem 
fall af :math:`x`.

-------

Útvíkkun fyrir lokuð bil
------------------------

Ef fallið :math:`f` er skilgreint á lokuðu bili þá getum við skilgreint
afleiðuna í endapunktunum með því að taka markgildi frá hægri/vinstri
eftir því sem við á.

.. index::
    afleiða; hægri/vinstri

Skilgreining: Hægri/vinstri afleiða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(i)  *Hægri afleiða falls* :math:`f` *í punkti* :math:`x` er skilgreind
     sem

     .. math:: f_+'(x)=\lim_{h\rightarrow 0^+}\frac{f(x+h)-f(x)}{h}.

(ii) *Vinstri afleiða falls* :math:`f` *í punkti* :math:`x` er
     skilgreind sem

     .. math:: f_-'(x)=\lim_{h\rightarrow 0^-}\frac{f(x+h)-f(x)}{h}.

Setning
~~~~~~~

Ef :math:`x` er innri punktur í skilgreiningarsvæði fallsins :math:`f`
þá er :math:`f` diffranlegt í :math:`x` þá og því aðeins að

.. math::

   f_+'(x)=\lim_{h\rightarrow 0^+}\frac{f(x+h)-f(x)}{h}
   =   f_-'(x)=\lim_{h\rightarrow 0^-}\frac{f(x+h)-f(x)}{h},

og þá er :math:`f'(x)` jafnt og markgildin hér fyrir ofan.

Þetta leiðir beint af skilgreiningunum hér á undan og 
:ref:`Setningu 2.2.5 <setning-hv_markgildi>`.
 
.. index::
    afleiða; diffranlegt fall

Skilgreining: Diffranlegt fall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera fall með skilgreiningarsvæði :math:`A`. Gerum ráð
fyrir að :math:`A` sé sammengi endanlega margra bila. Við segjum að
fallið :math:`f` sé *diffranlegt* ef það er diffranlegt í öllum innri
punktum :math:`A` og diffranlegt frá vinstri/hægri í jaðarpunktum
:math:`A` eftir því sem við á.

Ritháttur
~~~~~~~~~

Afleiða falls :math:`f` er ýmist táknuð með

.. math:: f', \qquad \frac {df}{dx}, \qquad D_x f \qquad \text{eða} \qquad Df.

Ef við skrifum :math:`y=f(x)` þá má einnig tákna hana með

.. math:: y', \qquad \frac {dy}{dx}, \qquad D_x y \qquad \text{eða} \qquad Dy.

Dæmi
~~~~

Fallið :math:`f(x) = \sqrt{x}`, :math:`f:[0,\infty[\to {{\mathbb  R}}`
er diffranlegt á menginu :math:`]0,\infty[` og afleiðan er gefin með
:math:`f'(x) = \frac 1{2\sqrt{x}} = \frac 12 x^{-1/2}` þar. Hins vegar
er :math:`f` ekki diffranlegt í :math:`x=0` þrátt fyrir að fallgildið sé
vel skilgreint (og fallið samfellt frá hægri) þar.

Ef :math:`x>0` þá fæst

.. math::

   \begin{aligned}
     \lim_{h\to 0} \frac{\sqrt{x+h}-\sqrt{x}}h &= 
     \lim_{h\to 0} \frac{(\sqrt{x+h}-\sqrt{x})(\sqrt{x+h}+\sqrt{x})}{h(\sqrt{x+h}+\sqrt{x})}\\ 
     &= \lim_{h\to 0} \frac{\sqrt{x+h}^2-\sqrt{x}^2}{h(\sqrt{x+h}+\sqrt{x})}\\
     &= \lim_{h\to 0} \frac{x+h-x}{h(\sqrt{x+h}+\sqrt{x})}\\
     &= \lim_{h\to 0} \frac{1}{\sqrt{x+h}+\sqrt{x}} = \frac{1}{2\sqrt{x}},\end{aligned}

sem segir okkur að :math:`f'(x) = \frac 12 x^{-1/2}`.

Í vinstri endapunkti skilgreingarsvæðisins, :math:`x=0`, þá fæst hins
vegar

.. math::

   \begin{aligned}
     \lim_{h\to 0^+} \frac{\sqrt{h}-\sqrt{0}}h &= 
     \lim_{h\to 0^+} \frac{\sqrt{h}}h\\
     &= \lim_{h\to 0^+} \frac{1}{\sqrt{h}} = \infty,\end{aligned}

sem sýnir að fallið er ekki diffranlegt frá hægri í :math:`x=0`.

--------

Reiknireglur
------------

.. _`Setning 3.3.1`:

Setning
~~~~~~~

Látum :math:`f` og :math:`g` vera föll sem eru diffranleg í punkti
:math:`x`. Þá eru föllin :math:`f+g,\ f-g, kf` (þar sem :math:`k` er
fasti) og :math:`fg` diffranleg í punktinum :math:`x`, og ef
:math:`g(x)\neq 0` þá eru föllin :math:`1/g` og :math:`f/g` líka
diffranleg í :math:`x`.

Eftirfarandi formúlur gilda um afleiður fallanna sem talin eru upp hér
að framan:

(i)   :math:`(f+g)'(x)=f'(x)+g'(x)`

(ii)  :math:`(f-g)'(x)=f'(x)-g'(x)`

(iii) :math:`(kf)'(x)=kf'(x)`, þar sem :math:`k` er fasti

(iv)  :math:`(fg)'(x)=f'(x)g(x)+f(x)g'(x)`

(v)   :math:`\displaystyle\Bigg(\frac{1}{g}\Bigg)'(x)=\frac{-g'(x)}{g(x)^2}`,
      ef :math:`g(x)\neq 0`

(vi)  :math:`\displaystyle\Bigg(\frac{f}{g}\Bigg)'(x)=
      \frac{f'(x)g(x)-f(x)g'(x)}{g(x)^2}`, ef :math:`g(x)\neq 0`

.. _`Setning 3.3.2`:
      
Nokkrar afleiður
~~~~~~~~~~~~~~~~

(i)   :math:`\frac{d}{dx} c =  \lim_{h\to 0} \frac{c-c}h = 0`

(ii)  :math:`\frac{d}{dx} x =  \lim_{h\to 0} \frac{x+h-x}h = 1`

(iii) :math:`\frac{d}{dx} x^2 = \lim_{h\to 0} \frac{x^2+2xh+h^2-x^2}h
      = \lim_{h\to 0} \frac{2xh + h^2}h = \lim_{h\to 0} 2x+h= 2x`

.. _`Setning 3.3.3`:

Setning
~~~~~~~

.. math:: \frac{d}{dx} x^n = n x^{n-1}

.. begin-toggle::
    :label: Sýna sönnun

**Sönnun**

Sýnum þetta með þrepun.Tilfellið :math:`n=1` er afgreitt hér að ofan
(`3.3.2 (2) <Setning 3.3.2>`_).
Gerum ráð fyrir að niðurstaðan gildi fyrir :math:`n` og sýnum að þá
gildi hún einnig fyrir :math:`n+1`,

.. math::

   \frac{d}{dx} x^{n+1} = \frac{d}{dx} (x\cdot x^n) = 
       \left(\frac{d}{dx} x\right) x^n + x\frac{d}{dx} x^n
       = x^n + x\, 
       \underbrace{n\, x^{n-1}}_\text{þ.f.} 
       = (n+1) x^n.

.. end-toggle::

Afleiður margliða
~~~~~~~~~~~~~~~~~

Með því að nota setningarnar að ofan þá eigum við ekki í neinum
vandræðum með að diffra margliður. `Setning 3.3.1`_ (i) segir
að við getum diffrað hvern lið fyrir sig, liður (iii) í sömu setningu
segir að við getum tekið fastana fram fyrir afleiðuna og loks segir
`Setning 3.3.3`_ hvernig við diffrum :math:`x^n`.

Dæmi: Afleiða margliðu
~~~~~~~~~~~~~~~~~~~~~~

Finnum afleiðu margliðunnar :math:`p(x) = 4x^3-2x + 5`. Nú er

.. math::

   \begin{aligned}
   \frac{d}{dx} p(x) 
   &= \frac{d}{dx}4x^3 - \frac{d}{dx}2x + \frac{d}{dx}5 \\
   &= 4\frac{d}{dx}x^3 -2\frac{d}{dx}x + \frac{d}{dx}5 =
   4\cdot 3x^2 -2\cdot 1 + 0 = 12x^2-2\end{aligned}

.. index::
    keðjureglan
    
.. _kedjuregla:
   
Setning: Keðjureglan
~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`f` og :math:`g` séu föll þannig að :math:`g`
er diffranlegt í :math:`x` og :math:`f` er diffranlegt í :math:`g(x)`.
Þá er samskeytingin :math:`f\circ g` diffranleg í :math:`x` og

.. math:: (f\circ g)'(x) = f'(g(x))\cdot g'(x).

Dæmi
~~~~

Skoðum föllin :math:`f(x) = \sqrt x` og :math:`g(x) = 3x^5`. Bæði þessi föll eru
diffranleg og afleiðurnar eru :math:`f'(x) = \frac 12 x^{-1/2}` og 
:math:`g'(x) = 15x^4`. Afleiða samskeytingarinnar :math:`f\circ g` er þá 
samkvæmt keðjureglunni

.. math::
        (f\circ g)'(x) = \frac 12 (3x^5)^{-1/2} \cdot 15x^4.

--------

   
Hærri afleiður
--------------

Skilgreining
~~~~~~~~~~~~

Látum :math:`f` vera fall. *Afleiðan* :math:`f'` er fall sem skilgreint er
í öllum punktum þar sem :math:`f` er diffranlegt.

Ef fallið :math:`f'` er diffranlegt í punkti :math:`x` þá er afleiða
:math:`f'` í punktinum :math:`x` táknuð með :math:`f''(x)` og kölluð
:hover:`önnur afleiða` :math:`f` í punktinum :math:`x`. Líta má á aðra afleiðu
:math:`f` sem fall :math:`f''` sem er skilgreint í öllum punktum þar sem
:math:`f'` er diffranlegt.

Almennt má skilgreina :math:`n`\ *-tu afleiðu* :math:`f`, táknaða með
:math:`f^{(n)}`, þannig að í þeim punktum :math:`x` þar sem fallið
:math:`f^{(n-1)}` er diffranlegt þá er
:math:`f^{(n)}(x)=\frac{d}{dx}f^{(n-1)}(x)`.

Dæmi
~~~~

Ef :math:`f(x)  = 3x^2`, þá er

.. math:: f'(x) = 3\frac{d}{dx}x^2 = 3\cdot 2x = 6x 

og

.. math:: f''(x) = \frac{d}{dx} 6x = 6.

Ritháttur
~~~~~~~~~

Ritum :math:`y=f(x)`.

Þá má tákna fyrstu afleiðu :math:`f` með

.. math:: y'= f'(x)=\frac{d}{dx}f(x)=D_xf(x)\ =\ D_x y= \frac{dy}{dx},

aðra afleiðuna með

.. math::

   \begin{aligned}
   y'' &=
   f''(x)=\frac{d}{dx}f'(x)=\frac{d}{dx}\frac{d}{dx}f(x)
   = D^2_xf(x)= D^2_x y=\frac{d^2}{dx^2}f(x)=\frac{d^2 y}{dx^2}\end{aligned}

og almennt :math:`n`-tu afleiðuna 

.. math::

   \begin{aligned}
   y^{(n)} &= f^{(n)}(x)=\frac{d}{dx}f^{(n-1)}(x)=
   \frac{d}{dx}\Big(\frac{d^{n-1}}{dx^{n-1}}f(x)\Big) \\
   &=D^n_xf(x)\ =\ D^n_x y
   =\frac{d^n}{dx^n}f(x)
   = \frac{d^n y}{dx^n}.\end{aligned}

.. note::
    Venja er að rita :math:`f'''` til að tákna þriðju afleiðu :math:`f` en
    afar sjaldgæft að :math:`f''''` sé notað til að tákna fjórðu afleiðu
    :math:`f` og mun algengara að nota :math:`f^{(4)}`.

------

.. _utgildi:

Útgildi
-------

.. index::
    útgildi
    útgildi; hágildi
    útgildi; lággildi


Skilgreining: Útgildi
~~~~~~~~~~~~~~~~~~~~~

Við segjum að fall :math:`f` hafi :hover:`staðbundið hágildi` í punktinum
:math:`x_0` ef til er bil :math:`(a,b)` umhverfis :math:`x_0`, sem er
þannig að

.. math:: f(x) \leq f(x_0), \quad \text{ fyrir öll } x \in (a,b).

Við segjum að fall :math:`f` hafi :hover:`staðbundið lággildi` í punktinum
:math:`x_0` ef til er bil :math:`(a,b)` umhverfis :math:`x_0`, sem er
þannig að

.. math:: f(x) \geq f(x_0), \quad \text{ fyrir öll } x \in (a,b).

Tölum um að fallið :math:`f` hafi :hover:`staðbundið útgildi` í punktinum
:math:`x_0` ef það hefur staðbundið hágildi eða staðbundið lággildi þar.

.. _`Setning 3.5.2`:

Setning
~~~~~~~

Ef fallið :math:`f` hefur staðbundið útgildi í punktinum :math:`x_0` og
er diffranlegt þá er :math:`f'(x_0)=0`.

.. begin-toggle::
    :label: Sýna sönnun

|

**Sönnun**

Gerum ráð fyrir að :math:`f` hafi staðbundið hágildi í punktinum :math:`x_0`.
Þá er :math:`f(x_0)-f(x)\geq 0` og ef :math:`x<x_0`, 
þá fæst að  :math:`\frac{f(x_0)-f(x)}{x_0-x}\geq 0`. Þetta þýðir að

.. math::

   \lim_{x \to x_0^-} = \frac{f(x_0) - f(x)}{x_0-x} \geq 0.

Eins þá er :math:`f(x_0)-f(x)\geq 0` og ef :math:`x_0<x`,
þá er :math:`\frac{f(x_0)-f(x)}{x_0-x} \leq 0`.
Þetta þýðir að

.. math::

   \lim_{x \to x_0^+} = \frac{f(x_0) - f(x)}{x_0-x} \leq 0.

Við vitum að markgildið
:math:`\lim_{x\to x_0} \frac{f(x_0)-f(x)}{x_0-x}` er til þar sem fallið
er diffranlegt, það þýðir að markgildin frá hægri og vinstri eru þau
sömu. Eina leiðin til þess að það samræmist hægri og vinstri markgildunum 
hér að ofan er ef

.. math:: f'(x_0) = \lim_{x\to x_0} \frac{f(x_0)-f(x)}{x_0-x} = 0.

.. end-toggle::

|
|

.. warning::

    Þó að :math:`f'(a)=0` þá er ekki víst að :math:`a` sé staðbundið útgildi.

    Til dæmis þá hefur fallið :math:`f(x) = x^3` ekkert staðbundið útgildi
    þrátt fyrir að :math:`f'(0) = 0` (:math:`f'(x) = 3x^2`).

----------

Hornaföll og afleiður þeirra
----------------------------

Setning
~~~~~~~

(i)   :math:`\displaystyle\lim_{x\rightarrow 0}\frac{\sin x}{x}=1`

(ii)  :math:`\displaystyle\lim_{x\rightarrow 0}\frac{\cos x-1}{x}=0`

(iii) :math:`\displaystyle\frac{d}{dx}\sin x=\cos x`

(iv)  :math:`\displaystyle\frac{d}{dx}\cos x=-\sin x`

(v)   :math:`\displaystyle\frac{d}{dx}\tan x=\frac{1}{\cos^2 x}=1+\tan^2 x`

--------

Meðalgildissetningin
--------------------

.. index::
    setning Rolle

.. _`rolle`: 
    
Setning Rolle
~~~~~~~~~~~~~

Látum :math:`g:[a,b]\rightarrow{{\mathbb  R}}` vera samfellt fall. Gerum
ráð fyrir að :math:`g` sé diffranlegt í öllum punktum í bilinu
:math:`(a,b)`. Ef :math:`g(a)=g(b)` þá er til punktur :math:`c` á bilinu
:math:`(a,b)` þannig að :math:`g'(c)=0`.

.. begin-toggle::
    :label: Sýna sönnun

**Sönnun**

Ef :math:`g(x)=c` er fasti, þá er :math:`g'(x)=0`. Ef hins vegar
:math:`g` er ekki fasti þá er til :math:`x \in (a,b)` þannig að
:math:`g(x)\neq g(a)`, gerum ráð fyrir að :math:`g(x)>g(a)` 
(tilfellið ef :math:`g(x)<g(a)` gengur nánast eins fyrir sig).
Samkvæmt `Há- og lággildislögmálinu <Há- og lággildislögmálið>`_ 
þá tekur fallið :math:`g` sitt hæsta
gildi í punkti :math:`c` á bilinu :math:`[a,b]`.Þar sem
:math:`g(c)\geq g(x) >  g(a) = g(b)` þá getur :math:`c` hvorki verið
:math:`a` né :math:`b`.
Þar sem :math:`c`
er útgildi þá segir `Setning 3.5.2`_ að :math:`g'(c)=0`.

.. end-toggle::

.. index::
    meðalgildissetningin

Meðalgildissetningin
~~~~~~~~~~~~~~~~~~~~

Látum :math:`f:[a,b]\rightarrow{{\mathbb  R}}` vera samfellt fall. Gerum
ráð fyrir að :math:`f` sé diffranlegt í öllum punktum í bilinu
:math:`(a,b)`. Þá er til punktur :math:`c` í bilinu :math:`(a,b)` þannig
að

.. math:: \frac{f(b)-f(a)}{b-a}=f'(c).

.. begin-toggle::
	:label: Sýna sönnun

**Sönnun**

Skilgreinum nýtt fall 

.. math:: h(x)=f(x)-\left(f(a)+ \frac{f(b)-f(a)}{b-a}(x-a)\right).

Athugið að :math:`h` er bara :math:`f` mínus :hover:`línufallið,línufall` gegnum punktana
:math:`(a,f(a))` og :math:`(b,f(b))`. Þetta þýðir að :math:`h` er diffranlegt
og að :math:`h(a)=h(b)=0`. Þá gefur `Setning Rolle <rolle>`_ að til er :math:`c` þannig að
:math:`h'(c)=0`. 

Nú er 

.. math:: 
	h'(x) = f'(x) - \left(0+\frac{f(b)-f(a)}{b-a}(1-0)\right)
	= f'(x) - \frac{f(b)-f(a)}{b-a}

þannig að

.. math:: 0 = h'(c) = f'(c) - \frac{f(b)-f(a)}{b-a},

eða

.. math:: f'(c) = \frac{f(b)-f(a)}{b-a}.

.. end-toggle::

.. note::
    Niðurstöðuna úr :hover:`meðalgildissetningunni,meðalgildissetning` má orða svona: 

    Í einhverjum punkti á bilinu er stundarbreytingin jöfn meðalbreytingunni
    yfir allt bilið.

.. index::
    meðalgildissetningin

Alhæfða meðalgildissetningin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að föllin :math:`f` og :math:`g` séu samfelld á lokaða
bilinu :math:`[a,b]` og diffranleg á opna bilinu :math:`(a,b)`. Gerum
auk þess ráð fyrir að fyrir allar tölur :math:`x` í :math:`(a,b)` sé
:math:`g'(x)\neq 0`. Þá er til tala :math:`c\in (a,b)` þannig að

.. math:: \frac{f(b)-f(a)}{g(b)-g(a)}=\frac{f'(c)}{g'(c)}.

----------

.. _vaxandiminnkandi:

Vaxandi og minnkandi föll
-------------------------

.. index::
    fall; vaxandi/minnkandi

Skilgreining: Vaxandi/minnkandi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fall :math:`f` er *vaxandi* á bili :math:`(a,b)` ef um
alla punkta :math:`x_1` og :math:`x_2` á :math:`(a,b)` þannig að
:math:`x_1 < x_2` gildir að

.. math:: f(x_1) \leq f(x_2).

Fall :math:`f` er *stranglega vaxandi* á bili :math:`(a,b)`
ef um alla punkta :math:`x_1` og :math:`x_2` á :math:`(a,b)` þannig að
:math:`x_1 < x_2` gildir að

.. math:: f(x_1) < f(x_2).

Fall :math:`f` er *minnkandi* á bili :math:`(a,b)` ef um
alla punkta :math:`x_1` og :math:`x_2` á :math:`(a,b)` þannig að
:math:`x_1 < x_2` gildir að

.. math:: f(x_1) \geq f(x_2).

Fall :math:`f` er *stranglega minnkandi* á bili
:math:`(a,b)` ef um alla punkta :math:`x_1` og :math:`x_2` á
:math:`(a,b)` þannig að :math:`x_1 < x_2` gildir að

.. math:: f(x_1) > f(x_2).

.. note::
    Kennslubókin notar *nondecreasing/nonincreasing* fyrir vaxandi/minnkandi og
    *increasing/decreasing* fyrir stranglega vaxandi/minnkandi.

    Einnig þekkist að nota *increasing/decreasing* og *strictly increasing/decreasing*.
    Til dæmis er það gert á `Wikipedia: Monotonic functions <https://en.wikipedia.org/wiki/Monotonic_function>`_.

.. _vaxandieoae:

Setning
~~~~~~~

Látum :math:`f` vera diffranlegt fall á bili. Þá er :math:`f` vaxandi þá og því
aðeins að :math:`f' \geq 0`.

.. begin-toggle::
    :label: Sýna sönnun

**Sönnun**

Byrjum á að gera ráð fyrir að fallið sé vaxandi. Festum punkt :math:`x` og 
sýnum að :math:`f'(x)\geq 0`. Þar sem :math:`f` er vaxandi þá gildir fyrir 
sérhvert :math:`h>0` að

.. math::
    \frac{f(x+h)-f(x)}{h} \geq 0

Þá gildir einnig um markgildið :math:`\lim_{h\to 0^+} \frac{f(x+h)-f(x)}h \geq 0`.

Ef hins vegar :math:`h<0` þá er :math:`x+h < x` og því 
:math:`f(x+h)<f(x)`. Þetta gefur að 

.. math::
    \frac{f(x+h)-f(x)}h \geq 0

sem þýðir að :math:`\lim_{h\to 0^-} \frac{f(x+h)-f(x)}h \geq 0`. Og þar af leiðandi
er :math:`f'(x) = \lim_{h\to 0} \frac{f(x+h)-f(x)}h \geq 0`.

--------------

Gerum nú ráð fyrir :math:`f'\geq 0` og sýnum að þá sé fallið vaxandi. 
Festum tvo punkta :math:`x_1 < x_2`. Ef :math:`f(x_1) > f(x_2)`, það er
:math:`f(x_2)-f(x_1)<0` 
þá er 

.. math:: 
    \frac{f(x_2)-f(x_1)}{x_2-x_1} < 0.

Samkvæmt meðalgildissetningunni þá er til punktur :math:`¢` á bilinu :math:`[x_1,x_2]` 
þar sem afleiðan tekur þetta gildi, en það er í mótsögn við að  :math:`f'(c)\geq 0`.

.. end-toggle::

.. _minnkandieoae:

Setning
~~~~~~~

Látum :math:`f` vera diffranlegt fall á bili. Þá er :math:`f` minnkandi þá og
því aðeins að :math:`f' \leq 0`.

Setning
~~~~~~~

Látum :math:`f` vera diffranlegt fall á bili. Ef :math:`f'>0` þá er :math:`f`
stranglega vaxandi.

Setning
~~~~~~~

Látum :math:`f` vera diffranlegt fall á bili. Ef :math:`f'<0` þá er :math:`f`
stranglega minnkandi.

.. warning::

    Diffranlegt fall getur verið stranglega vaxandi/minnkandi án þess að
    afleiðan sé alls staðar stærri/minni en 0. Til dæmis er afleiða :math:`f(x)=x^3` jöfn 0 í
    :math:`x=0` en fallið er stranglega vaxandi á öllum rauntalnaásnum.

Afleiður fastafalla
~~~~~~~~~~~~~~~~~~~

Við vitum að ef :math:`f` er fasti, það er :math:`f(x)=c`, þá er
:math:`f'(x)=0` fyrir öll :math:`x`.

Nú fáum við einnig eftirfarandi út frá Setningum :ref:`3.8.2 <vaxandieoae>` og :ref:`3.8.3 <minnkandieoae>`:

Ef :math:`f` er diffranlegt fall á bili :math:`I` sem er þannig að
:math:`f'(x) = 0` á :math:`I`, þá er :math:`f` fasti,
þ.e. \ :math:`f(x) = c` fyrir öll :math:`x\in I`.

----------

Fólgin diffrun
--------------

Dæmi
~~~~

Jafna hrings með geisla 1 er :math:`x^2+y^2=1`. Við vitum að hægt er að
skrifa efri og neðri helminga hans sem föll af :math:`y`, annars vegar
:math:`y=\sqrt{1-x^2}` og hins vegar :math:`y=-\sqrt{1-x^2}`. Ef við
viljum finna snertil við hringinn getum við notað þessi föll. En þar sem
við vitum að hægt er að skrifa :math:`y` sem fall af :math:`x` þá getum
við einnig diffrað jöfnu hringsins beint með aðstoð keðjureglunnar,

.. math::

   \begin{aligned}
   \frac{d}{dx}(x^2+y^2) &=& \frac{d}{dx} 1\\
       2x + 2y\frac{dy}{dx} &=& 0\\
       y\frac{dy}{dx} &=& -x\\
       \frac{dy}{dx} &=& -\frac xy.\end{aligned}

.. image:: ./myndir/kafli03/11_hringur.png
	:align: center
	:width: 12cm

Setning: Andhverfusetningin
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum feril vera gefinn með :math:`F(x,y) =0`, þar sem :math:`F` er
diffranlegt í bæði :math:`x` og :math:`y`. Í punktum þar sem *snertill* 
ferilsins er ekki lóðréttur (þ.e. :math:`\frac{d}{dy}F \neq 0`) þá er hægt að
skrifa :math:`y` sem fall af :math:`x` og þá fæst af keðjureglunni að

.. math:: \frac{d}{dx} F(x,y) + \frac{d}{dy}F(x,y) \frac{dy}{dx} = 0,

þ.e.

.. math:: \frac{dy}{dx} = -\frac{\frac{d}{dx} F(x,y)}{\frac{d}{dy} F(x,y)}.

Sjá https://en.wikipedia.org/wiki/Inverse_function_theorem

Með öðrum orðum
~~~~~~~~~~~~~~~

Það kemur í sama stað niður að einangra :math:`y=f(x)`, ef það er
mögulegt, og finna :math:`y'` með því að diffra, eins og að diffra
:math:`F(x,y)=0` og einangra svo :math:`y'=\frac{dy}{dx}`.

Vinnulag
~~~~~~~~

(i)     Diffrum báðar hliðar jöfnunar með tilliti til :math:`x`, og lítum á
        :math:`y` sem fall af :math:`x` sem við diffrum með aðstoð
        keðjureglunnar (og gleymum ekki :math:`y'`)

(ii)    Einangrum :math:`y'`

(iii)   Skiptum :math:`y` út fyrir :math:`f(x)`.

Setning: Hagnýting á fólginni diffrun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`n` og :math:`m` eru heilar tölur þá er

.. math:: \frac{d}{dx} x^{\frac nm} = \frac nm x^{\frac nm -1}.

.. begin-toggle:: 
    :label: Sýna sönnun

**Sönnun**

Punktar á grafi fallsins :math:`x^{n/m}` ákvarðast af jöfnunni :math:`y=x^{n/m}`, það er
:math:`y^m = x^n`. Skilgreinum því 

.. math:: F(x,y) = x^n-y^m

Þar sem :math:`\frac d{dx} F(x,y) = nx^{n-1}` og 
:math:`\frac d{dy} F(x,y) = -my^{m-1}` þá fæst að 

.. math:: 

   \begin{aligned}
   y' &= \frac {d}{dx} y = 
   - \frac{n x^{n-1}}{-m y^{m-1}} = 
   \frac{n x^{n-1}}{m (x^{\frac nm})^{m-1}} \\
   &= \frac nm x^{(n-1) - \frac nm(m-1)} 
   = \frac nm x^{n-1-n+\frac nm} = \frac nm x^{\frac nm -1}. \end{aligned}

.. end-toggle::

------

.. index::
    fall; andhverfa

Andhverf föll
-------------

.. todo::
    Flytja/vísa í kafla 1?


Rifjum upp að gagntæk vörpun :math:`f:X\to Y` hefur andhverfu 
:math:`f^{-1}:Y\to X` sem uppfyllir að

.. math:: y=f(x)\qquad\text{þá og því aðeins að}\qquad x=f^{-1}(y).

Sjá :ref:`kafla 1.4 <andhverfa>`.


Athugasemd
~~~~~~~~~~

Látum :math:`f:X \to Y` vera fall sem skilgreint er á mengi :math:`X`. Gerum ráð
fyrir að :math:`f` sé eintækt. Með því að einskorða bakmengi :math:`f` við 
myndmengið :math:`\tilde Y = f(X)` þá verður :math:`f:X\to \tilde Y` gagntækt fall. 
Þá er til andhverfa :math:`f^{-1}:\tilde Y \to X` sem uppfyllir

.. math:: y=f(x)\qquad\text{þá og því aðeins að}\qquad x=f^{-1}(y).


Setning
~~~~~~~

Fall sem er strangt vaxandi eða strangt minnkandi er eintækt og á sér
því andhverfu.

Eiginleikar
~~~~~~~~~~~

(i)    :math:`y=f^{-1}(x)` þá og því aðeins að :math:`x=f(y)`.

(ii)   Skilgreingarsvæði :math:`f` er myndmengi :math:`f^{-1}`.

(iii)  Myndmengi :math:`f^{-1}` er jafnt skilgreiningarsvæði :math:`f`.

(iv)   :math:`f^{-1}(f(x))=x` fyrir öll :math:`x` í skilgreiningarsvæði
       :math:`f`.

(v)    :math:`f(f^{-1}(x))=x` fyrir öll :math:`x` í skilgreiningarsvæði
       :math:`f^{-1}`.

(vi)   :math:`(f^{-1})^{-1}(x)=f(x)` fyrir öll :math:`x` í
       skilgreiningarsvæði :math:`f`, alltsvo :math:`(f^{-1})^{-1}=f`.

(vii)  Graf :math:`f^{-1}` er speglun á grafi :math:`f` um línuna
       :math:`y=x`.

.. index::
    afleiða; andhverfa
       
Setning: Afleiða andhverfunnar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f` hafi andhverfu :math:`f^{-1}`. Látum
:math:`x` vera á skilgreiningarsvæði :math:`f` og gerum ráð fyrir að
:math:`f` sé diffranlegt í punktinum :math:`f^{-1}(x)` og að
:math:`f'(f^{-1}(x)) \neq 0`. Þá er :math:`f^{-1}` diffranlegt í
punktinum :math:`x` og

.. math:: \left(f^{-1}\right)'(x)=\frac{1}{f'(f^{-1}(x))}

.. note::
    Setningin segir okkur sér í lagi að láréttur snertill við :math:`f`
    svarar til lóðrétts snertils við :math:`f^{-1}`.

--------

Línulegar nálganir
------------------

Staðbundnar nálganir
~~~~~~~~~~~~~~~~~~~~

Skoðum diffranlegt fall :math:`f` í grennd um fastan punkt
:math:`a`. Látum :math:`x` vera punkt í grennd um :math:`a`.
Ef graf fallsins er ekki ,,mjög
sveigt” þá er snertillinn við :math:`(a,f(a))` næstum samsíða
sniðlinum gegnum :math:`(a,f(a))` og :math:`(x,f(x))`. 
Það þýðir að 

.. math::
   \begin{aligned}
        \frac{f(x)-f(a)}{x-a} &\approx f'(a),\\
        f(x)-f(a) &\approx  f'(a)(x-a),\\
        f(x) &\approx f'(a)(x-a) + f(a).
   \end{aligned}

.. warning:: 
    Athugið að hér er :math:`a` fast en :math:`x` breytist.


.. note:: 
    Einnig er hægt að skrifa þetta á eftirfarandi hátt.
    Setjum :math:`\Delta x = x-a` og 
    :math:`\Delta y = f(x) - f(a)` þá þýðir þetta að 
    :math:`\Delta y \approx \Delta x f'(a)`.

    Það er, breytingin á fallgildinum er um það bil breytingin í 
    breytunni margfaldað við afleiðuna í punktinum.


Skilgreining: Línuleg nálgun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Línuleg nálgun á falli :math:`f` nálægt :math:`a`, eða 1. stigs 
Taylor-margliða :math:`f` í :math:`a`, er gefin með
:math:`P_1(x)=f(a)+f'(a)(x-a)`.

Setning: Skekkjumat
~~~~~~~~~~~~~~~~~~~

Skekkjan í nálguninni :math:`E_1(x)=f(x)-P_1(x)` uppfyllir að til er
tala :math:`X \in (a,x)` þannig að

.. math:: E_1(x)=\frac{f''(X)}{2}(x-a)^2.

Skekkjumat fyrir línulegar nálganir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`f''(t)` sé skilgreint fyrir öll :math:`t` í
opnu bili sem inniheldur bæði :math:`a` og :math:`x`. Gerum enn fremur
ráð fyrir að :math:`m` og :math:`M` séu tölur þannig að fyrir öll
:math:`t\in (a, x)` gildi að :math:`m\leq f''(t)\leq M`. Þá er

.. math::

   \frac{m}{2}(x-a)^2\leq E_1(x)
   =\frac{f''(X)}{2}(x-a)^2\leq \frac{M}{2}(x-a)^2,

sem gefur að

.. math::

   f(a)+f'(a)(x-a)+\frac{m}{2}(x-a)^2\leq f(x) 
   \leq f(a)+f'(a)(x-a)+\frac{M}{2}(x-a)^2.

------

Taylor-margliður
----------------

Línuleg nálgun á falli er ekkert annað en nálgun með fyrsta stigs
margliðu.

Spurningin er því hvort hægt sé að nota margliður af hærra stigi og fá
þá betri nálgun?

Hvernig er 0. stigs nálgun á falli?

.. index::
    Taylor margliða

Skilgreining: Taylor-margliða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f` sé diffranlegt :math:`n` sinnum í
punkti :math:`a`, þ.e.a.s. við gerum ráð fyrir að :math:`n`-ta afleiðan
:math:`f^{(n)}(a)` sé skilgreind. *Taylor margliða* af :math:`n`-ta
stigi fyrir :math:`f` um :math:`x=a` (oft líka sagt með *miðju* í
:math:`a`) er margliðan

.. math::

   \begin{gathered}
       P_n(x)=f(a)+f'(a)(x-a)+\frac{f''(a)}{2}(x-a)^2+ \\
       \frac{f'''(a)}{3!}(x-a)^3+\cdots+\frac{f^{(n)}(a)}{n!}(x-a)^n.\end{gathered}

Talað er um :math:`n`-ta stigs Taylor-nálgun þegar gildið :math:`P_n(x)`
er notað sem nálgun fyrir :math:`f(x)`.

Skekkjan í nálguninni (munurinn á réttu fallgildi og nálgunargildi) er
táknaður með

.. math:: E_n(x)=f(x)-P_n(x).

Skekkjumat fyrir Taylor-margliður
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`n+1`-afleiðan :math:`f^{(n+1)}(t)` sé
skilgreind fyrir öll :math:`t` í opnu bili sem inniheldur bæði :math:`a`
og :math:`x`. Þá er til tala :math:`X` á milli :math:`a` og :math:`x`
þannig að

.. math:: E_n(x)=\frac{f^{(n+1)}(X)}{(n+1)!}(x-a)^{n+1}.

Því má rita

.. math::

   \begin{aligned}
   f(x)
   =&f(a)+f'(a)(x-a)+\frac{f''(a)}{2}(x-a)^2+ \\
    & \cdots+\frac{f^{(n)}(a)}{n!}(x-a)^n+E_n(x)\\
   =&f(a)+f'(a)(x-a)+\frac{f''(a)}{2}(x-a)^2+\\
    & \cdots+\frac{f^{(n)}(a)}{n!}(x-a)^n
     +\frac{f^{(n+1)}(X)}{(n+1)!}(x-a)^{n+1}.\end{aligned}

.. warning::
    Yfirleitt er engin leið til þess að finna :math:`X`. 
    Hins vegar getum við haft gagn af skekkjumatinu ef
    við höfum mat á :math:`f^{(n+1)}`.

Fylgisetning
~~~~~~~~~~~~

Gerum ráð fyrir að :math:`f` sé :math:`n+1` diffranlegt á bili sem
inniheldur bæði :math:`a` og :math:`x`. Gerum enn fremur ráð fyrir að
:math:`m` og :math:`M` séu tölur þannig að fyrir öll :math:`t` 
á milli `a` og `x`
gildi að :math:`m\leq f^{(n+1)}(t)\leq M`. Þá er

.. math::

   P_n(x) + \frac{m}{(n+1)!}(x-a)^{n+1} \leq f(x)
   \leq P_n(x) + \frac{M}{(n+1)!}(x-a)^{n+1}.

.. index::
    O-ritháttur
   
Ritháttur
~~~~~~~~~

Við ritum

.. math::

   f(x)=O(u(x)) \text{ þegar } x\rightarrow a

ef til er fasti :math:`K` og tala :math:`\delta>0` þannig að

.. math:: |f(x)|<K|u(x)|\quad\text{ fyrir öll}\quad x\in(a-\delta, a+\delta).

Einnig er ritað

.. math::

   f(x)=g(x)+O(u(x)) \text{ þegar }x\rightarrow a

ef :math:`f(x)-g(x)=O(u(x))` þegar :math:`x\rightarrow a`.

Tilgangur þessa ritháttar er að skilgreina tól sem getur sagt okkur 
hversu hratt :math:`f` stefnir á markgildið þegar :math:`x\to a`.

Athugasemd
~~~~~~~~~~

Við sjáum að

.. math:: f(x) = P_n(x) + O((x-a)^{n+1}) \text{ þegar } x\rightarrow a,

því hægt er að nota :math:`K = \frac{\max\{-m,M\}}{(n+1)!}` í skilgreiningunni
hér á undan.

Setning
~~~~~~~

Gerum ráð fyrir að :math:`Q_n(x)` sé margliða af stigi ekki hærra en
:math:`n`. Ef :math:`f(x)=Q_n(x)+O((x-a)^{n+1})` þegar
:math:`x\rightarrow a` þá er :math:`Q_n(x)=P_n(x)` þar sem
:math:`P_n(x)` er :math:`n`-ta stigs Taylor-margliða :math:`f` með miðju
í :math:`a`.

Með öðrum orðum, :math:`P_n` er sú margliða af stigi :math:`\leq n` sem 
nálgar :math:`f` best.

.. index::
    regla l’Hôpital

------

Regla de l’Hôpital
------------------

Regla de l’Hôpital, einhliða útgáfa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að föllin :math:`f` og :math:`g` séu diffranleg á opnu
bili :math:`(a,
b)` og að :math:`g'(x)\neq 0` fyrir öll :math:`x\in (a, b)`. Gerum enn
fremur ráð fyrir að

.. math::

   \lim_{x\rightarrow a^+}f(x)=0, \quad \lim_{x\rightarrow a^+}g(x)=0
   \quad\text{og}\quad \lim_{x\rightarrow a^+}\frac{f'(x)}{g'(x)}=L.

(Hér má :math:`L` vera rauntala, :math:`\infty` eða :math:`-\infty`.)

Þá er

.. math:: \lim_{x\rightarrow a^+}\frac{f(x)}{g(x)}=L.


Eins má skoða markgildi frá vinstri :math:`x\to a^-`.

.. begin-toggle::
    :label: Sýna sönnun

Þar sem :math:`\lim_{x\rightarrow a^+}f(x)=\lim_{x\rightarrow a^+}g(x)=0`
þá getum við gert ráð fyrir að :math:`f` og :math:`g` séu samfelld á
bilinu :math:`[a,b)` og taki gildið 0 í :math:`a`.

Þá fæst af alhæfðu meðalgildissetningunni fyrir sérhvert :math:`x\in (a,b)`
að til er :math:`c \in (a,x)` þannig að 

.. math::
    \frac{f(x)}{g(x)} = \frac{f(x)-f(a)}{g(x)-g(0)} = \frac{f'(c)}{g'(c)}

Þegar :math:`x \to a^+` þá gildir einnig að :math:`c \to a^+` því 
:math:`c` er klemmt á milli :math:`a` og :math:`x`. 
Þar sem markgildið 

.. math::
    \lim_{c\to a^+} \frac{f'(c)}{g'(x)} = L

er til, þá er markgildið :math:`\lim_{x\rightarrow a^+}\frac{f(x)}{g(x)}`
einnig til og er jafnt og :math:`L`.

.. end-toggle::

Regla de l’Hôpital
~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að föllin :math:`f` og :math:`g` séu diffranleg á bilum
:math:`(x_1, a)` og :math:`(a, x_2)` og að :math:`g'(x)\neq 0` fyrir öll
:math:`x` í þessum bilum.
Gerum enn fremur ráð fyrir að

.. math::

   \lim_{x\rightarrow a}f(x)=0, \quad \lim_{x\rightarrow a}g(x)=0
   \quad\text{og}\quad \lim_{x\rightarrow a}\frac{f'(x)}{g'(x)}=L.

(Hér má :math:`L` vera rauntala, :math:`\infty` eða :math:`-\infty`.)

Þá er

.. math:: \lim_{x\rightarrow a}\frac{f(x)}{g(x)}=L.

Dæmi
~~~~

Við höfum áður séð að :math:`\lim_{x\to 0} \sin(x)/x = 1`. 
Skoðum hvernig hægt er að sýna þetta með lítilli fyrirhöfn og reglu de l’Hôpital.

Sjáum að :math:`f(x) = \sin(x)` og :math:`g(x)` eru diffranleg í grennd um 0
og að :math:`g'(x) = 1 \neq 0`. Þá fæst að 

.. math::
    \lim_{x \to 0} \frac{\sin(x)}{x} = \lim_{x \to 0} \frac{\cos(x)}{1} = 1.

Regla de l’Hôpital, :math:`\infty`-útgáfa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að föllin :math:`f` og :math:`g` séu diffranleg á bilum
:math:`(x_1, \infty)` og að :math:`g'(x)\neq 0` fyrir öll
:math:`x\in (x_1, \infty)`. Gerum enn fremur ráð fyrir að

.. math::

   \lim_{x\rightarrow \infty}f(x)=0, \quad \lim_{x\rightarrow \infty}g(x)=0
   \quad\text{og}\quad \lim_{x\rightarrow \infty}\frac{f'(x)}{g'(x)}=L.

(Hér má :math:`L` vera rauntala, :math:`\infty` eða :math:`-\infty`.)

Þá er

.. math:: \lim_{x\rightarrow \infty}\frac{f(x)}{g(x)}=L.

Regla de l’Hôpital, tvíhliða útgáfa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að föllin :math:`f` og :math:`g` séu diffranleg á bilum
:math:`(x_1, a)` og :math:`(a, x_2)` og að :math:`g'(x)\neq 0` fyrir öll
:math:`x` í þessum bilum. Gerum enn fremur ráð fyrir að

.. math::

   \lim_{x\rightarrow a}g(x)=\pm\infty
   \quad\text{og}\quad \lim_{x\rightarrow a}\frac{f'(x)}{g'(x)}=L.

(Hér má :math:`L` vera rauntala, :math:`\infty` eða :math:`-\infty`.)

Þá er

.. math:: \lim_{x\rightarrow a}\frac{f(x)}{g(x)}=L.
