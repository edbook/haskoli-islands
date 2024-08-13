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

    **Forkröfur prófs:** Normaldreifing

    **Forkröfur prófs:** Normaldreifing


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

Viljum við kanna hvort dreifni í ferðatíma sé mismunandi á milli þeirra sem koma gangandi í skólann
og þeirra sem gera það ekki (takið eftir að gögnin eru á löngu sniði):
Viljum við kanna hvort dreifni í ferðatíma sé mismunandi á milli þeirra sem koma gangandi í skólann
og þeirra sem gera það ekki (takið eftir að gögnin eru á löngu sniði):

::

   var.test(konnun$ferdatimi_skoli~konnun$ferdamati_skoli=="Gangandi / skokkandi")
   ##
   ##  F test to compare two variances
   ##
   ## data:  konnun$ferdatimi_skoli by konnun$ferdamati_skoli == "Gangandi / skokkandi"
   ## F = 5.4739, num df = 166, denom df = 33, p-value = 2.875e-07
   ## alternative hypothesis: true ratio of variances is not equal to 1
   ## 95 percent confidence interval:
   ##  3.053460 8.912866
   ##  3.053460 8.912866
   ## sample estimates:
   ## ratio of variances 
   ##           5.473898
   ## ratio of variances 
   ##           5.473898

Úr úttakinu má lesa m.a. eftirfarandi:

-  Gildið á prófstærðinni: :math:`f` = 5.4739
-  Gildið á prófstærðinni: :math:`f` = 5.4739

-  p-gildið: 2.875e-07
-  p-gildið: 2.875e-07

-  Öryggisbilið: 95 percent confidence interval:
   :math:`[3.053460, 8.912866]`
   :math:`[3.053460, 8.912866]`

Við sjáum að p-gildið er minna en 0.05 svo við höfnum núlltilgátunni
og drögum þá ályktun að munur sé á dreifni ferðatíma eftir því hvort farið sé gangandi eða ekki. 
Við sjáum líka að 95% öryggisbil fyrir hlutfallið á dreifninni er
:math:`[3.053460, 8.912866]`. Hlutlausa ástandið er að hlutfallið sé 1
(því þá er dreifnin jöfn í báðum hópum). Takið eftir að öryggisbilið
inniheldur ekki töluna 1 í samræmi við að við höfnum núlltilgátunni.
Við sjáum að p-gildið er minna en 0.05 svo við höfnum núlltilgátunni
og drögum þá ályktun að munur sé á dreifni ferðatíma eftir því hvort farið sé gangandi eða ekki. 
Við sjáum líka að 95% öryggisbil fyrir hlutfallið á dreifninni er
:math:`[3.053460, 8.912866]`. Hlutlausa ástandið er að hlutfallið sé 1
(því þá er dreifnin jöfn í báðum hópum). Takið eftir að öryggisbilið
inniheldur ekki töluna 1 í samræmi við að við höfnum núlltilgátunni.

Dreifni í fleiri þýðum
~~~~~~~~~~~~~~~~~~~~~~

bartlett.test()
^^^^^^^^^^^^^^^

.. attention::

    **Inntak:** nöfn á talnabreytu og flokkabreytu
    
    **Úttak:** gildi á prófstærð, p-gildi, öryggisbil og fleira

    **Forkröfur prófs:** Normaldreifing

    **Forkröfur prófs:** Normaldreifing


--------------

Þegar þýðin/hóparnir eru fleiri en tveir má nota ``bartlett.test()``
aðferðina. Við þurfum að mata aðferðina með vigri sem inniheldur
mælingarnar okkar og annan vigur sem tilgreinir hvaða hópi mælingarnar
tilheyra. Við notum svo ``bartlett.test()`` aðferðina til að kanna hvort
munur sé á dreifni hópanna. Við mötum aðferðina með

::

   bartlett.test(maeling ~ hopur)

Viljum við kanna hvort dreifni ferðatíma sé ólík á milli 
einhverra tveggja ferðamáta gerum við það með:
Viljum við kanna hvort dreifni ferðatíma sé ólík á milli 
einhverra tveggja ferðamáta gerum við það með:

::

   bartlett.test(konnun$ferdatimi_skoli~konnun$ferdamati_skoli)
   ##
   ##  Bartlett test of homogeneity of variances
   ##
   ## data:  konnun$ferdatimi_skoli by konnun$ferdamati_skoli
   ## Bartlett's K-squared = 31.33, df = 4, p-value = 2.622e-06

Við sjáum að gildið á prófstærðinni er :math:`31.33` og p-gildið er
:math:`2.622e-06`. P-gildið er minna en 0.05 og því höfnum við núlltilgátunni
og ályktum að dreifnin sé misjöfn í einhverjum tveimur hóp.
Við sjáum að gildið á prófstærðinni er :math:`31.33` og p-gildið er
:math:`2.622e-06`. P-gildið er minna en 0.05 og því höfnum við núlltilgátunni
og ályktum að dreifnin sé misjöfn í einhverjum tveimur hóp.

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

    **Forkröfur prófs:** Meðaltöl normaldreifð, þ.e. mörg úrtök eða normaldreifð gögn

    **Forkröfur prófs:** Meðaltöl normaldreifð, þ.e. mörg úrtök eða normaldreifð gögn


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
samanburður er óáhugaverður ef við viljum t.d. kanna ferðatíma nemenda í skólann
því líklega búa mjög fáir nemendur í háskólabíó. Könnum frekar hvort ferðatíminn
sé frábrugðinn 20 og tilgreinum það með stillingunni ``mu``.
samanburður er óáhugaverður ef við viljum t.d. kanna ferðatíma nemenda í skólann
því líklega búa mjög fáir nemendur í háskólabíó. Könnum frekar hvort ferðatíminn
sé frábrugðinn 20 og tilgreinum það með stillingunni ``mu``.

::

   t.test(konnun$ferdatimi_skoli, mu=20)
   ##
   ##  One Sample t-test
   ##
   ## data:  konnun$ferdatimi_skoli
   ## t = -0.57532, df = 200, p-value = 0.5657
   ## alternative hypothesis: true mean is not equal to 20
   ## 95 percent confidence interval:
   ##  17.46685 21.38887
   ##  17.46685 21.38887
   ## sample estimates:
   ## mean of x 
   ##  19.42786 
   ## mean of x 
   ##  19.42786 

Í úttakinu eru fólgnar gífurlegar upplýsingar. Við fáum:

-  Prófstærðina: t = -0.57532
-  Prófstærðina: t = -0.57532

-  Fjölda frígráða: 200
-  Fjölda frígráða: 200

-  p-gildið: :math:`0.5657`
-  p-gildið: :math:`0.5657`

-  Öryggisbilið, með örygginu tilgreindu: 95 percent confidence
   interval: :math:`[17.46685, 21.38887]`
   interval: :math:`[17.46685, 21.38887]`

-  Úrtaksmeðaltalið: mean of x 19.42786
-  Úrtaksmeðaltalið: mean of x 19.42786

.. _s.tvomedaltol:

Ályktanir um mismun tveggja meðaltala
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Þegar draga á ályktanir um mismun meðaltala tveggja þýða
:math:`\mu_1-\mu_2` og þegar framkvæma á tilgátupróf fyrir paraðar
mælingar geta gögnin okkar verið á mismunandi formi. Annars vegar geta
gögnin verið á löngu sniði, þar sem að ein breyta inniheldur mælingarnar
á talnabreytunni og önnur breyta tilgreinir hvaða hópi hver og ein
mæling tilheyrir. Algengast er að gögn séu geymd á slíku sniði og eru
gögnin um ferðatíma og máta dæmi. Hins vegar geta gögnin verið á víðu sniði þar sem búið
gögnin um ferðatíma og máta dæmi. Hins vegar geta gögnin verið á víðu sniði þar sem búið
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
Þar sem ferðatímagögnin eru á löngu sniði gefum við skipunina:
Þar sem ferðatímagögnin eru á löngu sniði gefum við skipunina:

::

   t.test(konnun$ferdatimi_skoli~konnun$ferdamati_skoli=='Gangandi / skokkandi')
   ##
   ## data:  konnun$ferdatimi_skoli by konnun$ferdamati_skoli == "Gangandi / skokkandi"
   ## t = 9.5068, df = 118.32, p-value = 2.889e-16
   ## alternative hypothesis: true difference in means between group FALSE and group TRUE is not equal to 0
   ## 95 percent confidence interval:
   ##  11.28187 17.21830
   ##  11.28187 17.21830
   ## sample estimates:
   ## mean in group FALSE  mean in group TRUE 
   ##           21.838323            7.588235 
   ## mean in group FALSE  mean in group TRUE 
   ##           21.838323            7.588235 

Í úttakinu eru fólgnar gífurlegar upplýsingar. Við fáum:

-  Prófstærðina: t = 9.5068
-  Prófstærðina: t = 9.5068

-  Fjölda frígráða: 118.32
-  Fjölda frígráða: 118.32

-  p-gildið: 2.889e-16
-  p-gildið: 2.889e-16

-  Öryggisbilið, með örygginu tilgreindu: 95 percent confidence
   interval: :math:`[11.28187,17.21830]`
   interval: :math:`[11.28187,17.21830]`

-  Úrtaksmeðaltölin: 21.838323, 7.588235
-  Úrtaksmeðaltölin: 21.838323, 7.588235

Séu gögnin á víðu sniði er ``t.test()`` mötuð með breytunum tveimur sem
bera á saman. Í þessu tilviki komum við ferðatímagögnunum á vítt snið með
aðstoð skipunarinnar ``pivot_wider``, sem kynnt var í kassa
bera á saman. Í þessu tilviki komum við ferðatímagögnunum á vítt snið með
aðstoð skipunarinnar ``pivot_wider``, sem kynnt var í kassa
:numref:`%s <rf.spread>`.

::

   ferdirvitt <- konnun %>% mutate(fotgangandi=(ferdamati_skoli=="Gangandi / skokkandi")) 
                     %>% pivot_wider(names_from=fotgangandi, 
                     values_from=ferdatimi_skoli, names_prefix="Gangandi_")


Athugið að ef við hefðum ekki notað stillinguna ``names_prefix`` hefðum við fengið dálkanöfnin
``TRUE`` og ``FALSE`` en það eru frátekin lykilorð í R. Við hefðum þó geta nálgast dálkana
með því að nota gæsalappir eða úrfellingarmerki, t.d. ``"TRUE"``.
Athugið að ef við hefðum ekki notað stillinguna ``names_prefix`` hefðum við fengið dálkanöfnin
``TRUE`` og ``FALSE`` en það eru frátekin lykilorð í R. Við hefðum þó geta nálgast dálkana
með því að nota gæsalappir eða úrfellingarmerki, t.d. ``"TRUE"``.
Hérna framkvæmum við sama t-prófið með skipuninni:

::

   t.test(ferdirvitt$Gangandi_FALSE, ferdirvitt$Gangandi_TRUE)
   t.test(ferdirvitt$Gangandi_FALSE, ferdirvitt$Gangandi_TRUE)
   ##
   ##  Welch Two Sample t-test
   ##
   ## data:  ferdirvitt$Gangandi_FALSE and ferdirvitt$Gangandi_TRUE
   ## t = 9.5068, df = 118.32, p-value = 2.889e-16
   ## data:  ferdirvitt$Gangandi_FALSE and ferdirvitt$Gangandi_TRUE
   ## t = 9.5068, df = 118.32, p-value = 2.889e-16
   ## alternative hypothesis: true difference in means is not equal to 0
   ## 95 percent confidence interval:
   ##  11.28187 17.21830
   ##  11.28187 17.21830
   ## sample estimates:
   ## mean of x mean of y 
   ## 21.838323  7.588235 
   ## mean of x mean of y 
   ## 21.838323  7.588235 

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

    **Forkröfur prófs:** Munur á dreifingu er hliðrun um fasta

    **Forkröfur prófs:** Munur á dreifingu er hliðrun um fasta


--------------

Prófið má framkvæma til að kanna eitt miðgildi eða bera saman tvö
miðgildi og þá einnig fyrir paraðar mælingar. Skipunin er mötuð á sama
hátt og ``t.test()``. Gætið ykkar að stikalaus próf geta einnig verið
skilyrðum háð. Sem dæmi þá krefst óparaða Wilcox prófið þess að eini
munurinn á dreifingu breytanna tveggja sé hliðrun um fasta tölu og því á
það ekki við ef breytileiki breytanna er ólíkur.

Hér fyrir neðan má sjá sömu dæmi og hér að ofan framkvæmd með
``wilcox.test()``:

::

   wilcox.test(puls$fyrriPuls,mu=70)
   ##
   ##  Wilcoxon signed rank test with continuity correction
   ##
   ## data:  konnun$ferdatimi_skoli
   ## V = 6159, p-value = 0.1073
   ## alternative hypothesis: true location is not equal to 20

::
   
   wilcox.test(konnun$ferdatimi_skoli~konnun$ferdamati_skoli=='Gangandi / skokkandi')
   ##
   ##  Wilcoxon rank sum test with continuity correction
   ##
   ## data:  konnun$ferdatimi_skoli by konnun$ferdamati_skoli == "Gangandi / skokkandi"
   ## W = 4847.5, p-value = 6.877e-11
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
    puls <- read.table ("https://raw.githubusercontent.com/edbook/haskoli-islands/main/pulsAll.csv", header=TRUE, sep=";")

    # Setjid ykkar eigin koda her fyrir nedan:
    # Sem daemi, skipunin head(puls) skilar fyrstu nokkrar radirnar i gognunum
    # asamt dalkarheitum.
    head(puls)
