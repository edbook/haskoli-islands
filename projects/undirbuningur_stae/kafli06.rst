Margliður
=========

Margliður
---------
:hover:`Margliða` er fall :math:`\mathbb{R} \to \mathbb{R}` sem tákna má með formúlu af gerðinni

.. math::
	p(x)=a_nx^n+a_{n-1}x^{n-1}+ \cdots + a_1x+a_0

þar sem :math:`n` er :hover:`náttúruleg tala` og stuðlarnir :math:`a_j` eru :hover:`rauntölur, rauntala` og :math:`a_n \neq 0`. Þá kallast talan :math:`n` *stig* margliðunnar. Skoðum dæmi um margliður.

.. tip::

	**1.** :math:`p(x)=8x^4+3x^2+2x+1` er dæmi um margliðu.

	 Þessi margliða hefur stigið :math:`n=4`. Hér er :math:`a_0=1`, :math:`a_1=2`, :math:`a_2=3`, :math:`a_3=0` og :math:`a_4=8`.

	**2.** :math:`p(x)=3x^5+\pi x^2-\dfrac{4}{5}` er dæmi um margliðu.

	 Þessi margliða hefur stig :math:`n=5`. Hér er :math:`a_0=-\frac{4}{5}`, :math:`a_2=\pi`, :math:`a_5=3` og :math:`a_1=a_3=a_4=0`.

	**3.** :math:`p(x)=3^x` er ekki margliða.

	**4.** :math:`p(x)=\sin(x)+4x^2` er ekki margliða.


Núllstöðvar margliða
--------------------

Ef :math:`p` er margliða og :math:`x_0` er tala þ.a. :math:`p(x_0)=0` þá segjum við að :math:`x_0` sé :hover:`rót` eða :hover:`núllstöð` margliðunnar `p`.


Margliður geta haft margar núllstöðvar, en fjöldi þeirra er takmarkaður eins og fram kemur í eftirfarandi reglu:

Regla
~~~~~
Látum :math:`p` vera margliðu af stigi :math:`n`. Fjöldi mismunandi núllstöðva margliðunnar :math:`p` er þá í mesta lagi :math:`n`.

.. note::
	Þessi regla þýðir því að:
	 * fyrsta stigs margliða hefur enga eða eina núllstöð,
	 * annars stigs margliða hefur enga, eina, eða tvær núllstöðvar,
	 * þriðja stigs margliða hefur enga, eina, tvær, eða þrjár núllstöðvar,
	 * ... og svo framvegis.

	 Sumar margliður hafa engar rauntölunúllstöðvar.
	 Til dæmis hefur margliðan :math:`p(x)=x^2+1` engar rauntölunúllstöðvar því rauntalan :math:`x^2` getur aldrei verið neikvæð.

.. tip::
	**1.** Margliðan :math:`x^2-1` hefur tvær mismunandi núllstöðvar, það er, jafnan :math:`x^2-1=0` hefur lausnirnar :math:`x=1` og :math:`x=-1`.

	**2.** Margliðan :math:`(x-1)^2` hefur bara eina núllstöð, það er, jafnan :math:`(x-1)^2=0` hefur bara lausnina :math:`x=1`.

	.. warning::
		Í seinna tilvikinu tölum við oft um að margliðan hafi eina :hover:`tvöfalda núllstöð, tvöföld rót`.


Fyrsta og annars stigs margliður
--------------------------------
Rifjum upp kaflan um :ref:`jöfnur<s.jofnur>`.

Fyrsta stigs margliður
~~~~~~~~~~~~~~~~~~~~~~
Fyrsta stigs margliða er fall af gerðinni

.. math::
	\begin{aligned}
	&p(x)=ax+b \\
	&\text{þar sem} \qquad a \neq 0 \quad \text{og} \quad b \in \mathbb{R}.
	\end{aligned}

Graf hennar er :hover:`lína`. Þessi margliða hefur í mesta lagi eina núllstöð og hana er auðvelt að finna.
Við leysum einfaldlega :math:`x` úr jöfnunni :math:`ax+b=0`. Við þekkjum lausn þessarar jöfnu, hún er :math:`x=-\frac{b}{a}`.

.. _s.annarsstigs:

Annars stigs margliður
~~~~~~~~~~~~~~~~~~~~~~
:hover:`Annars stigs margliða` er fall af gerðinni

.. math::
	\begin{aligned}
	&p(x)=ax^2+bx+c \\
	&\text{þar sem} \qquad a \neq 0 \quad \text{og} \quad b,c \in \mathbb{R}
	\end{aligned}

Graf hennar er :hover:`fleygbogi`. Til að finna núllstöðvar hennar þá leysum við jöfnuna :math:`ax^2+bx+c=0`. Rifjum aftur upp regluna til að leysa slíkar jöfnur, sem má finna í kaflanum um :ref:`annars stigs jöfnur <s.annars stigs jöfnur>`.

Regla
~~~~~

Látum :math:`ax^2+bx+c=0` vera annars stigs jöfnu.

1. Ef :math:`b^2-4ac<0` þá hefur jafnan enga rauntölulausn.
2. Ef :math:`b^2-4ac=0` þá hefur jafnan eina lausn:

.. math::
	x=\frac{-b}{2a}.

3. Ef :math:`b^2-4ac>0` þá hefur jafnan tvær lausnir:

.. math::
	x_1=\frac{-b+\sqrt{b^2-4ac}}{2a} \qquad \text{og} \qquad x_2=\frac{-b-\sqrt{b^2-4ac}}{2a}.

.. tip::
	**1.** Finnum núllstöð margliðunnar :math:`p(x)=81x+121`.

	 Hún hefur eina núllstöð þar sem þetta er fyrsta stigs margliða. Leysum þá jöfnuna :math:`81x+121=0`. Fáum

	 .. math::
	 	\begin{aligned}
	 	81x &=-121 \\
		x &=-121/81
		\end{aligned}

	 Því er núllstöðin :math:`x=-121/81` .

	**2.** Finnum núllstöðvar margliðunnar :math:`p(x)=2x^2-21x+1`.

	 Leysum jöfnuna :math:`2x^2-21x+1=0`. Höfum

	 .. math::
	 	b^2-4ac=(-21)^2-4 \cdot 2 \cdot 1=441-8=433 >0

	 Núllstöðvar eru því tvær: :math:`x_1=\frac{21+\sqrt{443}}{4}` og :math:`x_2=\frac{21-\sqrt{443}}{4}`.

Deiling með afgangi - margliður
-------------------------------
Ef tvær margliður :math:`p` og :math:`q` eru lagðar saman eða önnur dregin frá hinni verður útkoman ný margliða.
Margfeldið :math:`p \cdot q` verður einnig ný margliða, en það sama verður ekki sagt um deilingu.

Eins og á heiltölunum er deiling á margliðum ekki fullkomin í þeim skilningi að ef einni margliðu er deilt með annarri fæst ekki alltaf margliða út. Þegar tölu er deilt með annarri fæst ekki alltaf heiltala.
Við notum því deilingu með afgangi til að hjálpa okkur:

Látum :math:`p` og :math:`q` vera margliður.
Þá eru til margliður :math:`s` og :math:`r` þannig að :math:`p=qs+r` og stig :math:`r` er minna en stig :math:`q`.

Það að finna þessar margliður :math:`s` og :math:`r` kallast deiling með afgangi. Margliðan :math:`s` kallast :hover:`kvóti` og margliðan :math:`r` kallast :hover:`afgangur`.

Hægt er að nota aðferð sem er mjög lík löngudeilingu með heiltölur til að deila margliðum með afgangi. Best er að sjá þessa aðferð með dæmum:

.. tip::


	**1.** Deilið með margliðunni :math:`q(x)=x+4` í margliðuna :math:`p(x) =x^4 + 2x - 4` með afgangi.

	 Notum löngudeilingu: byrjum á því að margfalda :math:`q(x)=x+4` með :math:`s_1=x^3` til þess að fremsti liður :math:`q(x)` verði jafn fremsta lið :math:`p(x)` .
	 Drögum :math:`x^3 \cdot q(x)=x^3\cdot(x+4) = x^4+4x^3 \quad` frá :math:`\quad p(x) =x^4 + 2x - 4` og fáum afganginn :math:`p_1(x)=-4x^3+2x-4` .

	 .. image:: ./myndir/marglidur/mdeilingA.svg
			:align: center
			:width: 60%

	 Endurtökum skrefin fyrir afganginn.
	 Margföldum :math:`q(x)=x+4` með :math:`s_2=-4x^2` til þess að fremsti liður :math:`q(x)` verði jafn fremsta lið :math:`p_1(x)` .
	 Drögum :math:`-4x^2 \cdot q(x)=-4x^2\cdot(x+4) = -4x^3-16x^3 \quad`  frá  :math:`\quad p_1(x)=-4x^3+2x-4` og fáum afganginn :math:`p_2(x)=16x^2+2x-4` .

	 .. image:: ./myndir/marglidur/mdeilingB.svg
	 	:align: center
	 	:width: 60%

	 Margföldum :math:`q(x)=x+4` með :math:`s_3=16x` til þess að fremsti liður :math:`q(x)` verði jafn fremsta lið :math:`p_2(x)` .
	 Drögum :math:`16x \cdot q(x)=16x\cdot(x+4) = 16x^2+64x \quad` frá :math:`\quad p_2(x)=16x^2+2x-4` og fáum afganginn :math:`p_3(x)=-62x-4` .


	 .. image:: ./myndir/marglidur/mdeilingC.svg
		:align: center
		:width: 60%

	 Margföldum :math:`q(x)=x+4` með :math:`s_4=-62` til þess að fremsti liður :math:`q(x)` verði jafn fremsta lið :math:`p_3(x)` .
	 Drögum :math:`-62 \cdot q(x)=-62\cdot(x+4) = -62x-248 \quad` frá :math:`\quad p_3(x)=-62x-4` og fáum afganginn :math:`p_4(x)=r=244` .

	 .. image:: ./myndir/marglidur/mdeilingD.svg
	 	:align: center
	 	:width: 60%

	 Þetta segir okkur að :math:`s(x) = s_1+s_2+s_3+s_4 = x^3 -4x^2 +16x -62` og :math:`r(x) = 244`. Við getum nú skrifað

	 .. math::
		x^4 +2x -4 = (x+4)(x^3 - 4x^2 + 16x - 62) + 244

	**2.** Deilið með margliðunni :math:`q(x)=x-3` í margliðuna :math:`p(x) =x^3 + 6x^2 -2x - 8` með afgangi.

	 Með löngudeilingu fæst eftirfarandi

	 .. image:: ./myndir/marglidur/mdeiling2.svg
		:align: center
		:width: 60%

	 Þetta segir okkur að :math:`s(x) =x^2+ 9x +25` og :math:`r(x) = 67`. Við getum nú skrifað

	 .. math::
		x^4 +2x -4 = (x-3)(x^2 + 9x - 25) + 67


Þáttun margliða
---------------
Ef afgangurinn er :math:`r=0` þá getum við notað löngudeilingu (margliðudeilingu) til þess að :hover:`þátta, þáttun` margliður.

Skilgreining
~~~~~~~~~~~~
Látum :math:`p` og :math:`q` vera margliður. Ef að til er margliða :math:`h` þannig að :math:`p=h \cdot q` þá segjum við að margliðan :math:`q` gangi upp í margliðunni :math:`p`. Þá skrifum við líka :math:`\dfrac{p}{q}=h`.

Að skrifa margliðu :math:`q` sem margfeldi margliða af lægra stigi kallast :hover:`þáttun` margliðu.

Margliða :math:`q` er sögð :hover:`óþáttanleg, óþættanleiki` ef engin margliða af lægra stigi en :math:`q` gengur upp í :math:`q`.

Margliða er sögð vera fullþáttuð ef að búið er að skrifa hana sem margfeldi af óþáttanlegum margliðum.

.. tip::
	Þessa margliðu má þátta svona:

	.. math::
		x^3-6x^2-9x+14 = (x-1)(x+2)(x-7)

	og til dæmis má þátta þessa margliðu svona:

	.. math::
		x^3+4x^2-x-4 = (x-1)(x+1)(x+4)

	Sjáum nánar dæmi um hvernig þessi lausn fæst hér að :ref:`neðan<s.dæmi>`.


Núllstöðvar margliða og þáttun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Margliða kallast :hover:`stöðluð, stöðluð margliða` ef :math:`a_n=1`, það er, fremsti stuðullinn, eða stuðullinn við hæsta veldið, er :math:`1`. Fyrir staðlaðar margliður gildir eftirfarandi regla:

Regla
~~~~~
Ef :math:`p` er stöðluð margliða af stigi :math:`n` og hún hefur :math:`n` ólíkar rætur, :math:`x_1, x_2, \dots, x_n`, þá má skrifa

.. math::
	p(x)=(x-x_1)(x-x_2) \dots (x-x_n)

Raunar fæst eftirfarandi niðurstaða:

Regla
~~~~~
Látum :math:`p` vera margliðu. Þá gengur margliðan :math:`x-x_0` upp í margliðunni :math:`p` þá og því aðeins að :math:`x_0` sé núllstöð margliðunnar :math:`p`.


.. begin-toggle::
	:label: Sýnidæmi
	:starthidden: True


Sannreynum að hægt sé að þátta annars stigs margliðu í rætur sínar, þ.e. sýnum að:

.. math::
	  ax^2+bx+c=a\left(x-\frac{-b+\sqrt{b^2-4ac}}{2a}\right)\left(x-\frac{-b-\sqrt{b^2-4ac}}{2a}\right)

Margföldum saman svigana:

.. math::
	\begin{aligned}
		&a\left(x-\frac{-b+\sqrt{b^2-4ac}}{2a}\right)\left(x-\frac{-b-\sqrt{b^2-4ac}}{2a}  \right)\\
		&= a\left(x+\frac{b-\sqrt{b^2-4ac}}{2a}\right)\left(x+\frac{b+\sqrt{b^2-4ac}}{2a} \right)\\
		&=ax^2+a\cdot\frac{b-\sqrt{b^2-4ac}}{2a}x+a\cdot\frac{b+\sqrt{b^2-4ac}}{2a}x\\
		&+a\cdot\left(\frac{b-\sqrt{b^2-4ac}}{2a}\right)\left(\frac{b+\sqrt{b^2-4ac}}{2a}\right)\\
		&=ax^2 + \frac{a\cdot x}{2a}\left(b-\sqrt{b^2-4ac}+b+\sqrt{b^2-4ac}\right)\\
		&+\frac{a}{4a^2}\left(b-\sqrt{b^2-4ac}\right)\left(b-\sqrt{b^2-4ac}\right)\\
		&=ax^2+\frac{x}{2}(2b)+\frac{1}{4a}(b^2-(b^2-4ac)) \\
		&=ax^2+bx+c
	\end{aligned}
.. end-toggle::


.. tip::
	Til þess að þátta margliður byrjum við á að finna allar núllstöðvar hennar og skrifum margliðuna síðan sem margfeldi óþáttanlegra margliða.

	Fullþáttum :math:`p(x)=x^2+2x-5`. Notum lausnarformúlu annars stigs jöfnu til að finna núllstöðvarnar. Hér er :math:`a=1`, :math:`b=2` og :math:`c=-5`. Fáum því

	.. math::
		\begin{aligned}
		x=\dfrac{-2\pm\sqrt{2^2-4\cdot 1\cdot (-5)}}{2}&=\dfrac{-2\pm\sqrt{24}}{2}\\
		&=\dfrac{-2\pm 2\sqrt{6}}{2}\\
		&=-1\pm\sqrt{6}
		\end{aligned}

	þ.e. :math:`x_1=-1+\sqrt{6}` og :math:`x_2=-1-\sqrt{6}`. Samkvæmt reglunni hér fyrir ofan fáum við þá þáttunina

	.. math::
		\begin{aligned}
		p(x)&=(x-x_1)(x-x_2)\\
		&=(x-(-1+\sqrt{6}))(x-(-1-\sqrt{6}))\\
		&=(x+1-\sqrt{6})(x+1+\sqrt{6})
		\end{aligned}

    það er,

	.. math::
		p(x)=(x+1-\sqrt{6})(x+1+\sqrt{6})

	.. note::
		Þetta segir okkur að margliðurnar :math:`x+(1-\sqrt{6})` og :math:`x+(1+\sqrt{6})` ganga báðar upp í margliðuna :math:`p(x)`.

.. _s.dæmi:
.. tip::
  Þáttum þriðja stigs margliðuna :math:`x^3+4x^2-x-4` .

  Við þurfum að byrja á því að finna núllstöðvar margliðunnar, það er, þau :math:`x` þannig að :math:`x^3+4x^2-x-4=0`.
  Þægilegt er að sjá að :math:`x=1` er núllstöð:

  .. math::
    x^3+4x^2-x-4 |_{x=1} = 1^3+4\cdot 1^2 -1-4 = 0

  Því má skrifa margliðuna sem liðinn :math:`(x-1)` margfaldaðan við annars stigs margliðu.
  Finnum þá margliðu með margliðudeilingu:

  .. figure:: ./myndir/marglidur/longud1.svg
    :align: center
    :width: 50%

  Höfum því :math:`x^3+4x^2-x-4 = (x-1)(x^2+5x+4)` .
  Þáttum nú :math:`x^2+5x+4` en við sjáum að :math:`x=-1` er núllstöð hennar:

  .. math::
    x^2+5x+4|_{x=-1} = (-1)^2+5\cdot(-1)+4 =0

  Því má skrifa :math:`x^2+5x+4` sem :math:`(x+1)` margfaldað við aðra fyrsta stigs margliðu.
  Hana má líka finna með margliðudeilingu:

  .. figure:: ./myndir/marglidur/longud2.svg
    :align: center
    :width: 40%

  Sjáum að :math:`x=-4` er líka núllstöð.
  Við höfum því fundið þrjár núllstöðvar fyrir þriðja stigs margliðu (en þær geta ekki verið fleiri) og því er fullþáttun margliðunnar

  .. math::
    x^3+4x^2-x-4 = (x-1)(x+1)(x+4)


p/q-aðferð
----------

Engin almenn leið er til sem að finnur núllstöðvar margliða af háum stigum. Eftirfarandi regla kemur þó stundum að gagni, ef til er ræð núllstöð:

Regla
~~~~~
Látum :math:`r(x)=a_nx^n+a_{n-1}x^{n-1}+ \dots + a_1x+a_0` vera margliðu af stigi :math:`n` þar sem stuðlarnir eru heilar tölur. Ef til er ræð tala :math:`p/q` sem er núllstöð margliðunnar :math:`r` þá gengur :math:`p` upp í :math:`a_0` og :math:`q` gengur upp í :math:`a_n`.

.. note::
	Þessi regla segir okkur að ef við viljum finna einhverja núllstöð margliðu, þá er ráðlagt að ,,giska'' fyrst á núllstöðvarnar af gerðinni :math:`\frac{p}{q}` þar sem :math:`p` gengur upp í :math:`a_0` og :math:`q` gengur upp í :math:`a_n`. Það getur verið sniðugt að byrja á því að athuga hvort :math:`1` eða :math:`-1` eru núllstöðvar því það er fljótgert.

.. tip::
	**1.** Finnum einhverja núllstöð :math:`h(x)=15x^4-3x^3-10x^2+x-3`.

	 Góð regla er að byrja á því að athuga hvort :math:`1` eða :math:`-1` eru núllstöðvar. Fáum

	 .. math::
	 	\begin{aligned}
	 		h(1)&=15 \cdot 1-3 \cdot 1 -10 \cdot 1 + 1 \cdot 1 -3 \\
			&=15-3-10+1-3\\
			&=0
	 	\end{aligned}

	 svo :math:`x=1` er núllstöð.

	**2.** Finnum einhverja núllstöð :math:`g(x)=10x^4+8x^3+8x^2+5x-5`.

	 Við sjáum auðveldlega að :math:`1` er ekki núllstöð.

	 Munum að :math:`(-1)^n=-1` ef :math:`n` er oddatala og :math:`(-1)^n=1` ef :math:`n` er slétt tala.

	 Fáum nú

	 .. math::
	 	\begin{aligned}
	 		g(-1) &= 10 \cdot (-1)^4 + 8 \cdot (-1)^3 + 8 \cdot (-1)^2+5 \cdot (-1)-5\\
			& =10-8+8-5-5\\
			&=0
		\end{aligned}

	 svo að :math:`x=-1` er núllstöð.

	**3.** Finnum einhverja núllstöð á margliðunni :math:`r(x)=2x^4-5x^3-2x^2-9`.

	 Sjáum með prófun að hvorki :math:`1` né :math:`-1` eru núllstöðvar. Beitum þá :math:`p/q`-aðferð.

	 Mengi allra talna sem gengur upp í tölunni :math:`2` er :math:`A=\{1,-1,2,-2\}`.
	 Mengi allra talna sem gengur upp í tölunni :math:`9` er :math:`B=\{1,-1,3,-3,9,-9 \}`.
	 :math:`\frac{p}{q}`-aðferð segir okkur að við eigum að giska á núllstöð af gerðinni :math:`\frac{p}{q}` þar sem :math:`p\in B` og :math:`q\in A`.

	 Öll möguleg brot af slíkri gerð eru mjög mörg talsins, hins vegar má í raun sleppa öllum mínustölum í öðru hvoru menginu því annars tvíteljum við margar tölur. Sleppum mínustölunum í :math:`A` og þá eru möguleikarnir:

	 .. math::
			\dfrac{1}{1}, \;
			\dfrac{1}{2}, \;
			\dfrac{-1}{1}, \;
			\dfrac{-1}{2}, \;
			\dfrac{3}{1},\;
			\dfrac{3}{2}, \;
			\dfrac{-3}{1}, \;
			\dfrac{-3}{2}, \;
			\dfrac{9}{1}, \;
			\dfrac{9}{2}, \;
			\dfrac{-9}{1},\;
			\dfrac{-9}{2}\;

	 Stingum öllum þessum tölum inn í margliðuna :math:`r` (við erum búin að prófa :math:`1` og :math:`-1`):

	 .. math::
		\begin{aligned}
			r\left(\frac{1}{2}\right)& =-10 \\
			r\left(\frac{-1}{2}\right)&=-\frac{35}{4}\\
			r\left(\frac{3}{1}\right)&=r(3)=0\\
			r\left(\frac{3}{2}\right)&=-\frac{81}{4}\\
			r\left(\frac{-3}{1}\right)&=r(-3)=270\\
			r\left(\frac{-3}{2}\right)&=\frac{27}{2}\\
			r\left(\frac{9}{1}\right)&=r(9)=9306\\
			r\left(\frac{9}{2}\right)&=315\\
			r\left(\frac{-9}{1}\right)&=r(-9)=16596\\
			r\left(\frac{-9}{2}\right)&=\frac{4905}{4}
		\end{aligned}

	 Með þessari aðferð fundum við eina núllstöð, :math:`x=3`, því að :math:`r(3)=0`.

Pascal
------
Rifjum upp nokkrar mikilvægar :hover:`liðanir, liða`:

.. math::
	\begin{aligned}
	& (a+b)^2=a^2+2ab+b^2 \qquad &\textit{(ferningsregla fyrir summu)} \\
	& (a-b)^2=a^2-2ab+b^2 \qquad &\textit{(ferningsregla fyrir mismun)} \\
	& (a+b)(a-b)=a^2-b^2 \qquad &\textit{(samokaregla)} \\
	\end{aligned}

Prófum að liða :math:`(a+b)^3`:

.. math::
   \begin{aligned}
   (a+b)^3 &= (a+b)(a+b)(a+b) \\
   &= (a+b)(a^2+2ab+b^2) \\
   &= a^3 + 2a^2b +ab^2 +ba^2 +2ab^2 + b^3\\
   &=a^3+3a^2b+3ab^2+b^3\\
   \end{aligned}

Skoðum fleiri liðanir á forminu :math:`(a + b)^n`:

.. math::
   	(a + b)^0 = 1

.. math::
    (a + b)^1 = a + b

.. math::
    (a + b)^2 = a^2 + 2ab + b^2

.. math::
    (a + b)^3 = a^3 + 3a^2 b + 3a b^2 + b^3

.. math::
    (a + b)^4 = a^4 + 4 a^3 b + 6a^2 b^2 + 4ab^3 + b^4

.. math::
    (a + b)^5 = a^5 + 5a^4 b + 10a^3b^2 + 10a^2 b^3 + 5 ab^4 +b^5

Skoðum aðeins mynstrið sem er að verða til:

1. það eru alltaf :math:`n+1` liðir,

2. í hverjum lið er summa veldana jafn :math:`n`,

3. veldið á :math:`a` lækkar frá :math:`n` niður í :math:`0` og veldið á b hækkar frá :math:`0` upp í :math:`n`,

4. stuðlarnir fyrir framan liðina byrja á því að hækka og svo speglast þeir og lækka þegar komið er að miðju liðinum.

Þessir stuðlar mynda mynstur sem getur borgað sig að hafa á hreinu.

Mynstrið kallast **Pascal þríhyrningurinn**:

.. image:: ./myndir/pascal.svg
   :width: 80%
   :align: center

Hér eru stuðlarnir fyrir :math:`n=0,1,2,3,...,8`.

Hvert stak í Pascal þríhyrningnum er summa stakanna sem eru fyrir ofan það og auk þess er ásum raðað á endana.


.. image:: ./myndir/pascal2.svg
   :width: 80%
   :align: center

----------------------------------------------------

.. tip::
	Hvernig er liðuninn á :math:`(a+b)^9`?

	Hér er :math:`n=9` svo veldið á :math:`a` byrjar í 9 og lækkar síðan niður í núll.
	Veldið á :math:`b` byrjar í núll og hækkar upp í 9.

	Stuðlarnir fyrir framan liðina koma úr Pascal-þríhyrningnum.
	Á efri myndinni eru stuðlarnir fyrir :math:`n=8` í neðstu línunni.
	Reiknum næstu línu, stuðlana fyrir :math:`n=9` með því að leggja saman tölurnar fyrir ofan og bæta við einum á hvorn endann.

	Fáum t.d. :math:`70+56=126` svo stuðlarnir eru:

	.. figure:: ./myndir/pascald.svg
		:width: 60%
		:align: center

	Því er liðunin á :math:`(a+b)^9` :

	:math:`a^9 + 9a^8b + 36a^7b^2 + 84a^6b^3 + 126a^5b^4 + 126a^4b^5 + 84a^3b^6 + 36a^2b^7 +  9ab^8 + b^9`.


Það er hægt að reikna stuðlana án þess að teikna upp allan þríhyrninginn.
Þessir stuðlar eru kallaðir :hover:`tvíliðustuðlar, tvíliðustuðull` og fást úr eftirfarandi formúlu:

.. math::
   \begin{pmatrix} n \\ k \end{pmatrix} = \frac{n!}{k!(n-k)!}

Hér er :math:`n` veldið á :math:`(a+b)^n` eða númer raðar í þríhyrningnum og :math:`k` er númer liðsins sem við erum að skoða.
Athugum að :math:`k` tekur heiltölugildi frá núll upp í :math:`n` (oft segjum við að :math:`k` *hlaupi* frá núll upp í :math:`n` ).

.. warning::
	Athugið að við byrjum að telja línurnar og stökin í núlli!

Þegar tölur eru hrópmerktar með ! þá erum við að reikna :hover:`aðfeldi` þeirra og þá gildir

.. math::
   n! = \prod_{i=1}^{n}i = 1 \cdot 2 \cdot 3 \cdot ... \cdot (n-1) \cdot n

.. warning::
   Núll hrópmerkt er skilgreint sem :math:`0!=1`

.. tip::
	 :math:`5! = 1\cdot 2\cdot 3\cdot 4\cdot 5 = 120`

Því getum við skrifað liðunina á margliðum á forminu :math:`(a+b)^n` sem

.. math::
	\begin{aligned}
		(a+b)^n &= \begin{pmatrix} n \\ 0 \end{pmatrix} a^nb^0 + \begin{pmatrix} n \\ 1 \end{pmatrix} a^{n-1}b^1 + \begin{pmatrix} n \\ 2 \end{pmatrix} a^{n-2}b^2 + \\ &...+ \begin{pmatrix} n \\ n-2 \end{pmatrix} a^2b^{n-2} + \begin{pmatrix} n \\ n-1 \end{pmatrix}a^1b^{n-1} + \begin{pmatrix} n \\ n \end{pmatrix}a^0b^n
	\end{aligned}

.. tip::
	Skoðum liðunina á  :math:`(a+b)^4` . Hér er :math:`n=4` svo fyrsti stuðullin við :math:`a^4\cdot b^0 = a^4` er :math:`\begin{pmatrix} 4 \\ 0 \end{pmatrix}`

	.. math::
	    \begin{aligned}
	     \begin{pmatrix} 4 \\ 0 \end{pmatrix} &= \frac{4!}{0!(4-0)!} \\
	     &= \frac{4!}{4!}\\
	     &= \frac{1\cdot 2\cdot 3\cdot 4}{1\cdot 2\cdot 3\cdot 4} \\
	     &= 1
	     \end{aligned}

	Næsti er :math:`\begin{pmatrix} 4 \\ 1 \end{pmatrix} a^3 b`

	.. math::
	    \begin{aligned}
	     \begin{pmatrix} 4 \\ 1 \end{pmatrix} &= \frac{4!}{1!(4-1)!} \\
	     &= \frac{4!}{3!}\\
	     &= \frac{1\cdot 2 \cdot 3\cdot 4}{1\cdot 2\cdot 3} \\
	     &= \frac{24}{6} \\
	     &= 4
	     \end{aligned}

	Nú  :math:`\begin{pmatrix} 4 \\ 2 \end{pmatrix} a^3 b`

	.. math::
	       \begin{aligned}
	     \begin{pmatrix} 4 \\ 2 \end{pmatrix} &= \frac{4!}{2!(4-2)!} \\
	     &= \frac{4!}{2!(2)!}\\
	     &= \frac{1\cdot 2\cdot 3\cdot 4}{1\cdot 2 \cdot(1 \cdot 2)} \\
	     &= \frac{24}{4} \\
	     &= 6
	     \end{aligned}

	og svo framvegis.

	Fáum þá

	.. math::
	    \begin{aligned}
	    (a + b)^4 &= \begin{pmatrix} 4 \\ 0 \end{pmatrix} a^4  + \begin{pmatrix} 4 \\ 1 \end{pmatrix} a^3b  + \begin{pmatrix} 4 \\ 2 \end{pmatrix}a^2b^2  + \begin{pmatrix} 4 \\ 3 \end{pmatrix} ab^3  + \begin{pmatrix} 4 \\ 4 \end{pmatrix} b^4 \\
	    &= \quad a^4 \quad +\quad 4 a^3b \quad + \quad 6 a^2b^2 \quad + \quad 4 ab^3 \quad + \quad b^4
	    \end{aligned}

	Sjáum að stuðlarnir eru einmitt fjórða línan í Pascal þríhyrningnum.

Hér sjáum við samantekt af tvíliðustuðlum upp í :math:`n=6` :

.. image:: ./myndir/pascalbin.svg
   :width: 110%
   :align: center


.. note::
	Takið eftir að eftirfarandi gildir alltaf:

	.. math::
		\begin{pmatrix} n \\ 0 \end{pmatrix} = \begin{pmatrix} n \\ n \end{pmatrix} = 1
