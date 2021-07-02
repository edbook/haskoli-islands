.. _c.hlutfoll:

Ályktanir um flokkabreytur
==========================

Ályktanir um hlutföll og tengslatöflur eru geysimikið notaðar í almennri
tölfræðiúrvinnslu. Slík tilgátupróf er afar auðvelt að framkvæma í R
enda má nálgast allar helstu upplýsingar um tilgátuprófin sem og
öryggisbil fyrir metlana í einni skipun. Við byrjum á því að fjalla um
ályktanir um eitt hlutfall í kafla :numref:`%s <s.eitthlutfall>`. Í kafla
:numref:`%s <s.tvohlutfoll>` fjöllum við um ályktanir um tvö eða fleiri hlutföll
sem byggja á normalnálgun og að lokum fjöllum við um tengslatöflur í
kafla :numref:`%s <s.tengslatoflur>`.

Stuðst verður við skipanirnar ``binom.test()``, ``prop.test()``,
``chisq.test()`` og ``fisher.test()``.

.. _s.eitthlutfall:

Ályktanir um eitt hlutfall
--------------------------

Ályktanir um eitt hlutfall
~~~~~~~~~~~~~~~~~~~~~~~~~~

Við notum aðferðina ``binom.test()`` til að kanna tilgátur og smíða
öryggisbil fyrir hlutfall þýðis. Skipunin er mötuð á fjölda útkoma af
hvorri gerð sem fá má með skipuninni ``table()`` sem var sýnd í kassa
:numref:`%s <rf.table>`. Hér er dæmi þar sem aðferðin er notuð til að kanna
hvort kynjahlutfallið sé jafnt í nemendahópnum sem púlsgögnin byggja á.

binom.test()
^^^^^^^^^^^^

.. attention::

    **Inntak:** tafla - úttak úr table
    
    **Úttak:** gildi á prófstærð, p-gildi, öryggisbil ofl.
    
    **Helstu stillingar:** conf.level, p


--------------

Byrjum á því að nota ``prop.table()`` skipunina, (kassa
:numref:`%s <rf.prop.table>`) til að sjá hvert kynjahlutfallið er:

::

   prop.table(table(puls$kyn))
   ##
   ##       kvk        kk
   ## 0.6518047 0.3481953

Tilgátuprófið, öryggisbilið, prófstærðin og tilgátuprófið fást öll í
einu með einni skipun:

::

   binom.test(table(puls$kyn))
   ##
   ##  Exact binomial test
   ##
   ## data:  table(puls$kyn)
   ## number of successes = 307, number of trials = 471, p-value =
   ## 4.308e-11
   ## alternative hypothesis: true probability of success is not equal to 0.5
   ## 95 percent confidence interval:
   ##  0.6068703 0.6948191
   ## sample estimates:
   ## probability of success
   ##              0.6518047

Lesa má geysimiklar upplýsingar úr úttakinu. Fyrst sjáum við að fjöldi
heppnaðra tilrauna (sem í þessu tilviki er fjöldi kvenna) er 307,
heildarfjöldi nemenda er 471 og p-gildi tilgátuprófsins er
:math:`4.3078955\times 10^{-11}`.

Næst sjáum við hver gagntilgáta tilgátuprófsins er og þar á eftir 95%
öryggisbil fyrir hlutfallið, sem reyndist
:math:`[0.6068703, 0.6948191]`. Að lokum sjáum við sjálft matið á
hlutfalli kvenna í námskeiðinu, :math:`\hat{p} = 0.6518047`.

.. _s.tvohlutfoll:

Ályktanir um tvö eða fleiri hlutföll
------------------------------------

Ályktanir um tvö eða fleiri hlutföll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Viljum við draga ályktanir um tvö eða fleiri hlutföll getum við ekki
lengur notað ``binom.test()`` skipunina. Þess í stað notum við skipunina
``prop.test()`` sem byggir á normalnálgun. Hún gefur sömu niðurstöðu og
algengar aðferðir sem hægt er að reikna í höndunum og eru kenndar í
flestum kennslubókum.

prop.test()
^^^^^^^^^^^

.. attention::

    **Inntak:** tafla - úttak úr table
    
    **Úttak:** gildi á prófstærð, p-gildi, öryggisbil ofl.
    
    **Helstu stillingar:** conf.level, p


--------------

Skoðum nú hvort kynjahlutfallið sé það sama í námskeiðunum LAN203 og
STAE209. Byrjum sem fyrr á því að skoða hvert kynjahlutfallið er með
``prop.table()`` (kassi :numref:`%s <rf.prop.table>`).

::

   prop.table(table(puls$kyn, puls$namskeid),margin=2)
   ##
   ##          LAN203   STAE209
   ##   kvk 0.6453488 0.6555184
   ##   kk  0.3546512 0.3444816

Tilgátuprófið, öryggisbilið, prófstærðin og tilgátuprófið fást öll í
einu með einni skipun:

::

   prop.test(table(puls$namskeid, puls$kyn))
   ##
   ##  2-sample test for equality of proportions with continuity
   ##  correction
   ##
   ## data:  table(puls$namskeid, puls$kyn)
   ## X-squared = 0.015035, df = 1, p-value = 0.9024
   ## alternative hypothesis: two.sided
   ## 95 percent confidence interval:
   ##  -0.10426340  0.08392429
   ## sample estimates:
   ##    prop 1    prop 2
   ## 0.6453488 0.6555184

Fyrst sjáum við að prófstærðin er 0.015035, sem fylgir kí-kvaðrat prófi
með 1 frígráðu og p-gildi tilgátuprófsins er 0.9024.

Næst sjáum við hver gagntilgáta tilgátuprófsins er og þar á eftir 95%
öryggisbil fyrir mismun hlutfallanna, sem reyndist
:math:`[-0.1042634, 0.0839243]`.

Að lokum sjáum við sjálf mötin á hlutfalli kvenna í námskeiðunum
tveimur, 0.6453488 og 0.6555184.

Einnig er hægt að nota skipunina ``prop.test()`` til að bera saman
hlutföll fleiri en tveggja hópa. Þá þarf að gæta þess að tengslataflan
snúi rétt, þ.e.a.s. að hún hafi eingöngu tvo dálka en ekki fleiri. Í því
felst að flokkabreytan með fleiri en tvo flokka sé tilgreind á undan
þeirri sem hefur eingöngu tvo flokka:

::

   prop.test(table(puls$likamsraektf, puls$kyn))
   ##
   ##  3-sample test for equality of proportions without continuity
   ##  correction
   ##
   ## data:  table(puls$likamsraektf, puls$kyn)
   ## X-squared = 11.3, df = 2, p-value = 0.003518
   ## alternative hypothesis: two.sided
   ## sample estimates:
   ##    prop 1    prop 2    prop 3
   ## 0.6117647 0.7382199 0.5789474

Sé þessu snúið öfugt fæst villa og ekki er hægt að meta tilgátuprófið:

::

   prop.test(table(puls$kyn, puls$likamsraektf))
   ## Error in prop.test(table(puls$kyn, puls$likamsraektf)): ’x’ must have 2 columns

.. _s.tengslatoflur:

Ályktanir um tengslatöflur
--------------------------

Ályktanir um tengslatöflur
~~~~~~~~~~~~~~~~~~~~~~~~~~

Viljum við kanna hvort samband sé á milli tveggja flokkabreyta er notuð 
``chisq.test()`` aðferðin. Þá skipun er einni hægt að nota
til að bera saman hlutföll tveggja eða fleiri þýða en hún gefur að vísu
ekki öryggisbil eins og ``prop.test()`` skipunin.

chisq.test()
^^^^^^^^^^^^

.. attention::

    **Inntak:** tafla - úttak úr table
    
    **Úttak:** gildi á prófstærð, p-gildi, ofl.
    
    **Helstu stillingar:** conf.level, simulate.p.value


--------------

Könnum nú hvort samband sé á milli námskeiðs og líkamsræktarástundunar.
Við byrjum á að búa til töflu mældrar tíðni:

::

   chisq.test(table(puls$namskeid,puls$likamsraektf))
   ##
   ##  Pearson's Chi-squared test
   ##
   ## data:  table(puls$namskeid, puls$likamsraektf)
   ## X-squared = 4.1576, df = 2, p-value = 0.1251

Hér sést að prófstærðin er 4.1576, sem fylgir kí-kvaðrat prófi með 2
frígráður og p-gildi tilgátuprófsins er 0.1251.

Munið að til þess að geta notað kí-kvaðrat prófið þurfa allar tölurnar í
væntitíðnitöflunni að vera stærri en 5. Við getum fengið væntitíðnitöflu
út úr R með að vista það sem ``chisq.test()`` aðferðin skilar sem hlut
(hann má heita hvað sem er) og draga svo ``expected`` hlutann fram:

::

   kikv1<-chisq.test(table(puls$namskeid,puls$likamsraektf))
   kikv1$expected
   ##
   ##              Lítil  Miðlungs     Mikil
   ##   LAN203  31.19099  70.08798  69.72103
   ##   STAE209 53.80901 120.91202 120.27897

Ef einhverjar tölur eru minni en fimm í væntitíðnitöflunni varar R okkur
við. Sjáum til dæmis hvað gerist ef við viljum skoða samband reykinga og
hreyfingar fyrir eingöngu þá nemendur sem sátu námskeiðið árið 2013:

::

   puls2013 <- filter(puls, ar==2013)
   chisq.test(table(puls2013$reykir,puls2013$likamsraektf))
   
   ## Warning in chisq.test(table(puls2013$reykir, puls2013$likamsraektf)):
   ## Chi-squared approximation may be incorrect
   
   ##
   ##  Pearson's Chi-squared test
   ##
   ## data:  table(puls2013$reykir, puls2013$likamsraektf)
   ## X-squared = 11.247, df = 2, p-value = 0.003612

Þá getum við annað hvort reiknað prófstærðina með endurvalsaðferðum, sem
er tilgreint með stillingunni ``simulate.p.value``:

::

   chisq.test(table(puls2013$reykir,puls2013$likamsraektf), simulate.p.value=TRUE)
   ##
   ##  Pearson's Chi-squared test with simulated p-value (based on 2000
   ##  replicates)
   ##
   ## data:  table(puls2013$reykir, puls2013$likamsraektf)
   ## X-squared = 11.247, df = NA, p-value = 0.002999

eða þá framkvæmt annað tilgátupróf sem kallast Fisher próf. Það er gert
með skipuninni ``fisher.test()``:

::

   fisher.test(table(puls2013$reykir,puls2013$likamsraektf))
   ##
   ##  Fisher's Exact Test for Count Data
   ##
   ## data:  table(puls2013$reykir, puls2013$likamsraektf)
   ## p-value = 0.001259
   ## alternative hypothesis: two.sided

fisher.test()
^^^^^^^^^^^^^

.. attention::

    **Inntak:** tafla - úttak úr table
    
    **Úttak:** gildi á prófstærð, p-gildi, öryggisbil ofl.
    
    **Helstu stillingar:** conf.level, p


--------------


Leiksvæði fyrir R kóða
----------------------

Hér fyrir neðan er hægt að skrifa R kóða og keyra hann. Notið þetta svæði til að prófa ykkur áfram með skipanir kaflans. Athugið að við höfum þegar sett inn skipun til að lesa inn ``puls`` gögnin sem eru notuð gegnum alla bókina.

.. datacamp::
    :lang: r

    # Gogn sott og sett i breytuna puls.
    puls <- read.table ("https://edbook.hi.is/gogn/pulsAll.csv", header=TRUE, sep=";")

    # Setjid ykkar eigin koda her fyrir nedan:
    # Sem daemi, skipunin head(puls) skilar fyrstu nokkrar radirnar i gognunum
    # asamt dalkarheitum.
    head(puls)