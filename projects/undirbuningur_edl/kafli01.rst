Mælieiningar
============

SI-einingakerfið
----------------

Í (næstum) öllum löndum heims er notað samræmt mælikerfi, SI einingakerfið, þar sem einkennandi stærðir heimsins hafa eigin grunneiningar.
Lengd hefur þar grunneininguna metri og tími grunneininguna sekúnda.

SI-grunneiningarnar eru sjö:

.. math::
 \begin{array}{c | c | c}
	  \text{Mælistærð} & \text{Eining} & \text{Tákn} \\ \hline
	  \text{Vegalengd} & \text{Metri} & m \\
    \text{Tími} & \text{Sekúnda} & s \\
    \text{Massi} & \text{Kílógramm} & kg\\
	  \text{Rafstraumur} & \text{Amper} & A\\
    \text{Hitastig} & \text{Kelvin} & K \\
    \text{Ljósstyrkur} & \text{Candela} & cd \\
    \text{Fjöldi} & \text{Mól} & n \\ \hline
  \end{array}

Einingar fyrir aðrar stærðir eru settar saman úr grunneiningum SI einingakerfisins.
Hraði, breyting á staðsetningu yfir eitthvert tímabil, hefur eininguna metrar á sekúndu (m/s).

.. tip::
  **Að breyta á milli eininga**

  Í daglegu tali notum við oft eininguna kílómetrar á klukkustund fyrir hraða, þó SI-einingin sé önnur. Skoðum hvernig við breytum á milli þessara eininga.

  Við vitum að ein klukkustund hefur 3600 sekúndur (af því það eru 60 mínútur í hverri klukkustund og 60 sekúndur í hverri mínútu: :math:`60\cdot 60 = 3600`) og að einn kílómetri eru 1000 metrar. Þar sem :math:`1 \text{ klst} = 3600 \text{ s}` þá er hlutfallið 1, þ.e.

  .. math::

  	\frac{1\text{ klst}}{3600\text{ s}}=1

  og eins fyrir lengdareininguna:

  .. math::

  	\frac{1000\text{ m}}{1\text{ km}} =1

  Þar sem það breytir ekki stærð að margfalda hana með einum þá getum við breytt kílómetrum á klukkustund yfir í metra á sekúndu svona:

  .. math::
    1 \frac{\text{km}}{\text{klst}} = 1\frac{\text{km}}{\text{klst}}\cdot \frac{1\text{ klst}}{3600\text{ s}} \cdot \frac{1000\text{ m}}{1\text{ km}}

  Svo styttast einingarnar út:

  .. math::
    1 \frac{\text{km}}{\text{klst}} = \frac{1000}{3600}\frac{\sout{\text{km}}}{\sout{\text{klst}}}\cdot \frac{\sout{\text{ klst}}}{\text{ s}} \cdot \frac{\text{ m}}{\sout{\text{ km}}} = \frac{1}{3.6} \frac{\text{ m}}{\text{ s}}

  Þessa aðferð má nota til þess að breyta á milli allra eininga.

.. note::
  Í jöfnum þurfa einingarnar að passa saman, en allir liðir hverrar jöfnu þurfa að hafa sömu einingar. Það er til dæmis alveg merkingarlaust að leggja saman hraða og staðsetningu eða hitastig og massa. Þetta á líka við þegar mismunandi einingar eru notaðar til að lýsa sama fyrirbærinu, en ef leggja á saman eina stærð sem mæld er í metrum og aðra sem er mæld í millímetrum þá þarf að breyta öðru hvoru í hitt:

  .. math::

  	1 \text{ m} + 3\text{ mm} = 1000 \text{ mm} + 3\text{ mm} = 1003 \text{ mm} = 1.003 \text{m}

.. tip::
  Skoðum eina af :ref:`hreyfijöfnunum <s.hreyfijofnur>` sem lýsir staðsetningu hlutar (:math:`x`) sem falli af upphafsstaðsetningu (:math:`x_0`), upphafshraða hans (:math:`v_0`), hröðuninni sem hann hefur (:math:`a`) og tíma (:math:`t`):

  .. math::

  	x=x_0 + v_0t + \frac12 at^2

  Allir liðir þessarar jöfnu þurfa að hafa einguna fyrir staðsetningu, metra. Athugum hvort þetta passi ekki örugglega.

  * :math:`x_0` hefur eininguna metri, svo fyrsti liður jöfnunnar er í lagi.
  * Í öðrum liðnum kemur fyrir margfeldi hraða og tíma, en þá verður einingin líka metri: :math:`1 \frac{\text{m}}{\text{s}}\cdot \text{s} = 1 \text{ m}`
  * Þriðji liðurinn er líka í lagi af því að hröðun hefur eininguna metri á sekúndu í öðru veldi og svo er margfaldað við tíma í öðru veldi: :math:`1 \frac{\text{m}}{\text{s}^2} \cdot \text{s}^2 = 1 \text{ m}`

*Rúmmál* (e. volume) hefur SI-eininguna rúmmetri (:math:`\text{m}^3`) en í daglegu tali notum við oft lítra (L), en í einum rúmmetra eru þúsund lítrar. Einn millílíter (:math:`\text{mL}`, :math:`\frac{1}{1000}` úr lítra) er einn rúmsentímetri (:math:`\text{cm}^3`) .

*Eðlismassi* (e. density) einhvers er hlutfall massa þess og rúmmálsins sem það tekur, oft táknað með gríska stafnum ró (:math:`\rho`). SI-eining eðlismassa er kílógramm á rúmmetra (:math:`\text{kg/m}^3`) en einingarnar gramm á rúmsentímetra (:math:`\text{g/cm}^3`) og kílógramm á líter :math:`\text{kg/L}` eru líka stundum notaðar.

Ferskvatn hefur eðlismassa sem er í kringum :math:`\rho_{vatn}=1000 \text{kg/m}^3`. Saltvatn er aðeins þyngra, :math:`\rho_{sjór}=1030 \text{kg/m}^3`. Járn hefur háan eðlismassa :math:`\rho_{jarn}=7850\text{kg/m}^3` en loft lágan :math:`\rho_{loft} =1.2 \text{kg/m}^3`.

Hlutir sem hafa hærri eðlismassa sökkva í efnum sem hafa lægri eðlismassa. Þannig sekkur járn til sjávarbotns og helíumblöðrur reyna að flýja eigendur sína á 17. júní.



Forskeyti SI-kerfisins
~~~~~~~~~~~~~~~~~~~~~~

Þegar fengist er við stærri mælistærðir, svo sem langar vegalengdir, er unnið með marga metra.
Því hafa vísindamenn vanið sig á að kalla þúsund metra öðru nafni: einn kílómetra (:math:`1000 \text{m} = 1 \text{km}`). Þegar fengist er við litlar mælistærðir, svo sem þykkt á pappír, fást aðeins brot af heilum metrum.
Algengt er að nota millímetra, einn þúsundasta úr metra. Þetta er tekið saman í þessari töflu,
á milli kíló og millí eru:

.. math::
  \begin{array}{c|c|c}
    \text{Forskeyti} & \text{Tákn} & \text{Veldi} & \text{Margfeldi}\\ \hline
    \text{Kíló} & \text{k} & 10^{3} & 1000\\
    \text{Hektó} & \text{h} & 10^{2} & 100 \\
    \text{Deka} & \text{da} & 10^{1} & 10 \\
    \text{--} & \text{--} & 10^{0} & 1 \\
    \text{Desi} & \text{d} & 10^{-1} & 0.1\\
    \text{Centi} & \text{c} & 10^{-2} & 0.01\\
    \text{Millí} & \text{m} & 10^{-3} & 0.001 \\ \hline
  \end{array}

Við getum því lýst 10 metrum sem 1 dam, 100 dm eða 1000 cm.
Mörg hafa séð svona mynd sem nota má til að breyta á milli:

.. image:: ./myndir/einingar/einingahus.svg
  :width: 90 %
  :align: center

Í eðlisfræði er líka fengist við risastór fyrirbæri (eins og stjörnuþokur úti í geimi) og allra minnstu fyrirbærin (eins og rafeindir).
Þá þarf enn stærri forskeyti:

.. math::
  \begin{array}{c|c|c}
    \text{Forskeyti} & \text{Tákn} & \text{Veldi} & \text{Margfeldi}\\ \hline
    \text{Peta} & \text{P} & 10^{15} & 1 000 000 000 000 000 \\
    \text{Tera} & \text{T} & 10^{12} & 1 000 000 000 000 \\
    \text{Giga} & \text{G} & 10^{9} & 1 000 000 000 \\
    \text{Mega} & \text{M} & 10^{6} & 1 000 000 \\
    \text{Kíló} & \text{k} & 10^{3} & 1 000\\
    \text{--} & \text{--} & 10^0 & 1\\
    \text{Millí} & \text{m} & 10^{-3} & 0.001 \\
    \text{Míkró} & \mu & 10^{-6} & 0.000 001 \\
    \text{Nanó} & \text{n} & 10^{-9} & 0.000 000 001 \\
    \text{Píkó} & \text{p} & 10^{-12} & 0.000 000 000 001 \\
    \text{Femtó} & \text{f} & 10^{-15} & 0.000 000 000 000 001 \\ \hline
  \end{array}

.. image:: ./myndir/einingar/einingahus2.svg
  :width: 90 %
  :align: center

.. note::
  Athugið að þegar fengist er við massa þá er SI-einingin kílógramm en ekki gramm. Forskeyti eru sjaldan notuð þegar talað er um massa, þ.e. það er aldrei talað um mega-kílógramm því það væri mjög ruglandi. Það eru þó ein undantekning á þessu, en sagt er að þúsund kíló séu eitt *tonn*. Í öðrum vísindagreinum er gramm notað sem grunneining fyrir massa, t.d. lyf eru oftast mæld í millígrömmum (:math:`1\text{mg} = 1\cdot 10^{-3}\text{g} = 1\cdot 10^{-3}\cdot 10^{-3}\text{kg}=1\cdot 10^{-6}\text{kg}`).

.. tip::
  Frá jörðinni til sólarinnar eru :math:`1.496 \cdot 10^{11}` m. Ritum þetta með mismunandi einingum.

  .. figure:: ./myndir/einingar/sol.svg
    :align: center
    :width: 50%

  .. math::
    \begin{aligned}
      1.496 \cdot 10^{11} \text{ m} &= 149600000000 \text{ m} \\
      & = 149.6 \cdot 10^{9} \text{ m} \\
      & = 149.6 \text{ Gm} \\
    \end{aligned}

  Það eru því 149.6 gígametrar til sólarinnar.

.. tip::
  Rafeind í vetnisatómi ferðast í kringum kjarnann í fjarlægðinni :math:`5.29\cdot 10^{-11}` m.
  Ritum þetta með mismunandi einingum.

  .. figure:: ./myndir/einingar/atom.svg
    :align: center
    :width: 50%

  .. math::
    \begin{aligned}
      5.29 \cdot 10^{-11} \text{ m} &= 0.0000000000529 \text{ m}\\
      &= 52.9 \cdot 10^{-12} \text{ m}\\
      &= 52.9 \text{ pm}\\
    \end{aligned}

  Rafeindin er því í 52.9 píkómetra fjarlægð frá kjarnanum.

.. tip::

  Edda á jörð sem er 12 ferkílómetrar. Hvað er lóðin margir hektarar (ferhektómetrar)?

  **Lausn**

  1 ferkílómetri er reitur sem er 1 kílómetri á hvorn kant. 1 kílómetri er 10 hektómetrar og því er:

  .. math::
    \begin{aligned}
    1 \text{ km}^2 &= 1 \text{ km} \cdot 1 \text{ km} \\
     &= 10 \text{ hm} \cdot 10 \text{ hm}\\ &= 100 \text{ hm}^2.
    \end{aligned}

  Jörðin hennar Eddu er því 1200 hektarar.

  .. figure:: ./myndir/einingar/hektari.svg
    :align: center
    :width: 60%

-----------

.. eqt:: daemi-edlismassi

  **Æfingadæmi** Eðlismassi kvikasilfurs (Hg) er :math:`\rho_{Hg}=13.5 \text{g/cm}^3`. Hver er eðlismassinn í SI-einingum?

  A) :eqt:`I` :math:`\rho_{Hg}=13.5 \text{ kg/L}`

  #) :eqt:`I` :math:`\rho_{Hg}=13500 \text{ kg/L}`

  #) :eqt:`C` :math:`\rho_{Hg}=13500\text{ kg/m}^3`

  #) :eqt:`I` :math:`\rho_{Hg}=13.5\text{ kg/m}^3`

--------------

Önnur mælikerfi
---------------

Í Bandaríkjunum er SI-einingakerfið ekki alltaf notað. Við notum þær aldrei hér en það er ágætt að þekkja þær engu að síður.
Þar eru lengdir mældar í  eftirfarandi einingum:

.. math::
  \begin{array}{c | c | c  }
	  \text{Mælistærð} & \text{Enskt heiti}& \text{Grunneining} \\ \hline
	  \text{Míla} & \text{mile} & 1609 \text{ m} \\
    \text{Stika} &\text{yard} & 0.9144 \text{ m} \\
    \text{Fet} & \text{foot} &  0.3048 \text{ m} \\
	  \text{Tomma} & \text{inch} &  0.0254 \text{ m} \\ \hline
  \end{array}

.. tip::

  Jörðin hennar Eddu er 12 ferkílómetrar. Hvað eru það margar fermílur?

  **Lausn**

  .. math::
    \begin{aligned}
      1 \text{ míla} &= 1609 \text{ m} = 1.609 \text{ km} \\
      (1 \text{ km})^2 &= \left( \frac{1}{1.609} \text{ míla} \right) ^2 \\
      1 \text{ km}^2 &= 0.386   \text{ míla}^2 \\
      12 \text{ km}^2 &=   12 \cdot 0.386 \text{ míla}^2 = 4.635 \text{ míla}^2 \\
    \end{aligned}

  12 ferkílómetrar eru því 4.635 fermílur.

Massi er þar mældur í pundum (e. pound) og únsum (e. ounces) en :math:`1 \text{ pund} = 0.4536 \text{ kg}` og :math:`1 \text{ únsa}=0.0283495 \text{kg}`.

Þar er hitastig mælt á Fahrenheit-kvarða, sem breyta má í Celcius (sem við notum) með eftirfarandi formúlu:

.. math::
  T_{°C}=\frac{5}{9}(T_{°F}-32)

SI- einingin fyrir hitastig er aftur á móti hvorki Celcius-kvarðinn né Fahrenheit-kvarðinn, heldur *Kelvin*.
Svona má breyta Celcius í Kelvin:

.. math::
  T_{K}=T_{°C}+273.15

Kelvin-kvarðinn er svipaður Celcius-kvarðanum að því leyti að aukning í hita um 1 K er jafnt aukningu í hita um 1 °C.
Munurinn er sá að Celcius setur 0 °C við frostmark vatns þá setur Kelvin 0 við *alkul*, lægsta mögulega hitastig efnisheimsins (:math:`-273.15^{\circ}\text{C} = 0\text{ K}`) en þá verða atóm alveg kyrr.
Það eru því ekki til neikvæð hitastig á Kelvin-kvarðanum!

Staðalform
----------

Staðalform (e. `scientific notation <https://en.wikipedia.org/wiki/Scientific_notation>`_) er gjarnan til þess að lýsa stærðum í eðlisfræði.
Þá er komman færð fram um :math:`n` bil og talan margfölduð með :math:`10^n` .
Þetta skýrist best með dæmum:

.. tip::
	Ljóshraðinn, með níu markverðum stöfum, er :math:`c=299792458` m/s. Á staðalformi er ljóshraðinn skrifaður :math:`c=2.99792458\cdot10^8` m/s, en þá er komman færð áfram um 8 sæti.

	Í langflestum tilvikum er nógu nákvæmt að vinna með :math:`c=3.00\cdot10^8` m/s og er það yfirleitt gert.


Notkun staðalforms auðveldar eðlisfræðingum að átta sig á *stærðargráðu* þess sem þau erum að skoða. Í öllum útreikningum þá getur maður metið um það bil hversu stóra tölu við búumst við í niðurstöðunni. Ef við erum að reikna hversu hratt bíll keyrir eftir götu sést að útreikningarnir hljóta að vera rangir ef svarið er af of stórri stærðargráðu:

.. math::

	v=1\cdot 10^4 \text{ m/s}= 10000\text{ m/s}

eða of lítilli:

.. math::

	v=1\cdot 10^{-5}\text{ m/s}=0.00001\text{ m/s}

-------------

.. eqt:: daemi-stadalform

  **Æfingadæmi** Hvernig er hraðinn :math:`0.002\text{ m/s}`  skrifaður á staðalformi?

  A) :eqt:`I` :math:`0.002\text{ m/s}`

  #) :eqt:`I` :math:`2\cdot 10^3 \text{ m/s}`

  #) :eqt:`C` :math:`2\cdot 10^{-3}\text{ m/s}`

  #) :eqt:`I` :math:`2\cdot 10^{-2}\text{ m/s}`

-----------------

Markverðir stafir
-----------------
Ef þú myndir mæla þykkt kennslubókarinnar í *Eðlisfræði 1* með venjulegri reglustriku myndirðu geta sagt að hún væri 2.7 cm á þykkt.
Þú mættir ekki segja að hún væri 2.70 cm þykk af því reglustrikur eru ekki sérlega nákvæmar, bókin gæti allt eins verið 2.68 cm eða 2.73 cm án þess að þú sæir það í mælingunni.
Ef þú myndir síðan mæla þykktina aftur en nú með `skíðmáli <https://is.wikipedia.org/wiki/Sk%C3%ADðmál>`_ myndirðu komast að því að hún væri 2.723 cm þykk.
Munurinn sem væri á mælingunum tveimur væri sá að *óvissa* (e. uncertainty) eða *skekkja* (e. error) skíðmálsins er minni en óvissa reglustrikunnar.

Við táknum *nákvæmni* (e. accuracy) mældrar stærðar með tákninu :math:`\pm` (plús-mínus).
Mæling reglustrikunnar á þykkt bókarinnar myndum við tákna með :math:`2.7 \pm 0.1` cm, en mælinguna með skíðmálinu með :math:`2.723 \pm 0.001` cm.
Reglustrikan myndi gefa þykkt bókarinnar með tveimur markverðum stöfum, en skíðmálið með fjórum.

.. tip::
  .. math::
    \begin{aligned}
      11.2 &= 1.12\cdot 10^1  & \text{þrír markverðir stafir}\\
      0.0000045&=4.5\cdot 10^{-6} & \text{tveir markverðir stafir}
    \end{aligned}

--------------

Þegar stærðir eru margfaldaðar saman þá má útkoman ekki hafa fleiri markverða stafi en sú tala sem hafði fæsta markverða stafi.

.. tip::
  .. math::
    \frac{0.745\cdot 2.2}{3.885} = 0.42

  Sú tala sem hefur fæsta stafi í þessu dæmi er 2.2, sem hefur 2 markverða stafi.
  Því er rétt að gefa svarið með 2 markverðum stöfum, 0.42, þó að flestar reiknivélar myndu gefa svarið :math:`0.4218790219`.


Þegar stærðir eru lagðar saman þá má útkoman ekki hafa minni óvissu en sú sem hafði mesta óvissu.
Markverðir stafir í samlagningu fer því eftir aukastöfum stærðanna, en ekki óvissu þeirra.

.. tip::
	.. math::
		27.153 + 138.2-11.74=153.6

	Hér hefur talan 138.2 mesta óvissu (fæsta aukastafi aftan við kommu) svo gefa þarf svarið með jafn mikilli óvissu, þ.e. einum aukastaf á eftir kommu. Flestar reiknivélar myndu gefa svarið 153.613 en í vísindalegum útreikningum getum við ekki tekið mark á síðustu tveimur tölunum.

Reglur þessar um meðferð markverðra stafa eiga við um alla útreikninga í eðlisfræði, bæði verklegum og fræðilegum.
