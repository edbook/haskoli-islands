.. include:: rst-include

Pandas
------
Pandas er pakki fyrir gagnameðhöndlun og gagnagreiningu í Python. Með Pandas er auðvelt að lesa stórar gagnaskrár, bæði textaskrár og töflureikniskrár (t.d. úr Excel eða Google sheets) og flokka gögnin á ýmsa vegu, velja hlutgögn (línur eða dálka), gera ýmsa útreikninga, og skrifa niðurstöðuna, annaðhvort í venjulegt úttak (í vinnubók/á skjá) eða í nýja skrá. Það er líka hægt að búa til NumPy-fylki úr Pandas-töflum og nota Matplotlib til að birta niðurstöður grafískt. Dæmigerðar Pandas-aðgerðir eru oft framkvæmdar í töflureikni, en það hefur ýmsa kosti að gera þær í forriti, t.d. ef maður vill framkvæma samsskonar reikninga aftur og til þess er Pandas pakkinn tilvalinn.

Á netinu má finna `10 mín. leiðbeiningar <https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html>`_, `svindlblað <https://assets.datacamp.com/blog_assets/PandasPythonForDataScience.pdf>`_ og annað `slíkt <https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf>`_. Það síðara er e.t.v. heldur vandaðra.

.. _pandas-gögn:

Pandas gögn
~~~~~~~~~~~
Pandas-pakkinn er skv. hefð fluttur inn með

    :code:`import pandas as pd`

Aðalgagnatögin í Pandas eru pd.Series (*runa*] sem er einvíð runa gagna, og
pd.DataFrame (*gagnatafla*) sem er tvívíð tafla. Tvennt greinir Pandas frá
NumPy: Í fyrsta lagi hafa stökin í rununum og línur og dálkar taflanna auðkenni
eða nöfn, og í öðru lagi geta dálkar taflanna verið af mismunandi tagi, einn
dálkur gæti t.d. geymt strengi, annar heiltölur og sá þriðji kommutölur.

Venjulega er vísað í einstaka dálka og línur eftir nöfnum þeirra, en það er líka
hægt að vísa í þær eftir númeri (sem sé hvar þær eru í röðinni). Sama gildir um
hluttöflur. :numref:`Tafla %s <helstu-pandas-skipanir>` sýnir skipanir fyrir
báðar aðferðirnar.

.. admonition:: Athugasemd
   :class: athugid

   Í opinberri Pandas-hjálp eru auðkenni eða nöfn á línum og dálkum kölluð
   *labels*, og línurnar stundum kallaðar *index*.

.. Sýnidæmi
.. important::   

   Á vef hagstofunnar er hægt að hlaða niður allskonar talnaefni, m.a.
   kosningaúrslitum. Skráin :h:`<a href="https://cs.hi.is/python/kosningar.xlsx"
   download="kosningar.xlsx"><b>cs.hi.is/python/kosningar.xlsx</b></a>` sem er
   fengin þaðan geymir úrslit alþingiskosninga 2017. Skráin hefur fjóra dálka:
   **stafur**, **flokkur**, **atkvæði** og **þingsæti** (*stafur* er
   listabókstafur). Smellið gjarna á þessa skrá og skoðið hana í Excel.

   Hér er svo forritsbútur sem les skrána, og birtir hana, reiknar heildarfjölda
   atkvæða, bætir við dálki með hlutfalli atkvæðanna sem hver flokkur fékk, og
   birtir loks þessa auknu töflu::
 
     import pandas as pd
     kosn = pd.read_excel("http://cs.hi.is/python/kosningar.xlsx")
     display(kosn)
     n = sum(kosn["Atkvæði"])
     kosn["Hlutf"] = kosn["Atkvæði"]/n
     display(kosn)

   Breytan kosn er *gagnatafla* af taginu ``pd.DataFrame``. Hér fylgir byrjunin á
   töflunni sem birtist:

   .. figure:: myndir/atkvæði1.png
      :align: center
      :figwidth: 13cm

.. Æfing
.. hint::

   Afritið Sýnidæmið yfir í vinnubók og keyrið það. Prófið að nota print í
   stað display. Bætið svo við samtals-línu með:

   .. code:: python
             
       kosn.loc["Samtals"] = kosn.sum()
       kosn.loc["Samtals", "Stafur"] = ""
       kosn.loc["Samtals", "Flokkur"] = ""

   (seinni tvær línurnar eru tilkomnar vegna þess að það á ekki að leggja saman
   stafina og listana). Bætið líka við dálki "Atkv-sætis" með atkvæði á bak við
   hvert þingsæti með því að deila í atkvæðin með þingsætunum. Loks er hægt að
   birta hlutfallið sem prósentu og einum aukastaf, og aftasta dálkinn án
   aukastafa með skipununum:

   .. code:: python
             
      birt = kosn.style.format({"Hlutf": "{:.1%}", "Atkv-sætis": "{:.0f}"})
      display(birt)

   (í innri slaufusvigunum eru snið líkt og í f-strengjum).

Í sýnidæminu og æfingunni sést að sjálfgefin auðkenni línanna eru einfaldlega
tölurnar 0–10, en dálkarnir fá nöfn úr hauslínu Excel-skrárinnar. Með
``display`` prentast taflan út HTML-sniðin, en með ``print`` fæst hún með
textasniði.

Við sjáum líka að vísað er í dálk töflu eins og í gildi í uppflettitöflu
(*dictionary*), með vísi sem er nafn dálksins innan hornklofa, en með því að
nota `.loc` er í staðinn vísað í línu, og þá er líka hægt að vísa í einstakt
stak eða reit í töflunni eins og í NumPy fylki með
``gagnatafla.loc[lína,dálkur]``. Tökum líka eftir að reikniaðgerð (hér deiling)
verkar á öll stök dálks í einu, eins og í NumPy.

Smíði gagnatafla
~~~~~~~~~~~~~~~~
Í stað þess að lesa gagnatöflur úr skrám eins og gert er í kaflanum hér á undan
er hægt að búa þær til úr breytum sem þegar eru fyrir hendi, hvort sem er
uppflettitöflum, listum eða NumPy-fylkjum. Til þess er hægt að nota
gagnatöflusmiðinn (-constructor) ``pd.DataFrame``. Einfallt kall á hann er:

.. code::
   
   df = pd.DataFrame(data)
          
þar sem ``data`` getur verið *NumPy-fylki*, *listi af listum* eða
*uppflettitafla*. Í tveimur fyrri tilvikunum fá dálkarnir nöfn 0, 1, 2,... en
með uppflettitöflu gefa lyklar hennar nöfn dálkanna. Þegar ``data`` er listi af
listum verður hver innri listi lína í gagnatöflunni, en ef það er uppflettitafla
með gildi sem eru listar lenda þeir í dálkum gagnatöflunnar. Svo er hægt að bæta
viðbótarstikum við kallið á ``DataFrame``, t.d. ``columns=["D1", "D2"]`` til að
gefa dálkunum nöfn og ``index=[1,2,3]`` til að gefa línunum nöfn (auðkenni).

Þegar gagnatafla er búin til úr NumPy-fylki með ``df = pd.DataFrame(A)`` er
fylkið ekki afritað heldur geymir taflan tilvísun í fylkið, sbr. athugasemd í
kafla :numref:`stök fylkis, línur og dálkar`. Til að taka í staðinn afrit má
nota kallið

    ``df = pd.DataFrame(A, copy=True)``

.. admonition:: Sýnidæmi: 
   :class: synidaemi

   Skipanirnar:
   
   .. code:: python

      T = {"nafn": ["Ari", "Ása"], "aldur":[12,18]}
      rng = np.random.default_rng(seed=42)
      A = rng.random(size=(2,3))
      df = pd.DataFrame(T)
      slembi = pd.DataFrame(A, columns=["A", "B", "C"])
      print(df)
      print(slembi)

   prenta út:

   .. code:: text
   
      nafn  aldur
    0  Ari     12
    1  Ása     18
              A         B         C
    0  0.773956  0.438878  0.858598
    1  0.697368  0.094177  0.975622



Helstu Pandas-skipanir
~~~~~~~~~~~~~~~~~~~~~~
Hér fylgja töflur yfir nokkrar helstu Pandas-skipanirnar. Þær eru hvergi nærri
tæmandi, en í staðinn vísast í *svindlblöðin* sem nefnd eru hér fremst í
:ref:`innganginum <Pandas>`. Í töflunum stendur ``df.`` fyrir gagnatöflu
(*DataFrame*) og ``s.`` fyrir runu (*Series*), sem sé stakan dálk eða línu.


.. list-table:: DataFrame smiðurinn
   :widths: auto
   :name: dataframe-smiðurinn

   * - ``df = pd.DataFrame(uppflettitafla)``
     - Býr til {"col1":[1,2,3], col2
          
.. list-table:: Skipanir til að ná í dálka, línur og hluttöflur
   :widths: auto
   :name: helstu-pandas-skipanir

   * - ``df["nafn"]``                    
     - Vísað í dálk ``"nafn"`` (skilar runu (*Sequence*))

   * - ``df.iloc[:,2]``
     - Dálkur númer 2 (runa)

   * - ``df.loc[3]``                  
     - Lína með auðkenni 3 (runa)

   * - ``df.loc["Samtals"]``
     - Lína með auðkenni ``"Samtals"`` (runa) |br|
       (auðkenni geta verið heiltölur eða strengir)

   * - ``df.iloc[3]``
     - Lína númer 3 (runa)

   * - ``df.loc[[2,4,5]]``
     - Línur auðkenndar 2, 4 og 5 (hluttafla)

   * - ``df.iloc[3:6]``
     - Línur númer 3, 4 og 5 (hluttafla)

   * - ``df[["A", "B", "D"]]``
     - Dálkar A, B og D (hluttafla)

   * - ``df.loc[(3,4,5), "A":"C"]``
     - Línur auðkenndar 3, 4 og 5, dálkar frá A t.o.m. C

   * - ``df.loc[3,"nfn"]``              
     - Vísað í tiltekinn reit

   * - ``df[df["A"] > 0]``              
     - Velja línur þar sem dálkur ``A`` er jákvæður

.. list-table:: Skipanir til að lesa og skrifa skrár
   :widths: auto
   :name: pandas-innlestur

   * - ``df = pd.read_excel(excelskrá)``  
     - Lesa fremsta vinnublað (*sheet*) inn í df

   * - ``df = pd.read_excel(excelskrá,s)``
     - Lesa vinnublað s inn í df (s má vera nafn eða nr.)

   * - ``df = pd.read_excel(…,dtype=str)``
     - Lesa alla dálka sem strengi

   * - ``df.to_excel(excelskrá)``        
     - Skrifa í Excelskrá

   * - ``df = pd.read_csv(skrá)``
     - Lesa töflu ``df`` úr skrá með kommum milli dálka, |br|
       efsta lína fyrirsögn með dálkanöfnum

   * - ``df = pd.read_csv(skrá,`` |br| |sp3| ``sep=";")``
     - Dálkar aðskildir með ``;``

   * - ``df = pd.read_csv(skrá,`` |br| |sp3| ``names=["d1","d2"...])``
     - Lesa kommuaðskilda skrá (þmt 1. línu), |br|
       dálkanöfn úr ``names``

   * - ``df = pd.read_csv(skrá,`` |br| |sp3| ``index_col=2)``
     - Lesa kommuaðskilda skrá, línuauðkenni úr dálki 2

   * - ``df = pd.read_csv(skrá,`` |br| |sp3| ``delim_whitespace=True)``
     - Lesa skrá með bilum á milli dálka

   * - ``df = pd.read_fwf(skrá)``
     - Lesa skrá með fastri dálkabreidd. Breidd dálka er |br|
       fundin sjálfkrafa út með því að skoða skrána. |br|
       Nota má stika ``dtype`` og ``names``; sjá að ofan |br|
       (fwf = *fixed width file*)

.. list-table:: Ýmsar skipanir fyrir gagnatöflur
   :widths: auto
   :name: ýmsar-pandas-skipanir

   * - ``df["nýrdálkur"] = df["A"]*2``  
     - Bætt við nýjum dálki sem er tvöfaldur dálkur ``A``

   * - ``df = df.drop(3)``
     - Eyða línu með auðkenni 3

   * - ``df = df.drop(columns = ["A","D"])``
     - Eyða dálkum A og D

   * - ``display(df)``                  
     - Skrifa töflu á skjá, með HTML-sniði

   * - ``print(df)``
     - Skrifa töflu á skjá með textasniði

   * - ``display(df.style.format(fmt))``
     - Skrifa HTML-töflu með sniði ``fmt`` sem getur t.d. |br|
       verið ``"{:.2%}"`` eða ``{"A": "{:.2f}"}`` |br|
       (til að sníða bara dálk ``A``)

   * - ``df = df.sort_values(by="dálkur")``  
     - Raða töflu eftir gildunum í *dálki*

   * - ``df = df.sort_values(by="dálkur",`` |br| |sp3| ``ascending=False)``
     - Raða töflu í minnkandi röð

   * - ``df.describe()``                
     - Skila töflu yfir meðaltöl, staðalfrávik o.fl.

   * - ``df = df1.join(df2)``
     - Sameina ``df1`` og ``df1`` með
       `join
       <https://en.wikipedia.org/wiki/Relational_algebra#Joins_and_join-like_operators>`_-virkja
       útfrá |br| línuauðkennum (*indexum*)

   * - ``L = list(df["nfn"])``          
     - Dálki "nfn" breytt í venjulegan Python lista

   * - ``A = np.array(df.loc[:,"A":"C"])``
     - Hluttöflu breytt í NumPy fylki

   * - ``A = df.loc[:,"A":"C"].values``
     - Önnur leið til að búa til NumPy fylki

.. Æfing
.. hint::

   Eyðið flokki að eigin vali úr kosningaúrslitatöflunni, þó ekki þeims síðasta.
   Prófið svo að birta línur þar fyrir aftan, annars vegar með ``loc`` og hinsvegar
   með ``iloc`` og takið eftir muninum.

.. list-table:: Skipanir fyrir runur (*sequences*)
   :widths: auto
   :name: pandas-fyrir-runur

   * - ``s[nafn]``
     - Stak með gefið nafn

   * - ``s.iloc[nr]``
     - Stak númer nr
       
   * - v = np.array(s) |br|
       v = s.values
     - Runu breytt í NumPy vigur

   * - s.mean()
     - Meðaltal

   * - s.std()
     - Staðalfrávik

   * - L = list(s.index)
     - Venjulegur listi með auðkennum s

Innbyggð Python föll og Pandas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Oft er hægt að beita algengum innbyggðum Python-föllum á hvort sem er
gagnatöflur eða Pandas-runur beint. Þannig er hægt að finna stærsta stak runu og
fjölda lína í töflu með ``max(s)`` og ``len(df)``. Annað dæmi er ``zip``: til að
búa til uppflettitöflu frá listabókstaf í flokk í sýnidæminu í :numref:`kafla
%s<pandas gögn>` má nota ``U = dict(zip(kosn["Stafur"], kosn["Flokkur"]))``. Það
þarf sem sé ekki nauðsynlega að breyta Pandas-hlutum í venjulega lista áður en
unnið er með þá áfram.

Það sama gildir um bæði NumPy-föll og Matplotlib-skipanir, að þeim má oft beita
beint á Pandas-hluti. Ef ``df`` er ferningslaga og ``s`` hefur rétta lengd þá má
t.d. leysa jöfnuhneppi með ``la.solve(df, s)`` og reikna kvaðratrætur allra
staka með ``np.sqrt(df)``. Þetta er samt ekki alveg algilt, t.d. er hægt að
reikna ``sum(df.values)`` en ekki ``sum(df)``. Um notkun Pandas með Matplotlib
er svo rætt í næsta kafla.

Pandas og teikningar
~~~~~~~~~~~~~~~~~~~~
Matplotlib teikniskipanir geta notað dálka í Pandas-töflum sem viðföng. Til dæmis, ef ``xy.xlsx`` hefði tvo dálka, "x" og "y", þá mætti teikna línurit af þeim með skipununum::

    df = pd.readexcel("xy.xlsx")
    plt.plot(df["x"], df["y"])

Í eftirfarandi dæmi eru Pandas-dálkar notaðir sem viðföng í skipanirnar :code:`bar` og :code:`xticks`.
   
.. admonition:: Sýnidæmi: Kosningaúrslit með Pandas
   :class: synidaemi

   Hér er dæmi sem teiknar súlurit af kosningaúrslitunum 2017 sem voru
   á dagskrá í sýnidæmi í grein :numref:`pandas-gögn`:

   .. code:: python

      plt.figure(dpi=100)
      kosn = pd.read_excel("http://cs.hi.is/python/kosningar.xlsx")
      x = range(len(kosn))
      plt.bar(x, kosn["Atkvæði"], color="tomato")
      plt.xticks(x, kosn["Stafur"])
      plt.ylabel('Atkvæði')
      plt.title('Úrslit alþingiskosninga 2017');

   Hér er x listinn [0,1,2...9] (það voru 10 framboðslistar). Lista ef liti má finna 
   `hér <https://en.wikipedia.org/wiki/Web_colors#Extended_colors>`_.
   Forritið teiknar þessa mynd:

   .. figure:: myndir/kosningar-2017.jpg
      :align: center
      :figwidth: 11cm

Fleiri Pandas æfingar
~~~~~~~~~~~~~~~~~~~~~
Til að læra betur á Pandas er tilvalið að beita því til að leysa ýmis verkefni tengd
skráavinnslu aftast í þessum fyrirlestrarnótum, t.d. verkefni :numref:`reiknað með fylkjum`, :numref:`sameining nafnaskrár og einkunnaskrár`, :numref:`kosningaúrslit`, :numref:`hiti og úrkoma`, :numref:`málmavinnsla`, :numref:`körfuboltamenn` og :numref:`póker`. Með því gefst tækifæri til að nota ýmsar af þeim skipunum sem gefnar eru í töflunum í kafla :numref:`helstu pandas-skipanir`

Punktritháttur
~~~~~~~~~~~~~~
Í Python eru hornklofar notaðir til að tákna gildi í uppflettitöflum eins og við
kynntumst í :numref:`%s. kafla<uppflettitöflur>`, á svipaðan hátt og Pandas
notar hornklofa til að vísa í töfludálka. Í Javascript er hægt að skilgreina
hluti (*objects*) sem svara að mörgu leyti til uppflettitaflna í Python. Þar er
hægt að nota hornklofa til að fletta upp eiginleikum hluta, en maður hefur
val og getur líka notað punkt. Eftirfarandi er löglegt Javascript forrit:

.. code:: javascript

   let einst = {'nafn': 'Jón', 'aldur': 33}
   einst['sími'] = 888-7777
   einst.kennitala = '111213-3210'
   console.log(einst["nafn"], einst.aldur, einst.sími)

Það sama á svo við um Pandas: Það er hægt að nota punkt til að vísa í dálka í
Pandas gagnatöflum. Þetta er nefnt *punktritháttur* (*dot notation*). Þannig
mætti hafa sýnidæmið í kafla :numref:`pandas gögn` svona:

.. code:: python

   import pandas as pd
   kosn = pd.read_excel("http://cs.hi.is/python/kosningar.xlsx")
   display(kosn)
   n = sum(kosn.Atkvæði)
   kosn["Hlutf"] = kosn.Atkvæði/n
   display(kosn)          

og miðparturinn í sýnidæminu í kafla :numref:`pandas og teikningar` yrði:

.. code:: python
          
   x = range(len(kosn))
   plt.bar(x, kosn.Atkvæði, color="tomato")
   plt.xticks(x, kosn.Stafur)

Það eru ýmsar takmarkanir á punktrithættinum:

- það er ekki hægt að nota hann til að bæta við dálkum (``kosn.Hlutf =
  kosn.Atkvæði/n`` dugar ekki)
- dálknafnið má ekki vera tala, nafn á Pandas-aðferð eða frátekið Python-nafn (t.d.
  hvorki 37, *count* eða *class*)
- dálknafnið getur ekki innihaldið bil.

Engu að síður er punktrithátturinn talsvert notaður; hann sparar þrjá stafi
miðað við hornklofana og er auðveldari að lesa. Hér er ágæt `umræða
<https://www.dataschool.io/pandas-dot-notation-vs-brackets/>`_ um málið.
