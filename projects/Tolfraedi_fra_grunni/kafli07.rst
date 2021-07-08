.. _c.alyktanirumflokkabreytur:

Ályktanir um flokkabreytur
==========================

Nú er komið að því að beita ályktunartölfræði á breyturnar okkar. Við
byrjum á því að skoða *álykanir um flokkabreytur* sem er umfjöllunarefni
þessa kafla. Eins og við nefndum í kafla :numref:`%s <s.breytur>`, þá segja
útkomur flokkabreyta til um það hvaða flokki mælingarnar okkar tilheyra
og eru því ekki mældar í neinum tilteknum einingum. Það er því
merkingarlaust að tala um meðaltöl og staðalfrávik þegar unnið er með
flokkabreytur. Hins vegar getum við unnið með *hlutföll* (e.
proportions), það er við getum kannað hversu hátt hlutfall mælinganna
lenti í tilteknum flokki.

Í kafla :numref:`%s <s.eitthlutfall>` byrjum við á að skoða tilgátupróf og
öryggisbil fyrir *eitt hlutfall*, með öðrum orðum skoðum við hversu hátt
hlutfall viðfangsefna þýðisins hefur tiltekið gildi flokkabreytu. Þar á
eftir, í kafla :numref:`%s <s.tvohlutfoll>`, könnum við hvernig bera má saman
*hlutföll tveggja þýða*. Þá skoðum við hlutfall mælinga sem hljóta
tiltekið gildi flokkabreytu í einu þýði og berum saman við hlutfallið í
hinu þýðinu. Í kafla :numref:`%s <s.fleirihlutfoll>` munum við sjá hvernig hægt
er að útvíkka aðferðina til að skoða fleiri en tvö þýði. Loks í kafla
:numref:`%s <s.tengslatoflur>` kynnumst við svo tilgátuprófum fyrir svokallaðar
tengslatöflur sem notuð eru til að kanna hvort samband sé milli tveggja
flokkabreyta sem eru þá mældar á sama þýðinu.

Eins og áður gerum við ráð fyrir að þýðið skiptist með einhverjum
ákveðnum hætti og innihaldi því einhver raunveruleg hlutföll.
Aðferðirnar okkar miðast að því að draga ályktanir um og meta hver þessi
hlutföll eru.

.. _s.eitthlutfall:

Ályktanir um hlutfall þýðis
---------------------------

Í þessum hluta munum við skoða bilmat og tilgátupróf fyrir eitt
hlutfall, :math:`p`, sem lýsir því hversu hátt hlutfall mælinga tekur
eitt ákveðið gildi flokkabreytu. Sem dæmi má nefna skoðanakönnum þar sem
fólk er spurt ,,styður þú ríkisstjórnina? “ Hlutfallið sem við skoðum er
það hlutfall viðfangsefna sem svarar spurningunni játandi. Markmið
rannsókna af þessu tagi er oftar en ekki að draga ályktanir um hlutfall
alls þýðisins, :math:`p`, sem við ekki þekkjum. Í þessu dæmi væri það að
kanna hversu hátt hlutfall allra kjósanda styður ríkisstjórnina.

Útkomur mælinganna sem framkvæmdar eru á úrtakinu eru notaðar til að
finna mat á óþekkta hlutfallinu og notum við :math:`\hat{p}` (lesið
:math:`p` -hatt) til að tákna það mat. Við metum þýðishlutfallið
:math:`p`, með úrtakshlutfallinu, það er

.. math::
   \hat{p} = \frac{x}{n}
   :label: eq.phat

þar sem :math:`x` er fjöldi þeirra mælinga sem hljóta viðkomandi útkomu
(,,já“ í dæminu hér að ofan) og :math:`n` er stærð úrtaksins.

Tilgátuprófið í þessum hluta prófar núlltilgátuna hvort hlutfall
þýðisins, :math:`p`, séu jafnt einhverju ákveðnu gildi sem við köllum
:math:`p_0`. Núlltilgátuna ritum við :math:`H_0: p= p_0`.

Normalnálgun
~~~~~~~~~~~~

Þegar við skoðum hvort flokkabreyta tekur ákveðið tiltekið gildi, getum
litið á sérhverja mælingu sem Bernoulli tilraun (sjá kassa
:numref:`%s <em.bernoulli>` í kafla :numref:`%s <s.binom>`). Ef mælingin hlýtur tiltekið
gildi flokkabreytunnar lítum við á hana sem ,,heppnaða tilraun“, annars
ekki. Mögulegar útkomur eru eingöngu tvær (í hópnum eða ekki), með sömu
líkur í hvert sinn og þar sem við gerum alltaf þá kröfu að mælingarnar
séu óháðar og einsdreifðar má líta á þær sem röð óháðra tilrauna.

Þar sem við getum litið á hverja mælingu sem Bernoulli tilraun getum við
sömuleiðis litið svo á að heildarfjöldi heppnaðra tilrauna fylgi
tvíkostadreifingunni (sjá kassa :numref:`%s <em.tvikostadreifingin>` í kafla
:numref:`%s <s.binom>`). Þá er stikinn :math:`p` hlutfallið í dreifingunni og
:math:`n` er heildarfjöldi mælinga. Því er hægt að nota aðferðir byggðar
á tvíkostadreifingunni til að álykta um :math:`p`. Þær aðferðir eru hins
vegar það stærðfræðilega erfiðar að ekki er unnt að reikna þær í
höndunum.

Þegar ákveðnum skilyrðum er uppfyllt líkist tvíkostadreifingin
normaldreifingunni nægjanlega mikið til að hægt sé að beita aðferðum sem
byggðar eru á eiginleikum normaldreifingarinnar til að draga ályktanir
um slembistærðir sem í raun fylgja tvíkostadreifingu. Það köllum við að
beita *normalnálgun*. Í þessum kafla munum við aðallega styðjast við
aðferðir sem byggja á þeirri nálgun.

Tilgátuprófið í þessum hluta byggir á normalnálgun. Við munum notast við
þumalputtaregluna að séu  :math:`n\hat{p}`  og  :math:`n(1-\hat{p})`
 stærri en 15 má nota nálgunina. Það er ætíð mikilvægt að gæta þess að
þessi skilyrði séu uppfyllt. Ef skilyrðin eru ekki uppfyllt má nota
tilgátupróf sem byggir beint á tvíkostadreifingunni, eða þá
*endurvalsaðferð* til að meta tilgátuprófið. Hvoruga aðferðina má reikna
í höndunum en þær eru útfærðar í öllum helstu tölfræðihugbúnuðum.

Öryggisbil og tilgátupróf
~~~~~~~~~~~~~~~~~~~~~~~~~

Öryggisbil fyrir hlutfall þýðis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Séu skilyrðin fyrir að nota normalnálgunina uppfyllt, það er ef
     :math:`n\hat{p}`  og  :math:`n(1-\hat{p})`  eru stærri en 15 má reikna
    neðra öryggismark fyrir :math:`p` með:
    
    .. math::
       \hat{p} - z_{1-\alpha/2} \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
       :label: eq.pnedra
    
    og efra öryggismarkið með
    
    .. math::
       \hat{p} + z_{1-\alpha/2} \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
       :label: eq.pefra
    
    þar sem :math:`\hat{p} = \frac{x}{n}` og :math:`z_{1-\alpha/2}` fæst með
    að fletta upp í töflu stöðluðu normaldreifingarinnar í kafla
    :ref:`T.1 <a.normaltafla>`.
    
    Öryggisbilið má því skrifa sem
    
    .. math::
       \hat{p} - z_{1-\alpha/2} \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
       < p < 
       \hat{p} + z_{1-\alpha/2} \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}


--------------

Tilgátupróf fyrir hlutfall þýðis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Séu skilyrðin fyrir að nota normalnálgunina uppfyllt, þ.e.a.s. ef
     :math:`n\hat{p}`  og  :math:`n(1-\hat{p})`  eru stærri en 15 má nota
    eftirfarandi tilgátupróf.
    
    Núlltilgátan er:
    
    .. math:: \text{H}_0: p = p_0
    
    Prófstærðin er:
    
    .. math::
       Z = \frac{X - np_0}{\sqrt{np_0(1-p_0)}}
       :label: eq.pprofstaerd
    
    þar sem :math:`X` er fjöldi heppnaðra tilrauna og :math:`n` er stærð
    úrtaksins.
    
    Ef núlltilgátan er sönn fylgir prófstærðin stöðluðu normaldreifingunni,
    eða :math:`Z \sim N(0,1)`. Gagntilgátan getur verið einhliða eða
    tvíhliða og má sjá þær ásamt höfnunarsvæðunum hér að neðan.
    
    +---------------------------+--------------------------------------------------------------+
    | Gagntilgáta               | Hafna :math:`H_0` ef:                                        |
    +===========================+==============================================================+
    | :math:`H_1: p < p_0`      | :math:`Z < -z_{1-\alpha}`                                    |
    +---------------------------+--------------------------------------------------------------+
    | :math:`H_1: p > p_0`      | :math:`Z > z_{1-\alpha}`                                     |
    +---------------------------+--------------------------------------------------------------+
    | :math:`H_1: p \neq p_0`   | :math:`Z < -z_{1-\alpha/2}` eða :math:`Z > z_{1-\alpha/2}`   |
    +---------------------------+--------------------------------------------------------------+


--------------

.. _e.p:

Sýnidæmi: Ályktanir um hlutfall þýðis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Fyrirtæki hér í borg ákvað að framkvæma skoðanakönnun til að kanna fylgi
    ríkisstjórnarinnar. Fyrirtæki þetta er með marga færa próffræðinga á
    sínum snærum svo við getum gert ráð fyrir að úrtakshögun og úrvinnsla
    hafi verið til fyrirmyndar. Niðurstaðan var að af þeim 8750 sem spurðir
    voru “styður þú ríkisstjórnina“ sögðu 4530 já og 4220 nei. Finnið 95%
    öryggisbil fyrir :math:`p`, hlutfall þeirra sem styðja ríkisstjórnina.
    Taka skal fram að tölurnar í þessu dæmi eru uppspuni.
    
    Byrjum á að finna :math:`p` með jöfnu :eq:`eq.phat`
    
    .. math:: \hat{p} = \frac{x}{n} = \frac{4530}{8750} = 0.5177
    
    Skilyrðin um normalnálgun eru uppfyllt þar sem  :math:`n\hat{p}`  og
     :math:`n(1-\hat{p})`  eru bæði stærri en 15 . Nú má reikna neðra
    öryggismark með jöfnu :eq:`eq.pnedra`
    
    .. math::
       \hat{p} - z_{1-\alpha/2} \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} =
       0.5177 - 1.96 \cdot \sqrt{\frac{0.5177(1-0.5177)}{8750}} = 0.5072
    
    og efra öryggismark með jöfnu :eq:`eq.pefra`
    
    .. math::
       \hat{p} + z_{1-\alpha/2} \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} =
       0.5177 + 1.96 \cdot \sqrt{\frac{0.5177(1-0.5177)}{8750}} =  0.5282
    
    Öryggisbilið má því skrifa sem
    
    .. math:: 0.5072 < \ p \ < 0.5282
    
    Við áætlum því að 51.77% kjósenda styðji ríkisstjórnina og fullyrðum með
    95% vissu að það hlutfall liggi á bilinu frá 50.72% upp í 52.82%.

.. _s.tvohlutfoll:

Ályktanir um hlutföll tveggja þýða
----------------------------------

Ályktanir um hlutföll tveggja þýða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Í þessum hluta munum við skoða bilmat og tilgátupróf þar sem hlutföll
mælinga sem hljóta tiltekið gildi flokkabreytu eru borin saman milli
tveggja þýða. Dæmi um slíkt væri að kanna hvort hlutfall kvenna sem
styður ríkistjórnina sé jafnt hlutfalli karla sem séu þeirrar skoðunar.

Þegar bera á saman hlutföll í tveimur þýðum er, til þæginda, venjan að
kalla það þýði sem úrtakshlutfallið er hærra þýði 1 og hitt þýði 2. Við
köllum hlutföll heppnaðra tilrauna í þýðunum tveimur :math:`p_1` og
:math:`p_2`. Tekin eru slembiúrtök úr þýðunum tveimur af stærð
:math:`n_1` og :math:`n_2` og úrtakshlutföllin, :math:`\hat{p}_1` og
:math:`\hat{p}_2` notuð til að meta þýðishlutföllin :math:`p_1` og
:math:`p_2`. Jöfnur þeirra eru

.. math::
   \begin{aligned}
   \hat{p}_1 = \frac{x_1}{n_1}\end{aligned}
   :label: eq.p1hat

.. math::
   \begin{aligned}
   \hat{p}_2 = \frac{x_2}{n_2}\end{aligned}
   :label: eq.p2hat

þar sem :math:`x_1` og :math:`x_2` eru fjöldi heppnaðra tilrauna í
úrtökunum tveimur.

Tilgátuprófið í þessum hluta prófar núlltilgátuna hvort hlutföllin í
hópunum tveimur séu jöfn. Núlltilgátuna ritum við
:math:`H_0: p_1 = p_2`.

Líkt og þegar við könnum hlutfall eins þýðis notum við normalnálgun til
að bera saman hlutföll tveggja þýða. Í þessu tilviki notum við
þumalputtaregluna að séu  :math:`n_1 \hat{p}_1`,
 :math:`n_1(1-\hat{p}_1)`, :math:`n_2 \hat{p}_2`  og
 :math:`n_2(1-\hat{p}_2)`  eru öll stærri en 15 má beita normalnálgun .
Ef skilyrðin eru ekki uppfyllt má nota tilgátupróf *endurvalsaðferð* til
að meta tilgátuprófið eða framkvæma svokallað *Fishers próf*. Hvoruga
aðferðina má reikna í höndunum en þær eru útfærðar í öllum helstu
tölfræðihugbúnuðum.

Öryggisbil fyrir hlutföll tveggja þýða
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Séu skilyrðin fyrir að nota normalnálgunina uppfyllt, þ.e.a.s. ef
     :math:`n_1\hat{p}_1`,  :math:`n_1(1-\hat{p}_1)`, :math:`n_2\hat{p}_2`
     og  :math:`n_2(1-\hat{p}_2)`  eru öll stærri en 15 má reikna neðra
    öryggismark fyrir muninn á :math:`p_1` og :math:`p_2` með:
    
    .. math::
       \hat{p}_1 - \hat{p}_2 - z_{1-\alpha/2} \cdot
       \sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}
       :label: eq.tvopnedra
    
    og efra öryggismarkið með
    
    .. math::
       \hat{p}_1 - \hat{p}_2 + z_{1-\alpha/2} \cdot
       \sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}
       :label: eq.tvopefra
    
    þar sem :math:`\hat{p}_1 = \frac{x_1}{n_1}`,
    :math:`\hat{p}_2 = \frac{x_2}{n_2}` og :math:`z_{1-\alpha/2}` fæst með
    að fletta upp í töflu stöðluðu normaldreifingarinnar í kafla
    :ref:`T.1 <a.normaltafla>`.


--------------

Tilgátupróf fyrir hlutföll tveggja þýða
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Séu skilyrðin fyrir að nota normalnálgunina uppfyllt, þ.e.a.s. ef
     :math:`n_1\hat{p}_1`,  :math:`n_1(1-\hat{p}_1)`, :math:`n_2\hat{p}_2`
     og  :math:`n_2(1-\hat{p}_2)`  eru öll stærri en 15 má nota eftirfarandi
    tilgátupróf:
    
    Núlltilgátan er:
    
    .. math:: \text{H}_0: p_1 = p_2
    
    Prófstærðin er:
    
    .. math::
       \hspace{5mm}
       Z = \frac{\frac{X_1}{n_1} - \frac{X_2}{n_2}}{\sqrt{\hat p(1- \hat p)\left(\frac{1}{n_1} + \frac{1}{n_2} \right)}},
       \ \ \text{þar sem} \ \ \hat p = \frac{X_1 + X_2}{n_1 + n_2}
       :label: eq.tvopprof
    
    Ef núlltilgátan er sönn fylgir prófstærðin stöðluðu normaldreifingunni,
    eða :math:`Z \sim N(0,1)`. Gagntilgátan getur verið einhliða eða
    tvíhliða og má sjá þær ásamt höfnunarsvæðunum hér að neðan.
    
    +-----------------------------+--------------------------------------------------------------+
    | Gagntilgáta                 | Hafna :math:`H_0` ef:                                        |
    +=============================+==============================================================+
    | :math:`H_1: p_1 < p_2`      | :math:`Z < -z_{1-\alpha}`                                    |
    +-----------------------------+--------------------------------------------------------------+
    | :math:`H_1: p_1 > p_2`      | :math:`Z > z_{1-\alpha}`                                     |
    +-----------------------------+--------------------------------------------------------------+
    | :math:`H_1: p_1 \neq p_2`   | :math:`Z < -z_{1-\alpha/2}` eða :math:`Z > z_{1-\alpha/2}`   |
    +-----------------------------+--------------------------------------------------------------+


--------------

.. _e.tvop:

Sýnidæmi: Ályktanir um hlutföll tveggja þýða
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Skoðum aftur dæmi :numref:`%s <e.p>`. Við fáum nú að vita að í raun voru úrtökin
    tvö, 4375 konur og 4375 karlar. Niðurstaðan var að af þeim 8750 sem
    spurðir voru “styður þú ríkisstjórnina“ sögðu 4530 já og 4220 nei. Af
    þeim 4530 sem sögðust styðja ríkistjórnina voru 2337 konur. Finnið 95%
    öryggisbil fyrir mun á hlutföllum kvenna og karla sem styðja
    ríkisstjórnina og kannið hvort munur sé á hlutföllum kvenna og karla sem
    styðja ríkisstjórnina. Notið :math:`\alpha = 0.05`. Taka skal fram að
    þetta dæmi er uppspuni.
    
    Skilyrðin um normalnálgun eru uppfyllt þar sem  :math:`n_1\hat{p}_1`,
     :math:`n_1(1-\hat{p}_1)`,  :math:`n_2\hat{p}_2`  og
     :math:`n_2(1-\hat{p}_2)`  eru öll stærri en 15.
    
    Byrjum á að finna :math:`\hat{p}_1` og :math:`\hat{p}_2`. Gefið er í
    dæminu að fjöldi karla og fjöldi kvenna er jafn,
    :math:`n_1 = n_2 = 4375`. Einnig var gefið að fjöldi kvenna sem sagðist
    styðja ríkisstjórnina er 2337 og fjöldi karla því 4530-2337 = 2193, því
    eru :math:`x_1 = 2337` og :math:`x_2 = 2193`.
    
    Reiknum nú :math:`\hat{p}_1` og :math:`\hat{p}_2` með jöfnum
    :eq:`eq.p1hat` og :eq:`eq.p2hat`
    
    .. math::
       \hat{p}_1 = \frac{x_1}{n_1} = \frac{2337}{4375} = 0.5342 \ \ \text{og}
       \ \ \hat{p}_2 = \frac{x_2}{n_2} = \frac{2193}{4375} = 0.5013
    
    Nú má reikna neðra öryggismark með jöfnu :eq:`eq.tvopnedra`
    
    .. math::
       \hat{p}_1 - \hat{p}_2 - z_{1-\alpha/2} \cdot
       \sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}=
    
    .. math:: 0.5342 - 0.5013 - 1.96\sqrt{\frac{0.5342(1-0.5342)}{4375} + \frac{0.5013(1-0.5013)}{4375}} = 0.0119
    
    og efra öryggismark með jöfnu :eq:`eq.tvopefra`
    
    .. math::
       \hat{p}_1 - \hat{p}_2 + z_{1-\alpha/2} \cdot
       \sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}} =
    
    .. math:: 0.5342 - 0.5013 + 1.96\sqrt{\frac{0.5342(1-0.5342)}{4375} + \frac{0.5013(1-0.5013)}{4375}} = 0.0537
    
    Öryggisbilið má því skrifa sem
    
    .. math:: 0.0119 < \ p_1 - p_2 \ < 0.0537
    
    Til að kanna hvort munur sé á hlutföllunum förum við eftir samantektinni
    um framkvæmd tilgátuprófa.
    
    #) Við ætlum að álykta um mun á tveimur hlutföllum og notum við því próf
       fyrir mismun hlutfalla tveggja þýða. Við notum normalnálgun þar sem
        :math:`n_1 \hat{p}_1`,  :math:`n_1(1 - \hat{p}_1)`,
        :math:`n_2\hat{p}_2`  og  :math:`n_2(1-\hat{p}_2)`  eru öll stærri
       en 15.
    
    #) Við fengum uppgefið að nota :math:`\alpha = 0.05.`
    
    #) Við eigum að kanna hvort munur sé á hlutföllum karla og kvenna sem
       styðja ríkisstjórnina. Við notum því tvíhliða próf. Tilgáturnar eru:
    
       .. math::
          \begin{aligned}
          H_0&:& p_1 = p_2\\
          H_1&:& p_1 \neq p_2\end{aligned}
    
    #) Við vitum að :math:`\hat{p}_1 = 0.5342` og
       :math:`\hat{p}_2 = 0.5013`. Reiknum nú :math:`\hat p`, sjá jöfnu
       :eq:`eq.tvopprof`, þar sem :math:`\hat p` kemur fyrir í prófstærðinni
    
       .. math:: \hat p= \frac{x_1 + x_2}{n_1 + n_2} = \frac{4530}{8750} = 0.5177
    
       Prófstærðina má svo reikna með jöfnu :eq:`eq.tvopprof`
    
       .. math::
          z = \frac{\frac{x_1}{n_1} - \frac{x_2}{n_2}}{\sqrt{\hat p(1-\hat p)\left(\frac{1}{n_1} + \frac{1}{n_2} \right)}}
          = \frac{0.5342 - 0.5013}{\sqrt{0.5177(1-0.5177)\left(\frac{1}{4375} + \frac{1}{4375} \right)}} = 3.08
    
    #) Við notum töflu stöðluðu normaldreifingarinnar til að finna
       höfnunarsvæðin: :math:`z_{1-\alpha/2}` = :math:`z_{0.975}` = 1.96.
       Við höfnum því núlltilgátunni ef :math:`z> 1.96` eða ef
       :math:`z < -1.96`. Við sjáum að :math:`z> 1.96` svo prófstærðin
       fellur á höfnunarsvæði.
    
    #) Við höfnum núlltilgátunni og ályktum því að munur sé á hlutföllum
       kvenna og karla sem styðja ríkisstjórnina.
    
    .. figure:: myndir/ztvihlida196.svg

.. _s.fleirihlutfoll:

Ályktanir um hlutföll fleiri þýða
---------------------------------

Ályktanir um hlutföll fleiri þýða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tilgátuna úr síðasta hluta má útvíkka þannig að hægt sé að bera saman
hlutföll fleiri en tveggja þýða. Þá er ekki lengur hægt að nota aðferðir
byggðar á nálgun normaldreifingarinnar heldur er stuðst við svokölluð
kí-kvaðrat próf (:math:`\chi^2`-próf). Aðferðina má einnig nota þegar
bera á saman hlutföll tveggja þýða eins og í hlutanum hér að framan, þó
aðeins ef gagntilgátan er tvíhliða. Þá munu Kí-kvaðrat prófið og prófið
sem byggir á normalnálgun alltaf gefa sömu niðurstöðuna.

Tilgátuprófið í þessum hluta prófar hvort hlutföll allra :math:`d`
þýðanna séu jöfn. Hana ritum við :math:`H_0: p_1 = p_2 = ... = p_d`. Ef
við höfnum henni getum við ályktað að hlutföllin séu ekki öll jöfn hvort
öðru en það felur ekki endilega í sér að þau séu öll ólík. Beita þyrfti
þróaðri tölfræðiaðferðum, utan efni þessar bókar, til að komast að raun
um það.

Eins og áður þurfa viss skilyrði að vera uppfyllt til að beita megi
kí-kvaðrat prófi. Þeim skilyrðum er þó torvelt að lýsa án þess að þekkja
aðferðina og því munum við koma aftur að þeim síðar. Kí-kvaðrat
aðferðinni er sömuleiðis auðveldara að lýsa með dæmi en í orðum og förum
við því þá leið hér á eftir.

Áður en hægt er að framkvæma kí-kvaðrat próf er gott að búa til þrjár
töflur sem hjálpa okkur við að reikna prófstærðina sem notuð er í
prófinu. Í kassa :numref:`%s <em.ki-kvad-kassar>` má sjá hvernig búa má til
þessar þrjár töflur og í kassa :numref:`%s <em.ki-kvadprof>` má sjá tilgáturnar
og prófstærðina sem notuð er til að prófa tilgáturnar.

.. _em.ki-kvad-kassar:

Töflur fyrir kí-kvaðrat próf
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Þegar framkvæma á kí-kvaðrat próf er gott að búa til þrjár töflur:
    
    -  Tafla mældrar tíðni: Inniheldur tíðni sem við fáum úr rannsókninni,
       táknuð með :math:`o`.
    
    -  Tafla væntanlegrar tíðni: Inniheldur væntanlega tíðni, táknuð með
       :math:`e`. Gildin fást með því að margfalda samtalstölurnar úr töflu
       mældrar tíðni úr þeim dálki og þeirri línu sem við erum stödd í og
       deila með heildarfjölda. Allar tölur í þessari töflu verða að vera
       hærri en 5 annars er ekki hægt að nota prófið.
    
    -  Tafla prófstærðar: Inniheldur framlag til prófstærðar reiknað með
       :math:`\frac{(o-e)^2}{e}`. Að lokum eru allar tölurnar í töflu
       prófstærðar lagðar saman til að fá gildið á prófstærðinni (sjá kassa
       :numref:`%s <em.ki-kvadprof>`).


--------------

.. _em.ki-kvadprof:

Kí-kvaðrat próf fyrir hlutföll
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Tilgáturnar eru:
    
    .. math:: H_0: p_1 = p_2 = ... = p_d
    
    .. math:: H_1: \text{hlutföllin eru ekki öll jöfn}
    
    Prófstærðin er:
    
    .. math::
       \chi^2 = \sum_{i = 1}^{l}\sum_{j = 1}^{d} \frac{(o_{ij}-e_{ij})^2}{e_{ij}}
       :label: eq.kikvadrat2
    
    þar sem :math:`l` er fjöldi lína, :math:`d` er fjöldi dálka, :math:`o`
    er mæld tíðni og :math:`e` er væntanleg tíðni.
    
    Sé núlltilgátan sönn fylgir prófstærðin :math:`\chi^2`-dreifingu með
    (:math:`l` - 1) :math:`\cdot` (:math:`d` - 1) fjölda frígráða.
    
    Hafna skal núlltilgátunni sé
    :math:`\chi^2 > \chi^2_{1-\alpha,((l - 1) \cdot (d - 1))}`.


--------------

Þegar við vinnum með tvö þýði getum við hvort heldur notað aðferðina úr
síðasta hluta sem byggði á normalnálgun eða kí-kvaðrat próf. Notum nú
dæmið um ríkisstjórnina úr síðasta hluta (dæmi :numref:`%s <e.tvop>`) til að
skoða hvernig við búum til töflurnar þrjár sem við notum til að
framkvæma kí-kvaðrat prófið.

Tafla mældrar tíðni
^^^^^^^^^^^^^^^^^^^

Fjöldi kvenna í úrtaki var 4375, fjöldi í karla úrtaki var 4375, fjöldi
kvenna sem voru fylgjandi ríkisstjórninni voru 2337 og fjöldi karla sem
voru fylgjandi ríkisstjórninni voru 2139. Setjum nú þessar upplýsingar
sem við köllum mælda tíðni (e. observed frequency), upp í töflu. Köllum nú
þessa töflu *töflu mældrar tíðni* og táknum gildi hennar með :math:`o`.

+----------------------------------+------------+------------+------------+
| **Tafla mældrar tíðni**          | Konur      | Karlar     | Samtals    |
+==================================+============+============+============+
| Fylgjandi ríkisstjórninni        | **2337**   | **2193**   | **4530**   |
+----------------------------------+------------+------------+------------+
| Ekki fylgjandi ríkisstjórninni   | 2038       | 2182       | **4220**   |
+----------------------------------+------------+------------+------------+
| Samtals                          | **4375**   | **4375**   | **8750**   |
+----------------------------------+------------+------------+------------+

Látum :math:`d` tákna fjölda dálka í töflu sem þessari og :math:`l`
fjölda lína, að samtalsdálknum og samtalslínunni undanskildri. Þá köllum
við töflu sem þessa :math:`l`\ x\ :math:`d`-töflu. Taflan hér að ofan er
því 2x2-tafla.

Tafla væntanlegrar tíðni
^^^^^^^^^^^^^^^^^^^^^^^^

Því næst búum við til aðra töflu sem inniheldur svonefnda *væntanlega
tíðni* (e. expected frequency). Hún inniheldur þann fjölda sem búast mætti
við að sjá í hverjum hóp ef núlltilgátan væri sönn. Sú tafla er þar af
leiðandi af sömu stærð og tafla mældrar tíðni, í þessu tilviki 2x2.
Köllum þessa töflu *töflu væntanlegrar tíðni* og táknum gildi hennar með
:math:`e`.

Gildin í töflu væntanlegrar tíðni fást með því að margfalda
samtalstölurnar úr töflu mældrar tíðni úr þeim dálki og þeirri línu sem
við erum stödd í og deila með heildarfjölda. Skilyrðið sem þarf að gilda
til að framkvæma megi kí-kvaðrat próf er að tölurnar í þessari töflu séu
stærri en 5.

+----------------------------------+----------------------------------------------+----------------------------------------------+
| **Tafla væntanlegrar tíðni**     | Konur                                        | Karlar                                       |
+==================================+==============================================+==============================================+
| Fylgjandi ríkisstjórninni        | :math:`\frac{4375\cdot 4530}{8750} = 2265`   | :math:`\frac{4375\cdot 4530}{8750} = 2265`   |
+----------------------------------+----------------------------------------------+----------------------------------------------+
| Ekki fylgjandi ríkisstjórninni   | :math:`\frac{4375\cdot 4220}{8750} = 2110`   | :math:`\frac{4375\cdot 4220}{8750} = 2110`   |
+----------------------------------+----------------------------------------------+----------------------------------------------+

Tafla prófstærðar
^^^^^^^^^^^^^^^^^

Til að reikna út prófstærðina fyrir kí-kvaðrat prófið er best að búa til
töflu sem inniheldur framlag til prófstærðarinnar. Köllum hana *töflu
prófstærðar*. Taflan er að sömu stærð og töflunar hér að framan, í þessu
tilfelli 2x2. Fyrir hvert pláss í töflunni reiknum við
:math:`\frac{(o-e)^2}{e}` þar sem :math:`o` og :math:`e` eru gildin í
töflu mældrar tíðni og töflu væntanlegrar tíðni sem eru á sama stað í
töflunum og það gildi sem verið er að reikna út. Skoðum nú aftur fyrstu
töflurnar tvær og hvernig reikna má út gildin í töflu prófstærðar.

+------------------------------------+---------+----------+
| **Tafla mældrar tíðni** (:math:`o`)| Konur   | Karlar   |
+====================================+=========+==========+
| Fylgjandi                          | 2337    | 2193     |
+------------------------------------+---------+----------+
| Ekki fylgjandi                     | 2038    | 2182     |
+------------------------------------+---------+----------+

+-----------------------------------------+---------+----------+
| **Tafla væntanlegrar tíðni** (:math:`e`)| Konur   | Karlar   |
+=========================================+=========+==========+
| Fylgjandi                               | 2265    | 2265     |
+-----------------------------------------+---------+----------+
| Ekki fylgjandi                          | 2110    | 2110     |
+-----------------------------------------+---------+----------+

Reiknum nú gildin í töflu prófstærðar með :math:`\frac{(o-e)^2}{e}`.

+-------------------------+-----------------------------------------------+-----------------------------------------------+
| **Tafla prófstærðar**   | Konur                                         | Karlar                                        |
+=========================+===============================================+===============================================+
| Fylgjandi               | :math:`\frac{(2337 - 2265)^2}{2265} = 2.29`   | :math:`\frac{(2193 - 2265)^2}{2265} = 2.29`   |
+-------------------------+-----------------------------------------------+-----------------------------------------------+
| Ekki fylgjandi          | :math:`\frac{(2038 - 2110)^2}{2110} = 2.46`   | :math:`\frac{(2182 - 2110)^2}{2110} = 2.46`   |
+-------------------------+-----------------------------------------------+-----------------------------------------------+

Til að reikna prófstærðina þurfum við að lokum að leggja saman allar
tölurnar í töflu prófstærðar.

Sýnidæmi: Kí-kvaðrat próf - 2x2 tafla
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Skoðum aftur dæmið um ríkisstjórnina frá dæmi :numref:`%s <e.tvop>`. Kannið nú
    hvort munur sé á stuðningi við ríkisstjórnina milli kynja með að nota
    kí-kvaðrat próf.
    
    Í dæmi sem þessu þarf að byrja á að búa til töflurnar þrjár. Við höfum
    þegar gert það fyrir þessi gögn og getum við því hafist handa við
    tilgátuprófið.
    
    #) Við ætlum að álykta um mun á tveimur hlutföllum með að nota
       kí-kvaðrat próf. Í töflunni fyrir væntanlega tíðni eru allar tölurnar
       stærri en 5 og því er í lagi að nota prófið.
    
    #) Notum :math:`\alpha = 0.05.`
    
    #) Við eigum að kanna hvort munur sé á hlutfalli karla og kvenna sem
       styðja ríkisstjórnina. Við notum því tvíhliða próf. Tilgáturnar eru:
    
       .. math::
          \begin{aligned}
          H_0&:& p_1 = p_2\\
          H_1&:& p_1 \neq p_2\end{aligned}
    
    #) Við notum töflu prófstærðar til að finna gildin sem fara inn í
       útreikningana fyrir prófstærðina. Prófstærðin er:
    
       .. math:: \chi^2 = \sum \sum \frac{(o-e)^2}{e} = 2.29 + 2.29 + 2.46 + 2.46 = 9.50
    
    #) Við flettum upp í kí-kvaðrat töflu með einni frígráðu til að finna
       höfnunarsvæðið. :math:`\chi^2_{1-\alpha,((l-1)\cdot(d-1))}` =
       :math:`\chi^2_{0.95,(1)}` = 3.84. Við höfnum því núlltilgátunni ef
       :math:`\chi^2> 3.84`. Við sjáum að :math:`\chi^2> 3.84` svo
       prófstærðin fellur á höfnunarsvæði.
    
    #) Við höfnum núlltilgátunni og ályktum því að munur sé á hlutfalli
       kvenna og karla sem styðja ríkisstjórnina.
    
    .. figure:: myndir/chisqdf1.svg

Aðferðirnar tvær, að nota normalnálgun og kí-kvaðrat prófið, munu alltaf
gefa sömu niðurstöðu. Það gildir nefnilega að kí-kvaðrat prófstærðin er
jöfn z-prófstærðinni í öðru veldi. Skoðum nú annað dæmi þar sem hóparnir
sem við erum að skoða eru fleiri en 2.

Sýnidæmi: Kí-kvaðrat próf - 2x3 tafla
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Eftirfarandi gögn eru niðurstöður könnunar þar sem slembiúrtak úr þremur
    ráðuneytum hér á landi var tekið og fólk spurt hvort það væri ánægt með
    eftirlaunaáætlun ríkisins. Úrtak af stærð 100 var tekið úr fyrsta
    ráðuneytinu og úrtök af stærð 150 úr hinum tveimur.
    
    +-------------------------+---------------+---------------+---------------+
    |                         | Ráðuneyti 1   | Ráðuneyti 2   | Ráðuneyti 3   |
    +=========================+===============+===============+===============+
    | Ánægt með áætlun        | 66            | 85            | 108           |
    +-------------------------+---------------+---------------+---------------+
    | Ekki ánægt með áætlun   | 34            | 65            | 42            |
    +-------------------------+---------------+---------------+---------------+
    
    Í dæmi sem þessu þarf að byrja á að búa til töflurnar þrjár. Fyrsta
    taflan er sú sama og hér að ofan nema við bætum við samtalsdálki og
    -línu.
    
    +------------------------------+---------------+---------------+---------------+-----------+
    | **Mæld tíðni** - :math:`o`   | Ráðuneyti 1   | Ráðuneyti 2   | Ráðuneyti 3   | Samtals   |
    +==============================+===============+===============+===============+===========+
    | Ánægt                        | 66            | 85            | 108           | 259       |
    +------------------------------+---------------+---------------+---------------+-----------+
    | Ekki ánægt                   | 34            | 65            | 42            | 141       |
    +------------------------------+---------------+---------------+---------------+-----------+
    | Samtals                      | 100           | 150           | 150           | 400       |
    +------------------------------+---------------+---------------+---------------+-----------+
    
    Gildin í töflu væntanlegrar tíðni fást með því að margfalda
    samtalstölurnar úr töflu mældrar tíðni úr þeim dálki og þeirri línu sem
    við erum stödd í og deila með heildarfjölda.
    
    +-----------------------------------+--------------------------------------------+--------------------------------------------+--------------------------------------------+
    | **Væntanleg tíðni** - :math:`e`   | Ráðuneyti 1                                | Ráðuneyti 2                                | Ráðuneyti 3                                |
    +===================================+============================================+============================================+============================================+
    | Ánægt                             | :math:`\frac{100\cdot 259}{400} = 64.75`   | :math:`\frac{150\cdot 259}{400} = 97.13`   | :math:`\frac{150\cdot 259}{400} = 97.13`   |
    +-----------------------------------+--------------------------------------------+--------------------------------------------+--------------------------------------------+
    | Ekki ánægt                        | :math:`\frac{100\cdot 141}{400} = 35.25`   | :math:`\frac{150\cdot 141}{400} = 52.88`   | :math:`\frac{150\cdot 141}{400} = 52.88`   |
    +-----------------------------------+--------------------------------------------+--------------------------------------------+--------------------------------------------+
    
    Reiknum nú gildin í töflu prófstærðar með :math:`\frac{(o-e)^2}{e}`
    
    +-----------------+---------------------------------------------+---------------------------------------------+----------------------------------------------+
    | **Prófstærð**   | Ráðuneyti 1                                 | Ráðuneyti 2                                 | Ráðuneyti 3                                  |
    +=================+=============================================+=============================================+==============================================+
    | Ánægt           | :math:`\frac{(66-64.75)^2}{64.75} = 0.02`   | :math:`\frac{(85-97.13)^2}{97.13} = 1.51`   | :math:`\frac{(108-97.13)^2}{97.13} = 1.22`   |
    +-----------------+---------------------------------------------+---------------------------------------------+----------------------------------------------+
    | Ekki ánægt      | :math:`\frac{(34-35.25)^2}{35.25} = 0.04`   | :math:`\frac{(65-52.88)^2}{52.88} = 2.78`   | :math:`\frac{(42-52.88)^2}{52.88} = 2.24`    |
    +-----------------+---------------------------------------------+---------------------------------------------+----------------------------------------------+
    
    Nú erum við tilbúin að hefjast handa við tilgátuprófið.
    
    #) Við ætlum að álykta um mun á þremur hlutföllum með því að nota
       kí-kvaðrat próf. Í töflunni fyrir væntanlega tíðni eru allar tölurnar
       stærri en 5 og því er í lagi að nota prófið.
    
    #) Notum :math:`\alpha = 0.05.`
    
    #) Við eigum að kanna tilgátuna hvort munur sé milli ráðuneyta á ánægju
       með eftirlaunaáætlun. Tilgáturnar eru:
    
       .. math::
          \begin{aligned}
          H_0&:& p_1 = p_2 = p_3\\
          H_1&:& \text{$p_1, p_2, p_3,$ eru ekki öll jöfn}\end{aligned}
    
    #) Við notum töflu prófstærðar til að finna gildin sem fara inn í
       útreikningana fyrir prófstærðina. Prófstærðin er:
    
       .. math::
          \begin{aligned}
          \chi^2 = & \sum \sum \frac{(o-e)^2}{e} = 0.02 + 1.51 + 1.22 + 0.04 + 2.78 + 2.24\\
          = & 7.81 \end{aligned}
    
    #) Við flettum upp í kí-kvaðrat töflu með tveimur frígráðum til að finna
       höfnunarsvæðið. :math:`\chi^2_{1-\alpha,((l-1)\cdot(d-1))}` =
       :math:`\chi^2_{0.95,(2)}` = 5.99. Við höfnum því núlltilgátunni ef
       :math:`\chi^2 > 5.99`. Við sjáum að :math:`\chi^2> 5.99` svo
       prófstærðin fellur á höfnunarsvæði.
    
    #) Við höfnum núlltilgátunni og ályktum því að munur sé á hlutfalli
       þeirra sem eru ánægðir með eftirlaunaáætlunina í ráðuneytunum þremur.
    
    .. figure:: myndir/chisqdf2.svg
        :align: center
        :alt: Mynd

Mátgæðapróf
~~~~~~~~~~~

Aðferðina í þessum hluta má einnig nota til að framkvæma svokölluð
*mátgæðapróf* (e. goodness of fit tests). Þeim prófum beitum við þegar
við höfum fyrirfram ákveðnar kenningar um það hver hlutföllin
:math:`p_1, \ldots, p_d` eigi að vera og við viljum kanna hvort að
mælingarnar okkar samræmist þeirri kenningu.

Tilgátuprófið er framkvæmt á nákvæmlega sama hátt, nema það verður
einfaldara að reikna væntanlegu tíðnina, :math:`e`, í töflu væntanlegrar
tíðni. Væntanlega tíðnin í hverjum dálki er einfaldlega
:math:`n\cdot p_i`, þ.e. heildarfjöldi mælinga sinnum það hlutfall sem
við gerum ráð fyrir að gildi fyrir þennan flokk. Prófstærðin er reiknuð
á sama hátt en núna miðum við hana við gildið
:math:`\chi^2_{1-\alpha, d-1}`.

Mátgæðapróf eru sérstök að því leyti að við viljum yfirleitt ekki hafna
núlltilgátunni. Við notum þau því ekki til að draga miklar ályktanir,
því ef við höfum fáar mælingar höfum við sennilega of lítinn styrk til
að hafna núlltilgátunni þrátt fyrir að hún sé í raun ósönn og ef við
höfum margar mælingar getum við hafnað núlltilgátunni þrátt fyrir að
frávikin séu ekki ýkja mikil. Því notum við mátgæðapróf eingöngu til að
fá vísbendingu um hvort niðurstöðurnar séu nokkuð í hrópandi mótsögn við
kenningarnar okkar.

.. _s.tengslatoflur:

Tengslatöflur
-------------

Tengslatöflur
~~~~~~~~~~~~~

Í hluta :numref:`%s <s.fleirihlutfoll>` sáum við hvernig bera má saman skiptingu
flokkabreytu í mismunandi þýðum. Í þessum hluta munum við sjá hvernig
bera má saman tvær flokkabreytur þar sem gögnum er aflað úr sama þýðinu.
Til þess eru notaðar svokallaðar tengslatöflur og prófin ganga út á að
svara spurningunni hvort breyturnar tvær séu óháðar. Prófstærðin sem
notast er við er sú sama og áður og eru allir útreikningar því eins.
Tilgáturnar eru þó settar fram á annan máta.

Eins og í hluta :numref:`%s <s.fleirihlutfoll>` má ekki framkvæma tilgátuprófið
ef einhverjar tölur í töflu væntanlegrar tíðni eru minni en fimm. Þá má
annað hvort framkvæma *endurvalsaðferð* til að framkvæma prófið eða þá
að framkvæma *Fishers próf*. Þær aðferðir er sem fyrr ekki hægt að
framkvæma í höndunum. Einnig er algengt að fara þá leið að *sameina suma
flokka* annarrar eða beggja flokkabreytanna eins og lýst var í
undirkafla :numref:`%s <ss.nyjarbreytur>`. Er það einungis gert ef að skipting
flokkanna í flokkabreytunni var óþarflega fín og flokkarnir tveir eða
fleiri sem sameinaðir eru séu mjög líkir að eiginleikum.

Tengslatöflur (contingency tables)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Tengslatöflur eru notaðar til að kanna hvort samband sé á milli tveggja
    flokkabreyta . Tilgáturnar eru
    
    .. math::
       \begin{aligned}
       H_0&:& \text{Það er ekki samband á milli breytanna tveggja}\\
       H_1&:& \text{Það er samband á milli breytanna tveggja}\end{aligned}
    
    Prófstærðin er
    
    .. math::
       \chi^2 = \sum_{i = 1}^{l}\sum_{j = 1}^{d} \frac{(o_{ij}-e_{ij})^2}{e_{ij}}
       :label: eq.kikvadrat
    
    þar sem :math:`l` er fjöldi lína, :math:`j` er fjöldi dálka, :math:`o`
    er mæld tíðni og :math:`e` er væntanleg tíðni. Sé núlltilgátan sönn
    fylgir prófstærðin :math:`\chi^2`-dreifingu með (:math:`l` - 1)
    :math:`\cdot` (:math:`d` - 1) fjölda frígráða. Hafna skal núlltilgátunni
    sé :math:`\chi^2 > \chi^2_{1-\alpha,((l - 1) \cdot (d - 1))}`.


--------------

Sýnidæmi: Tengslatöflur
^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Fyrirtæki hafði áhuga á að kanna hvort það væri samband á milli þess
    hvernig starfsmenn stæðu sig í þjálfunarprógrammi og hvernig þeir stæðu
    sig svo í vinnunni. Til að kanna hvort svo væri var tekið slembiúrtak af
    stærð 400. Niðurstöðurnar má sjá hér að neðan.
    
    +---------+----------------+--------------------+---------+---------------+
    |         |                |                 Þjálfunarprógram             |
    +---------+----------------+--------------------+---------+---------------+
    |         |                | Neðan meðals       | Meðal   | Ofan meðals   |
    +---------+----------------+--------------------+---------+---------------+
    |         | Neðan meðals   | 24                 | 59      | 29            |
    +         +----------------+--------------------+---------+---------------+
    | Vinna   | Meðal          | 24                 | 79      | 64            |
    +         +----------------+--------------------+---------+---------------+
    |         | Ofan meðals    | 12                 | 49      | 60            |
    +---------+----------------+--------------------+---------+---------------+
    
    Kannið með viðeigandi tilgátuprófi hvort samand sé á milli hvernig
    starfsmenn stæðu sig í þjálfunarprógrammi og hvernig þeir stæðu sig svo
    í vinnunni.
    
    Byrjum á að búa til töflurnar þrjár. Fyrsta taflan er sú sama og hér að
    ofan nema við bætum við samtalsdálki og -línu.
    
    +------------------------------+----------------+---------+---------------+-----------+
    | **Mæld tíðni** - :math:`o`   | Neðan meðals   | Meðal   | Ofan meðals   | Samtals   |
    +==============================+================+=========+===============+===========+
    | Neðan meðals                 | 24             | 59      | 29            | 112       |
    +------------------------------+----------------+---------+---------------+-----------+
    | Meðal                        | 24             | 79      | 64            | 167       |
    +------------------------------+----------------+---------+---------------+-----------+
    | Ofan meðals                  | 12             | 49      | 60            | 121       |
    +------------------------------+----------------+---------+---------------+-----------+
    | Samtals                      | 60             | 187     | 153           | 400       |
    +------------------------------+----------------+---------+---------------+-----------+
    
    Gildin í töflu væntanlegrar tíðni fást með því að margfalda
    samtalstölurnar úr töflu mældrar tíðni úr þeim dálki og þeirri línu sem
    við erum stödd í og deila með heildarfjölda.
    
    +-----------------------------------+--------------------------------------------+---------------------------------------------+---------------------------------------------+
    | **Væntanleg tíðni** - :math:`e`   | Neðan meðals                               | Meðal                                       | Ofan meðals                                 |
    +===================================+============================================+=============================================+=============================================+
    | Neðan meðals                      | :math:`\frac{60 \cdot 112}{400} = 16.80`   | :math:`\frac{187 \cdot 112}{400} = 52.36`   | :math:`\frac{153 \cdot 112}{400} = 42.84`   |
    +-----------------------------------+--------------------------------------------+---------------------------------------------+---------------------------------------------+
    | Meðal                             | :math:`\frac{60 \cdot 167}{400} = 25.05`   | :math:`\frac{187 \cdot 167}{400} = 78.07`   | :math:`\frac{153 \cdot 167}{400} = 63.88`   |
    +-----------------------------------+--------------------------------------------+---------------------------------------------+---------------------------------------------+
    | Ofan meðals                       | :math:`\frac{60 \cdot 121}{400} = 18.15`   | :math:`\frac{187 \cdot 121}{400} = 56.57`   | :math:`\frac{153 \cdot 121}{400} = 46.28`   |
    +-----------------------------------+--------------------------------------------+---------------------------------------------+---------------------------------------------+
    
    Reiknum gildin í töflu prófstærðar með :math:`\frac{(o-e)^2}{e}`
    
    +-----------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | **Prófstærð**   | Neðan meðals                                  | Meðal                                         | Ofan meðals                                   |
    +=================+===============================================+===============================================+===============================================+
    | Neðan meðals    | :math:`\frac{(24 - 16.80)^2}{16.80} = 3.09`   | :math:`\frac{(59 - 52.36)^2}{52.36} = 0.84`   | :math:`\frac{(29 - 42.84)^2}{42.84} = 4.47`   |
    +-----------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | Meðal           | :math:`\frac{(24 - 25.05)^2}{25.05} = 0.04`   | :math:`\frac{(79 - 78.07)^2}{78.07} = 0.01`   | :math:`\frac{(64 - 63.88)^2}{63.88} = 0.00`   |
    +-----------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | Ofan meðals     | :math:`\frac{(12 - 18.15)^2}{18.15} = 2.08`   | :math:`\frac{(49 - 56.57)^2}{56.57} = 1.01`   | :math:`\frac{(60 - 46.28)^2}{46.28} = 4.07`   |
    +-----------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    
    Nú erum við tilbúin að hefjast handa við tilgátuprófið.
    
    #) Við höfum tengslatöflu og notum því kí-kvaðrat próf. Við höfum
       tengslatöflu því við erum að kanna hvort samband sé á milli tveggja
       breyta í einu þýði. Í töflunni fyrir væntanlega tíðni eru allar
       tölurnar stærri en 5 og því er í lagi að nota prófið.
    
    #) Notum :math:`\alpha = 0.05.`
    
    #) Við eigum að kanna hvort samband sé á milli árangurs í
       þjálfunarprógrammi og vinnu. Tilgáturnar eru:
    
       .. math::
          \begin{aligned}
          H_0&:& \text{Það er ekki samband á milli frammistöðu í þjálfun og vinnu}\\
          H_1&:& \text{Það er samband á milli frammistöðu í þjálfun og vinnu}\end{aligned}
    
    #) Við notum töflu prófstærðar til að finna gildin sem fara inn í
       útreikningana fyrir prófstærðina. Prófstærðin er:
    
       .. math::
          \begin{aligned}
          \chi^2 &= \sum \sum \frac{(o-e)^2}{e} = 3.09 + 0.84 + 4.47 \\
          &+ 0.04 + 0.01 + 0.00 + 2.09 + 1.01 + 4.07 = 15.62 \end{aligned}
    
    #) Við flettum upp í kí-kvaðrat töflu með fjórum frígráðum til að finna
       höfnunarsvæðið. :math:`\chi^2_{1-\alpha,((l-1)\cdot(d-1))}` =
       :math:`\chi^2_{0.95,(4)}` = 9.488. Við höfnum því núlltilgátunni ef
       :math:`\chi^2 > 9.488`. Við sjáum að :math:`\chi^2 > 9.488` svo
       prófstærðin fellur á höfnunarsvæði.
    
    #) Við höfnum núlltilgátunni og ályktum því að samband sé á milli
       frammistöðu í þjálfunarprógrammi og vinnu.
    
    .. figure:: myndir/chisqdf4.svg
        :align: center
        :alt: Mynd

Dæmi
----

Dæmi
~~~~

Í tilraun með áhrif mismunandi fóðrunar á frjósemi sauðfjár voru tveir
fóðurflokkar kannaðir, A og B og fékkst eftirfarandi fjöldi einlembdra
og tvílembdra áa í hvorum flokki:

+--------------+------------------+------------------+
|              | Fóðurflokkur A   | Fóðurflokkur B   |
+==============+==================+==================+
| Einlembdar   | 60               | 82               |
+--------------+------------------+------------------+
| Tvílembdar   | 132              | 108              |
+--------------+------------------+------------------+

Kannið með viðeigandi tilgátuprófi hvort munur sé á milli frjósemi eftir
fóðurflokkum. Notið :math:`\alpha = 0.05`.

Dæmi
~~~~

Um áramótin 2009 var gerð könnun meðal 2500 landsmanna um afstöðu þeirra
til byggingar Norðlingaölduveitu. Niðurtöður könnunarinnar var sú að
1577 sögðust hlynntir og 923 á móti. Finnið 95% öryggisbil fyrir
hlutfall landsmanna sem hlyntir eru Norðlingaölduveitu.

Dæmi
~~~~

Skólayfirvöld í skóla nokkrum höfðu stóðu fyrir tilraun þar sem 230
stúdentar voru valdir af handahófi og þeir spurðir tveggja spurninga.
Fyrri spurningin var hvort þau ættu börn eða ekki og sú seinni var hvort
þau væru í fullu námi eða ekki. Niðurstöðurnar má sjá hér að neðan:

+-----------------------+----------+---------------+
| Tafla mældrar tíðni   | Á börn   | Á ekki börn   |
+=======================+==========+===============+
| Í fullu námi          | 31       | 170           |
+-----------------------+----------+---------------+
| Ekki í fullu námi     | 15       | 14            |
+-----------------------+----------+---------------+

Skólayfirvöld í skólanum ætla nú að greina þessi gögn með kí-kvaðrat
prófi.

a) Hér að neðan má sjá töflu væntanlegrar tíðni en það vantar eitt
   gildi. Hvert er gildið?

   +----------------------------+----------+---------------+
   | Tafla væntanlegrar tíðni   | Á börn   | Á ekki börn   |
   +============================+==========+===============+
   | Í fullu námi               |          | 160.8         |
   +----------------------------+----------+---------------+
   | Ekki í fullu námi          | 5.8      | 23.2          |
   +----------------------------+----------+---------------+

#) Hér að neðan má sjá töflu prófstærðar en það vantar eitt gildi. Hvert
   er gildið?

   +---------------------+----------+---------------+
   | Tafla prófstærðar   | Á börn   | Á ekki börn   |
   +=====================+==========+===============+
   | Í fullu námi        | 2.105    | 0.526         |
   +---------------------+----------+---------------+
   | Ekki í fullu námi   | 14.593   |               |
   +---------------------+----------+---------------+

#) Hvaða gagntilgáta er viðeigandi fyrir gögn af þessu tagi?

Dæmi
~~~~

Lalli lífefnafræðingur er að vinna með 4x4 tengslatöflu. Hversu margar
frígráður hefur prófstærðin sem hann á að nota?

Dæmi
~~~~

8. apríl 2011 stóð fyrirtæki nokkurt fyrir skoðanakönnun þar sem spurt
var: ,,Ef kosið yrði um nýjustu Icesave lögin í dag, hvort myndir þú
kjósa með eða á móti?“ 722 tóku afstöðu og af þeim sögðust 414 ætla að
kjósa á móti lögunum. Göngum út frá að tilrunahögunin hafi verið í lagi.

a) Hvert er mat þitt á hlutfalli kjósenda sem ætluðu sér að kjósa á móti
   lögunum?

#) Finnið neðra mark 95% öryggisbils fyrir hlutfall kjósenda sem ætluðu
   sér að kjósa á móti lögunum.

Dæmi
~~~~

Fyrirtæki hér í bæ stóð fyrir skoðanakönnun þar sem fylgi forsetans var
kannað. 200 einstaklingar sem búsettir eru á landsbyggðinni og 200
einstaklingar búsettir á höfuðborgasvæðinu voru spurðir hvort þeir
styðji forsetann. Af þeim einstaklingum sem búsettir eru á
landsbyggðinni sögðust 108 styðja forsetann en 95 af þeim sem búa á
höfuðborgarsvæðinu.

a) Finnið efra mark 95% öryggisbils fyrir mun á hlutfalli þeirra sem
   styðja forsetann á landsbyggðinni og hlutfalli þeirra sem styðja
   forsetann á höfuðborgarsvæðinu.

#) Hvert er höfnunarsvæðið ef kanna á hvort hlutfall fólks sem styður
   forsetann sé mismunandi á landsbyggðinni og á höfuðborgarsvæðinu
   (notið :math:`\alpha = 0.05`)?

Dæmi
~~~~

Í boltalandinu í IKEA eru rauðir og bláir boltar. Siggi sæti veltir
fyrir sér hvort jafnmargir boltar séu af hvorum lit og ákveður að nota
tölfræðiþekkingu sína til að rannsaka það. Hann velur af handahófi 200
bolta og telur allar rauðu boltana. Boltalandið í IKEA er mjög stórt og
þar eru miklu fleiri en 200 boltar. Í úrtakinu hans Sigga sæta voru 104
rauðir boltar.

a) Hvert er mat Sigga sæta á hlutfalli rauðra bolta í boltalandinu?

#) Hvert er :math:`95\%`-öryggisbil fyrir hlutfall rauðra bolta?

Dæmi
~~~~

Til að kanna hvort hlutfall karla og kvenna með of hátt kólestról í
blóðinu sé mismunandi hátt voru valdir af handahófi 500 karlmenn og 600
konur og kólesteról í blóði þeirra mælt. 131 karlmaður mældist með of
hátt kólesteról og 118 konur. Kannið með viðeigandi tilgátuprófi hvort
hlutfall karla með of hátt kólesteról í blóði sé frábrugðið hlutfalli
kvenna. (:math:`\alpha = 0.05`).

Dæmi
~~~~

Skoðunarkönnun var framkvæmd í Bandaríkjunum til að kanna hvort samaband
væri á milli kyns og stjórnmálaskoðana. 300 manns tóku þátt í könnuninni
og talið hversu margir konur og karlar kjósa Demókrata, Repúblikana og
voru óháðir. Niðurstöðurnar má sjá hér að neðan:

+--------+-------------+---------------+----------+
|        | Demókrati   | Repúblikani   | Óháður   |
+========+=============+===============+==========+
| Kona   | 68          | 56            | 32       |
+--------+-------------+---------------+----------+
| Karl   | 52          | 72            | 20       |
+--------+-------------+---------------+----------+

Kannið með viðeigandi tilgátuprófi hvort samband sé á milli kyns og
stjórnmálaskoðana. Notið :math:`\alpha = 0.05`.
