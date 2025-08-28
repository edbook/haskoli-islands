.. _ch.NDTFL:

Náttúruleg afleiðsla fyrir setningarökfræði
===========================================

.. _`s:NDVeryIdea`:

Hugmyndin á bakvið náttúrulega afleiðslu
----------------------------------------

Í kafla §\ `[s:Valid] <#s:Valid>`__ sögðum við að rökfærsla væri gild
eff það er ómögulegt fyrir allar forsendur hennar að vera sannar en
niðurstöðuna ósanna.

Með því að nota sanntöflur höfðum við svo í höndunum aðferð til að meta
hvort rökfærsla sé gild. Við getum þýtt rökfærsluna yfir á mál
setningarökfræði og fyllum út sanntöflu: ef til er sanngildadreifing þar
sem niðurstöðurnar eru allar sannar en niðurstaðan ósönn, þá er
rökfærslan ekki gild.

En oft veita sanntöflur litla innsýn í eðli rökfærslunnar sem um ræðir.
Tökum tvö dæmi um rökfærslur á máli setningarökfræði:

.. math::

   \begin{aligned}
   P \eor Q, \enot P & \therefore Q\\
   P \eif Q, P & \therefore Q
   \end{aligned}

Þetta eru greinilega gildar rökfærslur. Við getum staðfest það með að
fylla út sanntöflur. En það segir okkur lítið um það *hvers vegna*
þessar rökfærslur eru gildar—um *form* þeirra.

Markmið náttúrulegrar afleiðslu er að sýna að rökfærslur séu gildar án
þess að glata þessari innsýn í það hvers vegna rökfærslurnar eru gildar.
Grunnhugmyndin á bak við sannanir er þessi: við byrjum með einhverjar
setningar sem við vitum að eru sannar (eða gefum okkur að séu sannar),
nefnilega forsendurnar, notum svo reglur sem við vitum að eru góðar til
að breyta setningunum sem við byrjuðum með í aðrar setningar, sem við
vitum þá að eru líka sannar, og svo áfram þangað til við komum að
niðurstöðunni. Af því að við vitum að reglurnar eru góðar, þá vitum við
að niðurstaðan er líka sönn.

Við veljum svo þessar reglur þannig að þær endurspegli, að svo miklu
leyti sem hægt er, hvernig við setjum rökfærslur fram í mæltu máli.

*Þetta er allt önnur sýn á rökfærslur en við höfum séð hingað til*. Við
notum sanntöflur til að skoða með beinum hætti hvernig setningar eru
sannar eða ósannar. Við kölluðum þetta *merkingarfræðilega* aðferð við
að meta rökfærslur. Sannanir í setningarökfræði eiga hins vegar mun
meira sameiginlegt með myndunarreglunum sem við notuðum til að ákvarða
hvaða táknrunur eru leyfilegar sem setningar í setningarökfræði og
hverjar ekki: sannanir eru aðferð við að meta rökfærslur. Það þýðir að
sannanir snúast bara um *form* setninganna, en ekki merkingu þeirra eða
sannleiksgildi grunnsetninganna sem koma fyrir í þeim. Við munum sjá
hvað það merkir um leið og við kynnum reglurnar sjálfar til sögunnar.

Það eru þó fleiri ástæður en þær sem nefndar voru hér að ofan til að
nota sannanir til að meta rökfærslur. Í raun er það oft *nauðsynlegt*.
Skoðum til dæmis eftirfarandi rökfærslu:

.. math:: A_1 \eif C_1 \therefore (A_1 \eand A_2 \eand A_3 \eand A_4 \eand A_5) \eif (C_1 \eor C_2 \eor C_3 \eor C_4 \eor C_5)

Til að athuga hvort þessi rökfærsla sé gild með fullri sanntöflu þarf
töflu sem er 1024 línur. Ef hún er fyllt rétt út, sem er alls ekki
sjálfgefið þegar um er að ræða svona stóra töflu, þá myndum við sjá að
það eru engar línur þar sem forsendurnar eru allar sannar en niðurstaðan
ósönn. Við myndum því vita að rökfærslan er gild.

En skoðum nú þessa rökfærslu:

.. math::

   \begin{aligned}
   A_1 \eif C_1 \therefore {}& (A_1 \eand A_2 \eand A_3 \eand A_4 \eand A_5 \eand A_6 \eand A_7 \eand A_8 \eand A_9 \eand A_{10}) \eif \phantom{(}\\
   &(C_1 \eor C_2 \eor C_3 \eor C_4 \eor C_5 \eor C_6 \eor C_7 \eor C_8 \eor C_9 \eor C_{10})
   \end{aligned}

Þessi rökfærsla er líka gild—og það af svipuðum ástæðum og sú hér að
ofan—en til að kanna það með sanntöflu þyrftum við
:math:`2^{20} = 1048576` línur. 21 grunnsetning þyrfti svo
:math:`2^{21} = 2097152` línur, o.s.frv. Það væri auðvitað alltaf hægt
að forrita tölvu til að fylla út hverja línu og skila svo niðurstöðu að
lokum, en jafnvel það verður fljótt óviðráðanlegt (ef það tekur tölvuna
0,01 sekúndu að fylla út hverja línu, þá tæki það 6 klukkutíma að fylla
út sanntöfluna. Það þýðir að það tæki tölvuna meira en 12 milljarða ára
að fylla út sanntöflu með 64 grunnsetningum!). Í praxís geta flóknar
rökfærslur því fljótlega orðið illviðráðanlegar.

Það eru svo frekari ástæður fyrir mikilvægi sannanna sem við munum
fjalla um þegar við komum að umsagnarökfræði í næsta hluta bókarinnar.

.. _`s:BasicTFL`:

Grunnreglur náttúrulegrar afleiðslu fyrir setningarökfræði
----------------------------------------------------------

Nú munum við kynna til sögunnar. Fyrir hvert setningatengi munum við
skilgreina , sem skiptast í sem gera okkur kleift að *innleiða* setningu
í sönnunina okkar sem hefur það setningatengi sem aðaltengi og sem gerir
það mögulegt að losna við setningu sem hefur það tengi sem aðaltengi.

Formlegar sannanir
~~~~~~~~~~~~~~~~~~

Við segjum að *formleg sönnun* sé runa af setningum, þar sem einhverjar
þeirra (eða engin) eru forsendur. Síðasta setningin í sönnuninni er
niðurstaðan. (Við munum einfaldlega tala um „sannanir“ héðan af, en það
er ágætt að hafa í huga að það eru líka til *óformlegar* sannanir).

Segjum að við höfum eftirfarandi rökfærslu og viljum sanna að hún sé
gild:

.. math:: \enot (A \eor B) \therefore \enot A \eand \enot B

Við byrjum sönnunina á því að skrifa forsenduna:

.. container:: proof

   *Proof.* ◻

Takið fyrst eftir því að við höfum númerað forsenduna vinstra megin í
því skyni að geta vísað í hana seinna. Raunar er *hver einasta* lína í
sönnun númeruð.

Takið líka eftir línunni sem dregin er undir forsenduna. Við notum þessa
línu til að *aðskilja* forsendurnar frá restinni af sönnuninni. Allt
fyrir ofan þessa línu er forsenda (þær geta verið fleiri en ein, eins og
við munum sjá) og allt fyrir neðan hana er annað hvort svokölluð
*aukaforsenda* (meira um þær innan skamms) eða leiðir af forsendunum
samkvæmt einhverri reglu.

Við viljum sanna að :math:`\enot A \eand \enot B`, svo við viljum að
síðasta línan í sönnuninni líti svona út:

.. container:: proof

   *Proof.* ◻

þar sem :math:`n` stendur fyrir númer línunnar. Það skiptir okkur ekki
máli hvaða tala kemur í stað :math:`n`, þó að við kjósum auðvitað heldur
stutta sönnun en langa.

Hér er annað dæmi. Segjum að við viljum athuga hvort eftirfarandi
rökfærsla sé gild:

.. math:: A\eor B, \enot (A\eand C), \enot (B \eand \enot D) \therefore \enot C\eor D

Þessi rökfærsla hefur þrjár forsendur, svo við skrifum þær allar niður í
röð, hverja á eftir annarri, númerum línurnar og drögum línu undir þær:

.. container:: proof

   *Proof.* ◻

Í þetta skiptið viljum við enda á línu sem lítur svona út:

.. container:: proof

   *Proof.* ◻

Við notum svo reglur til að leiða okkur frá forsendunum til
niðurstöðunnar. Við flokkum þessar reglur að mestu eftir
setningatengjum. Í því sem eftir er af þessum kafla munum við fara yfir
þessar reglur og það mun gera okkur kleift að fylla út það sem kemur á
milli forsendanna og niðurstöðunnar í svona sönnunum.

Og-tengi
~~~~~~~~

Við byrjum á innleiðingarreglunni fyrir og-tengið. Segjum að ég vilji
sýna að Jón sé hvort tveggja, sniðugur og snjall. Ein leið væri að sýna
fyrst að Jón sé sniðugur og svo að sýna að Jón sé snjall. Það myndi sýna
að Jón sé sniðugur og snjall.

Náttúruleg afleiðsla reynir að herma eftir þessu. Segjum að ég hafi
eftirfarandi þýðingarlykil:

.. container:: ekey

   Jón er sniðugur.

   Jón er snjall.

Hver lína í sönnun er, eins og áður sagði, annað hvort forsenda eða
leiðir af einhverri forsendu samkvæmt reglum náttúrulegrar afleiðslu.
Segjum að ég hafi þegar sannað :math:`S_1` á línu 8 og :math:`S_2` á
línu 15. Með því að nota innleiðingarregluna fyrir og-tengið, þá get ég
skrifað á nýja línu fyrir neðan: :math:`S_1 \eand S_2`:

.. container:: proof

   *Proof.* ◻

Við skrifum „\ :math:`\eand`\ I 8, 15“ til að gefa til kynna að
innleiðingarreglan fyrir og-tengið hafi verið notuð með línum 8 og 15.
Við segjum að línan sé þar með *réttlætt* með þeirri reglu. Hver einasta
lína í sönnun er annað hvort forsenda eða réttlætt með einhverri reglu
og sönnunin er *ekki* rétt mynduð nema við merkjum línuna með þessum
hætti. Þrípunktarnir sýna svo að einhverjar ótilgreindar línur eru á
milli línu 8 og línu 15.

Við hefðum líka getað skrifað „\ :math:`\eand`\ I 15, 8“ til að gefa til
kynna að lína 15 hafi verið notuð fyrst, og svo lína 8. Þá hefði röð
setninganna í samtengingunni breyst:

.. container:: proof

   *Proof.* ◻

En þetta eru bara dæmi. Almennt form innleiðingarreglunnar fyrir
og-tengið lítur svona út: Hvað á ég við með *almennt form*? Með því á ég
við að reglan sjálf er *ekki* sönnun. :math:`\meta{A}` og
:math:`\meta{B}` eru ekki setningar í setningarökfræði, heldur tákn sem
við notum í framsetningarmálinu til að tala *um* hvaða setningu sem er á
táknmáli setningarökfræði (sjá §\ `[s:UseMention] <#s:UseMention>`__).
Form reglunnar nær því yfir hvaða setningar sem er og hvaða röð á þeim
sem er.

:math:`n` og :math:`m` eru þess vegna líka tákn í framsetningarmálinu og
standa fyrir tölurnar sem við notum til að númera línur í sönnun. Í
raunverulegri sönnun myndu línurnar vera númeraðar með raunverulegum
tölum, :math:`1`, :math:`2`, :math:`3`, og svo framvegis, en þegar við
skilgreinum regluna verðum við að nota tákn sem geta staðið fyrir hvaða
tölu sem er, því við viljum að hægt sé að beita reglunni hvenær sem er í
sönnun.

Við gerum *ekki* ráð fyrir að línurnar tvær, *m* og *n*, þurfi að vera
hlið við hlið og því geta komið eins margar línur og verða vill á milli
:math:`\meta{A}`, :math:`\meta{B}` og svo
:math:`\meta{A} \eand \meta{B}`.

Nú getum við loksins séð fulla sönnun, þó einföld sé. Segjum að við
höfum rökfærslu á þessu formi:

.. math:: A, B \therefore A \eand B

\ Full sönnun á henni lítur svona út:

.. container:: proof

   *Proof.* ◻

Fyrst skrifum við forsendurnar niður, eina í hverri línu, og strikum svo
línu undir þær. Því næst notum við innleiðingarregluna fyrir og-tengið
og fáum :math:`A \eand B`. Við skrifum svo „\ :math:`\eand`\ I 1, 2“ við
línu 3 til að gefa til kynna að sú lína hafi verið fengin með því að
nota innleiðingarregluna fyrir og-tengið á línur 1 og 2.

Þessi regla er kölluð „innleiðingarregla fyrir og-tengið“ (eða
„og-innleiðingarregla“) af því hún bætir við nýju og-tengi
(„\ :math:`\eand`\ “) í sönnunina. Eftir að við höfum beitt reglunni eru
fleiri og-tengi í sönnuninni en áður.

En við höfum líka reglu sem *fækkar* og-tengjum. Við köllum hana
„eyðingarreglu fyrir og-tengið“ (eða „og-eyðingarreglu“). Segjum að við
vitum að Jón sé sniðugur og snjall. Ef svo er, þá getum við dregið þá
ályktun að Jón sé sniðugur. Við getum líka dregið þá ályktun að Jón sé
snjall.

Eyðingarreglan fyrir og-tengið er því í raun tvær reglur. Almennt form
þeirra er:

og: Þessar reglur segja að ef við höfum samtengingu á einhverri línu í
sönnun, þá getum við notað E til þess að fá annan hvorn liðinn sem
samtengingin samanstendur úr. Við þurfum tvær reglur, því ef við hefðum
bara aðra þeirra, þá gætum við bara fengið annan liðinn, en ekki hvorn
þeirra sem er. Það er þó mikilvægt að hafa í huga að þessi regla gildir
*bara* um aðaltengið í setningunni. Við getum til dæmis *ekki* dregið þá
ályktun að :math:`D` ef við höfum :math:`C \eor (D \eand E)`! Hér er
„\ :math:`\eor`\ “ aðaltengið og aðrar reglur gilda um það. Reglurnar
horfa bara til *forms* setninganna og setningin
:math:`C \eor (D \eand E)` hefur formið :math:`\meta{A} \eor \meta{B}`.
Til að beita eyðingarreglunni fyrir :math:`\eand` þarf setningin hins
vegar að vera á forminu :math:`\meta{A} \eand \meta{B}`.

Þó að við höfum enn sem komið er bara kynnt til sögunnar tvær reglur, þá
getum við strax séð hvaða kraftur býr í formlegum sönnunum. Tökum sem
dæmi eftirfarandi rökfærslu:

.. container:: earg

   :math:`[(A\eor B)\eif(C\eor D)] \eand [(E \eor F) \eif (G\eor H)]`

   :math:`[(E \eor F) \eif (G\eor H)] \eand [(A\eor B)\eif(C\eor D)]`

Hér hafa bæði forsendan og niðurstaðan og-tengi sem aðaltengi. Takið
líka eftir því að fyrri liðurinn í forsendunni er seinni liðurinn í
niðurstöðunni, og öfugt.

Til að sanna að þessi rökfærsla sé gild, þá byrjum á því að skrifa niður
forsenduna og drögum línu undir hana. Allt sem kemur á eftir þessari
línu verður að leiða af forsendunum í samræmi við ályktunarreglurnar sem
við höfum kynnt til sögunnar. Fyrsta línan í sönnuninni lítur því svona
út:

.. container:: proof

   *Proof.* ◻

Við getum núna notað og-eyðingarregluna til að taka forsenduna í sundur
og fengið hvorn lið samtengingarinnar í sitthvoru lagi:

.. container:: proof

   *Proof.* æab æab ◻

Við getum svo notað innleiðingarregluna fyrir og-tengi á línur 3 og 2 (í
þeirri röð) og fengið rétta niðurstöðu. Fullkláruð lítur sönnunin svona
út:

.. container:: proof

   *Proof.* æab æab ◻

Þetta er mjög einföld sönnun, en hún sýnir þó hvernig við getum ofið
margar mismunandi ályktunarreglur saman til að mynda flóknar sannanir.
Það er vert að taka eftir því að þessi sönnun er bara fjórar línur.
Setningarnar innihalda hins vegar samtals átta grunnsetningar, og því
yrði full sanntafla sem sýnir að þessi rökfærsla sé gild í heildina 256
línur. Það munar um minna.

Skoðum annað dæmi. Í
§\ `[s:MoreBracketingConventions] <#s:MoreBracketingConventions>`__
sögðum við að þessi rökfærsla væri gild:

.. math:: A \eand (B \eand C) \therefore (A \eand B) \eand C

Til að sanna hana, þá byrjum við á að skrifa forsenduna undirstrikaða í
fyrstu línuna:

.. container:: proof

   *Proof.* ◻

Forsendan er samtenging sem samanstendur af tveimur liðum, :math:`A` og
:math:`B \eand C`. Við getum fengið sitthvorn þeirra með að beita
:math:`\eand`\ E tvisvar. Við getum svo fengið hvorn lið í
:math:`B \eand C` með því að gera það sama aftur. Þá höfum við:

.. container:: proof

   *Proof.* æab æab æbc æbc ◻

Nú getum við svo notað innleiðingarregluna til að setja
grunnsetningarnar saman í þeirri röð sem við viljum. Sönnunin lítur því
svona út:

.. container:: proof

   *Proof.* æabc æabc æbc æbc ◻

Munið að samkvæmt myndunarreglunum fyrir setningar í setningarökfræði
eru strangt til tekið einungis samtengingar með tveimur liðum leyfðar.
Þegar við fjölluðum um merkingarfræðileg hugtök, þá leyfðum við okkur þó
að sleppa innri svigum í löngum samtengingum með þeim rökum að röð
sviganna hefði engin áhrif á sanntöflu setninganna. Þessi sönnun bendir
til þess að við gætum gert slíkt hið sama þegar kemur að sönnunum. En
þetta er ekki venja og því munum við ekki gera það. Við munum fylgja
ströngustu svigareglum þegar vinnum með sannanir. Undantekningin á því
er að við munum leyfa okkur að sleppa *ystu* svigum, en bara þeim.

Skoðum eitt dæmi að lokum. Þegar við notum :math:`\eand`\ I er ekkert
sem kemur í veg fyrir að við notum hana tvisvar á sömu línu. Við getum
því formlega sannað :math:`A` að því gefnu að :math:`A`, ef við viljum.
Sönnunin liti svona út:

.. container:: proof

   *Proof.* æaa ◻

Það mun koma í ljós síðar hvers vegna við viljum geta gert þetta. Þessi
sönnun sýnir þó vel formlegt eðli sannanna. Ef við hefðum ekki getað
beitt :math:`\eand I` hér, þá hefðum við einfaldlega ekki getað sannað
:math:`A \therefore A`, eins og augljóst og það annars er. Það hefði
ekki verið nein leið til að nota forsenduna til að búa til niðurstöðu.

Skilyrðistengi
~~~~~~~~~~~~~~

Skoðum eftirfarandi rökfærslu:

   Ef Anna er snjöll, þá er hún sniðug. Anna er snjöll. Þar af leiðandi
   er Anna sniðug.

Þessi rökfærsla er sannarlega gild. Hún samsvarar eyðingarreglunni fyrir
skilyrðistengið (:math:`\eif`\ E). Almennt form hennar er svona: Þessi
regla er oft kölluð *modus ponens* og við munum oft vísa til hennar með
því nafni. Þetta er eyðingarregla þar sem hún byrjar með setningu þar
sem :math:`\eif` er aðaltengi og fær úr henni setningu þar sem
:math:`\eif` er ekki aðaltengi. Takið eftir því að form reglunnar krefst
þess ekki að for- og bakliðirnir komi fyrir á línum hverri á eftir
annarri, né að þeir verði að koma fyrir í einhverri sérstakri röð. Þegar
við vísum í regluna, þá vísum við þó alltaf fyrst í skilyrðissetninguna
og svo í forliðinn.

Ef við látum :math:`S_1` standa fyrir „Anna er snjöll“ og :math:`S_2`
standa fyrir „Anna er sniðug“, þá liti full sönnun fyrir rökfærsluna hér
að ofan svona út:

.. container:: proof

   *Proof.* ◻

Við þurfum líka innleiðingarreglu fyrir skilyrðistengið. Eftirfarandi
rökfærsla ætti að vera gild:

   Anna er sniðug. Því gildir: ef Anna er snjöll, þá er Anna sniðug og
   snjöll.

Ef einhver drægi gildi þessarar rökfærslu í efa, þá gætum við reynt að
sannfæra viðkomandi svona:

   Gerum ráð fyrir að Anna sé sniðug. Gerum svo *að auki* ráð fyrir að
   Anna sé snjöll. Með og-innleiðingarreglu getum við þá dregið þá
   ályktun að Anna sé bæði sniðug og snjöll. Að þeirri aukaforsendu
   gefinni, að Anna sé snjöll, þá er Anna því bæði sniðug og snjöll. En
   það er bara það sama og að segja að *ef* Anna er snjöll, þá er Anna
   bæði sniðug og snjöll.

Hér höfum við kynnt til sögunnar hugmyndina um . Þær eru forsendur sem
við gefum okkur tímabundið í því skyni að leiða út einhverja aðra
setningu. Í réttlætingu okkar fyrir rökfærsluna hér að ofan notfærðum
við okkur aukaforsendu—við gáfum okkur að Anna væri snjöll sem
aukaforsendu og notuðum hana til að sýna að *ef* Anna er snjöll, þá er
hún bæði sniðug og snjöll.

Við þurfum því einhverja leið til að tjá þessa hugmynd um aukaforsendur
í náttúrulegri afleiðslu. Við gerum það svona. Við byrjuðum með eina
forsendu, að Anna sé sniðug. Við skrifum hana eins og venjulega, svona:

.. container:: proof

   *Proof.* ◻

Næst gáfum við okkur að Anna væri snjöll sem aukaforsendu. Til að gefa
það til kynna höldum við svona áfram:

.. container:: proof

   *Proof.* ◻

Við höfum þó *alls ekki* sannað að lína 2 leiði af línu 1. Við þurfum
því ekki að skrifa neina réttlætingu fyrir þessari línu til hliðar. Við
þurfum hins vegar að sýna að um aukaforsendu sé að ræða og við gerum það
með að draga línu til hliðar við og undir hana, auk þess að skrifa hana
örlítið til hliðar.

Nú getum við notað aukaforsenduna, rétt eins og um venjulega forsendu
væri að ræða (þó með skilyrðum sem við komum að síðar):

.. container:: proof

   *Proof.* ◻

Við höfum því sýnt, að aukaforsendunni :math:`S_2` gefinni, að
:math:`S_1 \eand S_2`. Við getum þess vegna dregið þá ályktun að ef
:math:`S_2` er satt, þá er :math:`S_1 \eand S_2` líka satt. Eða
einfaldlega, að :math:`S_2 \eif (S_1 \eand S_2)` sé satt:

.. container:: proof

   *Proof.* ◻

Takið eftir því að við skrifum aftur bara eina lóðrétta línu í sönnunni.
Við segjum að aukaforsendan :math:`S_2` hafi verið *losuð*, þar eð
skilyrðissetninguna leiðir bara af upprunalegu forsendunni, :math:`S_1`.

Þegar við sönnum skilyrðissetningu, þá gefum við okkur fyrst forliðinn
sem aukaforsendu, :math:`\meta{A}`, og notum hana til að sanna
bakliðinn, :math:`\meta{B}`. Ef það tekst, þá vitum við að ef
:math:`\meta{A}`, þá :math:`\meta{B}`. Almennt form reglunnar er því
svona: Það geta verið eins margar línur og verða vill milli :math:`i` og
:math:`j`.

Það er hjálplegt að skoða annað dæmi um það hvernig :math:`\eif`\ I
virkar. Sönnum að eftirfarandi rökfærsla sé gild:

.. math:: P \eif Q, Q \eif R \therefore P \eif R

Við byrjum á að skrifa niður *báðar* forsendurnar. Þar sem við viljum
sanna skilyrðissetningu (nefnilega :math:`P \eif R`), þá gefum við okkur
því næst forliðinn sem aukaforsendu. Sönnunin byrjar því svona:

.. container:: proof

   *Proof.* ◻

Nú þegar við höfum gefið okkur :math:`P` sem aukaforsendu, þá getum við
notað hana í sönnuninni. Við getum því notað E á fyrstu forsenduna. Það
gefur okkur :math:`Q`, sem við getum svo notað með E á aðra forsenduna.
Með því að gefa okkur :math:`P` gátum við því leitt út :math:`R`. Þá
getum við beitt I og losað aukaforsenduna :math:`P` og þar með klárað
sönnunina. Sönnunin lítur því svona út:

.. container:: proof

   *Proof.* ◻

Það er þess virði að skoða þessa sönnun mjög vel.

Aukaforsendur og hlutasannanir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Innleiðingarreglan fyrir skilyrðistengið byggðist á þeirri hugmynd að
nota aukaforsendur. Þær þarf að meðhöndla af nokkurri gætni, auk þess
sem skilningur á þeim er algjört grundvallaratriði þegar kemur að því að
ná tökum á formlegum sönnunum í rökfræði. Þess vegna ætla ég að segja
nokkur orð í viðbót um þær hér, auk þess að taka fleiri dæmi.

Skoðum eftirfarandi sönnun:

.. container:: proof

   *Proof.* æbb ◻

Þetta er fullkomlega í samræmi við þær reglur sem við höfum nú þegar
kynnst. Niðurstaðan ætti heldur ekki að koma neitt sérstaklega á óvart.
„\ :math:`B\eif B`\ “ er jú klifun og því ætti ekki að þurfa neinar
forsendur til að sanna hana.

En hvað ef við héldum áfram líkt og hér að neðan?

.. container:: proof

   *Proof.* æbb ◻

Ef þetta væri leyfilegt, þá væri það stórslys: við gætum sannað hvaða
setningu sem er, sama hvaða forsendu við gæfum okkur! Ef þú segðir mér
að Anna sé snjall rökfræðingur („\ :math:`A`\ “), þá ætti ég ekki að
geta dregið þá ályktun að Bjössi sé 100 metra hár („\ :math:`B`\ “).
Eitthvað hlýtur að hafa farið úrskeiðis og því hlýtur að þurfa einhverja
reglu sem bannar ályktanir á borð við þessa.

Í því skyni kynnum við til sögunnar : þær eru sannanir sem eiga sér stað
innan annarrar sönnunar. Hlutasönnun hefst á aukaforsendu og er afmörkuð
frá aðalsönnuninni með lóðréttri línu, rétt eins og við sáum að ofan.
Við getum hugsað okkur að hlutasönnun svari þeirri spurningu, *hvað
annað getum við sannað, ef við gefum okkur þetta sem aukaforsendu?*

Þegar við höfum opnað hlutasönnun, þá getum við ekki bara notað
aukaforsenduna sem við gáfum okkur, heldur líka allar þær forsendur sem
voru hluti af aðalsönnuninni, auk alls sem við höfum leitt af þeim. Við
segjum að þær línur sem eru fyrir ofan hlutasönnunina séu enn *í gildi*.
En það kemur að því að við viljum hætta að nota aukaforsenduna sem við
gáfum okkur og snúa aftur til aðalsönnunarinnar. Til að gefa það til
kynna, þá hættum við að draga lóðréttu línuna sem afmarkar
hlutasönnunina. Þá segjum við að hlutasönnuninni hafi verið . Þegar við
lokum hlutasönnun, þá hættum við að nota aukaforsenduna sem við gáfum
okkur þegar við hófum hlutasönnunina og getum því ekki lengur notað
hana, né það sem leiddi af henni.

Við segjum því að:

Þessi regla útilokar sönnunina hér að ofan. Eyðingarreglan fyrir
skilyrðistengi segir að við þurfum tvær línur sem koma fyrir fyrr í
sönnuninni. Í þessari meintu sönnun hér að ofan, þá kom ein þessara lína
fyrir innan hlutasönnunar (lína 4) sem hafði verið lokað þegar vísað var
í hana (lína 6). Þetta er óleyfilegt.

Þegar við lokum hlutasönnun, segjum við að aukaforsendan sem hún hófst á
hafi verið . Við getum því orðað ofangreint svona: *það er ekki
leyfilegt að vísa í línur sem reiða sig á losaðar aukaforsendur*.

Hlutasannanir leyfa okkur því að hugsa um hvað við gætum sannað, ef við
myndum gefa okkur einhverja nýja forsendu. Ef við getum lokað þeim, með
því að vísa í einhverja reglu sem þarfnast hlutasönnunnar, forms síns
vegna, rétt eins og innleiðingarreglan fyrir skilyrðistengi gerir, þá
hefur okkur tekist að leiða út eitthvað nýtt í aðalsönnuninni. En eins
og ofangreint sýnir, þá þurfum við að fylgjast vel með því hvaða
aukaforsendur við höfum gefið okkur á hverju stigi sönnunarinnar.
Náttúruleg afleiðsla gerir þetta á *myndrænan* hátt (og það er raunar
ástæðan fyrir því að hún hentar okkur vel).

Það er ekkert sem stoppar okkur í að opna nýja hlutasönnun innan
annarrar hlutasönnunar, svo framarlega sem við fylgjum reglunni hér að
ofan. Hér er dæmi:

.. container:: proof

   *Proof.* ◻

Takið eftir því að vísunin í línu 4 vísar í upprunalegu forsenduna (á
línu 1) og aukaforsendu sem kemur fyrir í hlutasönnun (á línu 2). Þetta
er í góðu lagi, því hvorug forsendanna hefur verið losuð þegar vísunin á
sér stað (þ.e. í línu 4).

En við þurfum samt að fara varlega. Við hefðum ekki getað haldið áfram
svona:

.. container:: proof

   *Proof.* ◻

Þetta væri stórslys. Ef ég segði við þig að Anna sé snjöll, þá ættirðu
ekki að geta dregið þá ályktun að ef Jón sé líka snjall
(„\ :math:`J`\ “), þá sé Anna snjöll *og* að Esjan sé á tunglinu
(„\ :math:`E`\ “). En ef þessi sönnun væri leyfileg, þá ættum við að
geta hugsað svona.

Vandinn hér er að hlutasönnunin sem hefst á :math:`J` veltur á því að
við höfðum þegar gert ráð fyrir :math:`E` á línu 2. Í línu 6, höfum við
aukaforsenduna :math:`B`: við erum ekki lengur að velta fyrir okkur hvað
við getum sannað ef við gerum líka ráð fyrir að :math:`J` sé satt. Það
væri því tómt svindl að reyna að notfæra okkur (á línu 7) hlutasönnunina
sem hófst á :math:`J`. Þess vegna segjum við líka:

Þessi sönnun brýtur í bága við þessa reglu. Hlutasönnunin í línum 3–4
kemur fyrir innan hlutasönnuninnar í línum 2–5, svo hlutasönnunin í
línum 3–4 getur ekki verið notuð í línu 7.

Það er alltaf leyfilegt að opna hlutasönnun með hvaða aukaforsendu sem
er. Það kann að hljóma einkennilega, að við getum bara gefið okkur hvað
sem er, en í raun er það ekki svo skrýtið: það er nefnilega ekki hægt að
loka öllum hlutasönnunum þannig að nokkuð gagnlegt verði úr því. Það
þarf því að velja aukaforsendur af kostgæfni. Það er til dæmis oft góð
hugmynd, ef markmiðið er að sanna skilyrðissetningu, að gefa sér
forliðinn. Ef hægt er að leiða út bakliðinn, að forliðnum gefnum, þá er
hægt að loka hlutasönnuninni með innleiðingarreglunni fyrir
skilyrðistengið.

Það er líka alltaf leyfilegt að loka hlutasönnun og losa aukaforsendur
hennar. En það þýðir samt ekki að það sé alltaf gagnlegt. Það þarf líka
að sýna útsjónarsemi við að loka þeim.

Jafngildistengið
~~~~~~~~~~~~~~~~

Innleiðingarreglan fyrir jafngildistengið er eins og tvöföld útgáfa af
reglunni fyrir skilyrðistengið: til að sanna „\ :math:`F \eiff G`\ “
þarf að sanna „\ :math:`G`\ “ að því gefnu sem aukaforsendu að :math:`F`
*og* :math:`F` að því gefnu sem aukaforsendu að :math:`G`. Þessi regla
þarfnast því *tveggja* hlutasannanna. Almennt form reglunnar er svona:

Það geta verið eins margar línur á milli :math:`i` og :math:`j` og verða
vill (sem eins og við munum, standa fyrir hvaða línur í sönnun sem er)
og hið sama gildir um :math:`k` og :math:`l`. Hlutasannanirnar geta líka
verið í hvaða röð sem er og sú seinni þarf ekki að koma fyrir beint á
eftir þeirri fyrri.

Eyðingarreglan (E) er mjög svipuð eyðingarreglunni fyrir
skilyrðistengið, nema í þetta skiptið gengur hún í báðar áttir: ef við
höfum vinstri liðinn gefinn, þá getum við ályktað að sá hægri sé sannur,
og ef við höfum þann hægri, þá getum við ályktað að sá vinstri sé
sannur. Almennt form reglunnar er því svona:

og á sama hátt: Rétt eins og í tilfelli skilyrðistengisins, þá geta
setningarnar birst í hvaða röð sem er, en þegar við vísum í ákveðnar
línur þegar við réttlætum notkun reglunnar, þá vísum við alltaf fyrst í
línuna þar sem jafngildistengið sjálft kemur fyrir.

Hér er svo dæmi um notkun innleiðingarreglunnar. Við sönnum að
:math:`(A \eif B) \eand (B \eif A) \therefore A \eiff B` sé gild
rökfærsla:

.. container:: proof

   *Proof.* æ1 æ1 ◻

Eða-tengi
~~~~~~~~~

Gerum ráð fyrir að Anna sé snjöll. Þá er það víst að Anna er annað hvort
snjöll eða sniðug. Af hverju? Jú, setningin „Anna er snjöll eða Anna er
sniðug“ er sönn ef önnur setninganna sem mynda hana er sönn og við vitum
að setningin „Anna er snjöll“ er sönn. Setningin hlýtur því öll að vera
sönn.

Þetta gildir um *hvaða* setningar sem er. Segjum að Anna sé snjöll. Þá
leiðir af því að Anna sé annað hvort snjöll eða banani. Það leiðir líka
af að Anna sé snjöll að Anna sé snjöll eða að Akureyri sé á tunglinu, og
að Anna sé snjöll eða að Jón sé 500 metra hár. Þetta eru auðvitað
furðulegar ályktanir, sem við myndum líklega aldrei draga, en það er
ekkert *rökfræðilega* athugavert við þær og það getum við staðfest með
að skoða skilgreiningarsanntöfluna fyrir eða-tengið.

Með þetta í huga, þá setjum við fram almennt form innleiðslureglunnar
fyrir eða-tengið svona:

og Athugið að :math:`\meta{B}` getur verið *hvaða* setning sem er.
Eftirfarandi sönnun er því fullkomlega rétt:

.. container:: proof

   *Proof.* ◻

Til að sýna að þessi rökfærsla sé gild með fullri sanntöflu þyrfti 128
línur.

Eyðingarreglan fyrir eða-tengi er öllu flóknari. Gerum ráð fyrir að Anna
sé snjöll eða að Anna sé sniðug. Hvaða ályktun getum við þá dregið? Ekki
að Anna sé snjöll, hún gæti jú bara verið sniðug. Eins getum við ekki
sagt að hún sé sniðug, því hún gæti bara verið snjöll. Það er því
óttalega lítið sem ályktað ef við höfum setningu með eða-tengi.

En hvað ef við gætum sýnt hvort tveggja af eftirfarandi: fyrst, að það
að Anna sé snjöll leiði af sér að hún sé góður vinur; og svo að það að
Anna sé sniðug leiði af sér að hún sé góður vinur? Þá vitum við að sama
hvort er, að Anna sé snjöll eða sniðug, þá er hún góður vinur.

Þetta er hugsunin á bak við eyðingarregluna fyrir eða-tengið
:math:`\eor`\ E. Almennt form hennar er svona:

Þessi regla er öllu klunnalegri en fyrri reglur, en hugmyndin er
tiltölulega einföld. Segjum að við höfum einhverja setningu á borð við
:math:`\meta{A} \eor \meta{B}`. Gerum svo ráð fyrir að við höfum tvær
hlutasannanir sem sýna hver um sig að :math:`\meta{C}` leiði af
aukaforsendunni :math:`\meta{A}` annars vegar og af aukaforsendunni
:math:`\meta{B}` hins vegar. Þá getum við dregið þá ályktun að
:math:`\meta{C}`. Eins og áður, þá geta verið eins margar línur og þarf
milli :math:`i` og :math:`j`, og hið sama gildir um :math:`k` og
:math:`l`. Hlutasannanirnar og setningin með eða-tenginu geta komið í
hvaða röð sem er, og þurfa ekki að vera hlið við hlið.

Hér eru nokkur dæmi til skýringar. Skoðum eftirfarandi rökfærslu:

.. math:: (P \eand Q) \eor (P \eand R) \therefore P

Hér er svo dæmi um sönnun. Takið eftir að við gefum okkur fyrst
:math:`P \eand Q` sem aukaforsendu og svo :math:`P \eand R`:

.. container:: proof

   *Proof.* æpq æpr œprem, pq-p1, pr-p2 ◻

Hér er svo aðeins flóknara dæmi. Skoðum:

.. math:: A \eand (B \eor C) \therefore (A \eand B) \eor (A \eand C)

Hér er svo sönnun:

.. container:: proof

   *Proof.* æaboc æaboc œboc, b-abo, c-aco ◻

Takið sérstaklega vel eftir því hvernig innleiðingarreglan fyrir
:math:`\eor` er notuð.

Ekki láta ykkur bregða ef þið sjáið ekki hvernig í ósköpunum þið hefðuð
átt að láta ykkur detta þessi sönnun í hug. Það að finna upp á nýjum
sönnunum er alls ekki einfalt mál og þarfnast æfingar. Á þessu stigi
málsins ættuð þið að einbeita ykkur að því að lesa sannanirnar
gaumgæfilega og aðgæta hvort þær séu ekki í samræmi við reglurnar sem
við höfum skilgreint. Það þýðir að þið ættuð að skoða hverja línu og
athuga hvort hún sé réttlætt á réttan hátt.

Það er þess virði að fara sérstaklega vel yfir kaflann um það hvernig
hlutasannanir virka, enda eru þær á margan hátt lykillinn að réttum
skilningi á náttúrulegri afleiðslu.

Mótsögn og neitun
~~~~~~~~~~~~~~~~~

Nú er einungis eitt setningatengi eftir, neitun. Reglurnar fyrir neitun
eru nátengdar *mótsögnum*.

Mótsögn er, eins og við sögðum hér að ofan, setning sem er ósönn fyrir
hvaða sanngildadreifingu sem er. Einföld mótsögn, kannski sú
einfaldasta, er setning á borð við :math:`A \eand \enot A`. Segjum að
einhver rökfærsla leiði okkur að niðurstöðu á þessu formi, til dæmis að
slökkt sé á ljósinu og ekki slökkt á ljósinu. Það getur augljóslega ekki
verið, svo eitthvað hefur greinilega farið úrskeiðis í rökfærslunni. Ef
við gerum ráð fyrir að við höfum ekki dregið *ranga* ályktun í neinu
skrefi, þá hlýtur að vera að einhver af *forsendunum* sem við gáfum
okkur sé ósönn. Sannar forsendur, með réttum skrefum, geta jú ekki leitt
okkur að ósannri niðurstöðu, en öðru máli gegnir um ósannar forsendur:
þær geta hæglega leitt okkur að ósannri niðurstöðu.

Reglurnar fyrir neitun byggja á þessari hugmynd. Við kynnum fyrst til
sögunnar nýtt tákn, „\ :math:`\ered`\ “. Við lesum það sem „mótsögn!“,
„það er út í hött!“ eða „þetta getur ekki verið!“. Eyðingarreglan fyrir
neitun segir að hvenær sem við höfum setningu og neitun hennar, þá megum
við innleiða þetta tákn:

Það skiptir ekki máli í hvaða röð setningin :math:`\meta{A}` og neitun
hennar koma fyrir, og það þarf ekki að vera á aðliggjandi línum. En við
vísum alltaf fyrst í setninguna og svo neitunina þegar við réttlætum
notkun þessarar reglu.

Við köllum þessa reglu eyðingarreglu fyrir neitun (:math:`\enot`\ E) af
því neitun kemur fyrir í einum af setningunum, en ekki í setningunni sem
leiðir af reglunni. Neitun er því í vissum skilningi eytt úr sönnuninni.
Við hefðum líka getað kallað þessa reglu „innleiðingarreglu fyrir
:math:`\ered`\ “, því hún innleiðir það tákn, en það þykir snyrtilegt að
hafa innleiðingar- og eyðingarreglu fyrir hvert tákn, svo við fylgjum
þeirri venju hér.

Næst er það innleiðingarreglan fyrir neitun. Hún byggir á hugmyndinni
hér að ofan: að ef einhver aukaforsenda leiði til mótsagnar, þá hlýtur
hún að vera ósönn: Það er að segja: ef við gefum okkur :math:`\meta{A}`
og getum leitt mótsögn af þeirri aukaforsendu, þá getum við leitt af því
neitun :math:`\meta{A}`, :math:`\enot \meta{A}`. Það er vert að taka
fram að það geta verið eins margar línur á milli :math:`i` og :math:`j`
og þörf krefur. Þessi regla er oft kölluð *reductio ad absurdum* og
sannanir sem notfæra sér þessa reglu eru oft kallaðar *óbeinar
sannanir*.

Hér er dæmi um samspil innleiðingar- og eyðingarreglunnar fyrir neitun:

.. container:: proof

   *Proof.* ◻

Hér er annað dæmi, sem sýnir að rökfærslan
:math:`A \eif B, \enot B \therefore \enot A` sé gild:

.. container:: proof

   *Proof.* A B B A B A ◻

Hér höfum við tvær forsendur, :math:`A \eif B` og :math:`\enot B`. Við
gefum okkur svo :math:`A` sem aukaforsendu og leiðum af henni :math:`B`
með modus ponens (E), þar sem :math:`A \eif B` er jú ein af forsendunum.
Þá höfum við mótsögn við eina af forsendunum okkar, nefnilega
:math:`\enot B`, og getum leitt af því :math:`\bot`. Þá vitum við að
aukaforsendan sem við gáfum okkur er röng, samkvæmt innleiðingarreglunni
fyrir neitun, og lokum því hlutasönnunnin með :math:`\enot A`.

Eins og minnst var á að ofan, þá er hægt að líta á eyðingarregluna fyrir
neitun sem innleiðingarreglu fyrir „\ :math:`\ered`\ “. Það væri því
ágætt að hafa samsvarandi eyðingarreglu. Reglan sem við notum kallast
„sprengiregla“ eða *ex falso quodlibet*. Þessi regla segir að *hvað sem
er* leiði af mótsögn. Það þýðir að ef við höfum mótsögn í sönnun, þá
getum við leitt af henni hvaða setningu sem er. Nafnið „sprengiregla“ er
dregið af þessu, því það er litið svo á að mótsögnin „sprengi“
ályktunina og geri *allt* satt.

Hér er almennt form sprengireglunnar: Það er vert að leggja áherslu á að
:math:`\meta{A}` má vera *hvaða setning sem er*!

Sprengireglan er óneitanlega furðuleg regla. Af hverju ætti það að vera
satt að :math:`\meta{A}` leiði af mótsögn, *sama* hvað :math:`\meta{A}`
er? Er það ekki bara eitthvað bull? En það eru góðar ástæður fyrir því
að þetta er í raun og veru góð regla. Fyrsta ástæðan, og sú
mikilvægasta, hefur að gera með skilgreininguna okkar á rökfræðilegri
afleiðingu. Við sögðum að :math:`\meta{B}` leiði rökfræðilega af
:math:`\meta{A}_1,...,\meta{A}_n` ef og aðeins ef það er ekki til
sanngildadreifing þar sem :math:`\meta{A}_1,...,\meta{A}_n` eru allar
sannar en :math:`\meta{B}` ósönn.

Fyllum nú út sanntöflu fyrir einhverja rökfærslu þar sem forsendan er
mótsögn, t.d. :math:`P \eand \enot P` og niðurstaðan einhver
grunnsetning, t.d. :math:`Q`. Í samræmi við skilgreininguna á
rökfræðilegri afleiðingu, þá þurfum við bara að skoða línurnar þar sem
:math:`Q` er ósönn:

.. container:: center

   .. container:: tabular

      | c c \|d e e f \| c :math:`Q` & :math:`P` & :math:`P` & & &
        :math:`P` & :math:`Q`
      | Ó & S & S & **Ó** & Ó & S & Ó
      | Ó & Ó & Ó & **Ó** & S & Ó & Ó

Munum að rökfærsla er gild eff ekki er til lína þar sem forsendurnar eru
allar sannar og niðurstaðan ósönn. Við sjáum að svo er ekki—það er
*ekki* til lína þar sem :math:`P \eand \enot P` er sönn og :math:`Q`
ósönn, enda er :math:`P \eand \enot P` alltaf ósönn. Rökfærslan
:math:`P \eand \enot P \therefore Q` er því gild, sama hvað :math:`P` og
:math:`Q` standa fyrir!

Þetta er engin tilviljun. Skilgreiningin okkar á gildi (og rökfræðilegri
afleiðingu) er hugsuð á þann hátt að gild rökfærsla sé þannig að það sé
engin leið að fara frá sönnum forsendum yfir í ósanna niðurstöðu. *Gildi
varðveitir sannleika*. En mótsagnir eru alltaf ósannar, svo það er
enginn sannleikur sem ályktunin þarf að varðveita: sprengireglan getur
einfaldlega ekki leitt okkur frá sannri forsendu til ósannrar
niðurstöðu, því forsendan er þegar ósönn.

Önnur ástæða hefur að gera með tengslin milli rökfræðilegrar afleiðingar
og skilyrðistengisins. Í setningarökfræði gildir almennt að
:math:`\meta{A} \entails \meta{B}` ef og aðeins ef
:math:`\entails \meta{A} \eif \meta{B}`. Þar sem
:math:`\entails \meta{A} \eif \meta{B}` er klifun ef :math:`\meta{A}` er
mótsögn (skilyrðissetningar eru alltaf sannar ef forliðurinn er
ósannur), þá myndu þessi tengsl rofna ef við neitum sprengjureglunni.

Það er að lokum önnur ástæða, nefnilega sú að sprengireglan er í raun og
veru *afleidd regla*, en það þýðir að hægt er að leiða hana út með því
að nota aðrar reglur náttúrulegrar afleiðslu. Við munum kynnast
afleiddum reglum innan skamms í §\ `6 <#s:Derived>`__ og þá munum við
sjá hvað það merkir.

Af framansögðu sjáum við þó að við komumst í raun ekki af án
sprengireglunnar, nema gera miklar breytingar á setningarökfræðinni. Það
vill svo til að það eru til rökfræðikerfi án sprengjureglunnar,
t.d. svokölluð mótsagnarökfræði (en hún er utan efnis þessarar bókar).

Hér er dæmi um notkun sprengireglunnar:

.. container:: proof

   *Proof.* A B A C B A C B C C œ1,4-5,6-8 ◻

Að ofan sögðum við að táknið „\ :math:`\ered`\ “ ætti að lesa sem
„mótsögn!“ eða eitthvað slíkt. En það er þó ekki nóg—hvernig eigum við
að hugsa um þetta tákn? Við höfum þrjá möguleika:

.. container:: ebullet

   Við gætum litið á táknið „\ :math:`\ered`\ “ sem sérstaka
   grunnsetningu á máli setningarökfræði en þó þannig að hún fái alltaf
   sanngildið „ósatt“.

   Við gætum líka litið á „\ :math:`\ered`\ “ sem skammstöfun á
   einhverri tiltekinni mótsögn á máli setningarökfræði, til dæmis
   „\ :math:`A \eand \enot A`\ “. Það myndi hafa sömu afleiðingar og
   fyrsti möguleikinn, þar eð „\ :math:`A \eand \enot A`\ “ er alltaf
   ósönn—en við myndum líka sleppa við að bæta við nýju tákni við mál
   setningarökfræðinnar.

   Loks gætum við litið á „\ :math:`\ered`\ “ sem nokkurs konar
   *greinarmerki* sem kemur fyrir í sönnunum, rétt eins og
   línumerkingarnar og línurnar sem við drögum undir forsendur.

Við munum velja annan möguleikann hér. Við munum líta á
„\ :math:`\ered`\ “ sem skammstöfun á einhverri mótsögn. Það þýðir að
við getum beitt öðrum reglum þetta tákn, rétt eins og um venjulega
setningu sé að ræða.

Tertium non datur
~~~~~~~~~~~~~~~~~

Við munum bæta við einni reglu í viðbót í þessum kafla. Hún er mjög lík
eyðingarreglunni fyrir eða-tengið.

Gerum ráð fyrir að við höfum sýnt að ef það er sól úti, þá fari Jón í
sund. Gerum líka ráð fyrir að við höfum sýnt að ef það er *ekki* sól
úti, þá fari Jón líka í sund. Það er annað hvort sól úti eða ekki, svo
sama hvernig veðrið er, þá mun Jón fara í sund. Við getum því dregið þá
ályktun að *sama hvað*, þá fer Jón í sund. Þessi hugsun liggur að baki
almennu formi reglunnar: Þessi regla er kölluð *tertium non datur*, sem
er latína og merkir „[hið] þriðja er ekki gefið“. [1]_ Það geta verið
eins margar línur og verða vill milli :math:`i` og :math:`j` annars
vegar og :math:`k` og :math:`l` hins vegar. Hlutasannanirnar geta komið
í hvaða röð sem er og sú seinni þarf ekki að koma strax á eftir þeirri
fyrstu.

Notum þessa reglu til að sanna að rökfærslan

.. math:: P \therefore (P \eand D) \eor (P \eand \enot D)

\ sé gild:

.. container:: proof

   *Proof.* ◻

*Þetta eru allar grunnreglurnar fyrir náttúrulega afleiðslu í
setningarökfræði*.

Eftirfarandi tvær „sannanir“ eru *ekki* réttar. Útskýrið mistökin sem
hafa verið gerð.

.. container:: multicols

   2

   .. container:: proof

      *Proof.* ◻

   .. container:: proof

      *Proof.* æabc ◻

Eftirfarandi þrjár sannanir vantar tilvísanir (í reglur og línur). Bætið
þeim við til að klára sannanirnar. Skrifið líka niður rökfærsluna sem
hver sönnun samsvarar (og munið eftir rithættinum sem notar
:math:`\therefore`).

.. container:: multicols

   2

   .. container:: proof

      *Proof.* ◻

   .. container:: proof

      *Proof.* ◻

   .. container:: proof

      *Proof.* ◻

Sannið að eftirfarandi rökfærslur séu gildar:

.. container:: earg

   :math:`J\eif\enot J \therefore \enot J`

   :math:`Q\eif(Q\eand\enot Q) \therefore \enot Q`

   :math:`A\eif (B\eif C) \therefore (A\eand B)\eif C`

   :math:`K\eand L \therefore K\eiff L`

   :math:`(C\eand D)\eor E \therefore E\eor D`

   :math:`A\eiff B, B\eiff C \therefore A\eiff C`

   :math:`\enot F\eif G, F\eif H \therefore G\eor H`

   :math:`(Z\eand K) \eor (K\eand M), K \eif D \therefore D`

   :math:`P \eand (Q\eor R), P\eif \enot R \therefore Q\eor E`

   :math:`S\eiff T \therefore S\eiff (T\eor S)`

   :math:`\enot (P \eif Q) \therefore \enot Q`

   :math:`\enot (P \eif Q) \therefore P`

.. _`s:Further`:

Fleiri reglur náttúrulegrar afleiðslu fyrir setningarökfræði
------------------------------------------------------------

Í §\ `2 <#s:BasicTFL>`__ kynntumst við grunnreglum náttúrulegrar
afleiðslu fyrir setningarökfræði. Í þessum hluta bætum við fleiri
reglum. Þessar reglur eiga það sameiginlegt að auðvelda alla sannanagerð
(en í §\ `6 <#s:Derived>`__ munum við sjá að þær eru strangt til tekið
ekki nauðsynlegar).

Endurtekningaregla
~~~~~~~~~~~~~~~~~~

Fyrsta aukareglan sem við skoðum er *endurtekingarreglan* (R). Hún
leyfir okkur að endurtaka línur sem við höfum þegar skrifað niður: Nú er
þetta augljóslega gild regla: hún mun aldrei leiða okkur í neinar
ógöngur. En hvers vegna í ósköpunum þurfum við hana? Skoðum dæmi:

.. container:: proof

   *Proof.* œfog, f-g, g2-g3 ◻

Þessi sönnun sýnir að rökfærslan :math:`F \eor G, F \eif G \therefore G`
er gild. Til þess að geta notað :math:`\eor E` í línu 7, þurfum við að
ljúka tveimur hlutasönnunum, einni sem hefst á aukaforsendunni :math:`F`
og einni sem hefst á aukaforsendunni :math:`G`. Báðar þurfa þær að enda
á :math:`G`. Þetta er einfaldlega það sem *form* eyðingarreglunnar fyrir
eða-tengið krefst.

En þetta form krefst að minnsta kosti *tveggja* lína—og við þurftum
ekkert meira en aukaforsenduna sjálfa. Ef við hefðum enga leið til að
endurtaka aukaforsenduna, þá værum við *föst* og gætum ekki klárað
sönnunina.

En þá vaknar spurningin: af hverju þurfum við regluna yfirleitt? Er
þetta ekki svo augljóslega satt að sérstök regla er óþarfi? Svarið við
því felst í *setningarfræðilegu eðli* sannanna. Sannanir eru þannig
hugsaðar að *form* þeirra er það eina sem skiptir máli, ekki merking
einstakra lína. Ef formið er í samræmi við þær reglur sem lagðar hafa
verið niður, þá er sönnunin góð, annars ekki. Þess vegna þurfum við
endurtekningarregluna, án hennar gætum við ekki gætt að því að form
þessarar sönnunar sé rétt.

Eða-samleiðuregla
~~~~~~~~~~~~~~~~~

Þessi rökfærsla virðist fullkomlega eðlileg:

   Guðni Th. er annað hvort á Bessastöðum eða Sóleyjargötu. Hann er ekki
   á Bessastöðum, svo hann hlýtur að vera á Sóleyjargötu.

Eftirfarandi regla reynir að fanga form þessarar rökfærslu:

og Við köllum þessa reglu *eða-samleiðureglu* (en enska heiti hennar er
„disjunctive syllogism“, sem útskýrir skammstöfunina *DS*). Eins og áður
mega setningin með eða-tenginu og liðurinn sem neitað er koma fyrir í
hvaða röð sem er. Setningarnar þurfa heldur ekki að vera samliggjandi.
En við vísum alltaf fyrst í setninguna með eða-tenginu.

Modus tollens
~~~~~~~~~~~~~

Annað gagnlegt rökfærslumynstur sést hér:

   Ef Anna lærir heima, þá stendur hún sig vel í rökfræði. Anna stendur
   sig ekki vel í rökfræði. Þar af leiðandi lærir hún ekki heima.

Þetta mynstur kallast *modus tollens* og liggur að baki eftirfarandi
reglu: Hér mega setningarnar að sjálfsögðu koma fyrir í hvaða röð sem er
og þurfa ekki að vera aðliggjandi. Við vísum þó alltaf fyrst í
skilyrðissetninguna.

Tvöföld neitunareyðing
~~~~~~~~~~~~~~~~~~~~~~

Önnur regla sem getur verið gagnleg er *tvöföld neitunareyðing* (en á
ensku er hún kölluð „double negation elimination“, en þaðan er
skammstöfunin komin). Nafnið er heldur lýsandi: Við getum auðveldlega
kannað með sanntöflu að þessi regla hlýtur að vera í lagi.

En við þurfum samt að fara varlega, því oft er merking tvöfaldrar
neitunar í mæltu máli ekki alveg svona einföld. Til dæmis getum við ekki
sagt að ef Jón er ekki óánægður að hann sé ánægður. Kannski er hann
hvorki ánægður né óánægður. Við þurfum alltaf að hafa í huga að
setningarökfræðin getur ekki fangað öll blæbrigði.

De Morgan-reglur
~~~~~~~~~~~~~~~~

Síðustu reglurnar sem við bætum við eru svokallaðar De Morgan-reglur,
kenndar við rökfræðingin August De Morgan. Þær gera okkur kleift að færa
neitun inn og út úr svigum sem innihalda eða-tengi og og-tengi. Takið
eftir að eða-tengi breytist í og-tengi og öfugt þegar reglunum er beitt.

Fyrsta De Morgan-reglan er: Önnur De Morgan-reglan er eins og sú fyrsta,
nema að hún gengur í öfuga átt: Þriðja De Morgan-reglan samsvarar þeirri
fyrstu, nema með eða-tengi í stað og-tengis sem aðaltengi. Fjórða og
síðasta De Morgan-reglan er svo eins og sú þriðja, nema öfugt: De
Morgan-reglurnar geta verið mjög gagnlegar, sérstaklega þegar þær eru
notaðar í óbeinum sönnunum.

*Þetta eru allar aukareglurnar sem við bætum við náttúrulega afleiðslu í
setningarökfræði*.

Eftirfarandi sannanir vantar tilvísanir (í reglur og línur). Bætið þeim
við til að klára sannanirnar.

.. container:: multicols

   2

   .. container:: proof

      *Proof.* ◻

   .. container:: proof

      *Proof.* ◻

   .. container:: proof

      *Proof.* ◻

Sannið að eftirfarandi rökfærslur séu gildar:

.. container:: earg

   :math:`E\eor F`, :math:`F\eor G`,
   :math:`\enot F \therefore E \eand G`

   :math:`M\eor(N\eif M) \therefore \enot M \eif \enot N`

   :math:`(M \eor N) \eand (O \eor P)`, :math:`N \eif P`,
   :math:`\enot P \therefore M\eand O`

   :math:`(X\eand Y)\eor(X\eand Z)`, :math:`\enot(X\eand D)`,
   :math:`D\eor M \therefore M`

.. _`s:ProofTheoreticConcepts`:

Hugtök sem tengjast sönnunum
----------------------------

Rétt eins og við kynntum til sögunnar ákveðin merkingarfræðilega hugtök
til að auðvelda okkur að tala um sannleika og merkingarfræðileg tengsl
milli setninga, þá viljum við gera slíkt hið sama fyrir sannanir. Við
köllum þessi hugtök hugtök. Við segjum að

.. math:: \meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n \proves \meta{B}

\ þýði að til sé sönnun sem hefur
:math:`\meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n` sem ólosaðar
forsendur en :math:`\meta{B}` sem niðurstöðu. Ef við viljum segja að
*ekki* sé til slík sönnun, þá skrifum við:

.. math:: \meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n \nproves \meta{B}

Það er mikilvægt að taka vel eftir því að táknið „\ :math:`\proves`\ “
er *ekki* það sama og táknið „\ :math:`\entails`\ “ sem við notuðum til
að tákna rökfræðilega afleiðingu í kafla
`[ch.TruthTables] <#ch.TruthTables>`__ (og komum aftur að í kafla
`[ch.semantics] <#ch.semantics>`__). „\ :math:`\proves`\ “ segir
nefnilega að ákveðin sönnun sé til, en „\ :math:`\entails`\ “ segir að
ekki séu til ákveðnar sanngildadreifingar. *Það er mikilvægt að halda
þessu aðskildu.*

Með þessum nýja rithætti getum við kynnt til sögunnar ýmis ný hugtök. Ef
hægt er að sanna :math:`\meta{A}` án nokkurra ólosaðra forsenda, til
dæmis, þá skrifum við:

.. math:: {} \proves \meta{A}

\ Við segjum þá að :math:`\meta{A}` sé . Þetta þýðir að sönnunin notast
ekki við neinar forsendur aðrar en þær sem koma fyrir sem aukaforsendur
innan hlutasannanna.

Hér er dæmi. Segjum að við viljum sýna að
:math:`{}\proves \enot (A \eand \enot A)`. Það þýðir, eins og áður
sagði, að til er sönnun á :math:`\enot(A \eand \enot A)` sem hefur
*engar* ólosaðar forsendur. Þar sem setningin hefur neitun sem aðaltengi
er ágæt hugmynd að prófa *neitunarinnleiðingu* og gefa okkur þá
:math:`A \eand \enot A` sem aukaforsendu í hlutasönnun. Ef við getum
sýnt að það leiði til mótsagnar, þá erum við búin. Sönnunin lítur því
svona út:

.. container:: proof

   *Proof.* æcon æcon ◻

Þegar við lokum hlutasönnuninni, losum við aukaforsenduna eins og lög
gera ráð fyrir. Við höfum því sannað :math:`\enot (A \eand \enot A)` án
nokkura (ólosaðra) forsenda. Þá segjum við að
:math:`\enot (A \eand \enot A)` sé *sannanleg* setning, eða einfaldlega
að :math:`{}\proves \enot (A \eand \enot A)`.

Til að sýna að einhver tiltekin setning sé sannanleg, þá þurfum við að
finna rétta sönnun. En það er mun erfiðara að sýna að tiltekin setning
sé *ekki* sannanleg, því til þess þyrfti að sýna að *engin* sönnun sé
möguleg. Það skiptir engu máli hversu lengi við höfum reynt að finna
slíka sönnun eða hversu margar mismunandi leiðir við höfum reynt, það er
alltaf möguleiki að við höfum bara ekki reynt nógu lengi eða ekki prófað
nógu margt. Hugsanlega er sönnunin bara of flókin fyrir okkur.

Hér er önnur skilgreining: Rétt eins og fyrr er tiltölulega auðvelt að
sýna að tvær setningar, :math:`\meta{A}` og :math:`\meta{B}`, séu
sannanlega jafngildar. Til þess þurfum við bara tvær sannanir, eina þar
sem :math:`\meta{A}` er forsenda og :math:`\meta{B}` niðurstaða og eina
þar sem :math:`\meta{B}` er forsenda og :math:`\meta{A}` niðurstaða. En
að sýna að tvær setningar séu *ekki* sannanlega jafngildar er mun
erfiðara, en til þess þyrfti að sýna að ekki sé til að minnsta kosti ein
sönnun.

Hér er þriðja skilgreiningin:

Til að sýna að setningar séu sannanlega andstæðar er nóg að gefa sér þær
allar sem forsendur og leiða af þeim mótsögn. En að sýna að þær séu
*ekki* sannanlega andstæðar er mun erfiðara. Þá þarf aftur að sýna að
tiltekin sönnun sé *ekki* til.

|  
| Þessi tafla dregur saman hvort ein eða tvær sannanir dugi, eða hvort
  við þurfum að taka allar mögulegar sannanir til greina.

.. container:: center

   ====================== ============= ========================
   \                      **Já**        **Nei**
   ====================== ============= ========================
   sannanleg setning?     ein sönnun    allar mögulegar sannanir
   sannanlega jafngildar? tvær sannanir allar mögulegar sannanir
   sannanlega andstæðar?  ein sönnun    allar mögulegar sannanir
   ====================== ============= ========================

Sýnið að eftirfarandi setningar séu sannanlegar:

.. container:: earg

   :math:`O \eif O`

   :math:`N \eor \enot N`

   :math:`J \eiff [J\eor (L\eand\enot L)]`

   :math:`((A \eif B) \eif A) \eif A`

Sannið eftirfarandi:

.. container:: earg

   :math:`C\eif(E\eand G), \enot C \eif G \proves G`

   :math:`M \eand (\enot N \eif \enot M) \proves (N \eand M) \eor \enot M`

   :math:`(Z\eand K)\eiff(Y\eand M), D\eand(D\eif M) \proves Y\eif Z`

   :math:`(W \eor X) \eor (Y \eor Z), X\eif Y, \enot Z \proves W\eor Y`

Sýnið að eftirfarandi setningapör séu sannanlega jafngild.

.. container:: earg

   :math:`R \eiff E`, :math:`E \eiff R`

   :math:`G`, :math:`\enot\enot\enot\enot G`

   :math:`T\eif S`, :math:`\enot S \eif \enot T`

   :math:`U \eif I`, :math:`\enot(U \eand \enot I)`

   :math:`\enot (C \eif D), C \eand \enot D`

   :math:`\enot G \eiff H`, :math:`\enot(G \eiff H)`

| Ef við vitum að :math:`\meta{A} \proves \meta{B}`, hvað getum við þá
  sagt um :math:`\meta{A} \eand \meta{C} \proves \meta{B}`? Hvað með
  :math:`\meta{A} \eor \meta{C} \proves \meta{B}`?
| Í þessum hluta hélt ég því fram að það væri jafn erfitt að sýna að
  tvær setningar séu ekki sannanlega jafngildar og það er að sýna að
  setning sé ekki sannanleg. Af hverju? (*Ábending*: veltið fyrir ykkur
  hvort til sé setning sem væri sannanleg ef og aðeins ef
  :math:`\meta{A}` og :math:`\meta{B}` eru sannanlega jafngildar).

Ráð við uppgötvun sannana
-------------------------

Sannanir í setningarökfræði hafa ýmsa kosti. Þær eru styttri og
fljótlegri en sanntöflur og það er auðveldlega hægt að ganga úr skugga
um að tiltekin sönnun sé rétt. En það er ekki til nein pottþétt aðferð
við að *uppgötva* sannanir, sérstaklega þegar við færum okkur yfir í
umsagnarökfræði. Það kemur því ekkert í stað æfingar og reynslu við
uppgötvun sannanna. En það er þó hægt að hafa nokkur ráð í huga.

Að skoða niðurstöðuna.
                      

Markmið sönnunar er að sanna niðurstöðuna. Með því að athuga hvert
aðaltengið í niðurstöðunni er, þá sjáum við í fljótu bragði hvaða
innleiðingarreglu þarf að beita í síðasta skrefi sönnunarinnar. Ef við
vitum hvaða innleiðingarreglu þarf að beita, þá vitum við líka hvaða
setningar við þurfum til að geta beitt þeirri reglu. Þá getum við spurt
okkur, hvað þarf að gerast í sönnunninni til að leiða út þær setningar?

Það er sérstaklega gott að hafa í huga að ef form niðurstöðunnar er
skilyrðissetning, þá er oftast best að prófa að gefa sér forliðinn og
sjá hvort ekki sé hægt að finna einhverja leið til að sanna bakliðinn.
Þá er hægt að nota innleiðingarregluna fyrir :math:`\eif` og losa
aukaforsenduna. Um þetta eru mörg dæmi í bókinni.

Skoða forsendurnar.
                   

Við getum líka byrjað á að skoða forsendurnar. Setningarnar sem mynda
forsendurnar ákvarða hvaða eyðingarreglum við getum beitt fyrst. Það
segir okkur hvaða möguleika við höfum í sönnuninni.

Í stuttri sönnun er oft nóg að beita eyðingarreglum á forsendurnar og
svo einhverri innleiðingarreglu til að fá niðurstöðuna. Löng sönnun er í
raun bara margar stuttar sannanir, svo með því að skoða niðurstöðuna og
forsendurnar til skiptis er oft hægt að finna einhverja leið frá
forsendunum að niðurstöðunni.

Prófa óbeina sönnun
                   

Ef allt þrýtur er oft hægt að prófa óbeina sönnun. Til að sanna
:math:`\meta{A}` myndum við þá byrja á því að gefa okkur
:math:`\enot \meta{A}` og reyna að leiða af því mótsögn. Ef hún finnst,
þá getum við dregið þá ályktun að :math:`\enot \enot \meta{A}` með
:math:`\enot`\ I. Þá er bara eftir að beita tvöfaldri neitunareyðingu og
fá :math:`\meta{A}`.

Það er ágætt að hafa í huga að þessi aðferð virkar sérstaklega vel í
samspili við De Morgan-reglurnar. Það er mjög oft hægt að finna mótsögn
með því að gefa sér neitun þess sem á að sanna og beita svo einhverjum
af De Morgan-reglunum til að finna mótsögnina.

Ekki gefast upp.
                

Það er oft gott að prófa bara mismunandi aðferðir við sönnunina. Ef ein
virkar ekki, þá má prófa aðra. Ef setningin er sannanleg af forsendunum,
þá virkar eitthvað.

.. _`s:Derived`:

Afleiddar reglur
----------------

Í þessum hluta verður loks útskýrt hvers vegna við kynntum reglurnar
fyrir náttúrulega afleiðslu til sögunnar í tveimur hlutum. Við munum
sýna að reglurnar sem við bættum við í §\ `3 <#s:Further>`__ eru strangt
til tekið ekki nauðsynlegar, heldur sé hægt að leiða þær af
grunnreglunum sem við kynntumst í §\ `2 <#s:BasicTFL>`__.

Útleiðsla á endurtekingarreglunni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Segjum að við höfum sönnun þar sem eftirfarandi lína kemur fyrir:

.. container:: proof

   *Proof.* ◻

Ef við vildum svo seinna endurtaka þessa línu, segjum á línu :math:`k`,
þá gætum við bara notað endurtekingarregluna (R) sem kynnt var til
sögunnar í §\ `3 <#s:Further>`__. En við gætum líka einskorðað okkur við
grunnreglurnar úr §\ `2 <#s:BasicTFL>`__ og gert eftirfarandi:

.. container:: proof

   *Proof.* æaa ◻

Það er þó mikilvægt að átta sig á því að þetta er í sjálfu sér ekki
sönnun, heldur gróf lýsing á mögulegum sönnunum (enda er
:math:`\meta{A}` ekki setning á máli setningarökfræði, heldur hluti af
framsetningarmálinu). Þetta er frekar eins og uppskrift sem sýnir okkur
hvernig við getum skipt út endurtekningarreglunni fyrir aðrar reglur.
Við *þurfum* því strangt til tekið ekki á henni að halda, heldur gætum
alltaf bara fylgt þessari uppskrift þegar við viljum endurtaka okkur.

Takið þó eftir því að þessi uppskrift byggir á því að beita
innleiðingarreglunni fyrir og-tengið *tvisvar* á sömu línu. Það er
ekkert í kerfinu okkar sem bannar þetta, en ef svo væri, þá yrðum við að
kynna endurtekningarregluna til sögunnar sem grunnreglu.

Útleiðsla á eða-samliðureglunni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Segjum að eftirfarandi tvær línur komi fyrir í sönnun:

.. container:: proof

   *Proof.* ◻

Ef við viljum nota þessar línur til að sanna :math:`\meta{B}`, þá getum
við notað eða-samliðuregluna (DS) úr §\ `3 <#s:Further>`__. En við getum
líka notað eftirfarandi uppskrift sem eingöngu notar grunnreglurnar úr
§\ `2 <#s:BasicTFL>`__:

.. container:: proof

   *Proof.* æbb œab, a-b1, b-b2 ◻

Við getum því greinilega leitt eða-samliðuregluna út með því að nota
einungis grunnreglurnar. Við getum ekki sannað neitt fleira þegar við
bætum henni við. Í hvert sinn sem við notum regluna gætum við
einfaldlega notað aðeins fleiri línur í samræmi við þessa uppskrift.
Eða-samliðureglan er því *afleidd regla*.

Hið sama gildir um aðrar afleiddar reglur: það er alltaf hægt að skipta
þeim út fyrir fleiri línur sem fylgja einhverri uppskrift af þessu tagi.
Nú eigum við bara eftir að fara í gegnum modus tollens, De
Morgan-reglurnar og tvöfalda neitunareyðingu.

Útleiðsla á modus tollens
~~~~~~~~~~~~~~~~~~~~~~~~~

Segjum að eftirfarandi tvær línur komi fyrir í sönnun:

.. container:: proof

   *Proof.* ◻

Ef við viljum nota þessar línur til að sanna :math:`\enot \meta{A}`, þá
getum við notað *modus tollens* sem kynnt var til sögunnar í
§\ `3 <#s:Further>`__. En við gætum líka fylgt eftirfarandi uppskrift:

.. container:: proof

   *Proof.* ◻

Modus tollens er því afleidd regla og bætir engu við grunnreglurnar sem
kynntar voru til sögunnar í §\ `2 <#s:BasicTFL>`__.

Útleiðsla á De Morgan-reglunum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hér útleiðsla á fyrstu De Morgan-reglunni sem einungis notar
grunnreglurnar:

.. container:: proof

   *Proof.* ◻

Hér útleiðsla á annarri De Morgan-reglunni:

.. container:: proof

   *Proof.* æab æab œnab, na-c1, nb-c2 ◻

Hægt er að gefa svipaðar útleiðslur á þriðju og fjórðu De
Morgan-reglunum, en ég læt þær lesendum eftir sem æfingar.

Útleiðsla á tvöföldu neitunarreglunni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hér útleiðsla á tvöföldu neitunarreglunni sem einungis notar
grunnreglurnar:

.. container:: proof

   *Proof.* ◻

| Leiðið út þriðju og fjórðu De Morgan-regluna.
| Við kynntum sprengiregluna til sögunnar sem *grunnreglu* í
  §\ `2 <#s:BasicTFL>`__. En í raun er hægt að leiða hana út með því að
  nota einungis aðrar grunnreglur. Finnið slíka útleiðslu (*ábending*:
  sprengireglan leyfir okkur að draga hvaða ályktun sem er af mótsögn.
  Er ekki til grunnregla sem leyfir okkur að kynna til sögunnar hvaða
  setningu sem er?).

.. [1]
   Við gerum hér greinarmun á *ályktunarreglunni* „tertium non datur“ og
   svo því sem nefnt hefur verið „lögmálið um annað tveggja“. Lögmálið
   um annað tveggja er *sannanleg setning* í setningarökfræði, sem hefur
   formið :math:`\proves A \eand \enot A`. Við fjöllum um þennan rithátt
   að neðan í §\ \ `4 <#s:ProofTheoreticConcepts>`__.
