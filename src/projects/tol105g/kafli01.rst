.. include:: rst-include

.. role:: matlab(code)
   :language: matlab
   :class: highlight

.. _c.inngangur:

Inngangur: Um Python
====================

.. _inngangur:

Einfalt og auðlært mál
----------------------

Python er forritunarmál sem kom fram árið 1991 og hefur náð mikilli útbreiðslu. Það var hollenski tölvufræðingurinn Guido van Rossum sem bjó Python til og spilaði stórt hlutverk í þróun þess, en margir fleiri hafa lagt hönd á plóg. Málið heitir eftir grínistahópnum *Monty Python* (sem aftur dregur nafn af kyrkislöngum, *pythons*). 

.. figure:: myndir/monty-python.jpg
   :align: center
   :figwidth: 9cm

   Monty Python grínistarnir

Vinsælasta útgáfan af Python nefnist formlega CPython og er opin og ókeypis. Hana er að finna á `python.org <http://python.org>`_ og þar má líka lesa um *Python Software Foundation* sem hefur síðan 2001 séð um þróun málsins, leyfi, dreifingu, Python-ráðstefnur o.s.frv.

Frá upphafi var markmiðið að búa til einfalt og auðlært forritunarmál, sem væri þannig að oftast væri bara ein augljós og einföld leið til að útfæra tiltekna aðgerð eða reikninga. Forrit áttu að samanstanda af enskum orðum að mestu leyti en ekki samansuðu tákna eins og algengt er t.d. í Perl-forritum, sem minna á blótsyrði í Andrés-blaði.

.. figure:: myndir/perl.png
   :align: center
   :figwidth: 10cm

   Perl-forrit og Andrés Önd
.. _pakkar:

Fallasafn og pakkar
-------------------
Með Python fylgir viðamikið fallasafn (*standard library*) og auk þess eru til ótal viðbætur sem kallast **pakkar** (*packages*) og eru ekki hluti af hinu eiginlega forritunarmáli. Opinber `pakkavefur <https://pypi.org>`_ fyrir Python hefur 322.000 pakka í ágúst 2021, og hann fer ört vaxandi (voru 164.000 í janúar 2019). Fallasafnið samanstendur af mörgum **einingum** (*modules*), og það sama gildir um flesta pakka. Það er sama hvort ætlunin sé að tengjast Oracle gagnagrunni, búa til vefsíðu, skrifa tölvuleik eða leysa stærðfræðileg verkefni: maður getur alltaf fundið vandaðan og almennan Python-pakka í verkið. Síðar í þessum nótum verður fjallað um nokkra slíka m.a. NumPy (fyrir vigur- (*vector-*) og fylkjareikninga), SciPy (fyrir reiknifræði), Pandas (fyrir gagnavinnslu) og Matplotlib (til að teikna).

Útbreiðsla
----------
Ýmsir vefir mæla vöxt og vinsældir forritunarmála og mælist Python í efstu sætunum á þeim flestum, ásamt Javascript, Java, C, C# og C++. Á einum þeirra má t.d. finna eftirfarandi mynd:

.. figure:: myndir/python-vöxtur.png
   :align: center

   Vöxtur í vinsældum Python

Framkvæmd forrita
-----------------
Python er túlkað forritunarmál sem þýðir að forrit eru ekki þýdd fyrirfram á vélamál, heldur eru skipanir þess lesnar af Python túlkinum hver á fætur annarri og framkvæmdar jafnóðum. Hægt er að hugsa sér að túlkurinn hermi eftir ímynduðum gjörva sem hefur Python sem móðurmál. Þetta er reyndar nokkur einföldun, því Python er venjulega þýtt yfir á millimál sem er fljótlegra að túlka. Túlkuð forrit keyra hægar en þýdd, en á móti kemur að ekki þarf að bíða eftir þýðingu, og auk þess fylgja ýmsir kostir fyrir villuleit og þróun forrita skref fyrir skref.

Gildi eru töguð en breytur ekki
-------------------------------
Eitt sem skilur Python frá ýmsum öðrum forritunarmálum, t.d. Java og C, er að það er engin þörf á að skilgreina breytur fyrirfram og segja Python-kerfinu af hvaða tagi (*type*) þær séu. Vissulega hefur Python allskyns tög (*types*), heiltölur, kommutölur, strengi, vigra, mengi o.s.frv., en það eru gildin sem breyturnar fá sem hafa tög, en ekki breyturnar sjálfar. Forrit getur haft skipun :code:`x = 3.5`, og þá verður x kommutala, og neðar getur svo staðið :code:`x = {2, 5, 8}` og eftir það er x mengi.

.. _python-leiðbein-á-netinu:
     
Python-leiðbeiningar á netinu
-----------------------------
Fjölmargar leiðbeiningar um Python má finna á netinu, stuttar og langar, ókeypis og til sölu. Hér eru nokkrar gjaldfrjálsar:

- `Think Python <https://greenteapress.com/wp/think-python-2e/>`_ (ókeypis byrjendakennslubók sem hefur verið kennd í Tölvunarfræði 1a)
- `Google's Python Class <https://developers.google.com/edu/python/>`_ (líka fyrir byrjendur)
- `Learn Python <https://www.learnpython.org/>`_ (með reitum til að keyra forrit og skoða úttak)
- `The Python Tutorial <https://docs.python.org/3/tutorial/index.html>`_ (opinberar Python leiðbeiningar á python.org, fyrir svolítið lengra komna)

.. _kafli1_1:

Dæmi um Python forrit
=====================
Tafla yfir veldi
----------------
Eitt af því sem tölvur eru góðar í er að framkvæma sömu hlutina aftur og aftur. Ein einfaldasta leiðin til að endurtaka skipanir í Python er að nota *for*-skipun. Hér er dæmi um Python-forrit sem reiknar og skrifar út önnur og þriðju veldi talnanna 1 til 5:

.. code-block:: python
   :caption: Veldatafla
   :name: veldatafla

   print(" k  k²   k³")
   print("–––––––––––")
   for k in range(1,6):
      print(f"{k:2} {k**2:3} {k**3:4}")

Þetta forrit kynnir fleira til sögunnar, t.d. svonefnda f-strengi til að stjórna sniði þess sem er prentað og virkjann :code:`**` sem gefur veldi.

.. Æfing
.. hint::
   Ýmsar vefsíður bjóða upp á keyrslu Python forrita, t.d. `ideone.com
   <http://ideone.com/l/python-3>`_ og `online-python.com
   <http://online-python.com/online_python_compiler>`_
   Afritið (eða sláið inn) forritið Veldatafla inn í aðra hvora af þessum síðum
   og keyrið það. Prófið að breyta forritinu (finnið t.d. fleiri veldi).

Collatz-runur
-------------
Collatz-runur eru reiknaðar þannig að byrjað er með einhverja tölu :math:`n_0`
og svo er næsta tala reiknuð aftur og aftur skv. 

.. math::
   n_{k+1} = \begin{cases}
      \displaystyle\frac{n_k}{2} \text{ ef $n_k$ er slétt tala}\\
      3n_k+1 \text{ ef $n_k$ er oddatala}
      \end{cases}

Ef nýja talan :math:`n_{k+1} = 1` þá er hætt.

Ef við byrjum t.d. með :math:`n_0=5` þá fæst runan 5, 16, 8, 4, 2, 1. Runurnar heita eftir þýska stærðfræðingnum Lothar Collatz (1910–1990) sem setti fram þá tilgátu árið 1937 að það sé sama hvaða :math:`n_0` er byrjað með, runan muni alltaf að lokum lenda í 1 og hætta. Enn hefur engum tekist að sanna tilgátuna, og reyndar virðast jafnvel færustu stærðfræðingar ekki hafa hugmynd um hvernig ætti að byrja.

Forrit fyrir Collatz-runur
--------------------------

Eftirfarandi Python forrit finnur og prentar út Collatz-runur sem byrja á 2, 3,..., 7:

.. code-block:: python
   :caption: Collatz
   :name: Collatz

   # COLLATZ ÆFING
   def næsta(x):
       '''skilar næstu tölu á eftir x í Collatz-runu'''
       if x % 2 == 0:
           f = x//2
       else:
           f = 3*x + 1
       return f

   def collatz_runa(n):
       '''finnur og skrifar út Collatz-runu sem byrjar á n'''
       print('runa: ', end='')
       while n > 1:
           print(n, end=', ')
           n = næsta(n)
       print(n)

   # Forrit sem prentar út Collatz-runur sem byrja á 2, 3,...,7:
   print('Nokkrar Collatz-runur')
   for n0 in range(2,8):
       collatz_runa(n0)

.. _icollatz:
   
Python atriði sem koma fyrir í forritinu Collatz
------------------------------------------------
- Ný föll má skilgreina með því að byrja á **def** og nöfn þeirra mega hafa
  íslenska stafi (og líka gríska). Á eftir *def*-línunni er hefð fyrir að setja
  *skjölunarstreng* innan þrefaldra gæsalapa. Nánar tiltekið er ritað:

    .. code:: python3

       def nafn(stiki1, stiki2... ):
          '''útskýring-á-hvað-fallið-gerir'''
          skilgreining-falls

- **Ef**-setning hefur ekki sviga utan um skilyrðið, öfugt við mörg forritunarmál (t.d. C og Java). Sniðið er svona:

    .. code:: python3

        if skilyrði:
            skipanir
        elif skilyrði:
            skipanir
        else:
            skipanir

  Það má líka sleppa eða hafa fleiri **elif** kafla og/eða sleppa **else** kafla. 

- **While**-lykkjur hafa snið

    .. code:: python3

       while skilyrði:
           skipanir

- **For**-lykkjur hafa snið

    .. code:: python3
       
       for k in range(b,e):
           skipanir

    k tekur þá gildi b, b+1,..., e–1. :code:`range(e)` jafngildir
    :code:`range(0,e)`, og svo má taka stærri skref: :code:`range(b,e,d)` hleypur
    í gegn um k = b, b + d, b + 2d,... og hættir ef k ≥ e.
           
- **Athugasemdir** (*comments*) byrja á #

- Virkinn `%` gefur **afgang** úr deilingu (*mod*)

- // gefur **heiltöludeilingu** (og ef útkoman er brot er hún lækkuð niður í átt að 0)

- Eins og í flestum forritunarmálum er "=" **gildisgjöf** (*assignment*) og "=="
  samanburður

- Föll sem **skila gildi** enda oftast á :code:`return gildi`

- **Inndráttur** er notaður til að sýna hvar blokkir enda (þ.e.a.s. blokkir sem *def*, *if*, *else*, *while* o.fl. skilgreina). Skipanir sem byrja slíkar blokkir enda alltaf á tvípunkti (þ.e.a.s. :)

- **Strengi** má búa til með því að setja einfaldar gæsalappir utan um þá, en líka má
  nota tvöfaldar, t.d. :code:`"strengur"`.

- Til að **kalla á fall** er notað :code:`nafn(viðföng)` (t.d. *næsta*, *collatz_runa* og innbyggða fallið
  *print*)

- Fallið **print** fer sjálfkrafa í næstu línu eftir prentun, nema ef viðbótin
  *end=...* er með.

Umhverfi fyrir Python: Jupyter og Colab
=======================================
Árið 2014 var byrjað á verkefni sem nefnist `Jupyter <http://jupyter.org>`_ (sbr. `Wikipediu <https://en.wikipedia.org/wiki/Project_Jupyter>`_) sem snýst um að búa til umhverfi þar sem blanda má saman lýsingu verkefna, stærðfræðiformúlum, forritum, og úttaki forrita í sama skjali eða vinnubók. Upphaflega var hægt að nota eitt af þremur forritunarmálum, Julia, Python og R, og af þeim er nafnið dregið, en síðan hafa bæst við fleiri mál. Hægt er að nota Jupyter vinnubækur á eigin tölvu, t.d. með því að setja upp hugbúnað sem nefnist *JupyterLab*, en það er líka hægt að búa þær til í vafra í kerfinu *Google Colaboratory* (oft stytt í Colab) sem keyrir `í skýinu <http://colab.research.google.com>`_. Þessar fyrirlestrarnótur miðast við að Jupyter-vinnubækur séu notaðar.

.. _colab:

Notkun Google Colab
-------------------
Google Colabatory er þjónusta hjá Google til að búa til og vinna með Jupyter
vinnubækur. Vinnubækurnar eru geymdar á Google Drive svæði notanda, og forritin
í þeim eru keyrð á sérstakri gervitölvu (*virtual machine*) sem Google leggur
til. Skrár sem sem forritin þurfa eða búa til eru geymdar á tímabundnu disksvæði
á þesari gervitölvu. Python-þýðandinn er nýlegur (nánar
tiltekið útgáfa 3.7.11 í ágúst 2021), helstu pakkar eru þegar uppsettir (m.a. þeir
sem nefndir eru í kafla :numref:`pakkar`), og auðvelt er að bæta við pökkum
eftir þörf.

Til að byrja á vinnubók á Colab þarf fyrst að stofna reikning hjá Google. Síðan má heimsækja `colab.research.google.com <http://colab.research.google.com>`_ og velja *File–New notebook*. Í reitinn sem birtist má slá inn Python-forrit, og svo má keyra forritið með því að smella á þríhyrningstáknið á vinstri brún reitsins eða með því að slá á ctrl/enter. Hægt er að bæta við textareitum og forritsreitum, vista vinnubókina, prenta hana o.s.frv. og eru helstu slíkar skipanir sýndar hér að neðan í kafla :numref:`jupyter-skipanir`.

.. attention:: Ef þið viljið ekki nota reikning hjá Google getið þið í staðinn sett upp Anaconda á eigin tölvu og notað JupyterLab, eins og lýst er að neðan í kafla :numref:`anaconda-uppsetning`.
               
.. Æfing
.. hint::
   
   a) Farið inn á Google Colab, afritið forritið :numref:`Collatz` (þ.e. Collatz)
      inn í keyrslureitinn og prófið að keyra hann.

   b) Bætið við textareit ofan við keyrslureitinn (ef smellt er á **+ Text** kemur
      textareitur fyrir neðan, sem hægt er að færa upp með því að smella á
      **uppörina** efst til hægri (**↑**). Setjið titil og smá skýringartexta inn í
      reitinn með því slá inn:

      .. code-block:: text

          # Forrit sem reiknar Collatz-runur
      
          $n_{k+1} = 3n_k + 1$ ef $n$ er oddatala<br>
          $n_{k+1} = \dfrac{n_k}{2}$ ef $n$ er slétt tala
      
          Ef nýja talan $n_{k+1} = 1$ þá er hætt að reikna.
          ***

   c) Búið til nýjan forritsreit neðst (með **+ Code**) og setjið þar eftirfarandi
      skipanir:

      .. code:: python3

         n0 = int(input("Sláið inn tölu til að byrja Collatz runu"))
         collatz_runa(n0)

      Keyrið reitinn og sláið inn 27 (sem gefur langa röð) og aðrar tölur ef vill.

   d) Búið til PDF-skjal úr vinnubókinni með því að velja **File**–*Print* og
      síðan *PDF–Save as PDF* eða *Microsoft Print to PDF* eða *PDF–Open in
      Preview* (eftir vafra/tölvu). Takið eftir að lárétta línan sem fæst með
      :code:`***` hjálpar til við að aðskilja textareitinn og forritsreitinn.
      
.. figure:: myndir/colab.jpg
   :align: center

   Google Colab viðmótið.

   Hér hefur verið smellt á hnappinn í græna hringnum til að fá efnisyfirlit.
   Aðrir hnappar sem nefndir eru í æfingunni að framan eru sýndir með rauðum hring.

.. _anaconda-uppsetning:
   
Uppsetning á Anaconda og JupyterLab
-----------------------------------
Athugið að þessum kafla má sleppa ef Google Colab er notað.

**Anaconda.** Auðveldasta leiðin til að setja upp bæði Python og Jupyter á eigin tölvu er að setja upp hugbúnaðarpakka sem nefnist Anaconda (sem er stærsta kyrkislanga í heimi, sbr. að Python er líka svoleiðis slanga). Með Anaconda fylgir nýlegur Python túlkur, Jupyter, meira en 1000 vinsælir Python-pakkar og ýmislegt fleira. Til að setja það upp þarf að heimsækja `anaconda.com <https://anaconda.com/>`_, velja *Products–Individual Edition*, hlaða niður 64 bita *Graphical Installer* fyrir ykkar stýrikerfi og fylgja leiðbeiningum.

.. figure:: myndir/anaconda.jpg
   :align: center
   :figwidth: 10cm

   Græn anaconda slanga
       
**Keyrsla JupyterLab.** Eftir uppsetningu Anaconda má smella á
"Anaconda-Navigator" appið og velja þar *JupyterLab*. Þá opnast JupyterLab í
glugga í aðalvafra tölvunnar. Heimamappa er sjálfgefin í fyrsta sinn, en næst
opnast JupyterLab á sama stað og síðast var hætt. JupyterLab-glugginn lítur
svona út:

.. figure:: myndir/jupyterlab.png
   :align: center

   JupyterLab-glugginn

Hér hefur verið byrjað í möppunni :code:`dropbox/strei` undir heimamöppu. Þarna eru tvær undirmöppur og fjórar skrár: tvær vinnubækur eða Jupyter-bækur (auðkenndar með .ipynb, en Jupyter hét áður IPython), eitt Python-forrit (auðkennt með .py) og ein pdf-skrá. Til að búa til nýja vinnubók er smellt á efri *Python 3*-hnappinn, og þá opnast bókin í nýjum flipa í vafranum. Hún heitir sjálfkrafa *Untitled2* en með því að hægri-smella á nafnið (eða smella á *File*) og velja *Rename notebook* má skíra hana einhverju skynsemlegra nafni. Eldri bók er opnuð með því að smella á hana í skráalistanum vinstra megin.

Vinnubækur
----------
Eins og fram kom í æfingunni í kafla :numref:`colab` innihalda vinnubækur **reiti** (*cells*) af tvennu tagi, **forritsreiti** (*code*), og **textareiti** (*markdown*). Í þeim fyrrnefndu eru Python-forrit eða forritsbútar, en í hinum eru fyrirsagnir og skýringartextar sniðnir með umbrotsmálinu (*markup language*) *Markdown*. Í textareitina er líka hægt að setja stærðfræðiformúlur sniðnar með formúlumálinu *LaTeX* og jafnvel myndir ef vill. Forritsbútana er hægt að keyra og fer úttak keyrslu inn í bókina, neðst í viðkomandi forritsreit. Segðin sem er neðst í hverjum reit skrifast sjálfkrafa út, en nota þarf print-fallið til að skrifa út niðurstöður framar í reitnum.

Það er sæmilega auðvelt að læra á notkun hvort sem er Colab eða JupyterLab með því að prófa sig áfram, en líka getur verið gagnlegt að skoða leiðbeiningar á netinu, sbr grein :numref:`jupyter-leiðbein-á-netinu`. Mikilvægustu skipanir beggja labbanna fylgja svo hér í næsta kafla.

.. _jupyter-skipanir:

Colab og JupyterLab skipanir
----------------------------

.. list-table:: Skráaskipanir
   :widths: auto
   :name: jupyterskráaskipanir
   :header-rows: 1

   * - Aðgerð
     - Colab skipun
     - JupyterLab skipun
       
   * - Skipta um nafn á vinnubók
     - Smella á nafnið efst t.v. 
     - ▸ Hægri-smella á nafnið efst t.v. og velja *Rename-Notebook* |br|
       ▸ File→Rename-Notebook

   * - Ná í eintak á eigin tölvu
     - File→Download
     - (þarf ekki)
       
   * - Vista undir nýju nafni
     - File→Save-a-copy-in-Drive og endurnefna afritið
     - File→Save-Notebook-As

   * - Vista
     - ▸ File→Save |br|
       ▸ ctrl/s (⌘s á Mac)
     - ▸ File→Save-Notebeook |br|
       ▸ ctrl/s (⌘s á Mac) |br|
       ▸ smellt á diskling

   * - Vista sem PDF
     - File→Print→Save-as-PDF
     - File→Export notebook as→HTML, opna HTML-skjal og velja File→Print þar.  

.. list-table:: Keyrsluskipanir
   :widths: auto
   :name: jupyterkeyrsluskipanir            
   :header-rows: 1

   * - Aðgerð
     - Colab skipun
     - JupyterLab skipun
       
   * - Keyra forritsreit
     - ▸ ctrl/enter |br|
       ▸ smella á "play"
     - ▸ ctrl/enter |br|
       ▸ smella á "play"

   * - Stoppa keyrslu
     - ▸ ctrl/m i |br|
       ▸ smella á "stop" |br|
       ▸ Runtime→Interrupt-execution
     - ▸ esc i i |br|
       ▸ smella á "stop" |br|
       ▸ Kernel→Interrupt-kernel

   * - Núllstilla Python
     - ▸ ctrl/m . |br|
       ▸ Runtime→Restart-runtime
     - ▸ esc 0 0 |br|
       ▸ Kernel→Restart-kernel

.. list-table:: Reitaskipanir
   :widths: auto
   :name: jupyterreitaskipanir            
   :header-rows: 1

   * - Aðgerð
     - Colab skipun
     - JupyterLab skipun
       
   * - Setja inn forritsreit
       neðan við virkan reit
     - ▸ smella á **+ Code** |br|
       ▸ esc b
     - ▸ smella á **+** |br|
       ▸ esc b

   * - Setja inn textareit neðan við virkan reit
     - ▸ smella á **+ Text** |br|
       ▸ esc b ctrl/m m
     - ▸ smella á **+** og svo Code → Markdown |br|
       ▸ esc b esc m

   * - Færa reit
     - smella á upp-ör/niur-ör efst t.h.
     - beita "Drag-and-drop" á reit

   * - Kljúfa reit
     - ctrl/m – |br|
     - ▸ ctrl/shift/– |br|
       ▸ Edit→Split-cell

   * - Sameina reiti
     - mála reiti → hægri smella → Merge-selected-cells
     - mála reiti → Edit → Merge-Selected-Cells

   * - Eyða reit
     - ▸ ctrl/m d |br|
       ▸ hægri-smella → Delete cell 
     - ▸ esc d d |br|
       ▸ hægri-smella → Delete cells

   * - Sýna textareit sem *markdown* (til að breyta)
     - ▸ tvísmella á reit |br|
       ▸ velja reit og slá á Enter
     - ▸ tvísmella á reit |br|
       ▸ velja reit og slá á Enter

   * - Sníða textareit
     - Velja einhvern annan reit
     - ▸ ctrl/enter |br|
       ▸ smella á "play"

   * - Afturkalla ("undo") reitaskipun
     - ▸ Edit→Undo ... |br|
       ▸ ctrl/m z
     - ▸ Edit→Undo-Cell-Operation |br|
       ▸ esc z

   * - Endurtaka ("redo") reitaskipun
     - Edit→Redo ...
     - Edit→Redo-Cell-Operation

.. list-table:: Ritilskipanir
   :widths: auto
   :name: jupyterritilskipanir
   :header-rows: 1

   * - Aðgerð
     - Colab/JupyterLab skipun
       
   * - Færa bendil
     - ▸ örvar |br|
       ▸ Home, End (Fn/←, Fn/→ á Mac) |br|
       ▸ PgUp, PgDn (Fn/↑, Fn/↓)
   * - Eyða
     - Backspace, Del (Fn/Bcksp)
   * - Velja, klippa, afrita, líma
     - ▸ mála með mús |br|
       ▸ shift/örvar |br|
       ▸ ctrl/xcv (⌘/xcv á Mac)     - 
   * - Velja allt í reit
     - ctrl/a (⌘/a)
   * - Flytja til hægri, vinstri (indent, unindent)
     - tab, shift/tab
   * - Afturkalla ("undo")
     - ctrl/z (⌘/z)
   * - Endurtaka ("redo")
     - ctrl/shift/z (⌘/shift/z)
       
Vistun vinnubóka á PDF-sniði
----------------------------
**Colab.** Veljið *File → Print*, eða sláið á ctrl/p eða ⌘/p (Mac), og svo
*Destination → Save-as-PDF* (*PDF → Save-as-PDF* á Mac). Þá birtist gluggi þar
sem velja má möppu og nafn fyrir PDF-skjalið.

.. danger::
   Í Safari virðist stundum þurfa að velja *File → Print* í vafranum en ekki í
   Colab-flipanum, en í Chrome virðist ekki skipta máli hvoru megin *File → Print*
   er valið.

**JupyterLab.** Í JupyterLab er lús þannig að með *File → Print* vistast stærðfræðiformúlur ekki rétt. Það þarf að fara krókaleið og velja fyrst *File → Export notebook as → HTML* og svo þarf að opna HTML-skjalið sem verður til og vista það í PDF með *File → Print*.
PDF.

Markdown og Latex
-----------------

Finna má ýmsar leiðbeiningar um *Markdown*-málið á netinu, sbr. grein :numref:`jupyter-leiðbein-á-netinu`). Þar er
útskýrt hvernig búa má til fyrirsagnir (með #, ##, ###), skáletra og feitletra
(með \*texti\* og \*\*texti\*\*), búa til lista, setja inn myndir (þær er hægt
að líma inn eða draga inn með músinni), setja láréttar línur og ýmislegt fleira.

Texti sem er inndreginn um a.m.k. fjögur bil birtist óbreyttur með jafnbilaletri (*monospaced font*).

.. sidebar:: Dæmi um töflu
   
   .. figure:: myndir/töfludæmi.png
      :align: center
      :width: 5cm

Til að búa til töflu má nota lóðrétt strik til að afmarka dálka og : til að tilgreina
vinstri/hægri jöfnun eða miðjun. Hér er einfalt dæmi:

.. code-block:: text
          
   nr |nafn    |aldur
   ---|:------:|----:
   1  |Ari     | 9
   2  |Bryndís | 11
   ...
   105|Örn     |8
   
Stærðfræðiformúlur eru með LaTeX-sniði og settar inn með $ *formúla* $ eða

   | \$\$
   | *formúla*
   | \$\$

LaTeX getur búið til gríska stafi og allskyns stærðfræðitákn, það setur
sjálfkrafa skáletur á breytur og hæfileg bil á milli einstakra hluta í formúlum.
`Wikibókin um LaTeX-stærðfræði
<https://en.wikibooks.org/wiki/LaTeX/Mathematics>`_ er sæmilega ítarleg, og svo
má finna fjölmarga styttri hjálpartexta, t.d. `þennan
<https://davidhamann.de/2017/06/12/latex-cheat-sheet>`_ eftir David Chapman.
Fallegasti stærðfræðitextinn fæst með því að setja dollaramerki utan um alla
stærðfræði, hvort sem það eru flóknar formúlur eða bara ":math:`x=3`" og
":math:`a` og :math:`b` eru vigrar" (sem sé :code:`$x=3$` og :code:`$a$ og $b$
eru vigrar`) en ekki "x=3" og "a og b eru vigrar".



.. _jupyter-leiðbein-á-netinu:

Colab- og JupyterLab-leiðbeiningar á netinu
-------------------------------------------

Hægt er að finna ýmsar vefsíður með leiðbeiningum um Google Colab og JupyterLab, t.d.:

    - `Google Colab yfirlit <https://colab.research.google.com/notebooks/basic_features_overview.ipynb>`_
    - `Markdown fyrir Colab <https://colab.research.google.com/notebooks/markdown_guide.ipynb>`_
    - `Nokkuð ítarlegar Colab leiðbeiningar hjá Tutorialspoint <https://www.tutorialspoint.com/google_colab/google_colab_quick_guide.htm>`_
    - `Stuttar JupiterLab leiðbeiningar <http://www.rpgroup.caltech.edu/ncbs_pboc/code/t0b_jupyter_notebooks.html>`_
    - `Working efficiently with JupyterLab Notebooks <https://florianwilhelm.info/2018/11/working_efficiently_with_jupyter_lab>`_

(fyrstu tvær eru frá Google sjálfum).
      
.. _jupyter-æfing:
      
.. Æfing
.. hint::
   
   Vinnubókin `kynning.ipynb
   <https://colab.research.google.com/drive/1H-x6BX7OhkTRVj3YHH5_2mSOtJEnA9l8?usp=sharing>`_
   byrjar á tveimur æfingum í notkun Google Colab. Ef smellt er á hana opnast
   hún hjá Google Drive og hægt er að velja *Copy-to-Drive* (eða *File→Download*
   til að nota JupyterLab). Þá lendir skráin sjálfkrafa í möppu sem heitir
   *Colab Notebooks* og þar er hægt að breyta henni og vista breytingar.
   Náið í þessa skrá og leysið tvær fyrstu æfingarnar, A og B.

.. _grunn-python:
   
Grunnatriði Python
==================

Breytur og tög
--------------
**Breyta** (*variable*) er nafn á minnishólfi í tölvu, þar sem geyma má **gildi** (*value*). Gildin geta svo verið af ýmsu tagi, eða haft ýmis **tög** (*types*), og eins og fyrr segir eru þessi tög tengd gildunum en ekki breytunum sjálfum. Fyrir utan gildi sem geymd eru í breytum er líka talað um gildi sem útkomu úr **útreikningi** (*computation*) eða **segð** (*expression*), t.d. hefur segðin :math:`2 + 2` gildið :math:`4`. Ósamsett gildi, t.d. 2, heitir **fasti** (*constant*).

Grunntögin í Python og dæmi um fasta af hverju tagi eru:

    - *kommutala (float)* t.d. :code:`2.0`, :code:`-543.62`, :code:`16e-22`
    - *heiltala (int)*	 t.d. :code:`2`, :code:`123456789012345678901234567890`,
      :code:`round(1e100)`; engin takmörk á stærð
    - *strengur (str)*	 t.d. :code:`'abc'`, :code:`"strengur með bili"`;
      nota má hvort sem maður vill :code:`"` eða :code:`'`
    - *rökgildi (bool)* , :code:`True` og :code:`False`
    - *"EkkertTag" (NoneType)*, :code:`None` sérstakt tag sem fæst m.a. úr
      föllum sem engu skila.

Önnur algengustu innbyggð tög eru (sjá kafla :numref:`söfn`) eru:

    - *Listar (list)*
    - *Samantektir (tuple)*
    - *Mengi (set)*
    - *Ítrarar (iterator)*
    - *Uppflettitöflur (dictionary)*
      
Loks gildir sú regla að nafn breytu skal vera runa af bókstöfum, tölustöfum, og _, hún má ekki byrja á tölu og hún má ekki vera lykilorð í málinu eins og "for" eða "return". Í sumum forritunarmálum verða bókstafirnir að vera enskir, en sú takmörkun á ekki við um Python, Dæmi um lögleg breytunöfn eru: x_1, hæð, ∆.

Í nútímaforritum er algengt að nota fremur löng og lýsandi breytunöfn, t.d. :code:`radíus_hrings`. Sú regla er oft brotin í inngangsnámskeiðum í forritun, því þar þvælast löng nöfn frekar fyrir en að hjálpa til, og dæmigert væri að nota :code:`r` fyrir geisla hrings.

Aðgerðir og virkjar
-------------------
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

**Yfirlit.** Hér er yfirlit yfir helstu virkja fyrir grunntögin í Python:

.. code-block:: text

   + – * /          # eins og í flestum öðrum forritunarmálum
   %                # x % y er afgangur úr deilingunni x//y (7%4 gefur 3)
   **               # veldi (x**y táknar x í veldinu y)
   //               # heiltöludeiling (aukastafir skornir af; 7//4 gefur 1)
   < > <= >= == !=  # samanburðarvirkar, eins og í Java eða C
   and or not       # rökvirkjar
   << >> & ~ ^      # bitavirkjar, eins og í C, ~ er fyllitala og ^ er xor
   str + str        # samskeyting strengja ("ab" + "12" gefur "ab12")
   str*n            # fjölföldun strengs ("ab"*3 er "ababab")
   (...)            # svigar stýra röð útreiknings

**Útkoma úr blönduðum útreikningi.** Grunnreglan um útkomu úr aðgerð með tveimur tölum er að ef önnur eða báðar eru kommutala þá er niðurstaðan kommutala, en ef báðar eru heiltölur kemur út heiltala. Aðalundantekningin er deiling, en deiling tveggja heiltalna með /-virkja gefur kommutölu.

Bent skal á að hér eru orðin heiltala og kommutala notuð í tölvufræðilegri merkingu, sem sé að viðkomandi gildi séu af heiltölu- eða kommutölutagi. Tölvur greina nefnilega á milli heiltölnnar 2 og kommutölunnar 2.0, þær eru af mismunandi tagi og geymdar með mismunandi bitarunum í minni tölvunnar.

**Forgangsröð aðgerða.** Eftirfarandi tafla sýnir röð sem aðgerðir eru framkvæmdar í ef svigar segja ekki til um aðra röð:

.. code:: text

   **             # frá hægri til vinstri, 4**3**2 = 4**(3**2) = 262144
   *, /, // og %  # frá vinstri til hægri; x/y*z jafngildir (x/y)*z
   + og –         # frá v til h; a - b*c + d jafngildir (a - (b*c)) + d
   samanburður    # frá v til h; x < y < z jafngildir x < y og y < z
   not            # ath. að not x < y jafngildir not (x < y)
   and           
   or

.. _gildisgjöf:
   
Gildisgjöf
----------
Í stærðfræði er **gildisgjöf** (*assignment*) stundum táknuð með virkjanum :math:`:=` (t.d. :math:`x := 1`), og í reikniritum er stundum notuð ör (:math:`x \gets 1`), og þá er einfalt jafnaðarmerki notað til að segja að tvær stærðir séu jafnar eða kanna hvort þær séu jafnar: ":math:`x = 1`" þýðir að breytan :math:`x` (sem þegar hefur verið skilgreind) hafi gildið 1, og "ef :math:`x = 1`, þá..." spyr hvort :math:`x` sé 1. Í forritunarmálum er hinsvegar orðið mjög algengt að nota einfalt jafnaðarmerki fyrir gildisgjöf og tvö í röð fyrir samanburðarvirkjann `==` og Python er engin undantekning frá þeirri venju.

Gildisgjöf í Python er tvennskonar, hægt er að gefa breytu gildi og svo er líka hægt að uppfæra gildið sem breyta geymir, sem sé:

   .. code:: python

      breyta = segð   # t.d. a = x + 3
      breyta += segð  # leggur segð við breytu, t.d. er a += 3 jafngilt a = a + 3
      breyta -= segð  # dregur frá; líka má *=, /= o.s.frv.

Það eru síðan nokkrir fleiri möguleikar sem verða útskýrðir betur í næstu köflum: Viðtakandi gildisins má vera stak í lista (t.d. :code:`L[i]`) eða eiginleiki í hlut (:code:`punktur.x`). Svo er líka hægt að gefa mörgum breytum gildi samtímis með því að skrifa:

   .. code:: python

      breyta, breyta... = runa    # lengd runu þarf að vera jafn fjölda breyta
      (breyta, breyta...) = runa  # annar möguleiki
      (x,y) = (y,x)               # þessi skipun skiptir á gildum x og y
      
.. _útprentun:      
      
Útprentun og innlestur
----------------------
Aðalaðferðin til að prenta út gildi í Python er að nota :code:`print`-fallið en í vinnubókum er líka hægt að nota fallið :code:`display`, sem gefur stundum öðruvísi úttak, t.d. ef prentaðir eru strengir eða nöfn taga og falla (sjá næstu æfingu). Sumir pakkar sem þið gætuð átt eftir að kynnast, t.d. pandas og statmodels, skila stundum HTML-sniðnum töflum, og til að birta þær þarf að nota :code:`display`.

    - :code:`print(segð,segð...)`: Prentar segðirnar með bilum á milli
    - :code:`print(..., sep=",")`: Prentar með kommum á milli
    - :code:`print(..., end=" ")`: Endar með bili í stað nýrrar línu |br|
      Sjá mörg dæmi um print að framan og í sýnidæminu í grein :numref:`stýriskipanir`.
    - :code:`s = input('texti')`: Prentar textann og bíður eftir að notandi
      slái inn streng og <Enter>; innslegið gildi → s.

Næsta grein (:numref:`fstrengir`) útskýrir svo hvernig **sníða** (*formatera*) má útprentuð gildi með svonefndum f-strengjum.

    .. Æfing
    .. hint::
       
       a. Input-fallið skilar streng s, sem hægt er að breyta í tölu með
          :code:`t = float(s)` eða :code:`k = int(x)`. Afritið eftirfarandi
          skipanir yfir í Colab. Notið tækifærið og prófið Colab-skipanirnar
          til að velja allt í reit og flytja það til vinstri (shift/tab,
          *unindent*), sbr. :numref:`jupyterritilskipanir`. Keyrið, sláið inn
          tölu, og prófið líka að slá inn eitthvað annað en tölu.
      
          .. code:: python3

             s = input('Sláðu inn tölu: ')
             t = float(s)
             print(t)

       b. Afritið eftirfarandi forritsbút yfir í Colab. Keyrið, og prófið svo
          að nota :code:`end=";"` og :code:`sep=","` og prófið líka að breyta
          print í display.

          .. code:: python3

             x = 2
             s = "AB"
             print(x, s)
             print(x*2, s*2)

.. _fstrengir:

F-strengir
----------

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
     - Heiltala og strengur skrifast óbreytt og kommutala með jafnmörgum
       aukastöfum og þarf til að sýna nákvæmt gildi hennar.

   * - :code:`{heiltala:n}` |br|
       :code:`{strengur:n}`
     - Skrifað í n stafa breitt svið, tölur hægri-jafnaðar og strengir
       vinstri-jafnaðir

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
     - Skrifa kommutölu með m stöfum fyrir aftan kommu

   * - :code:`{kommutala:n.mf}`
     - Skrifa kommutölu með m stöfum fyrir aftan kommu í n stafa breitt
       svið

Tilgangurinn með að gefa heildarfjölda stafa (breidd sviðs) getur t.d. verið að
láta dálka í töflu standast á: forritið í sýnidæminu í grein :numref:`stýriskipanir`
notar f-strengi til að sníða (*"formatera"*) litla töflu. Hér eru þrjú dæmi í
viðbót:

    .. code:: python3

       f'hæð = {h}, breidd = {x*y}'
       f"A = {A:.3f}, B = {B:.2f}"
       f'Halló {nafn} og vertu velkomin(n)'

þar sem gert er ráð fyrir að h, x og y séu heiltölubreytur, A og B séu
kommutölubreytur og nafn sé strengjabreyta.
       
.. danger::
   F-strengir eru nýleg viðbót við Python, þeir komu í Python 3.6 í desember
   2016. Í eldri Python-útgáfum er hægt að nota %-virkja. Forritið í sýnidæminu
   í grein :numref:`stýriskipanir` gæti t.d. haft: |br|
   |sp3| |sp3| :code:`print('%d   %.4f   %2d' % (x, math.sqrt(x), x**2))` |br|
   í öftustu línunni.
   
Föll notanda (ný föll)
----------------------

**Skilgreining falls**

    .. code:: python3

       def fall(stiki, stiki...):
           '''skjölunarstrengur'''
           skipanir
           return g
           
       # Skjölunarstrengurinn er valkvæður en góð regla að hafa hann með
       # Ef fallið skilar mörgum gildum endar það á: return (g1,g2...)
       # Ef það skilar engu er return-skipun sleppt
           
**Kallað á fall**

    :code:`g = fall(viðfang, viðfang...)` |br|
    Má líka nota í segð: :code:`h = 2*fall(viðföng) + 1` |br|
    Ef fallið skilar engu: :code:`fall(viðföng)` |br|
    Ef fallið skilar mörgum gildum: :code:`(g1,g2...) = fall(viðföng)` |br|
    Líka má sleppa svigunum: :code:`g1,g2... = fall(viðföng)` |br|

**Viðföng og stikar.**

    Breyturnar innan sviga á eftir fallsnafninu þar sem það er skilgreint kallast **stikar** (*parameters*), en þegar kallað er á fallið þá heita gildin sem sett eru í sviga á eftir fallsnafninu **viðföng** (*arguments*). Þau þurfa ekki að vera breytur en mega vera hvaða segðir sem er. **Viðfang** er sem sé gildi sem sent er inn í fall, en **stiki** er breyta í skilgreiningu fallsins sem tekur við gildinu.

.. _mikilvægustu-innbyggð:

Mikilvægustu innbyggð föll
--------------------------

**Almenn föll**

    .. table::
        :widths: auto
        :name: tab:almenn-föll

        +-----+------------------------------------------+
        |abs  |tölugildi, abs(-3) → 3                    |
        +-----+------------------------------------------+
        |max  |hámark: max(1,2) → 2                      |
        +-----+------------------------------------------+
        |min  |lágmark: min(1,2) → 1                     |
        +-----+------------------------------------------+
        |int  |kommutala → heiltala, strengur → heiltala |
        +-----+------------------------------------------+
        |float|heiltala → kommutala, strengur → kommutala|
        +-----+------------------------------------------+
        |range|sjá grein :numref:`icollatz`              |
        +-----+------------------------------------------+
        |len  |lengd strengs                             |
        +-----+------------------------------------------+
        |type |tag breytu                                |
        +-----+------------------------------------------+

    .. Æfing
    .. hint::
       a) Opnið vinnubók og prófið öll þessi föll. Látið t.d. x = –3,
          y = 2.7, s = \"abc\" og finnið \|x\|, max(x,y), min(x,y), float(x),
          int(y), range(4), len(s) og type(s).
          
       b) Skoðið muninn á því sem :code:`print(type(s))` og :code:`display(type(s)` birta.

**Helstu stærðfræðiföll og fastar**

    :code:`sin, cos, tan, asin, acos, atan, atan2`: Hornaföll í radíönum |br| 
    :code:`exp, log, log2, log10, sqrt`: Vísisfall, lograr og kvaðratrót |br|
    :code:`pi, e, inf, nan`: (stærðfræði)fastar |br|
    :code:`radians, degrees`: breytt úr gráðum í radíana og öfugt |br| 
    Ef nota á sin, cos og pi (til dæmis) má rita fremst: |br|
    |sp3| :code:`from math import sin, cos, pi`, eða: |br|
    |sp3| :code:`import math` og svo :code:`math.sin`, :code:`math.cos`... |br|
    Sjá nánar í `Python hjálpinni
    <https://docs.python.org/3/library/math.html>`_, |sp2| og greinar
    :numref:`stýriskipanir` og :numref:`polhnit`.

    .. Æfing
    .. hint::
              
       .. figure:: myndir/gormakerfi.png
                   :align: center
                   :figwidth: 10cm

       **Sveiflutími gorms**: Á myndinni er gormakerfi: Hlutur með massa
       :math:`m` hvílir á fleti án núningsmótstöðu og er festur við veggina með
       gormum með stífnifasta :math:`k_1` og :math:`k_2`. Eiginsveiflutími
       kerfisins verður

       .. math::
          T = 2\pi\sqrt{\frac{m}{k_1+k_2}}

       a) Skrifið fall :code:`sveifla(m,k1,k2)` sem reiknar sveiflutímann.

       b) Skrifið forrit prófar fallið með m = 2, k1 = 3 og k2 = 4, og skrifar
          út sveiflutímann á sniðinu `T = x.xxx` (með f-streng).

Fallbreytur
-----------
Breytur geta tekið gildi sem eru föll: :code:`def fall: ...` og neðar: :code:`x = fall` eins og eftirfarandi dæmi sýnir.


   .. admonition:: Sýnidæmi
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

.. _stýriskipanir:
      
Stýriskipanir
-------------

- :code:`if-elif-else`: sjá grein :numref:`icollatz`
- :code:`while`: sjá grein :numref:`icollatz`
- :code:`for-in`: sjá grein :numref:`icollatz`
- :code:`continue`: fara í næstu umferð lykkju (for- eða while-)
- :code:`break`: brjótast út úr lykkju

.. Sýnidæmi
.. important::

   **Rætur og veldi.** Eftirfarandi forrit reiknar kvaðratrætur og önnur veldi
   talnanna 2, 3, 4 og 5. Það sýnir notkun á nokkrum atriðum sem fjallað hefur
   verið um hér á undan.

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

.. Æfing
.. hint ::

    Sláið forritið í sýnidæminu hér á undan inn í vinnubók (eða
    afritið það). Prófið svo að breyta forritinu með því að:

      a) Sleppa 2, í range kallinu
      b) Nota :code:`for x in range(0,8,2)`
      c) Láta n = 3 (á undan for-lykkjunni) og breyta .4f í .{n}f

    (Ath. að nota má V, |sp| ^2 og - í stað *unicode* táknanna √, |sp| ² og
    ― ef maður vill)       

Skilyrt gildi
-------------
Skipunin:

  .. code:: python3

     x = segð1 if skilyrði else segð2          

jafngildir:

  .. code:: python3

     if skilyrði:
        x = segð1
     else
        x = segð2

Þetta jafngildir skipuninni ``x = skilyrði ? segð1 : segð2`` í Java eða C.
Til dæmis mætti reikna tölugildi með ``a = -x if x < 0 else x``.
      
.. Æfing
.. hint::

   Í vinnubókinni :ref:`kynning.ipynb<jupyter-æfing>` sem náð var í í Æfingu
   aftan við kafla :numref:`jupyter-leiðbein-á-netinu` er hægt að prófa mörg af
   þeim Python-atriðum sem lýst hefur verið í þessum kafla og æfa sig í þeim.
   Opnið þessa bók í Colab og fylgið leiðbeiningum í henni.
