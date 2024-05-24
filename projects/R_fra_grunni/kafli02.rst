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
um þetta er að nota gildið 1 ef samningur er ónothæfur og 0 ef samningurinn
er nothæfur í kaupskrá í breytunni ``onothaefur_samningur``. Þar sem breytan 
inniheldur eingöngu tölur er ``onothaefur_samningur`` skilgreind sem talnabreyta 
eftir innlestur í R. Áður en úrvinnsla hefst þarf að breyta talnabreytunni 
í flokkabreytu (sjá kafla :numref:`%s <s.kodun>` ). Það getur einnig gerst 
að talnabreytur séu ranglega vistaðar sem flokkabreytur og getur það t.d. 
gerst þegar einhverjar mælingar á breytunni innihalda bókstafi eða þegar ekki 
er rétt tilgreint hvernig tugabrot eru aðskilin. Þetta þarf allt að laga 
áður en úrvinnsla hefst.

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

   names(dat)
   ##  [1] "is"              "ferdatimi_skoli"  "styrikerfi_simi" "ferdamati_skoli"   
   ##  [5] "systkini_fjoldi" "dyr"              "feministi"       "staerdfraedi_gaman"
   ##  [9] "smjor_kostar"    "napoleon_faeddur" "stefnumot"       "messi_staerd"      
   ##  [13] "kosid" 

nöfnin á öllum þeim breytum sem tilheyra gagnatöflunni ``dat``.

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

   head(dat)
   ##    is          ferdatimi_skoli   styrikerfi_simi   ferdamati_skoli   
   ## 1  Jarðaberja  15                Android           Með einkabíl      
   ## 2  Vanilla     20                iOS               Með einkabíl     
   ## 3  Súkkulaði   8                 iOS               Með einkabíl     
   ## 4  Jarðaberja  12                Android           Gangandi/ skokkandi      
   ## 5  Súkkulaði   15                iOS               Með einkabíl       
   ## 6  Súkkulaði   42                Android           Með einkabíl     
   ##    systkini_fjoldi   dyr      feministi     staerdfraedi_gaman
   ## 1  1                 Hunda    Rétt          9
   ## 2  2                 Hunda    Rétt          8
   ## 3  3                 Hunda    Rangt         7
   ## 4  2                 Ketti    Rétt          3
   ## 5  2                 Hunda    Rétt          9
   ## 6  5                 Hunda    Rétt          7
   ##   smjor_kostar    napoleon_faeddur  stefnumot   messi_staerd   kosid
   ## 1  750            1750              Á kaffihús  170            Rétt
   ## 2  700            1784              Á ísrúnt    168            Rangt
   ## 3  800            1778              Á ísrúnt    170            Rangt
   ## 4  700            1870              Á ísrúnt    160            Rétt
   ## 5  1100           1779              Á kaffihús  169            Rétt
   ## 6  437            1767              Á ísrúnt    174            Rétt

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

   str(dat)
   ## 'data.frame':	201 obs. of  13 variables:
   ##  $ is                : chr [1:201] "Jarðaberja" "Vanilla" "Súkkulaði" "Jarðaberja" ...
   ## $ ferdatimi_skoli   : num [1:201] 15 20 8 12 15 42 20 7 15 25 ...
   ## $ styrikerfi_simi   : chr [1:201] "Android" "iOS" "iOS" "Android" ...
   ## $ ferdamati_skoli   : chr [1:201] "Með einkabíl" "Með einkabíl" "Með einkabíl" "Gangandi / skokkandi" ...
   ## $ systkini_fjoldi   : num [1:201] 1 2 3 2 2 5 2 3 2 2 ...
   ## $ dyr               : chr [1:201] "Hunda" "Hunda" "Hunda" "Ketti" ...
   ## $ feministi         : chr [1:201] "Rétt" "Rétt" "Rangt" "Rétt" ...
   ## $ staerdfraedi_gaman: int [1:201] 9 8 7 3 9 7 7 7 9 8 ...
   ## $ smjor_kostar      : num [1:201] 750 700 800 700 1100 437 1490 279 1400 1200 ...
   ## $ napoleon_faeddur  : num [1:201] 1750 1784 1778 1870 1779 ...
   ## $ stefnumot         : chr [1:201] "Á kaffihús" "Á ísrúnt" "Á ísrúnt" "Á ísrúnt" ...
   ## $ messi_staerd      : num [1:201] 170 168 170 160 169 174 169 179 170 170 ...
   ## $ kosid             : chr [1:201] "Rétt" "Rangt" "Rangt" "Rétt" ...

Við mælum eindregið með að nota ávalt ``str()`` skipunina til að kanna
hvort allar breytur gagnatöflunnar séu á réttu formi eftir innlestur
gagnanna.

length()
^^^^^^^^

.. attention::

    **Inntak:** nafn á vigri
    
    **Úttak:** lengd vigursins


--------------

Skipunin ``length()`` gefur okkur lengd þess vigurs (breytu) sem hún er
mötuð með, þ.e.a.s. hún segir okkur hversu margar mælingar eru geymdar í
tilteknum vigri. Í dæminu að ofan gefur skipunin

::

   length(dat$ferdatimi_skoli)
   ## [1] 201

útkomuna :math:`201`. Þ.e.a.s. það eru :math:`201` mælingar á ferðatíma í skóla
geymdar í breytunni ``ferdatimi_skoli`` í gagnatöflunni ``dat``.

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

   dat2 <-na.omit(dat)


smíðar gagnatöfluna ``dat2`` sem inniheldur aðeins einstaklinga sem
enga mælingu vantar hjá. Gætið ykkar að við viljum afar sjaldan eyða út
öllum einstaklingum í gagnatöflu sem vantar *einhverja* mælingu hjá.
Segjum sem sem dæmi að það vanti margar mælingar á breytunni ``smjor_kostar``
í gagnasafninu okkar en í raun höfum við mestan áhuga á að rannsaka
breytuna ``messi_staerd``. Með því að henda út öllum einstaklingum sem vantar
mælingar á breytunni ``smjor_kostar`` erum við búin að henda út mælingum sem
við gætum notað í rannsóknum okkar á hæð Messi.

Óraunhæfum mælingum breytt í NA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Stundum viljum við að mælingarnar okkar séu á ákveðnu bili. Þá getum við breytt 
óraunhæfu mælingunum í NA gildi. Skoðum t.d. breytuna napoleon_faeddur þar sem 
nemendur giskuðu hvenær þau héldu að Napóleon Bonaparte hafi fæðst. Viljum að 
ágiskanirnar séu á bilinu 1500-1900. Við breytum þá óraunhæfum gildum í NA með 
eftirfarandi skipun:

::

   dat$napoleon_faeddur[dat$<1500|dat$napoleon_faeddur>1900]<-NA

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
annars. Í skipuninni hér að neðan skoðum við vigurinn 
``kaupskra$onothaefur_samningur`` sem inniheldur hvort samningur sé nothæfur 
eða ekki.

::

   kaupskra$onothaefur_samningur == 0
   ##   [1] TRUE TRUE  FALSE  FALSE  TRUE  FALSE  FALSE FALSE  FALSE FALSE FALSE
   ##  [12] FALSE  TRUE TRUE  TRUE  TRUE TRUE TRUE  TRUE TRUE  TRUE  TRUE
   ##  [23] TRUE  FALSE  TRUE  TRUE FALSE  FALSE FALSE  FALSE FALSE  TRUE FALSE
   ....

Ekki gleyma því að setja gæsalappir utanum gildi breytunnar eigi það
við. Þær þurfum við alltaf að setja þegar gildið sem við viljum kanna er
kóðað með *orði* en ekki tölustaf.

Berið útkomuvigurinn saman við vigurinn

::

   dat$onothaefur_samningur
   ##  [1] 0 0 1 1 0 1 1 1 1 1 1 0
   ##  [13] 0 0 0 0 0 0 0 0 0 0 0 1
   ##  [25] 0 0 1 1 1 1 1 0 0 0 0 0
   ....

þannig sjáið þið að útkomuvigurinn inniheldur ``FALSE`` alls staðar þar
sem ``kaupskra$onothaefur_samningur`` hefur gildið ``1`` en ``TRUE`` annars.
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
t.d. búa til nýja gagnatöflu ``datT`` sem inniheldur aðeins einstaklinga
sem halda að Messi sé hærri en 170 cm gerum við það með:

::

   datT <- dat[dat$messi_staerd > 170, ]

eða
::

   datT <- filter(dat$messi_staerd > 170)

Skoðum ``filter()`` skipunina betur í `%s <s.Ákveðin gildi valin úr gagnatöflu>`
Hvað varðar neðri virkjana tvo, þá er virkinn :math:`\&` mataður með
tveimur skilyrðum og skilar ``TRUE`` eingöngu ef *bæði* skilyrðin eru
uppfyllt. Virkinn :math:`|` er sömuleiðis mataður með tveimur skilyrðum
en það nægir að eingöngu *annað* þeirra séu uppfyllt til að hann skili
``TRUE``.

Síðast en ekki síst er virkinn ``%in%`` mikið notaður. Hann má nota til
að spyrja hvort gildi mælingar sé meðal einhverra annarra gildi. T.d.
skilar skipunin:

::

   dat$systkini_fjoldi%in%c(0,3,7)
   ## [1] FALSE FALSE  TRUE FALSE FALSE FALSE FALSE  TRUE
   ## [9] FALSE FALSE  TRUE FALSE TRUE FALSE FALSE FALSE
   ## [17]  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
   ....

gildinu ``TRUE`` ef breytan ``systkini_fjoldi`` tekur eitthvert gildanna 0,
3 eða 7, en ``FALSE`` annars.

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

   dat.first<-slice(dat,1:10)

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
gagnatöflu sem inniheldur aðeins þá sem eiga engin systkini með:

::

   engin_systkini<-filter(dat, systkini_fjoldi==0)

Ef við viljum skoða gögn þeirra sem finnst jarðaberjaís bestur og kunna 
betur við hunda heldur en ketti (takið eftir að hér er ekki búin til ný gagnatafla):

::

   filter(dat, is=="Jarðaberja", dyr=="Hunda")

::

   ##    is          ferdatimi_skoli   styrikerfi_simi   ferdamati_skoli 
   ## 1  Jarðaberja  15                Android           Með einkabíl    
   ## 2  Jarðaberja  7                 Android           Gangandi/ skokkandi
   ##    systkini_fjoldi   dyr      feministi   staerdfraedi_gaman   smjor_kostar
   ## 1  1                 Hunda    Rétt        9                    750
   ## 2  3                 Hunda    Rétt        7                    279
   ##    napoleon_faeddur  stefnumot      messi_staerd   kosid
   ## 1  1750              Á kaffihús     170            Rétt
   ## 2  1551              Á ísrúnt       179            Rétt
   ....

Einnig er, eins og við sáum hér á undan, hægt að nota hornklofa
(``[ ]``) til að velja hluta af gagnatöflu. Þá mötum við hornklofann með
tveimur vigrum af vísum sem við aðgreinum með kommu. Fyrst kemur
vísavigurinn sem tilgreinir hvaða viðfangsefni (línur) við viljum velja
síðan kemur vísavigurinn sem tilgreinir hvaða breytur (dálka) við viljum
velja. Við númerum viðfangsefni frá efsta viðfangsefninu til þess neðsta
(þ.e.a.s. efsta línan er númer eitt), en breyturnar frá vinstri til
hægri (þ.e.a.s. breytan lengst til vinstri er númer eitt).

Ef við viljum skoða hver mælingin á breytu 2 (``ferdatimi_skoli``) á viðfangsefni
46 er í gagnatöflunni okkar ``dat`` gefum við skipunina:

::

   dat[46,2]
   ## [1] 20

Ef við sleppum fyrri vísavigrinum fáum við mælingar á öllum
viðfangsefnum fyrir breyturnar sem við tilgreinum í seinni vigrinum.
Þannig gefur skipunin

::

   dat[,2]

mælingarnar á ferðatíma í skóla fyrir öll viðfangsefnin. Ef við sleppum seinni
vísavigrinum fáum við mælingar á öllum breytum fyrir viðfangsefnin sem
við tilgreinum í fyrri vigrinum. Þannig gefur skipunin

::

   dat[c(46,52),]
   ##     is         ferdatimi_skoli   styrikerfi_simi   ferdamati_skoli   
   ## 46  Vanilla    20                iOS               Með einkabíl      
   ## 52  Vanilla    13                iOS               Með einkabíl      
   ##     systkini_fjoldi   dyr      feministi     staerdfraedi_gaman
   ## 46  7                 Ketti    Rétt          7
   ## 52  3                 Hunda    Rétt          9
   ##     smjor_kostar    napoleon_faeddur  stefnumot       messi_staerd   kosid
   ## 46  549             1769              Í bíó           171            Rangt
   ## 52  359             1120              Í fjallgöngu    171            Rétt

allar mælingar fyrir viðfangsefni númer 46 og 52.

Að lokum getum við notað mínus til að skoða mælingar í gagnatöflu fyrir
öll viðfangsefni *nema* einhver tiltekin, eða allar breytur *nema*
einhverjar tilteknar.

::

   dat[-c(46,52), -2]

gefur mælingar fyrir öll viðfangsefni *nema* númer 46 og 52 og allar
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
getum t.d. kannað hvaða einstaklingar halda að Messi sé hærri en 180 cm í dat
gögnunum okkar:

::

   which(dat$messi_staerd>180)
   ##  [1]   29   64    77    130    136     142   168   195    

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
Eftirfarandi skipun finnur til dæmis vísi allra þeirra ferdamati_skoli sem
innihalda textastrenginn ``skokkandi``.

::

   grep("skokkandi", dat$ferdamati_skoli)
   ## [1]  4   8   12  13  24  25  57  59  67
   ## [10] 77  93  96  97  100 117 119 122 130
   ## [19] 131 132 133 136 139 142 147 148 158
   ## [28] 160 162 168 169 184 188 196 
   ....

Ef við gefum stillinguna ``value=TRUE`` fáum við mælingarnar sem pössuðu
við leitarskilyrðið en ekki bara vísa þeirra:

::

   grep("skokkandi", dat$ferdamati_skoli, value=TRUE)
   ##   [1] "Gangandi / skokkandi" "Gangandi / skokkandi" "Gangandi / skokkandi" 
   ##   [4] "Gangandi / skokkandi" "Gangandi / skokkandi" "Gangandi / skokkandi"
   ##   [7] "Gangandi / skokkandi" "Gangandi / skokkandi" "Gangandi / skokkandi"
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
``onothaefur_samningur`` í gagnatöflunni ``kaupskra``. Við notum skipunina 
``factor()`` til að gefa R til kynna að breyta sé flokkabreyta. Ef við viljum leiðrétta
hvernig breytan ``onothaefur_samningur`` er vistuð í gagnatöflunni sjálfri notum við
skipunina:

::

   kaupskra$onothaefur_samningur <- factor(kaupskra$onothaefur_samningur)

Takið eftir því að hér að ofan yfirskrifum við gömlu talnabreytuna
``onothaefur_samningur`` með nýju flokkabreytunni (þær bera sama nafn). 
Í þessu tilviki er það einmitt það sem við viljum gera. Það gæti þó komið 
fyrir að við viljum halda í gömlu talnabreytuna en þá þurfum við að búa 
til nýja breytu í stað þess að skrifa yfir þá gömlu. Til að gera það þurfum við
að gæta að nota annað nafn en á upphaflegu talnabreytunni. Með
eftirfarandi skipun búum við til nýja breytu ``onothaefur_samningur2`` 
í gagnatöflunni ``kaupskra``.

::

   kaupskra$onothaefur_samningur2 <- factor(kaupskra$onothaefur_samningur)

Hefðum við aðeins keyrt seinni ``factor()`` skipunina ættum við til
talnabreytuna ``onothaefur_samningur`` í gagnatöflunni ásamt flokkabreytunni 
``onothaefur_samningur2``.

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
``onothaefur_samningur`` er ágætt að byrja á að keyra skipunina

::

   levels(kaupskra$onothaefur_samningur)
   ## [1] "0" "1"

því hún skilar okkur núverandi nöfnum. Viljum við breyta nöfnunum á
flokkunum í ``Nothæfur samningur`` og ``Ónothæfur samningur`` gerum 
við það með:

::

   levels(kaupskra$onothaefur_samningur)<-c("Nothæfur samningur","Ónothæfur samningur")

Hér þarf að passa að röðunin sé rétt miðað við gömlu heitin, annars
breytum við öllum nothæfu samningunum í ónothæfa og öfugt.

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

Búum nú til flokkabreytu úr talnabreytunni ``systkini_fjoldi``. Við ætlum
að skipta viðfangsefnunum upp í þrjá flokka, þau sem eiga engin systkini,
þau sem eiga nokkur systkini (1-2) og þau sem eiga mörg systkini (:math:`>` 3 ). 
Gætið þess að skýra nýju breytuna eitthvað annað en ``systkini_fjoldi`` svo við 
yfirskrifum ekki talnabreytuna heldur búum þess í stað til nýja breytu. Við mötum
aðferðina með nafninu á talnabreytunni ``systkini_fjoldi`` og mörkunum á
flokkunum. Ætlum við að tilgreina vinstri mörkin á flokkunum okkar
(lægri mörkin) notum við ``right=F`` stillinguna. Við mötum því
aðferðina með 0,1,3 (neðri mörkin á flokkunum okkar) en þurfum svo að
gefa efra mark á síðasta flokknum. Þetta þarf að vera gildi sem er
a.m.k. einu gildi hærra en hæsta gildið sem talnabreytan tekur. Hér
notum við gildið 15 (fallegra væri að nota
``max(dat$systkini_fjoldi)+1``):

::

   dat$systkini_fjoldi_stig<-cut(dat$systkini_fjoldi,c(0,1,3,15),right=F)

Hér sjáum við hversu margir verða í hverjum flokki:

::

   table(dat$systkini_fjoldi_stig)
   ##
   ##   [0,1)   [1,3) [3,15)
   ##      3     123     75

Við getum svo notað ``levels()`` skipunina til að endurskýra flokkana:

::

   levels(dat$systkini_fjoldi_stig)<-c("Engin","Nokkur","Mörg")
   table(dat$systkini_fjoldi_stig)
   ##
   ##    Engin    Nokkur   Mörg
   ##    3        123      75

C: Flokkar sameinaðir
~~~~~~~~~~~~~~~~~~~~~

Afar oft viljum við sameina tvo eða fleiri flokka flokkabreytu. Í R
framkvæmum við það með því að gefa tveimur eða fleiri flokkum sama
heitið með skipuninni ``levels()``. Segjum að við viljum
sérstaklega kanna mun á þeim nemendum sem koma í skólann með ökutæki í
samanburði við alla aðra nemendur. Þá væri sniðugt að hafa nýja breytu
``ferdamati_skoli_okutaeki`` sem tekur bara tvö gildi: ``med_okutaeki`` 
og ``ekki_med_okutaeki``.

Þegar við búum til breytuna ætlum við að sameina flokkana ``Með einkabíl`` og
``Með strætó`` undir nafninu ``med_okutaeki`` og sameinum flokkana 
``Á hjóli/ rafhlaupahjóli``, ``Gangandi/ skokkandi`` og ``Á annan hátt``. 
Búum fyrst til afrit af breytunni og sjáum í hvaða röð flokkarnir eru taldir upp:

::

   dat$ferdamati_skoli_okutaeki <- dat$ferdatimi_skoli
   levels(dat$ferdamati_skoli_okutaeki)
   ## [1] "Á annan hátt"  "Á hjóli/ rafhlaupahjóli"  "Gangandi/ skokkandi"
   ## [4] "Með einkabíl"  "Með strætó"

Flokkarnir sem við ætlum að sameina eru fyrstu þrír flokkarnir sem eru
taldir upp. Því skrifum við ``ekki_med_okutaeki`` í fyrstu þrjú sætin en
``með_okutakei`` í síðustu tv- sætin.

::

   levels(dat$ferdamati_skoli_okutaeki) <- 
   c('ekki_med_okutaeki','ekki_med_okutaeki','ekki_med_okutaeki', 'med_okutaeki', 'med_okutaeki')

Nýja sameinaða breytan hefur eingöngu tvo flokka:

::

   str(dat$ferdamati_skoli_okutaeki)
   ##  Factor w/ 2 levels "ekki_med_okutaeki","med_okutaeki
   ": 2 2 2 1 2 2 1 2 2 1 ...


Einnig má gera þetta með að nota ``fct_recode()`` skipunina úr forcats pakkanum.
Hana má nota svona:

byrjum að sækja forcats pakkann

::
   library(forcats)

Búum fyrst til nýjan flokk sem er afrit að ferdamati_skoli

::

   dat$ferdamati_skoli_okutaeki <- dat$ferdatimi_skoli

Búum svo til nýju flokkana

::
   dat$ferdamati_skoli_okutaeki<- fct_recode(dat$ferdamati_skoli_okutaeki, 
   "ekki_med_okutaeki" = "Á hjóli / rafhlaupahjóli","ekki_med_okutaeki"  
   = "Gangandi / skokkandi", "ekki_med_okutaeki" = "Á annan hátt", 
   "med_okutaeki" = "Með einkabíl", "med_okutaeki" = "Með strætó")

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

Getum líka notað ``str_detect()`` skipunina úr stringr pakkanum til að búa til breytur.
Þá er hægt t.d. að búa til nýja breytu ``Laugarvegur`` sem geymir TRUE ef eignin er 
á Laugarveginum.

::
   kaupskra$Laugarvegur<-str_detect(kaupskra$heimilisfang, "Laugarvegur") 

Skoðum hvaða eignir eru á Laugarveginum

::
   which(kaupskra$Laugarvegur==TRUE)
   ## [1]  75723  75724  75725  75726  75727  75728  75729  75730
   ## [9]  75731  75732  75733  75734  75735  75736  75737  75903
   ## [17] 75904  75905  75906  75907  75908  75909  75910  75911

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
``is`` í ``uppahalds_is`` gerum við það með:

::

   dat<-rename(dat,uppahalds_is=is)

Til að valda ekki ruglingi hér breytum við nafninu aftur í ``is``
með:

::

   dat<-rename(dat,is=uppahalds_is)

G: Vörpunum beitt á talnabreytur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Að lokum viljum við oft búa til nýjar, afleiddar breytur út frá öðrum
flokkabreytum. Þannig getum við t.d. búið til breytuna fermetraverð út 
frá kaupverði og einingarflatarmál eignar:

::

   kaupskra$fermetraverd <- kaupskra$kaupverd*1000/kaupskra$einflm

Athugið að hér þarf að margfalda kaupverð með 1000, þar sem í kaupskra 
er kaupverd ekki gefið í milljónum.

Hér má einnig nota ``mutate()`` fallið sem er oft þægilegra.
::
   kaupskra <- mutate(kaupskra, fermetraverd=kaupverd*1000/einflm)


.. _s.umrodun:

Umröðun gagna
-------------

Umröðun gagna
~~~~~~~~~~~~~

Ef gagnatöflurnar sem verið er að vinna með innihalda margar breytur
getur verið gott að geta valið þær breytur sem við ætlum að vinna með á
auðveldan hátt. Við getum t.d. búið til nýja gagnatöflu sem inniheldur
aðeins breyturnar ``keupverd`` og ``einflm`` (takið eftir að nýja
gagnataflan er ekki geymd í nýjum hlut hér, ætlum við að nota hana
þurfum við að búa til nýja töflu eins og hér að neðan).

::

   select(kaupskra,einflm,kaupverd)
   ##     einflm  kaupverd
   ## 1   780.4   87000
   ## 2   400.0   36000
   ## 3   310.2   31000
   ## 4   310.2   31000
   ## 5   71.4    23500
   ## 6   325.0   33500
   ## 7   310.2   31000
   ## 8   310.2   31000
   ## 9   307.2   37000
   ....

Getum búið til nýtt gagnasett sem inniheldur einungis breyturnar 
kaupverd og einflm með:

::
   kaupskra2 <-select(kaupskra, einflm, kaupverd)


Við getum einnig notað ``select()`` aðferðina til að búa til nýja
gagnatöflu sem inniheldur alla dálka upphaflegu töflunnar að
undanskildum nokkrum. Viljum við t.d. búa til nýja gagnatöflu sem
inniheldur allar breytur upphaflegu töflunnar nema ``postnr`` og
``sveitarfelag`` gerum við það með:

::

   kaupskra3<-select(kaupskra,-c(postnr,sveitarfelag))

group_by()
^^^^^^^^^^

.. attention::

    **Inntak:** nafn á gagnatöflu og nafn á flokkabreytum
    
    **Úttak:** ???
    
    **Helstu stillingar:** .drop1


--------------

Group_by() skipunin leyfir okkur að skipta  gagnasafninu upp eftir einni eða fleiri
ákveðinni breytu. Síðan má reikna allskyns lýsistærðir fyrir hvern og einn hóp. 

Skoðum með meðalferðtími fólks er í skóla eftir ferðamáta

::

   hopar <- group_by(dat, ferdamati_skoli)
   summarise(hopar, mean(ferdatimi_skoli))
   ## ferdamati_skoli            mean(ferdatimi_skoli) 
   ## Gangandi / skokkandi	      7.588235
   ## Með einkabíl	            19.923077
   ## Með strætó	               33.733333
   ## Á annan hátt	            2.500000
   ## Á hjóli / rafhlaupahjóli   11.666667


Skoðum svo hver lengst ferðatími í skóla eftir bæði ferðamáta 
og uppáhaldsís.

::

   hopar2 <- group_by(dat, ferdamati_skoli, is)
   summarise(hopar, max(ferdatimi_skoli))
   ## ferdamati_skoli         is             max(ferdamati_skoli)
   ## Gangandi / skokkandi	   Jarðaberja	   30
   ## Gangandi / skokkandi	   Súkkulaði	   25
   ## Gangandi / skokkandi	   Vanilla	      11
   ## Með einkabíl	         Jarðaberja	   45
   ## Með einkabíl	         Súkkulaði	   50
   ## Með einkabíl	         Vanilla	      60
   ## Með strætó	            Jarðaberja	   70
   ## Með strætó	            Súkkulaði	   45
   ## Með strætó	            Vanilla	      75
   ## Á annan hátt	         Jarðaberja     0

sort()
^^^^^^

.. attention::

    **Inntak:** nafn á vigri
    
    **Úttak:** vigur með röðuðum gildum
    
    **Helstu stillingar:** decreasing


--------------

Oft getur verið þægilegt að raða mælingunum okkar eftir stærðarröð.
Viljum við raða gildunum á einni breytu/vigri í stærðarröð gerum við það
með ``sort()`` aðferðinni. Viljum við t.d. skoða mælingarnar á kaupverði í
stærðarröð gerum við það með:

::

   sort(kaupskra$kaupverd)
   ##   [1]    1    1    1    1    1   1    1    1    1    1
   ##   [11]   1    1    1    1    1   1    1    1    1    2
   ##   [21]   10   19   20   30   30  30   40   50   50   50
   ##   [31]   50   60   66   66  100  100  100  100  100  100
   ##   [41]  100  100  100  100  100  100  100  100  130  150
   ##   [51]  150  150  164  164  167  170  194  200  200  200
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
viðfangsefnunum í kaupskra gagnasafninu eftir kaupverði gerum við það með:

::

   arrange(kaupskra,kaupverd)
   ##     kaupverd   utgdag      postnr   sveitarfelag      byggar   tegund 
   ## 1   1          2006-09-05	580      Fjallabyggð       1937     Atvinnuhusnaedi
   ## 2   1          2018-06-08  760      Fjallabyggð       1973     Atvinnuhusnaedi
   ## 3   1          2015-10-13  750      Fjallabyggð       NA       Serbyli
   ## 4   1          2006-09-05  580      Fjallabyggð       1947     Atvinnuhusnaedi
   ## 5   1          2015-10-13	750      Fjallabyggð       NA       Serbyli
   ## 6   1          2015-10-13  750      Fjallabyggð       NA       Serbyli
   ## 7   1          2015-10-13  750      Fjallabyggð       NA       Serbyli
   ## 8   1          2008-12-22  104      Reykjarvíkurborg  1967     Fjolbyli
   ## 9   1          2016-06-02  640      Norðurþing        1995     Fjolbyli
   ....

Viljum við hins vegar raða fyrst eftir dagsetning undirskriftar kaupsamnings og svo eftir 
kaupverði gerum við það með:

::

   arrange(kaupskra,utgdag,kaupverd)
   ##     kaupverd   utgdag      postnr   sveitarfelag      byggar    tegund 
   ## 1   14800      2006-01-20	810      Hveragerðisbær    1930      Serbyli
   ## 2   17411      2006-01-31  103      Reykjarvíkurborg  2007      Fjolbyli
   ## 3   396000     2006-02-02  700      Múlaþing          1977      Atvinnuhusnaedi
   ## 4   396000     2006-02-02  700      Múlaþing          1977      Atvinnuhusnaedi
   ## 5   396000     2006-02-02	700      Múlaþing          1977      Atvinnuhusnaedi
   ## 6   396000     2006-02-02  700      Múlaþing          1966      Atvinnuhusnaedi
   ## 7   396000     2006-02-02  700      Múlaþing          1966      Atvinnuhusnaedi
   ## 8   396000     2006-02-02  700      Múlaþing          1924      Atvinnuhusnaedi
   ## 9   4000       2006-02-11  425      Ísafjarðarbær     1958      Serbyli
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
tilgreinir í hvaða sveitarfélago og hvaða póstnúmer ein er í.

::

   kaupskra$sveitarf_post <- paste(kaupskra$sveitarfelag, kaupskra$postnr)
   str(kaupskra$sveitarf_post)
   ##  chr [1:169636] "Kópavogsbær 200" "Hafnarfjarðarkaupstaður 220" 
   ##  "Reykjavíkurborg 104" ...

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

   sprintf('Dagurinn í dag er %s', Sys.Date())
   ## [1] "Dagurinn í dag er 2024-16-05"

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

   kaupskra_nytt <- separate(kaupskra, utgdag, into=c('ar','manudur','dagur'), sep='-')

Hér má sjá nýju gagnatöfluna, með þremur nýjum breytum:

::

   head(kaupskra_nytt)
   ##     kaupverd  ar    manudur   dagur    postnr   sveitarfelag    
   ## 1   87000     2012  07        30	      200      Kópavogsbær       
   ## 2   36000     2011  02        28       220      Hafnarfjarðarkaupstaður  
   ## 3   31000     2012  04        16       104      Reykjarvíkurborg        
   ## 4   31000     2012  04        16       104      Reykjarvíkurborg         
   ## 5   23500     2018  02        20	      104      Reykjarvíkurborg          
   ## 6   33500     2013  10        25       104      Reykjarvíkurborg          
   ...

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

   substr(kaupskra$tegund, 1,3)
   ##   [1] "Atv" "Atv" "Atv" "Atv" "Atv" "Atv" "Atv" "Atv" "Atv" "Fjo" 
   ##   [11] "Atv" "Atv" "Fjo" "Fjo" "Fjo" "Fjo" "Atv" "Atv" "Fjo" "Fjo" 
   ##   [21] "Fjo" "Fjo" "Atv" "Fjo" "Fjo" "Atv" "Atv" "Atv" "Atv" "Atv"
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
    puls <- read.table ("https://raw.githubusercontent.com/edbook/haskoli-islands/main/pulsAll.csv", header=TRUE, sep=";")

    # Setjid ykkar eigin koda her fyrir nedan:
    # Sem daemi, skipunin head(puls) skilar fyrstu nokkrar radirnar i gognunum
    # asamt dalkarheitum.
    head(puls)