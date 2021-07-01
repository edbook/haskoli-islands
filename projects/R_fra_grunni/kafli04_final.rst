.. _c.lysandi:

Lýsandi tölfræði
================

Í þessum kafla munum við fjalla um algengar lýsistærðir sem notaðar eru
til að lýsa gögnum. Við munum skipta umfjölluninni upp eftir því hvort
verið sé að vinna með talnabreytur eða flokkabreytur. Fyrir
talnabreyturnar munum við kynnast aðferðunum ``min()``, ``max()``,
``mean()`` ,\ ``median()``, ``var()``, ``sd()``, ``quantile()``, og
``IQR()``. Þær eru teknar fyrir í hluta :numref:`%s <s.talnabreytur>`. Á
flokkbreytur notum við skipanirnar ``table()`` og ``prop.table`` en þær eru
teknar fyrir í hluta :numref:`%s <s.flokkabreytur>`. Að lokum fjallar hluti
:numref:`%s <s.adrargagnlegar>` um aðrar gagnlegar skipanir. Þar munum við sjá
aðferðirnar ``round()``, ``summary()`` og ``tapply()``.

.. _s.talnabreytur:

Talnabreytur
------------

Talnabreytur
~~~~~~~~~~~~

Í þessum hluta munum við skoða lýsistærðir fyrir talnabreytur. Við
byrjum á að sjá hvernig við getum auðveldlega fundið hæsta og lægsta
gildið sem breytan tekur en snúum okkur svo að lýsistærðum sem lýsa
miðju og breytileika talnabreyta. Það er oft svo að það vantar mælingar
í breytunni okkar, þá kemur ``na.rm = T`` stillingin að góðum notum en
hana má nota í nær öllum aðferðunum sem fjallað verður um í þessum
hluta.

max()
^^^^^

.. attention::

    **Inntak:** nafn á vigri/breytu
    
    **Úttak:** hæsta gildi
    
    **Helstu stillingar:** na.rm


--------------

Aðferðin ``max()`` gefur hæsta gildið. Viljum við finna hæsta gildið af
3, 4, 7 og 8 gerum við það með

::

   max(c(3,4,7,8))
   ## [1] 8

en viljum við finna hæsta gildi ákveðinnar breytu gerum við það með að
mata aðferðina með nafni breytunnar.

::

   max(puls$haed, na.rm=T)
   ## [1] 198

min()
^^^^^

.. attention::

    **Inntak:** nafn á vigri/breytu
    
    **Úttak:** lægsta gildi
    
    **Helstu stillingar:** na.rm


--------------

Aðferðin ``min()`` gefur lægsta gildið. Viljum við finna lægsta gildið
af 3, 4, 7 og 8 gerum við það með

::

   min(c(3,4,7,8), na.rm=T)
   ## [1] 3

en viljum við finna lægsta gildi ákveðinnar breytu gerum við það með að
mata aðferðina með nafni breytunnar.

::

   min(puls$haed, na.rm=T)
   ## [1] 150

Miðja
~~~~~

mean()
^^^^^^

.. attention::

    **Inntak:** nafn á vigri/breytu
    
    **Úttak:** meðaltal
    
    **Helstu stillingar:** na.rm


--------------

Aðferðin ``mean()`` reiknar meðaltal. Viljum við reikna meðaltal
talnanna 3, 4, 7 og 8 gerum við það með:

::

   mean(c(3,4,7,8))
   ## [1] 5.5

Viljum við reikna meðaltal ákveðinnar breytu gerum við það með að mata
aðferðina með nafni breytunnar.

::

   mean(puls$haed, na.rm=T)
   ## [1] 173.2532

median()
^^^^^^^^

.. attention::

    **Inntak:** nafn á vigri/breytu
    
    **Úttak:** miðgildið
    
    **Helstu stillingar:** na.rm


--------------

Aðferðin ``median()`` reiknar miðgildi. Viljum við reikna miðgildi
talnanna 3, 4, 7 og 8 gerum við það með

::

   median(c(3,4,7,8))
   ## [1] 5.5

en viljum við reikna miðgildi ákveðinnar breytu gerum við það með að
mata aðferðina með nafni breytunnar:

::

   median(puls$haed, na.rm=T)
   ## [1] 172

Breytileiki
~~~~~~~~~~~

var()
^^^^^

.. attention::

    **Inntak:** nafn á vigri/breytu
    
    **Úttak:** dreifni
    
    **Helstu stillingar:** na.rm


--------------

Aðferðin ``var()`` reiknar dreifni. Viljum við reikna dreifni talnanna
3, 4, 7 og 8 gerum við það með

::

   var(c(3,4,7,8))

en viljum við reikna dreifni ákveðinnar breytu gerum við það með að mata
aðferðina með nafni breytunnar:

::

   var(puls$haed, na.rm=T)

sd()
^^^^

.. attention::

    **Inntak:** nafn á vigri/breytu
    
    **Úttak:** staðalfrávik
    
    **Helstu stillingar:** na.rm


--------------

Aðferðin ``sd()`` reiknar staðalfrávik. Viljum við reikna staðalfrávik
talnanna 3, 4, 7 og 8 gerum við það með

::

   sd(c(3,4,7,8))
   ## [1] 2.380476

en viljum við reikna staðalfrávik ákveðinnar breytu gerum við það með að
mata aðferðina með nafni breytunnar:

::

   sd(puls$haed, na.rm=T)
   ## [1] 9.774032

quantile()
^^^^^^^^^^

.. attention::

    **Inntak:** nafn á vigri/breytu
    
    **Úttak:** hlutfallsmörk
    
    **Helstu stillingar:** na.rm, probs


--------------

Aðferðin ``quantile`` reiknar út hlutfallsmörk. Sjálfgefna stilling
aðferðarinnar skilar okkur fjórðungamörkunum. Við mötum aðferðina með
nafninu á breytunni:

::

   quantile(puls$haed, na.rm=T)
   ##   0%  25%  50%  75% 100%
   ##  150  166  172  181  198

Við getum notað ``probs`` stillinguna til að reikna hvaða hlutfallsmörk
sem er.

Samspil tveggja talnabreyta
~~~~~~~~~~~~~~~~~~~~~~~~~~~

cor()
^^^^^

.. attention::

    **Inntak:** nafn á tveimur vigrum/breytum
    
    **Úttak:** fylgni
    
    **Helstu stillingar:** use


--------------

Reikna má fylgni milli tveggja breyta í R með ``cor()`` aðferðinni. Við
þurfum að mata aðferðina með heitunum á breytunum sem við ætlum að
reikna fylgnina á milli. Viljum við reikna fylgnina á milli breytanna
``haed`` og ``thyngd`` notum við skipunina:

::

   cor(puls$haed,puls$thyngd,use="complete.obs")
   ## [1] 0.6765718

Stillinguna ``use="complete.obs"`` notum við vanti einhverjar mælingar.
Munið að við reiknum aðeins út fylgnistuðul sé línulegt samband á milli
breytanna!

.. _s.flokkabreytur:

Flokkabreytur
-------------

Í þessum hluta reiknum við út lýsistærðir fyrir flokkabreytur. Við
byrjum á að sjá hvernig finna má tíðni og hlutföll á auðveldan hátt og
skoðum svo lýsistærðir sem lýsa sambandi tveggja flokkabreyta.

Tíðni og hlutfall
~~~~~~~~~~~~~~~~~

.. _rf.table:

table()
^^^^^^^

.. attention::

    **Inntak:** nafn á flokkabreyt(um)
    
    **Úttak:** tíðni


--------------

``table()`` skipunin telur hversu oft hver og ein útkoma flokkabreytu
kemur fyrir. Viljum við sjá hversu margir nemendur voru í LAN203 og
STÆ209 í gagnasafninu okkar gerum við það með:

::

   table(puls$namskeid)
   ##
   ##  LAN203 STAE209
   ##     172     299

Við getum líka matað ``table()`` með tveimur flokkabreytum og þá telur
hún hversu oft hversu mörg viðfangsefni hljóta hverja og eina af
mögulegum samsetningum útkoma beggja breytanna eins og er sýnt hér að
neðan.

::

   table(puls$namskeid,puls$kyn)
   ##
   ##           kvk  kk
   ##   LAN203  111  61
   ##   STAE209 196 103

.. _rf.prop.table:

prop.table()
^^^^^^^^^^^^

.. attention::

    **Inntak:** tafla - úttak úr ``table()``
    
    **Úttak:** hlutföll
    
    **Helstu stillingar:** margin


--------------

``table()`` skipunin skilar okkur fjölda/tíðni en viljum við frekar
hlutföll getum við notað ``prop.table()`` aðferðina. Við mötum hana með
því sem ``table()`` aðferðin skilar:

::

   prop.table(table(puls$namskeid))
   ##
   ##    LAN203   STAE209
   ## 0.3651805 0.6348195

Séum við að vinna með tvær breytur má mata ``prop.table()`` aðferðina á
þrennan hátt. Viljum við fá heildarhlutföllin gerum við það með:

::

   prop.table(table(puls$namskeid,puls$kyn))
   ##
   ##                 kvk        kk
   ##   LAN203  0.2356688 0.1295117
   ##   STAE209 0.4161359 0.2186837

Í töflunni má t.d. sjá að um 23.6% nemenda í gagnasafninu eru kvenkyns
nemendur í LAN203. Viljum við aftur á máti skoða hlutföllin eftir línum
í töflunni gerum við það með:

::

   prop.table(table(puls$namskeid,puls$kyn),margin=1)
   ##
   ##                 kvk        kk
   ##   LAN203  0.6453488 0.3546512
   ##   STAE209 0.6555184 0.3444816

Í töflunni má t.d. sjá að um 64.5% nemenda í LAN203 eru kvenkyns. Viljum
við hins vegar skoða hlutföllin eftir dálkum í töflunni gerum við það
með:

::

   prop.table(table(puls$namskeid,puls$kyn),margin=2)
   ##
   ##                 kvk        kk
   ##   LAN203  0.3615635 0.3719512
   ##   STAE209 0.6384365 0.6280488

Í töflunni má t.d. sjá að um 36.2% kvenkyns nemenda er í LAN203.

Takið eftir að nota má ``prop.table()`` til að reikna lýsistærðirnar
næmi (e. sensitivity) og sértæki (e. specificity).

.. _s.adrargagnlegar:

Aðrar gagnlegar skipanir
------------------------

Aðrar gagnlegar skipanir
~~~~~~~~~~~~~~~~~~~~~~~~

round()
^^^^^^^

.. attention::

    **Inntak:** gildi, vigur, tafla...
    
    **Úttak:** gildi, vigur, tafla með námunduðum gildum
    
    **Helstu stillingar:** digits


--------------

R skilar stundum óþarflega mörgum aukastöfum. Við getum notað
``round()`` aðferðina til að stjórna hversu mörgum aukastöfum er skilað.
Við mötum aðferðina með því sem reikna á og fjölda aukastafa sem á að
skila. Skoðum t.d. töfluna hér að ofan. Viljum við aðeins að þremur
aukastöfum sé skilað gerum við það með:

::

   round(prop.table(table(puls$namskeid,puls$kyn),2),3)
   ##
   ##             kvk    kk
   ##   LAN203  0.362 0.372
   ##   STAE209 0.638 0.628

summary()
^^^^^^^^^

.. attention::

    **Inntak:** allt milli himins og jarðar
    
    **Úttak:** flest það sem þú vilt vita


--------------

Við munum rekast á skipunina ``summary()`` nokkrum sinnum í þessari bók.
Skipunin skilar mismunandi úttaki eftir því með hverju hún er mötuð. Sé
hún mötuð með talnabreytu gefur ``summary()`` aðferðin okkur fimm tölu
samantekt og meðaltal. Það er bæði hægt að mata aðferðina með tölum

::

   summary(c(3,4,7,8))
   ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
   ##    3.00    3.75    5.50    5.50    7.25    8.00

og með nafni breytu:

::

   summary(puls$haed)
   ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's
   ##   150.0   166.0   172.0   173.3   181.0   198.0       1

Ef breytan sem við erum að skoða er flokkabreyta gefur ``summary()``
aðferðin okkur nafnið á flokkunum og fjölda viðfangsefna í hverjum
flokki.

Það er líka hægt að mata ``summary()`` aðferðina með nafninu á
gagnatöflu og fáum við þá upplýsingar um allar breyturnar í töflunni.

::

   summary(puls)
   ##        id           namskeid        haed           thyngd
   ##  Min.   :  1.0   LAN203 :172   Min.   :150.0   Min.   : 40.00
   ##  1st Qu.:118.5   STAE209:299   1st Qu.:166.0   1st Qu.: 60.00
   ##  Median :236.0                 Median :172.0   Median : 70.00
   ##  Mean   :236.0                 Mean   :173.3   Mean   : 71.46
   ##  3rd Qu.:353.5                 3rd Qu.:181.0   3rd Qu.: 80.00
   ##  Max.   :471.0                 Max.   :198.0   Max.   :121.00
   ##                                NA's   :1       NA's   :10
   ##      aldur        kyn       reykir    drekkur     likamsraekt
   ##  Min.   :19.00   kvk:307   ja  : 46   ja  :389   Min.   : 0.000
   ##  1st Qu.:20.00   kk :164   nei :412   nei : 76   1st Qu.: 2.000
   ##  Median :22.00             NA's: 13   NA's:  6   Median : 4.000
   ##  Mean   :24.24                                   Mean   : 4.492
   ##  3rd Qu.:25.00                                   3rd Qu.: 6.000
   ##  Max.   :70.00                                   Max.   :25.000
   ##                                                  NA's   :5
   ##    likamsraektf       kronukast     fyrriPuls        seinniPuls
   ##  Lítil   : 85   landvaettir:263   Min.   : 42.00   Min.   : 42.00
   ##  Miðlungs:191   thorskur   :208   1st Qu.: 64.00   1st Qu.: 68.00
   ##  Mikil   :190                     Median : 71.50   Median : 77.00
   ##  NA's    :  5                     Mean   : 71.98   Mean   : 82.21
   ##                                   3rd Qu.: 80.00   3rd Qu.: 93.00
   ##                                   Max.   :120.00   Max.   :162.00
   ##                                   NA's   :17       NA's   :14
   ##      inngrip      dagsetning               ar        namskeidar
   ##  hljop   :183   Min.   :2013-01-07   Min.   :2013   Length:471
   ##  sat_kyrr:286   1st Qu.:2013-01-07   1st Qu.:2013   Class :character
   ##  NA's    :  2   Median :2014-01-06   Median :2014   Mode  :character
   ##                 Mean   :2014-01-07   Mean   :2014
   ##                 3rd Qu.:2015-01-05   3rd Qu.:2015
   ##                 Max.   :2015-01-05   Max.   :2015
   ##

.. _rf.tapply:

tapply()
^^^^^^^^

.. attention::

    **Inntak:** nafn á talnabreytu, nafn á flokkabreytu og nafn á aðferð
    fyrir lýsistærð
    
    **Úttak:** gildi á lýsistærð fyrir talnabreytuna reiknað fyrir sérhvern
    flokk flokkabreytunnar


--------------

``tapply()`` skipunin getur verið mjög gagnleg viljum við reikna út
lýsistærðir talnabreytu fyrir hvern flokk í flokkabreytu sem tilheyrir
sömu gagnatöflu og talnabreytan. Við mötum ``tapply()`` aðferðina með
nafninu á talnabreytunni, nafninu á flokkabreytunni og nafninu á
aðferðinni sem við viljum beita. Ef það vantar einhver gildi þurfum við
að nota ``na.rm=TRUE`` líkt og áður. Viljum við t.d. reikna út meðaltal
fyrri púlsmælinganna í líkamsræktarhópunum þremur sem við mynduðum hér að
ofan gerum við það með:

::

   tapply(puls$fyrriPuls,puls$likamsraektf,mean,na.rm=TRUE)
   ##    Lítil Miðlungs    Mikil
   ## 75.14815 73.21739 69.13587


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