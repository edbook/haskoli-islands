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

    **Inntak:** formúla, gögn
    
    **Úttak:** tvíkosta aðhvarfsgreining á gögnunum byggt á formúlunni
    
    **Helstu stillingar:** family


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

Tvíkosta aðhvarfsgreiningu má nota til að meta hvort nemendur sem stunda
mikla líkamsrækt séu ólíklegri til að reykja heldur en þá sem stunda
litla líkamsrækt. Líkanið metum við með neðangreindri skipun og það
borgar sig að vista líkanið sem hlut.

::

   glm1 <- glm(reykir=='ja' ~ likamsraekt, data=puls, family='binomial')

Fyrsta inntakið í skipunina er formúla. Á vinstri hönd hennar verður að
vera breyta sem tekur gildin 0 og 1, eða þá TRUE og FALSE. Í þessu dæmi
er inntakið yrðingin ``reykir==’ja’`` sem skilar TRUE ef
einstaklingurinn reykir en FALSE annars. Þar af leiðandi mun líkanið
meta gagnlíkindin á því að reykja. Á hægri hönd formúlunnar er
skýribreytan, sem í þessu tilviki er ``likamsraekt``.

Næstu tvö inntök skipunarinnar er nafnið á gagnatöflunni sem geymir
gögnin (``puls``) og af hvaða gerð aðhvarfsgreiningarlíkanið er. Með
stillingunni ``family=’binomial’`` tilgreinum við að tvíkosta
aðhvarfsgreining skuli framkvæmd með logistic tengifallinu.

Skipunin ``summary()`` gefur okkur miklar upplýsingar um útkomu
aðhvarfsgreiningarinnar:

::

   summary(glm1)
   ##
   ## Call:
   ## glm(formula = reykir == "ja" ~ likamsraekt, family = "binomial",
   ##     data = puls)
   ##
   ## Deviance Residuals:
   ##     Min       1Q   Median       3Q      Max
   ## -0.5680  -0.4825  -0.4566  -0.3864   3.0534
   ##
   ## Coefficients:
   ##             Estimate Std. Error z value Pr(>|z|)
   ## (Intercept)  -1.7428     0.2482  -7.023 2.18e-12 ***
   ## likamsraekt  -0.1164     0.0547  -2.127   0.0334 *
   ## ---
   ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
   ##
   ## (Dispersion parameter for binomial family taken to be 1)
   ##
   ##     Null deviance: 293.2  on 452  degrees of freedom
   ## Residual deviance: 287.9  on 451  degrees of freedom
   ##   (18 observations deleted due to missingness)
   ## AIC: 291.9
   ##
   ## Number of Fisher Scoring iterations: 5

Mikilvægustu upplýsingarnar úr aðhvarfsgreiningunni eru fólgnar í
töflunni ``Coefficients:``

-  Í fyrsta dálki hennar má sjá metnu stuðlana,
   :math:`\hat \beta_0 = -1.7428` og :math:`\hat \beta_1 = -0.1164`.

-  Staðalskekkju fyrir mat á stuðlunum má sjá í öðrum dálki.

-  Í þriðja dálki má sjá prófstærðir fyrir tilgátupróf sem prófa
   núlltilgátuna hvort stuðlarnir séu núll. Þannig prófar prófstærðin
   :math:`-7.023` núlltilgátuna :math:`\beta_0 = 0` og prófstærðin
   :math:`-2.127` prófar núlltilgátuna :math:`\beta_1=0`.

-  P-gildin sem svara til þessara prófstærða má svo finna í fjórða
   dálkinum. P-gildið fyrir núlltilgátuna :math:`\beta_1=0` er
   :math:`0.0334`, sem er minna en 0.05 og þar sem stuðullin er
   neikvæður getum við fullyrt að nemendur sem stunda mikla líkamsrækt
   séu ólíklegri til að reykja heldur en þeir sem stunda litla
   líkamsrækt.

Með því að setja metnu stuðlana í veldið á e fæst gagnlíkindahlutfall
fyrir því að reykja við hverja aukna klukkustund sem að einstaklingur
stundar líkamsrækt á viku. Þau finnum við með skipuninni:

::

   exp(coef(glm1))
   ## (Intercept) likamsraekt
   ##   0.1750381   0.8901369

Í flestum tilvikum höfum við lítin áhuga á gagnlíkindahlutfallinu sem 
svarar til ``(Intercept)``. Hins vegar höfum við mikinn áhuga á 
gagnlíkindahlutfallinu sem stendur við ``likamsraekt``.
Hér sjáum við að gagnlíkindahlutfallið fyrir því að reykja við
hverja aukna klukkustund sem að einstaklingur stundar líkamsrækt á viku
er :math:`0.8901369`.

95% öryggisbil fyrir gagnlíkindahlutföllin sem fengust í tvíkosta
aðhvarfsgreiningunni má finna með skipuninni:

::

   exp(confint(glm1))
   ##                 2.5 %    97.5 %
   ## (Intercept) 0.1061636 0.2811427
   ## likamsraekt 0.7941909 0.9840247

Sem fyrr höfum við ekki áhuga á öryggisbilinu sem svarar til
``(Intercept)``. Öryggisbilið fyrir ``likamsraekt`` er það sem við
viljum skoða, það er :math:`[0.7941909, 0.9840247]`. Öryggisbilið
inniheldur ekki 1 í samræmi við það að við höfnuðum núlltilgátunni.

.. _s.tvikostastrjal:

Tvíkosta aðhvarfsgreining með strjála skýribreytu
-------------------------------------------------

Tvíkosta aðhvarfsgreiningu má einnig beita á strjála skýribreytu. Til
dæmis til að meta hvort nemendur sem drekka áfengi séu líklegri til að
reykja heldur en þá sem ekki drekka áfengi. Líkanið metum við með
neðangreindri skipun:

::

   glm2 <- glm(reykir=='ja' ~ drekkur, data=puls, family='binomial')

Skipunin lítur á nákvæmlega sama hátt út og í kafla
:numref:`%s <s.tvikostasamfelld>` nema að nú hefur breytan ``drekkur`` tekið
stað breytunnar ``likamsraekt``. Skoðum nú ``summary()`` af útkomu
aðhvarfsgreiningarinnar:

::

   summary(glm2)
   ##
   ## Call:
   ## glm(formula = reykir == "ja" ~ drekkur, family = "binomial",
   ##     data = puls)
   ##
   ## Deviance Residuals:
   ##     Min       1Q   Median       3Q      Max
   ## -0.5007  -0.5007  -0.5007  -0.1684   2.9198
   ##
   ## Coefficients:
   ##             Estimate Std. Error z value Pr(>|z|)
   ## (Intercept)  -2.0134     0.1587 -12.686   <2e-16 ***
   ## drekkurnei   -2.2351     1.0190  -2.193   0.0283 *
   ## ---
   ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
   ##
   ## (Dispersion parameter for binomial family taken to be 1)
   ##
   ##     Null deviance: 297.59  on 452  degrees of freedom
   ## Residual deviance: 287.48  on 451  degrees of freedom
   ##   (18 observations deleted due to missingness)
   ## AIC: 291.48
   ##
   ## Number of Fisher Scoring iterations: 6

Mikilvægustu upplýsingarnar úr aðhvarfsgreiningunni eru sem fyrr fólgnar
í töflunni ``Coefficients:``. Taflan er einnig byggð upp á sama hátt en
nú birtist sér lína fyrir hvern flokk skýribreytunnar, annan en
viðmiðunarflokkinn. Þannig gefur heitið í línunni ``drekkurnei`` að um
sé að ræða stuðla fyrir flokkinn ``nei`` í skýribreytunni ``drekkur`` og
viðmiðunarflokkurinn er því ``ja``.

-  Í fyrsta dálki töflunnar má sjá metnu stuðlana,
   :math:`\hat \beta = -2.0134` og :math:`\hat \beta_a = -2.2351`.

-  Í þriðja dálki má sjá að prófstærðin :math:`-12.686` prófa
   núlltilgátuna :math:`\beta = 0` og prófstærðin :math:`-2.193` prófar
   núlltilgátuna :math:`\beta_a=0`.

-  P-gildið fyrir núlltilgátuna :math:`\beta_a=0` er :math:`0.0283`, sem
   er minna en 0.05 og þar sem stuðullin er neikvæður getum við fullyrt
   að nemendur sem ekki drekka áfengi séu ólíklegri til að reykja heldur
   en þeir sem stunda drekka áfengi.

Með því að setja metnu stuðlana í veldið á e fæst gagnlíkindahlutfall
fyrir því að reykja á móti því að drekka ekki áfengi. Þau finnum við með
skipuninni:

::

   exp(coef(glm2))
   ## (Intercept)  drekkurnei
   ##   0.1335312   0.1069842

Við höfum ekki áhuga á gagnlíkindahlutfallinu sem svarar til ``(Intercept)``,
en það sem stendur við ``drekkurnei`` sýnir okkur gagnlíkindahlutfallið
fyrir því að reykja á móti því að drekka ekki er :math:`0.1069842` sem
telst ansi lítið.

95% öryggisbil fyrir gagnlíkindahlutföllin sem fengust í tvíkosta
aðhvarfsgreiningunni má finna með skipuninni:

::

   exp(confint(glm2))
   ##                   2.5 %    97.5 %
   ## (Intercept) 0.096558897 0.1801504
   ## drekkurnei  0.005988971 0.5029970

Sem fyrr höfum við ekki áhuga á öryggisbilinu sem svarar til
``(Intercept)``, heldur það sem stendur við ``drekkurnei``, það er
:math:`[0.005989, 0.502997]`. Öryggisbilið inniheldur ekki 1 í samræmi
við það að við höfnuðum núlltilgátunni.


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