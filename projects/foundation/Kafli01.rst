Algebra
=======
Talnakerfi
----------

.. panopto:: bfb3abf8-891c-4a53-8cee-08640552d8f0
    :width: 100%
    :height: 405

--------------------------------------------------------------------------------------------------

Náttúrulegu tölurnar  :math:`\mathbb{N}`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tölurnar :math:`0,1,2,3, \dots` köllum við :hover:`náttúrulegu tölurnar, náttúruleg tala`. :hover:`Mengi, set` náttúrulegu talnanna er táknað með :math:`\mathbb{N}.`

Heiltölurnar :math:`\mathbb{Z}`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:hover:`Heilu tölurnar, heiltala` eru talnakerfi allra heilla talna. Það inniheldur

* neikvæðu heiltölurnar; :math:`-1,-2,-3, \dots`

* jákvæðu heiltölurnar; :math:`1,2,3, \dots`

* og töluna :math:`0`.

Mengi heiltalna er táknað með :math:`\mathbb{Z}`.

Ræðu tölurnar :math:`\mathbb{Q}`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:hover:`Ræðar tölur, ræð tala` samanstanda af öllum brotum :math:`\frac{p}{q}` þar sem :math:`p` og :math:`q` eru heilar tölur og :math:`q \neq 0`. Talan :math:`p` nefnist :hover:`teljari` brotsins og talan :math:`q` :hover:`nefnari` þess.

Mengi ræðra talna er táknað með :math:`\mathbb{Q}`.

Rauntölurnar :math:`\mathbb{R}`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ekki eru allar tölur ræðar tölur.
Tölur sem ekki er hægt að skrifa sem brot heilla talna köllum við :hover:`óræðar tölur, óræð tala`.
Til dæmis er talan :math:`\pi` (pí) óræð.

Mengi allra ræðra talna, auk óræðra talna, nefnist :hover:`rauntölurnar, rauntala`. Það er táknað með :math:`\mathbb{R}`.

.. image:: ./myndir/algebra/mynd-mengi.svg
    :width: 75 %
    :align: center

Hér höfum við mengjamynd af talnamengjunum. Sjáum til dæmis að :math:`\mathbb{N}` er :hover:`hlutmengi` í :math:`\mathbb{R}`, það er allar náttúrulegar tölur eru rauntölur.
(Í :ref:`kaflanum um mengi <s.Mengi>` má finna skilgreiningu á :ref:`hlutmengi <s.hlutmengi>`)

Forgangsröðun aðgerða
---------------------

.. panopto:: 8982adb1-99d4-4fc3-a1d9-b5ef571f1f6a
    :width: 100%
    :height: 405

-------------------------------------------------------------------------------------

Þegar reiknað er með tölum þarf að framkvæma :hover:`aðgerðir, reikniaðgerð` í eftirfarandi röð:

1. Reikningsaðgerðir innan sviga
2. Margföldunar- og deilingaraðgerðir
3. Samlagningar- og frádráttaraðgerðir

.. tip::
	Notum forgangsröðun aðgerða:

	**1.** Reiknum :math:`1+2 \cdot 3`

	.. math::
		\begin{aligned}
			1+2 \cdot 3&=1+6\\
			&=7
		\end{aligned}

	**2.** Reiknum :math:`(1+2)\cdot 3+4`

	.. math::
		\begin{aligned}
			(1+2)\cdot 3+4&= 3 \cdot 3+4\\
			&=9+4 \\
			&= 13
		\end{aligned}

	**3.** Reiknum :math:`((1+1) \cdot 5+3 \cdot (2-4))\cdot 2`

	.. math::
		\begin{aligned}
			((1+1) \cdot 5+3 \cdot (2-4))\cdot 2 &=(2 \cdot 5+3 \cdot (-2)) \cdot 2\\
			& = (10-6) \cdot 2\\
			&=4 \cdot 2\\
			&=8
		\end{aligned}




Reiknireglur
------------
Nokkrar einfaldar reiknireglur gilda um tölur í talnakerfunum:

.. math::
	\begin{aligned}
	(a+b)+c=a+(b+c) &  \qquad \textit{ (tengiregla samlagningar)}\\
	(ab)c=a(bc) & \qquad \textit{ (tengiregla margföldunar)}\\
	a+b=b+a & \qquad \textit{ (víxlregla samlagningar)}\\
	ab=ba & \qquad \textit{ (víxlregla margföldunar)}\\
	a(b+c)=ab+ac & \qquad \textit{ (dreifiregla)}\\
	1 \cdot a=a & \qquad \textit{ (1 er margföldunarhlutleysa)}\\
	a+0=a & \qquad \textit{ (0 er samlagningarhlutleysa)}\\
	0 \cdot a=0  & \qquad \textit{ (margföldun með núlli gefur núll)}\\
	\end{aligned}

.. warning::
	Athugum að tvær neikvæðar tölur margfaldaðar saman verða að jákvæðri tölu, til dæmis :math:`(-3)\cdot (-4) = 3\cdot 4 =12` .

.. tip::
	Prófum dreifiregluna [:math:`a(b+c)=ab+ac`] fyrir tölurnar :math:`a=3`, :math:`b=-9` og :math:`c=5`.

	Vinstra megin jafnaðarmerkisins stendur :math:`3(-9+5)=3\cdot(-4)=-12`.

	Hægra megin jafnaðarmerkisins stendur :math:`3\cdot(-9)+3\cdot 5=-27+15=-12`.

	Við höfum því sömu stærð báðum megin jafnaðarmerkis.

Frumtölur
---------

Skilgreining: Deilanleiki
~~~~~~~~~~~~~~~~~~~~~~~~~
Heiltala :math:`a` er sögð vera deilanleg með heiltölunni :math:`b` ef til er heiltala :math:`x` þannig að :math:`a=bx`.

.. tip::
  Talan 14 er deilanleg með 2 því hana má skrifa sem :math:`14=2\cdot 7` .

.. note::
	Allar tölur :math:`a` eru deilanlegar með einum og sjálfri sér því :math:`a= 1 \cdot a` . Tölur geta haft fleiri deila, til dæmis er :math:`12` deilanleg með :math:`3` og :math:`4` og talan :math:`15` er deilanleg með :math:`3` og :math:`5`.

Sumar náttúrulegar tölur eru aðeins deilanlegar með einum og sjálfri sér.
Þær eru nefndar :hover:`frumtölur, frumtala`, en talan :math:`1` er **ekki** skilgreind sem frumtala.


Skilgreining: Frumtölur
~~~~~~~~~~~~~~~~~~~~~~~
Ef náttúruleg tala :math:`p \geq 2` er aðeins deilanleg með einum og sjálfri sér þá segjum við að :math:`p` sé *frumtala*.

.. tip::
	:math:`7` er frumtala, því eina jákvæða heiltölulausninn á :math:`7=bx` er :math:`b=7` og :math:`x=1`, þ.e. :math:`7 = 7 \cdot 1`,

	en :math:`6` er ekki frumtala því :math:`6=2 \cdot 3`.

.. note::
	Nokkrar fyrstu frumtölurnar eru: :math:`2,3,5,7,11,13,17,19,23,29, \dots`

.. image:: ./myndir/algebra/frumtölur.png
    :width: 100 %
    :align: center

Hér eru 25 fyrstu frumtölurnar merktar bláar.

.. _s.frumþáttun:

Allar heiltölur sem eru ekki frumtölur eru margfeldi frumtalna. Af því leiðir að sérhverja heiltölu megi skrifa sem margfeldi frumtalna.

Frumþáttun
~~~~~~~~~~

Sérhverja náttúrulega tölu :math:`a \geq 2` má skrifa sem margfeldi frumtalna

.. math::
	a=p_1 p_2 p_3 \dots p_m

þar sem sumar frumtölur geta verið endurteknar.

.. tip::

	.. math::
		7=7, \qquad 24=2 \cdot 2 \cdot 2 \cdot 3=2^3 \cdot 3, \qquad 250= 2 \cdot 5 \cdot 5 \cdot 5=2 \cdot 5^3.

Engin skilvirk aðferð hefur verið fundin til að :hover:`frumþátta, frumþáttun` stórar tölur. Eftirfarandi aðferð til að frumþátta byggir á prófun:

1. Athugum hvort einhver frumtala minni en talan gangi upp í hana. Hér er best að byrja á lægstu frumtölunni, 2, og svo næstu frumtölu, 3, o.s.fr.v.
2. Ef við finnum slíka frumtölu deilum við með henni og fáum út aðra tölu, og skoðum hana.
3. Athugum hvort við finnum frumtölu sem gengur upp í nýju töluna og endurtökum þá skref 1 og 2.
4. Höldum þessu áfram þar til við finnum enga frumtölu sem gengur upp í töluna, þá er talan sjálf frumtala. Frumþáttunin er svo rituð sem margfeldi allra frumtalnanna sem við fundum.

.. note::
	Ef við leitum að frumtölu sem gengur upp í tölu þá nægir að skoða frumtölur **minni en eða jafnar kvaðratrót tölunnar**. Þetta getur flýtt fyrir við að frumþátta stórar tölur.

.. tip::

	**1.** Frumþáttum töluna :math:`273`. Athugum að :math:`2` gengur ekki upp í :math:`273`, en :math:`3` gerir það, samkvæmt prófun. Skoðum þá næst :math:`273/3=91`. Með prófun sést að :math:`2,3` og :math:`5` ganga ekki upp í :math:`91`, en :math:`7` gerir það.  Skoðum þá næst :math:`91/7=13`. En :math:`13` er frumtala. Því höfum við fundið frumþáttunina. Hún er :math:`273=3 \cdot 7 \cdot 13`. Oft er þægilegt að setja upp frumþáttunina í tré:

	.. image:: ./myndir/algebra/frumthattun.svg
		:width: 75 %
		:align: center


	**2.** Frumþáttum töluna :math:`101`. Notfærum okkur athugasemd hér að ofan. Við þurfum bara að prófa frumtölur minni en eða jafnar :math:`\sqrt{101} \approx 10.05`. Með prófun sést að :math:`2, 3,5` og :math:`7` ganga ekki upp í :math:`101`. Því er :math:`101` frumtala.

  .. note::
    Allar tölur sem hafa þversummu sem er margfeldi af þremur eru deilanlegar með þremur.
    Til dæmis má sjá í lið **1.** hér að ofan að þversumma 273 er :math:`2+7+3 = 12 =3 \cdot 4` og því er 273 deilanleg með 3 (:math:`273=3\cdot 91` ).



Þessi aðferð frumþáttunar byggir á því að finna frumtölu sem gengur upp í töluna, en oft getur verið þægilegra að finna samsetta tölu og frumþátta hana síðan.

.. tip::
	Frumþáttum töluna 270:

	.. figure:: ./myndir/frth270.svg
		:align: center
		:width: 60%

	Frumþáttun 270 er því:

	.. math::
		270 = 2\cdot 5\cdot 3\cdot 3\cdot 3


.. tip::
	Ef við skoðum :math:`36` þá getum við fundið alla deila hennar með því að skoða allar tölur sem ganga upp í :math:`36`.
	Hér eru allar tölurnar sem ganga upp í :math:`36`

	.. math::
		{1, 2, 3, 4, 6, 9, 12, 18, 36}


Stærsti samdeilir og minnsta samfeldi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:hover:`Stærsti samdeilir` tveggja talna er stærsta talan sem gengur upp í báðar tölurnar.
Hann er hægt að finna með því að frumþátta báðar tölurnar og finna hvaða frumþættir eru sameiginlegir.

.. tip::
  Finnum stærsta samdeili 792 og 756.

  *Lausn*

  Byrjum á því að frumþátta tölurnar:

  .. math::
    \begin{aligned}
    792 &= 2\cdot 2\cdot 2\cdot 3\cdot 3\cdot 11 \\
    &= 2^3\cdot 3^2\cdot 11  \\
    & \\
    756 &= 2\cdot 2\cdot 3\cdot 3\cdot 3\cdot 7 \\
    &= 2^2\cdot 3^3 \cdot 7
    \end{aligned}

  Sjáum því að sameiginlegir frumþættir 792 og 756 eru :math:`2^2` og :math:`3^2` og því er stærsti samdeilir þeirra:

  .. math::
    \text{ssd}(792,756) = 2^2 \cdot 3^2 = 36

  Það þýðir að 36 er stærsta talan sem gengur upp í bæði 792 og 756

  .. math::
    \begin{aligned}
    792&=36\cdot 22 \\
    756&=36\cdot 21
    \end{aligned}

:hover:`Minnsta samfeldi` tveggja talna er minnsta talan sem báðar tölurnar ganga upp í.
Það er hægt að finna með því að margfalda saman frumþættina í hæsta veldinu sem þeir koma fram í.

.. tip::
  Finnum minnsta samfeldi 792 og 756.

  *Lausn*

  Eins og áður er frumþáttun talnanna:

  .. math::
    \begin{aligned}
    792 &= 2\cdot 2\cdot 2\cdot 3\cdot 3\cdot 11 \\
    &= 2^3\cdot 3^2\cdot 11  \\
    & \\
    756 &= 2\cdot 2\cdot 3\cdot 3\cdot 3\cdot 7 \\
    &= 2^2\cdot 3^3 \cdot 7
    \end{aligned}

  Frumþættirnir sem fram koma eru 2, 3, 7 og 11.
  Hæsta veldið á 2 er 3 (í frumþáttuninni á 792), hæsta veldið á 3 er 3 (í frumþáttuninni á 756) en 7 og 11 koma aðeins einu sinni fyrir. Því er:

  .. math::
    \text{msf}(792,756) = 2^3\cdot 3^3 \cdot 7\cdot 11 = 16632

.. note::
  Fyrir sérhvert par talna :math:`a` og :math:`b` gildir að

  .. math::
    a \cdot b = \text{ssd}(a,b)\cdot \text{msf}(a,b)




Brotareikningur
---------------
Rifjum upp skilgreiningu á ræðum tölum.

Skilgreining: Ræðar tölur
~~~~~~~~~~~~~~~~~~~~~~~~~
*Ræðar tölur* samanstanda af öllum brotum :math:`\frac{p}{q}` þar sem :math:`p` og :math:`q` eru heilar tölur og :math:`q \neq 0`. Talan :math:`p` nefnist *teljari* brotsins en talan :math:`q` *nefnari* þess.

.. note::
	Allar heilar tölur eru ræðar tölur með nefnarann :math:`1`, til dæmis er :math:`3= \frac31`.

Fullstytt brot
~~~~~~~~~~~~~~

Ef :math:`a`, :math:`b` og :math:`t` eru heilar tölur gildir

.. math::
	\frac{at}{bt}=\frac{a}{b}

Þegar við styttum töluna :math:`t` út tölum við um að :hover:`stytta` brotið og þegar við margföldum með :math:`t` fyrir ofan og neðan strik tölum við um að :hover:`lengja, framlengja` brotið.

.. tip::
	Skoðum brotið :math:`\frac{9}{21}`. Við getum lengt brotið með :math:`2` með því að margfalda með :math:`2` fyrir ofan og neðan strik

	.. math::
		\frac{9}{21}=\frac{9 \cdot 2}{21 \cdot 2}=\frac{18}{42}

	Við getum einnig stytt brotið :math:`\frac{9}{21}` með því að athuga að :math:`9=3 \cdot 3` og :math:`21=3 \cdot 7`. Þá fæst

	.. math::
		\frac{9}{21}=\frac{3 \cdot 3}{3 \cdot 7}=\frac{3}{7}

.. note::
	Við sjáum að sama brotið er hægt að skrifa á margan hátt. Þess vegna er góð venja að *fullstytta* brotið. Við segjum að brot sé *fullstytt* ef við getum ekki stytt það frekar. Til þess að fullstytta brot er hægt að frumþátta bæði nefnara og teljara og stytta út sameiginlega frumþætti.

.. tip::
	Fullstyttum brotið :math:`\frac{525}{980}`.

	Frumþáttum tölurnar eins og lýst er í kaflanum á undan. Við fáum :math:`525=3 \cdot 5 \cdot 5 \cdot 7` og :math:`980=2 \cdot 2 \cdot 5 \cdot 7 \cdot 7`.

	Nú getum við ritað

	.. math::
		\frac{525}{980}=\frac{3 \cdot 5 \cdot 5 \cdot 7}{2 \cdot 2 \cdot 5 \cdot 7 \cdot 7}

	og við sjáum því að við gettum stytt út eina fimmu og eina sjöu. Eftir stendur þá brotið

	.. math::
		\frac{525}{980}=\frac{3 \cdot 5 \cdot 5 \cdot 7}{2 \cdot 2 \cdot 5 \cdot 7 \cdot 7} = \frac{3 \cdot 5}{2 \cdot 2 \cdot 7}

	sem hefur enga sameiginlega frumtölu fyrir ofan og neðan strik.
	Margföldum nú tölurnar saman og fáum :math:`\frac{3 \cdot 5}{2 \cdot 2 \cdot 7}=\frac{15}{28}`, sem er því brotið fullstytt.

	.. math::
		\frac{525}{980}=\frac{15}{28}


.. warning::
	Stærð almenns brots breytist ekki við lengingu eða styttingu.

Röðun ræðra talna
~~~~~~~~~~~~~~~~~
Þegar fjallað er um mengi heilla talna hafa flestir mjög skýra hugmynd um hvað það þýðir að ein tala sé stærri en önnur. Við vitum til dæmis að :math:`3468` er stærri en :math:`2497` og við skrifum :math:`3468>2497`.

Í mengi ræðra talna eru hlutir ekki jafn einfaldir. Til dæmis þykir ekki augljóst hvor af tölunum
:math:`\frac{13}{512}` og :math:`\frac{26}{1023}` er stærri.
Ein leiðin væri einfaldlega að slá báðar tölurnar inn í vasareikni og sjá að

.. math::
	\frac{13}{512}\approx 0,02539 \quad \text{og} \quad \frac{26}{1023}\approx 0,02542.

Þá sést að

.. math::
	\frac{26}{1023}>\frac{13}{512} \quad \text{því að} \quad 0,02542>0,02539.

Við viljum hins vegar geta reiknað hlutina á blaði án vasareiknis.

Ef tvö brot hafa sama nefnara er auðvelt að skera úr um hvort þeirra er stærra.
Við vitum að brotið :math:`\frac{p}{s}` er stærra en :math:`\frac{q}{s}` og skrifum

.. math::
	\frac{p}{s}>\frac{q}{s} \quad \text{ef} \quad p>q.

Þetta getum við sagt því að brotin hafa sameiginlegan nefnara :math:`s`. Til dæmis er :math:`\frac{7}{3}` stærra en :math:`\frac{6}{3}` því bæði brotin hafa nefnarann :math:`3`.
Þessa staðreynd getum við nýtt okkur þegar reynt er að meta flóknari brot.

Til þess að geta lagt tvö brot saman, eða fundið mismun þeirra, þurfum við að gera þau samnefnd, það er, við þurfum  þannig að þau hafi sömu tölu í nefnara. Þetta er hægt að gera með því að lengja brotin.

Fyrir tvö brot :math:`\dfrac{a}{b}` og :math:`\dfrac{c}{d}` getum við til dæmis gert þau samnefnd með því að lengja það fyrra með :math:`d` og það seinna með :math:`b`. Þá hafa þau bæði sama nefnarann, sem er :math:`b \cdot d`.

.. tip::
	Hvort brotið er stærra :math:`\frac{3}{4}` eða :math:`\frac{5}{12}`?

	Lengjum fyrra brotið með :math:`12` og það seinna með :math:`4`

	.. math::
		\begin{aligned}
			\frac{3}{4} &= \frac{3\cdot 12}{4\cdot 12}=\frac{36}{48} \\
			&\text{og} \\
			\frac{5}{12} &= \frac{5\cdot 4}{12\cdot 4}=\frac{20}{48}
		\end{aligned}

	Nú hafa brotin sama jákvæða nefnara, :math:`36>20` og því segjum við að :math:`\frac{3}{4}>\frac{5}{12}`.


Reiknireglur
~~~~~~~~~~~~


Í mengi ræðra talna má leggja saman, draga frá, margfalda og deila. Þessar aðgerðir eru framkvæmdar svona:

1.

.. math::
	\frac{p}{q}+\frac{r}{s}=\frac{ps}{qs}+\frac{qr}{qs}=\frac{ps+qr}{qs}

2.

.. math::
	\frac{p}{q}-\frac{r}{s}=\frac{ps-qr}{qs}

3.

.. math::
	\frac{p}{q} \cdot \frac{r}{s}=\frac{pr}{qs}

4.

.. math::
	\frac{p/q}{r/s} =\frac{ps}{qr}

.. warning::
	Athugið að það má alls ekki stytta út lið! Dæmi:

	.. math::
		\frac{x+3}{3} \neq x


.. tip::
 **1.** Leggjum saman brotin :math:`\frac{7}{11}` og :math:`\frac{10}{13}`.

  Gerum brotin fyrst samnefnd með því að lengja fyrra brotið með nefnara seinna brotsins og seinna brotið með nefnara fyrra brotsins.
  Að því loknu er lítið mál að leggja brotin saman með því að leggja saman teljarana

	.. math::
		\begin{aligned}
		  \frac{7}{11}+\frac{10}{13}&=\frac{7 \cdot 13}{11 \cdot 13}+ \frac{11 \cdot 10}{13 \cdot 11}\\
		   &= \frac{91}{143}+\frac{110}{143}\\
		   &=\frac{91+110}{143}\\
		   &=\frac{201}{143}
		\end{aligned}

 **2.** Leggjum saman brotin :math:`\frac{2}{7}` og :math:`\frac{3}{2}`.

  Eins og í dæmi **1** gerum við brotin fyrst samnefnd með því að lengja fyrra brotið með nefnara seinna brotsins og seinna brotið með nefnara fyrra brotsins.
  Teljarar brotanna eru síðan lagðir saman

	.. math::
		\begin{aligned}
		\frac{2}{7}+\frac{3}{2}&=\frac{2 \cdot 2}{7 \cdot 2} + \frac{7 \cdot 3}{7 \cdot 2}\\
		&=\frac{4}{14}+\frac{21}{14}\\
		&=\frac{4+21}{14}\\
		&=\frac{25}{14}
		\end{aligned}

 **3.** Margföldum saman brotin :math:`\frac{11}{9}` og :math:`\frac{7}{5}`.

  Þegar brot eru margfölduð saman eru teljararnir margfaldaðir saman og nefnararnir margfaldaðir saman.

	.. math::
		\frac{11}{9} \cdot \frac{7}{5}=\frac{11 \cdot 7}{9 \cdot 5}=\frac{77}{45}

 **4.** Deilum brotinu :math:`\frac{11}{45}` með brotinu :math:`\frac{1}{2}`.

	.. math::
		\frac{11/45}{1/2}=\frac{11 \cdot 2}{45 \cdot 1}=\frac{22}{45}

	.. warning::
		Nefnari í nefnara verður teljari!

.. tip::
	Reiknum úr þessu broti og fullstyttum það síðan:

	.. math::
		\frac{\left(\frac{1}{4}+\frac{2}{3} \right)\cdot\frac{3}{2}}{5/2}

  *Lausn:*

  Byrjum á að leggja saman brotin í sviganum:

  .. math::
    \begin{aligned}
    \frac{\left(\frac{1}{4}+\frac{2}{3} \right)\cdot\frac{3}{2}}{5/2} &= \frac{\frac{1\cdot 3+4\cdot 2}{4\cdot 3}\cdot\frac{3}{2}}{5/2} \\
    &= \frac{\frac{11}{12}\cdot\frac{3}{2}}{5/2} \\
   \end{aligned}

  Margföldum síðan saman brotin í teljaranum:

  .. math::
    \begin{aligned}
  		\frac{\frac{11}{12}\cdot\frac{3}{2}}{5/2}&= \frac{(11\cdot 3)/(12\cdot 2)}{5/2} \\
  		&= \frac{33/24}{5/2} \\
   \end{aligned}

  Deilum nú brotinu í teljaranum með brotinu í nefnaranum:

  .. math::
    \begin{aligned}
    \frac{33/24}{5/2} &= \frac{33\cdot 2}{24\cdot 5} \\
    &= \frac{66}{120}
    \end{aligned}

  Fullstyttum svo brotið:

	.. math::
		\begin{aligned}
		\frac{66}{120} &= \frac{2\cdot 3\cdot 11}{2\cdot 2 \cdot 2 \cdot 3\cdot 5} \\
		&= \frac{11}{2\cdot 2\cdot 5} \\
		&= \frac{11}{20}
		\end{aligned}

Deiling með afgangi
-------------------

Látum :math:`a` og :math:`b` vera :hover:`heiltölur, heiltala`.
Það er ekki alltaf hægt að deila heilli tölu :math:`a` með heilli tölu :math:`b` og fá út aðra heila tölu.
Við getum hins vegar notað *deilingu með* :hover:`afgangi, afgangur`.
Hún gengur út á að finna tvær heiltölur :math:`x` og :math:`y` þannig að

.. math::
	a=bx+y

þar sem :math:`y` er jákvæð tala og :math:`y<b`.

Við segjum að :math:`b` gangi :math:`x` sinnum upp í :math:`a` með afgang :math:`y`.

Ef afgangurinn er :math:`0` þá segjum við að :math:`b` gangi upp í :math:`a`.

.. tip::
  **1.** Deilum tölunni :math:`a=81` með tölunni :math:`b=8` með afgangi.

   Athugum að :math:`8 \cdot 10=80` en :math:`8 \cdot 11=88`. Við leitum að stærstu tölu sem er margfeldi af :math:`8` og er minni en eða jöfn 81, þess vegna notum við :math:`10` en ekki :math:`11`. Afgangurinn er síðan :math:`1`, þ.e.a.s. við getum ritað

   .. math::
    81=8 \cdot 10 + 1

   Því er :math:`x=10` og :math:`y=1`. Við getum nú sagt að :math:`8` gangi :math:`10` sinnum upp í :math:`81` með afgang :math:`1`.


  **2.** Deilum tölunni :math:`a=79` með tölunni :math:`b=8` með afgangi.

   Athugum að :math:`8 \cdot 9=72` en :math:`8 \cdot 10=80`. Afgangurinn er nú :math:`79-72=7`. Því getum við ritað

   .. math::
    79=8 \cdot 9 + 7

   en hér er :math:`x=9` og :math:`y=7`. Við getum nú sagt að :math:`8` gangi :math:`9` sinnum upp í :math:`79` með afgang :math:`7`.

.. note::
	Afgangurinn er alltaf minni en :math:`b`. Ef afgangurinn er stærri en (eða jafn) :math:`b` þá getum við notað stærra :math:`x`.

Stundum, til dæmis í forritun, þurfum við að reikna með afgangi.
Þá tölum við um :hover:`módulus, leifastofn` eða leifastofn (":math:`a` módulus :math:`b` er :math:`y`" ) og táknum það með

.. math::
  a\mod b = y.

Þegar talan :math:`b` gengur upp í :math:`a` þá er módulus þeirra núll.

.. tip::
  .. math::
    \begin{aligned}
      6 \mod \; 3 &=0 \quad & \text{ því } \quad 6 = 3\cdot 2 + 0\\
      5 \mod \; 3 &=2 \quad & \text{ því } \quad 5 = 3\cdot 1 + 2\\
      4 \mod \; 3 &=1 \quad & \text{ því } \quad 4 = 3\cdot 1 + 1 \\
      3 \mod \; 3 &=0 \quad & \text{ því } \quad 3 = 3\cdot 1 + 0 \\
    \end{aligned}


Veldi og rætur
---------------
Veldi
~~~~~

.. panopto:: 60e4c107-9666-46b6-a990-7be29df41cf6
    :width: 100%
    :height: 405

---------------------------------------------------------------------------

:hover:`Veldi` er þegar tala er margfölduð með sjálfri sér.
Látum :math:`a` vera tölu og :math:`n>0` vera heiltölu. Við skilgreinum

.. math::
  \begin{aligned}
	a^0&=1 \\
	a^n&=a \cdot a \cdot \dots \cdot a \qquad (n\text{-sinnum}) \\
	a^{-n}&=\frac{1}{a^n}
  \end{aligned}

Talan :math:`a` í rithættinum :math:`a^n` nefnist :hover:`veldisstofn` og talan :math:`n` nefnist :hover:`veldisvísir`.

.. note::
	Við segjum að :math:`a` sé í :math:`n`-ta veldi þegar :math:`a^n`.

.. tip::
	**1.**

	.. math::
		a \cdot a \cdot a \cdot a \cdot a=a^5

	**2.**

	.. math::
		4^3=4 \cdot 4 \cdot 4=64

	**3.**

	.. math::
		4^{-3}=\frac{1}{4^3}=\frac{1}{64}

Reiknireglur fyrir veldi
~~~~~~~~~~~~~~~~~~~~~~~~

Höfum eftirfarandi reiknireglur fyrir veldi:

.. math::

	\begin{aligned}
	a^n\cdot a^m&=a^{n+m} &\\
	\dfrac {a^n}{a^m}&=a^{n-m}&\\
	a^n\cdot b^n&=(ab)^n&\\
	(a^n)^m&=a^{nm} &\\
	(-1)^n &= 1 &\quad \text{þegar } n \text{ er slétt tala} \\
	(-1)^n &= -1& \quad \text{þegar } n \text{ er oddatala} \\
	\end{aligned}


.. tip::
	**1.**

	.. math::
		2^2 \cdot 2^3=2^{2+3}=2^5

	**2.**

	.. math::
		\frac{2^{62}}{2^{60}}=2^{62-60}=2^{2}=4

	**3.**

	.. math::
		2^5 \cdot 36^5=(2 \cdot 36)^5=72^5

	**4.**

	.. math::
		(2^2)^3=2^{2 \cdot 3}=2^6=64

	**5.**

	.. math::
		2^2\cdot 2^3\cdot 5^5=2^{(2+3)}\cdot 5^5=2^5\cdot 5^5=(2\cdot 5)^5=10^5=100000.

	**6.** Einföldum

	.. math::
		(a^{x+y})^z (a^{x-z})^y.

	Við beitum veldareglunum og fáum:

	.. math::
		(a^{x+y})^z (a^{x-z})^y = a^{zx + zy}a^{yx - zy} = a^{zx + zy + yx - zy} = a^{zx + yx} = (a^{z+y})^x.

Rætur
~~~~~

.. panopto:: 42da725a-d1a0-4158-a663-7fedb94c8a4e
    :width: 100%
    :height: 405

------------------------------------------------------------------

Látum :math:`q` vera jákvæða heiltölu og :math:`a` vera jákvæða tölu. Þá er til nákvæmlega ein tala :math:`x \geq 0` þannig að :math:`x^q=a`. Þessi tala nefnist :math:`q`-ta :hover:`rótin, rót` af :math:`a` og er táknuð með

.. math::
	\sqrt[q]{a}

Við skrifum þó yfirleitt ekki :math:`\sqrt[2]{a}` heldur :math:`\sqrt{a}` og nefnum þessa stærð :hover:`kvaðratrót, önnur rót`, oft kölluð ferningsrót.

.. tip::
	**1.** :math:`\sqrt{4}=2 \quad` því :math:`\quad 2^2=4`

	**2.** :math:`\sqrt{64}=8 \quad` því :math:`\quad 8^2=64`

	**3.** :math:`\sqrt[3]{27}=3 \quad` því :math:`\quad 3^3=27`

	**4.** :math:`\sqrt[4]{16}=2 \quad` því :math:`\quad 2^4=16`.

Reiknireglur fyrir rætur
~~~~~~~~~~~~~~~~~~~~~~~~

Höfum eftirfarandi reiknireglur fyrir rætur:

.. math::

	\begin{aligned}
	  \sqrt[q]{ab} &=\sqrt[q]{a}\cdot \sqrt[q]{b} \\
    & \qquad \\
    \sqrt[q]{\dfrac ab}& =\dfrac{\sqrt[q]{a}}{\sqrt[q] {b}}\\
    & \qquad \\
    \sqrt[q]{a^p}& =(\sqrt[q]{a})^p\\
    & \qquad \\
    \sqrt[sq]{a^{sp}} &={\sqrt[q]{a^p}}\\
    & \qquad \\
    \sqrt[sq]{ a} &=\sqrt[s]{\sqrt[q]{a}}\\
  \end{aligned}

.. note::
	Rætur virða ekki samlagningu, þ.e.a.s. almennt er :math:`\sqrt[q]{a+b} \neq \sqrt[q]{a}+ \sqrt[q]{b}`.

.. tip::
	**1.** :math:`\sqrt[4]{2} \cdot \sqrt[4]{8}= \sqrt[4]{2 \cdot 8}= \sqrt[4]{16}=2`

	**2.** :math:`\frac{\sqrt[3]{135}}{\sqrt[3]{5}}=\sqrt[3]{\frac{135}{5}}=\sqrt[3]{27}=3`

	**3.** :math:`\sqrt[4]{256} = \sqrt[4]{16^2}=\left(\sqrt[4]16\right)^2=2^2=4`

Brotin veldi
~~~~~~~~~~~~
Þegar tala hefur ræða tölu í veldisvísi sem er ekki heiltala tölum við um brotið veldi. Látum :math:`r` vera ræða tölu og skrifum hana :math:`r=\frac{p}{q}` þar sem :math:`p` og :math:`q` eru heilar tölur, :math:`q>0`. Þá er

.. math::
	a^r=a^{\frac{p}{q}}=\sqrt[q]{a^p}

Það er, við skilgreinum :math:`a^{\frac{p}{q}}` þannig að

.. math::
	a^{\frac{p}{q}}=\sqrt[q]{a^p}

Veldareglurnar gilda einnig fyrir ræða veldisvísa. Athugum að þriðja veldareglan segir að

.. math::
	a^r=\sqrt[q]{a^p}=(\sqrt[q]{a})^p.

Einnig er

.. math::
	a^{\frac{1}{q}}=\sqrt[q]{a}

fyrir allar heiltölur :math:`q`.

.. tip::
	**1.** :math:`\sqrt{a}=a^{\frac12}`

	**2.** :math:`9^{\frac12}=\sqrt{9}=3`

	**3.** :math:`32^{\frac25}=\sqrt[5]{32^2}=\left(\sqrt[5]{32}\right)^2=2^2=4`

	**4.** :math:`8^{\frac{1}{3}}=\sqrt[3]8 = 2`

	**5.** :math:`16^{\frac{3}{4}}=\sqrt[4]{(16^3)}=\left(\sqrt[4]{16}\right)^3=2^3=8`

	**6.** Látum :math:`a,b > 0`. Einföldum

	.. math::
		\sqrt[3]{\left(\sqrt{a}\right)^3 \left(\sqrt[4]{b}\right)^6 }

	Hér beitum við reiknireglum fyrir rætur:

	.. math::
		\begin{aligned}

		\sqrt[3]{\left(\sqrt{a}\right)^3 \left(\sqrt[4]{b}\right)^6 }
		&= \sqrt[3]{\left(\sqrt{a}\right)^3 } \sqrt[3]{ \left(\sqrt[4]{b}\right)^6 } \\
		&= \sqrt{a} \left(\sqrt[4]{b}\right)^2 \\
		&= \sqrt{a} \cdot b^{\frac24} \\
		&=\sqrt{a} \cdot b^{\frac12} \\
		&=\sqrt{a} \sqrt{b} = \sqrt{ab}\\

		\end{aligned}
