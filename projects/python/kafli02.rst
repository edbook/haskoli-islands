.. include:: rst-include

.. _dæmi-um-forrit:
             
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

.. admonition:: Æfing: Veldatöfluforrit prófað
   :class: aefing

   Ýmsar vefsíður bjóða upp á keyrslu Python forrita, t.d. `ideone.com
   <https://ideone.com/l/python-3>`_ og `online-python.com
   <https://online-python.com/online_python_compiler>`_
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

.. _collatzforrit:

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
  annaðhvort **athugasemd** (*comment*) sem byrjar á :code:`#` eða
  **skjölunarstreng** (*doc-string*) innan þrefaldra gæsalappa,
  sem lýsir því hvað fallið gerir. Nánar tiltekið er ritað:

    .. code:: python3

       def nafn(stiki1, stiki2... ):    eða:  def nafn(stiki1, stiki2... ):      
          # lýsing-á-hvað-fallið-gerir           '''lýsing-á-hvað-fallið-gerir'''
          skilgreining-falls                     skilgreining-falls              

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
