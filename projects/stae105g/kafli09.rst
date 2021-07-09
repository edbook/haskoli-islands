Runur og raðir
===============

.. note::
	**Nauðsynleg undirstaða**

	- Eitthvað

	- Eitthvað

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

Runum má líka lísa með *rakningarvenslum*. Þá er sagt að

.. math::
  \begin{cases}
    a_1=2\\
    a_n = 2a_{n-1}, & n \geq 2.\\
  \end{cases}

Skilgreining: Runa
~~~~~~~~~~~~~~~~~~~

*Runan* :math:`{a_n}` er raðaður listi á forminu

.. math:: a_1, a_2, a_3, \dots, a_n, \dots

þar sem :math:`n` er kallaður *knévísir* rununnar og hvert :math:`a_n` er
*liður* hennar. Sumar runur eiga sér *lokað form* en þá er hægt að lýsa
hverjum lið hennar með einhverju falli af :math:`n`, þ.e. :math:`a_n = f(n)`
þar sem :math:`n` er náttúruleg tala. Í öðrum tilfellum má lýsa sérhverjum lið
með *rakningarvenslum* þar sem hver liður er skilgreindur með lið sem kom á undan í
rununni, nema upphafsliðurinn sem er þá gefinn.

Athugum að ekkert er því til fyrirstöðu að láta knévísinn byrja á annarri tölu en
:math:`n=1`. Oft er notast við að upphafsliðurinn sé liður númer núll, þ.e.
:math:`a_0` en runan mætti þess vegna byrja á :math:`a_2` eða :math:`a_{-3}` sé
þörf fyrir því. Tvær týpur af runum koma oft fyrir í kennslubókum, það eru *jafnmunaruna* (einnig
kölluð mismunaruna) og *geómetrísk runa*.

Í **jafnmunarunu** er mismunur milli allra liða það sama. Til að mynda er runan

.. math:: 3,7,11,15,19,\dots

jafnmunaruna því það munar 4 á öllum liðunum og má nota rakningarvenslin

.. math::
  \begin{cases}
    a_1=3\\
    a_n = a_{n-1}+4, & n \geq 4
  \end{cases}

Almennt má skrifa jafnmunarunu á forminu :math:`a_n=cn+b`.

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

Þar sem fyrsti liður rununnar er :math:`2` og hlutfallið :math:`-\frac{1}{3}`
þá má einnig lýsa sérhverjum lið númer :math:`n` í rununni með lokaða forminu

.. math:: a_n = 2\left(-\frac{1}{3}\right)^{n-1}.

Almennt má skrifa geómetríska runu á forminu :math:`a_n=cr^n`.

Dæmi: Lokað form
~~~~~~~~~~~~~~~~~

Finnum lokað form rununnar

.. math:: \frac{3}{4}, \frac{9}{7}, \frac{27}{10}, \frac{81}{13}, \frac{243}{16},\dots.

Teljarar brotanna eru :math:`3,9,27,81,243` á meðan nefarar þeirra eru :math:`4,7,10,13,16`.
Við sjáum að fyrri runan er geómetrísk runa þar sem sérhver liður er þrefalt stærri
en liðurinn á undan á meðan seinni runan er jafnmunaruna þar sem það munar 3 á
hverjum tveimur aðliggjandi liðum. Fyrri rununni má því lýsa með :math:`3^n` en
þeirri seinni :math:`3n+1`. Lokað form rununnar er því

.. math:: a_n = \frac{3^n}{3n+1}.

Dæmi: Lokað form
~~~~~~~~~~~~~~~~~

Finnum lokað form rununnar sem skilgreind er með rakningarvenslunum

.. math::
  \begin{cases}
    a_1=2\\
    a_n = -3a_{n-1}, & n \geq 2.
  \end{cases}

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
Þar sem runa er fall sem er skilgrein á náttúrulegu tölunum er rökrétt að
leiða hugann að því hvort allir liðirnir stefni á sama gildið, þ.e. hvort
markgildi liðanna í rununni sé samleitið.

Skilgreining: Markgildi runu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Af því gefnu að liðir rununnar :math:`\{a_n\}` nálgist gildið :math:`L` óendanlega
mikið eftir því sem :math:`n` stækkar segjum við að :math:`\{a_n\}` sé *samleitin runa*
og að :math:`L` sé *markgildi rununnar*. Við ritum þá að

.. math:: \lim_{n \rightarrow \infty} a_n = L.

Ef runan :math:`\{a_n\}` er ekki samleitin segjum við að hún sé *ósamleitin runa*.

Skilgreining
~~~~~~~~~~~~~

Runan :math:`\{a_n\}` er samleitin á rauntölu :math:`L` fyrir öll :math:`\varepsilon > 0`
er til heil tala :math:`N` þannig að :math:`|a_n - L|<\varepsilon` ef :math:`n \geq N`.
Þá er talan :math:`L` kölluð markgildi rununnar og við skrifum

.. math:: \lim_{n \rightarrow \infty} a_n = L \text{ eða } a_n \rightarrow L.

Þá er runan :math:`\{a_n\}` s0gð ver asamleitin runa. Runa sem er ekki samleitin
er kölluð ósamleitin runa og við segjum að markgildi hennar sé ekki til.


Dæmi: Samleitin og ósamleitin runa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Runan

.. math:: -1, 1, -1, 1, -1, 1, \dots = \{(-1)^n\}

kallast *víxlruna* þar sem annar hver liður er sá sami og víxlar runan þannig
á milli tveggja gilda. Þessi runa er ekki samleitin af því að liðirnir heldur
óendanlega áfram að víxla á milli gildanna -1 og 1 og nálgast runan því ekki
eina ákveðna tölu :math:`L`.

Runan

.. math:: 1,2,3,4,5,6, \dots = \{n\}

er einnig ósamleitin af því að

.. math:: \lim_{n \rightarrow \infty} a_n = \infty

og til þess að runa sé samleitin verður markgildi hennar að vera einhver
tala :math:`L < \infty`. Hinsvegar er runan

.. math:: 1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \frac{1}{5}, \dots = \{\frac{1}{n}\}

samleitin þar sem liðirnir verða alltaf minni og minni og stefna á endanum á 0,
þ.e.

.. math:: \lim_{n \rightarrow \infty } a_n  = 0.

Setning: Markgildi runu skilgreint með falli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lítum á rununa :math:`\{a_n\}` uppfylla að :math:`n`-ta staki hennar má lýsa
með fallinu :math:`f(n)`, þ.e. :math:`a_n=f(n)` fyrir öll :math:`n\geq 1`. Ef
til er rauntala :math:`L` þannig að

.. math:: \lim_{x \rightarrow \infty} f(x)=L

er sagt að runan sé samleitin og

.. math:: \lim_{n \rightarrow \infty a_n} = L.

Við getum notað þessa setningu til að meta markgildið

.. math:: \lim_{n \rightarrow \infty } r^n

fyrir :math:`0 \leq r < 1`. Við skulum líta á rununa :math:`\{(1/2)^n\}` og
sambærilegt vísisfall :math:`f(x)=(1/2)^x`. Þar sem

.. math:: \lim_{x \rightarrow \infty} (1/2)^x = 0

getum við staðhæft að runan  :math:`\{(1/2)^n\}` hafi markgildið 0. SAmbærilega
gildir fyrir sérhverja rauntölu :math:`r` sem uppfyllir að :math:`0 \leq r < 1`
að

.. math:: \lim_{x \rightarrow \infty} r^x = 0

og þar með er runan :math:`\{r^n\}` samleitin. Ef hins vegar :math:`r=1` er
markgildið


.. math:: \lim_{x \rightarrow \infty} r^x = 1

og runan er samleitin með markgildið 1. Ef hins vegar :math:`r>1` er

.. math:: \lim_{x \rightarrow \infty} r^x = \infty

og við getum þar með ekki beitt þessari setningu. Í því tilfelli. Af þessu
leiðir að

.. math::
  \begin{align}
    r^n &\rightarrow 0 \text{ ef } 0 < r < 1\\
    r^n &\rightarrow 1 \text{ ef } r=1\\
    r^n &\rightarrow \infty \text{ ef } r > 1\\
  \end{align}

Setning: Markgildisreglur
~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`\{a_n\}` og :math:`\{b_n\}` vera gefnar runur og :math:`c` einhverja
rauntölu. Ef til eru fastar :math:`A` og :math:`B` þannig að :math:`\lim_{n \rightarrow \rightarrow} a_n = A`
:math:`\lim_{n \rightarrow \rightarrow} b_n = B`. Þá gildir

  #. :math:`\lim_{n \rightarrow \infty} c = c`

  #. :math:`\lim_{n\rightarrow \infty} ca_n = c\lim_{n\rightarrow \infty}a_n = cA`

  #. :math:`\lim_{n\rightarrow \infty} (a_n \pm b_n) = \lim_{n\rightarrow \infty} a_n \pm \lim_{n\rightarrow \infty} b_n = A \pm B`

  #. :math:`\lim_{n\rightarrow \infty} (a_n \cdot b_n) = \left(\lim_{n\rightarrow \infty} a_n \right) \cdot \left(\lim_{n\rightarrow \infty} b_n \right) = A \cdot B`

  #. :math:`\lim_{n\rightarrow \infty} \lim_{n\rightarrow \infty} \left( \frac{a_n}{b_n} \right) = \frac{\lim_{n\rightarrow \infty} a_n}{\lim_{n\rightarrow \infty} b_n} = \frac{A}{B}` af því gefnu að :math:`B \neq 0` og hvert :math:`b_n \neq 0`.

Dæmi: Ákvaðra samleitni og reikna markgildið
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ákvörðum hvort runan

.. math:: \left\{5 - \frac{3}{n^2} \right\}

sé samleitin og ef svo er reiknum þá markgildi hennar.

Við vitum að :math:`1/n \rightarrow 0` og því gildir að

.. math:: \lim_{n \rightarrow \infty} \frac{1}{n^2} = \lim_{n \rightarrow \infty} \left(\frac{1}{n}\right) \cdot \lim_{n \rightarrow \infty} \left(\frac{1}{n}\right)  = 0 \cdot 0 = 0.

Svo markgildi rununnar er

.. math:: \lim_{n \rightarrow \infty} 5 - \frac{3}{n^2} = \lim_{n \rightarrow \infty} 5 - 3  \lim_{n \rightarrow \infty} \frac{1}{n^2} = 5 - 3\cdot 0 = 5.




d
