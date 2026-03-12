.. _ch.NDFOL:

Náttúruleg afleiðsla fyrir umsagnarökfræði
==========================================

.. _`s:BasicFOL`:

Grunnreglur náttúrulegrar afleiðslu fyrir umsagnarökfræði
---------------------------------------------------------

Táknmál umsagnarökfræði notar öll sömu setningatengin og
setningarökfræðin. Sannanir í umsagnarökfræði munu því líka nota sömu
reglur sannanir í setningarökfræði, bæði grunnreglurnar og afleiddar
reglur (sjá §\ `[ch.NDTFL] <#ch.NDTFL>`__). Við munum líka nota sömu
sönnunarfræðilegu hugtök og setningarökfræðin studdist við, og voru
kynnt til sögunnar í þeim kafla, einkum og sér í lagi táknið
„\ :math:`\proves`\ “. Við þurfum hins vegar nýjar reglur fyrir
magnarana og samsemdarmerkið.

Rétt eins og í tilfelli setningarökfræði, þá skilgreinum við
innleiðingar- og eyðingarreglur fyrir hvert tákn.

Almagnaraeyðing
~~~~~~~~~~~~~~~

Ef við vitum að allt sé :math:`F`, þá getum við dregið þá ályktun að
sérhver tiltekinn hlutur sé :math:`F`—nefndu það, sá hlutur er
:math:`F`. Það er að segja ef allt er :math:`F`, þá er :math:`a` líka
:math:`F`, og :math:`b`, og :math:`c\ldots` Eftirfarandi ætti því að
vera í lagi:

.. container:: proof

   *Proof.* ◻

Hér höfum við :math:`\forall xRxxd` sem forsendu, og fáum línu 2 með því
að fjarlægja almagnarann og setja nafnið „\ :math:`a`\ “ í stað
breytunnar :math:`x`, allstaðar þar sem hún kemur fyrir. Eftirfarandi
ætti líka að vera í lagi:

.. container:: proof

   *Proof.* ◻

Hér höfum við gert það sama, nema við höfum skipt út :math:`x` fyrir
„\ :math:`d`\ “ allstaðar þar sem :math:`x` kemur fyrir. Við hefðum
getað gert slíkt hið sama fyrir hvaða nafn sem er annað, enda hlýtur það
sem gildir um allt í yfirgripinu líka að gilda um allt sem við höfum
nafn yfir, því það er jú hluti af yfirgripinu.

Almennt form almagnaraeyðingar (:math:`\forall`\ E) er því þetta:

Þessi ritháttur var kynntur til sögunnar í
§\ `[s:TruthFOL] <#s:TruthFOL>`__. Í stuttu máli, þá merkir
:math:`\meta{A}(\ldots \meta{x} \ldots \meta{x}\ldots)` formúlu þar sem
breytan :math:`\meta{x}` kemur fyrir að minnsta kosti einu sinni fyrir í
formúlunni :math:`\meta{A}` og :math:`\meta{x}` er óbundin, og
:math:`\meta{A}(\ldots \meta{c} \ldots \meta{c}\ldots)` merkir formúlu
þar sem öllu :math:`\meta{x}`-unum í
:math:`\meta{A}(\ldots \meta{x} \ldots \meta{x}\ldots)` hefur verið
skipt út fyrir :math:`\meta{c}`. Þetta þýðir sem sagt bara að þegar við
beitum reglunni, þá tökum við almagnarann framan af, og skiptum út öllum
breytunum sem hann bindur út fyrir eitthvað nafn.

Við megum þó ekki gleyma að við getum *bara* beitt þessari reglu, rétt
eins og gildir um allar eyðingarreglur, þegar almagnarinn er aðalvirkinn
í setningunni. Eftirfarandi er því *ekki* leyfilegt:

.. container:: proof

   *Proof.* ◻

Hér er „\ :math:`\forall x`\ “ ekki aðalvirkinn í línu 1, heldur
„\ :math:`\eif`\ “. Þessi rökfærsla er ógild (forsendan er nauðsynlega
sönn, en niðurstaðan ekki. Það sýnir að eitthvað hefur farið úrskeiðis).
Þetta eru mjög algeng mistök byrjenda, svo það er vel þess virði að taka
vel eftir þessu.

Innleiðing tilvistarmagnara
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef við vitum að einhver tiltekinn hlutur er *F*, þá getum við dregið þá
ályktun að eitthvað sé *F*—nefnilega það sem við vissum að væri *F*.
Eftirfarandi ætti því að vera í lagi:

.. container:: proof

   *Proof.* ◻

Hér höfum við skipt út nafninu „\ :math:`d`\ “ fyrir breytuna
„\ :math:`x`\ “ og bundið hana svo við magnara. Við hefðum líka getað
farið aðra leið:

.. container:: proof

   *Proof.* ◻

Hér höfum við skipt út nafninu „\ :math:`a`\ “ út á tveimur stöðum fyrir
breytuna :math:`x` og bundið hana við magnara. Hér hefðum við ekki þurft
að skipta út nafninu „\ :math:`a`\ “ á báðum stöðum: Ef Ólafur elskar
sjálfan sig, þá er jú einhver sem elskar Ólaf. Eftirfarandi er því líka
leyfilegt:

.. container:: proof

   *Proof.* ◻

Hér höfum við skipt út nafninu „\ :math:`a`\ “ fyrir :math:`„x“` á öðrum
af tveimur stöðum þar sem það kemur fyrir, og svo bundið hana með
tilvistarmagnara. Þessi dæmi liggja að baki almennu formi reglunnar, en
til að geta gefið slíkt form þurfum við fyrst að að kynna til sögunnar
nýjan rithátt, líkan þeim sem við notuðum hér að ofan.

Hann er svona: Ef :math:`\meta{A}` er formúla þar sem nafnið
:math:`\meta{c}` kemur fyrir, þá getum við skrifað

.. math:: \meta{A}(\ldots \meta{c} \ldots \meta{c}\ldots)

\ til að gefa það til kynna. Við getum svo skrifað

.. math:: \meta{A}(\ldots \meta{x} \ldots \meta{c}\ldots)

til að tákna formúlu þar sem sumum (og hugsanlega öllum)
:math:`\meta{c}`-unum í :math:`\meta{A}` hefur verið skipt út fyrir
breytuna :math:`\meta{x}`.

Með þennan rithátt að vopni, þá getum við loks gefið almennt form
reglunnar:

Þessi síðasta klausa er til að tryggja að táknrunan sem verður til við
skiptinguna sé setning í umsagnarökfræði. Eftirfarandi er því leyfilegt:

.. container:: proof

   *Proof.* ◻

En svona er bannað:

.. container:: proof

   *Proof.* ◻

Táknrunan á línu 3 inniheldur breytu sem er innan sviðs tveggja magnara
sem báðir reyna að stjórna henni, og því er hún ekki setning á táknmáli
umsagnarökfræði. Klausan sem við bættum við regluna kemur í veg fyrir að
þetta geti gerst.

.. _tomtyfirgrip:

Tóm yfirgrip
~~~~~~~~~~~~

Eftirfarandi sönnun notar báðar reglurnar sem við höfum kynnst fram að
þessu:

.. container:: proof

   *Proof.* ◻

Erum við viss um að þessi sönnun sé í lagi? Ef eitthvað er til
yfirleitt, þá getum við vissulega dregið þá ályktun að eitthvað sé
:math:`F`, ef allt er :math:`F`. En hvað ef *ekkert* væri til? Þá er það
samt satt að allt sé :math:`F`, þ.e. setningin :math:`\forall x Fx` er
sönn. Af hverju?

Ein ástæða sem oft er gefin er að þá getum við aldrei fundið mótdæmi:
það er ekkert :math:`x` sem er *ekki* :math:`F`. Það er í raun alveg
nógu góð ástæða, því eins og við höfum skilgreint magnarana, þá er
setningin :math:`\forall x Fx` er jafngild setningunni
:math:`\enot \exists x \enot Fx`, en hún segir að það sé ekki til
:math:`x` sem er ekki-:math:`F` (og raunar getum við sannað þetta
jafngildi síðar í þessum kafla). En ef yfirgripið er tómt, þá hlýtur
þessi setning að vera sönn, því ef :math:`\enot \exists x \enot Fx` væri
ósönn, þá væri setningin :math:`\exists x \enot Fx` sönn, og það getur
ekki verið ef yfirgripið er tómt. Í kaflanum um afleiddar reglur í
umsagnarökfræði hér að neðan (§\ `4 <#s:DerivedFOL>`__) sjáum við svo af
hverju við erum í raun nauðbeygð til að samþykkja þetta jafngildi.

En leiðir þá af því að :math:`\forall x Fx` sé sönn ef yfirgripið er
tómt að til sé :math:`x` sem er :math:`F`? Einmitt ekki! Við verðum því
að hafa eitthvað í yfirgripinu, ef við viljum að sönnunin sem við
skoðuðum hér að ofan sé góð (og þar með að þessar augljósu reglur fyrir
magnarana séu gildar). En það þýðir auðvitað líka að við þurfum að
samþykkja að það sé rökfræðileg staðreynd að eitthvað sé til fremur en
ekkert—ef við viljum segja að :math:`\exists x Fx` leiði af
:math:`\forall x Fx` rökfræðilega.

Það gæti einhverjum fundist of langt gengið. En við erum í raun nú þegar
búin að taka þessa ákvörðun. Í
§\ `[s:FOLBuildingBlocks] <#s:FOLBuildingBlocks>`__ sögðum við að
yfirgrip í umsagnarökfræði mættu ekki vera tóm. Setning í
umsagnarökfræði er svo rökfræðilega sönn ef og aðeins ef hún er sönn
fyrir allar túlkanir—það er að segja sönn sama hvað.
:math:`\exists x(x = x)` er sönn sama hvað, og af því leiðir
rökfræðilega að eitthvað sé til.

En einhver gæti maldað í móinn og neitað því einfaldlega að það sé
rökfræðileg staðreynd að eitthvað sé til. [1]_ Þetta er bara tómt
svindl! En ef við neitum að svindla með þessum hætti, hverjar eru
afleiðingarnar? Hér er þrennt sem við viljum halda í:

.. container:: ebullet

   :math:`\forall x Fx \proves Fa`: þetta er reglan :math:`\forall`\ E.

   :math:`Fa \proves \exists x Fx`: þetta er reglan :math:`\exists`\ I.

   að geta klippt og límt saman sannanir: ef við getum sannað
   :math:`\meta{A} \proves \meta{B}` og
   :math:`\meta{B} \proves \meta{C}`, þá viljum við geta sannað
   :math:`\meta{A} \proves \meta{C}` með því að taka fyrri sönnunina og
   setja hana fyrir framan seinni sönnunina.

Ef við viljum halda þessu þrennu, þá verðum við að samþykkja (með
semingi eða ekki) að :math:`\forall xFx \proves \exists x Fx`. Það
leiðir af þessu að rökfræðin okkar hlýtur að segja að eitthvað sé til
fremur en ekkert. Ef við viljum ekki viðurkenna það, þá þurfum við að
hafna einhverju af þessu—augljósum reglum, eða getunni til að klippa og
líma saman sannanir, sem sjálf virðist augljós.

En áður en við förum að velja eitthvað af þessu til að hafna, þá ættum
við kannski frekar að spyrja okkur hversu *mikið* svindl þetta er. Jú,
það verður erfiðara að eiga í heimspekilegum eða guðfræðilegum rökræðum
um það af hverju eitthvað er til frekar en ekkert, en að öðru leyti
skiptir þetta okkur litlu—við gerum jú langoftast ráð fyrir því að
eitthvað sé til þegar við beitum rökhugsuninni. Við ættum því kannski
bara að bíta í þetta súra epli og taka þá reglu í sátt að yfirgripið
megi ekki vera tómt. Ef við viljum svo eiga í slíkum rökræðum síðar, þá
gætum við farið að leita okkur að flóknara sannanakerfi. Þangað til er
óþarfi að rugga bátnum.

Almagnarainnleiðing
~~~~~~~~~~~~~~~~~~~

Segjum sem svo að við höfum sannað um hvern einasta hlut í yfirgripinu
að hann sé :math:`F`. Þá getum við hikstalaust sagt að allt sé
:math:`F`. Okkur gæti þá dottið í hug að það væri góð regla fyrir
almagnarainnleiðingu að segja sem svo að ef við getum sannað að
:math:`F\meta{c}` fyrir hvert og eitt :math:`\meta{c}`, þá getum við
dregið þá ályktun að :math:`\forall x Fx`.

En því miður væri slík regla ónothæf. Það væri nefnilega ekki nóg að
sanna :math:`F\meta{c}` fyrir þau nöfn sem til eru í einhverjum
þýðingarlykli, því yfirgripið getur alltaf verið (og oftast er) stærra
en fjöldi nafna sem við höfum tekið fram gefur til kynna, og það sem
verra er, oft er það óendanlegt. Til að sanna :math:`F\meta{c}` fyrir
öll :math:`\meta{c}`, þyrfti því að gefa öllu í yfirgripinu nafn og
sanna svo fyrir hvert og eitt nafn að :math:`F\meta{c}`—til dæmis að
:math:`Fa`, :math:`Fb`, :math:`\ldots`, :math:`Fj_1`, :math:`Fj_2`,
:math:`\ldots`, :math:`Fr_{79002}`, :math:`\ldots` og svona mætti lengi
telja. Raunar eru óendanlega mörg möguleg nöfn í táknmáli
umsagnarökfræði, og því myndi sönnun af þessu tagi aldrei taka enda. Við
gætum því aldrei beitt slíkri reglu. Við þurfum að vera útsjónarsamari.

Byrjum á að skoða eftirfarandi rökfærslu:

.. math:: \forall x Fx \therefore \forall y Fy

\ Þessi rökfærsla er greinilega gild: það skiptir engu máli hvaða
breytunöfn við notum, svo forsendan og niðurstaðan segja það sama. En
hvernig ættum við að sanna þetta? Við gætum byrjað á sönnun svona:

.. container:: proof

   *Proof.* ◻

Nú höfum við sannað :math:`Fa`. En við hefðum getað notað hvaða nafn
sem! Við hefðum getað sannað :math:`Fb`, :math:`Fb`, :math:`Fj_1`,
:math:`Fj_2`, :math:`\ldots`, :math:`Fr_{79002}`, :math:`\ldots` eða
hvað sem er. Með þetta í huga, þá sjáum við að í vissum skilningi er
hægt að sanna :math:`F\meta{c}`, fyrir hvaða :math:`\meta{c}` sem er,
því ef við *gætum gert* þetta fyrir hvaða nafn sem er, þá er í raun
engin ástæða til að *gera* það fyrir hvaða nafn sem er. Við ættum að
geta sagt að :math:`F` *sé* satt um allt, bara af því að við vitum að
við hefðum getað sagt það um hvað sem. Við ættum því að geta klárað
sönnunina svona:

.. container:: proof

   *Proof.* ◻

Lykilhugsunin hér er að það er ekkert sérstakt við :math:`a`—það er bara
nafn sem við veljum *af handahófi*. Við hefðum getað valið hvaða nafn
sem er annað og sönnunin hefði ekkert breyst. Það er þessi hugsun sem
liggur að baki almennu formi innleiðingarreglunnar fyrir almagnarann
(:math:`\forall`\ I): Lykilhugsunin birtist í fyrri klausunni. Hún
tryggir að nafnið sem við veljum sé af handahófi og hefði allt eins
getað gilt um hvað sem er annað í yfirgripinu. [2]_

Þessi regla er oft erfið fyrir byrjendur, sem finnst eins og einhvers
staðar liggi fiskur undir steini, að það hljóti bara að vera eitthvað
svindl hérna á ferðinni. En svo er ekki: ef nafnið sem við notum gengur
ekki í berhögg við þau skilyrði sem reglan setur, þá hefðum við í raun
getað notað hvaða nafn sem er annað, og þá hlýtur umsögnin að gilda um
allt.

Tökum tvö dæmi um óleyfilega notkun nafna með þessari reglu, sem
hugsanlega gæti skýrt betur af hverju hún virkar í raun og veru. Notum
eftirfarandi þýðingarlykil:

.. container:: ekey

   er skemmtilegur

   er hress

   Jón

Gerum ráð fyrir að við vitum að Jón sé skemmtilegur. Þá gætum við
kannski reynt eftirfarandi:

.. container:: proof

   *Proof.* Sj Hj Sj 1̊ Hj Sj x (Hx Sx) ◻

Forsendan segir að Jón sé skemmtilegur og niðurstaðan að ef allir eru
hressir, þá eru þeir skemmtilegir. Hér hefur greinilega eitthvað farið
úrskeiðis, því það sem er satt um Jón þarf alls ekkert að vera satt um
alla. Sumir eru kannski þannig að ef þeir eru hressir, þá eru þeir
frekar óþolandi!

Vandinn hér er að nafnið :math:`j` hefur þegar verið notað um Jón og því
getum við ekki notað innleiðingarregluna fyrir almagnarann. Nafnið kemur
fyrir í ólosaðri forsendu og var því ekki valið af handahófi—við alhæfum
um það sem við vitum bara að á við um Jón.

Hér er annað dæmi:

   Allir elska Gísla Martein; þar af leiðandi elska allir sjálfa sig.

Þetta er greinilega ógild rökfærsla, sem við gætum ef til vill táknað
svona:

.. math:: \forall x Lxg \therefore \forall x Lxx

Segjum svo að við viljum reyna að sanna þessa afleitu rökfærslu með
eftirfarandi tilraun til sönnunar:

.. container:: proof

   *Proof.* ◻

Þetta er ekki leyfilegt, því :math:`g` kemur fyrir í ólosaðri forsendu,
nefnilega í línu 1. Við verðum alltaf að hafa í huga að ef við höfum
gefið okkur eitthvað um tiltekinn hlut, hvort sem að það er í forsendu
eða aukaforsendu, þá getum við ekki notað :math:`\forall`\ I í línu þar
sem nafnið yfir þann hlut kemur fyrir.

Athugið þó að reglan segir einungis að nafnið megi ekki koma fyrir í
*ólosaðri* forsendu. Það er í fínu lagi að það komi fyrir í *losaðri*
forsendu—það er að segja, í hlutasönnun sem við höfum þegar lokað. Þessi
sönnun er til dæmis í lagi:

.. container:: proof

   *Proof.* ◻

Þetta segir okkur að :math:`\forall z (Gz \eif Gz)` sé *sannanleg
setning* og það ætti hún líka að vera.

Það er eitt í viðbót sem við verðum að hafa í huga. Þegar við notum
:math:`\forall`\ I, þá verðum alltaf að skipta út öllum -um sem koma
fyrir í :math:`\meta{A}(\ldots \meta{x}\ldots\meta{x}\ldots)` fyrir . Ef
við skiptum bara út *sumum* -um, þá gætum við „sannað“ ansi skrýtna
hluti. Til dæmis:

   Allir eru jafngamlir sjálfum sér; þar af leiðandi eru allir jafn
   gamlir og Ingimundur gamli.

Við gætum þýtt þessa rökfærslu svona:

.. math:: \forall x Gxx \therefore \forall x Gxi

Athugum þá eftirfarandi tilraun til sönnunar:

.. container:: proof

   *Proof.* ◻

En reglurnar okkar leyfa þetta ekki, sem betur fer. Þessi sönnun er
óleyfileg, því við skiptum ekki út nafninu :math:`d` út fyrir breytuna
:math:`x` *alls staðar* þar sem það kom fyrir í línu 2.

Summagnaraeyðing
~~~~~~~~~~~~~~~~

Þá er eftir summagnaraeyðing. Segjum að við vitum að *eitthvað* sé *F*.
Ef við vitum það, þá vitum við því miður ekki mjög margt. Til dæmis
höfum við ekki hugmynd um hvað það er sem er :math:`F`. Það virðist því
sem við getum ekki sagt neitt um hvort tilteknar setningar á forminu
:math:`F\meta{c}` séu sannar. Hvað getum við þá gert?

Hvað ef við vitum að eitthvað sé :math:`F` og að allt sem er :math:`F`,
sé :math:`G`? Þá gætum við kannski hugsað sem svo:

   Fyrst eitthvað er :math:`F`, þá er einhver tiltekinn hlutur sem er
   :math:`F`. Við vitum ekkert um þennan hlut, annað en að hann sé
   :math:`F`. Köllum þennan hlut, hver sem hann er, bara :math:`a` til
   hægðarauka. Þá er :math:`a` :math:`F`. Fyrst við vitum að allt sem er
   :math:`F` er :math:`G`, þá vitum við að :math:`a` er :math:`G`. En þá
   leiðir af því að eitthvað er :math:`G`, nefnilega :math:`a`. Þar sem
   nafnið skiptir í raun engu máli, þá vitum við að eitthvað er
   :math:`G`.

Við gætum reynt að fanga þessa rökfærslu með eftirfarandi sönnun:

.. container:: proof

   *Proof.* ◻

Við byrjuðum á því að skrifa niður forsendurnar okkar. Í línu 3 gáfum
við okkur svo aukaforsendu, :math:`Fa`. Þetta er bara innsetningartilvik
af :math:`\exists x Fx`—þ.e. magnarinn tekinn af og nafn sett í stað
breytunnar. Að því gefnu gátum við sýnt að :math:`\exists x Gx`. En við
gáfum okkur *ekkert sérstakt* um hlutinn sem nafnið :math:`a` vísar til,
nema að hann uppfylli :math:`\exists x Fx`. Það skiptir því engu máli
hvaða hlutur það er í raun og veru, því við vitum af línu 1 að
*eitthvað* uppfyllir :math:`\exists x Fx`. Þessi rökfærsla er því
fullkomlega almenn og ættum því að geta lokað hlutasönnuninni og losað
forsenduna og dregið þá ályktun að :math:`\exists x Gx`.

Þetta er hugsunin sem liggur að baki almennu formi reglunnar fyrir
summagnaraeyðingu (:math:`\exists`\ E): Rétt eins og í tilfelli
almagnarainnleiðingar eru þessar aukaklausur mjög mikilvægar. Hér eru
dæmi um afleita rökfærslu:

   Júlía er rökfræðingur. Einhver er ekki rökfræðingur. Þar af leiðandi
   er Júlía bæði rökfræðingur og ekki rökfræðingur.

Við gætum þýtt þessa hræðilegu rökfærslu yfir á táknmál umsagnarökfræði
svona:

.. math:: Rj, \exists x \enot Rx \therefore Rj \eand \enot Rj

Hér er tilraun til sönnunar:

.. container:: proof

   *Proof.* æf, na ◻

Síðasta línan í þessari sönnun er ekki leyfileg. Nafnið sem við setjum
inn í stað fyrir :math:`x` í :math:`\exists x \enot Lx` á línu 3,
nefnilega :math:`j`, kemur fyrir í línu 4. Þetta væri ekki mikið betri
tilraun:

.. container:: proof

   *Proof.* æf, na ◻

Síðasta línan hér er heldur ekki leyfileg. Nafnið sem við setjum inn
fyrir í x í stað :math:`\exists x \enot Lx`, nefnilega :math:`b`, kemur
nefnilega fyrir í ólosaðri forsendu, í línu 1.

Það er þó til einföld leið til að tryggja að maður haldi sig alltaf
innan leyfilegra marka þegar þessi regla er notuð: Veljum bara
*splúnkunýtt* nafn í hlutasönnun summagnaraeyðingarinnar—nafn sem er
hvergi annars staðar sjáanlegt í sönnuninni.

Útskýrið af hverju þessar tvær tilraunir til sannanir eru ekki réttar.
Finnið upp á þýðingarlyklum sem sýna að rökfærslurnar sem reynt er að
sýna að séu gildar séu það ekki.

.. container:: multicols

   2

   .. container:: proof

      *Proof.* ◻

   .. container:: proof

      *Proof.* ◻

Í eftirfarandi tilraunum til sönnunar vantar réttar merkingar
(þ.e. tilvísanir í reglur og línunúmer). Bætið þeim við til að klára
sannanirnar.

.. container:: proof

   *Proof.* ◻

.. container:: multicols

   2

   .. container:: proof

      *Proof.* ◻

   .. container:: proof

      *Proof.* ◻

Í æfingunum í §\ `[s:MoreMonadic] <#s:MoreMonadic>`__, hluta A, skoðuðum
við fimmtán rökhendur sem koma fyrir í aristótelískri rökfræði. Finnið
sannanir fyrir hverja rökhendu. Ráðlegging: Þetta er mun einfaldara ef
„Engin :math:`F` eru :math:`G`\ “ er þýtt sem
:math:`\forall x (Fx \eif \enot Gx)`.  

Sannið eftirfarandi.

.. container:: earg

   :math:`\proves \forall x Fx \eor \enot \forall x Fx`

   :math:`\proves\forall z (Pz \eor \enot Pz)`

   :math:`\forall x(Ax\eif Bx), \exists x Ax \proves \exists x Bx`

   :math:`\forall x(Mx \eiff Nx), Ma\eand\exists x Rxa\proves \exists x Nx`

   :math:`\forall x \forall y Gxy\proves\exists x Gxx`

   :math:`\proves\forall x Rxx\eif \exists x \exists y Rxy`

   :math:`\proves\forall y \exists x (Qy \eif Qx)`

   :math:`Na \eif \forall x(Mx \eiff Ma), Ma, \enot Mb\proves \enot Na`

   :math:`\forall x \forall y (Gxy \eif Gyx) \proves \forall x\forall y (Gxy \eiff Gyx)`

   :math:`\forall x(\enot Mx \eor Ljx), \forall x(Bx\eif Ljx), \forall x(Mx\eor Bx)\proves \forall xLjx`

Finnið þýðingarlykil fyrir eftirfarandi rökfærslu, þýðið hana yfir á
táknmál umsagnarökfræði og sannið.

   Það er einhver sem elskar alla sem elskar alla sem hún elskar. Þar af
   leiðandi er einhver sem elskar sjálfan sig.

Sýnið að setningarnar í eftirfarandi setningapörum séu sannanlega
jafngildar, ef þær eru það, en finnið þýðingarlykil sem sýnir að þær eru
það ekki, annars.

.. container:: earg

   :math:`\forall x Px \eif Qc, \forall x (Px \eif Qc)`

   :math:`\forall x\forall y \forall z Bxyz, \forall x Bxxx`

   :math:`\forall x\forall y Dxy, \forall y\forall x Dxy`

   :math:`\exists x\forall y Dxy, \forall y\exists x Dxy`

   :math:`\forall x (Rca \eiff Rxa), Rca \eiff \forall x Rxa`

Sannið eftirfarandi rökfærslur, ef þær eru gildar. Ef þær eru ógildar,
finnið þýðingarlykil sem sýnir það.

.. container:: earg

   :math:`\exists y\forall x Rxy \therefore \forall x\exists y Rxy`

   :math:`\exists x(Px \eand \enot Qx) \therefore \forall x(Px \eif \enot Qx)`

   :math:`\forall x(Sx \eif Ta), Sd \therefore Ta`

   :math:`\forall x(Ax\eif Bx), \forall x(Bx \eif Cx) \therefore \forall x(Ax \eif Cx)`

   :math:`\exists x(Dx \eor Ex), \forall x(Dx \eif Fx) \therefore \exists x(Dx \eand Fx)`

   :math:`\forall x\forall y(Rxy \eor Ryx) \therefore Rjj`

   :math:`\exists x\exists y(Rxy \eor Ryx) \therefore Rjj`

   :math:`\forall x Px \eif \forall x Qx, \exists x \enot Px \therefore \exists x \enot Qx`

.. _`s:CQ`:

Umbreytingarreglur fyrir magnara
--------------------------------

Við bætum núna við reglum sem gera okkur kleift að umbreyta mögnurunum
hvora í aðra.

Í §\ `[s:FOLBuildingBlocks] <#s:FOLBuildingBlocks>`__ sögðum við að
:math:`\enot\exists x\meta{A}` væri rökfræðilega jafngilt
:math:`\forall x \enot\meta{A}`. Nú bætum við við reglum til að þetta
verði endurspeglað í sannanakerfinu okkar. Fyrsta regluparið sem við
bætum við er: og Svo þurfum við líka að bæta við: og

Sýnið að eftirfarandi setningar séu sannanlega andstæðar.

.. container:: earg

   :math:`Sa\eif Tm, Tm \eif Sa, Tm \eand \enot Sa`

   :math:`\enot\exists x Rxa, \forall x \forall y Ryx`

   :math:`\enot\exists x \exists y Lxy, Laa`

   :math:`\forall x(Px \eif Qx), \forall z(Pz \eif Rz), \forall y Py, \enot Qa \eand \enot Rb`

Sýnið fyrir hvert setningapar hér að neðan að setningarnar tvær séu
sannanlega jafngildar:

.. container:: earg

   :math:`\forall x (Ax\eif \enot Bx), \enot\exists x(Ax \eand Bx)`

   :math:`\forall x (\enot Ax\eif Bd), \forall x Ax \eor Bd`

Sýnið fyrir hvert setningapar hér að neðan að setningarnar tvær séu
sannanlega jafngildar:

.. container:: earg

   :math:`\forall x (Fx \eand Ga), \forall x Fx \eand Ga`

   :math:`\exists x (Fx \eor Ga), \exists x Fx \eor Ga`

   :math:`\forall x(Ga \eif Fx), Ga \eif \forall x Fx`

   :math:`\forall x(Fx \eif Ga), \exists x Fx \eif Ga`

   :math:`\exists x(Ga \eif Fx), Ga \eif \exists x Fx`

   :math:`\exists x(Fx \eif Ga), \forall x Fx \eif Ga`

Takið eftir að breytan :math:`x` kemur ekki fyrir í :math:`Ga`. Þegar
allir magnarar í setningu eru fremst er sagt að hún sé *á staðalformi*.
Við getum litið á þessi jafngildi sem reglur sem gera okkur kleift að
breyta hvaða setningu sem er í setningu á staðalformi.

Samsemdarreglur
---------------

Í §\ `[s:Interpretations] <#s:Interpretations>`__ minntumst við á hið
svokallaða *lögmál um samsemd óaðgreinanlegra hluta*. Það er sú
fullyrðing að hlutir sem ekki er hægt að greina í sundur, það er hafa
alla sömu eiginleika og hver annar, séu í raun sami hluturinn. Þetta
lögmál er heimspekilega mjög umdeilt og við tókum líka fram að við
myndum ekki aðhyllast þetta lögmál. Það leiðir af þessu, að það skiptir
ekki máli hversu mikið við vitum um tvo hluti, við getum ekki sannað að
þeir séu sami hluturinn, nema auðvitað að okkur sé sagt það
sérstaklega—en þá er sönnunin varla neitt sérstaklega upplýsandi.

Þetta þýðir auðvitað að *engar setningar* sem ekki innihalda
samsemdarmerkið þá þegar geta nokkru sinni leyft okkur að draga þá
ályktun að :math:`a = b`. Innleiðingarreglan fyrir samsemdarmerkið getur
því ekki kynnt til sögunnar *nýja* setningu sem inniheldur tvö *ólík*
nöfn.

Á hinn bóginn er sérhver hlutur sá sami og hann sjálfur. Við þurfum því
engar sérstakar forsendur til að geta dregið á ályktun að eitthvað sé
það sama og það sjálft. Þetta er grunnurinn að innleiðingarreglunni
fyrir samsemdarmerkið: Takið eftir því að þessi regla vísar ekki til
neinna lína sem koma á undan henni sjálfri. Fyrir hvaða nafn sem er, ,
við getum hvenær sem er skrifað niður :math:`\meta{c}=\meta{c}` bara með
því að vísa til reglunnar =I.

Eyðingarreglan er áhugaverðari. Ef við höfum sýnt að :math:`a = b`, þá
er allt sem er satt um hlutinn sem nafnið :math:`a` vísar til, líka satt
um hlutinn sem nafnið :math:`b` vísar til. Þeir eru jú sami hluturinn!
Við ættum því að geta tekið hvaða setningu sem er, þar sem nafnið
:math:`a` kemur fyrir, og skipt því út alls staðar fyrir nafnið
:math:`b`, og niðurstaðan hlýtur að vera rökfræðilega jafngild. Til
dæmis, ef við vitum að :math:`Raa` og :math:`a = b`, þá hljótum við að
geta dregið þá ályktun að :math:`Rab`, :math:`Rba` og :math:`Rbb`.

Eyðingarreglan byggir á þessari hugmynd. Almennt form hennar er því
svona: Rithátturinn hér er sá sami og fyrir :math:`\exists`\ I.
:math:`\meta{A}(\ldots \meta{a} \ldots \meta{a}\ldots)` er því formúla
sem inniheldur nafnið :math:`\meta{a}`, og
:math:`\meta{A}(\ldots \meta{b} \ldots \meta{a}\ldots)` er formúla sem
fæst með að skipta út nafninu :math:`\meta{a}` fyrir nafnið
:math:`\meta{b}` í einu eða fleiri tilvikum. Línurnar :math:`m` og
:math:`n` mega koma fyrir í hvaða röð sem er og þurfa ekki að vera hlið
við hlið. Við vitnum þó alltaf fyrst í setninguna sem tjáir samsemdina
fyrst. Við leyfum líka: Þessi regla er oft kölluð *lögmál Leibniz* í
höfuðið á þýska heimspekingnum Gottfried Leibniz.

Skoðum dæmi. Sönnum fyrst að samsemd sé *samhverf*:

.. container:: proof

   *Proof.* ◻

Við fáum línu 3 með því að skipta út einu tilviki af :math:`a` í línu 2
fyrir :math:`b`. Þetta er leyfilegt vegna þess að við höfum
:math:`a = b`.

Næst sýnum við að samsemd sé *gegnvirk*: [3]_

.. container:: proof

   *Proof.* æabc æabc ◻

Við fáum línu 4 með því að skipta út :math:`b` í línu 3 fyrir
:math:`a`—enda er :math:`a =b`.

Sannið eftirfarandi setningar.

.. container:: earg

   :math:`Pa \eor Qb, Qb \eif b=c, \enot Pa \proves Qc`

   :math:`m=n \eor n=o, An \proves Am \eor Ao`

   :math:`\forall x\ x=m, Rma\proves \exists x Rxx`

   :math:`\forall x\forall y(Rxy \eif x=y)\proves Rab \eif Rba`

   :math:`\enot \exists x\enot x = m \proves \forall x\forall y (Px \eif Py)`

   :math:`\exists x Jx, \exists x \enot Jx\proves \exists x \exists y\ \enot x = y`

   :math:`\forall x(x=n \eiff Mx), \forall x(Ox \eor \enot Mx)\proves On`

   :math:`\exists x Dx, \forall x(x=p \eiff Dx)\proves Dp`

   :math:`\exists x\bigl[(Kx \eand \forall y(Ky \eif x=y)) \eand Bx\bigr], Kd\proves Bd`

   :math:`\proves Pa \eif \forall x(Px \eor \enot x = a)`

Sýnið að eftirfarandi setningar séu sannanlega jafngildar.

.. container:: ebullet

   :math:`\exists x \bigl([Fx \eand \forall y (Fy \eif x = y)] \eand x = n\bigr)`

   :math:`Fn \eand \forall y (Fy \eif n= y)`

 

Í §\ `[sec.identity] <#sec.identity>`__ héldum við fram að eftirfarandi
setningar væru jafngóðar þýðingar á setningunni „Til er nákvæmlega eitt
:math:`F`\ “:

.. container:: ebullet

   :math:`\exists x Fx \eand \forall x \forall y \bigl[(Fx \eand Fy) \eif x = y\bigr]`

   :math:`\exists x \bigl[Fx \eand \forall y (Fy \eif x = y)\bigr]`

   :math:`\exists x \forall y (Fy \eiff x = y)`

Sýnið að þær séu allar sannanlega jafngildar. (Ráðlegging: Til að sýna
að þrjár setningar séu sannanlega jafngildar er nóg að sýna að önnur
leiði af þeirri fyrstu, sú þriðja af annarri og sú þriðja sanni þá
fyrstu. Í kaflanum hér að ofan var kynnt til sögunnar hugtak sem ætti að
útskýra af hverju.)

  Þýðið eftirfarandi rökfærslu yfir á táknmál umsagnarökfræði:

   Til er nákvæmlega eitt :math:`F`. Til er nákvæmlega eitt :math:`G`.
   Ekkert er bæði :math:`F` og :math:`G`. Þar af leiðandi eru nákvæmlega
   tveir hlutir sem eru annað hvort :math:`F` eða :math:`G`.

Sannið þessa rökfærslu.

.. _`s:DerivedFOL`:

Afleiddar reglur í umsagnarökfræði
----------------------------------

Í setningarökfræðinni kynntum við fyrst til sögunnar reglur sem við
kölluðum *grunnreglur*. Við bættum svo við fleiri reglum sem við gátum
leitt af þessum grunnreglum. Þessar afleiddu reglur voru bara notaðar
til hægðarauka, en í raun hefðum við getað sleppt þeim.

Það vill svo til að magnarareglurnar sem við kynntum til sögunnar hér að
ofan eru afleiddar reglur þar sem við getum leitt þær af grunnreglunum
sem við notuðumst við í §\ `1 <#s:BasicFOL>`__. Rétt eins og áður, þá
sýnum við að regla sé afleidd regla með því að gefa nokkur konar
uppskrift að því hvernig hægt væri að skipta reglunni út fyrir lengri
sönnun í hvert sinn sem hún er notuð.

Hér er slík uppskrift fyrir fyrstu umbreytingaregluna fyrir magnara:

.. container:: proof

   *Proof.* ◻

Og hér er svo samskonar uppskrift fyrir aðra umbreytingarregluna:

.. container:: proof

   *Proof.* ◻

Þetta útskýrir af hverju við getum litið á umbreytingarreglurnar fyrir
magnara sem afleiddar reglur. Athugið þó að þessar uppskriftir nota
tiltekna formúlu (nefnilega :math:`Ax`) og eru því ekki fullkomlega
almennar. Það væri þó lítið mál að breyta þeim þannig að þær verði það.
Hægt væri að gefa svipaðar uppskriftir fyrir umbreytingarreglur 3 og 4.

Það er vert að nefna hér að þetta sýnir enn betur af hverju við verðum
að samþykkja að :math:`\forall x Fx` sé sönn setning ef yfirgripið er
tómt. Af hverju? Jú, af því að við sýndum að ef :math:`\forall x Fx`
væri ósönn, þá væri :math:`\exists x \enot Fx` sönn—og hún segir að
yfirgripið sé ekki tómt. Það væri mótsögn. Ef þessar umbreytingarreglur
eru afleiddar reglur, en ekki grunnreglur, þá þýðir það að ef við sættum
okkur ekki við að :math:`\forall x Fx` sé sönn í tómu yfirgripi, þá
yrðum við að breyta einhverri af grunnreglunum okkar til að forðast
mótsögnina. Það hefur að sjálfsögðu verið reynt, en niðurstaðan er ekki
endilega betri eða einfaldari, svo það borgar sig frekar (að minnsta
kosti fyrir okkur) að fara bara þá leið að :math:`\forall x Fx` sé sönn,
ef yfirgripið er tómt. [4]_

Sýnið að þriðju og fjórðu umbreytingarreglurnar fyrir magnarana eru
afleiddar reglur.

Munurinn á sannanafræðilegum hugtökum og merkingarfræðilegum
------------------------------------------------------------

Fram að þessu höfum við notað tvö mismunandi tákn til að tákna sambandið
milli forsenda og niðurstöðu. Við höfum notað

.. math:: \meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n \proves \meta{B}

til að tákna að til sé sönnun á :math:`\meta{B}` sem hefur
:math:`\meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n` sem ólosaðar
forsendur. Þetta köllum við *sannanafræðilegt hugtak* af því að það
hefur að gera með sannanir.

Við höfum svo á hinn bóginn notað

.. math:: \meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n \entails \meta{B}

til að tákna að ekki sé til nein sanngildadreifing (eða túlkun) þar sem
:math:`\meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n` eru allar sannar, en
:math:`\meta{B}` ósönn. Þetta hefur að gera með sannleika setninga. Við
höfum kallað þetta *merkingarfræðilegt* hugtak—þó að sú nafngift sé að
mörgu leyti óheppileg. [5]_

Það er mjög mikilvægt að hafa í huga að þetta eru *ólík hugtök*. Annað
snýr að tilvist tiltekinna sannanna og hitt hefur að gera með hvort til
séu ákveðnar sanngildadreifingar. Þetta er greinilega ekki það sama.

En þrátt fyrir þennan mikilvæga greinarmun—sem við erum hér viljandi að
þrástagast á—eru djúp tengsl þarna á milli. Til að sjá það er gott að
skoða sambandið milli röksanninda og sannanlegra setninga.

Ef við viljum sýna að setning sé sannanleg setning, þá þurfum við bara
að finna sönnun. Það getur reyndar verið erfitt, sérstaklega ef sönnunin
sem þarf er löng, en það er hins vegar lítið mál að athuga hvort
tiltekin sönnun sé rétt: það er nóg að athuga hverja línu og athuga
hvort hún sé rétt, og ef allar línurnar eru réttar, þá er sönnunin í
heild rétt. En til að sýna að setning sé rökfræðileg sannindi þarf að
segja eitthvað um *allar mögulegar túlkanir*. Það getur verið mjög
erfitt, ef ekki ómögulegt. Það er því mun auðveldara að sýna að setning
sé sannanleg en að sýna að hún sé röksannindi.

Á hinn bóginn er mjög erfitt að sýna að setning sé *ekki* sannanleg. Til
þess þyrfti að segja eitthvað um *allar mögulegar sannanir*. Það er líka
mjög erfitt, ef ekki ómögulegt. En til að sýna að setning sé ekki
röksannindi er nóg að finna túlkun sem gerir setninguna ósanna. Það
getur verið erfitt að finna slíka túlkun, en það er auðvelt að ganga úr
skugga um hvort tiltekin túlkun sé geri setninguna í raun ósanna. Í
þetta skiptið er því auðveldara að sýna að setning sé *ekki* röksannindi
en að sýna að hún sé *ekki* sannanleg.

Það vill hins vegar svo heppilega til að *setning er sannanleg ef og
aðeins ef hún er röksannindi*. Það þýðir að ef við getum fundið sönnun á
:math:`\meta{A}` sem notar engar ólosaðar forsendur, það er er að segja,
sýnt að :math:`\proves \meta{A}`, þá getum við líka dregið þá ályktun að
:math:`\meta{A}` séu röksannindi, eða með öðrum orðum, að
:math:`\entails \meta{A}`. Þetta gengur í hina áttina líka. Ef við getum
fundið túlkun þar sem :math:`\meta{A}` er ósönn og þar með að
:math:`\meta{A}` séu ekki röksannindi, þá getum við dregið þá ályktun að
ekki sé til nein sönnun á :math:`\meta{A}` sem notar engar ólosaðar
forsendur. Það er að segja, ef við getum sýnt að
:math:`\nentails \meta{A}`, þá vitum við þar með að
:math:`\nproves \meta{A}`.

Almennt getum við því sagt að gildi:

.. math:: \meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n \proves\meta{B} \textbf{ ef og aðeins ef }\meta{A}_1, \meta{A}_2, \ldots, \meta{A}_n \entails\meta{B}

Þetta sýnir að þó að sannanleiki og rökfræðileg afleiðing séu mismunandi
hugtök, þá eiga þau við nákvæmlega sömu setningarnar. Þess vegna gildir:

.. container:: ebullet

   Rökfærsla er gild ef og aðeins ef *hægt er að sanna niðurstöðuna að
   forsendunum gefnum*.

   Setningar eru rökfræðilega jafngildar ef og aðeins ef þær eru
   sannanlega jafngildar.

   Setningar eru samrýmanlegar ef og aðeins ef þær eru ekki
   ósamrýmanlegar.

Við getum því alltaf valið þá aðferð sem okkur hentar best í það og það
skiptið, allt eftir því hvað við erum að reyna að gera. Taflan á næstu
síðu tekur saman hvað er (oftast) auðveldast.

Það ætti kannski ekki að koma á óvart að sannanleiki og rökfræðileg
afleiðing fari saman. En við megum þó ekki—og það er þess vert að taka
þetta fram enn og aftur—gleyma því að þetta eru ólík hugtök. Það tók
langan tíma fyrir rökfræðinga að sýna fram á jafngildi þessara tveggja
mikilvægu hugtaka og sönnunin á því er síður en svo augljós. [6]_

Raunar má segja að það að sýna fram á að sannanleiki og rökfræðileg
afleiðing eigi við um nákvæmlega sömu setningarnar séu skilin milli þess
sem kalla mætti inngang að rökfræði og rökfræði fyrir lengra komna. Í
tilfelli umsagnarökfræði er þessi niðurstaða ein af fyrstu stóru
niðurstöðum rökfræðinnar sem fræðigreinar.

.. container:: sidewaystable

   .. container:: center

      +----------------------+----------------------+----------------------+
      |                      | **Já**               | **Nei**              |
      +----------------------+----------------------+----------------------+
      |                      |                      |                      |
      +----------------------+----------------------+----------------------+
      | Er :math:`\meta{A}`  | finna sönnun sem     | finna túlkun þar sem |
      | **röksannindi**?     | sýnir að             | :math:`\meta{A}` er  |
      |                      | :ma                  | ósönn                |
      |                      | th:`\proves\meta{A}` |                      |
      +----------------------+----------------------+----------------------+
      |                      |                      |                      |
      +----------------------+----------------------+----------------------+
      | Er :math:`\meta{A}`  | finna sönnun sem     | finna túlkun þar sem |
      | **mótsögn**?         | sýnir að             | :math:`\meta{A}` er  |
      |                      | :math:`\             | sönn                 |
      |                      | proves\enot\meta{A}` |                      |
      +----------------------+----------------------+----------------------+
      |                      |                      |                      |
      +----------------------+----------------------+----------------------+
      | Eru :math:`\meta{A}` | finna tvær sannanir, | finna túlkun þar sem |
      | og :math:`\meta{B}`  | eina fyrir           | :math:`\meta{A}` og  |
      | **jafngildar**?      | :math:`\met          | :math:`\meta{B}`     |
      |                      | a{A}\proves\meta{B}` | hafa ólík sanngildi  |
      |                      | og eina fyrir        |                      |
      |                      | :math:`\met          |                      |
      |                      | a{B}\proves\meta{A}` |                      |
      +----------------------+----------------------+----------------------+
      |                      |                      |                      |
      +----------------------+----------------------+----------------------+
      | Eru                  | finna túlkun þar sem | sanna að             |
      | :math:`\me           | :math:`\me           | forsendurnar         |
      | ta{A}_1, \meta{A}_2, | ta{A}_1, \meta{A}_2, | :math:`\me           |
      |  \ldots, \meta{A}_n` |  \ldots, \meta{A}_n` | ta{A}_1, \meta{A}_2, |
      | **samrýmanlegar**?   | eru allar sannar     |  \ldots, \meta{A}_n` |
      |                      |                      | leiði til mótsagnar  |
      +----------------------+----------------------+----------------------+
      |                      |                      |                      |
      +----------------------+----------------------+----------------------+
      | Er                   | finna sönnun með     | finna túlkun þar sem |
      | :math:`\me           | :math:`\me           | :math:`\me           |
      | ta{A}_1, \meta{A}_2, | ta{A}_1, \meta{A}_2, | ta{A}_1, \meta{A}_2, |
      |  \ldots, \meta{A}_n  |  \ldots, \meta{A}_n` |  \ldots, \meta{A}_n` |
      | \therefore \meta{B}` | sem forsendum og     | eru allar sannar og  |
      | **gild**?            | :math:`\meta{B}` sem | :math:`\meta{B}` er  |
      |                      | niðurstöðu           | ósönn                |
      +----------------------+----------------------+----------------------+

.. [1]
   Ludwig Wittgenstein er dæmi um heimspeking sem neitaði þessu.

.. [2]
   Munið að í §\ \ `[s:BasicTFL] <#s:BasicTFL>`__ sögðum við að
   ‘:math:`\ered`’ stæði fyrir einhverja tiltekna mótsögn. Í
   umsagnarökfræði má þessi mótsögn ekki innihalda nein nöfn, því annars
   gæti það brotið í bága við þessa reglu.

.. [3]
   En það merkir einfaldlega vensl sem eru þannig að ef
   :math:`\meta{R}ab` og :math:`\meta{R}bc`, þá :math:`\meta{R}ac`. Dæmi
   um slík vensl er til dæmis að vera „stærri en“: Ef Anna er stærri en
   Felix og Jón er stærri en Anna, þá er Jón stærri en Felix.

.. [4]
   Þetta er svokölluð frjáls rökfræði (e. *free logic*). Sjá til dæmis
   John Nolt, „Free Logic“, 2021, í *Stanford Encyclopedia of
   Philosophy*
   (https://plato.stanford.edu/archives/fall2021/entries/logic-free/).

.. [5]
   Fyrir þá lesendur sem ekki hafa lesið kafla §\ \ `[s] <#s>`__, þá
   samsvara *túlkanir* í umsagnarökfræði sanngildadreifingunum úr
   setningarökfræði. Við köllum setningar sem eru sannar fyrir hvaða
   túlkun sem er *röksannindi*. Þau samsvara klifunum úr
   setningarökfræði.

.. [6]
   Ágætlega aðgengilega sönnun má finna í Sider, T. *Logic for
   Philosophy*. Oxford: Oxford University Press.
