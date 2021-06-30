Heildun
=======

.. note::
	**Nauðsynleg undirstaða**

	- :ref:`Markgildi`. Sjá einnig `undirstöðuatriði um markgildi <https://notendur.hi.is/~guh96/edbook-undirb/undirbuningur_stae/Kafli10.html>`_.

	- :ref:`Afleiður <afleidur>`.  Sjá einnig `undirstöðuatriði um afleiður <https://notendur.hi.is/~guh96/edbook-undirb/undirbuningur_stae/Kafli11.html>`_.

	- :ref:`Reiknireglur fyrir afleiður <Setning 3.3.1>`, sér í lagi :ref:`keðjureglan <kedjuregla>`.

------


.. epigraph::

  *"You cannot pass,” he said. The orcs stood still, and a dead silence fell. “I am a servant of the Secret Fire, wielder of the flame of Anor. You cannot pass. The dark fire will not avail you, flame of Udûn. Go back to the Shadow! You cannot pass."*

  \– Gandalf, The Fellowship of the Ring

------

.. epigraph::

	*But you can pass this course.*

	\– Hulda

------


.. index::
    heildi; jákvæðs falls
    heildi
    heildismörk
    fall; heildanlegt
    flatarmál

.. _heildun:


.. index::
    stofnfall

Stofnföll
---------

Andstæðan við diffrun
~~~~~~~~~~~~~~~~~~~~~~

Við höfum nú skoðað hvernig hægt er að finna afleiður ýmissa falla. En ef okkur
er gefin afleiða, hvernig getum við vitað hvert upprunalega fallið var? Ef við
vitum einungis afleiðu falls þá er talað um að finna *stofnfallið*.

Skilgreining: Stofnfall
~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera fall sem er skilgreint á bili :math:`I`. Fall
:math:`F` kallast :hover:`stofnfall` fyrir :math:`f` á
bilinu :math:`I` ef :math:`F'(x)=f(x)` fyrir öll :math:`x` í :math:`I`.

Setning: Form stofnalla
~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`F` vera stofnfall :math:`f` yfir bilið :math:`I`. Þá gildi:

	#. Fyrir sérhvern fasta :math:`C` er fallið :math:`F(x)+C` einnig stofnfall fyrir :math:`f` yfir :math:`I`.

	#. Ef :math:`G` er stofnfall :math:`f` yfir :math:`I` þá er til fasti :math:`C` þannig að :math:`G(x)=F(x)+C` yfir :math:`I`.


Með öðrum orðum þá er :math:`F(x)+C` almennt form stofnfalla fyrir :math:`f` yfir :math:`I`.


.. tip::
	Þar sem sérhvert fall :math:`f(x)` sem á sér stofnfall á sér fleiri en eitt stofnfall
	þá segjum við að stofnföll séu *ekki ótvírætt ákvörðuð*. Yfirleitt leyfum við okkur þó
	að velja fastann :math:`C=0` og tölum því um að :math:`F(x)=x^2` sé stofnfallið fyrir :math:`f(x)=2x`.
	Þó er ekkert því til fyrirstöðu að velja :math:`C=1` og segja að :math:`F(x)=x^2+1` sé
	stofnfall fyrir :math:`f(x)=2x`.

Dæmi: Stofnfall
~~~~~~~~~~~~~~~

	#. :math:`f(x)=3x^2` á sér stofnfallði :math:`F(x)=x^3` af því :math:`F'(x)=3x^2`.

	#. :math:`f(x)=\frac{1}{x}` á sér stofnfallði :math:`F(x)=\ln(x)` af því :math:`F'(x)=\frac{1}{x}`.

	#. :math:`f(x)=\cos(x)` á sér stofnfallði :math:`F(x)=\sin(x)` af því :math:`F'(x)=\cos(x)`.

	#. :math:`f(x)=e^x` á sér stofnfallði :math:`F(x)=e^x` af því :math:`F'(x)=e^x`.

Óákveðin heildi
----------------

Lítum nú á formlega rithátt stofnfalla og skoðum eiginleika þeirra.
Þessir eiginleikar gera okkur kleyft að finna stofnföll flóknari falla.
Ef við höfum fall :math:`f` þá má nota ritháttinn :math:`f'(x)` eða
:math:`\frac{df}{dx}` til að tákna afleiðu fallsins. Ef :math:`F` er
stofnfall :math:`f`, þá getum við sagt að :math:`F(x)+C` sé algengasta leiðin
til að tákna stofnfall :math:`f` og ritað


.. math:: \int f(x) dx = F(x) + C.

Táknið :math:`\int` er kallað *heildistákn* og :math:`\int f(x) dx` er kallað
*óákveðið heildi*.

.. tip::
	Mismunandi er eftir skólum hvaða orð eru notuð til að tala um *derivatives* og
	*antiderivatives/integrals*. Sem dæmi má nefna:

	#. Í MR og víðar er talað um að diffra og tegra. Nanforðin eru þá diffur og tegur.

	#. Víða er talað um að heilda og deilda og nafnorðin heildun og deildun, sem formlegri tilraun til að íslenska orðin, en orðið diffur kemur af orðinu **differ**\ ernation og tegur er dregið af orðinu in\ **tegra**\ l.

	#. Víðast hvar eru orðin afleiða og stofnfall notuð að einhverju leyti.

Skilgreining: Óákveðið heildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fyrir fallið :math:`f` er *óákveðna heildi* fallsins táknað

.. math:: \int f(x) dx.

Ef :math:`F` er stofnfall :math:`f` þá gildir að

.. math:: \int f(x) dx = F(x)+C.

Hér er :math:`f(x)` kallað heildisstofn og :math:`x` breytan sem heildar er
með tilliti til.

Setning: Veldisregla fyrir heildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`n \neq -1` gildir að

.. math:: \int x^n dx = \frac{x^{n+1}}{n+1}+C.

Ábending: Gagnleg óeiginleg heildi og afleiður
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::
	.. csv-table:: Óeiginleg heildi og afleiður sem gott er að kannast við
		:widths: 50, 50

		"**Afleiða**","**Óeiginlegt heildi**"
		":math:`\frac{d}{dx} k = 0`", ":math:`\int k dx = kx+C`"
		":math:`\frac{d}{dx} x^n = nx^{n-1}`", ":math:`\int x^n dx = \frac{x^{n+1}}{n+1}+C \text{ fyrir } n \neq -1`"
		":math:`\frac{d}{dx} \ln(|x|)=\frac{1}{x}`", ":math:`\int \frac{1}{x} dx = \ln(|x|)+C`"
		":math:`\frac{d}{dx} e^x = e^x`", ":math:`\int e^x dx = e^x+C`"
		":math:`\frac{d}{dx} \sin(x) = \cos(x)`", ":math:`\int \cos(x) dx = \sin(x)+C`"
		":math:`\frac{d}{dx} \cos(x) = -\sin(x)`", ":math:`\int \sin(x) dx = -\cos(x)+C`"
		":math:`\frac{d}{dx} \tan(x) = \frac{1}{\cos^2(x)}`", ":math:`\int e^x dx = e^x+C`"
		":math:`\frac{d}{dx} \sin^{-1}(x) = \frac{1}{\sqrt{1-x^2}}`", ":math:`\int \frac{1}{\sqrt{1-x^2}} dx = \sin^{-1}(x)+C`"
		":math:`\frac{d}{dx} \cos^{-1}(x) = -\frac{1}{\sqrt{1-x^2}}`", ":math:`\int -\frac{1}{\sqrt{1-x^2}} dx = \cos^{-1}(x)+C`"
		":math:`\frac{d}{dx} \tan^{-1}(x) = \frac{1}{1+x^2}`", ":math:`\int \frac{1}{1+x^2} dx = \tan^{-1}(x)+C`"

Reiknireglur: Óeiginleg heildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

	Látum :math:`F` og :math:`G` vera stofnföll :math:`f` og :math:`g` og :math:`k \in \mathbb{R}`.

		#. **Summuregla:** :math:`\int (f(x) \pm g(x)) dx=  F(x) \pm G(x) + C`

		#. **Margföldun með fasta:** :math:`\int kf(x) dx = k F(x) + C`

Dæmi: Summuregla
~~~~~~~~~~~~~~~~

.. math::	\int \frac{x+1}{x} dx = \int \left(\frac{x}{x}+\frac{1}{x}\right) dx = \int \left(1 + \frac{1}{x}\right) dx = x + \ln(|x|)+C

Dæmi: Margföldun með fasta
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: \int \frac{4}{x^2} dx = \int 4x^{-2} dx = -4x^{-1} + C

Diffurjöfnur
-------------

Diffurjafna er jafna sem sýnir tengsl eins eða fleiri falla við afleiður sínar. Til dæmis

.. math:: f'(x)=2xe^x.

Það að leysa diffurjöfnu snýst um að ákvarða fallið eða föllin. Lausnin við diffurjöfnunni
hér að ofan er t.a.m.

.. math:: f(x)=x2e^x-2e^x+C

þar sem :math:`C` er fasti. Diffurjöfnur hafa almennt ekki ótvírætt ákvarðaðar lausnir nema
gefnar séu fleiri upplýsingar. Ef við hefðum t.a.m. fengið þær upplýsingar að
:math:`f(0)=3` þá gætum við séð að

.. math:: f(0)=0\cdot 2e^0 - 2e^0 + C = -2 + C = 3.

Með því að einangra :math:`C` fæst að :math:`C=3+2 = 5` og lausnin væri því


.. math:: f(x)=x2e^x-2e^x+5.

þessar upplýsingar, þ.e. :math:`f(0)=5` eru kallaðar *upphafgildi* og eru svona
diffurjöfnur því gjarnan kallaðar upphafsgildisverkefni.

Diffurjöfnur eru eitt mikilvægasta málefni stærðfræðigreiningar og eitt helsta viðfangsefni þeirra sem hagnýta
stærðfræði eins og verkfræðingar og eðlisfræðingar. Almennt er *mjög erfitt*
að leysa diffurjöfnur og eru margar þeirra jafnvel óleysanlegar með analytískum
aðferðum. Þó er auðveldara að leysa sumar gerðir af diffurjöfnum en aðrar.

.. warning::

 	Við munum hér kafa mjög grunnt í óravíddir diffurjafna og aðeins skoða þær
	allra auðveldustu. Mikilvægt er að hafa í huga að diffurjöfnur eru gríðarlega mikilvægar í stærðfræði
	og margt sem verður látið ósagt um þær. Þetta á einungis að gefa nemendum
	hugmynd um hvernig hægt er að nota heildi á hagnýtan hátt til að leysa raunveruleg
	verkefni.


Aðgreinanlegar diffurjöfnur
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gefum okkur að eitthvað fall :math:`y=F(x)` uppfylli að :math:`F'(x)=f(x)`, þ.e.
orðum þá er :math:`F(x)` stofnfall :math:`f(x)`. Við vitume ekki hvað :math:`F(x)` er
en við þekkjum :math:`f(x)`. Við gætum einnig ritað þetta svona

.. math:: \frac{dy}{dx}=f(x).

Svona diffurjafna kallst *aðgreinanleg diffurjafna* af því hana má skrifa sem

.. math:: dy = f(x)dx

þar sem við erum einungis með :math:`y` vinstra megin og einungis með :math:`x` hægra megin.
Við höfum m.ö.o. aðskilið breytistærðir diffurjöfnunnar. Þetta er einstaklega þægileg
gerð diffurjafna því þetta má leysa með því að heilda báðar hliðar jöfnunnar.

.. math:: \int dy = \int f(x) dx \Leftrightarrow y = \int f(x) dx

og þar sem að :math:`y=F(x)` þá þekkjum við nú gildi :math:`F(x)`, af því gefnu
að við kunnum að heilda :math:`f(x)`.

Dæmi: Aðgreinanleg diffurjafna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lítum á diffurjöfnuna :math:`\frac{dy}{dx} = 6x^2`. Hún er aðgreinanleg þar sem
að hana má rita sem

.. math:: dy = 6x^2 dx.

Við getum nú heildað báðar hliðar og fengið að

.. math:: y = \int 6x^2 dx = 2x^3 + C.

Dæmi: Óaðgreinanleg diffurjafa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef við höfum diffurjöfnuna :math:`\frac{dy}{dx}=e^{xy}` þá er engin leið fyrir okkur að
aðgreina diffurjöfnuna þannig að við séum einungis með :math:`y` vinstra megin
og :math:`x` hægra megin jafnaðarmerkisins. Hún er því ekki aðgreinanleg.

Upphafsgildisverkefni
~~~~~~~~~~~~~~~~~~~~~

Ef við erum heppin og fáum upphafsgildisverkefni þar sem diffurjafnan er aðgreinanleg
þá getum við leyst hana nokkuð auðveldlega. Það fyrsta sem þarf að gera að að aðgreina
diffurjöfnuna og nota svo upphafsgildið til að finna ótvírætt ákvarðaða lausn.

Dæmi: Upphafsgildisverkefni með aðgreinanlegri diffurjöfnu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Leysum verkefnið

.. math:: \frac{dy}{dx} = \sin(x), \quad y(0)=5.

Þessi diffurjafna er aðgreinanleg og því fáum við að

.. math:: y = \int \sin(x)dx = -\cos(x) + C.

Við getum nú notfært okkur að :math:`y(0)=5` og fengið að

.. math:: y(0) = -\cos(0)+C = -1+C=5.

Ef við einangrum :math:`C` fæst að :math:`C=6`. Lausnin er því

.. math:: y=-\cos(x)+6.

Nálgun svæða
-------------

Summuvirkinn :math:`\Sigma`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Það getur verið óhentugt að skrifa út langar sumur, t.a.m.

.. math:: 1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20.

Til þess að komast hjá því að skrifa út alla liðima í langri summu, sér í lagi
þar sem allir liðirnir fylgja einhverri einhverri reglu (t.d. hækka allir um einn),
getur verið heppilegt að grípa til summuvirkjans :math:`\Sigma`. Stafurinn :math:`\Sigma`
er grískur og kallast sigma. Þetta er nánar til tekið stóra sigma en litla sigma
er :math:`\sigma`. Summumerkinu fylgir oftast summuvísir sem tiltekur hversu
oft þú vilt leggja saman, þ.e. hvað eru margir liðir í summunni þinni. Þá er
t.a.m. summan :math:`\sum_{i=1}^{20}` með 20 liðum en :math:`\sum_{i=21}^{30}` með
10 liðum.

Summuna hér að ofan mætti skrifa með

.. math:: \sum_{i=1}^{10} i.

Hún byrjar þá á því að láta :math:`i=1`, í næsta skrefi leggur hún við
:math:`i=2` og svo koll af kolli upp í :math:`i=20`. Almennt form summu er

.. math:: \sum_{i=1}^n a_i

þar sem sérhver liður :math:`a_i` tekur eitthvað gildi háð summuvísinum :math:`i`
og hættir ekki að leggja saman fyrr en komið er upp í :math:`n`. Þannig að

.. math:: a_1 + a_2 + \ldots + a_n = \sum_{i=1}^n a_i.

Reiknireglur: Summuvirkinn
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

	#. :math:`\sum_{i=1}^n c = nc`

	#. :math:`\sum_{i=1}^n ca_i = c \sum_{i=1}^n a_i`

	#. :math:`\sum_{i=1}^n (a_i \pm b_i) = \sum_{i=1}^n a_i \pm \sum_{i=1}^n b_i`

	#. :math:`\sum_{i=1}^n a_i = \sum_{i=1}^m a_i + \sum_{i=m+1}^n a_i`

Setning: Nokkrar summur til að þekkja
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef hægt er að skrifa summu :math:`\sum_{i=1}^n` sem fall af :math:`n` er það
kallað lokað form summunnar.

.. note::

	Gott getur verið að kanast við lokað form eftirfarandi summa.

	#. :math:`\sum_{i=1}^n i = 1+2+\dots+n = \frac{n(n+1)}{2}`

	#. :math:`\sum_{i=1}^n i^2 = 1^2+2^2+\dots+n^2 = \frac{n(n+1)(2n+1)}{6}

	#. :math:`\sum_{i=1}^n i^3 = 1^3+2^3+\dots+n^3 = \frac{n^2(n+1)^2}{4}``

Nálgun svæða
~~~~~~~~~~~~

Lítum á jákvætt fall :math:`f(x)` sem skilgreint er á lokaða bilinu :math:`[a,b]`.
Við viljum nálga svæðið :math:`A` sem markast af :math:`x`-ásnum, línunum :math:`x=a`
og :math:`x=b` og ferli fallsins :math:`f`.

.. image:: ./myndir/Kafli05/PMA_svaedi_undir_ferli.png
	:align: center
	:width: 75%

Spurningin er *hvernig má nálga flatarmál svæðisins undir þessum ferli?*

Við byrjum á því að skipta bilinu :math:`[a,b]` upp í :math:`n` hlutbil af jafnri
lengd, :math:`\frac{b-a}{n}`. Við gerum þetta með því að velja punkta með jöfnu
bili :math:`x_, x_1, x_2, \dots, x_n` þar sem :math:`x_0=a`, :math:`x_n=b` og

.. math:: x_i - x_{i-1} = \frac{b-a}{n}.

Þá má tákna lengd hvers undirbils með

.. math:: \Delta x = \frac{b-a}{n}.

Skilgreining: Skipting
~~~~~~~~~~~~~~~~~~~~~~

Mengi punkta :math:`P=\{x_0,x_1,\dots,x_n\}` þar sem :math:`a<x_0<x_1<\dots < x_n=b`
sem skiptir bilinu [a,b] í hlutbil á forminu :math:`[x_0,x_1], [x_1,x_2], \dots, [x_{n-1},x_n]`
kallast *skipting* bilsins :math:`[a,b]`. Ef hlutbilin hafa öll sömu lengd, er
myndar mengi punktanna *reglulega skiptingu* bilsins :math:`[a,b]`.

Reglulega skiptingu bils má svo nota sem grunninn að því að meta svæði undir ferli.

Setning: Nálgun með vinstri endapunkti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Á sérhverju hlutbili :math:`[x_{i-1},x_{i}]` fyrir :math:`i=1,2,\dots n` búum við til
rétthyrning með breiddina :math:`\Delta x` og hæðina :math:`f(x_{i-1})`, þ.e. fallgildið
í vinstri endapunkti hlutbilsins. Þá er flatarmál þessa rétthyrnings :math:`f(x_{i-1})\cdot x_i`.
Ef við summum saman flatarmál allra þessara rétthyrninga fæst nálgunargildi á
flatarmál svæðisins :math:`A`. Við notum ritháttinn :math:`L_n` til að tákna að
þetta sé nálgun með vinstri endapunkti (:math:`L` fyrir e. *left*) með :math:`n`
hlutbilum. Formúlan er því

.. math:: A \approx L_n = \sum_{i=1}^n f(x_{i-1})\cdot \Delta x.

.. image:: ./myndir/Kafli05/PMA_L6.png
	:align: center
	:width: 75%


Dæmi: Nálgun með vinstri endapunkti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Myndin hér að ofan notar :math:`n=5` hlutbil til að nálga flatarmál svæðisins
sem myndast á milli línanna :math:`x=1` og :math:`x=6`, er fyrir ofan :math:`x`-ásinn
og undir ferli fallsins :math:`f(x)=\cos(x)+3`. Sérhvert hlutbil hefur lengdina
:math:`\Delta x = 1`. Hæð rétthyrninganna má reikna með :math:`\cos(x)+3`
fyrir :math:`x=1,\dots,5` og er (frá vinstri til hægri)
:math:`3,54`, :math:`2,58`, :math:`2,01`, :math:`2,35`, og :math:`3,28`. Þar sem
lengd bilanna er :math:`1` þá er þetta jafnframt flatarmál rétthyrninganna þar sem
:math:`(\cos(x_i)+3) \cdot \Delta x = (\cos(x_i)+3) \cdot 1 = \cos(x_i)`. Því fæst að
nálgun á flatarmáli :math:`A` sé

.. math:: L_5 = 3,54 + 2,58 + 2,01 + 2,35 + 3,28 =13,76.

Raunverulegt flatarmál svæðisins er :math:`A = 15-\sin(1)+\sin(6)\approx 13,88`.
Skekkjan er því :math:`13,88-13,76=0,12` eða u.þ.b. :math:`0,9\%` munur, sem
hlýtur að teljast nokkuð gott miðað við nálgun sem notar ansi fá hlutbil.

.. image:: ./myndir/Kafli05/PMA_nalgun_svaedis_L.png
 :align: center
 :width: 75%

Setning: Nálgun með hægri endapunkti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Á sérhverju hlutbili :math:`[x_{i-1},x_{i}]` fyrir :math:`i=1,2,\dots n` búum við til
rétthyrning með breiddina :math:`\Delta x` og hæðina :math:`f(x_{1})`, þ.e. fallgildið
í hægri endapunkti hlutbilsins. Þá er flatarmál þessa rétthyrnings :math:`f(x_{i-1})\cdot x_i`.
Ef við summum saman flatarmál allra þessara rétthyrninga fæst nálgunargildi á
flatarmál svæðisins :math:`A`. Við notum ritháttinn :math:`R_n` til að tákna að
þetta sé nálgun með vinstri endapunkti (:math:`R` fyrir e. *right*) með :math:`n`
hlutbilum. Formúlan er því

.. math:: A \approx R_n = \sum_{i=1}^n f(x_{i})\cdot \Delta x.

.. image:: ./myndir/Kafli05/PMA_H6.png
	:align: center
	:width: 75%

Dæmi: Nálgun með hægri endapunkti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við nálgum nú sama svæði og hér að ofan nema nú hafa rétthyrningarnir
hæð sem svarar til fallgildis :math:`f(x)=\cos(x)+3` í hægri endapunkti,
þ.e. :math:`\cos(x)+3` þar sem :math:`x=2,\dots,6`. Húner því (frá vinstri til hægri)
:math:`2,58`, :math:`2,01`, :math:`2,35`, :math:`3,28`, og :math:`3,96`.
Með sömu rökum og áður fæst því að

.. math:: H_5 = 2,58 + 2,01 + 2,35 + 3,28 + 3,96 = 14,18.

Skekkjan er nú :math:`14,18-13,88,76=0,3` eða u.þ.b. :math:`1\%` munur.

.. image:: ./myndir/Kafli05/PMA_nalgun_svaedis_H.png
 :align: center
 :width: 75%

Athugasemd: Fjöldi rétthyrninga
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::
	Því fleiri rétthyrningar sem eru notaðir eru til þess að nálga flatarmál svæðis,
	þeim mun nákvæmari verður nálgunin.


Skilgreining: Riemann summa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f(x)` vera skilgreint á lokaða bilinu :math:`[a,b]` og :math:`P`
vera reglulega skiptingu á bilinu. Látum :math:`\Delta x` vera lengd sérhvers
hlutbils :math:`[x_{i-1},x_i]` og fyrir hvert :math:`i` látum við :math:`x_i^*`
vera hvaða tölu sem er á bilinu :math:`[x_{i-1},x_i]`. Þá er Riemann summa
skilgriend sem

.. math:: \sum_{i=1}^n f(x_i^*)\Delta x.

Setning: Flatarmál svæðis
~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f(x)` vera samfellt, jákvætt fall á lokaða bilinu :math:`[a,b]` og
látum :math:`\sum_{i=1}^n f(x_i^*) \Delta x` vera Riemann summu fyrir :math:`f(x)`.
Þá má reikna flatarmál svæðisins sem myndast undir ferli fallsins :math:`y=f(x)` á
bilinu :math:`[a,b]` með

.. math:: A = \lim_{n \rightarrow \infty} \sum_{i=1}^n f(x_i^*) \Delta x.

.. note::
	Unnt er að sanna að ef :math:`f(x)` er samfellt fall á lokuðu bili þá skiptir
	ekki máli hvaða mengi :math:`\{x_i^*\}` er valið, markgildið er alltaf það sama.
	Við munum þó ekki setja fram sönnun á því hér.

Skilgreining: Undir- og yfirsumma
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	#. Ef mengið :math:`\{x_i^*\}` í Riemann-summu er valið þannig að :math:`f(x_i^*) \leq f(x)` fyrir öll :math:`x \in [x_{i-1},x_i], i = 1,\dots,n` þá er ljóst að nálgaða flatarmálið er minna en hið raunverulega flatarmál. Þá er Riemann summan kölluð *undirsumma*.

	#. Ef mengið :math:`\{x_i^*\}` í Riemann-summu er valið þannig að :math:`f(x_i^*) \geq f(x)` fyrir öll :math:`x \in [x_{i-1},x_i], i = 1,\dots,n` þá er ljóst að nálgaða flatarmálið er stærra en hið raunverulega flatarmál. Þá er Riemann summan kölluð *yfirsumma*.

+---------------------------------------------------------+----------------------------------------------------+
| .. _figaa:                                              | .. _figbb:                                         |
|                                                         |                                                    |
| .. image:: ./myndir/kafli05/PMA_undirsumma.png          | .. image:: ./myndir/kafli05/PMA_yfirsumma.png      |
|    :width: 120%                                         |    :width: 120%                                    |
|    :align: center                                       |    :align: center                                  |
|                                                         |                                                    |
+---------------------------------------------------------+----------------------------------------------------+

Ákveðin heildi
---------------

Skilgreining: Ákveðið heildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`f(x)` er fall skilgreint á bilinu :math:`[a,b]` þá er *ákveðna heildið*
yfir :math:`f` frá :math:`a` til :math:`b` gefið með

.. math:: \int_a^b f(x) dx = \lim_{n \rightarrow \infty} \sum_{i=1}^n f(x_i^*) \Delta x,

af því gefnu að markgildið sé til. Ef markgildið er til, þá er fallið :math:`f(x)`
sagt vera heildanlegt á bilinu :math:`[a,b]` eða einfaldlega bara heildanlegt.

.. warning::

	Óákveðið heildi er fjölskylda falla á meðan ákveðið heildi er tala.

Setning: Samfelld föll eru heildanleg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`f(x)` er samfellt fall á :math:`[a,b]` þá er :math:`f` heildalegt á :math:`[a,b]`.

.. warning::

	Föll sem ekki eru samfelld á :math:`[a,b]` gætu verið heildanleg á bilinu. Það er
	þó ekki hægt að tryggja það líkt og með samfelld föll.

Dæmi: Ákveðið heildi
~~~~~~~~~~~~~~~~~~~~~

Metum ákveðna heildið

.. math:: \int_0^2 x^2 dx.

Notum hægri endapunkts nálgun til þess að búa til Riemann summuna. Höfum að
:math:`[a,b]=[0,2]` og ef notuð er regluleg skipting :math:`P=\{x_i\}`
fyrir bilið fæst að

.. math:: \Delta x = \frac{b-a}{n}=\frac{2}{n}`.

Þar sem við notumst við hægri endapunkts nálgun til að búa til Riemann summuna
þurfum við að reikna fallgildið í endapunkti bilsins :math:`[x_{i-1},x_i]`
fyrir sérhvert :math:`i`. Hægri endapunktur bilsins er :math:`x_i` og þar sem
:math:`P` er regluleg skipting fæst

.. math:: x_i = x_0 + i \Delta x = \frac{2i}{n}

og fallgildið í hægri endapunkti er því

.. math:: f(x_i) = \left(\frac{2i}{n}\right)^2 = \frac{4i^2}{n^2}.

Þá hefur Riemann summan formið

.. math:: \sum_{i=1}^n f(x_i) \Delta x = \sum_{i=1}^n \left(\frac{4i^2}{n^2}\right)\frac{2}{n} = \sum_{i=1}^n \frac{8i^2}{n^3} = \frac{8}{n^3}\sum_{i=1}^n i^2.

Við getum notfært okkur að við þekkjum lokað form þessarar summu. Því fæst

.. math:: \frac{8}{n^3}\sum_{i=1}^n i^2 = \frac{8}{n^3} \frac{n(n+1)(2n+1)}{6} = \frac{8}{3} + \frac{4}{n}+\frac{8}{6n^2}.

Til þess að meta heildið þurfum við að reikna markgildið þegar :math:`n` stefnir á óendanlegt.

.. math:: \lim_{n \rightarrow \infty} \left(\frac{8}{3} + \frac{4}{n}+\frac{8}{6n^2} \right) = \frac{8}{3}.

Því er

.. math:: \int_0^2 x^2 dx = \frac{8}{3}.

Hér fyrir neðan má draga stikuna :math:`k` til og frá til að sjá
nálgunina þegar notaðir eru :math:`k` rétthyrningar í Riemann summunni.

.. ggb:: frtbvg44
    :width: 700
    :height: 400
    :img: ./myndir/PMA_hen.png
    :imgwidth: 12cm

Flatarmál falla sem ekki eru jákvæð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hingað til höfum við takmarkað okkur við að reikna flatarmál sem myndast á ákveðnu
bili milli ferils jákvæðs falls og :math:`x`-ássins. Við skulum athuga hvað gerist
þegar við fellum kröfuna um að :math:`f \geq 0`.

Gerum ráð fyrir að :math:`f(x)` sé fall skilgreint á bilinu :math:`[a,b]` og
sé að hluta til fyrir ofan :math:`x`-ásinn og að hluta til fyrir neðan hann. Notum
:math:`n` punkta á bilinu og veljum :math:`\{x_i^*\}` sem vinstri punkt hvers hlutbilsbils :math:`[x_{i-1},x_i]`. Búum til
rétthyrning á hverju hlutbili með hæðina :math:`|f(x_i^*)|` og breiddina :math:`\Delta x`.
Þegar :math:`f(x_i^*)>0` þá er :math:`f(x_i^*) \Delta x` flatarmál rétthyrningins
líkt og áður. Þegar :math:`f(x_i^*)<0` er :math:`f(x_i^*) \Delta x` *neikvætt flatarmál*
rétthyrningsins. Köllum flatarmál rétthyrninganna fyrir ofan :math:`x`-ás :math:`A_1`
og rétthyrninganna fyrir neðan :math:`x`-ás :math:`A_2`. Riemann summan, sem
mun nálga flatarmálið sem myndast undir fallinu þar sem það er jákvætt á bilinu og
fyrir ofan fallið þar sem það er neikvætt á bilinu, er þá

.. math:: \sum_{i=1}^n f(x_i^*) \Delta x  = A_1-A_2

og ákveðna heildi fallsins yfir bilið, sem gefur nákvæmt flatarmál svæðisins, má reikna

.. math:: \int_0^2 f(x) dx = \lim_{n \rightarrow \infty} \sum_{i=1}^n f(c_i) \Delta x = A_1 - A_2

þar sem :math:`c_i` er einhver punktur á hlutbilinu :math:`[x_{i-1},x_i]`.

.. image:: ./myndir/kafli05/PMA_neikvaett_flatarmal.png
	:align: center
	:width: 75%

Athugum að þessi skilgreining virkar jafnvel þó fallið sé alfarið fyrir ofan
eða neðan :math:`x`-ásinn. Það eina sem gerist er að annað hvort mun :math:`A_1`
eða :math:`A_2` taka gildið 0.

Setning: Reglur um ákveðin heildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
	Eftirfarandi gildir um ákveðin heildi.

		#. :math:`\int_a^a f(x) dx = 0`

		#. :math:`\int_b^a f(x) dx = - \int_a^b f(x) dx`

		#. :math:`\int_a^n (f(x) \pm g(x))dx = \int_a^b f(x) dx \pm \int_a^b g(x) dx`

		#. :math:`\int_a^b c f(x) dx = c \int_a^b f(x) dx`

		#. :math:`\int_a^b f(x) dx = \int_a^c f(x) dx + \int_c^b f(x) dx`

Setning: Samanburður heilda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

	Eftirfarandi gildir um ákveðin heildi.

		#. Ef :math:`f(x) \geq 0` fyrir :math:`a \leq x \leq b` þá gildir að :math:`\int_a^b f(x) dx \geq 0`.

		#. Ef :math:`f(x) \geq g(x)` fyrir :math:`a \leq x \leq b` þá gildir að :math:`\int_a^b f(x) dx \geq \int_a^b g(x) dx`.

		#. Ef :math:`m` og :math:`M` eru fastar þannig að :math:`m \leq f(x) \leq M` fyrir :math:`a \leq x \leq b` þá gildir að :math:`m(b-a) \leq \int_a^b f(x) dx \leq M(b-a)`.

Meðalgildi falls
~~~~~~~~~~~~~~~~

Flestir nemendur þekkja það vel að reikna meðaltal talnasafna, þar sem
meðaltal talnasafnsins :math:`x_1, x_2, \dots, x_n` er :math:`\frac{1}{n}\sum_{i=1}^n x_i`.
Á svipaðan hátt má reikna meðalgildi falls.

Látum :math:`f(x)` vera samfellt á bilinu :math:`[a,b]` og skiptum bilinu í :math:`n`
hlutbil af breiddinni :math:`\Delta x = (b-a)/n`. Veljum eitt gildi :math:`x_i^*`
af hverju hlutbili og reiknum :math:`f(x_i^*)` fyrir :math:`i=1,2,\dots,n`.
Þar sem fallið er samfellt en þessi gildi stjrál þá gefur þetta okkur einungis
mat á meðatali fallsins á bilinu, sem má þá reikna á sambærilegan hátt og
meðaltal talnasafns með

.. math:: \overline{f} \approx \frac{1}{n}\sum_{i=1}^n f(x_i^*).

Með einfaldri algebru má sýna að þetta sé jafngilt því að rita

.. math:: \overline{f} \approx \frac{1}{b-a}\sum_{i=1}^n f(x_i^*) \Delta x.

Þetta er Riemann summa. Þá má fá nákvæmt gildi á meðaltalinu með því að reikna

.. math:: \overline{f} = \frac{1}{b-a} \lim_{n \rightarrow \infty} \sum_{i=1}^n f(x_i) \Delta x = \frac{1}{b-a} \int_a^b f(x) dx.

Skilgreining: Meðalgildi falls á bili
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`f(x)` er samfellt fall á bilinu :math:`[a,b]` þá er meðalgildi fallsins
á bilinu gefið með

.. math:: \overline{f} = \frac{1}{b-a} \int_a^b f(x) dx.

.. warning::
	Bókin notar :math:`f_{\text{ave}}` (ave fyrir enska orðið *average*)
	til þess að tákna meðagildi falls.
	Hér munum við nota :math:`\overline{f}` til að halda samræmi við að tákna meðatal
	talnasafns :math:`x_1, x_2, \dots, x_m` með :math:`\overline{x}`, ritháttur sem
	er notaður í flestum áföngum Háskóla Íslands.

Undirstöðusetning stærðfræðigreiningar
--------------------------------------

Meðalgildissetningin fyrir heildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`f(x)` er samfellt á bilinu :math:`[a,b]` þá er að minnsta kosti einn
punktur :math:`c\in [a,b]` sem uppfyllir að

.. math:: f(c) = \frac{1}{b-a} \int_a^b f(x) dx.

Setning: Undirstöðusetning stærðfræðigreiningar (I)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`f(x)` er samfellt á bilinu :math:`[a,b]` og fallið :math:`F(x)` er
skilgreint þannig að

.. math:: F(x) = \int_a^x f(t) dt

þá gildir að :math:`F'(x) =f(x)` á :math:`[a,b]`.

Dæmi: Undirstöðusetning stærðfræðigreiningar (I)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`u=\sqrt{x}` og gerum ráð fyrir að

.. math:: F(x) = \int_1^{u(x)} \sin(t) dt.

Samkvæmt undirstöðusetningu stærðfræðigreiningar (I) og keðjureglunni fæst

.. math::
	\begin{align}
		F'(x) &= \sin(u(x))\frac{du}{dx}\\
		&= \sin(u(x)) \cdot (\frac{1}{2} x^{-1/2})\\
		&= \frac{\sin(\sqrt{x})}{2\sqrt{x}}.
	\end{align}

	Setning: Undirstöðusetning stærðfræðigreiningar (II)
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	Ef :math:`f(x)`er samfellt á bilinu :math:`[a,b]` og :math:`F(x)` er
	eitthvað stofnfall fyrir :math:`f(x)` þá gildir að

	.. math:: \int_a^b f(x) dx = F(b)-F(a).

	.. tip::
		Nemendur gera sér oft ekki grein fyrir því hversu gríðarlega mikilvæg
		undirstöðusetning stærðfræðigreiningarinnar er. Það tók stærðfræðinga
		meira en 500 ár að fínpússa þá tækni sem vísinda- og fræðimenn notast við í
		dag til að útskýra hegðun ýmissa fyrirbæra.
		Stærðfræðigreining gerði okkur loksins kleyft að reikna út fjarlægðir í
		geiminum og kortleggja sporbauga reykistjarna. Vegna hennar varð mögulegt að reikna jaðarkostnað og
		spá fyrir um heildargróða með einföldum hætti og nákvæmni. Stærðfræðigreiningin gaf verkfræðingum
		þá fræðilegu þekkingu sem nauðsynleg var svo þeir gætu
		reiknað svigþol efna og hreyfingu hluta í þrívíðu rúmi. Heimsýn okkar breyttist
		með tilkomu stærðfræðigreiningar. 
