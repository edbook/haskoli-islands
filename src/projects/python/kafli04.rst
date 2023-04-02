.. include:: rst-include

.. _grunn-python:
   
====================
 Grunnatriði Python
====================

Breytur og tög
==============

.. rubric:: Breytur

**Breyta** (*variable*) er nafn á minnishólfi í tölvu, þar sem geyma má **gildi** (*value*). Gildin geta svo verið af ýmsu tagi, eða haft ýmis **tög** (*types*), og eins og fyrr segir eru þessi tög tengd gildunum en ekki breytunum sjálfum. Fyrir utan gildi sem geymd eru í breytum er líka talað um gildi sem útkomu úr **útreikningi** (*computation*) eða **segð** (*expression*), t.d. hefur segðin :math:`2 + 2` gildið :math:`4`. Ósamsett gildi, t.d. 2, heitir **fasti** (*constant*).

.. rubric:: Grunntög

Hér er listi yfir grunntögin í Python og dæmi um fasta af hverju tagi:

    - *kommutala (float)* t.d. :code:`2.0`, :code:`-543.62`, :code:`16e-22`
    - *heiltala (int)*	 t.d. :code:`2`, :code:`123456789012345678901234567890`,
      :code:`round(1e100)`; engin takmörk á stærð
    - *strengur (str)*	 t.d. :code:`'abc'`, :code:`"strengur með bili"`;
      nota má hvort sem maður vill :code:`"` eða :code:`'`
    - *rökgildi (bool)* , :code:`True` og :code:`False`
    - *"EkkertTag" (NoneType)*, :code:`None` sérstakt tag sem fæst m.a. úr
      föllum sem engu skila.

.. rubric:: Önnur tög

Önnur algengustu innbyggð tög eru:

    - *Listar (list)*
    - *Samantektir (tuple)*
    - *Mengi (set)*
    - *Ítrarar (iterator)*
    - *Uppflettitöflur (dictionary)*

Um öll þessi tög ef fjallað síðar í þessum fyrirlestrarnótum.

.. rubric:: Nöfn breyta
      
Sú regla gildir að nafn breytu skal vera runa af bókstöfum, tölustöfum, og _, það má ekki byrja á tölu og það má ekki vera lykilorð í málinu eins og "for" eða "return". Í sumum forritunarmálum verða bókstafirnir að vera enskir, en sú takmörkun á ekki við um Python, Dæmi um lögleg breytunöfn eru: x_1, hæð, ∆.

Í nútímaforritum er algengt að nota fremur löng og lýsandi breytunöfn, t.d. :code:`radíus_hrings`. Sú regla er oft brotin í inngangsnámskeiðum í forritun, því þar þvælast löng nöfn frekar fyrir en að hjálpa til, og dæmigert væri að nota :code:`r` fyrir geisla hrings.

.. admonition:: Æfing: Ólögleg breytunöfn
   :class: aefing
      
   1. Hverjir eftirfarandi strengja eru ekki lögleg breytunöfn?

      a. 01rst

      b. rst01
      
      c. rst-01
      
      e. ρστ01 
      
      d. Sérdeilis_afskaplega_langt_breytunafn_sem_ætti_að_reyna_að_stytta
      
      f. abc
      
      g. def
         
   2. Googlið "python reserved words". Hvaða lykilorð í málinu byrja á a eða b (og eru þar
      með dæmi um ólögleg breytunöfn)?

.. _adgerdir-og-virkjar:   

Aðgerðir og virkjar
===================
Í stærðfræði er það að ákvarða útkomu segðar oft kallað **aðgerð** (*operation*). Grunnbyggingareiningar segða eru oftast **einstæðar** (*unary*) eða **tvístæðar** (*binary*) aðgerðir. Einstæð aðgerð er ýmist af taginu :math:`\circ x` eða :math:`f(x)` þar sem :math:`\circ` er einstæður **virki** (*operator*), :math:`f` er **fall** (*function*) og :math:`x` er gildi. Tvístæð aðgerð er oft af taginu :math:`x \circ y` þar sem :math:`x` og :math:`y` eru gildi og :math:`\circ` er tvístæður virki. Gildin sem virkjar verka á eru stundum kallaðir **þolendur** (*operands*). Hér eru nokkur dæmi:

    .. math::
       \begin{align}
       \textrm{einstæðar aðgerðir }&
       \begin{cases}
       \texttt{not p}\\
       \texttt{–segð}\\
       \texttt{fall(13)}
       \end{cases}\\
       \textrm{tvístæð aðgerð: }&\text{a + 2}
       \end{align}

Virkjar í Python eru flestir eins og algengast er í forritunarmálum, sér í lagi gildir það um venjulegu reikningsaðgerðirnar fjórar og **samanburðarvirkja** (*relational operators*) til að bera saman stærð. Forritunarmál skiptast svo í þrennt varðandi `veldisvirkja <https://en.wikipedia.org/wiki/Exponentiation#In_programming_languages>`_, sum nota :code:`**`, sum nota ``^`` og sum hafa engan sérstakan virkja fyrir veldishafningu (t.d. C, C++ og Java). Python fellur í fyrsta flokkinn.

Útkoma úr **deilingu heiltalna** er annað vandamál sem forritunarmál leysa með mismunandi hætti: sum skila kommutölu og sum skera aukastafi af og skila heiltölu. Í Python er málið leyst með því að hafa tvo virkja, :code:`/` skilar kommutölu, en :code:`//` lækkar útkomu í átt að núlli og skilar heiltölu. Virkjar til að finna `afgang <https://en.wikipedia.org/wiki/Modulo_operation#In_programming_languages>`_ úr heiltöludeilingu eru nokkuð misjafnir milli forritunarmála, en virkinn sem Python notar, :code:`%`, er algengastur.

Loks notar Python ensk orð, *and*, *or* og *not*, fyrir **rökvirkja** (*logical operators*), eins og boðað var í innganginum að framan, en ekki virkjana ``&&``, ``||`` og ``!`` sem mörg forritunarmál hafa.

.. rubric::
   Yfirlit

Hér er yfirlit yfir helstu virkja fyrir grunntögin í Python:

.. code-block:: text

   + – * /          # eins og í flestum öðrum forritunarmálum
   %                # x % y er afgangur úr deilingunni x//y (7%4 gefur 3)
   **               # veldi (x**y táknar x í veldinu y)
   //               # heiltöludeiling (aukastafir skornir af; 7//4 gefur 1)
   < > <= >= == !=  # samanburðarvirkar (eins og í Java eða C)
   and or not       # rökvirkjar
   << >> & ~ ^      # bitavirkjar, eins og í C, ~ er fyllitala og ^ er xor
   str + str        # samskeyting strengja ("ab" + "12" gefur "ab12")
   str*n            # fjölföldun strengs ("ab"*3 er "ababab")
   (...)            # svigar stýra röð útreiknings

.. rubric::
   Útkoma úr blönduðum útreikningi

Grunnreglan um útkomu úr aðgerð með tveimur tölum er að ef önnur eða báðar eru kommutala þá er niðurstaðan kommutala, en ef báðar eru heiltölur kemur út heiltala. Aðalundantekningin er deiling, en deiling tveggja heiltalna með /-virkja gefur kommutölu.

Bent skal á að hér eru orðin heiltala og kommutala notuð í tölvufræðilegri merkingu, sem sé að viðkomandi gildi séu af heiltölu- eða kommutölutagi. Tölvur greina nefnilega á milli heiltölunnar 2 og kommutölunnar 2.0, þær eru af mismunandi tagi og geymdar með mismunandi bitarunum í minni tölvunnar.

.. rubric:: Forgangsröð aðgerða

Eftirfarandi tafla sýnir röð sem aðgerðir eru framkvæmdar í ef svigar segja ekki til um aðra röð:

.. code:: text

   **             # frá hægri til vinstri, 4**3**2 = 4**(3**2) = 262144
   *, /, // og %  # frá vinstri til hægri; x/y*z jafngildir (x/y)*z
   + og –         # frá v til h; a - b*c + d jafngildir (a - (b*c)) + d
   samanburður    # frá v til h; x < y < z jafngildir x < y og y < z
   not            # ath. að not x < y jafngildir not (x < y)
   and           
   or

.. admonition:: Æfing: Útreikningur
   :class: aefing

   Byrjið á að opna tóma vinnubók.
   
   1. Reiknið :code:`7/4, 7//4, 8/4, 8//4`
      
   2. Búið til nýjan reit og reiknið þar :code:`7 % 4` og :code:`7**4`.
      Hvað er verið að reikna?
      
   3. Látið :code:`x = 5` og notið rökvirkja, samanburðarvirkja og
      afgangsvirkjann :code:`%` til að kanna sannleiksgildi yrðinganna:
         
      .. math::
         & 2 < x < 7\text{ og }x \neq 10 \\
         & x \text{ er slétt tala minni en } 8

Gildisgjöf
==========
Í stærðfræði er **gildisgjöf** (*assignment*) stundum táknuð með virkjanum :math:`:=` (t.d. :math:`x := 1`), og í reikniritum er stundum notuð ör (:math:`x \gets 1`), og þá er einfalt jafnaðarmerki notað til að segja að tvær stærðir séu jafnar eða kanna hvort þær séu jafnar: ":math:`x = 1`" þýðir að breytan :math:`x` (sem þegar hefur verið skilgreind) hafi gildið 1, og "ef :math:`x = 1`, þá..." spyr hvort :math:`x` sé 1. Í forritunarmálum er hinsvegar orðið mjög algengt að nota einfalt jafnaðarmerki fyrir gildisgjöf og tvö í röð fyrir samanburðarvirkjann `==` og Python er engin undantekning frá þeirri venju.

Gildisgjöf í Python er tvennskonar, hægt er að gefa breytu gildi og svo er líka hægt að uppfæra gildið sem breyta geymir, sem sé:

   .. code:: python

      breyta = segð   # t.d. a = x + 3
      breyta += segð  # leggur segð við breytu, t.d. er a += 3 jafngilt a = a + 3
      breyta -= segð  # dregur frá; líka má *=, /= o.s.frv.

Það eru síðan nokkrir fleiri möguleikar sem verða útskýrðir betur í næstu köflum: Viðtakandi gildisins má vera stak í lista (t.d. :code:`L[i]`) eða eiginleiki í hlut (:code:`punktur.x`). Svo er líka hægt að gefa mörgum breytum gildi samtímis með því að skrifa:

   .. code:: python
             
      breyta, breyta... = runa    # lengd runu þarf að vera jafn fjölda breyta
                                  # Dæmi: x,y,z = 5,6,7
      (breyta, breyta...) = runa  # annar möguleiki; dæmi (x,y,z) = (5,6,7)
      (x,y) = (y,x)               # þessi skipun skiptir á gildum x og y

.. admonition:: Æfing: Breytum breytt
   :class: aefing
           
   Haldið áfram með vinnubókina úr síðustu æfingu og búið til nýja reiti eftir þörfum.
   
   1. Lát :code:`x = 5` og reiknið svo :code:`p = x == 5` og :code:`q = x == 6`.
   2. Hækkið x um 2 með :code:`+=` virkja
   3. Lát :code:`y = 10` og skiptið á x og y

.. _útprentun:      
      
Útprentun og innlestur
======================
Aðalaðferðin til að prenta út gildi í Python er að nota :code:`print`-fallið en í vinnubókum er líka hægt að nota fallið :code:`display`, sem gefur stundum öðruvísi úttak, t.d. ef prentaðir eru strengir eða nöfn taga og falla (sjá næstu æfingu). Sumir pakkar sem þið gætuð átt eftir að kynnast, t.d. pandas og statmodels, skila stundum HTML-sniðnum töflum, og til að birta þær þarf að nota :code:`display`. 

    - :code:`print(segð,segð...)`: Prentar segðirnar með bilum á milli
    - :code:`print(..., sep=",")`: Prentar með kommum á milli
    - :code:`print(..., end=" ")`: Endar með bili í stað nýrrar línu
    - :code:`s = input('texti')`: Prentar textann og bíður eftir að notandi
      slái inn streng og <Enter>; innslegið gildi → s.

Næsta grein (:numref:`fstrengir`) útskýrir svo hvernig **sníða** (*formatera*) má útprentuð gildi með svonefndum f-strengjum.

.. admonition:: Æfing: input og print 
   :class: aefing

   1. Input-fallið skilar streng s, sem hægt er að breyta í tölu með
      :code:`t = float(s)` eða :code:`k = int(x)`. Afritið eftirfarandi
      skipanir yfir í vinnubók. Notið tækifærið og prófið vinnubókarskipanir
      til að velja allt í reit og flytja það til vinstri (shift/tab,
      *unindent*), sbr. :numref:`vinnubokarritilskipanir`. Keyrið, sláið inn
      tölu, og prófið líka að slá inn eitthvað annað en tölu.

      .. code:: python3

         s = input('Sláðu inn tölu: ')
         t = float(s)
         print(t)

   2. Afritið eftirfarandi forritsbút yfir í vinnubók. Keyrið, og prófið svo
      að nota :code:`end=";"` og :code:`sep=","` og prófið líka að breyta
      :code:`print` í :code:`display`.

      .. code:: python3

         x = 2
         s = "AB"
         print(x, s)
         print(x*2, s*2)

.. _fstrengir:

F-strengir
==========

F-strengir (*f-strings*) eru ætlaðir til útprentunar, og með þeim má tvinna
saman strengi (textabúta), breytur og gildi (segðir). Breytur og gildi eru sett
innan slaufusviga og þeim getur líka fylgt snið á eftir tvípunkti, sem sé:

    .. code:: python3

       f'texti {segð} texti {segð:snið} texti {segð:snið} ...'

Hér getur hver segð (*expression*) verið breyta eða útreiknuð stærð, og snið (sem
má sem sé sleppa) gefur oftast heildarfjölda stafa og/eða fjölda aukastafa.
Hér er tafla yfir nokkur möguleg snið:

.. list-table:: Nokkur möguleg snið í f-strengjum
   :widths: auto
   :name: fstrengjasnið
       
   * - :code:`{heiltala}` |br|
       :code:`{strengur}` |br|
       :code:`{kommutala}`
     - Heiltala og strengur skrifast óbreytt og kommutala með  |br|
       jafnmörgum aukastöfum og þarf til að sýna nákvæmt gildi hennar.

   * - :code:`{heiltala:n}` |br|
       :code:`{strengur:n}`
     - Skrifað í n stafa breitt svið, tölur hægri-jafnaðar og  |br|
       strengir vinstri-jafnaðir

   * - :code:`{heiltala:0n}`
     - Skrifa töluna hægri-jafnaða í n-stafa breitt svið og fylla með |br|
       núllum frá vinstri; ``{k:03}`` myndi skrifa ``007`` ef k=7

   * - :code:`{heiltala:<n}`
     - Vinstri-jafna heiltölu í n stafa svið

   * - :code:`{strengur:>n}`
     - Hægri-jafna streng í n stafa svið

   * - :code:`{heiltala:^n}` |br|
       :code:`{strengur:^n}`
     - Skrifa miðjað í n stafa svið

   * - :code:`{kommutala:n}`
     - Skrifa kommutölu með n "marktækum stöfum" (*significant digits*)

   * - :code:`{kommutala:.mf}`
     - Skrifa kommutölu með m aukastöfum fyrir aftan kommu

   * - :code:`{kommutala:n.mf}`
     - Skrifa kommutölu með m aukastöfum í n stafa breitt svið

   * - :code:`{kommutala:.mE}`
     - Skrifa kommutölu á staðalformi með tugveldistáknun og m |br|
       aukastöfum, t.d. skrifar :code:`{10**13:.2E}` út :code:`1.00E+13`. |br|
       Nota má :code:`n.mE` til að skrifa í n stafa breitt svið, og :code:`n.me` |br|
       til að fá lítið e í útskriftina (t.d. :code:`1.00e+13`)

Tilgangurinn með að gefa heildarfjölda stafa (breidd sviðs) getur t.d. verið að
láta dálka í töflu standast á: forritið í sýnidæminu í grein :numref:`for-lykkjur`
notar f-strengi til að sníða (*"formatera"*) litla töflu. Hér eru þrjú dæmi í
viðbót:

    .. code:: python3

       f'hæð = {h}, breidd = {x*y}'
       f"A = {A:.3f}, B = {B:.2f}"
       f'Halló {nafn} og vertu velkomin(n)'

þar sem gert er ráð fyrir að h, x og y séu heiltölubreytur, A og B séu
kommutölubreytur og nafn sé strengjabreyta. Forritið gæti t.d. skrifað út:

   .. code:: text
      
      hæð = 10, breidd = 28
      A = 6.281, B = 11.37
      Halló Kristján og vertu velkomin(n)
       
.. danger::
   F-strengir eru nýleg viðbót við Python, þeir komu í Python 3.6 í desember
   2016. Í eldri Python-útgáfum er hægt að nota %-virkja. Forritið í sýnidæminu
   í grein :numref:`for-lykkjur` gæti t.d. haft: |br|
   |sp3| |sp3| :code:`print('%d   %.4f   %2d' % (x, math.sqrt(x), x**2))` |br|
   í öftustu línunni.
   
.. _ny-foll:
   
Föll notanda (ný föll)
======================
Notendaföll (*user-defined functions*) eru næstum jafngömul forritun, og fyrstu
forritunarmálin gáfu kost á skilgreiningu þeirra. Stundum er reyndar notað orðið
**undirforrit** (*subroutine*) í stað falls einkum um föll sem engu skila (sbr.
kafla :numref:`virka`), en í Python er yfirleitt bara talað um föll. Við höfum
þegar séð dæmi um föll, í forritinu Collatz í kafla :numref:`collatz`.

.. rubric:: Af hverju þarf föll?
            
Það eru ýmsar ástæður til að skilgreina og nota ný
föll, en þær mikilvægustu eru:

1. Að gera forritin skýrari, helst þannig að þau útskýri sig sjálf.
   Forsenda fyrir því er að valin séu góð nöfn á föllin, sem segja
   í orðum hvað föllin gera.
2. Að skipta stærri forritum upp minni einingar sem auðvelt er að útfæra
   (skrifa forrit fyrir) hverja um sig. Það getur verið erfitt að halda
   utan um alla þræði stórs forrits og muna hvað hver hluti þess gerir.
   En ef búið er að skrifa fall fyrir ákveðna aðgerð, og lýsa því hvað
   það gerir og hvernig kallað er á það, þá má gleyma öllu um hvernig
   það vinnur.
3. Að losna við endurteknar blokkir af sömu skipunum. Þessi ástæða
   birtist þannig að kallað er á fall oftar en einu sinni í sama forriti.
4. Að geta endurnýtt forritsbúta seinna. Þessi ástæða birtist þannig að kallað
   er á sama fall í mismunandi forritum.

Föllin í Collatz-forritinu falla í flokka 1 og 2. Til að láta þau falla vel
í flokk 1 ættum við reyndar að skíra þau lengri nöfnum, t.d.
:code:`finna_næstu_tölu_á_eftir` og :code:`finna_collatz_runu_sem_byrjar_á`.
Ef það er gert mætti sem best sleppa dokk-strengjunum. 

.. rubric:: Skilgreining falls

.. code:: python3

   def fall(stiki, stiki...):
       '''skjölunarstrengur'''
       skipanir
       return g

   # Skjölunarstrengurinn er valkvæður en góð regla að hafa hann með
   # Ef fallið skilar mörgum gildum endar það á: return (g1,g2...)
   # Ef það skilar engu er return-skipun sleppt
           
.. rubric:: Kallað á fall

:code:`g = fall(viðfang, viðfang...)` |br|
Má líka nota í segð: :code:`h = 2*fall(viðföng) + 1` |br|
Ef fallið skilar engu: :code:`fall(viðföng)` |br|
Ef fallið skilar mörgum gildum: :code:`(g1,g2...) = fall(viðföng)` |br|
Líka má sleppa svigunum: :code:`g1,g2... = fall(viðföng)` |br|

.. admonition:: Sýnidæmi: Rúmmál keilu
   :class: synidaemi

   Hér er fall sem reiknar rúmmál keilu með gefna hæð og radíus grunnflatar, skv. formúlunni

   .. math:: R = \frac{\pi r^2 h}{3}
           
   .. code:: python
             
      def rúmmál_keilu(h, r):
          '''skilar rúmmáli keilu með hæð h og radíus grunnflatar r'''
          pí = 3.14159265
          R = pí*r**2*h/3
          return R

   og hér er fall sem reiknar rúmmál tveggja keila, sú fyrri hefur :math:`h=4` og
   :math:`r=3` og hin hefur :math:`h=2` og :math:`r=1`.

   .. code:: python

      # Forrit sem reiknar rúmmál tveggja keila
      R1 = rúmmál_keilu(4,3)
      R2 = rúmmál_keilu(2,1)
      print(f"Rúmmál keilanna eru {R1:.3f} og {R2:.3f}")

   Fallið prentar út :code:`Rúmmál keilanna eru 37.699 og 2.094`

.. _virka:
   
Hvernig virka föll
==================
.. rubric:: Viðföng og stikar
            
Breyturnar innan sviga á eftir fallsnafninu þar sem það er skilgreint kallast **stikar** (*parameters*), en þegar kallað er á fallið þá heita gildin sem sett eru í sviga á eftir fallsnafninu **viðföng** (*arguments*). Þau þurfa ekki að vera breytur en mega vera hvaða segðir sem er. **Viðfang** er sem sé gildi sem sent er inn í fall, en **stiki** er breyta í skilgreiningu fallsins sem tekur við gildinu.

.. rubric:: Keyrsla forrits og falla
            
Hægt er að hugsa sér að forrit keyri þannig að það sé bendill sem færist niður eftir
forritstextanum og bendi á næstu línu sem á að framkvæma. Þegar bendillinn kemur
að kalli á fall færist hann yfir í fyrstu línu fallsins. Áður en hann 
heldur áfram þar eru framkvæmdar ósýnilegar gildisgjafarskipanir, :code:`stiki = viðfang`
fyrir alla stikana sem koma við sögu. Í fyrra kallinu í sýnidæminu er framkvæmt:
:code:`h=4` og :code:`r=3`. Þegar fallið er á enda færist bendillinn svo aftur
þangað sem frá var horfið í forritinu sem kallaði, og þar er niðurstöðu fallsins
skilað inn í viðtökubreytu (sem í dæminu okkar er :code:`R1`).

.. rubric:: Fjöldi skilagilda

Fallið í sýnidæminu í kafla :numref:`ny-foll` skilaði einu gildi, rúmmálinu sem
verið var að reikna. En það er líka hægt að búa til föll sem skila **mörgum gildum**
eða **engu** gildi, sbr eftirfarandi sýnidæmi.

Forrit sem engu skila gegna oft því hlutverki að birta eitthvað á skjá, t.d.
útprentun á tölu, hnapp á vefsíðu, eða merkingu á x-ás í línuriti sem verið er
að teikna. Þau gætu líka skrifað gögn í skrá, og stundum eru þau notuð til að
stjórna ýmsu sem síðar er birt, t.d. litum á næstu línum í línuritinu.

.. admonition:: Sýnidæmi: Fall sem skilar tveimur niðurstöðum
   :class: synidaemi

   Fall sem skilar bæði ummáli og flatarmáli hrings með radíus :code:`r` ásamt
   tilheyrandi kalli fyrir hring með radíus 1. Þetta forrit prentar út
   :code:`Flatarmálið er 3.142 og ummálið 6.283`

   .. code:: python

      def flat_og_um(r):
          pi = 3.14159265
          F = r**2*pi
          U = 2*r*pi
          return F,U

      (F,U) = flat_og_um(1)
      print(f"Flatarmálið er {F:.3f} og ummálið {U:.3f}")

.. admonition:: Sýnidæmi: Fall sem skilar engu
   :class: synidaemi

   Þetta fall prentar línu með stjörnum. Ef kallað er með
   :code:`prenta_stjörnur(10)` prentar það :code:`**********`.

   .. code:: python

      def prenta_stjörnur(n):
          '''prentar línu með n stjörnum'''
          print(n*"*")

   Fallið notar virkjann :code:`*` til að fjölfalda streng; sjá kafla
   :numref:`adgerdir-og-virkjar`

.. _mikilvægustu-innbyggð:
       
Innbyggð föll
=============
Fyrir utan föll sem notendur skrifa hafa forritunarmál yfirleitt fjöldan allan af
innbyggðum föllum, sem hönnuðir málanna hafa skrifað og gert aðgengileg fyrir
notendur. Mörg þessara falla eru notuð í útreikningum, en auk þess eru ýmis önnur
föll, t.d. föll til að prenta (sem sé sýna texta og gildi á breytum á skjá),
til að búa til runur, eða til að breyta um tög (t.d. breyta kommutölu í heiltölu
eða streng í tölu). Í Python eru nokkur almenn föll sem alltaf eru aðgengileg,
en flest föll eru geymd einingum (*modules*) sem tilheyra pökkum (*packages*) sbr.
kafla :numref:`pakkar`. Þau þarf að gera aðgengileg með því að *flytja inn* viðkomandi einingu með :code:`import` skipun.
   
.. rubric::
   Mikilvæg almenn föll

.. table::
    :widths: auto
    :name: tab:almenn-föll

    +-----+---------------------------------------------+
    |abs  |tölugildi, abs(-3) → 3                       |
    +-----+---------------------------------------------+
    |max  |hámark: max(1,2) → 2                         |
    +-----+---------------------------------------------+
    |min  |lágmark: min(1,2) → 1                        |
    +-----+---------------------------------------------+
    |int  |kommutala → heiltala, strengur → heiltala    |
    +-----+---------------------------------------------+
    |round|kommutala → næsta heiltala (rúnnað)          |
    +-----+---------------------------------------------+
    |float|heiltala → kommutala, strengur → kommutala   |
    +-----+---------------------------------------------+
    |range|býr til runu til að nota í for-lykkju,       |
    |     |sjá grein :numref:`icollatz`                 |
    +-----+---------------------------------------------+
    |len  |lengd strengs                                |
    +-----+---------------------------------------------+
    |type |tag breytu                                   |
    +-----+---------------------------------------------+

**Ath.** Með ``int`` eru aukastafir skornir af en með ``round`` eru tölur
hækkaðar eða lækkaðar eftir því hvort aukastafirnir eru > 0.5 eða < 0.5.
Ef aukastafir eru = 0.5 er valin næsta slétta tala: 2.5 → 2 og 3.5 → 4.
    
.. admonition:: Æfing: Prófun almennra falla
   :class: aefing
           
   1. Opnið vinnubók og prófið öll þessi föll. Látið t.d. x = –3,
      y = 2.7, s = \"abc\" og finnið \|x\|, max(x,y), min(x,y), float(x),
      int(y), range(4), len(s) og type(s).

   2. Skoðið muninn á því sem :code:`print(type(s))` og :code:`display(type(s)` birta.

.. rubric::       
   Helstu stærðfræðiföll og fastar

Til að virkja innbyggð stærðfræðiföll í Python þarf að flytja inn sérstakt fallasafn eða einingu, ``math`` með því að skrifa fremst í forritinu:

    :code:`import math`

og svo þarf að setja :code:`math.` framan við fallsnafnið þar sem fallið er
notað, t.d. mundi

.. code::
   
   import math
   print(math.sin(math.pi/6))

reikna og prenta út :math:`\sin \pi/6` (sem er 0.5). Svo er líka hægt að skrifa

    :code:`from math import nafn, nafn...`

þar sem nafn, nafn... eru stærðfræðiföll eða -fastar, og þá þarf ekki að setja
``math.`` framan við nöfnin. Önnur leið til að reikna :math:`\sin \pi/6` er sem sé:

.. code::
   
   from math import sin, pi
   print(sin(pi/6))

Hér er upptalning á helstu innbyggðum stærðfræðiföllum og -föstum:

.. code::
   
    sin, cos, tan, asin, acos, atan  # Hornaföll í radíönum
    atan2                            # Arctan fyrir pólhnit, Sjá verkefni :numref:`pólhnit`
    exp, log, log2, log10, sqrt      # Vísisfall, lograr og kvaðratrót
    pi, e, inf, nan                  # (stærðfræði)fastar
    radians, degrees                 # breytt úr gráðum í radíana og öfugt

Ath. að ``log(x)`` gefur náttúrulegan logra (lógaritma), sem oft er táknaður ln(x).

Sjá nánar í `Python hjálpinni <https://docs.python.org/3/library/math.html>`_,
og ýmis dæmi í þessum fyrirlestrarnótum, t.d. sýnidæmið hér næst, "Ósamsett trapisuregla" í kafla :numref:`fallbreytur`, "Rætur og veldi" í kafla
:numref:`for-lykkjur` og :numref:`verkefni %s<pólhnit>` aftast í nótunum.

.. admonition:: Sýnidæmi: Regla Herons
   :class: synidaemi

   Flatarmál þríhyrnings með hliðarlengdir :math:`a`, :math:`b` og :math:`c` er
   gefið með reglu Herons:
   
   .. math:: F = \sqrt{s(s-a)(s-b)(s-c)}

   þar sem :math:`s` er hálft ummál þríhyrningsins, :math:`s=\dfrac{a+b+c}{3}`.
   Hér er Python-forrit sem reiknar flatarmál þríhyrnings með hliðarlengdir
   3, 4 og 5 (auðvelt er að sjá að það á að koma út 6):

   .. code:: python
             
      import math
      a = 3
      b = 4
      c = 5
      s = (3 + 4 + 5)/2
      F = math.sqrt(s*(s-a)*(s-b)*(s-c))
      print(f"Flatarmálið er {F}")
            
.. admonition:: Æfing: Sveiflutími gorms
   :class: aefing
           
   .. figure:: myndir/gormakerfi.png
               :align: center
               :figwidth: 10cm

   Á myndinni er gormakerfi: Hlutur með massa :math:`m` hvílir á fleti án
   núningsmótstöðu og er festur við veggina með gormum með stífnifasta
   :math:`k_1` og :math:`k_2`. Eiginsveiflutími kerfisins verður

   .. math::
      T = 2\pi\sqrt{\frac{m}{k_1+k_2}}

   1. Skrifið fall :code:`sveifla(m,k1,k2)` sem reiknar sveiflutímann. Pí fæst
      með :code:`math.pi`.

   2. Skrifið forrit sem prófar fallið með m = 2, k1 = 3 og k2 = 4, og skrifar
      út sveiflutímann á sniðinu `T = x.xxx` (með f-streng).

Fallbreytur
===========
Breytur geta tekið gildi sem eru föll: :code:`def fall: ...` og neðar: :code:`x = fall` eins og eftirfarandi dæmi sýnir.

   .. admonition:: Sýnidæmi: Bulla tvisvar
      :class: synidaemi

      .. code:: python3

         def gera_tvisvar(f):
             '''framkvæmir f tvisvar'''
             f()
             f()

         def bulla():
             '''skrifar "bull"'''
             print("bull")

         b = bulla         # b er fallbreyta
         gera_tvisvar(b)   # prentar bull tvisvar

Meðal þess sem hægt er að nota fallbreytur í er ýmis vinna með stærðfræðiföll, til
dæmis að teikna þau, finna heildi (*integrals*) eða leysa jöfnur. Segjum til
dæmis að við viljum reikna heildið:

.. math::  (*)\hspace{4cm}\int_1^2\frac{\sin(x)}{x} dx\hspace{4cm}

Þetta heildi er ekki hægt að reikna með venjulegum aðferðum stærðfræðigreiningar
en hinsvegar er auðvelt að reikna það tölulega, t.d. með svonefndri
`trapisureglu <https://en.wikipedia.org/wiki/Trapezoidal_rule>`_, sem nálgar
heildið með flatarmáli trapisu, nánar tiltekið:

.. math:: \int_a^b{f(x)dx} \approx \frac{(b-a)(f(a) + f(b))}{2}

Það væri hægt að skrifa Python-fall til að reikna :math:`(*)` með
trapisureglu, en ef við vildum reikna eitthvað annað heildi þyrfti að skrifa
nýtt fall. Með því að nota fallbreytu er hægt að forrita trapisureglu í eitt
skipti fyrir öll Í Python, eins og hér er sýnt:

.. admonition:: Sýnidæmi: Ósamsett trapisuregla
   :class: synidaemi

   Í þessu dæmi er heildið :math:`(*)` nálgað með ósamsettri trapisureglu og einnig heildið
   :math:`\int_0^1 h(x)dx` þar sem :math:`h(x)=e^x`.

   .. code:: python3

      def trap1(f,a,b):
          '''heildi f frá a til b með ósamsettri trapisureglu'''
          I = (b-a)*(f(a)+f(b))/2
          return I

      from math import sin, e
      def g(x): return sin(x)/x
      def h(x): return e**x

      I1 = trap1(g,1,2)
      I2 = trap1(h,0,1)
      print(f'I1={I1:.3f}, I2={I2:.3f}')
          # prentar "I1=0.648, I2=1.859"

   Nákvæm gildi á þessum heildum eru I1 = 0.659 og I2 = 1.718. Takið
   eftir að hægt er að skilgreina einföld föll á einni línu.

.. admonition:: Æfing: Tvær trapisur
   :class: aefing

   Betri nálgun á heildi fæst með því að nota tvær trapisur:

   :math:`\qquad\displaystyle\int_a^b{f(x)dx} \approx`
   :code:`trap1(f,a,m) + trap1(f,m,b)`
   
   þar sem :math:`m` er miðpunktur bilsins; :math:`m = \dfrac{a+b}{2}`. Skrifið
   fall :code:`trap2` sem útfærir slíka reglu með því að kalla tvisvar á :code:`trap1` og
   prófið með því að nálga sömu heildi og í sýnidæminu. Ef rétt er forritað fást
   nú gildin I1 = 0.657 og I2 = 1.754.
   
Stýriskipanir
=============
Í kafla :numref:`virka` var talað um að forrit keyri þannig að bendill færist
niður eftir forritstextanum og bendi á næstu línu sem á að framkvæma, og hvernig
þessi bendill stekkur á annan stað þegar kallað er á föll. Þetta er hinsvegar
ekki eina leiðin til að flytja bendilinn, það er líka hægt með svonefndum
**stýriskipunum** (*control statements*). Það eru tvær aðalgerðir af stýriskipunum
**ef-setningar** (*if statement*) og **lykkjuskipanir** (*loop statement*).
Við höfum þegar séð ef-setningar í Collatz-forritinu í kafla :numref:`dæmi-um-forrit`,
og þar voru líka tvær gerðir af lykkjuskipunum, while-lykkjur og for-lykkjur.

Ef-setningar
------------
Hlutverk ef-setninga er að keyra mismunandi kafla forrits eftir því hvort
tiltekið skilyrði er uppfyllt eða ekki. Ef-setningin er stundum kölluð
*ef-þá-annars* (*if-then-else*) skipun því í mörgum forritunarmálum er orðið
*then* notað á eftir skilyrðinu. Eins og sýnt var í kafla :numref:`icollatz`
er grunnsnið ef-setningar svona:

.. code:: python

   if skilyrði:
       skipun1
       skipun2
       ...
   else:
       skipun3
       skipun4
       ...
   skipun5

Ef skilyrðið er uppfyllt keyra skipanir 1 og 2 og svo fer bendillinn í skipun 5,
en annars keyra skipanir 3 og 4 og svo áfram í númer 5. Kaflarnir sem
ef-setningin stýrir eru inndregnir um eitt eða fleiri bil. Maður ræður hve
mikill inndrátturinn er, en það þarf að draga allar línur hvers kafla jafnmikið
inn. Svo er hægt að bæta við *elif* (stytting á *else if*) kafla eða köflum á
undan else-kaflanum eins og næsta sýnidæmi sýnir:

.. admonition:: Sýnidæmi: Notkun ef-setningar
   :class: synidaemi

   Þetta dæmi les aldur tveggja manna Jóns og Páls og athugar hvor er eldri.

   .. code:: python
             
      ajons = int(input("Aldur Jóns: "))
      apals = int(input("Aldur Páls: "))
      if ajons > apals:
          print("Jón er eldri en Páll")
      elif ajons == apals:
          print("Jón og Páll eru jafngamlir")
      else:
          print("Páll er eldri en Jón")
      print("–og hér heldur forritið áfram")

For-lykkjur
-----------
Til að keyra kafla í forriti aftur og aftur og uppfæra svonefnda **stýribreytu**
(*control variable*) í hverri umferð með nýju gildi má nota for-lykkjur. Snið
for-lykkju er:

.. code:: python

   for stýribreyta in runa:
       skipun1
       skipun2
       ...
   skipun3
      
Hér er :code:`runa` einhver Python-aðferð til að búa til endanlega runu
(*sequence*) af gildum sem stýribreytan fær. Skipanir 1 og 2 keyra jafn oft og
lengd rununnar er, og í hverri umferð fær breytan næsta gildi rununnar. Að því
loknu er haldið áfram með skipun 3. Algengasta aðferðin til að búa til rununa er
að nota range-fallið, sbr. Collatz-forritið og næsta sýnidæmi. Hér eru helstu
möguleikar á range fallinu:

.. code:: python

   range(5)       runan 0, 1, 2, 3, 4
   range(2,5)     runan 2, 3, 4
   range(2,10,2)  runan 2, 4, 6, 8
   range(6,1,-1)  runan 6, 5, 4, 3, 2

.. admonition:: Sýnidæmi: Rætur og veldi
   :class: synidaemi

   Eftirfarandi forrit reiknar kvaðratrætur og önnur veldi talnanna 2, 3, 4 og
   5. Það sýnir notkun á nokkrum atriðum sem fjallað hefur verið um hér á undan.

   .. code-block:: python

      import math
      print('x     √x     x²')
      print('―――――――――――――――')
      for x in range(2,6):
          print(f'{x}   {math.sqrt(x):.4f}   {x**2:2}')

   Fallið prentar út eftirfarandi töflu

   .. code-block:: text

       x     √x     x²
       ―――――――――――――――
       2   1.4142    4
       3   1.7321    9
       4   2.0000   16
       5   2.2361   25

.. admonition:: Æfing: *Range* og breytilegur aukastafafjöldi
   :class: aefing

   Sláið forritið í sýnidæminu hér á undan inn í vinnubók (eða
   afritið það). Prófið svo að breyta forritinu með því að:

     1. Sleppa 2, í range kallinu
     2. Nota :code:`for x in range(0,8,2)`
     3. Láta n = 3 (á undan for-lykkjunni) og breyta .4f í .{n}f

   (Ath. að nota má V, |sp| ^2 og - í stað *unicode* táknanna √, |sp| ² og
   ― ef maður vill)       

While-lykkjur
-------------
Stundum þarf enga stýribreytu, heldur er eðlilegra að halda áfram að endurtaka
meðan tiltekið skilyrði er uppfyllt. Gott dæmi um þetta er í forritinu Collatz,
þar sem haldið er áfram meðan ný tala í rununni er stærri en 1. Eins og þar
sást er snið while-lykkju svona:

.. code:: python

   while skilyrði:
       skipun1
       skipun2
       ...
   skipun3

Næsta æfing gefur síðan klassíska og nokkuð ítarlega notkun á while-lykkju. Það
gefur líka innsýn inn í hugtakið reiknirit (*algorithm*) sbr. athugasemdina
aftan við sýnidæmið.

.. admonition:: Æfing: Reiknirit Evklíðs
   :class: aefing

   Reiknirit Evklíðs er notað til að finna stærsta samþátt (*greatest common
   divisor*) tveggja talna :math:`x` og :math:`y`, sem oft er táknaður
   :math:`\gcd(x,y)`. Til dæmis er :math:`\gcd(9,15) = 3` því 3 er stærsta talan
   sem gengur upp í bæði 9 og 15. Skoðið stuttlega 
   `Wikipediugreinina <https://en.wikipedia.org/wiki/Euclidean_algorithm>`_ um
   reikniritið. Hér er lýsing á því í orðum: "Deilið minni tölunni í þá stærri.
   Ef afgangurinn er ekki núll verður hann nýr deilir og minni talan verður nýr
   deilistofn. Svo er deilt aftur og aftur þar til deilingin gengur upp. Stærsti
   samþátturinn er síðasti jákvæði afgangurinn."

   1. Hvað er þetta reiknirit gamalt?
   2. Nefnið a.m.k. eitt notkunarsvið þess nú á tímum.
   3. Reiknið :math:`\gcd(102,27)` með blaði og blýanti.
   4. Wikipedia er með nokkrar útfærslur reikniritsins á blendingsmáli í
      `Implementations <https://en.wikipedia.org/wiki/Euclidean_algorithm#Implementations>`_.
      Þýðið þá fyrstu yfir í Python og prófið. Setjið inn print-skipun til að
      skoða alla afgangana sem fást.

|br|

.. admonition:: Athugasemd: Reiknirit og Python
   :class: athugid

   **Reiknirit** er endanleg runa af skipunum sem hægt er að þýða yfir í
   tölvuforrit. Reiknirit eru venjulega notuð til að leysa ákveðin verkefni og
   þau eru alltaf ótvíræð. Reiknirit eru of skrifuð í blendingsmáli
   (*pseudocode*), en það er frjálsleg lýsing á tölvureikningum, þar sem blandað
   er saman forritsskipunum, lýsingu skrefa á íslensku (eða ensku) og
   stærðfræðiformúlum (sbr. `þetta
   <https://en.wikipedia.org/wiki/Ford–Fulkerson_algorithm#Algorithm>`_).
   Forritsskipanirnar mega vera á íslensku og svolítið frjálslegar, og
   stærðfræðiformúlurnar mega vera allflóknar, t.d. með brotastrikum og summum.
   Ef borin eru saman forrit í Python, forrit í ýmsum öðrum forritunarmálum, og
   reiknirit á blendingsmáli (t.d. á Wikipediu) sést að Python minnir um margt á
   sum þessara reiknirita.
  
Skipanirnar *continue* og *break*
---------------------------------
Inni í lykkjum er hægt að nota tvær skipanir í viðbót til að færa
keyrslubendilinn sem talað var um í byrjun kaflans, :code:`continue` sem
hleypur yfir afgang lykkjukaflans og byrjar strax á næstu umferð, og svo er
:code:`break` notað til að brjótast strax út úr lykkjunni og halda áfram
með næstu skipun á eftir henni. Af þessum tveimur er :code:`break` meira
notuð. Með henni er hægt að láta for-lykkju herma eftir while-lykkju, svona:

.. code:: python
          
   for i in range(99999999):
       if not skilyrði: break
       skipun1
       skipun2
       ...

Hér þarf að passa að velja nógu stóra tölu í range-fallinu.

Skilyrt gildi
=============
Í stærðfræði er hægt að skilgreina breytur og föll með svonefndum gaffalformúlum,
þar sem gildið sem breytan eða fallið fær fer eftir tilteknu skilyrði. Hér er dæmi:

.. math::
   f(x) =
   \begin{cases} x^2 & \text{ef } x < 1 \\ 2x - 1 & \text{annars}
   \end{cases}

Svona skilgreiningu má búa til í Python með svonefndu **skilyrtu gildi** (*conditional
expression*). Skipunin:

  .. code:: python3

     x = segð1 if skilyrði else segð2          

jafngildir:

  .. code:: python3

     if skilyrði:
        x = segð1
     else
        x = segð2

Til dæmis mætti reikna tölugildi með ``a = -x if x < 0 else x``. Í Java og C er
hægt að búa til svona gildi með :code:`x = skilyrði ? segð1 : segð2` og
tölugildið fengist með ``a = x < 1 ? -x : x``.

.. admonition:: Æfing: Gaffalformúla
   :class: aefing

   Búið til Python fall til að reikna fallið :math:`f(x)` sem skilgreint er með
   gaffalformúlunni hér að ofan. Notið skilyrt gildi. Prófið að reikna
   :math:`f(0)`, og :math:`f(3)` (sem ætti að gefa 0 og 5).

Lokaæfingin
===========
.. admonition:: Æfing: Kynning á vinnubókum II
   :class: aefing

   Í vinnubókinni :ref:`kynning.ipynb<jupyter-æfing>` sem náð var í í Æfingu
   aftan við kafla :numref:`jupyter-leiðbein-á-netinu` er hægt að prófa mörg af
   þeim Python-atriðum sem lýst hefur verið í þessum :numref:`grunn-python`.
   kafla og æfa sig í þeim. Opnið þessa bók í Colab og fylgið leiðbeiningum í
   henni.
