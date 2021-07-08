Ályktanir um talnabreytur
=========================

Í þessum kafla munum við skoða aðferðir til að kanna ályktanir um
meðaltöl og dreifni talnabreyta. Tilgátur rannsakenda miðast oft að því
að því að kanna meðaltöl, oftar en ekki að bera tvö meðaltöl saman. Áður
en það er gert er þó ávallt gott (oft nauðsynlegt) að kanna hvort
breytileiki í þýðunum/breytunum sem við erum að rannsaka sé svipaður.

Við byrjum á að kanna mun á dreifni í tveimur (``var.test()``) eða
fleiri normaldreifðum þýðum (``bartlett.test()``). Við vindum okkur svo
í að framkvæma tilgátupróf og smíða öryggisbil fyrir meðaltöl í einu eða
tveimur þýðum. Ef úrtak er nægjanlega stór má ætíð framkvæma slík próf
með z-prófi og sé úrtakið lítið má nota t-próf ef breytan er
normaldreifð. T-prófið er íhaldssamara en z-prófið, þ.e.a.s. ef við
framkvæmum bæði t-próf og z-próf á sömu gögnunum þá mun t-prófið
hafa minni villulíkur. Því er hægt að réttlæta notkun t-prófs alltaf
þegar skilyrði fyrir z-próf eru uppfyllt. Gætið ykkar að það gildir ekki
í hina áttina. Því eru t-próf innbyggð í flest tölfræðiforrit, þar með
talið R, en z-próf eru minna notuð. Viljum við kanna meðaltöl í fleirum
en tveimur þýðum er það gert með einþátta fervikagreiningu en hún er
umfjöllunarefni kafla :numref:`%s <c.fervikagreining>`.

.. _s.dreifni:

Ályktanir um dreifni
--------------------

Dreifni í tveimur þýðum
~~~~~~~~~~~~~~~~~~~~~~~

var.test()
^^^^^^^^^^

.. attention::

    **Inntak:** nöfn á tveimur talnabreytum eða nafn á talnabreytu og
    flokkabreytu
    
    **Úttak:** gildi á prófstærð, p-gildi, öryggisbil og fleira
    
    **Helstu stillingar:** alternative, conf.level


--------------

Við mötum ``var.test()`` aðferðina á mismunandi hátt eftir því hvort
gögnin okkar séu á löngu eða víðu sniði (sjá kafla :numref:`%s <s.umrodun>`).
Algengast er að gögn séu á löngu sniði en þá inniheldur ein breyta
mælingar á talnabreytunni og gildin á annarri breytu gefa til kynna
hvaða hópi hver og ein mæling tilheyrir. Hins vegar geta gögnin verið á
víðu sniði þar sem búið er að skipta talnabreytunni upp í tvær breytur,
eina fyrir hvorn hóp.

Gerum nú ráð fyrir að við höfum normaldreifða breytu mælda í tveimur
þýðum og látum :math:`\sigma_1^2` tákna dreifni þýðis 1 og
:math:`\sigma_2^2` tákna dreifni þýðis 2. Gerum fyrst ráð fyrir að
mælingarnar séu vistaðar á víðu sniði, í breytunum
``breyta1`` og ``breyta2``. Til að kanna hvort dreifni þýðanna sé mismunandi
notum við:

::

   var.test(breyta1,breyta2)

Ef við erum aftur á móti með mælingarnar okkar á löngu sniði þar sem
mælingarnar okkar eru geymdar í breytunni ``maeling`` og flokkabreytan
(``hopur``) inniheldur gildi sem gefa til kynna í hvaða flokki
mælingarnar tilheyra mötum við aðferðina með:

::

   var.test(maeling~hopur)

Núlltilgátan er: :math:`H_0: \sigma^2_1 = \sigma^2_2`, en með
stillingunni ``alternative`` ráðum við gagntilgátunni.

+-------------------------+-----------------------------------------+
| stilling                | gagntilgáta                             |
+=========================+=========================================+
| alternative=“two.sided” | :math:`H_1: \sigma^2_1 \neq \sigma^2_2` |
+-------------------------+-----------------------------------------+
| alternative=“greater”   | :math:`H_1: \sigma^2_1 > \sigma^2_2`    |
+-------------------------+-----------------------------------------+
| alternative=“less”      | :math:`H_1: \sigma^2_1 < \sigma^2_2`    |
+-------------------------+-----------------------------------------+

Viljum við kanna hvort dreifni í púls sé mismunandi á milli kynjanna
gerum við það með (takið eftir að gögnin eru á löngu sniði):

::

   var.test(puls$fyrriPuls~puls$kyn)
   ##
   ##  F test to compare two variances
   ##
   ## data:  puls$fyrriPuls by puls$kyn
   ## F = 1.2512, num df = 293, denom df = 159, p-value = 0.1155
   ## alternative hypothesis: true ratio of variances is not equal to 1
   ## 95 percent confidence interval:
   ##  0.9461411 1.6360633
   ## sample estimates:
   ## ratio of variances
   ##           1.251186

Úr úttakinu má lesa m.a. eftirfarandi:

-  Gildið á prófstærðinni: :math:`f` = 1.2512

-  p-gildið: 0.1155

-  Öryggisbilið: 95 percent confidence interval:
   :math:`[0.9461411, 1.6360633]`

Við sjáum að p-gildið er hátt svo við höfnum ekki núlltilgátunni (m.v.
:math:`\alpha = 0.05`) og drögum því enga ályktun. Við sjáum líka að 95%
öryggisbil fyrir hlutfallið á dreifninni er
:math:`[0.9461411, 1.6360633]`. Hlutlausa ástandið er að hlutfallið sé 1
(því þá er dreifnin jöfn í báðum hópum) og þar sem öryggisbilið
inniheldur töluna 1 höfnum við ekki núlltilgátunni í samræmi við það sem
p-gildið segir.

Dreifni í fleiri þýðum
~~~~~~~~~~~~~~~~~~~~~~

bartlett.test()
^^^^^^^^^^^^^^^

.. attention::

    **Inntak:** nöfn á talnabreytu og flokkabreytu
    
    **Úttak:** gildi á prófstærð, p-gildi, öryggisbil og fleira
    
    **Helstu stillingar:**


--------------

Þegar þýðin/hóparnir eru fleiri en tveir má nota ``bartlett.test()``
aðferðina. Við þurfum að mata aðferðina með vigri sem inniheldur
mælingarnar okkar og annan vigur sem tilgreinir hvaða hópi mælingarnar
tilheyra. Við notum svo ``bartlett.test()`` aðferðina til að kanna hvort
munur sé á dreifni hópanna. Við mötum aðferðina með

::

   bartlett.test(maeling ~ hopur)

Viljum við kanna hvort dreifnin er ólík í púlsmælingum í
líkamsræktarhópunum þremur gerum við það með:

::

   bartlett.test(puls$fyrriPuls ~ puls$likamsraektf)
   ##
   ##  Bartlett test of homogeneity of variances
   ##
   ## data:  puls$fyrriPuls by puls$likamsraektf
   ## Bartlett's K-squared = 4.1246, df = 2, p-value = 0.1272

Við sjáum að gildið á prófstærðinni er :math:`4.1246` og p-gildið er
:math:`0.1272`. P-gildið er hærra en 0.05 og því getum við ekki ályktað
að dreifnin sé misjöfn í hópunum.

Ályktanir um meðaltöl
---------------------

Ályktanir um meðaltöl
~~~~~~~~~~~~~~~~~~~~~

t.test()
^^^^^^^^

.. attention::

    **Inntak:** nöfn á einni eða tveimur talnabreytum eða nafn á talnabreytu
    og flokkabreytu
    
    **Úttak:** gildi á prófstærð, p-gildi, öryggisbil og fleira
    
    **Helstu stillingar:** paired, mu, alternative, conf.level


--------------

T-próf eru framkvæmd með skipuninni ``t.test()``. Hana má nota nota til
að draga ályktanir um meðaltöl eins þýðis, samanburð tveggja þýða jafnt
og samanburð paraðra mælinga, allt eftir því á hverju hún er mötuð og
hvaða stillingar eru gefnar. Fyrst munum við sjá hvernig skipunin er
notuð til að draga ályktanir um meðaltal þýðis. Að því loknu sjáum við
hvernig við berum saman meðaltöl tveggja þýða og að lokum berum við
saman paraðar mælingar.

.. _s.eittmedaltal:

Ályktanir um eitt meðaltal
~~~~~~~~~~~~~~~~~~~~~~~~~~

Þegar skipunin ``t.test()`` er mötuð með einungis einni breytu
framkvæmir hún t-próf fyrir eitt meðaltal. Aðrar stillingar eru:

-  ``mu``: Við prófum tilgátuprófið :math:`H_0: \mu =` ``mu``. ``mu`` er
   því viðmiðunargildi núlltilgátunnar.

-  ``alternative``: Við gefum skipunina ``alternative="two.sided"`` ef
   gagntilgátan er tvíhliða, ``alternative="greater"`` ef gagntilgátan
   er :math:`\mu > \mu_0` og ``alternative="less"`` ef gagntilgátan er
   :math:`\mu < \mu_0`. Sjálfgefið er að hafa tvíhliða gagntilgátu.

-  ``conf.level``: Þar tilgreinum við hvert öryggið (og þá um leið
   villulíkurnar) á að vera fyrir tilgátuprófið og öryggisbilið.
   Sjálfgefið er að hafa öryggið :math:`1-\alpha` = 0.95.

Sjálfgefið er að kanna núlltilgátuna: :math:`H_0: \mu=0`. Slíkur
samanburður er óáhugaverður ef við viljum t.d. kanna fyrri púls nemenda
því vonandi voru nemendurnir ekki dauðir úr öllum æðum á þeim
mánudagsmorgnum sem tilraunin var framkvæmd. Könnum frekar hvort púlsinn
sé frábrugðinn 70 og tilgreinum það með stillingunni ``mu``.

::

   t.test(puls$fyrriPuls,mu=70)
   ##
   ##  One Sample t-test
   ##
   ## data:  puls$fyrriPuls
   ## t = 3.5612, df = 453, p-value = 0.0004082
   ## alternative hypothesis: true mean is not equal to 70
   ## 95 percent confidence interval:
   ##  70.88843 73.07633
   ## sample estimates:
   ## mean of x
   ##  71.98238

Í úttakinu eru fólgnar gífurlegar upplýsingar. Við fáum:

-  Prófstærðina: t = 3.5612

-  Fjölda frígráða: 453

-  p-gildið: :math:`4.0820624\times 10^{-4}`

-  Öryggisbilið, með örygginu tilgreindu: 95 percent confidence
   interval: :math:`[70.8884,73.0763]`

-  Úrtaksmeðaltalið: mean of x 71.9824

.. _s.tvomedaltol:

Ályktanir um mismun tveggja meðaltala
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Þegar draga á ályktanir um mismun meðaltala tveggja þýða
:math:`\mu_1-\mu_2` og þegar framkvæma á tilgátupróf fyrir paraðar
mælingar geta gögnin okkar verið á mismunandi formi. Annars vegar geta
gögnin verið á löngu sniði, þar sem að ein breyta inniheldur mælingarnar
á talnabreytunni og önnur breyta tilgreinir hvaða hópi hver og ein
mæling tilheyrir. Algengast er að gögn séu geymd á slíku sniði og eru
púlsgögnin dæmi. Hins vegar geta gögnin verið á víðu sniði þar sem búið
er að skipta talnabreytunni upp í tvær breytur, eina fyrir hvorn hóp.

Við mötum ``t.test()`` aðferðina á mismunandi vegu eftir því á hvaða
sniði gögnin eru. Enn fremur er hægt að gefa eftirfarandi stillingar

-  ``mu``: Við prófum tilgátuprófið :math:`H_0: \mu_1 - \mu_2 =` ``mu``.
   ``mu`` er því viðmiðunargildi núlltilgátunnar.

-  ``conf.level``: Þar tilgreinum við hvert öryggið (og þá um leið
   villulíkurnar) á að vera fyrir tilgátuprófið og öryggisbilið.
   Sjálfgefið er að hafa öryggið :math:`1-\alpha` = 0.95.

-  ``alternative``: Við gefum skipunina ``alternative="two.sided"`` ef
   gagntilgátan er tvíhliða, ``alternative="greater"`` ef gagntilgátan
   er :math:`\mu_1 - \mu_2 > \delta` og ``alternative="less"`` ef
   gagntilgátan er :math:`\mu_1 - \mu_2 < \delta`. Sjálfgefið er að hafa
   tvíhliða gagntilgátu.

Segjum sem svo að við viljum bera saman fyrri púls nemenda eftir kynjum.
Þar sem púls gögnin eru á löngu sniði gefum við skipunina:

::

   t.test(puls$fyrriPuls~puls$kyn)
   ##
   ##  Welch Two Sample t-test
   ##
   ## data:  puls$fyrriPuls by puls$kyn
   ## t = 2.6808, df = 358.94, p-value = 0.007684
   ## alternative hypothesis: true difference in means is not equal to 0
   ## 95 percent confidence interval:
   ##  0.8000951 5.2065375
   ## sample estimates:
   ## mean in group kvk  mean in group kk
   ##          73.04082          70.03750

Í úttakinu eru fólgnar gífurlegar upplýsingar. Við fáum:

-  Prófstærðina: t = 2.6808

-  Fjölda frígráða: 358.9407899

-  p-gildið: 0.0076844

-  Öryggisbilið, með örygginu tilgreindu: 95 percent confidence
   interval: :math:`[0.8001,5.2065]`

-  Úrtaksmeðaltölin: 73.0408, 70.0375

Séu gögnin á víðu sniði er ``t.test()`` mötuð með breytunum tveimur sem
bera á saman. Í þessu tilviki komum við púlsgögnunum á vítt snið með
aðstoð skipunarinnar ``spread()``, sem kynnt var í kassa
:numref:`%s <rf.spread>`.

::

   pulsvid <- spread(puls, kyn, fyrriPuls)

Hérna framkvæmum við sama t-prófið með skipuninni:

::

   t.test(pulsvid$kvk, pulsvid$kk)
   ##
   ##  Welch Two Sample t-test
   ##
   ## data:  pulsvid$kvk and pulsvid$kk
   ## t = 2.6808, df = 358.94, p-value = 0.007684
   ## alternative hypothesis: true difference in means is not equal to 0
   ## 95 percent confidence interval:
   ##  0.8000951 5.2065375
   ## sample estimates:
   ## mean of x mean of y
   ##  73.04082  70.03750

.. _s.fleirimedaltol:

Ályktanir um mismun fleiri meðaltala
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Eins og fjallað hefur verið um má nota z- og t-próf til að kanna mun á
meðaltölum í tveimur þýðum. Viljum við kanna mun á meðaltölum í fleiri
en tveimur þýðum notum við einþátta fervikagreiningu en hún er
umfjöllunarefni kafla :numref:`%s <c.fervikagreining>`.

.. _s.paradar:

Ályktanir um mismun meðaltala paraðra mælinga
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Þegar t-próf er framkvæmt fyrir mismun paraðra mælinga er skipunin
``t.test()`` mötuð með stillingunni:

-  paired=TRUE

Annars er skipunin mötuð á nákvæmlega sama hátt og í kafla
:numref:`%s <s.tvomedaltol>` þegar borin eru saman tvö meðaltöl.

Þegar t-próf er framkvæmt til að bera saman mismun paraðra mælinga er
enn fremur hægt að gefa aðferðinni eftirfarandi stillingar:

-  ``mu``: Við prófum tilgátuprófið :math:`H_0: \mu_d=` ``mu``. ``mu``
   er því viðmiðunargildi núlltilgátunnar.

-  ``conf.level``. Þar tilgreinum við hvert öryggið (og þá um leið
   villulíkurnar) á að vera fyrir tilgátuprófið og öryggisbilið.
   Sjálfgefið er að hafa öryggið :math:`1-\alpha` = 0.95.

-  ``alternative``: Við gefum skipunina ``alternative=”two.sided”`` ef
   gagntilgátan er tvíhliða, ``alternative=”greater”`` ef gagntilgátan
   er :math:`\mu_d > \delta` og ``alternative=”less”`` ef gagntilgátan
   er :math:`\mu_d < \delta`. Sjálfgefið er að hafa tvíhliða
   gagntilgátu.

-  ``conf.level``: Þar tilgreinum við hvert öryggið (og þá um leið
   villulíkurnar) á að vera fyrir tilgátuprófið og öryggisbilið.
   Sjálfgefið er að hafa öryggið :math:`1-\alpha` = 0.95.

Í púlsgögnunum liggur beint við að bera saman fyrri og seinni púls
þeirra nemenda sem að hlupu í eina mínútu. Einnig væri áhugavert að
kanna mun á fyrri og seinni. Byrjum á því að búa til tvær minni
gagnatöflur, eina fyrir þá nemendur sem hlupu og aðra fyrir þá sem hlupu
ekki.

::

   pulshljop <- filter(puls, inngrip=='hljop')
   pulskyrr<- filter(puls, inngrip=='sat_kyrr')

Könnum tilgátuna að púlsinn sé frábrugðinn fyrir og eftir krónukastið
fyrir þá sem hlupu. Athugið að núna eru pöruðu mælingarnar tvær geymdar
í tveimur dálkum og því eru gögnin á víðu sniði með því tilliti. Því
mötum við skipunina á eftirfarandi hátt:

::

   t.test(pulshljop$fyrriPuls, pulshljop$seinniPuls, paired=TRUE)
   ##
   ##  Paired t-test
   ##
   ## data:  pulshljop$fyrriPuls and pulshljop$seinniPuls
   ## t = -19.421, df = 179, p-value < 2.2e-16
   ## alternative hypothesis: true difference in means is not equal to 0
   ## 95 percent confidence interval:
   ##  -28.40310 -23.16357
   ## sample estimates:
   ## mean of the differences
   ##               -25.78333

Í úttakinu sjáum við:

-  Prófstærðina: t = :math:`-19.421`

-  Fjölda frígráða: 179

-  p-gildið: :math:`6.1948544\times 10^{-46}`

-  Öryggisbilið, með örygginu tilgreindu: 95 percent confidence
   interval: :math:`-28.4031`, :math:`-23.1636`

-  Úrtaksmeðaltal mismunanna: mean of the differences
   :math:`[-28.4031,-23.1636]`

Við höfnum því núlltilgátunni og fullyrðum að munur sé á fyrri og seinni
púls þeirra nemenda sem hlupu í eina mínútu.

Berum því næst saman púls þeirra nemenda sem sátu kyrrir á meðan hinir
púluðu.

::

   t.test(pulskyrr$fyrriPuls, pulskyrr$seinniPuls, paired=TRUE)
   ##
   ##  Paired t-test
   ##
   ## data:  pulskyrr$fyrriPuls and pulskyrr$seinniPuls
   ## t = -0.22089, df = 273, p-value = 0.8253
   ## alternative hypothesis: true difference in means is not equal to 0
   ## 95 percent confidence interval:
   ##  -0.7597236  0.6064389
   ## sample estimates:
   ## mean of the differences
   ##             -0.07664234

Hér er p-gildið :math:`0.825344` og þar af leiðandi getum við ekki
hafnað núlltilgátunni og megum því ekki draga ályktanir út frá
tilgátuprófinu. Við megum þó ekki gleyma því að heilmiklar upplýsingar
eru fólgnar í öryggisbilinu fyrir mismun mælinganna. Öryggisbilið er
:math:`[-0.7597,0.6064]` svo við getum fullyrt með 95% vissu að púlsinn
hafi ekki minnkað um meira en :math:`-0.7597` slög á mínútu og ekki
hækkað um meira en :math:`0.6064` slög á mínútu. Við getum því hæglega
fullyrt að breyting púlsins sé innan við eitt slag á mínútu.

Levene próf fyrir dreifni\ :math:`^\ast`
----------------------------------------

Ef gögnin okkar fylgja normaldreifingu er Bartlett prófið sem fjallað
var um hér að framan besta prófið að nota til að kanna hvort munur sé á
dreifni hópanna. Ef gögnin fylgja ekki normaldreifingu er betra að nota
svo kallað Levene-próf. Skipunin ``leveneTest()`` sem tilheyrir ``car``
pakkanum framkvæmir Levene próf.

.. _s.stikalaus:

Stikalaus próf\ :math:`^\ast`
-----------------------------

Stikalaus próf\ :math:`^\ast`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef skilyrði þess að hægt sé að framkvæma t-próf eru ekki uppfyllt er í
sumum tilvikum hægt að nota stikalaus próf þeirra í stað. Algengasta
stikalausa prófið er Wilcox prófið sem hægt er framkvæma með skipuninni
``wilcox.test()``.

wilcox.test()
^^^^^^^^^^^^^

.. attention::

    **Inntak:** nöfn á einni eða tveimur talnabreytum eða nafn á talnabreytu
    og flokkabreytu
    
    **Úttak:** gildi á prófstærð, p-gildi
    
    **Helstu stillingar:** paired, mu, alternative


--------------

Prófið má framkvæma til að kanna eitt miðgildi eða bera saman tvö
miðgildi og þá einnig fyrir paraðar mælingar. Skipunin er mötuð á sama
hátt og ``t.test()``. Gætið ykkar að stikalaus próf geta einnig verið
skilyrðum háð. Sem dæmi þá krefst óparaða Wilcox prófið þess að eini
munurinn á dreifingu breytanna tveggja sé hliðrun um fasta tölu og því á
það ekki við ef breytileiki breytanna er ólíkur.

Hér fyrir neðan má sjá sömu dæmi og hér að ofan framkvæmd með
``wilcos.test()``:

::

   wilcox.test(puls$fyrriPuls,mu=70)
   ##
   ##  Wilcoxon signed rank test with continuity correction
   ##
   ## data:  puls$fyrriPuls
   ## V = 51812, p-value = 0.003055
   ## alternative hypothesis: true location is not equal to 70

::

   ##
   ##  Wilcoxon rank sum test with continuity correction
   ##
   ## data:  puls$fyrriPuls by puls$kyn
   ## W = 26878, p-value = 0.01187
   ## alternative hypothesis: true location shift is not equal to 0

::

   wilcox.test(pulshljop$fyrriPuls, pulshljop$seinniPuls, paired=TRUE)
   ##
   ##  Wilcoxon signed rank test with continuity correction
   ##
   ## data:  pulshljop$fyrriPuls and pulshljop$seinniPuls
   ## V = 8, p-value < 2.2e-16
   ## alternative hypothesis: true location shift is not equal to 0

::

   wilcox.test(pulskyrr$fyrriPuls, pulskyrr$seinniPuls, paired=TRUE)
   ##
   ##  Wilcoxon signed rank test with continuity correction
   ##
   ## data:  pulskyrr$fyrriPuls and pulskyrr$seinniPuls
   ## V = 13897, p-value = 0.9758
   ## alternative hypothesis: true location shift is not equal to 0


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