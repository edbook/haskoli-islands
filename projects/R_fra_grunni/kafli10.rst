.. _c.linulegtadhvarf:

Línuleg aðhvarfsgreining
========================

Aðhvarfsgreining er notuð til að kanna samband milli einnar samfelldrar
svarbreytu og einnar eða fleiri skýribreyta sem geta hvort sem heldur
verið samfelldar eða strjálar. Í einfaldasta tilvikinu er eingöngu ein
samfelld skýribreyta og er þá talað um einfalt línulegt aðhvarf. Því
tilviki helgum við meginhluta kaflans en útfærslur með strjálli
skýribreytu sem og fleiri en einni skýribreytu eru ræddar undir lok
hans.

Í kafla :numref:`%s <s.likanmetid>` kynntum við skipunina ``lm()`` sem metur
einfalt línulegt aðhvarf og skoðum úttak hennar með ``summary()``. Þar
næst, í kafla :numref:`%s <s.lmoryggis>`, skoðum við hvernig skipunin
``confint()`` gefur okkur öryggisbil fyrir stuðla líkansins. Í kafla
:numref:`%s <s.lmleifar>` könnum við mátgæði líkansins með fallinu ``resid()``
og í kafla :numref:`%s <s.lmspa>` sjáum við hvernig framkvæma má spár með
fallinu ``predict()``. Að lokum fjallar kafli :numref:`%s <s.onnurprof>` um
hvernig framkvæma má tilgátupróf fyrir fylgnistuðul með ``cor.test()``.

.. _s.likanmetid:

Línulegt líkan smíðað
---------------------

Línulegt líkan smíðað
~~~~~~~~~~~~~~~~~~~~~

lm()
^^^^

.. attention::

    **Inntak:** formúlan sem við viljum meta, gögnin sem við byggjum á
    
    **Úttak:** metnir stuðlar, p-gildi, skýringarhlutfall ofl.


--------------

Einfalt línulegt aðhvarfsgreiningarlíkan er líkan á forminu:

.. math:: y = \beta_0 + \beta_1 x

Aðferðin ``lm()`` metur gildi stikanna :math:`\beta_0` og
:math:`\beta_1` ásamt ýmiss annars. Hún er mötuð með tvennu:

-  Formúlu með heitum breytanna sem lýsir sambandinu sem við viljum
   meta. Svarbreytan er vinstra megin við :math:`\sim` merkið, en hægra
   megin koma skýribreyturnar.

-  Gagnatöflunni sem geymir gögnin.

Þegar aðhvarfsgreining er framkvæmd margborgar sig að búa til hlut sem
inniheldur allt það sem hún skilar. Metum nú stuðla í líkani sem lýsir
því hvaða áhrif hæð hefur á þyngd nemenda og vistum líkanið undir
nafninu ``lm1``. Þar sem við metum áhrif hæðar á þyngd er svarbreytan
``thyngd`` vinstra megin í formúlunni.

::

   lm1<-lm(thyngd~haed,data=puls)
   names(lm1)
   ##  [1] "coefficients"  "residuals"     "effects"       "rank"
   ##  [5] "fitted.values" "assign"        "qr"            "df.residual"
   ##  [9] "na.action"     "xlevels"       "call"          "terms"
   ## [13] "model"

Eins og þið sjáið eru þarna heilmargt að finna. Þar við bætist að
skipunina ``summary()`` má, líkt og svo oft áður, mata með
aðhvarfsgreiningarhlutnum ``lm1`` til að fá ýmsar upplýsingar:

::

   summary(lm1)
   ##
   ## Call:
   ## lm(formula = thyngd ~ haed, data = puls)
   ##
   ## Residuals:
   ##     Min      1Q  Median      3Q     Max
   ## -27.781  -7.473  -1.984   5.306  37.215
   ##
   ## Coefficients:
   ##               Estimate Std. Error t value Pr(>|t|)
   ## (Intercept) -108.75402    9.18021  -11.85   <2e-16 ***
   ## haed           1.03987    0.05288   19.66   <2e-16 ***
   ## ---
   ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
   ##
   ## Residual standard error: 11.17 on 458 degrees of freedom
   ##   (11 observations deleted due to missingness)
   ## Multiple R-squared:  0.4577, Adjusted R-squared:  0.4566
   ## F-statistic: 386.6 on 1 and 458 DF,  p-value: < 2.2e-16

Ýmislegt má lesa út úr úttakinu. Þar ber helst að:

-  Matið á skurðpunktinum (:math:`b_0`) er -108.75402.

-  Matið á hallatölunni (:math:`b_1`) er 1.03987.

-  Prófstærðin t = -11.85 kannar tilgátuprófið hvort :math:`\beta_0 = 0`.

-  Prófstærðin t = 19.66 kannar tilgátuprófið hvort :math:`\beta_1 = 0`.

-  Skýringarhlutfallið er :math:`R^2` = 0.458.

-  Matið á :math:`\sigma` er :math:`s_e =` 11.17.

.. _s.lmoryggis:

Öryggisbil fyrir stuðla líkansins
---------------------------------

Öryggisbil fyrir stuðla líkansins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

confint()
^^^^^^^^^

.. attention::

    **Inntak:** metið líkan
    
    **Úttak:** öryggisbil fyrir stuðla líkansins
    
    **Helstu stillingar:** level


--------------

Öryggisbil fyrir :math:`\beta_0` og :math:`\beta_1` má finna með
skipuninni ``confint()``. Hún er mötuð með aðhvarfsgreiningarhlutnum sem
við bjuggum til en skilar öryggisbili fyrir hvorn stuðul fyrir sig. Með
stillingunni ``level`` má tilgreina hvert öryggi bilsins er. Sjálfgefið
er að það sé 95%.

::

   confint(lm1)
   ##                    2.5 %     97.5 %
   ## (Intercept) -126.7945689 -90.713462
   ## haed           0.9359419   1.143796

Hér sést að:

-  Öryggisbil fyrir :math:`\beta_0` er :math:`[-126.7945689, -90.7134618]`.

-  Öryggisbil fyrir :math:`\beta_1` er :math:`[0.9359419, 1.1437964]`.

.. _s.lmleifar:

Mátgæði líkansins könnuð
------------------------

Forsenda aðhvarfsgreiningar er að leifar hennar séu óháðar og
normaldreifðar, með sömu dreifni. Leifarnar má nálgast með:

::

   lm1$resid
   ##            1            2            4            5            6
   ##   1.33508486  31.37822565  -5.18321388  -3.74465341 -14.22308301
   ##            7            8            9           10           11
   ##  -6.34269041   4.13901085  -6.26295215   7.73704785  -6.78125088
   ##           12           13           14           15           16
   ....

Gott er að teikna normaldreifingarrit af leifunum. Takið eftir því að
hér mötum við skipunina ``ggplot()`` með aðhvarfsgreiningarhlutnum
``lm1``, en ekki gagnatöflunni ``puls``.

::

   ggplot(data=lm1, aes(sample=.resid)) + stat_qq()

.. figure:: myndir/unnamed-chunk-235-1.svg

.. _s.lmspa:

Spágildi og spábil
------------------

Spágildi og spábil
~~~~~~~~~~~~~~~~~~

predict()
^^^^^^^^^

.. attention::

    **Inntak:** metið líkan, gagnatafla með gildum skýribreytanna sem á að
    spá fyrir með
    
    **Úttak:** spá og spábil
    
    **Helstu stillingar:** level


--------------

Við getum spáð fyrir gildi á svarbreytunni fyrir ákveðið gildi á
skýribreytunni með aðferðinni ``predict()``. Mata þarf aðferðina með
nafninu á aðhvarfsgreiningarhlutnum, nafninu á skýribreytunni og
gagnatöflu sem inniheldur þau gildi á skýribreytunni sem við viljum fá
spá fyrir. Hér fyrir neðan reiknum við spá fyrir þyngd einstaklings serm
er 180 cm á hæð:

::

   predict(lm1,newdata=data.frame(haed=180))
   ##        1
   ## 78.42243

Aðferðina má einnig nota til að fá spábil:

::

   predict(lm1,interval="prediction",newdata=data.frame(haed=180))
   ##        fit      lwr      upr
   ## 1 78.42243 56.43465 100.4102

.. _s.onnurprof:

Próf á fylgnistuðli
-------------------

Tilgátupróf fyrir :math:`\rho` má framkvæma með ``cor.test()``
aðferðinni. Við þurfum að mata aðferðina með heitunum á breytunum sem
við ætlum að kanna fylgnina á milli. Viljum við kanna fylgnina á milli
breytanna ``thyngd`` og ``haed`` notum við skipunina:

::

   cor.test(puls$thyngd,puls$haed)
   ##
   ##  Pearson's product-moment correlation
   ##
   ## data:  puls$thyngd and puls$haed
   ## t = 19.663, df = 458, p-value < 2.2e-16
   ## alternative hypothesis: true correlation is not equal to 0
   ## 95 percent confidence interval:
   ##  0.6237265 0.7232602
   ## sample estimates:
   ##       cor
   ## 0.6765718

Takið eftir að prófstærðin er t = 19.663 sem er nákvæmlega það sama og
þegar við prófuðum núlltilgátuna :math:`H_0: \beta_1=0`.

.. _s.lmstrjal:

Strjál skýribreyta
------------------

Í kafla :numref:`%s <c.fervikagreining>` fjölluðum við um einþátta
fervikagreiningu en líta má á fervikagreiningu sem sértilfelli af
aðhvarfsgreiningu þegar skýribreyta er strjál. Einþátta fervikagreiningu
má skrifa sem línulegt líkan á eftirfarandi hátt:

.. math:: y_{ij}  = \mu + \tau_i  + \varepsilon_{ij}

þar sem :math:`i = 1,2,...,a` og :math:`j = 1,2,...,n`. Hér gerum við
ráð fyrir að við höfum jafn margar mælingar í hverjum flokki/hópi
(:math:`n`).

-  :math:`y_{ij}` er mæling nr. :math:`j` í hópi/flokki nr. :math:`i`.

-  :math:`\mu` er heildarmeðaltalið.

-  :math:`\tau_i` er frávik flokks nr. :math:`i` frá heildarmeðaltalinu :math:`\mu`.

-  :math:`\varepsilon_{ij}` eru frávik mælingar nr. :math:`j` frá
   gildinu :math:`\mu + \tau_i` sem henni tilheyrir, við köllum
   :math:`\varepsilon_{ij}` *leifar* (e. residuals).

Við sáum í kafla :numref:`%s <c.fervikagreining>` að nota má ``aov()`` aðferðina
og ``anova()`` aðferðirnar til að fá fervikagreiningartöfluna. Í stað
``aov()`` aðferðarinnar má nota ``lm()`` aðferðina líkt og við gerðum
hér að ofan fyrir línulegu aðhvarfsgreininguna. Skoðum aftur samband
``fyrriPuls`` og ``likamsraektf`` en notum nú ``lm()`` aðferðina:

::

   lm.puls <- lm(fyrriPuls ~ likamsraektf, data = puls)

Við getum fengið fervikasummutöfluna á sama hátt og áður með ``anova()``
aðferðinni:

::

   anova(lm.puls)
   ## Analysis of Variance Table
   ##
   ## Response: fyrriPuls
   ##               Df Sum Sq Mean Sq F value    Pr(>F)
   ## likamsraektf   2   2580  1289.9  9.5055 9.065e-05 ***
   ## Residuals    446  60521   135.7
   ## ---
   ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

en við getum einnig fengið möt á stikum líkansins með ``summary()``
aðferðinni:

::

   summary(lm.puls)
   ##
   ## Call:
   ## lm(formula = fyrriPuls ~ likamsraektf, data = puls)
   ##
   ## Residuals:
   ##     Min      1Q  Median      3Q     Max
   ## -31.217  -8.217  -0.148   6.783  46.783
   ##
   ## Coefficients:
   ##                      Estimate Std. Error t value Pr(>|t|)
   ## (Intercept)            75.148      1.294  58.060  < 2e-16 ***
   ## likamsraektfMiðlungs   -1.931      1.553  -1.243 0.214522
   ## likamsraektfMikil      -6.012      1.553  -3.871 0.000125 ***
   ## ---
   ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
   ##
   ## Residual standard error: 11.65 on 446 degrees of freedom
   ##   (22 observations deleted due to missingness)
   ## Multiple R-squared:  0.04088,    Adjusted R-squared:  0.03658
   ## F-statistic: 9.505 on 2 and 446 DF,  p-value: 9.065e-05

Hægt er að stilla hvaða *samanburðarstuðla* (e. contrasts) eru notaðir en
sjálfgegna stillingin er að nota svo kallaða *contr.treatment* en þá er
lægsti flokkur flokkabreytu valinn sem viðmiðunarflokkur. Í einþátta
fervikagreiningu má lesa matið fyrir viðmiðunarflokkinn úr
``(Intercept)`` línunni og finna svo matið fyrir hina flokkana með að
leggja gildið á viðkomandi stika við matið fyrir viðmiðunarflokkinn.

Í dæminu hér að ofan má því lesa eftirfarandi:

-  Matið á fyrri púls í flokknum sem stundar litla líkamsrækt er 75.148.

-  Matið á fyrri púls í flokknum sem stundar miðlungs líkamsrækt er
   75.148 + (-1.931) = 73.217.

-  Matið á fyrri púls í flokknum sem stundar mikla líkamsrækt er 75.148
   + (-6.012) = 69.136.

.. _s.lmfleiribreytur:

Fleiri skýribreytur\ :math:`^\ast`
----------------------------------

Eins og fjallað var um í hluta :numref:`%s <s.aovfleiribreytur>` má mata
``aov()`` aðferðina með fleiri en einum þætti. Sömu sögu er að segja um
``lm()`` aðferðina. Mötum við hana með fleiri en einni samfelldri breytu
smíðum við fjölvítt aðhvarfsgreiningrlíkan, með fleiri en einni
flokkabreytu smíðum við fjölþátta fervikagreiningarlíkan en ef
skýribreyturnar eru sambland af samfeldum breytum og flokkabreytur
smíðum við samvikagreiningarlíkan (ANCOVA). Það er gríðarlega margt sem
hafa þarf í huga þegar líkön af þessum gerðum eru smíðuð og verður ekki
farið í það nánar hér en líkt og greint var frá í kafla
:numref:`%s <s.aovfleiribreytur>` geta ``add1()``, ``drop1()`` og ``step()``
aðferðirnar komið að góðum notum þegar velja á skýribreytur í líkanið.


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