.. container::

   Háskóli Íslands – Umhverfis og byggingarverkfræðideild Húsagerð

   Björn Marteinsson

Raki, rakaflutningur og rakaþétting
======================================

Almennt
-----------


Raki í byggingum og byggingarhlutum orsakast af fjórum megin ástæðum;

-  Byggingarraki

-  Loftraki

-  Úrkoma (snjór og slagregn)

-  Jarðvegsraki (grunnvatn)

Raki í byggingarefnum og byggingum getur haft óheppilegar aukaverkanir
s.s. stuðlað að hraðara efnaniðurbroti heldur en væri í þurrum efnum og
einnig valdið óhollustu, t.d. vegna rakaþéttingar. Það er því mikilvægt
að hafa þekkingu til að geta metið rakaálag á byggingarhluta og
byggingar, og geta kannað hvort rakaástand verði efnum og mannvirki
óhagstætt.

**Almennar líkingar og gildi;**

Almenni gasfastinn;        R=8314,3 J/(kmol∙K)

Yfirborðsspenna vatns;     :math:`\sigma \cong 78 \cdot (1-0,0032\cdot\theta) \cdot 10^{-3}  N/m`

Gufuhleypni í lofti (DIN 52615); :math:`\delta_0(T)=2.0 \cdot 10^{-7} \frac{T^{0.81}}{P_a} kg/(m \cdot Pa \cdot s)`

Raki í byggingarefnum og byggingum
--------------------------------------

Byggingarraki
?????????????

Af náttúrulegum ástæðum, eða tengt framleiðsluferli sumra efna, þá
innihalda efnin rakamagn sem getur verið hærra heldur en sem nemur
jafnvægisraka (fjallað er um hugtakið jafnvægisraki í námsefni um
efnisfræði) á notkunartíma. Þessi raki er nefndur byggingarraki
(skilgreiningin ræðst af umhverfi, og er því háð aðstæðum hverju sinni).
Dæmi um þetta er t.d. timbur sem iðulega er þurrkað niður í 18-20 %
efnisraka (af þurri þyngd) áður en það er selt til notanda, en
jafnvægisraki í notkun liggur á bilinu 6 – 18 %, háð notkunarsviði.
Hliðstætt þá nemur umframraki í steypu á byggingartímanum iðulega
nokkrum tugum lítra á hvern rúmmetra steypu.

Almennt er miðað við að halda byggingarefnum eins þurrum og kostur er á
byggingartíma, og síðan gert ráð fyrir að byggingarefnin nái að losi sig
við byggingarraka á notkunartíma þar til einhverju jafnvægi er náð, sem
stjórnast af umhverfisáraun hverju sinni.

Loftraki
????????

Mettunarraki lofts er ýmist gefinn upp sem gufuinnihald, kg/kg (eða
kg/m\ :sup:`3`\ ), eða rakaþrýstingur, Pa. Upplýsingar um mettunarraka
má finna t.d. í Mollier-línuriti eða í töflum (sjá aftast í kaflanum).
Mettunarrakaþrýsting lofts má einnig nálga samkvæmt jöfnu 3.1 sem er
gefin upp í DIN 4108 TEIL 5 og sögð gilda á hitasviðinu –20 til 30 °C.

.. admonition:: Jafna 3.1
   :class: jafna

   .. math::
      p_{v,sat}(\theta) = a \cdot (b+ \frac{\theta}{100})^n , (Pa)    

þar sem 

.. list-table:: 
  :widths: 5 5 5 5
  :header-rows: 0 

  * - :math:`\theta`
    - a 
    - b 
    - n 
  * - :math:`0 \leq \theta \leq 30`
    - 288,68
    - 1,098
    - 8,02
  * - :math:`-20 \leq \theta \leq 0`
    - 4,689
    - 1,486
    - 12,3

Hlutfallsraki innilofts (% HR) er háður rakamagni lofts (t.d. :math:`g/m^3` ), eða hlutfallsþrýstingi vatnsgufu, og lofthita.
Loftrakinn reiknast ætíð sem hlutfallstala af mettunarraka loftsins (sem
er háður lofthita). Milli mettunarþrýstings (Pa) og mettunarraka
(:math:`kg/m^3` ) er beint samband eins og augljóst er af almenna
gaslögmálinu, jafna 3.2

.. admonition:: Jafna 3.2
 :class: jafna

   .. math::
      w_{sat} = p_{sat} \cdot \frac{M_{H_{2}O}}{R \cdot T} 

þar sem 

.. list-table::
   :widths: 5 5 5
   :header-rows: 0

   * - :math:`w_{sat}`
     - Mettunarraki
     - :math:`{kg/m^3}`
   * - :math:`p_{sat}`
     - Mettunarþrýstingur
     - Pa
   * - :math:`M_{H_{2}O}`
     - mólmassi vatns
     - :math:`\frac{kg}{kmol}`
   * - :math:`R`
     - almenni gasfastinn
     - :math:`\frac{J}{kmol \cdot K}`
   * - :math:`T`
     - hitastig
     - K

Hlutfallsraki lofts er skilgreindur eins og sýnt er í jöfnu 3.3 (nákvæm
hliðstæða gildir ef í stað rakaþrýstings er notað samsvarandi rakamagn).

 .. admonition:: Jafna 3.3
   :class: jafna
   
      .. math::
         \phi = \frac{p_v}{p_{v,sat}(T)} 

þar sem 

.. list-table::
   :widths: 5 5 5
   :header-rows: 0

   * - :math:`\phi`
     - Hlutfallsraki 
     - Hlutfallstala eða %
   * - :math:`p_v`
     - Rakaþrýstingur lofts
     - Pa
   * - :math:`P_{w,sat}`
     - Mettunarþrýstingur vatnsgufu í lofti
     - Pa
   * - T 
     - Aflfræðilegt hitastig
     - K

.. list-table:: *Tafla 3.1 Rakaframleiðsla í íbúðarhúsnæði*
   :header-rows: 1
   :widths: 40 15 15

   * - **Lýsing**
     - **Rakamagn**  
     - **Heimild**
   * - 
     - *kg / sólarhr.*
     - 
   * - **Íbúð (danskar tölur):**
     - 
     - /1/
   * - Matargerð, þvottar og frá íbúum
     - 15
     - 
   * - **Fjögurra manna fjölskylda (amerískar tölur):**
     - 
     - /2/
   * - Eldun (3 máltíðir á dag)
     - 0,9
     - 
   * - Uppþvottur (3 x dag ??)
     - 0,45
     - 
   * - Sturta
     - 0,2
     - 
   * - Bað
     - 0,05
     - 
   * - Þvottur (1 x viku)
     - 1,8
     - 
   * - Þurrka þvott inni eða barkalaus þurrkari
     - 11,7
     - 
   * - Þvo gólf (pr. 10 m²)
     - 1,3
     - 
   * - Íbúar
     - 5,4
     - 

/1/ SBI Anvisning 76

/2/ Laaly, H.O. (1992) The Science and Technology of Traditional and Modern Roofing Systems,
Laaly Scientific Publishing, Los Angeles, CA

Raki í innilofti er alltaf háður útiloftraka og rakagjöf til innilofts,
en getur einnig tímabundið verið háður öðrum orsökum s.s. byggingarraka,
leka vegna úrkomu eða frá lögnum og loks vegna jarðvegsraka. Útfrá
upplýsingum um mettunarraka, háð lofthita, má auðveldlega sjá að fyrir
sama rakamagn lofts lækkar loftraki með hækkandi hitastigi. Inniloft
inniheldur það rakamagn sem loftið hafði sem útiloft, auk þess raka sem
loftið tekur í sig þann tíma sem það er inni. Rakaviðbótin (fyrir hvern
m\ :sup:`3`\  innilofts) er því háð tveim atriðum þ.e. loftskiptum í
húsinu (loftræsingu) og rakagjöf innanhúss, sjá töflu 3.1.
 
Rakamagn í innilofti má almennt reikna eins og jafna 3.4 sýnir, þar sem
miðað er við að rakagjöf hefjist á tíma t=0;

.. admonition:: Jafna 3.4
   :class: jafna

   .. math::
      w_{i} = w_e + \frac{G}{n \cdot V} \cdot (1 - e^{-nt}) 

þar sem 

.. list-table::
   :width: 5 5 5 
   :header-rows: 0
   
   * - :math:`w_i`
     - Rakamagn í innilofti
     - :math:`kg/m^3`
   * - :math:`w_e`  
     - Rakamagn í útilofti 
     - :math:`kg/m^3`
   * - G 
     - Rakabæting
     - kg/klst
   * - n 
     - Fjöldi loftskipta
     - 1/klst
   * - V
     - Loftræst rými
     - m\ :sup:`3`
   * - t
     - tími
     - h
 
Af jöfnu 3.4 má sjá að með vaxandi tíma þá nálgast lausnin að verða
stöðug; Jafna 3.5

.. admonition:: Jafna 3.5
   :class: jafna

   .. math::
      w_i = w_e + \frac{G}{n \cdot V}

Til þess að taka samtímis tillit til áhrifa rakagjafar og loftskipta á
inniloftraka þá er rakagjöfin iðulega gefin upp sem rakamagn á hvern
rúmmetra í loftskiptum á tímaeiningu, g/(m\ :sup:`3`\ ·klst). Rakamagn
innilofts fæst þá sem loftraki útilofts að viðbættri rakagjöfinni. Í
Svíþjóð er t.d. iðulega miðað við að slík rakagjöf í íbúðarhúsi sé
2-4g/m\ :sup:`3`\ , tölur frá Bandaríkjunum gefa svipaða niðurstöðu ef
miðað er við ein loftskipti á klukkustund en tölur frá Danmörku gefa
fyrir 1 loftskipti á klukkustund um 2 g/m\ :sup:`3`\  fyrir
300m\ :sup:`3`\  íbúð. Rakagjöf til innilofts, reiknað á loftskiptamagn,
er hugsanlega minni hér á Reykjavíkur-svæðinu vegna ódýrrar hitunarorku
og því hugsanlega mikillar loftræstingar.

Í staðlinum ÍST EN ISO 13788:2012 er sett fram tillaga að reiknislegri
rakabætingu í húsum, reiknað á hvern rúmmetra í loftskiptum og háð
útihita, sjá línurit 3.1.

Útfrá upplýsingum um lofthita og raka í útilofti, gefinn innihita og
rakagjöf þá má reikna hvernig loftraki innilofts breytist eftir
árstíðum, línurit 3.2. Í íbúðarhúsnæði er rakagjöf mismunandi eftir
herbergjum og loftræsting getur einnig verið mismunandi. Þannig má t.d.
búast við að tímabundið geti loftraki orðið mjög hár í baðherbergjum og
loftraki í svefnherbergjum getur einnig orðið allhár að næturlagi ef
lítið er loftræst.

.. image:: myndir/kafli03/linurit1.png
   :name: Picture 8
   :width: 362px
   :height: 226px

*Línurit 3.1: Reiknisleg rakabæting í inniloft*; (:math:`0-8 g/m^3` *á
rúmmetra í loftskiptum)* 
*(Heimild: ÍST EN ISO 13788:2012)*

.. image:: myndir/kafli03/linurit2.png
   :name: Picture 9
   :width: 363px
   :height: 260px

*Línurit 3.2: Hlutfallsraki lofts innanhúss í Reykjavík fyrir mismunandi
rakabætingu (0-8 g/m\ :sup:`3`\ ) og innihita 20°C. Útiaðstæður meðaltal
áranna 1996-2004.*

Almennt má þó miða við (og stutt af mælingum í húsum) að algengur
loftraki í íbúðarhúsum hérlendis sé á bilinu 25-40 %HR að vetrarlagi,
eða rakagjöf 2-4 g/loftræstan m\ :sup:`3`\ . Til viðmiðunar má nefna að
ef rakinn fer yfir 40-45 % þegar kalt er úti þá verður rakaþétting innan
á tvöföldu einangrunargleri. Að sumarlagi fer loftrakinn talsvert hærra
að skaðlausu, eða upp í 50-60 %HR; þ.e. samsvarar rakabætingu í inniloft
svo nemur allt að tæpum 4 g/m\ :sup:`3`\ .

Úrkoma og slagregn
??????????????????

Úrkoma og slagregn eru oft beinn áhrifavaldur á efnisraka, jafnvel í
veggjum, þar sem vatnsfilma á vatnsdrægu yfirborði mun ætið hafa áhrif á
rakaástand efnisins.

Ótruflað slagregn á vegg er reiknað samkvæmt jöfnu 3.6.

.. admonition:: Jafna 3.6
   :class: jafna

   .. math::
      S = N \cdot u_v / u_r

.. figure:: ./myndir/kafli03/Slagregn.png
  :align: center
  :width: 50%

.. centered:: Mynd 3.1 Slagregn

þar sem 

.. list-table::
   :width: 5 5 5
   :header-rows: 0

   * - S 
     - Slagregnsmagn á lóðréttan flöt
     - :math:`kg/m^2`
   * - N 
     - Mæld úrkoma á láréttan flöt 
     - :math:`kg/m^2`
   * - :math:`u_v` 
     - Vindhraði
     - m/s
   * - :math:`u_r`  
     - Fallhraði regndropa
     - m/s

Vitaskuld þarf að taka tillit til stefnu normals á veggyfirborð og
vindáttar við ákvörðun slagregnmagns, þó svo þessi atriði komi ekki fram
í jöfnu 3.6.

Fallhraði regndropa er háður stærð þeirra og er fyrir stærstu dropana
gjarnan á bilinu 7-10 m/s. Í útreikningi á slagregnsmagni er oft miðað
við :math:`u_r = 7 m/s`.
 
Þegar vindur nálgast byggingu þá sveigir hann framhjá fyrirstöðunni (sjá
umfjöllun um lofhreyfingar við byggingar) og regndroparnir fylgja
loftinu í þessari hreyfingu að einhverju leyti, en hluti þeirra
slöngvast áfram vegna hreyfitregðu. Það er því ósennilegt að regn sem
lendir á fyrirstöðunni sé jafnmikið og útreiknað slagregnsmagn í
ótrufluðu slagregni. Erlendis hafa verið gerðar mælingar á slagregni
(m.a. Noregur, Svíþjóð, England) og í staðaluppkastinu prEN 13013-3:1997
er gerð tillaga varðandi reiknislega dreifingu slagregns á veggi, mynd
3.2, þar sem stuðullinn W er formstuðull slagregnsdreifingar á veggi
(hliðstæða við formstuðul vindálags). Í staðaluppkastinu er grunngildi
slagregns reiknað talsvert frábrugðið því sem sýnt er í jöfnu 3.6 (í
staðaluppkastinu er tekið tillit til stefnuhorns, umhverfis o.f.l.).
Þegar mynd 3.2 er skoðuð þá er áberandi að slagregn er iðulega meira
efst á veggjum og síðan niður með úthornum, þessa mun gæta í
rakainnihaldi veggjarins og viðhaldsþörf.

.. figure:: ./myndir/kafli03/Slagregn_dreifing.png
  :align: center
  :width: 90%

.. centered:: Mynd 3.2 Slagregnsdreifing á veggi (heimild: prEN 13013-3:1997)

Jarðraki
????????

Raki frá jarðvegi getur verið tilkominn vegna yfirborðsvatns (úrkomu)
sem leitar að byggingu og hinsvegar raka frá grunnvatni. Háð tegund
jarðvegs og frágangi byggingarhluta neðan jarðvegsyfirborðs getur rakinn
verið í formi vatns sem; (i) liggur að yfirborði og veldur þá
vatnsþrýstingi á yfirborði, (ii) rennur niður yfirborð, eða í formi raks
jarðvegs sem liggur að yfirborði. Byggingarhlutar sem standa dýpra
heldur en grunnvatnsyfirborð munu ávallt verða fyrir vatnsþrýstingi.

Jarðraki gerir að verkum að hlutfallsraki lofts í jarðvegi getur
auðveldlega verið 100 %.

Til að draga úr jarðraka þarf að leiða frárennsli frá þaki, og almennt
vatnsfráhrindandi yfirborðum, í fráveitu, halla jarðvegsyfirborði frá
húsi og loks draga eftir mætti úr vatnsdrægni yfirborða í jörðu og ásamt
því að tryggja dren frá byggingarhlutum í jörðu.

Rakaflutningur
------------------

Drifkraftur sem knýr rakaflutning getur verið margskonar s.s.
rakainnihald, rakaþrýstingur, hiti, póruþrýstingur, vindþrýstingur,
þyngdarkraftur ofl.

Meginleiðir rakaflutningur eru eftirfarandi;

-  Rakaflæði

-  Rakastreymi

-  Hárpípuflutningur

-  Útsveim og varmasveim

og verður hér fjallað lauslega um hverja þessara leiða.

Rakaflæði
?????????

Rakaflæði á sér stað ef stigull í rakaþrýstingi eða rakainnihaldi er til
staðar, jafna 3.7.

.. admonition:: Jafna 3.7
   :class: jafna

   .. math::
      g = - D \cdot \nabla \Psi

Þar sem

.. list-table::
   :widths: 5 20 10
   :header-rows: 0

   * - g
     - Þéttleiki rakaflutnings
     - :math:`kg / (m^2 \cdot s)`
   * - D
     - Rakaflutningsstuðull 
     - 
   * - :math:`\nabla \Psi`
     - Stigull drifkrafts rakaflutnings
     -

Rakaflutningur í einni vídd er þá;

.. admonition:: Jafna 3.8
   :class: jafna

   .. math::
      g = - D \frac{\partial \Psi}{\partial x}

Augljós líkindi eru með jöfnu 3.7 og jöfnu Fourier’s fyrir varmaflutning
(jafna 2. 1), rakaflutningur vegna flæðis er enda reiknaður á hliðstæðan
máta og varmaflæði.

Jafna 3.7 gildir sérstaklega um rakaflutning í lofti, en getur einnig
gilt fyrir rakaflutning í lofthluta efnis-loftblöndu (pórótt efni) en þá
þarf að leiðrétta fyrir breyttu flutningsþversniði (og breyttri lengd
flutningsleiðar). Slík leiðrétting er gerð með því að innfæra sérstakan
efnisstuðul, :math:`\mu`, sjá síðar (jafna 3.16).

Drifkraftur fyrir rakaflæði er í eldri bókum gjarnan rakainnihald en í
nýrri ritum, og uppkasti að staðli, er notaður rakaþrýstingur.

Rakastreymi í lofti
???????????????????

Þegar þrýstimunar gætir í lofti þá á sér stað lofstreymi, streymið getur
átt upptök sín í þvinguðu streymi eða óþvinguðu sbr. umfjöllun um
varmaflutning. Loftstreymi mun ávallt flytja með sér vatnsgufu ef hún er
til staðar í loftinu. Þrýstimunur yfir byggingarhluta getur þannig þrýst
(röku) lofti í gegnum leka byggingarhluta, og háð því hvort loftið
hitnar upp eða kólnar á leið sinni í gegn þá geta áhrifin verið til
útþornunar byggingarhlutans eða rakasöfnunar í byggingarhluta vegna
rakaþéttingar. Nánar verður fjallað um þennan lið í kafla 4.

Hárpípuflutningur
?????????????????

Kraftajafnvægi fyrir hárpípu (mynd 3.3), sem er í snertingu við
vatnsyfirborð, gefur jöfnu 3.9;

.. math::
   \pi \cdot r^2 \cdot \rho \cdot H = 2 \cdot \pi \cdot r \cdot \sigma \cdot cos(\phi)

.. admonition:: Jafna 3.9
   :class: jafna

   .. math::
      H = \frac{2 \cdot \sigma}{r \cdot \rho \cdot g} cos(\phi)


.. image:: myndir/kafli03/Hárpípa.png
   :name: Picture 13
   :width: 237px
   :height: 189px
   :align: center

.. centered:: Mynd 3.3 Hárpípa
 
þar sem

.. list-table::
   :widths: 5 20 10
   :header-rows: 0

   * - r
     - Radíus hárpípu
     - m
   * - :math:`\rho`
     - Eðlisþéttleiki vökvans
     - :math:`kg/m^3`
   * - H 
     - Vökvahæð í pípunni
     - m 
   * - :math:`\sigma`
     - Yfirborðsspenna vökva
     - N/m
   * - :math:`\phi`
     - Snertihorn vökva við pípu
     -  
   
Fyrir vatn og venjuleg byggingarefni er snertihornið almennt sett jafnt
0, en með vatnsverjandi efnum má auka snertihornið verulega og þannig
lágmarka hárpípukrafta.

Í reynd eru hárpípur í efni af mismunandi vídd en ekki með eitt ákveðið
þversnið hver um sig, því er einungis í undantekningartilvikum hægt að
nota jöfnu 3.9 til að ákvarða ísogshæð vökva. Jafnframt er áhugvert að
geta lagt mat á hraða ísogsins og magn vökva sem efnið tekur upp. Það er
því almennt nauðsynlegt að mæla efniseiginleikana og notaðar eru jöfnur
sem skilgreina má fyrir slík tilvik. Jafna 3.10 gefur vatnsísog frá fríu
vatnsyfirborði;

.. admonition:: Jafna 3.10
   :class: jafna

   .. math::
      G = A \cdot \sqrt{t}
 

þar sem 

.. list-table::
   :widths: 5 20 10
   :header-rows: 0

   * - G
     - Vatnsmagn 
     - :math:`kg/m^2`
   * - A 
     - Ísogsstuðull
     - :math:`kg/(m^2 \cdot \sqrt{t})`
   * - t 
     - Tími 
     - s

Jafna 3.11 gefur vatnsdýpi í efninu;

.. admonition:: Jafna 3.11
   :class: jafna

   .. math::
      x = B \cdot \sqrt{t}

þar sem 

.. list-table::
   :widths: 5 20 10
   :header-rows: 0

   * - x
     - Vatnshæð (eða dýpi) 
     - m
   * - B 
     - Ísogsstuðull vatnsdýpis
     - :math:`m/\sqrt{s}`
   * - t 
     - Tími 
     - s

Vatnsdýpi vex stöðugt með tíma fyrir láréttar pórur, en í lóðréttum
pórum gildir að vatnshæðin verður mest eins og jafna 3.9 sýnir.

Dæmi um gildi á stuðlunum A og B eru sýnd í töflu 3.2 fyrir nokkur efni.

.. list-table:: *Tafla 3.2 Ísogsstuðlar efna* (heimild: Newander og Elmarsson, 1994)
   :header-rows: 2
   :widths: 30 10 20 20

   * - **Efni**
     - **Þéttleiki**
     - **Stuðull fyrir ísogsmagn, A**
     - **Stuðull fyrir ísogsdýpi, B**
   * -
     - :math:`kg/m^3`
     - :math:`kg/(m^2·\sqrt{s})`
     - :math:`×10^{-3} m/\sqrt{s}`
   * - Tígulsteinn
     - 1700
     - 0,37
     - 1,4
   * - Léttsteypa (sænsk)
     - 1900
     - 0,08
     - 0,4
   * - Sementsmúr (sænskur)
     - 1900
     - 0,03
     - 0,5
   * - Steypa v/s 0,3 (sænsk)
     - 
     - 0,010
     - 0,14
   * - Steypa v/s 0,5 (sænsk)
     - 
     - 0,020
     - 0,17
   * - Steypa v/s 0,7 (sænsk)
     - 
     - 0,028
     - 0,25
   * - Timbur ∥ trefjum
     - 450
     - 0,016
     - -
   * - Timbur ⊥ trefjar
     - 450
     - 0,004
     - -

Rakþrýstingur verður lægri yfir sveigðu vatnsyfirborði heldur en flötu,
þar sem yfirborðskraftar sem verka á vatnssameindirnar eru hærri í
fyrrnefnda tilvikinu. Jafna Kelvins segir til um samband pórustærðar og hlutfallsraka lofts
yfir vatnsborði í slíkri póru (sem hlutfall af mettunarraka yfir sléttu
yfirborði) , jafna 3.12;

.. admonition:: Jafna 3.12
   :class: jafna

   .. math::
      \varphi = e^{\frac{2 \cdot \sigma \cdot M_w}{r \cdot \rho_w \cdot R \cdot T}}
 
Thompson jafnan er:

.. math::
   p=p_s \cdot e^{\frac{2 \cdot \sigma \cdot M_w}{r \cdot \rho_w \cdot R \cdot T}}

þar sem

.. list-table:: 
   :widths: 5 5 5 
   :header-rows: 0

   * - :math:`\phi`
     - hlutfallsraki lofts (hlutfallstala 0 - 1)
     - :math:`\phi = \frac{p}{p_s}`
   * - :math:`p`
     - mettunarrakaprýstingur í pípu
     - :math:`Pa`
   * - :math:`p_s`
     - mettunarrakaprýstingur yfir sléttu yfirborði
     - :math:`Pa`
   * - :math:`\sigma`
     - yfirborðsspenna (hitastigsháð)
     - :math:`N/m`
   * - :math:`M_w`
     - mólmassi vatns
     - :math:`kg/mol`
   * - :math:`r`
     - radíus pórunnar
     - :math:`m`
   * - :math:`\rho_w`
     - eðlisþéttleiki vatns
     - :math:`kg/m^3`
   * - :math:`R`
     - almenni gasfastinn
     - :math:`8314.3,  [J/(kmol \cdot K)]`
   * - :math:`T`
     - hitastig
     - :math:`K`

Undirþrýstingur í póru er iðulega settur sem (jafna 3.13);

.. admonition:: Jafna 3.13
   :class: jafna

   .. math::
      p_w = \frac{2 \cdot \sigma}{r}

Jafna 3.13 ásamt 3.12 gefur (jafna 3.14);

.. admonition:: Jafna 3.14
   :class: jafna

   .. math::
      p_w= - \frac{\rho_w \cdot R \cdot T}{M_w} ln(\varphi)

Jafna 3.14 gefur samband milli undirþrýstings í póru og rakaþrýstings,
en undirþrýstingur í póru (e. suction) hentar vel sem mat á drifkrafti
rakaflutnings vegna hárpípukrafta.

Útsveim og varmasveim
?????????????????????

Í þeim tilvikum sem pórustærð í efni er svipuð eða minni heldur en “frí”
fjarlægð milli vatnssameinda, þá ákvarðast hreyfing sameinda ekki af
innbyrðis áhrifum þeirra heldur áhrifum frá yfirborðum póranna.
Sameindirnar hreyfast innbyrðis óháð, slíkur rakaflutningur nefnist
útsveim (e. effusion).

Rakaflutningur á gufuformi í efni getur einnig orðið vegna áhrifa
hitastiguls. Hitamunur í gasblöndu veldur aðskilnaði vegna mismunandi
mólmassa gastegunda. Í röku lofti er sameindamassi vatnsgufu lægri
heldur en mólmassi súrefnis og köfnunarefnis, vatnsgufan leitar því til
heitari hlutans en súrefni og köfnunarefni til þess kaldari. Áhrif
varmasveims (e. termodiffusion) verða helst merkjanleg í mjög póróttum
efnum og við mikinn hitastigul.

Útreikningur á rakaflutningi
--------------------------------

Rakaflutningur verður helst eftir þrem leiðum eins og þegar hefur verið
nefnt; flæði, streymi í lofti og hárpípukröftum. Iðulega er erfitt að
skilja á milli flutnings annarsvegar sem flæði og hinsvegar streymi í
lofti (hliðstætt vandamál og varðar varmaflutning), en þó er vitað að
áhrifa vegna streymis í lofti verður fyrst merkjanlegt við háan loftraka
(oft :math:`\varphi` >  80 – 85 %).

Rakaflutningur í hárpípum á sér aðeins stað frá efni með lágan
flutningsstuðul til efnis með háan flutningsstuðul (frá grófpóróttu efni
til fínpóróttara).

Rakaflutningur verður hér reiknaður samkvæmt staðaluppkastinu TC 89 WI
29.3:2003. Tilvísanir í staðalinn verða hér styttar í TC89.

Í efni reiknast þéttleiki rakaflutnings, :math:`kg/(m^2 \cdot s)` eins og
jafna 3.15 sýnir;

.. admonition:: Jafna 3.15
   :class: jafna

   .. math::
      g = g_v + g_l

þar sem 

.. list-table::
   :header-rows: 0
   :widths: 5 20

   * - :math:`g_v`
     - Rakaflutningur vegna flæðis (:math:`g_p`) og streymis í lofti (:math:`g_c`)
   * - :math:`g_l`
     - Hárpípuflutningur

Rakaflutningur vegna flæðis og streymis í lofti, :math:`g_v`, er
skilgreint eins og jafna 3.16 sýnir;

.. admonition:: Jafna 3.16
   :class: jafna

   .. math::
      g_v = - \frac{1}{\mu (\varphi)} \delta_0(T) \frac{\partial p_v}{\partial x} + \frac{g_a}{\rho_a} \frac{p_v}{R_{H_{2}O} \cdot T}

þar sem 

.. list-table:: *Tákn og skýringar – Vatnsgufuflæði*
   :header-rows: 0
   :widths: 10 60 30

   * - :math:`\mu(\varphi)`
     - mótstöðutala vatnsgufuflæðis við rakainnihald :math:`\varphi`
     - 
   * - :math:`\delta_0(T)`
     - gufuheypni í lofti með hitastig :math:`T`
     - :math:`kg/(m \cdot Pa \cdot s)`
   * - :math:`\delta p_v / \delta x`
     - stigull gufþrýstings í lofti
     - :math:`Pa`
   * - :math:`g_a`
     - þéttleiki loftflutnings
     - :math:`kg/(m^2 \cdot s)`
   * - :math:`\rho_a`
     - þéttleiki lofts
     - :math:`kg/m^3`
   * - :math:`p_v`
     - hlutfallsþrýstingur vatnsgufu
     - :math:`Pa`

.. math::
   R_{H_{2}O} = \frac{R}{M_w} = \frac{8.314}{0.018}  = 461.889

Gufuhleypni í lofti, er eins og jafna 3.17 sýnir (DIN 52615);

.. admonition:: Jafna 3.17
   :class: jafna

   .. math::
      \delta_0 = 2.0 \cdot 10^{-7} \cdot \frac{T^{0.81}}{P_a}, kg/(m \cdot Pa \cdot s)

Í fræðiritum (þetta var og er jafnvel víða venja enn) eru stuðlarnir við
drifkraft rakaflæðis teknir saman í eina stærð, sbr. jöfnu 3.7.
Stuðullinn er oft nefndur :math:`D_x` þar sem lágmerkið skýrir hvaða
drifkraftur er notaður; oft w fyrir rakainnihald og p fyrir
rakaþrýsting, sem dæmi um þetta má nefna gildið :math:`\delta_p; \delta_p=\delta_0/\mu`. Ókostur aðferðarinnar er sá að
rakaflæðistuðullinn D er augljóslega háður drifkraftinum. Til er
fjöldinn allur af mismunandi efnisgildum fyrir útreikning á
rakaflutningi, umreiknistuðla fyrir öll algengustu gildi er t.d. að
finna í Rb-blaðinu Rb (I3).001 ”Vindþéttilög í
húsbyggingum-efniseiginleikar og frágangur”. Kosturinn við framsetningu
staðaluppkastsins er að stuðullinn :math:`\mu` er hrein hlutfallstala sem er
efnisháð, og einungis þarf að velja :math:`\delta` stuðulinn þannig að hann passi
fyrir valinn drifkraft.

Fyrir yfirborðslög (yfirborðsmótstöður, málningar o.f.l.) þá er
jafngilda formið fyrir jöfnu 3.16 , eins og jafna 3.18 sýnir;

.. admonition:: Jafna 3.18
   :class: jafna

   .. math::
      g_v = - \frac{1}{s_{d,s}} \delta_0 \cdot (p_{v,a} - p_{v,s}) + \frac{g_a}{\rho_a} \cdot \frac{p_{v,a}}{R_{H_{2}O} \cdot T_a}

Af samanburði milli jafnanna 3.16 og 3.18 sést að jafngildisþykkt
loftlags, :math:`s_d`, fæst sem; :math:`s_d= \mu \cdot d`, þar sem d er
þykkt efnislags. Þá gildir almennt að mótstaða efnislags, eða yfirborðs,
fæst sem (jafna 3.19);

.. admonition:: Jafna 3.19
   :class: jafna

   .. math::
      Z_p = \frac{s_d}{\delta_0} = \frac{d \cdot \mu}{\delta_0}

Efnisgildi til útreikninga á rakaflutningi má finna t.d. í staðlinum ÍST
EN 12524:2000, tækniblaðinu NBI 573.430 og handbókum eftir S. Geving og
J. V. Thue (2002), Nevander og Elmarsson (1994). Rakaflæðimótstaða efna
er alltaf háð hitastigi (sem leiðrétt er fyrir með :math:`\delta_0` 
stuðlinum í jöfnum 3.14 og 3.16) og iðulega einnig rakainnihaldi efna,
þar sem rakaflæðimótstaðan fellur almennt með hækkandi efnisraka.

Efnisframleiðendur og efnissalar, og einnig eldri rit, gefa stundum upp
rakaflutningsmótstöðuna Z í stað :math:`s_d`  gildis eins og nú
tíðkast. Þá þarf þó að skoða vandlega hvaða eining er á uppgefnu
Z-gildinu (oft :math:`GPa \cdot s \cdot m^2 /kg`) og taka tillit til þess í
útreikningunum.

Jafngildisþykkt yfirborðsloftlags (mótstaða við yfirborð),
:math:`s_{d,s}`, er sýnd í töflu 3.3.

.. list-table:: *Tafla 3.3 Jafngildisþykkt yfirborðsloftlags* *(e: boundary layer)* (heimild: TC 89)
   :header-rows: 1
   :widths: 40 20

   * - **Yfirborð inni – Stefna varmaflutnings**
     - :math:`s_{d,si}` (m)
   * - Lárétt
     - 0,008
   * - Upp
     - 0,004
   * - Niður
     - 0,03
   * - **Yfirborð úti** (háð vindhraða :math:`v`)
     - :math:`s_{d,se}` (m)
   * - 
     - :math:`\frac{1}{67 + 90 \cdot v}`

Samantekt fyrir nokkur algeng byggingarefni er í töflu 3. 4 og fyrir
algeng efnislög í töflu 3.5.

.. list-table:: *Tafla 3.4 Rakaflæði­mótstaða efna,* :math:`\mu` *(heimild: NBI 573.430, o.fl.)*
   :header-rows: 2
   :widths: 25 10 13 13 13 13

   * - **Efni**
     - **Þéttleiki**  
     - :math:`\mu` **við 35–70 % HR**
     - :math:`\mu` **við 70–80 % HR**
     - :math:`\mu` **við 80–90 % HR**
     - :math:`\mu` **við 90–95 % HR**
   * - 
     - *(kg/m³)*
     - 
     - 
     - 
     - 
   * - Steinull
     - 
     - 35–70
     - 
     - 
     - 
   * - Steinull
     - 15
     - 1,2–1,8
     - 
     - 
     - 
   * - Frauðplast, þanið
     - 200
     - 2,2–3,3
     - 
     - 
     - 
   * - Frauðplast, þanið
     - 20
     - 19–29
     - 19–29
     - 19–29
     - 19–29
   * - Frauðplast, sprautað
     - 30
     - 98
     - 
     - 
     - 
   * - Frauðplast, sprautað
     - 20–60
     - 150
     - 
     - 
     - 
   * - Steypa v/s 0,5 (norsk)
     - 
     - 131–195
     - 82–131
     - 27–82
     - 9–27
   * - Fura – þvert á trefjastefnu
     - 
     - 29–130
     - 13–51
     - 7,4–26
     - 
   * - Krossviður
     - 
     - 29–130
     - 14–51
     - 8–25
     - 
   * - OSB plata
     - 650
     - 49
     - 
     - 
     - 
   * - Spónaplata
     - 635
     - 37
     - 
     - 
     - 
   * - Trétrefjaplata
     - 900
     - 102
     - 
     - 
     - 
   * - EPDM dúkefni
     - 
     - ..
     - 60000
     - ..
     - 
   * - PVC
     - 
     - ..
     - 40000
     - ..
     - 

.. list-table:: *Tafla 3.5 Rakaflæðimótstaða efnislaga,* :math:`s_d` *(heimild: NBI 573.430)*
   :header-rows: 2
   :widths: 50 10 20

   * - **Efni**
     - **Þykkt**
     - **Jafngildisþykkt loftlags,** :math:`s_d`
   * -
     - *(mm)*
     - *(m)*
   * - Textíl teppi – með latex bakhlið
     - 
     - 3,3–4,1
   * - Linoleum, HR 35–70%
     - 2,5
     - 10
   * - Linoleum, HR 70–80%
     - 2,5
     - 5,3
   * - Vinyl gólfdúkur, mjög lokaður
     - 
     - 254
   * - Akrýllatex málning
     - 0,05
     - 0,14–0,53
   * - Alkýdmálning, 2umf., mött vegg- og loftamálning
     - 
     - 2,5–5
   * - Epoxy gólfmálning – tveggja þátta, 2umf.
     - 
     - 7,6–14
   * - Polyethylen (PE) rakavarnarlag
     - 0,15
     - 70
   * - .. do
     - 0,20
     - 90
   * - Tjörupappi (polyester vefur)
     - 
     - 100
   * - PVC þakdúkur
     - 1,4
     - 19
   * - Polyisobutylen (PIB) þakdúkur
     - 1,5
     - 390
 
Í eftirfarandi verður litið framhjá áhrifum loftflutnings í efni og
hárpípuflutnings á rakaflutning (nema að því leyti sem þessi áhrif eru
innifalinn í viðeigandi efnisgildum). Útreikningar taka hér einvörðu
tillit til rakaflæðis.

Rakaflutningur, rakaástand og rakaþétting
?????????????????????????????????????????

Við stöðug hita- og rakaskilyrði í umhverfi byggingarhluta þá næst
rakajafnvægi í byggingarhluta þegar rakaástandið ákvarðast af rakaflæði,
ef aðstæður eru þannig að rakaþétting á sér ekki stað.
Mettunarrakaþrýstingur, jafna 3.1 (og mettunarrakamagn, jafna 3.2) í
hverju sniði ræðst af hitastigi þar, en hitafall í einsleitu efnislagi
er línulegt við stöðug skilyrði eins og fjallað var um í kafla 2.
Rakaþrýstingur í sniðinu, jafna 3.16, verður því aðeins línulegur að
rakaflæðimótstaðan Z (jafna 3.19) sé óháð hitastigi og efnisraka,
mettunarrakaaferillinn verður hinsvegar alltaf aðeins sveigður þar sem
samband mettunarraka og hitastigs er ekki línulegt.

Þrátt fyrir að rakaflæðimótstaðan sé nánast alltaf hita- og rakaháð þá
er venja í útreikningum við stöðug skilyrði að líta framhjá þessu, til
einföldunar er gert ráð fyrir að bæði rakaþrýstingur og
mettunarrakaþrýstingur í einsleitu efnislagi breytist línulega.

Mettunarrakaþrýstingur í efnislagi er því ákvarðaður útfrá hitastigi á
yfirborðum efnislags og rakaþrýstingur í efninu útfrá rakaþrýstingi á
yfirborðum. Reikningur rakaþrýstings í byggingarhluta sem samsettur er
úr mörgum efnislögum er gerður hliðstætt og gert var fyrir
hitastigsdreifingu í kafla 2, reiknuð er mótstöðutala rakaflæðis lag
fyrir lag og rakaþrýstingur reiknaður hlutfallslega útfrá
umhverfisaðstæðum. Í þeim tilvikum sem reiknaður rakaþrýstingur er hærri
heldur en mettunarþrýstingur í sniði þá á sér stað rakaþétting, annars
ekki. Skoða þarf tvö tilvik (mynd 3.3);

.. figure:: ./myndir/kafli03/Raka_og_mettunarþrýstingur.png
  :align: center
  :width: 90%

.. centered:: 
   Mynd 3.3 Raka- og mettunarrakaþrýstingur í sniði

**I. Engin rakapétting**

Rakaflutning, á flatar- og tímaeiningu, í gegnum byggingarhluta má
ákvarða í samræmi við (fyrri hluta) jöfnu 3.16, sem nú er umskrifuð eins
og jafna 3.20 sýnir;

.. admonition:: Jafna 3.20
   :class: jafna

   .. math::
      g = \frac{1}{Z_T} \cdot (P-1 - p_2)

Þar sem

.. list-table:: 
   :header-rows: 0
   :widths: 10 70 20

   * - :math:`g`
     - rakaflutningur frá 1 til 2
     - :math:`kg/(m^2 \cdot s)`
   * - :math:`Z_T`
     - heildarmótstaða gegn rakaflæði
     - :math:`m^2 \cdot s \cdot Pa / kg`
   * - :math:`p_1, p_2`
     - rakaþrýstingur beggja vegna við byggingarhluta
     - :math:`Pa`

**II. Rakaþétting**

Rakaþéttingin er til einföldunar öll reiknuð í “fyrsta kalda sniði” í
byggingarhluta (á mynd 3.3 er það snið n+2, þegar rakaflutningur er frá
1 til 2, og mettunarraki þar er :math:`p_cond` ). Í því tilviki að
rakaþétting reiknast verða í tveim eða fleiri sniðum, þá þarf að setja
rakaþrýsting í innsta sniðinu jafnt og mettunarrakaþrýsting, og
endurreikna dæmið frá þeim punkti og svo koll af kolli fyrir hvert snið
utar þar sem rakþrýstingur fer yfir mettunarraka.

Reiknaðar eru mótstöður innan- og utan við þéttingarsniðið,
:math:`Z_{inn}` og :math:`Z_{út}`, og samsvarandi rakaflutningur, sjá
mynd 3.3;

.. admonition:: Jafna 3.21
   :class: jafna

   .. math::
      g_{inn} = \frac{1}{Z_{inn}} \cdot (p_1 - p_{cond})

.. admonition:: Jafna 3.22
   :class: jafna

   .. math::
      g_{út} = \frac{1}{Z_{út}} \cdot (p_{cond} - p_{2})

.. admonition:: Jafna 3.23
   :class: jafna

   .. math::
      g_{uppsafnað} = g_{inn} - g_{út}

Þegar útreikningar sýna að rakaþétting eigi sér stað þá þarf að meta
yfir hversu langan tíma þetta ástand varir og athuga svo hvort
byggingarhlutinn geti losað sig við rakann þegar aðstæður breytast
(samsvarandi reikningar og í lið II.), það þarf þannig að leggja mat á
hvort rakauppsöfnun verði viðvarandi eða hvort um árstíðasveiflu sé að
ræða. Þegar reiknuð er útþornun þá þarf vitaskuld að reikna rakaþrýsting
miðað við rakaþéttingu í þéttingarsniðinu og með ítrun áætla hvort
útþornun eigi sér stað og þá hversu langan tíma hún tekur.

Það er þó ekki einungis rakaþétting sem er áhugaverð heldur einnig sá
tími þegar hár loftraki helst í einstökum sniðum byggingarhluta. Hætta á
mygluvexti er metin útfrá rakaástandi og á sama tíma hitaástandi yfir
skilgreindum mörkum, og talinn saman tími sem skilyrðin eru uppfyllt.

|

Í Byggingarreglugerð, kafla 10.5, er fjallað almennt um raka (m.a. grein
10.5.1);

.. figure:: ./myndir/kafli03/grein10_5_1.png
  :align: center
  :width: 90%

|

Orðalagið “skaða á mannvirki” er ekki skilgreint sérstaklega, og er því
á verksviði hönnuðar hverju sinni að meta hvort t.d. rakauppsöfnun,
tímabundin eða varanleg, sé skaðleg. Í þessu sambandi er nauðsynlegt að
leggja mat á áreiðanleika þeirra aðferða sem beitt er til að meta
rakaástand í byggingarhluta á hönnunarstigi bygginga.

Í hefðbundnum útreikningum, eins og hér er fjallað um þarf að hafa
eftirfarandi í huga;

#. Útreikningar byggja á einfölduðum reiknilíkönum.

#. Upplýsingar um efniseiginleika (og rakaþol) eru iðulega af skornum
   skammti.

#. Upplýsingar um umhverfisaðstæður (raka og hita) eru háðar óvissu.

#. Hæfni efna til að taka upp raka (tímabundið) án þess að skemmdir
   hljótist af.

Það er því ástæða að hafa í huga að reiknislegt mat á rakaástandi er
fremur gæðamat heldur en fræðilegt mat og því eðlilegt að halda sig
frekar öruggu megin þegar niðurstöður eru metnar. Í þessu sambandi er
eðlilegt að miða við að öryggi valinnar uppbyggingar sé nægjanlegt, t.d.
að reiknuð útþornun sé umtalsvert meiri heldur en reiknuð rakauppsöfnun.



Reiknaður rakaflutningur í byggingarhluta og metin hætta á rakaþéttingu
-----------------------------------------------------------------------

Dæmi:

Steyptur veggur einangraður að innan með 100 mm frauðplasti, múraður að
innan með 20 mm sementsmúr, en að utan með 25 mm sementsmúr. Veggurinn
málaður að innan með alkydmálningu (2 umf) og akryllatex að utan (2
umf). – Efnisgildi fyrir rakaeiginleika tekin úr töflum 3.3 og 3.4,
einangrunargildi samsvarandi og í kafla 2.

Reiknað er hitastig og rakaástand í sniði fyrir aðstæður; inni 22 °C /
45 %HR, úti -2 °C / 80 %HR (undir meðallagi fyrir janúar í Reykjavík).

Útreikningar og niðurstöður í töflu;

.. figure:: ./myndir/kafli03/útreikningur.png
  :align: center
  :width: 90%

|

Niðurstöður sýna að við framangreindar aðstæður verður rakaþétting í
veggnum svo nemur :math:`0,0070 g/(m^2,h)`, eða :math:`5 g/m^2`,
mánuð – rakaþéttingin er óveruleg þegar tekið er tillit til mögulegrar
rakaupptöku veggjarins, en athuga ber að hitastig innra byrðis
steypunnar er undir frostmarki og þéttingin mun því byggjast upp sem
klakabrynja. Aðstæðurnar sem um ræðir munu þó sjaldan standa nema
stuttan tíma í senn og þegar veggyfirborðið þiðnar þá getur steypan
sennilega tekið við rakanum án vandkvæða.

.. figure:: ./myndir/kafli03/Mollier.png
  :align: center
  :width: 90%

.. centered::
   Línurit 3.3 Mollier línurit fyrir rakt loft

|

.. centered::
   Tafla 3.6 Mettunarraki; þrýstingur og rakamagn í lofti, háð hitastigi. Fyrir hitastig undir frostmarki
   er miðað við aðstæður yfir ís.

.. figure:: ./myndir/kafli03/Tafla3_6.png
  :align: center
  :width: 90%

Heimildir og ítarefni
---------------------

Björn Marteinsson (1999) ” Loftræsing í íbúðarhúsum”, erindi á ráðstefnu
Lagnafélags Íslands, birt í ráðstefnuriti

DIN (1981) Wärmeschutz im Hochbau DIN 4108

DIN (1987) Bestimmung der Wasserdampfdurchlässigkeit von Bau- und
Dämmstoffen DIN 52615

S. Geving og J. V. Thue (2002) Fukt i bygninger, Norges
byggforskningsinstitutt, Håndbok 50, Oslo

E. Hagemann (1988), Byggematerialer – grundbog, polyteknisk Forlag,
København

ÍST EN 12524:2000 Building materials and products - Hygrothermal
properties - tabulated design values

Jón Sigurjónsson (1983) Rb (I3).001 ”Vindþéttilög í
húsbyggingum-efniseiginleikar og frágangur”, Rb-blað, Rannsóknastofnun
byggingariðnaðarins, Keldnaholti

NBI (2003) Materialdata for vanndamptransport, Byggforskserien
Byggdetaljer 573.430 Oslo,

L. E. Nevander, B. Elmarsson (1994) Fukthandboken, Svensk byggtjänst,
Stockholm

Óli Hilmar Jónsson (1982) Raki í húsum, sérrit 46, Rannsóknastofnun
byggingariðnaðarins, Keldnaholti

ISO (1997) Draft prEN 13013-3:1997 Hygrothermal performance of buildings
– climatic data-part 3: calculation of driving rain index for vertical
surfaces from hourly wind and rain data

ÍST EN ISO (2012) 13788:2012 \ *Hygrothermal performance of building
components and building elements - Internal surface temperature to avoid
critical surface humidity and interstitial condensation – Calculation
method*

K. Sandin (1987) Fukttillstånd i autoklaverade lättbetongväggar -
Fältmätning av slagregnets och ytskiktets inverkan, LTH,
Byggnadsmateriallära, Rapport TVBM 3026, Lund

TC 89 WI 29.3:2003 (2003-04) Hygrothermal performance of building
components and building elements – Assessment of moisture transfer by
numerical simulation

Ýmsir (1997), Husbygningsteknikk – Bind 1, Institutt for
husbygningsteknikk, Norges tekniske høgskole, Universitetet i Trondheim,
Norge

| 

.. container::

.. |image1| image:: myndir/kafli03_html_a7d8479859b54b1d.png
   :name: Object1
.. |image2| image:: myndir/kafli03_html_cd3e6f54e7978999.png
   :name: Object2
.. |image3| image:: myndir/kafli03_html_ad3a34a5c13f82f5.png
   :name: Object3
.. |image4| image:: myndir/kafli03_html_fbb3b67d1be73d4c.png
   :name: Object4
.. |image5| image:: myndir/kafli03_html_4286c875169890a4.png
   :name: Object5
.. |image6| image:: myndir/kafli03_html_5de366bcdd9065f3.png
   :name: Object6
.. |Shape1| image:: myndir/kafli03_html_202b5496f648e91b.png
   :name: Shape1
   :width: 186px
   :height: 252px
.. |image7| image:: myndir/kafli03_html_765f8cd62da42455.png
   :name: Object7
.. |image8| image:: myndir/kafli03_html_c1c1313a75f4cb67.png
   :name: Object8
.. |Shape2| image:: myndir/kafli03_html_9c80ea57b8f7efc4.png
   :name: Shape2
   :width: 232px
   :height: 240px
.. |image9| image:: myndir/kafli03_html_39bf052b0923e521.png
   :name: Object9
.. |image10| image:: myndir/kafli03_html_1eea0bfffb2381d4.png
   :name: Object10
.. |image11| image:: myndir/kafli03_html_6ad426cd2874ef93.png
   :name: Object11
.. |image12| image:: myndir/kafli03_html_f7a8b52f238cb8d1.png
   :name: Object12
.. |image13| image:: myndir/kafli03_html_2636065125cc81ec.png
   :name: Object13
.. |image14| image:: myndir/kafli03_html_336d59f5ffb29ca5.png
   :name: Object14
.. |image15| image:: myndir/kafli03_html_a80e5b35ae65e0b6.png
   :name: Object15
.. |image16| image:: myndir/kafli03_html_3b4150303398fc73.png
   :name: Object16
.. |image17| image:: myndir/kafli03_html_497bf3b85aa288ac.png
   :name: Object17
.. |image18| image:: myndir/kafli03_html_a7d8479859b54b1d.png
   :name: Object18
.. |image19| image:: myndir/kafli03_html_41c53768b29768af.png
   :name: Object19
.. |Shape3| image:: myndir/kafli03_html_2e0938f5994fc94f.png
   :name: Shape3
   :width: 586px
   :height: 1px
.. |image20| image:: myndir/kafli03_html_93ec2217c352a041.png
   :name: Object20
.. |Shape4| image:: myndir/kafli03_html_2e0938f5994fc94f.png
   :name: Shape4
   :width: 586px
   :height: 1px
.. |image21| image:: myndir/kafli03_html_286cdc60b9a19392.png
   :name: Object21
.. |image22| image:: myndir/kafli03_html_2b5c02407f7cc8e9.png
   :name: Object22
.. |image23| image:: myndir/kafli03_html_71cbbfb4e5447db9.png
   :name: Object23


