Runur og raðir
===============

.. admonition:: Nauðsynleg undirstaða
  :class: athugasemd

	- Föll

	- Markgildi

------

.. epigraph::

  **Sam:**
  *What we need is a few good taters.*

  **Gollum:**
  *What´s taters, precious? What´s taters, eh?*

  **Sam:**
  *Po-tay-toes. Boil´em, mash´em, stick´em in a stew. Lovely big golden chips with a nice piece of fried fish.*

  **Sam:**
  *Even you couldn´t say no to that.*

  **Gollum:**
  *Oh yes we could. Spoilin´ nice fish. Give it to us raw and wrigglin´. You keep nasty chips.*

  **Sam:**
  *You´re hopeless.*

  \– Samwise Gamgee and Gollum, The Two Towers (Movie)

------

Runur
-----

Ritháttur
~~~~~~~~~~

Óendanleg runa er raðaður listi á forminu

.. math:: a_1, a_2, a_3, \dots, a_n, \dots

þar sem hvert :math:`a_n`, :math:`n \in \mathbb{N}` er kallaður *liður* rununnar.
Talan :math:`n` er kölluð *knévísir* eða einfaldlega bara *vísir* rununnar.
Hægt er að tákna rununna hér að ofan með

.. math:: \{a_n\}_{n=1}^\infty \text{ eða eindaldlega bara } \{a_n\}.

Athugum að þó rithátturinn fyrir mengi sé svipaður þá eru mengi ekki röðuð á meðan
runur eru það, sem þýðir að röðin í runum skiptir máli en ekki í mengjum. Því
eru mengin :math:`\{1,2,3\}` og :math:`\{3,1,2\}` þau sömu en runurnar :math:`1,2,3,\dots`
og :math:`3,1,2,\dots` það ekki. Ef við skoðum rununa

.. math:: 2,4,8,18,32,\dots

sjáum við að hún inniheldur öll jákvæð heiltöluveldi af 2 í stækkandi röð. Hana má því
tákna með

.. math:: \{2^n\}_{n=1}^\infty \text{ eða eindaldlega } \{2^n\}.

Runum má líka lýsa með *rakningarvenslum*. Þá er sagt að

.. math::
  \begin{cases}
    a_1=2\\
    a_n = 2a_{n-1}, & n \geq 2.\\
  \end{cases}

Skilgreining: Runa
~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

	*Runan* :math:`{a_n}` er raðaður listi á forminu

	.. math:: a_1, a_2, a_3, \dots, a_n, \dots

	þar sem :math:`n` er kallaður *knévísir* rununnar og hvert :math:`a_n` er
	*liður* hennar. Sumar runur eiga sér *lokað form* en þá er hægt að lýsa
	hverjum lið hennar sem falli af :math:`n`, þ.e. :math:`a_n = f(n)`
	þar sem :math:`n` er náttúruleg tala. Í öðrum tilfellum má lýsa liðum rununnar
	með *rakningarvenslum* þar sem hver liður er skilgreindur með lið sem kom á undan í
	rununni, nema upphafsliðurinn sem er þá gefinn.

Athugum að ekkert er því til fyrirstöðu að láta knévísinn byrja á annarri tölu en
:math:`n=1`. Oft er notast við að upphafsliðurinn sé liður númer núll, þ.e.
:math:`a_0` en runan mætti þess vegna byrja á :math:`a_2` eða :math:`a_{-3}` sé
þörf fyrir því. Tvær týpur af runum koma oftar fyrir en aðrar í kennslubókum, þær eru *jafnmunaruna* (einnig
kölluð *mismunaruna*) og *geómetrísk runa*.

Í **jafnmunarunu** er mismunur milli allra liða rununnar sá sami. Til að mynda er runan

.. math:: 3,7,11,15,19,\dots

jafnmunaruna því það munar 4 á öllum liðunum og má nota rakningarvenslin

.. math::
	\begin{cases}
		a_1=3\\
		a_n = a_{n-1}+4, & n \geq 2
	\end{cases}

til að lýsa henni. Þar sem fyrsti liður rununnar er :math:`3` og mismunur á milli liða er
:math:`4` má einnig lýsa :math:`n`-ta lið rununnar með

.. math:: a_n=3n+4.

Jafnmunarunur hafa almennt lokaða formið :math:`a_n=cn+b` þar sem :math:`a_1 = c` er
fyrsti liður rununnar og :math:`b` er mismunurmunurinn aðliggjandi liða.

Í **geómetrískri runu** er hlutfallið milli allra liða það sama. Til að mynda er
runan

.. math:: 2, \frac{-2}{3}, \frac{2}{9}, -\frac{2}{27}, \frac{2}{81},\dots

geómetrísk runa því hlutfallið milli hverra tveggja aðliggjandi liða er
:math:`-\frac{1}{3}` og not má rakningarvenslin

.. math::
  \begin{cases}
    a_1=2\\
    a_n = -\frac{1}{3}a_{n-1}, & n \geq 2.
  \end{cases}

til að lýsa henni. Þar sem fyrsti liður rununnar er :math:`2` og hlutfallið :math:`-\frac{1}{3}`
má lýsa :math:`n`-ta lið rununnar með

.. math:: a_n = 2\left(-\frac{1}{3}\right)^{n-1}.

Almennt hefur geómetrísk runa lokaða formið :math:`a_n=cr^{n-1}` þar sem :math:`c` er
fyrsti liður rununnar og :math:`a_1=r` er hlutfallið milli aðliggjandi liða.

Dæmi: Lokað form
~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Finnum lokað form rununnar

	.. math:: \frac{3}{4}, \frac{9}{7}, \frac{27}{10}, \frac{81}{13}, \frac{243}{16},\dots.

.. admonition:: Lausn
  :class: daemi, dropdown

	Teljarar brotanna eru :math:`3,9,27,81,243, \dots` á meðan nefnarar þeirra eru :math:`4,7,10,13,16, \dots`.
	Við sjáum að fyrri runan er geómetrísk runa þar sem sérhver liður er þrefalt stærri
	en liðurinn á undan á meðan seinni runan er jafnmunaruna þar sem það munar 3 á
	hverjum tveimur aðliggjandi liðum. Fyrri rununni má því lýsa með :math:`3^n` en
	þeirri seinni :math:`3n+1`. Lokað form rununnar er því

	.. math:: a_n = \frac{3^n}{3n+1}.

Dæmi: Lokað form
~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Finnum lokað form rununnar sem skilgreind er með rakningarvenslunum

	.. math::
	  \begin{cases}
	    a_1=2\\
	    a_n = -3a_{n-1}, & n \geq 2.
	  \end{cases}

.. admonition:: Lausn
  :class: daemi, dropdown

	Byrjum á því að átta okkur á því hvaða runa þetta er. Skrifum út nokkra liði
	hennar.

	.. math::
	  \begin{align}
	    a_1 &= 2\\
	    a_2 &= -3 a_1 = (-3)\cdot 2\\
	    a_3 &= -3 a_2 = (-3) \cdot (-3) \cdot 2\\
	    a_4 &= -3 a_3 = (-3) \cdot (-3) \cdot (-3) \cdot 2\\.
	  \end{align}

	Oft getur hjálpað að reikna útreikningana ekki alveg til enda til að auðveldara
	sé að koma auga á mynstrið. Hér sést að

	.. math:: a_n = (-3)^{n-1}\cdot2.

Markgildi runa
~~~~~~~~~~~~~~~

Ein af þeim grundvallarspurningum sem hægt er að spurja þegar kemur að runum er
hvernig runan hegðar sér þegar knévísirinn :math:`n` stefnir á :math:`\infty`.
Þar sem runa er fall sem er skilgreint á náttúrulegu tölunum er rökrétt að
leiða hugann að því hvort allir liðirnir stefni á sama gildið, þ.e. hvort
markgildi liðanna í rununni sé samleitið.

Skilgreining: Markgildi runu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

	Af því gefnu að liðir rununnar :math:`\{a_n\}` nálgist gildið :math:`L` óendanlega
	mikið eftir því sem :math:`n` stækkar segjum við að :math:`\{a_n\}` sé *samleitin runa*
	og að :math:`L` sé *markgildi rununnar*. Við ritum þá að

	.. math:: \lim_{n \rightarrow \infty} a_n = L.

	Ef runan :math:`\{a_n\}` er ekki samleitin segjum við að hún sé *ósamleitin runa*.

Skilgreining
~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

	Runan :math:`\{a_n\}` er samleitin að rauntölu :math:`L` ef fyrir öll :math:`\varepsilon > 0`
	er til heil tala :math:`N` þannig að :math:`|a_n - L|<\varepsilon` fyrir :math:`n \geq N`.
	Þá er talan :math:`L` kölluð *markgildi* rununnar og við skrifum

	.. math:: \lim_{n \rightarrow \infty} a_n = L \text{ eða } a_n \rightarrow L.

	Þá er runan :math:`\{a_n\}` sögð vera *samleitin runa*. Runa sem er ekki samleitin
	er kölluð ósamleitin runa og við segjum að markgildi hennar sé ekki til.


Dæmi: Samleitin og ósamleitin runa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Runan

	.. math:: -1, 1, -1, 1, -1, 1, \dots = \{(-1)^n\}

	kallast *víxlruna* þar sem annar hver liður er sá sami og víxlar runan þannig
	á milli tveggja gilda. Þessi runa er ekki samleitin af því að liðirnir halda áfram
	fram í hið óendanlega að víxla á milli gildanna -1 og 1 og nálgast runan því ekki
	eina ákveðna tölu :math:`L`.

	Runan

	.. math:: 1,2,3,4,5,6, \dots = \{n\}

	er einnig ósamleitin af því að

	.. math:: \lim_{n \rightarrow \infty} a_n = \infty

	og til þess að runa sé samleitin verður markgildi hennar að vera einhver
	tala :math:`L < \infty`. Hinsvegar er runan

	.. math:: 1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \frac{1}{5}, \dots = \left\{\frac{1}{n}\right\}

	samleitin þar sem liðirnir verða alltaf minni og minni og stefna á endanum á 0,
	þ.e.

	.. math:: \lim_{n \rightarrow \infty } \left\{\frac{1}{n}\right\}  = 0.

Setning: Markgildi runu skilgreint með falli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Gerum ráð fyrir að runan :math:`\{a_n\}` uppfylli að :math:`n`-ta staki hennar megi lýsa
	með fallinu :math:`f(n)`, þ.e. :math:`a_n=f(n)` fyrir öll :math:`n\geq 1`. Ef
	til er rauntala :math:`L` þannig að

	.. math:: \lim_{x \rightarrow \infty} f(x)=L

	er sagt að runan sé samleitin og

	.. math:: \lim_{n \rightarrow \infty} a_n = L.

	Við getum notað þessa setningu til að meta markgildið

	.. math:: \lim_{n \rightarrow \infty } r^n

	fyrir :math:`0 \leq r < 1`. Við skulum líta á rununa :math:`\{(1/2)^n\}` og
	sambærilegt vísisfall :math:`f(x)=(1/2)^x`. Þar sem

	.. math:: \lim_{x \rightarrow \infty} (1/2)^x = 0

	getum við staðhæft að runan  :math:`\{(1/2)^n\}` hafi markgildið 0. Sambærilega
	gildir fyrir sérhverja rauntölu :math:`r` sem uppfyllir að :math:`0 \leq r < 1`
	að

	.. math:: \lim_{x \rightarrow \infty} r^x = 0

	og þar með er runan :math:`\{r^n\}` samleitin með markgildið 0. Ef hins vegar :math:`r=1` er
	markgildið

	.. math:: \lim_{x \rightarrow \infty} r^x = 1

	og runan er samleitin með markgildið 1. Ef hins vegar :math:`r>1` er

	.. math:: \lim_{x \rightarrow \infty} r^x = \infty

	og við getum þar með ekki beitt setningunni um að skilgreina markgildi runu með falli.
	Af þessu leiðir að

	.. math::
	  \begin{align}
	    r^n &\rightarrow 0 \text{ ef } 0 < r < 1\\
	    r^n &\rightarrow 1 \text{ ef } r=1\\
	    r^n &\rightarrow \infty \text{ ef } r > 1\\
	  \end{align}

Setning: Markgildisreglur fyrir runur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Látum :math:`\{a_n\}` og :math:`\{b_n\}` vera gefnar runur og :math:`c` einhverja
	rauntölu. Ef til eru fastar :math:`A` og :math:`B` þannig að :math:`\lim_{n \rightarrow \infty} a_n = A`
	og :math:`\lim_{n \rightarrow \infty} b_n = B` gildir

	  #. :math:`\lim_{n \rightarrow \infty} c = c`

	  #. :math:`\lim_{n\rightarrow \infty} ca_n = c\lim_{n\rightarrow \infty}a_n = cA`

	  #. :math:`\lim_{n\rightarrow \infty} (a_n \pm b_n) = \lim_{n\rightarrow \infty} a_n \pm \lim_{n\rightarrow \infty} b_n = A \pm B`

	  #. :math:`\lim_{n\rightarrow \infty} (a_n \cdot b_n) = \left(\lim_{n\rightarrow \infty} a_n \right) \cdot \left(\lim_{n\rightarrow \infty} b_n \right) = A \cdot B`

	  #. :math:`\lim_{n\rightarrow \infty} \lim_{n\rightarrow \infty} \left( \frac{a_n}{b_n} \right) = \frac{\lim_{n\rightarrow \infty} a_n}{\lim_{n\rightarrow \infty} b_n} = \frac{A}{B}` af því gefnu að :math:`B \neq 0` og hvert :math:`b_n \neq 0`.

Dæmi: Ákvarða samleitni og reikna markgildið
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Ákvörðum hvort runan

	.. math:: \left\{5 - \frac{3}{n^2} \right\}

	sé samleitin og ef svo er reiknum þá markgildi hennar.

.. admonition:: Lausn
	:class: daemi, dropdown

	Við vitum að :math:`1/n \rightarrow 0` og því gildir að

	.. math:: \lim_{n \rightarrow \infty} \frac{1}{n^2} = \lim_{n \rightarrow \infty} \left(\frac{1}{n}\right) \cdot \lim_{n \rightarrow \infty} \left(\frac{1}{n}\right)  = 0 \cdot 0 = 0.

	Svo markgildi rununnar er

	.. math:: \lim_{n \rightarrow \infty} 5 - \frac{3}{n^2} = \lim_{n \rightarrow \infty} 5 - 3  \lim_{n \rightarrow \infty} \frac{1}{n^2} = 5 - 3\cdot 0 = 5.

Setning: Samfelld föll skilgreind á samleitnum runum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Látum :math:`\{a_n\}` vera runu og gerum ráð fyrir að til sé tala :math:`L` þannig
	að

	.. math:: \lim_{n \rightarrow n} a_n = L.

	Gerum einnig ráð fyrir að fallið :math:`f` sé samfellt í :math:`L`. Þá er til
	heil tala :math:`N` sem uppfyllir að :math:`f` er skilgreint í öllum :math:`a_n`
	fyrir :math:`n \geq N` og runan :math:`\{f(a_n)\}` er samleitin að :math:`f(L)`.

Dæmi: Samfelld föll skilgreind á samleitnum runum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Ákvörðum hvort runan :math:`\left\{ \cos(3/n^2) \right\}` sé samleitin. Ef hún
	er samleitin, finnum þá markgildið.

.. admonition:: Lausn
  :class: daemi, dropdown

	Þar sem runan :math:`\{3/n^2\}` er samleitin að 0  og :math:`\cos(x)` er samfellt
	í :math:`x=0` getum við staðhæft að runan :math:`\{3/n^2\}`  samleitin og að
	markgildið sé

	.. math:: \lim_{n \rightarrow \infty} \cos\left(\frac{3}{n^2}\right) = \cos(0)=1.

Setning: Klemmureglan fyrir runur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Látum :math:`\{a_n\}`, :math:`\{b_n\}` og :math:`\{c_n\}` vera gefnar runur. Gerum
	ráðu fyrir því að til sé heil tala :math:`N` þannig að

	.. math:: a_n \leq b_n \leq c_n \text{ fyrir öll } n \geq N.

	Ef til er rauntala :math:`L` þannig að

	.. math:: \lim_{n \rightarrow \infty} a_n = L = \lim_{n \rightarrow \infty} c_n,

	þá er :math:`\{b_n\}` samleitin og :math:`\lim_{n \rightarrow \infty} b_n = L`.

Dæmi: Klemmureglan fyrir runur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Notum klemmuregluna fyrir runur til að finna markgildi rununnar

	.. math:: \left\{ \frac{\cos(n)}{n^2}\right \}.

.. admonition:: Lausn
	:class: daemi, dropdown

	Þar sem :math:`-1 \leq \cos(n) \leq 1` fyrir allar heiltölur :math:`n` höfum við að

	.. math:: -\frac{1}{n^2} \leq \frac{\cos(n)}{n} \leq \frac{1}{n^2}.

	Þar sem :math:`-1/n^2 \rightarrow 0` og :math:`1/n^2 \rightarrow 0` fæst
	skv. klemmureglunni að

	.. math:: \lim_{n \rightarrow \infty } = \left\{ \frac{\cos(n)}{n^2}\right \} = 0.

Takmarkaðar runur
~~~~~~~~~~~~~~~~~~

Við beinum nú sjónum okkar að einni mikilvægustu setningu stærðfræðgreingarinnar sem við kemur runum,
setningin um einhalla samleitni. Við þurfum hins vegar að byrja á því að skilgreina örfá hugtök.

Skilgreining: Takmörkun
~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

	Runan :math:`\{a_n\}` er sögð vera *takmörkuð að ofan* ef til er rauntala :math:`M` þannig að

	.. math:: a_n \leq M

	fyrir allar jákvæðar heiltölur :math:`n`.

	Runan :math:`\{a_n\}` er sögð vera *takmörkuð að neðan* ef til er rauntala :math:`M` þannig að

	.. math:: M \leq a_n

	fyrir allar jákvæðar heiltölur :math:`n`.

	Runan :math:`\{a_n\}` er sögð vera *takmörkuð runa* hún er takmörkuð að ofan og neðan.
	Ef runa er ekki takmörkuð er hún sögð vera *ótakmörku runa*.

Til að mynda er runan :math:`\{1/n\}` takmörkuð að ofan af því að :math:`1/n \leq 1`
fyrir allar jákvæðar heiltölur :math:`n`. Hún er einnig takmörkuð að neðan þar sem
:math:`1/n \geq 0` fyrir allar jákvæðar heiltölur :math:`n`. Ef við lítum hins
vegar á rununa :math:`\{2^n\}` þá er hú ekki takmörkuð að ofan þar sem :math:`\lim_{n \rightarrow \infty} 2^n = \infty`
og jafnvel þó hún sé takmörkuð að neðan þar sem :math:`2^n > 0` fyrir allar
jákvæðar heiltölur þá segjum við samt sem áður að runan sé ótakmörkuð þar sem
hún er ekki takmörkuð að ofan og neðan.

Setning: Samleitnar runur eru takmarkaðar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Ef runan :math:`\{a_n\}` er samleitin þá er hún takmörkuð.

.. admonition:: Aðvörun
  :class: advorun

	  Þetta gildir ekki öfugt. Til eru takmarkaðar runur sem ekki eru samleitnar.

Skilgreining: Einhalla runa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

	Runa :math:`\{a_n\}` er sögð *vaxandi* fyrir öll :math:`n \geq n_0` ef

	.. math:: a_n \leq a_{n+1} \text{ fyrir öll } n \geq n_0.

	Runa :math:`\{a_n\}` er sögð *minnkandi* fyrir öll :math:`n \geq n_0` ef

	.. math:: a_n \geq a_{n+1} \text{ fyrir öll } n \geq n_0.

	Runa :math:`\{a_n\}` er sögð *einhalla* fyrir öll :math:`n \geq n_0` er hún
	er vaxandi fyrir öll :math:`n \geq n_0` eða minnkandi fyrir öll :math:`n \geq n_0`.

Þá er ekkert annað að gera en að setja fram setninguna um einhalla runur.

Setning: Setningin um einhalla runur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Ef :math:`\{a_n\}` er takmörkuð runa og til er jákvæð heil tala :math:`n_0` þannig
	að :math:`\{a_n\}`  sé einhalla fyrir öll :math:`n \geq n_0` þá er runan samleitin.


Dæmi: Setningin um einhalla runur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Notum setninguna um einhalla runur til að sýna að runan

	.. math:: \left\{\frac{4^n}{n!}\right\}

	sé samleitin og ákvörðum markgildi hennar.

.. admonition:: Lausn
  :class: daemi, dropdown

	Skoðum fyrstu liði rununnar.

	.. math:: \left\{\frac{4^n}{n!}\right\} = 8,4, \frac{32}{3}, \frac{32}{3}, \frac{128}{15}, \dots.

	Í fyrstu vex runan en frá og með :math:`n \geq 3` minnka liðirnir. Þetta má sýna fram
	á með eftirfarandi hætti.

	.. math:: a_{n+1} = \frac{4^{n+1}}{(n+1)!} = \frac{4^{n+1}}{(n+1)!} = \frac{4}{n+1}\cdot \frac{4^n}{n!} = \frac{4}{n+1}\cdot a_n \leq a_n \text{ ef } n \geq 3.

	Við sjáum einnig að runan er takmörkuð að neðan af 0 þar sem :math:`4^n/n! \geq 0`
	fyrir allar jákvæðar heiltölur :math:`n`. Þar með segir setningin um einhalla runir
	að runan sé samleitin.

	Til að ákvarða markgildið þurfum við að nota að þá vitneskju að runan sé samleitin
	og láta

	.. math:: L = \lim_{n \rightarrow \infty} a_n.

	Athugum nú sérstsaklega að þar sem runan inniheldur óendanlega marga
	liði hefur það ekki áhrif á markgildi hennar að fjarlægja úr henni endanlega
	marga liði. Þar sem :math:`\{a_{n+1}\}` er sama runa og :math:`\{a_{n}\}` að öllu leyti nema
	hún sleppir fyrsta liðnum í :math:`\{a_{n}\}` fæst því að

	.. math:: \lim_{n \rightarrow \infty} a_n = \lim_{n \rightarrow \infty} a_{n+1} = L.

	Notum nú þetta auk þess að

	.. math:: a_{n+1} = \frac{4}{n+1}a_n.

	Tökum markgildi af báðum hliðum jöfnunnar

	.. math:: \lim_{n \rightarrow \infty} a_{n+1} = \lim_{n \rightarrow \infty} \frac{4}{n+1}a_n.

	Þar sem :math:`\lim_{n \rightarrow \infty} \frac{4}{n+1} = 0` fæst samkvæmt reiknireglum
	um markgildi að

	.. math:: \lim_{n \rightarrow \infty} \frac{4}{n+1}a_n = 0.

	Og þar sem

	.. math:: \lim_{n \rightarrow \infty} a_n = \lim_{n \rightarrow \infty} a_{n+1} = \lim_{n \rightarrow \infty} \frac{4}{n+1}a_n.

	hefur runan :math:`\left\{\frac{4^n}{n!}\right\}` markgildið :math:`L=0`.

--------

Raðir
-----

Skilreining: Röð
~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

	Óendanleg *röð* er summa sem hefur óendanlega marga liði og er rituð á forminu

	.. math:: \sum_{n=1}^\infty a_n = a_1 + a_2 + a_3 + \dots.

	Fér sérhverja jákvæða heiltölu :math:`k` er summan

	.. math:: S_k = \sum_{n=1}^k a_n = a_1 + a_2 + a_3 + \dots a_k

	er kölluð :math:`k`-ta *hlutsumma* raðarinnar. Hlutsummurnar mynda rununa
	:math:`\{S_k\}`. Ef runa hlutsummanna er samleitin að rauntölu :math:`S` er
	sagt að röðin sé samleitin og :math:`S` sé summa hennar. Við ritum þá

	.. math:: \sum_{n=1}^\infty a_n = S.

	Ef runa hlutsumanna er ósamleitin segjum við að *röðin sé ósamleitin*.

Athugum að röðin þarf ekki að byrja í :math:`n=1`, ef þörf krefst má byrja
röðina í :math:`n=0` eða :math:`n=-1` eða hvaða tölu sem er. Sem dæmi þá er
röðin

.. math:: \sum_{n=2} \frac{1}{n^2}

fullkomlega fullgild röð. Ef við viljum skrifa hana þannig að summuvísirinn
byrji í 1 má nota innsetningu með :math:`m=n+1` og fæst þá

.. math:: \sum_{m=1}^\infty \frac{1}{(m+1)^2}

sem er algerlega jafngild framsetning af sömu röðinni.

Dæmi: Markgildi hlutsumma
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Notum runu hlutsumma til að ákvarða hvort röðin

	.. math:: \sum_{n=1}^\infty \frac{n}{n+1}

	sé samleitin eða ósamleitin.

.. admonition:: Lausn
  :class: daemi, dropdown

	Runa hlutsumanna :math:`\{S_k\}` uppfyllir að

	.. math::
		\begin{align}
		S_1 &= \frac{1}{2}\\
		S_2 &= \frac{1}{2}+\frac{2}{3}\\
		S_3 &= \frac{1}{2}+\frac{2}{3}+\frac{3}{4}\\
		S_4 &= \frac{1}{2}+\frac{2}{3}+\frac{3}{4}+\frac{4}{5}.\\
		\end{align}

	Athugum að hverjum lið sem bætt er við er stærri en :math:`1/2`. Af því leiðir að

	.. math::
		\begin{align}
		S_1 &= \frac{1}{2} \\
		S_2 &= \frac{1}{2}+\frac{2}{3}> \frac{1}{2} + \frac{1}{2} = 2\left(\frac{1}{2}\right)\\
		S_3 &= \frac{1}{2}+\frac{2}{3}+\frac{3}{4} > \frac{1}{2} + \frac{1}{2} + \frac{1}{2} = 3 \left(\frac{1}{2}\right)\\
		S_4 &= \frac{1}{2}+\frac{2}{3}+\frac{3}{4}+\frac{4}{5} > \frac{1}{2} + \frac{1}{2} + \frac{1}{2} + \frac{1}{2} = 4 \left(\frac{1}{2}\right).\\
		\end{align}

	Út frá þessu mynstri sést að :math:`S_k > k\left(\frac{1}{2}\right)` fyrir
	sérhverja heiltölu :math:`k`. Þar með er :math:`\{S_k\}` ótakmörkuð og
	því ósamleitin. Því fæst að röðin

	.. math:: \sum_{n=1}^\infty \frac{n}{n+1}

	er ósamleitin.

Skilgreining: Harmoníska röðin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	 Röðin

	.. math:: \sum_{n=1}^\infty 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \dots .

	nefnist *harmoníska röðin* (e. *the harmonic series*).

Harmoníska röðin er áhugaverð að því leyti að hún er ósamleitin en verður það afar hægt.
Það er ekki auðvelt að sjá það út undan sér að hún sé ósamleitin,
í fyrstu sýn mætti halda að hún væri samleitin. Liðir hennar stefna hraðbyris á 0
svo sífellt bætist minna við.

Reiknireglur: Samleitnar raðir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Reiknireglur: Samleitnar raðir
  :class: setning

	Látum :math:`\sum_{n=1}^\infty a_n` og :math:`\sum_{n=1}^\infty b_n` vera samleitnar
	raðir og :math:`c` vera einhverja rauntölu. Þá gildir eftirfarandi.

		#. Röðin :math:`\sum_{n=1}^\infty (a_n \pm b_n)` er samleitin og :math:`\sum_{n=1}^\infty (a_n \pm b_n) = \sum_{n=1}^\infty a_n \pm \sum_{n=1}^\infty b_n`.

		#. Röðin :math:`\sum_{n=1}^\infty ca_n` er samleitin og :math:`\sum_{n=1}^\infty ca_n = c\sum_{n=1}^\infty a_n`.


Dæmi: Reiknireglur um samleitnar raðir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Metum

	.. math:: \sum_{n=1}^\infty \left( \frac{3}{n(n+1)} + \left(\frac{1}{2}\right)^{n-2} \right)

	af því gefnu að vitað sé að

	.. math:: \sum_{n=1}^\infty \frac{1}{n(n+1)}= 1

	og

	.. math:: \sum_{n=1}^\infty \left(\frac{1}{2}\right)^{n-1} = 2.

.. admonition:: Lausn
	:class: daemi, dropdown

	Fáum samkvæmt reglum um samleitnar raðir að

	.. math::
		\begin{align}
			\sum_{n=1}^\infty \left( \frac{3}{n(n+1)} + \left(\frac{1}{2}\right)^{n-2} \right) &= 3\sum_{n=1}^\infty \frac{1}{n(n+1)} + \left(\frac{1}{2}\right)^{-1} \sum_{n=1}^\infty \left(\frac{1}{2}\right)^{n-1}\\
			&= 3 \cdot 1 + \left(\frac{1}{2}\right)^{-1}  \cdot 2\\
			&= 3 + 4\\
			&= 7.
		\end{align}

Skilgreining: Geómetrísk röð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	*Geómetrísk röð* er röð sem rita má á forminu

	.. math:: a+ar+ar^2+ar^3+\dots = \sum_{n=1}^\infty ar^{n-1}.

	Þar sem hlutfallið milli aðliggjandi liða er táknað með :math:`r` og nefnist *hlutfallstala* raðarinnar
	og talan :math:`a` er nefnist *fyrsti liður raðarinnar*.

	Ef :math:`|r|<1` er röðin samleitin og

	.. math:: \sum_{n=1}^\infty ar^{n-1} = \frac{1}{1-r} \text{ fyrir } |r|<1.

	Ef :math:`|r| \geq 1` er röðin ósamleitin.

Dæmi: Samleitni geómetrískar raðar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Ákvörðum hvort geómetríska röðin

	.. math:: \sum_{n=1}^\infty e^{2n}

	sé samleitin og ef hún er samleitin finnum þá summu hennar.

.. admonition:: Lausn
  :class: daemi, dropdown

	Ef við ritum röðina á forminu

	.. math:: e^2 \sum_{n=1}^\infty (e^2)^{n-1}

	sést að :math:`r=e^2>1` svo röðin er ósamleitin.

Dæmi: Samleitni geómetrískar raðar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Ákvörðum hvort geómetríska röðin

	.. math:: \sum_{n=1}^\infty \frac{(-3)^{n+1}}{4^{n-1}}

	sé samleitin og ef hún er samleitin finnum þá summu hennar.

.. admonition:: Lausn
  :class: daemi, dropdown

	Ef við skrifum út fyrstu liði raðarinnar fæst

	.. math::
		\begin{align}
			\sum_{n=1}^\infty \frac{(-3)^{n+1}}{4^{n-1}} &= \frac{(-3)^2}{4^0} + \frac{(-3)^3}{4^1} + \frac{(-3)^4}{4^2}+ \dots\\
			&= (-3)^2 + (-3)^2\cdot (-3/4) + (-3)^2 \cdot (-3/4)^2 + \dots \\
			&= 9 + 9 \cdot (-3/4) + 9 \cdot (-3/4)^2 + \dots.
		\end{align}

	Fyrsti liður raðarinnar er :math:`a=-3` og hlutfallstalan er :math:`r=-3/4`. Þar
	sem :math:`|r|=3/4 < 1` er röðin samleitin og summa hennar er

	.. math:: \frac{9}{1-(-3/4)} = \frac{36}{7}.

Skilgreining: Kíkisröð
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

	*Kíkisröð* er röð þar sem flestir liðir raðarinnar styttast út í hlutsummum hennar
	og eftir standa aðeins endanlega margir af fyrstu og síðustu liðum hlutsummanna.

Dæmi: Kíkisröð
~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Ákvörðum hvort kíkisröðin

	.. math:: \sum_{n=1}^\infty \left( \cos\left(\frac{1}{n}\right) - \cos\left(\frac{1}{n+1}\right) \right)

	sé samleitin eða ekki. Ef hún er samleitin, finnum þá summu hennar.

.. admonition:: Lausn
  :class: daemi, dropdown

	Ef við skrifum út liði hlutsummanna fáum við að

	.. math::
		\begin{align}
			S_1 &= \cos(1)-\cos(1/2)\\
			S_2 &= (\cos(1) - \cos(1/2))+(\cos(1/2)-\cos(1/3)) = \cos(1)-\cos(1/3)\\
			S_3 &= (\cos(1)-\cos(1/2)) + (\cos(1/2)-\cos(1/3)) + (\cos(1/3) - \cos(1/4))\\
			&= \cos(1)-\cos(1/4).
		\end{align}

	Almennt gildir því að

	.. math:: S_k = \cos(1) - \cos(1/(k+1)).

	Þar sem :math:`1/(k+1) \rightarrow 0` þegar :math:`k \rightarrow 0` og
	:math:`\cos(x)` er samfellt fall þá gildir að :math:`\cos(1/(k+1)) \rightarrow \cos(0)=1`.
	Þar með fæst að :math:`S_k \rightarrow \cos(1)-1`. Kíkisröðin er því samleitin og
	summa hennar er gefin með

	.. math:: \sum_{n=1}^\infty \left( \cos\left(\frac{1}{n}\right) - \cos\left(\frac{1}{n+1}\right) \right) = \cos(1) - 1.

---------

Sundurleitnipróf og heildispróf
--------------------------------

Ef röðin :math:`\sum_{n=1}^\infty a_n` á að vera samleitin verður að gilda
að :math:`a_n \rightarrow 0` þegar :math:`n \rightarrow \infty`. Því er hægt að setja
fram eftirfarandi setningu.

Setning: Sundurleitnipróf
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Ef :math:`\lim_{n \rightarrow \infty} a_n = c \neq 0` eða :math:`\lim_{n \rightarrow \infty} a_n`
	er ekki til þá er röðin :math:`\sum_{n=1}^\infty a_n` ósamleitin.

.. admonition:: Aðvörun
  :class: advorun

	Hið andstæða er ekki satt, það er ekki nóg að

	.. math:: \lim_{n \rightarrow \infty} a_n = 0

	til þess að röðin

	.. math:: \sum_{n=1}^\infty a_n

	sé samleitin. Við segjum við að :math:`\lim_{n \rightarrow \infty} a_n = 0` sé
	nauðsynleg en ekki nægjanleg forsenda fyrir samleitni raðar.

--------

Heildisprófið
--------------

Heildisprófið gerir samanburð á milli óendanlegrar summu og óeiginlegs heildis.

Setning: Heildisprófið
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Gerum ráð fyrir að :math:`\sum_{n=1}^\infty a_i` sé röð af jákvæðum liðum :math:`a_n`þ
	Gerum einnig ráð fyrir að til sé fall :math:`f` og jákvæð heiltala :math:`N`
	þannig að eftirfarandi þrjú skilyrði séu uppfyllt:

		#. :math:`f` er samfellt

		#. :math:`f` er minnkandi

		#. :math:`f(n)=a_n` fyrir allar heiltölur :math:`n \geq N`.

	Þá gildir að

	.. math:: \int_{n=1}^\infty a_n \text{ og } \int_N^\infty f(x) dx.

	eru annað hvort bæði samleitin eða bæði ósamleitin.
	Athugum að jafnvel þó samleitni heildisins :math:`\int_N^\infty f(x) dx` hafi það í
	för með sér að :math:`\sum_{n=1}^\infty a_n` sé samleitið þýðir það ekki að
	gildi þeirra er það saman.

Dæmi: Heildisprófið
~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Ákvörðum hvort röðin

	.. math:: \sum_{n=1}^\infty 1/n^3

	sé samleitin eða ekki.

.. admonition:: Lausn
  :class: daemi, dropdown

	Þar sem :math:`1/n^3 > 0` fyrir öll :math:`n \in \mathbb{N}` og fallið :math:`1/x^3`
	er samfellt, minnkandi og :math:`f(n)=a_n` fyrir öll :math:`n \in \mathbb{N}` þá
	getum við við nota heildisprófið. Berum saman

	.. math:: \sum_{n=1}^\infty \frac{1}{n^3} \text{ og } \int_1^\infty \frac{1}{x^3} dx.

	Höfum að

	.. math::
		\begin{align}
			\int_1^\infty \frac{1}{x^3} dx &= \lim_{b \rightarrow \infty} \int_1^b \frac{1}{x^3} dx\\
			&= \lim_{b \rightarrow \infty} - \frac{1}{2b^2} - \left( -\frac{1}{2\cdot 1^2}\right)\\
			&= 0 + \frac{1}{2}\\
			&= \frac{1}{2}.
		\end{align}

	Þar sem heildið :math:`\int_1^\infty \frac{1}{x^3} dx` er samleitið þá er röðin
	:math:`\sum_{n=1}^\infty \frac{1}{n^3}` það einnig.

:math:`p`-raðir
~~~~~~~~~~~~~~~~

Raðirnar :math:`\sum_{n=1}^\infty \frac{1}{n}` og :math:`\sum_{n=1}^\infty \frac{1}{n^2}`
eru dæmi um :math:`p`-raðir.

Skilgreining: :math:`p`-röð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

	Fyrir sérhverja rauntölu :math:`p` er röðin

	.. math:: \sum_{n=1}^\infty \frac{1}{n^p}

	kölluð :math:`p`-*röð*.

Nú er harmoníska röðin, þ.e. þar sem :math:`p=1`

.. math:: \sum_{n=1}^\infty \frac{1}{n}

ósamleitin en röðin

.. math:: \sum_{n=1}^\infty \frac{1}{n^2}

er samleitin. Við skulum velta því fyrir okkur hvað ræður því hvort :math:`p`-röð
sé samleitin.

Ef :math:`p<0` þá gildir að :math:`1/n^p \rightarrow \infty` og þegar :math:`p=0`
gildir að :math:`1/n^p \rightarrow 1`. Svo því fæst að

.. math:: \sum_{n=1}^\infty \frac{1}{n^p} \text{ er ósamleitin ef } p \leq 0.

Ef :math:`p>0` er :math:`f(x)=1/x^p` jákvætt, samfellt og minnkandi fall sem
uppfyllir að :math:`f(n)=a_n` fyrir öll :math:`n \in \mathbb{N}`. Því getum við
notað heildisprófið og borið saman

.. math:: \sum_{n=1}^\infty \frac{1}{n^p} \text{ og } \int_1^\infty \frac{1}{x^p} dx.

Við ætlum að skoða tilfellið þegar :math:`p>0, p \neq 1`. Í því tilfellið gildir að

.. math::
	\begin{align}
	\int_1^\infty \frac{1}{x^p} dx &= \lim_{b \rightarrow \infty} \left[ \frac{1}{1-p} x^{1-p}\right]_1^b\\
	&= \lim_{b \rightarrow \infty} \frac{1}{1-p} \left(b^{1-p}-1 \right).
	\end{align}

Þar sem

.. math:: b^{1-p} \rightarrow 0 \text{ ef } p>1 \text{ og } b^{1-p}\rightarrow \infty \text{ ef } p<1,

þá gildir að

.. math::
	\int_1^\infty \frac{1}{x^p} dx=
	\begin{cases}
		\frac{1}{p-1}, & p>1\\
		\infty, & p \leq 1
	\end{cases}
	.

Þar með gildir að

.. math::
	\sum_{n=1}^\infty 1/n^p
	\begin{cases}
		\text{samleitin ef } p>1\\
		\text{ósamleitin ef } p \leq 1
	\end{cases}
	.

Dæmi: Samleitni :math:`p`-raða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Ákvörðum hvort :math:`p`-röðin

	.. math:: \sum_{n=1}^\infty \frac{1}{n^{2/3}}

	sé samleitin.

.. admonition:: Lausn
  :class: daemi, dropdown

	Þar sem :math:`p = 2/3 < 1` er röðin ósamleitin.

Að meta gildi raða
~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að þekkt sé að röðin :math:`\sum_{n=1}^\infty a_n` sé samleitin og
nú viljum við ákvarða summu hennar. Ein leið væri að nota gildi hlutsummunnar :math:`\sum_{n=1}^N a_n`
til að nálga gildi raðarinnar. Spurningin er því hve gott slíkt mat væri. Ef við
látum

.. math:: R_n = \sum_{n=1}^\infty a_n - \sum_{n=1}^N a_n

hve stórt er þá :math:`R_N`? Sumar raðir leyfa okkur að nota svipaða aðferðarfræði
og notuð er í heildisprófinu til að meta *skekkjuna* :math:`R_n`.

Setning: Skekkjumat
~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Gerum ráð fyrir að þekkt sé að röðin :math:`\sum_{n=1}^\infty a_n` sé samleitin
	röð af jákvæðum liðum.
	Gerum einnig ráð fyrir að til sé fall :math:`f` og jákvæð heiltala :math:`N`
	þannig að eftirfarandi þrjú skilyrði séu uppfyllt:

		#. :math:`f` er samfellt

		#. :math:`f` er minnkandi

		#. :math:`f(n)=a_n` fyrir allar heiltölur :math:`n \geq N`.

	Látum :math:`S_n` vera :math:`N`-tu hlutsummu :math:`\sum_{n=1}^\infty a_n`.
	Fyrir allar jákvæðar heiltölur :math:`N` fæst að

	.. math:: S_n + \int_{N+1}^\infty f(x) dx < \sum_{n=1}^\infty a_n < S_n + \int_N^\infty f(x) dx.

	Með öðrum orðum þá uppfyllir skekkjan

	.. math:: R_n = \sum_{n=1}^\infty  a_n - S_n = \sum_{n=N+1}^\infty a_n

	eftirfarandi mat:

	.. math:: \int_{N+1}^\infty f(x) dx < R_n < \int_N^\infty f(x) dx.

	Þetta er þekkt sem *skekkjumatið*.

Dæmi: Skekkjumat
~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Lítum á röðina

	.. math:: \sum_{n=1}^\infty 1/n^3.

	a) Reiknum hlutsummuna :math:`S_{10} = \sum_{n=1}^{10} 1/n^3` og metum skekkjuna.

	b) Ákvörðum minnsta gildið á :math:`N` sem uppfyllir að skekkjan sé minni en :math:`0,001`.

.. admonition:: Lausn
  :class: daemi, dropdown

	a) Lausn:
		Reiknum og fáum að

		.. math:: S_{10} = 1 + \frac{1}{2^3} + \frac{1}{3^3} + \frac{1}{4^3} + \dots + \frac{1}{10^3} \approx 1,19753.

		Skekkjumatið gefur okkur að

		.. math:: R_n < \int_N^\infty \frac{1}{x^3} dx.

		Við höfum því að

		.. math::
			\begin{align}
				\int_{10}^\infty \frac{1}{x^3} dx &= \lim_{b \rightarrow \infty} \int_{10}^\infty \frac{1}{x^3} dx\\
				&= \lim_{b \rightarrow \infty} \left[-\frac{1}{2x^2}\right]_N^b\\
				&= \lim_{b \rightarrow \infty} \left(-\frac{1}{2b^2} + \frac{1}{2N^2}\right)\\
				&= \frac{1}{2N^2}.
			\end{align}

		Svo skekkjan er :math:`R_{10} < \frac{1}{2\cdot 10^2} = 0,005`.

	b) Lausn:
		Í a. hluta sýndum við að :math:`R_N < \frac{1}{2N^2}`. Þar með er
		skekkjan :math:`R_N < 0,001` svo lengi sem :math:`\frac{1}{2N^2} < 0,001`. Ef við
		einangrum :math:`N^2` fæst að :math:`N^2 > 500`. Við getum nú tekið rótina af báðum hliðum
		ójöfnunnar og þar sem :math:`N` er jákvæð tala fæst að lausnin sé :math:`N > 22,36`.
		Þar sem :math:`N` er heil tala þurfum við að námunda upp í næstu heilu tölu til
		að tryggja að skekkjan sé innan þeirra marga sem óskað var eftir. Því fæst að minnsta
		gildið sé :math:`N=23`.

Samanburðarprófið
------------------

Setning: Samanburðarprófið
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

		#. Gerum ráð fyrir að til sé heil tala :math:`N` þannig að :math:`0 \leq a_n \leq b_n` fyrir öll :math:`n \geq N`. Ef :math:`\sum_{n=1}^\infty b_n` er samleitið þá er :math:`\sum_{n=1}^\infty a_n` það einnig.

		#. Gerum ráð fyrir að til sé heil tala :math:`N` þannig að :math:`a_n \geq b_n \geq 0` fyrir öll :math:`n \geq N`. Ef :math:`\sum_{n=1}^\infty b_n` er ósamleitin þá er :math:`\sum_{n=1}^\infty a_n` það einnig.

Dæmi: Samanburðarprófið
~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Notum samanburðarprófið til að ákvarða hvort

	.. math:: \sum_{n=1}^\infty \frac{1}{n^3+3n+1}

	sé samleitin eða ekki.

.. admonition:: Lausn
  :class: daemi, dropdown

	Berum röðina sem gefin var við :math:`p`-röðina :math:`\sum_{n=1}^\infty \frac{1}{n^3}`.
	Höfum að

	.. math:: \frac{1}{n^3+3n+1} < \frac{1}{n^3}

	fyrir allar jákvæðar heiltölur :math:`n`. Þar sem :math:`p=3` segja niðurstöður
	okkar um :math:`p`-raðir að :math:`\sum_{n=1}^\infty \frac{1}{n^3}` sé samleitin og
	því er :math:`\sum_{n=1}^\infty \frac{1}{n^3+3n+1}` það einnig.

Setning: Samanburður með markgildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Látum :math:`a_n,b_n \geq 0` fyrir öll :math:`n \geq 1`.

		#. Ef :math:`\lim_{n \rightarrow \infty} a_n/b_n = L \neq 0` þá eru :math:`\sum_{n=1}^\infty a_n` og :math:`\sum_{n=1}^\infty b_n` annað hvort báðar samleitnar eða ósamleitnar.

		#. Ef :math:`\lim_{n \rightarrow \infty} a_n/b_n = 0` og :math:`\sum_{n=1}^\infty b_n` er samleitin þá er :math:`\sum_{n=1}^\infty a_n` það einnig.

		#. Ef :math:`\lim_{n \rightarrow \infty} a_n/b_n = \infty` og :math:`\sum_{n=1}^\infty b_n` er ósamleitin þá er :math:`\sum_{n=1}^\infty a_n` það einnig.

Dæmi: Samanburður með markgildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Notum samanburð með markgildi til að ákvarða hvort röðin

	.. math:: \sum_{n=1}^\infty \frac{1}{\sqrt{n}+1}

	sé samleitin eða ekki.

.. admonition:: Lausn
	:class: daemi, dropdown

	Berum röðina :math:`\sum_{n=1}^\infty \frac{1}{\sqrt{n}+1}` saman við :math:`\sum_{n=1}^\infty \frac{1}{\sqrt{n}}`.
	Reiknum markgildið

	.. math:: \lim_{n \rightarrow \infty} \frac{1/(\sqrt{n}+1)}{1/\sqrt{n}} = \lim_{n \rightarrow \infty} \frac{1}{1+1/\sqrt{n}} = 1

	Með því að nota samanburð með markgildi fæst að þar sem röðin :math:`\sum_{n=1}^\infty \frac{1}{\sqrt{n}}` er ósamleitin er röðin
	:math:`\sum_{n=1}^\infty \frac{1}{\sqrt{n}+1}` það einnig.

-----

Víxlmerkjaraðir
---------------

Raðir sem víxla formerkjum á öðrum hverjum lið, þ.e. annar hver liður er jákvæð
tala og hinir liðirnir á móti eru neikvæðar, nefnast *víxlmerkjaraðir*. Til að
mynda er röðin

.. math:: \sum_{n=1}^\infty \left( -\frac{1}{2} \right) = - \frac{1}{2} + \frac{1}{4} - \frac{1}{8} + \frac{1}{16} - \dots

víxlmerkjaröð.

Skilgreining: Víxlmerkjaröð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

	Sérhver röð sem hefur liði sem skiptast á að vera jákvæðir og neikvæðir á mis
	er kölluð *víxlmerkjaröð*. Víxlmerkjaröð má skrifa á forminu

	.. math:: \sum_{n=1}^\infty (-1)^{n+1} b_n = b_1 - b_2 + b_3 - b_4 + \dots

	eða

	.. math:: \sum_{n=1}^\infty (-1)^n b_n = -b_1 + b_2 - b_3 + b_4 + \dots

	þar sem :math:`b_n \geq 0` fyrir allar jákvæðar heiltölur :math:`n`.

Setning: Próf fyrir víxlmerkjaraðir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Víxlmerkjaröð á forminu

	.. math:: \sum_{n=1}^\infty (-1)^{n+1} b_n \text{ eða } \sum_{n=1}^\infty (-1)^n b_n

	er samleitin ef

	#. :math:`0 \leq b_{n+1} \leq b_n` fyrir öll :math:`n \geq 1` og
	#. :math:`\lim_{n \rightarrow \infty} b_n = 0`.

	Þetta er kallað *próf fyrir víxlmerkjaraðir*.

Dæmi: Próf fyrir víxlmerkjaröð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Ákvörðum hvort röðin

	.. math:: \sum_{n=1}^\infty (-1)^{n+1}/n^2

	sé samleitin eða ekki.

.. admonition:: Lausn
  :class: daemi, dropdown

	Þar sem

	.. math:: \frac{1}{(n+1)^2} < \frac{1}{n^2}

	og

	.. math:: \frac{1}{n^2} \rightarrow 0

	er röðin samleitin.

Setning: Skekkja í víxlmerkjaröðum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Lítum á víxlmerkjaröð á forminu

	.. math:: \sum_{n=1}^\infty (-1)^{n+1} b_n \text{ eða } \sum_{n=1}^\infty (-1)^n b_n

	sem uppfyllir skilyrði prófsins fyrir víxlmerkjaraðir. Látum :math:`S` merkja
	summu raðarinnar og :math:`S_N` tákna :math:`N`-tu hlutsummu raðarinnar. Fyrir
	sérhverja heiltölu :math:`N \geq 1` uppfyllir *skekkjan* :math:`R_N = S - S_N` að

	.. math:: |R_N| \leq b_{N+1}.

Dæmi: Skekkja víxlmerkjaraðar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Lítum á röðina

	.. math:: \sum_{n=1}^\infty \frac{(-1)^{n+1}}{n^2}.

	Notum skekkju víxlmerkjaraðar til þess að ákvarða efra mark fyrir skekkjuna :math:`R_{10}`
	ef við nálgum summuna með hlutsummunni :math:`S_{10}`.

.. admonition:: Lausn
  :class: daemi, dropdown

	Fáum að

	.. math:: |R_{10}| \leq b_{11} = \frac{1}{11^2} \approx 0,008265.

Skilgreining: Alsamleitni og skilyrt samleitni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

	Röð :math:`\sum_{n=1}^\infty a_n` er *alsamleitin* ef röðin :math:`\sum_{=1}^\infty |a_n|`
	er samleitin. Röðin :math:`\sum_{n=1}^\infty a_n` er *skilyrt samleitin* ef
	:math:`\sum_{n=1}^\infty a_n` er samleitin en :math:`\sum_{n=1}^\infty |a_n|` er
	ósamleitin.

Setning: Alsamleitni leiðir til samleitni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Ef :math:`\sum_{n=1}^\infty |a_n|` er samleitin þá er :math:`\sum_{n=1}^\infty a_n`
	það einnig.

Dæmi: Alsamleitni vs. skilyrt samleitni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Ákvörðum hvort eftirfarandi raðir séu alsamleitnar,
	skilyrt samleitnar eða ósamleitnar.

		a) :math:`\sum_{n=1}^\infty (-1)^{n+1}/(3n+1)`

		b) :math:`\sum_{n=1}^\infty \cos(n)/n^2`.

.. admonition:: Lausn
  :class: daemi, dropdown

		a) Lausn:
			Við getum séð að

			.. math:: \sum_{n=1}^\infty \left| \frac{(-1)^{n+1}}{3n+1} \right| = \sum_{n=1}^\infty \frac{1}{3n+1}

			sem er ósamleitin með því að nota samanburð með markgildi fyrir harmoníska röð. Raunar gildir að

			.. math:: \lim_{n \rightarrow \infty} \frac{1/(3n+1)}{1/n} = \frac{1}{3}.

			Þar með er röðin ekki alsamleitin. Hinsvegar gildir að

			.. math:: \frac{1}{3(n+1)+1} < \frac{1}{3n+1} \text{ og } \frac{1}{3n+1} \rightarrow 0.

			og þar með er röðin samleitin. Við ályktum sem svo að röðin :math:`\sum_{n=1}^\infty (-1)^{n+1}/(3n+1)`
			sé skilyrt samleitin.

		b) Lausn:
			Tökum eftir að :math:`|\cos(n)| \leq 1` og notum það til að ákvarða hvort röðin
			sé alsamleitin. Berum röðina

			.. math:: \sum_{n=1}^\infty \left| \frac{\cos(n)}{n^2} \right|

			saman við :math:`\sum_{n=1}^\infty 1/n^2`. Þar sem :math:`\sum_{n=1}^\infty 1/n^2`
			er samleitin fæst skv. samanburðarprófinu að :math:`\sum_{n=1}^\infty |\cos(n)/n^2|`
			sé samleitin og þar með er :math:`\sum_{n=1}^\infty \cos(n)/n^2` alsamleitin.

Dæmi: Munurinn á alsamleitni og skilyrtri samleitni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Lítum á röðina

	.. math:: \sum_{n=1}^\infty (-1)^{n+1} \frac{1}{n}.

	Gefið er að röðin er skilyrt samleitin og að

	.. math:: \sum_{n=1}^\infty (-1)^{n+1} \frac{1}{n} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \dots = \ln(2).

	Látum nú

	.. math:: \sum_{n=1}^\infty a_n = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \frac{1}{6} + \frac{1}{7} - \frac{1}{8} + \dots.

	Þar sem :math:`\sum_{n=1}^\infty a_n = \ln(2)` getum við notað reiknireglur um
	samleitnar raðir til að fá að

	.. math:: \sum_{n=1}^\infty \frac{1}{2}a_n = \frac{1}{2} - \frac{1}{4} + \frac{1}{6} - \frac{1}{8} + \dots = \frac{1}{2} \sum_{n=1}^\infty a_n = \frac{\ln(2)}{2}.

	Kynnum nú til sögunnar röðina :math:`\sum_{n=1}^\infty b_n` sem uppfyllir að fyrir
	öll :math:`n \geq 1` að :math:`b_{2n-1} = 0` og :math:`b_{2n} = a_n/2`. Þá gildir að

	.. math:: \sum_{n=1}^\infty b_n = 0 + \frac{1}{2} - 0 - \frac{1}{4} + 0 + \frac{1}{6} + 0 - \frac{1}{8} + \dots = \frac{\ln(2)}{2}.

	Notum nú þann eiginleika samleitinna raða að þar sem :math:`\sum_{n=1}^\infty a_n` og
	:math:`\sum_{n=1}^\infty b_n` eru samleitnar þá er :math:`\sum_{n=1}^\infty (a_n + b_n)`
	samleitin og fáum að

	.. math:: \sum_{n=1}^\infty (a_n + b_n) = \sum_{n=1}^\infty a_n + \sum_{n=1}^\infty b_n = \ln(2) + \frac{\ln(2)}{2} = \frac{3 \ln(2)}{2}.

	Ef við leggjum nú saman samsvarandi liði :math:`a_n` og :math:`b_n` sjáum við að

	.. math::
		\begin{aligned}
			\sum_{n=1}^\infty (a_n+b_n) &= (1+0)+ (-\tfrac{1}{2}+-\tfrac{1}{2}) + (\tfrac{1}{3}+0)+(-\tfrac{1}{4}+\tfrac{1}{4})+(\tfrac{1}{5}+0)\\
			&+(-\tfrac{1}{6}+\tfrac{1}{6}) + (\tfrac{1}{7}+0)+(-\tfrac{1}{8}+\tfrac{1}{8}) + \dots \\
			&= 1 + \frac{1}{3}-\frac{1}{2}+\frac{1}{5}+\frac{1}{7}-\frac{1}{4} + \dots \quad (*)\\
			&= \frac{3\ln(2)}{2}
		\end{aligned}

	þar sem síðasta skrefið er samkvæmt því sem við fundum hér að ofan.
	Athugum að röðin sem merkt er með :math:`(*)` inniheldur nákvæmlega sömu
	liði og upprunalega röðin okkar

	.. math:: \sum_{n=1}^\infty a_n = \sum_{n=1}^\infty (-1)^{n+1} \frac{1}{n} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \frac{1}{6} + \frac{1}{7} - \dots.

	nema þeir birtast með annarri uppröðun. Höfum í huga að :math:`\sum_{n=1}^\infty a_n = \ln(2)`
	en :math:`\sum_{n=1}^\infty (a_n + b_n) = \frac{3\ln(2)}{2}`.
	Svo bara með því að breyta uppröðuninni á liðum raðarinnar gátum við sýnt fram á að
	summa raðarinnar breyttist, þ.e. tvær raðir sem eru alveg eins nema að því leyti
	að liðir þeirra birtast ekki í sömu röð hafa tvær, mismunandi summur.

	Þetta er einn af mikilvægustu og skrítnustu eiginleikum raða sem eru skilyrt samleitnar, þ.e.
	það að breyta því í hvaða röð liðir eru lagðir saman getur breytt summu raðarinnar.
	Þetta er hins vegar ekki hægt að gera í alsamleitnum röðum. Þar skiptir engu máli
	í hvaða röð liðir eru lagðir saman, summan er alltaf sú saman.

-------

Kvóta- og rótarpróf
--------------------

Setning: Kvótaprófið
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Látum :math:`\sum_{n=1}^\infty a_n` vera röð með enga núllliði. Látum

	.. math:: \rho = \lim_{n \rightarrow \infty} \left| \frac{a_{n+1}}{a_n} \right|.

	Þá gildir eftirfarandi:

		#. Ef :math:`0 \leq \rho < 1` er röðin alsamleitin.

		#. Ef :math:`\rho > 1` eða :math:`\rho = \infty` er röðin ósamleitin.

		#. Ef :math:`\rho = 1` er niðurstaða prófsins ófullnægjandi og segir okkur ekkert um samleitni raðarinnar.

Dæmi: Kvótaprófið
~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Notum kvótaprófið til að ákvarða hvort röðin

	.. math:: \sum_{n=1}^\infty \frac{2^n}{n!}

	sé samleitin eða ekki.

.. admonition:: Lausn
  :class: daemi, dropdown

	Samkvæmt rótarprófinu fæst að

	.. math:: \rho = \lim_{n \rightarrow \infty} \frac{2^{n+1}/(n+1)!}{2^n/n!} = \lim_{n \rightarrow \infty} \frac{2^{n+1}}{(n+1)!} \cdot \frac{n!}{2^n}.

	Þar sem :math:`(n+1)! = (n+1)\cdot n!` fæst að

	.. math:: \rho = \lim_{n \rightarrow \infty}  \frac{2}{n+1}=0.

	Þar sem :math:`0 \leq \rho < 1` fæst að röðin sé samleitin.

Setning: Rótarprófið
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Lítum á röðina :math:`\sum_{n=1}^\infty a_n`. Látum

	.. math:: \rho = \lim_{n \rightarrow \infty} \sqrt[n]{a_n}.

	#. Ef :math:`0 \leq \rho < 1` er röðin alsamleitin.

	#. Ef :math:`\rho > 1` eða :math:`\rho = \infty` er röðin ósamleitin.

	#. Ef :math:`\rho = 1` er niðurstaða prófsins ófullnægjandi og segir okkur ekkret um samleitni raðarinnar.

Dæmi: Rótarprófið
~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Notum rótarprófið til að ákvarða hvort röðin

	.. math:: \sum_{n=1}^\infty \frac{(n^2+3n)^n}{(4n^3+5)^n}

	sé samleitin eða ekki.

.. admonition:: Lausn
  :class: daemi, dropdown

	Reiknum

	.. math:: \rho = \lim_{n \rightarrow \infty} \sqrt[n]{(n^2 + 3n)^n /(4n^2+5)^n} = \lim_{n \rightarrow \infty} \frac{n^2+3n}{4n^2+5} = \frac{1}{4}.

	Þar sem :math:`0 \leq \rho < 1` er röðin alsamleitin.

------

Samantekt
---------

.. list-table:: Gátlisti fyrir raðir
	:widths: 20 15 15
	:header-rows: 1

	* - Próf eða röð
	  - Niðurstöður
	  - Athugasemdir
	* - **Sundurleitnipróf:**

		Fyrir sérhverjaröð :math:`\sum_{n=1}^\infty a_n` metum við markgildið

		.. math:: \lim_{n \rightarrow \infty} a_n.
	  -

		Ef markgildið :math:`\lim_{n \rightarrow \infty} a_n = 0` er prófið ómarktækt.

		Ef :math:`\lim_{n \rightarrow \infty} a_n \neq 0` er röðin ósamleitin.
	  - Ekki er hægt að nota prófið til að sýna fram á samleitni raða.
	* - **Geómetrískar raðir:**

			:math:`\sum_{n=1}^\infty ar^{n-1}`
	  - Ef :math:`|r|<1` er röðin samleitin að :math:`a/(1-r)` en annars er hún ósamleitin.
	  -

			Sérhverja geómetrísk röð má skrifa á forminu :math:`a + ar + ar^2 + \dots`.

			Talan :math:`a` nefnist fyrsti liður raðarinnar.

			Talan :math:`r` nefnist hlutfallstala raðarinnar.
	* - :math:`p`-**raðir:**

			:math:`\sum_{n=1}^\infty \frac{1}{n^p}`
	  - Ef :math:`p > 1` er röðin samleitin, annars ekki.
	  - Fyrir :math:`p=1` er röðin kölluð harmoníska röðin.
	* - **Samanburðarpróf:**

			Ef :math:`a_n \geq 0`, :math:`n=1,2,3,\dots` berum við

			:math:`\sum_{n=1}^\infty a_n` saman við :math:`\sum_{n=1}^\infty b_n`.
	  -

		Ef :math:`a_n \leq b_n` fyrir öll :math:`n \geq N` og :math:`\sum_{n=1}^\infty b_n`
		er samleitin þá er :math:`\sum_{n=1}^\infty a_n` samleitin.

		Ef :math:`a_n \leq b_n` fyrir öll :math:`n \geq N` og :math:`\sum_{n=1}^\infty b_n`
		er ósamleitin þá er :math:`\sum_{n=1}^\infty a_n` ósamleitin.
	  -

		Oftast notað fyrir raðir sem svipa til :math:`p`-raða eða geómetrískra raða.

		Erfitt getur verið að finna viðeigandi röð til samanburðar.
	* - **Samanburður með markgildi:**

		Ef :math:`a_n > 0`, :math:`n=1,2,3,\dots` berum við :math:`\sum_{n=1}^\infty a_n`

		saman við :math:`\sum_{n=1}^\infty b_n` með því að meta markgildið

		.. math:: L = \lim_{n \rightarrow \infty} \frac{a_n}{b_n}.
	  -

			Ef :math:`L \in \mathbb{R} \setminus \{0\}` þá eru annað hvort :math:`\sum_{n=1}^\infty a_n` og :math:`\sum_{n=1}^\infty b_n` bæði samleitin eða bæði ósamleitin.

			Ef :math:`L=0` og :math:`\sum_{n=1}^\infty b_n` er samleitin þá er :math:`\sum_{n=1}^\infty a_n` einnig samleitin.

			Ef :math:`L=\infty` og :math:`\sum_{n=1}^\infty b_n` er ósamleitin þá er :math:`\sum_{n=1}^\infty a_n` einnig ósamleitin.
	  -

		Oftast notað fyrir raðir sem svipa til :math:`p`-raða eða geómetrískra raða.

		Oft auðveldara í notkun en samanburðarprófið.
	* - **Heildispróf:**

		Ef til er jákvætt, samfellt, minnkandi fall :math:`f`

		þ.a. :math:`a_n=f(n)` fyrir öll :math:`n \geq N` reiknum við

		.. math:: \int_N^\infty f(x) dx.
	  - Ef :math:`b_{n+1} \leq b_n` fyrir öll :math:`n \geq 1` og :math:`b_n \rightarrow 0` þá er röðin samleitin.
	  - Takmarkað við þær raðir sem hafa samsvarandi fall sem auðvelt er að heilda.
	* - **Víxlmerkjaraðir:**

		.. math:: \sum_{n=1}^\infty (-1)^{n+1}b_n \text{ eða } \sum_{n=1}^\infty (-1)^{n}b_n.
	  - Ef :math:`b_{n+1} \leq b_n` fyrir öll :math:`n \geq 1` og :math:`b_n \rightarrow 0` þá er röðin samleitin.
	  - Á aðeins við um víxlmerkjaraðir.
	* - **Kvótapróf:**

		Fyrir hvaða röð :math:`\sum_{n=1}^\infty a_n` þar sem :math:`a_n \neq 0`

		fyrir :math:`n=1,2,3,\dots` látum við

		.. math:: \rho = \lim_{n \rightarrow \infty} \left| \frac{a_{n+1}}{a_n} \right|.
	  -

		Ef :math:`0 \leq \rho < 1` er röðin alsamleitin.

		Ef :math:`\rho > 1` eða :math:`\rho = \infty` er röðin ósamleitin.

		Ef :math:`\rho = 1` er prófið ómarktækt og segir okkur ekkert.
	  - Oft notað fyrir raðir sem innihalda hrópmerkingar eða veldi.
	* - **Rótarpróf:**

		Fyrir hvaða röð :math:`\sum_{n=1}^\infty a_n` sem er látum við

		.. math:: \rho = \lim_{n \rightarrow \infty} \sqrt[n]{|a_n|}.
	  -

		Ef :math:`0 \leq \rho < 1` er röðin alsamleitin.

		Ef :math:`\rho > 1` eða :math:`\rho = \infty` er röðin ósamleitin.

		Ef :math:`\rho = 1` er prófið ómarktækt og segir okkur ekkert.
	  - Oft notað fyrir raðir sem innihalda :math:`|a_n|=b_n^n`.
