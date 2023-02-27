.. _c.tvikostaadhvarfsgreining:

Tvíkosta aðhvarfsgreining
=========================

Í kafla :numref:`%s <c.adhvarfsgreining>` kynntumst við því hvernig línuleg
aðhvarfsgreining er framkvæmd til að kanna samband svarbreytu og
skýribreytu hennar. Línulegri aðhvarfsgreiningu má einungis beita þegar
svarbreytan er samfelld en er ekki boðleg þegar svarbreytan er mjög
strál. Hins vegar er afar algengt að verkefni okkar fjalli um strjálar
svarbreytur og þá sérstaklega *tvíkosta* breytur (e. binary variables),
en svo kallast breytur sem taka einungis tvö gildi. Í þeim tilvikum
kemur *tvíkosta aðhvarfsgreining* (e. logistic regression) til bjargar.

Við byrjum á að kynnast fræðilegri undirstöðu tvíkosta
aðhvarfsgreiningarlíkansins og þá sérstaklega ákveðið *tengifall* (e. link
function) sem á ensku kallast the logit function í kafla :numref:`%s <c.logit>`.
Í kafla :numref:`%s <c.logitstrjal>` munum við framkvæma tvíkosta
aðhvarfsgreiningu þar sem skýribreytan er líka strjál og sjá hvernig
gagnlíkindahlutföll skjótast út úr líkaninu. Í kafla
:numref:`%s <c.logitsamfelld>` munum við gera slíkt hið sama fyrir samfelldar
skýribreytur. Að lokum verður fjallað um hvernig reikna má líkur út frá
metnum stikum í tvíkosta aðhvarfsgreiningarlíkani í kafla
:numref:`%s <c.logitlikur>`.

.. _c.logit:

Tvíkosta aðhvarfsgreiningarlíkanið
----------------------------------

Tvíkosta aðhvarfsgreiningarlíkanið
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Í tvíkosta aðhvarfsgreiningu gerum við ráð fyrir að gildin tvö sem
svarbreytan getur tekið séu gildin 0 og 1, þ.e.a.s. talan núll stendur
fyrir annan möguleikann en talan einn hinn. Til samanburðar gat
svarbreytan í línulegri aðhvarfsgreiningu tekið hvaða gildi sem er. Í
línulegri aðhvarfsgreiningu lýstum við sambandi svarbreytu og
skýribreytu með jöfnu beinnar línu, :math:`y = \beta_0 + \beta_1 x`
(jafna :eq:`eq.jafnabeinnarlinu`). Sú framsetning er hins vegar ótæk
þegar útkoman er tvíkosta, því þá eru útkomurnar víðsfjarri því að detta
á beina línu, gildið á :math:`y` ás er annað hvort núll eða einn og
ekkert þar á milli.

Ein leið til að brúa þetta bil er með aðstoð svokallaðs *tengifalls* (e.
link funcion). Algengast er að nota ákveðið tengifall sem á ensku
kallast logistic fallið en ekki hefur gengið vel að þýða á íslensku.

Tengifall (link function)
^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Tengifallið
    
    .. math::
       p(t) = \frac{e^t}{1+e^t}
       :label: eq.tengifall
    
    varpar hvaða tölu sem er yfir í gildi á milli 0 og 1. Andhverfa þess er
    
    .. math::
       g(p) = \log \left( \frac{p}{1-p} \right)
       :label: eq.logit


--------------

Með aðstoð tengifallsins opnast nýr möguleiki, með því að stinga
útkomunni úr aðhvarfslínunni inn í tengifallið tryggjum við að útkoman
verði á milli 0 og 1. Þannig getum við notað aðhvarfsgreiningu til að
meta *líkurnar* á að svarbreytan okkar taki gildið 1. Á þessu byggir
tvíkosta aðhvarfsgreining.

.. _em.tvikostaadhvarf:

Tvíkosta aðhvarfsgreiningarlíkanið (logistic regression model)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Tvíkosta aðhvarfsgreiningarlíkanið er
    
    .. math::
       \log \left( \frac{p}{1-p} \right)  = \beta_0 + \beta_1 x + \varepsilon
       :label: eq.tvikostaadhvarf
    
    þar sem :math:`p` eru líkurnar á því að svarbreytan taki gildið 1.


--------------

Takið eftir því að á vinstri hlið jöfnu :eq:`eq.tvikostaadhvarf` stendur
lógarithminn af stærðinni :math:`\frac{p}{1-p}` sem er einmitt
gagnlíkindin á því að svarbreytan taki gildið 1. Gagnlíkindum kynntumst
við í kassa :numref:`%s <em.gagnlikindi>` í kafla :numref:`%s <ss.gagnlikindahlutfall>`.

.. _c.logitsamfelld:

Tvíkosta aðhvarfsgreining með samfelldri skýribreytu
----------------------------------------------------

Tvíkosta aðhvarfsgreining með samfelldri skýribreytu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _em.logsamfelld:

Tvíkosta aðhvarf með samfelldri skýribreytu (logistic regression with a continuous explanatory variable)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Gerum ráð fyrir að sambandi skýribreytunnar :math:`x` og því svarbreyta
    taki gildið 1 megi lýsa með tvíkosta aðhvarfsgreiningarlíkaninu
    
    .. math:: \log \left( \frac{p}{1-p} \right)  = \beta_0 + \beta_1 x + \varepsilon
    
    Þá er gagnlíkindahlutfallið á því að svarbreytan taki gildið 1 fyrir
    hverja :math:`a` eininga hækkun á skýribreytunni metið með
    :math:`e^{\hat \beta_1 a}`.


--------------

Sýnidæmi: Tvíkosta aðhvarfsgreining með samfelldri skýribreytu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Jói kannar hvort nemendur sem stunda mikla líkamsrækt séu líklegri til
    að reykja heldur en þeir sem stunda litla líkamsrækt. Hann metur
    tvíkosta aðhvarfsgreiningarlíkan til að kanna sambandið þar sem
    skýribreytan er fjöldi klukkustunda sem nemendur stunda líkamsrækt á
    viku. Hann mat stuðlana sem
    
    .. math::
       \begin{aligned}
       \hat \beta_0 &= -1.7428, \\
       \hat \beta_1 &= -0.1164 \end{aligned}
    
    Hvert er gagnlíkindahlutfall þess að nemandi sem stundar líkamsrækt í 8
    klukkustundir á viku reyki sígarettur á móti þeim sem stundar líkamsrækt
    í 5 klukkustundir á viku?
    
    Fyrri nemandinn stundar :math:`8-5 = 3` klukkustundum meiri líkamsrækt í
    viku heldur en sá seinni. Því er gagnlíkindahlutfall þess að hann reyki
    á móti hinum nemandanum gefið með
    
    .. math:: e^{\hat \beta_1} = e^{-0.1164 \cdot 3 } =  e^{-0.3492 } = 0.7052521
    
    Þar sem gagnlíkindahlutfallið er minna en einn minnka líkurnar á því að
    nemendur reyki eftir því sem þeir stunda meiri líkamsrækt.

.. _c.logitstrjal:

Tvíkosta aðhvarfsgreining með strjálli skýribreytu
--------------------------------------------------

Tvíkosta aðhvarfsgreining með strjálli skýribreytu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Þegar skýribreyta tvíkostaaðhvarfsgreiningarlíkans er strál er litið á
einn flokk breytunnar sem viðmiðunarflokk en stuðlar líkansins meta
frávik frá þessum viðmiðunarflokki.

.. _em.logstrjal:

Tvíkosta aðhvarf með strjálli skýribreytu (logistic regression with a discrete explanatory variable)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Gerum ráð fyrir að sambandi skýribreytunnar :math:`x` og því svarbreyta
    taki gildið 1 megi lýsa með tvíkosta aðhvarfsgreiningarlíkaninu
    
    .. math:: \log \left( \frac{p}{1-p} \right)  = \beta_0 + \beta_a I_{x=a} + \varepsilon
    
    þar sem :math:`I_{x=a}` er 1 ef :math:`x=a` en núll annars. Þá er
    gagnlíkindahlutfallið á því að svarbreytan taki gildið 1 þegar
    skýribreytan :math:`x` tekur gildið :math:`a` á móti því þegar hún tekur
    viðmiðunargildið metið með :math:`e^{\hat \beta_a}`.


--------------

Sýnidæmi: Tvíkosta aðhvarfsgreining með strjálli skýribreytu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Guðný kannar hvort nemendur sem drekka áfengi séu líklegri til að reykja
    heldur en þeir sem ekki drekka áfengi. Hún metur tvíkosta
    aðhvarfsgreiningarlíkan til að kanna sambandið og metur gildi stuðlanna
    sem
    
    .. math::
       \begin{aligned}
       \hat \beta_0 &= -4.248, \\
       \hat \beta_a &= 2.235 \end{aligned}
    
    Þeir nemendur sem ekki drukku áfengi töldust til viðmiðunarflokksins.
    Hvert er gagnlíkindahlutfall þess að nemandi sem drekkur áfengi reyki
    sígarettur á móti þeim sem ekki drekkur áfengi?
    
    Gagnlíkindahlutfall þess að nemandi sem drekkur áfengi reyki sígarettur
    á móti þeim sem ekki drekkur áfengi er gefið með
    
    .. math:: e^{\hat \beta_a} = e^{2.235} = 9.346482
    
    Þar sem gagnlíkindahlutfallið er stærra en einn eru nemendur sem drekka
    áfengi líklegri til að reykja heldur en þeir sem ekki drekka áfengi.

.. _c.logitlikur:

Líkur í tvíkosta aðhvarfsgreiningu 
-----------------------------------

Líkur í tvíkosta aðhvarfsgreiningu 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tvíkosta aðhvarf og líkur (logistic regression and probability)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    Gerum ráð fyrir að sambandi skýribreytunnar :math:`x` og því svarbreyta
    taki gildið 1 megi lýsa með tvíkosta aðhvarfsgreiningarlíkaninu
    
    .. math:: \log \left( \frac{p}{1-p} \right)  = \beta_0 + \beta_1 x + \varepsilon
    
    Þá eru líkurnar á því að svarbreytan taki gildið 1 þegar gildi
    skýribreytunnar er :math:`x` eru gefnar með
    
    .. math::
       \hat p = \frac{e^{\hat \beta_0 + \hat \beta_1 x}}{1 + e^{\hat \beta_0 + \hat \beta_1 x }}
       :label: eq.logitlikur

    ef skýribreytan er samfelld en 

    .. math::
       \hat p = \frac{e^{\hat \beta_0 + \hat \beta_a I_{x=a}}}{1 + e^{\hat \beta_0 + \hat \beta_a I_{x=a} }}
       :label: eq.logitlikurstrjal

    ef skýribreytan er strjál.


--------------

Sýnidæmi: Líkur í tvíkosta aðhvarfsgreiningu með samfelldri skýribreytu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Jói kannar hvort nemendur sem stunda mikla líkamsrækt séu líklegri til
    að reykja heldur en þeir sem stunda litla líkamsrækt. Hann metur
    tvíkosta aðhvarfsgreiningarlíkan til að kanna sambandið þar sem
    skýribreytan er fjöldi klukkustunda sem nemendur stunda líkamsrækt á
    viku. Hann mat stuðlana sem
    
    .. math::
       \begin{aligned}
       \hat \beta_0 &= -1.7428, \\
       \hat \beta_1 &= -0.1164 \end{aligned}
    
    Hverjar eru líkur þess að nemandi sem stundar líkamsrækt í 8
    klukkustundir á viku reyki sígarettur? En nemanda sem stundar líkamsrækt
    í 5 klukkustundir á viku?
    
    Líkur þess að nemandi sem stundar líkamsrækt í 8 klukkustundir á viku
    reyki sígarettur eru gefnar með
    
    .. math::
       \begin{aligned}
       \hat p &= \frac{e^{\hat \beta_0 + \hat \beta_1 \cdot 8}}{1 + e^{\hat \beta_0 + \hat \beta_1 \cdot 8 }} \\
       &= \frac{e^{ -1.7428  -0.1164  \cdot 8}}{1 + e^{ -1.7428  -0.1164   \cdot 8}} \\
       &=  0.0645251 \end{aligned}
    
    Líkur þess að nemandi sem stundar líkamsrækt í 5 klukkustundir á viku
    reyki sígarettur eru gefnar með
    
    .. math::
       \begin{aligned}
       \hat p &= \frac{e^{\hat \beta_0 + \hat \beta_1 \cdot 5}}{1 + e^{\hat \beta_0 + \hat \beta_1 \cdot 5 }} \\
       &= \frac{e^{ -1.7428  -0.1164  \cdot 5}}{1 + e^{ -1.7428  -0.1164   \cdot 5}}\\
       &=  0.08908976 \end{aligned}

Sýnidæmi: Líkur í tvíkosta aðhvarfsgreiningu með strjálli skýribreytu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Guðný kannar hvort nemendur sem drekka áfengi séu líklegri til að reykja
    heldur en þeir sem ekki drekka áfengi. Hún metur tvíkosta
    aðhvarfsgreiningarlíkan til að kanna sambandið og metur gildi stuðlanna
    sem
    
    .. math::
       \begin{aligned}
       \hat \beta_0 &= -4.248, \\
       \hat \beta_a &= 2.235 \end{aligned}
    
    Þeir nemendur sem ekki drukku áfengi töldust til viðmiðunarflokksins.
    Hverjar eru líkur þess að nemandi sem drekkur áfengi reyki sígarettur?
    Hverjar eru líkurnar á því að nemandi sem drekkur ekki áfengi reyki
    sígarettur
    
    Líkur þess að nemandi sem drekkur áfengi reyki sígarettur eru gefnar með
    
    .. math::
       \begin{aligned}
       \hat p &= \frac{e^{\hat \beta_0 + \hat \beta_a I_{x=a}}}{1 + e^{\hat \beta_0 + \hat \beta_a I_{x=a} }} \\
       &= \frac{e^{-4.248 + 2.235}}{1 + e^{-4.248 + 2.235}} \\
       &=  0.1178447 \end{aligned}
    
    Þar sem nemendur sem drekka ekki áfengi tilheyra viðmiðunarhópnum er :math:`I_{x=a}=0` og því eru
    líkur þess að þeir reyki sígarettur gefnar með
    
    .. math::
       \begin{aligned}
       \hat p &= \frac{e^{\hat \beta_0 }}{1 + e^{\hat \beta_0  }} \\
       &= \frac{e^{-4.248 }}{1 + e^{-4.248 }} \\
       &=  0.01409139 \end{aligned}

