.. _c.tvikostaadhvarf:

Tvíkosta aðhvarfsgreining
=========================

Á eftir línulegri aðhvarfsgreiningu, sem við fjölluðum um í kafla
:numref:`%s <c.linulegtadhvarf>`, er tvíkosta aðhvarfsgreining sennilega mest
notaða aðhvarfsgreiningarlíkanið. Í R er tvíkosta aðhvarfsgreining
framkvæmd á mjög sambærilegan hátt og línuleg aðhvarfsgreining, nema nú
er notast við fallið ``glm()`` í stað fallsins ``lm()``. Í tvíkosta
aðhvarfsgreiningu hefur svarbreytan eingöngu tvær útkomur, 0 og 1 og eru
líkönin því metin með aðstoð tengifalla. Algengasta tengifallið kallast
á ensku the logistic function og því er oft talað um lógistíska
aðhvarfsgreiningu. Í raun má nota fallið ``glm()`` til að framkvæma
fjölda annarra alhæfðra línulegra aðhvarfsgreiningarlíkana en það er
utan efnis þessarar bókar.

glm()
^^^^^

.. attention::

    **Inntak:** formúla, gögn (tvíkosta breyta~breyta, gögn)
    
    **Úttak:** tvíkosta aðhvarfsgreining á gögnunum byggt á formúlunni
    
    **Helstu stillingar:** family

    **Forkröfur prófs:** ??


--------------

Auk fallsins ``glm()`` munum við einnig nota skipanirnar ``summary()``,
``coef()`` og ``confint()`` á svipaðan hátt og þið sáuð í kafla
:numref:`%s <c.linulegtadhvarf>`.

Í kafla :numref:`%s <s.tvikostasamfelld>` sýnum við hvernig tvíkosta
aðhvarfsgreining er framkvæmd þegar skýribreytan er samfelld en í kafla
:numref:`%s <s.tvikostastrjal>` sýnum við hvað gerist þegar skýribreytan er
strjál. Við munum finna möt á stikum líkansins, framkvæma tilgátupróf
fyrir þá og reikna öryggisbil.

.. _s.tvikostasamfelld:

Tvíkosta aðhvarfsgreining með samfellda skýribreytu
---------------------------------------------------

Tvíkosta aðhvarfsgreiningu má nota til að meta hvort nemendur sem koma 
gangandi eða skokkandi í skólann séu ólíklegri til að vera lengi á leiðinni 
í skólann heldur en þeir sem ferðast á skólann á annan máta. Líkanið metum
við með neðangreindri skipun og það borgar sig að vista líkanið sem hlut.

::

   glm1<-glm(ferdamati_skoli=='Gangandi / skokkandi'~ferdatimi_skoli, data=konnun, family='binomial')

Fyrsta inntakið í skipunina er formúla. Á vinstri hönd hennar verður að
vera breyta sem tekur gildin 0 og 1, eða þá TRUE og FALSE. Í þessu dæmi
er inntakið yrðingin ``ferdamati_skoli=='Gangandi / skokkandi'`` sem skilar TRUE ef
einstaklingurinn kemur gangandi í skólann en FALSE annars. Þar af leiðandi mun líkanið
meta gagnlíkindin á því að koma gangandi. Á hægri hönd formúlunnar er
skýribreytan, sem í þessu tilviki er ``ferdatimi_skoli``.
er inntakið yrðingin ``ferdamati_skoli=='Gangandi / skokkandi'`` sem skilar TRUE ef
einstaklingurinn kemur gangandi í skólann en FALSE annars. Þar af leiðandi mun líkanið
meta gagnlíkindin á því að koma gangandi. Á hægri hönd formúlunnar er
skýribreytan, sem í þessu tilviki er ``ferdatimi_skoli``.

Næstu tvö inntök skipunarinnar er nafnið á gagnatöflunni sem geymir
gögnin (``konnun``) og af hvaða gerð aðhvarfsgreiningarlíkanið er. Með
stillingunni ``family=’binomial’`` tilgreinum við að tvíkosta
aðhvarfsgreining skuli framkvæmd með logistic tengifallinu.

Skipunin ``summary()`` gefur okkur miklar upplýsingar um útkomu
aðhvarfsgreiningarinnar:

::

   summary(glm1)
   ##
   ## Call:
   ## glm(formula = ferdamati_skoli == "Gangandi / skokkandi" ~ ferdatimi_skoli, 
   ##     family = "binomial", data = konnun)
   ## 
   ## Coefficients:
   ##                 Estimate Std. Error z value Pr(>|z|)    
   ## (Intercept)      0.68296    0.39389   1.734   0.0829 .  
   ## ferdatimi_skoli -0.18181    0.03693  -4.923 8.54e-07 ***
   ##                 Estimate Std. Error z value Pr(>|z|)    
   ## (Intercept)      0.68296    0.39389   1.734   0.0829 .  
   ## ferdatimi_skoli -0.18181    0.03693  -4.923 8.54e-07 ***
   ## ---
   ## Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
   ## 
   ## Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
   ## 
   ## (Dispersion parameter for binomial family taken to be 1)
   ## 
   ##     Null deviance: 182.73  on 200  degrees of freedom
   ## Residual deviance: 133.79  on 199  degrees of freedom
   ## AIC: 137.79
   ## 
   ## Number of Fisher Scoring iterations: 7
   ## 
   ##     Null deviance: 182.73  on 200  degrees of freedom
   ## Residual deviance: 133.79  on 199  degrees of freedom
   ## AIC: 137.79
   ## 
   ## Number of Fisher Scoring iterations: 7

Mikilvægustu upplýsingarnar úr aðhvarfsgreiningunni eru fólgnar í
töflunni ``Coefficients:``

-  Í fyrsta dálki hennar má sjá metnu stuðlana,
   :math:`\hat \beta_0 = 0.68296` og :math:`\hat \beta_1 = -0.18181`.
   :math:`\hat \beta_0 = 0.68296` og :math:`\hat \beta_1 = -0.18181`.

-  Staðalskekkju fyrir mat á stuðlunum má sjá í öðrum dálki.

-  Í þriðja dálki má sjá prófstærðir fyrir tilgátupróf sem prófa
   núlltilgátuna hvort stuðlarnir séu núll. Þannig prófar prófstærðin
   :math:`1.734` núlltilgátuna :math:`\beta_0 = 0` og prófstærðin
   :math:`-4.923` prófar núlltilgátuna :math:`\beta_1=0`.
   :math:`1.734` núlltilgátuna :math:`\beta_0 = 0` og prófstærðin
   :math:`-4.923` prófar núlltilgátuna :math:`\beta_1=0`.

-  P-gildin sem svara til þessara prófstærða má svo finna í fjórða
   dálkinum. P-gildið fyrir núlltilgátuna :math:`\beta_1=0` er
   :math:`8.54e-07`, sem er minna en 0.05 og þar sem stuðullin er
   neikvæður getum við fullyrt að nemendur sem eru lengi á leiðinni í skólann
   séu ólíklegri til að fara gangandi heldur en þeir eru fljótir í skólann.
   :math:`8.54e-07`, sem er minna en 0.05 og þar sem stuðullin er
   neikvæður getum við fullyrt að nemendur sem eru lengi á leiðinni í skólann
   séu ólíklegri til að fara gangandi heldur en þeir eru fljótir í skólann.

Með því að setja metnu stuðlana í veldið á e fæst gagnlíkindahlutfall
fyrir því að fara gangandi við hverja aukna mínútu sem að nemandi
eyðir í að komast í skólann. Þau finnum við með skipuninni:
fyrir því að fara gangandi við hverja aukna mínútu sem að nemandi
eyðir í að komast í skólann. Þau finnum við með skipuninni:

::

   exp(coef(glm1))
   ##     (Intercept) ferdatimi_skoli 
   ##       1.9797338       0.8337605
   ##     (Intercept) ferdatimi_skoli 
   ##       1.9797338       0.8337605

Í flestum tilvikum höfum við lítin áhuga á gagnlíkindahlutfallinu sem 
svarar til ``(Intercept)``. Hins vegar höfum við mikinn áhuga á 
gagnlíkindahlutfallinu sem stendur við ``ferdatimi_skoli``.
Hér sjáum við að gagnlíkindahlutfallið fyrir því að fara gangandi við
hverja auka mínútu sem að nemandi eyðir í að komast í skólann
er :math:`0.8337605`.
gagnlíkindahlutfallinu sem stendur við ``ferdatimi_skoli``.
Hér sjáum við að gagnlíkindahlutfallið fyrir því að fara gangandi við
hverja auka mínútu sem að nemandi eyðir í að komast í skólann
er :math:`0.8337605`.

95% öryggisbil fyrir gagnlíkindahlutföllin sem fengust í tvíkosta
aðhvarfsgreiningunni má finna með skipuninni:

::

   exp(confint(glm1))
   ##                     2.5 %    97.5 %
   ## (Intercept)     0.9289593 4.3876029
   ## ferdatimi_skoli 0.7694803 0.8901376
   ##                     2.5 %    97.5 %
   ## (Intercept)     0.9289593 4.3876029
   ## ferdatimi_skoli 0.7694803 0.8901376

Sem fyrr höfum við ekki áhuga á öryggisbilinu sem svarar til
``(Intercept)``. Öryggisbilið fyrir ``ferdatimi_skoli`` er það sem við
viljum skoða, það er :math:`[0.7694803, 0.8901376]`. Öryggisbilið
``(Intercept)``. Öryggisbilið fyrir ``ferdatimi_skoli`` er það sem við
viljum skoða, það er :math:`[0.7694803, 0.8901376]`. Öryggisbilið
inniheldur ekki 1 í samræmi við það að við höfnuðum núlltilgátunni.

.. _s.tvikostastrjal:

Tvíkosta aðhvarfsgreining með strjála skýribreytu
-------------------------------------------------

Tvíkosta aðhvarfsgreiningu má einnig beita á strjála skýribreytu. Til
dæmis til að meta hvort nemendur sem eru femínistar séu líklegri til að
vera kattamanneskjur heldur en þeir sem eru ekki femínistar. Líkanið metum við með
dæmis til að meta hvort nemendur sem eru femínistar séu líklegri til að
vera kattamanneskjur heldur en þeir sem eru ekki femínistar. Líkanið metum við með
neðangreindri skipun:

::

   glm2<-glm(feministi=='Rétt'~dyr, data=konnun, family='binomial')

Skipunin lítur á nákvæmlega sama hátt út og í kafla
:numref:`%s <s.tvikostasamfelld>` nema að nú hefur ``feministi=='Rétt'`` komið í stað 
``ferdamati_skoli=='Gangandi / skokkandi'`` og breytan ``dyr`` tekið
stað breytunnar ``ferdatimi_skoli``. Skoðum nú ``summary()`` af útkomu
:numref:`%s <s.tvikostasamfelld>` nema að nú hefur ``feministi=='Rétt'`` komið í stað 
``ferdamati_skoli=='Gangandi / skokkandi'`` og breytan ``dyr`` tekið
stað breytunnar ``ferdatimi_skoli``. Skoðum nú ``summary()`` af útkomu
aðhvarfsgreiningarinnar:

::

   summary(glm2)
   ##
   ## Call:
   ## glm(formula = feministi == "Rétt" ~ dyr, family = "binomial", 
   ##     data = konnun)
   ## 
   ## Coefficients:
   ##             Estimate Std. Error z value Pr(>|z|)    
   ## (Intercept)   1.1304     0.2066   5.472 4.45e-08 ***
   ## dyrKetti      2.4532     0.7460   3.288  0.00101 ** 
   ##             Estimate Std. Error z value Pr(>|z|)    
   ## (Intercept)   1.1304     0.2066   5.472 4.45e-08 ***
   ## dyrKetti      2.4532     0.7460   3.288  0.00101 ** 
   ## ---
   ## Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
   ## 
   ## Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
   ## 
   ## (Dispersion parameter for binomial family taken to be 1)
   ## 
   ##     Null deviance: 179.51  on 200  degrees of freedom
   ## Residual deviance: 159.55  on 199  degrees of freedom
   ## AIC: 163.55
   ## 
   ## 
   ##     Null deviance: 179.51  on 200  degrees of freedom
   ## Residual deviance: 159.55  on 199  degrees of freedom
   ## AIC: 163.55
   ## 
   ## Number of Fisher Scoring iterations: 6

Mikilvægustu upplýsingarnar úr aðhvarfsgreiningunni eru sem fyrr fólgnar
í töflunni ``Coefficients:``. Taflan er einnig byggð upp á sama hátt en
nú birtist sér lína fyrir hvern flokk skýribreytunnar, annan en
viðmiðunarflokkinn. Þannig gefur heitið í línunni ``dyrKetti`` að um
sé að ræða stuðla fyrir flokkinn ``Ketti`` í skýribreytunni ``feministi`` og
viðmiðunarflokkurinn er því ``Hunda``.
viðmiðunarflokkinn. Þannig gefur heitið í línunni ``dyrKetti`` að um
sé að ræða stuðla fyrir flokkinn ``Ketti`` í skýribreytunni ``feministi`` og
viðmiðunarflokkurinn er því ``Hunda``.

-  Í fyrsta dálki töflunnar má sjá metnu stuðlana,
   :math:`\hat \beta = 1.1304` og :math:`\hat \beta_a = 2.4532`.
   :math:`\hat \beta = 1.1304` og :math:`\hat \beta_a = 2.4532`.

-  Í þriðja dálki má sjá að prófstærðin :math:`5.472` prófa
   núlltilgátuna :math:`\beta = 0` og prófstærðin :math:`3.288` prófar
-  Í þriðja dálki má sjá að prófstærðin :math:`5.472` prófa
   núlltilgátuna :math:`\beta = 0` og prófstærðin :math:`3.288` prófar
   núlltilgátuna :math:`\beta_a=0`.

-  P-gildið fyrir núlltilgátuna :math:`\beta_a=0` er :math:`0.00101`, sem
   er minna en 0.05 og þar sem stuðullin er jákvæður getum við fullyrt
   að nemendur sem eru hrifnir af köttum séu líklegri til vera femínistar heldur
   en þeir sem eru hrifnir af hundum.
-  P-gildið fyrir núlltilgátuna :math:`\beta_a=0` er :math:`0.00101`, sem
   er minna en 0.05 og þar sem stuðullin er jákvæður getum við fullyrt
   að nemendur sem eru hrifnir af köttum séu líklegri til vera femínistar heldur
   en þeir sem eru hrifnir af hundum.

Með því að setja metnu stuðlana í veldið á e fæst gagnlíkindahlutfall
fyrir því að vera femínisti á móti því að vera hrifinn af köttum. Þau finnum við með
fyrir því að vera femínisti á móti því að vera hrifinn af köttum. Þau finnum við með
skipuninni:

::

   exp(coef(glm2))
   ## (Intercept)    dyrKetti 
   ##    3.096774   11.625000 
   ## (Intercept)    dyrKetti 
   ##    3.096774   11.625000 

Við höfum ekki áhuga á gagnlíkindahlutfallinu sem svarar til ``(Intercept)``,
en það sem stendur við ``dyrKetti`` sýnir okkur gagnlíkindahlutfallið
fyrir því að vera femínisti því að vera hrifinn af köttum er :math:`11.625000`.
en það sem stendur við ``dyrKetti`` sýnir okkur gagnlíkindahlutfallið
fyrir því að vera femínisti því að vera hrifinn af köttum er :math:`11.625000`.

95% öryggisbil fyrir gagnlíkindahlutföllin sem fengust í tvíkosta
aðhvarfsgreiningunni má finna með skipuninni:

::

   exp(confint(glm2))
   ##                2.5 %    97.5 %
   ## (Intercept) 2.091788  4.715258
   ## dyrKetti    3.366706 73.263708
   ##                2.5 %    97.5 %
   ## (Intercept) 2.091788  4.715258
   ## dyrKetti    3.366706 73.263708

Sem fyrr höfum við ekki áhuga á öryggisbilinu sem svarar til
``(Intercept)``, heldur það sem stendur við ``dyrKetti``, það er
:math:`[3.366706, 73.263708]`. Öryggisbilið inniheldur ekki 1 í samræmi
``(Intercept)``, heldur það sem stendur við ``dyrKetti``, það er
:math:`[3.366706, 73.263708]`. Öryggisbilið inniheldur ekki 1 í samræmi
við það að við höfnuðum núlltilgátunni.


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
