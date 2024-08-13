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
hvort hlutfall þeirra sem eru hrifinn af hundum og þeirra sem eru hrifinn af köttum
sé jafnt í nemendahópnum sem konnun gögnin byggja á.

binom.test()
^^^^^^^^^^^^

.. attention::

    **Inntak:** tafla - úttak úr table
    
    **Úttak:** gildi á prófstærð, p-gildi, öryggisbil ofl.
    
    **Helstu stillingar:** conf.level, p

    **Forkröfur prófs:** Engar

    **Forkröfur prófs:** Engar


--------------

Byrjum á því að nota ``prop.table()`` skipunina, (kassa
:numref:`%s <rf.prop.table>`) til að sjá hvert uppáhalds dýr fólks er:
:numref:`%s <rf.prop.table>`) til að sjá hvert uppáhalds dýr fólks er:

::

   prop.table(table(konnun$dyr))
   ##
   ##     Hunda     Ketti 
   ## 0.6318408 0.3681592
   ##     Hunda     Ketti 
   ## 0.6318408 0.3681592

Tilgátuprófið, öryggisbilið og prófstærðin fást öll í
einu með einni skipun:

::

   binom.test(table(konnun$dyr))
   ##
   ##  Exact binomial test
   ## 
   ## data:  table(konnun$dyr)
   ## number of successes = 127, number of trials = 201, p-value = 0.0002267
   ## alternative hypothesis: true probability of success is not equal to 0.5
   ## 95 percent confidence interval:
   ##  0.5611205 0.6986092
   ##  0.5611205 0.6986092
   ## sample estimates:
   ## probability of success 
   ##              0.6318408 

   ## probability of success 
   ##              0.6318408 


Lesa má geysimiklar upplýsingar úr úttakinu. Fyrst sjáum við að fjöldi
heppnaðra tilrauna (sem í þessu tilviki er fjöldi þeirra sem er hrifinn af hundum) er 127,
heildarfjöldi nemenda er 201 og p-gildi tilgátuprófsins er
:math:`0.0002267`.
heppnaðra tilrauna (sem í þessu tilviki er fjöldi þeirra sem er hrifinn af hundum) er 127,
heildarfjöldi nemenda er 201 og p-gildi tilgátuprófsins er
:math:`0.0002267`.

Næst sjáum við hver gagntilgáta tilgátuprófsins er og þar á eftir 95%
öryggisbil fyrir hlutfallið, sem reynist
:math:`[0.5611205, 0.6986092]`. Að lokum sjáum við sjálft matið á
hlutfalli þeirra sem eru hrifinn af hundum í námskeiðinu, :math:`\hat{p} = 0.6318408`.
öryggisbil fyrir hlutfallið, sem reynist
:math:`[0.5611205, 0.6986092]`. Að lokum sjáum við sjálft matið á
hlutfalli þeirra sem eru hrifinn af hundum í námskeiðinu, :math:`\hat{p} = 0.6318408`.

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

    **Forkröfur prófs:** Normalnálgun

    **Forkröfur prófs:** Normalnálgun


--------------

Skoðum nú hvort hlutfall þeirra sem er hrifið af hundum og þeirra sem er hrifið af köttum sé það sama hjá iOS og
Android notendum. Byrjum sem fyrr á því að skoða hvert hlutfallið innan stýrikerfa er með
Skoðum nú hvort hlutfall þeirra sem er hrifið af hundum og þeirra sem er hrifið af köttum sé það sama hjá iOS og
Android notendum. Byrjum sem fyrr á því að skoða hvert hlutfallið innan stýrikerfa er með
``prop.table()`` (kassi :numref:`%s <rf.prop.table>`).

::

   prop.table(table(konnun$dyr, konnun$styrikerfi_simi), margin=2)
   ##
   ##          Android       iOS
   ##  Hunda 0.5957447 0.6428571
   ##  Ketti 0.4042553 0.3571429
   ##          Android       iOS
   ##  Hunda 0.5957447 0.6428571
   ##  Ketti 0.4042553 0.3571429

Tilgátuprófið, öryggisbilið og prófstærðin fást öll í
einu með einni skipun:

::

   prop.test(table(konnun$dyr, konnun$styrikerfi_simi))
   ##
   ##  2-sample test for equality of proportions with continuity
   ##  correction
   ##
   ## data:  table(konnun$styrikerfi_simi, konnun$dyr)
   ## X-squared = 0.17091, df = 1, p-value = 0.6793
   ## alternative hypothesis: two.sided
   ## 95 percent confidence interval:
   ##  -0.2204061  0.1261812
   ##  -0.2204061  0.1261812
   ## sample estimates:
   ##    prop 1    prop 2 
   ## 0.5957447 0.6428571 
   ##    prop 1    prop 2 
   ## 0.5957447 0.6428571 

Fyrst sjáum við að prófstærðin er 0.17091, sem fylgir kí-kvaðrat prófi
með 1 frígráðu og p-gildi tilgátuprófsins er 0.6793.
Fyrst sjáum við að prófstærðin er 0.17091, sem fylgir kí-kvaðrat prófi
með 1 frígráðu og p-gildi tilgátuprófsins er 0.6793.

Næst sjáum við hver gagntilgáta tilgátuprófsins er og þar á eftir 95%
öryggisbil fyrir mismun hlutfallanna, sem reyndist
:math:`[-0.2204061, 0.1261812]`.
:math:`[-0.2204061, 0.1261812]`.

Að lokum sjáum við sjálf mötin á hlutfalli þeirra sem eru hrifinn af hundum eftir stýrikerfi,
0.5957447 hjá Android notendum og 0.6428571 hjá iOS notendum.
Að lokum sjáum við sjálf mötin á hlutfalli þeirra sem eru hrifinn af hundum eftir stýrikerfi,
0.5957447 hjá Android notendum og 0.6428571 hjá iOS notendum.

Einnig er hægt að nota skipunina ``prop.test()`` til að bera saman
hlutföll fleiri en tveggja hópa. Þá þarf að gæta þess að tengslataflan
snúi rétt, þ.e.a.s. að hún hafi eingöngu tvo dálka en ekki fleiri. Í því
felst að flokkabreytan með fleiri en tvo flokka sé tilgreind á undan
þeirri sem hefur eingöngu tvo flokka:

::

   prop.test(table(konnun$is, konnun$dyr))
   ##
   ##  3-sample test for equality of proportions without continuity
   ##  correction
   ##
   ## data:  table(konnun$is, konnun$dyr)
   ## X-squared = 1.0863, df = 2, p-value = 0.5809
   ## alternative hypothesis: two.sided
   ## sample estimates:
   ##    prop 1    prop 2    prop 3 
   ## 0.5897436 0.6703297 0.6056338
   ##    prop 1    prop 2    prop 3 
   ## 0.5897436 0.6703297 0.6056338

Sé þessu snúið öfugt fæst villa og ekki er hægt að meta tilgátuprófið:

::

   prop.test(table(konnun$dyr, konnun$is))
   ## Error in prop.test(table(konnun$dyr, konnun$is)) : 'x' must have 2 columns

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

    **Forkröfur prófs:** Normalnálgun, allar töflur í væntitöflu >5

    **Forkröfur prófs:** Normalnálgun, allar töflur í væntitöflu >5


--------------

Könnum nú hvort samband sé á milli hvaða ís nemendur velja og hvort þau hafi kosið.
Könnum nú hvort samband sé á milli hvaða ís nemendur velja og hvort þau hafi kosið.
Við byrjum á að búa til töflu mældrar tíðni:

::

   chisq.test(table(konnun$is,konnun$kosid))
   ##
   ##  Pearson's Chi-squared test
   ##
   ## data:  table(konnun$is, konnun$kosid)
   ## X-squared = 0.41817, df = 2, p-value = 0.8113

Hér sést að prófstærðin er 0.41817, sem fylgir kí-kvaðrat prófi með 2
frígráðum og p-gildi tilgátuprófsins er 0.8113.
Hér sést að prófstærðin er 0.41817, sem fylgir kí-kvaðrat prófi með 2
frígráðum og p-gildi tilgátuprófsins er 0.8113.

Munið að til þess að geta notað kí-kvaðrat prófið þurfa allar tölurnar í
væntitíðnitöflunni að vera stærri en 5. Við getum fengið væntitíðnitöflu
út úr R með að vista það sem ``chisq.test()`` aðferðin skilar sem hlut
(hann má heita hvað sem er) og draga svo ``expected`` hlutann fram:

::

   kikv1<-chisq.test(table(puls$namskeid,puls$likamsraektf))
   kikv1$expected
   ##
   ##                 Rangt     Rétt
   ##   Jarðaberja 11.05970 27.94030
   ##   Súkkulaði  25.80597 65.19403
   ##   Vanilla    20.13433 50.86567
   ##                 Rangt     Rétt
   ##   Jarðaberja 11.05970 27.94030
   ##   Súkkulaði  25.80597 65.19403
   ##   Vanilla    20.13433 50.86567

Ef einhverjar tölur eru minni en fimm í væntitíðnitöflunni varar R okkur
við. Sjáum til dæmis hvað gerist ef við viljum skoða samband þess að vera vera hrifinn af hundum eða köttum og
hvert nemendur vilja helst fara á stefnumót:

::

   chisq.test(table(konnun$dyr,konnun$stefnumot))
   ##
   ##  Pearson's Chi-squared test
   ##
   ## data:  table(dkonnunat$dyr, konnun$stefnumot)
   ## X-squared = 6.8392, df = 3, p-value = 0.0772 
   ##
   ## Warning message:
   ## In chisq.test(table(konnun$dyr, konnun$stefnumot)) :
   ##   Chi-squared approximation may be incorrect

Þá getum við annað hvort reiknað prófstærðina með endurvalsaðferðum, sem
er tilgreint með stillingunni ``simulate.p.value``:

::

   chisq.test(table(konnun$dyr,konnun$stefnumot), simulate.p.value=T)
   ##
   ##  Pearson's Chi-squared test with simulated p-value (based on 2000
   ##  replicates)
   ##
   ## data:  table(konnun$dyr, konnun$stefnumot)
   ## X-squared = 6.8392, df = NA, p-value = 0.07146 

eða þá framkvæmt annað tilgátupróf sem kallast Fisher próf. Það er gert
með skipuninni ``fisher.test()``:

::

   fisher.test(table(konnun$dyr, konnun$stefnumot))
   ##
   ##  Fisher's Exact Test for Count Data
   ##
   ## data:  table(konnun$dyr, konnun$stefnumot)
   ## p-value = 0.07907
   ## alternative hypothesis: two.sided

fisher.test()
^^^^^^^^^^^^^

.. attention::

    **Inntak:** tafla - úttak úr table
    
    **Úttak:** gildi á prófstærð, p-gildi, öryggisbil ofl.
    
    **Helstu stillingar:** conf.level, p

    **Forkröfur prófs:** Engar

    **Forkröfur prófs:** Engar


--------------


Leiksvæði fyrir R kóða
----------------------

Hér fyrir neðan er hægt að skrifa R kóða og keyra hann. Notið þetta svæði til að prófa ykkur áfram með skipanir kaflans. Athugið að við höfum þegar sett inn skipun til að lesa inn ``puls`` gögnin sem eru notuð gegnum alla bókina.

.. datacamp::
    :lang: r

    # Gogn sott og sett i breytuna puls.
    puls <- read.table ("https://raw.githubusercontent.com/edbook/haskoli-islands/main/pulsAll.csv", header=TRUE, sep=";")

    # Setjid ykkar eigin koda her fyrir nedan:
    # Sem daemi, skipunin head(puls) skilar fyrstu nokkrar radirnar i gognunum
    # asamt dalkarheitum.
    head(puls)
