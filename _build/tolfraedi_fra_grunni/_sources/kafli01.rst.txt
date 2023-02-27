.. _c.inngangur:

Inngangur
=========

Nú á dögum er hægt að fá tölulegar upplýsingar um nánast allt milli
himins og jarðar og mikilvægi góðrar tölfræðikunnáttu fer vaxandi hjá
sífellt fleiri fræðasviðum. Hvort sem um er að ræða lyfjafræðing sem
vill kanna hvort nýtt lyf hafi sambærilega virkni og önnur lyf á
markaðnum eða ferðamálafræðing sem skoðar vinsælustu áfangastaði
hérlendis, styðjast báðir aðilar við tölfræði til að draga ályktanir
sínar.

Í stuttu máli má segja að verkefni okkar í tölfræði snúist um að nýta
sem best þær upplýsingar sem við fáum með tölulegum gögnum. Til að svo
megi verða þarf að huga að mörgu: Högun tilraunarinnar þaðan sem
gögnunum er aflað, skráningu og úrvinnslu gagnanna og að lokum túlkun á
niðurstöðunum. Í þessari bók verður veigamestu atriðum þessara fjögurra
þátta gerð skil og auk þess fjallað um hinar ýmsu tölfræðiaðferðir sem
nota má á breiðan flokk gagna.

Framsetning
-----------

Framsetning
~~~~~~~~~~~

Lestur þessarar bókar gerir ekki forkröfu um stærðfræðikunnáttu utan
almenns stúdentsprófs og ætti hún því að vera aðgengileg flestum þeim
sem feta sín fyrstu spor í tölfræðinámi. Skerpt er á áhersluatriðum með
því að rita þau í áherslukassa eins og sjá má á næstu síðu. Sérhver
kassi ber titil og enska þýðingu á titlinum þegar við á. Þeir hafa
einnig hver sitt númer sem vísar til kaflans þar sem þeir standa. Því
ætti að vera fljótlegt að fletta upp kössum sem vísað er til í öðrum
köflum.

Þegar kassarnir innihalda áhersluatriði sem eru stærðfræðilega krefjandi
fylgir nánari skýring á umfjöllunarefni kassans beint að honum loknum í
skýringarkassa. Hann má sjá á næstu síðu. Lesendur með góða
stærðfræðikunnáttu geta því litið framhjá efni skýringarkassanna en þeir
koma lesendum með minni færni í stærðfræði vonandi að góðum notum.

Áhersluatriði (Ensk þýðing ef við á)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Lýsing á áhersluatriðinu.


--------------

.. note::

    Nánari skýring á áhersluatriðinu að ofan ef þurfa þykir.


--------------

Tugabrotum er skipt upp í heiltöluhluta og aukastafi. Á Íslandi er hefð
fyrir því að nota kommu til að skilja á milli heiltöluhluta og aukastafa
tugabrota. Heiltöluhlutinn stendur vinstra megin við kommuna en
aukastafirnir hægra megin við hana. Sá ritháttur er þó sjaldgæfur í
öðrum löndum, algengast er að punktur sé notaður til að greina á milli
heiltöluhluta og aukastafa. Það veldur því að mörg tölfræðiforrit gera
ráð fyrir því að aukastafir tugabrota séu aðgreindir með punkti og
stundum getur verið illfært að lesa inn gögn þar sem komma er notuð til
aðgreiningar. Þá sögu er til að mynda að segja um tölfræðiforritið R sem
er geysiöflugt og mikið notað bæði hér á landi sem erlendis. Því munum
við ætíð nota **punkt** til aðgreiningar aukastafa. Þannig er stærðin
,,þrír komma fjórir“ rituð 3.4 en ekki 3,4 eins og margir eiga að
venjast.

.. _s.alyktunartolfaedioglysanditolfraedi:

Yfirlit yfir efni bókarinnar
----------------------------

Tölfræði getur verið margslungin og til að beita henni af öryggi er viss
kunnátta í stærðfræði, sérstaklega líkindafræði, nauðsynleg. Því leggjum
við nokkrar lykkjur á leið okkar í umfjöllun um tölfræði; til að leggja
grunn að þeim líkindafræðihugtökum sem á þarf að halda. Þessar lykkjur
mega þó ekki verða til þess að við missum stefnuna og því ætlum við í
upphafi lesturs að gefa stutt yfirlit yfir það hvað tölfræði er og hvert
markmið okkar er með þeim tölfræðiaðferðum sem við beitum.

Margar kennslubækur skipta tölfræði upp í *lýsandi tölfræði* og
*ályktunartölfræði*. Þó að þessir tveir flokkar dugi ekki til að lýsa
öllu því sem við köllum tölfræði, eins og til dæmis úrtakshögun, þá eru
þeir afar mikilvægir og spanna ógrynni gagnlegra aðferða.

*Lýsandi tölfræði* (e. descriptive statistics) snýst um að lýsa sem best
því úrtaki sem við höfum í höndunum. Það gerum við bæði með því að
reikna útkomur ákveðinna lýsistærða sem lýsa gögnunum en einnig með því
að setja gögnin skýrt fram á myndrænan hátt. Þið hafið eflaust heyrt um
algengustu lýsistærðirnar eins og meðaltal og staðalfrávik og það er
sjaldgæft að fletta dagblaði án þess að rekast á nokkur gröf. Lýsandi
tölfræði verður tekin fyrir í köflum :numref:`%s <c.myndraenframsetning>` og
:numref:`%s <c.lysanditolfraedi>`.

*Ályktunartölfræði* (e. inferential statistics) beinir kastljósinu frá
úrtakinu sjálfu og að öllu þýðinu. Markmið ályktunartölfræði er að
staðhæfa um allt þýðið út frá úrtaki sem við höfum mælingar á. Þar koma
fyrir hugtök eins og *öryggisbil* og *villulíkur* sem oft eru notuð í
daglegu tali. Ályktunartölfræði er eingöngu hægt að framkvæma á
*slembiúrtökum* sem kynnt eru í kafla :numref:`%s <c.fratilrauntilgagna>`. Því
leyfum við okkur, þegar við fjöllum um ályktunartölfræði, að tala um
úrtök þegar við eigum strangt til tekið við slembiúrtök.

Líkt og í lýsandi tölfræði reiðum við okkur á lýsistærðir í
ályktunartölfræði. Hins vegar skoðum við ekki einvörðungu útkomuna
sjálfa heldur segjum einnig til um hvaða önnur gildi er líklegt að fá ef
nýtt slembiúrtak væri valið. Slíkt krefst þekkingar á líkindafræði,
slembistærðum, helstu líkindadreifingum og nánari kynnum af
líkindafræðilegum eiginleikum lýsistærða. Þessi atriði verða tekin fyrir
í kafla :numref:`%s <c.likindafraedi>`. Að því loknu fjöllum við um þá
hugmyndafræði sem ályktunartölfræði byggir á (í kafla
:numref:`%s <c.alyktunartolfraedi>` ) en ályktunartölfræði mun ráða ríkjum í
öllum köflum þaðan í frá.

Sú ályktunartölfræði sem kynnt er í þessari bók er fyrst og fremst af
tvennum toga. Annars vegar reiknum við öryggisbil og hins vegar
framkvæmum við tilgátupróf. Við byrjum á kafla
:numref:`%s <c.alyktanirumflokkabreytur>` þar sem við fjöllum um
ályktunartölfræði sem við framkvæmum á flokkabreytum. Að því loknu eru
ályktanir um talnabreytur teknar fyrir í kafla
:numref:`%s <c.alyktanirumtalnabreytur>`. Fervikagreining er umfjöllunarefni
:numref:`%s <c.fervikagreining>`. kafla en hana má einnig nota til að draga
ályktanir um talnabreytur. Í :numref:`%s <c.adhvarfsgreining>`. kafla kveður við
nýjan tón þegar við skoðum línulega aðhvarfsgreiningu en markmið hennar
er að kanna línulegt samband tveggja breyta. Að lokum kynnumst við
tvíkosta aðhvarfsgreiningu í kafla :numref:`%s <c.tvikostaadhvarfsgreining>`.
