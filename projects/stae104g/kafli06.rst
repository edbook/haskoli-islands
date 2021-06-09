Heildun
=======

.. note::
	**Nauðsynleg undirstaða**
	
	- markgildi 

	- afleiður

	- keðjureglan 

	- reiknireglur fyrir afleiður

*It can be very dangerous to see things from somebody else's point of view without the proper training.*

\- Douglas Adams, The Ultimate Hitchhiker's Guide : Five Complete Novels and One Story

.. index::
    heildi; jákvæðs falls
    heildi
    heildismörk
    fall; heildanlegt
    flatarmál

-----

Heildun
-------

Óformleg skilgreining á heildi jákvæðs falls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f:[a,b]\rightarrow {{\mathbb  R}}` vera fall þannig að
:math:`f(x)\geq 0` fyrir öll :math:`x\in[a,b]`.

Þegar :hover:`heildið,heildi` :math:`\int_a^b f(x)\,dx` er skilgreint er útkoman úr því
flatarmál svæðisins sem liggur á milli :math:`x`-ás og grafs fallsins
(og afmarkast til vinstri af línunni :math:`x=a` og til hægri af línunni
:math:`x=b`).

Ef heildið :math:`\int_a^b f(x)\,dx` er skilgreint þá segjum við að
fallið :math:`f` sé :hover:`heildanlegt,heildanlegur` yfir bilið :math:`[a,b]`.

Tölurnar :math:`a` og :math:`b` kallast :hover:`heildismörk,heildismark` heildisins.

Skilgreining
~~~~~~~~~~~~

Látum :math:`f` vera fall. Skilgreinum föllin :math:`f_+` og
:math:`f_-`, sem bæði hafa sama skilgreiningarsvæði og :math:`f`, með

.. math::

   f_+(x)=\left\{\begin{array}{ll} f(x) & \text{ef }f(x)\geq 0,\\
     0 & \text{ef }f(x)<0, \end{array} \right. \qquad
     f_-(x)=\left\{\begin{array}{ll} 0 & \text{ef }f(x)\geq 0,\\
     -f(x) & \text{ef }f(x)<0. \end{array}\right.

Athugið að :math:`f(x)=f_+(x)-f_-(x)`.

.. image:: ./myndir/kafli06/01_fplusminus.png
	:align: center
	:width: 12cm


Óformleg skilgreining á heildi falls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Takmarkað fall :math:`f` er *heildanlegt* yfir bilið :math:`[a, b]` ef
bæði föllin :math:`f_+` og :math:`f_-` eru heildanleg yfir bilið
:math:`[a,
b]`. Ef fallið :math:`f` er heildanlegt þá skilgreinum við heildi þess
með formúlunni

.. math:: \int_a^b f(x)\,dx=\int_a^b f_+(x)\,dx-\int_a^b f_-(x)\,dx.

.. note:: Flatarmálið sem er undir :math:`x`-ás reiknast neikvætt.

Undir- og yfirsummur
--------------------

Dæmi: Að finna heildi
~~~~~~~~~~~~~~~~~~~~~

Hvernig getum við fundið flatarmálið :math:`\int_a^b f(x)\, dx`?

**Svar:** Við þurfum að nálga flatarmálið með formum sem hafa þekkt
flatarmál, til dæmis rétthyrningum.

.. index::
    undirsumma
    heildun; undirsumma

Skilgreining: Undirsumma
~~~~~~~~~~~~~~~~~~~~~~~~

Skiptum bilinu :math:`[a,b]` í :math:`n` hlutbil. Á hverju hlutbili komum
við fyrir rétthyrningi sem liggur undir grafi fallsins, þ.e. hæðin á
honum er lággildi fallsins á þessum tiltekna hlutbili.

.. image:: ./myndir/kafli06/03_undirsumma.png
	:align: center
	:width: 12cm

Látum :math:`u_k` vera flatarmál rétthyrninganna, þar sem
:math:`k=1,\ldots,n`.

Við köllum flatarmál allra rétthyrninganna :hover:`undirsummu,undirsumma` fyrir heildið og
táknum hana með :math:`U(n)`, það er :math:`U(n) = \sum_{k=1}^n u_k`.

Þá er augljóslega :math:`U(n) \leq \int_a^b f(x)\, dx`.

Þegar :math:`n` stækkar þá fáum við betri og betri nálgun á heildinu.

.. index::
    yfirsumma
    heildun; yfirsumma

Skilgreining: Yfirsumma
~~~~~~~~~~~~~~~~~~~~~~~

Skiptum bilinu :math:`[a,b]` í :math:`n` hlutbil. Á hverju hlutbili komum
við fyrir rétthyrning sem er þannig að hæðin á honum er hágildi fallsins
á þessum tiltekna hlutbili.

.. image:: ./myndir/kafli06/03_yfirsumma.png
	:align: center
	:width: 12cm

Táknum flatarmál hans með :math:`y_k`, þar sem :math:`k=1,\ldots,n`. Við
köllum summu flatarmáls allra rétthyrninganna :hover:`yfirsummu,yfirsumma` fyrir heildið
og táknum hana með :math:`Y(n)`, það er :math:`Y(n) = \sum_{k=1}^n y_k`.

Þá fæst að :math:`\int_a^b f(x)\, dx \leq Y(n)`.

Þegar :math:`n` stækkar þá fáum við betri og betri nálgun á heildinu.

Skilgreining: Heildi
~~~~~~~~~~~~~~~~~~~~

Ef til er **nákvæmlega ein** tala :math:`I` þannig að

.. math:: U(n) \leq I \leq Y(n),

fyrir allar undirsummur :math:`U(n)` og yfirsummur :math:`Y(n)` þá er
fallið :math:`f` heildanlegt á :math:`[a,b]` og

.. math:: I = \int_a^b f(x)\, dx.

.. ggb:: pCuJwqEE
    :width: 700
    :height: 400
    :img: ./03_undirogyfirsumma.png
    :imgwidth: 12cm


.. note::
    Við sögðum ekkert um það hvernig við skiptum bilinu :math:`[a,b]` í
    :math:`n` hlutbil. Það má gera hvernig sem er, það er ekki nauðsynlegt að
    þau séu öll jafn stór. Eina krafan er að stærð allra hlutbila stefni á
    0 þegar :math:`n\to \infty`. 

.. note::
    Við erum ekki bundin af því að skoða rétthyrninga sem með hæð sem er
    há/lággildi fallsins á hverju hlutbili, t.d. má taka miðgildið á hveru
    hlutbili, gildið í hægri endapunkti þess eða gildið í vinstri endapunkti þess.
    
    Niðurstaðan þegar :math:`n\to \infty` verður hins vegar alltaf sú sama,
    þ.e. við nálgumst heildið.

.. note::
    Einnig er mögulegt að nálga heildið með öðrum formum en rétthyrningum,
    t.d.trapisum, og hentar það hugsanlega betur í
    tölulegum útreikningum.



Eiginleikar heildisins
----------------------

Setning
~~~~~~~

(i)  Ef fallið :math:`f` er samfellt á bilinu :math:`[a, b]` þá er
     :math:`f` heildanlegt yfir bilið :math:`[a, b]`.

(ii) Einhalla fall skilgreint á bili :math:`[a,b]` er heildanlegt.

Setning
~~~~~~~

Látum :math:`f` vera fall sem er heildanlegt yfir bilið :math:`[a, b]`.
Þá er

.. math:: \Big|\int_a^b f(x)\,dx\Big|\leq \int_a^b |f(x)|\,dx.

Skilgreining: Heildismörkunum snúið við
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef fallið :math:`f` er heildanlegt yfir bilið :math:`[a,b]` (hér er
:math:`a<b`) þá skilgreinum við

.. math:: \int_b^a f(x)\,dx=-\int_a^b f(x)\,dx.

Setning
~~~~~~~

(i)  :math:`\int_a^a f(x)\,dx=0`.

(ii) :math:`\int_a^b f(x)\,dx=\int_a^c f(x)\,dx+\int_c^b f(x)\,dx`

     (Hér er náttúrlega forsenda að öll heildin séu skilgreind.)

Setning
~~~~~~~

Látum :math:`f` og :math:`g` vera föll sem eru heildanleg yfir bilið
:math:`[a,b]` og látum :math:`A` og :math:`B` vera fasta. Þá er

.. math:: \int_a^b Af(x)+Bg(x)\,dx=A\int_a^b f(x)\,dx+B\int_a^b g(x)\,dx.

Með öðrum orðum, heildun er línuleg aðgerð.

Setning
~~~~~~~

Látum :math:`f` vera fall sem er heildanlegt yfir bilið :math:`[a, b]`.
Gerum ráð fyrir að um öll :math:`x\in [a, b]` gildi að
:math:`f(x)\geq 0`. Þá er

.. math:: \int_a^b f(x)\,dx\geq 0.

Fylgisetning
~~~~~~~~~~~~

(i)  Látum :math:`f` og :math:`g` vera föll sem eru heildanleg yfir
     bilið :math:`[a, b]`. Gerum ráð fyrir að um öll :math:`x\in [a, b]`
     gildi að :math:`f(x)\leq g(x)`. Þá er

     .. math:: \int_a^b f(x)\,dx\leq \int_a^b g(x)\,dx.

(ii) Látum :math:`f` vera fall sem er heildanlegt yfir bilið
     :math:`[a, b]`. Ef :math:`m` og :math:`M` eru fastar þannig að um
     öll :math:`x\in [a, b]` gildir að :math:`m\leq f(x)\leq M` þá er

     .. math:: m(b-a)= \int_a^b m\,dx \leq  \int_a^b f(x)\,dx \leq \int_a^b M\,dx =M(b-a).

Setning
~~~~~~~

Látum :math:`f` vera fall sem er heildanlegt yfir bil :math:`[-a, a]`.

(i)  Ef fallið :math:`f` er oddstætt þá er

     .. math:: \int_{-a}^a f(x)\,dx=0.

(ii) Ef fallið :math:`f` er jafnstætt þá er

     .. math:: \int_{-a}^a f(x)\,dx=2\int_0^a f(x)\,dx.

.. index:: 
        fall; meðalgildi
     
Skilgreining
~~~~~~~~~~~~

Látum :math:`f` vera fall sem er heildanlegt yfir bilið :math:`[a, b]`.
:hover:`Meðalgildi,meðalgildi` fallsins :math:`f` á bilinu :math:`[a, b]` er skilgreint
sem

.. math:: \bar{f}=\frac{1}{b-a}\int_{a}^b f(x)\,dx.

.. index::
    milligildissetning; fyrir heildi

Setning: Meðalgildissetning fyrir heildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fallið :math:`f` sé **samfellt** á bilinu
:math:`[a, b]`. Þá er til punktur :math:`c` í bilinu :math:`[a, b]`
þannig að

.. math:: \int_a^b f(x)\,dx=(b-a)f(c).

Það er að segja, til er punktur :math:`c` í bilinu :math:`[a, b]` þannig
að :math:`f(c)=\bar{f}`.


Undirstöðusetning stærðfræðigreiningarinnar
-------------------------------------------

.. index:: 
    fall; skilgreint með heildi

Skilgreining og setning: Fall skilgreint með heildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera fall sem er heildanlegt yfir bil :math:`[a, b]`.
Fyrir :math:`x\in[a, b]` skilgreinum við :math:`F(x)=\int_a^x f(t)\,dt`.
Fallið :math:`F` er samfellt á :math:`[a, b]`.

.. warning::
    Athugið að :math:`t` er breytan sem er heildað með tilliti til, en
    :math:`x` er haldið föstu á meðan. :math:`t` hverfur svo þegar búið er
    að reikna heildið.

.. index::
    undirstöðusetning stærðfræðigreiningar, fyrri hluti
   
.. _undirstodusetning-fyrri:

Setning: Undirstöðusetning stærðfræðigreiningar, fyrri hluti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fallið :math:`f` sé samfellt á bili :math:`I` og
:math:`a` sé punktur í :math:`I`. Fyrir :math:`x` í :math:`I`
skilgreinum við :math:`F(x)=\int_a^x f(t)\,dt`. Þá er fallið :math:`F`
diffranlegt og

.. math:: F'(x)=f(x)

fyrir öll :math:`x\in I`.

.. index::
    stofnfall

Stofnföll
---------

Skilgreining: Stofnfall
~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera fall sem er skilgreint á bili :math:`I`. Fall
:math:`G` kallast :hover:`stofnfall` fyrir :math:`f` á
bilinu :math:`I` ef :math:`G'(x)=f(x)` fyrir öll :math:`x` í :math:`I`.

Fylgisetning
~~~~~~~~~~~~

Látum :math:`f` vera samfellt fall skilgreint á bili :math:`I`. Þá er
til stofnfall fyrir :math:`f` 
samkvæmt :ref:`fyrri hluta undirstöðustöðusetningarinnar <undirstodusetning-fyrri>`.

Hjálparsetning
~~~~~~~~~~~~~~

Ef :math:`F` og :math:`G` eru hvor tveggja stofnföll fyrir :math:`f` á
bilinu :math:`I`, þá er til fasti :math:`C` þannig að
:math:`F(x)=G(x)+C` fyrir öll :math:`x` í :math:`I`.

**Sönnun**: Þar sem

.. math:: \frac{d}{dx}(G(x) - F(x)) = G'(x) - F'(x) = f(x) - f(x) = 0

fyrir öll :math:`x\in I` þá er :math:`G(x)-F(x) = C` fasti.

.. index::
    undirstöðusetning stærðfræðigreiningar, seinni hluti


Setning: Undirstöðusetning stærðfræðigreiningar, seinni hluti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`f` er samfellt fall á bilinu :math:`I` og :math:`G` er
eitthvert stofnfall fyrir :math:`f` þá er

.. math:: \int_a^b f(t)\,dt=G(b)-G(a).

.. note::
    Það skiptir ekki máli hvaða stofnfall er valið í setningunni að ofan,
    heildið er alltaf það sama.

Ritháttur
~~~~~~~~~

Þegar :math:`F` er stofnfall fyrir :math:`f` þá ritum við

.. math:: \int_a^b f(x)\,dx=F(x)\,\bigg|_a^b= F(b)-F(a),

eða

.. math:: \int_a^b f(x)\,dx=\left[F(x)\right]_a^b= F(b)-F(a).

-------

Aðferðir við að reikna stofnföll
--------------------------------

Skilgreiningin á heildi með undir- og yfirsummum er gagnleg til að útskýra
og sanna eiginleika heilda en hún er ekki mjög góð til þess að reikna
heildi. Því er nauðsynlegt að koma sér upp tólum sem henta betur til þess.
Ef þau duga ekki þá þurfum við að grípa til tölulegra reikninga. 

Verkfærin
~~~~~~~~~

Helstu tæknilegu aðferðirnar við að finna stofnföll eru:

(i)   :hover:`Innsetning` / breytuskipti.

(ii)  :hover:`Hlutheildun`.

(iii) :hover:`Stofnbrotaliðun`.

Athugasemd
~~~~~~~~~~

Gerum ráð fyrir að :math:`F` sé stofnfall :math:`f`, þ.e.

.. math:: F(x)=\int f(t)\,dt.

Svo að

.. math:: F'(x)=f(x).

Látum nú :math:`g` vera fall og skoðum fallið :math:`F\circ g`. Þá fæst
samkvæmt :ref:`keðjureglunni <kedjuregla>` að

.. math:: \frac{d}{dx}F(g(x))=F'(g(x))g'(x) = f(g(x))g'(x),

eða, með því að heilda beggja vegna jafnaðarmerkisins,

.. math:: F(g(x))+C = \int f(g(x))g'(x)\,dx.

.. index::
    heildun; innsetning

Innsetning
~~~~~~~~~~

Ef við viljum reikna :math:`\int f(g(x))g'(x)\, dx` þá dugar okkur að
geta fundið :math:`\int f(x)\, dx`.

Notkun á innsetningu
~~~~~~~~~~~~~~~~~~~~

Setjum :math:`u=g(x)`. Þá er

.. math:: \frac{du}{dx}=g'(x)\qquad \text{eða} \qquad du=g'(x)\,dx.

Svo

.. math::

   \underbrace{\int f(g(x))g'(x)\,dx}_{\text{Viljum finna}}  = 
   \int f(u)\,du  
   =
   \underbrace{F(u)+C}_{\text{Getum reiknað}}  =
   \underbrace{F(g(x))+C}_{\text{Svarið}}.

.. warning::
    Ef við breytum heildi með tilliti til :math:`x` í heildi með tilliti til
    annarar breytistærðar :math:`u` þá verða **öll** :math:`x` að hverfa úr
    heildinu við breytinguna.

Notkun á innsetningu með mörkum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Með mörkum þá verður innsetningin svona

.. math::

   \begin{aligned}
     \int_a^b f(g(x))g'(x)\, dx  &=&
     \int_{x=a}^{x=b} f(u)\, du  = 
     [F(u)]_{x=a}^{x=b}    \\ &=& 
     [F(g(x))]_{x=a}^{x=b}     =
     F(g(b)) - F(g(a)).\end{aligned}

Ef :math:`A=g(a)` og :math:`B=g(b)` þá getum við eins skrifað þetta
svona

.. math::

   \begin{aligned}
   \int_a^b f(g(x))g'(x)\, dx  &=&
   \int_{x=a}^{x=b} f(u)\, du  = 
   \int_{A}^{B} f(u)\, du    \\ &=& 
   [F(u)]_A^B      = 
   F(B) - F(A).\end{aligned}

.. index::
    heildun; öfug innsetning
   
Öfug innsetning
~~~~~~~~~~~~~~~

Reiknum :math:`\int f(x)\, dx`, með því að finna hugsanlega flóknara
heildi sem við getum reiknað

.. math:: 
    \int f(g(u))g'(u)\, du.

.. warning:: 
    Athugið að hér þurfum við að finna heppilegt :math:`g`. Það
    er ekki alltaf augljóst hvaða :math:`g` er hægt að nota.

Notkun á öfugri innsetningu
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setjum :math:`x=g(u)`. Þá er

.. math:: \frac{dx}{du}=g'(u)\qquad\quad dx=g'(u)\,du.

Sem gefur að

.. math::

   \underbrace{\int f(x)\,dx}_{\text{Viljum finna}}  =
   \int f(g(u))g'(u)\,du 
   =
   \underbrace{F(u) + C}_{\text{Getum reiknað}}
   = \underbrace{F(g^{-1}(x)) + C}_{\text{Svarið}}.

Öfug innsetning með mörkum
~~~~~~~~~~~~~~~~~~~~~~~~~~

Við öfuga innsetningu þarf að passa að breyta mörkunum. Það er

.. math::

   \begin{aligned}
   \int_a^b f(x)\,dx    &= \int_{x=a}^{x=b} f(g(u))g'(u)\,du  \\ 
   &= [F(u)]_{x=a}^{x=b} = [F(g^{-1}(x))]_a^b = F(g^{-1}(b)) - F(g^{-1}(a)).\end{aligned}

Eða ef :math:`a=g(A)` og :math:`b=g(B)` (það er :math:`g^{-1}(a) = A` og
:math:`g^{-1}(b) = B`),

.. math:: \int_a^b f(x)\,dx  = \int_A^B f(g(u))g'(u)\,du= [F(u)]_A^B = F(B) - F(A).

.. index::
    heildun; hlutheildun

Hlutheildun
~~~~~~~~~~~

Munum að ef :math:`u` og :math:`v` eru föll þá er
:math:`(u\cdot v)' = u'\cdot v + u \cdot v'`.

Notum Undirstöðusetningu stærðfræðigreiningarinnar og heildum beggja
vegna jafnaðarmerkisins, þá fæst

.. math:: u(x)v(x) = \int (u(x)v(x))'\, dx = \int u'(x)v(x)\, dx + \int u(x)v'(x)\, dx.

Það er

.. math:: \int u'(x)v(x)\, dx = u(x)v(x) -  \int u(x)v'(x)\, dx.

Hlutheildun með mörkum
~~~~~~~~~~~~~~~~~~~~~~

Eða með mörkum

.. math:: \int_a^b u'(x)v(x)\, dx = [u(x)v(x)]_a^b -  \int_a^b u(x)v'(x)\, dx.

(Athugið að þá verða engin :math:`x` í svarinu.)

.. index::
    heildun; stofnbrotaliðun
    stofnbrotaliðun

Stofnbrotaliðun
~~~~~~~~~~~~~~~

Viljum heilda rætt fall :math:`\frac{P(x)}{Q(x)}` þar sem :math:`P(x)`
og :math:`Q(x)` eru margliður. Stofnbrotaliðun gengur út á það að skrifa ræða fallið
:math:`\frac{P(x)}{Q(x)}` sem summu af liðum á forminu

.. math:: \frac{1}{ax+b}, \quad \frac{x}{x^2+bx+c} \quad\text{ og }\quad \frac{1}{x^2+bx+c},

því svona liði getum við heildað hvern fyrir sig.

Nánar er fjallað um stofnbrotaliðun í kafla 6.2 í kennslubókinni.

.. todo::
    bæta við stofnbrotaliðun
    
.. index::
    heildi; óeiginleg
    
Óeiginleg heildi
----------------

Skilgreining: Óeiginleg heildi I
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera samfellt fall á bilinu :math:`[a, \infty)`.
Skilgreinum

.. math:: \int_a^\infty f(x)\,dx=\lim_{R\rightarrow\infty} \int_a^R f(x)\,dx.

Fyrir fall :math:`f` sem er samfellt á bili :math:`(-\infty, b]`
skilgreinum við

.. math:: \int_{-\infty}^b f(x)\,dx=\lim_{R\rightarrow-\infty} \int_R^b f(x)\,dx.

Heildi eins og þau hér að ofan kallast :hover:`óeiginlegt heildi`.

Í báðum tilvikum segjum við að óeiginlega heildið sé samleitið ef
markgildið er til, en ósamleitið ef markgildið er ekki til.

.. warning::
      Ef :math:`f` stefnir ekki á 0 þegar :math:`x\to \infty` þá
      er heildið ekki samleitið. En jafnvel þó fallið stefni á 
      0 þá er ekki víst að heildið sé samleitið, samanber
      eftirfarandi dæmi.
      
Dæmi
~~~~

Heildið :math:`\int_1^\infty \frac{1}{x^p}\,dx` er samleitið ef
:math:`p>1` en ósamleitið ef :math:`p\leq 1`.

Ef :math:`p>1` þá er

.. math:: \int_1^\infty \frac{1}{x^p}\,dx=\frac{1}{p-1}.

Skilgreining: Óeiginleg heildi I, framhald
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera fall sem er samfellt á öllum rauntalnaásnum.

Heildi af gerðinni :math:`\int_{-\infty}^\infty f(x)\,dx` er sagt
samleitið ef bæði heildin :math:`\int_{-\infty}^0 f(x)\,dx` og
:math:`\int_0^\infty f(x)\,dx` eru samleitin og þá er

.. math::

   \int_{-\infty}^\infty f(x)\,dx=\int_{-\infty}^0 f(x)\,dx +
     \int_0^\infty f(x)\,dx.

.. note::
    Það skiptir ekki máli í hvaða punkti heildinu er skipt í tvennt, það má
    velja aðra tölu heldur en 0, útkoman verður alltaf sú sama.

Skilgreining: Óeiginleg heildi II
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera samfellt fall á bilinu :math:`(a, b]` og hugsanlega
ótakmarkað í grennd við :math:`a`. Skilgreinum

.. math:: \int_a^b f(x)\,dx=\lim_{c\rightarrow a^+} \int_c^b f(x)\,dx.

Fyrir fall :math:`f` sem er samfellt á bili :math:`[a, b)` og hugsanlega
ótakmarkað í grennd við :math:`b` þá skilgreinum við

.. math:: \int_a^b f(x)\,dx=\lim_{c\rightarrow b^-} \int_a^c f(x)\,dx.

Í báðum tilvikum segjum við að óeiginlega heildið sé samleitið ef
markgildið er til en ósamleitið ef markgildið er ekki til.

Dæmi
~~~~

Heildið :math:`\int_0^1 \frac{1}{x^p}\,dx` er samleitið ef :math:`p<1`
en ósamleitið ef :math:`p\geq 1`. Ef :math:`p<1` þá er

.. math::

   \int_0^1
   \frac{1}{x^p}\,dx=\frac{1}{1-p}.

Skilgreining
~~~~~~~~~~~~

Látum :math:`f` vera samfellt fall á bili :math:`(a,\infty)` og
ótakmarkað í grennd við :math:`a`. Látum :math:`c` vera einhverja tölu
þannig að :math:`a<c<\infty`.

Heildið :math:`\int_a^\infty f(x)\,dx` er sagt vera samleitið ef bæði
heildin :math:`\int_a^c f(x)\,dx` og :math:`\int_c^\infty f(x)\,dx` eru
samleitin og þá er

.. math:: \int_{a}^\infty f(x)\,dx=\int_{a}^c f(x)\,dx + \int_c^\infty f(x)\,dx.

.. note::
    Það er sama hvað tala :math:`c` er valin hér að ofan, útkoman verður
    alltaf sú sama.

.. ggb:: 1430547
    :width: 700
    :height: 300
    :img: 07_samleitidheildi.png
    :imgwidth: 12cm
    
Setning
~~~~~~~

Látum :math:`-\infty\leq a<b\leq \infty`. Gerum ráð fyrir að föllin
:math:`f` og :math:`g` séu samfelld á :math:`(a, b)` og að um öll
:math:`x\in (a, b)` gildi að :math:`0\leq f(x)\leq g(x)`.

(i)  Ef heildið :math:`\int_a^b g(x)\,dx` er samleitið þá er heildið
     :math:`\int_a^b f(x)\,dx` líka samleitið og

     .. math:: \int_a^b f(x)\,dx \leq \int_a^b g(x)\,dx.

(ii) Ef heildið :math:`\int_a^b f(x)\,dx` er ósamleitið þá er heildið
     :math:`\int_a^b g(x)\,dx` líka ósamleitið.
