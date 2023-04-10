.. include:: rst-include

Dæmi um hagnýtingu fylkjareikninga
==================================

Fylkjamargföldun og tölvugrafík
-------------------------------

.. rubric:: Nokkrar myndavarpanir

Hægt er að líta á flatarmyndir, t.d. hringi, þríhyrninga, eða myndir af húsum
sem mengi af punktum í plani, og punktarnir jafngilda svo auðvitað tvívíðum vigrum. Ef við höfum gefið fylki :math:`A` þá er hægt að skilgreina vörpun eða fall frá planinu yfir í sjálft sig sem svarar til margföldunar með :math:`A`, með öðrum orðum:

.. math:: f_A: \Bbb{R}^2 \to \Bbb{R}^2, f_A(x) = Ax
          
Svo má beita fallinu á alla punkta flatarmyndar og skoða myndmengið sem kemur út. Nokkrar tegundir af fylkjum svara til vel þekktra breytinga á flatarmyndunum, þeirra á meðal eru:

- **snúningur** (*rotation*) um tiltekið horn miðað við :math:`(0,0)`
- **skölun** (*scaling*) í x- og/eða y-stefnu
- **skekking** (*shear deformation*) um tiltekið horn
- **speglun** (*reflection*) um x-ás eða y-ás

Sem dæmis er fylkið:

.. math:: K = \begin{pmatrix} 1 & \sin 30° \\ 0 & 1 \end{pmatrix}

skekkingarfylki sem hallar lóðréttum línum um 30° til hægri. Aftar í þessum
kafla eru formúlur fyrir fleiri fylkjum, en skoðum þær fyrst myndrænt með dæmum:

.. figure:: myndir/tvividarvarpanir.png
   :width: 100%
   :align: center

Svona fylkjamargföldunarvarpanir eru kallaðar **línulegar varpanir** (*linear
mappings*). Þær hafa þann eiginleika að línustrik varpast í línustrik, þannig að
til að finna myndmengi slíks striks nægir að varpa endapunktum þess.

.. rubric:: Samskeyting varpana er fylkjamargföldun

Með því að skeyta slíkum vörpunum saman má svo t.d. spegla um hvaða ás sem er
(snúa, spegla, snúa til baka) eða bæði skala og skekkja (feitletra og skáletra).
Svona samskeyting varpananna svarar til fylkjamargföldunar því að:

.. math::
   &f_A(f_B(x)) = f_A(Bx) = ABx\quad\text{þ.e.a.s.}\\ 
   &f_A \circ f_B = f_{AB}

Svo er hægt að framkvæma hliðrun með því að leggja hliðrunarvigur, :math:`h` við alla punkta mengisins. Þá erum við að nota fallið

.. math:: g_h: \Bbb{R}^2 \to \Bbb{R}^2, g_h(x) = x + h

Með því að skeyta saman hliðrun og fylkjavörpununum er svo t.d. hægt að snúa
miðað við hvaða punkt sem er (hliðra, snúa og hliðra til baka).

.. rubric:: Myndmengi fundið með einni fylkjamargföldun

Ef mynd samanstendur af punktunum :math:`(x_1, y_1), (x_2, y_2),\ldots (x_n, y_n)` og strikum milli þeirra má varpa myndinni með fylki :math:`A` með því að byrja á að búa til fylkið

.. math:: B = \begin{pmatrix}x_1 & x_2 & \cdots & x_n\\y_1 & y_2 & \cdots & y_n\end{pmatrix}

reikna svo

.. math:: AB = C = \begin{pmatrix}c_1 & c_2 & \cdots & c_n\\d_1 & d_2 & \cdots & d_n\end{pmatrix}

Svo eru búnir til punktar :math:`(c_1, d_1), (c_2, d_2), \ldots` úr dálkunum í C og nýja myndin fæst með því að tengja þá saman með strikum. Í Python er hægt að "lyfta pennanum" og hoppa á nýjan stað með því að hafa dálka af svokölluðum *ekki-tölum* (*not-a-number*) sem hægt er að búa til með ``nan`` eftir innflutning ``from math import nan``.

.. admonition:: Sýnidæmi: Rétthyrningur með striki
   :class: synidaemi

   .. figure:: myndir/rétthyrningur-með-striki.png
      :width: 3cm
      :align: right

   Hér er dæmi um fylki sem lýsir rétthyrningi með striki inni í sér (sjá mynd):

   .. math::
      M = \begin{pmatrix}
      0 & 3 & 3 & 0 & 0 & \text{nan} & 1 & 2 \\
      0 & 0 & 2 & 2 & 0 & \text{nan} & 1 & 1
      \end{pmatrix}

   .. figure:: myndir/samsíðungur.png
      :width: 4cm
      :align: right

   Ef :math:`K` er skekkingarfylkið sem gefið er hér neðar myndi fylkið

   .. math:: C = KM

   lýsa samsíðungi með striki.

.. _formúlur-fyrir-vörpunarfylkjum:

.. rubric:: Formúlur fyrir tvívíðum vörpunarfylkjum

**SNÚNINGSFYLKI** sem snýr mynd rangsælis um hornið :math:`\theta` með
snúningspunkt :math:`(0,0)` er gefið með

.. math::
   R_{\theta} = \begin{pmatrix}
   \cos \theta & -\sin \theta \\
   \sin \theta & \cos \theta
   \end{pmatrix}

Til að spegla réttsælis má nota neikvætt :math:`\theta`.
   
**SKÖLUNARFYLKI** sem skalar um :math:`a` í :math:`x`-stefnu og :math:`b` í
:math:`y`-stefnu er

.. math::
   S_{a,b} = \begin{pmatrix}a & 0 \\ 0 & b \end{pmatrix}

**SKEKKINGARFYLKI:**

.. math::
   K_{x,\theta} = \begin{pmatrix} 1 & \sin \theta \\ 0 & 1 \end{pmatrix}
   \;\text{ og }\;
   K_{y,\theta} = \begin{pmatrix} 1 & 0 \\ \sin \theta & 1 \end{pmatrix}

:math:`K_{x,\theta}` hallar lóðréttum línum um horn :math:`\theta` til hægri en varðveitir
láréttar línur, og :math:`K_{y,\theta}` hallar láréttum línum upp en varðveitir þær
lóðréttu. Til að halla til vinstri eða niður má nota neikvætt :math:`\theta`.

**SPEGLUNARFYLKI** sem spegla um :math:`x`-ás og :math:`y`-ás eru

.. math::
   M_x = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \;\text{ og }\;
   M_y = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}

.. rubric:: Fylki í tölvugrafík

Allar þessar aðgerðir eru grunnaðgerðir í tölvugrafík. Hliðranir eru stundum
líka útfærðar með fylkjamargföldun með því að bæta við gervihniti og vinna með
svonefnd *jafnþætt* eða *hómógen* (*homogeneous*) hnit, þrívíða vigra og
:math:`3 \times 3` fylki.

Nútíma tölvugrafík er svo auðvitað oftast þrívíð og þar þarf að takast á við
þrívíða snúninga, speglanir og skalanir, og auk þess bæði hliðranir og 
fjarvídd (*perspective*). Allt þetta er hægt að útfæra með fjórvíðum
vigrum og :math:`4 \times 4` fylkjum, þar sem eitt hnitið er gervihnit.

.. admonition:: Æfing: Snúið, skekkt og speglað.
   :class: aefing

   Leysið :numref:`verkefni %s <æfing í tölvugrafík>`: Æfing í tölvugrafík.

.. admonition:: Athugasemd: 
   :class: athugid

   Til að varpanirnar sem hér hefur verið lýst gefi réttar myndir í Matplotlib
   teiknigluggum þarf að gæta þess að einingar á x- og y-ás séu jafnar. Það má
   gera með því að láta stærð myndarinnar (sem stilla má með
   ``figure(figsize=...)``) passa við fjölda eininga á hvorum ás fyrir sig, en
   svo er líka hægt að enda með skipuninni ``plt.axis('scaled')`` sem mjókkar
   eða breikkar myndina til að einingar á x- og y-ás verði jafnar, eða
   skipuninni ``plt.axis('equal')`` sem breytir mörkum á x-ás til að einingarnar
   verði jafnar.
   
Fylki og net
------------

**Net** (*graph* eða *network*) er safn af **hnútum** (eða *punktum*) (*vertices*, nodes*) og **leggjum** (*edges*) milli hnútanna. Net geta verið **stefnd** (*directed*) eða **óstefnd**, og þegar þau eru stefnd eru leggirnir stundum kallaðir örvar. Net geta líka haft leggi sem tengja punkta við sjálfa sig, kallaðir **snörur** (*loops*). :numref:`dæmi-um-net` sýnir dæmi um net. Netið í miðjunni er það sama og netið til hægri.

.. figure:: myndir/dæmi-um-net.png
   :width: 13cm
   :name: dæmi-um-net
   :align: center

   Óstefnt net (t.v.) og stefnt net (í miðju og t.h.).

Margar fleiri myndir af netum má skoða með því að gúgla *graph mathematics* og
smella á *images*.

.. admonition:: Skilgreining: Grannafylki 
   :class: regla
   
   **Grannafylki** (*adjacency matrix*) stefnds nets er fylki :math:`A` með

   .. math::
      a_{ij} = \left\{\begin{array}{ll}
      1 &\text{ef það er ör frá hnút } i \text{ yfir í hnút } j \\
      0 &\text{annars}
      \end{array}
      \right.
   
   **Grannafylki** óstefnds nets er samhverft fylki :math:`A` með

   .. math::
      a_{ij} = a_{ji} = \left\{\begin{array}{ll}
      1 &\text{ef leggur tengir hnút } i \text{ og hnút } j \\
      0 &\text{annars}
      \end{array}
      \right.

.. Sýnidæmi
.. important::
   Grannafylki netanna á :numref:`dæmi-um-net` eru

   .. math::
      \begin{pmatrix}
      0 & 1 & 1 \\
      1 & 0 & 1 \\
      1 & 1 & 0
      \end{pmatrix}
      \;\text{ (netið t.v.) og }\;
      \begin{pmatrix}
      0 & 1 & 1 \\
      0 & 0 & 1 \\
      0 & 1 & 0
      \end{pmatrix}
      \;\text{ (hin tvö)}\;

.. rubric:: Vegir í netum

**Vegur** (*path*) með lengd :math:`L` í neti er runa af :math:`L + 1` hnút þannig
að leggur tengi hnút 1 við hnút 2, hnút 2 við hnút 3, o.s.frv. Sagt er að
vegurinn tengi fyrsta hnútinn við þann síðasta. Veg með lengd 3 frá :math:`v_1`
til :math:`v_4` má rita

.. math::
   v_1 \to v_2 \to v_3 \to v_4 \;\text{ eða }\; (v_1, v_2, v_3, v_4).

Skemmtileg regla tengir fjölda vega milli hnúta og veldi grannafylka:

.. admonition:: Regla: Vegafjöldi
   :class: regla

   Grannafylki nets sé :math:`A`. Þá er :math:`(i,j)`-stak
   :math:`A^n` jafnt og fjöldi mismunandi vega með lengd :math:`{} = n` frá
   hnút :math:`i` til hnúts :math:`j` og :math:`(i,j)`-stak fylkisins

    .. math:: B = A + A^2 + A^3 + \ldots + A^n`

    gefur fjölda mismunandi vega með lengd :math:`{} \leq n` (hér
    er :math:`A^n` fylkjaveldi, sbr. kafla :numref:`grunnreikniaðgerðir`).

Þessi skilgreining og reglan sömuleiðis eiga bæði við um stefnd og óstefnd net.

.. Sýnidæmi
.. important::
   Skoðum stefnda netið á eftirfarandi mynd:

   .. figure:: myndir/stefnt-net.png
      :width: 6cm
      :align: center

   Grannafylkið og annað veldi þess eru gefin með

   .. math::
      A =
      \begin{pmatrix}0&1&0&1&0\\1&0&0&0&0\\0&1&1&0&0\\0&0&1&0&1\\1&0&1&0&0\end{pmatrix}
      \;\text{ og }\; A^2 = B =
      \begin{pmatrix}1&0&1&0&1\\0&1&0&1&0\\1&1&1&0&0\\1&1&2&0&0\\0&2&1&1&0\end{pmatrix}

   Við sjáum að :math:`b_{11} = 1` og að það er nákvæmlega einn vegur sem tengir
   hnút 1 við sjálfan sig, nefnilega vegurinn :math:`1 \to 2 \to 1`.  Til að
   taka annað dæmi þá eru tveir vegir frá hnút 4 til hnúts 3, nefnilega
   :math:`4 \to 5 \to 3` og :math:`4 \to 3 \to 3`, enda er :math:`(4,3)`-stak
   :math:`A^2` :math:`{}= b_{43} = 2`.

.. Æfing
.. hint::
   Stefnt net hefur leggi:
   
   .. math::
      \begin{array}{ll}
      1 \to 2 &\qquad 2 \to 3 \\
      1 \to 3 &\qquad 2 \to 4 \\
      1 \to 4 &\qquad 3 \to 4
      \end{array}

   1. Teiknið netið
   2. Finnið grannafylkið :math:`A`
   3. Reiknið :math:`A^2` og :math:`A^3`
   4. Reiknið :math:`B = A + A^2 + A^3`. Þið ættuð að fá út að :math:`b_{14} = 4`.
      Finnið vegina fjóra frá hnút 1 til hnúts 4.

.. admonition:: Skilgreining: Legufylki
   :class: regla

   Ef bæði hnútar og leggir nets eru tölusettir þá er hægt að skilgreina
   **legufylki** (*incidence matrix*) þess. Fyrir **óstefnt** net með :math:`n`
   hnútum og :math:`m` leggum er það :math:`n \times m` fylki :math:`A` með

   .. math::
      a_{ij} = \left\{\begin{array}{ll}
      1 &\text{ef hnútur } i \text{ er endi á legg } j \\
      0 &\text{annars}
      \end{array}
      \right.


   Ef netið er **stefnt** þá er sett formerki á stök legufylkisins til að sýna
   stefnu örvanna:

   .. math::
      a_{ij} = \left\{\begin{array}{ll}
      -1 &\text{ef ör } j \text{ byrjar í hnút } i \\
      1  &\text{ef ör } j \text{ endar í hnút } i \\
      0  &\text{annars}
      \end{array}
      \right.
      
Það eru sem sé tveir ásar (stak sem er :math:`= 1`) í dálki hvers leggs óstefnds nets, nema
hann sé snara, þá er bara einn ás. Ef netið er stefnt og leggurinn ekki snara er :math:`-1` í línu hnútsins þar sem leggurinn byrjar og :math:`1` í línu hnútsins þar sem hann endar Stundum er þetta samt haft öfugt. Fyrir snörur látum við formerkið vera :math:`{}+{}`.

.. Sýnidæmi
.. important::

   .. figure:: myndir/legufylki.png
      :width: 6cm
      :align: center

   Netið á myndinni hefur legufylki:

   .. math::
      \begin{pmatrix}-1&-1&0&1&0\\1&0&-1&0&0\\0&0&1&-1&-1\\0&1&0&0&1\end{pmatrix}

.. Æfing
.. hint::
   Óstefnt net hefur leggi :math:`e_1: v_1`---:math:`v_2`, :math:`e_2:
   v_2`---:math:`v_2` og :math:`e_3: v_2`---:math:`v_3`.
   
   1. Teiknið netið.

   2. Ákvarðið grannafylki þess.
      
   3. Ákvarðið legufylki þess.
      
   4. Ákvarðið legufylkið fyrir tilsvarandi stefnt net með örvar :math:`v_1 \to
      v_2`, :math:`v_2 \to v_2` og :math:`v_2 \to v_3`

Flæðinet
~~~~~~~~

Net sem lýsir kerfi þar sem eitthvað flæðir eftir hverjum legg, rafmagn, vatn,
umferð, vörur o.s.frv. er kallað **flæðinet** (*network*). Hnútpunktarnir eru þá
t.d. tengibox/tengivirki, tengipunktar, gatnamót eða dreifistöðvar. Í
slíkum netum eru tölur tengdar hverjum legg, stundum fleiri en ein. Fyrir legg
:math:`e_j` gæti t.d. gilt:

.. math::
   &\text{flæði } = x_j \\
   &\text{hámarksflæði eða burðargeta } = b_j \\
   &\text{kostnaður á flutta einingu } = c_j

Aðrir möguleikar á upplýsingum um leggi gætu t.d. verið lengdir þeirra eða
viðnám í þeim. Þessar upplýsingar mætti setja fram með fylki sem hefur ekki-núll
í sömu sætum og í grannafylki netsins (því þar er jú ás í sæti
:math:`(i,j)` ef leggur tengir hnúta :math:`i` og :math:`j`). Flæðinet
eru oft stefnd, en þá táknar stefna örvanna/leggjanna ekki stefnu
flæðisins, heldur einungis í hvaða stefnu flæðið telst jákvætt. Ef flæði er á
móti ör verður :math:`x_j < 0`.

Lindir og ósar
~~~~~~~~~~~~~~

Legufylki eru oft gagnleg fyrir verkefni sem tengjast flæðinetum. Það
er ekki erfitt að sjá að ef :math:`x` er flæðivigur með :math:`x_j` =
flæði eftir ör :math:`j` í stefndu neti með legufylki :math:`A` og :math:`y =
Ax` þá gefur :math:`y_i` nettóflæði inn í hnút :math:`i` fyrir öll :math:`i`. 
Ef :math:`y_i > 0` þá er yfirflæði í hnútnum sem við hugsum okkur að renni út
úr netinu, og slíkur hnútur er kallaður **ós** (*sink*). Ef hinsvegar :math:`y_i <
0` þá þarf að bæta í flæðið í hnút :math:`i` til að flæðið í netinu sé
allsstaðar varðveitt; slíkur hnútur kallast **lind** (*source*). Ef
:math:`s` er vigur með

.. math::
   &s_i = \text{ nettóflæði inn í hnút } i \text{, og þar með:} \\
   &s_i \left\{\begin{array}{l}
   {} < 0 \text{ fyrir ósa}\\
   {} > 0 \text{ fyrir lindir}\\
   {} = 0 \text{ fyrir aðra hnúta}
   \end{array}\right.

.. admonition:: Regla: Varðveisla flæðis
   :class: regla

   Ef :math:`A` er legufylki nets með flæðivigur :math:`x` og :math:`s` lýsir
   nettó innflæði þá gildir:

   .. math:: Ax + s = 0
   
Ef netið er tré (hringalaust) þá má leysa þessa jöfnu til að finna flæði í öllum
leggjum, en annars þarf meiri upplýsingar t.d. um viðnám eða þrýsting/spennu.
   
Eftirfarandi mynd sýnir flæðinet. Myndin segir ekkert um formerki flæðigilda svo
það er ekki hægt að sjá hvaða hnútpunktar eru lindir og hverjir eru ósar. Öll
:math:`s_i`-in eru látin stefna inn í netið. Þar sem :math:`s_i` er jákvætt
passar sú stefna, þar eru lindir sem skila flæði inn í netið, en þar sem
:math:`s_i` er neikvætt er raunverulega að flæða út úr netinu.

.. figure:: myndir/flæðinet.png
   :width: 9cm
   :align: center

.. Æfing
.. hint::

   Gerið ráð fyrir að flæðivigur á myndinni hér á undan sé :math:`x = (1, 3, 2, 4, -1)`.
   Ákvarðið legufylkið :math:`A` og í framhaldi nettóinnflæðið :math:`s`.
   Flokkið svo hnútana í lindir, ósa og aðra hnúta.

Línuleg hreyfikerfi
-------------------

Í þessari grein kynnumst við notkun fylkjamargföldunar til að lýsa
kerfum sem breytast með tíma. Tekin verða dæmi um stofnstærð/mannfjölda
þar sem svonefnd Leslie fylki koma við sögu, og um hreyfingu massa
sem kraftar verka á.

Skilgreining línulegra hreyfikerfa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lát :math:`x_t` vera :math:`n`-vigur sem lýsir einhverju **ástandi** (*state*)
kerfis á tíma :math:`t`, :math:`t = 0, 1, 2, \ldots` (stundum er *state* líka
þýtt með **staða**). Við skoðum sem sé kerfið á gefnum tímapunktum: tíminn líður
í strjálum (*discrete*) skrefum sem gætu verið sekúndur eða ár.

.. admonition:: Skilgreining: Línulegt hreyfikerfi
   :class: regla

   **Línulegt hreyfikerfi** (*linear dynamical system*) er líkan af kerfi með
   ástandsvigur :math:`x_t` þar sem :math:`x_{t+1}` er línulegt fall af
   :math:`x_t`:

   .. math::
      x_{t+1} = A_t x_t\quad (t = 0, 1, 2, \ldots)

Fylkin :math:`A_t` (sem eru :math:`n \times n`) eru kölluð **hreyfifylki**
(*dynamics matrices*). Ef þessi fylki og :math:`x_0` eru þekkt þá er hægt
að nota líkanið til að reikna öll framtíðargildi ástandsvigursins :math:`x_t`.
Hér er fylkinu leyft að vera háð :math:`t` en oft er :math:`A`-fylkið fast og
óháð :math:`t`.

Ef ytri aðstæður hafa áhrif á þróun kerfisins er hægt að útvíkka hugtakið: 

.. admonition:: Skilgreining: Hliðrað línulegt hreyfikerfi
   :class: regla

   **Hliðruðu línulegu hreyfikerfi** (*non-homogeneous...*) er lýst með líkani:

   .. math::
      x_{t+1} = A_t x_t + B_t u_t \quad (t = 0, 1, 2, \ldots)

   :math:`B_t` er **inntaksfylki** (*input matrix*) og :math:`u_t` eru **ytri**
   (*exogenous*) breytur (":math:`B` tekur ytri breyturnar **inn** í kerfið").

Eins og að ofan eru fylkin :math:`A_t` og/eða :math:`B_t` oft föst og óháð :math:`t`: :math:`A_t = A` fyrir öll :math:`t`, :math:`B_t = B` fyrir öll :math:`t`.

Þróun mannfjölda eða stofnstærðar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við byrjum á að tala um mannfjölda, en augljóslega má nota sömu stærðfræði til
að lýsa stofnstærð dýrategunda. Gerum ráð fyrir að :math:`x_t` sé
:math:`n`-vigur með :math:`i`-ta stak jafnt og fjöldi fólks í tilteknu landi sem
eru á :math:`i`-ta aldursári (sem sé :math:`i-1` ára gamlir), :math:`t` árum
eftir tiltekinn byrjunartíma. Við gætum látið :math:`n = 120`. Oft er svona
vigur kallaður *aldursdreifing* í landinu og hér er mynd sem sýnir
aldursdreifingu fólks yngra en 100 ára í Bandaríkjunum árið 2010.

.. figure:: myndir/aldursdreifing.png
   :width: 9cm
   :align: center

   Aldursdreifing Bandaríkjamanna árið 2010. |br|
   Milljónir á :math:`y`-ás og aldur á :math:`x`-ás.
      
Látum fæðingartíðni og dánartíðni vera gefna með vigrum :math:`b` og :math:`d`: :math:`b_i` = árlegur meðalfjöldi lifandi fæddra barna foreldra sem eru að meðaltali á :math:`i`-ta aldursári og :math:`d_i` = hlutfall fólks á :math:`i`-ta aldursári sem deyr. Til að vera nákvæmur mætti síðan skoða karla og konur aðskilið. Hér er mynd af :math:`b` og :math:`d` fyrir Bandaríkin í kring um árið 2010. Á þessum myndum er aftur miðað við fólk yngra en 100 ára.

.. figure:: myndir/fæðingarogdánartíðni.png
   :width: 100%
   :align: center

   Fæðingartíðni (t.v.) og dánartíðni (t.h.) í prósentum eftir aldri í
   Bandaríkjunum í lok árs 2010. 

.. rubric:: Leslie-fylki
   
Smá skoðun leiðir nú í ljós að ef horft er framhjá aðfluttum og
brottfluttum má lýsa þróun mannfjöldans með línulega hreyfikerfinu:

.. math::
   x_{t+1} = A x_t =
   \begin{pmatrix}
   b_1 & b_2 & b_3 & \cdots & b_{119} & b_{120} \\
   1-d_1 & 0 & 0   & \cdots & 0 & 0 \\
   0 & 1-d_2 & 0   & \cdots & 0 & 0 \\
   \vdots & \vdots & \vdots && \vdots & \vdots \\
   0 & 0 & 0       & \cdots & 1-d_{119} & 0
   \end{pmatrix}
   x_t

Svona mannfjöldafylki (eða stofnstærðar-) er kallað **Leslie-fylki**. Það er sett
saman úr þremur þáttum:

1. Fæðingartíðni eftir ári í efstu línu
2. Dánartíðni eftir ári á skálínu neðan hornalínu
3. Ásar á sömu skálínu sem færa :math:`i` ára á ári :math:`t` í :math:`i+1`
   ára árið :math:`t+1`.

Ef taka skal tillit til aðfluttra og brottfluttra má nota hliðrað hreyfikerfi:

.. math::
   x_{t+1} = A x_t + B u_t

þar sem :math:`B` er einingafylkið og :math:`(i+1)`-ta stak :math:`u_t` er fjöldi
:math:`i` ára gamalla aðfluttra umfram brottflutta á ári :math:`t`.
   
.. Æfing
.. hint::
   Tegund lifir í hámark 3 ár. Hver 0 ára gefur 0.2 núll-ára afkvæmi árið eftir,
   hver 1 árs 0.6 afkvæmi ári síðar og hver 2 ára 0.8. 20% núll-ára eru dauð ári
   seinna, og dánartíðni eins-árs er 50%.

   Í upphafi er stofnstærðin 3000 einstaklingar, 1200 núll-ára, 1000 eins árs og 800 tveggja ára. 

   1. Ákvarðið Leslie-fylkið
   2. Ákvarðið stofnstærð eftir 1 ár
   3. Ákvarðið stofnstærð eftir 2 ár

Diffurjafna fyrir hreyfingu hlutar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Línuleg hreyfikerfi má nota til að líkja eftir hreyfingu margvíslegra
aflfræðilegra kerfa, t.d. flugféla, skipa, bíla eða bygginga í jarðskjálfta. Hér
lýsum við mjög einföldu kerfi, massa sem færist í beina línu fyrir áhrif
drifkrafts og verður jafnframt fyrir núningsmótstöðu. Við getum hugsað okkur
að um sé að ræða bát með utanborðsmótor.

.. figure:: myndir/hraðbátur.png
   :width: 12cm
   :align: center

   Hraðbátur á Khövsgöl vatni í Mongólíu

Um slíka hreyfingu gildir 2. lögmál Newtons:

.. math::
   \text{kraftur} = \text{massi} \cdot \text{hröðun}

Auk þess gildir að núningsmótstaðan verkar eins og kraftur sem er í
réttu hlutfalli við hraðann, sem sé

.. math::
   \text{núningskraftur} = n \cdot \text{hraði}

þar sem :math:`n` er núningsstuðull. Ef:

.. math::
   &m = \text{massi} \\
   &t = \text{tími} \\
   &f(t) = \text{drifkraftur á tíma } t\\
   &v(t) = \text{hraði á tíma } t \text{ og} \\
   &a(t) = \text{hröðun á tíma } t

og hugað er að formerkjum liða þá fæst:

.. math::
   (*)\qquad\qquad m a(t) = -n v(t) + f(t) \qquad\qquad\quad{}
   
Ef við látum líka :math:`p(t)` vera staðsetningu á tíma :math:`t` þá segir
eðlisfræðin okkur að :math:`v(t) = p'(t)` og :math:`a(t) = p''(t)` og þar með
verður :math:`(*)` að diffurjöfnunni:

.. math::
   m p''(t) = -n p'(t) + f(t)
   
Þessa annarsstigs diffurjöfnu er einfalt að umrita sem fyrsta stigs
diffurjöfnukerfi í tvívíða fallinu :math:`(p(t), v(t))`:

.. math::
   \begin{pmatrix}p'(t)\\mv'(t)\end{pmatrix} =
   \begin{pmatrix}v(t)\\-nv(t) + f(t)\end{pmatrix}

Diffurjöfnu breytt í línulegt hreyfikerfi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
Nálgun við diffurjöfnukerfið að framan fæst með því að umrita staðsetningu og
hraða á tíma :math:`t^+ = t+1` útfrá sömu stærðum á tíma :math:`t` með fyrsta stigs  
Taylor-nálgun, sem fjallað er um í stærðfræðigreiningu. Hún segir að

.. math:: f(x) \approx f(a) + f'(a)(x-a)

Við beitum þessari setningu annarsvegar á :math:`p` og hinsvegar á :math:`v` og það gefur:

.. math::      
   p(t^+) &\approx p(t)+p'(t)(t^+-t) \text{ þ.e. }p'(t) \approx p(t^+)-p(t)\\
   v(t^+) &\approx v(t)+v'(t)(t^+-t) \text{ þ.e. }v'(t) \approx v(t^+)-v(t)

Þessi nálgun verður góð ef við veljum tímaeininguna nógu litla (t.d. 1 sekúndu).
Ef þessari nálgun er stungið inn í diffurjöfnukerfið og við notum ritháttinn
:math:`p_t, v_t` og :math:`f_t` í stað :math:`p(t), v(t)` og :math:`f(t)` fæst:

.. math::
   \begin{pmatrix}p_{t+1}-p_t \\ m(v_{t+1} - v_t)\end{pmatrix} =
   \begin{pmatrix}v_t\\-nv_t + f_t\end{pmatrix}

það er að segja:

.. math::
   \begin{pmatrix}p_{t+1} \\ v_{t+1}\end{pmatrix} &=
   \begin{pmatrix}p_t + v_t\\ (1 - n/m) v_t + (1/m)f_t\end{pmatrix}\\ &=
   \begin{pmatrix}1 & 1\\ 0 & 1-n/m\end{pmatrix}
   \begin{pmatrix}p_t\\ v_t\end{pmatrix} +
   \begin{pmatrix}0\\ 1/m\end{pmatrix} f_t

Þetta kerfi er greinilega hliðrað línulegt hreyfikerfi:

.. math::
   (**)\qquad\qquad x_{t+1} = Ax_t + Bf_t\qquad\qquad\;\;{}
   
með ástandsvigri :math:`x_t = (p_t, v_t)`, ytri breytum
:math:`f_t`, og hreyfifylki og inntaksfylki:

.. math::
   A = \begin{pmatrix}1 & 1\\ 0 & 1-n/m\end{pmatrix}\;\text{ og }\;
   B = \begin{pmatrix}0\\1/m\end{pmatrix}

.. Sýnidæmi
.. important::
   
   Látum hreyfikerfið líkja eftir ferð 500 kg báts með utanborðsmótor í 50
   sekúndur. Mótorinn er settur í gang eftir 5 sekúndur með 3000 newtona krafti
   áfram, 10 sekúndum seinna er skipt í bakkgír, með 2500 newtona krafti í 15
   sekúndur og svo er drepið á mótornum. Núningsstuðull er :math:`n = 100`.

   Byrjað er með :math:`x_0 = (0,0)` og svo er :math:`x_{t+1}` reiknað 50 sinnum
   með :math:`(**)`. Hér eru myndir með niðurstöðum reikninganna (kN eru kílónewton):

   .. figure:: myndir/krafturhraði.png
      :width: 100%
      :align: center

.. Æfing
.. hint::
   1. Notið tölurnar sem gefnar eru í sýnidæminu hér á undan og ákvarðið
      hreyfifylkið :math:`A` og inntaksfylkið :math:`B`.
      
   2. Báturinn er kyrr í 5 sekúndur en þá fer hann af stað.
      Reiknið staðsetningu og hraða hans eftir 6 og 7 sekúndur með blaði og
      blýanti.

   3. Notið nú Python til að líkja eftir hreyfingu bátsins í 50
      sekúndur og endurskapa þannig línuritin í sýnidæminu.

   4. Notið Python til að finna hámarkshraða bátsins.

      
