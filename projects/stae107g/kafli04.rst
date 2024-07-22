Vigurrúm
========

Vigurrúm og hlutrúm 
-------------------

Skilgreining: Vigurrúm
^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    **Vigurrúm** (e. vector space) er ekki tómt mengi :math:`V` með stökum sem
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

    **vigursumma** (eða einfaldlega summa) (e. vector sum) þeirra.

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

    Látum :math:`A` vera :math:`m\times n` fylki. **Núllrúm** :math:`A` (e. nullspace) er skilgreint sem
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

    Látum :math:`A` vera :math:`m\times n` fylki. Mengið sem **dálkvigrar** :math:`A` spanna kallast
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

    - Við munum alltaf gera ráð fyrir að það séu endanlega margir vigrar í grunni. Þegar haldið er áfram með línulega algebru getum við þurft að nota grunna með óendanlega mörgum vigrum. Dæmi um slíkt vigurrúm er vigurrúm allra margliðna af einni breytu, þar er :math:`\{1,x,x^2,\ldots\}` grunnur.



TODO: SKRIFA UPP DÆMI UM GRUNNA 

Setning: Um spann mengja 
^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`S=\{\ve v_1, \ve v_2, \ldots, \ve v_p\}` vera mengi vigra í :math:`V` sem spannar hlutrúmið :math:`H`. 

    **a.** Gerum ráð fyrir að einn vigranna í :math:`S`, :math:`\ve v_k`, sé línuleg samantekt af hinum vigrunum í :math:`S`. Þá spannar
    :math:`S^\prime=\{\ve v_1, \ve v_2, \ldots,\ve v_{k-1}, \ve v_{k+1}, \ldots, \ve v_p\}` líka hlutrúmið :math:`H`.+

    **b.** Ef :math:`H\neq\{\ve 0\}` þá er eitthvað ekki tómt hlutmengi úr :math:`S` grunnur fyrir :math:`H`. 

    Athugasemd: Ef :math:`H=\{\ve 0\}` þá er :math:`\emptyset` grunnur fyrir :math:`H`, og er í raun eini grunnurinn fyrir :math:`H`.


TODO: dæmi um að finna grunna fyrir núll-og dálkrúm

Setning: Að finna grunn fyrir dálkrúm 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera fylki og :math:`U` vera efra stallaform :math:`A`. Þeir dálkar í :math:`A` þar sem er forystustuðull 
    í efra stallaforminu :math:`U` mynda grunn fyrir dálkrúm :math:`A`. 

    Athugasemdir: 
    - Mjög mikilvægt er að taka dálkana fyrir grunninn úr :math:`A`, ekki úr :math:`U`. Við notum :math:`U` bara til að ákveða 
    hvaða dálka úr :math:`A` við tökum.
    - Nóg er að finna efra stallaform. Það er enginn þörf fyrir að rutt efra stallaform. 

TODO: dæmi


Setning: Tveir eiginleikar grunna 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`V` vera vigurrúm og :math:`S` vera endanlegt mengi sem spannar :math:`V`.
    Þá inniheldur :math:`S` grunn fyrir :math:`V`

    Ef :math:`T` er línulega óháð hlutmengi í :math:`V` þá er :math:`T` innihaldið í einhverjum(ekki endilega þeim sama og :math:`S` inniheldur) 
    grunni fyrir :math:`V`.

    Þetta má orða sem svo: Grunnur er eins lítið spannmengi og eins stórt línulega óháð mengi í vigurrúmi og mögulegt er.

Setning: Um tilvist hnita 
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Gerum ráð fyrir að :math:`\mathcal{B}=\{\ve b_1, \ve b_2, \ldots, \ve b_n\}` sé grunnur fyrir vigurrúmið :math:`V`.
    Þá gildir fyrir sérhvern vigur :math:`\ve v` í :math:`V` að til eru *ótvírætt* ákvarðaðar tölur :math:`c_1, c_2, \ldots, c_n`
    þannig að

    .. math:: \ve v= c_1\ve b_1 + c_2\ve b_2 + \ldots + c_n\ve b_n 

    Athugasemdir:
    - Þetta má orða á þann hátt að jafnan :math:`x_1\ve b_1 + x_2\ve b_2 + \ldots + x_n\ve b_n=\ve v` hafi nákvæmlega eina lausn.
    - Þetta má einnig orða þannig að fyrir gefinn grunn þá er til nákvæmlega ein leið til að rita gefinn vigur sem línulega samantekt vigranna í grunninum.

Skilgreining: Hnit
^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    Gerum ráð fyrir að :math:`\mathcal{B}=\{\ve b_1, \ve b_2, \ldots, \ve b_n\}` sé grunnur fyrir vigurrúmið :math:`V`.
    Tölurnar :math:`c_1, c_2, \ldots, c_n` þannig að 

    .. math:: \ve v= c_1\ve b_1 + c_2\ve b_2 + \ldots + c_n\ve b_n 

    kallast hnit vigursins :math:`\ve v` með tilliti til grunsins :math:`\mathcal{B}` (e. coordinates of :math:`v` relative to the basis :math:`\mathcal{B}`). 
    Við tölum líka um :math:`\mathcal{B}`-hnit vigursins :math:`v` (e. :math:`\mathcal{B}`-coordinates of :math:`v`).

Skilgreining: Hnitavigur
^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    Ef tölurnar :math:`c_1, c_2, \ldots, c_n` eru hnit vigursins :math:`\ve x` með tilliti til grunsins :math:`\mathcal{B}`
    þá segjum við að vigurinn

    .. math:: [\ve x]_{\mathcal{B}}=\begin{bmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{bmatrix}

    sé hnitavigur :math:`\ve x` með tilliti til grunnsins :math:`\mathcal{B}` 
    (e. coordinate vector of :math:`x` relative to :math:`\mathcal{B}`, or :math:`\mathcal{B}`-coordinate vector). 

TODO: dæmi

Skilgreining: Hnitavörpun
^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    Gerum ráð fyrir að :math:`\mathcal{B}=\{\ve b_1, \ve b_2, \ldots, \ve b_n\}` sé grunnur fyrir vigurrúm :math:`V`. Vörpunin

    .. math:: V\rightarrow\R^n; \quad \ve x\mapsto [\ve x]_{\mathcal{B}}

    kallast hnitavörpunin með tilliti til :math:`\mathcal{B}` (e. coordiante mapping determined by :math:`\mathcal{B}`).


Vídd og rankur
--------------

Setning: Línulegt hæði mengja stærri en grunns 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Gerum ráð fyrir að :math:`\mathcal{B}=\{\ve b_1, \ve b_2, \ldots, \ve b_n\}` sé grunnur fyrir vigurrúm :math:`V`. 
    Mengi (eða upptalning) með fleiri en :math:`n` vigrum er línulega háð.

Setning: Um stærð grunna 
^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Ef vigurrúm :math:`V` hefur grunn með nákvæmlega :math:`n` vigrum þá hefur sérhver grunnur :math:`V` nákvæmlega :math:`n` vigra.

Skilgreining: Vídd
^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    Ef til er endanlegt mengi vigra sem spanna vigurrúm :math:`V` þá segjum við að :math:`V` hafi endanlega vídd (e. finite-dimensional). 
    Vídd vigurrúmsins :math:`V` er þá skilgreind sem fjöldi vigra í grunni fyrir :math:`V` og er táknuð með :math:`\dim{V}`.

    Ef slíkt mengi er ekki til þá segjum við að :math:`V` hafi óendanlega vídd.

    Athugasemdir:

    - Samkvæmt setningunni hér að ofan er fjöldi vigra í grunni alltaf sá sami svo vídd endanlega víðs vigurrúms er vel skilgreind tala.

    - Ef við þekkjum einn grunn fyrir vigurrúm er vídd þess fjöldi vigra í þeim grunni. Við þurfum því bara að finna einhvern einn grunn til að segja til um víddina.

TODO: dæmi

Setning: Vídd hlutrúms
^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`H` vera hlutrúm í endanlega víðu vigurrúmi :math:`V`.

    **a.** Ef við höfum línulega óháð mengi vigra í :math:`H` þá má bæta við það vigrum til að smíða grunn fyrir :math:`V`.

    **b.** :math:`\dim{H}\leq\dim{V}`.

Setning: Samsemd línulegs óhæðis og spanns
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`V` vera vigurrúm með vídd :math:`n`.

    **a.** Sérhvert mengi af :math:`n` línulega óháðum vigrum í :math:`V` er grunnur fyrir :math:`V`.

    **b.** Sérhvert mengi af :math:`n` af vigrum í :math:`V` sem spanna :math:`V` er grunnur fyrir :math:`V`.

    Athugasemd: Grunnur fyrir vigurrúm þarf að uppfylla tvö skilyrði. Hann þarf að vera línulega óháður og spanna allt vigurrúmið.
    Það nægir að tékka annað skilyrðið því hitt fylgir sjálfkrafa.

Setning: Forystustuðlar og vídd
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki og :math:`U` (einhvert) efra stallaform :math:`A`. 

    **a.** Vídd :math:`\nul{A}` er jöfn fjölda frjálsra breyta, það er að segja víddin er jöfn fjölda dálka í :math:`U` 
    sem innihalda ekki forystustuðul.

    **b.** Vídd :math:`\col{A}` er jöfn fjölda dálka í :math:`U` sem innihalda forystustuðul (Víddin er jöfn fjölda forystustuðla).

Skilgreining: Línurúm 
^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`A` vera :math:`m\times n` fylki. Línurúm (e. row space) fylkisins :math:`A` er hlutmengið í :math:`\R^n` sem línuvigrar
    :math:`A` spanna. Línurúm :math:`A` er táknað með :math:`\row{A}`.

    Athugasemdir: Ef :math:`A` er :math:`m\times n` fylki þá gildir að

    -:math:`\col{A}` er hlutrúm í :math:`\R^m`.

    -:math:`\row{A}` er hlutrúm í :math:`\R^n`.

    -:math:`\nul{A}` er hlutrúm í :math:`\R^n`.


Setning: Grunnur fyrir línurúm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    **a.** Ef tvö fylki :math:`A` og :math:`B` eru línujafngild (það er að fá má annað út frá hinu með einföldum línuaðgerðum) 
    þá eru línurúm þeirra jöfn, það er :math:`\row{A}=\row{B}`.

    **b.** Ef :math:`U` er efra stallaform fylkisins :math:`A` þá mynda þeir línuvigrar í :math:`U` sem eru ekki núll 
    grunn fyrir línurúm :math:`A`.

    Athugasemd: Það eru ekki-núll línuvigrarnir úr efra stallaforminu sem gefa grunninn, ekki línuvigrarnir úr :math:`A`.

TODO: dæmi

Skilgreining: Rankur 
^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`A` vera :math:`m\times n` fylki. Rankur (e. rank), eða myndvídd, fylkisins :math:`A` er vídd dálkrúms :math:`A`.
    Rankur fylkisins :math:`A` er táknaður með :math:`\rnk{A}`.

TODO: dæmi?

Setning: Ranksetningin
^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki.

    **a.** Rankur fylkisins :math:`A` er jafn fjölda forystustuðla í efra stallaformi :math:`A`.

    **b.** Vídd dálkrúmsins og vídd línurúmsins eru jafnar. Rankur fylkisins er því einnig jafn vídd línurúmsins.

    **c.** Summa víddar dálkrúmsins og víddar núllrúmsins er jöfn fjölda dálka fylkisins, eðA

    .. math:: \rnk{A}+\dim{\nul{A}}=n.


TODO: dæmi?

TODO: tala um löngu andhverfusetninguna, hlekkur til baka

Setning: Viðbót við löngu andhverfusetninguna
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`n\times n` fylki. Eftirfarandi 7 skilyrði eru öll jafngildi.

    **1.** :math:`A` er andhverfanlegt.

    **13.** Dálkvigrar :math:`A` mynda grunn fyrir :math:`\R^n`.

    **14.** :math:`\col{A}=\R^n`.

    **15.** :math:`\dim{\col{a}}=n`.

    **16.** :math:`\rnk{A}=n`.

    **17.** :math:`\nul{A}=\{\ve 0\}`.

    **18.** :math:`\dim{\nul{A}}=0`.


Hnitaskipti
-----------

TODO: texti

Setning: Um línuleika hnitavarpanna
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Gerum ráð fyrir að :math:`V` sé endanlega vítt vigurrúm með grunn :math:`\mathcal{B}=\{\ve b_1, \ve b_2, \ldots, \ve b_n\}`. 
    Hnitavörpunin 

    .. math:: V\rightarrow\R^n; \quad \ve x\mapsto [\ve x]_{\mathcal{B}}

    er línuleg vörpun. Hún er einnig gagntæk.


Setning: Tilvist gagntækra varpanna milli jafnstóra rúma
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`V` vera vigurrúm með vídd :math:`n`. Þá er til gagntæk línuleg vörpun milli :math:`V` og :math:`\R^n`.

    Athugasemd: Ef til er gagntæk línuleg vörpun milli tveggja vigurrúma segjum við að þau séu einsmóta (e. isomorphic) og 
    vörpunin sé einsmótun (e. isomorphism). Einsmóta vigurrúm eru "eins" og með einsmótunum má yfirfæra útreikninga frá öðru 
    vigurrúminu í hitt.

TODO: texti um hnitaskipti, sýnidæmi

Setning: Um hnitaskiptafylki
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`V` vera vigurrúm af vídd :math:`n` og gerum ráð fyrir að :math:`\mathcal{B}=\{\ve b_1, \ve b_2, \ldots, \ve b_n\}` 
    og :math:`\mathcal{C}=\{\ve c_1, \ve c_2, \ldots, \ve c_n\}` séu grunnar fyrir :math:`V`.

    **a.** Til er línuleg vörpun :math:`T\colon \R^n\to\R^n` þannig að :math:`T([x]_{\mathcal{B}})=[]_{\mathcal{C}}` fyrir 
    alla vigra :math:`\ve x\in V`. Fylki þessrar vörpunar er 

    .. math:: P_{\mathcal{C}\leftarrow\mathcal{B}}=[[\ve b_1]_{\mathcal{C}}\quad [\ve b_2]_{\mathcal{C}}\quad \ldots \quad [\ve b_n]_{\mathcal{C}}].

    **b.** Fylkið :math:`P_{\mathcal{C}\leftarrow\mathcal{B}}` úr lið (a) er andhverfanlegt og andhverfa þess er 
    hnitaskiptafylkið úr :math:`\mathcal{C}`-hnitum yfir í :math:`\mathcal{B}`-hnit. Það er að segja

    .. math:: P_{\mathcal{B}\leftarrow\mathcal{C}}=(P_{\mathcal{C}\leftarrow\mathcal{B}})^{-1}

    og fyrir sérhvern vigur :math:`\ve x\in V` gildir að 

    .. math:: [\ve x]_{\mathcal{B}}=(P_{\mathcal{C}\leftarrow\mathcal{B}})^{-1}[\ve x]_{\mathcal{C}}.


Oftast vinnum við með venjulega grunninn fyrir :math:`\R^n`, það er grunninn :math:`\mathcal{E}=\{\ve e_1, \ve e_2, \ldots, \ve e_n\}` 
þar sem :math:`\ve e_i` hefur i-ta hnitið 1 en öll önnur hnit 0. Þegar við skrifum vigur sem :math:`\ve x=\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}`
erum við að segja að :math:`x_1, x_2, \ldots, x_n` séu hnit vigursins :math:`\ve x` með tilliti til grunsins :math:`\mathcal{E}`. 
Við fáum því eftirfarandi fylgisetningu þegar við skoðum hnitaskipti í og úr venjulega grunninum.

Setning: Hnitaskiptafylki yfir í venjulega grunninn
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`\mathcal{B}=\{\ve b_1, \ve b_2, \ldots, \ve b_n\}` vera grunn fyrir :math:`\R^n` og látum :math:`\mathcal{E}` vera 
    venjulega grunninn fyrir :math:`\R^n`. Þá er hnitaskiptafylkið frá :math:`\mathcal{B}`-hnitum til :math:`\mathcal{E}`-hnita 
    gefið með

    .. math:: P_{\mathcal{E}\leftarrow\mathcal{B}}=[\ve b_1 \quad \ve b_2 \quad \ldots \quad \ve b_n]

    og hnitaskiptafylkið frá :math:`\mathcal{E}`-hnitum til :math:`\mathcal{B}`-hnita gefið með

    .. math:: P_{\mathcal{B}\leftarrow\mathcal{E}}=(P_{\mathcal{E}\leftarrow\mathcal{B}})^{-1}

TODO: dæmi

Setning: Formúla fyrir hnitaskiptifylki
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`\mathcal{B}` og :math:`\mathcal{C}` vera grunna fyrir :math:`\R^n` og látum :math:`\mathcal{E}` tákna venjulega grunninn.
    Þá er 

    .. math:: P_{\mathcal{C}\leftarrow\mathcal{B}}=P_{\mathcal{C}\leftarrow\mathcal{E}}P_{\mathcal{E}\leftarrow\mathcal{B}}
        =(P_{\mathcal{E}\leftarrow\mathcal{C}})^{-1} P_{\mathcal{E}\leftarrow\mathcal{B}}


Reikniaðferð fyrir hnitaskiptafylki
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Aðferð
    :class: skilgreining

    Látum :math:`\mathcal{B}=\{\ve b_1, \ve b_2, \dots, \ve b_n\}` og :math:`\mathcal{C}=\{\ve c_1, \ve c_2, \dots, \ve c_n\}` 
    vera grunna fyrir :math:`\R^n`. Til þess að finna hnitaskiptafylkið frá :math:`\mathcal{B}`-hnitum yfir í :math:`\mathcal{C}`-hnit, 
    :math:`P_{\mathcal{C}\leftarrow\mathcal{B}}` gerum við eftirfarandi

    **1.** Búum til aukna fylkið :math:`[\ve c_1 \ \ve c_2 \ \dots \ \ve c_n \ | \ \ve b_1 \ \ve b_2 \ \dots \ \ve b_n]`

    **2.** Breytum vinstri hluta aukna fylkisins í einingarfylkið með einföldum línuaðgerðum. Það sem eftir stendur í 
    hægri hluta aukna fylkisins er þá hnitaskiptafylkið :math:`P_{\mathcal{C}\leftarrow\mathcal{B}}`.

TODO: Dæmi

TODO: fylki vörpunnar með tilliti til grunns


