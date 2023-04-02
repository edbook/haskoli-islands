.. include:: rst-include

VERKEFNI
========

VV1. Hlutafleiður og stiglar
----------------------------
Reiknið með blaði og blýanti (og sýnið útreikninga eftir því sem við á):

1. :math:`f_x` ef :math:`f(x,y) = e^{xy}\log(xy)` |br1|

2. :math:`D_y \left((x+y^3)^5 - \sin(x-y)\right)` |br1|

3. :math:`\dfrac{\partial}{\partial z} \dfrac{\log(xz)}{z^2}` |br1|

4. :math:`\nabla f` ef :math:`f(x,y) = x^2y + xy + y^3` |br1|

5. :math:`\nabla f(1,2)` ef :math:`f` er fallið í lið 4 |br1|

6. hlutafleiður fallsins :math:`f(x,y) = (x+1) \exp(y-x) - 3y\sin(xy)`

VV2. Formengi og útgildi
------------------------
1. Ákvarðið stærsta mögulegt formengi fallsins

   .. math:: f(x,y) = \sqrt{x^2-5x+6}\sqrt{y^2+5y-6}

2. Gefið er fallið

   .. math:: g(x,y) = 4x^2 - 4xy + 2y^2 + 10x - 6y

   Fallið hefur einn útgildispunkt sem ákvarða skal (með blaði og blýanti). Er
   hann lággildi eða hágildi? (rökstyðjið)

VV3. Fall Rosenbrocks
---------------------
Í æfingu í kafla :ref:`A3 <teikning-stigla>` er "Fall Rosenbrocks" skilgreint og
sýnd mynd af því. Fallið er:

.. math:: f(x, y) = (1 - x)^2 + 100(y - x^2)^2

1. Skrifið fall ``rosen(x,y)`` til að reikna gildi fallsins. Prófið að reikna
   :math:`f(-1.2, 1)` sem ætti að gefa 24.2.

2. Teiknið hæðarlínumynd af Rosenbrock-fallinu með ``plt.contour`` á svæðinu
   :math:`[-2,2] \times [-1,3]`. Látið hæðarlínurnar vera dökkbláar, merkið þær líkt
   og gert er í sýnidæminu *Hæðarlínur falls* í kafla A1, og  hafið netlínur (*grid*)
   með. Til að fá góða mynd þarf bæði að reikna fallið á þéttu neti (t.d. :math:`300
   \times 300)` og velja hæðarlínugildin, sem fást með stikanum ``levels`` vel.
   Gildin :math:`0.2, 2^2, 6^2, 10^2,\ldots, 46^2` gefa t.d. ágæta mynd. Þau má búa
   til með:

       ``levels = np.append([0.2], np.arange(2,50,4)**2)``

VV4. Próf í stærðfræði og reiknifræði 2019
------------------------------------------
Athugið að í þessu prófi voru engin hjálpargögn leyfileg nema reiknivél og
formúlublað.

.. rubric:: A. Python forrit
            
1. Skrifið Python fall með tvo stika, :math:`a` og :math:`n`. Ef :math:`a < 0` á
   fallið að skila :math:`a^n` en ef :math:`a \geq 0` á það að skila
   :math:`\sqrt{a^n+a}`. Skrifið tilheyrandi Python forrit sem kallar á fallið
   með :math:`a=2`, :math:`n=7` og með :math:`a=-2`, :math:`n=3` og skrifar út
   niðurstöðu þess í báðum tilvikum.

2. Skrifið Python fall eða reiknirit sem tekur inn einhvern lista af tölum og
   skilar staðsetningu fyrstu tölunnar sem uppfyllir jöfnuna :math:`x^5 + x =
   246`. Ef engin slík tala finnst á fallið að skila –1. Skrifið tilsvarandi
   forrit eða reiknirit sem prófar fallið með listanum ``[5, 4, 3, 2, 1]``.

.. rubric:: B. Gagnasafn

Gefin eru gögn :math:`(x_i, y_i), i=1,\ldots, n`.

1. Skrifið formúlu falls sem hægt væri að lágmarka til að ákvarða bestu línu
   fyrir gagnasafnið. Teiknið skýringarmynd.

2. Skrifið formúlu falls sem lágmarka mætti til að ákvarða bestu parabólu fyrir gagnasafnið.
 
3. Nú kemur í ljós að :math:`y` er ekki bara háð :math:`x` heldur líka tímanum.
   Fyrir hvern punkt :math:`(x_i, y_i)` er gefinn tími, :math:`t_i`, og
   markmiðið er að smíða aðhvarfslíkan sem lýsir gögnunum sem best. Hvað kemur
   til greina að gera, og hvaða fall væri hægt að lágmarka? Hvaða stikar koma
   við sögu?

.. rubric:: C. Hlutafleiður

1. Finnið hlutafleiðuna :math:`D_x (x^2 + y)^6 + e^{y-x}`
2. Finnið stigul fallsins :math:`f(x,y) = x^3 + xy - y^3`
3. Finnið fyrsta stigs Taylor-nálgun við :math:`f` í punktinum :math:`(1, 2)`. 

.. rubric:: D. Vigrar

1. Sýnið að vigrarnir :math:`a = (1, 2, 3)`, :math:`b= (4, 2, 0)` og :math:`c =
   (1, 0, 1)` séu línulega óháðir.

2. Hve margar gráður er hornið milli :math:`a` og :math:`b`?

3. Finnið vigur :math:`d` þannig að :math:`a`, :math:`b` og `d` verði línulega háðir.

4. Nokkrir ætla að leggja í púkk til að kaupa hlut. Ef hver borgar átta peninga
   eru þrír peningar afgangs en ef hver borgar sjö vantar fjóra upp á. Þetta
   dæmi mætti leysa með því að leysa jöfnu :math:`Ax=b` þar sem :math:`A` er
   :math:`2 \times 2` fylki og :math:`b \in \Bbb{R}^2`. Ákvarðið :math:`A` og
   :math:`b` (ekki skal leysa jöfnuna).

.. rubric:: E. Stofnstærð

Tegund lifir í max 3 ár. Hver núll-ára gefur 0.2 núll-ára afkvæmi árið eftir, hver eins árs 0.6 afkvæmi ári síðar og hver tveggja ára 0.8. 20% núll-ára eru dauð ári seinna, og dánartíðni eins árs er 50%. Í upphafi er stofnstærðin 2000 einstaklingar, 1000 núll-ára, 600 eins árs og 400 tveggja ára.

1. Ákvarðið Leslie-fylki fyrir þennan stofn.
2. Ákvarðið stofnstærð eftir eitt ár
3. Lýsið með orðum og/eða jöfnum aðferð sem nota mætti til að ákvarða hvort
   stofninn muni að lokum deyja út.

VV5. Flokkun veðurgagna með k-means reikniriti
----------------------------------------------
1. Lesið skrána http://cs.hi.is/python/hiti-urkoma.txt inn í þrjá vigra: ár,
   hiti, úrkoma. Búið svo til :math:`n \times 2` fylki úr hita og úrkomu (t.d.
   með ``X = np.c_[...]``), staðlið það með ``whiten`` og flokkið í fjóra hópa
   með k-means reikniritinu. Hafið ``npr.seed()`` með svo sömu flokkar fáist við
   endurteknar keyrslur. Hverjir eru miðpunktar hópanna og hvað eru mörg ár í
   hverjum hópi?

2. Teiknið mynd af hópunum eins og gert er í sýnidæminu í kafla
   :numref:`kmeans`; merkið m.a. miðpunktana inn með stjörnum. Notið ``qcmap``
   til að velja liti og bætið svo við rúðuneti og ásamerkingum sbr. aftasta
   sýnidæmið í kafla :ref:`A5 <litastikur>` í Viðauka A. Bætið loks við
   litastiku eins og þar er gert sem sýnir flokkun áranna, en þau ættu að
   flokkast gróflega í þurr, blaut, heit og köld.

3. Teiknið nú nýja mynd þar sem árin eru flokkuð í 10 hópa. Merkið hópana
   á litastiku þessarar myndar með tölunum 1–10 og setjið ``label`` á
   stikuna: **Flokkur**. Látið litastiku þessarar myndar líka vera breiðari
   en á myndinni í lið 2.

VV6. Hlutapróf 2 vorið 2021
---------------------------
.. rubric:: A. Stiglar og lágmörkun

Gefið er fallið

.. math:: 
   f(x,y) = x^2y + 2xy^2 - 3xy + 4 

punkturinn :math:`p = (1,1)` og vigurinn :math:`u = (-1,-1)`.

1. Ákvarðið stigul :math:`f` (þ.e.a.s. :math:`\nabla f`), skrifið Python-fall
   sem finnur hann og notið það til að reikna :math:`\nabla f(p)`

2. Lát :math:`u = (-1,-1)`. Notið Python-fallið úr a-lið líka til að reikna
   stefnuafleiðu :math:`f` í stefnu :math:`u` í punktinum :math:`p`. Búið líka
   til einhvern punkt og vigur úr afmælisdegi ykkar og reiknið tilsvarandi
   stefnuafleiðu.

3. Lát :math:`u = (-1,-1)`. Notið Python-fallið úr a-lið líka til að reikna
   stefnuafleiðu :math:`f` í stefnu :math:`u` í punktinum :math:`p`. Búið líka
   til einhvern punkt og vigur úr afmælisdegi ykkar og reiknið tilsvarandi
   stefnuafleiðu.

4. Teiknið að lokum hæðarlínur :math:`f` á svæðinu :math:`[0,3] \times [0,2]`.

.. rubric:: B. Er punktur í plani?

Í þessu dæmi á að skrifa Python-fall til að kanna hvort gefinn punktur liggi í gefnu plani í þrívíðu rúmi. Vegna þess að Python reiknar með endanlegri nákvæmni verður að láta duga að athuga hvort punkturinn sé í planinu eða mjög nálægt því.

1. Skrifið Python-fall ``næstum_eins(u,v)`` sem skilar sönnu (``True``) ef
   :math:`u \approx v` í þeim skilningi að fjarlægðin milli vigranna :math:`u`
   og :math:`v` sé minni en :math:`10^{-8}`, en annars ósönnu (``False``).
   Prófið með pari vigra sem eru ólíkir og pari mjög líkra vigra.

2. Í kafla :numref:`þverstaðlaðir grunnar` er gefið skilyrði (merkt
   :math:`(*)`), sem nota má til að kanna hvort punktur (eða vigur) :math:`u` sé
   í planinu sem tveir þverstaðlaðir vigrar :math:`a` og :math:`b` spanna, sbr.
   sýnidæmið aftast í greininni. Fyrir tvo vigra segir reglan að það gildi
   þ.þ.a.a.

   .. math:: 
      u = (a\cdot u)a + (b\cdot u)b

   Skrifið Python-fall ``í_plani(u,a,b)`` þar sem stikarnir eru vigrar í
   :math:`\Bbb R^3` og :math:`\{a,b\}` er þverstaðlaður grunnur. Það á að nota
   fallið úr a-lið til að rannsaka hvort :math:`u` sé (næstum) í planinu sem
   :math:`a` og :math:`b` spanna.

3. Prófið fallið úr b-lið með vigrunum og punktunum sem gefnir eru í sýnidæminu,
   sem sé :math:`a = (0.48, 0.64, 0.60)`, :math:`b = (0.8, -0.6, 0)`, og svo:

   :math:`a)` :math:`u=A=(4,2,3)` (í planinu) og |br|
   :math:`b)` :math:`u=B=(6,3,2)` (ekki í planinu).

.. rubric:: C. Efnisspurningar

1. Skilgreinið graf tvívíðs falls (annaðhvort með orðum eða formúlu).

2. Gerðar eru daglegar mælingar á loftmengun á fimm stöðum í Reykjavík.
   Mælingarnar felast í að mæla styrk svifryks með tveimur kornastærðum auk
   fjögurra mengandi lofttegunda. Eitt fylki geymir mælingar á hverjum stað í
   hverjum mánuði. Hvað þarf stórt fylki til að geyma mælingar á Grensásvegi í
   apríl?

3. Reynt er að lýsa styrk brennisteinstvíoxíðs við Grensásveg sem falli af
   vindhraða í m/s og hitastigi í °C. Hvaða formengi væri skynsamlegt að nota
   til að teikna fallið ef ætlunin er að fanga flest veðurskilyrði, en ekki
   endilega öll.

4. Hver er munurinn á vigursviði og skalarsviði?

5. Lát :math:`f\colon\Bbb R^2\to\Bbb R`. Gerið grein fyrir muninum á almennu
   hlutafleiðunni :math:`\dfrac{\partial f}{\partial x}` og hlutafleiðunni í
   tilteknum punkti, :math:`\dfrac{\partial f(a,b)}{\partial x}`

6. Hver eftirfarandi falla :math:`f\colon\Bbb R^4\to\Bbb R` eru línuleg? (Það
   þarf ekki að rökstyðja svörin, bara svara rétt).

   :math:`a)` :math:`f(x) = x\cdot x` |br|
   :math:`b)` :math:`f(x) = (3,4,5)\cdot x` |br|
   :math:`c)` :math:`f(x) = \text{staðalfrávik }x` |br|
   :math:`d)` :math:`f(x) = \text{minnsta stak }x` |br|
   :math:`e)` :math:`f(x) = \text{aftasta stak }x` |br| |br|

7. Greindar hafa verið 3 Íslendingasögur með orðtíðni. Hornin á milli þeirra eru
   sýnd í eftirfarandi töflu:

   .. csv-table::
      :widths: auto
      :delim: |
      :header-rows: 1

      **Saga**|A  |B  | C
      **A**   |–  |68°|85°
      **B**   |68°|–  |45°
      **C**   |85°|45°| –

   Talið er að Snorri Sturluson hafi skrifað tvær af sögunum. Hvaða sögur er
   líklegast að það hafi verið miðað við þessar upplýsingar? Rökstyðjið örstutt.

8. Sýnið dæmi um tvo vigra í :math:`\Bbb R^3` sem mynda grunn og annað dæmi um
   tvo vigra sem mynda ekki grunn.

9. Lýsið (eða nefnið) tvær aðferðir sem nota má til að finna útgildi falls, aðra
   stærðfræðilega og hina með aðstoð forrits.

10. Leysa skal hneppi af þremur jöfnum í þremur óþekktum. Hvaða skilyrði þarf
    fylki hneppisins að uppfylla til að til sé einkvæm lausn? Hvaða Python-fall
    mætti nota til að kanna þetta skilyrði?

VV7. Lágmörkun Rosenbrock-fallsins
----------------------------------
Fall Rosenbrocks var kynnt í æfingu í kafla :ref:`A3 <teikning-stigla>` og verkefni VV3. Algengt er að nota þetta fall til að prófa aðferðir í tölulegri bestun. Hér er forrit með hluta af lausn á VV3, sem skilgreinir fallið og teiknar hæðarlínur þess:

.. code:: python

    def rosen(x):
      res = (1-x[0])**2 + 100*(x[1] - x[0]**2)**2
      return res

    import matplotlib.pyplot as plt
    import numpy as np
    plt.figure(figsize=(8,8))
    x = np.linspace(-2,2,400)
    y = np.linspace(-1,3,400)
    [X,Y] = np.meshgrid(x,y)
    Z = rosen([X,Y])
    levels = [0.2, 5, 50] + list(range(200,2300,400))
    c = plt.contour(X, Y, Z, levels = levels, colors = 'gray')
    levstr = {l:str(l) for l in levels}
    plt.clabel(c, fmt=levstr)
    plt.xticks(range(-2,3))
    plt.yticks(range(-1,4))
    plt.grid("True")

Fallið er örlítið breytt frá VV3, það hefur bara einn stika, tveggja stak vigur x,
með x- og y-gildunum þar sem reikna skal fallsgildið. Takið eftir hvernig
fallsgildin eru reiknuð á :math:`400 \times 400` neti í einu lagi með því að búa
til lista úr fylkjunum ``X`` og ``Y``. Uppflettitaflan ``levstr`` nýtist til að
hafa hæðarlínumerkingarnar aukastafalausar, nema þá innstu.

1. Afritið forritið að ofan inn í Colab. Minnkið svæðið sem fallið er teiknað á
   um hálfa einingu á öllum hliðum, niður í ferninginn :math:`[-1.5, 1.5] \times
   [-0.5, 2.5]`. Prófið að fjölga hæðarlínunum. Reiknið líka fallsgildið í
   :math:`x_0 = (-1.2, 1)` sem ætti að vera 24.2 og :math:`x^* = (1,1)` sem
   ætti að vera 0.
   
2. Í SciPy er pakki, **optimize**, fyrir tölulega bestun. Hann er oft fluttur inn með:

      ``import scipy.optimize as opt``
    
   sem *opt*, m.a. að ofan. Í honum er fall, `minimize`, til að finna lággildi
   falla sem notast svona:

   .. code:: python
             
      result = opt.minimize(f, x0)
      xmin = result.x

   þar sem ``f`` er fallið sem á að lágmarka, ``x0`` er vigur með byrjunarágiskun og
   ``xmin`` er lággildispunkturinn. Notið ``minimize`` til að lágmarka fall
   Rosenbrocks með :math:`x_0 = (-1.2, 1)`. Skoðið hvað er í ``result`` og skrifið
   örfá orð um það.

3. `minimize` getur tekið inn viðbótarstika ``callback=cb``, og þá kallar það á
   ``cb(xk)`` með núverandi ítrekunargildi ``xk`` í hverri ítrekun (í þessu
   tilviki er ``xk`` tveggja staka vigur). Notið þennan "fídus" til að teikna
   ítrekunargildin inn á hæðarlínumyndina (hægt er að láta ``cb`` kalla á
   ``plt.scatter(x[0],x[1])``)

4. ``minimize`` getur líka tekið inn stika ``method="aðferð"``, þar sem aðferð
   getur t.d. verið ``"L-BFGS-B"``, ``"CG"``, og ``"Powell"`` fyrir utan þá sjálfvöldu,
   ``"BFGS"``. Prófið og segið skipulega frá niðurstöðum. Prófið líka eina
   sjálfvalda aðferð (skoðið `skjölun um minimize
   <https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html>`_
   á netinu til að sjá möguleikana).

   .. admonition:: Athugasemd: 
      :class: athugid

      ``result.nit`` gefur fjölda ítrekana og ``result.nfev`` gefur fjölda kalla
      á ``rosen``. Það er ágætt að sýna niðurstöðurnar (í textareitnum) með
      töflu yfir fjölda ítrekana og fallsgilda fyrir hverja aðferð (sjá kafla
      `3.6 <https://cs.hi.is/python/kafli03/#markdown-og-latex>`_ í
      Python-nótum). Þegar bornar eru saman svona niðurstöður er venjan að reikna
      með að meginhluti útreikninganna sé í fallinu sjálfu svo maður ætti að
      leggja áherslu á samanburð á ``nfev``.

5. Ákvarðið hlutafleiður og þar með stigul Rosenbrock-fallsins (á blaði) og
   forritið hann í Python falli ``rosg(x)`` sem skilar tveggja staka NumPy-vigri
   með stiglinum í punktinum :math:`x = (x_0, x_1)`. Ef rétt er forritað ætti
   stigullinn í :math:`x_0` að vera :math:`(-215.6, -88)` og í :math:`x=(1,1)`
   ætti hann að vera :math:`(0,0)`.

6. Í ``minimize`` er ``jac``-stiki til að tilgreina stigul fallsins sem á að
   lágmarka (**jac** er stytting á **Jacobian**, sem fyrir
   :math:`f\colon\Bbb{R^2}\to\Bbb{R}` er samheiti við **gradient**). Ef stigullinn er
   nýttur svona ættu að sparast ítrekanir og (líklega) heildarreikningar. Prófið
   það með sjálfgefnu BFGS-aðferðinni, og kannið hve mikið sparast miðað við
   b-lið. Í samanburðinum má má gera ráð fyrir að stigull kosti eins og tvö
   fallsgildi. Segið í örfáum orðum frá niðurstöðunni.

VV8. Jarðskjálftar og eldgos á Reykjanesskaga 2021
--------------------------------------------------
Í þessu verkefni á að vinna með jarðaskjálftana sem urðu á Reykjanesskaga í
febrúar og mars 2021, m.a. teikna þá inn á kort. Þið þurfið auk þess að búa til
nokkur línurit og skrifa smá skýrslu um hvað þau segja okkur. Skráin
http://cs.hi.is/python/skjalftar.txt er ættuð frá Veðurstofu Íslands og geymir
lista yfir skjálftana, tíma, staðsetningu og stærð hvers skjálfta. Þið áttið
ykkur strax á innihaldinu með því að smella á skrána.

1. **Skjálftaskrá lesin.** Byrjið á að lesa skrána inn í Pandas töflu, sbr. `15.
   kafla <https://cs.hi.is/python/kafli15/#pandas>`_ í Fyrirlestrarnótum um
   Python. Athugið að flestar NumPy- og Matplotlib-skipanir ráða við viðföng sem
   eru Pandas-dálkar, en það er líka hægt að nota *values*: Ef ``x =
   df.x.values`` skilar NumPy-vigri með dálkinum x. Tímadálkurinn þarf sérstaka
   meðhöndlun. Ef ``df.tími`` er Pandas-dálkur með tímasetningum á sama sniði og
   eru í skránni þá dugar eftirfarandi skipanir til að búa til Pandas runu með
   degi og broti úr degi frá miðnætti 24. febrúar fyrir hverja tímasetningu:

   .. code:: python

      tími = pd.to_datetime(df.tími)
      dagur1 = pd.to_datetime('24.02.2021')
      dagur = (tími - dagur1).dt.total_seconds()/(60*60*24)

2. **Línurit og töflur.** Búið nú til nokkrar teikningar og/eða töflur af
   skjálftunum. Hér er gott að nota hugmyndaflugið: Þið getið t.d. gert súlurit
   yfir stærð skjálftanna (með 3.5–6 á x-ás og fjölda á y-ás), línurit yfir
   lengd sem falla af tíma og annað fyrir breidd (tvö línurit, t.d. hlið við
   hlið (með ``subplot`` sbr. kafla `13.6
   <https://cs.hi.is/python/kafli13/?highlight=subplot#gervigogn>`_ í
   Python-nótunum), súlurit yfir fjölda pr. dag (eða viku), eða töflu yfir
   meðalstaðsetningu skjálfta í hverri viku. Ath. að á Reykjanesskaga er hver
   lengdargráða u.þ.b. 44% (þ.e. cos 64°) af breiddargráðu. Svo kemur líka vel
   til greina að breyta staðsetningunum fyrst í (x,y) hnit sbr. lið 3 áður en
   línurit af staðsetningum eru gerð.

   Það er hægt að teikna rununa ``dagur`` á x-ás en svo er líka hægt að teikna
   ``tími`` beint með eftirfarandi falli sem merkir inn réttar dagsetningar:

   .. code:: python
             
      def daga_xás():
        # Undirbýr teikningu tímasetninga á x-ás. Hentar fyrir tímabil frá 
        # nokkrum dögum og upp í nokkrar vikur.
        import matplotlib as mpl
        ax = plt.gca()
        ax.xaxis.set_minor_locator(mpl.dates.HourLocator(byhour=[0]))
        ax.xaxis.set_major_locator(mpl.dates.HourLocator(byhour=[12]))
        ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter())
        ax.xaxis.set_major_formatter(mpl.dates.DateFormatter("%d.%m.%Y"))
        ax.tick_params(which='major', length=0)
        ax.tick_params(axis='x', labelrotation=90)
        ax.grid(axis='y')
        ax.grid(axis='x', which='minor')

   Skrifið stutta skýrslu um hvað þessar myndir segja okkur, t.d. um þróun
   skjálftavirkninnar, hlutfall stórra og lítilla skjálfta eða hvað annað sem
   ykkur finnst áhugavert.

3. **Breytt úr hnattstöðu í xy-hnit.** Til að undirbúa teikningu skjálftanna inn
   á kort þarf að breyta staðsetningu þeirra úr hnattstöðu í svonend landshnit.
   Til þess má nota Python-pakkann `pyproj`. Hann þarf að setja upp sérstaklega
   með skipuninni:

     ``!pip install pyproj``

   Eftir það er hægt að keyra eftirfarandi skipanir sem búa til fall `hnatt2xy`
   sem nota má með `(x,y) = hnatt2xy(breidd,lengd)` til að breyta úr lengd og
   breidd yfir í landshnit. Viðföngin og skilabreyturnar mega vera NumPy-vigrar.

   .. code:: python
             
      from pyproj import Transformer as Trans
      hnatt2xy = Trans.from_crs('latlon',3057).transform

   .. admonition:: Athugasemd: Um landshnitakerfið
      :class: athugid

      Landshnitakerfi Íslands með auðkenni ISN93 er algeng kortavörpunin fyrir
      Íslandskort. Kerfið hefur einingu metra, og x- og y-ásar þess snúa í austur og
      norður eins og hefðbundið er um þá ása. Þetta kerfi er númer 3057 í svonendri
      EPSG skrá sem er alþjóðleg skrá um kortavarpanir sem margvíslegur
      kortahugbúnaður þekkir, m.a. Pyproj-pakkinn. Vörpunin er hornsönn keiluvörpun
      (conformal conic projection) Lamberts með miðpunkt í 65°N, 19°V sem hefur hnit
      (500000,500000) og viðmiðunarbreiddarbauga 64.25°N og 65.75°N. Tvær nýrri
      varpanir eru til, ISN2004 og ISN2016. Báðar hafa sama miðpunkt og breiddarbauga
      en hnit miðpunktsins eru önnur, (1700,300) km og (2700,300) km. Þessi munur
      gerir mögulegt að þekkja strax í sundur úr hvaða kerfi tiltekin hnit eru. Auk
      þess hafa hnit einstakra mælipunkta færst smávegis vegna landreksins sem er um
      hálfur metri frá 1993 til 2016.

4. **Landakort með skjálftum.** Næst á að merkja skjálftana inn á kort, Skráin
   `https://cs.hi.is/python/reykjanesskagi.png
   <https://cs.hi.is/python/reykjanesskagi.png>`_ geymir kort af Reykjanesskaga
   sem hægt er að nota sem bakgrunn til að teikna inn á. Með því að stilla mörk
   ása á sömu hnit og mörk kortsins er hægt að merkja skjálftana á nákvæmlega
   rétta staði. Kortaskráin er búin til með forriti sem heitir **qgis**, og
   henni fylgir svokölluð "world" skrá
   (https://cs.hi.is/python/reykjanesskagi.pgw) með upplýsingum um hnit svæðisins
   sem kortið nær yfir. Hér fyrir neðan er fall sem les slíkt par af skrám og annað fall
   til að birta kortið sem bakgrunn í Matplotlib glugga.

   Til að fá gott kort ætti að velja `gluggabreidd` sæmilega stóra svo kortið
   fylli upp breidd skjalsins sem þið búið til. Merkið svo skjálftana inn á
   kortið með `scatter` og látið stærð skjálftanna ráða stærð markeranna og
   jafnvel lit. Enn ein hugmynd er að sýna stærstu skjálftana með stjörnu.
   
   Skrifið að lokum nokkur orð um það sem kortið segir ykkur, t.d. með vísun
   til örnefna (þið gætuð jafnvel skoðað önnur kort með fleiri örnefnum)

   .. code:: Python

      #KORTFÖLL
      def lesa_qgis_kort(skrá):
        # Les kort úr skrá.png og skrá.pgw og skilar pari (kort,mörk) með þrívíðu
        # NumPy-fylki með kortinu ásamt fjögurra staka vigur með hnitum í kílómetrum
        # á vestur-, austur-, suður- og norðurbrúnum kortsins, mörk = [xv,xa,ys,yn].
        kort = np.flipud(plt.imread(skrá + ".png")) # svo kortið sé ekki á hvolfi
        world = np.loadtxt(skrá + ".pgw")
        (hæð,breidd) = np.shape(kort)[0:2]
        skali = world[0]  # metrar á díl (pixel) í png-skránni
        xv = world[4]
        xa = xv + skali*breidd
        yn = world[5]
        ys = yn - skali*hæð
        mörk = np.array([xv,xa,ys,yn])/1000  # breytt í km
        return (kort,mörk)

      def sýna_kort(kort, mörk, gluggabreidd, dpi=100):
        # Birtir kort í Matplotlib glugga og setur mörk ása til samræmis við mörk 
        # kortsins; gluggabreidd og dpi eru notuð til að búa gluggann til með 
        # plt.figure kalli, sem gefur glugganum tilgreinda breidd (í tommum) og hæð 
        # sem ákvarðast hlutfallslega eftir lögun kortsins
        (hæð, breidd) = np.shape(kort)[0:2]
        plt.figure(figsize=(gluggabreidd, gluggabreidd*hæð/breidd), dpi=dpi)
        plt.axis(mörk)
        plt.imshow(kort, origin='lower', extent=plt.axis())
