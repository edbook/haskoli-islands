.. include:: rst-include

.. _söfn:
   
Söfn: Eitt nafn en mörg gildi
=============================

.. _söfn-inngangur:

Inngangur
---------
Fyrir utan grunngagnatögin sem fjallað hefur verið um að framan er Python með ýmis innbyggð tög fyrir **söfn** (*containers*), en breytur af slíku tagi geta geymt mörg stök eða gildi. Reyndar hefur þegar verið talað svolítið um eitt slíkt tag, nefnilega strengi sem geta geymt marga stafi. Mörg safntögin í Python teljast **runur** (*sequences*), nánar tiltekið eru það **strengir**, **listar** (*lists*), **samstæður** (*tuples*) og **ítrarar** (*iterators*; t.d. útkoma úr range), en önnur teljast ekki runur, m.a. **mengi** (*sets*) og **uppflettitöflur** (*dictionaries*). Uppflettitöflurnar eru svolítið sér á parti og umfjöllun um þær kemur seinna, en í þessum kafla og þeim næsta verða hin safntögin á dagskrá. Eftirfarandi tafla sýnir hvernig hægt er að safna tölunum 1, 2, 3 og 4 í streng, lista, samstæðu, mengi og ítrara:

   .. list-table::
      :widths: auto
         
      * - strengur
        - :code:`st = "1234"`

      * - listi
        - :code:`L = [1, 2, 3, 4]`

      * - samstæða
        - :code:`S = (1, 2, 3, 4)`

      * - mengi
        - :code:`M = {1, 2, 3, 4}`

      * - ítrari
        - :code:`Í = range(1,5)`

Strengurinn er reyndar sér á parti því hann geymir ekki heiltölurnar 1–4 heldur tölustafina 1–4, sem eru geymdir öðruvísi í minni tölvunnar.        
          
Það sem er sameiginlegt öllum runum er að hægt er að vísa í tiltekin stök eða gildi í rununni með hornklofum: ef R er runa og k er heiltala þá er

    ``R[k]``

stakið í sæti k í rununni, og fremsta stakið telst vera númer 0. Fyrir runur og mengi er hægt er að nota:

    ``if g in R:...``  til að kanna hvort gildi ``g`` sé í ``R``, og |br|
    ``for g in R:...`` til að láta ``g`` hlaupa í gegn um öll stökin í ``R``

Svo má telja stökin með :code:`len(R)` og ennfremur er hægt að nota samskeytingar- og fjölföldunarvirkjana (``+`` og ``*``) á allar runur. Öll þessi atriði verða útlistuð nánar að neðan, m.a. í kafla :numref:`helstu-aðgerðir`.

Strengir
--------
Strengjatagið heitir :code:`str` og í strengjum má geyma runur af hvaða *Unicode* stöfum sem vera skal (Unicode er alþjóðlegur staðall til að skrá í tölvu bókstafi allra heimsins tungumála auk fjölmargra annarra rittákna: tölur, greinarmerki, stærðfræðitákn, broskallar, o.s.frv.). Strengir eru búnir til með því að setja texta innan einfaldra eða tvöfaldra gæsalappa:

    :code:`s1 = "Ísland"`, :code:`s2 = 'Ísland'`, :code:`s3 =` :math:`\textrm{"}\mathrm{\beta\in A \cap B}\textrm{"}`

Ef s er strengur þá er hægt að ná í einstaka stafi með :code:`s[i]` þar sem i er númer sætis (fremst er sæti 0), og svo er hægt að ná í **hlutstrengi** (*slices*) með :code:`s[i:j]` (stök ``i``,..., ``j-1``), :code:`s[:j]` (frá byrjun til ``j-1``) og :code:`s[i:]` (frá ``i`` og út í enda). Ef i er mínustala er talið aftanfrá. Ef s er :code:`"abcdef"` og gefin er skipun :code:`print(a[0], a[1:3], a[-3:-1], a[-1]` þá prentast út:

   :code:`a bc de f`

Í grein :numref:`gildisgjöf` var sýnt hvernig hægt er að skeyta saman og fjölfalda strengi, og ýmsar strengjaaðgerðir eru sýndar í kynningarvinnubókinni í æfingunni aftan við kafla :numref:`jupyter-leiðbein-á-netinu`. 

    .. table:: Nokkrar strengjaaðgerðir
        :widths: 1 2
        :name: tab:strengjaaðgerðir
                 
        +------------------+------------------------------------------+
        |``s = s1 + s2``   |samskeyting strengja                      |
        +------------------+------------------------------------------+
        |``s = s1*3``      |sama og s1 + s1 + s1                      |
        +------------------+------------------------------------------+
        |``s[3]``          |stafur í sæti 3                           |
        +------------------+------------------------------------------+
        |``s[2:5]``        |hlutstrengur í sætum 2,3,4                |
        +------------------+------------------------------------------+
        |``s.lower()``     |breyta í lágstafi                         |
        +------------------+------------------------------------------+
        |``s.upper()``     |breyta í hástafi                          |
        +------------------+------------------------------------------+
        |``s.capitalize()``|breyta fremsta staf í hástaf              |
        +------------------+------------------------------------------+
        |``s.find(s1)``    |staðsetning s1 í s, -1 ef ekkert s1 finnst|
        +------------------+------------------------------------------+
        |``len(s)``        |lengd strengsins                          |
        +------------------+------------------------------------------+
        |``c in s``        |er stafurinn c í strengnum s?             |
        +------------------+------------------------------------------+
        |``s.isupper()``   |eru allir stafir í s hástafir?            |
        +------------------+------------------------------------------+

.. admonition:: Æfing: Strengjablús
   :class: Æfing

   Búið til streng með nafninu ykkar (t.d. ``s = "Kristján Jónasson"``). Notið aðgerðir úr töflunnin að ofan til að:
   
   1. finna hvar fyrsta bilið er (á eftir fornafni/fyrsta nafni) með ``find``,
   2. ná í fornafnið,
   3. finna lengd þess,
   4. athuga hvort það sé r í nafninu (hér ætti að nota ``lower`` ef nafnið skyldi byrja á R.
   5. prófið líka ``upper`` og ``capitalize``
        
Listar
------
**Listi** (`list <https://en.wikipedia.org/wiki/List_(abstract_data_type)>`_) er grunnhugtak í tölvufræði. Listi geymir endanlegan fjölda staka í röð og hvert stak getur komið fyrir oftar en einu sinni. Python hefur safntag *list* sem útfærir lista. Það eru engin takmörk á því hvernig stök má geyma, þau mega sjálf vera söfn og þurfa ekki öll að vera af sama tagi. **Tómur listi** fæst með :code:`L = []` og almennan lista má búa til með því að skrifa:

    :code:`L = [gildi, gildi...]`

Listaaðgerðir
~~~~~~~~~~~~~
          
**Aðgerðir fyrir tölvufræðilega lista** eru m.a. að ná í fremsta stakið (**haus**, *head*), að ná í öll hin stökin (**hali**, *tail*) að bæta staki framan á eða aftan á lista, og að ná í stak í tilteknu sæti. Python listar bjóða upp á þessar aðgerðir og ýmsar fleiri (sjá æfinguna í kafla :numref:`fleiri listaföll`).

.. figure:: myndir/head-tail.png
   :align: center
   :figwidth: 7cm

   Haus og hali

Vísað í stök
~~~~~~~~~~~~
Eins og fyrr segir má vísa í einstök stök í lista með :code:`L[i]` þar sem i er heiltala með númeri staks, og **hlutlistar** (*slices*) fást eins og fyrir strengi, sbr. eftirfarandi dæmi:

   .. code:: python3

      L = [2, 'abc', 4.33, [1,2]]  
      print(L[1], L[2], L[-1])
      print(L[1:3])
      print(L[2:])

      # Forritið að ofan prentar út:
      abc 4.33 [1, 2]
      ['abc', 4.33]
      [4.33, [1, 2]]

Samskeyting og margföldun
~~~~~~~~~~~~~~~~~~~~~~~~~
Aðgerðunum ``+`` og ``*`` sem við höfum séð að duga til að skeyta saman og fjölfalda strengi má líka beita á lista. Þannig gefur :code:`[2,3,5] + [7,11]` listann :code:`[2,3,5,7,11]` og :code:`[2,3,5]*2` er :code:`[2,3,5,2,3,5]`.
 
Gildisgjöf gefur tilvísun
~~~~~~~~~~~~~~~~~~~~~~~~~
Ef lista er gefið gildi með venjulegri gildisgjöf :code:`M = L` þá verður ekki til nýr listi heldur bara ný **tilvísun** (*reference*) eða nýtt nafn á listann :code:`L`. Til að afrita listann mætti rita :code:`N = L.copy()`. Hér er dæmi:

.. admonition:: Sýnidæmi: Afrit og tilvísun
   :class: synidaemi
           
   .. code:: python3

      L = [2, 3, 5, 7, 9]
      M = L
      N = L.copy()
      L[4] = 11
      print(M)   # prentar [2, 3, 5, 7, 11]
      print(N)   # prentar [2, 3, 5, 7, 9]

   Takið eftir að ``L`` og ``M`` verða tvö nöfn á sama listanum, en ``N`` er nýr listi sem geymdur
   er á öðrum stað í minni tölvunnar.

Þegar kallað er á fall með lista sem viðfang þá fær fallið tilvísun í listann.
Það þýðir að fallið getur breytt listanum sem það hefur sem stika og við
það breytist tilsvarandi viðfang þar sem kallið er. Þetta gerist ekki ef kallað er
á föll með stök gildi sem viðfang. Hér er dæmi sem sýnir þetta:

.. admonition:: Sýnidæmi: Listaviðfang og töluviðfang
   :class: synidaemi
           
   .. code:: python3

      def listafall(A): A[0] = 3
      def tölufall(a):  a = 3

      tala = 5
      listi = [5,6]
      tölufall(tala)
      listafall(listi)
      print(tala,listi)  # prentar 5 [3, 6] 

Bætt við lista
~~~~~~~~~~~~~~
Í dæmunum hér á undan sést hvernig hægt er að breyta einu staki í lista, en sú aðferð dugar ekki til að lengja listann: :code:`L[5] = 13` mundi gefa villu. Til að bæta 13 aftan á listann mætti nota aðra hvora af eftirfarandi skipunum

   .. code:: python3

      L.append(13)
      L = L + [13]

Aðferðir
~~~~~~~~
Köllin á :code:`copy` og :code:`append` eru óvenjuleg. Fall sem kallað er á svona, með :code:`breyta.fall(...)`, er kallað **aðferð** (*method*), en aðferðir eru eitt af grundvallarhugtökum í hlutbundinni forritun (*object oriented programming*). Breytan á undan punktinum er þá kölluð **hlutur** (*object*), og aðferðin virkar sem sé á hann. Fallið :code:`find` í töflunni yfir strengjaðgerðir hér framar er annað dæmi um aðferð.

Fleiri listaföll
~~~~~~~~~~~~~~~~

Til eru fjölmörg fleiri föll fyrir lista til viðbótar við :code:`copy` og :code:`append`. Mörg þessara falla duga líka á önnur safntög, sér í lagi samstæður og mengi, og í þessum fyrirlestrarnótum hafa töflur með mikilvægustu safnaföllum verið settar á einn stað, í :numref:`%s. kafla <helstu-aðgerðir>`. Þar á meðal eru ýmis fleiri dæmi um hlutbundnar aðferðir

.. admonition:: Æfing: Listablús
   :class: aefing
          
   1. Skrifið föll :code:`haus(L)` og :code:`hali(L)` sem skila haus og hala
      lista L. Prófið.

   2. Flettið upp á *insert*-fallinu í grein :numref:`bara-listar` og notið
      það til að búa til fall :code:`setjafremst(L,g)` sem bætir ``g`` við sem
      nýjum haus fremst í listann. Ath. að fallið á ekki að hafa neina return
      skipun, heldur notfærir það sér að listaviðföng eru tilvísanir. Prófið.

   3. Búið til fall :code:`oddalisti(n)` sem skilar lista með n fyrstu
      oddatölunum. Byrjið með tóman lista, :code:`[]`, og notið svo for-lykkju
      sem hleypur í gegn um tölurnar :math:`1, 3,\ldots, 2n-1` og bætir hverri
      þeirra aftan á listann. Prófið.

Samstæður
---------
Annað safntag í Python sem líka útfærir tölvunarfræðilega lista er **samstæða** (*tuple*). Enska orðið *tuple* er fengið að láni úr stærðfræði, en stærðfræðilegt `tuple <https://en.wikipedia.org/wiki/Tuple>`_ (þýtt í `stærðfræðiorðasafninu <https://stæ.is/os>`_ með n-und) er skilgreint sem "endanleg röðuð runa af stökum", venjulega táknuð með því að telja stökin upp innan sviga t.d. :math:`(2, 3, 4)`. N-undir eiga margt skylt með punktum í plani eða rúmi, enda rithátturinn sá sami. Hér er hugtakið þýtt með samstæða, en undirrituðum finnst n-und stirt og hálfljótt. Svigarithátturinn er einmitt notaður til að búa til samstæður í Python:

    :code:`S = (gildi, gildi...)`.

Reyndar má sleppa svigunum: :code:`S = gildi, gildi...` er jafngilt. Til að búa til **tóma samstæðu** má rita ``S = ()`` og til að búa til **samstæðu með einu staki** þarf að enda á kommu, t.d. ``S = (4,)``. Samstæða tveggja staka nefnist **par** eða **tvennd** (*pair*, *couple*), og þriggja staka samstæða er **þrennd** (*triple*).

Hornklofa má áfram nota til að vísa í einstök stök og hlutsamstæður: :code:`print(S[0])` prentar fyrsta gildið í :code:`S` og :code:`print(S[0:2])` prentar fyrstu tvö. Einn helsti munurinn á listum og samstæðum er sá að það er ekki hægt að breyta stökum gildum í samstæðum, stækka þær eða minnka eftir að þær hafa verið búnar til:

   .. code:: python
      
      L = [1,2,3]  # þriggja staka listi
      L[1] = 4     # þetta má
      S = (1,2,3)  # þrennd
      S[1] = 4     # þetta gefur villu

Sagt er að samstæður séu **óbreytanlegar** (*immutable*) en listar séu
**breytanlegir** (*mutable*). Stundum er gott að geta treyst því að einstök
gildi breytist ekki, og auk þess notar Python málið samstæður í ýmsum skipunum,
t.d. þegar kallað er á föll sem skila fleiru en einu gildi, sbr. :numref:`kafla
%s<virka>`, og til að búa til föll með breytilegum stikafjölda (sjá kafla 12.4 í
`Think Python <https://greenteapress.com/thinkpython2/thinkpython2.pdf>`_
kennslubók). Eitt í viðbót sem er frábrugðið: Hægt er að búa til mengi af
samstæðum, og þær geta verið lyklar í uppflettitöflum, en hvorugt má með listum.



Flest föllin sem talin eru upp í :numref:`%s. kafla <helstu-aðgerðir>` duga á samstæður, nema föllin í grein :numref:`bara-listar`. Eins og fyrr segir má líka nota samskeytingarvirkjana + og * á þær.

Mengi
-----
Stærðfræðihugtakið **mengi** (`set <https://en.wikipedia.org/wiki/Set_(mathematics)>`_) er skilgreint sem "safn ólíkra staka" og endanleg mengi má tákna með því að telja stökin upp innan slaufusviga: :math:`\{2, 3, 4\}`. Mengi eru óröðuð og þótt stök séu talin tvisvar breytir það ekki menginu. Þannig gildir:

.. math::
   \{4, 3, 2\} = \{2, 3, 4\} = \{2, 3, 3, 4\}

Mengi í Python eru táknuð með sama hætti:

   .. code:: python3
      
      M = {gildi, gildi, ...}

Tómamengið er búið til með :code:`tómt = set()` (rithátturinn ``{}`` er frátekinn til að búa til tóma uppflettitöflu). Mengi eru óbreytileg eins og samstæður þannig að eftir að þau hafa verið búin til er ekki hægt að breyta þeim. Það er heldur ekki hægt að vísa í stök með hornklofum, en hinsvegar eru til Python-virkjar fyrir helstu mengjaaðgerðir, eins og sýnt er í töflunni hér að neðan, og auk þess er hægt að nota föllin í töflunum í greinum :numref:`öll-söfn` og :numref:`söfn-af-tölum`.

Af því mengin eru ekki röðuð er alls ekki tryggt print skipun prenti þau í röð. Ef við viljum prenta mengi í röð er hægt að breyta þeim í raðaðan lista með fallinu ``sorted`` og prenta hann svo, sem sé ``print(sorted(M))``.

.. list-table:: Mengjavirkjar
   :widths: auto
   :align: center
   :header-rows: 1
   :name: tab:mengjavirkjar

   * - Python-virki
     - stærðfræði-virki
     - aðgerð

   * - :code:`in`
     - :math:`\in`
     - er stak í

   * - :code:`not in`
     - :math:`\notin`
     - er ekki stak í

   * - :code:`<=`
     - :math:`\subseteq`
     - er hlutmengi í

   * - :code:`&`
     - :math:`\cap`
     - sniðmengi

   * - :code:`|`
     - :math:`\cup`
     - sammengi

   * - :code:`–` 
     - :math:`-\textrm{ eða }\smallsetminus`
     - mengjamismunur

   * - :code:`^`
     - :math:`\Delta`
     - samhverfur mismunur

.. figure:: myndir/mengjamunur.png
   :align: center
   :figwidth: 8cm

   Mengjamismunurinn *A* – *B*
       
.. figure:: myndir/samhverfur-munur.png
   :align: center
   :figwidth: 9cm

   Samhverfi mismunurinn *A* ∆ *B*

.. admonition:: Æfing: Prímtölur < 20
   :class: aefing

   1. Búið til mengi S með sléttum tölum 2–20 og M3 með tölunum 3, 6,..., 18
      og M5 með 5, 10, 15, 20 (með því að nota :code:`set(range(...))`).
      Prentið svo M6 = S :math:`\cap` M3 (margfeldi af 6 sem eru < 20).

   2. Látið X vera mengi talnanna 2–20 og finnið P = mengi prímtalna < 20 sem
      (X – (S :math:`\cup` M3 :math:`\cup` M5)) :math:`\cup` {2,3,5}

.. admonition:: Æfing: Enska og saga
   :class: aefing
         
   Ef E er mengi nemenda í Ensku og S er mengi nemenda í Sögu þá er E
   :math:`\cap` S mengi þeirra sem eru í báðum fögum, E :math:`\cup` S er mengi
   þeirra sem eru í einhverju fagi og E :math:`\Delta` S eru þeir sem eru í
   nákvæmlega einu fagi. Látið :code:`E = {"Ari", "Ása", "Fía", "Jói"}`,
   :code:`S = {"Fía", "Jói", "Nói"}` og ákvarðið samsettu mengin þrjú með
   Python-mengjaaðgerðum. Teiknið gjarna mynd á blað.
        
Ítrarar
-------
Um fallið **range** sem notað er í for-lykkjum var fjallað í greinum
:numref:`icollatz` og :numref:`for-lykkjur`. Það skilar gildi af taginu
**ítrari** (*iterator*). Í for-lykkjum má líka nota nota aðrar gerðir af runum
en ítararnir hafa þann kost að spara minnispláss, því aðeins byrjunargildið,
lokagildið og skrefið eru geymd. Hér eru nokkur dæmi:

   .. code:: python

      for i in range(1000): ... # þ.e. fyrir i = 0,1,2...999
      r = range(2,8)            # r geymir bara 2, 8 og skrefið 1
      r1 = range(2,11,3)        # r1 geymir 2, 11 og skrefið 3
      L1 = list(r1)             # gefur L1 = [2, 5, 8]
      for i in r1: ...          # fyrir i = 2, 5, 8
      L = list(range(1000))     # gefur L = [0,1,...,999]
      for k in L: ...           # jafngilt fyrsta dæminu en þarf meira minni

.. admonition:: Æfing: 
   :class: aefing
           
   Fallið :code:`sys.getsizeof(x)` skilar fjölda bæta sem breytan :code:`x`
   tekur í minni. Finnið út hve mikið minni :code:`range(1000)` og
   :code:`list(range(1000))` taka (byrjið með :code:`import sys`).

Annað þægilegt fall sem skilar ítrara er fallið **enumerate**, en ``enumerate(L)`` skilar ítrara sem rennir sér í gegn um öll stök í ``L`` og býr til pör (0, L[0]), (1, L[1]) o.s.frv. Hugsum okkur að við höfum lista af nöfnum og viljum skrifa þau út ásamt númerum þeirra í listanum. Eftirfarandi dæmi sýnir tvær jafngildar leiðir til þess.

.. admonition:: Sýnidæmi: Nöfn og númer
   :class: synidaemi
         
   Báðar lykkjurnar í eftirfarandi forriti skrifa út:

   .. code:: text

      1 Ása
      2 Bjarni
      3 Dóra
      4 Einar
      
   .. code:: python

      nöfn = ["Ása", "Bjarni", "Dóra", "Einar"]
      for (nr,nafn) in enumerate(nöfn):
          print(nr,nafn)

      for nr in range(len(nöfn)): # Þessi lykkja er jafngild þeirri að ofan
          nafn = nöfn[nr]
          print(nr,nafn)

      Við sjáum að forritið er aðeins einfaldara þegar enumerate er notað.

Það er líka hægt að byrja að telja í 1 með ``enumerate(L,1)`` og svo má líka
setja pörin sem verða til inn í sérstaka breytu:

.. admonition:: Sýnidæmi: Byrjað með númer 1
   :class: synidaemi

   .. code:: python

      for p in enumerate([5,25,125], 1):  # veldi af 5
          print(p)                        # prentar (1, 5), (2, 25) og (3, 125) 
   
   Þetta jafngildir:
  
   .. code:: python

      L = [5, 25, 125]
      for i in range(len(L)):
          p = (i+1, L[i])
          print(p)

**zip** er annað fall sem smíðar pör; það tekur inn tvo (eða fleiri) jafnlanga lista og
parar þá saman: :code:`zip([0,1,2], [5,6,7])` skilar pörunum :code:`(0,5)`,
:code:`(1,6)` og :code:`(2,7)`.

.. admonition:: Æfing: enumerate og zip 
   :class: aefing
               
   1. Smíðið pörin (0,2), (1,4), (2,6), (3,8), (4,10) með *enumerate* og prentið
      út (til dæmis dugar :code:`E = enumerate(...)` og :code:`print(list(E))`).
      
   2. Smíðið sömu pör með *zip*.

   3. Látið ``nöfn`` vera nafnalistann í sýnidæminu "Nöfn og númer" og ``eink`` vera
      ``[8, 7, 10, 9]`` (einkunnir í landafræði). Skrifið forrit sem notar enumerate
      til að búa til töfluna:

      .. code:: text

         Nr  Nafn  Einkunn
         –––––––––––––––––
         1   Ása      8
         2   Bjarni   7
         3   Dóra    10
         4   Einar    9

      **Leiðbeining:** Hægt er að nota *enumerate* og *zip* saman svona:
      
          :code:`for nr,(s1,s2) in enumerate(zip(L1,L2),1)`

      Þá hleypur nr í gegn um 1,2,3... og samtímis hlaupa s1 og s2 í gegn um
      stökin í L1 og L2.
