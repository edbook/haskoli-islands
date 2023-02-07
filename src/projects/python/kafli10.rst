.. include:: rst-include

.. _numpy:
   
=============
NumPy pakkinn
=============

.. _numpy-inngangur:

Inngangur
=========
NumPy pakkinn er ætlaður fyrir vinnu með **vigra** (*vectors*) og **fylki**
(*matrices*) í Python og auk þess ýmsa tölulega reikninga (*numerical
computations*) af einfaldara tagi. Pakkinn **SciPy** er síðan ætlaður fyrir
allskyns sérhæfðari vísindalega reikninga.

Vigrar og fylki í stærðfræði
----------------------------
Nákvæmar skilgreingar á stærðfræðilegum vigrum og fylkjum og skyldum hugtökum
eru umfjöllunarefni í námskeiðum um línuleg algebru. Hér látum við duga styttri útgáfur.

**Vigur** (*vector*) er runa af endanlega mörgum tölum sem gefið er nafn og notuð sem ein heild. Einstakar tölur nefnast **stök** (*elements*), þau eru oftast tölusett 1, 2, 3... en stundum 0, 1, 2..., og i-ta stak vigurs :math:`a` er táknað :math:`a_i`. Vigur :math:`a` með tölunum 1, 2 og 4 má rita

.. math:: a=(1,2,4)\quad\text{eða}\quad a=\begin{pmatrix}1\\2\\4\end{pmatrix}

**Fylki** (*matrix*) er tafla með tölum sem gefið er nafn og notuð sem heild. Tölur í fylki heita líka stök. Stakið í línu :math:`i` og dálki :math:`j` í fylki :math:`A` er táknað :math:`a_{ij}`. Í stærðfræðilegri umfjöllun er oftast byrjað að telja í 1 svo stakið efst til vinstri er :math:`a_{11}`, en þegar verið er reikna í tölvum er oft byrjað að telja í 0. Fylki með :math:`m` línum og :math:`n` dálkum er kallað :math:`m` sinnum :math:`n` fylki, táknað :math:`m \times n`. Hér er dæmi um :math:`2 \times 3` fylki:

.. math::
   A = \begin{pmatrix}1 & 2 & 3\\6 & 7 & 8\end{pmatrix}

.. _um-orðið-fylki:

Um orðið Fylki
--------------
Skv. `Tölvuorðasafninu <https://tos.sky.is>`_ hefur orðið fylki tvær merkingar á
íslensku:

(1) [einkum í stærðfræði] *rétthyrnd tafla af tölum (eða öðrum gildum)* = e.
    *matrix*.

(2) [einkum í tölvufræði] *samsteypa (aggregate) hluta af sama tagi þar sem
    hægt er að vísa í einstök stök með vísi eða vísum (index, indices)* = e.
    *array*.

Í seinni merkingunni er fylki notað sem samheiti yfir vigra, tvívíð fylki, og
margvíð fylki (þar sem vísarnir eru 3 eða fleiri). Stundum er talað um vigra sem
einvíð fylki.

.. danger::
   Þar sem NumPy er beggja megin veggjar, í stærðfræði og í tölvufræði, verður
   orðið fylki notað í báðum merkingunum hér – lesandi þarf stundum af
   ráða af samhenginu við hvað er átt.

.. _fylkjareikn:

Import-skipanir fyrir NumPy
---------------------------
Í NumPy er undirpakki sem heitir ``numpy.linalg`` sem er talsvert notaður. Hann geymir meðal annars föll til að reikna norm vigurs og til að leysa jöfnuhneppi. Alsiða er að skammstafa numpy með np og numpy.linalg með la, sem sé að flytja inn með:

.. code:: python

   import numpy as np
   import numpy.linalg as la

Síðan er sett ``np.`` eða ``la.`` á undan NumPy-skipunum og -föllum sem notuð eru.

Vigrar í NumPy
==============
Vigur í NumPy er að mörgu leyti líkur venjulegum Python lista. Aðalmunurinn er
sá að í vigrum eru öll stök tölur, oftast kommutölur (*float*) en það er líka
hægt að geyma heiltölur eða strengi. En öll stök vigursins verða að vera af sama
gagnatagi, og með því sparast minnispláss og auk þess fæst mun hraðvirkari
vinnsla þegar unnið er með mörg stök.

.. _vigur-gefið-gildi:

Vigur gefið gildi
-----------------
NumPy er viðbót við Python, og öfugt við grunntögin sem öll gefa kost á að búa
til fasta af hverju tagi (sjá kafla :numref:`breytur og tög` og
:numref:`söfn-inngangur`) er ekki boðið upp á vigur-fasta, heldur þarf að nota
NumPy-föll til að búa til vigra.

Eitt þeirra er fallið ``np.array`` sem breytir venjulegum Python-lista af tölum
í vigur. Til að búa til vigurinn :math:`x = (1,2,3,4,6)` má nota skipunina:

   ``x = np.array([1,2,3,4,6])``

Svo eru til skipanir til að búa til ýmsa sérstaka vigra, til dæmis fæst núllvigur með 3 stökum, :math:`z = (0,0,0)`, með:

   ``z = np.zeros(3)``

Loks skal tekið fram að ef vigur er gefið gildi með öðrum vigri (t.d. ``y = x``)
er ekki tekið afrit heldur er búin til ný tilvísun í vigurinn, sbr. kafla
:numref:`gildisgjöf gefur tilvísun` og :numref:`aðgerðir sem duga á öll söfn`.
Til að taka afrit mætti nota:

   ``y = x.copy()``

Einstök stök og hlutvigrar
--------------------------
Vísað í einstök stök í vigrum með hornklofum, alveg eins og í listum, og fyrsta
stakið er líka númer 0. Ef x er :math:`(1,2,3,4,6)` þá væri ``x[2]`` = 3,
``x[2:]`` væri NumPy vigurinn :math:`(3,4,6)` og ``x[::2]`` væri vigurinn
:math:`(1,3,6)`.

.. admonition:: Æfing: Fyrsta NumPy-æfingin
   :class: aefing

   Prófið skipanirnar í næsta kafla á undan (:numref:`vigur-gefið-gildi`) og
   þessum kafla
   
Útprentun vigra
---------------
Til að prenta út vigur x er hægt að skrifa einfaldlega

   ``print(x)`` eða ``print("x =", x)``
   
Það er hægt að stjórna fjölda aukastafa sem ``print`` birtir en við látum það
bíða aðeins (sjá kafla :numref:`innskot`). Svo er hægt að prenta einstök stök í
for-lykkju, og þá er hægt að nota f-strengi, sbr. eftirfarandi dæmi

.. code:: python
          
   a = np.array([5.55,7.77])
   for (i,ai) in enumerate(a):
      print(f"a[{i}] = {a[i]}")

sem mundi prenta

.. code:: text

   a[0] = 5.55
   a[1] = 7.77

Föll af vigrum
--------------
Föllin sem sagt var frá í köflum :numref:`öll-söfn` og :numref:`söfn-af-tölum`
og hægt er að nota á lista af tölum er líka hægt að nota á vigra. Það eru einkum
``len, min, max`` og ``sum`` sem eru nytsamleg. Með NumPy má auk þessara falla
nota ``np.argmin(x)`` og ``np.argmax(x)`` sem skila sætisnúmeri minnsta eða
stærsta staks x, ``np.mean(x)`` sem reiknar meðaltal stakanna og ``la.norm(x)``
sem skilar norminu af x, :math:`\|x\|`, en **norm** af n-staka vigur x er
skilgreint með:

.. math:: \text{norm(x)} = \|x\| = \sqrt{x_0^2 + x_1^2 + \ldots + x_{n-1}^2}

Aðferðir í stað falla
---------------------
Öll föllin sem nefnd eru hér næst á undan nema len og norm eru líka til sem aðferðir.
Ef x er vigur má sem sé skrifa ``x.sum()`` í stað ``np.sum(x)`` (og spara tvo stafi). Þetta er ekki hægt ef x er listi. Hér fylgir tafla yfir öll umrædd föll og aðferðir: 
          
.. csv-table::
   :widths: auto
   :header: fall, aðferð, skilagildi
   :delim: ;

   ``len(x)``      ; –;              fjöldi staka í x
   ``sum(x)``      ; ``x.sum()``;    summa stakanna í x
   ``min(x)``      ; ``x.min()``;    minnsta stak í x
   ``max(x)``      ; ``x.max()``;    stærsta stak í x
   ``np.argmin(x)``; ``x.argmin()``; sæti minnsta staks í x
   ``np.argmax(x)``; ``x.argmax()``; sæti stærsta staks í x 
   ``np.mean(x)``  ; ``x.mean()``;   meðaltal stakanna í x
   ``la.norm(x)``  ; –;              normið af x, :math:`\|x\|`

Takið eftir að ekki þarf að setja ``np.`` fremst í fyrstu fjögur föllin, sem eru
innbyggð í Python-málið.
          
.. admonition:: Æfing: Nokkur NumPy föll
   :class: aefing
         
   Búið til vigur :math:`(2,3,5,7,11)`, prentið hann út, og prófið svo öll
   föllin sem hér voru talin upp
   
Föll til að búa til vigra
-------------------------
Nokkur þægileg og mikilvæg föll má nota til að búa til vigra. Við höfum þegar
séð fallið zeros en auk þess er til ones og tvö föll til að búa til vigra með
hlaupandi stökum:

.. csv-table::
   :widths: auto
   :delim: ;
   :header: kall, skilar

   ``x = np.zeros(n)``       ; vigur með n núllum
   ``x = np.ones(n)``        ; vigur með n ásum, :math:`(1,1,1...)`
   ``x = np.linspace(a,b,n)``; n-staka vigur jafnt dreifður á bilið :math:`[a,b]`
   ``x = np.arange(a,b)``    ; :math:`(a, a+1, a+2,...,b-1)`
   ``x = np.arange(a,b,d)``  ; :math:`(a, a+d, a+2d,...,b-d)`

Við tökum eftir að í arange er b ekki með í x, alveg eins og með innbyggða fallinu ``range``.

.. admonition:: Æfing: Vigratilbúningur
   :class: aefing

   - Búið til vigurinn :math:`(3, 4, 5, 6, 7)` bæði með linspace og arange
   - Búið til :math:`(2.0, 2.1, 2.2,\ldots, 3.9, 4.0)` með linspace og arange

Útreikningur með vigrum
=======================

.. _reiknað-með-vigrum:

Reiknað með vigrum í stærðfræði
-------------------------------
Í stærðfræði, nánar tiltekið undirgrein hennar sem kallast línuleg algebra, er fjallað um ýmsa útreikninga með vigrum. Það er hægt að leggja saman vigra, draga þá hvern frá öðrum og margfalda þá með tölum. Það er líka hægt að reikna **innfeldi** (*scalar product*) tveggja vigra og fá út tölu, og svo má reikna norm vigurs með fyrrnefndu norm-falli

.. admonition:: Sýnidæmi: Vigurreikningar
   :class: synidaemi

   Lát :math:`x = (2,3,6)` og :math:`y = (1,1,2)`. Þá gildir:

   .. math::

      x + y     &= (3,4,8)\\
      x - y     &= (1,2,4)\\
      2x        &= (4,6,12)\\
      \|x\|     &= \sqrt{2^2 + 3^2 + 6^2} = \sqrt{49} = 7\\
      x \cdot y &= 2\cdot 1 + 3\cdot 1 + 6\cdot 2 = 2 + 3 + 12 = 17

Aðgerðin í neðstu línunni nefnist innfeldi, og það er skilgreint með: 

   .. math:: x \cdot y = x_0 y_0 + x_1 y_1 + \ldots + x_{n-1} y_{n-1}

þar sem bæði :math:`x` og :math:`y` eru :math:`n`-staka vigrar.   

.. _plús-mínus-margföldun:

Plús, mínus, margföldun og deiling í NumPy
------------------------------------------
Rifjum upp þegar aðgerðunum plús og sinnum (``+`` og ``*``) er beitt á lista þá
skeyta þær saman listum eða fjölfalda þá. Hér skilur leiðir með listum og
vigrum: Þegar þessar aðgerðir eru notaðar á vigra þá leggjast þeir saman eða
margfaldast eins og í stærðfræði. Hér er tafla yfir helstu NumPy reikniaðgerðir,
þar sem x, y og z eru vigrar en a er tala:

.. csv-table::
   :widths: auto
   :delim: ;
   :header: útreikningur, skilar

   ``y = x*a``    ; margfaldar öll stök í x með tölunni a
   ``y = x/a``    ; deilir með tölu a upp í öll stök x
   ``z = x + a``  ; leggur a við öll stök x
   ``z = x - a``  ; dregur a frá öllum stökum x
   ``z = x + y``  ; leggur saman tilsvarandi stök, ``z[i] = x[i]+y[i]`` fyrir öll ``i``
   ``z = x - y``  ; dregur frá, ``z[i] = x[i]-y[i]``
   ``z = x*y``    ; margfaldar tilsvarandi stök, ``z[i] = x[i]*y[i]``
   ``z = x@y``    ; innfeldi x og y

Takið eftir margföldunarvirkinn ``*`` reiknar ekki innfeldi heldur margfaldast
tilsvarandi stök saman. Slík notkun á margföldunarvirkja er ekki hefðbundin í
stærðfræði. Í Python er notaður sérstakur virki sem reiknar innfeldi, ``@``. Í
stærðfræði er líka óhefðbundið að leggja tölu við vigur eða draga frá.

.. admonition:: Æfing: Vigurreikningar
   :class: aefing

   Búið til vigrana :math:`x = (2,4,6)` og :math:`y = (3,4,5)` og reiknið í
   framhaldi:

   - :math:`x + y`
   - :math:`3x - 2y`
   - innfeldið :math:`x\cdot y`
   - vigurinn :math:`z` sem gefinn er með :math:`z_i = 2x_iy_i + 3x_i`

Venjulegum stærðfræðiföllum beitt á vigra
-----------------------------------------
Í NumPy eru sérstakar útgáfur af venjulegu stærðfræðiföllunum, sqrt, exp, log, sin,
cos o.s.frv. sem reikna fallsgildi í öllum stökum vigurs sem þeim er beitt á.
Þannig gefur ``np.sqrt(np.array([4,9,25]))`` vigurinn :math:`(2, 3, 5)`.

.. admonition:: Æfing: Stærðfræðiföll af vigrum
   :class: aefing

   Búið til vigurinn :math:`(0, \pi/2, \pi, 3\pi/2, 2\pi)` með því að byrja á að
   búa til :math:`(0, 1, 2, 3, 4)` með ``np.arange`` og margfalda hann svo með
   :math:`\pi` og deila með tveimur. Reiknið svo sínus, kósínus og tangens af
   þessum vigri með ``np.``-hornaföllunum.

.. _rökvigrar-og-rökvísun:
         
Rökvigrar og rökvísun
=====================

.. _rökvigrar:

Rökvigrar (*logical vectors*)
-----------------------------
Við höfum aðeins fengið nasasjón af listum með rökgildum í kafla
:numref:`söfn-af-tölum`. Slíkir listar (reyndar vigrar) eru talsvert notaðir
þegar unnið er með NumPy. Það eru nefnilega ekki bara reiknivirkjarnir +, – * og
/ og stærðfræðiföll sem virka stakvís á vigra heldur gildir það líka um
samanburðarvirkjana, < > <= >= == og !=.

Ef x og y eru jafnlangir vigrar þá er ``x < y`` vigur af rökgildum með
:math:`i`-ta sæti satt (``True``) ef :math:`x_i < y_i`. Slíkan vigur má líka
reikna með yfirgripi (*comprehension*) sbr. kafla :numref:`yfirgrip` þannig að:

   ``x < y = np.array([x[i] < y[i] for i in range(len(x))])``

Svo mætti líka nota zip og fá sömu niðurstöðu með ``np.array([xi < yi for
(xi,yi) in zip(x,y)])``. Í framhaldi má svo nota innbyggðu föllin :math:`any` og
:math:`all` til að athuga hvort eitthvert eða öll stök rökvigranna séu sönn.

.. admonition:: Sýnidæmi: Jákvæð stök og samanburður vigra
   :class: synidaemi

   Lát :math:`x = (-1,3,-2,5)` og :math:`y = (-2,2,3,4)`. Þá má gefa x og y
   gildi og finna út hvar stök :math:`x` og :math:`y` eru jákvæð og hvar
   :math:`x < y` með Python forritsbútnum:

   .. code:: python
             
      x = np.array([-1,3,-2,5])
      y = np.array([-2,2,3,4])
      xpos = x > 0
      ypos = y > 0
      xlessy = x < y
      
   og svo má kanna t.d. hvort öll y-in séu jákvæð (sem þau eru ekki) með

   .. code:: python
             
      if all(ypos):...   # eða:
      if all(y > 0):...

Rökvísun (*logical indexing*)
-----------------------------
Hægt er að nota rökvigur sem vísi í vigur. Ef x er einhver vigur af tölum og I
er vigur með rökgildum þá er `x(I)` vigur með stökum í sætum þar sem tilsvarandi
sæti í I er satt. Skoðum þetta betur í næsta sýnidæmi.

.. admonition:: Sýnidæmi: Rökvísun
   :class: synidaemi

   Reiknum í framhaldi af síðasta sýnidæmi:

   .. code:: python

      z = x[x < 0]
      w = y[ypos]

   Þá verður z vigurinn :math:`(-1,-2)` og w verður :math:`(-1,-2)`. Það mætti
   líka nota skilyrt yfirgrip til að búa til z:

      ``z = np.array([xi for xi in x if xi < 0]``

Það er líka hægt að nota svona rökvísun vinstra megin í gildisgjafarsetningu til
að breyta hluta af stökum vigurs eins og gert er í sýnidæminu í næsta kafla.

Stakvísir rökvirkjar
--------------------
Ef beita á rökaðgerðunum og/eða/ekki stakvíst (*element-wise*) á öll stök vigra
er Python með sérstaka rökvirkja, nefnilega ``&``, ``|`` og ``~`` í stað
venjulegu virkjanna and, or og not. Ef x og y eru eins og í sýnidæminu í kafla
:numref:`rökvigrar` þá verður ``xpos & ypos`` rökvigur sem segir okkur hvar bæði
x og y eru jákvæðir (sem sé ``(False, True, False, True)``), ``xpos | ypos``
segir hvar annar hvor er jákvæður (``(False, True, True, True``) og ``~xpos``
segir hvar x er ekki jákvæður (``(True, False, True, False)``).

Ath. ef formúla er með bæði samanburðarvirkja og stakvísan rökvirkja þarf að slá svigum utan um samanburðinn, t.d. ``bothpos = (x > 0) & (y > 0)``.

Hér er sýnidæmi sem sýnir hvernig má nota rökvísun og stakvísan ekki-virkja til
að reikna vigur með gildum falls sem skilgreint er með gaffalformúlu:
      
.. admonition:: Sýnidæmi: 
   :class: synidaemi

   Lát:

   .. math::
      f(x) =
      \begin{cases} x^2 & \text{ef } x < 0 \\ x^3 & \text{ef x >= 0}
      \end{cases}

   og x vera vigur af þétt liggjandi gildum t.d. ``x = np.linspace(-2,2)``. Þá
   er hægt að reikna fallsgildi í öllum x-unum með

   .. figure:: myndir/squarecube.jpg
      :align: right
      :figwidth: 5cm

   .. code:: python

      I = x < 0
      y = np.zeros(len(x))
      y[I] = x[I]**2
      y[~I] = x[~I]**3

   Svo mætti teikna fallið með ``plt.plot(x,y)``, því að Matplotlib getur teiknað
   hvort sem er lista af tölum eða NumPy vigra.

.. admonition:: Æfing: Rökvigrar
   :class: aefing

   Látið :math:`x` og :math:`y` vera vigrana :math:`(0, 14, 15, 16, 15, 13)` og
   :math:`(5,8,7,0,2,4)`. Finnið rökvigra sem svara til :math:`x_i \neq 0`,
   :math:`y_i \neq 0` og í framhaldi vigur með True þar sem bæði :math:`x_i \neq
   0` og :math:`y_i \neq 0`. Búið svo til punktarit (*scatter-plot*) af jákvæðum
   pörum :math:`(x_i,y_i)`.
   
Fylki í NumPy
=============

.. _listi-af-listum:

Fylki er listi af listum
------------------------
Í NumPy er fylki búið til með því að nota ``np.array`` fallið á lista af listum, sem hver um sig gefur eina línu í fylkinu, og NumPy skrifar líka fylki út með svipuðum hætti.

.. admonition:: Sýnidæmi: Fyrsta NumPy fylkið
   :class: synidaemi

   Hér er forrit sem býr til fylkið :math:`A` í kafla :numref:`numpy-inngangur`
   og skrifar það út:

   .. code:: python

      A = np.array([[1,2,3],
                    [6,7,8]])
      print(A)

   Forritið prentar út:

   .. code:: text

      [[1 2 3]
       [6 7 8]]

Það væri líka hægt að búa A til á einni línu með ``A = np.array([[1,2,3],[6,7,8]])``.

Stök fylkis, línur og dálkar
----------------------------
Hægt er að vísa í :math:`a_{ij}` (þ.e.a.s. stakið í línu :math:`i` og dálki
:math:`j`) með ``A[i,j]``. Lína i fæst með ``A[i]`` eða ``A[i,:]`` og dálkur j
fæst með ``A[:,j]``. Eins og fyrir vigra þá byrjar Python að telja í 0 og þessar
vísanir má líka nota vinstra megin í gildisgjöf til að breyta stökum, línum eða
dálkum, t.d. ``A[0,0]=37``, ``A[0,:]=[2,2,2]`` eða ``A[:,0]=0`` (setur öll stök
í fremsta dálki = 0)`.

.. admonition:: Athugasemd: Gildisgjöf gefur tilvísun
   :class: athugid

   Ef gefin er skipunin

       ``a0 = A[0,:]``

   þá er búin til **tilvísun** í fyrstu línuna en ekki ný breyta með gildi hennar
   (sbr. kafla :numref:`gildisgjöf gefur tilvísun`, :numref:`aðgerðir sem duga á
   öll söfn` og :numref:`vigur gefið gildi`). Í raun er verið að gefa línunni
   nafn, þannig að framhaldsskipunin ``a0 = [2,2,2]`` mundi breyta fyrstu
   línunni í A. Á sama hátt mundi skipunin

       ``B = A``

   búa til tilvísun í fylkið. Til að taka afrit á nýjan stað í minni tölvnnar má
   nota aðferðina ``copy``, t.d. ``a0 = A[0,:].copy()`` eða ``B = A.copy()``.

Núllfylki
---------
Til að fá :math:`m \times n` núllfylki má nota ``Z = np.zeros((m,n))`` og ``Z =
np.zeros((m,n),int)`` gefur heiltölu-núllfylki (það má líka skrifa
``np.zeros((m,n),dtype=int)``).

.. admonition:: Æfing: Margföldunartafla
   :class: aefing
           
   1. Búið til :math:`2 \times 2` núllfylki og prentið það út
   2. Búið til fylkin

      .. math::
         C = \begin{pmatrix}1 & 2\\3 & 4\end{pmatrix}\;\text{ og }\;
         D = \begin{pmatrix}5 & 0\\0 & 5\end{pmatrix}

      Leggið svo neðri línu :math:`D` við efri línu :math:`C` og prentið út nýja
      :math:`C`-ið.
   3. Búið til :math:`10 \times 10` fylki :math:`M` með margföldunartöflu með
      því að byrja með heiltölu-núllfylki og reikna svo:

      .. math::
         m_{ij} = (i+1)(j+1)\quad (i=0,\ldots,9, j=0,\ldots, 9)

Bylting
-------
Bylting (*transpose*) fylkis fæst með því að skipta á línum og dálkum.
Stærðfræðilegi rithátturinn fyrir byltingu fylkis :math:`A` er :math:`A^T`,
lesið "A bylt". Í NumPy má rita ``A.T`` til að bylta fylki ``A``, til dæmis:

.. code:: python

   import numpy as np
   A = np.array([
       [3,2,1],
       [0,1,0], 
       [2,2,2]])
   B = A.T
   print(B)

   # Skrifar:
   [[3 0 2]
    [2 1 2]
    [1 0 2]]

.. admonition:: Athugasemd: Bylta fylkið er tilvísun
   :class: athugid

   Fylkið B í dæminu hér að framan verður tilvísun í A bylt, sem uppfærist sjálfkrafa
   ef A breytist. Til að fá nýtt fylki mætti nota ``B = A.copy().T``.

Afpökkun
--------
Í ýmsu samhengi virkar fylki eins og samstæða af línum sínum, bæði þegar því er gefið gildi (eins og við höfum séð) en líka þegar það er notað til að gefa gildi. Ef A er 3 x 3 fylki má þannig skrifa

   ``(u,v,w) = A``

til að setja línur ``A`` inn í ``u``, ``v`` og ``w``. Það má líka sleppa svigunum: ``u,v,w = A``. Hér virkar ``A`` eins og þrennd af línum sínum, og þegar þrennd er gefið gildi með ``A`` fer hver lína inn í sitt stak – eftir ``par = (3,4); (u,v) = par`` verður ``u=3`` og ``v=4``. Þetta er kallað `afpökkun` (*unpacking*).

Slík afpökkun er notuð í næsta kafla þegar lesið er inn í NumPy vigra úr línum eða dálkum í skrá, og byltingin úr síðasta kafla er líka notuð.

.. admonition:: Æfing: Bylting og afpökkun 
   :class: aefing

   Búið til fylkið:

   .. math:: M = \begin{pmatrix}1 & 4\\2 & 5\\3 & 6\end{pmatrix}
   
   Náið svo í dálka þess inn í tvo vigra með því að bylta því fyrst og afpakka svo.

Föll til að búa til fylki
-------------------------
Við höfum þegar séð hvernig hægt er að búa til fylki með því að telja upp stökin
í því og líka hvernig búa má til núllfylki með fallinu ``np.zeros``. Hér er
tafla yfir fleiri föll til að búa til fylki, m.a. nokkur sem verður nánar lýst í
seinni köflum.

.. list-table::
   :widths: auto

   * - ``zeros((n,m))``
     - Skilar :math:`n \times m` núllfylki

   * - ``eye(n)``
     - :math:`n \times n` einingafylki, sjá kafla :numref:`núllfylki og einingafylki`

   * - ``diag(v)``
     - (fyrir :math:`n`-vigur ``v``) skilar :math:`n \times n` hornalínufylki með stökum
       ``v`` á |br| hornalínunni (sjá `Fyrirlestrarnótur um stærðfræði og reiknifræði
       <https://cs.hi.is/strei/kafli02/#ymis-vigur-og-fylkjahugtok>`_) 

   * - ``inv(A)``
     - andhverfa ``A`` (sjá kafla :numref:`andhverfur og ákveður`)

   * - ``rng.random((n,m))``
     - :math:`n \times m` slembifylki (sjá kafla :numref:`slembitölur með numpy`)

   * - ``np.c_[x,y]``
     - (fyrir :math:`n`-vigra ``x`` og ``y``) skilar :math:`n \times 2` fylki með
       dálka ``x`` og ``y``

   * - ``np.vstack((x,y))``
     - (fyrir `n`-vigra ``x`` og ``y``) skilar :math:`2 \times n` fylki með línur
       ``x`` og ``y``

Í kaflanum um slembitölur (:numref:`slembitölur með numpy`) er lýst fleiri
föllum til að búa til slembifylki. Varðandi neðstu tvö föllin þá eru líka til
``np.r_`` og ``np.hstack`` til að skeyta saman lóðrétt og lárétt en notkun
þeirra er óþægilegri en þessara tveggja.
   
.. _inn-og-út:

Innlestur og útskrift
=====================
Talnalestur
-----------
Það er fremur auðvelt að lesa fylki úr textaskrá með fallinu :code:`loadtxt`.
Skráin verður að hafa jafnmörg svið (jafnmargar tölur) í hverri línu og sjálfgefið er að sviðin séu afmörkuð með bilum (sbr. kafla :numref:`csv-lestur-bilafmark`). Fyrir utan
textaskrár sem geymdar eru í núverandi möppu getur ``loadtxt`` lesið skrár sem
eru á netinu án vandkvæða. Hér eru nokkur dæmi sem skýra notkunina::

   skrá = 'datafile.txt'                 #
   A = np.loadtxt(skrá)                  # les alla skrána inn í eitt fylki A
   x,y,z = np.loadtxt(skrá)              # les þriggja línu skrá inn í þrjá vigra
   x,y,z = np.loadtxt(skrá).T            # les þriggja dálka skrá inn í þrjá vigra
   A = np.loadtxt(skrá, skiprows=1)      # sleppir fyrstu línunni
   A = np.loadtxt(skrá, usecols=(0,1))   # les bara fyrstu tvo dálkana
   A = np.loadtxt(skrá, delimiter=',')   # les csv-skrá
   url = 'https://cs.hi.is/python/'      #
   netskrá = url + 'hiti-urkoma.txt'     # skrá á netinu
   (ár,hiti,úrk) = np.loadtxt(netskrá).T # les hana inn í þrjá vigra


Þessi dæmi miðast við að skráin innihaldi bara tölur, en þó mega vera
textastrengir í fyrstu línunni ef henni er sleppt með ``skiprows``, og eins mega
vera dálkar með strengjum ef þeim er sleppt með ``usecols``. Takið sérstaklega
eftir hvernig bylting er notuð í fjórðu línunni, og líka í neðstu línunni, til
að breyta þremur dálkum í þrjár línur, sem svo er afpakkað inn í þrjá vigra. Í
næsta kafla sjáum við hvernig hægt er að lesa inn textadálka.

.. admonition:: Æfing: loadtxt
   :class: aefing

   1. Lesið skrána `https://cs.hi.is/python/hiti-urkoma.txt
      <https://cs.hi.is/python/hiti-urkoma.txt>`_ og plottið svo ártal og úrkomu.
   2. Lesið `https://cs.hi.is/python/malmar.txt <https://cs.hi.is/python/malmar.txt>`_ og
      teiknið punktarit. Það þarf að sleppa bæði fyrstu línunni og fyrsta dálkinum.

Útskrift talna
--------------
Til að skrifa fylki í skrá má nota ``savetxt`` fallið:
   
   ``np.savetxt('skrá.txt', x, fmt='«snið»')`` (t.d. með f.«snið» = ``%5.2f``)

.. _numpy-skrár-með-textadálkum:
   
Innlestur skráa með textadálkum
-------------------------------
Í Numpy er hægt að lesa textafylki með því nota ``loadtxt(..., dtype=str)``.
Síðan er hægt að nota aðferðirnar ``astype`` til að ná í talnadálka og
``tolist`` til að breyta textadálkum í lista af strengjum. Þetta er útskýrt með
eftirfarandi dæmi.

.. admonition:: Sýnidæmi: Lestur textadálka
   :class: synidaemi

   Skráin `https://cs.hi.is/python/malmar.txt
   <https://cs.hi.is/python/malmar.txt>`_ er með streng í fyrsta dálki,
   kommutölu í öðrum dálki og heiltölu í þeim þriðja. Hún er líka með titillínu.
   Hér er forrit sem les skrána

   .. code:: python

      skrá = "https://cs.hi.is/python/malmar.txt"
      (m,e,b) = np.loadtxt(skrá, skiprows=1, dtype=str).T
      málmur = m.tolist()
      eðlisþ = e.astype(float)
      bræðslum = b.astype(int)
      print(málmur)
      print(eðlisþ)
      print(bræðslum)

   Forritið prentar út

   .. code:: text

      ['Ál', 'Járn', 'Kopar', 'Gull']
      [ 2.7   7.87  8.96 19.3 ]
      [ 933 1538 1085 1064]

   Það mætti líka lesa með ``A = np.loadtxt(skrá...).T`` og ná svo t.d. í
   málmanöfnin með ``málmur = A[0].tolist()``.

.. _skrár-úr-excel:   
   
CSV-skár úr Excel
-----------------
Til að lesa Excel-skrár eru tvær leiðir bestar:

1. Að byrja að vista þær sem csv-skrár og lesa inn með NumPy
2. Að nota Pandas

Lítum hér á fyrri möguleikann. Í skránni `https://cs.hi.is/python/allir-malmar.xlsx <https://cs.hi.is/python/allir-malmar.xlsx>`_ eru upplýsingar um alla 70 málmana sem hafa sætistölu minni en 94 (plúton), nánar tiltekið (dæmi í svigum):

- efnatákn (Fe)
- íslenskt nafn (járn)
- sætistala (26)
- eðlisþyngd (7,87)
- bræðslumark (1535)
- enskt nafn (iron)

Í Excel er hægt að vista skrána sem csv-skrá með því að velja *File – Save As...*. Það hefur þegar verið gert og niðurstaðan skrifuð í 

  `https://cs.hi.is/python/allir-malmar.txt <https://cs.hi.is/python/allir-malmar.txt>`_

Þetta var gert með tölvuna stillta á íslensku og þá koma kommur í stað punkta í eðlisþyngdirnar. CSV-skrána má lesa inn með:

   .. code:: python

      skrá = "https://cs.hi.is/python/allir-malmar.txt"
      A = np.loadtxt(skrá, skiprows=1, delimiter=';', dtype='str').T
      efnatákn    = A[0].tolist()
      nafn        = A[1].tolist()
      sætistala   = A[2].astype(int)
      A3          = np.char.replace(A[3], ",", ".")
      eðlisþyngd  = A3.astype(float)
      bræðslumark = A[4].astype(int)
      enskt_nafn  = A[5].tolist()

Hér hefur fallið ``np.char.replace`` verið notað til að breyta kommutölunum í
enska útgáfu, sem er sú eina sem Python skilur.

.. admonition:: Æfing: Allir málmar
   :class: aefing

   1. Smellið bæði á Excel-skrána (ef þið eruð með Excel) og CSV-skrána og
      skoðið innihaldið
   2. Lesið csv-skrána með því að keyra forritsbútinn hér á undan og búið svo
      til punktarit af sætistölu og eðlisþyngd.
   3. Búið til súlurit af bræðslumarki
   4. Opnið Excel-skrána og búið til csv-skrá (ef þið hafið Excel)

Listi yfir skrár á cs.hi.is/python
==================================
Eftirfarandi skrár sem koma við sögu ýmist í sýnidæmum, æfingum eða verkefnum í
þessum fyrirlestrarnótum eru á ``https://cs.hi.is/python``. Þær má nota til að
prófa ýmsar aðferðir til að lesa skrár og vinna með gögn í NumPy (eða Pandas).

- `ord.txt <https://cs.hi.is/python/ord.txt>`_
- `karfa.txt <https://cs.hi.is/python/karfa.txt>`_
- `hiti-urkoma.txt <https://cs.hi.is/python/hiti-urkoma.txt>`_
- `data.txt <https://cs.hi.is/python/data.txt>`_
- `simaskra.txt <https://cs.hi.is/python/simaskra.txt>`_
- `nofn.txt <https://cs.hi.is/python/nofn.txt>`_
- `einkunn.txt <https://cs.hi.is/python/einkunn.txt>`_
- `kennitolur.txt <https://cs.hi.is/python/kennitolur.txt>`_
- `kosningar-2021.txt <https://cs.hi.is/python/kosningar-2021.txt>`_
- `flokksnofn.txt <https://cs.hi.is/python/flokksnofn.txt>`_
- `flokkslitir.txt <https://cs.hi.is/python/flokkslitir.txt>`_
- `malmar.txt <https://cs.hi.is/python/malmar.txt>`_
- `allir-malmar.txt <https://cs.hi.is/python/allir-malmar.txt>`_
- `blom.txt <https://cs.hi.is/python/blom.txt>`_
- `evropulond.txt <https://cs.hi.is/python/evropulond.txt>`_
- `hofudborgir.txt <https://cs.hi.is/python/hofudborgir.txt>`_

Aðferðirnar sem lýst er að framan duga ekki til að lesa skrána **simaskra.txt**,
en hún er með dálka aðskilda með kommu og runu af bilum. Til að lesa hana má
nota:

.. code:: python
          
   (nafn, sími, heimili) = np.genfromtxt(
       'https://cs.hi.is/python/simaskra.txt',
       skip_header = 1,
       delimiter = ',',
       autostrip = True,
       dtype = str).T.tolist()

Fallið *genfromtxt* er systurfall *loadtxt* með aðeins aðra valkosti, m.a.
*autostrip*, auk þess sem *skip_header* kemur í stað *skiprows*. Vegna þess að
það eru engir talnadálkar er hægt er að hengja ``.tolist()`` aftan á
innlestrarskipunina til að breyta öllum dálkunum í venjulega lista af strengjum
í einu lagi.

Önnur skrá sem er sérstök er **flokksnofn.txt** sem er með svið aðskilin með
tab-táknum. Til að lesa hana með ``np.loadtxt`` dugar að setja ``delimiter =
'\t'``. Svo eru heldur engir talnadálkar í þeirri skrá svo það er líka hægt að
hengja ``.T.tolist()`` aftan á ``loadtxt``-kallið (sjá :numref:`verkefni
%sc<kosningaúrslit>`).
