.. _c.tilraun:

Frá tilraun til gagna
=====================

Mörg verk þarf að vinna frá því að niðurstöðum rannsóknar hefur verið
safnað þar til að hægt er að framkvæma tölfræðiúrvinnslu á þeim
niðurstöðum. Í þessum kafla verður gengið í gegnum þau helstu skref sem
þarf að stíga á þeirri leið.

Við hefjum umfjöllunina á góðum ráðleggingum varðandi innslátt og
skráningu gagnanna, sem er efni kafla :numref:`%s <s.skraning>`. Í kafla
:numref:`%s <s.innlestur>` sýnum við hvernig gögnin eru lesin inn í R, með
aðstoð skipunarinnar ``read.table()``. Einnig sýnum við nokkrar
handhægar skipanir til að búa til mælingar, þær eru ``c()``, ``rep()``
og ``seq()``.

Eftir að gögn hafa verið lesið inn er mikilvægt að fá gróft yfirlit yfir
gögnin til að tryggja að innlesturinn hafi gengið sem skildi. Til þess
notum við skipanirnar ``View()``, ``names()``, ``head()``, ``str()``,
``length()`` og ``dim()`` sem við sjáum í kafla :numref:`%s <s.innlestur>`.

Mikilvægt atriði í meðhöndlun gagna er meðhöndlun mælinga sem vantar í
gagnasafnið. Það er umfjöllunarefni kafla :numref:`%s <s.vontun>` þar sem við
kynnumst skipununum ``is.na()`` og ``na.omit()``. Í kafla
:numref:`%s <s.gildivalin>` sjáum við svo leiðir til að velja tilteknar línur úr
gagnatöflunni. Til þess notum við skipanirnar ``slice()``, ``filter()``,
``which()`` og ``grep()``.

Í kafla :numref:`%s <s.kodun>`  sýnum við handhægar skipanir til að koma
breytunum okkar á það form sem við viljum vinna með, þ.e.a.s. *kóða*
þær. Mesta púðrið fer yfirleitt í að kóða flokkabreytur en einnig lýsum
við því beita má vörpunum á talnabreytur og dagsetningar eru
meðhöndlaðar. Þar koma við sögu skipanirnar ``factor()``, ``levels()``,
``cut()``, ``as.Date()`` og ``rename()``.

Síðast en ekki síst fjallar kafli :numref:`%s <s.umrodun>` um handhægar leiðir
til að umraða og umbreyta gagnatöflum. Skipunin ``select()`` hjálpar
okkur að búa til minni gagnatöflur með færri breytum. Skipanirnar
``sort()`` og ``arrange()`` gera okkur kleift að raða gildum eftir línum
og dálkum á meðan skipanirnar ``spread()`` og ``gather()`` varpað úr
löngu sniði í vítt og öfugt. Að lokum gerir skipunin ``merge()`` okkur
kleift að sameina tvær eða fleiri gagnatöflur.

.. _s.skraning:

Skráning gagna
--------------

Fyrsta ráðleggingin sem við viljum gefa varðandi skráningu gagna er að
gæta þess að geyma ætíð frumeintak af mælingunum í annarri skrá áður en
þið hefjist handa við nokkra úrvinnslu, þar á meðal að undirbúa lestur
gagnanna inn í R. Bæði viljum við ekki eiga á hættu á að gera einhverjar
óafturkræfar breytingar á mælingunum og eins gætum við viljað skrá hjá
okkur ýmsar upplýsingar sem við notum ekki beint í tölfræðiúrvinnslunni
en gætum viljað kanna síðar meir.

Gögn eru oftar en ekki skráð í einhvers konar töflureikni, til dæmis
Excel, Numbers, LibreOffice eða Google Sheets, og miðum við umfjöllun
kaflans við það. Við gerum ráð fyrir að við mælum margar breytur en
höfum eingöngu eina mælingu á hverri breytu fyrir hvert viðfangsefni.
Séu fleiri en ein mæling framkvæmd á hverju viðfangsefni þarf að velja á
hvaða *gagnasniði* gögnin eru. Við ræðum slíkt stuttlega í kafla
:numref:`%s <s.umrodun>`.

Eftirfarandi gátlisti spannar það helsta sem þarf að hafa í huga við
skráningu gagna í töflureikni:

1. Hefur hver breyta sinn dálk og hvert viðfangsefni sína línu?

   Gætið þess að allar mælingar á sama viðfangsefni séu í einni og sömu
   línunni og að allar mælingar á sömu breytu séu í einum og sama
   dálkinum.

\2. Eru nokkrar óþarfa línur?

   Skráin á að halda gagnatöfluna eina og ekkert annað. Efsta línan á að
   geyma nöfnin á breytunum, þar fyrir neðan koma mælingarnar á
   viðfangsefnunum. Ekkert annað á að vera í skránni.

\3. Inniheldur skráin séríslenska stafi?

   Séríslenskir stafir, svo sem þ, ð og æ, geta oft valdið usla þegar
   gögn eru flutt á milli tölva. Því borgar sig að forðast alla
   séríslenska stafi, hvort sem heldur í breytuheitum eða þeim gildum
   sem mælingarnar taka. Ritið þannig breytuna ``hæð`` heldur sem
   breytuna ``haed`` svo dæmi sé nefnt. Ef þið skráið ekki gögnin sjálf
   heldur fáið í hendur gögn sem innihalda séríslenska stafi þá má þó
   prófa að notast við skrána með séríslensku stöfunum og skipta þeim
   ekki út fyrr en við höfum séð að þeir valdi vandræðum.

\4. Eru nokkur bil?

   Það getur að sama skapi valdið vandræðum þegar breytuheiti eða gildi
   mælinga eru skráð með tveimur eða fleiri orðum. Það er hægt að komast
   hjá því með því að annað hvort leika sér með hástafi og lágstafi eða
   nota :math:`\_` táknið. Þannig væri hægt að skrá breytuna
   ``fyrsta koma`` sem annað hvort sem ``fyrstaKoma`` eða
   ``fyrsta\_koma`` til dæmis.

\5. Eru sömu útkomurnar skráðar á sama hátt?

   Við þurfum alltaf að gæta þess að skilgreina nákvæmlega hvaða útkomur
   breyturnar okkar geta tekið og að skrá sömu útkomurnar á sama hátt.
   Að ``ja`` sé ekki stundum skráð sem ``Ja`` eða jafnvel ``ju``.
   Stundum þvælast óþarfa auð tákn með í útkomuna sem valda vandræðum
   seinna meir. Oft getur borgað sig að kóða útkomurnar heldur með
   tölustöfum heldur en orðum.

\6. Hefur hver breyta sitt nafn?

   Pössum að engar tvær breytur hafi sama nafnið. Að það séu til dæmis
   ekki tveir dálkar sem bera heitið ``numer``. Gætið þess að hafa
   breytuheiti lýsandi án þess að vera of löng.

\7. Er fullt samræmi í því hvernig tölur eru skráðar?

   Er "þrír komma fjórir" ritað sem 3,4 eða 3.4 eða kannski beggja
   blands hér og þar í skjalinu?

\8. Eru nokkrir punktar sem gætu valið misskilningi?

   Notum eingöngu punkta til að aðgreina á milli heiltöluhluta og
   aukastafa en ekki til að gera þúsund og milljónir læsilegri. Á
   Íslandi er stærðin 3482 oft rituð sem 3.482 en fáum við eingöngu
   töluna 3.482 gefna er ekki ljóst hvort hún eigi við töluna "þrjú
   þúsund fjögur hundruð áttatíu og tveir" eða "þrír komma fjórir átta
   tveir".

Þegar við höfum gengið úr skugga um ofangreind atriði er tímabært að
vista gögnin á forminu .csv. Nær allir ritlar geta vistað skrár á þessu
formi. Þá þurfum við oftast að fara í ``File``, ``Save as`` og velja svo
``comma seperated value``, ``text csv`` eða eitthvað álíka eftir því
hvert forritið er. Þessa .csv skrá köllum við *gagnaskrá*.

Oft koma einhverjir valmöguleikar upp með það hvernig breytur séu
aðgreindar frá dálki til dálks. Við mælum með því að nota annað hvort
``tab`` eða semikommur en alls ekki kommur því þær gætu einnig verið
notaðar til að aðgreina heiltöluhluta og tugabrot.

Flest forrit á Íslandi nota kommur til að aðgreina heiltöluhluta og
tölustafi en R aðgreinir með punkti. Séu heiltöluhlutar og tugabrot
aðskilin með kommu í .csv skránni okkar þurfum við að fara aðra af
tveimur leiðum:

#) Gefa R til kynna að kommur séu notaðar til að aðgreina milli
   heiltöluhluta og tugabrota. Það er stillingaratriði í aðferðinni
   ``read.table()`` sem við kynnumst hér að neðan.

#) Opna .csv skrána í einföldum ritli eins og ``Notepad`` eða
   ``TextEdit``. Fara svo yfir skjalið með ``find`` og ``replace`` og
   skipta öllum kommum út fyrir punkta. Gætið þess að vista skrána aftur
   á forminu .csv. Stundum er hægt að gera þetta beint í Excel eða Open
   Office.

Fyrst um sinn er einfaldast og þægilegast að vista gagnaskrárnar í sömu
möppu og við geymum skipanaskrárnar. R gerir að vísu enga kröfu um það,
R getur náð í skrár hvaðan sem er af tölvunni (við þurfum bara að vísa á
réttan stað), en það einfaldar ykkur úrvinnslu þegar verkefnin eru ekki
mjög stór og gagnasöfnin sem við vinnum með eru ekki mörg. Séum við hins
vegar að vinna stærri verkefni með nokkrum gagnasöfnum borgar sig að
hafa sérstaka undirmöppu sem geymir einvörðungu gögnin.

Nú fyrst er tímabært að lesa gögnin inn í R.

.. _s.innlestur:

Innlestur gagna
---------------

Innlestur gagna
~~~~~~~~~~~~~~~

read.table()
^^^^^^^^^^^^

.. attention::

    **Inntak:** nafn á gagnaskrá
    
    **Úttak:** gagnatafla
    
    **Helstu stillingar:** header, sep, dec, na.strings, stringsAsFactors


--------------

Á síðu bókarinnar má finna gagnaskrána ``pulsAll.csv``. Byrjið á því að
vista hana í vinnumöppunni ykkar, þ.e.a.s. sömu möppu og þið geymið
skipanaskrána ykkar. Þá má lesa þau inn í R með skipuninni:

::

   puls <- read.table("pulsAll.csv", header=TRUE, sep=";")

Fyrst tilgreinum við nafnið á skránni: ``pulsAll.csv``. Þar á eftir
gefum við ýmis konar stillingar, aðgreindar með kommum.

Þær stillingar sem við komum oft til með að nota eru:

-  ``header=TRUE``: Að breytuheiti séu í efstu línu gagnaskráarinnar.

-  ``sep=”;”``: Dálkar/breytur eru aðgreindir með semikommu.

   Séu dálkar t.d. aðgreindir með ``tab`` skiptum við ``sep=”;”`` út
   fyrir ``sep=”\t”``.

-  ``dec=”,”``: Ef tugabrot og heiltöluhlutar eru aðgreind með kommu í
   stað punkts þarf að nota þessa stillingu.

-  ``na.strings``: Tilgreinir hvaða tákn á að líta á sem vantaðar
   mælingar (t.d. 999, NA osfrv).

-  ``stringsAsFActors``: Tilgreinir að strengjabreytur eigi ekki að
   vista sem flokkabreytur.

Um leið og við gefum skipunina höfum við lesið inn gögnin okkar og
vistað sem gagnatöflu undir heitinu ``puls``. Við hefðum getað gefið
töflunni hvaða heiti sem við viljum, hún hefði allt eins geta heitið
``gogn``, ``tilraun1`` eða hvað annað sem okkur dettur í hug . Það eina
sem ekki má er að láta nöfn byrja á tölustaf. Það væri því ekki í lagi
að gefa töflunni heitið ``1tilraun``.

Ef við sláum

::

   puls

inn í keyrslugluggann birtist svo öll taflan. Gætið ykkar að ef
gagnataflan er mjög stór fyllir hún fljótt marga skjái svo þetta er ekki
góð leið til að fá yfirlit yfir gögnin. Betra er að nota skipanirnar
s.s. ``head()`` og ``str()`` sem við fjöllum um hér fyrir neðan.

Þegar við höfum lesið gögn inn sem töflu getum við hæglega "dregið"
eina og eina breytu út úr töflunni, skoðað nánar og jafnvel breytt.
Viljum við t.d. ná í breytuna ``haed`` úr gagnatöflunni ``puls`` gerum
við það með:

::

   puls$haed

c()
^^^

.. attention::

    **Inntak:** gildi vigurs
    
    **Úttak:** vigur


--------------

Þegar við vinnum með lítil gagnasöfn eða fáar mælingar getur oft verið
hentugt að skrá þær beint inn í R, í stað þess að lesa gögnin úr .csv
skrá. Til þess höfum við skipunina ``c()``. Þannig býr skipunin

::

   postnumer <- c(170,107,110, 101,105,107,111,108,104,101)

til vigurinn ``postnumer`` sem inniheldur 10 mælingar á póstnúmerum.
Röðun póstnúmera í vigrinum er í þeirri röð sem þær eru slegnar:

::

   postnumer
   ##  [1] 170 107 110 101 105 107 111 108 104 101

seq()
^^^^^

.. attention::

    **Inntak:** upphafs- og endagildi
    
    **Úttak:** vigur
    
    **Helstu stillingar:** by


--------------

Skipunin ``seq()`` er sérlega handhæg til að búa til talnarunur.
Algengast er að mata hana með tveimur heiltölum og þá skilar hún vigri
með öllum heiltölum á því bili. Einnig má hafa styttra eða lengra bil á
milli talnanna í vigrinum, með stillingunni ``by`` tilgreinum við hvert
bilið á að vera á milli talnanna. Hér eru tvö dæmi:

::

   seq(3,7)
   ## [1] 3 4 5 6 7
   seq(3,7, by=0.5)
   ## [1] 3.0 3.5 4.0 4.5 5.0 5.5 6.0 6.5 7.0

Einnig er hægt að búa til runur af heiltölum með einföldum hætti með
tvípunkti:

::

   3:7
   ## [1] 3 4 5 6 7

rep()
^^^^^

.. attention::

    **Inntak:** gildi sem á að endurtaka
    
    **Úttak:** vigur
    
    **Helstu stillingar:** each


--------------

Önnur þægileg skipun er ``rep()``. Með henni getum við búið til vigra
þar sem sömu gildin eru endurtekin með kerfisbundnum hætti. Skipunin er
mötuð með gildi eða vigri sem á að endurtaka og hversu oft vigurinn skal
endurtekinn. Skipunin hér að neðan endurtekur vigurinn :math:`1, 2, 3`
fjórum sinnum.

::

   rep(1:3,4)
   ##  [1] 1 2 3 1 2 3 1 2 3 1 2 3

Einnig er hægt að gefa stillinguna ``each`` og þá er hvert stak í
upphaflega vigrinum endurtekið:

::

   rep(1:3,each=4)
   ##  [1] 1 1 1 1 2 2 2 2 3 3 3 3

Staðsetning skráa\ :math:`^\ast`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ein af stillingunum í ``read.table``, ``file=``, segir til um
staðsetningu skráarinnar sem lesin er inn. Ef skráin er staðsett í
vinnumöppu sem skilgreind er í R-setunni þá er ``read.table``
einfaldlega mötuð með nafninu á skránni. Hins vegar ef skráin er
staðsett annars staðar flækist málið lítið eitt.

.. figure:: myndir/tikz1.svg
    :align: center
    :alt: Mynd

Viljum við t.d. lesa Gagnaskrá_1 inn í R gefum við skipunina:

::

   dat <- read.table(file = 'Gagnaskrá_1')

Til þess að lesa Gagnaskrá_3 þurfum við að bæta við nafninu á möppunni
sem hún er í, þ.e.a.s. Gagnamappa_1:

::

   dat <- read.table(file = 'Gagnamappa_1/Gagnaskrá_3')

Til þess að lesa inn Gagnaskrá_2 er hægt bakka upp í yfirmöppuna með því
að vísa í hana með ".." og svo fara í Gagnamöppu_2:

::

   dat <- read.table(file = '../Gagnamappa_2/Gagnaskrá_2')

Skipunin að ofan vísar afstætt í Gagnaskrá_2. Einnig er hægt að víst
algilt á skránna. Sé yfirmappann staðsett sem fyrsta mappa á
stýrikerfisdisk má lesa skránna inn svona fyrir linux/MacOsX

::

   dat <- read.table(file = '/Yfirmappa/Gagnamappa_2/Gagnaskrá_2')

og fyrir Windows (að því gefnu að stýrikerfis sé á c drifi):

::

   dat <- read.table(file = 'c:/Yfirmappa/Gagnamappa_2/Gagnaskrá_2')

.. _s.yfirlit:

Gróft yfirlit gagna
-------------------

Gróft yfirlit gagna
~~~~~~~~~~~~~~~~~~~

Eftir að gögnin hafa verið lesin inn er skynsamlegt að kanna að
innlesturinn hafi gengið sem skyldi. Sé unnið í RStudio má smella á
nafnið á gagnatöflunni í glugganum í efra hægra horninu en þá opnast
gögnin á töfluformi. Til þess má einnig nota skipunina ``View()``.

Skipunin ``read.table()`` skráir sérhverja breytu hjá sér ýmist sem
flokkabreytu (``factor``) eða talnabreytu (``num`` eða ``int``). Breytur
sem innihalda eingöngu tölur eru sjálfkrafa vistaðar sem talnabreytur.
Ef þær innihalda bara heiltölur eru þær vistaðar sem ``int`` en ef þær
innihalda tugabrot eru þær vistaðar sem ``num``. Það skiptir engu máli í
úrvinnslunni hvort þær eru vistaðar sem ``int`` eða ``num``.

Algengt er að notaðir séu talnakóðar fyrir gildi á flokkabreytum. Dæmi
um þetta er að nota gildið 1 fyrir ``kona`` og 2 fyrir ``karl`` í
breytunni ``kyn``. Þar sem breytan inniheldur eingöngu tölur er ``kyn``
skilgreind sem talnabreyta eftir innlestur í R. Áður en úrvinnsla hefst
þarf að breyta talnabreytunni í flokkabreytu (sjá kafla :numref:`%s <s.kodun>` ).
Það getur einnig gerst að talnabreytur séu ranglega vistaðar sem
flokkabreytur og getur það t.d. gerst þegar einhverjar mælingar á
breytunni innihalda bókstafi eða þegar ekki er rétt tilgreint hvernig
tugabrot eru aðskilin. Þetta þarf allt að laga áður en úrvinnsla hefst.

View()
^^^^^^

.. attention::

    **Inntak:** nafn á gagnatöflu
    
    **Úttak:** gögnin birtast á töfluformi


--------------

R lítur sjálfkrafa á hvern dálk úr gagnaskrá sem mælingu á einni breytu.
Skipunin ``names()`` skilar nöfnunum á öllum breytum sem eru geymdar í
gagnatöflu.

names()
^^^^^^^

.. attention::

    **Inntak:** nafn á gagnatöflu
    
    **Úttak:** nöfn breytanna í gagnatöflunni skrifaðar út


--------------

Þannig gefur skipunin

::

   names(puls)
   ##  [1] "namskeid"    "kronukast"   "haed"        "thyngd"      "aldur"
   ##  [6] "kyn"         "reykir"      "drekkur"     "likamsraekt" "fyrriPuls"
   ## [11] "seinniPuls"  "inngrip"     "dagsetning"

nöfnin á öllum þeim breytum sem tilheyra gagnatöflunni ``puls``.

head()
^^^^^^

.. attention::

    **Inntak:** nafn á gagnatöflu
    
    **Úttak:** fyrstu sex línur gagnatöflunnar skrifaðar út
    
    **Helstu stillingar:** n


--------------

``head()`` skipunin sýnir okkur mælingar á fyrstu sex viðfangsefnunum.
Þannig getum við fengið fljótt yfirlit yfir það hvaða breytur eru
vistaðar í gagnatöflunni og hvernig þær eru skráðar. Í okkar tilviki
væri útkoman:

::

   head(puls)
   ##   namskeid   kronukast haed thyngd aldur kyn reykir drekkur likamsraekt
   ## 1  STAE209 landvaettir  161     60    23   1    nei     nei         3.5
   ## 2   LAN203    thorskur  185    115    52   2   <NA>      ja         0.0
   ## 3   LAN203 landvaettir  167     NA    22   1    nei      ja         2.0
   ## 4  STAE209    thorskur  174     67    21   1    nei      ja         1.0
   ## 5  STAE209    thorskur  163     57    20   1    nei      ja         5.0
   ## 6  STAE209 landvaettir  175     59    20   1    nei      ja         5.0
   ##   fyrriPuls seinniPuls  inngrip dagsetning
   ## 1        83         84 sat_kyrr   7.1.2013
   ## 2        80        103    hljop   7.1.2013
   ## 3        43         52 sat_kyrr   7.1.2013
   ## 4        76        105    hljop   7.1.2013
   ## 5        71         68 sat_kyrr   7.1.2013
   ## 6        65         65 sat_kyrr   7.1.2013

str()
^^^^^

.. attention::

    **Inntak:** nafn á gagnatöflu
    
    **Úttak:** samantektir fyrir breyturnar


--------------

Önnur góð leið til að fá fljótt yfirlit yfir breytur gagnatöflunnar er
að nota skipunina ``str()``. Hún sýnir okkur á hvaða formi R skráir
hvaða breytu og gefur einnig stutt yfirlit yfir það á hvaða bili
mælingarnar liggja. Í okkar tilviki væri skipunin:

::

   str(puls)
   ## 'data.frame':    471 obs. of  13 variables:
   ##  $ namskeid   : Factor w/ 2 levels "LAN203","STAE209": 2 1 1 2 2 2 1 2 2 1 ...
   ##  $ kronukast  : Factor w/ 2 levels "landvaettir",..: 1 2 1 2 2 1 1 1 2 1 ...
   ##  $ haed       : num  161 185 167 174 163 175 178 191 176 176 ...
   ##  $ thyngd     : num  60 115 NA 67 57 59 70 94 68 82 ...
   ##  $ aldur      : int  23 52 22 21 20 20 39 21 20 70 ...
   ##  $ kyn        : int  1 2 1 1 1 1 1 2 1 2 ...
   ##  $ reykir     : Factor w/ 2 levels "ja","nei": 2 NA 2 2 2 2 NA 2 2 2 ...
   ##  $ drekkur    : Factor w/ 2 levels "ja","nei": 2 1 1 1 1 1 1 1 1 1 ...
   ##  $ likamsraekt: num  3.5 0 2 1 5 5 3.5 0 10 14 ...
   ##  $ fyrriPuls  : int  83 80 43 76 71 65 77 79 73 65 ...
   ##  $ seinniPuls : int  84 103 52 105 68 65 75 83 90 78 ...
   ##  $ inngrip    : Factor w/ 2 levels "hljop","sat_kyrr": 2 1 2 1 2 2 2 2 1 1 ...
   ##  $ dagsetning : Factor w/ 3 levels "5.1.2015","6.1.2014",..: 3 3 3 3 3 3 3 3 ...

Við mælum eindregið með að nota ávalt ``str()`` skipunina til að kanna
hvort allar breytur gagnatöflunnar séu á réttu formi eftir innlestur
gagnanna.

length()
^^^^^^^^

.. attention::

    **Inntak:** nafn á vigri
    
    **Úttak:** lengd vigursins
    
    **Helstu stillingar:**


--------------

Skipunin ``length()`` gefur okkur lengd þess vigurs (breytu) sem hún er
mötuð með, þ.e.a.s. hún segir okkur hversu margar mælingar eru geymdar í
tilteknum vigri. Í dæminu að ofan gefur skipunin

::

   length(puls$haed)
   ## [1] 471

útkomuna :math:`471`. Þ.e.a.s. það eru :math:`471` mælingar á hæð
geymdar í breytunni ``haed`` í gagnatöflunni ``puls``.

dim()
^^^^^

.. attention::

    **Inntak:** nafn á gagnatöflu/fylki
    
    **Úttak:** vídd gagnatöflunnar/fylkisins


--------------

Skipunin ``dim()`` skilar fjölda lína og fjölda dálka í gagnatöflu,
þ.e.a.s. hversu margar mælingar og breytur eru í töflunni.

.. _s.vontun:

Vöntun mælinga
--------------

Vöntun mælinga
~~~~~~~~~~~~~~

Við vinnum afar oft með gagnatöflur þar sem það vantar mælingar á
einhverjum breytum hjá sumum viðfangsefnum. R leysir úr því með því að
gefa þeim mælingum gildið ``NA`` sem stendur einfaldlega fyrir "not
available", þ.e. mælinguna vantar. Í þessum undirkafla munum við kynnast
skipununum ``is.na()``, sem hjálpar okkur að finna mælingar sem vantar
og ``na.omit()`` sem fjarlægir mælingar sem vantar.

Margar þeirra R-skipana sem þið munuð kynnast seinna meir gefa villu ef
vigurinn sem við mötum þær með inniheldur NA gildi. Þar sem
stillingarnar eru ólíkar eftir því hverjar skipanirnar eru munum við
tilgreina þær með umfjöllun hverrar og einnar skipunar en ekki hér í
þessum kafla.

is.na()
^^^^^^^

.. attention::

    **Inntak:** vigur eða fylki
    
    **Úttak:** vigur eða fylki


--------------

Það er alltaf gott að kanna hvort það séu einhver NA gildi í breytunum
okkar áður en við hefjum úrvinnslu og hversu mörg þau eru. Til þess er
gott að nota skipunina ``is.na()`` en hún segir okkur hvort mæling sé NA
eða ekki. Sjáið sem dæmi:

::

   fjoldi <- c(2,5,3,NA,1)
   is.na(fjoldi)
   ## [1] FALSE FALSE FALSE  TRUE FALSE

Við mötuðum skipunina ``is.na()`` með vigri með fimm mælingum. Út kemur
vigur með fimm mælingum, þar sem stendur ``FALSE`` þar sem við höfum
mælingu en ``TRUE`` þar sem við höfum ``NA`` gildi, sem í þessu tilviki
er í fjórða sæti vigursins.

Það má líka mata gagnatöflu í ``is.na()`` og þá gefur skipunin töflu af
sömu stærð sem inniheldur FALSE á hverjum þeim stað sem mæling er til
staðar en TRUE þar sem NA gildi eru.

na.omit()
^^^^^^^^^

.. attention::

    **Inntak:** vigur eða fylki
    
    **Úttak:** vigur eða fylki


--------------

Önnur skipun, náskyld ``is.na()``, er ``na.omit()``. Hún getur bæði
verið mötuð á vigri og gagnatöflu. Sé hún mötuð á vigri skilar hún
samsvarandi vigri þar sem búið er að fjarlægja NA gildi. Sé hún mötuð
með gagnatöflu skilar hún nýrri gagnatöflu með viðfangsefnum sem enga
mælingu vantar hjá.

Skipunin

::

   puls2 <-na.omit(puls)

smíðar gagnatöfluna ``puls2`` sem inniheldur aðeins einstaklinga sem
enga mælingu vantar hjá. Gætið ykkar að við viljum afar sjaldan eyða út
öllum einstaklingum í gagnatöflu sem vantar *einhverja* mælingu hjá.
Segjum sem sem dæmi að það vanti margar mælingar á breytunni ``reykir``
í gagnasafninu okkar en í raun höfum við mestan áhuga á að rannsaka
breytuna ``haed``. Með því að henda út öllum einstaklingum sem vantar
mælingar á breytunni ``reykir`` erum við búin að henda út mælingum sem
við gætum notað í rannsóknum okkar á hæð.

.. _s.gildivalin:

Ákveðin gildi valin úr gagnatöflu
---------------------------------

Ákveðin gildi valin úr gagnatöflu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mikilvægur hluti af meðhöndlun gagna er að velja út ákveðinn hluta
gagnatöflunnar okkar. Eitt dæmi er ef við viljum skipta gögnunum okkar
upp í ``lög`` (e. strata) og annað er þegar við viljum búa til nýjar
breytur út frá þeim mælingum sem fyrir eru. Í þessum undirkafla munum
við fjalla um margar öflugar leiðir til að velja mælingar úr vigrum eða
gagnatöflum. Margar frábærar leiðir til slíks tilheyra pakkanum
``dplyr()`` og munum við kynnast nokkrum þeirra hér á eftir. Þá þarf að
gæta að pakkinn sé aðgengilegur í vinnulotunni okkar áður en við notum
aðferðirnar.

Nær allar aðferðir til að velja hluta af gögnum krefjast notkun
samanburðarvirkja. Sá einfaldasti þeirra er ``==`` en hann notum við til
að kanna hvort vigur innihaldi eitthvað tiltekið gildi. Þá ritum við
vigurinn fyrst, þá == og loks tiltekna gildið. Skipunin skilar
jafnlöngum vigri og þeim sem við mötuðum í skipunina sem inniheldur
eingöngu TRUE eða FALSE gildi. Sé ákveðna gildið í tilteknu sæti
vigursins inniheldur útkomuvigurinn TRUE í tilsvarandi sæti, en FALSE
annars. Í skipuninni hér að neðan skoðum við vigurinn ``puls$kyn`` sem
inniheldur kyn viðmælanda.

::

   puls$kyn == 1
   ##   [1]  TRUE FALSE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE  TRUE FALSE FALSE
   ##  [12] FALSE  TRUE FALSE  TRUE  TRUE FALSE FALSE  TRUE FALSE  TRUE  TRUE
   ##  [23] FALSE  TRUE  TRUE  TRUE FALSE  TRUE FALSE  TRUE FALSE  TRUE FALSE
   ....

Ekki gleyma því að setja gæsalappir utanum gildi breytunnar eigi það
við. Þær þurfum við alltaf að setja þegar gildið sem við viljum kanna er
kóðað með *orði* en ekki tölustaf.

Berið útkomuvigurinn saman við vigurinn

::

   puls$kyn
   ##   [1] 1 2 1 1 1 1 1 2 1 2 2 2 1 2 1 1 2 2 1 2 1 1 2 1 1 1 2 1 2 1 2 1 2 2 1
   ##  [36] 2 1 2 1 1 1 1 1 1 2 2 1 2 2 1 1 1 1 2 1 1 2 1 1 1 2 2 1 1 2 2 1 2 1 1
   ##  [71] 1 1 1 1 2 2 1 1 1 1 1 1 2 2 2 2 1 2 1 1 1 2 1 1 1 1 1 1 1 2 1 1 2 2 1
   ....

þannig sjáið þið að útkomuvigurinn inniheldur ``FALSE`` alls staðar þar
sem ``puls$kyn`` hefur gildið ``2`` en ``TRUE`` annars.
Samanburðarvirkinn er mikið notaður við lagskiptingu gagna.

Líkt og við notum ``==`` getum við einnig notað aðra samanburðarvirkja:

+--------+---------------------+
| ``>``  | stærri en           |
+--------+---------------------+
| ``>=`` | stærri eða jafnt og |
+--------+---------------------+
| ``<``  | minni en            |
+--------+---------------------+
| ``<=`` | minni eða jafnt og  |
+--------+---------------------+
| ``!=`` | ekki jafnt og       |
+--------+---------------------+
| ``&``  | og                  |
+--------+---------------------+
| ``|``  | eða                 |
+--------+---------------------+

Efstu virkjarnir fjórir skýra sig að mestu leyti sjálfir. Ef við viljum
t.d. búa til nýja gagnatöflu ``pulsS`` sem inniheldur aðeins einstaklinga
sem eru hærri en 170 cm á hæð gerum við það með:

::

   pulsS <- puls[puls$haed > 170, ]

Hvað varðar neðri virkjana tvo, þá er virkinn :math:`\&` mataður með
tveimur skilyrðum og skilar ``TRUE`` eingöngu ef *bæði* skilyrðin eru
uppfyllt. Virkinn :math:`|` er sömuleiðis mataður með tveimur skilyrðum
en það nægir að eingöngu *annað* þeirra séu uppfyllt til að hann skili
``TRUE``.

Síðast en ekki síst er virkinn ``%in%`` mikið notaður. Hann má nota til
að spyrja hvort gildi mælingar sé meðal einhverra annarra gildi. T.d.
skilar skipunin:

::

   puls$likamsraekt%in%c(7,8,9)
   ##   [1] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
   ##  [12] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE  TRUE FALSE
   ##  [23] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
   ....

gildinu ``TRUE`` ef breytan ``likamsraekt`` tekur eitthvert gildanna 7,
8 eða 9, en ``FALSE`` annars.

slice()
^^^^^^^

.. attention::

    **Inntak:** nafn á gagnatöflu og vigur
    
    **Úttak:** gagnatafla
    
    **Pakki:** dplyr


--------------

Fyrsta aðferðin sem við kynnumst úr ``dplyr`` er ``slice()``. Hana notum
við til að velja ákveðnar línur út gagnatöflu. Ef við viljum t.d. geyma
mælingar á fyrstu 10 viðfangsefnunum í ``puls`` gagnatöflunni í nýrri
gagnatöflu getum við gert það með:

::

   puls.first<-slice(puls,1:10)

filter()
^^^^^^^^

.. attention::

    **Inntak:** nafn á gagnatöflu og nöfn á breytum ásamt skilyrðum
    
    **Úttak:** gagnatafla
    
    **Pakki:** dplyr


--------------

Næsta skipun er ``filter()``. Hana notum við til að velja aðeins hluta
eða *lag* af gagnatöflunni okkar. Við mötum hana með nafninu á
gagnatöflunni sem við viljum lagskipta ásamt skilyrðum sem það lag sem
við ætlum að draga út þarf að uppfylla. Við getum t.d. búið til nýja
gagnatöflu sem inniheldur aðeins þá sem reykja með:

::

   puls.konur<-filter(puls,reykir=='ja')

Ef við viljum skoða gögn þeirra sem reykja og fengu landvætti getum við
gert það með (takið eftir að hér er ekki búin til ný gagnatafla):

::

   filter(puls,reykir=="ja", kronukast=='landvaettir')

::

   ##    namskeid   kronukast haed thyngd aldur kyn reykir drekkur likamsraekt
   ## 1   STAE209 landvaettir  194     79    28   2     ja      ja         4.0
   ## 2    LAN203 landvaettir  185     78    44   2     ja      ja         2.0
   ....

Einnig er, eins og við sáum hér á undan, hægt að nota hornklofa
(``[ ]``) til að velja hluta af gagnatöflu. Þá mötum við hornklofann með
tveimur vigrum af vísum sem við aðgreinum með kommu. Fyrst kemur
vísavigurinn sem tilgreinir hvaða viðfangsefni (línur) við viljum velja
síðan kemur vísavigurinn sem tilgreinir hvaða breytur (dálka) við viljum
velja. Við númerum viðfangsefni frá efsta viðfangsefninu til þess neðsta
(þ.e.a.s. efsta línan er númer eitt), en breyturnar frá vinstri til
hægri (þ.e.a.s. breytan lengst til vinstri er númer eitt).

Ef við viljum skoða hver mælingin á breytu 2 (``haed``) á viðfangsefni
23 er í gagnatöflunni okkar ``puls`` gefum við skipunina:

::

   puls[23,2]
   ## [1] thorskur
   ## Levels: landvaettir thorskur

Ef við sleppum fyrri vísavigrinum fáum við mælingar á öllum
viðfangsefnum fyrir breyturnar sem við tilgreinum í seinni vigrinum.
Þannig gefur skipunin

::

   puls[,2]

mælingarnar á hæð fyrir öll viðfangsefnin. Ef við sleppum seinni
vísavigrinum fáum við mælingar á öllum breytum fyrir viðfangsefnin sem
við tilgreinum í fyrri vigrinum. Þannig gefur skipunin

::

   puls[c(23,49),]
   ##    namskeid kronukast haed thyngd aldur kyn reykir drekkur likamsraekt
   ## 23  STAE209  thorskur  173     72    33   2     ja      ja           2
   ## 49  STAE209  thorskur  184     74    20   2    nei      ja          10
   ##    fyrriPuls seinniPuls inngrip dagsetning
   ## 23        68         79   hljop   7.1.2013
   ## 49        62         75   hljop   7.1.2013

allar mælingar fyrir viðfangsefni númer 23 og 49.

Að lokum getum við notað mínus til að skoða mælingar í gagnatöflu fyrir
öll viðfangsefni *nema* einhver tiltekin, eða allar breytur *nema*
einhverjar tilteknar.

::

   puls[-c(23,49), -2]

gefur mælingar fyrir öll viðfangsefni *nema* númer 23 og 49 og allar
breytur *nema* þá aðra.

which()
^^^^^^^

.. attention::

    **Inntak:** skilyrði
    
    **Úttak:** vigur eða fylki með vísum í stök sem uppfylla skilyrðið/in
    
    **Helstu stillingar:** arr.ind


--------------

Að lokum viljum við nefna tvær aðferðir sem fylgja grunnpakka R.
``which()`` aðferðin er einstaklega gagnleg og gefur hún okkur vísa á
gildi í vigri, gagnatöflu eða fylki sem uppfylla ákveðin skilyrði. Við
getum t.d. kannað hvaða einstaklingar eru hærri en 190 cm á hæð í puls
gögnunum okkar:

::

   which(puls$haed>190)
   ##  [1]   8  17  33  34  46  75  84 107 113 161 238 263 297 301 332 341 357
   ## [18] 358 370 399 408 431 437

Ef við mötum ``which()`` með tvívíðum hlut (fylki) og notum ``arr.ind``
stillinguna skilar aðferðin númerinu á línunni og á dálkinum sem
skilyrðunum er uppfyllt.

.. _rf.grep:

grep()
^^^^^^

.. attention::

    **Inntak:** nafn á skilyrði og nafn á vigri
    
    **Úttak:** gildi eða vísar fyrir gildi
    
    **Helstu stillingar:** value


--------------

Seinni skipunin er ``grep()``. Hún getur verið einstaklega handhæg ef
við viljum sem dæmi búa til flokkabreytur út frá textastrengjum.
Eftirfarandi skipun finnur til dæmis vísi allra þeirra dagsetninga sem
innihalda textastrenginn ``2013``.

::

   grep(2013, puls$dagsetning)
   ##   [1]   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
   ##  [18]  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34
   ##  [35]  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51
   ....

Ef við gefum stillinguna ``value=TRUE`` fáum við mælingarnar sem pössuðu
við leitarskilyrðið en ekki bara vísa þeirra:

::

   grep(2013, puls$dagsetning, value=TRUE)
   ##   [1] "7.1.2013" "7.1.2013" "7.1.2013" "7.1.2013" "7.1.2013" "7.1.2013"
   ##   [7] "7.1.2013" "7.1.2013" "7.1.2013" "7.1.2013" "7.1.2013" "7.1.2013"
   ##  [13] "7.1.2013" "7.1.2013" "7.1.2013" "7.1.2013" "7.1.2013" "7.1.2013"
   ....

.. _s.kodun:

Kóðun breyta
------------

Yfirleitt þarf að vinna talsvert með breyturnar í gagnatöflunni áður en
tölfræðileg úrvinnsla getur hafist. Bæði þarf oft að búa til nýjar,
afleiddar breytur, en einnig að gæta þess að breytur séu vistaðar á
réttu sniði og jafnvel að beita vörpunum af talnabreytum. Slíkt köllum
við einu orði að *kóða* breytur. Algengustu kóðanirnar sem við
framkvæmum eru að:

#) Kóða breytur sem voru skráðar sem tölur sem flokkabreytur og
   skilgreina gildi flokkanna með skipununum ``factor()`` og
   ``levels()``.

#) Skipta talnabreytum upp í bil og búa til flokkabreytur út frá þeim
   með skipuninni ``cut()``.

#) Sameina tvo eða fleiri flokka í flokkabreytu.

#) Kóða strengi eða flokkabreytur sem dagsetningar með ``as.Date()``.

#) Búa til breytu með því að leita eftir textabútum í strengjum með
   ``grep()``.

#) Gefa breytum þægilegri heiti með skipuninni ``rename()``.

#) Beita vörpunum á talnabreytur.

Við förum nánar í þessi atriði hér fyrir neðan.

A: Flokkabreytur skilgreindar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

factor()
^^^^^^^^

.. attention::

    **Inntak:** nafn talnabreytu
    
    **Úttak:** flokkabreyta
    
    **Helstu stillingar:** levels, labels, ordered


--------------

Flokkabreytur eru oft kóðaðar með tölum og þá mun R vista þær sem
talnabreytur þegar gögnin eru lesin inn. Slíkt á t.d. við breytuna
``kyn`` í gagnatöflunni ``puls``. Við notum skipunina ``factor()`` til
að gefa R til kynna að breyta sé flokkabreyta. Ef við viljum leiðrétta
hvernig breytan ``kyn`` er vistuð í gagnatöflunni sjálfri notum við
skipunina:

::

   puls$kyn <- factor(puls$kyn)

Takið eftir því að hér að ofan yfirskrifum við gömlu talnabreytuna
``kyn`` með nýju flokkabreytunni (þær bera sama nafn). Í þessu tilviki
er það einmitt það sem við viljum gera. Það gæti þó komið fyrir að við
viljum halda í gömlu talnabreytuna en þá þurfum við að búa til nýja
breytu í stað þess að skrifa yfir þá gömlu. Til að gera það þurfum við
að gæta að nota annað nafn en á upphaflegu talnabreytunni. Með
eftirfarandi skipun búum við til nýja breytu ``kynf`` í gagnatöflunni
``puls``.

::

   puls$kynf <- factor(puls$kyn)

Hefðum við aðeins keyrt seinni ``factor()`` skipunina ættum við til
talnabreytuna ``kyn`` í gagnatöflunni ásamt flokkabreytunni ``kynf``.

R meðhöndlar flokkabreytur á annan hátt en talnabreytur, réttilega. Því
er mikilvægt að breytur séu ætíð rétt skráðar svo að til að mynda gröf
af þeim breytum séu rétt teiknuð og margt fleira.

levels()
^^^^^^^^

.. attention::

    **Inntak:** nafn á flokkabreytu
    
    **Úttak:** nöfn á flokkum flokkabreytunnar


--------------

Hægt er að nota ``levels()`` skipunina til að endurskýra nöfn á flokkum
í flokkabreytu. Viljum við endurskýra nöfnin á flokkunum í breytunni
``kyn`` er ágætt að byrja á að keyra skipunina

::

   levels(puls$kyn)
   ## [1] "1" "2"

því hún skilar okkur núverandi nöfnum. Viljum við breyta nöfnunum á
flokkunum í ``kvk`` og ``kk`` gerum við það með:

::

   levels(puls$kyn)<-c("kvk","kk")

Hér þarf að passa að röðunin sé rétt miðað við gömlu heitin, annars
breytum við öllum konum í kk og körlum í kvk.

B: Talnabreytum skipt upp í bil
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

cut()
^^^^^

.. attention::

    **Inntak:** talnabreyta
    
    **Úttak:** flokkabreyta
    
    **Helstu stillingar:** breaks, include.lowest, right


--------------

Stundum viljum við skipta gildum talnabreytu upp í flokka. ``cut()``
aðferðin tekur inn talnabreytu, skiptir gildum hennar upp í flokka sem
notandinn skilgreinir og skilar svo flokkabreytu. Við mötum aðferðina
með mörkunum á flokkunum en það má gera á nokkra vegu með hjálp
``include.lowest`` og ``right`` stillingunum. Skoðið ``help(cut)`` til
að kanna nánar hvernig aðferðin virkar.

Búum nú til flokkabreytu úr talna breytunni ``likamsraekt``. Við ætlum
að skipta viðfangsefnunum upp í þrjá flokka, þá sem stunda litla
líkamsrækt (0-1 klst. á viku), miðlungs (2-4 klst. á viku) og þá sem
stunda mikla líkamsrækt (:math:`>` 5 klst. á viku). Gætið þess að skýra
nýju breytuna eitthvað annað en ``likamsraekt`` svo við yfirskrifum ekki
talnabreytuna heldur búum þess í stað til nýja breytu. Við mötum
aðferðina með nafninu á talnabreytunni ``likamsraekt`` og mörkunum á
flokkunum. Ætlum við að tilgreina vinstri mörkin á flokkunum okkar
(lægri mörkin) notum við ``right=F`` stillinguna. Við mötum því
aðferðina með 0,2,5 (neðri mörkin á flokkunum okkar) en þurfum svo að
gefa efra mark á síðasta flokknum. Þetta þarf að vera gildi sem er
a.m.k. einu gildi hærra en hæsta gildið sem talnabreytan tekur. Hér
notum við gildið 100 (fallegra væri að nota
``max(puls$likamsraekt)+1``):

::

   puls$likamsraektf<-cut(puls$likamsraekt,c(0,2,5,100),right=F)

Hér sjáum við hversu margir verða í hverjum flokki:

::

   table(puls$likamsraektf)
   ##
   ##   [0,2)   [2,5) [5,100)
   ##      85     191     190

Við getum svo notað ``levels()`` skipunina til að endurskýra flokkana:

::

   levels(puls$likamsraektf)<-c("Lítil","Miðlungs","Mikil")
   table(puls$likamsraektf)
   ##
   ##    Lítil Miðlungs    Mikil
   ##       85      191      190

C: Flokkar sameinaðir
~~~~~~~~~~~~~~~~~~~~~

Afar oft viljum við sameina tvo eða fleiri flokka flokkabreytu. Í R
framkvæmum við það með því að gefa tveimur eða fleiri flokkum sama
heitið með skipuninni ``levels()``. Segjum sem svo að við viljum
sérstaklega kanna mun á þeim nemendum sem stunda mikla líkamsrækt í
samanburði við alla aðra nemendur. Þá væri handhægt að hafa nýja breytu
``likamsraekt2`` sem tekur bara tvö gildi: ``ekkiMikil`` og ``Mikil``.

Þegar við búum til breytuna ætlum við að sameina flokkana ``Lítil`` og
``Miðlungs`` undir nafninu ``ekkiMikil``. Búum fyrst til afrit af
breytunni og sjáum í hvaða röð flokkarnir eru taldir upp:

::

   puls$likamsraekt2 <- puls$likamsraektf
   levels(puls$likamsraekt2)
   ## [1] "Lítil"    "Miðlungs" "Mikil"

Flokkarnir sem við ætlum að sameina eru fyrstu tveir flokkarnir sem eru
taldir upp. Því skrifum við ``ekkiMikil`` í fyrstu tvö sætin en
``Mikil`` á sama stað og hún stóð áður.

::

   levels(puls$likamsraekt2) <- c('ekkiMikil','ekkiMikil','Mikil')

Nýja sameinaða breytan hefur eingöngu tvo flokka:

::

   str(puls$likamsraekt2)
   ##  Factor w/ 2 levels "ekkiMikil","Mikil": 1 1 1 1 2 2 1 1 2 2 ...

D: Dagsetningabreytur skilgreindar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

as.Date()
^^^^^^^^^

.. attention::

    **Inntak:** nafn bókstafabreytu
    
    **Úttak:** dagsetningabreyta
    
    **Helstu stillingar:** format


--------------

Það er mjög algengt að einhverjar breytanna okkar geymi dagsetningar.
Yfirleitt verða þær sjálfkrafa lesnar inn sem flokkabreytur en við getum
sjaldnast unnið með þær á því formi. Þess í stað vistum við þær sem
dagsetningar með skipuninni ``as.Date()``. Með stillingunni ``format``
tilgreinum við hvernig dagsetningarnar eru skráðar. Kemur ártalið fyrst,
svo mánuðurinn og svo dagurinn eða jafnvel öfugt? Eru dagar og mánuðir
aðgreindir með punkti eða bandstriki? Allt það má tilgreina með
auðveldum hætti og má sjá öll möguleg snið með því að skoða:

::

   help(strptime)

Í okkar tilviki kemur fyrst dagur, svo mánuður og þá fjögurra bókstafa
ár, allt aðskilið með punkti. Því gefum við stillinguna
``format=’%d.%m.%Y’``. Einnig vistaðist dagsetningin sem flokkabreyta
við innlestur (þar sem hún inniheldur ekki bara tölur, heldur líka
punkta). Því þarf að mata ``as.Date()`` með
``as.character(puls$dagsetning)``, skipun sem breytir flokkabreytu í
orðabreytu.

::

   puls$dagsetning <- as.Date(as.character(puls$dagsetning), format='%d.%m.%Y' )

Nú sjáið þið að dagsetningin er komin á rétt form:

::

   str(puls)
   ## 'data.frame':    471 obs. of  15 variables:
   ##  $ namskeid    : Factor w/ 2 levels "LAN203","STAE209": 2 1 1 2 2 2 1 2 2 1 ...
   ##  $ kronukast   : Factor w/ 2 levels "landvaettir",..: 1 2 1 2 2 1 1 1 2 1 ...
   ##  $ haed        : num  161 185 167 174 163 175 178 191 176 176 ...
   ##  $ thyngd      : num  60 115 NA 67 57 59 70 94 68 82 ...
   ##  $ aldur       : int  23 52 22 21 20 20 39 21 20 70 ...
   ##  $ kyn         : Factor w/ 2 levels "kvk","kk": 1 2 1 1 1 1 1 2 1 2 ...
   ##  $ reykir      : Factor w/ 2 levels "ja","nei": 2 NA 2 2 2 2 NA 2 2 2 ...
   ##  $ drekkur     : Factor w/ 2 levels "ja","nei": 2 1 1 1 1 1 1 1 1 1 ...
   ##  $ likamsraekt : num  3.5 0 2 1 5 5 3.5 0 10 14 ...
   ##  $ fyrriPuls   : int  83 80 43 76 71 65 77 79 73 65 ...
   ##  $ seinniPuls  : int  84 103 52 105 68 65 75 83 90 78 ...
   ##  $ inngrip     : Factor w/ 2 levels "hljop","sat_kyrr": 2 1 2 1 2 2 2 2 1 1 ...
   ##  $ dagsetning  : Date, format: "2013-01-07" "2013-01-07" ...
   ##  $ likamsraektf: Factor w/ 3 levels "Lítil","Miðlungs",..: 2 1 2 1 3 3 2 1 3 ...
   ##  $ likamsraekt2: Factor w/ 2 levels "ekkiMikil","Mikil": 1 1 1 1 2 2 1 1 2 2 ...

E: Leitað eftir textastrengjum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Stundum eru sumar breyturnar okkar langir textastrengir sem geyma ýmsar
upplýsingar en við viljum draga tilteknar upplýsingar út úr strengjunum
og nota til að búa til breytur. Þá kemur skipunin ``grep()``, sem við
sáum í kassa :numref:`%s <rf.grep>`, að góðum notum. Ef við viljum sem dæmi búa
til nýja breytu, ``ar`` sem geymir hvaða ár tilraunin var framkvæmd
fyrir hverja mælingu þá má útbúa hana með:

::

   puls$ar <- NA
   puls$ar[grep(2013, puls$dagsetning)] <- 2013
   puls$ar[grep(2014, puls$dagsetning)] <- 2014
   puls$ar[grep(2015, puls$dagsetning)] <- 2015

Nú er orðin til ný breyta, sem inniheldur bara ártalið. Það sem það eru
bara tölur er breytan talnabreyta.

::

   str(puls$ar)
   ##  num [1:471] 2013 2013 2013 2013 2013 ...

F: Breytt um heiti á breytum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

rename()
^^^^^^^^

.. attention::

    **Inntak:** nafn á gagnatöflu og nöfn á breytum
    
    **Úttak:** gagnatafla
    
    **Pakki:** dplyr


--------------

Hægt er, á auðveldan hátt, að endurskýra breytur í gagnatöflu með
``rename()`` aðferðinni. Viljum við t.d. breyta nafninu á breytunni
``namskeid`` í ``nam`` gerum við það með:

::

   puls<-rename(puls,nam=namskeid)

Til að valda ekki ruglingi hér breytum við nafninu aftur í ``namskeid``
með:

::

   puls<-rename(puls,namskeid=nam)

G: Vörpunum beitt á talnabreytur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Að lokum viljum við oft búa til nýjar, afleiddar breytur út frá öðrum
flokkabreytum. Þannig getum við t.d. búið til breytuna BMI út frá hæð og
þyngd:

::

   puls$BMI <- puls$thyngd/(puls$haed/100)**2

.. _s.umrodun:

Umröðun gagna
-------------

Umröðun gagna
~~~~~~~~~~~~~

Ef gagnatöflurnar sem verið er að vinna með innihalda margar breytur
getur verið gott að geta valið þær breytur sem við ætlum að vinna með á
auðveldan hátt. Við getum t.d. búið til nýja gagnatöflu sem inniheldur
aðeins breyturnar ``haed`` og ``thyngd`` (takið eftir að nýja
gagnataflan er ekki geymd í nýjum hlut hér, ætlum við að nota hana
þurfum við að búa til nýja töflu eins og hér að neðan).

::

   select(puls,haed,thyngd)
   ##      haed thyngd
   ## 1   161.0   60.0
   ## 2   185.0  115.0
   ## 3   167.0     NA
   ## 4   174.0   67.0
   ## 5   163.0   57.0
   ## 6   175.0   59.0
   ## 7   178.0   70.0
   ## 8   191.0   94.0
   ## 9   176.0   68.0
   ....

Við getum einnig notað ``select()`` aðferðina til að búa til nýja
gagnatöflu sem inniheldur alla dálka upphaflegu töflunnar að
undanskildum nokkrum. Viljum við t.d. búa til nýja gagnatöflu sem
inniheldur allar breytur upphaflegu töflunnar nema ``haed`` og
``thyngd`` gerum við það með:

::

   puls.minni<-select(puls,-c(haed,thyngd))

sort()
^^^^^^

.. attention::

    **Inntak:** nafn á vigri
    
    **Úttak:** vigur með röðuðum gildum
    
    **Helstu stillingar:** decreasing


--------------

Oft getur verið þægilegt að raða mælingunum okkar eftir stærðarröð.
Viljum við raða gildunum á einni breytu/vigri í stærðarröð gerum við það
með ``sort()`` aðferðinni. Viljum við t.d. skoða mælingarnar á hæð í
stærðarröð gerum við það með:

::

   sort(puls$haed)
   ##   [1] 150.0 152.0 152.0 154.0 154.0 155.0 156.0 156.0 157.0 157.0 157.0
   ##  [12] 157.0 157.0 157.0 157.0 157.0 158.0 158.0 158.0 159.0 159.0 159.0
   ##  [23] 159.0 160.0 160.0 160.0 160.0 160.0 160.0 160.0 160.0 160.0 160.0
   ##  [34] 160.0 160.0 160.0 160.0 160.0 160.0 160.0 160.5 161.0 161.0 161.0
   ##  [45] 161.0 161.0 161.0 161.0 161.0 161.0 161.0 161.0 162.0 162.0 162.0
   ##  [56] 162.0 162.0 162.0 162.0 162.0 162.0 162.0 163.0 163.0 163.0 163.0
   ....

arrange()
^^^^^^^^^

.. attention::

    **Inntak:** nafn á gagnatöflu og nöfn á breytum
    
    **Úttak:** gagnatafla
    
    **Pakki:** dplyr


--------------

Í sumum tilfellum er einnig gott að geta raðað viðfangsefnum í
gagnatöflu eftir ákveðinni röð. ``arrange()`` aðferðin gerir okkur það
kleift á auðveldan hátt. Við mötum aðferðina með nafninu á gagnatöflunni
og breytunum sem við viljum raða eftir. Viljum við t.d. raða
viðfangsefnunum í puls gagnasafninu eftir hæð gerum við það með:

::

   arrange(puls,haed)
   ##     namskeid   kronukast  haed thyngd aldur kyn reykir drekkur likamsraekt
   ## 1    STAE209 landvaettir 150.0   76.3    23 kvk    nei     nei         2.0
   ## 2    STAE209 landvaettir 152.0   47.0    20 kvk    nei     nei         2.0
   ## 3    STAE209 landvaettir 152.0   47.0    20 kvk    nei     nei         2.0
   ## 4     LAN203 landvaettir 154.0   50.0    28 kvk    nei     nei         4.0
   ## 5     LAN203 landvaettir 154.0   50.0    28 kvk    nei     nei         4.0
   ## 6     LAN203 landvaettir 155.0   49.0    22 kvk     ja      ja        12.0
   ## 7     LAN203    thorskur 156.0   69.0    36 kvk    nei      ja         3.0
   ## 8    STAE209 landvaettir 156.0   65.0    21 kvk    nei     nei         2.0
   ## 9    STAE209 landvaettir 157.0   51.0    20 kvk    nei      ja         0.0
   ....

Viljum við hins vegar raða fyrst eftir aldri og svo eftir hæð gerum við
það með:

::

   arrange(puls,aldur,haed)
   ##     namskeid   kronukast  haed thyngd aldur kyn reykir drekkur likamsraekt
   ## 1    STAE209    thorskur 162.0   56.0    19 kvk    nei     nei         2.0
   ## 2    STAE209    thorskur 164.0   58.0    19 kvk    nei      ja         4.0
   ## 3    STAE209    thorskur 164.0   58.0    19 kvk    nei      ja         4.0
   ## 4    STAE209 landvaettir 172.0   55.0    19 kvk    nei      ja         6.0
   ## 5    STAE209    thorskur 172.0   53.0    19  kk    nei    <NA>         7.0
   ## 6    STAE209 landvaettir 172.0   55.0    19 kvk    nei      ja         6.0
   ## 7    STAE209 landvaettir 177.0   72.0    19 kvk    nei      ja         2.0
   ## 8     LAN203 landvaettir 181.0   85.0    19  kk    nei      ja         2.0
   ## 9     LAN203 landvaettir 185.0   60.0    19  kk    nei     nei         6.0
   ....

.. _rf.gather:

gather()
^^^^^^^^

.. attention::

    **Inntak:** nafn á gagnatöflu og tveir vigrar
    
    **Úttak:** gagnatafla
    
    **Pakki:** tidyr


--------------

Skipunin ``gather()`` varpar gögnum úr víðu sniði í langt á handhægan
hátt. Sem dæmi eru upplýsingarnar um púls núna geymdar í tveimur
breytum, ``fyrriPuls`` og ``seinniPuls``. Við gætum þess í stað haft
eina breytu, ``pulsmaeling``, sem geymir púlsmælinguna og aðra breytu,
``nr.maelingar`` sem tilgreinir hvort mælingin eigi við fyrri eða seinni
púlsmælinguna. Þetta er framkvæmt með skipuninni:

::

   pulslangt <- gather(puls, nr.maelingar, pulsmaeling, fyrriPuls:seinniPuls)

Fyrst tilgreinum við nafnið á gagnatöflunni sem við erum að vinna með,
þar næst kemur hvað breytan sem greinir að hvort að mælingin er fyrr eða
seinni púlsmæling á að heita. Við látum hana heita ``nr.maelingar``. Þar
næst kemur hvað breytan sem tilgreinir hver mældi púlsinn er heitir, við
gefum henni nafnið ``pulsmaeling`` og að lokum koma breyturnar tvær
``fyrriPuls`` og ``seinniPuls``, aðgreindar með ``:``, sem að áður
geymdu púlsmælingarnar á víðu sniði. Sjáið muninn:

::

   head(pulslangt)
   ##   namskeid   kronukast haed thyngd aldur kyn reykir drekkur likamsraekt
   ## 1  STAE209 landvaettir  161     60    23 kvk    nei     nei         3.5
   ## 2   LAN203    thorskur  185    115    52  kk   <NA>      ja         0.0
   ## 3   LAN203 landvaettir  167     NA    22 kvk    nei      ja         2.0
   ## 4  STAE209    thorskur  174     67    21 kvk    nei      ja         1.0
   ## 5  STAE209    thorskur  163     57    20 kvk    nei      ja         5.0
   ## 6  STAE209 landvaettir  175     59    20 kvk    nei      ja         5.0
   ##    inngrip dagsetning likamsraektf likamsraekt2   ar      BMI nr.maelingar
   ## 1 sat_kyrr 2013-01-07     Miðlungs    ekkiMikil 2013 23.14726    fyrriPuls
   ## 2    hljop 2013-01-07        Lítil    ekkiMikil 2013 33.60117    fyrriPuls
   ## 3 sat_kyrr 2013-01-07     Miðlungs    ekkiMikil 2013       NA    fyrriPuls
   ## 4    hljop 2013-01-07        Lítil    ekkiMikil 2013 22.12974    fyrriPuls
   ## 5 sat_kyrr 2013-01-07        Mikil        Mikil 2013 21.45357    fyrriPuls
   ## 6 sat_kyrr 2013-01-07        Mikil        Mikil 2013 19.26531    fyrriPuls
   ##   pulsmaeling
   ## 1          83
   ## 2          80
   ## 3          43
   ## 4          76
   ## 5          71
   ## 6          65

.. _rf.spread:

spread()
^^^^^^^^

.. attention::

    **Inntak:** nafn á gagnatöflu og tveir vigrar
    
    **Úttak:** gagnatafla
    
    **Pakki:** tidyr


--------------

Skipunin ``spread`` er andhverfa ``gather()``, þ.e.a.s. hún varpar
gögnum úr löngu sniði í vítt. Þannig vörpum við löngu ``pulslangt``
gögnunum sem við bjuggum til að ofan yfir í langt snið með skipuninni:

::

   pulsvitt <- spread(pulslangt, nr.maelingar, pulsmaeling)

Hér þarf eingöngu að tilgreina breyturnar tvær sem á að skilja í sundur.
R sér um rest, eins og sjá má:

::

   head(pulsvitt)
   ##   namskeid   kronukast haed thyngd aldur kyn reykir drekkur likamsraekt
   ## 1  STAE209 landvaettir  161     60    23 kvk    nei     nei         3.5
   ## 2   LAN203    thorskur  185    115    52  kk   <NA>      ja         0.0
   ## 3   LAN203 landvaettir  167     NA    22 kvk    nei      ja         2.0
   ## 4  STAE209    thorskur  174     67    21 kvk    nei      ja         1.0
   ## 5  STAE209    thorskur  163     57    20 kvk    nei      ja         5.0
   ## 6  STAE209 landvaettir  175     59    20 kvk    nei      ja         5.0
   ##    inngrip dagsetning likamsraektf likamsraekt2   ar      BMI fyrriPuls
   ## 1 sat_kyrr 2013-01-07     Miðlungs    ekkiMikil 2013 23.14726        83
   ## 2    hljop 2013-01-07        Lítil    ekkiMikil 2013 33.60117        80
   ## 3 sat_kyrr 2013-01-07     Miðlungs    ekkiMikil 2013       NA        43
   ## 4    hljop 2013-01-07        Lítil    ekkiMikil 2013 22.12974        76
   ## 5 sat_kyrr 2013-01-07        Mikil        Mikil 2013 21.45357        71
   ## 6 sat_kyrr 2013-01-07        Mikil        Mikil 2013 19.26531        65
   ##   seinniPuls
   ## 1         84
   ## 2        103
   ## 3         52
   ## 4        105
   ## 5         68
   ## 6         65

.. _rf.merge:

merge()
^^^^^^^

.. attention::

    **Inntak:** tvær gagnatöflur
    
    **Úttak:** ein sameinuð gagnatafla
    
    **Helstu stillingar:** by, all.x, all.y


--------------

Að lokum er ``merge()`` einstaklega handhæg skipun til að sameina tvær
gagnatöflur. Hugsum okkur sem svo að við hefðum bakgrunnsupplýsingar um
nemendurna í einni gagnatöflu, en púlsmælingarnar í annarri gagnatöflu.
Hver og ein skrá hefði svo að geyma *lykil*, t.d. gervinúmer fyrir hvern
og einn nemanda sem gerir okkur kleift að para saman mælingarnar. Búum
til að byrja með til tvær slíkar gagnatöflur til að geta sýnt hvernig
þær væru sameinaðar ef svo væri raunin:

::

   puls$id <- 1:(dim(puls)[1])  #lykill með gervinúmerum
   bakgrunnur <- select(puls,id, namskeid, haed, thyngd, aldur,
   kyn, reykir, drekkur, likamsraekt, likamsraektf )
   pulsmaeling <- select(puls, id, kronukast, fyrriPuls, seinniPuls,
   inngrip, dagsetning, ar)

Hér má sjá gagnatöflurnar tvær:

::

   head(bakgrunnur)
   ##   id namskeid haed thyngd aldur kyn reykir drekkur likamsraekt
   ## 1  1  STAE209  161     60    23 kvk    nei     nei         3.5
   ## 2  2   LAN203  185    115    52  kk   <NA>      ja         0.0
   ## 3  3   LAN203  167     NA    22 kvk    nei      ja         2.0
   ## 4  4  STAE209  174     67    21 kvk    nei      ja         1.0
   ## 5  5  STAE209  163     57    20 kvk    nei      ja         5.0
   ## 6  6  STAE209  175     59    20 kvk    nei      ja         5.0
   ##   likamsraektf
   ## 1     Miðlungs
   ## 2        Lítil
   ## 3     Miðlungs
   ## 4        Lítil
   ## 5        Mikil
   ## 6        Mikil
   head(pulsmaeling)
   ##   id   kronukast fyrriPuls seinniPuls  inngrip dagsetning   ar
   ## 1  1 landvaettir        83         84 sat_kyrr 2013-01-07 2013
   ## 2  2    thorskur        80        103    hljop 2013-01-07 2013
   ## 3  3 landvaettir        43         52 sat_kyrr 2013-01-07 2013
   ## 4  4    thorskur        76        105    hljop 2013-01-07 2013
   ## 5  5    thorskur        71         68 sat_kyrr 2013-01-07 2013
   ## 6  6 landvaettir        65         65 sat_kyrr 2013-01-07 2013

Þær eru sameinaðar með skipuninni ``merge():``

::

   puls <- merge(bakgrunnur, pulsmaeling)

sem er sama skrá og við byrjuðum með:

::

   dim(puls)
   ## [1] 471  16
   head(puls)
   ##   id namskeid haed thyngd aldur kyn reykir drekkur likamsraekt
   ## 1  1  STAE209  161     60    23 kvk    nei     nei         3.5
   ## 2  2   LAN203  185    115    52  kk   <NA>      ja         0.0
   ## 3  3   LAN203  167     NA    22 kvk    nei      ja         2.0
   ## 4  4  STAE209  174     67    21 kvk    nei      ja         1.0
   ## 5  5  STAE209  163     57    20 kvk    nei      ja         5.0
   ## 6  6  STAE209  175     59    20 kvk    nei      ja         5.0
   ##   likamsraektf   kronukast fyrriPuls seinniPuls  inngrip dagsetning   ar
   ## 1     Miðlungs landvaettir        83         84 sat_kyrr 2013-01-07 2013
   ## 2        Lítil    thorskur        80        103    hljop 2013-01-07 2013
   ## 3     Miðlungs landvaettir        43         52 sat_kyrr 2013-01-07 2013
   ## 4        Lítil    thorskur        76        105    hljop 2013-01-07 2013
   ## 5        Mikil    thorskur        71         68 sat_kyrr 2013-01-07 2013
   ## 6        Mikil landvaettir        65         65 sat_kyrr 2013-01-07 2013

Sjálfgefið er að sameina gagnatöflurnar tvær á öllum þeim breytum sem
bera sama heiti í töflunum tveimur. Í þessu tilviki er bara ein breyta
sem ber sama heitið, það er breytan ``id`` og því er eingöngu sameinað
eftir henni. Ef að fleiri breytur hafa sama heiti, en við viljum þó ekki
sameina eftir þeim, þá tilgreinum við það með stillingunni ``by``.

Sömuleiðis er sjálfgefið að sameina eingöngu þær mælingar sem svara til
lykils sem er að finna í báðum töflunum. Þ.e.a.s. ef að tiltekið ``id``
í dæminu hér að ofan væri eingöngu að finna í gagnatöflunni
``bakgrunnur`` en ekki í gagnatöflunni ``pulsmaeling`` þá væri henni
sleppt. Við getum sagt R að sleppa engri mælingu í fyrri gagnatöflunni
(og fylla þá upp í breyturnar úr seinni töflunni með ``NA`` með
stillingunni ``all.x=TRUE``). Á sama hátt getum við bætt við
``all.y=TRUE`` ef við viljum að það sama gildi fyrir seinni
gagnatöfluna.

.. _1.meira:

Fleiri skipanir fyrir kóðun breyta\ :math:`^\ast`
-------------------------------------------------

Fleiri skipanir fyrir kóðun breyta\ :math:`^\ast`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fjórar skipanir sem koma oft að góðum notum við kóðun breyta eru
``paste()``, ``sprintf()``, ``separate()`` og ``substr()``.

paste()
^^^^^^^

.. attention::

    **Inntak:** tveir vigrar, eða vigur og gildi
    
    **Úttak:** vigur með gildunum sameinuðum
    
    **Helstu stillingar:** sep


--------------

Skipunin ``paste()`` býr til einn vigur með því að skella saman gildunum
í tveimur vigrum. Stillingin ``sep`` tilgreinir hvaða tákna skal notað
til að sameina vigrana. Þannig getum við búið til nýja breytur sem
tilgreinir í hvaða námskeiði, hvaða ár nemendurnir eru með:

::

   puls$namskeidar <- paste(puls$namskeid, puls$ar)
   str(puls$namskeidar)
   ##  chr [1:471] "STAE209 2013" "LAN203 2013" "LAN203 2013" ...

sprintf()
^^^^^^^^^

.. attention::

    **Inntak:** strengur (eða strengjavigur) með skiptitákni, annað inntak
    
    **Úttak:** vigur með nýjum streng byggðum á inntaki


--------------

Skipunin ``sprintf()`` býr til einn vigur með því að taka streng með
sérstökum skiptitáknum og skipta þeim út fyrir gildin úr öðru inntaki
fallsins. Vilji maður t.d. búa til streng sem gefur manni dagsetningu þá
er það hægt með:

::

   sprintf('Dagurinn i dag er %s', Sys.Date())
   ## [1] "Dagurinn i dag er 2016-01-04"

þar sem :math:`\%`\ s er skiptitáknið.

separate()
^^^^^^^^^^

.. attention::

    **Inntak:** einn vigur og tákn sem á skipta gildunum upp eftir
    
    **Úttak:** tveir eða fleiri vigrara
    
    **Pakki:** tidyr


--------------

Skipunin ``separate()`` er andhverfa skipunarinnar ``paste()``, þ.e.a.s.
hún slítur í sundur breytur eftir einhverju tákni og býr til tvær eða
fleiri nýjar. Þannig getum við skipt dagsetningunni upp í þrjár breytur:
dag, mánuð og ár með skipuninni:

::

   pulsnytt <- separate(puls, dagsetning, into=c('ar','manudur','dagur'), sep='-')

Hér má sjá nýju gagnatöfluna, með þremur nýjum breytum:

::

   head(pulsnytt)
   ##   id namskeid haed thyngd aldur kyn reykir drekkur likamsraekt
   ## 1  1  STAE209  161     60    23 kvk    nei     nei         3.5
   ## 2  2   LAN203  185    115    52  kk   <NA>      ja         0.0
   ## 3  3   LAN203  167     NA    22 kvk    nei      ja         2.0
   ## 4  4  STAE209  174     67    21 kvk    nei      ja         1.0
   ## 5  5  STAE209  163     57    20 kvk    nei      ja         5.0
   ## 6  6  STAE209  175     59    20 kvk    nei      ja         5.0
   ##   likamsraektf   kronukast fyrriPuls seinniPuls  inngrip   ar manudur
   ## 1     Miðlungs landvaettir        83         84 sat_kyrr 2013      01
   ## 2        Lítil    thorskur        80        103    hljop 2013      01
   ## 3     Miðlungs landvaettir        43         52 sat_kyrr 2013      01
   ## 4        Lítil    thorskur        76        105    hljop 2013      01
   ## 5        Mikil    thorskur        71         68 sat_kyrr 2013      01
   ## 6        Mikil landvaettir        65         65 sat_kyrr 2013      01
   ##   dagur   ar   namskeidar
   ## 1    07 2013 STAE209 2013
   ## 2    07 2013  LAN203 2013
   ## 3    07 2013  LAN203 2013
   ## 4    07 2013 STAE209 2013
   ## 5    07 2013 STAE209 2013
   ## 6    07 2013 STAE209 2013

substr()
^^^^^^^^

.. attention::

    **Inntak:** orðabreyta og vísar bókstafa sem skulu valdir
    
    **Úttak:** sá hluti úr orðabreytunni sem svarar til þeirra vísa


--------------

Skipunin ``substr()`` velur ákveðna bókstafi úr orðabreytu, til dæmis
þriðja til sjöunda bókstafinn, eða álíka. Ef við viljum sem dæmi bara fá
fyrstu þrjá stafina í nöfnunum á námskeiðunum, þá gerum við það með:

::

   substr(puls$namskeid, 1,3)
   ##   [1] "STA" "LAN" "LAN" "STA" "STA" "STA" "LAN" "STA" "STA" "LAN" "LAN"
   ##  [12] "STA" "STA" "STA" "STA" "LAN" "LAN" "LAN" "STA" "LAN" "STA" "LAN"
   ##  [23] "STA" "STA" "STA" "STA" "STA" "STA" "LAN" "LAN" "STA" "STA" "STA"
   ##  [34] "STA" "LAN" "LAN" "LAN" "LAN" "STA" "LAN" "LAN" "STA" "LAN" "LAN"
   ....

.. _2.meira:

Fleiri skipanir fyrir sameiningu gagna\ :math:`^\ast`
-----------------------------------------------------

Fleiri skipanir fyrir sameiningu gagna\ :math:`^\ast`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

cbind()
^^^^^^^

.. attention::

    **Inntak:** vigrar, gagnatöflur eða fylki
    
    **Úttak:** gagnatöflur eða fylki


--------------

rbind()
^^^^^^^

.. attention::

    **Inntak:** vigrar, gagnatöflur eða fylki
    
    **Úttak:** gagnatöflur eða fylki


--------------

Það er einnig einfalt að sameina vigra, fylki eða gagnatöflur. Til þess
notum við skipanirnar ``rbind()`` og ``cbind()``. Skipunin ``rbind()``
bætir við línu á meðan skipunin ``cbind()`` bætir við dálki.

::

   rbind(1:4, 5:8)
   ##      [,1] [,2] [,3] [,4]
   ## [1,]    1    2    3    4
   ## [2,]    5    6    7    8
   cbind(1:4, 5:8)
   ##      [,1] [,2]
   ## [1,]    1    5
   ## [2,]    2    6
   ## [3,]    3    7
   ## [4,]    4    8


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