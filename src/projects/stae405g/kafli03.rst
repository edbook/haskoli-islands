Brúun
=====

*Over the centuries, mankind has tried many ways of combating the forces of evil... 
prayer, fasting, good works and so on. Up until Doom, no one seemed to have thought 
about the double-barrel shotgun. Eat leaden death, demon.*
-- Terry Pratchett

Inngangur
---------

.. index::
	brúun
	brúunarmargliða
	brúunarpunktur

Markmiðið
~~~~~~~~~

Viðfangsefni þessa kafla er að finna ferla sem ganga gegnum fyrirfram
gefna *brúunarpunkta* :math:`(x_0,y_0),\dots,(x_m,y_m)` í planinu eða liggja nálægt
punktunum í einhverjum skilningi.

Fyrst viljum við finna graf margliðu :math:`p` sem fer gegnum punktana.
Þá þurfum við að gefa okkur að :math:`x_i\neq x_j` ef :math:`i\neq j`.

Við sýnum fram á að það sé alltaf hægt að finna margliðu :math:`p` af
stigi :math:`\leq m` sem uppfyllir :math:`p(x_i)=y_i` í öllum punktum og
að slík margliða sé ótvírætt ákvörðuð.

Hún nefnist *brúunarmargliða* fyrir punktana
:math:`(x_0,y_0),\dots,(x_m,y_m)`.

Við alhæfum þetta verkefni með því að úthluta sérhverjum punkti jákvæðri
heiltölu :math:`m_i` og krefjast þess graf margliðunnar fari í gegnum
alla punktana og til viðbótar að allar afleiður :math:`p^{(j)}` upp að
stigi :math:`m_i-1` taki einnig fyrirfram gefin gildi :math:`y^{(j)}_i`.

Brúun
~~~~~

Við tilraunir þá fáum við oft aðeins strjálar mælingar, t.d. ef við
mælum hljóðhraða við mismunandi hitastig. Hins vegar þá viljum við vita
hvert sambandið er fyrir öll möguleg hitastig. Brúunin er margliða og
hún skilgreind er fyrir allar rauntölur og \`\`brúar\`\` því gildin
milli mælipunktanna.

.. index::
	setning Weierstrass

Afhverju margliður?
~~~~~~~~~~~~~~~~~~~

-  Einfalt að meta fallgildin fyrir margliður (`Reiknirit Horners`_).

-  Einfalt að diffra og heilda margliður.

-  Margliður eru óendanlega oft diffranlegar.

-  *Setning Weierstrass:* Látum :math:`f` vera samfellt fall á bili
   :math:`[a,b]`. Fyrir sérhvert :math:`{\varepsilon}> 0` þá er til
   margliða :math:`p` þannig að

   .. math:: \|f-p\|_\infty := \max_{x\in [a,b]} |f(x)-p(x)| < {\varepsilon}.

.. note::
	Setning Weierstrass segir að margliður nægja til að nálga samfelld föll.
	Það er sama hvað samfellda fall við skoðum það er alltaf til margliða
	sem nálgar það eins vel og við viljum á lokuðu bili. 

.. index::
	margliður
	margliður; stig

Margliður
~~~~~~~~~

Fall :math:`p` af gerðinni

.. math:: p(x) = a_0 + a_1 x + \ldots + a_m x^m

þar sem :math:`m` er heiltala og :math:`a_0, \ldots, a_m` eru tvinntölur
nefnist margliða.

Stærsta talan :math:`j` þannig að :math:`a_j \not= 0` nefnist *stig
margliðunnar* :math:`p`.

Ef allir stuðlarnir eru 0 þá nefnist :math:`p` *núllmargliðan* og við
segjum að stig hennar sé :math:`-\infty`.

Munum að stuðullinn :math:`a_j` við veldið :math:`x^j` er gefinn með
formúlunni

.. math:: a_j = \frac{p^{(j)}(0)}{j!}, \quad j = 0,1,2,\ldots,m.

.. index::
	margliður; staðalform

Mismunandi leiðir á framsetningu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hægt er að setja sömu margliðuna fram á marga mismunandi vegu, en við
nefnum framsetninguna hér að framan *staðalform margliðunnar* :math:`p`.

Ef við veljum okkur einhvern punkt :math:`x_0 \in {{\mathbb  R}}`, þá
getum við skrifað

.. math:: p(x) = b_0 + b_1(x-x_0) + \ldots + b_m(x-x_0)^m

og stuðlarnir :math:`b_j` eru gefnir með

.. math:: b_j = \frac{p^{(j)}(x_0)}{j!}, \quad j = 0,1,2,\ldots,m.

Þessi formúla er jafngild þeirri staðreynd að ef :math:`p` er margliða
af stigi :math:`m`. Þá er Taylor-röð :math:`p` í sérhverjum punkti
:math:`x_0 \in {{\mathbb  R}}` bara margliðan :math:`p`, og stuðlarnir í
Taylor-röðinni eru gefnir með formúlunum fyrir :math:`b_j` að ofan.

.. index::
	margliður; Newton-form

Newton-form margliðu
~~~~~~~~~~~~~~~~~~~~

Ef við veljum okkur :math:`m` punkta :math:`x_0, \ldots, x_{m-1}` þá
nefnist framsetning af gerðinni

.. math::

   p(x) = c_0 + c_1(x-x_0) + c_2(x-x_0)(x-x_1)
       + \ldots + c_m(x-x_0)\cdots(x-x_{m-1})

*Newton-form* margliðunnar :math:`p` miðað við punktana
:math:`x_0, \ldots,
x_{m-1}`.

.. index::
	reiknirit Horners

Reiknirit Horners
~~~~~~~~~~~~~~~~~

Við munum mikið fást við margliður á Newton-formi og því er nauðsynlegt
að hafa hraðvirkt reiknirit til þess að reikna út fallgildi :math:`p` út
frá þessari framsetningu.

Eitt slíkt reiknirit er nefnt *reiknirit Horners*. Það byggir á því að
nýta sér að þættirnir :math:`(x-x_j)` eru endurteknir í liðunum

.. math::

   (x-x_0), \quad (x-x_0)(x-x_1), 
       \quad (x-x_0)(x-x_1)(x-x_2), \quad \ldots

Þar sem við sleppum við að hefja í veldi þá komumst við af með fáar
reikniaðgerðir hér.

Ef :math:`m = 2` má skrifa Newton-form :math:`p` sem

.. math:: p(x) = c_0 + (x-x_0)(c_1 + (x-x_1) \cdot c_2).

Ef :math:`m = 3` er það

.. math:: p(x) = c_0 + (x-x_0)(c_1 + (x-x_1)(c_2 + (x-x_2)c_3))

og ef :math:`m = 4` er það

.. math::

   p(x) = c_0 + (x-x_0)(c_1 + (x-x_1)(c_2 + (x-x_2)
       (c_3 + c_4(x-x_3)))).

Reikniritið vinnur á þessari stæðu með því að margfalda upp úr svigunum
frá hægri til vinstri.

Skilgreinum tölur :math:`b_0`, :math:`b_1`, :math:`\ldots` á
eftirfarandi hátt. Fyrst setjum við

.. math:: b_n = c_n.

Fyrir hvert :math:`k` frá :math:`n-1` niður í 0 þá setjum við

.. math:: b_k = c_k + (a - x_k) b_{k+1}.

Þá er :math:`b_0 = p(a)`.

.. math::

   p(a) = 
       \underbrace{
         c_0 + (a-x_0)(
         \underbrace{
           c_1 + (a-x_1)(
             \underbrace{c_2 + (a-x_2)(
           \underbrace{c_3 + (a-x_3)
             \underbrace{c_4}_{b_4}
             }_{b_3})
           }_{b_2})
         }_{b_1})
       }_{b_0}.


.. index::
	brúun; brúunarmargliða
	brúun; brúunarverkefni

Margliðubrúun: Lagrange-form
----------------------------

Margliðubrúun
~~~~~~~~~~~~~

Látum nú :math:`(x_0,y_0), \ldots, (x_m,y_m)` vera gefna punkta í plani.
Við höfum áhuga á að finna margliðu :math:`p` af lægsta mögulega stigi
þannig að

.. math:: p(x_k) = y_k, \quad k = 0, \ldots, m.

Slík margliða nefnist *brúunarmargliða* fyrir punktana
:math:`(x_0,y_0), \ldots, (x_m,y_m)`

eða *brúunarmargliða gegnum punktana*
:math:`(x_0,y_0), \ldots, (x_m,y_m)`.

Augljóslega verðum við að gera ráð fyrir að :math:`x`-hnitin séu ólík,
það er :math:`x_j \not= x_k` ef :math:`j \not= k`.

Verkefnið að finna margliðuna :math:`p` nefnist *brúunarverkefni fyrir
punktana* :math:`(x_0,y_0), \ldots, (x_m,y_m)`.

Setning: Brúunarmargliðan er ótvírætt ákvörðuð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Brúunarmargliðan af stigi :math:`\leq m` fyrir :math:`(x_0,y_0),\ldots,(x_m,y_m)` er
ótvírætt ákvörðuð. 

.. begin-toggle::
	:label: Sönnun 

Ef :math:`p(x)` og :math:`q(x)` eru tvær
brúunarmargliður af stigi :math:`\leq m` fyrir punktana
:math:`(x_0,y_0), \ldots, (x_m,y_m)` þá er mismunurinn
:math:`r(x) = p(x) - q(x)` margliða af stigi :math:`\leq m` með
núllstöðvar :math:`x_0, \ldots, x_m`. Þetta eru :math:`m+1` ólíkir
punktar og því er :math:`r(x)` núllmargliðan samkvæmt 
`undirstöðusetningu algebrunnar <http://www.stae.is/fletta/undirst%C3%B6%C3%B0usetning/algebrunnar>`_. 
Þar með er :math:`p(x) - q(x)` núllmargliðan, þ.e. \ :math:`p(x) = q(x)`.

.. end-toggle::

Setning: Brúunarmargliðan er til
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Til er margliða :math:`p` af stigi :math:`\leq m` þannig að

.. math:: p(x_0) = y_0, \quad \ldots \quad p(x_n)=y_n.

.. begin-toggle::
	:label: Sönnun

Við notum þrepun til að sýna fram á tilvistina.

Ef :math:`m = 0`, þá erum við aðeins með eitt brúunarskilyrði,
:math:`p(x_0) = y_0`, og fastamargliðan :math:`p(x) = y_0` er lausn af
stigi :math:`\leq 0`.

G.r.f. að við getum leyst öll brúunarverkefni þar sem fjöldi punkta er
:math:`m` og sýnum að við getum þá leyst verkefnið fyrir :math:`m+1`
punkt.

Látum :math:`q` vera brúunarmargliðuna af stigi :math:`\leq m-1` fyrir
punktana :math:`(x_0,y_0), \ldots,
(x_{m-1},y_{m-1})` og :math:`r` vera brúunarmargliðuna af stigi
:math:`\leq m-1` fyrir punktana :math:`(x_1,y_1), \ldots, (x_m,y_m)` og
setjum síðan

.. math:: p(x) = \frac{x-x_m}{x_0-x_m}q(x) + \frac{x-x_0}{x_m-x_0}r(x),

:math:`p(x)` er greinilega margliða af stigi :math:`\leq m`. Skoðum nú
gildin á :math:`p`

.. math::

   \begin{aligned}
     p(x_0) &= 1 \cdot q(x_0) + 0\cdot r(x_0) = y_0, \\
     p(x_k) &= \frac{x_k-x_m}{x_0-x_m}y_k 
     + \frac{x_k-x_0}{x_m-x_0}y_k = y_k,\qquad k = 1, \ldots, m-1,\\
     p(x_m) &= 0 \cdot q(x_m) + 1 \cdot r(x_m) = y_m.\end{aligned}

Þar með er :math:`p` brúunarmargliðan sem uppfyllir :math:`p(x_j)=y_j`
fyrir :math:`j=0,\dots,m` og við höfum leyst brúunarverkefnið fyrir
:math:`m+1` punkt.

.. end-toggle::

.. index::
	margliður; Lagrange-form

Lagrange-form brúunarmargliðunnar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sönnunin á undan er í raun rakningarformúla til þess að reikna út gildi
brúunarmargliðunnar :math:`p` fyrir punktana
:math:`(x_0,y_0),\dots,(x_m,y_m)`.

Hægt er að skrifa lausnina niður beint

.. math:: p(x)=y_0\ell_0(x)+y_1\ell_1(x)+\cdots+y_m\ell_m(x),

þar sem :math:`\ell_0,\dots,\ell_m` er ákveðinn grunnur fyrir rúm allra
margliða :math:`{\cal P}_m` af stigi :math:`\leq m` og nefnast
*Lagrange-margliður fyrir punktasafnið*
:math:`(x_0,y_0),\dots,(x_m,y_m)`.

Lagrange-margliður, tilfellin :math:`m=0,1,2`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :math:`m=0` Ef :math:`m = 0` þá er :math:`p(x) = y_0` fastamargliða
   eins og við höfum séð.

-  :math:`m=1` Ef :math:`m = 1`, þá blasir við að lausnin er

   .. math::

      p(x) = y_0 \frac{(x-x_1)}{(x_0-x_1)}
        + y_1 \frac{(x-x_0)}{(x_1-x_0)},

   sem er margliða af stigi :math:`\leq 1` (þ.e. lína) sem leysir
   brúunarverkefnið.

-  :math:`m=2` Á hliðstæðan hátt fáum við fyrir :math:`m = 2` að

   .. math::

      p(x) = y_0 \frac{(x-x_1)(x-x_2)}{(x_0-x_1)(x_0-x_2)}
        + y_1 \frac{(x-x_0)(x-x_2)}{(x_1-x_0)(x_1-x_2)}
        + y_2 \frac{(x-x_0)(x-x_1)}{(x_2-x_0)(x_2-x_1)}

   leysir brúunarverkefnið.

Lagrange-margliður almenna tilfellið
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Almennt fæst lausnin

.. math::

   \label{p}
     p(x) = y_0 \, \ell_{0}(x) + y_1 \, \ell_{1}(x) 
     + \ldots + y_m \, \ell_{m}(x)

þar sem

.. math::

   \ell_{k} = \prod\limits_{\stackrel{j=0}{j\not=k}}^m
     \frac{(x-x_j)}{(x_k-x_j)}

.. note::
	.. math::

	   \label{l}
	     \ell_{k}(x_i) = \left\{ \begin{array}{cc}
		 1 & \text{ef } i = k \\
		 0 & \text{ef } i \not= k
	     \end{array} \right.

Allar margliðurnar :math:`\ell_{k}` eru af stigi :math:`m` og því er
:math:`p` af stigi :math:`\leq m`. Nú er augljóst útfrá ([p]) og ([l])
að :math:`p` er lausn brúunarverkefnisins.

Sýnidæmi
~~~~~~~~

Finnið brúunarmargliðuna gegnum punktana :math:`(1,1)`, :math:`(2,3)`
og :math:`(3,6)` með því að nota Lagrange-margliður.

.. begin-toggle::
	:label: Lausn

Reiknum fyrst margliðurnar :math:`\ell_{0}`, :math:`\ell_{1}` og
:math:`\ell_{2}`:

.. math::

   \begin{aligned}
     \ell_{0} &= \frac{(x-2)(x-3)}{(1-2)(1-3)} 
     = \frac{(x-2)(x-3)}{2} \\
     \ell_{1} &= \frac{(x-1)(x-3)}{(2-1)(2-3)}
     = -(x-1)(x-3) \\
     \ell_{2} &= \frac{(x-1)(x-2)}{(3-1)(3-2)}
     = \frac{(x-1)(x-2)}{2}\end{aligned}

Þá fæst að brúunarmargliðan :math:`p` er

.. math::

   p(x) = 1 \cdot \frac{(x-2)(x-3)}{2}
     - 3 \cdot (x-1)(x-3)
     + 6 \cdot \frac{(x-1)(x-2)}{2}

Þetta er greinilega annars stigs margliða og auðvelt er að sannfæra sig
um að :math:`p(1) = 1`, :math:`p(2) = 3` og :math:`p(3) = 6`.

.. end-toggle::

.. index::
	brúun; Newton-form

Margliðubrúun: Newton-form
--------------------------

Formúla fyrir :math:`c_0, \ldots, c_m`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú ætlum við að leiða út formúlu fyrir stuðlunum
:math:`c_0, \ldots, c_m` í Newton-formi brúunarmargliðunnar :math:`p`
miðað við röð brúunarpunktanna :math:`x_0, \ldots, x_{m-1}`.

Athugum að :math:`c_m = a_m`, þar sem :math:`a_m` er stuðullinn við
veldið :math:`x^m` í staðalframsetningunni á :math:`p`.

Til þess að reikna út :math:`c_0, \ldots, c_m` þurfum við að reikna út
með skipulegum hætti stuðulinn við veldið :math:`x^j` í
brúunarmargliðunni gegnum punktana
:math:`(x_i,y_i), \ldots, (x_{i+j},y_{i+j})`, fyrir öll
:math:`i = 0, \ldots, m` og :math:`j = 0, \ldots, m-i`. Við táknum
þennan stuðul með :math:`y[x_i, \ldots, x_{i+j}]`. 

.. warning::
	Verkefnið er háð röð punktanna, þ.e. framsetningin (Newton-formið) á
	margliðunni breytist eftir röð punktanna. 
	En auðvitað er margliðan og gildin á henni alltaf þau sömu
	
	*Dæmi:* Skoðum margliðuna :math:`p(x) = 2-7x+5x^2`.
	
	Ef :math:`x_0=0` og :math:`x_1=2` þá er Newton-form hennar
	
	.. math::
		p(x) = 3 + 3(x-0) + 5(x-0)(x-2).
		
	En ef :math:`x_0=2` og :math:`x_1=0` þá er Newton-form hennar
	
	.. math:: 
		p(x) = 8 + 3(x-2) + 5(x-2)(x-0).
	
.. index::
	mismunakvóti

Mismunakvótar
~~~~~~~~~~~~~

Skilgreinum mismunakvóta :math:`y[x_i,\ldots,x_{i+j}]` fyrir
punktasafnið :math:`(x_i,y_i),\ldots,(x_{i+j},y_{i+j})` á eftirfarandi
hátt:

-  :math:`j=0`: :math:`y[x_i] = y_i`.

-  :math:`j=1`: :math:`y[x_i,x_{i+1}] = \frac{y_{i+1}-y_i}{x_{i+1}-x_i}`

-  :math:`j=2`:
   :math:`y[x_i,x_{i+1},x_{i+2}] = \frac{y[x_{i+1},x_{i+2}] - y[x_i,x_{i+1}]}{x_{i+2}-x_i}`.

-  :math:`j>2`:
   :math:`y[x_i,\ldots,x_{i+j}] = \frac{y[x_{i+1},\ldots,x_{i+j}] - y[x_i,\ldots,x_{i+j-1}]}{x_{i+j}-x_i}`.

.. note::
	Stærðin :math:`y[x_{n-1},x_n]` hefur komið fyrir áður
	hjá okkur þegar við fjölluðum um `Sniðilsaðferð`, enda er sniðill 
	ekkert annað en brúunarmargliða fyrir tvö punkta í planinu.

Upprifjun á tilvistarsönnuninni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Þrepunarskrefið í `tilvistarsönnuninni <Setning: Brúunarmargliðan er til>`_
fyrir brúunarmargliður gefur okkur nú hvernig mismunakvótarnir nýtast okkur.

Látum :math:`q` vera brúunarmargliðuna af stigi :math:`\leq m-1` fyrir
punktana :math:`(x_0,y_0), \ldots,
(x_{m-1},y_{m-1})` og :math:`r` vera brúunarmargliðuna af stigi
:math:`\leq m-1` fyrir punktana :math:`(x_1,y_1), \ldots, (x_m,y_m)` og
setjum síðan

.. math:: p(x) = \frac{x-x_m}{x_0-x_m}q(x) + \frac{x-x_0}{x_m-x_0}r(x)

Gerum nú ráð fyrir að stuðullinn við veldið :math:`x^{m-1}` í
:math:`q(x)` sé :math:`y[x_0, \ldots, x_{m-1}]` og stuðullinn við veldið
:math:`x^{m-1}` í :math:`r(x)` sé :math:`y[x_1, \ldots, x_m]`.

Við sjáum þá að stuðullinn við veldið :math:`x^m` í :math:`p(x)` er

.. math::

   \frac{y[x_0, \ldots, x_{m-1}]}{x_0-x_m} + 
     \frac{y[x_1, \ldots, x_m]}{x_m - x_0}
     = y[x_0, \ldots, x_m]

.. note::
	Fyrir :math:`m=0` gildir að :math:`p(x) = y_0 = y[x_0]`.

.. index::
	brúun; mismunakvótatafla

Mismunakvótatöflur fyrir :math:`m=0,1,2,3`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mismunakvótar eru venjulega reiknaðir út í svokölluðum
*mismunakvótatöflum*.

.. begin-toggle::
	:label: Ef m=0

Ef :math:`m = 0` er mismunakvótataflan aðeins ein lína

.. math::

   \begin{array}{c|c|c}
       i & x_i & y[x_i] \\
       \hline
       0 & x_0 & y[x_0] = y_0
     \end{array}

.. end-toggle::

.. begin-toggle::
	:label: Ef m=1

Ef :math:`m = 1` er taflan

.. math::

   \begin{array}{c|c|cc}
       i & x_i & y[x_i] & y[x_i,x_{i+1}] \\
       \hline
       0 & x_0 & y[x_0] = y_0 & y[x_0,x_1] \\
       1 & x_1 & y[x_1] = y_1 & 
     \end{array}

og margliðan er

.. math:: p(x) = y[x_0] + y[x_0,x_1](x-x_0).

.. end-toggle::

.. begin-toggle::
	:label: Ef m=2

Ef :math:`m = 2` verður taflan

.. math::

   \begin{array}{c|c|ccc}
       i & x_i & y[x_i] & y[x_i,x_{i+1}] & y[x_i,x_{i+1},x_{i+2}] \\
       \hline
       0 & x_0 & y[x_0] = y_0 & y[x_0,x_1] & y[x_0,x_1,x_2] \\
       1 & x_1 & y[x_1] = y_1 & y[x_1,x_2] & \\
       2 & x_2 & y[x_2] = y_2 &  & 
     \end{array}

og margliðan er

.. math::

   p(x) = y[x_0] + y[x_0,x_1](x-x_0) 
     + y[x_0,x_1,x_2](x-x_0)(x-x_1).

.. end-toggle::

.. begin-toggle::
	:label: Ef m=3


Skoðum loks tilfellið :math:`m = 3`

.. math::

   \begin{array}{c|c|cccc}
       i & x_i & y[x_i] & y[x_i,x_{i+1}] & y[x_i,x_{i+1},x_{i+2}]
       & y[x_i,x_{i+1},x_{i+2},x_{i+3}] \\
       \hline
       0 & x_0 & y[x_0] = y_0 & y[x_0,x_1] & y[x_0,x_1,x_2]
       & y[x_0,x_1,x_2,x_3] \\
       1 & x_1 & y[x_1] = y_1 & y[x_1,x_2] & y[x_1,x_2,x_3] & \\
       2 & x_2 & y[x_2] = y_2 & y[x_2,x_3] & & \\
       3 & x_3 & y[x_3] = y_3 & & &
     \end{array}

Brúunarmargliðan fæst svo með því að nota stuðlana úr fyrstu línu
töflunnar:

.. math::

   \begin{aligned}
     p(x) = &y[x_0] + y[x_0,x_1](x-x_0) 
     + y[x_0,x_1,x_2](x-x_0)(x-x_1) \\ 
     &+ y[x_0,x_1,x_2,x_3](x-x_0)(x-x_1)(x-x_2)\end{aligned}

.. end-toggle::

Sýnidæmi
~~~~~~~~

Við skulum reikna út aftur brúunarmargliðuna gegnum :math:`(1,1)`,
:math:`(2,3)` og :math:`(3,6)`. 

.. begin-toggle::
	:label: Lausn

Stillum fyrst upp mismunakvótatöflu

.. math::

   \begin{array}{cc||ccc}
       i & x_i & y[x_i] & y[x_i,x_{i+1}] & y[x_i,x_{i+1},x_{i+2}] \\
       \hline
       0 & 1   &  1     &    &   \\
       1 & 2   &  3     &    &   \\
       2 & 3   &  6     &    &   
     \end{array}

Fyllum svo út í hana með að ganga á hvern dálk á fætur öðrum

.. math::

   \begin{array}{cc||ccc}
       i & x_i & y[x_i] & y[x_i,x_{i+1}] & y[x_i,x_{i+1},x_{i+2}] \\
       \hline
       0 & 1 & 1 & \dfrac{3-1}{2-1} = 2 & \dfrac{3-2}{3-1} = 1/2  \\
       1 & 2 & 3 & \dfrac{6-3}{3-2} = 3 & \\
       2 & 3 & 6 & &   
     \end{array}

Lesum út brúunarmargliðuna :math:`p` með að ganga á efstu línuna:

.. math:: p(x) = 1 + 2 \cdot (x-1) + \frac{1}{2} \cdot (x-1)(x-2).

Reiknum út brúunarmargliðuna gegnum :math:`(3,1)`, :math:`(1,-3)`,
:math:`(5,2)` og :math:`(6,4)`. Stillum upp og fyllum út í
mismunakvótatöflu:

.. math::

   \begin{array}{cc||cccc}
       i & x_i & y[x_i], & y[x_i,x_{i+1}], &
       y[x_i,x_{i+1},x_{i+2}], & y[x_i,\ldots,x_{i+3}] \\
       \hline
       1 & 3 & 1 & \frac{-3-1}{1-3} = 2 & \frac{5/4-2}{5-3} = -3/8 &
       \frac{3/20-(-3/8)}{6-3} = 7/40 \\
       2 & 1 & -3 & \frac{2-(-3)}{5-1} = 5/4 &
       \frac{2-5/4}{6-1} = 3/20 & \\
       3 & 5 & 2 & \frac{4-2}{6-5} = 2 & & \\
       4 & 6 & 4 & & &
     \end{array}

Nú getum við lesið brúunarmargliðuna okkar úr töflunni með að ganga á
efstu línuna, við fáum

.. math::

   p(x) = 1 + 2(x-3) - \frac 38 (x-3)(x-1)
     + \frac 7{40} (x-3)(x-1)(x-5)

.. end-toggle::

.. todo::
	Umraða

Samantekt
~~~~~~~~~

Ef gefnir eru punktar :math:`(x_0,y_0), \ldots, (x_m,y_m)` í
:math:`{{\mathbb  R}}^2`, þar sem :math:`x_i\neq x_j` ef
:math:`i\neq j`, þá er til nákvæmlega ein margliða :math:`p` af stigi
:math:`\leq m` þannig að

.. math:: p(x_k) = y_k, \quad k = 0, \ldots, m

Newton-form margliðunnar :math:`p` með tilliti til punktanna
:math:`x_0,\dots,x_{m-1}` er

.. math:: p(x)=y[x_0]+y[x_0,x_1](x-x_0)+\cdots+y[x_0,\dots,x_m](x-x_0)\cdots(x-x_m)

þar sem mismunakvótarnir eru reiknaðir með rakningarformúlunum
:math:`y[x_i]=y_i` og

.. math::

   y[x_i,\ldots,x_{i+j}]
     = \frac{y[x_{i+1},\ldots,x_{i+j}] - y[x_i,\ldots,x_{i+j-1}]}
     {x_{i+j} - x_i}, \qquad i=0,\dots,m, \quad j=0,\dots,m-i.

Samantekt – Newton-form
~~~~~~~~~~~~~~~~~~~~~~~

Venja er að setja mismunakvótana upp í töflu og stuðlarnir í
Newton-forminu raða sér í fyrstu línu töflunnar:

.. math::

   \begin{array}{c|c|cccccc}
       i & x_i & y[x_i] & y[x_i,x_{i+1}] & y[x_i,x_{i+1},x_{i+2}]
       & y[x_i,\dots,x_{i+3}] &y[x_i,\dots,x_{i+4}] &\dots  \\
       \hline
       0 & x_0 & y[x_0] = y_0 & y[x_0,x_1] & y[x_0,x_1,x_2]
       & y[x_0,x_1,x_2,x_3]&y[x_0,x_1,x_2,x_3,x_4]& \dots \\
       1 & x_1 & y[x_1] = y_1 & y[x_1,x_2] & y[x_1,x_2,x_3] &
       y[x_1,x_2,x_3,x_4]&\dots \\
       2 & x_2 & y[x_2] = y_2 & y[x_2,x_3] &y[x_2,x_3,x_4]&\dots & \\
       3 & x_3 & y[x_3] = y_3 & y[x_3,x_4] &\dots & & \\
       4 & x_4 & y[x_4] = y_4 & \dots &  \\
   \vdots & \vdots &\vdots
     \end{array}

Samantekt – Lagrange-margliður
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lagrange-form brúunarmargliðunnar er

.. math:: p(x)=\sum_{k=0}^m y_k\ell_{k}(x)

þar sem :math:`\ell_{k}` eru Lagrange-margliðurnar með tilliti til
punktanna :math:`x_0,\dots,x_m`,

.. math::

   \ell_{k}(x) = \prod_
       {\substack{j=0\\ j\neq k}}^m\dfrac{(x-x_j)}{(x_k-x_j)}
       = \dfrac{(x-x_0)\cdots(x-x_{k-1})
           (x-x_{k+1})\cdots(x-x_m)}
       {(x_k-x_0)\cdots(x_k-x_{k-1})
           (x_k-x_{k+1})\cdots(x_k-x_m)}.

 En þær uppfylla

.. math::

   \ell_{k}(x_i) = \left\{ \begin{array}{cc}
         1 & \text{ef } i = k \\
         0 & \text{ef } i \not= k
     \end{array} \right.

Samantekt
-------------

Lagrange-margliður
~~~~~~~~~~~~~~~~~~

-  Auðvelt að finna margliðuna

-  Dýrara að reikna fallgildin

Newton-margliður
~~~~~~~~~~~~~~~~

-  Erfiðara að finna margliðuna

-  Auðvelt að finna fallgildin (reiknirit Horners)

.. index::
    brúun; margfaldir punktar

Margliðubrúun: Margfaldir punktar
---------------------------------

Látum :math:`a_1, \ldots, a_k` vera ólíka punkta í
:math:`{{\mathbb  R}}`, :math:`m_1, \ldots, m_k` vera jákvæðar heiltölur
og hugsum okkur að gefnar séu rauntölur

.. math:: y_i^{(j)}, \quad j = 0, \ldots, m_i-1, \quad i = 1, \ldots, k.

Við viljum finna margliðu :math:`p` af lægsta mögulega stigi þannig að
margliðan :math:`p=p^{(0)}` og afleiður hennar :math:`p^{(j)}` uppfylli

.. math::

   p^{(j)}(a_i) = y_i^{(j)}, 
     \quad j = 0, \ldots, m_i-1, \quad i = 1, \ldots, k

Við nefnum verkefnið að finna slíka margliðu :math:`p` *alhæft
brúunarverkefni*, og margliða sem uppfyllir þessi skilyrði nefnist
*brúunarmargliða fyrir brúunarverkefnið* sem lýst er með gefnu
skilyrðunum.

.. index::
    brúunarpunktur; einfaldur
    brúunarpunktur; tvöfaldur
    brúunarpunktur; stig

Margfeldni punktanna
~~~~~~~~~~~~~~~~~~~~

Við segjum að :math:`a_i` sé *einfaldur brúunarpunktur* ef
:math:`m_i=1`, *tvöfaldur brúunarpunktur* ef :math:`m_i=2` o.s.frv.

Við skilgreinum nú töluna

.. math:: m = m_1 + m_2 + \ldots + m_k - 1.

Brúunarmargliðan okkar :math:`p` á að vera af stigi :math:`\leq m`, og
fjöldi skilyrða sem við setjum á hana eru :math:`m+1`. 

.. note:: 
    Tilfellið :math:`k=m+1`, :math:`m_j=1` er það sem við skoðuðum hér á undan.

Sértilfelli
~~~~~~~~~~~

Tvö sértilfelli þekkjum við nú þegar.


#. *Allir punktar eins:* Ef allir punktarnir eru einfaldir, þá er
   alhæfða brúunarverkefnið sama verkefni og brúunarverkefnið sem við
   leystum í `Margliðubrúun: Lagrange-form`_ og `Margliðubrúun: Newton-form`_.

   .. math:: p^{(0)}(a_i) = p(a_i) = y_i^{(0)},

   og lausnin var leidd út með

   .. math::

      x_0=a_1,\dots,x_m=a_k \quad \text{ og } \quad
      y_0=y_1^{(0)},\dots,y_m=y_k^{(0)}.

#. *Einn punktur:* Ef aftur á móti :math:`k = 1`, þá er lausn gefin
   með Taylor-margliðunni af röð :math:`m` í punktinum :math:`a_1`

   .. math::

      p(x) = y_1^{(0)} + \frac{y'}{1!}(x - a_1) + \frac{y''}{2!}(x - a_1)^2 +  
        \ldots + \frac{y_1^{(m)}}{m!}(x - a_1)^m.

Upprifjun
~~~~~~~~~

Munum að ef :math:`p` er margliða og :math:`p(a)=0` þá er :math:`p`
deilanleg með :math:`(x-a)`. Það er, hægt er að skrifa

.. math:: p(x) = (x-a)q(x),

þar sem :math:`q` er margliða af stigi sem er einu lægra en stig
:math:`p` (sjá `Undirstöðusetning algebrunnar <http://m.xn--st-2ia.is/fletta/undirst%C3%B6%C3%B0usetning/algebrunnar?device=desktop>`_).

Ótvíræðni lausnarinnar
~~~~~~~~~~~~~~~~~~~~~~

Nú ætlum við að sýna fram á að til sé nákvæmlega ein margliða
:math:`p(x)` af stigi :math:`\leq m` sem uppfyllir

.. math::

   p^{(j)}(a_i) = y_i^{(j)}, 
     \quad j = 0, \ldots, m_i-1, \quad i = 1, \ldots, k

Byrjum á að sýna að það er í mesta lagi ein margliða sem uppfyllir þetta.
     
.. begin-toggle::
    :label: Sönnun á ótvíræðni
     
Gerum ráð fyrir að
:math:`p(x)` og :math:`q(x)` séu tvær margliður af stigi :math:`\leq m`
sem uppfylla öll þessi skilyrði.

Þá uppfyllir margliðan :math:`r(x) = p(x) - q(x)` að

.. math::

   r^{(j)}(a_i) = 0, \quad j = 0, \ldots, m_i-1,
     \quad i = 1, \ldots,k

Af þessu leiðir að :math:`r(x)` er deilanlegt með :math:`(x-a_i)^{m_i}`
en samanlagt stig þessara þátta er :math:`m_1 + \ldots + m_k = m + 1`.

Nú er stig :math:`r(x)` minna eða jafnt :math:`m` svo þetta getur aðeins
gerst ef :math:`r(x)` er núllmargliðan.

Við höfum því að :math:`p(x) = q(x)` og ályktum að við höfum nákvæmlega
eina lausn á brúunarverkefninu ef við getum sýnt fram á tilvist á lausn.

.. end-toggle::

Tilvist á lausn
~~~~~~~~~~~~~~~

Nú beitum við sams konar röksemdafærslu og í `byrjum kaflans <Setning: Brúunarmargliðan er til>`_ til þess að sýna
fram á tilvist á lausn, þ.e. við notum þrepun.

.. begin-toggle::
    :label: Sönnun á tilvist

**Smíðum margliðuna:**

Ef :math:`m = 0`, þá er lausnin fastamargliðan
:math:`p(x) = y_1^{(0)}=y_0`.

Gerum nú ráð fyrir að við getum fundið brúunarmargliðu af stigi
:math:`\leq m-1` fyrir sérhvert alhæft brúunarverkefni þar sem
samanlagður fjöldi skilyrðanna er :math:`m`.

Lítum nú aftur á upprunalega brúunarverkefnið þar sem fjöldi skilyrðanna
er :math:`m+1`. Skilgreinum tvær runur af punktum

.. math::

   (x_0,x_1,\ldots,x_m) = 
     (\underbrace{a_1, \ldots, a_1}_{m_1 \, \text{sinnum}}, 
     \underbrace{a_2, \ldots , a_2}_{m_2 \, \text{sinnum}}, 
     \ldots , 
     \underbrace{a_k, \ldots , a_k}_{m_k \, \text{sinnum}})

og

.. math::

   (y_0,y_1,\ldots,y_m) = 
     (y_1^{(0)}, \ldots, y_1^{(m_1-1)}, \ldots,
     y_k^{(0)}, \ldots, y_k^{(m_k-1)})

Við höfum séð að í því tilfelli að við höfum einn punkt, :math:`k=1`,
:math:`x_0 = x_1 = \ldots = x_m = a_1` er lausnin gefin með
Taylor-margliðu í :math:`a_1`.

Við megum því gera ráð fyrir punktarnir séu a.m.k. tveir,
:math:`k\geq 2`. Það gefur að :math:`x_0 \not= x_m`.

Látum :math:`q(x)` vera margliðuna af stigi :math:`\leq m-1` sem
uppfyllir sömu skilyrði og :math:`p`, nema það síðasta um að
:math:`q^{(m_k-1)}(a_k)` þurfi að vera :math:`y_k^{(m_k-1)}` .

og látum :math:`r(x)` vera margliðuna sem uppfyllir öll
brúunarskilyrðin, nema síðasta skilyrðið í fyrsta punkti um að
:math:`r^{(m_1-1)}(a_1)` sé jafnt :math:`y_1^{(m_1-1)}`.

Setjum síðan

.. math::

   p(x) = \frac{x-x_m}{x_0-x_m}q(x) 
     + \frac{x-x_0}{x_m-x_0}r(x)
     = \frac{x-a_k}{a_1-a_k}q(x)
     + \frac{x-a_1}{a_k-a_1}r(x)


**Sýnum að gefin fallgildi eru tekin**

Nú þurfum við að staðfesta að öll skilyrðin séu uppfyllt.

Við byrjum á því að taka :math:`j=0` sem svarar til þess að :math:`p`
taki fyrirfram gefin fallgildi,

.. math::

   \begin{aligned}
     p(a_1) &= \frac{a_1-a_k}{a_1-a_k}q(a_1)
     + \frac{a_1-a_1}{a_k-a_1}r(a_1) = q(a_1) = y_1^{(0)}\\
     p(a_i) &= \frac{a_i-a_k}{a_1-a_k}q(a_i)
     + \frac{a_i-a_1}{a_k-a_1}r(a_i) 
     = \left( \frac{a_i-a_k}{a_1-a_k} 
       + \frac{a_i-a_1}{a_k-a_1} \right) y_i^{(0)} \\
       &= y_i^{(0)},  \qquad \text{fyrir } i=2,\ldots,k-1,\\
     p(a_k) &= \frac{a_k-a_k}{a_1-a_k}q(a_k)
     + \frac{a_k-a_1}{a_k-a_1}r(a_k) = r(a_k) = y_k^{(0)}.\end{aligned}


Sýnum svo að gildin á afleiðum :math:`p` séu rétt.

Rifjum upp margliðuna :math:`p`:

.. math::

   p(x) = \frac{x-x_m}{x_0-x_m}q(x) 
     + \frac{x-x_0}{x_m-x_0}r(x)
     = \frac{x-a_k}{a_1-a_k}q(x)
     + \frac{x-a_1}{a_k-a_1}r(x)

Afleiður hennar eru

.. math::

   p^{(j)}(x) = \frac{(x-a_k)}{(a_1-a_k)}q^{(j)}(x)
     + \frac{(x-a_1)}{(a_k-a_1)}r^{(j)}(x)
     + j \frac{\left( q^{(j-1)}(x)-r^{(j-1)}(x)\right)}{a_k-a_1}

Ef nú :math:`m_i > 1` þá er :math:`q^{(j-1)}(a_i) = y^{(j-1)}(a_i) =
r^{(j-1)}(a_i)` fyrir :math:`j = 1, \ldots, m_i-1` og því kemur alltaf
:math:`0` út úr síðasta liðnum ef við setjum inn :math:`x = a_i`, fyrir
öll :math:`i = 1, \ldots, k`.

Af þessu sést að afleiður :math:`p` uppfylla skilyrðin

.. math::

   p^{(j)}(a_i) = y^{(j)}_i, \qquad \text{fyrir } j=0,\ldots,m_i-1, 
     \quad i=1,\ldots,k.

.. end-toggle::

Samantekt
~~~~~~~~~

Við höfum því sannað eftirfarandi:

Ef gefnar eru

-  rauntölur :math:`a_1,\dots,a_k`, með :math:`a_j\neq a_k` ef
   :math:`j\neq k`,

-  jákvæðar heiltölur :math:`m_1,\dots,m_k`,

-  rauntölur :math:`y_i^{(j)}`, fyrir :math:`j=0,\dots, m_i-1`,
   :math:`i=1,\dots,k`,

og talan :math:`m` er skilgreind með :math:`m=m_1+\cdots+m_k-1`, þá er
til nákvæmlega ein margliða :math:`p` af stigi :math:`\leq m` þannig að

.. math:: p^{(j)}(a_i)=y_i^{(j)}, \qquad j=0,\dots, m_i-1, \quad i=1,\dots,k.

Brúunarmargliðan fundin
~~~~~~~~~~~~~~~~~~~~~~~

Ef skilgreindar eru runurnar

.. math:: (x_0,\dots,x_m)=(a_1,\dots,a_1,a_2,\dots,a_2,\dots,a_k,\dots,a_k)

þar sem :math:`a_1` kemur fyrir :math:`m_1` sinnum, :math:`a_2` kemur
fyrir :math:`m_2` sinnum o.s.frv., og

.. math::

   (y_0,\dots,y_m)=(y_1^{(0)},\cdot\cdot,y_1^{(m_1-1)},y_2^{(0)},\cdot\cdot,y_2^{(m_2-1)},
   \cdots,y_k^{(0)},\cdot\cdot,y_k^{(m_k-1)}),

þá er Newton-form margliðunnar :math:`p` með tilliti til punktanna
:math:`x_0,\dots,x_{m-1}` gefið með

.. math:: p(x)=y[x_0]+y[x_0,x_1](x-x_0)+\cdots+y[x_0,\dots,x_m](x-x_0)\cdots(x-x_{m-1})

þar sem mismunakvótarnir :math:`y[x_i,\ldots,x_{i+j}]` eru reiknaðir með
rakningarformúlu þannig að :math:`y[x_i]=y_i` og

.. math::

   y[x_i,\ldots,x_{i+j}]
     = \begin{cases}\dfrac{y[x_{i+1},\ldots,x_{i+j}] - y[x_i,\ldots,x_{i+j-1}]}
     {x_{i+j} - x_i}, &\text{ ef } x_i\neq x_{i+j},\\
   \dfrac{y^{(j)}_i}{j!}, &\text{ ef } x_i=x_{i+j}.
   \end{cases}

Skynsamlegir skiptipunktar og Chebyshev margliður
-------------------------------------------------

Um val á brúunarpunktum
~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`(t_0,y_0),\dots,(t_n,y_n)` vera punkta í plani og gerum ráð
fyrir að :math:`a=t_0<t_1<\cdots<t_n=b`.

Við höfum nú lært að ákvarða margliðu :math:`p` af stigi :math:`\leq n`
sem tekur gildin :math:`y_i` í punktunum :math:`t_i`.

Ef punktarnir liggja á grafi fallsins :math:`f` og nota á margliðuna til
þess að nálga fallgildi :math:`f`, þá getur það verið ýmsum erfiðleikum
bundið þegar stig hennar stækkar. Til dæmis getur komið fram
óstöðugleiki í útreikningum þannig að örlítil frávik í :math:`x` geta
leitt til mikilla frávika í :math:`p(x)`, og þá hugsanlega í mikilli 
skekkju á :math:`f(x)-p(x)`.

Dæmi um óheppilega skiptipunkta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skoðum dæmi þar sem við brúum fallið :math:`f(x) = 1/(25x^2+1)` í 9
brúnarpunktum sem eru jafndreifðir á bilinu :math:`[-1,1]`.

.. image:: ./myndir/vond_bruun1.png

Hér sjáum við ,,þægilegt" fall þar sem brúunarmargliðan gefur afskaplega 
vonda nálgun. 

Val á brúunarpunktum
~~~~~~~~~~~~~~~~~~~~

Það er ekki sjálfgefið að við getum valið í hvaða brúunarpunkta við
notum, t.d. ef þeir ákvarðast af mælingum. Ef við hins vegar getum valið
þá óhindrað, þá vaknar sú spurning hvernig er best að gera það?

.. index::
    staðall; ℓ∞
    staðall; ℓ2
    

Skilgreining
~~~~~~~~~~~~

Fyrst þurfum við að útskýra betur hvað við eigum við með ,,best”. Við
munum bara notast við tvær leiðir hér til að mæla skekkjuna, en það er
:math:`\ell_\infty` og :math:`\ell_2` staðlarnir, fyrir samfellt fall
:math:`h` á bilinu :math:`[a,b]` þá eru þeir skilgreindir með

.. math:: \|h\|_\infty  = \max_{x\in[a,b]} |h(x)|,

og

.. math:: \|h\|_2 = \left( \int_a^b h(x)^2\, dx \right)^\frac 12

.. note::
    Það má líta þannig á þetta að :math:`\ell_\infty` staðallinn 
    mæli hámarksskekkju og :math:`\ell_2` mæli einhvers konar,,meðaltalsskekkju",
    þar sem meðaltalið er reiknað með heildi.

Verkefnið
~~~~~~~~~

Verkefnið er því eftirfarandi: Fyrir gefið fall :math:`f(x)` á bili
:math:`[a,b]` og fast :math:`n`, þá viljum við finna
:math:`x_0,\ldots,x_n` sem lágmarka annað hvort

.. math:: \|f-p\|_\infty \quad \text{ eða } \quad \|f-p\|_2.

Þar sem :math:`p` er brúunarmargliðan fyrir brúunarpunktana
:math:`(x_i,f(x_i))`.

Byrjum á að skoða :math:`\ell_\infty` tilvikið.

.. index::
    margliður; Chebyshev
    

Skilgreining: Chebyshev margliður
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fyrir náttúrlega tölu :math:`n` þá skilgreinum við
*Chebyshev margliðuna* :math:`T_n` á :math:`[-1,1]` með

.. math:: T_n(x) = \cos(n \arccos(x)).

Með því að setja inn :math:`n=0` og :math:`n=1` þá fæst að

.. math:: T_0(x) = 1 \quad \text{ og } \quad T_1(x) = x,

og með hornafallareglunum fæst að

.. math:: T_{n+1}(x) = 2xT_n(x) - T_{n-1}(x), n \geq 1.

Af jöfnunni hér á undan þá fæst með þrepun að

-  :math:`T_n(x)` er margliða af stigi :math:`n`.

-  Forystustuðull :math:`T_n` er :math:`2^{n-1}`.

-  :math:`T_n` er jafnstæð ef :math:`n` er slétt og oddstæð ef :math:`n`
   er oddatala.

Setning
~~~~~~~

Chebyshev margliðan :math:`T_n` hefur :math:`n` einfaldar
núllstöðvar á bilinu :math:`[-1,1]` og þær eru gefnar með

.. math:: x_j = \cos\left(\frac{2j+1}{2n}\pi\right),\qquad j=0,1,2,3,\ldots,n-1.

Auk þess eru útgildi :math:`T_n` á :math:`[-1,1]` staðsett í

.. math:: z_j = \cos\left( \frac{j\pi}{n}\right),\qquad j=0,1,2,\ldots,n,

og fallgildin þar uppfylla :math:`T_n(z_j) = (-1)^j`

.. index::
    margliður; staðlaðar

Staðlaðar Chebyshev margliður
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Margliða er kölluð *stöðluð* ef forystustuðull hennar er 1.

*Stöðluðu Chebyshev margliðurnar* :math:`\tilde T` eru skilgreindar á eftirfarandi hátt

.. math::

   \tilde T(x) = 
       \begin{cases} 
         T_0(x) & \text{ef } n = 0 \\
         2^{1-n}T_n(x)   & \text{ef } n\geq 1              \end{cases}

Fyrir sérhverja staðlaða margliðu :math:`q` af stigi
:math:`n` þá er

.. math:: \frac 1{2^{n-1}} = \max_{x\in [-1,1]} T_n(x) \leq \max_{x\in[-1,1]} |q(x)|.

Þ.e. af öllum stöðluðum margliðum þá eru stöðluðu Chebyshev margliðurnar
,,minnstar” á bilinu :math:`[-1,1]`.

Skynsamlegir skiptipunktar fyrir bilið :math:`[-1,1]`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við vitum að skekkjan í því að nálga fallið :math:`f` með
brúunarmargliðu :math:`p` með brúunarpunkta :math:`x_0,\ldots,x_n` er

.. math:: f(x)-p(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}\, (x-x_0)(x-x_1)\cdots (x-x_n),

þar sem :math:`\xi` er á minnsta bilinu sem inniheldur :math:`x` og
:math:`x_0,x_1,\ldots,x_n`. Ef við skoðum jöfnuna að ofan þá sjáum við
að þar sem :math:`n` og :math:`f` (og þar með :math:`f^{(n+1)}`) er fast
þá er stæðan :math:`(x-x_0)\cdots(x-x_n)` það eina sem við höfum
einhverja stjórn á.

Með því að nota Chebyshev margliðurnar þá getum við lágmarkað þennan
hluta skekkjunnar.

Athugið að :math:`(x-x_0)\cdots (x-x_n)` er stöðluð margliða af stigi
:math:`n+1`. Þannig að samkvæmt því sem kom fram hér að 
`ofan <Staðlaðar Chebyshev margliður>`_ þá lágmörkum við framlag hennar
til skekkjunnar með :math:`(x-x_0)\cdots (x-x_n) = \tilde T_{n+1}`,
þ.e. með því að velja

.. math:: x_i = \cos\left(\frac{2i+1}{2(n+1)}\pi\right), \qquad i=0,1,\ldots,n.

Hæsta gildi :math:`\tilde T_{n+1}` er :math:`\frac 1{2^n}`, sem þýðir að
við fáum skekkjumatið

.. math:: \|f(x)-p(x)\|_\infty \leq \frac{\|f^{(n+1)}\|_\infty}{2^n(n+1)!}.

Dæmi um óheppilega skiptipunkta skoðað aftur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skoðum aftur fallið :math:`f(x) = 1/(25x^2+1)`, en í stað þess að taka 9
jafndreifaða brúunarpunkta á bilinu :math:`[-1,1]`, þá skulum við nota
Chebyshev margliðurnar til að finna 9 punkta á bilinu.

.. image:: ./myndir/vond_bruun2.png

Skynsamlegir skiptipunktar fyrir bil :math:`[a,b]`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hér á undan miðaðist allt við að finna brúunarmargliðu fyrir fallið
:math:`f` á bilinu :math:`[-1,1]`. Ef við viljum skoða almennt bil
:math:`[a,b]` þá byrjum við á athuga að fallið
:math:`\eta:[-1,1]\to [a,b]`,

.. math:: \eta(t) = \frac{b-a}2 t + \frac{b+a}2

skilgreinir línulega vörpun (hliðrun og stríkkun) frá :math:`[-1,1]`
yfir á :math:`[a,b]`. Athugið að vörpunin sendir :math:`-1` í :math:`a`
og :math:`1` í :math:`b`.

Með því að taka rætur stöðluðu Chebyshev margliðunnar
:math:`\tilde T_{n+1}` og varpa þeim með :math:`\eta` yfir á bilið
:math:`[a,b]` þá fáum við þá punkta :math:`x_0,\ldots,x_n \in [a,b]` sem
lágmarka :math:`(x-x_0)\cdots (x-x_n)` á bilinu :math:`[a,b]`,\ 

.. math::

   x_i = \eta\left(\cos\left(\frac{2i+1}{2(n+1)}\pi\right)\right) 
       = \frac{b-a}2 \cos\left(\frac{2i+1}{2(n+1)}\pi\right) + \frac{b+a}2,

:math:`i=0,1,2,\ldots,n`.

Lágmörkun á skekkju með tilliti til :math:`\ell_2`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við skipta um staðal, þannig að í stað þess að lágmarka
:math:`\|f-p\|_\infty` þá skulum við reyna að lágmarka

.. math:: \|f-p\|_2 = \left(\int_a^b (f-p)^2\, dx\right)^{1/2}

Við vitum að skekkjan í því að nálga fallið :math:`f` með
brúunarmargliðu :math:`p` með brúunarpunkta :math:`x_0,\ldots,x_n` er

.. math:: f(x)-p(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}\, (x-x_0)(x-x_1)\cdots (x-x_n),

þar sem :math:`\xi` er á minnsta bilinu sem inniheldur :math:`x` og
:math:`x_0,x_1,\ldots,x_n`.

Eins og áður þá sjáum við að stæðan :math:`(x-x_0)\cdots(x-x_n)` það
eina sem við getum stjórnað með því að velja brúunarpunktana
:math:`x_j`.

.. index::
    margliður; Legendre

Skilgreining: Legendre margliðurnar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fyrir náttúrlega tölu :math:`n` þá skilgreinum við
*Legendre margliðurnar* svona

.. math::

   \begin{aligned}
      P_0(x) &= 1,\\
      P_1(x) &= x,\\
      P_n(x) &= \frac{2n-1}n x P_{n-1}(x) - \frac{n-1}n P_{n-2}(x).
     \end{aligned}

Af skilgreiningunni hér á undan þá sjáum við að

-  :math:`P_n(x)` er margliða af stigi :math:`n`.

-  Forystustuðull :math:`P_n` er
   :math:`\frac {2n-1}n \cdot \frac {2n-3}{n-2} \cdots \frac 32 \cdot 1`.

-  :math:`P_n` er jafnstæð ef :math:`n` er slétt og oddstæð ef :math:`n`
   er oddatala.

Setning
~~~~~~~

.. math::

   \int_{-1}^1 P_j(x) P_k(x)\, dx =
       \begin{cases}
        0, & \text{ef } j\neq k\\
        \frac{2}{2j+1}, & \text{ef } j=k.
       \end{cases}

Einnig gildir að ef :math:`q` er margliða af stigi minna en :math:`n` þá er

.. math:: \int_{-1}^1 q(x)P_n(x)\, dx = 0.

Þetta segir okkur að Legendre margliðurnar eru hornréttar (með tilliti
til innfeldisins sem heildið skilgreinir).

Setning
~~~~~~~

:math:`P_n` hefur :math:`n` ólíkar núllstöðvar sem liggja
allar á :math:`[-1,1]`.

Skilgreining: Staðlaðar Legendre margliður
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Eins og þegar við fengumst við Chebyshev margliðurnar þá skilgreinum við
*stöðluðu Legendre margliðurnar* :math:`\tilde P_n` með því að deila upp
í :math:`P_n` með forrystustuðlunum :math:`P_n`.

.. note::
    Setningarnar þrjár hér undan gilda um :math:`\tilde P` alveg eins og :math:`P`.

Setning: Lágmörkun með Legendre margliðunum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`p` er stöðluð margliða af stigi :math:`n+1` þá er
:math:`\|p\|_2\geq \|\tilde P_{n+1}\|_2`. 

.. begin-toggle::
    :label: Sönnun 

Skilgreinum
:math:`q = p-\tilde P_{n+1}`, sem þýðir að :math:`q` er margliða af
stigi minna en :math:`n+1`. Nú er

.. math::

   \begin{aligned}
      \|p\|_2^2 &= \|\tilde P_{n+1} + q\|_2^2 \\
      &= \int_{-1}^1 (\tilde P_{n+1}(x) + q(x))^2\, dx \\
      &= \int_{-1}^1 \tilde P_{n+1}(x)^2 + 2q(x)\tilde P_{n+1}(x) + q(x)^2\, dx\\
      &= \|\tilde P_{n+1}\|_2^2 + 2\int_{-1}^1 q(x)\tilde P_{n+1}(x)\, dx + \|q\|_2^2\\
      &= \|\tilde P_{n+1}\|_2^2 +  \|q\|_2^2 \geq \|\tilde P_{n+1}\|_2^2
     \end{aligned}

því :math:`\int_{-1}^1 q(x)\tilde P_{n+1}(x)\, dx=0` og
:math:`\|q\|_2 \geq 0`.

Af síðustu setningu sjáum við að til þess að lágmarka

.. math:: \|f(x)-p(x)\|_2 = \left\|\frac{f^{(n+1)}(\xi)}{(n+1)!}\, (x-x_0)(x-x_1)\cdots (x-x_n) \right\|_2,

þá veljum við :math:`x_1,\ldots,x_n` þannig að
:math:`(x-x_0)(x-x_1)\cdots (x-x_n) = \tilde P_{n+1}`.
Þ.e. \ :math:`x_j` þurfa að vera rætur stöðluðu Legendre margliðunnar af
stigi :math:`n+1`.

.. end-toggle::


Núllstöðvar :math:`P_n`, fyrir :math:`n=1,\ldots,10`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ólíkt Chebyshev margliðunum þá er ekki hlaupið að því að finna rætur
:math:`\tilde P_{n+1}`. Þannig að við þurfum að reikna þær tölulega og
geyma í töflu.

.. image:: ./myndir/legendre.png

Dæmi um óheppilega skiptipunkta skoðað aftur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skoðum enn einu sinni fallið :math:`f(x) = 1/(25x^2+1)`, en í stað þess
að taka 9 jafndreifaða brúunarpunkta á bilinu :math:`[-1,1]`, þá skulum
við nota Legendre margliðurnar til að finna 9 punkta á bilinu.

.. image:: ./myndir/vond_bruun3.png

Athugasemd um :math:`\ell_\infty` og :math:`\ell_2`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
    Það má líta þannig á þetta að :math:`\ell_\infty` staðallinn 
    mæli hámarksskekkju 
    og :math:`\ell_2` mæli einhvers konar,,heildarskekkju",
    þar sem skekkjan er reiknað með heildinu hér á undan og svarar því hér um
    bil til flatarmálsins á milli fallsins og brúunarmargliðunnar.


-   :math:`\ell_\infty` staðallinn mælir hámarksskekkju, þannig að með 
    því nota Chebyshev margliðurnar þá erum við að reyna að lágmarka mestu skekkju
    á bilinu.

-   :math:`\ell_2` mæli einhvers konar,,heildarskekkju",
    þar sem skekkjan er reiknað með heildi. 
    Þannig að með því að nota Legendre margliðurnar þá erum við 
    í einhverjum skilningi að lágmarka flatarmál.

.. index::
    brúun; skekkjumat
    
Skekkjumat
----------

Nálgun á föllum með margliðum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lítum nú aftur á almenna brúunarverkefnið og gefum okkur að tölurnar
:math:`y_i^{(j)}` séu af gerðinni :math:`f^{(j)}(a_i)` þar sem
:math:`f : I \to {{\mathbb  R}}` er fall á bili :math:`I` sem inniheldur
alla punktana :math:`a_1, \ldots, a_k`.

Þá snýst brúunarverkefnið um að finna margliðu af stigi :math:`\leq m`
sem uppfyllir

.. math::

   p^{(j)}(a_i) = f^{(j)}(a_i), \quad
     j = 0, \ldots, m_i-1, \quad i = 1, \ldots, k.

Við vitum að lausn þess er ótvírætt ákvörðuð. Ef við notum Newton form
lausnarinnar, þá táknum við mismunakvótana með

.. math:: f[x_i,\ldots,x_{i+j}]

í stað

.. math:: y[x_i,\ldots,x_{i+j}]

Nálgun á fallgildum
~~~~~~~~~~~~~~~~~~~

Runurnar :math:`(x_0,\ldots,x_m)` og :math:`(y_0,\ldots,y_m)` eru
skilgreindar með

.. math::

   (x_0,x_1,\ldots,x_m) = 
     (\underbrace{a_1, \ldots, a_1}_{m_1 \, \text{sinnum}}, 
     \underbrace{a_2, \ldots , a_2}_{m_2 \, \text{sinnum}}, 
     \ldots , 
     \underbrace{a_k, \ldots , a_k}_{m_k \, \text{sinnum}})

og

.. math::

   \begin{gathered}
     (y_0,y_1,\ldots,y_m) = 
     (f^{(0)}(a_1), \ldots, f^{(m_1-1)}(a_1),
   f^{(0)}(a_2), \ldots, f^{(m_2-1)}(a_2) \\ \ldots,
     f^{(0)}(a_k), \ldots, f^{(m_k-1)}(a_k))
     \label{bru.margfald.5}\end{gathered}

Skekkjumat
~~~~~~~~~~

Nú tökum við punkt :math:`x \in I` og spyrjum um skekkjuna
:math:`f(x) - p(x)` í nálgun á :math:`f(x)` með :math:`p(x)`. Ef
:math:`x` er einn punktana :math:`a_1, \ldots, a_k`, þá er
:math:`p(x) = f(x)` og skekkjan þar með 0, svo við skulum gera ráð fyrir
að :math:`x \not= a_i`, :math:`i = 1, \ldots, k`.

Við bætum nú :math:`(x,f(x))` sem einföldum brúunarpunkti við alhæfða
brúunar verkefnið og fáum sem lausn :math:`q(t)` á þessu aukna verkefni.
Margliðan :math:`q` er af stigi :math:`\leq m+1`. Við notum táknið
:math:`t` fyrir breytu, því :math:`x` er frátekið.

Þá uppfyllir :math:`q(t)` að :math:`q(x) = f(x)` auk allra skilyrðanna

.. math:: q^{(j)}(a_i) = p^{(j)}(a_i) = f^{(j)}(a_i)

í verkefninu sem við byrjuðum með.

Við getum þá skrifað (sjá `Newton-margliður` til hliðsjónar)

.. math::

   \begin{aligned}
     q(t) &= p(t) + f[x_0,\ldots,x_m,x](t-x_0)\cdots(t-x_m) \\
     &= p(t) + f[x_0,\ldots,x_m,x](t-a_1)^{m_1}\cdots(t-a_k)^{m_k}.\end{aligned}

Þegar við gefum breytunni :math:`t` gildið :math:`x`, þá fáum við
:math:`q(x) = f(x)` og því fæst formúla fyrir skekkjunni

.. math::

   f(x) - p(x) 
     = f[x_0,\ldots,x_m,x](x-a_1)^{m_1}\cdots(x-a_k)^{m_k}

Nú ætlum við að finna leið til þess að meta skekkjuliðinn. Til þess
þurfum við að gefa okkur að :math:`f` hafi að minnsta kosti :math:`m+1`
afleiðu.

Tilfellið þegar við höfum aðeins einn punkt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Munum nú að í tilfellinu þegar við erum bara með einn punkt :math:`a_1`,
þá erum við með :math:`m+1` skilyrði

.. math:: p^{(j)}(a_1)=f^{(j)}(a_1), \qquad j=0,\dots,m

og við fáum að :math:`p` er Taylor-margliða fallsins :math:`f` í
punktinum :math:`a_1`. Þá er :math:`x_0=\cdots=x_m=a_1` og við fáum

.. math::

   f(x) - p(x) 
     = f[x_0,\ldots,x_m,x](x-a_1)^{m+1}

Nú segir setning Taylors okkur að til sé punktur :math:`\xi` milli
:math:`a_1` og :math:`x` þannig að

.. math::

   f(x) - p(x) 
     = \dfrac{f^{(n+1)}(\xi)}{(n+1)!}(x-a_1)^{m+1}

Við getum því dregið þá ályktun að í þessu sértilfelli er

.. math:: f[x_0,\ldots,x_m,x]=\dfrac{f^{(n+1)}(\xi)}{(n+1)!}

Það kemur í ljós að þetta er almenn regla sem gildir fyrir *öll*
alhæfðu brúunarverkefnin.

**Tilfellið** :math:`m=1` **er meðalgildisreglan** 

Munum að tilfellið :math:`m=1` er meðalgildisreglan

.. math:: f[a_1,x]=\dfrac{f(x)-f(a_1)}{x-a_1}=f'(\xi).

Margfeldni núllstöðva
~~~~~~~~~~~~~~~~~~~~~

Samfellt fall :math:`\varphi` á bili :math:`I` er sagt hafa núllstöð *af
stigi að minnsta kosti* :math:`m>0` í punktinum :math:`a\in I`, ef til
er samfellt fall :math:`\psi` á :math:`I` þannig að

.. math:: \varphi(x)=(x-a)^m\psi(x)

Við segjum að :math:`\varphi` hafi núllstöð af *margfeldni* :math:`m` ef
:math:`\psi(a)\neq0`.

Athugið að ef :math:`\varphi` er deildanlegt :math:`I` með samfellda
afleiðu, þá er :math:`\psi` deildanlegt með samfellda afleiðu í
:math:`I\setminus\{a\}` og við höfum

.. math::

   \begin{aligned}
     \varphi'(x)&=m(x-a)^{m-1}\psi(x)+(x-a)^m\psi'(x)\\
   &= (x-a)^{m-1} \big(m\psi(x)+(x-a)\psi'(x)\big)\end{aligned}

Ef afleiðan :math:`\psi'` er takmörkuð í grennd um :math:`a`, þá sjáum
við á þessari formúlu að :math:`\varphi'` hefur núllstöð af stigi að
minnsta kosti :math:`m-1` í :math:`a`.

Hugsum okkur nú að við séum með :math:`a_1,\dots,a_k` ólíka punkta í
bilinu :math:`I` og að :math:`m_1,\dots,m_k` séu jákvæðar náttúrlegar
tölur.

Ef fallið :math:`\varphi` hefur núllstöðvar í öllum punktunum
:math:`a_j` og núllstöðin :math:`a_j` er af stigi að minnsta kosti
:math:`m_j`. Við segjum að þá hafi :math:`\varphi` *að minnsta kosti*

.. math:: n=m_1+\cdots+m_k

*núllstöðvar taldar með margfeldni*.

Eins þá segjum við að :math:`\varphi` hafi :math:`n` núllstöðvar í
:math:`\{a_1,\dots,a_k\}` *taldar með margfeldni* ef :math:`\varphi`
hefur núllstöðvar í öllum punktum :math:`a_1,\dots,a_k` og samanlögð
margfeldni þeirra er :math:`n`

Hugsum okkur nú að fallið :math:`\varphi` hafi núllstöð af stigi
:math:`m_j` í punktunum :math:`a_j` fyrir öll :math:`j=1,\dots,k` og að
:math:`n=m_1+\cdots+m_k`.

Til einföldunar gerum við ráð fyrir að

.. math:: a_1<a_2<\cdots<a_k.

Þá gefur meðalgildissetningin að :math:`\varphi'` hefur að minnsta kosti
eina núllstöð á sérhverju bilanna

.. math:: ]a_1,a_2[, \  ]a_2,a_3[, \ \dots \  ]a_{k-1},a_k[

Þau eru samanlagt :math:`k-1` talsins. Að auki vitum við að
:math:`\varphi'` hefur núllstöðvar af stigi að minnsta kosti
:math:`m_j-1` í punktinum :math:`a_j`. Ef við leggjum þetta saman, þá
fáum við að :math:`\varphi'` hefur núllstöðvar af margfeldni að minnsta
kosti

.. math:: k-1+(m_1-1)+\cdots+(m_k-1)=n-1

í minnsta lokaða bilinu sem inniheldur alla punktana
:math:`a_1,\dots,a_k`.

Setning: Skekkjumat
~~~~~~~~~~~~~~~~~~~

Nú ætlum við að sýna fram á að fyrir föll :math:`f` sem eru
:math:`(m+1)` sinnum samfellt deildanleg að til sé :math:`\xi` á minnsta
bili sem inniheldur :math:`a_1, \ldots, a_k` og :math:`x` þannig að

.. math:: f[x_0,\ldots,x_m,x] = \frac{f^{(m+1)}(\xi)}{(m+1)!}

.. begin-toggle::
    :label: Sönnun

Við skilgreinum fallið

.. math:: g(t) = f(t) - p(t) - \lambda w(t),

þar sem

.. math:: w(t) = (t-a_1)^{m_1} \cdots (t-a_k)^{m_k}

og talan :math:`\lambda` er valin þannig að :math:`g(x) = 0`.

Nú er :math:`p^{(j)}(a_i)=f^{(j)}(a_i)` fyrir :math:`j=0,\dots,m_i-1`,
þá gefur setning Taylors okkur að :math:`g` hefur núllstöð af stigi
:math:`m_i` í sérhverjum punktanna :math:`a_i`. Auk þess hefur :math:`g`
núllstöð í :math:`x`. Samanlagt eru þetta að minnsta kosti :math:`m+2`
núllstöðvar taldar með margfeldni.

Höfum:

-   :math:`g` hefur að minnsta kosti :math:`m+2` núllstöðvar taldar með margfeldni,

-   :math:`g'` hefur að minnsta kosti :math:`m+1` núllstöð talda með margfeldni,

-   :math:`g''` hefur að minnsta kosti :math:`m` núllstöðvar taldar með margfeldni

-   og þannig áfram, þar til við ályktum að

-   :math:`g^{(m+1)}` hefur að minnsta kosti eina núllstöð.

Tökum eina slíka og köllum hana :math:`\xi`.

Munum að

.. math:: g(t) = f(t) - p(t) - \lambda w(t),

þar sem

.. math:: w(t) = (t-a_1)^{m_1} \cdots (t-a_k)^{m_k}=t^{m+1}+b_mt^m+\cdots+b_1t+b_0

Margliðan :math:`p` hefur stig :math:`\leq m` svo
:math:`p^{(m+1)}(x) = 0` fyrir öll :math:`x`

og margliðan :math:`w` er af stigi :math:`m+1` með stuðul :math:`1` við
hæsta veldið, svo :math:`w^{(m+1)}(t) = (m+1)!`. Við höfum því

.. math:: 0 = g^{(m+1)}(\xi) = f^{(m+1)}(\xi) - \lambda \cdot (m+1)!

sem jafngildir því að

.. math:: \lambda =\dfrac{f^{(m+1)}(\xi)}{(m+1)!}

Við setjum nú inn :math:`t=x` sem gefur

.. math:: 0=g(x) = f(x) - p(x) - \lambda w(x),

og við fáum þar með formúlu fyrir skekkjunni á nálgun á :math:`f(x)` með
alhæfðu brúunarmargliðunni :math:`p(x)`,

.. math::

   f(x) - p(x) =\lambda w(x) = \dfrac{f^{(m+1)}(\xi)}{(m+1)!} 
   (x-a_1)^{m_1} \cdots (x-a_k)^{m_k}

.. end-toggle::

Samantekt
~~~~~~~~~

Ef gefið er fall :math:`f:I\to {{\mathbb  R}}` á bili :math:`I`,
:math:`a_1,\dots,a_k` í :math:`I`, með :math:`a_j\neq a_k` ef
:math:`j\neq k`, jákvæðar heiltölur :math:`m_1,\dots,m_k`, talan
:math:`m` er skilgreind með :math:`m=m_1+\cdots+m_k-1`, og gert er ráð
fyrir að :math:`f\in C^{m+1}(I)`, þá er til nákvæmlega ein margliða
:math:`p` af stigi :math:`\leq m` þannig að

.. math:: p^{(j)}(a_i)=f^{(j)}(a_i), \qquad j=0,\dots, m_i-1, \quad i=1,\dots,k.

Newton-form margliðunnar :math:`p` er gefið með

.. math:: p(x)=f[x_0]+f[x_0,x_1](x-x_0)+\cdots+f[x_0,\dots,x_m](x-x_0)\cdots(x-x_{m-1})

þar sem mismunakvótarnir :math:`f[x_i,\dots,x_{i+j}]` eru skilgreindir
sem :math:`y[x_i,\dots,x_{i+j}]` út frá gögnunum :math:`y^{(j)}_i`.
Fyrir sérhvert :math:`x` í :math:`I` er skekkjan :math:`f(x)-p(x)` í
nálgun á :math:`f(x)` með :math:`p(x)` gefin með

.. math:: f(x)-p(x)=f[x_0,\dots,x_m,x](x-a_1)^{m_1}\cdots(x-a_k)^{m_k}.

Fyrir sérhvert :math:`i=1,\dots,k` og :math:`j=0,\dots,m-i` þá gildir að
til er tala :math:`\xi` á minnsta bilinu sem inniheldur
:math:`x_i\dots,x_{i+j}` þannig að

.. math:: f[x_i,\dots,x_{i+j}]=\dfrac{f^{(j)}(\xi)}{j!},

því gildir sérstaklega að til er tala :math:`\xi` á minnsta bilinu sem
inniheldur :math:`a_1,\dots,a_k` og :math:`x` þannig að

.. math:: f(x)-p(x)=\dfrac{f^{(m+1)}(\xi)}{(m+1)!}(x-a_1)^{m_1}\cdots(x-a_k)^{m_k}.

Sýnidæmi
~~~~~~~~

Látum :math:`f(x)=x^2\ln x`.

#.  Setjið upp mismunakvótatöflu til þess að reikna út brúunarmargliðu
    :math:`p` af stigi :math:`\leq 3` fyrir fallið :math:`f`, sem hefur tvo
    tvöfalda brúunarpunkta :math:`a_1=1` og :math:`a_2=2`. Skrifið upp
    Newton-form margliðunnar :math:`p`.

#.  Reiknið út :math:`p(1.3)`. Notið aðferðarskekkju fyrir margliðubrúun
    til þess að meta skekkjuna :math:`f(1.3)-p(1.3)` að ofan og neðan og
    fáið þannig bil þar sem rétta gildið liggur. Veljið miðpunkt bilsins sem
    nálgunargildi fyrir :math:`f(1.3)` og afrúnið gildið miðað við mörk
    bilsins.

#.  Látum nú :math:`q` vera brúnunarmargliðuna af stigi :math:`\leq 4` sem
    uppfyllir sömu skilyrði og gefin eru í fyrsta lið að viðbættu því að
    :math:`a_2=2` á að vera þrefaldur brúunarpunktur. Sýnið hvernig hægt er
    að ákvarða mismunakvótatöfluna fyrir :math:`q` með því að stækka töfluna
    í **a)**. Ákvarðið síðan :math:`q` og reiknið út :math:`q(1.3)`.

.. begin-toggle::
    :label: Lausn

**1. og 2.**
Til þess að spara pláss skulum leysa fyrsta og þriðja lið báða í einu
með því að reikna strax út mismunakvótatöfluna fyrir fjórða stigs margliðuna í
3. lið. Punktarnir :math:`x_0,\dots,x_4` eru þá :math:`1,1,2,2,2` og
við höfum gefin fallgildin

.. math::

   f(1)=f[x_0]=f[x_1]=0 \qquad  \text{ og } \qquad
   f(2)=f[x_2]=f[x_3]=f[x_4].

Í 1. lið eru punktarnir tvöfaldir svo við höfum gefin gildi
afleiðunnar :math:`f'(x)=2x\ln x+x` í punktunum :math:`1` og :math:`2`.

.. math::

   f'(1)=f[1,1]=f[x_0,x_1]=1 \ \text{ og } \  
   f'(2)=f[2,2]=f[x_2,x_3]=4\ln 2+2.

Í 3. lið er gildið á 2. afleiðu :math:`f''(x)=2\ln x +3` gefið í
punktinum :math:`2`. Það gefur okkur

.. math:: f''(2)/2!=f[2,2,2]=f[x_2,x_3,x_4]=\ln 2+\tfrac 32.

Við setjum þessi gildi inn í mismunakvótatöfluna og fyllum hana út með
því að taka mismunakvóta milli allra gilda

.. math::

   \begin{matrix}
   i&x_i & f[x_i] &f[x_i,x_{i+1}] & f[x_i,x_{i+1},x_{i+2}] &
   f[x_i,\dots,x_{i+3}]&f[x_i,\dots,x_{i+4}] \\\hline
   0&1&0     &1       &4\ln 2-1        &-4\ln 2+3& 5\ln 2-\tfrac 72\\
   1&1&0     &4\ln 2  &2               &\ln 2-\tfrac 12\\
   2&2&4\ln 2&4\ln 2+2&\ln 2+\tfrac 32\\
   3&2&4\ln 2&4\ln 2+2\\
   4&2&4\ln 2
   \end{matrix}

Margliðan í 1. lið er því

.. math:: p(x)=(x-1)+(4\ln 2-1)(x-1)^2+(-4\ln 2+3)(x-1)^2(x-2).

en í 3. lið er hún

.. math:: q(x)=p(x)+(5\ln 2-\tfrac 72)(x-1)^2(x-2)^2

**2.** Við stingum gildinu :math:`x=1.3` inn í margliðuna og fáum
:math:`p(1.3)=0.445206074`. Skekkjan er

.. math:: f(x)-p(x)=\dfrac{f^{(4)}(\xi)}{4!}(x-1)^2(x-2)^2

þar sem :math:`\xi` er einhver punktur á bilinu :math:`[1,2]`.

Við þurfum því að meta fjórðu afleiðuna,

.. math::

   \begin{aligned}
   f(x) &=x^2\ln x, \quad
   f'(x)=2x\ln x+x, \quad
   f''(x)=2\ln x+3, \quad
   \\  
   f'''(x)& =2/x, \quad
   f^{(4)}(x)=-2/x^2.\end{aligned}

Ef :math:`x\in [1,2]`, þá höfum við matið
:math:`-2\leq f^{(4)}(x)\leq -\tfrac 12`.

Af ójöfnunum :math:`-2\leq f^{(4)}(x)\leq -\tfrac 12` leiðir síðan að

.. math::

   \alpha=\dfrac{-2\cdot(0.3)^2\cdot(-0.7)^2}{24}\leq f(1.3)-p(1.3)
   \leq \dfrac{-0.5\cdot(0.3)^2\cdot(-0.7)^2}{24}=\beta.

Við reiknum út úr báðum brotunum

.. math::

   \alpha=-0.003675 \qquad \text{ og } \qquad 
   \beta=-0.00091875.

þar með er :math:`f(1.3)` á bilinu milli :math:`p(1.3)+\alpha=0.441531`
og :math:`p(1.3)+\beta=0.444287`.

Nálgunargildi okkar á að vera miðpunktur þessa bils og algildi
skekkjunnar verður þá hálf billengdin. Það færir okkur nálgunina
:math:`f(1.3) \approx 0.442909` og skekkjuna :math:`\pm 0.0014`. Réttur
afrúningur er :math:`f(1.3)=0.44`.

Við eigum aðeins eftir að reikna út gildi margliðunnar :math:`q` í
punktinum :math:`1.3`. Út úr mismunakvótatöflunni fáum við

.. math:: q(x)=p(x)+(5\ln 2-\tfrac 72)(x-1)^2(x-2)^2

sem gefur okkur gildið

.. math:: q(1.3)=0.445206074-0.001511046=0.4436950278

Til samanburðar höfum við rétt gildi

.. math:: f(1.3)=0.443395606950060\ldots.

.. end-toggle::

.. index::
    brúun; splæsibrúun
    splæsibrúun

Splæsibrúun
-----------

Látum :math:`(t_0,y_0),\dots,(t_n,y_n)` vera punkta í plani og gerum ráð
fyrir að :math:`a=t_0<t_1<\cdots<t_n=b`.

Við höfum nú lært að ákvarða margliðu :math:`p` af stigi :math:`\leq n`
sem tekur gildin :math:`y_i` í punktunum :math:`t_i`.

Ef punktarnir liggja á grafi fallsins :math:`f` og nota á margliðuna til
þess að nálga fallgildi :math:`f`, þá getur það verið ýmsum erfiðleikum
bundið þegar stig hennar stækkar eins og við sáum í byrjun kaflans
`Skynsamlegir skiptipunktar og Chebyshev margliður`_.
Lausnin þar var að reyna að velja brúunarpunktana skynsamlega. Ef við
hins vegar getum ekki valið brúunarpunktana eftir eigin höfði þá erum
við í vandræðum og þurfum við að leita annarra leiða.

Almennt um splæsibrúun
~~~~~~~~~~~~~~~~~~~~~~

Splæsibrúun er leið út úr þessum vandræðum.

Með henni er fundið samfellt fall :math:`S` sem brúar gefnu punktana,
:math:`S(t_i)=y_i`, og er þannig að einskorðun þess við hlutbilin
:math:`[t_i,t_{i+1}]` er gefið með margliðu af stigi :math:`\leq m`, þar
sem :math:`m` er fyrirfram gefin tala.

Algengast er að nota :math:`m=3`.

.. index::
	splæsibrúun; fyrsta stigs

Fyrsta stigs splæsibrúun:
~~~~~~~~~~~~~~~~~~~~~~~~~

Ef stigið :math:`m` er :math:`1`, þá erum við einfaldlega að draga
línustrik milli punktanna og sjáum í hendi okkar að lausnin er

.. math::

   S(x) = \begin{cases}
           S_0(x) = \dfrac {y_1-y_0}{t_1-t_0}(x-t_0)+y_0, 
               & x \in [t_0,t_1],\\
           S_1(x) = \dfrac {y_2-y_1}{t_2-t_1}(x-t_1)+y_1, 
               & x \in [t_1,t_2],\\
           \vdots & \\
           S_{n-1}(x) = \dfrac {y_n-y_{n-1}}{t_n-t_{n-1}}
               (x-t_{n-1})+y_{n-1}, &x \in [t_{n-1},t_n].
       \end{cases}

Þessi aðferð er ekki mikið notuð því hún er ósannfærandi fyrir
deildanleg föll.

.. index::
	splæsibrúun; þriðja stigs

Þriðja stigs splæsibrúun
~~~~~~~~~~~~~~~~~~~~~~~~

Algengast er að framkvæma splæsibrúun með þriðja stigs margliðum.

Við skulum tákna einskorðun :math:`S` við hlutbilið
:math:`[t_i,t_{i+1}]` með :math:`S_i` og skrifa

.. math::

   S_i(x) = a_i+b_i(x-t_i)+c_i(x-t_i)^2+d_i(x-t_i)^3, 
           \qquad x\in [t_i,t_{i+1}).

Við ætlum að leiða út jöfnur fyrir stuðlunum :math:`a_i, b_i, c_i` og
:math:`d_i`. Kröfurnar sem við setjum eru:

#. :math:`S` er tvisvar sinnum samfellt deildanlegt á öllu bilinu :math:`[a,b]`

#. :math:`S` taki gildin :math:`y_i` í punktunum :math:`t_i`

Setjum til einföldunar :math:`h_i = t_{i+1}-t_i` fyrir :math:`i = 0,
\ldots, n-1`.

Skilyrðin tvö má því skrifa sem eftirfarandi jöfnuhneppi:

.. begin-toggle::
	:label: Útleiðsla á jöfnuhneppi


Á hverju hlutbili :math:`[t_i,t_{i+1}]` höfum við:

.. math::

   S_i(x) = a_i+b_i(x-t_i)+c_i(x-t_i)^2+d_i(x-t_i)^3, 
           \qquad x\in [t_i,t_{i+1}),

sem þýðir að skilyrðin tvö má skrifa sem

.. math::

   \begin{aligned}
       a_i &=& &S_i(t_i)& &=& y_i  
           &, \quad (1) \\
       a_i + b_ih_i + c_ih_i^2 + d_ih_i^3 &=& &S_i(t_{i+1})
           = S_{i+1}(t_{i+1})& &=& a_{i+1} 
           &, \quad (2) \\
       b_i + 2c_ih_i + 3d_ih_i^2 &=& &S_i'(t_{i+1}) 
           = S_{i+1}'(t_{i+1})& &=& b_{i+1}
           &, \quad (3) \\
       2c_i + 6d_ih_i &=& &S_i''(t_{i+1})
           = S_{i+1}''(t_{i+1})& &=& 2c_{i+1}
           &, \quad (4)\end{aligned}

Í (1) höfum við :math:`i = 0,\ldots,n` og í (2)-(4) höfum við
:math:`i=0,\ldots,n-2`.

Samtals: :math:`(n+1)+3(n-1)=4n-2` línulegar jöfnur til þess að ákvarða
:math:`4n` óþekktar stærðir.

Það er því ljóst að okkur vantar tvö skilyrði til þess að geta fengið
ótvírætt ákvarðaða lausn.

Fyrstu jöfnurnar gefa strax gildi :math:`a_i` og (4) gefur að

.. math:: d_i = \frac{c_{i+1}-c_i}{3h_i}, \quad i=0,\ldots,n-2

Ef við setjum þetta inn í (2) og (3) fæst

.. math::

   \begin{aligned}
       a_{i+1} = a_i + b_ih_i + \frac{c_{i+1}+c_i}{3}h_i^2
           &, \quad i=0,\ldots,n-2 \\
       b_{i+1} = b_i + (c_{i+1} + c_i)h_i
           &, \quad i=0,\ldots,n-2\end{aligned}

Þegar við leysum fyrri jöfnuna fyrir :math:`b_i` fæst

.. math::

   b_i = \frac{a_{i+1}-a_i}{h_i}-\frac{c_i+c_{i+1}}{3}h_i
           , \quad i=0,\ldots,n-2

og ef við setjum þetta inn í seinni jöfnuna fæst á endanum að

.. math::

   h_{i-1}c_{i-1} + 2(h_{i-1}+h_i)c_i + h_ic_{i+1} = 
       \frac{3}{h_i}(a_{i+1}-a_i) 
           - \frac{3}{h_{i-1}}(a_i-a_{i-1})
       , \quad i=1,\ldots,n-1

.. end-toggle::

Jöfnuhneppið
~~~~~~~~~~~~

.. math::

   \begin{aligned}
       \left[ \begin{array}{c:cccc:c}
       .?.  & .?.       &&&& \\ \hdashline
       h_0 & 2(h_0+h_1) & h_1 &&&\\
           & h_1        & 2(h_1+h_2) & h_2 &&\\
           &&&&&\\
           &            & \ddots      & \ddots & \ddots &\\
           &&&&&\\
           &  &  & h_{n-2}  & 2(h_{n-2} + h_{n-1}) & h_{n-1} 
           \\ \hdashline
           &  &  &   & .?.    & .?.
       \end{array} \right]
       \left[ \begin{array}{c}
       c_0 \\ \hdashline
       c_1 \\
       c_2 \\
       \\
       \vdots \\
       \\
       c_{n-1} \\ \hdashline
       c_n
       \end{array} \right] 
       \\
       = 3\left[ \begin{array}{c}
       .?. \\ \hdashline
       \dfrac{a_2-a_1}{h_1} - \dfrac{a_1-a_0}{h_0} \\
       \dfrac{a_3-a_2}{h_2} - \dfrac{a_2-a_1}{h_1} \\
       \vdots \\
       \dfrac{a_n-a_{n-1}}{h_{n-1}} 
           - \dfrac{a_{n-1}-a_{n-2}}{h_{n-2}}
       \\ \hdashline
       \end{array} \right]\end{aligned}

En það vantar í þetta einhver skilyrði á :math:`c_0` og :math:`c_n`.

Þegar þau hafa verið sett inn, þá getum við leyst þetta hneppi, reiknað svo
gildi :math:`b_i` og :math:`d_i` og þá höfum við fundið splæsifallið
okkar.

Það eru til margar leiðir til að ákvarða :math:`c_0` og :math:`c_n`, en
fjórar eru algengastar.

Tilfelli 1: Ekki-hnúts endaskilyrði
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef við höfum engar upplýsingar um fallið :math:`f` í :math:`t_1` og
:math:`t_{n-1}` liggur beint við að krefjast þess að :math:`S'''` sé
samfellt þar, sem þýðir að :math:`d_0 = d_1` og
:math:`d_{n-2} = d_{n-1}`. Með að nota jöfnurnar fyrir :math:`d_i` má
skrifa þetta sem

.. math::

   \begin{aligned}
       h_1c_0 - (h_0 + h_1)c_1 + h_0c_2 = 0 \\
       h_{n-1}c_{n-2}-(h_{n-2}+h_{n-1})c_{n-1}+h_{n-2}c_n = 0\end{aligned}

og þessar jöfnur, ásamt hinum, má leysa til að ákvarða :math:`c_i`-in.

Tilfelli 2: Þvinguð endaskilyrði
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef hallatala fallsins :math:`f` er þekkt í endapunktum bilsins er
eðlilegt að nota þær upplýsingar við ákvörðun splæsifallsins. Gerum því
ráð fyrir að :math:`f'(t_0) = A` og :math:`f'(t_n) = B`. Skilyrðið
:math:`S'(t_0) = A` gefur þá að

.. math:: A = \frac{a_1-a_0}{h_0} - \frac{2c_0+c_1}{3}h_0,

eða

.. math::

   2h_0c_0 + h_0c_1 = 
       3 \left( \frac{a_1-a_0}{h_0} - A \right)

og :math:`S'(t_n) = B` gefur

.. math:: B = b_{n-1} + 2c_{n-1}h_{n-1} + 3d_{n-1}h_{n-1}^2

og með að nota formúlurnar fyrir :math:`b_{n-1}` og :math:`d_{n-1}`
fæst

.. math::

   c_{n-1}h_{n-1} + 2c_nh_{n-1} = 
       3 \left( B  - \frac{a_n-a_{n-1}}{h_{n-1}} \right).

Tilfelli 3: Náttúrleg endaskilyrði
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Einfaldasta lausnin er að setja :math:`c_0 = c_n = 0`, en það jafngildir
því að :math:`S''(t_0) = S''(t_n) = 0`.

Tilfelli 4: Lotubundið endaskilyrði
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hugsum okkur að við viljum framlengja :math:`S` í tvisvar samfellt
deildanlegt :math:`(b-a)`-lotubundið fall á :math:`{{\mathbb  R}}`. Það
setur skilyrðin

.. math::

   y_0 = S(t_0) = S_(t_n) = y_n, \quad
       S'(t_0) = S'(t_n), \quad
       \text{ og } \quad
       S''(t_0) = S''(t_n)

Fljótséð er að :math:`S''(t_0) = S''(t_n)` þýðir að :math:`c_0 = c_n`,
eða

.. math:: c_0 - c_n = 0.

Þetta er fyrri jafnan sem við þurfum.

Nú gefur :math:`S'(t_0) = S'(t_n)` að

.. math:: b_0 = b_{n-1} + 2c_{n-1}h_{n-1} + 3d_{n-1}h_{n-1}^2

og með að setja inn formúlurnar fyrir :math:`b_0, b_{n-1}, d_{n-1}` og
nota að :math:`c_0 = c_n` fæst jafnan

.. math::

   h_0c_1 + 2h_{n-1}c_{n-1} + (2h_0 + 2h_{n-1})c_n
       = 3 \left( \frac{a_1-a_0}{h_0} 
           - \frac{a_n-a_{n-1}}{h_{n-1}} \right).

.. index::
	brúun; ferlar

Teikning á ferlum í planinu
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hægt er að nota brúun til þess að nálga ferla í :math:`\mathbb R^n`.
Skoðum tilvikið :math:`n=2`.

Gerum nú ráð fyrir að við höfum gefna punkta :math:`(x_0,y_0),\dots,(x_n,y_n) \in \mathbb R^2`
og að við viljum finna samfelldan splæsiferil í gegnum þá. Þetta er gert
í nokkrum skrefum:

#. Ákveðið er stikabil :math:`[a,b]` og skiptingu á því

   .. math:: a=t_0<t_1<\cdots<t_n=b

   til dæmis :math:`[0,n]` og skiptinguna

   .. math:: 0=t_0<t_1=1<\cdots<t_n=n.

#. Ákveðið er hvaða endaskilyrði eiga við.

#. Búin eru til tvö splæsiföll :math:`R(t)` fyrir punktasafnið
   :math:`x_0,\dots,x_n` og :math:`S(t)` fyrir punktasafnið
   :math:`y_0,\dots,y_n`.

#. Stikaferillinn :math:`[a,b]\ni t\mapsto (R(t),S(t))` er síðan teiknaður, en hann uppfyllir
   :math:`(R(t_j),S(t_j))=(x_j,y_j)`, :math:`j=0,\dots,n`.

.. warning::
	Athugið að hér er :math:`t` breytan okkar en :math:`x` og :math:`y` eru gildin sem við
	viljum að ferillinn taki. 
	
	Þetta er frábrugðið því þegar við skoðum graf af einni breytu en þá er 
	:math:`x` venjulega breytan og :math:`y` gildin sem viljum taka.

.. index::
	aðferð minnstu fervika

Aðferð minnstu fervika
----------------------

Látum :math:`(x_1,y_1),\dots,(x_m,y_m)` vera safn punkta í plani með
:math:`x_j\in
[a,b]` fyrir öll :math:`j` og látum :math:`f_1,\dots,f_n` vera raungild
föll á :math:`[a,b]`.

Við viljum finna það fall :math:`f` af gerðinni

.. math:: f(x)=c_1f_1(x) + \cdots + c_nf_n(x)

með stuðla :math:`c_1, \ldots, c_n` þannig að punktarnir
:math:`(x_j,f(x_j))` nálgi gefna punktasafnið sem best og þá er átt við
að ferningssummuna

.. math:: \sum_{i=1}^m\big(y_i-f(x_i)\big)^2

verði eins lítil og mögulegt er.


.. index::
	jafna bestu línu

Jafna bestu línu
~~~~~~~~~~~~~~~~

Flestir hafa heyrt talað um bestu línu gegnum punktasafn, hún fæst með
að taka hér :math:`f_1(x) = 1` og :math:`f_2(x) = x`, en lítið mál er að
finna einnig besta fleygboga, bestu margliðu af fyrirfram ákveðnu stigi
eða einhverja aðra samantekt falla gegnum punktasafnið.

Smávegis línuleg algebra
~~~~~~~~~~~~~~~~~~~~~~~~

Til þess að finna þessi gildi á stuðlunum :math:`c_i` er heppilegt að
notfæra sér nokkrar niðurstöður úr línulegri algebru. Fyrir gefin gildi
á :math:`c_1,\dots,c_n` setjum við

.. math::

   b_i = f(x_i) = c_1f(x_i) + \cdots + c_n f_n(x_i), 
       \qquad i=1,\dots,m,

og skilgreinum síðan dálkvigrana

.. math::

   b = [b_1,\dots,b_m]^T,\qquad 
       y = [y_1,\dots,y_m]^T,\quad \text{ og } \quad 
       c = [c_1,\dots,c_n]^T,\qquad

Þá er :math:`Ac=b`, þar sem :math:`A` er :math:`m\times n` fylkið

.. math::

   A = \left[\begin{matrix} 
           f_1(x_1)& f_2(x_1) & \dots & f_n(x_1) \\ 
           f_1(x_2)& f_2(x_2) & \dots & f_n(x_2) \\
           \vdots &\vdots &\ddots &\vdots \\
           f_1(x_m)& f_2(x_m) & \dots & f_n(x_m)
       \end{matrix}\right].

Verkefnið snýst nú um að finna þann vigur :math:`c\in {{\mathbb  R}}^n`
sem lágmarkar

.. math::

   \sum_{i=1}^m \big(y_i-b_i\big)^2
       = \| y - b \|^2 = \| y - Ac \|^2

þar sem :math:`\|\cdot\|` táknar `evklíðska fjarlægðina <https://en.wikipedia.org/wiki/Euclidean_distance>`_ 
(staðalinn) á :math:`{{\mathbb  R}}^m`.

Vigrar af gerðinni :math:`b= Ac` spanna dálkrúm fylkisins :math:`A` og
þá má skrifa sem línulegar samantektir af gerðinni

.. math:: b = c_1A_1 + \cdots + c_nA_n

þar sem :math:`A_j` er dálkur númer :math:`j`.

Verkefnið snýst um að finna þann vigur í dálkrúminu sem næstur er
:math:`y`. Vigurinn :math:`b` er næstur :math:`y` ef og aðeins ef
:math:`y-b` er hornréttur á alla vigra dálkrúmsins.

Þessi skilyrði má fá með innfeldi

.. math:: A_j \cdot (y-b) = 0, \qquad j = 1, \ldots , n

Með fylkjarithætti fæst ein jafna

.. math:: A^T (y-b) = 0.

Setjum nú inn :math:`b=Ac`. Þá ákvarðast :math:`c` af hneppinu

.. math:: A^T(y-Ac) = 0

sem jafngildir

.. math:: (A^TA)c = A^Ty

Við þurfum því aðeins að leysa þetta jöfnuhneppi

.. math:: (A^TA)c = A^Ty

fyrir :math:`c` til að finna stuðlana okkar. Ef fylkið :math:`A^TA`
hefur andhverfu, þá fæst alltaf ótvírætt ákvörðuð lausn :math:`c`.

Ef fylkið :math:`A^TA` hefur ekki andhverfu eða að það hefur ákveðu sem
er mjög nálægt :math:`0`, þá þurfum við að beita flóknari brögðum. Við
komum að því `síðar <LU-þáttun>`_.

.. index::
	jafna bestu línu

Jafna bestu línu
~~~~~~~~~~~~~~~~

Algengt er að menn vilji finna beina línu sem best fellur að
punktasafninu :math:`(x_1,y_1,)\dots,(x_m,y_m)`. Þá er :math:`n=2` og
við tökum lausnagrunninn :math:`f_1(x)=1` og :math:`f_2(x)=x`.

Fylkið er þá

.. math::

   A = \left[\begin{matrix} 
           1& x_1\\
           1& x_2 \\
           \vdots &\vdots \\
           1& x_m 
       \end{matrix}\right].

og þar með

.. math::

   A^TA = \left[\begin{matrix} 
           m& \sum_{j=1}^mx_j\\
           \sum_{j=1}^mx_j& \sum_{j=1}^mx_j^2 
       \end{matrix}\right].
   \qquad \text{ og } \qquad
       A^Ty = \left[\begin{matrix} 
            \sum_{j=1}^my_j\\
           \sum_{j=1}^mx_jy_j
       \end{matrix}\right].

.. note::
	Það er auðvelt að leysa þetta tilvik því við höfum einfalda formúlu fyrir andhverfum
	:math:`2 \times 2` fylkja (svo lengi sem ákveðan er ekki 0).
	
	Sjá `Wikipedia <https://en.wikipedia.org/wiki/Invertible_matrix#Inversion_of_2.C3.972_matrices>`_.

.. index::
	jafna besta fleygboga

Jafna bestu annars stigs margliðu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef við viljum finna bestu annars stigs margliðu gegnum punktasafnið, þá
er :math:`n=3` og við tökum lausnagrunninn :math:`f_1(x)=1`,
:math:`f_2(x)=x` og :math:`f_3(x)=x^2`.

Þetta val gefur fylkið

.. math::

   A = \left[\begin{matrix} 
           1& x_1 & x_1^2\\
           1& x_2 & x_2^2\\
           \vdots &\vdots &\vdots\\
           1& x_m& x_m^2 
       \end{matrix}\right].

Fylkið :math:`A^TA` er þá :math:`3\times 3` og vigurinn :math:`A^Ty` er
dálkvigur með :math:`3` hnit.

Sýnidæmi: besta annars stigs margliða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gefin eru mæligildin

+-------------+-------+--------+--------+--------+--------+-------+-------+
| :math:`x`   | 0     | 1      | 2      | 3      | 4      | 5     | 6     |
+=============+=======+========+========+========+========+=======+=======+
| :math:`y`   | 2.7   | -0.5   | -1.7   | -1.9   | -1.5   | 0.2   | 2.3   |
+-------------+-------+--------+--------+--------+--------+-------+-------+

Beitið aðferð minnstu fervika til þess að finna þá annars stigs margliðu
sem best fellur að þessum gögnum Teiknið upp gögnin og graf marliðunnar.

.. begin-toggle::
	:label: Lausn

Við leitum hér að þremur tölum :math:`c_1`, :math:`c_2` og
:math:`c_3` þannig að annars stigs margliðan
:math:`f(x)=c_1f_1(x)+c_2f_2(x)+c_3f_3(x)` falli sem best að gögnunum. 
Grunnföllin þrjú eru :math:`f_1(x)=1`, :math:`f_2(x)=x` og
:math:`f_3(x)=x^2`.

Í þessu dæmi er fylkið :math:`A` gefið með

.. math::

   A=\left[\begin{matrix}
   1 & 0&0\\
   1 & 1&1\\
   1&2&4\\
   1&3&9\\
   1&4&16\\
   1&5&25\\
   1&6&36
   \end{matrix}\right],

því stak númer :math:`(i,j)` í A er gefið með :math:`A_{ij} = f_j(x_i)`.

Nú látum við matlab um afganginn

::

    %  Matlab forrit sem teiknar upp bestu margliðunálgun á gefnum gögnum
    x=[0; 1; 2; 3; 4; 5; 6] 
    y=[2.7; -0.5; -1.7; -1.9; -1.5; 0.2; 2.3 ] 
    m=length(x); 

    % Við leitum að bestu margliðu af stigi 2 eða lægri 
    % og því eru  grunnföllin eru 3 talsins. 
    n=3; 

    % Stuðlafylkið er A=(a_{ij}), a_{ij}=x_i^{j-1}  
    A(1:m,1)=ones(m,1); 
    A(1:m,2)=x; 
    for j=3:n 
        A(1:m,j)=A(1:m,j-1).*x; 
    end  
    % Reiknum úr úr normaljöfnuhneppinu A^TAc=A^Ty:  
    c=(A'*A)\(A'*y); 

    % Teikning undirbúin 
    N=100;   
    X=linspace(min(x),max(x),N); 

    % Hliðrun í reikniriti horners er 0 
    % 
    hlidrun=zeros(n,1); 
    for j=1:N 
        Y(j)=horner(c, hlidrun, X(j)); 
    end 
    figure 
    plot(x,y,'*',X,Y) 
    xlabel('x'), ylabel('y') 
    title('Adferd minnstu fervika fyrir marglidu af stigi 2') 
    print 

Hér kemur myndin sem beðið var um:

.. image:: ./myndir/synidaemi_minnstu_fervik.png

.. end-toggle::
