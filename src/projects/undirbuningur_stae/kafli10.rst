Markgildi
=========

Markgildi falls
---------------

Áður en að við skilgreinum :hover:`markgildi` :hover:`falls, fall` formlega skulum við taka dæmi til að útskýra hver hugmyndin er.
Skilgreinum fall:

.. math::
	g:\;\mathbb{R}\setminus\{0\}\to \mathbb{R}, \qquad g(x)=\frac{\sin(x)}{x}.

Tökum eftir að við látum fallið :math:`g` ekki vera skilgreint í punktinum :math:`x=0`  til að komast hjá því að deila með núlli.

Það getur hins vegar verið áhugavert að skoða hvernig fallið hagar sér **nálægt** punktinum :math:`x=0`.
Teiknum mynd af fallinu :math:`g`:

.. figure:: ./myndir/markgildi/sin.svg
	:align: center
	:width: 60%

Við notum vasareikni til að reikna nokkur gildi á :math:`g` og merkjum inn í :hover:`hnitakerfið, hnitakerfi` punktana :math:`(x,g(x))`.
Athugum að fallið er :hover:`jafnstætt, jafnstæður` svo :math:`g(-x)=g(x)` fyrir öll :math:`x`.

.. math::
    \begin{aligned}
        g(-1) &=g(1) \approx 0,841470984 \\
        g(-0,5) &=g(0,5)\approx 0,958851077\\
        g(-0,25) &=g(0,25)\approx 0,989615837 \\
        g(-0,1) &=g(0,1)\approx 0,998334166 \\
        g(-0,001) &= g(0,001) \approx 0,9999833
    \end{aligned}


Takið sérstaklega eftir því að fallið virðist ekki fara upp eða niður í óendanleikann þegar við nálgumst gildið :math:`x=0`.
Öllu heldur þá virðist fallið stefna á gildið :math:`1`!

Við höfum séð að ef :math:`x_0` er tala sem er mjög nálægt núlli þá verður fallgildið :math:`g(x_0)` mjög nálægt því að verða :math:`1`.

Munum að fallið :math:`g` er **ekki skilgreint í núlli**, hins vegar höfum við sér orðalag fyrir svona tilvik.
Við segjum að :hover:`markgildi` fallsins :math:`g` í núlli sé einn.
Einnig má segja að :math:`g(x)` stefni á einn þegar :math:`x` stefnir á núll.
Á táknmáli er skrifað

.. math::
	\lim_{x\to 0}g(x)=1.

Þetta er hægt að gera almennt.

Látum nú :math:`a` vera stak í :hover:`bilinu, bil` :math:`I` í :math:`\mathbb{R}`.
Látum :math:`f:\;I\setminus\{a\}\to \mathbb{R}` vera eitthvað fall og :math:`b\in \mathbb{R}` vera tölu.
Við segjum að markgildi fallsins :math:`f` í punktinum :math:`x=a` sé :math:`b` ef fyrir allar tölur :math:`x_0` sem eru nálægt tölunni :math:`a` þá er talan :math:`f(x_0)` nálægt tölunni :math:`b`.
Þá skrifum við

.. math::
	\lim_{x\to a}f(x)=b.

Setjum fram skilgreininguna á markgildi.

Skilgreining
~~~~~~~~~~~~
Gerum ráð fyrir að :math:`I\subset \mathbb{R}` sé bil í :math:`\mathbb{R}` og að :math:`a\in I` sé punktur á bilinu sem er hvorugur endapunkta þess.

Gerum ráð fyrir að :math:`f:\; I\setminus\{a\}\to \mathbb{R}` sé fall og að :math:`b\in \mathbb{R}` sé tala.

Við segjum að markgildi fallsins :math:`f` í punktinum :math:`a` sé :math:`b` og ritum

.. math::
	\lim_{x\to a}f(x)=b

ef að eftirfarandi gildir:

Fyrir sérhvert :math:`\epsilon>0` er til :math:`\delta>0` þannig að
ef

.. math::
	|x-a|<\delta,

þá er

.. math::
	0<|f(x)-b|<\epsilon.

.. note::
  Í þessari skilgreiningu má ímynda sér að :math:`\epsilon` og :math:`\delta` séu rosalega litlar tölur.

  Ójafnan :math:`|x-a|<\delta` þýðir þá að :math:`x` sé rosalega nálægt því að vera :math:`a` og ójafnan :math:`0<|f(x)-b|<\epsilon` þýðir að :math:`f(x)` er rosalega nálægt því að vera :math:`b`.

  Athugum að :math:`a` og :math:`b` geta verið hvaða tölur sem er, jafnvel :math:`\pm \infty`.

.. warning::
	 Við segjum að markgildi fallsins **sé til** ef fallið stefnir á rauntölu.

	 Ef fall stefnir á :math:`+ \infty` eða :math:`-\infty` segjum við að markgildið **sé ekki til** .

---------------

Skoðum ræða fallið :math:`f(x) = \frac{x}{x-1}` .

.. figure:: ./myndir/markgildi/hv.svg
	:align: center
	:width: 70%

Hvert er markgildi :math:`f` þegar :math:`x` stefnir á 1?

Þegar við skoðum bláa grafið vinstra megin við vandræðapunktinn tekur fallið snögga dýfu niður í :math:`-\infty` þegar það nálgast 1.
Þetta köllum við að skoða *vinstra markgildi* og táknum með litlum mínus í hávísi.
Í þessu tilviki myndum við skrifa:

.. math::
	\lim_{x \to 1^{-}} \frac{x}{x-1} = -\infty

Hins vegar, þegar við eltum rauða ferilinn hægra megin við vandræðapunktinn stefnir fallið hratt upp í :math:`+\infty` þegar það nálgast 1.
Þetta köllum við *hægra markgildi* og táknum með litlum plús í hávísi.
Í þessu tilviki myndum við skrifa:

.. math::
	\lim_{x \to 1^{+}} \frac{x}{x-1} = \infty

.. note::
	Þegar hægra markgildi og vinstra markigildi falls í punkti er ekki það sama þá er *markgildið ekki til*.

	Markgildi :math:`f(x)` í punktinum :math:`x=a` er ekki til nema ef

	.. math::
		\lim_{x\to a^+} f(x) = \lim_{x\to a^-} f(x)


.. warning::
  Skoðum myndræn dæmi þar sem markgildið er **ekki til**.

  .. figure:: ./myndir/markgildi/markg.svg
  	:align: center

  Hér er fallið ekki að stefna á eitt gildi í punktinum :math:`a`, því það er ekki að stefna á sama gildi hægra megin og vinstra megin. Markgildið er því ekki til.

  .. figure:: ./myndir/markgildi/markg2.svg
  	:align: center

  Hér stefnir fallið á :math:`\infty` í punktinum :math:`a` og því er markgildið ekki til.

Ef við höfum markgildið :math:`\lim_{x \to c} f(x)` þar sem fallið er rætt, það er að segja á forminu :math:`f(x) = \frac{p(x)}{q(x)}`, þá þarf að passa að :math:`q(c) \neq 0`. Þá verða markgildisreikningarnir einfaldir, sjá dæmi 1 og 2.

.. tip::
	Finnið markgildin:

	**1.**
	 :math:`\lim_{x\to 2}\frac{x^3+2x^2}{x^3-x^2+1}`.

	 Hér er :math:`q(x)=x^3-x^2+1`
	 og :math:`q(2)=2^3-2^2+1=5\not=0`

	 Hér er :math:`2` í skilgreiningarmenginu svo til þess að reikna markgildið er gildinu einfaldlega stungið inn.
	 Markgildið er því:

	 .. math::
	 	\lim_{x\to 2}\frac{x^3+2x^2}{x^3-x^2+1}=\frac{2^3+2\cdot 2^2}{2^3-2^2+1}=\frac{16}{5}

	**2.**
	 :math:`\lim_{x\to 4}\frac{x^3-4x^2-4x+16}{x^2-16}` .

	 Hér er :math:`q(x)=x^2-16` og :math:`p(x)=x^3-4x^2-4x+16` .

	 Við tökum eftir að :math:`q(4)=0` og :math:`p(4)=0`.

	 Prófum að stytta út þætti.
	 Við getum umritað :math:`p(x) = (x-2)(x+2)(x-4)` og :math:`q(x)=(x-4)(x+4)`
	 og sjáum að :math:`(x-4)` er sameiginlegur þáttur sem styttist út.

	 Fáum því markgildið:

	 .. math::
		 \begin{aligned}
		  \lim_{x\to 4}\frac{x^3-4x^2-4x+16}{x^2-16} &= \lim_{x\to 4} \frac{(x-2)(x+2)(x-4)}{(x-4)(x+4)} \\
			&=\lim_{x\to 4}\frac{(x-2)(x+2)}{(x+4)}\\
		  &=\frac{(4-2)(4+2)}{4+4}\\
		  &=\frac{12}{8}\\
		  &=\frac{3}{2}
		 \end{aligned}

	**3.**
	 Látum :math:`f: \mathbb{R} \setminus \{1\} \to \mathbb{R} \qquad f(x)=x`.

	 Sýnið að :math:`\lim_{x \to 1} f(x) = 1` .

	 Þetta verður nánast augljóst ef grafið er teiknað.
	 Hér setjum við lítinn hring í punktinn :math:`(1, 1)` því fallið er ekki skilgreint þar.

	 .. figure:: ./myndir/markgildi/mkgexmp1.svg
	 	:align: center
		:width: 70%

	 Það er því ljóst að fallið stefnir á punktinn :math:`(1, 1)` frá báðum áttum.

	**4.**
	 Látum :math:`f : \mathbb{R} \setminus \{4\} \to \mathbb{R} \qquad f(x) = \sqrt{x}`.
	 Sýnið að :math:`\lim_{x \to 4} = 2`.

	 Aftur er nánast augljóst hvert markgildið er.
	 Ef ferill fallsins :math:`f` er teiknaður upp sést greinilega að hann stefnir á punktinn :math:`(4, 2)`.
	 Það er að segja, það sést að markgildi fallsins er tveir.

	 .. figure:: ./myndir/markgildi/mkgexmp.svg
	 	:align: center
		:width: 70%

	 Við skulum sýna þetta formlega.
	 Látum :math:`\epsilon > 0` vera einhverja gefna tölu.
	 Sýna þarf að til sé :math:`\delta>0` þannig að :math:`|x−4|<\delta` hafi í för með sér að :math:`| x−2|<\epsilon`. Látum :math:`\delta = 2 \cdot \epsilon`.
	 Þá fæst að ef :math:`|x − 4| < \delta` þá er

   .. math::
      \begin{aligned}
      |f(x) - 2| &= |\sqrt{x} - 2|,\\
      & = \frac{|\sqrt{x} - 2||\sqrt{x} + 2|}{|\sqrt{x} + 2|},\\
      & = \frac{|x - 4|}{|\sqrt{x} + 2|},\\
      & \leqq \frac{|x-4|}{|2|} \leqq \frac{\delta}{2} = \epsilon.
      \end{aligned}




Gerðir markgilda
----------------

Hér er samantekt af helstu gerðum markgilda:

1. :math:`\quad \lim_{x \to a} f(x) \qquad \qquad \quad` markgildið af :math:`f(x)` þegar :math:`x`  stefnir á  :math:`a`

2. :math:`\quad \lim_{x \to a+} f(x) \qquad\qquad\;` markgildið af :math:`f(x)` þegar :math:`x`  stefnir á :math:`a` frá hægri

3. :math:`\quad \lim_{x \to a-} f(x) \qquad \qquad \;` markgildið af :math:`f(x)` þegar :math:`x` stefnir á :math:`a` frá vinstri

4. :math:`\quad \lim_{x\to +\infty} f(x) \qquad \qquad` markgildið af :math:`f(x)` þegar :math:`x`  stefnir á plús óendanlegt

5. :math:`\quad \lim_{x\to -\infty} f(x) \qquad \qquad` markgildið af :math:`f(x)` þegar :math:`x` stefnir á mínus óendanlegt


---------------------

Skoðum markgildið :math:`\lim_{x \to \infty}\frac{1}{x^n}` fyrir öll :math:`n \in \mathbb{N}_+`

Byrjum á :math:`n=1`, þá er augljóst að

.. math::
	\lim_{x \to \infty}\frac{1}{x} = 0

því ef :math:`x` er stórt þá er :math:`\frac{1}{x}` lítið.
Því er :math:`\frac{1}{x}` að minnka þegar :math:`x` er að stækka.

Ef :math:`n=2` þá er líka augljóst að

.. math::
	\lim_{x \to \infty}\frac{1}{x^2} = \lim_{x \to \infty}\left(\frac{1}{x}\right)^2 = 0

vegna þess að

.. math::
	\begin{aligned}
	x&\leq x^2 \quad & \forall x \geq 1\\
	\frac{1}{x^2} &\leq \frac{1}{x} \quad &\forall x \geq 1 \end{aligned}

Þegar við hækkum veldið á :math:`x` í nefnaranum þá minnkar :math:`\frac{1}{x}` hraðar, því :math:`x` er að stækka hraðar.

Við sjáum því að :math:`\frac{1}{x^n}` stefnir á núll þegar :math:`x` stefnir á :math:`\infty` fyrir allar jákvæðar heiltölur tölur :math:`n`.

.. math::
	\lim_{x \to \infty} \frac{1}{x^n} = 0 \qquad \forall n \in \mathbb{Z}_+


.. figure:: ./myndir/markgildi/xminusn.svg
	:align: center
	:width: 40%

------------------

En hvað með markgildið :math:`\lim_{x\to 0^+} \frac{1}{x^n}` ?

Þegar við nálgumst núll ofan frá erum við að deila með sífellt minni tölu. Þá fáum við sífellt stærri tölu út:

.. math::
	\begin{aligned}
	&\frac{1}{2} <\frac{1}{1}<\frac{1}{0.5} <\frac{1}{0.1} <\frac{1}{0.001}\\
	&0.5<1<2<10 < 1000
	\end{aligned}

Því hlýtur

.. math::
	\lim_{x\to 0^+} \frac{1}{x^n} = \infty


------------------

Skoðum nokkur dæmi:

.. tip::

    Finnið eftirfarandi markgildi:

    *Hér munum við láta rökstuðning duga í staðinn fyrir að nota formlegu skilgreiningarnar.*


    **1.** :math:`\lim_{x\to 0}\frac{1}{(2^x-1)^2}`

     Þegar :math:`x` stefnir á núll þá stefnir :math:`(2^x-1)^2` á núll (því :math:`2^0=1`) svo að
     :math:`\frac{1}{(2^x-1)^2}` stefnir annað hvort á plús eða mínus óendanlegt. Þar sem  :math:`\frac{1}{(2^x-1)^2}=\left(\frac{1}{2^x-1}\right)^2` er stæða í öðru veldi þá er hún alltaf jákvæð. Hún hlýtur því að stefna á plús óendanlegt, við skrifum

     .. math::
        \lim_{x\to 0}\frac{1}{(2^x-1)^2}=\infty.

     .. figure:: ./myndir/markgildi/daemi2.svg
        :align: center
        :width: 40%

     Sjáum út frá mynd að fallið stefnir á plús óendalegu þegar :math:`x` stefnir á :math:`0` frá báðum áttum.


    **2.** :math:`\lim_{x\to \frac{\pi}{2}^-}\frac{1}{\cos(x)}`

     Þegar :math:`x` stefnir á :math:`\pi/2` þá stefnir :math:`\cos(x)` á núll svo :math:`\frac{1}{\cos(x)}` stefnir á plús eða mínus óendanlegt.
     Þekkt er að :math:`\cos(x)` er jákvætt ef :math:`0<x<\pi/2`. Stæðan :math:`\frac{1}{\cos(x)}` er þess vegna jákvæð á sama bili og þess vegna stefnir hún á plús óendanlegt ef :math:`x` nálgast :math:`\pi/2` frá vinstri.
     Við skrifum

     .. math::
         \lim_{x\to \frac{\pi}{2}^{-}}\frac{1}{\cos(x)}=\infty.

     .. figure:: ./myndir/markgildi/daemi3.svg
        :align: center
        :width: 100%

     Hér er fallið með :hover:`aðfellu, aðfella` í :math:`\frac{\pi}{2}` sem þýðir að fallið tekur ekki gildi í :math:`\frac{\pi}{2}` en við sjáum að fallið er að stefna á plús óendanlegt frá vinstri.


Reikniaðgerðir á markgildum
---------------------------

Þegar  markgildi eru reiknuð gilda reiknireglur sem ættu ekki að koma á óvart.

Gerum ráð fyrir að :math:`f` og :math:`g` séu föll og að :math:`c\in \mathbb{R} \cup\{-\infty,\infty\}`
Gerum ráð fyrir að bæði markgildin

.. math::
    \lim_{x\to c}f(x)\qquad \text{og}\qquad \lim_{x\to c}g(x)


séu skilgreind og að hvorugt þeirra sé jafnt plús eða mínus óendanlegu.
Gerum ráð fyrir að :math:`k\in\mathbb{R}` sé fasti.
Þá gildir:

.. math::
    \begin{aligned}
    1. & \qquad \lim_{x\to c}k=k \\
    \quad\\
    2. & \qquad \lim_{x\to c} \left(kf(x) \right)=k \cdot \left(\lim_{x\to c}f(x)\right) \\
    \quad\\
    3. & \qquad \lim_{x\to c} \left(f(x)+g(x)\right)=\lim_{x\to c}f(x)+\lim_{x\to c}g(x) \\
    \quad\\
    4. & \qquad \lim_{x\to c} \left(f(x)-g(x)\right)=\lim_{x\to c}f(x)-\lim_{x\to c}g(x) \\
    \quad\\
    5. & \qquad \lim_{x\to c} \left(f(x)\cdot g(x)\right)= \left( \lim_{x\to c}f(x) \right)\cdot \left(\lim_{x\to c}g(x) \right) \\
    \quad\\
    6. & \qquad \lim_{x\to c} \left( \frac{f(x)}{g(x)} \right)=\frac{\lim_{x\to c}f(x)}{\lim_{x\to c}g(x)} \qquad \text{ef} \qquad \lim_{x\to c}g(x)\not=0
    \end{aligned}

.. tip::
	Finnið eftirfarandi markgildið ef það er til.

 	.. math::
		\lim_{x \to \infty} \frac{x^2 + 1}{2x^2 + 5x +1}

	Við byrjum á því að deila með :math:`x^2` fyrir ofan og neðan strik. Við notum svo reiknireglurnar fyrir afganginn og þá staðreynd að :math:`\frac{1}{x^n}` stefnir á núll þegar :math:`x` stefnir á :math:`\infty` fyrir allar náttúrulegar tölur :math:`n`.

	.. math::
		\begin{aligned}
		\lim_{x \to \infty} \frac{x^2 + 1}{2x^2 + 5x +1}
		&= \lim_{x \to \infty} \frac{1 + \frac{1}{x^2}}{2 + \frac{5}{x} + \frac{1}{x^2}} \\
		&= \frac{\lim_{x \to \infty}( 1 + \frac{1}{x^2})}{\lim_{x \to \infty}( 2 + \frac{5}{x} + \frac{1}{x^2})} \\
		&=\frac{\lim_{x \to \infty}1+\lim_{x \to \infty} \frac{1}{x^2}}{\lim_{x \to \infty}2+\lim_{x \to \infty} \frac{5}{x} +\lim_{x \to \infty} \frac{1}{x^2}} \\
		&=\frac{1+0}{2+0+0}\\
		&=\frac{1}{2}
		\end{aligned}

.. tip::
  Finnið markgildið:

	.. math::
		\lim_{x\to \infty}\frac{(\sin(x))^2}{x}.

	Auðvelt er að sjá að fallið :math:`\frac{1}{x}` stefnir á núll þegar :math:`x` stefnir á óendanlegt.
	Þekkt er að :math:`|\sin(x)|\leq 1` fyrir öll :math:`x` og því fæst að :math:`0\leq (\sin(x))^2 \leq 1` fyrir öll :math:`x`.
	Þegar :math:`x` er stórt er því :math:`\frac{1}{x}` nálægt núlli og :math:`(\sin(x))^2` er á milli núll og einn.
	En þá er auðvelt að sjá að

	.. math::
		\frac{(\sin(x))^2}{x}=(\sin(x))^2\frac{1}{x}

  er nálægt núlli svo að markgildið er núll. Hér notuðum við reiknireglu 5.

  Við skrifum:

  .. math::
		\lim_{x\to\infty}\frac{(\sin(x))^2}{x}=0.

  .. figure:: ./myndir/markgildi/daemi1.svg
      :align: center
      :width: 100%

  Sjáum á grafinu að þegar við förum lengra eftir :math:`x`-ás nálgast fallið :math:`0`.

.. tip::
	Finnið markgildið:

	.. math::
		\lim_{x\to \infty} \frac{x}{2x+1}

	Þegar :math:`x` stefnir á stærri og stærri tölur byrjar :math:`1` að skipta minna máli því hann er mikið minni í samanburði við það sem :math:`x` stefnir á. Þá erum við komin með einfaldara markgildi til að skoða:

	.. math::
		\lim_{x\to \infty} \frac{x}{2x}

	Hér getum við stytt út :math:`x`-in og fáum að

	.. math::
		\lim_{x\to \infty} \frac{1}{2} = \frac{1}{2}

	.. image:: ./myndir/markgildi/tutor.svg
		:align: center




Samfelld föll
-------------

Óformlega má segja að fall :math:`f` sé :hover:`samfellt` ef að hægt er að teikna feril þess á blað með blýanti án þess að þurfa að lyfta blýantinum. Ef að fall er ekki samfellt segjum við að það sé :hover:`ósamfellt`.
Ef að fall :math:`f` er ósamfellt þá segjum við að það sé ósamfellt í þeim punktum þar sem lyfta þarf blýantinum af blaðinu.

.. figure:: ./myndir/markgildi/samfell.svg
	:align: center

Fallið að ofan er **ósamfellt**.

.. figure:: ./myndir/markgildi/samfell2.svg
	:align: center

Fallið að ofan er **samfellt**.

Skilgreinum nú samfelldni:

Skilgreining
~~~~~~~~~~~~
Látum :math:`f` vera fall. Ef :math:`f` hefur markgildi í :math:`a` og :math:`\lim_{x \to a} f(x)=f(a)` þá segjum við að :math:`f` sé *samfellt* í punktinum :math:`a`.

Ef :math:`f` er samfellt á öllu :hover:`skilgreiningarmengi` sínu köllum við :math:`f` *samfellt fall*.

Reglur um samfelldni
~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` og :math:`g` vera raunföll á bili :math:`I` og samfelld í punktinum :math:`a \in I`, þá gildir:

1. Fallið :math:`f+g` er samfellt í :math:`a`.
2. Fallið :math:`f \cdot g` er samfellt í :math:`a`.
3. Fallið :math:`\frac{f}{g}` er samfellt í :math:`a` ef :math:`g(a) \neq 0`.
4. Gerum ráð fyrir að fallið :math:`g` sé samfellt í :math:`f(a)`. Þá er :math:`(g \circ f)(x)=g(f(x))` samfellt í :math:`a`.

Nokkur þekkt samfelld föll
~~~~~~~~~~~~~~~~~~~~~~~~~~

Áður en við skoðum dæmi þá skulum við telja upp nokkur samfelld föll sem við þekkjum:

1. Fallið :math:`f(x)=x` er samfellt.
2. Sérhver margliða er samfelld.
3. Sérhvert rætt fall er samfellt á skilgreiningarmengi sínu (þ.e. þar sem nefnarinn er ekki núll).
4. Fyrir allar náttúrlegar tölur :math:`n` þá er fallið :math:`f(x)=\root n \of {x}` samfellt.
5. Ef :math:`r \in \mathbb{R}` er rauntala þá er fallið :math:`f(x)=x^r` samfellt.
6. Vísisföll eru samfelld.
7. Lograr eru samfelldir.
8. Hornaföllin eru samfelld.
9. Fallið :math:`f(x)=|x|` er samfellt.

.. tip::
	Segjum til um hvort föllin eru samfelld eða ekki.

	**1.**

	 .. math::
		 f(x)=|x|+\cos(x^3)

	 Fallið :math:`f` er samsett úr föllunum :math:`|x|`, :math:`\cos(x)` og :math:`x^3` sem eru öll samfelld föll. Þess vegna er :math:`f` samfellt.

	**2.**

	 .. math::
		 g(x) =
		\begin{cases}
			\hfill -1    \hfill & \text{ ef } x\leq 0,\\
			\hfill  1 \hfill & \text{ ef } x>0.\\
		\end{cases}

	 Í punktinum :math:`x=0` tekur fallið :math:`g` stökk frá því að vera jafnt mínus einum í það að vera jafnt einum. Fallið er þess vegna ósamfellt í þeim punkti.

	**3.**

		.. math::
			h(x) =
			\begin{cases}
				\hfill \sin(x)    \hfill & \text{ ef } x\leq 0,\\
				\hfill  x^2 \hfill & \text{ ef } x>0.\\
			\end{cases}


		Föllin :math:`\sin(x)` og :math:`x^2` eru bæði samfelld. Fallið :math:`h` er því samfellt í öllum punktum nema kannski núllpunktinum.
		Nú er þekkt að :math:`0^2=0` og :math:`\sin(0)=0`.
		Fallið :math:`h` stefnir þá á töluna núll í :math:`x=0` hvort sem að við nálgumst punktinn hægra eða vinstra megin frá. Fallið :math:`h` er þvi samfellt í núllpunktinum, og við höfum þá rökstutt að það er samfellt allstaðar.
