.. _c.fervikagreining:

Einþátta fervikagreining
========================

Einþátta fervikagreiningu notum við til að álykta hvort meðaltöl tveggja
eða fleiri hópa séu mismunandi. Við munum sýna hvernig má gera það með
``aov()`` og ``anova()`` skipununum. Einþátta fervikagreiningu má einnig
stilla upp sem línulegu líkani og leggja þannig grunnin að fjölþátta
fervikagreiningu. Eins og við munum sjá í kafla :numref:`%s <c.linulegtadhvarf>`
má smíða línuleg líkön með ``lm()`` aðferðinni en þá aðferð munum við
einnig nota um línulega aðhvarfsgreiningu í sama kafla.

Gera þarf ráð fyrir að dreifnin í hópunum sem bornir eru saman sé sú
sama og því skal ávallt skoða gögnin vel áður en fervikagreining er
framkvæmd og mögulega framkvæma tilgátupróf fyrir dreifni eins og lýst
var í kafla :numref:`%s <s.dreifni>`.

Ályktanir um tvö eða fleiri meðaltöl
------------------------------------

Ályktanir um tvö eða fleiri meðaltöl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hér á eftir gerum við ráð fyrir því að gögnin séu á löngu sniði (sjá
kafla :numref:`%s <s.umrodun>`). Önnur breytan er talnabreyta sem inniheldur
mælingarnar á viðfangsefnunum, hin breytan er flokkabreyta sem segir til
um það hvaða hópi hver mæling tilheyrir. Við skulum gera ráð fyrir að
fyrri breytan heiti ``maeling`` en hin ``hopur``.

aov()
^^^^^

.. attention::

    **Inntak:** nöfn á talnabreytu og flokkabreytu
    
    **Úttak:** fervikagreiningarhlutur
    
    **Helstu stillingar:**


--------------

Þegar framkvæma á fervikagreiningu með ``aov()`` er skynsamlegt að vista
úttakið í hlut því eins og við sjáum hér að neðan er ýmislegt að finna í
úttakinu. Hér vistum við það undir nafninu *fervik*.

::

   fervik <- aov(maeling ~ hopur)

Það er mjög mikilvægt að breytan ``hopur`` sé skilgreind sem
flokkabreyta (ef hún er það ekki þarf að nota ``factor()`` aðferðina til
að breyta henni).

anova()
^^^^^^^

.. attention::

    **Inntak:** nafn á fervikagreiningarhlut
    
    **Úttak:** gildi á prófstærð, p-gildi, öryggisbil og fleira
    
    **Helstu stillingar:**


--------------

Til að fá fervikagreiningartöflu mötum við ``anova()`` aðferðina með
fervikagreiningarhlut:

::

   anova(fervik)

Snúum okkur nú að gagnasafninu okkar. Í kafla :numref:`%s <s.kodun>` bjuggum við
til nýja flokkabreytu sem gefur til kynna hvort viðfangsefnin okkar
stundi "litla", "miðlungs" eða "mikla" líkamsrækt. Við reiknuðum svo
meðalpúls einstaklinga í hópunum þremur í kafla :numref:`%s <s.adrargagnlegar>`.
Nú getum við kannað með fervikagreiningu hvort munur sé á meðalpúlsi í
hópunum þremur. Byrjum á því að skoða kassarit af púlsmælingum eftir
líkamsræktarástundun:

::

   gogn <- na.omit(puls) # sleppum NA gildum
   ggplot(data=gogn,aes(likamsraektf,fyrriPuls))+geom_boxplot() +
   xlab("Líkamsræktarástundun") + ylab("Púls (slög/mínútu)")

.. figure:: myndir/unnamed-chunk-217-1.svg

Eins og sjá má myndinni virðist dreifni í hópunum vera nokkuð jöfn.
Því næst framkvæmum við Bartlett prófið fyrir dreifnina:

::

   bartlett.test(fyrriPuls ~ likamsraektf, data = puls)
   ##
   ##  Bartlett test of homogeneity of variances
   ##
   ## data:  fyrriPuls by likamsraektf
   ## Bartlett's K-squared = 4.1246, df = 2, p-value = 0.1272

Eins og sjá má er p-gildið = 0.1272 og getum við því ekki hafnað
núlltilgátunni um að dreifnin sé sú sama. Við verðum þó að gæta okkur á
að hátt p-gildi þýðir ekki að við höfum sýnt fram á að dreifnin sé sú
sama til þess þyrfti að kanna styrk prófsins (við samþykkjum jú ekki
núlltilgátur). Í þessu tilviki er fjöldi mælinga hár og styrkur prófsins
því væntanlega sæmilegur. Við getum því litið á þetta háa p-gildi sem
vísbendingu um það að dreifnin í hópunum sé ekki misjöfn.

Við framkvæmum fervikagreiningu með eftirfarandi skipunum:

::

   fervik <- aov(fyrriPuls ~ likamsraektf, data = puls)

Takið eftir að við tilgreinum fyrst nöfnin á breytunum og svo nafnið á
gagnatöflunni. Til að fá fervikasummutöfluna notum við ``anova()``
aðferðina.

::

   anova(fervik)
   ## Analysis of Variance Table
   ##
   ## Response: fyrriPuls
   ##               Df Sum Sq Mean Sq F value    Pr(>F)
   ## likamsraektf   2   2580  1289.9  9.5055 9.065e-05 ***
   ## Residuals    446  60521   135.7
   ## ---
   ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Hér sjáum við SSTr = 2580 og SSE = 60521 ásamt viðeigandi frígráðum (2
og 446).

Það er einnig búið að reikna meðalfervikasummurnar (1289.9 og 135.7) og
finna hlutfall þeirra, sem er einmitt F-prófstærðin (9.505). p-gildi
fyrir tilgátuprófið er svo lengst til hægri
(:math:`9.07\times 10^{-5}`). Eins og sjá má er ýmislegt annað að finna
í ``aov()`` úttakinu:

::

   names(fervik)
   ##  [1] "coefficients"  "residuals"     "effects"       "rank"
   ##  [5] "fitted.values" "assign"        "qr"            "df.residual"
   ##  [9] "na.action"     "contrasts"     "xlevels"       "call"
   ## [13] "terms"         "model"

Viljum við t.d. nálgast leifarnar gerum við það með:

::

   fervik$residuals

Eftiráprófanir
--------------

Eftiráprófanir
~~~~~~~~~~~~~~

Ef núlltilgátunni er hafnað í einþátta fervikagreiningu drögum við þá
ályktun að a.m.k. eitt meðaltal er frábrugðið hinum meðaltölunum. Ef við
viljum að lokum draga ályktanir um það hvaða meðaltöl eru frábrugðin
þurfum við að nota svo kölluð eftirápróf. Tukeys próf er eitt dæmi um
slíkt próf.

TukeyHSD()
^^^^^^^^^^

.. attention::

    **Inntak:** nafn á fervikagreiningarhlut
    
    **Úttak:** p-gildi, öryggisbil og fl.
    
    **Helstu stillingar:**


--------------

Til að framkvæma prófið í R notum við skipunina ``TukeyHSD()`` og mötum
hana með fervikagreiningarhlut.

::

   TukeyHSD(fervik)
   ##   Tukey multiple comparisons of means
   ##     95% family-wise confidence level
   ##
   ## Fit: aov(formula = fyrriPuls ~ likamsraektf, data = puls)
   ##
   ## $likamsraektf
   ##                     diff       lwr       upr     p adj
   ## Miðlungs-Lítil -1.930757 -5.583459  1.721946 0.4284916
   ## Mikil-Lítil    -6.012279 -9.664981 -2.359576 0.0003665
   ## Mikil-Miðlungs -4.081522 -6.937460 -1.225583 0.0024289

Það má líka skoð niðurstöðuna myndrænt með:

::

   plot(TukeyHSD(fervik))

.. figure:: myndir/unnamed-chunk-225-1.svg

Stikalaus próf\ :math:`^\ast`
-----------------------------

Stikalaus próf\ :math:`^\ast`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef skilyrði þess að hægt sé að framkvæma fervikagreiningu eru ekki
uppfyllt er í sumum tilvikum hægt að nota stikalaus próf þess í stað
(það er algengur misskilningur að það sé ávalt hægt að nota stikalaus
próf en svo er ekki). Algengasta stikalausa prófið er Kruskal Wallis
prófið sem hægt er framkvæma með skipuninni ``kruskal.test()``.

kruskal.test()
^^^^^^^^^^^^^^

.. attention::

    **Inntak:** nafn á talnabreytu og nafn á flokkabreytu
    
    **Úttak:** gildi á prófstærð, p-gildi
    
    **Helstu stillingar:**


--------------

Aðferðin er mötuð á sama hátt og ``aov()`` aðferðin hér að ofan.

.. _s.aovfleiribreytur:

Fleiri en tveir þættir\ :math:`^\ast`
-------------------------------------

Hægt er að framkvæma fervikagreiningu með fleiri en einum þátt. Það er
margt sem þarf að gæta að, s.s. misjafn fjöldi mælinga í hópunum
(e. unbalanced design), *gruggun* (e. confounding) og margt fleira. Við
munum ekki taka á því hér, aðeins sýna hvaða tæki og tól eru til staðar.

Skoðum aftur dæmið hér að ofan þar sem kannað var hvort meðalpúls fólks
var mismunandi eftir hversu mikla líkamsrækt þeir stunda. Hugsum okkur
sem svo að þessi tilraun hafi einnig verið framkvæmd til að kanna hvort
munur væri á kynjum í þessu tilliti. Við höfum nú tvo þætti, líkamsrækt
og kyn og notum því tveggja þátta fervikagreiningu til að kanna
tengslin.

Til að kanna hvort líkamsrækt hafi misjöfn áhrif á púls eftir kynjum
þurfum við að kanna hvort *víxlhrif* (e. interactions) séu til staðar á
milli breytanna tveggja. Gott er að byrja á því að skoða gögnin myndrænt
til að kanna hvort víxlhrif séu til staðar. Við gerum það í R með
*víxlhrifamynd*. Við búum til víxlhrifamynd með ``stat_summary``
aðferðinni úr ``ggplot2``. Hún er viðkvæm fyrir vöntun mælinga á
flokkabreytum og búum við því til gagnasafn þar sem ekki vantar neinar
mælingar.

::

   puls.na<-na.omit(puls)
   ggplot(puls.na,aes(likamsraektf,fyrriPuls,lty=kyn)) +
   stat_summary(aes(group=kyn),fun.y=mean,geom='line')

.. figure:: myndir/unnamed-chunk-226-1.svg

Á myndinni sjáum við meðalpúls í hópunum sex (konur sem stunda litla
líkamsrækt, karla sem stunda litla líkamsrækt, o.s.frv.). Við sjáum að
konurnar eru almennt með lægri púls en karlarnir, sér í lagi meðal
einstaklinga sem stunda litla líkamsrækt.

Við metum svo líkanið með ``aov()`` aðferðinni. Séu víxlhrif til staðar
prófum við ekki hina þættina í líkaninu. Ef engin víxlhrif eru til
staðar þá fjarlægjum við víxlhrifin úr líkaninu, metum það upp á nýtt og
prófum hina þættina tvo.

::

   fervik.2<-aov(fyrriPuls~likamsraektf + kyn + likamsraektf:kyn, data=puls)
   anova(fervik.2)
   ## Analysis of Variance Table
   ##
   ## Response: fyrriPuls
   ##                   Df Sum Sq Mean Sq F value    Pr(>F)
   ## likamsraektf       2   2580 1289.87  9.5709 8.525e-05 ***
   ## kyn                1    603  602.54  4.4709   0.03504 *
   ## likamsraektf:kyn   2    215  107.73  0.7994   0.45026
   ## Residuals        443  59703  134.77
   ## ---
   ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Við notum svo ``anova()`` aðferðina til að fá fervikasummurnar, p-gildi
og prófstærð.

Úr úttakinu má lesa að p-gildið fyrir víxlhrifin er 0.45026 og höfum við
því ekki sýnt fram á að munur sé á áhrif líkamsræktar eftir kynjum. Við
fjarlægjum því víxlhrifin úr líkaninu og metum það upp á nýtt.

::

   fervik.3<-aov(fyrriPuls~likamsraektf + kyn, data=puls)
   anova(fervik.3)
   ## Analysis of Variance Table
   ##
   ## Response: fyrriPuls
   ##               Df Sum Sq Mean Sq F value    Pr(>F)
   ## likamsraektf   2   2580 1289.87  9.5795 8.448e-05 ***
   ## kyn            1    603  602.54  4.4749   0.03495 *
   ## Residuals    445  59919  134.65
   ## ---
   ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Takið eftir að ``anova()`` aðferðin skilar okkur fervikasummum af gerð I
(type I SS). ``drop1()`` skipunin skilar okkur fervikasummum af gerð III
(type III SS) og í ``car`` pakkanum má finna aðferðina ``Anova()`` en
með henni er hægt að fá fervikasummur af gerð II. Skoðum nú úttakið úr
``drop1()`` aðferðinni:

::

   drop1(fervik.3, test="F")
   ## Single term deletions
   ##
   ## Model:
   ## fyrriPuls ~ likamsraektf + kyn
   ##              Df Sum of Sq   RSS    AIC F value    Pr(>F)
   ## <none>                    59919 2205.3
   ## likamsraektf  2   2340.59 62259 2218.5  8.6915 0.0001982 ***
   ## kyn           1    602.54 60521 2207.8  4.4749 0.0349509 *
   ## ---
   ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Sjá má á úttakinu að báðar breyturnar eru marktækar. Hér höfum við sýnt
fram á að marktækur munur sé á meðalpúls nemenda eftir því hversu mikla
líkamsrækt þeir hafa stundað eftir að búið er að leiðrétta fyrir
breytunni ``kyn``.

Eins og sagt var frá í upphafi þessa hluta er margt sem þarf að hafa í
huga þegar fjölþátta aðhvarfsgreining er framkvæmd. Hvernig á að velja
skýribreytur í líkaninu er stór þáttur og langt frá því að vera ein rétt
leið að því markmiði. Hér að ofan byrjuðum við með stærsta líkanið og
fjarlægðum svo eina breytu í einu (e. backward selection). Það má einnig
byrja með minnsta líkanið og bæta við einni breytu í einu (e. forward
selection) en hægt er að nota ``add1()`` aðferðina til þess. Að auki
eru til skref fyrir skref aðferðir (e. stepwise methods) en nota má fallið
``step()`` til þess.


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