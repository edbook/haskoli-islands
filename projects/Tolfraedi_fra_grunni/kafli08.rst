.. _c.alyktanirumtalnabreytur:

Ályktanir um talnabreytur
=========================

Í þessum kafla munum við fjalla um öryggisbil og tilgátupróf sem við
framkvæmum til að draga ályktanir um talnabreytur. Algengast er að
ályktanir um talnabreytur séu byggðar á meðaltölum þeirra og fjallar
meginhluti þessa kafla, eða allur kafli :numref:`%s <s.alyktanirummedaltol>`, um
*ályktanir um meðaltöl*. Það veltur hins vegar stundum á því hvernig
dreifni talnabreytanna er háttað, hvaða tilgátupróf um meðaltal er
viðeigandi að framkvæma og eru þá tilgátupróf fyrir dreifni oft
framkvæmd áður en hafist er handa við að kanna meðaltölin. Því munum við
hefja umfjöllunina á *ályktunum um dreifni*, sem er efni kafla
:numref:`%s <s.alyktanirumdreifni>`.

.. _s.alyktanirumdreifni:

Ályktanir um dreifni
--------------------

Tilgátuprófin og öryggisbilin sem við munum skoða í þessum hluta eiga
við þegar draga á ályktun um dreifni normaldreifðra þýða, sem við táknum
:math:`\sigma^2`. Við byrjum á að skoða ályktanir um dreifni í einu
þýði, en þess konar ályktanir eru meðal annars mikið notaðar við könnun
ýmissa framleiðsluferla. Við munu sjá dæmi um slíkt í hluta
:numref:`%s <ss.alyktanirumdreifni>`. Þar á eftir, í hluta
:numref:`%s <ss.alyktanirumdreifnitveggjathyda>`, skoðum við tilgátupróf sem
notað er til að kanna hvort dreifni tveggja þýða, :math:`\sigma^2_1` og
:math:`\sigma^2_2`, sé ólík. Ef við getum gert ráð fyrir að dreifni
tveggja þýða sé sú sama notum við annað tilgátupróf til að draga
ályktanir um mismun meðaltala þeirra, heldur en ef dreifnin væri ólík.
Því er tilgátuprófið í hluta :numref:`%s <ss.alyktanirumdreifnitveggjathyda>`
oft framkvæmt áður en meðaltöl þýðanna eru könnuð.

.. _ss.alyktanirumdreifni:

Ályktanir um dreifni í einu þýði
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Þegar reikna á öryggisbil og prófa tilgátur um dreifni þýðis er notast
við :math:`\chi^2`-dreifinguna, sjá kafla :numref:`%s <ss.kikvadratdreifing>`.
Núlltilgátan er sett fram á þann hátt að dreifni þýðisins sé jöfn
einhverju ákveðnu gildi sem við köllum :math:`\sigma^2_0`, ritað
:math:`H_0: \sigma^2 = \sigma^2_0`. Byrjum á að skoða hvernig smíða má
öryggisbilið:

Öryggisbil fyrir dreifni normaldreifðs þýðis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Neðra mark :math:`1 - \alpha` öryggisbils er:
    
    .. math:: \frac{(n-1) \cdot s^2}{\chi^2_{1-\alpha/2,(n-1)}}
    
    Efra mark :math:`1 - \alpha` öryggisbils er:
    
    .. math:: \frac{(n-1) \cdot s^2}{\chi^2_{\alpha/2,(n-1)}}
    
    Öryggisbilið má því skrifa:
    
    .. math::
       \frac{(n-1) \cdot s^2}{\chi^2_{1-\alpha/2,(n-1)}} < \sigma^2 < 
       \frac{(n-1) \cdot s^2}{\chi^2_{\alpha/2,(n-1)}}
    
    þar sem :math:`n` er fjöldi mælinga í úrtakinu og :math:`s^2` er dreifni
    úrtaksins. :math:`\chi^2_{1-\alpha/2,(n-1)}` og
    :math:`\chi^2_{\alpha/2,(n-1)}` má finna í :math:`\chi^2`-töfluna í kafla :ref:`T.3 <a.chisqtafla>`.


--------------

Tilgátuprófið má svo framkvæma á eftirfarandi hátt:

Tilgátupróf fyrir dreifni normaldreifðs þýðis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Núlltilgátan er:
    
    .. math:: H_0: \sigma^2 = \sigma_0^2
    
    Prófstærðin er:
    
    .. math:: \chi^2 = \frac{(n-1)S^2}{\sigma_0^2}
    
    Gagntilgáturnar og höfnunarsvæðin eru
    
    +-----------------------------------------+-------------------------------------------------------------------------------------------+
    | Gagntilgáta                             | Hafna :math:`H_0` ef:                                                                     |
    +=========================================+===========================================================================================+
    | :math:`H_1: \sigma^2 < \sigma_0^2`      | :math:`\chi^2 < \chi^2_{\alpha,(n-1)}`                                                    |
    +-----------------------------------------+-------------------------------------------------------------------------------------------+
    | :math:`H_1: \sigma^2 > \sigma_0^2`      | :math:`\chi^2 > \chi^2_{1-\alpha,(n-1)}`                                                  |
    +-----------------------------------------+-------------------------------------------------------------------------------------------+
    | :math:`H_1: \sigma^2 \neq \sigma_0^2`   | :math:`\chi^2 < \chi^2_{\alpha/2,(n-1)}` eða :math:`\chi^2 > \chi^2_{1-\alpha/2,(n-1)}`   |
    +-----------------------------------------+-------------------------------------------------------------------------------------------+


--------------

Sýnidæmi: Ályktanir um dreifni þýðis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Bjarki drekkur mikið gos. Hann og fleiri neytendur hafa undanfarið sent
    kvartanir til gosverksmiðju nokkurrar um að of lítið gos sé í flöskum
    sem verksmiðjan selur. Mikilvægt er að áfyllingarferlið í verksmiðjunni
    sé stöðugt og dreifnin fari ekki yfir 10 ml\ :math:`^2` því fari hún
    yfir það mark mun of hátt hlutfall flaskanna innihalda of lítið eða of
    mikið gos. Til að kanna þetta frekar ákvað stjórn fyrirtækisins að
    framkvæma tilraun þar sem slembiúrtak af stærð 30 var tekið og magn í
    flöskunum mælt. Gera má ráð fyrir að magn í flöskunum fylgi
    normaldreifingu. Staðalfrávik magns í flöskunum 30 var reiknað,
    :math:`s = 3.5`. Kannið með viðeigandi tilgátuprófi hvort dreifni
    ferlisins sé hærri en 10 ml\ :math:`^2`. Notið :math:`\alpha = 0.05`.
    
    Förum eftir samantektinni um framkvæmd tilgátuprófa.
    
    #) Við ætlum að kanna tilgátu um dreifni normaldreifðs þýðis.
    
    #) Við fengum uppgefið að nota :math:`\alpha = 0.05.`
    
    #) Við ætlum að kanna hvort dreifnin sé hærri en þar sem að dreifnin
       gæti í raun verið lægri notum við tvíhliða próf. Tilgáturnar eru:
    
       .. math::
          \begin{aligned}
          H_0&:& \sigma^2 = 10\\
          H_1&:& \sigma^2 \neq 10 \end{aligned}
    
    #) Prófstærðin er:
    
       .. math:: \chi^2 = \frac{(n-1)S^2}{\sigma_0^2}
    
       Pössum okkur á að við fengum gefið að staðalfrávikið sé
       :math:`s = 3.5`. Við þurfum því að hefja í annað veldi til að finna
       dreifnina, :math:`s^2 = 3.5^2 = 12.25`. Við höfum einnig að
       :math:`n - 1 = 30 - 1 = 29`, :math:`\sigma_0^2` = 10. Við setjum
       þessar tölur inn í jöfnu prófstærðarinnar og fáum
    
       .. math:: \chi^2 = \frac{29 \cdot 12.25}{10} = 35.53
    
    #) Við þurfum að finna höfnunarsvæðið og notum til þess
       :math:`\chi^2`-töflu, :math:`\chi^2_{0.025,(29)}` = 16.05 og
       :math:`\chi^2_{0.975,(29)}` = 45.72. Við höfnum því núlltilgátunni ef
       :math:`\chi^2 < 16.05` eða :math:`\chi^2 > 45.72`. Við sjáum að svo
       prófstærðin fellur ekki á höfnunarsvæðið.
    
    #) Við getum ekki hafnað núlltilgátunni og getum því ekki ályktað að
       dreifnin sé hærri en 10 ml\ :math:`^2`.
    
    .. figure:: myndir/chisq29_tvihlida.svg
        :align: center
        :alt: Mynd

.. _ss.alyktanirumdreifnitveggjathyda:

Ályktanir um dreifni tveggja þýða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tilgátuprófin sem við skoðum í þessum hluta eru notuð til að bera saman
dreifni tveggja þýða sem fylgja normaldreifingu . Próf af þessu tagi eru
meðal annars oft gerð áður en tilgátupróf fyrir mismun meðaltals tveggja
þýða er framkvæmt. Þegar reikna á öryggisbil og prófa tilgátur um
dreifni tveggja þýðis er notast við :math:`F`-dreifinguna, sjá kafla
:numref:`%s <ss.fdreifing>`.

Núlltilgátan lýsir hlutlausu ástandi, þ.e. að dreifni þýðanna tveggja sé
jöfn, ritað :math:`H_0: \sigma_1^2 = \sigma_2^2`.

.. _k.dreifnitveggjathyda:

Tilgátupróf fyrir dreifni tveggja normaldreifðra þýða
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Núlltilgátan er:
    
    .. math:: H_0: \sigma_1^2 = \sigma_2^2
    
    Gagntilgátan getur verið einhliða eða tvíhliða og er prófstærðin
    mismunandi eftir því hvernig gagntilgátan er sett upp. Mögulegar
    gagntilgátur, prófstærðir og höfnunarsvæði þeirra má sjá hér að neðan.
    
    +-------------------------------------------+-----------------------------------+------------------------------------------+
    | Gagntilgáta                               | Prófstærð                         | Hafna :math:`H_0` ef:                    |
    +===========================================+===================================+==========================================+
    | :math:`H_1: \sigma_1^2 < \sigma_2^2`      | :math:`F = \frac{S_2^2}{S_1^2}`   | :math:`F>F_{1-\alpha,(n_2-1,n_1-1)}`     |
    +-------------------------------------------+-----------------------------------+------------------------------------------+
    | :math:`H_1: \sigma_1^2 > \sigma_2^2`      | :math:`F = \frac{S_1^2}{S_2^2}`   | :math:`F>F_{1-\alpha,(n_1-1,n_2-1)}`     |
    +-------------------------------------------+-----------------------------------+------------------------------------------+
    | :math:`H_1: \sigma_1^2 \neq \sigma_2^2`   | :math:`F = \frac{S_M^2}{S_m^2}`   | :math:`F>F_{1-\alpha/2,(n_M-1,n_m-1)}`   |
    +-------------------------------------------+-----------------------------------+------------------------------------------+
    
    Í tvíhliða prófinu skal ávallt velja úrtakið með hærri dreifni sem úrtak
    :math:`M` og úrtakið með lægri dreifni sem úrtak :math:`m`.


--------------

.. _e.alyktanirumdreifni1:

Sýnidæmi: Ályktanir um dreifni tveggja normaldreifðra þýða
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Ingunn og Árni vinna á Jafnréttisstofu og hafa þau mikinn áhuga á
    rannsaka laun karla og kvenna sem starfa við kjötvinnslu.
    Jafnréttisstofa stóð því fyrir rannsókn til að kanna hvort munur sé á
    meðallaunum karla og kvenna. Slembiúrtök voru því tekin úr báðum þýðum,
    20 karlar og 20 konur. Meðaltal og staðalfrávik launa í karla úrtakinu
    voru 245163 kr og 22814. Í konu úrtakinu voru meðaltal og staðalfrávik
    218634 og 18312. Gerið ráð fyrir að launin fylgi normaldreifingu.
    
    Kannið með viðeigandi tilgátuprófi hvort dreifni þýðanna sé misjöfn.
    Notið :math:`\alpha = 0.05`.
    
    Förum eftir samantektinni um framkvæmd tilgátuprófa.
    
    #) Við ætlum að kanna tilgátu um dreifni tveggja normaldreifðra þýða.
    
    #) Við fengum uppgefið að nota :math:`\alpha = 0.05.`
    
    #) Við ætlum að kanna hvort dreifni þýðanna er mismunandi og notum við
       því tvíhliða próf.
    
       Tilgáturnar eru:
    
       .. math::
          \begin{aligned}
          H_0&:& \sigma_1^2 = \sigma_2^2\\
          H_1&:& \sigma_1^2 \neq \sigma_2^2\end{aligned}
    
    #) Prófstærðin er:
    
       .. math:: F = \frac{S_M^2}{S_m^2}
    
       Þar sem staðalfrávik í karla úrtakinu er hærra köllum við karla
       hópinn hóp :math:`M` og kvenna hópinn hóp :math:`m`. Setjum nú inn í
       prófstærðina og fáum
    
       .. math:: f = \frac{22814^2}{18312^2} = 1.55
    
    #) Við þurfum að finna höfnunarsvæðið og notum til þess :math:`F`-töflu.
       :math:`F_{1-\alpha/2,(n_M-1,n_m-1)} = F_{0.975,(19,19)}`. Sé F-taflan
       í kafla :ref:`T.6 <a.ftafla25>` skoðuð má sjá að þar er ekki að finna
       gildi fyrir :math:`F_{0.975,(19,19)}` og notum við því það sem er
       næst, :math:`F_{0.975,(20,19)} = 2.506`, svo við höfnum
       núlltilgátunni ef :math:`f > 2.506`. Við sjáum að :math:`f < 2.506`
       svo prófstærðin fellur ekki á höfnunarsvæðið.
    
    #) Við getum ekki hafnað núlltilgátunni og getum því ekki ályktað að
       dreifnin sé mismunandi.
    
    .. figure:: myndir/f2019.svg
        :align: center
        :alt: Mynd

.. _s.alyktanirummedaltol:

Ályktanir um meðaltöl
---------------------

Það er óhætt að segja að ályktanir um meðaltöl séu einna algengasta
ályktunartölfræði sem beitt er. Í þessum hluta skoðum við tilgátupróf og
öryggisbil sem eiga við þegar draga á ályktun um meðaltöl þýða, sem við
táknum :math:`\mu`. Í kafla :numref:`%s <ss.alyktanirummedaltal>` skoðum við
ályktanir um meðaltal í *einu þýð*\ i. Í kafla
:numref:`%s <ss.alyktanirummedaltoltveggja>` skoðum svo tilgátupróf sem notað er
til að kanna hvort meðaltöl *tveggja óháðra þýða*, :math:`\mu_1` og
:math:`\mu_2`, séu ólík og að lokum er fjallað um tilgátupróf fyrir
*paraðar mælingar* í hluta :numref:`%s <s.paradarmaelingar>`.

Það fer eftir aðstæðum hvers kyns tilgátupróf og öryggisbil við reiknum
þegar draga á ályktanir um meðaltöl þýðis. Í þessum kafla munum við
fjalla um z-próf/öryggisbil annars vegar og t-próf/öryggisbil hins
vegar. Almennt byrjum við á að skoða hvenær z-próf/öryggisbil eiga við
og í framhaldinu könnum við hvenær er viðeigandi að nota
t-próf/öryggisbil. Við munum sjá að t-próf hafa ætíð minni líkur á villu
af gerð I heldur en z-próf og þar af leiðandi er algengara að notast við
t-próf þegar unnið er í tölfræðihugbúnaði. Z-próf er hins vegar
auðveldara að reikna í höndunum.

Við viljum benda á að aðferðirnar í þessum kafla eiga ekki við ef hvort
tveggja gildir í senn: að úrtökin sem við byggjum ályktarnir okkar á eru
lítil og að ekki er hægt að gera ráð fyrir að þýðin fylgi
normaldreifingu. Í þeim tilvikum er stundum hægt að *umbreyta* (e.
transform) gögnunum, nota *endurvalsaðferðir* (e. resampling methods)
eða nota *stikalaus próf* (e. nonparametric tests) en ekki verður farið
nánar í það hér.

.. _ss.alyktanirummedaltal:

Ályktanir um meðaltal þýðis
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við byrjum á því að fjalla um tilgátupróf og öryggisbil fyrir meðaltal
þýðis, :math:`\mu`. Þessar aðferðir notum við ef við viljum til dæmis
sýna fram á að meðalvirkni lyfs sé meiri en eitthvað ákveðið
viðmiðunargildi eða að meðalfjöldi gistinátta í júlí síðustu tíu ár sé
frábrugðinn einhverju ákveðnu gildi.

Núlltilgátan er ávalt sú sama, hvort meðaltal þýðisins sé jafnt
einhverju ákveðnu gildi sem við köllum :math:`\mu_0`. Núlltilgátuna
ritum við :math:`H_0: \mu = \mu_0`.

Z-próf og öryggisbil
^^^^^^^^^^^^^^^^^^^^

Ein ástæða þess hve meðaltöl eru mikið notuð til að lýsa samfelldum
breytum er normaldreifingin. Við sáum í kafla
:numref:`%s <s.lysistaerdinmedaltal>` að þegar þýðið sem verið er að kanna
fylgir normaldreifingu mun úrtaksdreifing meðaltalsins fylgja
normaldreifingu sama hversu lítið úrtakið er. Jafnframt sagði
*Höfuðsetning tölfræðinnar* okkur, í kafla
:numref:`%s <s.hofudsetningtolfraedinnar>`, að ef úrtakið er stórt má nálga
úrtaksdreifingu meðaltalsins með normaldreifingu. Við miðum oft við
þumalputtaregluna að úrtakið þurfi að vera stærra en 30 til að svo
gildi.

Í kafla :numref:`%s <s.hofudsetningtolfraedinnar>` sáum við líka að í þessum
ofangreindu tilvikum er dreifni úrtaksdreifingar meðaltalsins
:math:`\sigma^2/n`, þar sem :math:`\sigma^2` er dreifni þýðisins, en
:math:`n` fjöldi mælinga. Ef að dreifni þýðisins, væri þekkt gætum við
þannig reiknað öryggisbil á svipstundu með því að margfalda
:math:`\sigma^2/n` með :math:`z_{1-\alpha/2}` og draga frá eða bæta við
reiknaða meðaltalið. Sú aðferð er sýnd í kassa
:numref:`%s <em.zobileittmedaltal>`. Á sambærilegan hátt er hægt að framkvæma
tilgátupróf og er það sýnt í kafla :numref:`%s <em.zprofeittmedaltal>`.

Í reynd þekkjum við yfirleitt aðeins dreifni úrtaksins, :math:`s^2`, sem
við reiknum út frá gögnunum okkar, en ekki dreifni alls þýðisins. Í þeim
tilvikum sem úrtaksstærðin er stór (:math:`n` > 30) veitir dreifni
úrtaksins þó góða nálgun á dreifni þýðisins og megum við því einnig nota
z-próf og öryggisbil í því tilviki. Til að draga þetta saman megum við
framkvæma :math:`z`-próf til að draga ályktanir um meðaltöl þegar:

-  Þýðið fylgir normaldreifingu og við gerum ráð fyrir að við þekkjum
   dreifni þess.

-  Úrtakið er stórt.

Í þessum tilvikum má nota eftirfarandi öryggisbil fyrir hið óþekkta
meðaltal þýðisins:

.. _em.zobileittmedaltal:

Z - öryggisbil fyrir :math:`\mu`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Neðra mark :math:`1 - \alpha` öryggisbils er:
    
    .. math::
       \bar{x} - z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}
       :label: eq.mut1nedra
    
    Efra mark :math:`1 - \alpha` öryggisbils er:
    
    .. math::
       \bar{x} + z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}
       :label: eq.mut1efra
    
    Öryggisbilið má því skrifa:
    
    .. math::
       \bar{x} - z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}} <  \mu  < \bar{x} + z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}
       :label: eq.mut1bil
    
    þar sem :math:`\bar{x}` er meðaltal úrtaksins og :math:`\sigma` er
    staðalfrávik þýðisins. :math:`z_{1-\alpha/2}` gildið má finna í töflu
    stöðluðu normaldreifingarinnar í kafla :ref:`T.1 <a.normaltafla>`.


--------------

Eins og fram kom hér að ofan veitir dreifni úrtaksins góða nálgun á
dreifni þýðisins þegar úrtakið er stórt. Þegar :math:`n` er stórt má því
skipta :math:`\sigma` út fyrir :math:`s` í formúlunum hér að ofan.
Samsvarandi tilgátupróf má framkvæma með:

.. _em.zprofeittmedaltal:

Z-próf fyrir :math:`\mu`
^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Núlltilgátan er:
    
    .. math:: H_0: \mu = \mu_0
    
    Prófstærðin er:
    
    .. math::
       Z = \frac{\overline{X}-\mu_0}{\sigma/\sqrt{n}}
       :label: eq.mut1profstaerd
    
    Ef núlltilgátan er sönn fylgir prófstærðin stöðluðu normaldreifingunni,
    eða :math:`Z \sim N(0,1)`.
    
    Höfnunarsvæðin eru:
    
    +-------------------------------+--------------------------------------------------------------+
    | Gagntilgáta                   | Hafna :math:`H_0` ef:                                        |
    +===============================+==============================================================+
    | :math:`H_1: \mu < \mu_0`      | :math:`Z < -z_{1-\alpha}`                                    |
    +-------------------------------+--------------------------------------------------------------+
    | :math:`H_1: \mu > \mu_0`      | :math:`Z > z_{1-\alpha}`                                     |
    +-------------------------------+--------------------------------------------------------------+
    | :math:`H_1: \mu \neq \mu_0`   | :math:`Z < -z_{1-\alpha/2}` eða :math:`Z > z_{1-\alpha/2}`   |
    +-------------------------------+--------------------------------------------------------------+


--------------

Að sama skapi og hér að ofan má skipta :math:`\sigma` út fyrir :math:`s`
þegar :math:`n` er stórt.

Sýnidæmi: Ályktanir um meðaltal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Jón rekur fiskvinnslu á Bíldudal sem verkar þorsk til sölu á
    Bretlandseyjum. Þorskurinn er sendur út í um 50 kg. pakkningum. Þar á bæ
    hafa menn fylgst grannt með þyngd pakkanna og komist að því að þyngd
    þeirra fylgir normaldreifingu með :math:`\sigma^2` = 0.8 kg. Við höfum
    nú áhuga á að draga ályktanir um :math:`\mu`. Til þess er tekið
    slembiúrtak af stærð :math:`n = 12` og meðalþyngd úrtaksins reiknuð,
    50.84 kg. Finnið 95% öryggisbil fyrir :math:`\mu` og kannið hvort
    meðalþyngd pakkanna sé frábrugðin 50 kg. Notið :math:`\alpha = 0.05`.
    
    Fengum upp gefið að:
    :math:`\bar{x} = 50.84, \ n = 12, \ \sigma^2 = 0.8`. Neðri mörk
    öryggisbilsins reiknum við með jöfnu :eq:`eq.mut1nedra`. Við þurfum að
    því að byrja á að finna :math:`z_{1-\alpha/2}`.
    :math:`z_{1-\alpha/2}= z_{1-0.05/2} = z_{0.975} = 1.96`.
    
    .. math::
       \bar{x} - z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}} = 50.84 - 1.96 \cdot \frac{\sqrt{0.8}}{\sqrt{12}}
       = 50.84 - 0.506 = 50.33
    
    og efri mörk öryggisbilsins með jöfnu :eq:`eq.mut1efra`
    
    .. math:: \bar{x} + z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}} = 50.84 + 0.506 = 51.35
    
    Öryggisbilið má þá skrifa sem
    
    .. math:: 50.33 < \mu < 51.35
    
    Til að kanna hvort meðalþyngd pakkanna sé frábrugðin 50 kg. förum við
    eftir samantektinni um framkvæmd tilgátuprófa.
    
    #) Við ætlum að álykta um :math:`\mu` og notum því próf fyrir meðaltal
       þýðis. Gefið er upp að þýðið fylgi normaldreifingu með þekktri
       dreifni og getum við því notað z-próf.
    
    #) Við fengum uppgefið að nota :math:`\alpha = 0.05.`
    
    #) Við eigum að kanna hvort meðalþyngd pakkanna sé **frábrugðin** 50 kg.
       Það gerum við með tvíhliða prófi. Tilgáturnar eru:
    
       .. math::
          \begin{aligned}
          H_0&:& \mu = 50\\
          H_1&:& \mu \neq 50\end{aligned}
    
    #) Fengum upp gefið að:
       :math:`\bar{x} = 50.84, \ n = 12, \ \sigma^2 = 0.8`. Prófstærðina
       reiknum við með jöfnu :eq:`eq.mut1profstaerd` og fáum
    
       .. math:: z = \frac{\overline{x}-\mu_0}{\sigma/\sqrt{n}} = \frac{50.84 - 50} {\sqrt{0.8}/\sqrt{12}} = 3.25
    
    #) Við notum töflu stöðluðu normaldreifingarinnar til að finna
       höfnunarsvæðin og fáum :math:`z_{1-\alpha/2}` = :math:`z_{0.975}` =
       1.96. Við höfnum því núlltilgátunni ef :math:`z< -1.96` eða
       :math:`z> 1.96`. Við sjáum að :math:`z> 1.96` svo prófstærðin fellur
       á höfnunarsvæði.
    
    #) Við höfnum núlltilgátunni og ályktum að meðalþyngd kassanna sé
       frábrugðin 50 kg.
    
    .. figure:: myndir/z196th.svg

Sýnidæmi: Ályktanir um :math:`\mu`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Gúgú er forstjóri í stóru fyrirtæki sem framleiðir bíla. Hún fullyrðir
    að bílategund nokkur geti keyrt að meðaltali 20 km. á lítra. Allmargar
    kvartanir hafa borist til Ingibjargar, formanns Neytendasamtakanna,
    vegna þessarar fullyrðingar og vill fólk meina að það nái alls ekki að
    keyra 20 km. á lítra. Neytendasamtökin framkvæmdu því tilraun til að
    sýna fram á að meðalfjöldi kílómetra á lítra væru færri en 20.
    Slembiúrtak af stærð 40 var tekið og meðaltal þess reiknað sem 19.2 og
    staðalfrávik úrtaksins reiknað sem 1.7. Notið viðeigandi tilgátupróf til
    að kanna hvort meðalfjöldi kílómetra á lítra séu færri en 20 með því að
    kanna hvort prófstærðin falli á höfnunarsvæði en einnig með að kanna
    p-gildi tilgátuprófsins. Notið :math:`\alpha = 0.05`.
    
    Förum eftir samantektinni um framkvæmd tilgátuprófa.
    
    1. Við ætlum að álykta um :math:`\mu` og notum því próf fyrir meðaltal
       þýðis. Við þekkjum hvorki líkindadreifingu né dreifni þýðisins en
       úrtakið er stórt svo við getum notað z-próf.
    
    #. Við fengum uppgefið að nota :math:`\alpha = 0.05.`
    
    3. Við eigum að kanna hvort meðalkílómetra fjöldi sé færri en 20 km en
       þar sem að fjöldinn getur í raun verið hærri en 20 km notum við tvíhliða
       próf. Tilgáturnar eru:
    
       .. math::
          \begin{aligned}
          H_0&:& \mu = 20\\
          H_1&:& \mu \neq 20\end{aligned}
    
    4. Við fengum upp gefið að :math:`\bar{x} = 19.2, \ s = 1.7, \ n = 40`.
       Við reiknum prófstærðina með jöfnu :eq:`eq.mut1profstaerd` en skiptum
       :math:`\sigma` út fyrir :math:`s`:
       
       .. math:: z = \frac{\overline{x}-\mu_0}{s/\sqrt{n}} = \frac{19.2 - 20}{1.7/\sqrt{40}} = -2.98
    
    5a. Við notum töflu stöðluðu normaldreifingarinnar til að finna höfnunarsvæðið:

        :math:`z_{1-\alpha/2}` = :math:`z_{0.975}` = 1.96. Við
        höfnum því núlltilgátunni ef :math:`z< -1.96` eða :math:`z> 1.96`. Við
        sjáum að :math:`z < -1.96` svo prófstærðin fellur á höfnunarsvæði.
    
    5b. Við notum töflu stöðluðu normaldreifingarinnar til að finna p-gildið.

        Gildið á prófstærðinni er -2.98 svo við finnum z= -2.98 í
        töflunni og lesum 0.0014. Þar sem tilgátuprófið er tvíhliða margföldum
        við p-gildið með 2 og fáum að p-gildið er 0.0028. Þar sem p-gildið er
        minna en :math:`\alpha` höfnum við núlltilgátunni.
    
    6. Við höfnum núlltilgátunni og ályktum að meðalfjöldi kílómetra er
       lægri en 20 á lítrann.
    
       .. figure:: myndir/z196th.svg

T-próf og öryggisbil
^^^^^^^^^^^^^^^^^^^^

Rifjum nú aftur upp að þegar við vinnum með normaldreift þýði, þá fylgir
úrtaksdreifing meðaltalsins alltaf normaldreifingu, sama hversu lítið
úrtakið er. Hins vegar er eitt vandamál við að framkvæma z-próf í því
tilviki, nefnilega það að matið á staðalfrávikinu verður ekki lengur
eins áreiðanlegt og því þurfum við að taka tillit til óvissunnar í því
mati.

Þegar þýðið fylgir normaldreifingu og við deilum í úrtaksdreifingu
meðaltalsins með :math:`s/\sqrt{n}` fylgir útkoman þekktri
líkindadreifingu, nefnilega *t-dreifingu* (sjá kafla
:numref:`%s <ss.tdreifing>`). T-dreifingin hefur mjög svipaða lögun og
normaldreifingin en hefur örlítið *þyngri hala* (meiri líkur á að fá
mjög stór eða mjög lítil gildi). Því eru minni líkur á villu af gerð I
þegar t-próf, í stað z-prófs, er framkvæmt á sömu gögnunum. Því er ætíð
óhætt að nota t-próf þegar z-próf á líka við og þar af leiðandi er
t-próf útfært í öllum helstu tölfræðihugbúnuðum en z-próf síður.

Til að draga saman, megum við nota t-próf og öryggisbil byggð á
t-dreifingu þegar:

-  Þýðið fylgir normaldreifingu, óháð stærð úrtaksins.

-  Úrtakið er stórt.

Í þessum tilvikum má notast við eftirfarandi öryggisbil:

T-öryggisbil fyrir :math:`\mu`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Neðra mark :math:`1 - \alpha` öryggisbils:
    
    .. math::
       \bar{x} - t_{1-\alpha/2,(n-1)} \cdot \frac{s}{\sqrt{n}}
       :label: eq.mut3nedra
    
    Efra mark :math:`1 - \alpha` öryggisbils:
    
    .. math::
       \bar{x} + t_{1-\alpha/2,(n-1)} \cdot \frac{s}{\sqrt{n}}
       :label: eq.mut3efra
    
    Öryggisbilið má því skrifa:
    
    .. math::
       \bar{x} - t_{1-\alpha/2,(n-1)} \cdot \frac{s}{\sqrt{n}} <  \mu  < \bar{x} + t_{1-\alpha/2,(n-1)} \cdot \frac{s}{\sqrt{n}}
       :label: eq.mut3bil
    
    þar sem :math:`\bar{x}` og :math:`s` eru meðaltal og staðalfrávik
    úrtaksins. :math:`t_{1-\alpha/2,(n-1)}` gildið má finna í t-töflu í kafla :ref:`T.2 <a.ttafla>`.


--------------

og eftirfarandi tilgátupróf:

T-próf fyrir :math:`\mu`
^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Núlltilgátan er:
    
    .. math:: H_0: \mu = \mu_0
    
    Prófstærðin er:
    
    .. math::
       T = \frac{\overline{X}-\mu_0}{S/\sqrt{n}}
       :label: eq.mut3profstaed
    
    Ef núlltilgátan er sönn fylgir prófstærðin t-dreifingu með :math:`(n-1)`
    frígráðu, eða :math:`T \sim t_{(n-1)}`.
    
    Höfnunarsvæðin eru:
    
    +-------------------------------+--------------------------------------------------------------------------+
    | Gagntilgáta                   | Hafna :math:`H_0` ef:                                                    |
    +===============================+==========================================================================+
    | :math:`H_1: \mu < \mu_0`      | :math:`T < -t_{1-\alpha,(n-1)}`                                          |
    +-------------------------------+--------------------------------------------------------------------------+
    | :math:`H_1: \mu > \mu_0`      | :math:`T > t_{1-\alpha,(n-1)}`                                           |
    +-------------------------------+--------------------------------------------------------------------------+
    | :math:`H_1: \mu \neq \mu_0`   | :math:`T < -t_{1-\alpha/2,(n-1)}` eða :math:`T > t_{1-\alpha/2,(n-1)}`   |
    +-------------------------------+--------------------------------------------------------------------------+


--------------

Sýnidæmi: Ályktanir fyrir :math:`\mu`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Sígarettuframleiðandi nokkur fullyrðir að nikótíninnihald í ákveðinni
    tegund af sígarettum sé að meðaltali 14 mg/sígarettu.
    Heilbrigðisyfirvöld í viðkomandi landi héldu því fram að
    nikótíninnihaldið væri að meðaltali hærra. Þau stóðu því fyrir tilraun
    til að sýna fram á að meðalinnihald nikótíns væri hærra en 14
    mg/sígarettu. Slembiúrtak af stærð 12 var tekið og meðaltal úrtaksins
    reiknað sem 14.3 og staðalfrávik þess 0.9. Kannið með viðeigandi
    tilgátuprófi hvort meðalinnihald nikótíns sé hærra en 14 mg/sígarettu.
    Notið :math:`\alpha = 0.05`. Gera má ráð fyrir að nikótíninnihald í
    sígarettum fylgi normaldreifingu.
    
    Förum nú eftir samantektinni um framkvæmd tilgátuprófa.
    
    #) Við ætlum að álykta um :math:`\mu` og notum því próf fyrir meðaltal
       þýðis. :math:`\sigma^2` er óþekkt og :math:`n` er lítið en þar sem
       við getum gert ráð fyrir að þýðið sem úrtakið er tekið úr fylgi
       normaldreifingu getum við notað t-próf.
    
    #) Við fengum uppgefið að nota :math:`\alpha = 0.05.`
    
    #) Við eigum að kanna hvort meðalinnihald nikótíns sé hærra en 14
       mg/sígarettu en þar sem það getur í raun verið lægra notum við
       tvíhliða próf. Tilgáturnar eru:
    
       .. math::
          \begin{aligned}
          H_0&:& \mu = 14\\
          H_1&:& \mu \neq 14\end{aligned}
    
    #) Við fáum upp gefið: :math:`n = 12, \ \bar{x} = 14.3, \ s = 0.9`. Við
       reiknum prófstærðina með jöfnu :eq:`eq.mut3profstaed` og fáum
    
       .. math:: t = \frac{\overline{x}-\mu_0}{s/\sqrt{n}} = \frac{14.3 - 14}{0.9/\sqrt{12}} = 1.15
    
    #) Við notum t-töfluna til að finna höfnunarsvæðið og flettum upp eftir
       :math:`n - 1 = 11` frígráðum:
       :math:`t_{1-\alpha/2,(n-1)} = t_{0.975,(11)}` = 2.20. Við höfnum því
       núlltilgátunni ef :math:`t < -2.20` eða :math:`t > 2.20`. Við sjáum
       að prófstærðin fellur ekki á höfnunarsvæði.
    
    #) Við getum ekki hafnað núlltilgátunni og getum því ekki ályktað að
       meðalnikótíninnihaldið sé hærra en 14 mg/sígarettu.
    
    .. figure:: myndir/t11_tvihlida.svg

.. _ss.alyktanirummedaltoltveggja:

Ályktanir um meðaltöl tveggja óháðra þýða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú er komið að því að fjalla um tilgátupróf og öryggisbil sem eiga við
þegar bera á saman meðaltöl tveggja óháðra þýða. Við köllum meðaltölin
:math:`\mu_1` og :math:`\mu_2` og viljum draga ályktanir um mismun
þeirra, :math:`\mu_1 - \mu_2`. Próf af þessu tagi mundum við nota ef við
viljum t.d. bera saman meðalhæð karla og kvenna og ef við viljum bera
saman meðalfjölda gistinátta í júlí og ágúst.

Í þessum hluta er núlltilgátan ávallt sú sama, þ.e. hvort mismunur
meðaltalanna tveggja sé jafn einhverju ákveðnu gildi sem við köllum
:math:`\delta`. Hana ritum við :math:`H_0: \mu_1 - \mu_2 = \delta`.
Takið eftir að :math:`\delta` er gríski bókstafurinn sem svarar til
latneska bókstafsins d samanber enska orðið difference. Það er í samræmi
við notkun okkar, við viljum yfirleitt sýna að munurinn á meðaltölum
hópanna tveggja sé frábrugðinn :math:`\delta`. Algengast er að nota
:math:`\delta = 0` en þá viljum við einfaldlega sýna að það sé munur á
milli hópanna. Núlltilgátan er þá eftirfarandi: ,,Eru meðaltöl þýðanna
tveggja jöfn?“

Líkt og þegar við viljum draga ályktanir um eitt meðaltal geta aðstæður
verið mismunandi. Við munum eins og áður notast við z-próf/öryggisbil og
t-próf/öryggisbil og má sjá hér að neðan hvenær þau eiga við.

Z-próf og öryggisbil
^^^^^^^^^^^^^^^^^^^^

Svipað og við lýstum í kafla :numref:`%s <ss.alyktanirummedaltal>` er mismunur
tveggja meðaltala normaldreifður ef þýðið sem hvort meðaltal fyrir sig
er fengið úr er einnig normaldreift. Sömuleiðis leiðir Höfuðsetning
tölfræðinnar af sér að það sama gildir ef að úrtakið er nógu stórt.

Ef að við vissum hver dreifni þýðanna væri, gætum deilt í mismun
meðaltalanna með dreifni hans til að fá út staðlaða normaldreifða stærð.
Í þessu tilviki er dreifni mismunarins stærðin
:math:`\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}`. Einnig
gildir að ef úrtökin eru nægjanlega stór veitir dreifni úrtakanna það
gott mat á dreifni þýðanna að hana má nota í staðinn. Hér er oft miðað
við að hvort úrtak þurfi að vera að minnsta kosti af stærð 30 til að
nægjanlegur fjöldi sé fyrir hendi.

Þar af leiðandi er í textanum gert ráð fyrir að dreifni þýðanna, þ.e.
:math:`\sigma^2_1` og :math:`\sigma^2_2`, sé þekkt, þó svo að sú sé
sjaldnast ekki raunin. Við þekkjum yfirleitt aðeins dreifni úrtakanna,
:math:`s^2_1` og :math:`s^2_2`, sem við reiknum út frá gögnunum okkar.
Til að draga þetta saman megum við nota z-próf og öryggisbil byggð á
normaldreifingu þegar:

-  Þýðin fylgja normaldreifingu og við gerum ráð fyrir að við þekkjum
   dreifni þýðanna.

-  Úrtökin eru stór.

Í þessum tilvikum má nota eftirfarandi öryggisbil fyrir mismun meðaltala
þýðanna:

Z-öryggisbil fyrir mismun tveggja meðaltala
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Neðra mark :math:`1 - \alpha` öryggisbils er:
    
    .. math::
       \bar{x}_1 - \bar{x}_2 - z_{1-\alpha/2} \cdot \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}
       :label: eq.tvomut1nedra
    
    Efra mark :math:`1 - \alpha` öryggisbils er:
    
    .. math::
       \bar{x}_1 - \bar{x}_2 + z_{1-\alpha/2} \cdot \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}
       :label: eq.tvomut1efra
    
    Öryggisbilið má því skrifa:
    
    .. math::
       \bar{x}_1 - \bar{x}_2 - z_{1-\alpha/2} \cdot \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}
       < \mu_1 - \mu_2  <
       \bar{x}_1 - \bar{x}_2 + z_{1-\alpha/2} \cdot \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}
       :label: eq.tvomut1bil
    
    þar sem :math:`\bar{x}_1`, :math:`\bar{x}_2` eru meðaltöl úrtakanna og
    :math:`\sigma_1^2`, :math:`\sigma_2^2` eru dreifni þýðanna.
    :math:`z_{1-\alpha/2}` má finna í töflu stöðluðu normaldreifingarinnar í
    kafla :ref:`T.1 <a.normaltafla>`.


--------------

Eins og fram kom hér að ofan veitir dreifni úrtaks góða nálgun á dreifni
þýðisins þegar úrtakið er stórt. Þegar :math:`n_1` og :math:`n_2` eru
stór má því skipta :math:`\sigma_1` og :math:`\sigma_2` út fyrir
:math:`s_1` og :math:`s_2` í formúlunum hér að ofan. Þegar framkvæma á
samsvarandi tilgátupróf má notast við eftirfarandi:

Z-próf fyrir mismun tveggja meðaltala
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Núlltilgátan er:
    
    .. math:: H_0: \mu_1 - \mu_2 = \delta
    
    Prófstærðin er:
    
    .. math::
       Z = \frac{\overline{X}_1 - \overline{X}_2 - \delta}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}
       :label: eq.tvomut1prof
    
    Ef núlltilgátan er sönn fylgir prófstærðin stöðluðu normaldreifingunni,
    eða :math:`Z \sim N(0,1)`.
    
    +------------------------------------------+--------------------------------------------------------------+
    | Gagntilgáta                              | Hafna :math:`H_0` ef:                                        |
    +==========================================+==============================================================+
    | :math:`H_1: \mu_1 - \mu_2 < \delta`      | :math:`Z < -z_{1-\alpha}`                                    |
    +------------------------------------------+--------------------------------------------------------------+
    | :math:`H_1: \mu_1 - \mu_2 > \delta`      | :math:`Z > z_{1-\alpha}`                                     |
    +------------------------------------------+--------------------------------------------------------------+
    | :math:`H_1: \mu_1 - \mu_2 \neq \delta`   | :math:`Z < -z_{1-\alpha/2}` eða :math:`Z > z_{1-\alpha/2}`   |
    +------------------------------------------+--------------------------------------------------------------+
    
    Athugið að :math:`\delta` getur verið hvaða tala sem er en í mörgum
    tilvikum er :math:`\delta = 0`.


--------------

Eins og áður má skipta skipta :math:`\sigma_1` og :math:`\sigma_2` út
fyrir :math:`s_1` og :math:`s_2` þegar :math:`n_1` og :math:`n_2` eru
stór.

Sýnidæmi: :math:`\mu_1 - \mu_2`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Hænsnabóndi nokkur hefur fylgst vel með þyngd unga við fæðingu.
    Hænsnabóndi þessi hefur áhuga á að kanna hvort munur sé á þyngd unganna
    eftir kyni og til að rannsaka það valdi hann 35 karlkyns unga og 35
    kvenkyns unga og vigtaði þá. Kvenkyns ungarnir vógu að meðaltali 212
    grömm og var staðalfrávikið 21 grömm. Karlkyns ungarnir vógu að
    meðaltali 220 grömm og var staðalfrávikið 26 grömm. Kannið með
    viðeigandi tilgátuprófi hvort munur sé á þyngd unganna eftir kyni.
    
    Förum nú eftir samantektinni um framkvæmd tilgátuprófa.
    
    #) Við ætlum að álykta um mun á meðaltölum tveggja þýða. Úrtökin eru
       **óháð**. Ekki er tekið fram að gera megi ráð fyrir að þyngdin fylgi
       normaldreifingu, við þekkjum ekki dreifni þýðanna en :math:`n`-in
       okkar eru stór og því megum við nota z-próf.
    
    #) Notum :math:`\alpha = 0.05.`
    
    #) Við ætlum að kanna hvort **munur** sé á meðalþyngd unga eftir kyni og
       notum við til þess tvíhliða próf. Tilgáturnar eru:
    
       .. math::
          \begin{aligned}
          H_0&:& \mu_1 - \mu_2 = 0\\
          H_1&:& \mu_1 - \mu_2 \neq 0\end{aligned}
    
    #) Prófstærðina reiknum við með jöfnu :eq:`eq.tvomut1prof` en skiptum út
       :math:`\sigma_1` og :math:`\sigma_2` með :math:`s_1` og :math:`s_2`:
    
       .. math:: z = \frac{\overline{x}_1 - \overline{x}_2 - \delta}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}
    
       Við vitum að :math:`n_1 = 35`, :math:`n_2 = 35`, :math:`\bar{x}_1` =
       220, :math:`s_1` = 26, :math:`\bar{x}_2` = 212, :math:`s_2` = 21 og
       :math:`\delta` = 0 (við látum karlkyns ungana vera þýði 1 og kvenkyns
       ungana vera þýði 2). Við setjum þessar tölur inn í jöfnuna og fáum
    
       .. math:: z = \frac{220 - 212 - 0}{\sqrt{\frac{26^2}{35} + \frac{21^2}{35}}} = 1.42
    
    #) Við þurfum að finna höfnunarsvæðið og notum til þess z-töflu. Sé
       núlltilgátan sönn fylgir prófstærðin stöðluðu normaldreifingunni:
       :math:`z_{1-\alpha/2,} = z_{0.975}` = 1.96, svo við höfnum
       núlltilgátunni ef :math:`z > 1.96` eða :math:`z < -1.96`. Við sjáum
       að hvorugt gildir svo prófstærðin fellur ekki á höfnunarsvæði.
    
    #) Við getum ekki hafnað núlltilgátunni svo við drögum enga ályktun.

T-próf og öryggisbil
^^^^^^^^^^^^^^^^^^^^

Á sama hátt og við lýstum í kafla :numref:`%s <ss.alyktanirummedaltal>` er
mismunur tveggja meðaltala normaldreifður ef þýðið sem hvort meðaltal
fyrir sig er fengið úr er einnig normaldreift. Við getum skalað
mismuninn til með því að deila með dreifninni á úrtaksdreifingu mismuns
meðaltalanna og þá fylgir útkoman *t-dreifingu* (sjá kafla
:numref:`%s <ss.tdreifing>`), alveg eins og í tilvikinu með eitt meðaltal. Þar
sem t-dreifing hefur þyngri hala en normaldreifing er ætíð óhætt að nota
t-próf þegar z-próf á líka við og þar af leiðandi er t-próf útfært í
öllum helstu tölfræðihugbúnuðum en z-próf síður.

Við megum því nota t-próf og öryggisbil byggð á t-dreifingu þegar:

-  Þýðin fylgja normaldreifingu, óháð stærð úrtakanna.

-  Úrtökin eru stór.

Við notum ólíka formúlu til að meta dreifnina á mismun meðaltal þýðanna
eftir því hvort við megum gera ráð fyrir því að dreifnin sé jöfn í
þýðunum tveimur eða ekki. Þar af leiðandi verða t-prófin og öryggisbilin
sem nota má til að kanna ályktanir um mismun tveggja óháðra þýða tvenns
konar. Annað prófið notum við þegar gera má ráð fyrir að dreifni þýðanna
er jöfn en hitt þegar svo er ekki. Takið efir að hér þekkjum við ekki
dreifni þýðanna en við getum notað tilgátupróf fyrir dreifni tveggja
þýða (sjá kassa :numref:`%s <k.dreifnitveggjathyda>`) til að skera úr um hvort
dreifni þýðanna sé það ólík að ekki sé hægt að gera ráð fyrir að hún sé
sú sama.

Ef gera má ráð fyrir að dreifni þýðanna sé jöfn þurfum við að reikna út
svokallaða *vegna dreifni* (e. pooled variance) úrtakanna sem við táknum
:math:`s_p^2` áður en við getum reiknað öryggisbil og kannað tilgátur:

.. math::
   s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}
   :label: eq.vegindreifni

þar sem :math:`s_1^2` og :math:`s_2^2` eru dreifni úrtakanna.
Öryggisbilið má svo smíða með:

T-öryggisbil fyrir mismun meðaltala tveggja þýða - gert er ráð fyrir að dreifnin sé sú sama
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Neðra mark :math:`1 - \alpha` öryggisbils er:
    
    .. math::
       \bar{x}_1 - \bar{x}_2 - t_{1-\alpha/2,(n_1 + n_2 - 2)} \cdot s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}
       :label: eq.tvomut3nedra
    
    Efra mark :math:`1 - \alpha` öryggisbils er:
    
    .. math::
       \bar{x}_1 - \bar{x}_2 + t_{1-\alpha/2,(n_1 + n_2 - 2)} \cdot s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}
       :label: eq.tvomut3efra
    
    þar sem :math:`\bar{x}_1`, :math:`\bar{x}_2` er meðaltöl úrtakanna og
    :math:`s_1^2`, :math:`s_2^2` er dreifni úrtakanna.
    :math:`t_{1-\alpha/2,(n_1 + n_2 - 2)}` má finna í t-töflu í kafla :ref:`T.2 <a.ttafla>`.


--------------

og framkvæma tilgátuprófið með:

T-próf fyrir mismun meðaltala tveggja þýða - gert er ráð fyrir að dreifnin sé sú sama
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Núlltilgátan er:
    
    .. math:: H_0: \mu_1 - \mu_2 = \delta
    
    Prófstærðin er:
    
    .. math::
       T = \frac{\overline{X}_1 - \overline{X}_2 - \delta}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}
       :label: eq.tvomut3profstaerd
    
    þar sem :math:`s_p` er reiknað með jöfnu :eq:`eq.vegindreifni`. Ef
    núlltilgátan er sönn fylgir prófstærðin t dreifingu með
    :math:`(n_1 + n_2 - 2)` frígráður, eða
    :math:`T \sim t_{(n_1 + n_2 -2)}`. Gagntilgáturnar og höfnunarsvæðin
    eru:
    
    +------------------------------------------+----------------------------------------------------------------------------------------------+
    | Gagntilgáta                              | Hafna :math:`H_0` ef:                                                                        |
    +==========================================+==============================================================================================+
    | :math:`H_1: \mu_1 - \mu_2 < \delta`      | :math:`T < -t_{1-\alpha,(n_1 + n_2 - 2)}`                                                    |
    +------------------------------------------+----------------------------------------------------------------------------------------------+
    | :math:`H_1: \mu_1 - \mu_2 > \delta`      | :math:`T > t_{1-\alpha,(n_1 + n_2 - 2)}`                                                     |
    +------------------------------------------+----------------------------------------------------------------------------------------------+
    | :math:`H_1: \mu_1 - \mu_2 \neq \delta`   | :math:`T < -t_{1-\alpha/2,(n_1 + n_2 - 2)}` eða :math:`T > t_{1-\alpha/2,(n_1 + n_2 - 2)}`   |
    +------------------------------------------+----------------------------------------------------------------------------------------------+
    
    Athugið að :math:`\delta` getur verið hvaða fasti sem er en í mörgum
    tilvikum er :math:`\delta = 0`.


--------------

Ef við getum ekki gert ráð fyrir að dreifnin í hópunum sé sú sama notum
við annars konar t-próf og öryggisbil. Við þurfum ekki að byrja á að
reikna út vegna dreifni en fjöldi frígráða í t-dreifingunni sem við
notum er ekki :math:`n_1 + n_2 - 2` eins og áður heldur táknum við þær
með :math:`\nu` og reiknum með

.. math::
   \nu = \frac{\Big(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2} \Big)^2}{\frac{(s_1^2/n_1)^2}{n_1 - 1} +
   \frac{(s_2^2/n_2)^2}{n_2 - 1}}
   :label: eq.fjoldifrigrada

Öryggisbilið má svo smíða með:

T-öryggisbil fyrir mismun meðaltala tveggja þýða - ólík dreifni
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Neðra mark :math:`1 - \alpha` öryggisbils er:
    
    .. math::
       \bar{x}_1 - \bar{x}_2 - t_{1-\alpha/2,(\nu)} \cdot \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}
       :label: eq.tvomut4nedra
    
    Efra mark :math:`1 - \alpha` öryggisbils er:
    
    .. math::
       \bar{x}_1 - \bar{x}_2 + t_{1-\alpha/2,(\nu)} \cdot \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}
       :label: eq.tvomut4efra
    
    Öryggisbilið má því skrifa:
    
    .. math::
       \bar{x}_1 - \bar{x}_2 - t_{1-\alpha/2,(\nu)} \cdot \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}
       < \mu_1 - \mu_2  <
       \bar{x}_1 - \bar{x}_2 + t_{1-\alpha/2,(\nu)} \cdot \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}
       :label: eq.tvomut4bil
    
    þar sem :math:`\bar{x}_1` og :math:`\bar{x}_2` eru meðaltöl úrtakanna og
    :math:`s_1^2` og :math:`s_2^2` eru dreifni úrtakanna.
    :math:`t_{1-\alpha/2,(\nu)}` má finna í t-töflu í kafla :ref:`T.2 <a.ttafla>`.
    Fjöldi frígráða í t-dreifingunum, :math:`\nu` er reiknað með jöfnu :eq:`eq.fjoldifrigrada`.


--------------

og tilgátuprófið má framkvæma með:

T-próf fyrir mismun meðaltala tveggja þýða - ólík dreifni
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Núlltilgátan er:
    
    .. math:: H_0: \mu_1 - \mu_2 = \delta
    
    Prófstærðin er:
    
    .. math::
       T = \frac{\overline{X}_1 - \overline{X}_2 - \delta}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}
       :label: eq.tvomut4profstaerd
    
    Ef núlltilgátan er sönn fylgir prófstærðin t-dreifingu með :math:`\nu`
    frígráðum eða :math:`T \sim t(\nu)` þar sem :math:`\nu` er reiknað með
    jöfnu :eq:`eq.fjoldifrigrada`.
    
    +------------------------------------------+--------------------------------------------------------------------------+
    | Gagntilgáta                              | Hafna :math:`H_0` ef:                                                    |
    +==========================================+==========================================================================+
    | :math:`H_1: \mu_1 - \mu_2 < \delta`      | :math:`T < -t_{1-\alpha,(\nu)}`                                          |
    +------------------------------------------+--------------------------------------------------------------------------+
    | :math:`H_1: \mu_1 - \mu_2 > \delta`      | :math:`T > t_{1-\alpha,(\nu)}`                                           |
    +------------------------------------------+--------------------------------------------------------------------------+
    | :math:`H_1: \mu_1 - \mu_2 \neq \delta`   | :math:`T < -t_{1-\alpha/2,(\nu)}` eða :math:`T > t_{1-\alpha/2,(\nu)}`   |
    +------------------------------------------+--------------------------------------------------------------------------+
    
    Athugið að :math:`\delta` getur verið hvaða fasti sem er en í mörgum
    tilvikum er :math:`\delta = 0`.


--------------

.. _e.alyktanirumtvomedaltol:

Sýnidæmi: Ályktanir um tvö meðaltöl
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Skoðum nú aftur dæmi :numref:`%s <e.alyktanirumdreifni1>`. Þar framkvæmdum við
    tilgátupróf til að kanna hvort dreifni launa milli kynja væri misjöfn.
    Nú vilja Ingunn og Árni kanna hvort munur sé á meðallaunum karla og
    kvenna sem starfa við kjötvinnslu.
    
    Við rifjum upp að Jafnréttisstofa stóð fyrir rannsókn þar sem að
    slembiúrtök voru tekin úr báðum þýðum, 20 karlar og 20 konur. Meðaltal
    og staðalfrávik launa í karla úrtakinu voru 245163 kr og 22814. Í konu
    úrtakinu voru meðaltal og staðalfrávik 218634 og 18312. Kannið nú með
    viðeigandi tilgátuprófi hvort munur sé á meðallaunum karla og kvenna sem
    starfa við kjötvinnslu. Notið :math:`\alpha = 0.05`. Gera má ráð fyrir
    að laun í báðum þýðum fylgi normaldreifingu.
    
    Förum nú eftir samantektinni um framkvæmd tilgátuprófa.
    
    #) Við ætlum að álykta um mun á meðaltölum tveggja þýða. Úrtökin eru
       **óháð**. Gera má ráð fyrir að launin séu normaldreifð. Við þekkjum
       ekki dreifni þýðanna en gerum ráð fyrir að hún sé jöfn (sjá dæmi
       :numref:`%s <e.alyktanirumdreifni1>`).
    
    #) Við fengum uppgefið að nota :math:`\alpha = 0.05.`
    
    #) Við ætlum að kanna hvort **munur** sé á meðallaunum karla og kvenna
       og notum við til þess tvíhliða próf. Tilgáturnar eru:
    
       .. math::
          \begin{aligned}
          H_0&:& \mu_1 - \mu_2 = 0\\
          H_1&:& \mu_1 - \mu_2 \neq 0 \end{aligned}
    
    #) Prófstærðina reiknum við með jöfnu :eq:`eq.tvomut3profstaerd`:
    
       .. math:: t = \frac{\overline{x}_1 - \overline{x}_2 - \delta}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}
    
       þar sem :math:`s_p^2` er reiknað samkvæmt jöfnu :eq:`eq.vegindreifni`
    
       .. math:: s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}
    
       Við vitum að :math:`n_1 = 20`, :math:`n_2 = 20`, :math:`\bar{x}_1` =
       245163, :math:`s_1` = 22814, :math:`\bar{x}_2` = 218634, :math:`s_2`
       = 18312 og :math:`\delta` = 0. Við setjum þessar tölur inn í
       jöfnurnar og fáum
    
       .. math:: s_p = \sqrt{\frac{(20 - 1)\cdot 22814^2 + (20 - 1)\cdot 18312^2}{20 + 20 - 2}} = 20685.84
    
       og
    
       .. math:: t = \frac{245163 - 218634 - 0}{20685.84 \sqrt{\frac{1}{20} + \frac{1}{20}}} = 4.06
    
    #) Við þurfum að finna höfnunarsvæðið og notum til þess t-töflu. Við
       flettum upp eftir :math:`n_1 + n_2 - 2 = 38`.
       :math:`t_{1-\alpha/2,(n_1 + n_2 - 2)} = t_{0.975,(38)}` = 2.024, svo
       við höfnum núlltilgátunni ef :math:`t > 2.024` eða
       :math:`t < -2.024`. Við sjáum að :math:`t > 2.024` svo prófstærðin
       fellur á höfnunarsvæði.
    
    #) Við höfnum núlltilgátunni og ályktum að meðallaun karla og kvenna sem
       starfa í kjötiðnaði séu ekki jöfn.
    
    .. figure:: myndir/t38.svg
        :align: center
        :alt: Mynd

Sýnidæmi: Ályktanir um tvö meðaltöl
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Hópur líffræðinga sem er að bera saman þyngd silunga í vötnum á Íslandi
    veiddi 51 silung í Þingvallavatni og reyndist meðalþyngd þeirra vera 550
    grömm og staðalfrávikið 65 grömm. Hópurinn veiddi auk þess 60 silunga í
    Úlfljótsvatni og var meðalþyngd þeirra 522 grömm og staðalfrávikið 30
    grömm. Kannið með viðeigandi tilgátuprófi hvort munur sé á meðalþyngd
    fiska í vötnunum tveimur. Gera má ráð fyrir að þyngd silunga fylgi
    normaldreifingu.
    
    Við þekkjum hvorki dreifni þýðanna né dreifingu þeirra en úrtökin eru
    stór. Við getum því notað t-próf. Við byrjum á að kanna hvort gera megi
    ráð fyrir að dreifnin í hópunum sé sú sama áður en við veljum viðeigandi
    t-próf.
    
    Förum eftir samantektinni um framkvæmd tilgátuprófa.
    
    #) Við ætlum að kanna tilgátu um dreifni tveggja normaldreifðra þýða.
    
    #) Við fengum uppgefið að nota :math:`\alpha = 0.05.`
    
    #) Við ætlum að kanna hvort dreifni þýðanna er mismunandi og notum við
       því tvíhliða próf.
    
       Tilgáturnar eru:
    
       .. math::
          \begin{aligned}
          H_0&:& \sigma_1^2 = \sigma_2^2\\
          H_1&:& \sigma_1^2 \neq \sigma_2^2\end{aligned}
    
    #) Prófstærðin er:
    
       .. math:: F = \frac{S_M^2}{S_m^2}
    
       Þar sem staðalfrávik í Þingvalla úrtakinu er hærra köllum við
       Þingvalla hópinn hóp :math:`M` og Úlfljótsvatns hópinn hóp :math:`m`.
       Setjum nú inn í prófstærðina og fáum
    
       .. math:: f = \frac{65^2}{30^2} = 4.69
    
    #) Við þurfum að finna höfnunarsvæðið og notum til þess :math:`F`-töflu.
       :math:`F_{1-\alpha/2,(n_M-1,n_m-1)} = F_{0.975,(50,59)}`. Sé F-taflan
       í kafla :ref:`T.6 <a.ftafla25>` skoðuð má sjá að þar er ekki að finna
       gildi fyrir :math:`F_{0.975,(50,59)}` og notum við því það sem er
       næst, :math:`F_{0.975,(\infty,60)} = 1.482`, svo við höfnum
       núlltilgátunni ef :math:`f > 1.482`. Við sjáum að :math:`f > 1.482`
       svo prófstærðin fellur á höfnunarsvæði.
    
    #) Við getum höfnað núlltilgátunni ályktað að dreifnin sé mismunandi.
    
    Þá erum við tilbúin til að kanna mismun meðaltalanna og förum við eftir
    samantekt um framkvæmd tilgátuprófa.
    
    #) Við ætlum að álykta um mun á meðaltölum tveggja þýða. Úrtökin eru
       **óháð**. Gera má ráð fyrir að þyngdin fylgi normaldreifingu. Við
       þekkjum ekki dreifni þýðanna og getum ekki gert ráð fyrir að hún sé
       jöfn. Við framkvæmum því t-próf fyrir ólíka dreifni.
    
    #) Notum :math:`\alpha = 0.05.`
    
    #) Við ætlum að kanna hvort **munur** sé á meðalþyngd silunga í
       Þingvallavatni og Úlfljótsvatni og notum við til þess tvíhliða próf.
       Tilgáturnar eru:
    
       .. math::
          \begin{aligned}
          H_0&:& \mu_1 - \mu_2 = 0\\
          H_1&:& \mu_1 - \mu_2 \neq 0 \end{aligned}
    
    #) Prófstærðina reiknum við með jöfnu :eq:`eq.tvomut4profstaerd`:
    
       .. math:: t = \frac{\overline{x}_1 - \overline{x}_2 - \delta}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}
    
       Við vitum að :math:`n_1 = 51`, :math:`n_2 = 60`, :math:`\bar{x}_1` =
       550, :math:`s_1` = 65, :math:`\bar{x}_2` = 522, :math:`s_2` = 30 og
       :math:`\delta` = 0. Við setjum þessar tölur inn í jöfnurnar og fáum
    
       .. math:: t = \frac{550 - 522 - 0}{\sqrt{\frac{65^2}{51} + \frac{30^2}{60}}} = 2.83
    
    #) Við þurfum að finna höfnunarsvæðið og notum til þess t-töflu. Sé
       núlltilgátan sönn fylgir prófstærðin t-dreifingu með :math:`\nu`
       frígráður. :math:`\nu` reiknum við með jöfnu :eq:`eq.fjoldifrigrada`:
    
       .. math::
          \nu = \frac{\Big(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2} \Big)^2}{\frac{(s_1^2/n_1)^2}{n_1 - 1} +
          \frac{(s_2^2/n_2)^2}{n_2 - 1}} = 67.9
    
       Sé t-taflan skoðuð má sjá að næsta gildi sem við höfum er fyrir 60
       frígráður, við notum það gildi.
       :math:`t_{1-\alpha/2,\nu} = t_{0.975,(60)}` = 2, svo við höfnum
       núlltilgátunni ef :math:`t > 2` eða :math:`t < -2`. Við sjáum að
       :math:`t > 2` svo prófstærðin fellur á höfnunarsvæði.
    
    #) Við höfnum núlltilgátunni og ályktum að meðalþyngd silunga í vötnunum
       tveimur sé ekki sú saman.

.. _s.paradarmaelingar:

Tilgátupróf fyrir paraðar mælingar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Margar rannsóknir eru gerðar á pöruðum slembiúrtökum eins og við kynntum
í kassa :numref:`%s <ss.paradslembiurtak>` í kafla :numref:`%s <c.fratilrauntilgagna>`.
Þær rannsóknir eru oftar en ekki þannig að gögnum er aflað fyrir og
eftir eitthvert inngrip. Tilgáturnar ganga þá iðulega út á að kanna
hvort inngripið hafi borið árangur. Við notum parað próf til að kanna
þessar tilgátur.

Gerum nú ráð fyrir að við höfum :math:`n` pör mælinga
:math:`(X_i, Y_i)`, :math:`i = 1,2,3...n`. Það fyrsta sem við þurfum að
gera er að finna mismun þessara pöruðu mælinga,

.. math::
   D_i = X_i - Y_i
   :label: eq.paradmismunur

Við lítum á :math:`D_i` sem slembiúrtak af stærð :math:`n` úr þýði með
meðaltal :math:`\mu_D`. Tilgátuprófin ganga út á að kanna :math:`\mu_D`.
Áður en við getum hafist handa við tilgátuprófin þurfum við að reikna
eftirfarandi stærðir:

.. math::
   \overline{D} = \frac{\sum_{i = 1}^{n} D_    i}{n}
   :label: eq.paradmedaltal

sem er meðaltal mismunanna og

.. math::
   {S_{D}}^{2} = \frac{\sum_{i = 1}^{n}(D_i - \overline{D})^2}{n-1}
   :label: eq.paraddreifni

sem er dreifni mismunanna.

Tilgátuprófin í þessum hluta prófa núlltilgátuna, hvort meðaltal mismuns
pöruðu mælinganna sé jafnt einhverju ákveðnu gildi sem við köllum
:math:`\mu_{D,0}`. Núlltilgátuna ritum við
:math:`H_0: \mu_D = \mu_{D,0}`. Algengast er að nota
:math:`\mu_{D,0} = 0` en þá er núlltilgátan einfaldlega: ,,Eru pöruðu
mælingarnar að meðaltali jafnar? “.

Líkt og áður eru notuð z-próf eða t-próf. Mun algengara er að nota
t-próf og munum við sýna það hér. Ef ekki er hægt að gera ráð fyrir að
mismunur mælinganna okkar fylgi normaldreifinu og mælingarnar okkar eru
fáar er hvorki hægt að framkvæma z- né t-próf. Þá þarf að grípa til
annarra aðferða, svo sem *stikalausra prófa* eða *endurvalsaðferða*, en
ekki verður fjallað um það nánar hér.

Fylgir mismunur mælinganna okkar normaldreifingu og/eða ef úrtakið er
stórt getum við notað eftirfarandi t-próf:

T-pŕof fyrir paraðar mælingar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Núlltilgátan er:
    
    .. math:: H_0: \mu_D = \mu_{D,0}
    
    Prófstærðin er:
    
    .. math::
       T = \frac{\overline{D}-\mu_{D,0}}{S_D/\sqrt{n}}
       :label: eq.paradtprof
    
    Ef núlltilgátan er sönn fylgir prófstærðin t-dreifingu með (:math:`n-1`)
    frígráðu, eða :math:`T \sim t_{(n-1)}`.
    
    +-------------------------------------+--------------------------------------------------------------------------+
    | Gagntilgáta                         | Hafna :math:`H_0` ef:                                                    |
    +=====================================+==========================================================================+
    | :math:`H_1: \mu_D < \mu_{D,0}`      | :math:`T < -t_{1-\alpha,(n-1)}`                                          |
    +-------------------------------------+--------------------------------------------------------------------------+
    | :math:`H_1: \mu_D > \mu_{D,0}`      | :math:`T > t_{1-\alpha,(n-1)}`                                           |
    +-------------------------------------+--------------------------------------------------------------------------+
    | :math:`H_1: \mu_D \neq \mu_{D,0}`   | :math:`T < -t_{1-\alpha/2,(n-1)}` eða :math:`T > t_{1-\alpha/2,(n-1)}`   |
    +-------------------------------------+--------------------------------------------------------------------------+
    
    :math:`t_{1-\alpha/2,(n-1)}` má finna í t-töflu í kafla :ref:`T.2 <a.ttafla>`.


--------------

Sýnidæmi: Ályktanir um paraðar mælingar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Lýðheilsustöð ákvað að standa fyrir rannsókn til að kanna hvort miðaldra
    menn sem eru yfir kjörþyngd geti lést á tveimur mánuðum hreyfi þeir sig
    í 30 mínútur dag hvern. Til að kanna það var slembiúrtak tekið af stærð
    6. Þyngd mannanna var mæld í upphafi átaksins og aftur í lok átaksins,
    tveimur mánuðum síðar. Mælingarnar má sjá hér að neðan. Kannið nú með
    viðeigandi tilgátuprófi hvort miðaldra menn sem eru yfir kjörþyngd geti
    að meðaltali lést á tveimur mánuðum hreyfi þeir sig í 30 mínútur dag
    hvern. Gera má ráð fyrir að þyngd fylgi normaldreifingu. Notið
    :math:`\alpha = 0.05`.
    
    +---------------+--------------------+--------------------+
    | Maður númer   | Þyngd fyrir [kg]   | Þyngd eftir [kg]   |
    +===============+====================+====================+
    | 1             | 123                | 120                |
    +---------------+--------------------+--------------------+
    | 2             | 112                | 108                |
    +---------------+--------------------+--------------------+
    | 3             | 107                | 106                |
    +---------------+--------------------+--------------------+
    | 4             | 101                | 99                 |
    +---------------+--------------------+--------------------+
    | 5             | 112                | 112                |
    +---------------+--------------------+--------------------+
    | 6             | 116                | 114                |
    +---------------+--------------------+--------------------+
    
    Áður en við hefjumst handa þurfum við að reikna :math:`D_i`,
    :math:`\overline{D}` og :math:`S_D`. Bætum nú við dálki í töfluna,
    :math:`d`. (við notum :math:`d` þar sem það eru mælingar á :math:`D`).
    
    +---------------+-----------------------------+-----------------------------+---------------------------+
    | Maður númer   | Þyngd fyrir (:math:`x_i`)   | Þyngd eftir (:math:`y_i`)   | :math:`d_i = x_i - y_i`   |
    +===============+=============================+=============================+===========================+
    | 1             | 123                         | 120                         | 3                         |
    +---------------+-----------------------------+-----------------------------+---------------------------+
    | 2             | 112                         | 108                         | 4                         |
    +---------------+-----------------------------+-----------------------------+---------------------------+
    | 3             | 107                         | 106                         | 1                         |
    +---------------+-----------------------------+-----------------------------+---------------------------+
    | 4             | 101                         | 99                          | 2                         |
    +---------------+-----------------------------+-----------------------------+---------------------------+
    | 5             | 112                         | 112                         | 0                         |
    +---------------+-----------------------------+-----------------------------+---------------------------+
    | 6             | 116                         | 114                         | 2                         |
    +---------------+-----------------------------+-----------------------------+---------------------------+
    
    Reiknum nú meðaltal mismunanna með jöfnu :eq:`eq.paradmedaltal`
    
    .. math:: \overline{d} = \frac{\sum_{i = 1}^{n} d_i}{n} = \frac{3+4+1+2+0+2}{6} = 2
    
    og dreifni mismunanna með jöfnu :eq:`eq.paraddreifni`
    
    .. math:: {s_d}^2 = \frac{\sum_{i = 1}^{n}(d_i - \bar{d})^2}{n-1} = \frac{(3-2)^2 + (4-2)^2 + ... + (2-2)^2}{5} =2
    
    Förum nú eftir samantektinni um framkvæmd tilgátuprófa.
    
    #) Við höfum **paraðar** mælingar þar sem :math:`n` er lítið en gera má
       ráð fyrir normaldreifðum þýðum. Við notum því parað t-próf.
    
    #) Við fengum uppgefið að nota :math:`\alpha = 0.05.`
    
    #) Við viljum sýna fram á að fólkið léttist en þar sem að fólkið gæti í
       raun verið að þyngjast notum við tvíhliða próf. Tilgáturnar eru:
    
       .. math::
          \begin{aligned}
          H_0&:& \mu_D = 0\\
          H_1&:& \mu_D \neq 0\end{aligned}
    
       (munið að við reiknuðum :math:`d = \text{fyrir} - \text{eftir}`.)
    
    #) Prófstærðina reiknum við með jöfnu :eq:`eq.paradtprof`
    
       .. math:: t = \frac{\overline{d}-\mu_{D,0}}{s_D/\sqrt{n}} = \frac{2 - 0}{\sqrt{2/6}} = 3.46
    
    #) Við notum t-töfluna til að finna höfnunarsvæðin og flettum upp eftir
       :math:`n - 1 = 5` frígráðum:
       :math:`t_{1-\alpha/2, (n-1)} = t_{0.975,5}` = 2.57, svo við höfnum
       núlltilgátunni ef :math:`t < -2.57` eða :math:`t > 2.57`. Við sjáum
       að :math:`t > 2.57` svo prófstærðin fellur á höfnunarsvæði.
    
    #) Við höfnum núlltilgátunni og ályktum að það að hreyfa sig í 30
       mínútur á dag í tvo mánuði ber árangur í baráttunni við aukakílóin
       fyrir miðaldra menn yfir kjörþyngd.
    
    .. figure:: myndir/t5_tvihlida.svg
        :align: center
        :alt: Mynd

Hvenær notum við hvaða próf?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við höfum nú fjallað um ályktanir fyrir meðaltal í einu þýði, mismun
óháðra meðaltala og mismun paraðra mælinga. Í öllum tilvikum getum við
notað z-próf/öryggisbil eða t-próf/öryggisbil við verkið. Tökum nú
stuttlega saman hvenær hvor dreifing á við.

Z-próf má nota þegar:

-  Þýðin fylgja normaldreifingu og við gerum ráð fyrir að við þekkjum
   dreifni þýðanna.

-  Úrtökin eru stór, óháð því hver dreifing þýðanna er.

t-próf má nota þegar:

-  Þýðin fylgja normaldreifingu, sama hversu lítil úrtökin eru.

-  Úrtökin eru stór, óháð því hver dreifing þýðanna er.

Þegar úrtökin eru stór hafa t-dreifingin og z-dreifingin nánast sömu
lögun og þá verða prófin/öryggisbilin tvö nánast jafngild. Þar sem
t-dreifingin hefur þyngri hala en normaldreifingin er erfiðara að hafna
núlltilgátunni í því tilviki og þar af leiðandi minni hætta á villu af
gerð eitt. Því er ívið varfærnara að nota t-prófið/öryggisbilið og þar
að auki eru t-próf innbyggð í flest tölfræðiforrit, ólíkt z-prófum, enda
mun algengari. Eins og þið sjáið er eina tilvikið sem stendur eftir
þegar úrtökin eru lítil og ekki er hægt að gera ráð fyrir að þýðin fylgi
normaldreifingu. Í þeim tilvikum er stundum hægt að *umbreyta*
(e. transform) gögnunum, nota *endurvalsaðferðir* (e. resampling methods) eða
nota *stikalaus próf* (e. nonparametric tests) en ekki verður farið nánar í
það hér.

Að lokum viljum við ítreka það að gæta vel að því hvenær við höfum í
höndunum *paraðar* mælingar og hvenær við könnum *tvö óháð* þýði. Í
hvert sinn sem við höfum innbyggða pörun fyrir hendi, þannig að við
getum með eðlilegum hætti reiknað mismun hvers pars og dregið ályktanir
um það, fæst meiri styrkur með því að nota tilgátupróf fyrir paraðar
mælingar og því skyldi það alltaf notað. Ef að hins vegar engin eðlileg
pörun er fyrir hendi er sá samanburður á sandi byggður. Í því tilviki
þegar mælingarnar eru mismargar grípa tölfræðiforritin oft þá villu og
vara okkur við. Ef ekki, erum við að gefa okkur forsendur sem gilda ekki
og líkurnar á villu af gerð I verða hærri en við höldum.

Dæmi
----

Dæmi
~~~~

Gera má ráð fyrir að hitastig á hádegi í júlí á ákveðnum stað á landinu
fylgi normaldreifingu. Ferðamálfræðingur nokkur hefur mikinn áhuga á að
meta stikana í þessari dreifingu og valdi hann tilviljunarkennt einn dag
í júlí síðustu átta ár og skráði hitastigið. Hann reiknaði meðaltal og
staðalfrávik mælinganna átta og fékk út að meðaltalið var 14.7 gráður og
staðalfrávikið 5.6 gráður. Finnið 95% öryggisbil fyrir dreifnina.

Dæmi
~~~~

Láki landfræðingur vill kanna hvort munur sé á dreifni í tveimur
normaldreifðum þýðum sem hann er að kanna. Til þess tók hann úrtök úr
þýðunum, bæði af stærð 18. Hann reiknaði staðalfrávik úrtakanna og fékk
út að staðalfrávikið í því fyrra var 21.43 og í því seinna 32.18. Hvert
er gildið á prófstærðinni sem nota á til að kanna að munur sé á dreifni
þýðanna tveggja?

Dæmi
~~~~

Finnur ferðamálafræðingur er að kanna hversu mikið ferðamenn eru
tilbúnir til að greiða fyrir að fá að sjá Gullfoss. Hann valdi af
handahófi 20 ferðamenn og reiknaði að ferðamennirnir 20 voru tilbúnir að
greiða 1243 krónur að meðaltali og var staðalfrávikið 126 krónur. Gera
má ráð fyrir að upphæðin sem ferðamenn eru tilbúnir til að greiða fylgi
normaldreifingu. Hvert er efra mark 95% öryggisbils fyrir dreifni
upphæðarinnar sem ferðamenn eru tilbúnir til að greiða?

Dæmi
~~~~

Fuglavinafélagið fylgist náið með þyngd stokkanda við tjörnina og
fullyrða vísindamenn innan félagsins að þyngd andanna fylgi
normaldreifingu. Félagið ákvað að skoða hvort dreifni þyngdar
stokkandarsteggja og stokkandakolla sé misjöfn og mældi því þyngd 7
steggja og 7 kollna og skráði. Niðurstöðurnar má sjá hér að neðan (mælt
í grömmum).

+-----------+-----------+
| Kollur    | Steggir   |
+===========+===========+
| 999.70    | 990.12    |
+-----------+-----------+
| 981.38    | 989.23    |
+-----------+-----------+
| 1012.47   | 987.56    |
+-----------+-----------+
| 976.15    | 976.46    |
+-----------+-----------+
| 968.19    | 1029.37   |
+-----------+-----------+
| 974.81    | 948.75    |
+-----------+-----------+
| 1023.01   | 975.55    |
+-----------+-----------+

Meðlimir fuglavinafélagsins reiknuðu út að staðalfrávik þyngdar
kollnanna sem mælar voru er 21.04 g og steggjanna 24.14 g. Kannið hvort
munur sé á dreifni þyngdar á kollum og steggjum. Notið
:math:`\alpha = 0.05`.

Dæmi
~~~~

Ferðamálafræðingur nokkur framkvæmdi tilraun til að meta hitastig í
náttúrulegri laug nálægt Hveragerði. Hann mældi hitastigið 40 sinnum og
var hitastigið að meðaltali 38.8 gráður og var staðalfrávikið 4.3
gráður. Finnið 90% öryggisbil fyrir meðalhitastigið í lauginni.

Dæmi
~~~~

Ferðamálafræðingarnir Siggi og Sigga ákváðu að kanna meðalfjölda hvala
sem sjást þegar farið er í hvalaskoðun á Húsavík í maí. Þau völdu af
handahófi 8 ferðir og skráðu fjölda hvala sem sáust. Að meðaltali sáust
12.3 hvalir í ferðunum og staðalfrávikið í þessum 8 ferðum var 4.3. Gera
má ráð fyrir að fjöldi hvala sem sjást í hvalaskoðunarferð fylgi
normaldreifingu.

a) Finnið :math:`95\%` öryggisbil fyrir meðalfjölda hvala sem sjást
   þegar farið er í hvalaskoðun á Húsavík í maí.

#) Kannið hvort meðalfjöldi hvala sem sjást þegar farið er í hvalaskoðun
   á Húsvík í maí sé frábrugðið 10 hvölum. Notið :math:`\alpha = 0.05.`

Dæmi
~~~~

Lífefnafræðingur nokkur er að kanna ákveðið efnahvarf. Þetta efnahvarf
hefur verið rannsakað mikið og gera má ráð fyrir tíminn sem það tekur
fyrir efnahvarfið að ljúka fylgi normaldreifingu með þekkta dreifni sem
er 1.2 mínútur. Lífefnafræðingurinn hefur bætt við hvata í efnahvarfið
og vill hann sýna fram á að með þessum hvata sé efnahvarfið að meðaltali
hraðara en 7.9 mínútur. Gera má ráð fyrir að dreifnin sé þekkt og sé sú
sama og án hvatans. Lífefnafræðingurinn tekur tímann sem það tekur
efnahvarfið með hvatanum að ljúka 12 sinnum og var meðaltíminn 7.2
mínútur. Kannið með viðeigandi tilgátuprófi hvort efnahvarfið sé að
meðaltali hraðara en 7.9 mínútur. Hér skal nota tvíhliða próf því
efnahvarfið gæti í raun verið hægara en 7.9 mínútur. Notið
:math:`\alpha = 5\%.`

Dæmi
~~~~

Borgaryfirvöld voru að velta fyrir sér meðalfjölda íbúa á heimili í
hverfi einu. Könnuð voru 24 heimili og kom í ljós að meðalfjöldi íbúa á
hvert heimili var 2.7 og staðalfrávikið var 2.6. Finnið 90% öryggisbil
fyrir meðalfjölda íbúa á heimili. Gerið ráð fyrir að fjöldi íbúa fylgi
normaldreifingu.

Dæmi
~~~~

Siggi sæti hefur áhuga á þyngd snickersstykkja. Hann fer útí búð og
kaupir 100 stykki sem hann svo vigtar og skráir samviskusamlega hjá sér
hvað hvert stykki er þungt. Á umbúðunum stendur að stykkið sé 42 grömm
en Sigga grunar að á meðaltali séu stykkin léttari en það sem gefið er
upp á pakkanum. Meðaltal stykkjanna sem Siggi sæti keypti var 40.5 grömm
og var staðalfrávikið 0.9 grömm. Kannið hvort snickersstykki séu að
meðaltali léttari en það sem gefið er upp á pakkanum, notið
:math:`\alpha = 0.05`.

Dæmi
~~~~

Rafhlöðuframleiðandi nokkur fullyrðir að meðallíftími rafhlaðna sem
fyrirtækið framleiðir sé 240 klukkustundir. Uppi er sú kenning hjá
gæðadeild fyrirtækisins að líftíminn sé frábrugðinn 240 klukkustundum.
Gæðadeildin ákvað því að framkvæma tilraun til að kanna þessa kenningu
sína. Tekið var slembiúrtak af stærð 18 og líftíminn kannaður.
Meðallíftími rafhlaðanna sem kannaðar voru var 237.056 klukkustundir og
staðalfrávik 11.280. Gera má ráð fyrir að líftími rafhlaðanna fylgi
normaldreifingu.

a) Finnið 95% öryggisbil fyrir meðallíftíma rafhlaðna.

#) Kannið hvort meðallíftími rafhlaðna sé frábrugðin 240 klukkustundum.
   Setjið fram tilgáturnar, kannið tilgátuna með viðeigandi prófstærð og
   lýsið niðurstöðum ykkar stuttlega í orðum. Notið :math:`\alpha` =
   0.05.

Dæmi
~~~~

Lyfjafræðingar sem hafa mikinn áhuga á kólestrólmagni í blóði íslenskra
karlmanna völdu af handahófi 20 karlmenn og mældu svo kólesterólið hjá
þeim. Meðaltal mælinganna var 205.2 og staðalfrávikið 6.4. Finnið
:math:`99\%` öryggisbil fyrir meðalkólestrólmagn í blóði íslenskra
karlmanna. Gera má ráð fyrir að kólesteról í blóði karlmanna á Íslandi
fylgir normaldreifingu.

Dæmi
~~~~

Margrét matvælafræðingur var að kanna gæði appelsínusafa sem hún er að
þróa og fékk 40 manns til að bragða á safanum og gefa honum einkunn frá
0 til 10. Appelsínuvinafélagið flokkar safa sem skora að meðaltali hærra
en 7 á sambærilegu prófi sem eðalappelsínusafa. Að tilrauninni lokinni
reiknaði Margrét út meðaleinkunn og staðalfrávik og fann hún að
meðaleinkunnin var 7.8 og staðalfrávikið 1.8. Kannið með viðeigandi
tilgátuprófi hvort Margrét geti kallað safann sinn eðalappelsínusafa
samkvæmt skilgreiningu appelsínuvinafélagsins. Sýnið öll skrefin sex.
Notið :math:`\alpha = 0.05`.

Dæmi
~~~~

Palli jarðfræðingur hefur áhuga á að bera saman skjálftavirkni á
suðurlandi og norðurlandi. Hann valdi 40 vikur af handahófi og taldi
fjölda skjálfta á hvorum staðnum fyrir sig. Á suðurlandi urðu að
meðaltali 23.3 skjálftar á viku og á norðurlandi 31.3 skjálftar.
Staðalfrávikið þessar 40 vikur á suðurlandi var 7.7 skjálftar og á
norðurlandi 9.1 skjálftar.

a) Finnið :math:`95\%` öryggisbil fyrir mun á meðalfjölda skjálfta á
   norðurlandi og suðurlandi.

#) Kannið með viðeigandi tilgátuprófi hvort munur sé á skjálftavirkni á
   suðurlandi og norðurlandi. Notið :math:`\alpha = 0.05`.

Dæmi
~~~~

Gulla lyfjafræðingur ætlar að kanna virkni hjartalyfs og ætlar hún að
framkvæma tilraunirnar á músum. Áður en hún framkvæmir tilraunina vill
hún kanna hvort munur sé á hjartslætti karlkyns og kvenkyns músa. Gera
má ráð fyrir að hjartsláttur kvenkyns og karlkyns músa fylgi
normaldreifingu. Gulla velur af handahófi 10 kvenkyns og 10 karlkyns mýs
og mældi hjartslátt þeirra. Hjartsláttur kvenkyns músanna var að
meðaltali 582.7 slög á mínútu og karlkyns músanna var hann 531.7 slög á
mínútu. Staðalfrávikið í kvenkyns hópnum voru 34.2 slög og 45.7 í karla
hópnum. Kannið með viðeigandi tilgátuprófi hvort munur sé á
meðalhjartslætti karkyns og kvenkyns músa. Notið :math:`\alpha = 0.05`.

Dæmi
~~~~

Eftirfarandi tölur sýna landaðan afla (í tonnum) á tveimur togurum mánuð
einn. Kannið hort munur sé á meðalafla togaranna með viðeigandi
tilgátuprófi. Gera ráð fyrir að þyngd aflans fylgi normaldreifingu.
Notið :math:`\alpha` = 0.05.

+----------------+------------+------------+
|                | Togari 1   | Togari 2   |
+================+============+============+
|                | 109        | 56         |
+                +------------+------------+
|                | 62         | 75         |
+                +------------+------------+
|                | 69         | 89         |
+                +------------+------------+
|                | 85         | 69         |
+                +------------+------------+
|                | 32         | 36         |
+                +------------+------------+
|                | 115        | 162        |
+----------------+------------+------------+
| Meðaltal       | 78.67      | 81.17      |
+----------------+------------+------------+
| Staðalfrávik   | 31.08      | 43.46      |
+----------------+------------+------------+

Dæmi
~~~~

Til að kanna hvort nagladekk minnki að meðaltali hemlunarvegalengd miðað
við venjuleg dekk var eftirfarandi tilraun framkvæmd. Sex bílar voru
notaðir og hemlunarvegalengd mæld með venjulegum dekkjum og
nagladekkjum. Aðrar breytur svo sem hraði, ástand vegar osfrv. var sá
sami í öllum tilraununum. Gögnin má sjá hér að neðan.

+--------------+-----------------+-------------+
| Bíll númer   | Venjuleg dekk   | Nagladekk   |
+==============+=================+=============+
| 1            | 73              | 71          |
+--------------+-----------------+-------------+
| 2            | 79              | 73          |
+--------------+-----------------+-------------+
| 3            | 64              | 63          |
+--------------+-----------------+-------------+
| 4            | 55              | 57          |
+--------------+-----------------+-------------+
| 5            | 72              | 72          |
+--------------+-----------------+-------------+
| 6            | 70              | 69          |
+--------------+-----------------+-------------+

Gera má ráð fyrir að hemlunarvegalengd fylgi normaldreifingu. Rökstyðjið
hvaða próf er viðeigandi fyrir þessi gögn til að kanna hvort nagladekk
minnki að meðaltali hemlunarvegalengd miðað við venjuleg dekk. Notið
tvíhliða próf því nagladekk geta í raun aukið hemlunarvegalengdina.
Notið :math:`\alpha` = 0.05. Setjið fram tilgáturnar, kannið tilgátuna
með viðeigandi prófstærð og lýsið niðurstöðu ykkar stuttlega í orðum.

Dæmi
~~~~

Svokallað PEFR skor (e. Peak Expiratory Flow Rate) er mælikvarði notaður
til að mæla lungnastarfsemi í astmasjúklingum. Því hærra sem gildið er
því betur starfa lungun. Sú kenning hefur lengi verið við líði að
göngutúrar í köldu veðri hafi jákvæð áhrif á lungnastarfsemina. Til að
kanna þessa kenningu ákvað landlæknisembættið að standa fyrir rannsókn
þar sem sex astmasjúklingar voru valdir af handahófi og þeir látnir
ganga úti í köldu veðri í einn klukkutíma. PEFR skor þeirra var mælt
fyrir göngutúrinn og aftur eftir göngutúrinn, einum tíma síðar. Gögnin
má sjá hér að neðan.

+-------------------------+-------------------+-------------------+
| Astmasjúklingur númer   | PEFR skor fyrir   | PEFR skor eftir   |
+=========================+===================+===================+
| 1                       | 300               | 312               |
+-------------------------+-------------------+-------------------+
| 2                       | 201               | 242               |
+-------------------------+-------------------+-------------------+
| 3                       | 232               | 340               |
+-------------------------+-------------------+-------------------+
| 4                       | 312               | 388               |
+-------------------------+-------------------+-------------------+
| 5                       | 220               | 296               |
+-------------------------+-------------------+-------------------+
| 6                       | 256               | 254               |
+-------------------------+-------------------+-------------------+

Gera má ráð fyrir að PEFR skor í astmasjúklingum fylgi normaldreifingu.
Rökstyðjið hvaða próf er viðeigandi fyrir þessi gögn til að kanna hvort
að ganga í köldu veðri í klukkustund hafi jákvæð áhrif á lungnastarfsemi
astmasjúklinga. Notið tvíhliða próf því ganga í köldu veðri getur í raun
haft neikvæð áhrif á lungnastarfsemi. Notið :math:`\alpha = 0.05`.
Setjið fram tilgáturnar, kannið tilgátuna með viðeigandi prófstærð og
lýsið niðurstöðu ykkar stuttlega í orðum.

Dæmi
~~~~

Ögmundur er mikill áhugamaður um kvikmyndir og ákvað hann að gera
óformlega könnun á lengd spennumynda annars vegar og rómantískra
gamanmynda hins vegar. Hann valdi sex spennumyndir og sex rómantískar
gamanmyndir af handahófi og skráði hversu langar þær voru.
Spennumyndirnar voru að meðaltali 112 mínútur og rómatísku
gamanmyndirnar voru að meðaltali 92 mínútur að lengd. Lengd kvikmynda af
þessum gerðum hefur verið rannsökuð mikið af kvikmyndavísindamönnum og
því má gera ráð fyrir að lengd spennumynda fylgi normaldreifingu með
þekkt staðalfrávik 22 mínútur og lengd rómantískra gamanmynda fylgi
normaldreifingu með þekkt staðalfrávik 8 mínútur.

a) Hvert er neðra öryggismark 95% öryggisbils fyrir mismun á meðaltölum
   spennumynda og gamanmynda?

#) Með rannsókninni vildi Ögmundur sýna að meðallengd rómantískra
   gamanmynda sé frábrugðin meðallengdar spennumynda. Hver á
   gagntilgátan að vera?

Dæmi
~~~~

Bjórvinafélag Íslands ákvað að framkvæma litla tilraun þar sem gæði
tveggja bjórtegunda var borin saman. 10 manns tóku þátt í rannsókninni
og var þeim skipt tilviljunarkennt í tvo hópa. Annar hópurinn fékk bjór
``x`` og hinn bjór ``y``. Þátttakendurnir gáfu svo bjórnum einkunn frá 0
til 10. Gera má ráð fyrir að einkunnirnar fylgi normaldreifingu.
Niðurstöðurnar má sjá hér að neðan:

+----------+----------+
| Bjór x   | Bjór y   |
+==========+==========+
| 8.6      | 6.2      |
+----------+----------+
| 9.2      | 7.2      |
+----------+----------+
| 7.8      | 7.6      |
+----------+----------+
| 7.2      | 8.2      |
+----------+----------+
| 8.9      | 6.1      |
+----------+----------+

Kannið með viðeigandi tilgátuprófi hvort munur sé á meðalgæðum bjóranna.
Notið :math:`\alpha = 0.01`.

Dæmi
~~~~

Hjartsláttur 5 kvenna var mældur fyrir og eftir að þær voru látnar
hlaupa upp 100 tröppur. Mælingarnar sjást í töflunni.

+--------+----------------------+----------------------+
| Kona   | Hjartsláttur fyrir   | Hjartsláttur eftir   |
+========+======================+======================+
| 1      | 60                   | 70                   |
+--------+----------------------+----------------------+
| 2      | 55                   | 61                   |
+--------+----------------------+----------------------+
| 3      | 62                   | 88                   |
+--------+----------------------+----------------------+
| 4      | 63                   | 72                   |
+--------+----------------------+----------------------+
| 5      | 59                   | 80                   |
+--------+----------------------+----------------------+

Kannið með viðeigandi tilgátuprófi hvort hjartsláttur aukist að
meðaltali við að hlaupa upp 100 tröppur. Gera má ráð fyrir að
hjartsláttur fylgi normaldreifingu. Notið :math:`\alpha = 0.05`.
