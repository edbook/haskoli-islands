.. _ch.TruthTables:

Sanntöflur
==========

.. _`s:CharacteristicTruthTables`:

Skilgreiningarsanntöflur
------------------------

Í síðasta kafla skilgreindum við nákvæmlega hvað telst vera setning í
setningrökfræði og hvað ekki. Við skilgreindum fyrst nákvæmlega hvaða
tákn eru leyfileg, hástafir fyrir grunnsetningar, svigar og fimm
setningatengi. Svo sögðum við að ekkert væri setning í setningarökfræði
nema það væri smíðað úr grunnsetningunum eftir ákveðnum myndunarreglum,
eina fyrir hvert setningatengi. Til dæmis er setningin :math:`D \eand E`
samsett úr :math:`D` og :math:`E` samkvæmt myndunarreglunni fyrir
„\ :math:`\eand`\ “ (með það í huga að við sleppum ystu svigunum, eftir
venju).

Markmið okkar er að greina rökfærslur með því að þýða þær yfir á táknmál
setningarökfræði og næsta skrefið á þeirri leið er að fá nákvæmari
útlistun á þessum tengjum. Við munum gera það með því að skilgreina
nákvæmlega hvenær setningarnar sem þau mynda eru sannar og hvenær
ósannar. Hugmyndin sem við munum útfæra er að sanngildi flókinnar
setningar ákvarðist af sanngildi þeirra hluta sem hún er mynduð úr. Til
dæmis, þá er setningin „Anna og Jón eru snjöll“ sönn ef og aðeins ef
setningin „Anna er snjöll“ er sönn og setningin „Jón er snjall“ er sönn.

Það sem við þurfum þá að gera er að vinna úr þessari hugmynd fyrir hvert
setningatengjanna fimm og búa til reglur sem ákvarða hvenær setningar
sem þau koma fyrir í eru sannar. Við gerum þetta með því sem kallað er .
Þær heita svo af því að þær *skilgreina* undir hvaða kringumstæðum
setning er sönn sem mynduð er úr tilteknu setningatengi. Við að fylla út
skilgreiningarsanntöflurnar er gott að stytta sér leið og því munum við
skrifa „S“ fyrir „Satt“ og „Ó“ fyrir „Ósatt“.

Það er mikilvægt að hafa í huga að hingað til höfum við kynnst
setningatengjunum með því að notast við þekkingu okkar á mæltu máli en
að markmiðið núna er að skilgreina *nákvæmlega* hver merking
setningatengjanna er. Skilgreiningasanntöflurnar *eru* þessar
skilgreiningar.

Neitun.
       

Ef setningin „Anna er snjöll“ er sönn, hvað getum við þá sagt um neitun
hennar, setninguna „Anna er ekki snjöll“? Jú, að hún er ósönn. Það sama
gildir í hina áttina: ef setningin er ósönn, þá er neitun hennar sönn.
Almennt gildir, fyrir hvaða setningu :math:`\meta{A}` sem er, að ef
:math:`\meta{A}` er sönn, þá er :math:`\enot \meta{A}` ósönn, og ef
:math:`\enot \meta{A}` sönn, þá er :math:`\meta{A}` ósönn. Við getum
sett þetta upp í töflu, sem við getum kallað *skilgreiningarsanntöflu*
fyrir neitun:

.. container:: center

   ================ =====================
   :math:`\meta{A}` :math:`\enot\meta{A}`
   ================ =====================
   S                Ó
   Ó                S
   ================ =====================

Við lesum úr þessari töflu þannig: vinstra megin undir :math:`\meta{A}`
eru möguleg sanngildi, satt og ósatt. Þar við hliðina á, eitt í hverri
línu, eru þau sanngildi sem :math:`\enot \meta{A}` hefur, að því gefnu
hvaða sanngildi :math:`\meta{A}` hefur. Við getum því lesið út úr
töflunni hvaða sanngildi :math:`\enot \meta{A}` hefur, ef við vitum
hvaða sanngildi :math:`\meta{A}` og hvaða sanngildi :math:`\meta{A}`
hefur, ef við vitum hvaða sanngildi :math:`\enot \meta{A}` hefur.

Og-tengi.
         

Eins og við sögðum hér að ofan, þá er setningin „Anna og Jón eru snjöll“
sönn ef og aðeins ef setningarnar „Anna er snjöll“ og „Jón er snjall“
eru báðar sannar. Það þýðir að ef önnur þeirra er ósönn, þá er öll
setningin líka ósönn. Þetta gildir almennt fyrir hvaða setningapar
:math:`\meta{A}` og :math:`\meta{B}` sem er:
:math:`\meta{A} \eand \meta{B}` er sönn ef og aðeins ef :math:`\meta{A}`
og :math:`\meta{B}` eru báðar sannar. Skilgreiningarsanntaflan fyrir
„\ :math:`\eand`\ “ lítur því svona út:

.. container:: center

   ================ ================ =============================
   :math:`\meta{A}` :math:`\meta{B}` :math:`\meta{A}\eand\meta{B}`
   ================ ================ =============================
   S                S                S
   S                Ó                Ó
   Ó                S                Ó
   Ó                Ó                Ó
   ================ ================ =============================

Við lesum úr þessari töflu á sama hátt. Fyrst höfum við öll möguleg
sanngildi fyrir setningarnar tvær: :math:`\meta{A}` og :math:`\meta{B}`
geta báðar verið sannar, það samsvarar efstu línunni, önnur þeirra getur
verið sönn og hin ósönn, það samsvarar annarri og þriðju línu, og svo
geta báðar verið ósannar. Það samsvarar neðstu línunni, línu fjögur.
Næst sjáum við svo hvert sanngildi allrar setningarinnar,
þ.e. :math:`\meta{A} \eand \meta{B}`, er fyrir hvern þessara möguleika.
Við sjáum að :math:`\meta{A} \eand \meta{B}` er einungis sönn ef báðir
liðir eru sannir, annars ósönn.

Takið eftir því að samtenging er *samhverf*. Sanngildi setningarinnar
:math:`\meta{A} \eand \meta{B}` er alltaf það sama og sanngildi
setningarinnar :math:`\meta{B} \eand \meta{A}`.

Eða-tengi.
          

Munum að táknið „\ :math:`\eor`\ “ stendur alltaf fyrir skarað eða. Það
þýðir að fyrir hvaða setningar sem er, :math:`\meta{A}` og
:math:`\meta{B}`, setningin :math:`\meta{A} \eor \meta{B}` er sönn ef og
aðeins ef að minnsta kosti *önnur* setninganna :math:`\meta{A}` eða
:math:`\meta{B}` er sönn. :math:`\meta{A} \eor \meta{B}` er því bara
ósönn ef báðar setningarnar eru ósannar. Skilgreiningarsanntaflan fyrir
„\ :math:`\eor`\ “ er því svona:

.. container:: center

   ================ ================ ============================
   :math:`\meta{A}` :math:`\meta{B}` :math:`\meta{A}\eor\meta{B}`
   ================ ================ ============================
   S                S                S
   S                Ó                S
   Ó                S                S
   Ó                Ó                Ó
   ================ ================ ============================

Setningar sem hafa „\ :math:`\eor`\ “ sem aðaltengi eru líka samhverfar.
:math:`\meta{A} \eor \meta{B}` er sönn ef og aðeins ef
:math:`\meta{B} \eor \meta{A}` er sönn. Rétt eins og við köllum
setningar sem er búnar til með „\ :math:`\eand`\ “ *samtengingar*, þá
köllum við setningar sem eru búnar til með „\ :math:`\eor`\ “ stundum
*mistengingar*. Þær eru líka stundum kallaðar „eðanir“ á íslensku—en við
munum forðast það orðalag.

Skilyrðistengi.
               

Næsta skilgreiningarsanntafla er sú fyrir skilyrðistengið. Hún er þannig
að :math:`\meta{A} \eif \meta{B}` er *ósönn* ef og aðeins ef
:math:`\meta{A}` er sönn og :math:`\meta{B}` er ósönn. Það er að segja,
við setjum S í hverja línu í sanntöflunni, nema þar sem :math:`\meta{A}`
er sönn og :math:`\meta{B}` ósönn:

.. container:: center

   ================ ================ ============================
   :math:`\meta{A}` :math:`\meta{B}` :math:`\meta{A}\eif\meta{B}`
   ================ ================ ============================
   S                S                S
   S                Ó                Ó
   Ó                S                S
   Ó                Ó                S
   ================ ================ ============================

Þessi sanntafla hefur ýmsar skrýtnar afleiðingar. Við sjáum til dæmis að
skilyrðissetning er *alltaf* sönn ef forliðurinn er ósannur. Það þýðir
að frá sjónarhóli setningarökfræðinnar er skilyrðissetningin „Ef
:math:`2+2=5`, þá er ég hundrað metra hár“ sönn. Það er virðist ósatt,
því bakliðurinn hefur ekkert forliðinn að gera. Þessi setning samsvarar
línu þrjú í töflunni og við gætum auðveldlega búið til álíka furðulegt
dæmi fyrir línu fjögur.

En af hverju er sanntaflan svona? Það hefur að gera með *takmarkanir*
setningarökfræðinnar. Sú setningarökfræði sem þessi bók fjallar um er
svokölluð *klassísk* setningarökfræði. Það þýðir meðal annars að við
gerum ráð fyrir því að hver setning hafi eitt af tveimur sanngildum,
satt eða ósatt. Hver einasta setning er því annað hvort sönn eða ósönn
og allar setningar verða að hafa eitt af þessum tveimur sanngildum. Við
viljum líka að sanngildi setninga ráðist fullkomlega af sanngildum
þeirra setninga sem hún er smíðuð úr. Það væri hægt að reyna að slaka á
þessum kröfum—og hefur verið gert, en staðreyndin er sú að þær tillögur
hafa líka alvarlega galla, auk þess að vera mun flóknari. Einhvers
staðar verður maður líka að byrja og til þess að geta tekið afstöðu í
þessum heimspekilegu deilumálum er nauðsynlegt að kunna góð skil á
klassískri setningarökfræði fyrst. Í köflum
§\ `2.3 <#s:IndicativeSubjunctive>`__ og
§\ `4.5 <#s:ParadoxesOfMaterialConditional>`__ munum við ræða sum af
þeim álitamálum sem styrr stendur um.

Ef við fyllum svo sanntöfluna út línu fyrir línu, þá sjáum við af hverju
hún hlýtur að vera svona. Látum :math:`\meta{A} \eif \meta{B}` standa
fyrir setninguna „Ef þessi fugl er hrafn, þá er hann svartur“. Ef
bakliðurinn og forliðurinn eru báðir sannir, þ.e. ef fuglinn er hrafn og
hann er svartur, þá er setningin ljóslega sönn—að minnsta kosti væri
skrýtið að segja að hún sé þar með *ósönn*.

Lína tvö virðist líka í lagi. Ef bakliðurinn er ósannur, þ.e. ef þessi
fugl er *ekki* svartur, þá virðist eðlilegt að segja að
skilyrðissetningin sé þar með afsönnuð, og því ósönn. Við getum líka
litið á skilyrðissetninguna sem *loforð*. Ef ég segði við þig: „Ef þú
stendur þig vel í rökfræði, þá býð ég þér í bíó“ og þú stæðir þig svo
vel, þá væri eðlilegt að segja að ég hafi *svikið* loforðið ef ég byði
þér svo *ekki* í bíó. Það væri á sama hátt eðlilegt að segja að ég hafi
*staðið* við það, ef ég myndi bjóða þér í bíó. Það samsvarar línu eitt.

Hvað með línur þrjú og fjögur? Skoðum fyrst línu fjögur. Hér eru bæði
forliðurinn og bakliðurinn ósannir. Það samsvarar því að fuglinn sé
hvorki hrafn né svartur. Kannski er hann hvítur svanur. Nú höfum við tvo
möguleika. Ef við segjum að setningin sé ósönn, þá hefði það í för með
sér að tilvist hvítra svana *afsanni* þá skilyrðissetningu að ef fuglinn
sé hrafn, þá sé hann svartur. Það væri verra en sá valkostur að segja
einfaldlega að setningin sé sönn, og við verðum að gera annað hvort.
Þetta passar líka ágætlega við hugmyndina um skilyrðissetningar sem
loforð: ef þú stendur þig illa, þá væri ég augljóslega ekki að brjóta
loforðið um að bjóða þér í bíó *ef þú stendur þig vel*, ef ég byði þér
*ekki* í bíó.

Lína þrjú er svipuð. Ef fuglinn er svartur og ekki hrafn, þá virðumst
við líka nauðbeygð til að segja að setningin sé sönn. Ef við segðum að
hún væri ósönn, þá myndi tilvist svartra fugla annarra en hrafna afsanna
skilyrðissetninguna að ef hann sé hrafn, þá sé hann svartur. En af
hverju ætti það að fuglinn sé kráka að sýna að það sé ósatt að ef hann
er hrafn, þá sé hann svartur? Það virðist mun verri kostur en að segja
bara að setningin sé sönn. Sama gildir ef við lítum á
skilyrðissetninguna sem loforð. Ef ég lofa að bjóða þér í bíó ef þú
stendur þig vel, þá væri skrýtið að segja að ég hafi *svikið* loforðið
ef ég býð þér samt. Það eina sem loforðið segir er að *ef* þú stendur
þig vel, *þá* býð ég þér í bíó. Það segir ekkert um hvað gerist ef þú
stendur þig illa.

Það er líklega auðveldast að leggja þessa sanntöflu á minnið ef maður
lítur á skilyrðissetningar sem loforð: þær eru bara ósannar ef það sem
þær „lofa“ rættist ekki. Við myndum einmitt segja að ef ég lofa því að
bjóða þér í bíó ef þú stendur þig vel, og geri það svo ekki, þá hafi ég
svikið loforðið, annars ekki. Það er þá eina línan þar sem
skilyrðissetningin er ósönn, hinar eru allar sannar. Að hugsa um
skilyrðistengið svona sýnir líka að þessi skilgreiningarsanntafla er
kannski ekki alveg jafn slæm og maður myndi annars halda.

Skilyrðissetningar eru *ekki samhverfar*. Það er ekki hægt að víxla
forlið og baklið án þess að breyta þar með merkingu setningarinnar.
:math:`\meta{A} \eif \meta{B}` og :math:`\meta{B} \eif \meta{A}` hafa
ólíkar sanntöflur, enda merkir setningin „ef þú stendur þig vel, þá býð
ég þér í bíó“ ekki það sama og setningin „ef ég býð þér í bíó, þá
stendur þú þig vel“.

Jafngildistengi.
                

Jafngildissetningar eru í raun samtenging skilyrðissetninga sem ganga í
báðar áttir:
:math:`(\meta{A} \eif \meta{B}) \eand (\meta{B} \eif \meta{A})`. Þær eru
þá sannar ef og aðeins ef báðar setningarnar eru sannar, það er að
segja, sannar ef báðar setningarnar eru sannar og ósannar ef báðar
setningarnar eru ósannar. Jafngildistengi er því satt þegar báðar
setningarnar hafa sama sanngildi, en annars ósannar.
Skilgreiningarsanntaflan fyrir jafngildistengið er því svona:

.. container:: center

   ================ ================ =============================
   :math:`\meta{A}` :math:`\meta{B}` :math:`\meta{A}\eiff\meta{B}`
   ================ ================ =============================
   S                S                S
   S                Ó                Ó
   Ó                S                Ó
   Ó                Ó                S
   ================ ================ =============================

Eins og við sjáum, þá er jafngildistengið samhverft:
:math:`\meta{A} \eiff \meta{B}` er það sama og
:math:`\meta{B}  \eiff \meta{A}`.

.. _`s:TruthFunctionality`:

Sannföll
--------

Hvað eru sannföll?
~~~~~~~~~~~~~~~~~~

Eftirfarandi er mikilvæg hugmynd í rökfræði: Öll setningatengin í
setningarökfræði eru sannföll. Sanngildi neitunar er ákvarðað
fullkomlega af sanngildi þeirrar setningar sem neitað er. Við þurfum
ekki að vita neitt annað til að vita sanngildið. Það sama gildir um hin
setningatengin. Sanngildi samtengingar er fullkomlega ákvarðað af
sanngildi setninganna sem það tengir og sanngildi mistengis
(þ.e. setningar sem hefur „\ :math:`\eor`\ “ sem aðaltengi) er
fullkomlega ákvarðað af sanngildi setninganna sem það tengir, o.s.frv.
Til þess að vita sanngildi setningar í setningarökfræði er nóg að vita
sanngildi setninganna sem hún er smíðuð úr.

Almennt er þetta ekki svona í mæltu máli. Til dæmis getum við búið til
nýja setningu á íslensku úr öðrum setningum með því að setja „Það er
nauðsynlega satt að…“ fyrir framan þær. Sanngildi slíkrar setningar er
*ekki* fullkomlega ákvarðað af sanngildi setningarinnar sem hún var búin
til úr. Skoðum tvö dæmi:

.. container:: earg

   :math:`2 + 2 = 4`

   Halldór Laxness skrifaði fjórtán skáldsögur.

Þessar setningar eru báðar sannar, en þó að það sé nauðsynlega satt að
:math:`2 + 2 = 4`, þá er það *ekki* nauðsynlega satt að Halldór Laxness
hafi skrifað fjórtán skáldsögur. Það hefði til dæmis vel getað gerst að
seinni heimsstyrjöldin hefði komið í veg fyrir að hann lyki við
Íslandsklukkuna, og þá hefði hann bara skrifað þrettán skáldsögur. Það
er því ekki nóg að vita bara sanngildi setningarinnar sem „Það er
nauðsynlega satt að…“ er skeytt við til að vita sanngildi
setningarninnar sem verður til við slíka skeytingu. „Það er nauðsynlega
satt að…“ er því ekki sannfall.

Þýðingar yfir á táknmál setningarökfræði
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Öll setningatengi setningarökfræðinnar eru sannföll. En í raun eru þau
heldur ekkert meira en það: þau segja okkur bara hvert er sanngildi
setningar ef við vitum sanngildi annarra setninga eða setningar,
nefnilega hlutasetninganna sem setningin samanstendur af.

Þegar við þýðum setningu yfir á táknmál setningarökfræði þá einblínum
við á sanngildi hlutasetninganna sem mynda setninguna og *hunsum* allt
annað. En í mæltu máli er margt annað hluti af merkingu setningarinnar,
til dæmis kaldhæðni, ljóðrænn blær, áhersla, eða að eitthvað sé gefið í
skyn. Þetta eru allt mikilvægir hlutir við hversdagslega notkun
tungumálsins. En setningarökfræðin er algjörlega blind á slík litbrigði
málsins og allt nema sanngildið glatast við slíka þýðingu. Skoðum
eftirfarandi setningar sem dæmi:

.. container:: earg

   Anna er smá og kná.

   Þó að Anna sé smá, þá er hún kná.

   Þrátt fyrir að vera smá, þá er Anna kná.

   Anna er smá, en kná.

   Þrátt fyrir smæðina, þá er Anna samt kná.

Þessar setningar yrðu allar þýddar yfir á táknmál setningarökfræði með
sama hætti, kannski sem :math:`S \eand K`.

Það er því mikilvægt að taka allt tal um „þýðingar“ yfir á táknmál
setningarökfræði ekki of hátíðlega. Almennt segjum við að góð þýðing sé
sú sem fangar sem flest blæbrigði og hughrif þess sem þýtt er, en
táknmál setningarökfræði er ekki í stakk búið til þess. Það eina sem
skiptir okkur máli er sanngildið.

Þetta hefur áhrif á það hvernig best er að skilja þýðingarlykla. Tökum
sem dæmi:

.. container:: ekey

   Anna er smá.

   Anna er kná.

Þegar við segjum að við notum þennan þýðingarlykil til að *þýða*
setningu yfir á táknmál setningarökfræði, þá ættum við ekki að skilja
það sem svo að *merking* setningastafanna sé sú sama og merking
setninganna. Það sem við erum að gera er að segja að *sanngildi*
setningastafanna eigi að vera það sama og sanngildi setninganna sem þeir
þýða. Með þessum þýðingarlykli erum við því að segja að grunnsetningin
:math:`S` eigi að vera sönn ef Anna er smá, og ósönn annars, og að
grunnsetningin :math:`K` eigi að vera sönn ef Anna er kná, og ósönn
annars.

.. _`s:IndicativeSubjunctive`:

Framsöguháttur og viðtengingarháttur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Til að hnykkja enn frekar á því að setningarökfræðin fáist aðeins við
sannföll, ætla ég að segja nokkur orð í viðbót um skilyrðissetningar.
Þegar ég kynnti skilgreiningarsanntöfluna fyrir skilyrðistengið til
sögunnar, þá reyndi ég að sýna fram á að sanntaflan væri í raun og veru
vel valin. Ég ætla að byrja á því að fara yfir eitt dæmi til viðbótar.
Dæmið er tekið frá Dorothy Edgington. [1]_

Segjum að Kristín vinkona mín hafi teiknað nokkur form á blað og litað
sum þeirra. Ég hef ekki séð neitt þeirra, en segi samt:

   Ef nokkurt form er grátt, þá er það form líka hringlaga.

Það vill svo til að Kristín hefur teiknað eftirfarandi form:

.. container:: center

Núna er það sem ég sagði ljóslega satt. Form C og D eru ekki grá, og
geta því varla verið *mótdæmi* við þá fullyrðingu að ef eitthvað sé
grátt, þá sé það hringlaga. A *er* grátt, en svo vill til að það er líka
hringlaga. Kristín getur því ekki bent á nein dæmi sem ganga gegn því
sem ég sagði og því liggur beinast við að segja að það sem ég sagði hafi
verið satt. Það þýðir líka að eftirfarandi setningar eru líka sannar:

.. container:: ebullet

   Ef A er grátt, þá er það hringlaga (sannur forliður, sannur bakliður)

   Ef C er grátt, þá er það hringlaga (ósannur forliður, sannur
   bakliður)

   Ef D er grátt, þá er það hringlaga (ósannur forliður, ósannur
   bakliður)

Segjum svo að Kristín teikni eitt form í viðbót, svona:

.. container:: center

Núna er það sem ég sagði ósatt, að ef form er grátt, þá er það
hringlaga. Eftirfarandi fullyrðing er því líka ósönn:

.. container:: ebullet

   Ef B er grátt, þá er það hringlaga (sannur forliður, ósannur
   bakliður)

Við munum að öll setningatengi í setningarökfræði eiga að vera sannföll.
Það þýðir að ekkert nema sanngildi for- og bakliðar ákvarðar sanngildi
skilyrðissetningarinnar sem þeir mynda. Við getum því séð af þessum
fjórum dæmum hver skilgreiningarsanntafla skilyrðistengisins hlýtur að
vera, enda eru þetta allir möguleikarnir, einn fyrir hverja línu í
sanntöflunni.

Þetta dæmi sýnir, með öðrum orðum, að setningatengið „\ :math:`\eif`\ “
sem við skilgreindum hér að ofan með skilgreiningarsanntöflu hefði ekki
getað verið öðruvísi. Þetta setningatengi er *besta skilyrðistengið sem
setningarökfræðin hefur upp á að bjóða*. En hversu vel virkar það sem
þýðing á skilyrðissetningum sem við notum í mæltu máli? Skoðum tvö dæmi:

.. container:: earg

   Ef Halla Tómasdóttir hefði farið með sigur af hólmi í
   forsetakosningunum árið 2016, þá hefði hún orðið önnur konan til að
   gegna embætti forseta.

   Ef Halla Tómasdóttir hefði farið með sigur af hólmi í
   forsetakosningunum árið 2016, þá hefði hún breyst í snjókarl.

Setning `[brownwins1] <#brownwins1>`__ er sönn; setning
`[brownwins2] <#brownwins2>`__ er ósönn. En báðar setninganna hafa
ósanna forliði og ósanna bakliði (Halla Tómasdóttir vann ekki; hún varð
ekki önnur konan til að gegna embætti forseta; og við ættum að geta
slegið því föstu að hún hefði ekki breyst í snjókarl ef svo hefði
verið). Það sýnir að sanngildi `[brownwins2] <#brownwins2>`__ í heild er
ekki fullkomlega ákvarðað af sanngildum hlutasetninganna.

Það sem skiptir mestu máli hér er að setningar
`[brownwins1] <#brownwins1>`__ og `[brownwins2] <#brownwins2>`__ eru í
*viðtengingarhætti*, fremur en *framsöguhætti*. Þegar við setjum fram
þessa hugsun, um hvað hefði gerst ef Halla Tómasdóttir hefði fengið
flest atkvæði í kosningunum, þá erum við að ímynda okkur eitthvað sem
gerðist ekki og svo ímynda okkur eitthvað annað sem *hefði* þá líka
gerst. Slíkt ræður „\ :math:`\eif`\ “ einfaldlega ekki við.

Við munum segja meira um vandkvæðin sem eru bundin skilyrðissetningum í
§\ `4.5 <#s:ParadoxesOfMaterialConditional>`__. Þangað til, þá verðum
við að sætta okkur við að „\ :math:`\eif`\ “ er eina mögulega sannfallið
sem gegnt getur hlutverki skilyrðistengis í setningarökfræði, en á sama
tíma að til séu setningar í mæltu máli sem ekki er hægt að þýða með því
að nota það. Setningarökfræðin er að þessu leyti takmörkuð og við getum
því ekki hugsunarlaust gert ráð fyrir því að allar setningar sem verða á
vegi okkar sé hægt að þýða yfir á táknmál hennar, svo vel sé.

.. _`s:CompleteTruthTables`:

Fullar sanntöflur
-----------------

Hingað til höfum við notað þýðingarlykla til að tiltaka sanngildi
setninga í setningarökfræði *óbeint*. Með því að láta grunnsetninguna
„\ :math:`A`\ “ standa til dæmis fyrir setninguna „Almannagjá er á
Þingvöllum“ þá höfum við þar með sagt að grunnsetningin „\ :math:`A`\ “
eigi að vera sönn ef og aðeins ef Almannagjá er á Þingvöllum. Almannagjá
*er* á Þingvöllum, svo grunnsetningin „\ :math:`A`\ “ er sönn samkvæmt
þessum þýðingarlykli. En við getum líka tiltekið sanngildi grunnsetninga
*beint*. Við getum ákveðið, ef við viljum, að grunnsetningin
„\ :math:`A`\ “ sé sönn án þess að blanda þýðingarlyklum í málið, ef
þess er ekki þörf (nú eða að hún sé ósönn, ef það hentar okkur betur).
Við getum *úthlutað* grunnsetningum sanngildum að vild.

Ef við ákveðum tiltekin sanngildi fyrir *allar* grunnsetningar í
setningu, þá köllum við slíka úthlutun *sanngildadrefingu*:

Í þessu liggur styrkur sanntafla. Hver einasta lína í fullri sanntöflu
stendur fyrir mögulega sanngildadreifingu og því stendur sanntaflan
sjálf fyrir allar mögulegar sanngildadreifingar. Við getum því notað
sanntöflur til að reikna út sanngildi samsettra setninga fyrir allar
mögulegar sanngildadreifingar. En þetta má kannski best sjá með dæmi.

Dæmi um sanntöflu
~~~~~~~~~~~~~~~~~

Tökum setninguna :math:`(H\eand I)\eif H` sem dæmi. Hægt er að úthluta
sanngildunum „satt“ og „ósatt“ á þessar grunnsetningar á fjóra vegu:
„\ :math:`H`\ “ og „\ :math:`I`\ “ geta báðar verið sannar, önnur þeirra
getur verið ósönn eða þær geta báðar verið ósannar. Það eru því fjórar
mögulegar sanngildadreifingar fyrir þessar tvær grunnsetningar. Við
getum táknað þær svona:

.. container:: center

   .. container:: tabular

      | c c|d e e e f
        :math:`H`\ &\ :math:`I`\ &\ :math:`(H`\ &&\ :math:`I)`\ &&\ :math:`H`
      | S & S
      | S & Ó
      | Ó & S
      | Ó & Ó

Til þess að reikna út sanngildi samsettu setningarinnar
:math:`(H \eand I) \eif H`, þá byrjum við á því að afrita sanngildin úr
dálkinum vinstra megin fyrir hvern setningarstaf og skrifum þau beint
fyrir neðan þann staf í samsettu setningunni hægra megin:

.. container:: center

   .. container:: tabular

      | c c|d e e e f
        :math:`H`\ &\ :math:`I`\ &\ :math:`(H`\ &&\ :math:`I)`\ &&\ :math:`H`
      | S & S & S & & S & & S
      | S & Ó & S & & Ó & & S
      | Ó & S & Ó & & S & & Ó
      | Ó & Ó & Ó & & Ó & & Ó

Skoðum núna hlutasetninguna :math:`(H\eand I)`. Þetta er samtenging á
forminu :math:`\meta{A} \eand \meta{B}` þar sem :math:`H` hefur hlutverk
:math:`\meta{A}` og :math:`I` hefur hlutverk :math:`\meta{B}`.
Skilgreiningasanntaflan fyrir „\ :math:`\eand`\ “ segir okkur nákvæmlega
hvenær *hvaða* setning sem er á þessu formi er sönn og hvenær ósönn,
sama hvað :math:`\meta{A}` og :math:`\meta{B}` eru. Samkvæmt henni er
samtenging sönn ef og aðeins ef báðir liðir hennar eru sannir. Í þessu
tilfelli eru liðirnir grunnsetningarnar :math:`H` og :math:`I`. Við
sjáum að þær eru bara sannar á fyrstu línu sanntöflunnar. Þá getum við
skrifað niður sanngildi samtengingar þeirra, :math:`(H\eand I)`, á öllum
fjórum línum sanntöflunnar.

.. container:: center

   .. container:: tabular

      | c c|d e e e f & & :math:`\meta{A}` & & :math:`\meta{B}` & &
      | :math:`H`\ &\ :math:`I`\ &\ :math:`(H`\ &&\ :math:`I)`\ &&\ :math:`H`
      | S & S & S & S & S & & S
      | S & Ó & S & Ó & Ó & & S
      | Ó & S & Ó & Ó & S & & Ó
      | Ó & Ó & Ó & Ó & Ó & & Ó

Nú erum við búin að fylla út hluta sanntöflunnar. Munum að setningin sem
við erum að skoða er setning sem hefur „\ :math:`\eif`\ “ sem aðaltengi,
:math:`\meta{A} \eif \meta{B}`, þar sem :math:`(H \eand I)` hefur
hlutverk :math:`\meta{A}` og :math:`H` hefur hlutverk :math:`\meta{B}`.
Við vitum með því að skoða skilgreiningartöfluna fyrir skilyrðistengið
að skilyrðissetning er sönn þegar forliðurinn er ósannur. Því getum við
skrifað „S“ í línu tvö, þrjú og fjögur undir tákninu fyrir
skilyrðistengið, „\ :math:`\eif`\ “, ( en forliðurinn er ósannur í öllum
þessum línum). Þá er eftir lína eitt, og ef við kíkjum á
skilgreiningarsanntöfluna fyrir skilyrðistengið, þá sjáum við að þar
ættum við líka að setja „S“, enda eru báðar setningarnar sannar þar og
þá er heildin líka sönn, samkvæmt töflunni.

Þá fáum við:

.. container:: center

   .. container:: tabular

      | c c\| d e e e f & & & :math:`\meta{A}` & &&\ :math:`\meta{B}`
      | :math:`H`\ &\ :math:`I`\ &\ :math:`(H`\ &&\ :math:`I)`\ &&\ :math:`H`
      | S & S & & S & &S & S
      | S & Ó & & Ó & &S & S
      | Ó & S & & Ó & &S & Ó
      | Ó & Ó & & Ó & &S & Ó

Skilyrðistengið (:math:`„\eif“`) er aðaltengi setningarinnar. Dálkurinn
undir skilyrðistenginu sýnir okkur því að setningin
:math:`(H \eand I)\eif H` er alltaf sönn, sama hvaða sanngildi :math:`H`
og :math:`I` hafa. Grunnsetningarnar geta verið sannar eða ósannar, í
hvaða samsetningu sem er, og samsetta setningin verður alltaf sönn.
Þetta þýðir að það skiptir ekki máli hvernig við úhlutum sanngildum á
grunnsetningarnar, setningin :math:`(H \eand I)\eif H` er alltaf sönn.
Við segjum þá að hún sé sönn fyrir allar mögulegar sanngildadreifingar.

Í dæminu hér að ofan skrifaði ég ekki hvert einasta sanngildi undir
hverju einasta setningatengi. Það var til þess að auðveldara væri að
lesa töfluna og sjá hvert aðaltengið er og hvaða sanngildi liggja undir
því. En þegar maður skrifar út sanntöflur með blaði og penna, þá er ekki
mjög praktískt að stroka út sanngildi sem maður hefur áður skrifað eða
að skrifa út nýja töflu fyrir hvert skref. Það er því líka hægt að
skrifa töfluna svona:

.. container:: center

   .. container:: tabular

      | c c\| d e e e f
        :math:`H`\ &\ :math:`I`\ &\ :math:`(H`\ &&\ :math:`I)`\ &&\ :math:`H`
      | S & S & S & S & S & & S
      | S & Ó & S & Ó & Ó & & S
      | Ó & S & Ó & Ó & S & & Ó
      | Ó & Ó & Ó & Ó & Ó & & Ó

Sá dálkur sem mestu máli skiptir—og hinir eru bara notaðir til að reikna
út—er sá sem er undir *aðaltengi* setningarinnar. Hann segir okkur hvert
sanngildi setningarinnar í heild er, og þess vegna er hann feitletraður
hér. Þegar maður handskrifar svona töflu er oft gott að gera eitthvað
svipað, t.d. með að strika undir dálkinn, eða eitthvað slíkt.

Að fylla út sanntöflur
~~~~~~~~~~~~~~~~~~~~~~

hefur eina línu fyrir hverja mögulega sanngildadreifingu
grunnsetninganna, þ.e. eina línu fyrir hverja úthlutun á sanngildunum
„satt“ og „ósatt“ á grunnsetningarnar. Hver lína stendur því fyrir eina
mögulega sanngildadreifingu og full tafla hefur eina línu fyrir hverja
mögulega dreifingu.

Stærð sanntöflunnar ræðst því af fjölda grunnsetninga í setningunni sem
verið er að skoða. Ef setning inniheldur einungis eina grunnsetningu, þá
þarf tvær línur, rétt eins og í skilgreiningarsanntöflunni fyrir neitun.
Það skiptir engu þó að sami stafurinn sé endurtekinn oft, til dæmis í
setningunni :math:`[(C\eiff C) \eif C] \eand \enot(C \eif C)`. Full
tafla fyrir þessa setningu er bara tvær línur, því það eru bara tvær
mögulegar sanngildadreifingar: :math:`C` getur verið sönn eða ósönn.
Full sanntafla fyrir þessa setningu lítur svona út:

.. container:: center

   .. container:: tabular

      | c\| d e e e e e e e e e e e e e e f
        :math:`C`\ &\ :math:`[(`\ &\ :math:`C`\ &&\ :math:`C`\ &\ :math:`)`\ &&\ :math:`C`\ &\ :math:`]`\ &&&\ :math:`(`\ &\ :math:`C`\ &&\ :math:`C`\ &\ :math:`)`
      | S & & S & S & S & & S & S & && Ó& & S & S & S &
      | Ó & & Ó & S & Ó & & Ó & Ó & && Ó& & Ó & S & Ó &

Ef við skoðum dálkinn undir aðaltengi setningarinnar (sá feitletraði),
þá sjáum við að setningin er ósönn í báðum línum. Setningin er því
ósönn, sama hvort :math:`C` er sönn eða ekki. Hún er ósönn fyrir allar
sanngildadreifingar.

Full sanntafla fyrir setningu sem samanstendur af tveimur grunnsetningum
er fjórar línur, rétt eins og skilgreiningasanntöflurnar fyrir öll
setningatengin nema neitun, eða setninguna :math:`(H \eand I)\eif H`.

Full sanntafla fyrir setningu sem inniheldur þrjár grunnsetningar er
átta línur, t.d. þessi:

.. container:: center

   .. container:: tabular

      | c c c|d e e e f
        :math:`M`\ &\ :math:`N`\ &\ :math:`P`\ &\ :math:`M`\ &&\ :math:`(N`\ &&\ :math:`P)`
      | S & S & S & S & & S & S & S
      | S & S & Ó & S & & S & S & Ó
      | S & Ó & S & S & & Ó & S & S
      | S & Ó & Ó & S & & Ó & Ó & Ó
      | Ó & S & S & Ó & & S & S & S
      | Ó & S & Ó & Ó & & S & S & Ó
      | Ó & Ó & S & Ó & & Ó & S & S
      | Ó & Ó & Ó & Ó & & Ó & Ó & Ó

Þessi tafla sýnir að setningin :math:`M\eand(N\eor P)` getur verið hvort
tveggja, sönn og ósönn, allt eftir því hvaða sanngildi grunnsetningarnar
:math:`M`, :math:`N` og :math:`P` hafa.

Full sanntafla fyrir setningu sem er sett saman úr fjórum grunnsetningum
þarf svo 16 línur, sanntafla með fimm grunnsetningum 32 línur og
sanntafla með sex grunnsetningum þarf 64 línur. Almennt gildir að full
sanntafla með :math:`n` grunnsetningum er :math:`2^n` línur.

Til þess að fylla út sanntöflu er best að byrja á að fylla út sanngildin
fyrir grunnsetninguna sem er lengst til hægri. Það er dálkurinn undir
„\ :math:`P`\ “ hér að ofan. Þar er best að skrifa „S“ efst og svo „Ó“
og „S“ á víxl í línurnar fyrir neðan. Fyrir næstu grunnsetningu til
vinstri skrifar maður svo tvö „S“ efst, og svo tvö „Ó“ fyrir neðan,
o.s.frv. Almennt gildir að fyrir næstu grunnsetningu til vinstri við þá
sem maður var að fylla út, þá fyllir maður út tvöfalt fleiri „S“ í einu
og tvöfalt fleiri „Ó“. Ef þetta er gert rétt, þá mun sanntaflan hafa
allar mögulegar sanngildadreifingar.

*Síðasti dálkurinn sem við fyllum út er dálkurinn undir aðaltengi
setningarinnar. Því þurfum við að finna aðaltengið og setningarnar sem
það tengir saman og þar gildir það sama: síðasti dálkurinn sem við
fyllum út í þeim er dálkurinn undir aðaltenginu sem tengir þær saman,
o.s.frv. Við vinnum okkur því svona niður þangað til við komum að
grunnsetningunum og þannig getum við fyllt út töfluna*.

Við getum líka, ef við viljum, fyllt út sanntöflur þar sem metabreytur
hafa sama hlutverk og grunnsetningarnar. Til dæmis gætum við fyllt út
eftirfarandi sanntöflu, þar sem :math:`\meta{A}` stendur í stað
:math:`C`:

.. container:: center

   .. container:: tabular

      | c\| d e e e e e e e e e e e e e e f
        :math:`\meta{A}`\ &\ :math:`[(`\ &\ :math:`\meta{A}`\ &&\ :math:`\meta{A}`\ &\ :math:`)`\ &&\ :math:`\meta{A}`\ &\ :math:`]`\ &&&\ :math:`(`\ &\ :math:`\meta{A}`\ &&\ :math:`\meta{A}`\ &\ :math:`)`
      | S & & S & S & S & & S & S & && Ó& & S & S & S &
      | Ó & & Ó & S & Ó & & Ó & Ó & && Ó& & Ó & S & Ó &

Hún sýnir að allar setningar á þessu *formi* hljóta að vera ósannar.

.. _`s:MoreBracketingConventions`:

Fleiri svigavenjur
~~~~~~~~~~~~~~~~~~

Skoðum eftirfarandi tvær setningar:

.. math::

   \begin{aligned}
           ((A \eand B) \eand C)\\
           (A \eand (B \eand C))
       
   \end{aligned}

Þessar setningar hafa ekki sömu myndunarsögu. Sú fyrri er mynduð úr
:math:`(A \eand B)` og :math:`C`, en sú seinni úr :math:`A` og
:math:`(B \eand C)`. Þær hafa þrátt fyrir það báðar sömu sanntöflu. Það
skiptir því engu máli—frá sjónarhóli setningarökfræðinnar—hvora
setninguna við notum, því setningarökfræðin hefur bara áhuga á
sanngildum (sjá §\ `2 <#s:TruthFunctionality>`__). Við getum því sleppt
því að skrifa svigana, því þeir skipta ekki máli. Við getum því sparað
okkur örlítið ómak með því að skrifa:

.. math::

   \begin{aligned}
           A \eand B \eand C
       
   \end{aligned}

Þetta gildir almennt um setningar af þessu tagi: ef við höfum margar
samtengingar hver á eftir annarri, þá getum við sleppt innri svigunum
(en við vorum þegar búin að leyfa að sleppa þeim ytri hér að ofan í
§\ `[s:TFLSentences] <#s:TFLSentences>`__).

Það sama má segja um mistengingar, þ.e. margar setningar í röð tengdar
saman með „\ :math:`\eor`\ “. Þar sem eftirfarandi tvær setningar hafa
sömu sanntöflu:

.. math::

   \begin{aligned}
           ((A \eor B) \eor C)\\
           (A \eor (B \eor C))
       
   \end{aligned}

getum við einfaldlega skrifað:

.. math::

   \begin{aligned}
           A \eor B \eor C
       
   \end{aligned}

Við getum því líka sleppt innri svigum ef við höfum margar mistengingar
hver á eftir annarri. En við þurfum að fara *varlega*! Þessar tvær
setningar hafa *ólíkar* sanntöflur:

.. math::

   \begin{aligned}
           ((A \eif B) \eif C)\\
           (A \eif (B \eif C))
       
   \end{aligned}

Það þýðir að setningin:

.. math::

   \begin{aligned}
           A \eif B \eif C
       
   \end{aligned}

er tvíræð. Það er ekki ljóst hvort hún standi fyrir setninguna
:math:`((A \eif B) \eif C)` eða setninguna :math:`(A \eif (B \eif C))`.
Við getum því *ekki* sleppt svigum þegar um er að ræða
skilyrðissetningar. Sama gildir um setningar af þessu tagi:

.. math::

   \begin{aligned}
           ((A \eor B) \eand C)\\
           (A \eor (B \eand C))
       
   \end{aligned}

Þær hafa ólíkar sanntöflur. Ef við myndum þá skrifa:

.. math::

   \begin{aligned}
           A \eor B \eand C
       
   \end{aligned}

þá væri setningin líka tvíræð. *Við sleppum því aldrei innri svigum
þegar um er að ræða blandaðar setningar*. Við getum *bara* sleppt þessum
svigum þegar um er að ræða margar setningar í röð tengdar saman með
*og-tengjum* eða *eða-tengjum*. Aldrei annars.

Fyllið út sanntöflur fyrir eftirfarandi setningar:

.. container:: earg

   :math:`A \eif A`

   :math:`C \eif\enot C`

   :math:`(A \eiff B) \eiff \enot(A\eiff \enot B)`

   :math:`(A \eif B) \eor (B \eif A)`

   :math:`(A \eand B) \eif (B \eor A)`

   :math:`\enot(A \eor B) \eiff (\enot A \eand \enot B)`

   :math:`\bigl[(A\eand B) \eand\enot(A\eand B)\bigr] \eand C`

   :math:`[(A \eand B) \eand C] \eif B`

   :math:`\enot\bigl[(C\eor A) \eor B\bigr]`

Sýnið að nýju svigavenjurnar sem voru kynntar til sögunnar í
§\ `3.3 <#s:MoreBracketingConventions>`__ séu í lagi, þ.e. sýnið:

.. container:: earg

   að :math:`((A \eand B) \eand C)` og :math:`(A \eand (B \eand C))`
   hafi sömu sanntöflu,

   að :math:`((A \eor B) \eor C)` og :math:`(A \eor (B \eor C))` hafi
   sömu sanntöflu,

   að :math:`((A \eor B) \eand C)` og :math:`(A \eor (B \eand C))` hafi
   *ekki* sömu sanntöflu,

   að :math:`((A \eif B) \eif C)`\ “ og :math:`(A \eif (B \eif C))` hafi
   *ekki* sömu sanntöflu.

Sýnið líka að :

.. container:: earg

   :math:`((A \eiff B) \eiff C)` og :math:`(A \eiff (B \eiff C))` hafi
   sömu sanntöflu.

Ef þið viljið æfa ykkur frekar, þá er hægt að fylla út sanntöflur fyrir
setningarnar og rökfærslurnar sem komu fyrir í æfingum síðasta kafla.

.. _`s:semanticconcepts`:

Merkingarfræðileg hugtök
------------------------

Í þessum hluta höfum við talað um sanngildadreifingar og hvernig er hægt
að ákvarða sanngildi hvaða setningar sem er í setningarökfræði, sama
hvaða sanngildadreifingu við veljum fyrir grunnsetningarnar með
sanntöflum. Núna ætlum við að fjalla um skyld hugtök og sýna hvernig
hægt er að nota sanntöflur til hjálpa okkur við beitingu þeirra.

Við köllum þessi hugtök *merkingarfræðileg hugtök*. Það er að vissu
leyti óheppileg nafngift, því þessi hugtök hafa að gera með *sannleika*
og *gildi*. En þetta er það sem þau eru kölluð og því vissara að halda
sig við hefðina.

Klifanir og mótsagnir
~~~~~~~~~~~~~~~~~~~~~

Í §\ `[s:BasicNotions] <#s:BasicNotions>`__, fjölluðum við um
*nauðsynlega sannar* og *nauðsynlega ósannar* setningar. Þessi hugtök
eiga sér hliðstæðu í setningarökfræði. Hliðstæðu nauðsynlegra sannra
setninga í setningarökfræði köllum við *klifanir*: Við getum notað
sanntöflur til að ákvarða hvort setning sé klifun. Ef setningin er sönn
á hverri línu sanntöflu sinnar, þá er hún sönn fyrir allar
sanngildadreifingar, og þá er hún klifun. Ein af setningunum hér að ofan
í §\ `3 <#s:CompleteTruthTables>`__, :math:`(H \eand I) \eif H`, er
klifun. Hún er sönn, sama hvað. Annað dæmi um einfalda klifun er
:math:`P \eor \enot P`.

*Klifun* er þó ekki nema hliðstæða nauðynlegs sannleika. Sumar
fullyrðingar eru nauðsynlega sannar án þess þó að vera þýðanlegar yfir á
táknmál setningarökfræði. Dæmi um slíka setningu er :math:`2+2=4`. Hún
er nauðsynlega sönn, en þó getum við ekki þýtt hana yfir á táknmál
setningarökfræði. Það besta sem við getum gert er að þýða hana sem
grunnsetningu—og engar grunnsetningar eru klifanir. Ef hins vegar er
hægt að þýða setningu á mæltu máli yfir á táknmál setningarökfræði svo
vel sé, og sú setning er klifun, þá er setningin nauðynlega sönn.

Svipuð hliðstæða er til fyrir nauðsynlega ósannar setningar. Þær köllum
við *mótsagnir*:

Við getum líka notað sanntöflur til að ákvarða hvort setning sé mótsögn.
Ef setningin er ósönn á hverri línu sanntöflu sinnar, þá er hún ósönn
fyrir allar sanngildadreifingar, og þá er hún mótsögn. Ein af
setningunum hér að ofan í §\ `3 <#s:CompleteTruthTables>`__,
:math:`[(C\eiff C) \eif C] \eand \enot(C \eif C)`, er mótsögn. Hún er
ósönn, sama hvað. Dæmi um einfalda mótsögn er :math:`P \eand \enot P`.

Rökfræðilegt jafngildi
~~~~~~~~~~~~~~~~~~~~~~

Hér er annað gagnlegt hugtak:

Við höfum nú þegar nýtt okkur þetta hugtak, í
§\ `3.3 <#s:MoreBracketingConventions>`__: Við getum sleppt svigum í
:math:`(A \eand B) \eand C` og :math:`A \eand (B \eand C)` af því að
þessar setningar eru rökfræðilega jafngildar. Það er auðvelt að nota
sanntöflur til að ganga úr skugga um hvort setningar séu rökfræðilega
jafngildar. Skoðum dæmi um tvær setningar, :math:`\enot(P \eor Q)` og
:math:`\enot P \eand \enot Q`. Við fyllum út sanntöflu fyrir þessar tvær
setningar samtímis, svona:

.. container:: center

   .. container:: tabular

      | c c|d e e f \|d e e e f
        :math:`P`\ &\ :math:`Q`\ &&\ :math:`(P`\ &&\ :math:`Q)`\ &&\ :math:`P`\ &&&\ :math:`Q`
      | S & S & & S & S & S & Ó & S & & Ó & S
      | S & Ó & & S & S & Ó & Ó & S & & S & Ó
      | Ó & S & & Ó & S & S & S & Ó & & Ó & S
      | Ó & Ó & & Ó & Ó & Ó & S & Ó & & S & Ó

Við skoðum dálkana sem liggja undir aðaltengjum setninganna. Í fyrri
setningunni er aðaltengið neitun, en og-tengi í þeirri seinni. Við sjáum
að á fyrstu þremur línunum eru báðar setningarnar ósannar, en í þeirri
síðustu eru báðar sannar. Setningarnar eru því sannar fyrir sömu
sanngildadreifingar og eru þar af leiðandi rökfræðilega jafngildar.

Rökfræðileg samkvæmni
~~~~~~~~~~~~~~~~~~~~~

Í §\ `[s:BasicNotions] <#s:BasicNotions>`__ hér að ofan sögðum við að
setningar væru *samrýmanlegar* ef og aðeins ef það er mögulegt fyrir þær
að vera allar sannar samtímis. Við höfum líka hliðstæðu við það í
setningarökfræði: Á sama hátt segjum við að setningar séu eff ekki er
til sanngildadreifing þar sem þær eru allar sannar. Við getum
auðveldlega notað sanntöflur til að athuga hvort setningar séu
rökfræðilega samkvæmar. Við förum alveg eins að við það og hér að ofan,
nema í þetta skiptið er nóg að athuga hvort til sé *ein* lína þar
setningarnar eru báðar sannar. Ef við viljum kanna rökfræðilega
*ósamkvæmni*, þá þurfum við að fullvissa okkur um að *engin* slík lína
sé til.

Rökfræðileg afleiðing og gildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú komum við að setningarfræðilegri hliðstæðu gildis: Þessi skilgreining
er almenn, og þarf að gilda fyrir hvaða fjölda setninga sem er og hvaða
setningar sem er. Þess vegna skrifum við feitletraða stafi með lágvísum
á þennan hátt.

En ef við skoðum einfaldara dæmi með einungis tveimur grunnsetningum, þá
verður hugmyndin ef til vill skýrari. Við segjum að :math:`Q` leiði
rökfræðilega af :math:`P \eif Q` og :math:`P` ef og aðeins ef *ekki* er
til sanngildadreifing þar sem :math:`P \eif Q` og :math:`P` eru báðar
sannar, en :math:`Q` ósönn. Við sjáum að svo er ekki: ef
:math:`P \eif Q` og :math:`P` eru sannar, þá vitum við forliður
:math:`P \eif Q` er sannur og að bakliðurinn er ekki ósannur (skoðið
skilgreiningasanntöfluna fyrir „\ :math:`\eif`\ “ til að fullvissa ykkur
um það!) og þá hlýtur :math:`Q` að vera sönn líka.

Þetta má kanna með sanntöflum. Tökum annað, flóknara dæmi. Til að vita
hvort :math:`J` leiði rökfræðilega af :math:`\enot L \eif (J \eor L)` og
:math:`\enot L` þá þurfum við að athuga hvort til sé sanngildadreifing
þar sem :math:`\enot L \eif (J \eor L)` og :math:`\enot L` eru sannar,
en :math:`J` ósönn. Ef svo er *ekki*, þá :math:`J` leiðir rökfræðilega
af :math:`\enot L \eif (J \eor L)` og :math:`\enot L`. Svona liti
sanntaflan út:

.. container:: center

   .. container:: tabular

      | c c|d e e e e f|d f\| c
        :math:`J`\ &\ :math:`L`\ &&\ :math:`L`\ &&\ :math:`(J`\ &&\ :math:`L)`\ &&\ :math:`L`\ &\ :math:`J`
      | S & S & Ó & S & & S & S & S & & S &
      | S & Ó & S & Ó & & S & S & Ó & & Ó &
      | Ó & S & Ó & S & & Ó & S & S & & S &
      | Ó & Ó & S & Ó & & Ó & Ó & Ó & & Ó &

Eina línan þar sem :math:`\enot L \eif (J \eor L)` og :math:`\enot L`
eru báðar sannar er lína tvö, og þar er :math:`J` líka sönn. Það er því
engin sanngildadreifing þar sem forsendurnar eru allar sannar,
:math:`\enot L \eif (J \eor L)` og :math:`\enot L`, en :math:`J` ósönn.
:math:`J` leiðir því rökfræðilega af :math:`\enot L \eif (J \eor L)` og
:math:`\enot L`.

Rökfræðileg samkvæmni er nátengd gildi: [2]_

Ástæðan er þessi: Ef :math:`\meta{B}` leiðir rökfræðilega af
:math:`\meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n`, þá er ekki til nein
sanngildadreifing þar sem
:math:`\meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n` eru sannar en
:math:`\meta{B}` ósönn. Það er því *rökfræðilega ómögulegt* að
:math:`\meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n` séu allar sannar en
:math:`\meta{B}` ósönn. En það er einmitt það sem skilgreiningin okkar á
gildi sagði, að rökfærsla sé gild ef og aðeins ef það er ómögulegt að
forsendurnar séu allar sannar en niðurstaðan ósönn.

Við höfum því loks fundið *aðferð* til að kanna gildi rökfærsla á mæltu
máli: fyrst þýðum við hana yfir á táknmál setningarökfræði og svo könnum
við rökfræðilega afleiðingu með því að nota sanntöflur. Það er þó vert
að nefna að hér notum við hugtakið „rökfræðileg afleiðing“ sem tæknilegt
hugtak samkvæmt skilgreiningunni hér að ofan. Í mæltu máli er það hins
vegar oft notað sem samheiti yfir gildi, eða eitthvað svipað.

.. _`s:ParadoxesOfMaterialConditional`:

Takmarkanir þessarar aðferðar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Þetta er þó merkur áfangi: aðferð til að meta gildi rökfærsla! En þessi
aðferð hefur því miður sínar takmarkanir. Skoðum þrjú dæmi:

Skoðum fyrst eftirfarandi rökfærslu:

.. container:: earg

   Búkolla er með fjóra fætur. Þar af leiðandi er Búkolla með fleiri en
   tvo fætur.

Til að þýða þessa rökfærslu yfir á táknmál setningarökfræði erum við
nauðbeygð til að nota mismunandi grunnsetningar—kannski :math:`F` og
:math:`T`—fyrir forsenduna og niðurstöðuna. En það er augljóst að
:math:`T` leiðir ekki rökfræðilega af :math:`F`. En þó er rökfærslan þó
greinilega gild!

Skoðum nú eftirfarandi setningu:

.. container:: earg

   Jón er hvorki sköllóttur né ekki-sköllóttur.

Það væri eðlilegt að þýða þessa setningu yfir á táknmál setningarökfæði
með :math:`\enot J \eand \enot \enot J`. En þetta er mótsögn (eins og
þið ættuð að kanna með sanntöflu). En setningin sjálf virðist ekki vera
mótsögn. Til dæmis gætum við sagt að Jón sé á mörkum þess að vera
sköllóttur.

Hér er eitt dæmi í viðbót:

.. container:: earg

   Það er ekki satt að ef Guð er til, þá svari hún bölbænum.

Ef við þýddum þessa setningu yfir á táknmál setningarökfræði, þá væri
:math:`\enot (G \eif M)` eðlileg þýðing. En :math:`G` leiðir
rökfræðilega af :math:`\enot (G \eif M)` (og þetta ættuð þið að athuga
með sanntöflu). En þetta þýðir að ef við þýðum
`[n:GodParadox] <#n:GodParadox>`__ yfir á táknmál setningarökfræði, þá
virðumst við hafa sannað tilvist Guðs! En það er varla svona auðvelt,
eða hvað? Ættu ekki jafnvel örgustu trúleysingar að geta tekið undir að
`[n:GodParadox] <#n:GodParadox>`__ sé sönn, án þess að lenda þar með í
mótsögn við sjálfa sig (og ef þið takið ekki undir það, athugið þá að
við gætum smíðað sambærilega setningu um Óðinn eða Þór)?

Þessi dæmi sýna, hvert á sinn hátt, takmarkanir þess að notast við mál
sem reiðir sig *eingöngu* á sannföll eins og setningarökfræðin gerir.
Þessar takmarkanir vekja upp ýmsar áhugaverðar spurningar í
heimspekilegri rökfræði (þ.e. þeim hluta heimspekinnar sem fjallar um
rökfræðileg málefni). Dæmið um hárið á Jóni (eða skortinn þar á) vekur
til dæmis upp spurningar hvernig best sé að eiga við setningar sem tjá
það sem er óljóst eða loðið: hvenær er maður sköllóttur og hvenær verða
sandkorn að hrúgu? Dæmið um Guð er svo tengt hinum svokölluðu
*skilyrðisþversögnum* (en við höfum séð fleiri slíkar, til dæmis að
skilyrðissetning með ósönnum forlið er alltaf sönn).

Af hverju þá að læra setningarökfræði? Hluti af svarinu er að það er
ekkert eitt kerfi sem er augljóslega betra og það er umdeilt hvernig
bregðast eigi við þessum spurningum. Til þess að geta tekist á við
slíkar spurningar þarf maður því að byrja einhvers staðar og
setningarökfræðin er þar langbesti kosturinn. Hún er einföld, vel þekkt
og í raun og veru furðulega sterk.

Sérstakt tákn fyrir rökfræðilega afleiðingu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við munum tala mikið um rökfræðilega afleiðingu í því sem eftir er af
bókinni. Það er þess vegna þægilegt að innleiða nýtt tákn til að tala um
hana. Við munum því sjaldan segja beint út að setninguna
:math:`\meta{B}` leiði rökfræðilega af
:math:`\meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n`, heldur frekar
skammstafa það með því að skrifa:

.. math:: \meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n \entails \meta{B}

Við notum táknið „\ :math:`\entails`\ “ því til að tákna rökfræðilega
afleiðingu.

Tökum samt *vel* eftir því að :math:`\entails`\ “ er ekki tákn á
táknmáli setningarökfræði. Það er tákn sem við skilgreinum í
framsetningarmálinu, í okkar tilfelli íslensku, til að eiga hægara með
að tala *um* setningar í setningarökfræði (sjá
§\ `[s:UseMention] <#s:UseMention>`__ fyrir frekari umfjöllun um þennan
greinarmun).

Eftirfarandi setning á *framsetningarmálinu*:

.. container:: ebullet

   :math:`P, P \eif Q \entails Q`

er því bara stytting eða skammstöfun á þessari setningu, sem líka er
hluti af viðfangsmálinu:

.. container:: ebullet

   Setninguna :math:`Q` leiðir rökfræðilega af setningunum :math:`P` og
   :math:`P \eif Q`.

Það eru engin takmörk fyrir því hversu margar setningar í
setningarökfræði við getum talað um í einu með þessu tákni. En við getum
líka sleppt því að setja nokkra setningu vinstra megin og skrifað:

.. math:: \phantom{\meta{A}}\entails \meta{B}

Þetta segir að það sé engin sanngildadreifing sem er þannig að allar
setningarnar vinstra megin við „\ :math:`\entails`\ “ séu sannar og að
:math:`\meta{B}` sé ósönn. Þar sem það eru *engar* setningar vinstra
megin, þá látum við þetta merkja að :math:`\meta{B}` sé sönn fyrir
*allar* sanngildadreifingar. Það er að segja: :math:`\meta{B}` er
klifun. Við höfum nú þegar séð dæmi um slíkar setningar. Til dæmis
gildir að

.. math:: \entails P \eor \enot P

Við notum svipaðan rithátt við að segja að :math:`\meta{B}` sé mótsögn:

.. math:: \meta{B} \entails\phantom{\meta{C}}

Þetta segir að :math:`\meta{B}` sé ósatt fyrir allar
sanngildadreifingar.

Stundum viljum við neita því að setningu leiði rökfræðilega af annarri.
Það er að segja:

.. container:: center

   það er ekki satt að
   :math:`\meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n \entails \meta{B}`

Hér styttum við okkur aftur leið og strikum einfaldlega yfir táknið:

.. math:: \meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n \nentails \meta{B}

Þetta merkir að það er til *einhver* sanngildadreifing sem er þannig að
:math:`\meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n` eru allar sannar en
:math:`\meta{B}` ósönn. Athugið *alveg sérstaklega vel* að þetta er ekki
það sama og
:math:`\meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n \entails \enot \meta{B}`!
Það myndi merkja að :math:`\enot \meta{B}` leiði rökfræðilega af
:math:`\meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n`.

„\ :math:`\entails`\ “ og „\ :math:`\eif`\ “
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hér að ofan sagði ég að „\ :math:`\entails`\ “ væri hluti af
framsetningarmálinu en ekki hluti af táknmáli setningarökfræðinnar. Á
gagnstæðan hátt er „\ :math:`\eif`\ “ hluti af táknmáli
setningarökfræðinnar, en ekki hluti af framsetningarmálinu. Það eru þó
tengsl þarna á milli.

Af ofansögðu vitum við að :math:`\meta{A} \entails \meta{B}` ef og
aðeins ef ekki er til sanngildadreifing þar sem :math:`\meta{A}` er sönn
og :math:`\meta{B}` ósönn.

Við vitum líka að: :math:`\meta{A} \eif \meta{B}` er klifun ef og aðeins
ef ekki er til sanngildadreifing þar sem :math:`\meta{A} \eif \meta{B}`
er ósönn. Við vitum líka að skilyrðissetning er alltaf sönn, nema þegar
forliðurinn er sannur en bakliðurinn ósannur, og því er
:math:`\meta{A} \eif \meta{B}` kilfun ef og aðeins ef ekki er til
sanngildadrefing þar sem :math:`\meta{A}` er sönn en :math:`\meta{B}`
ósönn. Með því að setja þetta tvennt saman, þá sjáum við að
:math:`\meta{A} \eif \meta{B}` er klifun ef og aðeins ef
:math:`\meta{A} \entails \meta{B}`.

Þrátt fyrir það er mikilvægt halda þessum tveimur táknum aðskildum:

Þegar við setjum tvær setningar á máli setningarökfræði sitthvoru megin
við „\ :math:`\eif`\ “, þá er útkoman lengri setning á máli
setningarökfræðinnar. Á hinn bóginn, þegar við notum
„\ :math:`\entails`\ “, þá er um að ræða setningu á framsetningarmálinu
sem *talar um* setningar á máli setningarökfræði.

Skoðið setningarnar í æfingu §\ `3 <#s:CompleteTruthTables>`__\ **A**
hér að ofan. Athugið með sanntöflum hvaða setningar eru klifanir,
hverjar mótsagnir og hverjar eru hvorki klifanir né mótsagnir.

Notið sanntöflur til að ákvörða hverjar af eftirfarandi setningum eru
rökfræðilega samkvæmar og hverjar eru rökfræðilega ósamkvæmar:

.. container:: earg

   :math:`A\eif A`, :math:`\enot A \eif \enot A`, :math:`A\eand A`,
   :math:`A\eor A`

   :math:`A\eor B`, :math:`A\eif C`, :math:`B\eif C`

   :math:`B\eand(C\eor A)`, :math:`A\eif B`, :math:`\enot(B\eor C)`

   :math:`A\eiff(B\eor C)`, :math:`C\eif \enot A`, :math:`A\eif \enot B`

Notið sanntöflur til að meta eftirfarandi rökfærslur:

.. container:: earg

   :math:`A\eif A \therefore A`

   :math:`A\eif(A\eand\enot A) \therefore \enot A`

   :math:`A\eor(B\eif A) \therefore\enot A \eif \enot B`

   :math:`A\eor B, B\eor C, \enot A \therefore B \eand C`

   :math:`(B\eand A)\eif C, (C\eand A)\eif B \therefore (C\eand B)\eif A`

Svarið eftirfarandi spurningum og rökstyðjið svarið.

.. container:: earg

   Gerum ráð fyrir að :math:`\meta{A}` og :math:`\meta{B}` séu
   rökfræðilega jafngildar. Hvað getum við sagt um
   :math:`\meta{A} \eiff \meta{B}`?

   Gerum ráð fyrir að :math:`(\meta{A} \eand \meta{B}) \eif \meta{C}` sé
   hvorki klifun né mótsögn. Hvað getum við sagt um
   :math:`\meta{A}, \meta{B} \entails \meta{C}`?

   Gerum ráð fyrir að :math:`\meta{A}`, :math:`\meta{B}` og
   :math:`\meta{C}` séu rökfræðilega ósamkvæmar. Hvað getum við sagt um
   :math:`\meta{A} \eand \meta{B} \eand\meta{C}`?

   Gerum ráð fyrir að :math:`\meta{A}` sé mótsögn. Hvað getum við sagt
   um eftirfarandi rökfærslu:
   :math:`\meta{A}, \meta{B} \therefore~\meta{C}`?

   Gerum ráð fyrir því að :math:`\meta{C}` sé klifun. Hvað getum við
   sagt um eftirfarandi rökfærslu:
   :math:`\meta{A}, \meta{B} \therefore~\meta{C}`?

   Gerum ráð fyrir að :math:`\meta{A}` og :math:`\meta{B}` séu
   rökfræðilega jafngildar. Hvað getum við sagt um
   :math:`\meta{A} \eor \meta{B}`?

   Gerum ráð fyrir að :math:`\meta{A}` og :math:`\meta{B}` séu *ekki*
   rökfræðilega jafngildar. Hvað getum við sagt um
   :math:`\meta{A} \eor \meta{B}`?

Skoðum eftirfarandi reglu:

.. container:: ebullet

   Gerum ráð fyrir að :math:`\meta{A}` og :math:`\meta{B}` séu
   rökfræðilega jafngildar. Ef rökfærsla inniheldur :math:`\meta{A}`,
   annað hvort sem forsendu eða niðurstöðu, þá væri gildi rökfærslunnar
   óbreytt, ef við skiptum :math:`\meta{A}` út fyrir :math:`\meta{B}`.

Er þessi regla rétt? Rökstyðjið svarið.

Að stytta sér leið
------------------

Með æfingu er fljótlega hægt að verða ansi lunkinn við að fylla út og
nota sanntöflur. Það er þó hægt að stytta sér leið með ýmsum hætti og í
þessum hluta ætla ég að nefna nokkra leiðir til þess.

Styttri leiðir við að fylla út sanntöflur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Það fyrsta sem ég vil nefna er að strangt til tekið þarf ekki að afrita
sanngildin undir hverri grunnsetningu vinstra megin yfir undir hverja
grunnsetningu hægra megin. Það er hægt að skrifa einfaldlega:

.. container:: center

   .. container:: tabular

      | c c|d e e e e f
        :math:`P`\ &\ :math:`Q`\ &\ :math:`(P`\ &&\ :math:`Q)`\ &&&\ :math:`P`
      | S & S & & S & & & Ó
      | S & Ó & & S & & & Ó
      | Ó & S & & S & & & S
      | Ó & Ó & & Ó & & & S

En þetta er þó tvíeggjað sverð. Þegar maður sleppir afrituninni, þá
aukast líkurnar á klaufavillum verulega og því ekki alltaf ljóst að
þetta spari manni mikla vinnu til lengri tíma litið. En fyrir þá sem
hafa skarpa sjón og örugga rithönd er gott að vita af þessum möguleika.

En hér er traustari möguleiki: Við vitum að setning sem tengd er saman
með eða-tengi er sönn þegar önnur setninganna sem hún er sett saman úr
er sönn. Svo ef við sjáum að ein þeirra er sönn, þá er engin ástæða til
að leita að hinni og athuga sanngildi þeirra. Því er hægt að skrifa:

.. container:: center

   .. container:: tabular

      | c c|d e e e e e e f :math:`P`\ &\ :math:`Q`\ & :math:`(\enot` &
        :math:`P`\ &&&\ :math:`Q)`\ &&&\ :math:`P`
      | S & S & Ó & & Ó & Ó& & & Ó
      | S & Ó & Ó & & S& S& & & Ó
      | Ó & S & & & & & & & S
      | Ó & Ó & & & & & & & S

Við vitum líka að samtenging er ósönn ef og aðeins ef önnur setninganna
sem hún er sett saman úr er ósönn. Ef við sjáum að önnur þeirra er
ósönn, er því engin ástæða til að athuga hvort hin sé sönn eða ósönn.
Við vitum strax að samtengingin er ósönn. Þess vegna getum við skrifað:

.. container:: center

   .. container:: tabular

      | c c|d e e e e e e f
        :math:`P`\ &\ :math:`Q`\ &&\ :math:`(P`\ &&&\ :math:`Q)`\ &&&\ :math:`P`
      | S & S & & & & & & & Ó
      | S & Ó & & && & & & Ó
      | Ó & S & S & & Ó & & & & S
      | Ó & Ó & S & & Ó & & & & S

Svipuðu máli gegnir um skilyrðissetningar. Við vitum að
skilyrðissetningar eru sannar ef forliðurinn er ósannur eða bakliðurinn
sannur (skilyrðissetning er jú bara *ósönn* ef forliðurinn er sannur og
bakliðurinn ósannur). Þá getum við stytt okkur leið svona:

.. container:: center

   .. container:: tabular

      | c c|d e e e e e f :math:`P`\ &\ :math:`Q`\ &
        :math:`((P`\ &&\ :math:`Q`)&&\ :math:`P)`\ &&\ :math:`P`
      | S & S & & & & & & &
      | S & Ó & & & && & &
      | Ó & S & & S & & Ó & & &
      | Ó & Ó & & S & & Ó & & &

Setningin „\ :math:`((P \eif Q) \eif P) \eif P`\ “ er því klifun—hún er
sönn fyrir hvaða sanngildadreifingu sem er. Þessi setning er raunar dæmi
um hið svokallaða *Pierce-lögmál*, en það er kennt við rökfræðinginn
Charles Sanders Peirce.

Styttri leiðir við kanna gildi og rökfræðilega afleiðingu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rökfærsla er gild, eins og við munum, þegar það er engin leið fyrir
forsendurnar að vera allar sannar en að niðurstöðuna sé ósanna. Við
vitum líka að ef niðurstöðu leiðir rökfræðilega af forsendum rökfærslu,
þá er hún gild. Hér að ofan í §\ `4 <#s:semanticconcepts>`__ lærðum við
að nota sanntöflur til að kanna hvort eina setningu leiðir rökfræðilega
af annarri.

Við gerðum það með því að leita að línu í sanntöflunni þar sem
forsendurnar eru allar sannar en niðurstaðan er ósönn. Köllum slíka línu
*slæma*. Ef við finnum slæma línu, þá vitum við að rökfærslan er *ekki*
gild og ef við finnum *ekki* slíka línu, þá vitum við að hún *er* gild.

Við vitum líka að:

.. container:: earg

   Ef niðurstaðan er sönn í einhverri tiltekinni línu, þá er sú lína
   ekki slæm (og við þurfum ekki að skoða neitt *frekar* á þeirri línu
   til að fullvissa okkur um það). Allar slæmar línur hafa ósanna
   niðurstöðu.

   Ef einhver af forsendunum er ósönn í tiltekinni línu, þá er sú lína
   ekki slæm (og við þurfum heldur ekki að skoða neitt *frekar* á þeirri
   línu til að fullvissa okkur um það). Allar forsendur eru sannar í
   slæmum línum.

Ef engin lína er slæm, þá vitum við að rökfærslan er gild. Með þetta í
huga, þá getum við flýtt fyrir okkur ansi mikið. Skoðum til dæmis
eftirfarandi rökfærslu:

.. math:: \enot L \eif (J \eor L), \enot L \therefore J

Það fyrsta sem við ættum að gera er að skoða niðurstöðuna. Ef við sjáum
að niðurstaðan er *sönn* á einhverri tiltekinni línu, þá er sú lína ekki
slæm. Þá getum við hunsað restina af henni. Eftir að hafa gert það, þá
höfum við:

.. container:: center

   .. container:: tabular

      | c c|d e e e e f \|d f|c
        :math:`J`\ &\ :math:`L`\ &&\ :math:`L`\ &&\ :math:`(J`\ &&\ :math:`L)`\ &&\ :math:`L`\ &\ :math:`J`
      | S & S & &&&&&&&& S
      | S & Ó & &&&&&&&& S
      | Ó & S & &&?&&&&?&& Ó
      | Ó & Ó & &&?&&&&?&& Ó

Hér tákna auðu línurnar línur sem við munum láta eiga sig hér eftir (þar
sem við vitum að þær eru ekki slæmar) og spurningamerkin tákna línur sem
við þurfum að skoða betur.

Það er auðvelt að kanna dálkinn þar sem „\ :math:`\enot L`\ “ kemur
fyrir og því gerum við það næst:

.. container:: center

   .. container:: tabular

      | c c|d e e e e f \|d f|c
        :math:`J`\ &\ :math:`L`\ &&\ :math:`L`\ &&\ :math:`(J`\ &&\ :math:`L)`\ &&\ :math:`L`\ &\ :math:`J`
      | S & S & &&&&&&&& S
      | S & Ó & &&&&&&&& S
      | Ó & S & &&&&&&Ó&& Ó
      | Ó & Ó & &&?&&&&S&& Ó

Við sjáum að lína þrjú er ekki slæm, því einhver forsenda er ósönn í
henni og því þurfum við ekki að skoða hana frekar. Loks klárum við
sanntöfluna með að fylla út línu fjögur:

.. container:: center

   .. container:: tabular

      | c c|d e e e e f \|d f|c
        :math:`J`\ &\ :math:`L`\ &&\ :math:`L`\ &&\ :math:`(J`\ &&\ :math:`L)`\ &&\ :math:`L`\ &\ :math:`J`
      | S & S & &&&&&&&& S
      | S & Ó & &&&&&&&& S
      | Ó & S & &&&&&&Ó& & Ó
      | Ó & Ó & S & & & & Ó & & S & & Ó

Það eru engar slæmar línur í þessari sanntöflu, engar línur þar sem
forsendurnar eru sannar en niðurstaðan ósönn. Rökfærslan er því gild.

Gagnsemi þessarar aðferðar sést kannski jafnvel enn betur ef við skoðum
rökfærslu með fleiri grunnsetningum. Til dæmis:

.. math:: A\eor B, \enot (B\eand C) \therefore (A \eor \enot C)

Við byrjum á því að skoða niðurstöðuna. Aðaltengið í henni er eða-tengi,
svo við getum flýtt fyrir með reglunum sem við kynntumst hér að ofan:

.. container:: center

   .. container:: tabular

      | c c c\| c|c|d e e f :math:`A` & :math:`B` & :math:`C` &
        :math:`A\eor B` & :math:`\enot (B \eand C)` & :math:`(A`
        &\ :math:`\eor`\ & :math:`\enot` & :math:`C)`
      | S & S & S & & & & & &
      | S & S & Ó & & & & & &
      | S & Ó & S & & & & & &
      | S & Ó & Ó & & & & & &
      | Ó & S & S & ? & ? & & &Ó &
      | Ó & S & Ó & & && & S&
      | Ó & Ó & S & ? & ? && & Ó&
      | Ó & Ó & Ó & & & & & S&

Við getum núna sleppt því að skoða allar nema þær tvær línur þar sem
niðurstaðan er ósönn. Með því að halda áfram, í samræmi við reglurnar
sem við höfum þegar séð, þá fáum við:

.. container:: center

   .. container:: tabular

      | c c c\| c|d e e f \|d e e f :math:`A` & :math:`B` & :math:`C` &
        :math:`A\eor B` &
        :math:`\enot (`\ &\ :math:`B`\ &\ :math:`\eand`\ &\ :math:`C)` &
        :math:`(A` &\ :math:`\eor`\ & :math:`\enot` & :math:`C)`
      | S & S & S & & &&& & & & &
      | S & S & Ó & & &&& & & & &
      | S & Ó & S & & &&& & & & &
      | S & Ó & Ó & & &&& & & & &
      | Ó & S & S & **S** & **Ó**\ &&S& & & &Ó &
      | Ó & S & Ó & &&& & && & S&
      | Ó & Ó & S & **Ó** & &&& & & & Ó&
      | Ó & Ó & Ó & &&&& && & S&

Hér eru engar línur þar sem niðurstöðurnar eru báðar sannar og
niðurstaðan ósönn. Niðurstöðuna leiðir því rökfræðilega af forsendunum.
Þessi sanntafla er mjög stór, en með því að nota reglurnar hér að ofan,
þá tókst okkur að komast hjá því að fylla út megnið af henni. Það hlýtur
að mega teljast vel af sér vikið.

Athugið hvort eftirfarandi setningar sú klifanir, mótsagnir eða hvorugt.
Styttið ykkur leið eins og lýst var hér að ofan.

.. container:: earg

   :math:`\enot B \eand B`

   :math:`\enot D \eor D`

   :math:`(A\eand B) \eor (B\eand A)`

   :math:`\enot[A \eif (B \eif A)]`

   :math:`A \eiff [A \eif (B \eand \enot B)]`

   :math:`\enot(A\eand B) \eiff A`

   :math:`A\eif(B\eor C)`

   :math:`(A \eand\enot A) \eif (B \eor C)`

   :math:`(B\eand D) \eiff [A \eiff(A \eor C)]`

.. _`s:PartialTruthTable`:

Ókláraðar sanntöflur
--------------------

Stundum er óþarfi að skoða hverja einustu línu í sanntöflu. Stundum er
nóg að vita hvað gerist á einni eða tveimur línum, til dæmis ef við
viljum vita hvort ákveðin sanngildadreifing er möguleg eða ekki. Við
getum sparað okkur mikla vinnu með því að reyna einfaldlega að „smíða“
slíkar sanngildadreifingar frá grunni. Í þessum hluta ætla ég að taka
nokkur dæmi um slíkt.

Klifanir.
         

Setning er klifun ef og aðeins ef hún er sönn fyrir allar
sanngildadreifingar. Það þýðir að við þurfum bara eina línu í sanntöflu
til að sýna að setning sé *ekki* klifun: við þurfum bara eina
sanngildadreifingu þar sem setningin er ósönn til að sýna að hún sé ekki
klifun. Það er því nóg að sýna eina línu í sanntöflunni þar sem
setningin er ósönn. Í stað þess að fylla út heila sanntöflu getum við
einfaldlega reynt að búa slíka sanngildadreifingu til. Ef það er hægt,
þá er setningin ekki klifun. Við köllum slíkt .

Segjum að við viljum sýna að setningin
:math:`(U \eand T) \eif (S \eand W)` sé *ekki* klifun. Við byrjum svona:

.. container:: center

   .. container:: tabular

      | c c c c \|d e e e e e f
        :math:`S`\ &\ :math:`T`\ &\ :math:`U`\ &\ :math:`W`\ &\ :math:`(U`\ &&\ :math:`T)`\ &&\ :math:`(S`\ &&\ :math:`W)`
      | & & & & & & && & &

Við höfum bara eina línu hér, þar sem við erum einungis að leita að
einni sanngildadreifingu þar sem setningin er ósönn. Við skrifum því
niður undir aðaltengið að setningin sé ósönn og reynum svo að fylla út
línuna. Ef við getum gert það, þá er setningin ekki klifun, en ef við
getum ekki gert það, þá er hún klifun.

Aðaltengi setningarinnar er skilyrðistengið. Skilyrðistengið er bara
ósatt ef forliðurinn er sannur og bakliðurinn er sannur. Við getum því
fyllt línuna út svona:

.. container:: center

   .. container:: tabular

      | c c c c \|d e e e e e f
        :math:`S`\ &\ :math:`T`\ &\ :math:`U`\ &\ :math:`W`\ &\ :math:`(U`\ &&\ :math:`T)`\ &&\ :math:`(S`\ &&\ :math:`W)`
      | & & & & & S & && & Ó &

Hlutasetningin :math:`(U\eand T)` er ekki sönn nema :math:`U` og
:math:`T` séu báðar sannar. Því höfum við:

.. container:: center

   .. container:: tabular

      | c c c c|d e e e e e f
        :math:`S`\ &\ :math:`T`\ &\ :math:`U`\ &\ :math:`W`\ &\ :math:`(U`\ &&\ :math:`T)`\ &&\ :math:`(S`\ &&\ :math:`W)`
      | & S & S & & S & S & S && & Ó &

Til þess að klára línuna þurfum við bara að :math:`(S\eand W)` sé ósönn.
Til þess er nóg að annað hvort :math:`S` eða :math:`W` séu ósannar, en
þær geta líka verið báðar ósannar. Það eina sem skiptir máli er að öll
setningin sé ósönn á þessari línu og hvaða leið við förum hér er okkar
eigin *ákvörðun*. Það skiptir ekki öllu máli hvað við veljum, svo við
tökum bara af skarið og klárum töfluna. Til dæmis svona:

.. container:: center

   .. container:: tabular

      | c c c c|d e e e e e f
        :math:`S`\ &\ :math:`T`\ &\ :math:`U`\ &\ :math:`W`\ &\ :math:`(U`\ &&\ :math:`T)`\ &&\ :math:`(S`\ &&\ :math:`W)`
      | Ó & S & S & Ó & S & S & S && Ó & Ó & Ó

Þetta er möguleg sanngildadreifing. Við höfum því sýnt að það sé til
sanngildadreifing þar sem :math:`(U \eand T) \eif (S \eand W)` er ósönn,
nefnilega sanngildadreifingin þar sem :math:`S` er ósönn, :math:`T`
sönn, :math:`U` sönn og :math:`W` ósönn. Við höfum því ókláraða
sanntöflu sem sýnir að :math:`(U \eand T) \eif (S \eand W)` sé ekki
klifun.

Þetta dæmi er auðvitað vel valið til að ganga upp. Ef setningin *hefði*
verið klifun, þá hefði ekki verið hægt að finna *neina*
sanngildadreifingu sem gerði setninguna *ósanna*. En hvernig lýsir það
sér við beitingu aðferðarinnar? Jú, við hefðum lent í því að þurfa að
setja bæði sanngildin á sömu grunnsetningu í töflunni, þ.e. við hefðum
verið nauðbeygð til að segja að einhver grunnsetning sé bæði sönn og
ósönn. En af því að grunnsetning getur bara haft eitt sanngildi, þá
sýnir það að slík sanngildadreifing er ekki til. Það sýnir þá að
setningin *gæti ekki* verið ósönn og þar með að hún væri klifun.

Hér er dæmi um einfalda klifun og hvernig aðferðin virkar ef ekki er til
nein sanngildadreifing sem gerir setninguna sanna:

.. container:: center

   .. container:: tabular

      | c|d c e e f
        :math:`P`\ &\ :math:`P`\ &\ :math:`\;\eor`\ &\ :math:`\enot`\ &\ :math:`P`
      | & & Ó & &

Við ætlum að reyna að sýna fram á að þessi setning sé *ekki* klifun og
byrjum þess vegna á að gefa okkur að öll setningin sé ósönn og skrifum
því „Ó“ undir aðaltengið. Þar sem við vitum að setning sem tengd er
saman með eða-tengi er aldrei ósönn nema báðar setningarnar sem mynda
hana séu ósannar, þá höfum við:

.. container:: center

   .. container:: tabular

      | c|d c e e f
        :math:`P`\ &\ :math:`P`\ &\ :math:`\;\eor`\ &\ :math:`\enot`\ &\ :math:`P`
      | Ó& Ó& Ó &Ó &

En fyrst :math:`\enot P` er aldrei ósönn nema „\ :math:`P`\ “ sé sönn,
þá þurfum við að setja „S“ undir grunnsetninguna :math:`P`—en þar erum
við nú þegar búin að setja „Ó“. Það er ekki leyfilegt og því ekki til
nein sanngildadreifing þar sem þessi setning er ósönn. Ef það er ekki
til nein sanngildadreifing þar sem þessi setning er ósönn, þá hlýtur hún
að vera sönn fyrir allar sanngildadreifingar—og þá er hún klifun.

Hér þurfum við þó að passa okkur: Ef við viljum sýna að engin
sanngildadreifing af ákveðnu tagi sé til og upp koma tveir möguleikar
við leitina (t.d. getur :math:`P \eand Q` verið ósönn ef :math:`P` er
ósönn *eða* :math:`Q` er ósönn), þá getum við ekki bara valið annan
hvorn möguleikann eins og að ofan. Það er vegna þess að ef við veldum
annan hvorn möguleikann og sýndum að hann gangi ekki upp, þá er alltaf
mögulegt að hinn geri það. Þess vegna þurfum við að bæta við línu, ef
þetta gerist: eina fyrir hvern möguleika.

Segjum sem dæmi að við viljum sýna að :math:`\enot(P \eand \enot P)` sé
klifun. Til að gera það, þurfum við að sýna að *enginn*
sanngildadreifing geri þessa setningu ósanna. Við byrjum á því að gera
setninguna ósanna, eins og áður:

.. container:: center

   .. container:: tabular

      | c|d e e e f :math:`P`\ &&\ :math:`(P`\ &&&\ :math:`P)`
      | & Ó& & & &

En við sjáum að þessi setning er ósönn ef :math:`P` er ósönn, eða ef
:math:`\enot P` er ósönn, þ.e. ef :math:`P` er sönn. Við þurfum því að
kanna tvo möguleika. Við byrjum á fyrstu línunni og gerum :math:`P`
ósanna þar:

.. container:: center

   .. container:: tabular

      | c|d e e e f :math:`P`\ &&\ :math:`(P`\ &&&\ :math:`P)`
      | Ó& Ó& & & &

En nú sjáum við að ef :math:`P` er ósönn, þá er :math:`P \eand \enot P`
ósönn, og þar með er :math:`\enot(P \eand \enot P)` sönn. En við höfðum
gefið okkur að :math:`\enot(P \eand \enot P)` væri ósönn og því þurfum
við að skrifa tvö sanngildi á sama stað í töflunni, og það er ekki hægt.
Þessi sanngildadreifing er því ekki möguleg. Við skrifum „X“ að sýna að
við höfum reynt að setja tvö sanngildi á sama stað:

.. container:: center

   .. container:: tabular

      | c|d e e e f :math:`P`\ &&\ :math:`(P`\ &&&\ :math:`P)`
      | Ó& X& Ó& Ó& S&Ó

Ef við reynum að gera :math:`P` satt, þá lendum við í sama vanda, því þá
er :math:`\enot P` ósönn:

.. container:: center

   .. container:: tabular

      | c|d e e e f :math:`P`\ &&\ :math:`(P`\ &&&\ :math:`P)`
      | Ó& X& Ó& Ó& S&Ó
      | S& X& S& Ó& Ó&S

Það er því ekki til nein sanngildadreifing sem gerir þessa setningu
ósanna og þess vegna hlýtur hún að vera klifun. Þetta er þó ekki nema
einfalt dæmi um hvernig við förum að ef tveir möguleikar koma upp, því
eins og glöggir lesendur hafa kannski tekið eftir, þá höfum við fyllt út
alla sanntöfluna við að beita þessari aðferð, og því enginn tími sem
sparaðist. En í flóknari dæmum, eins og við sjáum að neðan, getur oft
gegnt öðru máli.

Það er þó gott að hafa í huga að ef manni hugnast ekki að beita þessari
aðferð, þá er alltaf hægt að búa til fulla sanntöflu.

Mótsagnir.
          

Til að athuga hvort setning sé mótsögn eða ekki þarf heldur ekki heila
sanntöflu. Til þess að sýna að setning sé mótsögn þurfum við að sýna að
það sé engin sanngildadreifing til þar sem setningin er sönn. Til að
sýna að setning sé *ekki* mótsögn þurfum við að sýna að til sé að
minnsta kosti ein sanngildadreifing þar sem hún er sönn.

Byrjum á að skoða dæmi um setningu sem er ekki mótsögn. Við þurfum að
sýna að til sé sanngildadreifing þar sem setningin er sönn. Við getum
notað sama dæmi og að ofan, nema núna byrjum við á að skrifa að
setningin sé sönn undir aðaltenginu:

.. container:: center

   .. container:: tabular

      | c c c c|d e e e e e f
        :math:`S`\ &\ :math:`T`\ &\ :math:`U`\ &\ :math:`W`\ &\ :math:`(U`\ &&\ :math:`T)`\ &&\ :math:`(S`\ &&\ :math:`W)`
      | & & & & & & && & &

Til þess að setningin sé sönn, er nóg að forliðurinn sé ósannur,
samkvæmt skilgreiningarsanntöflunni fyrir skilyrðistengið. Forliðurinn
er svo samtenging og því nóg að einungis ein af setningunum sem mynda
hana sé ósönn. Við getum ráðið því sjálf hverja þeirra við veljum og
sett svo hvaða sanngildi sem er á hinar setningarnar. Segjum að
„\ :math:`U`\ “ sé ósönn. Þá fáum við:

.. container:: center

   .. container:: tabular

      | c c c c|d e e e e e f
        :math:`S`\ &\ :math:`T`\ &\ :math:`U`\ &\ :math:`W`\ &\ :math:`(U`\ &&\ :math:`T)`\ &&\ :math:`(S`\ &&\ :math:`W)`
      | & & Ó & & Ó & Ó & && & &

Nú getum við svo sett hvaða sanngildi sem við viljum á hinar
setningarnar og endum til dæmis með:

.. container:: center

   .. container:: tabular

      | c c c c|d e e e e e f
        :math:`S`\ &\ :math:`T`\ &\ :math:`U`\ &\ :math:`W`\ &\ :math:`(U`\ &&\ :math:`T)`\ &&\ :math:`(S`\ &&\ :math:`W)`
      | Ó & S & Ó & Ó & Ó & Ó & S && Ó & Ó & Ó

Þessi sanngildadreifing er þannig að setningin er sönn, og því getur hún
ekki verið mótsögn. En hvað ef setningin *hefði* verið mótsögn? Þá hefði
ekki verið til neinn sanngildadreifing þar sem hún er sönn. Þá hefðum
við ekki getað fyllt út línuna án þess að þurfa að setja bæði sanngildin
á einu og sömu grunnsetninguna. Þetta er alveg hliðstætt við dæmið hér
að ofan um klifanir.

Rökfræðilegt jafngildi.
                       

Til að sýna að tvær setningar séu ekki rökfræðilega jafngildar er nóg að
sýna að til sé a.m.k. ein sanngildadreifing þar sem þær hafa ólík
sanngildi. Til þess þurfum við bara eina línu: við látum eina vera sanna
og hina ósanna. Ef við getum klárað sanngildadreifinguna, þá eru
setningarnar rökfræðilega jafngildar.

En hvað ef setningar *eru* rökfræðilega jafngildar? Við gætum prófað að
gefa setningunum ólík sanngildi og fyllt út ókláraða sanntöflu: ef við
getum búið til slíka sanngildadreifingu, þá eru setningarnar ekki
rökfræðilega jafngildar. En rétt eins og að ofan er málið ekki alveg
svona einfalt.

Ef um er að ræða tvær setningar, :math:`\meta{A}` og :math:`\meta{B}`,
og við prófuðum að gefa :math:`\meta{A}` sanngildið „S“ og
:math:`\meta{B}` sanngildið „Ó“ og tækist svo ekki að fylla út línuna í
sanntöflunni, þá gætum við ekki dregið þá ályktun að :math:`\meta{A}` og
:math:`\meta{B}` hljóti að vera rökfræðilega jafngildar. Af hverju? Jú,
af því að þá hefðum við bara sýnt að ekki sé til sanngildadreifing þar
sem :math:`\meta{A}` er sönn en :math:`\meta{B}` ósönn. Hugsanlega væri
til sanngildadreifing þar sem :math:`\meta{B}` er sönn en
:math:`\meta{A}` ósönn. Hér þyrftum við því aftur tvær línur, eina fyrir
hvern möguleika.

Hér er dæmi:

.. container:: center

   .. container:: tabular

      | c c|d e e f \| d e f
        :math:`P`\ &\ :math:`Q`\ &\ :math:`\enot`\ &\ :math:`P\;`\ &&\ :math:`Q`\ &\ :math:`P`\ &&\ :math:`Q`
      | & & & & S & & & Ó &
      | & & & & Ó & & & S &

Við byrjum á því að gefa setningunum ólík sanngildi, fyrst þannig að
:math:`\enot P \eor Q` sé sönn en :math:`P \eif Q` ósönn, og svo öfugt.

Við byrjum á að fylla út efstu línuna: skilyrðissetning er bara ósönn ef
forliðurinn er sannur og bakliðurinn ósannur. Þá vitum við að :math:`P`
er sönn á þeirri línu og :math:`Q` ósönn. Þá höfum við:

.. container:: center

   .. container:: tabular

      | c c|d e e f \| d e f
        :math:`P`\ &\ :math:`Q`\ &\ :math:`\enot`\ &\ :math:`P\;`\ &&\ :math:`Q`\ &\ :math:`P`\ &&\ :math:`Q`
      | S & Ó & & S & S & Ó & S & Ó & Ó
      | & & & & Ó & & & S &

En :math:`\enot P` er ósönn ef :math:`P` er sönn og því þyrftum við að
setja „Ó“ í dálkinn undir „\ :math:`\enot`\ “. En þar verður að vera „S“
svo að :math:`\enot P \eor Q` sé sönn. Þessi sanngildadreifing er því
ekki möguleg. Við setjum aftur „X“ til að gefa það til kynna:

.. container:: center

   .. container:: tabular

      | c c|d e e f \| d e f
        :math:`P`\ &\ :math:`Q`\ &\ :math:`\enot`\ &\ :math:`P\;`\ &&\ :math:`Q`\ &\ :math:`P`\ &&\ :math:`Q`
      | S & Ó & X & S & S & Ó & S & Ó & Ó
      | & & & & Ó & & & S &

Við höldum svo áfram með hina línuna. Við vitum að
:math:`\enot P \eor Q` er bara ósönn ef báðar hlutasetningarnar eru
ósannar. Þá vitum við að :math:`Q` og :math:`\enot P` hljóta báðar að
vera ósannar. :math:`P` er því sönn. Þá höfum við:

.. container:: center

   .. container:: tabular

      | c c|d e e f \| d e f
        :math:`P`\ &\ :math:`Q`\ &\ :math:`\enot`\ &\ :math:`P\;`\ &&\ :math:`Q`\ &\ :math:`P`\ &&\ :math:`Q`
      | S & Ó & X & S & S & Ó & S & Ó & Ó
      | S & Ó & Ó & S & Ó & Ó & & S &

Núna vitum við hvaða sanngildi :math:`P` og :math:`Q` hljóta að hafa ef
:math:`\enot P \eor Q` er ósönn.

Ef við myndum svo halda áfram að fylla út línu tvö, þá myndum við sjá að
forliður skilyrðissetningarinnar hlýtur að vera sannur en bakliðurinn
ósannur. Því er skilyrðissetningin í heild ósönn, en af því að við gáfum
okkur að hún væri sönn, þá yrðum við að skrifa bæði sanngildin, satt og
ósatt, í dálkinn fyrir neðan skilyrðistengið. Það er ekki hægt, og því
er engin sanngildadreifing þar sem :math:`\enot P \eor Q` er ósönn en
:math:`P \eif Q` sönn. Við höfum því prófað báða möguleikana og sýnt að
ekki er til sanngildadreifing þar sem þessar tvær setningar hafa ólík
sanngildi, og því eru þær rökfræðilega jafngildar.

Það er þó gott að hafa í huga að manni ber engin skylda til að nota
þessa aðferð við að meta hvort tvær setningar séu rökfræðilega
jafngildar. Það er alltaf hægt að fylla út alla sanntöfluna og athuga
hvort þær hafi sama sanngildi í öllum línum.

Rökfræðileg samkvæmni.
                      

Til að sýna að setningar, tvær eða fleiri, séu rökfræðilega samkvæmar
hverri annarri þá þurfum við að sýna að til sé sanngildadreifing þar sem
þær eru allar sannar. Við gerum það með sama hætti og að ofan: við
setjum upp ókláraða sanntöflu þar sem allar setningarnar eru sannar og
fyllum hana út: ef okkur tekst það, þá eru þær samkvæmar, annars ekki.

Gildi/rökfræðileg afleiðing.
                            

Til að sýna að rökfærsla sé ógild er nóg að sýna að til sé
sanngildadreifing þar sem forsendurnar eru sannar en niðurstaðan ósönn.
Við getum því reynt að smíða slíka sanngildadreifingu með því að láta
forsendurnar vera allar sannar, en niðurstöðuna ósanna. Athugum hvort
:math:`Q, P \eif Q \therefore P` sé gild rökfærsla:

.. container:: center

   .. container:: tabular

      | c c|c\| d e f \| c
        :math:`P`\ &\ :math:`Q`\ &\ :math:`Q`\ &\ :math:`P`\ &&\ :math:`Q`\ &\ :math:`P`
      | & & S & &S & & Ó

Hér höfum við látið báðar forsendurnar vera sannar en niðurstöðuna
ósanna. Svo fyllum við línuna til samræmis og fáum:

.. container:: center

   .. container:: tabular

      | c c|c\| d e f \| c
        :math:`P`\ &\ :math:`Q`\ &\ :math:`Q`\ &\ :math:`P`\ &&\ :math:`Q`\ &\ :math:`P`
      | Ó & S & S & Ó & S & S & Ó

Hér er því komin sanngildadreifing þar sem forsendurnar eru báðar sannar
en niðurstaðan ósönn. Þetta er því ógild rökfærsla.

Til að sýna að rökfærsla sé *gild* þarf að sýna að *engin*
sanngildadreifing sé til þar sem niðurstöðurnar eru báðar sannar en
niðurstaðan ósönn. Við gerum þetta á nákvæmlega sama hátt og í hinum
dæmunum hér að ofan. Það er þó mikilvægt að hafa í huga að ef tveir
möguleikar eru í boði þegar við smíðum sanndreifinguna, þá verðum við að
hafa eina línu fyrir hvorn möguleika, rétt eins og talað var um hér að
ofan.

Hér er dæmi:

.. container:: center

   .. container:: tabular

      | c c c \| d d f \| d d d d d d f \| d d f
        :math:`P`\ &\ :math:`Q`\ &\ :math:`R`\ &\ :math:`P`\ &\ :math:`\eiff`\ &\ :math:`Q`\ &(:math:`Q`\ &\ :math:`\eand`\ &\ :math:`R`)&\ :math:`\eiff`\ &(:math:`P`\ &\ :math:`\eor`\ &\ :math:`R`)&\ :math:`Q`\ &\ :math:`\eiff`\ &\ :math:`R`
      | & & & & S & & & & & S & & & & & Ó &

Hér höfum við látið forsendurnar vera sannar en niðurstöðuna ósanna. En
engin frekari gildi í sanntöflunni eru ákvörðuð af því sem við höfum nú
þegar valið. Til dæmis er :math:`Q \eiff R` ósönn ef og aðeins ef báðir
liðir hafa mismunandi sanngildi. Við þurfum því að bæta við annarri
línu, einni fyrir hvorn möguleika. Við skrifum því tvær línur, eina þar
sem :math:`Q` er satt en :math:`R` ósatt, og svo öfugt:

.. container:: center

   .. container:: tabular

      | c c c \| d d f \| d d d d d d f \| d d f
        :math:`P`\ &\ :math:`Q`\ &\ :math:`R`\ &\ :math:`P`\ &\ :math:`\eiff`\ &\ :math:`Q`\ &(:math:`Q`\ &\ :math:`\eand`\ &\ :math:`R`)&\ :math:`\eiff`\ (&\ :math:`P`\ &\ :math:`\eor`\ &\ :math:`R`)&\ :math:`Q`\ &\ :math:`\eiff`\ &\ :math:`R`
      | & S & Ó & & S & & & & & S & & & & S & Ó & Ó
      | & Ó & S & & S & & & & & S & & & & Ó& Ó & S

Svo höldum við áfram að fylla út töfluna, sem er lítið mál, þar sem við
höfum nú þegar ákvarðað sanngildi tveggja af þremur grunnsetningum og
bara spurning um að afrita þau á rétta staði og halda áfram í samræmi
við skilgreiningarsanntöflurnar fyrir setningatengin:

.. container:: center

   .. container:: tabular

      | c c c \| d d f \| d d d d d d f \| d d f
        :math:`P`\ &\ :math:`Q`\ &\ :math:`R`\ &\ :math:`P`\ &\ :math:`\eiff`\ &\ :math:`Q`\ &(:math:`Q`\ &\ :math:`\eand`\ &\ :math:`R`)&\ :math:`\eiff`\ &(:math:`P`\ &\ :math:`\eor`\ &\ :math:`R`)&\ :math:`Q`\ &\ :math:`\eiff`\ &\ :math:`R`
      | S & S & Ó & S & S & S & S & & & S & S & & & S & Ó & Ó
      | Ó & Ó & S & Ó & S & Ó & Ó & & & S & Ó & & & Ó & Ó & S

Takið eftir því að sanngildið á :math:`P` ræðst af sanngildi :math:`Q`
og því að við höfum ákveðið að fremsta jafngildissetningin sé sönn.

Þegar hér er komið við sögu lendum við þó í vandræðum. Skoðum fyrst efri
línuna. Við vitum að :math:`R` hlýtur að vera ósönn þar, því niðurstaðan
er jafngildissetning og :math:`R` hefur því ekki sama sanngildi og
:math:`Q`, en sanngildi hennar vorum við þegar búin að ákvarða. Það
þýðir að :math:`Q \eand R` er ósönn og þar með vitum við að
:math:`P\eor R` hlýtur líka að vera ósönn (því jafngildissetningin er
sönn). En þá ætti :math:`P` líka að vera ósönn, en við vorum búin að
ákvarða að hún væri sönn. Þessi sanngildadreifing er því ekki möguleg.

Sömu sögu má segja um línu tvö: þar sem :math:`R` er satt, ætti
:math:`P \eor R` líka að vera satt. En þar sem :math:`Q` er ósatt hlýtur
:math:`Q \eand R` líka að vera ósatt og þá ætti öll jafngildissetningin
að vera ósönn. En við vorum búin að ákvarða að hún væri sönn. Þessi
sanngildadreifing er því heldur ekki möguleg. Við getum því ekki smíðað
*neina* sanngildadreifingu þar sem forsendurnar eru báðar sannar og
niðurstaðan ósönn, og því er samsvarandi rökfærsla *gild*.

Notið sanntöflur (fullar eða ókláraðar eftir hentisemi) til að ákvarða
hvort þessi setningapör séu rökfræðilega jafngild:

.. container:: earg

   :math:`A`, :math:`\enot A`

   :math:`A`, :math:`A \eor A`

   :math:`A\eif A`, :math:`A \eiff A`

   :math:`A \eor \enot B`, :math:`A\eif B`

   :math:`A \eand \enot A`, :math:`\enot B \eiff B`

   :math:`\enot(A \eand B)`, :math:`\enot A \eor \enot B`

   :math:`\enot(A \eif B)`, :math:`\enot A \eif \enot B`

   :math:`(A \eif B)`, :math:`(\enot B \eif \enot A)`

Notið sanntöflur (fullar eða ókláraðar eftir hentisemi) til að ákvarða
hvort setningarnar í hverri línu séu rökfræðilega samkvæmar eða
rökfræðilega ósamkvæmar:

.. container:: earg

   :math:`A \eand B`, :math:`C\eif \enot B`, :math:`C`

   :math:`A\eif B`, :math:`B\eif C`, :math:`A`, :math:`\enot C`

   :math:`A \eor B`, :math:`B\eor C`, :math:`C\eif \enot A`

   :math:`A`, :math:`B`, :math:`C`, :math:`\enot D`, :math:`\enot E`,
   :math:`F`

Notið sanntöflur (fullar eða ókláraðar eftir hentisemi) til að ákvarða
hvort þessar rökfærslur séu gildar eða ógildar:

.. container:: earg

   :math:`A\eor\bigl[A\eif(A\eiff A)\bigr] \therefore A`

   :math:`A\eiff\enot(B\eiff A) \therefore A`

   :math:`A\eif B, B \therefore A`

   :math:`A\eor B, B\eor C, \enot B \therefore A \eand C`

   :math:`A\eiff B, B\eiff C \therefore A\eiff C`

.. [1]
   Dorothy Edgington, „Conditionals, 2014, í *Stanford Encyclopedia of
   Philosophy* (http://plato.stanford.edu/entries/conditionals/).

.. [2]
   Munið að í §\ \ `[s:UseMention] <#s:UseMention>`__ notuðum við
   „\ \ :math:`\therefore`\ \ “ til að gefa til kynna hvaða setningar
   eru forsendur og hvaða setning er niðurstaða. Án þessa tákns, þá
   hefðum við þurft að skrifa í boxinu hér að ofan: Ef :math:`\meta{B}`
   leiðir rökfræðilega af
   :math:`\meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n`, þá er rökfærslan
   sem hefur :math:`\meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n` sem
   forsendur og :math:`\meta{B}` sem niðurstöðu gild.
