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

   max(dat$ferdatimi_skoli, na.rm=T)
   ## [1] 75

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

   min(dat$ferdatimi_skoli, na.rm=T)
   ## [1] 0

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

   mean(dat$ferdatimi_skoli, na.rm=T)
   ## [1] 19.42786

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

   median(dat$ferdatimi_skoli, na.rm=T)
   ## [1] 16

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

   var(dat$ferdatimi_skoli, na.rm=T)
   ## [1] 198.786

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

   sd(dat$ferdatimi_skoli, na.rm=T)
   ## [1] 14.09915

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

   quantile(dat$ferdatimi_skoli, na.rm=T)
   ## 0%  25%  50%  75% 100% 
   ## 0   8   16   25   75

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
reikna fylgnina á milli. Viljum við reikna fylgnina á heildarlengdar og
höfuðlengdar pokarotta, semsagt breytanna ``total_l`` og ``head_l``,
notum við skipunina:

::

   cor(possum$total_l, possum$head_l)
   ## [1] 0.6910937

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

   table(dat$is)
   ##
   ## Jarðaberja  Súkkulaði    Vanilla 
   ##         39        91         71 


Við getum líka matað ``table()`` með tveimur flokkabreytum og þá telur
hún hversu oft hversu mörg viðfangsefni hljóta hverja og eina af
mögulegum samsetningum útkoma beggja breytanna eins og er sýnt hér að
neðan.

::

   table(dat$is, dat$dyr)
   ##
   ##               Hunda Ketti
   ## Jarðaberja    23    16
   ## Súkkulaði     61    30
   ## Vanilla       43    28

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

   prop.table(table(dat$is))
   ##
   ## Jarðaberja  Súkkulaði    Vanilla 
   ##  0.1940299  0.4527363  0.3532338 

Séum við að vinna með tvær breytur má mata ``prop.table()`` aðferðina á
þrennan hátt. Viljum við fá heildarhlutföllin gerum við það með:

::

   prop.table(table(dat$is, dat$dyr))
   ##
   ##                  Hunda      Ketti
   ##  Jarðaberja 0.11442786 0.07960199
   ##  Súkkulaði  0.30348259 0.14925373
   ##  Vanilla    0.21393035 0.13930348

Í töflunni má t.d. sjá að um 30% nemenda í gagnasafninu sem eru hrifinn af hundum
elska súkkulaðiís. Viljum við aftur á máti skoða hlutföllin eftir línum
í töflunni gerum við það með:

::

   prop.table(table(dat$is, dat$dyr), margin=1)
   ##
   ##                 Hunda     Ketti
   ##  Jarðaberja 0.5897436 0.4102564
   ##  Súkkulaði  0.6703297 0.3296703
   ##  Vanilla    0.6056338 0.3943662

Í töflunni má t.d. sjá að um 67% nemenda sem elska súkkulaðiís eru hrifnir af hundum. 
Viljum við hins vegar skoða hlutföllin eftir dálkum í töflunni gerum við það
með:

::

   prop.table(table(dat$is, dat$dyr), margin=2)
   ##
   ##                 Hunda     Ketti
   ##  Jarðaberja 0.1811024 0.2162162
   ##  Súkkulaði  0.4803150 0.4054054
   ##  Vanilla    0.3385827 0.3783784

Í töflunni má t.d. sjá að um 21.6% þeirra sem eru hrifinn af köttum elskar jarðaberjaís.

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

   round(prop.table(table(dat$is, dat$dyr),2),3)
   ##
   ##             Hunda Ketti
   ##  Jarðaberja 0.181 0.216
   ##  Súkkulaði  0.480 0.405
   ##  Vanilla    0.339 0.378

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

   summary(dat$ferdatimi_skoli)
   ##   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
   ##   0.00    8.00   16.00   19.43   25.00   75.00 

Ef breytan sem við erum að skoða er flokkabreyta gefur ``summary()``
aðferðin okkur nafnið á flokkunum og fjölda viðfangsefna í hverjum
flokki.

Það er líka hægt að mata ``summary()`` aðferðina með nafninu á
gagnatöflu og fáum við þá upplýsingar um allar breyturnar í töflunni.

::

   summary(dat)
   ##       X            is            ferdatimi_skoli styrikerfi_simi   
   ## Min.   :  1   Length:201         Min.   : 0.00   Length:201        
   ## 1st Qu.: 51   Class :character   1st Qu.: 8.00   Class :character  
   ## Median :101   Mode  :character   Median :16.00   Mode  :character  
   ## Mean   :101                      Mean   :19.43                     
   ## 3rd Qu.:151                      3rd Qu.:25.00                     
   ## Max.   :201                      Max.   :75.00                     
   ## ferdamati_skoli    systkini_fjoldi      dyr             feministi        
   ## Length:201         Min.   : 0.000   Length:201         Length:201        
   ## Class :character   1st Qu.: 2.000   Class :character   Class :character  
   ## Mode  :character   Median : 2.000   Mode  :character   Mode  :character  
   ##                    Mean   : 2.541                                        
   ##                    3rd Qu.: 3.000                                        
   ##                    Max.   :10.000                                        
   ## staerdfraedi_gaman  smjor_kostar    napoleon_faeddur  stefnumot        
   ## Min.   :2          Min.   : 144.0   Min.   :  46     Length:201        
   ## 1st Qu.:6          1st Qu.: 450.0   1st Qu.:1740     Class :character  
   ## Median :7          Median : 595.0   Median :1769     Mode  :character  
   ## Mean   :7          Mean   : 593.8   Mean   :1733                       
   ## 3rd Qu.:8          3rd Qu.: 745.0   3rd Qu.:1800                       
   ## Max.   :9          Max.   :1490.0   Max.   :3142                       
   ##  messi_staerd       kosid          
   ## Min.   :  1.65   Length:201        
   ## 1st Qu.:163.00   Class :character  
   ## Median :169.00   Mode  :character  
   ## Mean   :163.58                     
   ## 3rd Qu.:172.00                     
   ## Max.   :191.00  

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

   tapply(dat$ferdatimi_skoli, dat$ferdamati_skoli, mean, na.rm=T)
   ##            Á annan hátt Á hjóli / rafhlaupahjóli     Gangandi / skokkandi 
   ##                2.500000                11.666667                 7.588235 
   ##            Með einkabíl               Með strætó 
   ##               19.923077                33.733333

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
