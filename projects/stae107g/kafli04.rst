Vigurrúm
========

Vigurrúm og hlutrúm 
-------------------

Skilgreining: Vigurrúm
^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    Vigurrúm (e. vector space) er ekki tómt mengi :math:`V` með stökum sem
    nefnd eru vigrar (e. vectors) ásamt tveimur aðgerðum
    samlagningu og margföldun með rauntölu, sem fullnægja
    eftirfarandi frumsendum fyrir alla vigra :math:`u, v\in V` og allar tölur :math:`c` og :math:`d` 
    :

     **1.** Ef :math:`\ve u,\ve v\in V` þá er :math:`\ve u+\ve v\in V`.
    
     **2.** :math:`\ve u + \ve v = \ve v + \ve u`.
    
     **3.** :math:`(\ve u + \ve v) +\ve w =\ve u + (\ve v +\ve w)`.
    
     **4.** Til er stak :math:`\ve{0}` í :math:`V` kallað núll eða núllvigur þannig að :math:`0 + u = u`.
    
     **5.** Fyrir sérhvert :math:`\ve u \in V` er til stak :math:`-\ve u \in V` þannig að :math:`\ve u +(-\ve u) =\ve 0` .
    
     **6.** Ef :math:`\ve u\in V` þá er :math:`c\ve u\in V`.
    
     **7.** :math:`c(\ve u+\ve v) = c\ve u +c\ve v`.
    
     **8.** :math:`(c+d)\ve u = c\ve u + d\ve u`.
    
     **9.** :math:`c(d\ve u) = (cd)\ve u`.
    
     **10.** :math:`1\ve u = \ve u`.

Nokkrar einfaldar afleiðingar af þessari skilgreiningu eru að:

    - Fyrir sérhvern vigur :math:`\ve u\in V` gildir að :math:`0\ve u = \ve 0`.
    - Fyrir sérhverja tölu :math:`c` gildir að :math:`c\ve 0 = \ve 0`.
    - Fyrir serhvern vigur :math:`\ve u\in V` er vigurinn :math:`-\ve u` ótvírætt ákvarðaður.
    - Fyrir sérhvern vigur :math:`\ve u\in V` gildir að :math:`-\ve u=(-1)\ve u`.
    - Núllvigurinn er ótvírætt ákvarðaður.


En af hverju að spá í vigurrúmum? Reiknireglurnar í vigurrúmi um samlagningu og margföldun með
tölu eru nákvæmlega sömu reiknireglur og gilda fyrir vigra í :math:`\R^n`.
Það sem við höfum gert í námskeiðinu þar sem ekki er beinlínis
verið að tala um hnit í vigri og fylki gildir almennt fyrir vigurrúm.
Hugtök eins og „línulega óháð“, „spann“ og „línuleg vörpun“ er hægt
að skilgreina í þessu almennara samhengi.
Það sem við græðum er að við getum nýtt það sem við gerum í
mun almennara samhengi. Við finnum almennt munstur sem hægt
er að nýta til að leysa mörg ólík verkefni.
Hægt að gera þetta enn almennara, t.d. með því að í stað
margföldun með rauntölu komi margföldun með tvinntölu. Það sem
er skilgreint hér að ofan myndum við þá kalla **vigurrúm yfir
rauntölur** og hitt væri **vigurrúm yfir tvinntölur**.


Dæmi um vigurrúm
^^^^^^^^^^^^^^^^

.. admonition:: Upptalning
    :class: daemi

    Efirfarandi eru dæmi um vigurrúm:

    **1.** :math:`\R^n` ásamt venjulegri samlagningu og margföldun með tölu er vigurrúm.

    **2.** :math:`\R^{m\times n}`, mengi allra :math:`m\times n` fylkja, er vigurrúm þar sem aðgerðirnar eru venjuleg samlagning fylkja og margföldun fylkis með tölu.

    **3.** Látum :math:`\mathbb{S}` vera mengi allra runa :math:`{y_k} = (\ldots, y_{-1}, y_0, y_1, y_2, \ldots)` af rauntölum. Rúmið :math:`\mathbb{S}`, sem er óendanlegt í báðar áttir, 
    kallast merkjarúm og stök þess kallast merki. Samlagning og margföldun með tölu á :math:`\mathbb{S}` eru skilgreind þannig að
    
    .. math:: {y_k } + {z_k } =(\ldots, y_{-1}+z_{-1}, y_0+z_0, y_1+z_1, y_2+z_2, \ldots)={y_k+z_k},

        r{y_k}= (\ldots, ry_{-1}, ry_0, ry_1, ry_2, \ldots)={ry_k}

    Mengið :math:`\mathbb{S}` ásamt þessum tveimur aðgerðum er vigurrúm.

    **4.** Látum :math:`\mathbb{P}_n` vera mengi allra margliða af stigi minna en eða jafnt :math:`n`. Stökin í :math:`\mathbb{P}_n` 
    eru margliður af taginu

    .. math:: \ve p(t)=a_0+a_1 t+a_2 t^2+\cdots +a_n t^n 

    Samlagning og margföldun með tölu eru skilgreind á venjulegan hátt. Með þessum tveimur aðgerðum er :math:`\mathbb{P}_n` vigurrúm.

    **5.** Látum :math:`\mathbb{P}` vera mengi allra margliða (af öllum stigum). Þá er :math:`\mathbb{P}` vigurrúm.

    Tökum einhverjar rauntölur :math:`a<b` og látum :math:`(a,b)` tákna opna bilið :math:`\{x \in \R\colon a < x < b\}\subset R`.

    **6.** Látum :math:`\mathcal{V}(a,b)` vera mengi allra falla :math:`f\colon (a,b)\to\R`. Samlagning og margföldun með tölu eru skilgreind á venjulegan hátt. 
    Með þessum tveimur aðgerðum er :math:`\mathcal{V}(a,b)` vigurrúm. Athugið að núllvigurinn í :math:`\mathcal{V}(a,b)` er fastafallið sem tekur gildið 0 í öllum punktum.

    **7.** Látum :math:`\mathcal{C}(a,b)` vera mengi allra samfelldra falla :math:`f\colon (a,b)\to\R`. 
    Samlagning og margföldun með tölu eru skilgreind á venjulegan hátt. 
    Athugið að þegar við leggjum saman tvö samfelld föll er útkoman samfellt fall og þegar við margföldum samfellt fall með tölu þá er útkoman samfellt fall.
    Með þessum tveimur aðgerðum er :math:`\mathcal{C}(a,b)` vigurrúm.

    **8.** Látum :math:`\mathcal{D}(a,b)` vera mengi allra diffranlegra falla :math:`f\colon (a,b)\to\R`. 
    Samlagning og margföldun með tölu eru skilgreind á venjulegan hátt. 
    Athugið að þegar við leggjum saman tvö diffranleg föll er útkoman diffranlegt fall og þegarvið margföldum diffranlegt fall með tölu þá er útkoman diffranlegt fall. 
    Með þessum tveimur aðgerðum er :math:`\mathcal{D}(a,b)` vigurrúm.

    Athugum að hér höfum við að :math:`\mathcal{D}(a,b)\subseteq\mathcal{C}(a,b)\subseteq\mathcal{V}(a,b)` svo hér er dæmi um að eitt vigurrúm er hlutmengi í öðru.


Skilgreining: Hlutrúm
^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    Hlutmengi :math:`H` í vigurrúmi :math:`V` kallast **hlutrúm** (e. subspace) ef eftirfarandi þrjú skilyrði eru öll uppfyllt 
    :

    **1.**  Núllvigurinn er stak í :math:`H`.

    **2.** Ef :math:`\ve u` og :math:`\ve v` eru vigrar í :math:`H` þá er vigurinn :math:`\ve u + \ve v` í :math:`H`. (Stundum sagt að mengi :math:`H` sé lokað undir samlagningu.)

    **3.** Ef :math:`\ve u` er vigur í :math:`H` og :math:`c` er rauntala þá er vigurinn :math:`c\ve u` í :math:`H`.(Stundum sagt að mengi :math:`H` sé lokað undir margföldun með tölu.)

    Athugasemdir:

    **(i)** Í stað skilyrðis **1.** er oft sett skilyrðið að mengið :math:`H` sé ekki tómt. 
    Þá má svo nota skilyrði **3.** til að sýna að :math:`\ve 0\in H`.

    **(ii)** Ef :math:`U` er hlutrúm í vigurrúminu :math:`V`, þá er :math:`U` vigurrúm með reikningsaðgerðunum sem það „erfir“ frá :math:`V`.

    **(iii)** :math:`\{\ve 0\}` og :math:`V` eru hlutrúm í :math:`V`.


Dæmi um hlutrúm
^^^^^^^^^^^^^^^

.. admonition:: Upptalning
    :class: daemi

    Efirfarandi eru dæmi um hlutrúm:

    **1.** Ef við látum :math:`V` vera vigurrúmið :math:`\R^3` þá eru mengin 

    .. math:: H_1=\{(x,0,0)^T\colon x\in\R\}, H_2=\{(x,y,0)^T\colon x,y\in\R\}, H_3=\{(x,x,x)^T\colon x\in\R\}

    allt dæmi um vigurrúm.

    **2.**  Mengi allra efri þríhyrningsfylkja í vigurrúminu :math:`\R^{n\times n}` er hlutrúm í :math:`\R^{n\times n}`.

    **3.** Mengið :math:`\mathbb{P}_n` af öllum margliðum af stigi :math:`n` eða lægra er hlutrúm í :math:`\mathbb{P}`, mengi allra margliðna.

    **4.** Mengið :math:`\mathcal{D}(a,b)` af öllum diffranlegum föllum á opna bilinu :math:`(a,b)` er hlutrúm í
    :math:`\mathcal{C}(a,b)`, mengi allra samfelldra falla á opna bilinu :math:`(a,b)`. Svo er :math:`\mathcal{C}(a,b)`
    sjálft hlutrúm í :math:`\mathcal{V}(a,b)`, mengi allra falla skilgreindra á opna bilinu :math:`(a,b)`. Við mættum einnig segja
    að :math:`\mathcal{D}(a,b)` sé hlutrúm í :math:`\mathcal{V}(a,b)`.


TODO HYPERLINK Á SKILGREININGAR UM LÍNULEGAR SAMANTEKTIR OG SPAN 

Setningar um vigra og hlutrúm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`\ve v_1, \ve v_2, \ldots, \ve v_p` vera vigra í vigurúmi :math:`V`. Þá er 
    :math:`\spn\{ \ve v_1, \ve v_2, \ldots, \ve v_p\}` hlutrúm í :math:`V`. 

.. admonition:: Setning
    :class: setning

    Látum :math:`U` vera hlutrúm í vigurrúmi :math:`V`. Ef :math:`\ve u_1, \ve u_2, \ldots, \ve u_p` eru vigrar í :math:`U` þá er 
    :math:`\spn\{ \ve u_1, \ve u_2, \ldots, \ve u_p\}\subseteq U`. 



Fleiri dæmi um hlutrúm
^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Upptalning
    :class: daemi

    Efirfarandi eru upptalning á öllum hlutrúmum í nokkrum vigurrúmum:

    **1.** Einu hlutrúmin í :math:`\R` eru :math:`\{0\}` og :math:`\R`

    **2.** Hlutrúmin í :math:`\R^2` eru :math:`\{\ve 0\}` og :math:`\R^2` ásamt öllum línum sem liggja um núllpunktinn.
    Lína gegnum núllpunktinn með stefnuvigur :math:`\ve v` er jöfn :math:`\spn\{\ve v\}`

    **3.** Hlutrúmin í :math:`\R^3` eru :math:`\{\ve 0\}` og :math:`\R^3` ásamt öllum línum og öllum sléttum sem liggja um núllpunktinn.
    Ef :math:`\Gamma` er slétta í :math:`\R^3` sem inniheldur núllpunktinn og :math:`\ve u` og :math:`\ve v` eru vigrar sem liggja í planinu 
    þannig að hvorugur sé margfeldi af hinum þá er :math:`\Gamma=\spn\{\ve u, \ve v\}`.

    Athugið að eftirfarandi eru **ekki** hlutrúm:

    **1.** Lína í :math:`\R^n` sem fer ekki í gegnum núllpunktinn er **ekki** hlutrúm.

    **2.** Slétta í :math:`\R^3` sem fer ekki í gegnum núllpunktinn er **ekki** hlutrúm.


Skilgreining: Vigursumma 
^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`U_1` og :math:`U_2` vera hlutrúm í vigurrúmi :math:`V`. Þá kallast hlutmengið

    .. math:: U_1+U_2=\{\ve x+\ve y\colon \ve x\in U_1, \ve y\in U_1 \}

    vigursumma(eða einfaldlega summa) (e. vector sum) þeirra.

Setning 
^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`U_1` og :math:`U_2` vera hlutrúm í :math:`V`. 
    Þá eru bæði :math:`U_1\cap U_2` og :math:`U_1+U_2` hlutrúm í :math:`V`.


Meira um hlutrúm: núllrúm og dálkrúm
------------------------------------

Skilgreining: Núllrúm fylkis 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`A` vera :math:`m\times n` fylki. Núllrúm :math:`A` (e. nullspace) er skilgreint sem
    mengi allra vigra :math:`\ve x\in\R^n` þannig að :math:`A\ve x=\ve 0`. Núllrúmið er táknað með :math:`\nul{A}` og

    .. math:: \nul{A}=\{\ve x\in\R^n\colon A\ve x=\ve 0\}

    Núllrúmið er semsagt mengi allra lausna jöfnunar :math:`A\ve x=\ve 0`.


Setning: Núllrúm er hlutrúm 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki. Núllrúm :math:`A`, :math:`\nul{A}`, er hlutrúm í :math:`\R^n`. 
    Þetta má líka orða sem að lausnarúm óhliðraðar jöfnu :math:`A\ve x=\ve 0` með :math:`n` óþekktum er
    hlutrúm í :math:`\R^n`.

    Athugasemd: Lausnarmengi hliðraðar jöfnu :math:`A\ve x=\ve b` með :math:`b\neq\ve 0` er **ekki** hlutrúm í :math:`\R^n`.
    Það sést til dæmis af því að :math:`\ve 0` er ekki í lausnarmenginu.

Skilgreining: Dálkrúm fylkis 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`A` vera :math:`m\times n` fylki. Mengið sem dálkvigrar :math:`A` spanna kallast
    dálkrúm :math:`A` (e. column space) og er táknað með :math:`\col{A}`. Ef :math:`A=[a_1 a_2 \cdots a_n]` þá er

    .. math:: \col{A}=\spn\{a_1,a_2,\ldots,a_n\}

Setning: Dálkrúm er hlutrúm 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki. Dálkrúm :math:`A`, :math:`\col{A}`, er hlutrúm í :math:`\R^m`.


Samanburður á núllrúmum og dálkrúmum
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Samanburður
    :class: daemi

    Látum :math:`A` vera :math:`m\times n` fylki.

    - Núllrúmið :math:`\nul{A}` er hlutrúm í :math:`\R^n` en dálkrúmið :math:`\col{A}` er hlutrúm í :math:`\R^m`.

    - Við finnum núllrúmið með því að leysa jöfnuna :math:`A\ve x=\ve 0`.
    - Við finnum dálkrúmið með því að skoða spann dálkvigranna.

    - Vigur :math:`\ve v\in\R^n` er í :math:`\nul{A}` ef og aðeins ef :math:`A\ve v=\ve 0`.
    - Vigur :math:`\ve b\in\R^m` er í :math:`\col{A}` ef og aðeins ef jafnan :math:`A\ve x=\ve b` hefur lausn. 


Skilgreining: Kjarni og mynd 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    :math:`T\colon V\to W` vera línulega vörpun.

    **a.** Kjarni (e. kernel, null space) vörpunarinnar T er mengi allra vigra :math:`\ve u\in V` þannig að
    :math:`T(\ve u)=\ve 0`. Kjarninn er táknaður með :math:`\ker{T}` og

    .. math:: \ker{T}=\{\ve u\in V\colon T(\ve u)=\ve 0\}.

    **b.** Mynd (e. range) vörpunarinnar T er mengi allra vigra í :math:`W` sem rita má á forminu 
    :math:`T(\ve x)` fyrir eitthvað :math:`\ve x\in V`. Myndin er oft táknuð :math:`\range{T}` og

    .. math:: \range{T}=\{T(\ve x)\colon \ve x\in V\}.

    Athugasemd: ef :math:`T(\ve x)=A\ve x` fyrir eitthvað fylki :math:`A` þá er :math:`\ker{T}=\nul{A}` og
    :math:`\range{T}=\col{A}`.

TODO: KANNSKI SKRIFA MEIRA UM KJARNA?? SKOÐA SETNINGU 14.2.4 HJÁ RÖGGA

Setning: Um tengsl varpanna og núll- og dálkrúma 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki og :math:`T\colon \R^n\to\R^m` vera línulega vörpun 
    þanning að :math:`T(\ve x)=A\ve x` fyrir alla vigra :math:`x\in\R^n`. Þá gildir
    :

    **1.** Vörpunin :math:`T` er eintæk þá og því aðeins að :math:`\nul{A}=\{\ve 0\}`.

    **2.** Vörpunin :math:`T` er átæk þá og því aðeins að :math:`\col{A}=\R^m`.

Við vitum núþegar að línuleg vörpun er eintæk ef og aðeins ef hún er átæk. Setningin segir okkur því líka að núllrúmið 
innihaldi aðeins :math:`\ve 0` þá og því aðeins að dálkrúmið sé :math:`\R^m`. Þetta samband gildir raun almennar eins og við
munum sjá í TODO: SETJA HYPERLINK Á RANKSETNINGARUMFJÖLLUN


Grunnar og hnit
---------------

Skilgreining: Grunnur
^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`H` vera hlutrúm í vigurrúmi :math:`V`. Upptalning :math:`\mathcal{B}=\{\ve b_1, \ve b_2, \ldots, \ve b_p\}`
    á vigrum í :math:`V` kallast grunnur fyrir :math:`H` ef eftirfarandi skilyrði eru bæði uppfyllt
    :

    **(i)** Upptalningin :math:`\mathcal{B}` er línulega óháð.

    **(ii)** :math:`H=\spn\{\ve b_1, \ve b_2, \ldots, \ve b_p\}`.

    Athugasemdir:

    - Ef :math:`\{\ve b_1, \ve b_2, \ldots, \ve b_p\}` er grunnur fyrir hlutrúm :math:`H` þá liggja allir vigrarnir :math:`\ve b_1, \ve b_2, \ldots, \ve b_p` í :math:`H`.
    - Öll vigurrúm eru hlutrúm í sjálfu sér. Grunnur fyrir vigurrúm :math:`V` er því línulega óháð upptalning :math:`\{\ve b_1, \ve b_2, \ldots, \ve b_p\}` á vigrum í :math:`V` sem spannar allt :math:`V`.



TODO: SKRIFA UPP DÆMI UM GRUNNA 

