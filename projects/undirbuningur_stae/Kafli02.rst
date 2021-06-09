Jöfnur og ójöfnur
=================

.. panopto:: 8d8a65f8-66dd-4d9b-980d-475e439fc0bd
    :width: 100%
    :height: 405

--------------------------------------------------------------------

Jöfnur
------
.. _s.jofnur:

:hover:`Jafna` lýsir sambandi milli stæða.
Jafnaðarmerkið :math:`=` merkir að stæðurnar sem standa beggja vegna jafnaðarmerkisins séu sama talan.
Til dæmis, ef við höfum jöfnuna :math:`x+2=4` sjáum við að jafnan gengur upp ef :math:`x=2` .

Við megum beita reikniaðgerðum þegar við vinnum með jöfnur, svo lengi sem við **gerum það sama báðum megin jafnaðarmerkis**.

Byrjum á því að skoða jöfnur af einni breytistærð. :hover:`Stig` stæðu er jafnt hæsta veldi :hover:`breytistærðarinnar, breytistærð`. Þá er :math:`x+2=0` fyrsta stigs jafna, :math:`x^2+2x+1=0` er annars stigs jafna, :math:`x^3+2x^2+3x=0` er þriðja stigs jafna og svo framvegis.

Fyrsta stigs jöfnur
~~~~~~~~~~~~~~~~~~~

*Fyrsta stigs jafna* hefur almennt form

.. math::
	ax+b=0

þar sem :math:`a \neq 0` og :math:`b` eru tölur. Jafnan hefur eina lausn, sem fæst með því að draga :math:`b` frá báðum megin við jafnaðarmerkið og deila svo með :math:`a`. Við köllum þetta að *einangra* :math:`x`. Lausnin er því :math:`x=\frac{-b}{a}`.

.. note::
	Fyrsta stigs jafna er ekki alltaf á forminu :math:`ax+b=0`, en við getum alltaf komið henni yfir á það form með reikniaðgerðum. Til dæmis er :math:`5x=-2` ekki á þessu formi en við getum lagt :math:`2` við báðum megin og fengið :math:`5x+2=0`.

.. tip::
	**1.** Leysum :math:`2x+3=0`. Drögum :math:`3` frá báðum megin og fáum :math:`2x=-3`. Deilum með :math:`2` og fáum :math:`x=-\frac{3}{2}`.

	**2.** Leysum :math:`17x=5`. Til þess að einangra :math:`x` þurfum við nú bara að deila í gegn með :math:`17`. Fáum þá :math:`x=\frac{5}{17}`.

Annars stigs jöfnur
~~~~~~~~~~~~~~~~~~~
.. _s.annars stigs jöfnur:

:hover:`Annars stigs jafna` hefur almennt form

.. math::
	ax^2+bx+c=0

þar sem :math:`a`, :math:`b` og :math:`c` eru :hover:`fastar, fasti`.

.. warning::
	Athugið b og c geta verið hvaða tölur sem er, en :math:`a \neq 0` því annars væri jafnan fyrsta stigs jafna.

Annars stigs jafna er ekki alltaf á almennu formi, en við getum komið henni á almennt form með reikniaðgerðum.

.. tip::
	**1.** Jafnan :math:`x^2+3x=4x+1` er ekki á almennu formi, en með því að beita reikniaðgerðum og ,,færa yfir jafnaðarmerkið'' fæst :math:`x^2-x+1=0`.
	Við sjáum því að þetta er annars stigs jafna með :math:`a=1`, :math:`b=-1` og :math:`c=1`.

	**2.** Jafnan :math:`2x(3-x)=2x` er ekki á almennu formi. Ef við margföldum upp úr sviganum fæst :math:`6x-2x^2=2x`, sem er jafngilt :math:`4x-2x^2=0`.
	Við getum víxlað röðinni og fengið :math:`-2x^2+4x=0` og þá er auðvelt að sjá að þetta er annars stigs jafna með :math:`a=-2`, :math:`b=4` og :math:`c=0`.

	**3.** Jafnan :math:`x^2+3x=x^2-4` er ekki á almennu formi. Með því að ,,færa yfir jafnaðarmerkið'' fæst :math:`x^2+3x-x^2+4=0` eða :math:`3x+4=0`.
	Við sjáum því að þetta er ekki annars stigs jafna, heldur fyrsta stigs.

Lausnarformúla fyrir annars stigs jöfnur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við höfum lausnarformúlu fyrir annars stigs jöfnur á almennu formi. Þær geta haft eina, tvær eða enga lausn.

Setning
```````
Látum :math:`ax^2+bx+c=0` vera annars stigs jöfnu. :hover:`Aðgreinirinn, aðgreinir` er :math:`d = b^2-4ac`.

1. Ef :math:`d = b^2-4ac<0` þá hefur jafnan enga rauntölulausn.
2. Ef :math:`d  = b^2-4ac=0` þá hefur jafnan eina lausn:

.. math::
	x=\frac{-b}{2a}

3. Ef :math:`d = b^2-4ac>0` þá hefur jafnan tvær lausnir:

.. math::
	x_1=\frac{-b+\sqrt{b^2-4ac}}{2a} \qquad \text{og} \qquad x_2=\frac{-b-\sqrt{b^2-4ac}}{2a}

.. note::
	Oft er almenna formúlan rituð

	.. math::
		x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}

.. warning::
	Áður en við notum þessa lausnarformúlu þurfum við að vera viss um að jafnan sé á almenna forminu :math:`ax^2+bx+c=0`.

.. tip::
 **1.** Leysum jöfnuna :math:`2x^2 + 3x - 5 = 2`.

  Við byrjum á að koma jöfnunni á almennt form með því að draga 2 frá beggja vegna jafnaðarmerkis, fáum :math:`2x^2 + 3x - 7=0`.
  Sjáum því að hér er :math:`a=2`, :math:`b=3` og :math:`c=-7`.

  Vitum að það eru tvær rauntölulausnir því :math:`d=(3)^2-4(2)(-7)=65 > 0`. Þá getum við notað lausnarformúlu annars stigs jöfnu.

  .. math::
     x = \frac{-3 \pm \sqrt{3^2 - 4 \cdot 2 \cdot (-7)}}{2 \cdot 2}
     = \frac{-3 \pm \sqrt{65}}{4}.

  Lausnirnar eru :math:`x_1=\frac{-3 + \sqrt{65}}{4}` og :math:`x_2=\frac{-3 - \sqrt{65} }{4}`.

 **2.** Leysum jöfnuna :math:`x^2-6(x-1)=-3`.

  Byrjum á að koma jöfnunni á almennt form.
  Margföldum upp úr sviganum og fáum :math:`x^2-6x+6=-3` eða :math:`x^2-6x+9=0`.
  Hér er því :math:`a=1`, :math:`b=-6` og :math:`c=9`.
  Vitum að það er bara ein lausn því :math:`d=(-6)^2-4(1)(9)=0`.
  Notum lausnarformúluna:

  .. math::
     x=\frac{6 \pm \sqrt{(-6)^2-4 \cdot 1 \cdot 9}}{2}=\frac{6 \pm \sqrt{36-36}}{2}=\frac{6}{2}=3

  Jafnan hefur lausnina, :math:`x=3`.

 **3.** Leysum jöfnuna :math:`x^2+1=0`.

  Hér er :math:`a=1`, :math:`b=0` og :math:`c=1`.

  Byrjum á að reikna út stærðina :math:`d=b^2-4ac` og fáum :math:`0^2-4 \cdot 1 \cdot 1=-4`, svo :math:`b^2-4ac<0` og jafnan hefur enga rauntölulausn.


Liðun og þáttun
---------------

Liðun
~~~~~

:hover:`Liðun, liða` kallast það þegar stærðtákni sem samanstendur af einum lið er breytt í fleiri liði.
Við tölum oft um að "margfalda upp úr svigum", til dæmis höfum við

.. math::
	(a+b)(c+d)=a(c+d)+b(c+d)=ac+ad+bc+bd

Í þessu tilviki þurfum við að margfalda báða liði fyrri svigans við báða liði seinni svigans, og við notum dreifireglu til þess. Höfum til dæmis

.. math::
	\begin{aligned}
	(x+2)(x+9)&=x \cdot x + x \cdot 9 + 2 \cdot x + 2 \cdot 9 \\
	&= x^2 + 9x + 2x + 18\\
	&= x^2 +11x +18
	\end{aligned}

Hér þarf að gæta þess að nota rétt formerki, höfum til dæmis

.. math::
	\begin{aligned}
	(x-2)(x+9)&=x \cdot x + x \cdot 9 + (-2) \cdot x + (-2) \cdot 9 \\
	& = x^2 + 9x - 2x - 18 \\
	& =x^2 +7x -18 \\
	\end{aligned}

------------------

Eftirfarandi reglur eru mikilvægar í liðun:

.. math::
	\begin{aligned}
	& (a+b)^2=a^2+2ab+b^2 \qquad &\textit{(ferningsregla fyrir summu)} \\
	& (a-b)^2=a^2-2ab+b^2 \qquad &\textit{(ferningsregla fyrir mismun)} \\
	& (a+b)(a-b)=a^2-b^2 \qquad &\textit{(samokaregla)} \\
	\end{aligned}

-------------------

.. tip::
 **1.** Liðum :math:`(x+2)^2`.

  Notum ferningsreglu fyrir summu. Þá fæst

  .. math::
    \begin{aligned}(x+2)^2&=x^2+2 \cdot 2 \cdot x + 2^2\\ &=x^2+4x+4 \end{aligned}


 **2.** Liðum :math:`(x+6)(x-6)`.

  Samokaregla gefur

  .. math::
    \begin{aligned} (x+6)(x-6)&=x^2-6^2\\ &=x^2-36 \end{aligned}


 **3.** Liðum :math:`(x-1)(x+1)^2`.

  Athugum að

  .. math::
    (x+1)^2=(x+1)(x+1)

  beitum samokareglu til að fá

	.. math::
	 	 \begin{aligned} (x-1)(x+1)^2&=(x-1)(x+1)(x+1)\\ &=(x^2-1)(x+1)\\ \end{aligned}

  Nú þurfum við bara að margfalda úr svigunum og fáum þá

  .. math::
    \begin{aligned}
    (x^2-1)(x+1)&=x^2 \cdot x + x^2 \cdot 1 - 1 \cdot x - 1 \cdot 1\\
    &=x^3 + x^2 -x -1
    \end{aligned}


 **4.** Liðum :math:`(x+4)^2(x-4)^2`.

  Höfum

	.. math::
	 	\begin{aligned} (x+4)^2(x-4)^2 &= ((x+4)(x-4))^2\\ & = (x^2 - 16)^2 \end{aligned}

  samkvæmt veldareglu og samokareglu. Notum nú ferningsreglu fyrir mismun og þá fæst

	.. math::
	 	\begin{aligned} (x^2 - 16)^2 &=(x^2)^2 - 2 \cdot 16x^2 + 16^2\\ &=x^4-32x^2+256\end{aligned}


Þáttun
~~~~~~
:hover:`Þáttun` er **andhverf aðgerð** við liðun. Þá er stæðu með fleiri en einum lið breytt í jafngilda stæðu sem samanstendur aðeins af þáttum.
Til eru margar leiðir til að þátta. Við getum í sumum tilfellum notað ferningsreglu eða samokareglu, sem settar eru fram hér að ofan.


.. tip::
	**1.** Þáttum :math:`x^2+4x+4`.

	 Notum ferningsreglu fyrir summu, það er,

	 .. math::
		a^2+2ab+b^2=(a+b)^2

	 Með samanburði sést að :math:`a=x` og :math:`b=2` gengur upp. Því er

	 .. math::
		x^2+4x+4=(x+2)^2

	**2.** Þáttum :math:`x^2-1`.

	 Beitum samokareglu og fáum

	 .. math::
		x^2-1 =(x+1)(x-1)

	**3.** Þáttum :math:`x^3-2x^2+x`.

	 Byrjum á því að athuga að :math:`x` er sameiginlegur þáttur allra liðanna. Þáttum :math:`x` út fyrir og fáum

	 .. math::
		x(x^2-2x+1)

	 Á seinni svigann getum við nú notað ferningsreglu fyrir mismun,

	 .. math::
		a^2-2ab+b^2=(a-b)^2

	 þar sem :math:`a=x` og :math:`b=1`. Við höfum því

	 .. math::
		x^3 - 2x^2 + x = x(x^2 - 2x + 1) = x(x-1)^2

Þáttun með ágiskunaraðferð
~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef við höfum stærð á forminu :math:`x^2+bx+c` getum við beitt svokallaðari ágiskunaraðferð. Hún gengur út á að finna tvær tölur :math:`s` og :math:`t` þannig að summa þeirra sé jöfn :math:`b` og margfeldi þeirra sé jafnt :math:`c`. Hún er kölluð ágiskunaraðferð þar sem við gætum þurft að prófa okkur áfram. Þess vegna getur verið gott að taka saman upplýsingar í töflu þannig að við byrjum á því að skrifa niður tvær tölur sem uppfylla það að margfeldi þeirra er jöfn síðustu tölunni. Þáttunin er síðan

.. math::
	x^2+bx+c=(x+s)(x+t)

þar sem :math:`s+t=b` og :math:`s\cdot t =c`.
Þetta skýrist best með dæmum.

.. note::
	Tökum eftir að ef annars stigs jafnan er á forminu :math:`ax^2+bx+c`, þar sem :math:`a\neq 1` þá tökum við :math:`a` út fyrir eða deilum í gegn með :math:`a` ef við erum að vinna með jöfnu (sjá dæmi **4** hér á eftir).

.. tip::
	**1.** Þáttum :math:`x^2+7x+12`.

	 Byrjum á að gera lista yfir tölur þannig að margfeldi þeirra sé :math:`12`. Fáum

	 .. math::
		\begin{array}{c}
		1 \text{ og } 12 \\
		2 \text{ og } 6 \\
		3 \text{ og } 4 \\
		\end{array}

	 Við getum séð að við erum komin með lausn með því að búa til dálk fyrir summu þessara tveggja talna

	 .. math::
		\begin{array}{ | c | c | c | }
		\hline
		s & t & \text{Summa} \\
		\hline
		1 & 12 & 13\\
		2 & 6 & 8\\
		3 & 4  & 7 \\
		\hline
		\end{array}

	 Við leitum að tveimur tölum sem hafa summuna :math:`7`. Við sjáum nú að tölurnar :math:`s = 3` og :math:`t = 4` uppfylla þetta skilyrði. Þáttunin er því

	 .. math::
	 	x^2+7x+12=(x+3)(x+4)

	**2.** Skoðum næst dæmi þar sem við þurfum að huga að formerkjunum. Þáttum :math:`x^2-26x+25`.

	 Finnum tölur þannig að margfeldi þeirra sé :math:`25`. En við sjáum að summa þeirra er neikvæð og margfeldi þeirra er jákvæð. Því er ljóst að báðar tölurnar eru neikvæðar. Möguleikar eru

	 .. math::
		\begin{array}{c}
		-1 \text{ og } -25 \\
		-5 \text{ og } -5 \\
		\end{array}

	 Leggjum tölurnar saman

 	 .. math::
		\begin{array}{ | c | c | c | }
		\hline
		s & t & \text{Summa} \\
		\hline
		-1 & -25 & -26\\
		-5 & -5 & -10\\
		\hline
		\end{array}

	 Sjáum að tölurnar :math:`s = -1` og :math:`t= -25` uppfylla skilyrðið svo þáttunin er

	 .. math::
	 	x^2-26x+25=(x+(-1))(x+(-25))=(x-1)(x-25).

	**3.** Þáttum :math:`x^2-x-6`.

	 Þar sem síðasta talan er neikvæð leitum við að neikvæðri tölu og jákvæðri tölu. Möguleikar eru því

	 .. math::
		\begin{array}{c}
		-1 \text{ og } 6 \\
		1 \text{ og } -6 \\
		-2 \text{ og } 3 \\
		2 \text{ og } -3 \\
		\end{array}

	 Leggjum tölurnar saman

	 .. math::
		\begin{array}{ | c | c | c | }
		\hline
		s & t & \text{Summa} \\
		\hline
		-1 & 6 & 5\\
		1 & -6 & -5 \\
		-2 & 3 & 1\\
		2 & -3 & -1\\
		\hline
		\end{array}

	 Sjáum því að tölurnar :math:`s = 2` og :math:`t = -3` uppfylla skilyrðið og þáttunin er

	 .. math::
	 	x^2-x-6=(x+2)(x-3).

	**4.** Þáttum :math:`2x^2+8x+6`.

	 Hér er :math:`a \neq 1` svo við getum umritað :math:`2x^2+8x+6` yfir í :math:`2(x^2+4x+3)` og þáttað :math:`x^2+4x+3`. Sjáum að :math:`1` og :math:`3` uppfylla skilyrðin.

	 .. math::
		\begin{array}{ | c | c | c | }
		\hline
		s & t & \text{Summa} \\
		\hline
		1 & 3 & 4\\
		\hline
		\end{array}

 	 Sjáum því að tölurnar :math:`s = 1` og :math:`t = 3` ganga en þá er þáttunin

	  .. math::
	  	x^2+4x+3 = (x+1)(x+3)

	 sem gefur okkur að :math:`2x^2+8x+6 = 2(x+1)(x+3)`.


.. note::
	Það er alls ekki nauðsynlegt að taka svona mörg skref við þáttun af þessu tagi.
  	Með æfingunni verður auðveldara að nota þessa aðferð í huganum og ekki er nauðsynlegt að sýna mörg skref.
  	Athugið að það getur komið í veg fyrir villur að sannreyna svarið, það er að liða stæðuna aftur.

Þáttun með lausnarformúlu
~~~~~~~~~~~~~~~~~~~~~~~~~

Til þess að þátta stærð á forminu :math:`ax^2+bx+c` getum við ávallt beitt lausnarformúlu fyrir annars stigs jöfnur. Munum að jafnan :math:`ax^2+bx+c=0` hefur lausnir

.. math::
	x_{1,2}=\frac{-b \pm \sqrt{b^2-4ac}}{2a}

Þáttunin verður þá

.. math::
	ax^2+bx+c=a(x-x_1)(x-x_2)

.. tip::
	**1.** Þáttum :math:`6x^2+5x-6`.

	 Finnum ræturnar. Hér er :math:`a=6`, :math:`b=5` og :math:`c=-6`. Notum lausnarformúluna og fáum

	 .. math::

		d = 5^2-4 \cdot 6 \cdot (-6) = 169 = 13^2

	 og

	 .. math::
		x_1 =\frac{-5+\sqrt{169}}{12}=\frac{-5+13}{12} =\frac{8}{12} =\frac{2}{3}

	 og

	 .. math::
		x_2=\frac{-5-13}{12}=-\frac{3}{2}

	 Samkvæmt formúlu að ofan er þáttunin því :math:`6x^2+5x-6=a(x-x_1)(x-x_2)`, það er,


	 .. math::
	 	\begin{aligned}
		6x^2+5x-6&=6\left(x-\frac{2}{3}\right)\left(x-\left(-\frac{3}{2}\right)\right)\\
		&=6\left(x-\frac{2}{3}\right)\left(x+\frac{3}{2}\right)
		\end{aligned}

	 Þetta svar er rétt, en við sjáum að við getum gert svarið snyrtilegra með því að athuga að :math:`6=2 \cdot 3` og margfalda fyrri svigann með :math:`3` og þann seinni með :math:`2`, það er,

	 .. math::
	 	\begin{aligned}
		6x^2+5x-6 &= 3 \left(x-\frac{2}{3}\right) \cdot 2\left(x+\frac{3}{2}\right)\\
		&=(3x-2)(2x+3)
		\end{aligned}

	 svo þáttunin er

	 .. math::
		6x^2+5x-6=(3x-2)(2x+3)

	**2.** Þáttum :math:`x^2+x-1`.

	 Hér er :math:`a=1`, :math:`b=1` og :math:`c=-1`. Lausnarformúlan gefur

	 .. math::
		x_1=\frac{-1+\sqrt{1^2-4 \cdot 1 \cdot (-1)}}{2 \cdot 1}=\frac{-1+\sqrt{5}}{2}

	 og

	 .. math::
		x_2=\frac{-1-\sqrt{5}}{2}

Fáum því að

	 .. math::
		x^2+x-1=\left(x-\frac{-1+\sqrt{5}}{2}\right)\left(x-\frac{-1-\sqrt{5}}{2}\right)

Jöfnuhneppi
-----------

Í sumum verkefnum koma fyrir fleiri en ein óþekkt stærð.
Til þess að leysa svoleiðis verkefni þurfum við að hafa jöfnur sem lýsa því hvernig stærðirnar tengjast.
Jöfnurnar þurfa að vera jafn margar og óþekktu stærðirnar.

Til eru tvær leiðir til þess að leysa svoleiðis verkefni, :hover:`eyðingaraðferð` og :hover:`innsetningaraðferð` .

Í **eyðingaraðferðinni** er reynt að eyða út einni óþekktri stærð úr jöfnuhneppi.
Til þess er önnur jafnan margfölduð með fasta svo stuðullinn fyrir framan stærðina sem á að eyða verði sá sami og stuðullinn í hinni jöfnunni.
Svo er önnur jafnan dregin frá hinni og útkoman er jafna án stærðarinnar sem eyða átti.

.. tip::
  Leysum jöfnuhneppið

  .. math::
    \begin{aligned}
      x+2y&=3 \\
      2x-y &=11
    \end{aligned}

  með eyðingaraðferð.

  **Lausn:**

  Stefnum á að eyða :math:`x` . Það gerum við með því að margfalda efri jöfnuna með 2 (beggja vegna jafnaðarmerkis):

  .. math::
    \begin{aligned}
      2x+4y&=6 \\
      2x-y &=11
    \end{aligned}

  Drögum nú efri jöfnuna frá þeirri neðri, hægri hlið efri frá hægri hlið neðri og vinstri hlið efri frá vinstri hlið neðri:

  .. math::
    \begin{aligned}
      (2x-y)-(2x+4y) &=11-6 \\
      -5y &= 5 \\
      y&=-1
    \end{aligned}

  Stefnum nú á að eyða :math:`y` úr upprunalega hneppinu:

  .. math::
    \begin{aligned}
      x+2y&=3 \\
      2x-y &=11
    \end{aligned}

  Á sama hátt og áður margföldum við neðri jöfnuna með 2 og fáum:

  .. math::
    \begin{aligned}
      x+2y&=3 \\
      4x-2y &=22
    \end{aligned}

  Leggjum nú jöfnurnar saman og fáum:

  .. math::
    \begin{aligned}
      (4x-2y )+ (x+2y) &=22 +3 \\
      5x &= 25 \\
      x&=5
    \end{aligned}

  Lausn jöfnuhneppisins er því :math:`x=5` og :math:`y=-1` .
  Myndrænt þýðir þetta að línurnar :math:`x+2y=3` og :math:`2x-y =11` skerist í punktinum :math:`(5,-1)` .
  Farið er nánar í þetta í kaflanum um rúmfræði.
.. _s.innsetning:

**Innsetningaraðferðin** gengur út á að einangra eina breytistærðina út frá annarri jöfnunni og setja inn í hina.
Þá hefur sú jafna bara eina óþekkta stærð.

.. tip::
  Leysum jöfnuhneppið

  .. math::
    \begin{aligned}
      2x+y&=2 \\
      3x+2y&=1 \\
    \end{aligned}

  með innsetningaraðferð.

  **Lausn:**

  Einangrum :math:`y` úr efri jöfnunni: :math:`y=2-2x` .
  Setjum þessa lýsingu á :math:`y` inn í neðri jöfnuna:

  .. math::
    \begin{aligned}
      3x+2y&=1 \\
      3x + 2(2-2x) &=1 \\
      3x+4-4x &=1\\
      -x&=-3\\
      x&=3
    \end{aligned}

  Nú vitum við rétt gildi á :math:`x` en þá er hægt að finna gildi á :math:`y` með því að setja gildið á :math:`x` inn í aðra hvora jöfnuna.
  Setjum því :math:`x=3` inn í efri jöfnuna og fáum:

  .. math::
    \begin{aligned}
      2x+y&=2 \\
      2\cdot 3 + y &=2 \\
      6+y &=2 \\
      y&=-4
    \end{aligned}

  Lausn jöfnuhneppisins

  .. math::
    \begin{aligned}
      2x+y&=2 \\
      3x+2y&=1 \\
    \end{aligned}

  er því :math:`x=3` og :math:`y=-4` .

.. note::
  Stundum getur verið þægilegt að finna fyrri breytistærðina með eyðingaraðferðinni og nota síðan innsetningu.

.. tip::
  Leysum jöfnuhneppið

  .. math::
    \begin{aligned}
    3x+2y&=14 \\
    x-y&=3
    \end{aligned}

  **Lausn:**

  Einangrum fyrst :math:`y` með eyðingaraðferð, það er, eyðum :math:`x` með því að margfalda neðri jöfnuna með þremur:

  .. math::
    \begin{aligned}
    3x+2y&=14 \\
    3x-3y&=9
    \end{aligned}

  Drögum síðan neðri jöfnuna frá þeirri efri og fáum

  .. math::
    \begin{aligned}
    2y-(-3y) &=14-9 \\
    5y &= 5 \\
    y&=1
    \end{aligned}

  Þá getum við nýtt okkur að gildi :math:`y` er þekkt og sett það inn í aðra hvora jöfnuna.
  Setjum því :math:`y=1` í neðri jöfnuna:

  .. math::
    \begin{aligned}
    x-y&=3 \\
    x-1&=3 \\
    x&=4
    \end{aligned}

  Lausn jöfnuhneppisins er því :math:`x=4` og :math:`y=1` .

Ójöfnur og tölugildi
--------------------
Ójöfnur
~~~~~~~
:hover:`Ójöfnur, ójafna` eru leystar á sambærilegan hátt og jöfnur. Eftirfarandi tákn eru notuð:

 :math:`< \qquad`  :hover:`Minna, minni`

 :math:`> \qquad` :hover:`Stærra, stærri`

 :math:`\leq \qquad` :hover:`Minna en eða jafnt, minni en eða jafn og`

 :math:`\geq \qquad` :hover:`Stærra en eða jafnt, stærri eða jafn og`

Þegar við leysum ójöfnur megum við beita sömu aðgerðum og þegar við leysum jöfnur, svo lengi sem við gerum það báðum megin. Það er bara ein undantekning: *margföldun/deiling með neikvæðri tölu*.

.. note::
	Tökum eftir að :math:`< \text{og} >` gefa :hover:`strangar ójöfnur, ströng ójafna`.

.. tip::
	**1.** Leysum ójöfnuna :math:`-2x+9 \leq 3`. Við megum draga frá :math:`9` báðum megin, þá fæst :math:`-2x \leq -6`. Hér þurfum við þó að einangra :math:`x` með því að deila í gegn með :math:`-2`, það er, margfalda með :math:`-\frac{1}{2}`. Þegar ójafna er margfölduð með neikvæðri tölu þarf að snúa ójöfnunni við vegna þess að :math:`a \leq b \implies -a \geq -b`. Við fáum því

	.. math::
		\left(-\frac12\right) \cdot (-2x) \geq \left(-\frac12\right) \cdot (-6) \quad \text{eða} \quad x \geq 3.

	Þetta þýðir því að :math:`x` má vera hvaða tala sem er, svo lengi sem hún er stærri en eða jöfn :math:`3`. Með prófun er hægt að staðfesta að þetta gengur upp.

	**2.** Leysum ójöfnuna :math:`2x+2 >30x`. Drögum frá :math:`2x` báðum megin og fáum :math:`2>28x`. Deiling með :math:`28` gefur :math:`\frac{1}{14}>x`. Hér þurftum við ekki að snúa ójafnaðarmerkinu við. Þó er skýrara að skila svarinu á forminu :math:`x<\frac{1}{14}`.


Tölugildi
~~~~~~~~~

Látum :math:`x` vera rauntölu. Fjarlægð tölunnar :math:`x` frá núllpunktinum á talnalínunni köllum við :hover:`tölugildi` eða :hover:`algildi` tölunnar :math:`x`. Við táknum það með :math:`|x|`. Athugum að fjarlægð getur ekki verið neikvæð svo að :math:`|x| \geq 0` fyrir öll :math:`x`.

Ef :math:`x` er jákvæð þá er :math:`|x|=x`. Ef :math:`x` er neikvæð þá fæst tölugildi hennar með því að ,,taka mínusinn af henni" . Í raun er jafngilt að margfalda hana með  :math:`-1` því að þá ,,hverfur mínusinn af henni". Með táknmáli er tölugildið skilgreint svona:

.. math::
	|x|= \begin{cases} x & \text{ ef } x \geq 0 \\ -x  & \text{ ef } x < 0 \end{cases}

Til dæmis er :math:`5 \geq 0` svo :math:`|5|=5` og :math:`-3 <0` svo að :math:`|-3|=(-1) \cdot (-3) = 3`.

Reiknireglur fyrir tölugildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Látum :math:`a` og :math:`b` vera rauntölur. Þá gildir eftirfarandi

.. math::
	\begin{aligned}
		a \leq |a|  \qquad & \text{(tölugildi getur aðeins stækkað tölu)}\\
		|a|=|-a|  \qquad & \text{(tölugildi eru óháð formerki)}\\
		|a|\cdot|b|=|ab| \qquad & \text{(tölugildi varðveitir margföldun)}\\
		|a|^2=a^2 \qquad  & \text{(önnur veldi eyða tölugildi)}\\
	\end{aligned}

.. note::
	Fyrir tölur :math:`a` og :math:`b` þá má túlka töluna :math:`|a-b|` sem fjarlægð :math:`a` frá :math:`b` á talnalínunni. Til dæmis ef :math:`a=3` og :math:`b=10` þá er fjarlægðin á milli þessara talna á talnalínunni :math:`7`. Það er í samræmi við reikninga okkar, höfum :math:`|3-10|=|-7|=7` og :math:`|10-3|=|7|=7`.

.. tip::
	Finnum öll :math:`x` sem uppfylla :math:`|x+4|=10`.
	Við komum með tvær lausnir:

	**Lausn 1:** Jafnan :math:`|x+4|=|x-(-4)|=10` segir okkur að fjarlægðin milli :math:`x` og tölunnar :math:`-4` er :math:`10`. Því er ljóst að :math:`x=-14` eða :math:`x=6`.

	**Lausn 2:** Jafnan :math:`|x+4|=10` segir okkur að annað hvort er :math:`x+4=10` eða :math:`x+4=-10`. Fyrri jafnan hefur lausnina :math:`x=6` og sú seinni :math:`x=-14`.

	.. image:: ./myndir/jofnur/mynd-algildi2.svg
		:width: 110 %
		:align: center

	Sjáum að :math:`-14` og :math:`6` eru jafn langt frá :math:`-4`

.. tip::
	Finnum öll :math:`x` sem uppfylla :math:`|x-3|=|x+7|`.

	Við komum með þrjár lausnir:

	**Lausn 1:** Rúmfræðilega þýðir jafnan :math:`|x-3|=|x-(-7)|` að fjarlægð tölunnar :math:`x` frá :math:`3` er jöfn fjarlægðar :math:`x` frá :math:`-7`. Þá hlýtur :math:`x` að vera talan sem er mitt á milli :math:`3` og :math:`-7` á talnalínunni. Með öðrum orðum er :math:`x` meðaltal þessara talna:

	 .. math::
		x=\frac{3+(-7)}{2}=-2

	**Lausn 2:** Skiptum í þrjú tilvik:

	1.  Ef :math:`x<-7` þá er :math:`x-3<0` og :math:`x+7<0`.

	 Samkvæmt skilgreiningu er því

	 .. math::
		|x-3|=-(x-3)=-x+3

	 og

	 .. math::
	 	|x+7|=-(x+7)=-x-7.

	 Eftir stendur jafnan :math:`-x+3=-x-7` sem jafngildir :math:`3=-7` sem er fráleitt.
	 Jafnan hefur því enga lausn :math:`x` sem uppfyllir :math:`x<-7`

	2. Ef :math:`-7\leq x<3` þá er :math:`x-3<0` og :math:`x+7\geq 0`.

	 Samkvæmt skilgreiningu er því

	 .. math::
		|x-3|=-(x-3)=-x+3 \quad

	 og

	 .. math::
	 	|x+7|=x+7.

	Eftir stendur jafnan :math:`-x+3=x+7` sem hefur lausnina :math:`x=-2`.

	3. Ef :math:`x\geq 3` þá er :math:`x-3\geq 0` og :math:`x+7>0`. Samkvæmt skilgreiningu er því

	 .. math::
		|x-3|=x-3 \quad

	 og

	 .. math::
	 	|x+7|=x+7.

	 Eftir stendur jafnan :math:`x-3=x+7` sem jafngildir :math:`-3=7` sem er fráleitt.
	 Jafnan hefur því enga lausn sem uppfyllir :math:`x\geq 3`

	**Lausn 3:** Setjum báðar hliðar jöfnunnar í annað veldi. Þá eyðast tölugildin skv. reiknireglu og eftir stendur: :math:`(x-3)^2=(x+7)^2` sem jafngildir

	 .. math::
		x^2-6x+9=x^2+14x+49 \quad

	 eða

	 .. math::
	 	-20x=40 \quad \text{þ.e.} \quad x=-2.

	 Ef þessari lausn er stungið inní upphaflegu jöfnuna þá sést að þetta er lausn sem virkar.


.. note::
	Takið eftir að í lausn 3 í dæminu hér á undan þá endum við á því að prófa lausnina sem við fengum.
	Það er af því að þegar jöfnur eru settar í annað veldi geta skapast ,,falskar lausnir".
  	Því þarf alltaf að athuga hvort lausnirnar sem fengust séu raunverulegar lausnir.

	Skoðum til dæmis jöfnuna :math:`4x=8`. Þessi jafna hefur augljóslega bara eina lausn :math:`x=2`. Ef þessi jafna er sett í annað veldi fæst jafnan :math:`16x^2=64` sem jafngildir :math:`x^2=4` eða :math:`x=\pm 2`. Hér varð til falska lausnin :math:`-2` sem er ekki lausn á upprunalegu jöfnunni. Upphaflega lausnin er hins vegar ennþá til staðar.

.. tip::
  Leysum ójöfnuna :math:`|x+2|>9`. Skiptum í tvö tilvik samkvæmt skilgreiningu, ef :math:`x+2>0`, eða :math:`x+2<0`.

  **Tilvik 1**:
  Ef :math:`x+2 \geq 0`, það er, :math:`x \geq -2`, þá fellum við tölugildið niður og þá fæst ójafnan :math:`x+2>9`, það er, :math:`x>7`.

  Við þurfum því að uppfylla bæði skilyrðin :math:`x \geq -2` og :math:`x>7` en ljóst er að seinna skilyrðið er sterkara (það má sjá á talnalínu). Ef :math:`x >7` þá hefur það í för með sér að :math:`x \geq -2`. Því er lausnin í þessu tilviki, :math:`x >7`.

  **Tilvik 2**:
  Ef :math:`x+2 \leq 0`, það er, :math:`x \leq -2`, þá fæst ójafnan :math:`-(x+2)>9`, eða :math:`-x-2>9`, eða :math:`x<-11`.

  Við þurfum að uppfylla bæði skilyrðin :math:`x \leq -2` og :math:`x<-11` en ljóst er að það seinna er sterkara. Lausnin er því :math:`x<-11`.

  Við fáum því lokasvarið

  .. math::
    x >7 \qquad \text{eða} \qquad x<-11

  Við getum líka skrifað þetta sem bil, jafngilt svar er

  .. math::
    x \in ]- \infty , -11[ \, \cup \, ]7, \infty[


Summu- og margfeldistáknið
--------------------------

.. panopto:: 26b3143f-25f5-454e-a137-649ed1207c7a
    :width: 100%
    :height: 405

-------------------------------------------

Stundum kemur fyrir að stærðfræðingar vilja leggja saman marga liði. Til dæmis

.. math::
	1+2+3+4+...+100

eða

.. math::
  \frac{1}{4}+\frac{1}{5}+\frac{1}{6}+...+\frac{1}{87}

Í báðum þessum dæmum ætti að vera augljóst hvað summan þýðir þó að svona þrípunktur sé ekki alvöru stærðfræðitákn.
Í fyrra dæminu er verið að leggja saman allar heiltölur frá einum upp í hundrað og í seinna dæminu er verið að leggja saman einn á móti sérhverri heiltölu frá fjórum upp í áttatíu-og-sjö.

Stundum vinnum við samt með flóknari gerðir af summum og þá dugar svona táknmál skammt. Þess vegna innleiðum við summutáknið :math:`\sum`.

Segjum að við viljum leggja saman allar tölur af gerðinni :math:`n(n+1)` þar sem :math:`n` gengur frá einum upp í hundrað. Einhverjum gæti dottið í hug að skrifa

.. math::
	\begin{aligned}
	& 1 \cdot (1+1)+2 \cdot (2+1)+3 \cdot (3+1)+4 \cdot (4+1)+...+100 \cdot (100+1)\\ &=2+6+12+20+...+10100 \end{aligned}

en þetta þykir ekki snyrtileg leið að tákna summu. Þess vegna skrifum við frekar

.. math::
	\sum_{n=1}^{100}n(n+1)

Fyrir neðan summutáknið stendur :math:`n=1` sem merkir að breytistærðin sem við vinnum í er :math:`n` og að við byrjum í einum. Fyrir ofan summutáknið stendur hundrað sem þýðir að við endum summuna þegar :math:`n=100`. Hægra megin við summutáknið stendur síðan formúlan fyrir sérhvern lið í summunni. Athugum að :math:`\sum_{n=1}^{100}n(n+1) = \sum_{n=0}^{99}(n+1)(n+2)`.

Summurnar sem teknar voru fram í byrjun kaflans yrðu táknaðar með

.. math::
	\sum_{n=1}^{100}n=1+2+3+...+100

og

.. math::
	\sum_{n=4}^{87}\frac{1}{n} = \frac{1}{4}+\frac{1}{5}+\frac{1}{6}+...+\frac{1}{87}

Stundum lendum við í sömu vandræðum með löng margfeldi. Þess vegna innleiðum við margfeldistáknið :math:`\prod` sem er notað á sama hátt og summutáknið en bara fyrir margfeldi.

Þannig er

.. math::
	\prod_{n=1}^{100}n=1\cdot 2\cdot 3\cdot 4\cdots 100\qquad \prod_{n=4}^{87}\frac{1}{n}=\frac{1}{4}\cdot\frac{1}{5}\cdot\frac{1}{6}\cdots\frac{1}{100}

og

.. math::
	\prod_{n=1}^{100}n(n+1)=1(1+1)\cdot 2(2+1)\cdot 3(3+1)\cdots 100(100+1)=2\cdot 6\cdot 12 \cdots 10100


.. note::
	Þessi tákn eru mikilvæg þegar unnið er með :hover:`runur, runa` og :hover:`raðir, röð`.
	*Runa* er raðaður listi af tölum og *röð* er summa liðanna.

.. tip::
	**1.** Reiknum

	.. math::
		\sum_{n=-3}^{5}n^2


	Höfum

	.. math::
		\begin{aligned}
		\sum_{n=-3}^{5}n^2 &=(-3)^2+(-2)^2+(-1)^2+0^2+1^2+2^2+3^2+4^2+5^2 \\ &=9+4+1+0+1+4+9+16+25=69
		\end{aligned}

	**2.** Reiknum

	.. math::
		\prod_{n=1}^{4}(1+n)

	Höfum

	.. math::
		\prod_{n=1}^{4}(1+n)=(1+1)(1+2)(1+3)(1+4)=2\cdot 3\cdot 4\cdot 5=120
