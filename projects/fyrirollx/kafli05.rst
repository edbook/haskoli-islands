.. _ch.FOL:

Umsagnarökfræði
===============

.. _`s:FOLBuildingBlocks`:

Grunneiningar umsagnarökfræði
-----------------------------

Þörfin fyrir umsagnarökfræði
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skoðum eftirfarandi rökfærslu, sem augljóslega er gild:

.. container:: earg

   Júlía er rökfræðingur.

   Allir rökfræðingar ganga um í furðufötum.

   Júlía gengur um í furðufötum.

Við gætum ef til vill þýtt hana yfir á mál setningarökfræði með
eftirfarandi þýðingarlykli:

.. container:: ekey

   Júlía er rökfræðingur.

   Allir rökfræðingar ganga um í furðufötum.

   Júlía gengur um í furðufötum.

Rökfærslan yrði þá svona á máli setningarökfræðinnar:

.. math:: R, F \therefore J

En við getum gengið úr skugga um það með sanntöflum að :math:`J` leiðir
ekki rökfræðilega af :math:`R` og :math:`F` og því myndum við kannski
vilja segja að þessi prýðilega rökfærsla sé eftir allt saman *ógild*.
Hvað hefur farið úrskeiðis?

Við höfum ekki gert nein mistök við þýðingu yfir mál
setningarökfræðinnar, enda er engin betri þýðing í boði. Vandinn snýr að
takmörkunum setningarökfræðinnar. Setningin „Allir rökfræðingar ganga um
í furðufötum“ snýr að rökfræðingum og fötunum sem þeir ganga í—setningin
fullyrðir eitthvað um tengsl þess að vera rökfræðingur og að ganga um í
furðufötum. Þegar við höfum þýtt rökfærsluna yfir á mál setningarökfræði
eru tengslin milli þess að Júlía sé rökfræðingur og að hún gangi um í
furðufötum horfin.

Smæstu einingar setningarökfræðinnar eru grunnsetningar og þær segja
okkur ekkert um *innri* gerð setningana sem þær tákna. Til þess að geta
það þurfum við að bæta einhverju við formlega málið sem við notum til að
greina rökfærslur. Það er efni þessa kafla og þeirra næstu. Við munum
kalla þetta mál *umsagnarökfræði*. [1]_

Áður en lengra er haldið, og við fjöllum ítarlega um hvernig
umsagnarökfræðin er byggð upp, er hér stutt yfirlit yfir hvernig hún er
hugsuð og úr hverju mál hennar samanstendur.

Fyrst ber að nefna *nöfn*. Í umsagnarökfræði notum við nöfn til að
standa fyrir ákveðið fólk eða tiltekna hluti. Við táknum nöfnin með
skáletruðum lágstöfum. Til dæmis gætum við látið bókstafinn
„\ :math:`j`\ “ standa fyrir Júlíu hér að ofan, eða látið
„\ :math:`a`\ “ standa fyrir Aragötu.

Því næst höfum við umsagnir. Þær eru setningabrot á borði við „ er
rökfræðingur“ eða „ er stór“. Umsagnir tjá ekki heila hugsun fyrr en við
höfum fyllt upp í götin með því að búa til heilar setningar, t.d. „Júlía
er rökfræðingur“ og „Felix er stór“. Í umsagnarökfræði notum við
skáletraða hástafi til að tákna umsagnir. Til dæmis getum við látið
setningastafinn „\ :math:`S`\ “ standa fyrir „ er stór“. Við setjum
saman svo umsögn og nafn til að tjá einhverja tiltekna setningu. Ef
„\ :math:`f`\ “ stæði fyrir Felix, þá getum við látið táknrununa
„\ :math:`Sf`\ “ standa fyrir setninguna „Felix er stór“. Eins myndi
„\ :math:`Rj`\ “ þá standa fyrir setninguna „Júlía er rökfræðingur“, ef
„\ :math:`R`\ “ stæði fyrir „ er rökfræðingur“ og „\ :math:`j`\ “ stæði
fyrir Júlíu.

Loks höfum við svokallaða magnara. Til dæmis, þá mun táknið
„\ :math:`\exists`\ “ standa fyrir eitthvað á borð við „Til er að
minnsta kosti eitt …“ eða „Til er *x* sem er þannig að …“. Setningin
„Álfar eru til“ væri því táknuð sem :math:`„\exists x Ex“` á máli
umsagnarökfræði (ef „\ :math:`E`\ “ stæði fyrir umsögnina „ er álfur“).
Seinna í kaflanum munum við fara nánar yfir það hvað þetta
„\ :math:`x`\ “ er að gera þarna.

Þetta er ekki nema yfirlit. Umsagnarökfræðin er mun margslungnari en
setningarökfræðin og því munum við fara okkur hægt. Við munum ekki
minnast á það sérstaklega, annars staðar en hér, en umsagnarökfræðin
inniheldur öll setningatengin úr setningarökfræðinni og er enginn munur
á því hvernig þau virka þar.

Nöfn
~~~~

*Einnefni* köllum við orð sem vísa til *tiltekinnar* manneskju, staðar
eða hlutar. Orðið „hundur“ er ekki einnefni, því það eru til fleiri en
einn hundur. Nafnið „Vaskur“ er einnefni, því það vísar til tiltekins
hunds, Vasks. Við getum líka litið á sum orðasambönd sem einnefni, til
dæmis orðasambandið „hundurinn hennar Siggu“, því þau gegna sama
hlutverki, í þessu tilfelli að vísa til tiltekins hunds.

Sérnöfn eru sérstaklega mikilvægur flokkur einnefna. Þau vísa til
einstaklinga án þess að lýsa þeim. Í umsagnarökfræði gegna sama
hlutverki og sérnöfn í mæltu máli. Á táknmáli umsagnarökfræði eru nöfn
skáletraðir lágstafir *fremst* í stafrófinu, „\ :math:`a`\ “ til
„\ :math:`r`\ “ (en eins og við munum sjá, er oft þægilegt að nota aðra
stafi ef það sem vísað er til er nátengt stafnum. Það er þó bara þægileg
venja). Ef þörf krefur, getum við líka notað lágvísa. Hér eru nokkur
nöfn í umsagnarökfræði:

.. math:: a,b,c,\ldots, r, a_1, f_{32}, j_{390}, m_{12}

En það er einn mikilvægur munur á sérnöfnum í mæltu máli og nöfnum í
umsagnarökfræði. „Jón“ er sérnafn en þó heita mjög margir Jón. Oftast
skiptir það okkur litlu máli, því samhengið sker úr um hvern þeirra við
erum að tala um, jafnvel þó að við þekkjum marga Jóna. Í umsagnarökfræði
gegnir öðru máli. Þar vísar hvert nafn til *nákvæmlega* eins hlutar (en
þó geta tvö nöfn vísað til sama hlutarins, það er í góðu lagi). Ef við
þurfum að tala um marga hluti sem bera sama nafn í mæltu máli, þá getum
við notað lágvísa til að aðgreina þá.

Rétt eins og í setningarökfræði notum við þýðingarlykla. Þeir segja
okkur hvernig við notum ákveðin nöfn í það og það skiptið. Til dæmis:

.. container:: ekey

   Anna

   Jón

   Vaskur

   Reykjavík

Glöggir lesendur gætu þó hafa tekið eftir því að hér höfum við notað
táknið „v“ til að standa fyrir Vask, þó að nöfn eigi formlega séð að
vera stafir fremst úr stafrófinu, nefnilega a–r. Hér er aftur um að ræða
*venju* þar sem við myndum nota annað tákn ef við ætluðum að fylgja
reglunum til hins ítrasta.

Oft er hins vegar einfaldlega of freistandi að nota einfaldlega fremsta
stafinn í nafni þess sem verið er að tákna og ef það veldur ekki
ruglingi er það oftast hættulaust. Það verður þó að hafa í huga að *x*,
*y* og *z* eru svo algeng breytunöfn að ef þessi tákn væru notuð sem
nöfn, þá myndi það örugglega alltaf valda misskilningi. Það ber því að
forðast.

Umsagnir
~~~~~~~~

*Umsagnir* segja eitthvað um tiltekinn hlut, til dæmis að hann hafi
ákveðna eiginleika. Hér eru dæmi um nokkrar umsagnir á mæltu máli:

   |  er hundur
   |  er meðlimur í Wu Tang Clan
   | Snjóflóð féll á

Almennt getum við hugsað um umsagnir sem eitthvað sem við skeytum saman
við nöfn til að mynda setningar. Við getum líka byrjað með setningar og
búið til umsagnir úr þeim með því að fjarlæga nöfnin. Tökum sem dæmi
setninguna „Anna fékk lánaðan bílinn hjá Jóni“. Með því að fjarlægja
nöfn getum við búið til þrjár mismunandi umsagnir (og takið eftir að við
notum „bíllinn“ sem nafn):

   |  fékk lánaðan bílinn hjá Jóni
   | Anna fékk lánaðan  hjá Jóni
   | Anna fékk lánaðan bílinn hjá

Í táknmáli umsagnarökfræði eru umsagnir táknaðar með skáletruðum
hástöfum, með eða án lágvísa. Við gætum til dæmis búið til eftirfarandi
þýðingarlykil:

.. container:: ekey

   er glaður

   er hundur

(Af hverju notum við lágvísa á götin í umsögnunum? Við komum betur að
þessu í §\ `3 <#s:MultipleGenerality>`__.)

Með því að blanda saman þýðingarlyklunum okkar fyrir umsagnir og nöfn,
þá getum við farið að þýða setningar af mæltu máli yfir á táknmál
umsagnarökfræði. Skoðum til dæmis eftirfarandi setningar:

.. container:: earg

   Vaskur er hundur.

   Anna og Jón eru glöð.

   Ef Anna og Jón eru glöð, þá er Vaskur það líka.

Setning `[terms1] <#terms1>`__ er tiltölulega einföld. Við táknum hana
sem :math:`Hv`. *Við táknum það sem samsvarar heilli grunnsetningu með
því að skrifa nafn beint á eftir umsögn.* Við förum betur í þetta að
neðan.

Setning `[terms2a] <#terms2a>`__ er samtenging tveggja setninga. Þær er
hægt að tákna hvora um sig sem :math:`Ga` og :math:`Gj`. Við getum svo
notað setningatengin úr setningarökfræðinni og táknað alla setninguna
sem :math:`Ga \eand Gj`.

Setning `[terms2] <#terms2>`__ er skilyrðistengi, þar sem forliðurinn er
`[terms2a] <#terms2a>`__ og bakliðurinn :math:`Gv`. Við getum því þýtt
þessa setningu yfir á táknmál umsagnarökfræði svona:
:math:`(Ga \eand Gj) \eif Gv`.

Magnarar
~~~~~~~~

Við getum núna kynnt magnara til sögunnar. Tökum eftirfarandi setningar
sem dæmi:

.. container:: earg

   Allir eru glaðir.

   Einhver er glaður.

Það væri freistandi að reyna að þýða `[q.a] <#q.a>`__ sem
:math:`Ga \eand Gj \eand Gv`. En þessi setning segir bara að Anna, Jón
og Vaskur séu glöð. Við viljum segja að *allir* séu glaðir, líka þeir
sem við höfum ekki nefnt í þýðingarlyklinum okkar. Til að gera það notum
við táknið „\ :math:`\forall`\ “. Það er kallað .

Á eftir mögnurum koma alltaf . Á táknmáli umsagnarökfræði eru breytur
táknaðar með skáletruðum lágstöfum, með eða án lágvísa, aftast úr
stafrófinu, „\ :math:`s`\ “ til „\ :math:`z`\ “. Langalgengast er þó að
nota bara :math:`x`, :math:`y` og :math:`z`. Við þýðum setningu
`[q.a] <#q.a>`__ svona: „\ :math:`\forall x Gx`\ “ og lesum það sem
„fyrir öll :math:`x`, :math:`x` er glatt“.

En hvað þýðir þetta? Við getum litið á táknrununa
„\ :math:`\forall xGx`\ “ þannig að hún segi: „veldu einhvern hlut og
kallaðu hann :math:`x`. Það skiptir ekki máli hvað þú velur, :math:`x`
er glatt“ eða „sama hvaða :math:`x` þú velur, :math:`x` er glatt“.
Breytur virka því á svipaðan hátt og fornöfn í mæltu máli: það skiptir
ekki máli hvað þú velur, *það* er glatt.

Það er engin sérstök ástæða til að nota :math:`x` frekar en aðrar
breytur. Setningarnar „\ :math:`\forall x Gx`\ “,
„\ :math:`\forall y Hy`\ “, „\ :math:`\forall z Hz`\ “ og
„\ :math:`\forall x_5 Hx_5`\ “ nota allar mismunandi breytur, en þær
segja allar það sama og eru rökfræðilega jafngildar.

Til að þýða setningu `[q.e] <#q.e>`__ yfir á táknmál umsagnarökfræði
kynnum við nýtt tákn til sögunnar: „\ :math:`\exists`\ “. Það er kallað
og stundum *summagnari*. Rétt eins og almagnarinn, þá þarf
tilvistarmagnarinn að taka með sér breytu. Við þýðum setningu
`[q.e] <#q.e>`__ sem „\ :math:`\exists x Gx`\ “. Þessi setning er lesin
sem „til er :math:`x` sem er þannig að :math:`x` er glatt“. Rétt eins og
áður, þá skiptir ekki máli hvaða breytu við notum, setningarnar
„\ :math:`\exists x Gx`\ “, „\ :math:`\exists z Gz`\ “ og
„\ :math:`\exists w_{256} Gw_{256}`\ “ merkja allar það sama.

Hér eru nokkur fleiri dæmi:

.. container:: earg

   Enginn er glaður.

   Einhver er ekki glaður.

   Það eru ekki allir glaðir.

Setningu `[q.ne] <#q.ne>`__ er hægt að umorða sem „Það er ekki satt að
einhver sé glaður“. Við getum þýtt þessa setningu yfir á táknmál
setningarökfræði með því að nota neitun og tilvistarmagnara:
„\ :math:`\enot \exists xGx`\ “: ekki er til :math:`x` sem er þannig að
:math:`x` er glatt. En `[q.ne] <#q.ne>`__ má líka umorða þannig, heldur
kauðalega: „Allir eru ekki glaðir“. Með þetta í huga, þá getum við þýtt
með neitun og almagnara: :math:`\forall x \enot Gx`. Þessar þýðingar eru
báðar jafngildar. Raunar mun koma í ljós síðar að það gildir almennt að
allar setningar á forminu :math:`\forall x \enot \meta{A}` og
:math:`\enot \exists x \meta{A}` eru jafngildar (hér notum við
:math:`\meta{A}` sem metabreytu sem stendur fyrir hvaða formúlu sem er í
umsagnarökfræði, sjá §\ `[s:UseMention] <#s:UseMention>`__ og
§\ `6.2 <#formula>`__). Stundum er eðlilegra að fylgja annarri þýðingu,
frekar en hinni, en almennt er þetta bara smekksatriði.

Setningu `[q.en] <#q.en>`__ má umorða sem „Til er :math:`x` sem er
þannig að :math:`x` er ekki glatt“. Við myndum þýða það yfir á táknmál
umsagnarökfræði sem „\ :math:`\exists x \enot Gx`\ “. Við hefðum líka
getað þýtt þessa setningu sem :math:`\enot \forall x Gx`, sem væri lesin
sem „ekki er satt að: fyrir öll :math:`x`, :math:`x` er glatt“. Það er
svo ágæt þýðing á `[q.na] <#q.na>`__. Setningar `[q.en] <#q.en>`__ og
`[q.na] <#q.na>`__ eru því jafngildar.

*Það er mikilvægt að gleyma ekki breytunum þegar við þýðum setningar
yfir á táknmál umsagnarökfræði.* Táknrunur á borð við
„\ :math:`\exists Gx`\ “ eða „\ :math:`\forall Gx`\ “ eru *ekki* gildar.
Breytan tengir saman magnarann og umsögnina og án breytunnar við
magnarann rofna þessi tengsl. Þegar við kynnumst flóknari setningum, þá
sjáum við betur af hverju þetta er nauðsynlegt.

Yfirgrip
~~~~~~~~

Samkvæmt þýðingarlyklinum sem við höfum verið að nota er setningin
:math:`\forall x Gx` þýðing á „Allir eru glaðir“ En hverjir eru „allir“?
Þegar við notum svona setningar á mæltu máli, þá meinum við ekki að
allir á jörðinni séu glaðir, því síður að *allt í alheiminum* sé glatt.
Við eigum oftast við alla í einhverju tilteknu samhengi: alla í bekknum,
alla í veislunni, o.s.frv.

Í umsagnarökfræðinni leysum við úr þessari margræðni með því að
skilgreina . Yfirgripið er mengi allra þeirra hluta sem við erum að tala
um. Ef við viljum tala um alla á Akureyri, þá skilgreinum við yfirgripið
þannig að það sé mengi allra á Akureyri. Við skrifum þetta í upphafi
þýðingarlykilsins, svona:

.. container:: ekey

   Fólk á Akureyri

Við segjum að magnararnir *nái yfir* yfirgripið. Að þessu yfirgripi
gefnu, þá myndum við lesa „\ :math:`\forall x`\ “ sem „Allir á Akureyri
eru þannig að...“ og „\ :math:`\exists x`\ “ sem „Einhver á Akureyri er
þannig að...“

Í umsagnarökfræði verður yfirgripið að innihalda að minnsta kosti einn
hlut; það má ekki vera tómt. Þegar við komum að reglunum fyrir
náttúrulega afleiðslu í umsagnarökfræði í
§\ `[tomtyfirgrip] <#tomtyfirgrip>`__, þá munum við sjá af hverju.

Við getum ennfremur dregið þá ályktun í mæltu máli að einhver sé glaður
ef við vitum að Jón sé glaður, Jón er jú einhver. Við viljum því geta
dregið þá ályktun af „\ :math:`Gj`\ “ að „\ :math:`\exists x Gx`\ “.
Hvert nafn verður því að standa fyrir nákvæmlega einn hlut í yfirgripinu
(ekki engan og ekki fleiri en einn). Við getum ekki talað um fleira en
það sem er í yfirgripinu, svo ef við viljum segja eitthvað um annað fólk
en það sem býr á Akureyri, þá verðum við að skilgreina yfirgripið
þannig.

Magnarar ná yfir alla hluti í yfirgripinu, en þeir eru óháðir hverjum
öðrum. Hvað við eigum við með því sést ef til vill best með dæmi. Segjum
sem svo að yfirgripið sé krukka með bláum, gulum og rauðum marmarakúlum,
þar sem *B* stendur fyrir „er blá kúla“, *G* fyrir er „er gul kúla“ og
*R* fyrir „er rauð kúla“. Setningin :math:`\exists x Bx` er því sönn eff
að minnsta kosti ein kúla í krukkunni er blá.

En setningin :math:`\exists x \exists y (Bx \eand By`) segir *ekki* að
til séu að minnsta kosti tvær bláar kúlur í krukkunni, heldur það sama
og :math:`\exists x Bx`. Ástæðan er sú að *báðir* magnararnir ná yfir
allt yfirgripið og segja, hvor um sig, að til sé að minnsta kosti ein
blá kúla. *x* og *y* geta því vísað til sömu kúlunnar. Við getum hugsað
um þetta svona: Fyrst gáum við hvort að við getum fundið einhverja kúlu
sem er blá. Ef það tekst, þá er setningin sönn. Þetta samsvarar fyrri
magnaranum. Svo setjum við kúluna *aftur ofan í krukkuna* og endurtökum
leikinn fyrir seinni magnarann. Af því að kúlan er komin aftur ofan í
krukkuna, þá getur seinni magnarinn fundið hana.

Í §\ `4 <#sec.identity>`__ munum við svo fara yfir það hvernig við getum
þýtt setningar af þessu tagi.

.. _`s:MoreMonadic`:

Setningar með einum magnara
---------------------------

Nú höfum við kynnst öllum einingum setningarökfræðinnar. Til að þýða
setningar yfir á mál hennar þarf þó að kunna að blanda saman umsögnum,
nöfnum, mögnurum, breytum og setningatengjum. Þetta þarf að æfa
sérstaklega og við munum skoða mörg dæmi í því sem eftir er af þessum
kafla.

Að þýða hliðstæð lýsingarorð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Stundum standa lýsingarorð með fallorði (t.d. gult blóm) og þá þarf að
sýna sérstaka aðgát við þýðingu. Hér er dæmi sem liggur nokkuð beint
við:

.. container:: earg

   Skjóni er grár hestur.

Þessa setningu má umorða sem „Skjóni er grár og Skjóni er hestur“. Notum
eftirfarandi þýðingarlykil:

.. container:: ekey

   er grár

   er hestur

   Skjóni

Nú getum við þýtt setningu `[syn1] <#syn1>`__ sem :math:`Gs \eand Hs`.
Þetta er, eins og áður sagði, engum sérstökum vandkvæðum bundið.

En skoðum núna eftirfarandi setningar:

.. container:: earg

   Dúmbó er lítill fíll.

   Dúmbó er spendýr.

   Dúmbó er lítið spendýr.

Ef við ætluðum að fylgja dæminu um Skjóna hér að ofan, þá gætum við
reynt eftirfarandi þýðingarlykil:

.. container:: ekey

   er lítill

   er fíll

   er spendýr

   Dúmbó

Þá myndum við þýða setningu `[syn2] <#syn2>`__ sem :math:`Ld \eand Fd`,
setningu `[syn3] <#syn3>`__ sem :math:`Sd` og setningu
`[syn4] <#syn4>`__ sem :math:`Ld \eand Sd`. En þá lendum við í
vandræðum! Það myndi þýða að setningu `[syn4] <#syn4>`__ leiddi af
setningum `[syn2] <#syn2>`__ og `[syn3] <#syn3>`__. En svo er ekki.
Dúmbó er kannski lítill fíll, en hann er alveg ábyggilega stórt spendýr.
Setning `[syn2] <#syn2>`__ segir nefnilega að Dúmbó sé lítill *af fíl að
vera* þó að hann sé stór miðað við önnur spendýr. Við þurfum því að
finna aðrar umsagnir til að þýða „ er lítill fíll“ og „er lítið
spendýr“.

Það er hægt að finna mörg svipuð dæmi. Allir skíðagarpar eru manneskjur,
en sumir góðir skíðagarpar eru ekki góðar manneskjur. Ég er kannski
afleitur skákmaður, en það er þó ekki þar með sagt að ég sé afleitur að
öllu leyti eða yfirleitt. Þetta þýðir að þegar við þýðum setningar þar
sem lýsingarorð standa með einhverju öðru orði (lítill fíll, stór bíll,
góð manneskja, rautt hús) þá þurfum við að athuga vel hvort hægt sé að
þýða þau saman sem samtengingu eða ekki.

Algengar setningar með mögnurum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skoðum eftirfarandi setningar:

.. container:: earg

   Allir smápeningarnir sem ég er með í vasanum eru fimmtíukallar.

   Einhver af smápeningunum á borðinu er tíkall.

   Ekki allir smápeningarnir á borðinu eru tíkallar.

   Enginn af smápeningunum sem ég er með í vasanum er tíkall.

Þegar við skilgreinum þýðingarlykil í umsagnarökfræði, þá þurfum við að
tilgreina yfirgrip. Hér erum við að tala um smápeninga sem ég er með í
vasanum, svo yfirgripið verður að minnsta kosti að innihalda þá. Við
erum ekki að tala um neitt annað en smápeninga heldur, svo við getum
látið yfirgripið ná yfir alla smápeninga. Við þurfum ekki að tilgreina
nein nöfn, því við minnumst ekki á neina einstaka peninga. Hér er þá
þýðingarlykillinn:

.. container:: ekey

   allir smápeningar

   er í vasanum á buxunum sem ég er í

   er á borðinu

   er fimmtíukall

   er tíkall

Setningu `[quan1] <#quan1>`__ er eðlilegast að þýða með almagnara. En
fyrst þurfum við að gæta að því að almagnarinn segir eitthvað um *allt*
í yfirgripinu—alla smápeninga—ekki bara þá sem smápeninga sem ég er með
í vasanum. Við leysum þetta með að segja sem svo að *ef* ég er með
eitthvað í vasanum, *þá* er það fimmtíukall. Við munum sjá
skilyrðissetningar notaðar svona með almögnurum aftur og aftur.

Við getum því þýtt setninguna yfir á táknmál umsagnarökfræði svona:
:math:`\forall x(Px \eif Qx)` og lesum hana sem „fyrir öll *x*, ef *Px*,
þá *Qx*\ “. Við getum líka hugsað um merkingu hennar svona, og
hugsanlega er það hjálplegt fyrir marga: „veldu hvað sem er úr
yfirgripinu, ef *það* er í vasanum á buxunum sem ég er í, þá er það
fimmtíukall“. Ef það er satt, þá hlýtur það að vera að allir smápeningar
sem ég er með í vasanum séu fimmtíukallar.

Setning `[quan1] <#quan1>`__ fjallar um smápeninga sem bæði eru í vasa
mínum og eru fimmtíukallar, og því gæti verið freistandi að reyna að
þýða hana sem samtengingu. En setningin :math:`\forall x(Px \eand Qx)`
hefur í raun gjörólíka merkingu. Hún segir um allt í yfirgripinu að það
séu bæði fimmtíukallar og í vasanum hjá mér, og þar sem yfirgripið er
allir fimmtíukallar, þá væri það jafngilt því að segja „allir
smápeningar eru fimmtíukallar sem ég er með í vasanum.“ Það er allt
annað—og alveg greinilega ósatt. Þess vegna höfum við: Hér er þörf á
stuttri athugasemd. Þegar við fjölluðum um setningarökfræðina notuðum
við feitletraða stafi sem stóðu fyrir hvaða setningu sem er á máli
setningarökfræði. Hér þurfum við hins vegar á einhverjum rithætti að
halda sem leyfir okkur að tala um hvaða *umsögn* sem er. Hér notum við
sömu aðferð og látum samhengið skera úr um hvort átt er við setningar
eða umsagnir.

Setningu `[quan2] <#quan2>`__ er eðlilegast að þýða með
tilvistarmagnara. Hægt er að umorða hana sem „til er einhver smápeningur
sem er á borðinu og er tíkall“. Hana þýðum við því sem
:math:`\exists x(Tx \eand Dx)`.

Takið eftir því að við þurftum að nota skilyrðissetningu þegar við
þýddum setninguna með almagnaranum, en samtengingu með
tilvistarmagnaranum. Hvað ef við hefðum skrifað í staðinn
„\ :math:`\exists x(Tx \eif Dx)`\ “? Það hefði merkt að til væri einhver
hlutur *x* í yfirgripinu sem er þannig að :math:`(Tx \eif Dx)` er satt
um *x*. Með öðrum orðum, það er til einhver smápeningur sem er þannig að
ef *hann* er á borðinu, þá er hann tíkall. Munum að í
setningarökfræðinni, þá er :math:`\meta{A} \eif \meta{B}` rökfræðilega
jafngilt :math:`\enot\meta{A} \eor \meta{B}`. Þetta jafngildi er líka
til staðar í umsagnarökfræði. Það þýðir að
:math:`\exists x (Tx \eif Dx)` er satt ef til er einhver hlutur *x* í
yfirgripinu sem er þannig að :math:`(\enot Tx \eor Dx)` er satt um *x*.
Með öðrum orðum, :math:`\exists x (Tx \eif Dx)` er satt ef einhver
smápeningur er *annað hvort* ekki á borðinu eða er tíkall. Það er mjög
auðvelt fyrir þessa setningu að vera sanna, enda eru margir smápeningar
ekki á borðinu—þeir eru raunar út um allt. Skilyrðissetningar sem eru
innan sviðs tilvistarmagnara er því í raun ekki mjög gagnlegar og best
að forðast þær, nema við séum viss um hvað við erum að gera.

Við getum umorðað setningu `[quan3] <#quan3>`__ sem „það er ekki satt að
allir smápeningar á borðinu séu tíkallar“. Ef við höfum í huga þýðingu
okkar á `[quan1] <#quan1>`__, þá liggur beint við að þýða
`[quan3] <#quan3>`__ sem :math:`\enot \forall x(Tx \eif Dx)`. En við
gætum litið svo á að eðlilegast væri að umorða `[quan3] <#quan3>`__ sem
„einhver smápeningur á borðinu er ekki tíkall“ (ef það er ekki satt að
þeir séu allir tíkallar, þá hlýtur jú að minnsta kosti einn að vera ekki
tíkall). Við myndum þá þýða það yfir á táknmál umsagnarökfræði sem
:math:`\exists x(Tx \eand \enot Dx)`.

Það er ekki augljóst á þessu stigi málsins, en þessar setningar eru
rökfræðilega jafngildar. Það er vegna þess að
:math:`\enot\forall x\meta{A}` and :math:`\exists x\enot\meta{A}` eru
rökfræðilega jafngildar, sem og setningarnar
:math:`\enot(\meta{A}\eif\meta{B})` og
:math:`\meta{A}\eand\enot\meta{B}`. [2]_

Hægt er að umorða setningu `[quan4] <#quan4>`__ sem „það er ekki satt að
ég sé með tíkall í vasanum“. Við getum þýtt þetta yfir á mál
umsagnarökfræði sem :math:`\enot\exists x(Px \eand Dx)`. Við gætum líka
gripið til orðalags sem passar illa við mælt mál og sagt „Allt sem ég er
með í vasanum er ekki-tíkall“ og því þýtt setninguna sem
:math:`\forall x(Px \eif \enot Dx)`. Þessar tvær setningar eru
rökfræðilega jafngildar og þær eru báðar jafn góðar sem þýðingar á
setningu `[quan4] <#quan4>`__.

.. _tomarumsagnir:

Tómar umsagnir
~~~~~~~~~~~~~~

Í §\ `1 <#s:FOLBuildingBlocks>`__ lögðum við áherslu á að hvert nafn
nefnir nákvæmlega einn hlut í yfirgripinu; aldrei fleiri en einn og
alltaf að minnsta kosti einn. Öðru máli gegnir um umsagnir, við gerum
enga kröfu um að þær eigi við eitthvað í yfirgripinu . Þá segjum við að
þær séu . Skoðum þetta aðeins betur.

Segjum að við viljum þýða eftirfarandi tvær setningar yfir á táknmál
umsagnarökfræði:

.. container:: earg

   Allir apar kunna að tefla.

   Sumir apar kunna að tefla.

Við getum notað eftirfarandi þýðingarlykil:

.. container:: ekey

   dýr

   er api.

   kann að tefla.

Setningu `[monkey1] <#monkey1>`__ er þá hægt að þýða sem
:math:`\forall x(Ax \eif Tx)` og setningu `[monkey2] <#monkey2>`__ sem
:math:`\exists x(Ax \eand Tx)`.

Það er óneitanlega freistandi að segja að setningu
`[monkey2] <#monkey2>`__ leiði af setningu `[monkey1] <#monkey1>`__. Það
er að segja, við gætum haldið að það væri ómögulegt að allir apar kunni
að tefla, nema sumir apar kunni að tefla. En þetta væru mistök, að
minnsta kosti í rökfræði, ef ekki í mæltu máli. Það er nefnilega
mögulegt að setningin :math:`\forall x(Ax \eif Tx)` sé sönn, jafnvel þó
að setningin :math:`\exists x(Ax \eand Tx)` sé ósönn.

Hvernig má það vera? Svarið er fólgið í því hvað myndi gerast ef *það
væru engir apar*. Ef það eru engir apar í yfirgripinu, þá væri setningin
:math:`\forall x(Ax \eif Tx)` sönn, en þó þannig að það er ekkert
sérstakt sem gerir hana sanna: það skiptir engu máli hvaða apa þú velur,
hann kann að tefla! En hið sama gildir ekki um
:math:`\exists x(Mx \eand Sx)`, enda væri hún ósönn ef engir apar eru í
yfirgripinu.

En af hverju ekki að segja bara að setning eins og
:math:`\forall x(Ax \eif Tx)` sé ósönn ef umsögnin í forliðnum er tóm?
Þetta tengist að sjálfsögðu skilyrðissetningum og hversu furðulegar þær
eru. Ef enginn api er í yfirgripinu, þá er umsögnin „ er api“ ekki sönn
um neinn hlut í yfirgripinu. Forliðurinn í skilyrðissetningunni er því
alltaf ósannur, og skv. skilgreiningarsanntöflunni fyrir skilyrðisstengi
eru skilyrðissetningar með ósönnum forlið alltaf sannar. Slík setning
hlýtur því alltaf að vera sönn.

Önnur, og skyld ástæða, er sú að við höfum sömu ályktunarreglur og við
höfðum í setningarökfræði í umsagnarökfræði. Við getum sannað í
setningarökfræði að :math:`\forall x(Ax \eif Tx)` og
:math:`\forall x(\enot Tx \eif \enot Ax)` séu sannanlega jafngildar
setningar. Sú seinni segir að fyrir öll dýr *x*, gildi að ef *x* kann
ekki að tefla, þá er *x* ekki api—og er sjálf jafngild
:math:`\enot \exists x (\enot Tx \eand Ax)` eins og við munum geta
sannað í næsta kafla.

Þar sem þessar þrjár setningar eru sannanlega jafngildar, þá viljum við
að þær séu sannar (og ósannar) undir sömu kringumstæðum. Hvenær eru
þessar setningin svo ósannar? Jú, ef til er eitthvað dýr sem kann ekki
að tefla og er api. En það eru engir apar—setningarnar geta því ekki
verið ósannar, og hljóta því allar að vera sannar. Það leiðir því
einfaldlega til mótsagnar að gefa sér að setning á borð við
:math:`\forall x(Ax \eif Tx)` sé ósönn, ef *A* er tóm umsögn.

Hvernig á að velja yfirgrip?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Þegar við þýðum setningu af mæltu máli yfir á táknmál umsagnarökfræði,
þá er þýðingarlykillinn óaðskiljanlegur hluti þýðingarinnar og oft getur
verið vandasamt að velja réttan lykil. Segjum til dæmis að við viljum
þýða eftirfarandi setningu:

.. container:: earg

   Engin er rós án þyrna.

Við gætum prófað eftirfarandi þýðingarlykil:

.. container:: ekey

   er rós

   hefur þyrna

„Enginn er rós án þyrna“ merkir það sama og „allar rósir hafa þyrna“.
Það væri þá freistandi að reyna að þýða
`[pickyfirgriprose] <#pickyfirgriprose>`__ sem
:math:`\forall x(Rx \eif Tx)`. En við höfum ekki enn tilgreint yfirgrip.
Ef yfirgripið innihéldi allar rósir, þá væri þetta góð þýðing. En ef
yfirgripið væri, til dæmis, *allir hlutir á skrifborðinu mínu*, þá myndi
:math:`\forall x(Rx \eif Tx)` segja að allar rósir sem eru á
skrifborðinu mínu hafi þyrna og það er ekki alveg það sem við erum að
reyna að tjá með upprunalegu setningunni. Ef það væru svo engar rósir á
skrifborðinu mínu, sem raunar eru tilfellið þegar þessi orð eru skrifuð,
þá væri setningin sönn, af engri ástæðu annarri en að yfirgripið er
tómt. Það er ekki það sem við erum á höttunum eftir. Til að þýða
setninguna sómasamlega þurfum við því að gæta að því að yfirgripið
innihaldi allar rósir.

En hér höfum við tvo möguleika. Í fyrsta lagi gætum við reynt að
takmarka yfirgripið við allar rósir, en *bara* rósir. Þá gætum við þýtt
`[pickyfirgriprose] <#pickyfirgriprose>`__ einfaldlega sem
:math:`\forall x Tx`. Þetta er satt eff (takið eftir því að hér eru tvö
eff!) allt í yfirgripinu hefur þyrna, og fyrst yfirgripið inniheldur
bara rósir, þá er þessi setning sönn eff allar rósir hafa þyrna,
þ.e. eff engin er rós án þyrna. Með því að takmarka yfirgripið með
þessum hætti, þá getum við því einfaldað þýðinguna töluvert, en þó bara
ef allar setningar sem við viljum þýða yfir á táknmál umsagnarökfræði í
þetta skiptið eru um rósir og ekkert annað en rósir.

Í öðru lagi gætum við látið yfirgripið ná yfir fleiri hluti: fífla,
fiðrildi, Framsóknarmenn, hvað sem er. Í það minnsta verður yfirgripið
að vera stærra ef við viljum til dæmis þýða eftirfarandi setningu á sama
tíma og `[pickyfirgriprose] <#pickyfirgriprose>`__:

.. container:: earg

   Allar kisur dansa tangó.

Nú verður yfirgripið að innihalda bæði allar rósir (svo við getum þýtt
setninguna `[pickyfirgriprose] <#pickyfirgriprose>`__) og allar kisur
(svo við getum þýtt `[pickyfirgripcowboy] <#pickyfirgripcowboy>`__). Við
gætum þá reynt að nota eftirfarandi þýðingarlykil:

.. container:: ekey

   dýr og plöntur

   er kisa

   dansar tangó

   er rós

   hefur þyrna

Nú verðum við að þýða `[pickyfirgriprose] <#pickyfirgriprose>`__ sem
:math:`\forall x (Rx \eif Tx)`, þar sem :math:`\forall x Tx` myndi
merkja „öll dýr og allar plöntur hafa þyrna“. Það sama gildir um
`[pickyfirgripcowboy] <#pickyfirgripcowboy>`__; hún er best þýdd sem
:math:`\forall x (Kx \eif Dx)`. Lexían er: yfirgripið ákvarðar hvernig
við getum þýtt setningar yfir á táknmál setningarökfræði.

Gagnsemi umorðunar
~~~~~~~~~~~~~~~~~~

Þegar við þýðum setningar yfir á mál umsagnarökfræði er mikilvægt að
átta sig vel á uppbyggingu setninganna sem við viljum þýða. Stundum
getum við farið beint úr upprunalegu setningunni yfir í einhverja
setningu á máli umsagnarökfræði, en stundum er gagnlegt að umorða
setninguna, einu sinni eða oftar, þannig að við eigum hægara með að þýða
hana yfir á táknmál umsagnarökfræði. Stundum er best að gera þetta í
skrefum þannig að hver umorðun færi okkur nær og nær einhverju sem við
getum svo þýtt.

Í næstu dæmum munum við nota þennan þýðingarlykil:

.. container:: ekey

   fólk

   er bassaleikari

   er rokkstjarna

   Anna

Skoðum nú þessar setningar:

.. container:: earg

   Ef Anna er bassaleikari, þá er hún rokkstjarna.

   Ef manneskja er bassaleikari, þá er hún rokkstjarna.

Hérna eru bakliðirnir báðir eins í setningum `[pronoun1] <#pronoun1>`__
og `[pronoun2] <#pronoun2>`__ („\ :math:`\ldots` hún er rokkstjarna“) en
þeir hafa mjög ólíka merkingu. Við getum dregið þetta fram með að umorða
upprunalegu setningarnar þannig að engin fornöfn komi lengur fyrir í
þeim.

Við getum þá til dæmis umorðað setningu `[pronoun1] <#pronoun1>`__ sem
„Ef Anna er bassaleikari, þá er Anna rokkstjarna“. Við getum þýtt hana
sem :math:`Ba \eif Ra`.

Við verðum að umorða setningu `[pronoun2] <#pronoun2>`__ á annan hátt,
nefnilega sem „Ef manneskja er bassaleikari, þá er *sú manneskja*
rokkstjarna“. Þessi setning er ekki um neina tiltekna manneskju, svo við
vitum að við þurfum að nota breytu einhvers staðar. Til bráðabirgða
getum við því umorðað hana sem „fyrir hvaða manneskju *x*, ef *x* er
manneskja, þá er *x* rokkstjarna“. Orðalagið „fyrir allar manneskjur
*x*\ “ merkir hér bara það að það skiptir ekki máli hvaða manneskju úr
yfirgripinu við veljum, það sem á eftir kemur á við hana, og við notum
breytuna *x* hér í staðinn fyrir fornafn. Nú getum við loks þýtt þessa
setningu sem :math:`\forall x (Bx \eif Rx)`. Þetta er sama setning og
við myndum hafa notað til að þýða „Allir sem eru bassaleikarar eru
rokkstjörnur“ og er greinilega sönn eff setning
`[pronoun2] <#pronoun2>`__ er sönn.

Skoðum nú þessar setningar:

.. container:: earg

   Ef einhver er bassaleikari, þá er Anna rokkstjarna.

   Ef einhver er bassaleikari, þá er hún rokkstjarna.

Hér eru forliðirnir eins („Ef einhver er
bassaleikari\ :math:`\ldots`\ “). En það getur verið ansi snúið að finna
út úr því hvernig best er að þýða þessar setningar. Hér kemur umorðun
aftur að gagni.

Við getum umorðað setningu `[anyone1] <#anyone1>`__ sem „Ef það er til
að minnsta kosti einn bassaleikari, þá er Anna rokkstjarna“. Við sjáum
því að þetta er skilyrðissetning þar sem forliðurinn er setning með
magnara. Við getum því þýtt hana svona, þar sem skilyrðistengið er
aðaltengið: :math:`\exists x Bx \eif Ra`. Takið eftir því að hér er svið
magnarans *ekki* öll setningin, heldur bara forliðurinn. Við munum tala
betur um svið magnara í §\ `2.6 <#s:quantscope>`__ hér fyrir neðan.

Setningu `[anyone2] <#anyone2>`__ er svo hægt að umorða sem „fyrir allt
fólk *x*, ef *x* er bassaleikari, þá er *x* rokkstjarna“. „Hún“ í
bakliðnum vísar til „einhvers“, hver sem það er, og umorðunin dregur
þetta fram. Þessa setningu mætti svo umorða frekar á eðlilegra mál sem
„Allir bassaleikarar eru rokkstjörnur“ og hana má greiðlega þýða sem
:math:`\forall x(Bx \eif Rx)`, rétt eins `[pronoun2] <#pronoun2>`__.

Lexían hér er að ef við reynum að þýða setningar af mæltu máli sem
innihalda orð eins og „einhver“, „sérhver“ og fleiri í þessum dúr, þá
þurfum við að nota magnara. En það getur stundum verið erfitt að sjá
hvort nota á tilvistar- eða almagnara og þá er gott að umorða setninguna
þannig að slík orð komi ekki fyrir.

.. _`s:quantscope`:

Svið magnara
~~~~~~~~~~~~

Notum nú sama þýðingarlykil og skoðum eftirfarandi setningar:

.. container:: earg

   Ef allir eru bassaleikarar, þá er Felix bassaleikari.

   Um alla gildir að ef þeir eru bassaleikarar, þá er Felix
   bassaleikari.

Felix hefur ekki verið í þýðingarlyklinum okkar til þessa, svo við bætum
við nýju nafni í þýðingarlykilinn:

.. container:: ekey

   Felix

Setning `[qscope1] <#qscope1>`__ er skilyrðissetning með bakliðinn
„allir eru bassaleikarar“. Þá þýðum við hana sem
:math:`\forall x Bx \eif Bb`. Þessi setning er *nauðsynlega* sönn: ef
*allir* eru bassaleikarar, þá hlýtur Felix að vera það líka. Ef hann
væri ekki bassaleikari, þá væri það jú ósatt að allir séu bassaleikarar.

Setningu `[qscope2] <#qscope2>`__ mætti hins vegar best umorða sem
„allar manneskjur *x* eru þannig að ef *x* er bassaleikari, þá er Felix
bassaleikari“. Það er að segja, skilyrðissetning á forminu
:math:`Bx \eif Bb` er sönn, sama hvað við setjum inn fyrir *x*. Þetta
getum við táknað á máli umsagnarökfræði sem
:math:`\forall x (Bx \eif Bb)`. Þessi setning er ósönn, ef Felix er ekki
bassaleikari. Til dæmis er Anna bassaleikari, svo :math:`Ba` er sönn. En
Felix er ekki bassaleikari, svo :math:`Bb` er ósönn. Þá er setningin
:math:`Ba \eif Bb` ósönn, og því til að minnsta kosti ein manneskja í
yfirgripinu sem hún er ósönn um, nefnilega Önnu.
:math:`\forall x (Bx \eif Bb)` er því ósönn líka.

Þetta dæmi er dálítið erfitt, svo það er hugsanlega þess virði að skoða
það aðeins betur. Setningin :math:`\forall x (Bx \eif Bb)` segir að
skilyrðissetningin sem er innan sviga sé sönn fyrir öll *x*.
Skilyrðissetning er ósönn ef forliðurinn er sannur og bakliðurinn
ósannur. Til að sýna að þessi setning sé ósönn, þá þurfum við því að
finna slíkt dæmi, þar sem forliðurinn er sannur, en bakliðurinn ósannur.
Við fundum slíkt dæmi, þar sem Felix er ekki bassaleikari, en Anna er
bassaleikari. Þetta hefur auðvitað þær skrýtnu afleiðingar að ef Felix
*er* bassaleikari, þá gildir það um allar manneskjur *x* að ef *x* er
bassaleikari, þá er Felix bassaleikari, því eins og við vitum með að
skoða skilgreiningarsanntöfluna fyrir skilyrðistengið, þá er
skilyrðisetning alltaf sönn ef bakliðurinn er sannur.

Það sem þessi tvö dæmi eiga að sýna er að :math:`\forall x Bx \eif Bb`
og :math:`\forall x (Bx \eif Bb)` eru mjög ólíkar setningar. Munurinn
hefur að gera með *svið* magnarans í hvorri setningu. Svið magnara er
mjög líkt sviði neitunar sem við skoðuðum þegar setningarökfræðin var
til umfjöllunar og það er gagnlegt að skoða magnarana á svipaðan hátt.

Í setningunni :math:`\enot Ba \eif Bb` er svið „\ :math:`\enot`\ “ bara
forliður skilyrðissetningarinnar. Hún merkir því eitthvað á borð við: ef
:math:`Ba` er ósönn, þá er :math:`Bb` sönn. Á sama hátt er svið
„\ :math:`\forall x`\ “ í setningunni :math:`\forall x Bx \eif Bb` bara
forliður skilyrðissetningarinnar. Hún merkir eitthvað á borð við ef
:math:`Bx` er satt um *allt*, þá er :math:`Bb` líka satt.

Í setningunni :math:`\enot(Bk \eif Bb)` er svið „\ :math:`\enot`\ “ hins
vegar öll setningin. Hún segir að *öll* setningin :math:`(Bk \eif Bb)`
sé ósönn. Það sama gildir um magnarann í :math:`\forall x (Bx \eif Bb)`,
svið hans er öll setningin. Hún segir því að skilyrðissetningin
:math:`(Bx \eif Bb)` sé sönn um *allt*.

Við þurfum því að sýna töluverða varkárni þegar kemur að því að þýða
skilyrðissetningar og við þurfum að passa að við höfum skilið svið
magnarans rétt.

Hér eru allar þær rökhendur sem Aristóteles og eftirmenn hans
uppgötvuðu, ásamt þeim nöfnum sem þær gengu undir á miðöldum:

.. container:: ebullet

   **Barbara.** Öll G eru F. Öll H er G. Þar af leiðandi: Öll H eru F.

   **Celarent.** Engin G eru F. Öll H eru G. Þar af leiðandi: Engin H
   eru F.

   **Ferio.** Engin G eru F. Sum H eru G. Þar af leiðandi: Sum H eru
   ekki F.

   **Darii.** Öll G eru F. Sum H eru G. Þar af leiðandi: Sum H er F.

   **Camestres.** Öll F eru G. Engin H eru G. Þar af leiðandi: Engin H
   eru F.

   **Cesare.** Engin F eru G. Öll H eru G. Þar af leiðandi: Engin H eru
   F.

   **Baroko.** Öll F eru G. Sum H eru ekki G. Þar af leiðandi: Sum H eru
   ekki F.

   **Festino.** Engin F eru G. Sum H eru G. Þar af leiðandi: Sum H eru
   ekki F.

   **Datisi.** Öll G eru F. Sum G eru H. Þar af leiðandi: Sum H eru F.

   **Disamis.** Sum G eru F. Öll G eru H. Þar af leiðandi: Sum H eru F.

   **Ferison.** Engin G eru F. Sum G eru H. Þar af leiðandi: Sum H eru
   ekki F.

   **Bokardo.** Sum G eru ekki F. Öll G eru H. Þar af leiðandi: Sum H
   eru ekki F.

   **Camenes.** Öll F eru G. Engin G eru H Þar af leiðandi: Engin H eru
   F.

   **Dimaris.** Sum F eru G. Öll G eru H. Þar af leiðandi: Sum H eru F.

   **Fresison.** Engin F eru G. Sum G eru H. Þar af leiðandi: Sum H eru
   ekki F.

| Þýðið þessar rökfærslur yfir á táknmál umsagnarökfræði.
|  Notið þennan þýðingarlykil til að þýða setningarnar hér að neðan yfir
  á táknmál umsagnarökfræði:

.. container:: ekey

   fólk

   kann talnalykilinn sem gengur að peningaskápnum

   er njósnari

   er grænmetisæta

   Hafþór

   Ingimar

.. container:: earg

   Hvorki Hafþór né Ingimar eru grænmetisætur.

   Enginn njósnari kann talnalykilinn em gengur að peningaskápnum

   Enginn kann talnalykilinn að peningaskápnum nema Ingimar kunni hann.

   Hafþór er njósnari, en enginn grænmetisæta er njósnari.

Notið þennan þýðingarlykil til að þýða setningarnar hér að neðan yfir á
táknmál umsagnarökfræði:

.. container:: ekey

   öll dýr

   er krókódíll.

   er api.

   er skriðdýr.

   býr í Húsdýragarðinum.

   Alli

   Bibbi

   Dísa

.. container:: earg

   Alli, Bibbi og Dísa búa öll í Húsdýragarðinum.

   Bibbi er skriðdýr, en ekki krókódíll.

   Sum skriðdýr búa í Húsdýragarðinum.

   Allir krókódílar eru skriðdýr.

   Öll dýr sem búa í Húsdýragarðinum eru annað hvort apar eða krókódílar

   Til eru skriðdýr sem eru ekki krókódílar.

   Ef eitthvað dýr er api, þá er það Alli.

   Ef eitthvað dýr er krókódíll, þá er það skriðdýr.

Búið til þýðingarlykil fyrir hverja rökfærslu hér að neðan og þýðið svo
yfir á táknmál umsagnarökfræði. Hugleiðið hvort rökfærslurnar séu
gildar.

.. container:: earg

   Júlía er rökfræðingur. Allir rökfræðingar ganga um í furðufötum. Þar
   af leiðandi gengur Júlía um í furðufötum.

   Ég tek eftir öllu á skrifborðinu mínu. Það er rós á skrifborðinu
   mínu. Það er því til rós sem ég tek eftir.

   Allt sem mig dreymir er í svart-hvítu. Gamlir sjónvarpsþættir eru í
   svart-hvítu. Þar af leiðandi er sumt sem mig dreymir gamlir
   sjónvarpsþættir.

   Hvorki Bjarni né Katrín hafa komið til Ástralíu. Enginn gæti séð
   kengúru nema hann hafi komið til Ástralíu eða í dýragarð. Þó að
   Bjarni hafi aldrei séð kengúru, þá hefur Katrín gert það. Þar af
   leiðandi hefur Katrín komið í dýragarð.

   Enginn verður óbarinn biskup. Enginn veit sína ævina fyrr en öll er.
   Þar af leiðandi, sá sem veit sína ævina fyrr en öll er verður barinn
   biskup.

   Öll smábörn eru óvitar. Enginn sem er óviti kann að stýra skipi.
   Tómas er smábarn. Þar af leiðandi kann Tómas ekki að stýra skipi.

.. _`s:MultipleGenerality`:

Setningar með fleiri en einum magnara
-------------------------------------

Fram að þessu höfum við bara skoðað setningar með einum magnara og
einsæta umsögnum. Umsagnarökfræðin nær þó ekki fullum mætti fyrr en við
kynnum margsæta umsagnir til sögunnar og setningar sem nota fleiri en
einn magnara.

Margsæta umsagnir
~~~~~~~~~~~~~~~~~

Allar þær umsagnir sem skoðuðum í fyrri kafla höfðu að gera með
eiginleika hluta. Umsagnirnar höfðu því eina eyðu og til að búa til
setningu þurftum við bara að fylla eyðuna með einu nafni. Þetta voru
svokallaðar umsagnir, því þær hafa eina eyðu, eða „sæti“.

En við getum líka skilgreint umsagnir sem hafa að gera með *tengsl*
milli tveggja hluta. Hér eru nokkur dæmi um slíkar umsagnir í setningum
á mæltu máli:

   |  elskar
   |  er til vinstri við
   |  skuldar  peninga

Þetta eru umsagnir. Við þurfum að fylla eyðurnar í þeim með tveimur
nöfnum til að búa til setningar. Við getum búið til slíkar umsagnir með
því að taka venjulegar íslenskar setningar sem innihalda mörg nöfn og
fjarlægt nöfnin eitt af öðru til að búa til tvísæta umsagnir. Tökum sem
dæmi setninguna sem við skoðuðum hér að ofan, „Anna fékk lánaðan bílinn
hjá Jóni“. Með því að fjarlægja tvö nöfn úr þessari setningu (og munið
að við lítum á orð eða orðasambönd sem vísa til eins hlutar, eins og
„bíllinn“ sem nöfn) getum við búið til þrjár tvísæta umsagnir.

   | Anna fékk lánaðan  hjá
   |  fékk lánaðan bílinn hjá
   |  fékk lánaðan  hjá Jóni

Og ef við fjarlægjum öll þrjú nöfnin í einu, þá fáum við umsögn:

    fékk lánaðan  hjá

Það eru engin mörk á hversu mörg sæti umsögn getur haft og við segjum að
umsögn sem hefur fleiri en eitt sæti sé .

Vandinn við eyður
~~~~~~~~~~~~~~~~~

Hér að ofan notuðum við sama táknið, „“, til að tákna eyður í setningum
sem urðu til við að nöfn voru fjarlægð úr þeim. En eins og Frege kenndi
okkur, þá eru ekki allar eyður sama eyðan. Við getum fyllt tvær eyður
með sama nafninu, en við getum líka sett inn mismunandi nöfn í
mismunandi röð. Hér fyrir neðan eru þrjár setningar sem hafa verið
fylltar með nöfnum á mismunandi hátt, og hafa allar mismunandi merkingu:

.. container:: earg

   Karl elskar Imre.

   Imre elskar Karl.

   Karl elskar Karl.

Við þurfum sem sagt einhvern veginn að henda reiður á því hvaða eyða er
hvað svo við getum vitað hvernig við fyllum þær af nöfnum. Við gerum það
einfaldlega með því að númera eyðurnar. Segjum til dæmis að við viljum
þýða setningarnar hér að ofan yfir á táknmál umsagnarökfræði. Við gætum
þá notað eftirfarandi þýðingarlykil:

.. container:: ekey

   fólk

   Imre

   Karl

   elskar

Þegar við þýðum setningar með fleiri en einni umsögn, þá setjum við
nöfnin öll í röð eftir umsögninni, í þeirri röð sem við viljum að þau
fari í eyðurnar. Setning `[terms3] <#terms3>`__ væri þá þýtt sem
:math:`Lki`, því :math:`k` á að fara í fyrstu eyðuna og :math:`i` í þá
seinni. Setning `[terms3b] <#terms3b>`__ væri þá þýdd sem :math:`Lik` og
setning `[terms3a] <#terms3a>`__ sem :math:`Lkk`. Hér eru nokkrar aðrar
setningar sem við getum þýtt með sama þýðingarlykli:

.. container:: earg

   Imre elskar sjálfan sig.

   Karl elskar Imre, en það er ekki gagnkvæmt.

   Karl er elskaður af Imre.

Við getum umorðað `[terms4] <#terms4>`__ sem „Imre elskar Imre“ og því
þýtt hana sem :math:`Lii`. Setning `[terms5] <#terms5>`__ er samtenging.
Við getum umorðað hana sem „Karl elskar Imre, en Imre elskar ekki Karl“
og því þýtt hana sem :math:`Lki \eand \enot Lik`. Setningu
`[terms6] <#terms6>`__ má umorða sem „Imre elskar Karl“, og því getum
við þýtt hana sem :math:`Lik`. Við að þýða síðustu setninguna höfum við
tapað einhverjum af þeim blæbrigðum sem þolmyndin tjáir, en engu að
síður höfum við náð merkingunni réttri.

En þessar tvær setningar, „Imre elskar Karl“ og „Karl er elskaður af
Imre“, draga fram nokkuð mikilvægt. Prófum að bæta eftirfarandi umsögn
við þýðingarlykilinn okkar:

.. container:: ekey

   elskar

:math:`M` notar nákvæmlega sömu orð og :math:`L` hér að ofan. *En við
höfum víxlað eyðunum!* (Skoðið bara lágvísana gaumgæfilega.) Þetta
skiptir máli.

Af hverju? Af því að þegar við sjáum setningu á borð við :math:`Lki`, þá
eigum við að taka *fyrsta* nafnið (þ.e. :math:`k`) og tengja það sem það
vísar til (þ.e. Karl) við eyðuna sem *merkt* er :math:`1`, taka *annað*
nafnið (þ.e. :math:`i`) og tengja það sem það vísar til (þ.e. Imre) við
eyðuna sem er merkt með :math:`2`. Þá fáum við setninguna „Karl elskar
Imre“. Ef við gerum þetta sama fyrir umsögnina :math:`M`, þá fáum við
setningina „Imre elskar Karl“ (af því að við höfum víxlað eyðunum).

Þar af leiðir að :math:`Lik` og :math:`Mki` eru *báðar* þýðingar á
setningunni „Imre elskar Karl“, en :math:`Lki` og :math:`Mik` eru báðar
þýðingar á „Karl elskar Imre“.

Hér er annað dæmi. Segjum að við bætum eftirfarandi umsögn við
þýðingarlykilinn okkar:

.. container:: ekey

   líkar betur við en

Þá er setningin :math:`Nik` þýðing á „Imre líkar betur við Imre en Karl“
og :math:`Nki` er þýðing á „Karli líkar betur við Karl en Imre“. Af
hverju? Af því að fyrstu tvær eyðurnar eru sama eyðan! Við hefðum getað
einfaldað þetta með að skilgreina :math:`N` sem

.. container:: ekey

   líkar betur við sjálfan sig en

Lexían hér er einföld: *Þegar við vinnum með margsæta umsagnir verðum
við að gæta að röð eyðanna!*

Röð magnara
~~~~~~~~~~~

Skoðum setningana „allir elska einhvern“. Þessi setning er tvíræð. Hún
gæti merkt annað af tvennu:

.. container:: earg

   Sérhver manneskja er þannig að til er einhver sem viðkomandi elskar.

   Það er til einhver tiltekin manneskja sem er þannig að allir elska þá
   manneskju.

Fyrri setningin segir sem sagt að það skiptir engu máli hvaða manneskju
við veljum, það er til einhver önnur manneskja sem hún elskar. Sú seinni
segir að það sé til einhver ein manneskja sem allir elska, þar með talið
hún sjálf. Við getum þýtt `[lovecycle] <#lovecycle>`__ sem
:math:`\forall x \exists y Lxy`. Hún væri til dæmis sönn ef yfirgripið
okkar innihéldi þrjár manneskjur, Imre, Ludwig og Karl og staða ástamála
milli þeirra væri þannig að Karl elskaði Imre, en ekki Ludwig, að Imre
elskaði Ludwig, en ekki Karl, og að Ludwig elskaði Karl, en ekki Imre.

Við getum þýtt `[loveconverge] <#loveconverge>`__ með setningunni
:math:`\exists y \forall x Lxy`. Hún er *ekki* sönn, ef ástandið er eins
og lýst er að ofan. Til þess þyrftu allir í yfirgripinu, Imre, Ludwig og
Karl, að elska einhvern einn þeirra.

Það sem þetta dæmi sýnir er að röð magnara skiptir mjög miklu máli:
þessar tvær setningar eru eins að öllu leyti, nema að magnararnir koma
fyrir í mismunandi röð, og þó er merking þeirra gerólík. Í raun er það
eitt helsta gagnið sem hægt er að hafa af formlegri rökfræði að skýra
merkingu setninga á mæltu máli sem eru best þýddar með mörgum mögnurum.
Slíkar setningar eru oft mjög óskýrar og uppspretta ýmissa rökvillna.
Hér er dæmi sem finnst til að mynda í heimspekisögunni:

.. container:: earg

   Hver og einn er þannig að það er einhver sannleikur sem hann veit
   ekki. (:math:`\forall \exists`)

   Það er til einhver sannleikur sem enginn getur vitað.
   (:math:`\exists \forall`)

Þetta er alveg greinilega ógild rökfærsla. Hún er á pari við:

.. container:: earg

   Allir eiga pabba. (:math:`\forall \exists`)

   Það er einhver sem er pabbi allra. (:math:`\exists \forall`)

Við þurfum því að sýna aðgát í meðferð magnara!

Að þýða í skrefum
~~~~~~~~~~~~~~~~~

Eins og ætti að vera orðið ljóst, getur það verið ansi snúið að þýða
setningar yfir á táknmál umsagnarökfræði. Það er ekki til nein pottþétt
aðferð til þess, en það hjálpar oft að umorða setningina í skrefum og
brjóta hana niður í smærri einingar sem við setjum svo saman aftur. Hér
kemur ekkert í stað þess að skoða dæmi og gera æfingar. Með tímanum
öðlast maður svo tilfinningu fyrir rökfræðilegri uppbyggingu setninganna
og hvernig er best að umorða þær svo út komi rétt þýðing.

Skoðum fyrst dæmin úr síðasta hluta:

.. container:: earg

   Sérhver manneskja er þannig að til er einhver sem viðkomandi elskar.

   Það er til einhver tiltekin manneskja sem er þannig að allir elska þá
   manneskju.

Við getum byrjað á því að umorða setningarnar yfir í orðalag sem líkist
táknmáli setningarökfræði betur. Byrjum á `[lovecycle] <#lovecycle>`__.
Hana getum við umorðað svona: „Um hverja manneskju *x* gildir að til er
einhver manneskja *y* sem *x* elskar“. Við vitum að „\ *x* elskar *y*\ “
væri þýtt sem :math:`Lxy`. Þá sjáum við að best væri að þýða þessa
setningu sem :math:`\forall x \exists yLxy`.

Setningu `[loveconverge] <#loveconverge>`__ mætti svo umorða sem „Til er
*y* sem er þannig að öll *x* eru þannig að *x* elskar *y*\ “. Þá sjáum
við að besta þýðingin er :math:`\exists y \forall x Lxy`.

En það getur verið erfitt að hafa góða tilfinningu fyrir hvernig er best
að umorða setningar, og því er önnur leið sem má prófa að setja inn nöfn
í staðinn fyrir breyturnar og fylla svo inn magnaranna einn af öðrum með
því að gera setninguna sífellt almennari. Ef við látum :math:`a` og
:math:`b` vera einhvern nöfn, þá segir :math:`Lab` að „a“ elski „b“.
Setningin :math:`\exists y Lay` segir þá að til sé eitthvað :math:`y`
sem :math:`a` elskar. Ef við hugsum svo sem svo að „a“ sé bara einhver,
og að það sem gildi um „a“, geti allt eins gilt um alla, þá fáum við
:math:`\forall x \exists Lxy`.

Við byrjum á sama hátt fyrir `[loveconverge] <#loveconverge>`__. Við
höfum :math:`Lab` sem segir að „a“ elski „b“. Ef „b“ er sá sem allir
elska, þá höfum við :math:`\forall x Lxb`. Þá er lítið mál að skipta út
:math:`b` fyrir tilvistarmagnara og við fáum
:math:`\exists y \forall x Lxy`.

Skoðum fleiri dæmi og notum eftirfarandi þýðingarlykil:

.. container:: ekey

   fólk og hundar

   er hundur

   er vinur

   er eigandi

   Guðbjörg

Þýðum nú eftirfarandi setningar:

.. container:: earg

   Guðbjörg er hundaeigandi.

   Einhver er hundaeigandi.

   Allir vinir Guðbjargar eru hundaeigendur.

   Allir hundaeigendur eiga vin sem er hundaeigandi.

Við getum umorðað setningu `[dog2] <#dog2>`__ sem „Til er hundur sem
Guðbjörg á“. Það er engum sérstökum vandkvæðum bundið að þýða að
einfaldlega sem :math:`\exists x(Hx \eand Egx)`

Við getum umorðað setningu `[dog3] <#dog3>`__ sem „Til er *y* sem er
þannig að *y* er hundaeigandi“. Hér væri skynsamlegt að umorða í styttri
skrefum. Við getum til dæmis umorðað setninguna yfir á blöndu af
íslensku og máli setningarökfræði sem:
:math:`\exists y(y\text{ er hundaeigandi})`. Setningarbrotið sem er
eftir, það er að segja „\ *y* er hundaeigandi“, er mjög líkt
`[dog2] <#dog2>`__, nema það fjallar ekki sérstaklega um Guðbjörgu,
heldur *y*, sama hvað það er. Við getum því þýtt setningu
`[dog3] <#dog3>`__ í heild sem

.. math:: \exists y \exists x(Hx \eand Eyx)

\ Ef við myndum þýða hana aftur yfir á mælt mál, eins beint og við
getum, þá myndi hún segja: „til er *x* og til er *y* þannig að *x* er
hundur og *y* er eigandi *x*.“ Að þessum þýðingarlykli gefnum, þá er
þetta það næsta sem við komumst merkingu `[dog3] <#dog3>`__.

Við getum umorðað setningu `[dog4] <#dog4>`__ sem „Hver sá sem er vinur
Guðbjargar er hundaeigandi“. Ef við notum svo sömu aðferð og að ofan, að
þýða yfir á blöndu af íslensku og máli setningarökfræði, þá getum við
umorðað hana svona:

.. math:: \forall x \bigl[Vxg \eif x \text{ er hundaeigandi}\bigr]

\ Það sem er eftir er, rétt eins og síðast, er eins og setning
`[dog2] <#dog2>`__. En hér þurfum við að passa okkur. Ef við myndum
skrifa, rétt eins og að ofan, einfaldlega:

.. math:: \forall x \bigl[Vxg \eif \exists x(Hx \eand Exx)\bigr]

þá lendum við í vandræðum, því breyturnar lenda í árekstri: svið
almagnarans, :math:`\forall x`, er öll setningin, svo *x*-ið í
:math:`Hx` myndi stjórnast af því. En :math:`Hx` fellur *líka* undir
svið tilvistarmagnarans :math:`\exists x` og ætti því líka að stjórnast
af honum. Hvort er rétt? Setningin er allt í einu orðin tvíræð, ef hún
hefur þá nokkra merkingu yfirleitt, og rökfræðingar hata tvíræðni. Við
verðum því að hafa í huga að engin breyta getur látið stjórnast af
tveimur herrum og slíkt tvíræðni má ekki líðast.

En hvað gerum við þá? Lausnin er einföld, við veljum bara nýja breytu og
þýðum setninguna sem:

.. math:: \forall x\bigl[Vxg \eif\exists z(Hz \eand Exz)\bigr]

Við getum umorðað setningu `[dog5] <#dog5>`__ sem „Fyrir öll *x* sem eru
hundaeigendur, er til hundaeigandi sem er vinur *x*\ “. Ef við notum
aftur sömu aðferð, að umorða í skrefum, þá getum við umorðað þessa
setningu sem

.. math:: \forall x\bigl[\mbox{$x$ er hundaeigandi}\eif\exists y(\mbox{$y$ er hundaeigandi}\eand Vyx)\bigr]

Við getum svo lokið þýðingunni (og pössum okkur á að engar breytur
rekist á) með því að skrifa:

.. math:: \forall x\bigl[\exists z(Hz \eand Exz)\eif\exists y\bigl(\exists z(Hz \eand Eyz)\eand Vyx\bigr)\bigr]

Glöggir lesendur taka kannski eftir því að hér kemur sama breyta,
:math:`z`, fyrir í forlið og baklið skilyrðissetningarinnar. Var það
ekki tvírætt og bar að varast? Ef við skoðum svið magnaranna tveggja, þá
sjáum við að svo er ekki. Svið magnarans sem stjórnar fyrstu
:math:`z`-breytunni er lokið áður en svið næsta magnara sem stjórnar
:math:`z`-breytu hefst. Það er því enginn árekstur og alveg ljóst hvað
er hvað. Við gætum sýnt þetta myndrænt svona:

.. math:: \overbrace{\forall x\bigl[\overbrace{\exists z(Hz \eand Exz)}^{\text{svið fyrsta `}\exists z\text{'}}\eif \overbrace{\exists y(\overbrace{\exists z(Hz \eand Eyz)}^{\text{svið annars `}\exists z\text{'}}\eand Vyx)\bigr]}^{\text{svið `}\exists y\text{'}}}^{\text{svið `}\forall x\text{'}}

Þetta sýnir að enginn breyta er hér látin þjóna tveimur herrum samtímis.

Notið þennan þýðingarlykil til að þýða setningarnar hér að neðan yfir á
táknmál umsagnarökfræði:

.. container:: ekey

   öll dýr

   er krókódíll

   er api

   er skriðdýr

   býr í Húsdýragarðinum

   elskar

   Alli

   Bibbi

   Dísa

.. container:: earg

   Ef Dísa elskar Bibba, þá er Bibbi api.

   Ef Bibbi og Dísa eru bæði krókódílar, þá elskar Alli þau bæði.

   Dísa elskar skriðdýr. [Ath.: Þessi setning er tvíræð. Hvaða tvær
   þýðingar eru mögulegar?]

   Bibbi elskar alla apana í Húsdýragarðinum.

   Allir aparnir sem Alli elskar elska hann líka.

   Allir apar sem Dísa elska eru líka elskaðir af Alla.

   Það er api sem elskar Bibba, en því miður elskar Bibbi hann ekki.

Notið þennan þýðingarlykil til að þýða setningarnar hér að neðan yfir á
táknmál umsagnarökfræði:

.. container:: ekey

   öll dýr

   er hundur

   elskar glæpamyndir

   er stærri en

   Vaskur

   Snotra

   Rökkvi

.. container:: earg

   Vaskur er hundur sem elskar glæpamyndir.

   Vaskur, Snotra og Rökkvi eru öll hundar.

   Vaskur er stærri en Rökkvi, og Snotra er stærri en Vaskur.

   Allir hundar elska glæpamyndir.

   Bara hundar elska glæpamyndir.

   Það er hundur sem er stærri en Rökkvi.

   Ef það er hundur sem er stærri en Snotra, þá er hundur sem er stærri
   en Vaskur.

   Ekkert dýr sem elskar glæpamyndir er stærri en Rökkvi.

   Engin hundur er stærri en Snotra.

   Sérhvert dýr sem elskar ekki glæpamyndir er stærra en Snotra.

   Það er til dýr sem er á milli Snotru og Vasks að stærð.

   Það er enginn hundur sem er á milli Snotru og Rökkva að stærð.

   Enginn hundur er stærri en hann sjálfur.

   Allir hundar eru stærri en einhver hundur.

   Það er til dýr sem er minna en allir hundar.

   Ef það er til dýr sem er stærra en allir hundar, þá elskar það dýr
   ekki við glæpamyndir.

Notið þennan þýðingarlykil til að þýða setningarnar hér að neðan yfir á
táknmál umsagnarökfræði:

.. container:: ekey

   fólk og réttir í matarboði

   er búinn.

   er á borðinu.

   er matarkyns.

   er manneskja.

   elskar .

   Arngrímur

   Friðrika

   sviðasultan

.. container:: earg

   Allur matur er kominn á borðið.

   Ef sviðasultan er ekki búin, þá er hún komin á borð.

   Allir elska sviðasultu.

   Ef einhver elskar sviðasultu, þá er það Arngrímur.

   Friðrika elskar bara réttina sem eru búnir.

   Friðika elskar engan, og enginn elskar Friðriku.

   Arngrímur elskar alla sem elska sviðasultu.

   Arngrímur elskar alla sem elska fólkið sem hann elskar.

   Ef einhver manneskja er uppi á borði, þá hlýtur allur maturinn að
   vera búinn.

Notið þennan þýðingarlykil til að þýða setningarnar hér að neðan yfir á
táknmál umsagnarökfræði:

.. container:: ekey

   fólk

   er ballettdansari.

   er kvenkyns.

   er karlkyns.

   er barn .

   er systkini .

   Leifur

   Freydís

   Eiríkur

.. container:: earg

   Öll börnin hennar Freydísar eru ballettdansarar.

   Freydís er dóttir Leifs.

   Leifur á dóttur.

   Freydís er einkabarn.

   Allir synir Eiríks dansa ballett.

   Leifur á enga syni.

   Eiríkur er bróðir Leifs.

   Freydís er bróðurdóttir Eiríks.

   Bræður Leifs eiga engin börn.

   Freydís er föðursystir.

   Allir sem dansa ballett eiga bróður sem dansar líka ballett.

   Allar konur sem dansa ballett eru börn einhvers sem dansar ballett.

.. _sec.identity:

Samsemd
-------

Skoðum eftirfarandi setningu:

.. container:: earg

   Andrés skuldar öllum peninga.

Andrés, er eins og frægt er, íbúi í Andabæ. Ef við látum yfirgripið
okkar vera alla íbúa Andabæjar, þá getum við þýtt „allir“ með einföldum
almagnara þegar við viljum tala um þá. Notum þá þennan þýðingarlykil:

.. container:: ekey

   skuldar peninga

   Andrés

Nú getum við þýtt setningu `[else1] <#else1>`__ sem
:math:`\forall x Sax`. [3]_ Þetta er þó kannski ekki það sem við meinum
þegar við segjum að Andrés skuldi öllum peninga. :math:`\forall x Sax`
segir nefnilega að fyrir hvaða *x* sem er í yfirgripinu, þá skuldar
Andrés *x* peninga. En Andrés er sjálfur í yfirgripinu, enda sjálfur
búsettur í Andabæ, og því leiðir af þýðingunni okkar að Andrés skuldar
sjálfum sér peninga. Það er líklega ekki það sem við vildum sagt hafa
með setningu `[else1] <#else1>`__. Kannski vildum við frekar segja
eitthvað af eftirfarandi:

.. container:: earg

   Andrés skuldar öllum *öðrum* peninga.

   Andrés skuldar öllum *öðrum en Andrési* peninga

   Andrés skuldar öllum peninga, *nema Andrési sjálfum*.

Enn sem komið er höfum við enga leið til að tjá skáletruðu hluta þessa
setninga. Lausnin er að bæta nýju tákni við táknmál umsagnarökfræði.

Samsemdarmerkinu bætt við
~~~~~~~~~~~~~~~~~~~~~~~~~

Til þess að geta þýtt setningar eins og þær hér að ofan, þá bætum við
eins og áður sagði nýju tákni við táknmál umsagnarökfræði. Það er táknið
:math:`=`\ „“.

Við látum þetta tákn standa fyrir sérstaka tvísæta umsögn og af því að
þessi umsögn mun hafa sérstaka merkingu, þá munum við bregða út af
vananum og skrifa táknið fyrir hana á milli tveggja einnefna, en ekki
fyrir framan, eins og venja er (þetta er ekkert sérstaklega óvenjulegt í
raun, enda fyndist okkur fullkomlega eðlilegt að skrifa
:math:`\frac{1}{2} = 0.5`). Merking þessarar umsagnar er sú sama og ef
við myndum *alltaf* bæta eftirfarandi línu við hvern þann þýðingarlykil
sem við notum í það og það skiptið:

.. container:: ekey

   er það sama og

Þetta merkir ekki *bara* að það sem talað er um sitthvorum megin við
:math:`=`-merkið sé ógreinanlegt frá hverju öðru, eða að allt sem er
satt um annað sé líka satt um hitt, heldur merkir þetta að það sé *sami
hluturinn*.

Hér er dæmi. Segjum að við viljum þýða eftirfarandi setningu yfir á
táknmál umsagnarökfræði:

.. container:: earg

   Andrés er Stálöndin.

Bætum eftirfarandi nafni við þýðingarlykilinn:

.. container:: ekey

   Stálöndin

Nú getum við þýtt `[else2] <#else2>`__ sem :math:`a = s`. Þessi setning
segir okkur að nöfnin :math:`a` og :math:`s` vísi bæði til sama
hlutarins í yfirgripinu. Ef við viljum segja að tvö nöfn vísi *ekki* til
sama hlutarins, til dæmis :math:`a` og :math:`s`, þá neitum við
einfaldlega þessari setningu: :math:`\enot (a = s)`.

Nú getum við loks þýtt setningar
`[else1b] <#else1b>`__–`[else1d] <#else1d>`__. Við getum umorðað þær
allar sem „Andrés skuldar öllum peninga sem ekki eru Andrés“. Frekari
umorðun gefur okkur svo: „Fyrir öll *x*, ef *x* er ekki Andrés, þá
skuldar Andrés *x* peninga“. Með því að nota neitun samsemdar, þá getum
við nú þýtt þessa setningu sem
:math:`\forall x (\enot(x = a) \eif Sax)`.

Það er hins vegar oft dálítið óþjált að skrifa sífellt neitunarmerki
fyrir framan sviga þegar maður vill neita samsemdarsetningu, og því
munum við nota annan rithátt fyrir setningar á forminu
„\ :math:`\enot(a = b)`\ “. [4]_ Við munum framvegis nota þá venju að
draga einfaldlega strik í gegnum samsemdarmerkið þegar við viljum neita
því, svona: :math:`a \neq b`. Við getum því einfaldað setninguna hér að
ofan sem: :math:`\forall x (x \neq a \eif Sax)`.

Við getum líka notað samsemd við að þýða annars konar setningar. Tökum
sem dæmi:

.. container:: earg

   Enginn nema Andrés skuldar Jóakim peninga.

   Bara Andrés skuldar Jóakim peninga.

Ef við látum :math:`j` standa fyrir Jóakim, þá getum við umorðað
`[else3] <#else3>`__ sem „Enginn sem er ekki Andrés skuldar Jóakim
peninga“. Það getum við svo þýtt yfir á táknmál umsagnarökfræði sem

.. math:: \enot\exists x(x \neq a \eand Sxj)

\ Við getum svo umorðað `[else4] <#else4>`__ sem „fyrir öll *x*, ef *x*
skuldar Jóakim peninga, þá er *x* Andrés.“ Við getum þýtt þessa setningu
yfir á táknmál umsagnarökfræði sem

.. math:: \forall x (Sxj \eif x = a)

Í kafla `[s:CQ] <#s:CQ>`__ munum við geta sýnt að þessar tvær setningar
séu rökfræðilega jafngildar.

Hér er þó einn hængur á. Ef einhver myndi heyra setningar
`[else3] <#else3>`__ og `[else4] <#else4>`__ á mæltu máli, þá myndi
viðkomandi líklega skilja það sem svo að Andrés skuldi Jóakim peninga.
En þýðingarnar okkar yfir á táknmál umsagnarökfræði segja það ekki. Þær
segja bara að *enginn annar* en Andrés skuldi honum peninga, en ekkert
um Andrés sjálfan. Ef við viljum þýða setningarnar eins og eðlilegt er
að skilja þær á mæltu máli, þá þurfum við að bæta við lið sem segir að
Andrés skuldi Jóakim peninga:
:math:`\enot\exists x(x \neq a \eand Sxj) \eand Saj` og
:math:`\forall x (Sxj \eif x = a) \eand Saj`.

Til eru að minnsta kosti…
~~~~~~~~~~~~~~~~~~~~~~~~~

Við getum líka notað samsemd til að segja hversu margir hlutir eru til
sem falla undir ákveðna umsögn (eða umsagnir). Tökum sem dæmi
eftirfarandi setningar:

.. container:: earg

   Til er að minnsta kosti eitt epli.

   Til eru að minnsta kosti tvö epli.

   Til eru að minnsta kosti þrjú epli.

Notum eftirfarandi þýðingarlykil:

.. container:: ekey

   er epli.

Setning `[atleast1] <#atleast1>`__ er einföld og við kunnum að þýða hana
nú þegar: :math:`\exists x Ex`. Hún segir að til séu epli í yfirgripinu,
kannski mörg, en að minnsta kosti eitt.

Það væri freistandi að reyna að þýða `[atleast2] <#atleast2>`__ með því
að nota einfaldlega tvo magnara:
:math:`\exists x \exists y(Ax \eand Ay)`. Þessi setning segir að til sé
eitthvað epli *x* í yfirgripinu og að til sé eitthvað epli *y* í
yfirgripinu, og eins og við sögðum að ofan í §\ `1.5 <#yfirgrip>`__, þá
er ekkert sem kemur í veg fyrir að *x* og *y* vísi til sama eplis. Þessi
setning er því sönn ef einungis eitt epli er í yfirgripinu. Til þess að
tryggja að hún sé sönn ef að minnsta kosti tvö epli eru í yfirgripinu,
þá getum við notað samsemd. Það sem okkur vantar er einfaldlega að taka
fram að *x* og *y* séu ekki sama eplið, og það kunnum við. Við getum því
þýtt setninguna sem

.. math:: \exists x \exists y(Ex \eand Ey \eand x \neq y)

\ Þessi setning segir að til sé epli *x* og til sé epli *y* og að *x* og
*y* sé ekki sama eplið. Þessi setning er einungis sönn ef *að minnsta
kosti* tvö epli eru í yfirgripinu (en kannski fleiri).

Setning `[atleast3] <#atleast3>`__ segir að til séu að minnsta kosti
þrjú epli. Hér er ekkert nýtt á ferðinni, nema við þurfum þrjá
tilvistarmagnara og að segja að enginn þeirra sé sá sami og einn af
hinum. Við þýðum því setninguna svona:

.. math:: \exists x \exists y\exists z(Ex \eand Ey \eand Ez \eand x \neq y \eand y \neq z \eand x \neq z)

\ Við sjáum að eftir því sem hlutunum fjölgar, þá lengjast setningarnar
mjög hratt!

Til eru í mesta lagi…
~~~~~~~~~~~~~~~~~~~~~

Skoðum nú eftirfarandi setningar:

.. container:: earg

   Til er í mesta lagi eitt epli.

   Til eru í mesta lagi tvö epli.

Ef `[atmost1] <#atmost1>`__ er sönn, þá vitum við að ekki eru til tvö
epli. Við getum því umorðað `[atmost1] <#atmost1>`__ sem „Það er ekki
satt að það séu að minnsta kosti *tvö* epli“ og það er bara neitun
`[atleast2] <#atleast2>`__:

.. math:: \enot \exists x \exists y(Ex \eand Ey \eand x \neq y)

\ En við getum líka hugsað um `[atmost1] <#atmost1>`__ á annan hátt. Hún
segir nefnilega að ef við tökum einhvern hlut úr yfirgripinu og hann er
epli, og svo gerum við það sama aftur, þá hljótum við að hafa tekið sama
eplið tvisvar. Ef það er jú bara eitt epli, þá getum við ekki tekið upp
tvö epli! Við getum því þýtt setninguna sem

.. math:: \forall x\forall y\bigl[(Ex \eand Ey) \eif x=y\bigr]

Við munum sjá seinna að þessar tvær setningar eru röklega jafngildar.

Við getum líka þýtt `[atmost2] <#atmost2>`__ á tvo ólíka vegu. Við getum
umorðað hana sem „Það er ekki satt að til séu *þrjú* epli“ og þýtt hana
sem

.. math:: \enot \exists x \exists y\exists z(Ex \eand Ey \eand Ez \eand x \neq y \eand y \neq z \eand x \neq z)

\ Við getum líka skilið hana sem svo að ef við finnum epli í
yfirgripinu, og svo epli og svo epli, þá hljótum við að hafa fundið sama
eplið oftar en einu sinni. Þá getum við þýtt hana sem

.. math:: \forall x\forall y\forall z\bigl[(Ex \eand Ey \eand Ez) \eif (x=y \eor x=z \eor y=z)\bigr]

\ Takið sérstaklega eftir því að í bakliðnum eru *eða-tengi*. Þessi
setning segir að fyrir öll *x*, öll *y* og öll *z*, ef *x*, *y* og *z*
eru epli, þá er *x* sama og *y*, *eða* *x* sama og *z*, *eða* *z* sama
og *y*.

Til eru nákvæmlega…
~~~~~~~~~~~~~~~~~~~

Núna getum við þýtt setningar sem segja nákvæmlega hversu mikið af
einhverju er til, til dæmis:

.. container:: earg

   Til er nákvæmlega eitt epli.

   Til eru nákvæmlega tvö epli.

   Til eru nákvæmlega þrjú epli.

Við getum umorðað `[exactly1] <#exactly1>`__ sem „Til er *að minnsta
kosti* eitt epli og til er *í mesta lagi* eitt epli“. Þetta er bara
samtenging setninga `[atleast1] <#atleast1>`__ og
`[atmost1] <#atmost1>`__. Setningin í heild lítur því svona út:

.. math:: \exists x Ex \eand \forall x\forall y\bigl[(Ex \eand Ey) \eif x=y\bigr]

\ En þetta er kannski ekkert alltof fallegt og heldur langt. Við getum
umorðað setninguna á annan, og kannski einfaldari hátt, með að segja:
„Til er *x* sem er epli og allt sem er epli er *x*\ “. Þá getum við þýtt
setninguna sem:

.. math:: \exists x\bigl[Ex \eand \forall y(Ey \eif x= y)\bigr]

Setning `[exactly2] <#exactly2>`__ getur verið umorðuð á sama hátt sem
„Til eru *að minnsta kosti* tvö epli og til eru *í mesta lagi* tvö
epli.“ Hún er samtenging `[atleast2] <#atleast2>`__
og\ `[atmost2] <#atmost2>`__:

.. math:: \exists x \exists y(Ex \eand Ey \eand x \neq y) \eand \forall x\forall y\forall z\bigl[(Ex \eand Ey \eand Ez) \eif (x=y \eor x=z \eor y=z)\bigr]

\ En við gætum líka umorðað hana sem „Til eru að minnsta kosti tvö
mismunandi epli og öll epli eru annað af þessum tveimur eplum“. Þá fáum
við:

.. math:: \exists x\exists y\bigl[Ex \eand Ey \eand x \neq y \eand \forall z(Ez \eif ( x= z \eor y = z)\bigr]

Setning `[exactly3] <#exactly3>`__ fengi svo sömu meðferð. Skoðum að
lokum þessa setningu:

.. container:: earg

   Til eru nákvæmlega tveir hlutir.

Hér væri kannski freistandi að bæta við umsögn í þýðingarlykilinn okkar
sem segir „ er hlutur“. En þetta er óþarfi. Slík umsögn myndi eiga við
allt í yfirgripinu og bætti því engu við. Við getum því þýtt þessa
setningu með eftirfarandi jafngildum þýðingum:

.. math:: \exists x \exists y (x \neq y) \eand \enot \exists x \exists y \exists z (x \neq y \eand y \neq z \eand x \neq z)

\ eða

.. math:: \exists x \exists y \bigl[x \neq y \eand \forall z(x=z \eor y = z)\bigr]

Útskýrið af hverju:

.. container:: ebullet

   :math:`\exists x \forall y(Ay \eiff x= y)` er góð þýðing á „Til er
   nákvæmlega eitt epli“.

   :math:`\exists x \exists y \bigl[\enot x = y \eand \forall z(Az \eiff (x= z \eor y = z)\bigr]`
   er góð þýðing á „Til eru nákvæmlega tvö epli“.

.. _subsec.defdesc:

Ákveðnar lýsingar
-----------------

Skoðum eftirfarandi setningar:

.. container:: earg

   Sæmundur er skrýtni heimspekingurinn.

   Skrýtni heimspekingurinn lærði við Svartaskóla.

   Presturinn er skrýtni heimspekingurinn.

Þetta eru ákveðnar lýsingar: þær vísa til *nákvæmlega eins* ákveðins
hlutar. Þær eru ólíkar bæði *óákveðnum lýsingum*, svo sem „Sæmundur er
prestur“ og almennum lýsingum sem á yfirborðinu virðast hafa svipað
form, t.d. „Hvalurinn er spendýr“ (en hér er átt við alla hvali,
*hvalinn* sem tegund). Þá vaknar spurningin: Hvernig getum við þýtt
ákveðnar lýsingar yfir á táknmál umsagnarökfræði?

Ákveðnar lýsingar sem einnefni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ein leið væri að kynna alltaf til sögunnar nýtt nafn í staðinn fyrir
ákveðna lýsingu. Til dæmis gætum við ákveðið að :math:`h` stæði fyrir
skrýtna heimspekinginn og þýtt setningu `[traitor1] <#traitor1>`__ sem
:math:`s = h` (þar sem „\ :math:`s`\ “ stæði fyrir Sæmund) og setningu
`[traitor2] <#traitor2>`__ sem :math:`Ss` (með S sem „ lærði við
Svartaskóla“). En þessi leið hefur ákveðinn galla: Við viljum geta
dregið þá ályktun að skrýtni heimspekingurinn sé skrýtinn heimspekingur.
En enga slíka ályktun er hægt að draga af nafninu „\ :math:`s`\ “.

Önnur leið væri að bæta við nýju tákni við táknmál umsagnarökfræði sem
hegðar sér svipað og magnari, nema það breytir umsögnum í ákveðnar
lýsingar. Ef við látum þetta tákn vera „\ :math:`\maththe`\ “, þá gætum
við lesið til dæmis :math:`\maththe x Fx` sem „það sem er F“ eða „F-ið“.
Táknrunur á forminu :math:`\maththe \meta{x} \meta{A}\meta{x}` myndu þá
hegða sér eins og nöfn. Þau væru *einnefni*. [5]_

Notum þá eftirfarandi þýðingarlykil til að þýða setningarnar hér að
ofan:

.. container:: ekey

   fólk

   er skrýtinn heimspekingur

   er prestur

   lærði við Svartaskóla

   Sæmundur

Nú getum við þýtt setningu `[traitor1] <#traitor1>`__ sem
:math:`\maththe x Hx = s`, setningu `[traitor2] <#traitor2>`__ sem
:math:`S\maththe xTx` og setningu `[traitor3] <#traitor3>`__ sem
:math:`\maththe x Px = \maththe x Hx`.

Það væri hins vegar gott ef við gætum meðhöndlað ákveðnar lýsingar *án
þess* að bæta nýju tákni við táknmál umsagnarökfræði.

Lýsingakenning Russells
~~~~~~~~~~~~~~~~~~~~~~~

Breski heimspekingurinn Bertrand Russell setti fram fræga kenningu um
ákveðnar lýsingar í upphafi síðustu aldar. Í stuttu máli, þá benti
Russell á að þegar við notum orðasambönd á forminu „\ *G*-ið sem er
*F*\ “, þá er *F* lýsing sem ætlunin er aðeins einn hlutur í yfirgripinu
uppfylli. Russell greinir því ákveðnar lýsingar sem lýsingar sum
uppfylla eftirfarandi skilyrði: [6]_

.. math::

   \begin{aligned}
           \text{F-ið er G \textbf{eff} }&\text{til er að minnsta kosti eitt F, \emph{og}}\\
       &\text{til er í mesta lagi eitt F, \emph{og}}\\ 
       &\text{öll F eru G}
   \end{aligned}

Takið eftir því að ákveðin greinir kemur ekki fyrir í skilgreiningunni,
enda er það ætlun Russells að skilgreina hvað ákveðin lýsing er, án þess
að ákveðnar lýsingar komi fyrir í skilgreiningunni. Hann *smættar* þær
niður í aðrar setningar sem ekki eru ákveðnar lýsingar.

Með þessa greiningu á ákveðnum lýsingum í huga, þá getum við þýtt
setningar sem hafa formið „\ *F*-ið er *G*\ “ yfir á táknmál
umsagnarökfræði með því að nota þær aðferðir sem við lærðum hér að ofan
við talningu, þar sem skilyrði Russells segja að til sé að minnsta kosti
eitt *F* og í mesta lagi eitt *F*.

Fyrsta skilyrði Russells væri þá þýtt einfaldlega sem
:math:`\exists x Fx`, annað skilyrðið sem
:math:`\forall x \forall y ((Fx \eand Fy) \eif x = y)` og það síðasta
sem :math:`\forall x (Fx \eif Gx)`. Sú fullyrðing að *F*-ið sé *G* yrði
því á máli umsagnarökfræði samtenging þessara þrigga setninga, eða

.. math:: \exists x Fx \eand \forall x \forall y ((Fx \eand Fy) \eif x = y) \eand \forall x (Fx \eif Gx)

Glöggir lesendur muna það kannski að sú fullyrðing að til sé að minnsta
kosti eitt *F* og í mesta lagi eitt *F* er sú sama og að fullyrða að til
sé nákvæmlega eitt *F*, og að við kunnum einfaldari leiðir til að tjá
það. Við getum því einfaldað þýðingu okkar töluvert með að þýða „F-ið er
G“ með því að segja frekar:

.. math:: \exists x \bigl[Fx \eand \forall y (Fy \eif x = y) \eand Gx\bigr]

Nú getum við þýtt setningar
`[traitor1] <#traitor1>`__–`[traitor3] <#traitor3>`__ yfir á táknmál
umsagnarökfræði *án þess* að nota neitt nýtt tákn eins og
„\ :math:`\maththe`\ “.

Setning `[traitor1] <#traitor1>`__ er keimlík þessum dæmum sem við vorum
að skoða. Við getum þess vegna þýtt hana sem

.. math:: \exists x (Hx \eand \forall y(Hy \eif x = y) \eand x = s)

\ Setning `[traitor2] <#traitor2>`__ er heldur ekkert vandamál. Við
þýðum hana á svipaðan hátt sem
:math:`\exists x (Hx \eand \forall y(Hy \eif x = y) \eand Sx)`.

Setning `[traitor3] <#traitor3>`__ er pínulítið meira vesen, því hún
tengir saman tvær ákveðnar lýsingar. En með því að fylgja greiningu
Russells, þá getum við umorðað hana sem „það er til nákvæmlega einn
skrýtinn heimspekingur *x*, nákvæmlega einn prestur *y* og *x* er sama
og *y*\ “. Við getum því þýtt hana yfir á táknmál umsagnarökfræði sem:

.. math:: \exists x \exists y \bigl(\bigl[Hx \eand \forall z(Hz \eif x = z)\bigr] \eand \bigl[Py \eand \forall z(Pz \eif y = z)\bigr] \eand x = y\bigr)

Takið eftir því að táknrunan :math:`x = y` (eða formúlan, eins og við
munum kalla það síðar) verður að vera innan sviðs beggja magnaranna.

Tómar ákveðnar lýsingar
~~~~~~~~~~~~~~~~~~~~~~~

Einn af kostunum við lýsingakenningu Russells er að hún leyfir okkur að
meðhöndla *tómar* ákveðnar lýsingar á snyrtilegan hátt.

Í Frakklandi er enginn konungur og hefur ekki verið um hríð. Ef við
myndum láta eitthvert nafn, til dæmis :math:`k`, standa fyrir núverandi
konung Frakklands, myndi allt ganga á afturfótunum hjá okkur. Við munum
úr §\ `1 <#s:FOLBuildingBlocks>`__ að nafn verður alltaf að vísa til
einhvers hlutar í yfirgripinu og það skiptir engu máli hvaða yfirgrip
við veljum, það mun aldrei innihalda konung Frakklands, sem er ekki til.
Við gætum því ekki einu sinni þýtt setninguna „Núverandi konungur
Frakklands er ekki til“ yfir á táknmál umsagnarökfræði.

Við gætum reynt að kynna til sögunnar umsögn, K: „ er núverandi konungur
Frakklands“ og greint „Núverandi konungur Frakklands er ekki til“ sem
:math:`\forall x\enot Kx`. Það væri kannski ásættanlegt, en hvað með
setninguna „Núverandi konungur Frakklands er sköllóttur“? Við gætum
prófað að láta *S* standa fyrir umsögnina „ er sköllóttur“ og reynt:
:math:`\forall x (Kx \eif Sx)`. En þessi setning væri sönn (því eins og
við munum, þá eru allar skilyrðissetningar með tómum umsögnum sannar),
og það er eitthvað skrýtið við að segja að setningin „Núverandi konungur
Frakklands er sköllóttur“ sé sönn, því hann er jú ekki til.

Á hinn bóginn væri líka skrýtið að segja að hún sé ósönn, því það myndi
þýða að neitun hennar væri sönn—og ættum við þá að halda að núverandi
konungur Frakklands sé með hár? Og hvernig ættum við þá að þýða þá
setningu?

Lýsingakenning Russells leyfir okkur að komast hjá öllum þessum
vandkvæðum með að greina setningar með tómum umsögnum þannig að þær
verða ósannar. Hún greinir setninguna „Núverandi konungur Frakklands er
sköllóttur“, eins og áður sagði, sem

.. math:: \exists x \bigl[Kx \eand \forall y (Ky \eif x = y) \eand Sx\bigr]

\ og þessi setning segir jú meðal annars að til sé að minnsta kosti eitt
*x* sem er núverandi konungur Frakklands, og það er ekki satt. Raunar
dregur lýsingakenning Russells fram hvernig slík setning getur verið
ósönn á tvo mismunandi vegu. Þegar við neitum setningunni „Núverandi
konungur Frakklands er skóllóttur“ þá gætum við meint annað af
eftirfarandi:

.. container:: earg

   Það er enginn sem er hvort tveggja, konungur Frakklands og
   skóllóttur.

   Það er einhver sem er núverandi konungur Frakklands, en hann er ekki
   skóllóttur.

Setningu `[outernegation] <#outernegation>`__ má þýða sem

.. math:: \enot \exists x\bigl[Kx \eand \forall y(Ky \eif  x = y) \eand Sx \bigr]

\ og því getum við kallað hana *ytri neitun* setningarinnar, því svið
neitunarinnar er öll setningin. Þessi setning er sönn ef það er enginn
konungur í Frakklandi.

Setningu `[innernegation] <#innernegation>`__ væri hins vegar best að
þýða sem

.. math:: \exists x (Kx \eand \forall y(Ky \eif x = y) \eand \enot Sx)

\ og hana getum við kalla *innri neitun* setningarinnar, því svið
neitunarinnar er innan ákveðnu lýsingarinnar sjálfrar. Þessi setning er
einungis sönn ef konungur Frakklands er til—og það gildir um þann mann
að hann er ekki sköllóttur.

Er lýsingakenning Russells nógu góð?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fram að þessu höfum við lofað lýsingakenningu Russells í hástert. En er
hún nógu góð? Þessi spurning hefur verið tilefni mikilla deilna innan
heimspekinnar allar götur síðan, en hér ætla ég þó bara að tæpa á
nokkrum hlutum sem nefndir hafa verið kenningunni til hnjóðs.

Hið fyrsta snýr að ákveðnum lýsingum sem eiga ekki við neitt, sem við
kölluðum *tómar* hér að ofan. Ef ekkert í yfirgripinu er *F*, þá leiðir
það af kenningu Russells að setningarnar „\ *F*-ið er *G*\ “ og
„\ *F*-ið er ekki *G*\ “ eru báðar ósannar. Breski heimspekingurinn
P.F. Strawson taldi að slíkar setningar ættu ekki að teljast ósannar,
heldur að sanngildi slíkra setninga gerir ráð fyrir að eitthvað sé *F*,
og því ættu þær að teljast hvorki sannar né ósannar. [7]_

Ef við tökum undir með Strawson, þá þurfum við að breyta rökfræðinni
okkar. Í þessari bók höfum við gert ráð fyrir að allar setningar séu
annað hvort sannar eða ósannar. Margar tillögur hafa verið gerðar í
þessa átt, en engin hefur náð neinni sérstakri hylli heimspekilegra
rökfræðinga.

En við þurfum ekki endilega að taka undir með Strawson. Það sem hann
segir hljómar sennilega í sumum tilfellum, en ekki endilega öðrum. Til
dæmis myndi maður halda að ég væri bara beinlínis að segja ósatt ef ég
héldi því fram að ég sé giftur núverandi konungi Frakklands, frekar en
að sú fullyrðing hafi ótilgreint sanngildi.

Keith Donnellan, bandarískur heimspekingur, færði fram annars konar
mótbárur. Þær hafa að gera með tilfelli þar sem mælandi tekur einhvern í
misgripum fyrir annan—hann heldur að hann sé að tala um eina manneskju,
en orð hans vísa í raun til annarrar. [8]_ Eitt af dæmum Donnellans er
svohljóðandi: Tveir menn standa úti í horni í samkvæmi. Annar þeirra er
mjög hávaxinn og er að drekka, að því er virðist, gin úr martiniglasi.
Hinn er mjög lágvaxinn og drekkur, að því að okkur sýnist, vatn úr
vatnsglasi. Anna sér þá standa þarna og segir:

.. container:: earg

   Maðurinn með ginið er mjög hávaxinn!

Samkvæmt Russell, þá ættum við að greina það sem Anna sagði svona:

.. container:: earg

   Það er nákvæmlega einn maður [úti í horni] sem drekkur gin, og hver
   sá sem drekkur gin [úti í horni] er mjög hávaxinn.

En segjum svo sem svo að fyrir algjöra tilviljun sé vatn í
martiniglasinu, ekki gin, og gin í vatnsglasinu. Við Anna höfðum rangt
fyrir okkur um hvaða drykkur var í hvaða glasi. Ef greining Russells er
rétt, þá hefur Anna sagt *ósatt*. En myndum við ekki frekar vilja segja
að hún hafi sagt *satt*, þrátt fyrir ruglinginn?

Það er ekki alveg ljóst hvað er best að segja um svona dæmi. Við getum
öll verið sammála um að Anna ætlaði að vísa til tiltekins manns og segja
eitthvað satt *um hann* (nefnilega að hann sé hávaxinn). Samkvæmt
Russell, þá vísaði hún raun til annars manns (þess lágvaxna) með orðum
sínum og sagði eitthvað ósatt um hann. Hugsanlega er nóg fyrir verjendur
kenningar Russells að útskýra *af hverju* ætlun Önnu gekk ekki upp og
þar með af hverju hún sagði eitthvað ósatt. Það er ekki mikið mál: Hún
sagði ósatt af því að hún hafði ósannar skoðanir um innihald drykkjanna
sem mennirnir tveir drukku; ef hún hefði haft sannar skoðanir, þá hefði
hún sagt satt. [9]_

Við látum staðar numið hér, enda væri hægt að dvelja við slík
heimspekileg úrlausnarefni langtímum saman. Það væri nú ekki nema af
hinu góða, en markmið okkar hér er hins vegar að læra formlega rökfræði.
Við munum því halda okkur við lýsingakenningu Russells þegar við þurfum
að þýða ákveðnar lýsingar yfir á táknmál umsagnarökfræði. Það er líklega
það besta sem er í boði, án þess að endurskoða þurfi rökfræðina sjálfa.

Notið þennan þýðingarlykil til að þýða setningarnar hér að neðan yfir á
táknmál umsagnarökfræði:

.. container:: ekey

   fólk

   kann talnalykilinn sem gengur að peningaskápnum

   er njósnari

   er grænmetisæta

   treystir .

   Hafþór

   Ingimar

.. container:: earg

   Hafþór treystir grænmetisætu.

   Allir sem treysta Ingimari treysta grænmetisætu.

   Allir sem treysta Ingimari treysta einhverjum sem treystir
   grænmætisætu.

   Bara Ingimar kann talnalykilinn sem gengur að peningaskápnum.

   Ingimar treystir Hafþóri, en engum öðrum.

   Manneskjan talnalykilinn sem gengur að peningaskápnum er
   grænmetisæta.

   Manneskjan talnalykilinn sem gengur að peningaskápnum er ekki
   njósnari.

Notið þennan þýðingarlykil til að þýða setningarnar hér að neðan yfir á
táknmál umsagnarökfræði:

.. container:: ekey

   spilin í spilastokki

   er svart.

   er spaði.

   er tvistur.

   er gosi.

   mannspil.

   er eineygður.

   er tromp.

.. container:: earg

   Allir spaðar eru svört spil.

   Það eru engin tromp.

   Það eru að minnsta kosti tveir spaðar.

   Það eru fleiri en einn eineygður gosi.

   Það eru í mesta lagi tveir eineygðir gosar.

   Það eru tveir svartir gosar.

   Það eru fjórir tvistar.

   Spaðatvisturinn er svartur.

   Ef spaðatvisturinn er tromp, þá er nákvæmlega eitt tromp.

   Eineygða mannspilið er ekki tromp.

   Spaðatvisturinn er ekki mannspil.

 

Notið þennan þýðingarlykil til að þýða setningarnar hér að neðan yfir á
táknmál umsagnarökfræði:

.. container:: ekey

   dýr

   er í haganum.

   er hestur.

   er Sleipnir.

   er áttfættur.

.. container:: earg

   Það eru að minnsta kosti þrír hestar í heiminum.

   Það eru að minnsta kosti þrjú dýr í heiminum.

   Það eru fleiri en einn hestur í haganum.

   Það eru þrír hestar í haganum.

   Það er einn áttfættur hestur í haganum; öll önnur dýr hljóta að vera
   ekki áttfætt.

   Sleipnir er áttfættur hestur.

   Dýrið í haganum er ekki hestur.

   Hesturinn í haganum er ekki áttfættur.

Í þessum hluta þýddum við „Sæmundur er skrýtni heimspekingurinn“ sem
:math:`\exists x (Hx \eand \forall y(Hy \eif x = y) \eand x = s)`.
Útskýrið af hverju eftirfarandi þýðingar eru jafngóðar.

.. container:: ebullet

   :math:`Hs \eand \forall y(Hy \eif s = y)`

   :math:`\forall y(Hy \eiff y = s)`

.. _`s:FOLSentences`:

Setningar í umsagnarökfræði
---------------------------

Nú þegar við kunnum að þýða setningar af mæltu máli yfir á táknmál
umsagnarökfræði er kominn tími til að skilgreina nákvæmlega hvað það er
fyrir einhverja táknrunu að vera setning í umsagnarökfræði, rétt eins og
við gerðum fyrir táknrunur í setningarökfræði í kafla
§\ `[tfl:SentencesDefined] <#tfl:SentencesDefined>`__.

Táknrunur
~~~~~~~~~

Það eru sex mismunandi gerðir af táknum í umsagnarökfræði:

.. container:: center

   ========================= ==============================================
   Umsagnir                  :math:`A,B,C,\ldots,Z`
   með lágvísum eftir þörfum :math:`A_1, B_1,Z_1,A_2,A_{25},J_{375},\ldots`
   \                         
   Nöfn                      :math:`a,b,c,\ldots, r`
   með lágvísum eftir þörfum :math:`a_1, b_{224}, h_7, m_{32},\ldots`
   \                         
   Breytur                   :math:`s, t, u, v, w, x,y,z`
   eftir þörfum              :math:`x_1, y_1, z_1, x_2,\ldots`
   \                         
   Setningatengi             :math:`\enot,\eand,\eor,\eif,\eiff`
   \                         
   Svigar                    ( , )
   \                         
   Magnarar                  :math:`\forall, \exists`
   ========================= ==============================================

Við skilgreinun sem hvaða streng sem er af táknum umsagnarökfræði. Hvaða
tákn sem er, sem fengin eru úr listanum hér að ofan, í hvaða röð sem er,
telst vera táknruna í umsagnarökfræði.

.. _formula:

Einnefni og formúlur
~~~~~~~~~~~~~~~~~~~~

Í §\ `[s:TFLSentences] <#s:TFLSentences>`__ skilgreindum við hvað
*setning* er með því að nota það sem við kölluðum þrepunarskilgreiningu:
Við skilgreindum grunnsetningar og smíðuðum svo fleiri og fleiri
setningar úr þeim með því að nota ákveðnar reglur. Vegna þesss hvernig
setningar í umsagnarökfræði eru byggðar upp, þá getum við ekki alltaf
tryggt að hægt sé að smíða setningar úr öðrum setningum á sama hátt og
áður. Til dæmis, þá þurfum við einhverja leið til að tengja saman
magnara og breytu annars vegar, t.d. :math:`\forall x`, og einhverja
aðra táknrunu, hinsvegar, t.d. :math:`(x = x)`. Ef við fylgjum þeirri
venju að kalla setningar allt það sem getur verið satt eða ósatt, þá
sjáum við að þessar tvær táknrunur sem saman mynda setninguna
:math:`\forall x(x = x)` eru ekki sjálfar setningar.

Við munum því skilgreina nýtt hugtak, *formúlur*. Formúla er táknruna
sem er annað hvort setning eða hægt er að breyta í setningu með að bæta
magnara og breytu fyrir framan. Þegar við skilgreinum formúlur, þá munum
við nota rakta skilgreiningu, rétt eins og í setningarökfræðinni, svo í
raun er fátt nýtt á ferðinni.

Við byrjum á að skilgreina hvað einnefni er. Hér eru nokkur einnefni:

.. math:: a, b, x, x_1 x_2, y, y_{254}, z

Næst skilgreinum við *grunnformúlur*. Hér notum við feitletraða stafi
sem metabreytur, rétt eins og við notuðum feitletraða stafi fyrir
setningar í setningarökfræði. :math:`\meta{R}` er því ekki sjálf umsögn,
heldur er hluti af framsetningarmálinu og talar um allar umsagnir í
umsagnarökfræði. Á sama hátt er :math:`\meta{t}_1` ekki einnefni, heldur
tákn í framsetningarmálinu sem við notum til að tala um öll einnefni.
Hér munum við nota feitletraða stafi til að tákna formúlur *eða*
setningar, allt eftir samhengi.

Fyrsta klausan hér að ofan segir því bara að ef við fyllum einhverja
umsögn með eins mörgum einnefnum og við getum, það er að segja, í
samræmi við hversu mörg sæti eru í umsögninni, þá verði niðurstaðan
formúla.

Segum til dæmis að :math:`F` sé einsæta umsögn, :math:`G` þriggja sæta
umsögn og :math:`S` sex sæta umsögn. Þá eru hér nokkrar grunnformúlur:

.. container:: center

   | :math:`x = a`
   | :math:`a = b`
   | :math:`Fx`
   | :math:`Fa`
   | :math:`Gxay`
   | :math:`Gaaa`
   | :math:`Sx_1 x_2 a b y x_1`
   | :math:`Sby_{254} z a a z`

:math:`Fxy` væri hins vegar ekki formúla, því hér hefðum við reynt að
setja tvær breytur á einsæta umsögn. :math:`Gxa` væri heldur ekki
formúla, því hún er þriggja sæta umsögn og hér hefur hún bara verið
fyllt af tveimur einnefnum. Reglan er einföld: Umsagnir fá jafnmörg
einnefni og fjöldi sæta segir til um.

Nú þegar við vitum hvað grunnformúlur eru, þá getum við notað rakta
skilgreiningu og búið til eins margar formúlur og við viljum. Fyrstu
klausurnar eru þær sömu og í setningarökfræðinni, nema við skilgreinum
formúlur, en ekki setningar:

Ef við gerum aftur ráð fyrir að :math:`F` sé einsæta umsögn, :math:`G`
þriggja sæta umsögn og :math:`S` sex sæta umsögn, þá eru hér nokkrar
formúlur:

.. container:: center

   | :math:`Fx`
   | :math:`Gayz`
   | :math:`Syzyayx`
   | :math:`(Gayz \eif Syzyayx)`
   | :math:`\forall z (Gayz \eif Syzyayx)`
   | :math:`Fx \eiff \forall z (Gayz \eif Syzyayx)`
   | :math:`\exists y (Fx \eiff \forall z (Gayz \eif Syzyayx))`
   | :math:`\forall x \exists y (Fx \eiff \forall z (Gayz \eif Syzyayx))`

En þetta er *ekki* formúla samkvæmt skilgreiningunni okkar:

.. container:: center

   :math:`\forall x \exists x Gxxx`

:math:`Gxxx` er vissulega formúla. Og :math:`\exists x Gxxx` er því
vissulega líka formúla. En við getum ekki búið til nýja formúlu með því
að setja :math:`\forall x` fyrir framan hana. Það myndi ganga í berhögg
við klausu 7 í skilgreiningunni okkar að ofan: Formúlan
:math:`\exists x Gxxx` inniheldur nú þegar minnst eitt :math:`x`, en
líka :math:`\exists x`.

Ástæðan fyrir því að við viljum takmarka hvaða formúlur við getum smíðað
með þessum hætti er sú að þannig getum við tryggt að hver breyta lúti
einungis stjórn eins magnara í einu (sjá
§\ `3 <#s:MultipleGenerality>`__). Við getum raunar núna gefið formlega
skilgreiningu á sviði, þar með talið sviði magnara. Þessi skilgreining
er svipuð og í setningarökfræðinni, nema við notum hugtakið til að tákna
setningatengi eða magnara:

Við getum núna sýnt svið virkjanna í síðasta dæminu hér að ofan
myndrænt:

.. math:: \overbrace{\forall x \overbrace{\exists y (Fx \eiff \overbrace{\forall z (Gayz \eif Syzyayx)}^{\text{svið `}\forall z\text{'}}}^{\text{svið `}\exists y\text{'}})}^{\text{svið `}\forall x\text{'}}

Setningar í umsagnarökfræði
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Í rökfræði veltum við nær eingöngu fyrir okkur setningum sem geta verið
annað hvort sannar eða ósannar. En ekki eru allar formúlur setningar.
Notum til dæmis eftirfarandi þýðingarlykil:

.. container:: ekey

   fólk

   elskar

   Ólafur

Allar grunnformúlur eru formúlur, og því er grunnformúlan :math:`Lzz`
formúla. En er hún sönn eða ósönn? Maður gæti haldið að hún væri ósönn
eff sá sem vísað er til með „\ :math:`z`\ “ elskar sjálfan sig, rétt
eins og formúlan :math:`Loo` er sönn ef og aðeins ef Ólafur (sá sem
nafnið „\ :math:`o`\ “ vísar til) elskar sjálfan sig. *En
„\ :math:`z`\ “ er breyta, og vísar því ekki til neins ákveðins hlutar í
yfirgripinu*. Breytur eru einfaldlega ekki þannig tákn að þær vísi til
hluta einar og sér.

Ef við myndum hins vegar, til dæmis, setja tilvistarmagnara fyrir framan
setninguna þannig að hún yrði :math:`\exists x L zz`, þá væri setningin
sönn ef og aðeins ef einhver elskar sjálfan sig. Á sama hátt væri
setningin :math:`\forall z Lzz` sönn eff allir elska sjálfan sig. Við
notum sem sagt magnara til að segja okkur hvernig breyturnar í
setningunni skuli túlkaðar.

Við getum tjáð þessa hugmynd á nákvæmari hátt:

Skoðum nú sem dæmi formúluna

.. math:: (\forall x(Ex \eor Dy) \eif \exists z(Ex \eif Lzx))

\ Svið almagnarans „\ :math:`\forall x`\ “ er
:math:`\forall x (Ex \eor Dy)`, svo fyrsta :math:`x`-ið er bundið af
almagnaranum. En annað og þriðja :math:`x`-ið eru ekki innan sviðs neins
magnara, og eru því frjáls. Hið sama gildir um fyrsta :math:`y`-ið. Svið
tilvistarmagnarans er svo :math:`(Ex \eif Lzx)` og því er :math:`z`
bundin.

Nú getum við loksins skilgreint: Með öðrum orðum, setning í
umsagnarökfræði er formúla þar sem allar breytur eru bundnar—falla innan
sviðs einhvers magnara sem bindur viðeigandi breytu.

Svigavenjur
~~~~~~~~~~~

Í umsagnarökfræðinni munum við nota sömu svigavenjur og í
setningaörkfræðinni (sjá §\ `[s:TFLSentences] <#s:TFLSentences>`__ og
§\ `[s:MoreBracketingConventions] <#s:MoreBracketingConventions>`__).
Þær voru í stuttu máli þessar:

-  Við leyfum okkur að sleppa ystu svigum í formúlu.

-  Við megum nota hornklofa, „[“ og „]“ í stað venjulegra sviga til að
   auðvelda lestur á formúlum, þó að þeir séu tæknilega séð ekki hluti
   af táknmáli umsagnarökfræði.

-  Við megum sleppa svigum milli samtenginga, þegar við skrifum langa
   runu af samteningum.

-  Hið sama gildir um langar runur af mistengingum, setningum sem eru
   tengdar saman með eða-tengjum: við megum sleppa svigum á milli þeirra
   í slíkri runu.

Hávísar á umsögnum
~~~~~~~~~~~~~~~~~~

Við sögðum hér að ofan að :math:`n` einnefni á eftir :math:`n`-sæta
umsögn sé grunnformúla. En það er ákveðinn galli við þessa
skilgreiningu: táknin sem við notum fyrir umsagnirnar bera það ekki utan
á sér hversu mörg sæti þau hafa. Stundum höfum við notað :math:`G` sem
einsæta umsögn, stundum sem þriggja sæta umsögn, og svo framvegis. Svo
ef það er ekki beinlínis tekið fram í það og það skiptið hversu mörg
sæti :math:`G` hefur, þá er *óákvarðað* hvort :math:`Ga`, svo við tökum
dæmi, sé grunnformúla eða ekki.

Það er til einföld leið út úr þessum vanda, sem er oft farin í
kennslubókum í rökfræði: Í stað þess að segja að táknin fyrir umsagnir
séu hástafir (með lágvísum eftir þörfum), þá er sagt að þær sú hástafir
með *hávísum* (og svo lágvísum eftir þörfum). Tilgangur hávísanna er þá
að segja til um hversu mörg sæti hver umsögn er. Þannig væri :math:`G^1`
einsæta umsögn og :math:`G^3` þriggja sæta umsögn. Þetta væru tvær
mismunandi umsagnir og þyrftu hver sína línu í þýðingarlykli.
:math:`G^1a` væri þá grunnformúla, en ekki :math:`G^3a`, rétt eins og
:math:`G^3abc` væri grunnformúla, en ekki :math:`G^1abc`.

Við *gætum* farið þessa leið. Þetta myndi hafa þann kost í för með sér
að það væri alltaf fullkomlega ljóst hvort réttur fjöldi einnefna fylgi
hverri umsögn. En það hefði líka þann ókost að formúlurnar sem yrðu til
með slíkum umsögnum yrðu mun þyngri í lestri, ekki síst ef lágvísar
fylgdu með líka, til dæmis: :math:`G^3_5xae`. Við munum því ekki fara
þessa leið. Umsagnirnar okkar munu vera án hávísa (enda taka langflestar
kennslubækur sem nota þá strax upp þá venju að sleppa þeim).

Þetta þýðir þó að ákveðin tvíræðni er möguleg. En í raun er þetta
sjaldan vandamál, og ef einhver hætta er á misskilningi, þá tökum við
bara fram hversu mörg sæti hver umsögn hefur.

Tilgreinið hvaða breytur eru frjálsar og hverjar eru bundnar.

.. container:: earg

   :math:`\exists x Lxy \eand \forall y Lyx`

   :math:`\forall x Ax \eand Bx`

   :math:`\forall x (Ax \eand Bx) \eand \forall y(Cx \eand Dy)`

   :math:`\forall x\exists y[Rxy \eif (Jz \eand Kx)] \eor Ryx`

   :math:`\forall x_1(Mx_2 \eiff Lx_2x_1) \eand \exists x_2 Lx_3x_2`

.. [1]
   „Umsagnarökfræði“ er þýðing á því sem á ensku er kallað „predicate
   logic“. Á ensku er algengara að talað sé um „first-order logic“, sem
   myndi útleggjast á íslensku sem „rökfræði fyrstu stéttar“. Það er
   hins vegar óþjált og alls ekki nákvæmara. Við munum því forðast þetta
   hugtak.

   En þá vakna auðvitað spurningarnar, „ hvað er þetta ‘fyrstu
   stéttar’?“ og eru þær fleiri en ein? Svarið við seinni spurningunni
   er já og við munum aðeins fjalla um hvað þetta merkir í kafla
   `6.5 <#>`__.

.. [2]
   Glöggir lesendur taka kannski eftir því að við skilgreindum
   „rökfræðilegt jafngildi“ á tæknilegan hátt fyrir setningar í
   setningarökfræði, nefnilega þannig að tvær setningar eru rökfræðilega
   jafngildar ef þær eru sannar og ósannar fyrir sömu
   sanngildadreifingar. En við höfum ekki skilgreint neitt svipað fyrir
   umsagnarökfræði. Það munum við gera seinna.

.. [3]
   Ef fleira en fólk væri í yfirgripinu, þá yrðum við að bæta við
   umsögninni „M: er manneskja við þýðingarlykilinn okkar og þýða
   setninguna sem :math:`\forall x (Mx \eif Sax)`. Með því að einskorða
   yfirgripið við fólk, þá þurfum við ekki að þrengja umfjöllunarefnið
   með þessum hætti með skilyrðissetningu.

.. [4]
   Það er raunar líka hættulaust að sleppa bara svigunum og skrifa
   „\ \ :math:`\enot a = b`\ \ “, en slíkt er erfitt í lestri og oft
   ruglandi.

.. [5]
   Hér er einfaldlega metabreyta sem á við allar breytur.

.. [6]
   Bertrand Russell, „On Denoting“, 1905, *Mind 14*, bls. 479–93.

.. [7]
   P.F. Strawson, „On Referring“, 1950, *Mind 59*, bls. 320–34.

.. [8]
   Keith Donnellan, „Reference and Definite Descriptions“, 1966,
   *Philosophical Review 77*, bls. 281–304.

.. [9]
   Sjá til dæmis Saul Kripke, „Speaker Reference and Semantic
   Reference’“, 1977.
