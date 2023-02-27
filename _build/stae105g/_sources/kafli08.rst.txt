Inngagur að diffurjöfnur
========================

.. admonition:: Nauðsynleg undirstaða
  :class: athugasemd

	- Föll

	- Afleiður

------

.. epigraph::

  *It’s the job that’s never started as takes longest to finish.*

  \– Samwise Gamgee, The Fellowship of the Ring

------

Grunnatriði
------------

Í kaflanum um hagnýtingar á heildun var snert á diffurjöfnum. Hér munum við skoða
þær aðeins nánar.

Skilgreining: Diffurjafna
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

	*Diffurjafna* er jafna sem sem inniheldur eitthvað óþekkt fall og eina eða fleiri
	af afleiðum þess. Lausn diffurjöfnu er fallið :math:`f` sem uppfyllir jöfnuna þegar
	fallinu og viðeigandi afleiðum er stungið inn fyrir óþekkta fallið og afleiður þess.

Dæmi: Diffurjafna
~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Göngum úr skugga um að fallið :math:`y=e^{-3x}+2x+3` sé lausn diffurjöfnunnar

	.. math:: y' + 3y = 6x + 11.

.. admonition:: Lausn
  :class: daemi, dropdown

	Við gerum þetta með því að stinga fallinu inn í jöfnuna. Byrjum á því að finna :math:`y'`.

	.. math:: y' = -3e^{-3x}+2.

	Stingum þessu nú inn í vinstri hlið jöfnunnar og fáum

	 .. math:: -3e^{-3x}+2 + 3(e^{-3x}+2x+3) = -3e^{-3x} + 2 -3e^{-3x} + 6x + 9 = 6x+11.

	Sjáum að þetta stemmir við khægri hlið diffurjöfnunnar. Því er fallið
	:math:`y=e^{-3x}+2x+3` lausn á diffurjöfnunni.

Skilgreining: Stig diffurjöfnu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

	*Stig diffurjöfnu* er hæsta stig afleiðu óþekkta fallsins sem kemur fyrir í jöfnunni.

Dæmi: Stig diffurjöfnu
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	 	#. Diffurjafnan :math:`2y''+3y+4=e^x` er af 2. stigi.

		#. Diffurjafnan :math:`y'''+4y=0` er af 3. stigi.

		#. Diffurjafnan :math:`y'=6x^2` er af 1. stigi.

Almennar lausnir og sérlausnir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vegna þess eiginleika diffrunar að fastar diffrast í burtu fæst að ef
:math:`y=f(x)` er lausn á diffurjöfnunni :math:`y'=g(x)` þá er :math:`y=f(x)+C`
það einnig, þar sem báðar jöfnur hafa afleiðuna :math:`y'=f'(x)`.
Fallið :math:`y=f(x)+C` köllum við *almenna lausn diffurjöfnunnar*. Ef gerðar
eru einhverjar kröfur um eiginleika fallsins, t.d. að það taki ákveðið gildi í
ákveðnum punkti, sem gerir það að verkum að aðeins einhver tiltekinn fasti :math:`C \in \mathbb{R}`
uppfyllir jöfnuna þá er sú lausn kölluð *sérlausn diffurjöfnunnar*.

Dæmi: Almenn lausn og sérlausn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Lítum á einfalda diffurjöfnu, t.a.m.

	.. math:: y' = 2x.

	Þessi diffurjafna er aðgreinanleg og
	því getum við heildað báðar hliðar hennar til að sjá að

	.. math:: y = x^2 + C.

	Hér er :math:`y=x^2+C` almenn lausn diffurjöfnunnar. Gerum nú ráð fyrir að gefið
	sé að fallið þurfi að uppfylla diffurjöfnuna

	.. math:: y' = 2x

	auk þess að fara í gegnum punktinn :math:`(2,7)`. Við vitum að almenn lausn diffurjöfnunnar er
	:math:`y=x^2+C` en sker aðeins punktinn :math:`(2,7)` ef :math:`C=3`. Auðvelt er
	að sýna fram á það með því að stinga :math:`y=3` og :math:`x=0` inn í jöfnuna
	og einangra :math:`C`:

	.. math::  7 = 2^2 + C \Leftrightarrow C = 3.

	Fyrir þetta skilyrði segjum við að :math:`y=x^2+3` sé sérlausn.

Upphafsgildisverkefni
~~~~~~~~~~~~~~~~~~~~~~

Skilyrði eins og að fall þurfi að fara í gegnum ákveðinn punkt er formlega nefnt
upphafsskilyrði og diffurjöfnur með upphafsskilyrði nefnast *upphafsgildisverkefni*.
Þau eru yfirleitt gefin á forminu

.. math::
	\begin{cases}
  	y' = g(x,y)\\
		y(a_1)=b_1, y'(a_2)=b_2
	\end{cases}

Þar sem :math:`a_1,a_2,b_1,b_2 \in \mathbb{R}` og :math:`g(x,y)` er eitthvað fall.

Dæmi: Upphafsgildisverkefni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Leysum upphafsgildisverkefnið

	.. math::
		\begin{cases}
	  	y' = 3e^x+2x+3\\
			y(0)=5
		\end{cases}

.. admonition:: Lausn
  :class: daemi, dropdown

	Þessi diffurjafna er aðgreinanleg og við getum því heildað báðar hliðar hennar
	til að fá að

	.. math:: y = 3e^x + \frac{1}{3}x^3 - 4x + C

	sé almenn lausn hennar. Stingum nú upphafsgildinu :math:`y(0)=5` inn til
	að finna sérlausnina, þ.e.

	.. math::
		\begin{align}
			5 &= 3e^0 + \frac{1}{3}\cdot 0^3 - 4\cdot 0 + C\\
			5 &= 3 + C\\
			C &= 2.
		\end{align}

	Sérlausn diffurjöfnunnar, þ.e. lausn upphafsgildisverkefnisins er því :math:`y=3e^x + \frac{1}{3}x^3-4x+2`.

--------

Aðskilnaður breytistærða
-------------------------

Aðskilnaður breytistærða er það þegar hægt er að umrita diffurjöfnu þannig að
önnur hlið jöfnunnar innihaldi aðra breytistærðina og hin hliðin innihaldi hina breytistærðina.
Yfirleitt eru breytistærðirnar breyturnar :math:`x` og :math:`y` en ekkert er því
til fyrirstöðu að nota aðrar breytistærðir. Ef hægt er að skilja breytistærðirnar að
með þessum hætti er diffurjafnan kölluð aðgreinanleg. Aðgreinanlegar diffurjöfnur
eru sérlega þægilegar þar sem þær hafa þann eiginleika að þegar búið er að skilja
breytistærðirnar að þá má heilda báðar hliðar jöfnunnar til að ákvarða lausn diffurjöfnunnar.

Skilgreining: Aðgreinanleg diffurjafna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

	Diffurjafna nefnist *aðgreinanleg* ef hægt er að skrifa hana á forminu

	.. math:: y'=f(x)g(y).

Dæmi: Aðskilnaður breytistærða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Finnum lausn upphafsgildisverkefnisins

	.. math::
		\begin{cases}
	  	y' = (2x+3)(y^2-3)\\
			y(0)=1
		\end{cases}

	með því að nota aðskilnað breytistærða.

.. admonition:: Lausn
  :class: daemi, dropdown

	Lítum á diffurjöfnuna

	.. math:: y' = (2x+3)(y^2-4).

	Ef við deilum beggja vegna jafnaðarmerkisins með :math:`(y^2-4)` fæst

	.. math:: \frac{y'}{y^2-4}=2x+3.

	Ljóst er að við höfum nú greint breytistærðirnar að þar sem öll :math:`x`-in
	eru hægra megin jafnaðarmerkisins en öll :math:`y`-in vinstra megin. Skiptum :math:`y'`
	út fyrir :math:`\frac{dy}{dx}` og margföldum báðum megin með :math:`dx` til að fá

	.. math:: \frac{dy}{y^2-4}=2x+3 dx.

	Nú fæst að

	.. math:: \int \frac{dy}{y^2-4}= \int (2x+3) dx

	sem með stofnbrotaliðun má umrita sem

	.. math:: \frac{1}{4} \int \left( \frac{1}{y-2} - \frac{1}{y+2}\right) dy = \int (2x+3) dx.

	Ef við heildum nú báðar hliðar fæst

	.. math:: \frac{1}{4} \left( \ln|y-2| - \ln|y+2| \right) = x^3+3x+C.

	Ef við lengjum báðar hliðar með 4 og notum lograreglur má fá

	.. math:: \ln\left|\frac{y-2}{y+2}\right|= 4x^2+12x+C.

	Athugum að þar sem :math:`C` er bara einhver fasti þá skiptir engu máli hvort ritað
	sé :math:`4C` eða :math:`C`. Þegar öllu er á botninn hvolft þá er :math:`4C` líka
	bara einhver fasti. Við getum nú beitt veldisvísifallinu á báðar hliðar til að fá

	.. math:: \left|\frac{y-2}{y+2}\right| = Ce^{4x^2+12x}

	þar sem við notfærum okkur að :math:`e^{C}` er einnig bara einhver (jákvæður)
	fasti sem við getum haldið áfram að nota :math:`C` til að tákna. Með því að
	leyfa :math:`C` að vera bæði neikvæður og jákvæður fasti getum við fell niður
	algildistáknið og með því að lengja báðar hliðar jöfnunnar með :math:`(y+2)` fæst

	.. math:: y-2 = C(y+2)e^{4x^2+12}.

	Ef við einangrum loks :math:`y` fæst

	.. math:: y= \frac{2+2Ce^{4x^2+12x}}{1-Ce^{4x^2+12x}}.

	Til að finna gildið á
	:math:`C` notum við upphafsgildið :math:`y(0)=1`. Stingum inn :math:`y=1` og :math:`x=0`
	í jöfnuna og einangrum :math:`C`. Útreikningar gefa að :math:`C=-3`. Lausn upphafsgildisverkefnisins
	er því

	.. math:: y= \frac{2-6e^{4x^2+12x}}{1+3xe^{4x^2+12x}}.

.. admonition:: Athugasemd
  :class: athugasemd

	Það er gamalt trikk í stærðfræði, þegar unnið er með óskilgreinda fasta
	í útreikningum að halda bara áfram að nota fastann :math:`C` í gegnum alla
	útreikningana, í stað þess að finna sífellt upp á nýjum bókstöfum
	til að tákna nýja, óskilgreinda fasta. Stafurinn :math:`C` er þá látinn halda sér, því
	þar sem hann var óskilgreindur til að byrja með þá breytir það ekki öllu
	hann megi t.a.m. skrifa sem margfeldi af 4 eða sem :math:`e` í einhverju veldi.

--------

Lógistíska jafnan
------------------

Til þess að búa til líkan sem lýsir vexti þýðis í gegnum diffurjöfnur þarf að
byrja á því að kynna til leiks nokkur hugtök. Breytan :math:`t` táknar tíma. Tímaeiningin
má vera hver sem er; sekúndur, mínútur, klukkustundir, dagar, ár og fer það einungis
eftir eðli verkefnisins. Breytan :math:`P` mun tákna þýðið. Þar sem fjöldi í
þýði breytist með tíma má tákna það sem fall af tíma, þ.e. :math:`P(t)`. Ef :math:`P(t)`
er diffranlegt fall þá hefur það fyrstu afleiðuna :math:`\frac{dP}{dt}`, sem
er táknræn fyrir breytingu á fjölda þýðisins sem fall af tíma.

Skilgreining: Burðargeta
~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

	*Burðargeta* lífvera í gefnu umhverfi er skilgreint sem hámarksfjöldinn þeirra
	lífvera sem umhverfið getur viðhaldið um ókomna tíð.

	Við notum stafinn :math:`K` til að tákna burðargetu umhverfisins og vaxtarhraða
	þýðisins táknum við með :math:`r`.

Skilgreining: Lógistísk diffurjafna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

	Látum :math:`K` vera burðargetu lífvera í gefnu umhverfi og látum :math:`r` vera
	rauntölu sem táknar vaxtarhraðann. Fallið :math:`P(t)` lýsir fjölda þessara lífvera
	sem falli af tíma og fastinn :math:`P_0` táknar upphafsástandi þýðisins (fjölda
	lífvera í þýðinu á tímapunktinum :math:`t=0`). Þá má setja *lógistísku diffurjöfnuna*
	fram með

	.. math:: \frac{dP}{dt} = rP\left(1-\frac{P}{K}\right).

	Ef lógistíska diffurjafnan er pöruð með upphafsgildinu :math:`P(0)=0` myndar
	hún upphafsgildsiverkefni fyrir :math:`P(t)`.

Setning: Lausn lógistískra diffurjafna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Lítum á lógistíska diffurjöfnu með upphafsfjöldann :math:`P_0` með burðargetu
	:math:`K` og vaxtarhraða :math:`r`. Lausnin á samsvarandi upphafsgildisverkefni
	er gefin með

	.. math:: P(t) = \frac{P_0Ke^{rt}}{(K-P_0)+P_0e^{rt}}.

Dæmi: Lógistísk diffurjafna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Gerum ráð fyrir að í þýði hreindýra séu 900.000 hreindýr. Líffræðingur spáði fyrir að
	fjölgun í stofninu fylgi veldisvísisvexti og stofninn tvöfaldist á þriggja ára fresti við
	kjöraðstæður, sem er sambærilegt því að segja að vaxtarhraðinn sé

	.. math:: r = \frac{\ln(2)}{3}\approx 0,2311.

	Ef svæðið sem hreindýrin lifa á er 39.732 ferkílómetrar og hver ferkílómetri getur
	hýst í mestalagi 27 hreindýr þá er burðargeta svæðsisins

	.. math:: K = 39.732 \cdot 27.1.072.764.

	Við skulum:

		a) Nota lógistískt líkan til að ákvarða upphafsgildisverkefnið.

		b) Leysa upphafsgildisverkefnið.

		c) Ákvarða hver fjöldi hreindýra verður eftir 3 ár.

		d) Finna hvenær stofninn mun ná stærðinni 1.200.000.

ALVÖRU:

.. admonition:: Lausn
  :class: daemi, dropdown

	a) Lausn:
		Upphafsgildisverkefnið er

		.. math::
			\begin{cases}
				\frac{dP}{dt} = 0,2311P\left(1-\frac{P}{1.072.764}\right)\\
  				P(0)=900.000
  			\end{cases}

	b) Lausn:
		Við getum notað aðskilnað breytistærða til að leysa jöfnuna. Með umritun á diffurjönfunni getum við fengið að

		.. math:: \frac{dP}{P(1.072.765-P)} = \frac{0,2311}{1.072.764}dt.

		Leysum þetta. Þetta er aðgreinanleg diffurjafna. Við getum því heildað báðar hliðar og fengið

		.. math::
			\begin{aligned}
				 && \frac{dP}{P(1.072.765-P)} &= \frac{0,2311}{1.072.764}dt\\
				\iff && \int \frac{dP}{P(1.072.765-P)} &= \int \frac{0,2311}{1.072.764}dt\\
				\iff && \frac{1}{1.072.764}\left(\ln|P| - \ln|1.072.764-P|\right) &= \frac{0,2311t}{1.072.764}+C.
			\end{aligned}

		Einangrum nú :math:`P` og fáum

		.. math:: P(t) = \frac{1.072.764Ce^{0,2311t}}{1+Ce^{0,2311t}}.

		Notum nú upphafsgildið :math:`P(0)=900.000` til að ákvarða gildi fastans :math:`C`.

		.. math::
			\begin{align}
				P(0) &= \frac{1.072.764Ce^{0,2311 \cdot 0}}{1+Ce^{0,2311 \cdot 0}}\\
				900.000 &= \frac{1.072.764C}{1+C}\\
				C &= \frac{25.000}{4799}\\
				C & \approx 5,209.
			\end{align}

		Fáum því, með örlítilli umritun, að

		.. math:: P(t) = \frac{1.072.764 e^{0,2311t}}{0,19196+e^{0,2311t}}.

	c. Lausn:
		Til að finna hver fjöldinn verður eftir 3 ár stingum við einfaldlega :math:`t=3`
		inn í jöfnuna og fáum

		.. math:: P(3) = \frac{1.072.764 e^{0,2311 \cdot 3}}{0,19196+e^{0,2311 \cdot 3}} \approx 978.830.

		Svo fjöldi hreindýra eftir 3 ár verður u.þ.b. 978.830 hreindýr. Við sjáum að
		samkvæmt lógistíska líkaninu er það langt því frá að vera tvöföldun á stofninum.

		d. Ef stofninn nær 1.200.000 hreindýrum þá væri nýja upphafsgildisverkefnið

		.. math::
			\begin{cases}
				\frac{dP}{dt}=0,2311P\left(1-\frac{P}{1.072.764}\right)\\
				P(0)=1.200.000\\
			\end{cases}

		sem hefur sömu almennu lausn og við fundum í b. lið.

		.. math:: P(t) = \frac{1.072.764Ce^{0,2311t}}{1+Ce^{0,2311t}}.

		Notum nýja upphafsgildið til að ákvarða :math:`C`. Fáum

		.. math::
			\begin{align}
				P(0) &= \frac{1.072.764Ce^{0,2311 \cdot 0}}{1+Ce^{0,2311 \cdot 0}}\\
				1.200.000 &= \frac{1.072.764C}{1+C}\\
				C & \approx -9.431.
			\end{align}

		Því fæst að

		.. math:: P(t) \approx \frac{10.117.551 e^{0,2311t}}{9,43129 e^{0,2311t}-1}.

		Sjáum á grafi fallsins hér að neðan að það fækkar í stofninum.

		.. image:: ./myndir/kafli08/PMA_hreindyr.png
			:align: center
			:width: 50%

-----

Fyrsta stigs línulegar diffurjöfnur
------------------------------------

Skilgreining: Línuleg diffurjafna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

	Fyrsta stigs diffurjafna er *línuleg* ef hana má rita  á forminu

	.. math:: a(x)y'+b(x)y=c(x)

	þar sem :math:`a(x),b(x),c(x)` eru einhver föll.

Skilgreining: Staðalform
~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

	Við segjum að fyrsta stigs línuleg diffurjafan sé á *staðalformi* ef
	hún er sett fram sem

	.. math:: y' + \frac{b(x)}{a(x)}y = \frac{c(x)}{a(x)}.

	Þetta má einnig setja fram með því að láta :math:`p(x)=\frac{b(x)}{a(x)}` og
	:math:`q(x)=\frac{c(x)}{a(x)}` og rita

	.. math:: y' + p(x)y = q(x).

Dæmi: Staðalform diffurjöfnu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Lítum á diffurjöfnuna

	.. math:: \frac{3xy'}{4y-3}=2

	þar sem :math:`x\neq 0` og :math:`y \neq \frac{3}{4}`. Setjum hana á staðalform.

.. admonition:: Lausn
  :class: daemi, dropdown

	Fáum

	.. math::
		\begin{align}
			\frac{3xy'}{4y-3}&=2\\
			3xy' = 2(4y-3)\\
			3xy' = 8y-6\\
			y' = \frac{8y}{3x}-\frac{6}{3x}\\
			y'-\frac{8y}{3x}=-\frac{2}{x}.
		\end{align}

	Þar sem við gerðum upphaflega ráð fyrir að :math:`x \neq 0` var okkur óhætt að
	deila í gegnum jöfnuna með :math:`x` og fá hana þannig yfir á staðalform. Ef
	:math:`x=0` í upprunalegu jöfnunni fæst :math:`0=2` sem er augljóslega ekki rétt.
	Í þessari jöfnu er því :math:`p(x)=-\frac{8y}{3x}` og :math:`q(x)=-\frac{2}{x}`.

Setning: Lausa fyrsta stigs línulegra diffurjafna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Línulega fyrsta stigs diffurjafnan

	.. math:: y' + p(x)y = q(x)

	hefur lausnina

	.. math:: y(x) = e^{-\mu(x)}\int e^{\mu(x)}q(x)dx

	þar sem :math:`\mu(x)=\int p(x) dx`, þ.e. :math:`\mu(x)` er eitthvað stofnfall
	fyrir :math:`p(x)`.

.. admonition:: Aðvörun
  :class: advorun

	Þessi setning er sett örlítið öðruvísi fram í bókinni. Við notum þessa framsetningu
	hér til að halda samræmi við aðra stærðfræðigreiningaráfanga Háskóla Íslands.
	Þetta er í grunninn sama jafnan svo ekki skiptir máli hvor þeirra er notuð, báðar
	gefa lausn við diffurjöfnunni.

Dæmi: Lausn línulegrar fyrsta stigs diffurjöfnu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Lítum á línulegu fyrsta stigs diffurjöfnuna

	.. math:: xy' + 3y = 4x^2-3x.

	og gerum ráði fyrir að :math:`x>0`.
	Notum lausnarformúlu fyrsta stigs línulegra diffurjafna til að leysa hana.

.. admonition:: Lausn
  :class: daemi, dropdown

	Við þurfum að byrja á því að koma diffurjöfnunni á staðalfrom sitt.
	Fáum að

	.. math::
		\begin{align}
			xy' + 3y &= 4x^2-3x\\
			y' + \frac{3}{x}y &= 4x - 3\\
		\end{align}

	Sjáum að hér er :math:`p(x)=\frac{3}{x}` og :math:`q(x)=4x - 3`. Finnum nú
	eitthvað stofnfall fyrir :math:`p(x)`.

	.. math:: \mu(x)=\int p(x) dx = \int \frac{3}{x} dx = 3\ln|x| = 3\ln(x).

	Athugum að hér má sleppa algildistákninu af því að við gerðum ráð fyrir því
	í byrjun dæmisins að :math:`x>0` og algildistáknið hefur aðeins áhrif á
	neikvæðar tölur. Lausn diffurjöfnunnar er því

	.. math::
		\begin{align}
			y(x) &= e^{-3\ln(x)}\int e^{3\ln(x)}(4x - 3)dx\\
			&= e^{\ln(x^{-3})}\int e^{\ln(x^3)}(4x - 3)dx\\
			&= x^{-3}\int x^3(4x - 3)dx\\
			&= x^{-3}\int (4x^4 - 3x^3 )dx\\
			&= x^{-3} \left(\frac{4}{5}x^5 - \frac{3}{4}x^4+C\right)\\
			&= \frac{4}{5}x^2 - \frac{3}{4}x+\frac{C}{x^3}
		\end{align}

	Svo lausnin á diffurjöfnunni er :math:`y(x)=\frac{4}{5}x^2 - \frac{3}{4}x+\frac{C}{x^3}`.
