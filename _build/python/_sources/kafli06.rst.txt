.. include:: rst-include

.. _helstu-aðgerðir:         
         
Helstu aðgerðir fyrir söfn
==========================
Töflurnar í þessum kafla eru ekki hugsaðar til að læra utanað, heldur fremur til að fletta
upp í þeim. Aðgerðirnar eru flokkaðar bæði eftir notkunarsviði og tögunum sem þær virka á. Þegar þær eru skoðaðar er gott að muna að **söfn** (*containers*) geta verið strengir, listar, samstæður, mengi og ítrarar, öll söfnin nema mengi teljast vera **runur** (*sequences*), og loks eru listar einu söfnin sem eru **breytanleg** (*mutable*; það er hægt að breyta stökum gildum í þeim). Það er skýringin á því að föll sem breyta stökum gildum eru öll saman í töflunni í kafla :numref:`bara-listar`: "Föll sem duga bara á lista".

Það er líka ágætt að rifja upp það sem stendur í kafla :numref:`aðferðir` um **aðferðir** (*methods*). Þær eru ein tegund af föllum sem kallað er á með ``breyta.aðferð(v1,v2...)``. Breytan á undan punktinum nefnist *hlutur* og aðferðin virkar á hann, og svo eru ``v1``, ``v2``... önnur viðföng sem send eru inn í aðferðina.

Í þessum kafla er orðið **aðgerð** (*operation*) notað sem samheiti yfir virkja,
aðgerðir og venjuleg föll. Töflur yfir sérstakar aðgerðir fyrir strengi og mengi
hafa þegar verið sýndar í :numref:`söfn`. kafla (:numref:`tab:strengjaaðgerðir`
og :numref:`tab:mengjavirkjar`), en hér bætast reyndar við nokkrar
strengjaaðgerðir, auk þess sem föllin í kafla :numref:`öll-söfn` duga sér í lagi
líka bæði á strengi og mengi og þau í kafla :numref:`söfn-af-tölum` má nota á
mengi.

.. _bua-til-sofn:

Föll til að búa til söfn eða breyta tegund safns
------------------------------------------------

   .. csv-table::
      :widths: auto
      :delim: ;

      ``T = tuple(S)``        ; breytir safni S í samstæðu
      ``M = set(S)``          ; breytir safni S í mengi
      ``L = list(S)``         ; breytir safni S í lista
      ``LS = sorted(R)``      ; býr til lista með safninu S röðuðu í vaxandi röð
      ``L = s.split()``       ; býr til lista með "orðum" strengsins s" (aðskilin með bilum)
      ``L = split(s,sep=":")``; býr til lista með hlutstrengjum s, milli tvípunkta
      ``R = range(n)``        ; býr til range-ítrara 0, 1, …, n – 1
      ``R = range(b,e)``      ; býr til range-ítrara b, b + 1, …, e – 1
      ``R = range(b,e,skref)``; býr til range-ítrara b, b + s, … til (en ekki með) e
      ``E = enumerate(r)``    ; býr til enumerate-ítrara, (0, r[0]), (1, r[1]), …
      ``z = zip(R,r)``        ; býr til zip-ítrara (R[0], r[0]), (R[1], r[1]), …

   .. admonition:: Æfing: Ýmis söfn búin til
      :class: aefing

      1. Búið til lista af tölum sem er ekki í röð og inniheldur einhver endurtekin
         stök. Búið til úr honum samstæðu, mengi og raðaðan lista.
      2. Breytið strengnum "abc" í lista með skipuninni :code:`L = list("abc")`.
      3. Notið split til að skipta :code:`"Afi minn og amma mín"` í stök orð.
      4. Búið til enumerate-ítrara E úr L. Prentið bæði E og list(E).
      5. Búið til zip-ítrara Z úr L og listanum ``["Ari", "Bjarni", "Ceres"]``.
         Prentið Z og list(Z).

.. _öll-söfn:

Aðgerðir sem duga á öll söfn
----------------------------

   .. csv-table::
      :widths: auto

      ``S == S1``      , er safnið S eins og safnið S1?
      ``S is S1``      , er S tilvísun í sama safn og S1?
      ``S != S1``      , er S :math:`\neq` S1?
      ``s in S``       , er stakið s í S?
      ``s not in S``   , er s ekki í S?
      ``len(S)``       , fjöldi staka í S
      ``S1 = S``       , býr til tilvísun í S (sjá kafla :numref:`vísað í stök`)
      ``S1 = S.copy()``, býr til afrit af S og setur í S1      

   .. admonition:: Æfing: Mismunandi samanburður
      :class: aefing

      Rifjið upp það sem stendur í kafla :numref:`vísað í stök` um tilvísanir og
      fallið ``copy``. Búið til lista L = [2, 3, 5, 7], afritið hann í L1 og L2
      með venjulegri gildisgjöf (L1 = L) og með copy (``L2 = L.copy()``). Prófið svo
      að bera listana saman bæði með "==" og með "is".
         
.. _söfn-af-tölum:   
   
Föll sem duga á söfn af tölum eða rökgildum
-------------------------------------------
   .. csv-table::
      :widths: auto

      ``min(S)``, minnsta stakið í S
      ``max(S)``, stærsta stakið í S
      ``sum(S)``, summa stakanna í S
      ``any(S)``, er eitthvert stak í S satt eða :math:`\neq 0`?  
      ``all(S)``, eru öll stök í S sönn eða :math:`\neq 0`?

   Það má reyndar líka beita min og max á söfn af strengjum, og þá finnast
   strengir sem eru fremst eða aftast í stafrófsröð.

   .. admonition:: Æfing: min, max og sum
      :class: aefing

      Notið fyrstu þrjú föllin til að finna minnsta og stærsta stak og summu
      staka í listanum ``L=[1,2,3,5]`` og menginu ``{2,8,4}``.

   .. admonition:: Æfing: Rökgildalistar
      :class: aefing
   
      Beitið ``any`` og ``all`` á rökgildalistana ``[True, True, False]``,
      ``[False, False]`` og ``[True, True]``.
      
   .. admonition:: Æfing: Mengjalisti
      :class: aefing

      1. Skrifið fall :code:`meðx(M,x)` þar M er listi af mengjum, :code:`M =
         [M[0], M[1],...]`, og x er eitthvað gildi. Fallið á að skila lista af
         rökgildum, r, þannig að r[i] sé satt ef x :math:`{}\in{}` M[i], annars
         ósatt. Prófið með :code:`M = [{0,1,2}, {1,2,3}, {2,3,4}]` og
         :code:`x=3` sem ætti að skila :code:`[False, True, True]`.

      2. Prófið föllin any og all á niðurstöðu prófunarinnar í lið 1.

.. _allar-runur:
         
Aðgerðir sem duga á allar runur
-------------------------------
       
   .. csv-table:: 
      :widths: auto
      :delim: ;

      ``R1 + R2``;     R1 og R2 er skeytt saman, [1, 2] + [3, 4] → [1, 2, 3, 4]
      ``R*n``;         runan R endurtekin n sinnum, [1,2]*2 → [1, 2, 1, 2]
      ``R.count(s)`` ; hve oft kemur s fyrir í R
      ``R.index(s)`` ; númer fyrstu staðsetningar s í R, villa ef ekkert finnst


   .. admonition:: Athugasemd
      :class: athugid

      Ef runan er strengur er hægt að nota fallið ``find`` í stað ``index``, það
      skilar -1 ef leitarstrengur (eða stafur) í stað þess að valda villu (sjá
      kafla :numref:`strengir`).

   .. admonition:: Æfing: Rómverskur riddari
      :class: aefing
         
      1. Hvað eru mörg r í "Rómverskur riddari réðst inn í Rómarborg, rændi þar
         og ruplaði radísum og rófum" (notið lower og count). Í hvaða sæti er æ-ið?

      2. Ef s kemur alls ekki fyrir í runu R þá skilar **index**-aðferðin villu.
         Ef hætta er á að það gerist þarf að verja sig með því að byrja á að
         spyrja ``if s in R:...``. Framkallið þessi villuskilaboð með því að
         leita að 4 í listanum ``[1,2,3]`` og búið í framhaldi til fall sem
         finnur staðsetninguna, en skilar -1 í staðinn fyrir að gefa villu þegar
         s finnst ekki. Prófið með því að leita að 3 og aftur að 4 í listanum
         ``[1,2,3]``

      3. Búið til samstæðuna (1, 2, 3, 1, 2, 3) bæði með samskeytingu og
         fjölföldun (``+`` og ``*``)

.. _bara-listar:      
      
Föll sem duga bara á lista
--------------------------
   .. csv-table::
      :widths: auto
      :delim: ;

      ``L.append(s)``   ;bætir staki s aftan á lista L
      ``L.extend(L1)``  ;bætir lista  aftan á lista L
      ``L.sort()``      ;raðar L
      ``s = L.pop()``   ;tekur aftasta stakið úr L og setur í s
      ``s = L.pop(i)``  ;tekur i-ta stakið úr L og setur í s
      ``L.remove(g)``   ;fjarlægir fyrsta stakið sem hefur gildið g úr L
      ``L.insert(i,s)`` ;stingur staki s inn í L á stað i

.. admonition:: Sýnidæmi: Listaviðbót og -brottfall
   :class: synidaemi

   .. code:: python3
      
      L = list()
      M = [7,8]
      L.append(1)
      L.append(2)    # Nú er L = [1,2]
      L.extend(M)    # jafngilt og L = L + M eða L += M
      L.remove(2)    # Nú er L = [1,7,8]

.. admonition:: Æfing: Lista breytt
   :class: aefing

   Sláið inn skipanirnar í sýnidæminu og prófið í framhaldi föllin
   ``pop``, ``remove`` og ``insert``.
      
For-lykkjur og söfn
-------------------

Það er ekki bara "range" sem hægt er að nota með for, heldur má rita

    :code:`for i in S`

þar sem S má vera af hvaða safntagi sem er (runa, mengi eða uppflettitafla) t.d.
mætti lykkja yfir tölur sem eru ekki með jöfnu millibili með:

    :code:`for p in [2,3,5,7,11,13]: print('{p} er prímtala)`

og til að gera eitthvað við öll stök í mengi M mætti skrifa:

    :code:`for s in M: ...`

.. admonition:: Æfing: Nemendalisti
   :class: aefing

   Látið :code:`L = ["Ari", "Ása", "Fía", "Jói", "Nói"]` (nemendurnir í mengjaæfingunni).

   1. Notið for-lykkju sem byrjar ``for x in L:`` til að prenta nöfn nemendanna,
      eitt á hverja línu.

   2. Notið nú for-lykkju sem byrjar á ``for (i,x) in enumerate(L,1):`` til að prenta
      nöfnin í töflu með númeri hvers nemanda fremst (byrjið sem sé á ``1. Ari``).

.. _yfirgrip:
      
Yfirgrip (*comprehension*)
--------------------------
- Við höfum séð hvernig hægt að gefa listum gildi með því að telja upp stökin í
  þeim innan hornklofa, með því að byrja með tóman lista og bæta smám saman
  við hann, og með því breyta samstæðu eða "range" í lista með ``list``-fallinu.

- Einn möguleiki enn er að nota svokallað "comprehension" sem mætti
  þýða sem **yfirgrip**.

- Hér eru dæmi:

   .. code:: python

      L1 = [k**2 for k in range(6)]    # L1 verður [0, 1, 4, 9, 16, 25]
      L2 = [L1[j] for j in (1,3,5)]    # L2 verður [1, 9, 25] 
      L3 = [k for k in L1 if k > 5]    # L3 verður [9, 16, 25]
      x = [(i,i) for i in range(1,4)]  # x = [(1,1), (2,2), (3,3)]
      a = [1.4, 999, 2.5, 4.0, 999]    # 999 táknar að gildi vanti 
      b = [x for x in a if x < 999]    # b = [1.4, 2.5, 4.0]

- Það eru sem sé tveir möguleikar:

   .. code:: python

      1) L = [segð for breyta in runa]
      2) L = [segð for breyta in runa if skilyrði] 

- Yfirgrip gefur oft mun styttri kóða en jafngild for-lykkja. Hér er
  dæmi jafngilt skilgreiningu á L3 í dæminu að ofan:

    .. code:: python
       
       L3 = list()
       for k in L1:
           if k > 5: L3.append(k)
           
.. admonition:: Æfing:  Yfirgrip
   :class: aefing

   1. Notið yfirgrip til að búa til lista með veldum af 2 frá 1 til 10, ``[2,4,8,..., 1024]``
      
   2. Látið ``x = [3,4,0,2,0,8,5]`` og notið yfirgrip til að búa til y með
      jákvæðum stökum x

Það er líka hægt að búa til mengi með yfirgripi, t.d. ``S = {k**2 for k in range(6)}``, og uppflettitöflur sbr. kafla :numref:`yfirgrip fyrir uppflettitöflur`, en hinsvegar ekki samstæður.
