Vigurrúm
========

Markmið þessa kafla er að alhæfa hugtakið vigur.
Við höfum séð hvernig það má leggja saman vigra, margfalda þá með tölu og hvernig þessar tvær aðgerðir tengjast með dreifireglu.
Nú viljum við telja til alla eiginleika vigra og skilgreina mismunandi "heimili" þeirra.  
Í stað vigurrúms með margföldun með rauntölu gætum við t.d. skilgreint vigurrúm með margföldun með tvinntölu. Við viljum einnig alhæfa hugtök sem við höfum áður séð eins og
*spann*, *línuleg vörpun* o.fl. fyrir almenn vigurrúm. 


Vigurrúm og hlutrúm 
-------------------

.. _skilgreining.vigurrum:

Skilgreining: Vigurrúm
~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    **Vigurrúm** (e. vector space) er ekki tómt mengi :math:`V` með stökum sem
    nefnd eru vigrar (e. vectors) ásamt tveimur aðgerðum
    samlagningu og margföldun með rauntölu, sem fullnægja
    eftirfarandi frumsendum fyrir alla vigra :math:`\ve u, \ve v\in V` og allar tölur :math:`c` og :math:`d` 
    :

     **1.** Ef :math:`\ve u,\ve v\in V` þá er :math:`\ve u+\ve v\in V`. \ *lokun við samlagningu*
    
     **2.** :math:`\ve u + \ve v = \ve v + \ve u`. \ *víxlregla samlagningar*
    
     **3.** :math:`(\ve u + \ve v) +\ve w =\ve u + (\ve v +\ve w)`. \ *tengiregla samlagningar*
    
     **4.** Til er stak :math:`\ve{0}` í :math:`V` kallað núll eða núllvigur þannig að :math:`\ve 0 + \ve u = \ve u`. \ *samlagningarhlutleysa*
    
     **5.** Fyrir sérhvert :math:`\ve u \in V` er til stak :math:`-\ve u \in V` þannig að :math:`\ve u +(-\ve u) =\ve 0` . \ *samlagningarandhverfa*
    
     **6.** Ef :math:`\ve u\in V` þá er :math:`c\ve u\in V`. \ *lokun við margföldun með tölu*
    
     **7.** :math:`c(d\ve u) = (cd)\ve u`. \ *tengiregla margföldunar*
    
     **8.** :math:`1\ve u = \ve u`. \ *margföldunarhlutleysa*

     **9.** :math:`c(\ve u+\ve v) = c\ve u +c\ve v`. \ *dreifiregla*
    
     **10.** :math:`(c+d)\ve u = c\ve u + d\ve u`. \ *dreifiregla*

Nokkrar afleiðingar af þessari skilgreiningu eru að:

    - Fyrir sérhvern vigur :math:`\ve u\in V` gildir að :math:`0\ve u = \ve 0`.
    - Fyrir sérhverja tölu :math:`c` gildir að :math:`c\ve 0 = \ve 0`.
    - Fyrir sérhvern vigur :math:`\ve u\in V` er vigurinn :math:`-\ve u` ótvírætt ákvarðaður.
    - Fyrir sérhvern vigur :math:`\ve u\in V` gildir að :math:`-\ve u=(-1)\ve u`.
    - Núllvigurinn er ótvírætt ákvarðaður.


Sýnidæmi: Vigurrúm
^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    **1.** :math:`\R^n` ásamt venjulegri samlagningu og margföldun með rauntölu er vigurrúm.

    **2.** :math:`\R^{m\times n}`, mengi allra :math:`m\times n` fylkja, er vigurrúm þar sem aðgerðirnar eru venjuleg samlagning fylkja og margföldun fylkis með tölu.

    **3.** Mengi allra runa :math:`{y_k} = (\ldots, y_{-1}, y_0, y_1, y_2, \ldots)` af rauntölum.
    Samlagning og margföldun með tölu eru skilgreind þannig að 

    .. math:: {y_k } + {z_k } =(\ldots, y_{-1}+z_{-1}, y_0+z_0, y_1+z_1, y_2+z_2, \ldots)={y_k+z_k},

        r{y_k}= (\ldots, ry_{-1}, ry_0, ry_1, ry_2, \ldots)={ry_k}

    Mengið ásamt þessum tveimur aðgerðum er vigurrúm.

    **4.** Látum :math:`\mathbb{P}_n` vera mengi allra margliða af stigi minna en eða jafnt :math:`n`. Stökin í :math:`\mathbb{P}_n` 
    eru margliður af taginu

    .. math:: \ve p(t)=a_0+a_1 t+a_2 t^2+\cdots +a_n t^n 

    Samlagning og margföldun með tölu eru skilgreind á venjulegan mátan. Með þessum tveimur aðgerðum er :math:`\mathbb{P}_n` vigurrúm.

    **5.** Mengi allra margliða (af öllum stigum):math:`\mathbb{P_n}` er vigurrúm.

    Tökum einhverjar rauntölur :math:`a<b` og látum :math:`(a,b)` tákna opna bilið :math:`\{x \in \R\colon a < x < b\}\subset R`.

    **6.** Látum :math:`\mathcal{V}(a,b)` vera mengi allra falla :math:`f\colon (a,b)\to\R`. Samlagning og margföldun með tölu eru skilgreind á venjulega mátann. 
    Með þessum tveimur aðgerðum er :math:`\mathcal{V}(a,b)` vigurrúm. Athugið að núllvigurinn í :math:`\mathcal{V}(a,b)` er fastafallið sem tekur gildið 0 í öllum punktum.

    **7.** Látum :math:`\mathcal{C}(a,b)` vera mengi allra samfelldra falla :math:`f\colon (a,b)\to\R`. 
    Samlagning og margföldun með tölu eru skilgreind á venjulega mátann. 
    Athugið að þegar við leggjum saman tvö samfelld föll er útkoman samfellt fall og þegar við margföldum samfellt fall með tölu þá er útkoman samfellt fall.
    Með þessum tveimur aðgerðum er :math:`\mathcal{C}(a,b)` vigurrúm.

    **8.** Látum :math:`\mathcal{D}(a,b)` vera mengi allra diffranlegra falla :math:`f\colon (a,b)\to\R`. 
    Samlagning og margföldun með tölu eru skilgreind á venjulega mátann. 
    Athugið að þegar við leggjum saman tvö diffranleg föll er útkoman diffranlegt fall og þegar við margföldum diffranlegt fall með tölu þá er útkoman diffranlegt fall. 
    Með þessum tveimur aðgerðum er :math:`\mathcal{D}(a,b)` vigurrúm.

    Athugum að hér höfum við að :math:`\mathcal{D}(a,b)\subseteq\mathcal{C}(a,b)\subseteq\mathcal{V}(a,b)` svo hér er dæmi um að eitt vigurrúm er hlutmengi í öðru.


Skilgreining: Hlutrúm
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Hlutmengi :math:`H` í vigurrúmi :math:`V` kallast **hlutrúm** (e. subspace) ef eftirfarandi þrjú skilyrði eru öll uppfyllt 
    :

    **1.**  Núllvigurinn er stak í :math:`H`.

    **2.** Ef :math:`\ve u` og :math:`\ve v` eru vigrar í :math:`H` þá er vigurinn :math:`\ve u + \ve v` í :math:`H`. Við segjum að mengi :math:`H` sé *lokað undir samlagningu.*

    **3.** Ef :math:`\ve u` er vigur í :math:`H` og :math:`c` er rauntala þá er vigurinn :math:`c\ve u` í :math:`H`. Við segjum að mengi :math:`H` sé *lokað undir margföldun með tölu.*

.. admonition:: Athugasemd
    :class: athugasemd

    **(i)** Í stað skilyrðis **1.** er stundum sagt að mengið :math:`H` sé ekki tómt. 
    Þá má svo nota skilyrði **3.** til að sýna að :math:`\ve 0\in H`.

    **(ii)** Ef :math:`U` er hlutrúm í vigurrúminu :math:`V`, þá er :math:`U` vigurrúm með reikningsaðgerðunum sem það „erfir“ frá :math:`V`.

    **(iii)** :math:`\{\ve 0\}` og :math:`V` eru hlutrúm í :math:`V`.


Sýnidæmi: Hlutrúm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    **1.** Höfum vigurrúmið :math:`V=\R^3`. Mengin

    .. math:: H_1=\{(x,0,0)^T\colon x\in\R\}, H_2=\{(x,y,0)^T\colon x,y\in\R\}, H_3=\{(x,x,x)^T\colon x\in\R\}

    eru allt dæmi um hlutrúm.

    **2.**  Mengi allra efri þríhyrningsfylkja í vigurrúminu :math:`\R^{n\times n}` er hlutrúm í :math:`\R^{n\times n}`.

    **3.** Mengið :math:`\mathbb{P}_n` af öllum margliðum af stigi :math:`n` eða lægra er hlutrúm í :math:`\mathbb{P}` mengi allra margliðna.

    **4.** Mengið :math:`\mathcal{D}(a,b)` af öllum diffranlegum föllum á opna bilinu :math:`(a,b)` er hlutrúm í
    :math:`\mathcal{C}(a,b)`, mengi allra samfelldra falla á opna bilinu :math:`(a,b)`. Svo er :math:`\mathcal{C}(a,b)`
    sjálft hlutrúm í :math:`\mathcal{V}(a,b)`, mengi allra falla skilgreindra á opna bilinu :math:`(a,b)`. Við mættum einnig segja
    að :math:`\mathcal{D}(a,b)` sé hlutrúm í :math:`\mathcal{V}(a,b)`.


Skilgreinig: Alhæfing línuleg samantekt og spann
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreinig
    :class: skilgreining

    Látum :math:`V` vera vigurrúm, :math:`\ve v_1, \dots, \ve v_p \in V` og :math:`c_1, \dots, c_p \in \R`. Vigurinn

    .. math:: c_1 \ve v_1 + \dots + c_p \ve v_p \in V
    
    kallast **línuleg samantekt** vigranna. Mengi allra línulegra samantekta :math:`\ve v_1, \dots, \ve v_p` kallast **spann** vigranna,

    .. math:: \text{Span}\{\ve v_1, \dots, \ve v_p\} \subseteq V.
    
Áður skilgreindum við línulega samantekt og spann fyrir :math:`\R^n`. Nú höfum við almennari skilgreiningu fyrir hverskyns vigurrúm.


Setning: Spann er hlutrúm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`\ve v_1, \dots, \ve v_p \in V`. Þá er :math:`\text{Span}\{\ve v_1, \dots, \ve v_p\}` hlutrúm í :math:`V`.

    Látum :math:`U` vera hlutrúm í vigurrúmi :math:`V`. Ef :math:`\ve u_1, \ve u_2, \ldots, \ve u_p` eru vigrar í :math:`U` þá er 
    :math:`\text{Span}\{\ve u_1, \ve u_2, \ldots, \ve u_p\}\subseteq U`. 



Sýnidæmi: Fleiri hlutrúm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Skoðum upptalningu á öllu hlutrúmum eftirfarandi vigurrúma: :math:`\R`, :math:`\R^2` og :math:`\R^3`

.. admonition:: Lausn
    :class: daemi, dropdown 


    **1.** Einu hlutrúmin í :math:`\R` eru :math:`\{0\}` og :math:`\R`.

    **2.** Hlutrúmin í :math:`\R^2` eru :math:`\{\ve 0\}` og :math:`\R^2` ásamt öllum línum sem liggja um núllpunktinn.
    Lína gegnum núllpunktinn með stefnuvigur :math:`\ve v` er jöfn :math:`\text{Span}\{\ve v\}`.

    **3.** Hlutrúmin í :math:`\R^3` eru :math:`\{\ve 0\}` og :math:`\R^3` ásamt öllum línum og öllum sléttum sem liggja um núllpunktinn.
    Ef :math:`\Gamma` er slétta í :math:`\R^3` sem inniheldur núllpunktinn og :math:`\ve u` og :math:`\ve v` eru vigrar sem liggja í planinu 
    þannig að hvorugur sé margfeldi af hinum þá er :math:`\Gamma=\text{Span}\{\ve u, \ve v\}`.

.. admonition:: Athugasemd
    :class: athugasemd

    Athugið að eftirfarandi eru **ekki** hlutrúm:

    **1.** Lína í :math:`\R^n` sem fer ekki í gegnum núllpunktinn er **ekki** hlutrúm.

    **2.** Slétta í :math:`\R^3` sem fer ekki í gegnum núllpunktinn er **ekki** hlutrúm.


Skilgreining: Vigursumma 
~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`U_1` og :math:`U_2` vera hlutrúm í vigurrúmi :math:`V`. Þá kallast hlutmengið

    .. math:: U_1+U_2=\{\ve x+\ve y\colon \ve x\in U_1, \ve y\in U_1 \}

    **vigursumma** (e. vector sum), eða einfaldlega summa, þeirra.

Setning 
~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`U_1` og :math:`U_2` vera hlutrúm í :math:`V`. 
    Þá eru bæði :math:`U_1\cap U_2` og :math:`U_1+U_2` hlutrúm í :math:`V`.


Null, Col, Ker og Range
----------------------------------------------

Skilgreining: Núllrúm fylkis 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`A` vera :math:`m\times n` fylki. **Núllrúm** :math:`A` (e. nullspace) er skilgreint sem
    mengi allra vigra :math:`\ve x\in\R^n` þannig að :math:`A\ve x=\ve 0`. Núllrúmið er táknað með :math:`\nul{A}` og

    .. math:: \nul{A}=\{\ve x\in\R^n\colon A\ve x=\ve 0\}

    Núllrúmið er sem sagt mengi allra lausna jöfnunar :math:`A\ve x=\ve 0`.

Setning: Núllrúm er hlutrúm 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki. Núllrúm :math:`A` er hlutrúm í :math:`\R^n`, táknað :math:`\nul{A}`,
    m.ö.o. lausnarúm óhliðraðar jöfnu :math:`A\ve x=\ve 0` með :math:`n` óþekktum stærðum er
    hlutrúm í :math:`\R^n`.


.. admonition:: Athugasemd
    :class: athugasemd

    Lausnarmengi hliðraðar jöfnu :math:`A\ve x=\ve b` þar sem :math:`b\neq\ve 0` er **ekki** hlutrúm í :math:`\R^n`.
    Það sést til dæmis af því að :math:`\ve 0` er ekki í lausnarmenginu.

Skilgreining: Dálkrúm fylkis 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`A` vera :math:`m\times n` fylki. Mengið sem dálkvigrar :math:`A` spanna kallast
    **dálkrúm** :math:`A` (e. column space) og er táknað með :math:`\col{A}`. Ef :math:`A=[a_1 a_2 \cdots a_n]` þá er

    .. math:: \col{A}=\text{Span}\{a_1,a_2,\ldots,a_n\}.

Setning: Dálkrúm er hlutrúm 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki. Dálkrúm :math:`A`, :math:`\col{A}`, er hlutrúm í :math:`\R^m`.


Samanburður á núllrúmum og dálkrúmum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki.

    - Núllrúmið :math:`\nul{A}` er hlutrúm í :math:`\R^n` en dálkrúmið :math:`\col{A}` er hlutrúm í :math:`\R^m`.

    - Við finnum :math:`\nul{A}` með því að leysa jöfnuna :math:`A\ve x=\ve 0`.
    - Við finnum :math:`\col{A}` með því að skoða spann dálkvigra :math:`A`.

    - Vigur :math:`\ve v\in\R^n` er í :math:`\nul{A}` ef og aðeins ef :math:`A\ve v=\ve 0`.
    - Vigur :math:`\ve b\in\R^m` er í :math:`\col{A}` ef og aðeins ef jafnan :math:`A\ve x=\ve b` hefur lausn. 



Sýnidæmi: Núllrúm
^^^^^^^^^^^^^^^^^

.. admonition:: Sýnidæmi
    :class: daemi

    Finnið nákvæma lýsingu á núllrúmi fylkisins 

    .. math:: A=\begin{bmatrix} 1 & 2 & 3 & 4 \\
        5 & 6 & 7 & 8 \\
        9 & 10 & 11 & 12
        \end{bmatrix}
    
    með stikaðri framsetningu.

.. admonition:: Lausn
    :class: daemi, dropdown 

    Fáum, með einföldum línuaðgerðum að:

    .. math:: \begin{align*} \begin{bmatrix}
        1&2&3&4\\
        5&6&7&8\\
        9&10&11&12\\
        \end{bmatrix}
        &\overset{\substack{R_2 - 5 R_1 \\
        R_3 - 9 R_1}}\sim
        \begin{bmatrix}
        1&2&3&4\\
        0&-4&-8&-12\\
        0&-8&-16&-24\\
        \end{bmatrix}\\
        &\overset{\substack{R_2 + 5 R_1/2\\
        R_3 + 4 R_1}}\sim
        \begin{bmatrix}
        1&2&3&4\\
        0&1&-2&-3\\
        0& 0& 0&0\\
        \end{bmatrix}\\
        &\overset{\substack{R_1 - 2 R_2}}\sim
        \begin{bmatrix}
        1&0&-1&-2\\
        0&1&2&3\\
        0&0&0&0\\
        \end{bmatrix}.\end{align*}
    
    Höfum því að 

    .. math:: A \sim \begin{bmatrix}
        1&0&-1&-2\\
        0&1&2&3\\
        0&0&0&0\\
        \end{bmatrix}.
    
    Vitum að :math:`\nul{A}` er lausnamengi :math:`A\ve x=\ve 0`. Það er stikað með

    .. math:: \begin{bmatrix}
        x_1\\x_2\\x_3\\x_4
        \end{bmatrix}=\begin{bmatrix}
        x_3+2x_4\\-2x_3-3x_4\\x_3\\x_4
        \end{bmatrix}=x_3\begin{bmatrix}
        1\\-2\\1\\0
        \end{bmatrix}+
        x_4\begin{bmatrix}
        2\\-3\\0\\1
        \end{bmatrix}.
    
    Við fáum því

    .. math:: \nul A = \text{Span}\left\{\begin{bmatrix}
        1\\-2\\1\\0
        \end{bmatrix},\begin{bmatrix}
        2\\-3\\0\\1
        \end{bmatrix}\right\}.
    
    Til að finna nákvæma lýsingu núllrúms þarf því að leysa línulegt jöfnuhneppi.

Sýnidæmi: Dálkrúm
^^^^^^^^^^^^^^^^^

.. admonition:: Sýnidæmi
    :class: daemi

    Látum 

    .. math:: A=\begin{bmatrix} 1 & -10 & -24 & -42 \\
        1 & -8 & -18 & -32 \\
        -2 & 20 & 51 & 87
        \end{bmatrix}.
    
    Finnið nákvæma lýsingu á dálkrúmi A.

.. admonition:: Lausn
    :class: daemi, dropdown

    Fáum með einföldum línuaðgerðum að:

    .. math:: \begin{bmatrix} 1 & -10 & -24 & -42 \\
        1 & -8 & -18 & -32 \\
        -2 & 20 & 51 & 87 \\
        \end{bmatrix} 
        \sim \cdots \sim 
        \begin{bmatrix} 1 & -10 & -24 & -42 \\
        0 & 2 & 6 & 10 \\
        0 & 0 & 3 & 3 \\
        \end{bmatrix}.

    Sjáum að fyrstu 3 dálkar fylkisins eru vendidálkar. Þá er 
    :math:`\col{A}` fyrstu 3 dálkarnir úr upprunalega :math:`A` fylkinu,

    .. math:: \col{A}=\left\{\begin{bmatrix} 1 \\ 1 \\ -2 \end{bmatrix} 
        \begin{bmatrix} -10 \\ -8 \\ 20 \end{bmatrix}
        \begin{bmatrix} -24 \\ -18 \\ 51 \end{bmatrix} \right\}.

    
Skilgreining: Kjarni og mynd vörpunar 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`T\colon V\to W` vera línulega vörpun.

    **Kjarni** (e. kernel, null space) vörpunarinnar T er mengi allra vigra :math:`\ve u\in V` þannig að
    :math:`T(\ve u)=\ve 0`. Kjarninn er táknaður með :math:`\ker{T}` og

    .. math:: \ker{T}=\{\ve u\in V \ \colon \ T(\ve u)=\ve 0\}.

    **Mynd** (e. range) vörpunarinnar T er mengi allra vigra í :math:`W` sem rita má á forminu 
    :math:`T(\ve x)` fyrir eitthvað :math:`\ve x\in V`. Myndin er oft táknuð :math:`\range{T}` og

    .. math:: \range{T}=\{T(\ve x) \ \colon \ \ve x\in V\}.

.. admonition:: Athugasemd
    :class: athugasemd
    
    Ef :math:`T(\ve x)=A\ve x` fyrir eitthvað fylki :math:`A` þá er :math:`\ker{T}=\nul{A}` og
    :math:`\range{T}=\col{A}`.


Setning: Kjarni og mynd eru hlutrúm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning 

    Látum :math:`T \colon V \rightarrow W` vera línulega vörpun.
    
        Kjarni vörpunarinnar :math:`T` er hlutrúm í :math:`V`.
        
        Mynd vörpunarinnar :math:`T` er hlutrúm í :math:`W`.

Setning: Eintækni og átækni varpana
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning 

    Látum :math:`T\colon V\to W` vera línulega vörpun.

        Vörpunin :math:`T` er eintæk ef og aðeins ef :math:`\ker{T}=\{\ve{0}\}`.

        Vörpunin :math:`T` er átæk ef og aðeins ef :math:`\range{T}=W`.

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki og :math:`T\colon \R^n\to\R^m` vera línulega vörpun 
    þanning að :math:`T(\ve x)=A\ve x` fyrir alla vigra :math:`x\in\R^n`. Þá gildir

        Vörpunin :math:`T` er eintæk þá og því aðeins að :math:`\nul{A}=\{\ve 0\}`.

        Vörpunin :math:`T` er átæk þá og því aðeins að :math:`\col{A}=\R^m`.

Við vitum nú þegar að línuleg vörpun er eintæk ef og aðeins ef hún er átæk. Setningin segir okkur því líka að núllrúmið 
innihaldi aðeins :math:`\ve 0` þá og því aðeins að dálkrúmið sé :math:`\R^m`.


Grunnar og hnit
---------------

Skilgreining: Grunnur
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`H` vera hlutrúm í vigurrúmi :math:`V`. Upptalning :math:`\mathcal{B}=\{\ve b_1, \ve b_2, \ldots, \ve b_p\}`
    á vigrum í :math:`V` kallast **grunnur** (e. basis) fyrir :math:`H` ef eftirfarandi skilyrði eru bæði uppfyllt

        **(i)** Upptalningin :math:`\mathcal{B}` er línulega óháð.

        **(ii)** :math:`H=\text{Span}\{\ve b_1, \ve b_2, \ldots, \ve b_p\}`.

.. admonition:: Athugasemd
    :class: athugasemd

    - Ef :math:`\{\ve b_1, \ve b_2, \ldots, \ve b_p\}` er grunnur fyrir hlutrúm :math:`H` þá liggja allir vigrarnir :math:`\ve b_1, \ve b_2, \ldots, \ve b_p` í :math:`H`.

    - Öll vigurrúm eru hlutrúm í sjálfu sér. Grunnur fyrir vigurrúm :math:`V` er því línulega óháð upptalning :math:`\{\ve b_1, \ve b_2, \ldots, \ve b_p\}` á vigrum í :math:`V` sem spannar allt :math:`V`.

    - Við munum alltaf gera ráð fyrir að það séu endanlega margir vigrar í grunni. Þegar haldið er áfram með línulega algebru getum við þurft að nota grunna með óendanlega mörgum vigrum. Dæmi um slíkt vigurrúm er vigurrúm allra margliðna af einni breytu, þar er :math:`\{1,x,x^2,\ldots\}` grunnur.

Sýnidæmi: Venjulegi grunnurinn
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Rifjum upp að vigrarnir

    .. math:: \ve e_1 = \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix},
        \quad \ve e_2 = \begin{bmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{bmatrix},
        \quad, \dots, \quad \ve e_n = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix},

    mynda venjulega grunninn fyrir :math:`\R^n`. Venjulegi grunninn fyrir :math:`\R^n` er *grunnur* fyrir :math:`\R^n` eins og nafnið gefur til kynna.

Sýnidæmi: Línulega óháðir dálkvigrar mynda grunn
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Látum :math:`A` vera andhverfanlegt :math:`n\times n` fylki. Þá eru dálkvigrar :math:`A` línulega óháðir og þeir spanna allt :math:`\R^n`. Dálkvigrarnir mynda því grunn fyrir :math:`\R^n`.



Sýnidæmi: Grunnar
^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Eru eftirfarandi grunnar fyrir :math:`\mathbb{R} ^3`?
    
    .. math:: a)\  \left\{\begin{bmatrix} 3 \\ 0 \\ 0 \end{bmatrix}, 
        \begin{bmatrix} 4958 \\ 968 \\ 0 \end{bmatrix}, 
        \begin{bmatrix} -34 \\ 102 \\ -66 \end{bmatrix} \right\},
        \quad b)\  \left\{\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}, 
        \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}\right\}.
    
    

.. admonition:: Lausn
    :class: daemi, dropdown

    *a)* Sjáum að 

    .. math:: \begin{bmatrix} 3 & 4958 & -34 \\
        0 & 968 & 102 \\
        0 & 0 & -66 \\
        \end{bmatrix}
    
    er andhverfanlegt fylki. Svo mengið er grunnur fyrir :math:`\mathbb{R} ^3`.

    *b)* Við erum með tvo vigra í :math:`\mathbb{R} ^3` svo þeir spanna í mesta lagi sléttu í
    :math:`\mathbb{R} ^3` en ekki allt rúmið. Mengið er því ekki grunnur fyrir :math:`\mathbb{R} ^3`. 


  
Setning: Um spann mengja 
~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`S=\{\ve v_1, \ve v_2, \ldots, \ve v_p\}` vera upptalningu (eða mengi) vigra í :math:`V` sem spannar hlutrúm :math:`H`. 

        **a.** Gerum ráð fyrir að einn vigranna í :math:`S`, :math:`\ve v_k`, sé línuleg samantekt af hinum vigrunum í :math:`S`. Þá spannar
        :math:`S^\prime=\{\ve v_1, \ve v_2, \ldots,\ve v_{k-1}, \ve v_{k+1}, \ldots, \ve v_p\}` líka hlutrúmið :math:`H`.

        **b.** Ef :math:`H\neq\{\ve 0\}` þá er eitthvað ekki tómt hlutmengi úr :math:`S` grunnur fyrir :math:`H`. Ef :math:`H=\{\ve 0\}` þá er :math:`\emptyset` grunnur fyrir :math:`H`, og er í raun eini grunnurinn fyrir :math:`H`.


Sýnidæmi: Grunnur fyrir núllrúm 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Finnum grunn fyrir núllrúm eftirfarandi fylkis

    .. math:: A=\begin{bmatrix} 1 & 2 & 3 & 4 & 5 \\
        6 & 7 & 8 & 9 & 10\\
        11 & 12 & 13 & 14 & 15
        \end{bmatrix}.

.. admonition:: Lausn
    :class: daemi, dropdown

    Með einföldum línuaðgerðum fáum við

    .. math:: \begin{bmatrix}
        1  & 2 & 3 & 4 & 5\\
        6 & 7 & 8 & 9 &10\\
        11 & 12 & 13 & 14 & 15
        \end{bmatrix}\sim\dots\sim
        \begin{bmatrix}
        1  & 0 & -1 & -2 & -3\\
        0 & 1 & 2 & 3 &4\\
        0 & 0 & 0 & 0 & 0
        \end{bmatrix}

    sem gefur okkur jöfnuhneppið

    .. math:: \begin{eqnarray*}
        x_1-x_3-2x_4-3x_5&=&0\\
        x_2+2x_3+3x_4+4x_5&=&0
        \end{eqnarray*}
    
    Þetta má umrita sem 

    .. math:: \begin{eqnarray*}
        x_1&=&x_3+2x_4+3x_5\\
        x_2&=&-2x_3-3x_4-4x_5
        \end{eqnarray*}
    
    sem gefur 

    .. math:: \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{bmatrix}
        = \begin{bmatrix} x_3+2x_4+3x_5 \\ x_3 \\ x_4 \\ x_5 \end{bmatrix}
        = x_3 \begin{bmatrix} 1 \\ -2 \\ 1 \\ 0 \\ 0 \end{bmatrix} 
        + x_4 \begin{bmatrix} 2 \\ -3 \\ 0 \\ 1 \\ 0 \end{bmatrix}
        + x_5 \begin{bmatrix} 3 \\ -4 \\ 0  \\ 0 \\ 1 \end{bmatrix}
    
    Ljóst að vigrarnir þrír spanna :math:`\nul{A}`. Með því að skoða stuðla þeirra má
    sjá að þeir eru línulega óháðir. Því er

    .. math:: \left\{
        \begin{bmatrix}
        1\\
        -2\\
        1\\
        0\\
        0\\
        \end{bmatrix}
        ,\begin{bmatrix}
        2\\
        -3\\
        0\\
        1\\
        0
        \end{bmatrix}
        ,\begin{bmatrix}
        3\\
        -4\\
        0\\
        0\\
        1
        \end{bmatrix}\right\}
    
    grunnur fyrir :math:`\nul{A}`.

Setning: Að finna grunn fyrir dálkrúm 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera fylki og :math:`U` vera efra stallaform þess.
    Dálkar :math:`A` sem hafa forystustuðull í :math:`U` mynda grunn fyrir dálkrúm :math:`A`. 


.. admonition:: Athugasemd
    :class: athugasemd

    Mjög mikilvægt er að taka dálkana fyrir grunninn úr :math:`A`, ekki úr :math:`U`. Við notum :math:`U` bara til að ákveða 
    hvaða dálka úr :math:`A` við tökum. Nóg er að finna efra stallaform. Það er enginn þörf fyrir að rutt efra stallaform. 

Sýnidæmi: Grunnur fyrir dálkrúm 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Finnum grunn fyrir dálkrúm

    .. math:: A=\begin{bmatrix} 1 & 2 & 3 & 4 & 5 \\
        6 & 7 & 8 & 9 & 10\\
        11 & 12 & 13 & 14 & 15
        \end{bmatrix}.

.. admonition:: Lausn
    :class: daemi, dropdown

    Beitum einföldum línuaðgerðum þar til efra stallaform fæst

    .. math:: \begin{bmatrix}
        1  & 2 & 3 & 4 & 5\\
        6 & 7 & 8 & 9 &10\\
        11 & 12 & 13 & 14 & 15
        \end{bmatrix}\sim\dots\sim
        \begin{bmatrix}
        1  & 0 & -1 & -2 & -3\\
        0 & 1 & 2 & 3 &4\\
        0 & 0 & 0 & 0 & 0
        \end{bmatrix}.
    
    Köllum síðara fylkið :math:`U= [\bf u_1 \dots u_5]`. Með því að skoða 
    :math:`U` má sjá að dálkvigrarnir eru ekki línulega óháðir. 
    Sjáum að :math:`\ve u_3, \ve u_4` og :math:`\ve u_5` eru línuleg samantekt 
    af :math:`\ve u_1` og :math:`\ve u_2`. Því er :math:`\col{A} = \text{Span}\{\ve a_1, \ve a_2 \}`.
    Við fáum því að 
    
    .. math:: \left\{ \begin{bmatrix} 1 \\ 6\\ 11 \end{bmatrix}, \begin{bmatrix} 2 \\ 7 \\ 1 \end{bmatrix} \right\}

    er grunnur fyrir :math:`\col{A}`.

Setning: Tveir eiginleikar grunna 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`V` vera vigurrúm og :math:`S` vera endanlegt mengi sem spannar :math:`V`.
    Þá inniheldur :math:`S` grunn fyrir :math:`V`.

    Ef :math:`R` er línulega óháð hlutmengi í :math:`V` þá er :math:`R` innihaldið í einhverjum (ekki endilega þeim sama og :math:`S` inniheldur) 
    grunni fyrir :math:`V`.

    Þetta má orða sem svo: *Grunnur er eins lítið spannmengi og eins stórt línulega óháð mengi í vigurrúmi og mögulegt er*.

Setning: Um tilvist hnita 
~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Gerum ráð fyrir að :math:`\mathcal{B}=\{\ve b_1, \ve b_2, \ldots, \ve b_n\}` sé grunnur fyrir :math:`V`.
    Þá gildir fyrir sérhvern vigur :math:`\ve v\in V` að til eru *ótvírætt* ákvarðaðar tölur :math:`c_1, c_2, \ldots, c_n`
    þannig að

    .. math:: \ve v= c_1\ve b_1 + c_2\ve b_2 + \ldots + c_n\ve b_n.

    Þetta má orða á þann hátt að jafnan :math:`x_1\ve b_1 + x_2\ve b_2 + \ldots + x_n\ve b_n=\ve v` hafi nákvæmlega eina lausn, þ.e. fyrir gefinn grunn þá er til nákvæmlega ein leið til að rita gefinn vigur sem línulega samantekt vigranna í grunninum.

Skilgreining: :math:`\mathcal{B}`-hnit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Gerum ráð fyrir að :math:`\mathcal{B}=\{\ve b_1, \ve b_2, \ldots, \ve b_n\}` sé grunnur fyrir :math:`V`.
    Tölurnar :math:`c_1, c_2, \ldots, c_n` þannig að 

    .. math:: \ve v= c_1\ve b_1 + c_2\ve b_2 + \ldots + c_n\ve b_n,

    kallast **hnit vigursins** :math:`\ve v` **með tilliti til grunsins** :math:`\mathcal{B}` (e. coordinates of :math:`\ve v` relative to the basis :math:`\mathcal{B}`). 
    Við tölum líka um :math:`\mathcal{B}`-hnit vigursins :math:`\ve v` (e. :math:`\mathcal{B}`-coordinates of :math:`\ve v`).

Skilgreining: Hnitavigur :math:`[\ve x]_{\mathcal{B}}`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Ef tölurnar :math:`c_1, c_2, \ldots, c_n` eru hnit vigursins :math:`\ve x` með tilliti til grunsins :math:`\mathcal{B}`
    þá segjum við að vigurinn

    .. math:: [\ve x]_{\mathcal{B}}=\begin{bmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{bmatrix}

    sé **hnitavigur** :math:`\ve x` **með tilliti til grunnsins** :math:`\mathcal{B}` 
    (e. coordinate vector of :math:`x` relative to :math:`\mathcal{B}`, or :math:`\mathcal{B}`-coordinate vector). 


Sýnidæmi: Að skipta um grunn
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Gefinn er grunnurinn

    .. math:: \mathcal{B} = \{\ve b_1, \ve b_2\}= \left\{\begin{bmatrix} -1 \\ 3 \end{bmatrix},
        \begin{bmatrix} 2 \\ 2 \end{bmatrix}\right\}
    
    Vigurinn :math:`\ve x` með tillit til :math:`\mathcal{B}` hefur hnitin  :math:`[\ve x]_{\mathcal{B}}=\begin{bmatrix} 1 \\ 2 \end{bmatrix}`. Finnið hnit :math:`\ve x` með tillit til venjulega grunnsins :math:`\mathcal{S}=\{\ve e_1, \ve e_2 \}`, þ.e. finnið :math:`[\ve x]_{\mathcal{S}}`.

.. admonition:: Lausn
    :class: daemi, dropdown

    Fáum

    .. math:: [\ve x]_{\mathcal{S}} = \ve x = 1\begin{bmatrix}
        -1\\3
        \end{bmatrix}+2\begin{bmatrix}
        2\\2
        \end{bmatrix}= \begin{bmatrix}
        -1+4\\3+4
        \end{bmatrix}=
        \begin{bmatrix}
        3\\7
        \end{bmatrix}.

Skilgreining: Hnitavörpun
~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Gerum ráð fyrir að :math:`\mathcal{B}=\{\ve b_1, \ve b_2, \ldots, \ve b_n\}` sé grunnur fyrir vigurrúm :math:`V`. Vörpunin

    .. math:: V\rightarrow\R^n; \quad \ve x\mapsto [\ve x]_{\mathcal{B}}

    kallast **hnitavörpunin með tilliti til** :math:`\mathcal{B}` (e. coordiante mapping determined by :math:`\mathcal{B}`).


Vídd og rankur
--------------

Setning: Línulegt hæði mengja stærri en grunns 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Gerum ráð fyrir að :math:`\mathcal{B}=\{\ve b_1, \ve b_2, \ldots, \ve b_n\}` sé grunnur fyrir :math:`V`. 
    Mengi (eða upptalning) með fleiri en :math:`n` vigrum er línulega háð.

Setning: Um stærð grunna 
~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Ef vigurrúm :math:`V` hefur grunn með nákvæmlega :math:`n` vigrum þá hefur sérhver grunnur :math:`V` nákvæmlega :math:`n` vigra.

Skilgreining: Vídd
~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    **Vídd** (e. dimension) vigurrúms :math:`V` er skilgreind sem fjöldi vigra í grunni :math:`V` og er táknuð með :math:`\dim{V}`.
    Ef til er endanlegt mengi vigra sem spannar vigurrúm :math:`V` þá segjum við að :math:`V` hafi **endanlega vídd** (e. finite-dimensional). 
    Ef slíkt mengi er ekki til þá segjum við að :math:`V` hafi **óendanlega vídd**.


.. admonition:: Athugasemd
    :class: athugsemd

    - Samkvæmt setningunni hér að ofan er fjöldi vigra í grunni alltaf sá sami svo vídd endanlega víðs vigurrúms er vel skilgreind tala.

    - Ef við þekkjum einn grunn fyrir vigurrúm er vídd þess fjöldi vigra í þeim grunni. Við þurfum því bara að finna einhvern grunn til að segja til um víddina.

Sýnidæmi: Vídd
^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    **1.** Vigurrúmið :math:`\mathbb{R}^1` hefur víddina 1.
    
    **2.** Vigurrúmið :math:`\mathbb{R}^3` hefur víddina 3.

    **3.** Vigurrúmið :math:`\mathbb{R}^n` hefur víddina :math:`n`.

Setning: Vídd hlutrúms
~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`H` vera hlutrúm í endanlega víðu vigurrúmi :math:`V`.

        **a.** Ef við höfum línulega óháð mengi vigra í :math:`H` þá má bæta við það vigrum til að smíða grunn fyrir :math:`V`.

        **b.** :math:`\dim{H}\leq\dim{V}`.

Setning: Samsemd línulegs óhæðis og spanns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`V` vera vigurrúm með vídd :math:`n`.

        **a.** Sérhvert mengi af :math:`n` línulega óháðum vigrum í :math:`V` er grunnur fyrir :math:`V`.

        **b.** Sérhvert mengi af :math:`n` af vigrum í :math:`V` sem spanna :math:`V` er grunnur fyrir :math:`V`.

.. admonition:: Athugasemd
    :class: athugasemd

    Grunnur fyrir vigurrúm þarf að uppfylla tvö skilyrði. Hann þarf að vera línulega óháður og spanna allt vigurrúmið.
    Það nægir að tékka annað skilyrðið því hitt fylgir sjálfkrafa.

Setning: Forystustuðlar og vídd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki og :math:`U` (einhvert) efra stallaform :math:`A`. 

        **a.** Vídd :math:`\nul{A}` er jöfn fjölda frjálsra breyta, það er að segja víddin er jöfn fjölda dálka í :math:`U` 
        sem innihalda ekki forystustuðul.

        **b.** Vídd :math:`\col{A}` er jöfn fjölda dálka í :math:`U` sem innihalda forystustuðul (Víddin er jöfn fjölda forystustuðla).

Skilgreining: Línurúm 
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`A` vera :math:`m\times n` fylki. Línurúm (e. row space) fylkisins :math:`A` er hlutmengið í :math:`\R^n` sem línuvigrar
    :math:`A` spanna. Línurúm :math:`A` er táknað með :math:`\row{A}`.

    Athugasemdir: Ef :math:`A` er :math:`m\times n` fylki þá gildir að

    -:math:`\col{A}` er hlutrúm í :math:`\R^m`.

    -:math:`\row{A}` er hlutrúm í :math:`\R^n`.

    -:math:`\nul{A}` er hlutrúm í :math:`\R^n`.


Setning: Grunnur fyrir línurúm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    **a.** Ef tvö fylki :math:`A` og :math:`B` eru línujafngild (það er að fá má annað út frá hinu með einföldum línuaðgerðum) 
    þá eru línurúm þeirra jöfn, það er :math:`\row{A}=\row{B}`.

    **b.** Ef :math:`U` er efra stallaform fylkisins :math:`A` þá mynda þeir línuvigrar í :math:`U` sem eru ekki núll 
    grunn fyrir línurúm :math:`A`.

    Athugasemd: Það eru ekki-núll línuvigrarnir úr efra stallaforminu sem gefa grunninn, ekki línuvigrarnir úr :math:`A`.

Sýnidæmi: Grunnur fyrir línurúm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Finnum línurúm fyklkisins

    .. math:: A= \begin{bmatrix} 
        1 & 2 & 3 & 4 \\
        5 & 6 & 7 & 8 \\
        9 & 10 & 11 & 12 \\
        \end{bmatrix}

.. admonition:: Lausn
    :class: daemi, dropdown

    Fáum að 

    .. math:: A = \begin{bmatrix} 
        1 & 2 & 3 & 4 \\
        5 & 6 & 7 & 8 \\
        9 & 10 & 11 & 12 \\
        \end{bmatrix} \sim
        \begin{bmatrix} 
        1 & 2 & 3 & 4 \\
        0 & -4 & -8 & -12 \\
        0 & 0 & 0 & 0 \\
        \end{bmatrix}
    
    Við erum komin með efri stallagerð og því er 

    .. math:: \{\begin{bmatrix} 1 & 2 & 3 & 4 \end{bmatrix}, \begin{bmatrix} 0 & -4 & -8 & -12 \end{bmatrix} \}

    grunnur fyrir :math:`\row{A}`. 

Skilgreining: Rankur 
~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`A` vera :math:`m\times n` fylki. Rankur (e. rank), eða myndvídd, fylkisins :math:`A` er vídd dálkrúms :math:`A`.
    Rankur fylkisins :math:`A` er táknaður með :math:`\rnk{A}`.

Setning: Ranksetningin
~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki.

    **a.** Rankur fylkisins :math:`A` er jafn fjölda forystustuðla í efra stallaformi :math:`A`.

    **b.** Vídd dálkrúmsins og vídd línurúmsins eru jafnar. Rankur fylkisins er því einnig jafn vídd línurúmsins.

    **c.** Summa víddar dálkrúmsins og víddar núllrúmsins er jöfn fjölda dálka fylkisins, eðA

    .. math:: \rnk{A}+\dim{\nul{A}}=n.


Sýnidæmi: Rankur og vídd
^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Reiknum rank og vídd núllrúms fyrir 

    .. math:: A=\begin{bmatrix} 
        1 & 2 & 3 & 4 \\
        5 & 6 & 7 & 8 \\
        9 & 10 & 11 & 12 \\
        \end{bmatrix}

.. admonition:: Lausn
    :class: daemi, dropdown

    Komum fylkinu á efri stallagerð

    .. math:: \begin{bmatrix} 
        1 & 2 & 3 & 4 \\
        5 & 6 & 7 & 8 \\
        9 & 10 & 11 & 12 \\
        \end{bmatrix}\sim
        \begin{bmatrix} 
        1 & 0 & -1 & -2 \\
        0 & 1 & 2 & 3 \\
        0 & 0 & 0 & 0 \\
        \end{bmatrix}
    
    Rankur fylkisins er vídd dálkrúms sem er fjöldi vendidálka.
    Svo :math:`\rnk{A}=2`. Vídd núllrúms er fjöldi frjálsra breyta
    svo :math:`\nul{A}=2`.

Langa setningin um andhverfanleg fylki (linkur) gefur 11 skilyrði sem eru öll jafngild því að fylki sé   andhverfanlegt. 
Nú höfum við lært fullt af nýjum hugtökum og getum bætt við 
fleiri skilyrðum. TODO linkur að löngu setningunni.

Setning: Viðbót við löngu andhverfusetninguna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`n\times n` fylki. Eftirfarandi 7 skilyrði eru öll jafngildi.

    **1.** :math:`A` er andhverfanlegt.

    **13.** Dálkvigrar :math:`A` mynda grunn fyrir :math:`\R^n`.

    **14.** :math:`\col{A}=\R^n`.

    **15.** :math:`\dim{\col{A}}=n`.

    **16.** :math:`\rnk{A}=n`.

    **17.** :math:`\nul{A}=\{\ve 0\}`.

    **18.** :math:`\dim{\nul{A}}=0`.


Hnitaskipti
-----------

Við höfum áður framkvæmt hnitaskipti. Sáum að :math:`\mathcal{P}_\mathcal{B}[\ve x]_\mathcal{B}=\ve x`
þar sem :math:`\mathcal{P}_\mathcal{B}` er hnitaskiptafylki sem breytir úr hnitum með tillit til :math:`\mathcal{B}`
yfir í hnit með tilliti til venjulega grunnarins. 

    Til dæmis ef :math:`\mathcal{B}=\{\ve b_1, \ve b_2\}=\left\{\begin{bmatrix} 1 \\ 2 \end{bmatrix}, \begin{bmatrix} 5 \\ -1 \end{bmatrix}\right\}` þá er
    :math:`\mathcal{P}_\mathcal{B}=\begin{bmatrix} 1 & 5 \\ 2 & -1 \end{bmatrix}`. 

Önnur leið til að rita :math:`\mathcal{P}_\mathcal{B}` er :math:`\mathcal{P}_\mathcal{B}=\mathcal{P}_{\mathcal{E}\leftarrow\mathcal{B}}` 
af því að við erum að skipta úr  :math:`\mathcal{B}`-hnitum yfir í  :math:`\mathcal{E}`-hnit (venjulegt hnit). 
Okkur langar að finna hnitskiptafylki :math:`\mathcal{P}_{\mathcal{E}\leftarrow\mathcal{B}}` hugmyndin er að 
:math:`\mathcal{P}_{\mathcal{B}\leftarrow\mathcal{C}}=\mathcal{P}_{\mathcal{B}\leftarrow\mathcal{E}}\mathcal{P}_{\mathcal{E}\leftarrow\mathcal{C}}`.


Setning: Um hnitaskiptafylki
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`V` vera vigurrúm af vídd :math:`n` og gerum ráð fyrir að :math:`\mathcal{B}=\{\ve b_1, \ve b_2, \ldots, \ve b_n\}` 
    og :math:`\mathcal{C}=\{\ve c_1, \ve c_2, \ldots, \ve c_n\}` séu grunnar fyrir :math:`V`.

    **a.** Til er línuleg vörpun :math:`T\colon \R^n\to\R^n` þannig að :math:`T([x]_{\mathcal{B}})=[\ve x]_{\mathcal{C}}` fyrir 
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`\mathcal{B}=\{\ve b_1, \ve b_2, \ldots, \ve b_n\}` vera grunn fyrir :math:`\R^n` og látum :math:`\mathcal{E}` vera 
    venjulega grunninn fyrir :math:`\R^n`. Þá er hnitaskiptafylkið frá :math:`\mathcal{B}`-hnitum til :math:`\mathcal{E}`-hnita 
    gefið með

    .. math:: P_{\mathcal{E}\leftarrow\mathcal{B}}=[\ve b_1 \quad \ve b_2 \quad \ldots \quad \ve b_n]

    og hnitaskiptafylkið frá :math:`\mathcal{E}`-hnitum til :math:`\mathcal{B}`-hnita gefið með

    .. math:: P_{\mathcal{B}\leftarrow\mathcal{E}}=(P_{\mathcal{E}\leftarrow\mathcal{B}})^{-1}

Sýnidæmi: Hnitaskiptafylki yfir í venjulega grunninn
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Látum :math:`\mathcal{B}={(1,2),(3,1)}` vera grunn fyrir :math:`\R^2` og :math:`\mathcal{E}` vera venjulega grunninn
    fyrir :math:`\R^2`. Þá er 

    .. math:: \mathcal{P}_{\mathcal{E}\leftarrow\mathcal{B}}
        =\begin{bmatrix} \ve b_1 & \ve b_2 & \cdots & \ve b_n \end{bmatrix}
        =\begin{bmatrix} 1 & 3 \\ 2 & 1 \end{bmatrix}

    og 

    .. math:: \mathcal{P}_{\mathcal{B}\leftarrow\mathcal{E}}=(\mathcal{P}_{\mathcal{E}\leftarrow\mathcal{B}})^{-1}=\frac{1}{-5}
        \begin{bmatrix} 1 & -3 \\ -2 & 1 \end{bmatrix}

Setning: Formúla fyrir hnitaskiptifylki
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


Sýnidæmi: Hnitaskiptafylki
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

     Viljum finna :math:`\mathcal{P}_{\mathcal{C}\leftarrow\mathcal{B}}` ef :math:`\mathcal{B}` og :math:`\mathcal{C}` eru

    .. math:: \begin{align*}
        \mathcal{B} &= \left\{
        \begin{bmatrix}
        1 \\
        2 \\
        0
        \end{bmatrix},
        \begin{bmatrix}
        -1 \\
        1 \\
        2
        \end{bmatrix},
        \begin{bmatrix}
        0 \\
        1 \\
        3
        \end{bmatrix}
        \right\} \quad
        \mathcal{C} = \left\{
        \begin{bmatrix}
        1 \\
        0 \\
        1
        \end{bmatrix},
        \begin{bmatrix}
        0 \\
        2 \\
        1
        \end{bmatrix},
        \begin{bmatrix}
        1 \\
        1 \\
        -1
        \end{bmatrix}
        \right\}
        \end{align*}

.. admonition:: Lausn
    :class: daemi, dropdown

    Við myndum fylkið :math:`[C \ | \ B]` 
    og framkvæmum einfaldar línuaðgerðir til að umbreyta :math:`[C \ | \ B]` í :math:`[I \ | \ X]`:

    .. math:: [C \ | \ B] &= \left[\begin{array}{@{}ccc|ccc@{}}
        1 & 0 & 1 & 1 & -1 & 0 \\
        0 & 2 & 1 & 2 & 1 & 1 \\
        1 & 1 & -1 &  0 & 2 & 3
        \end{array}\right] \\&\sim
        \left[\begin{array}{@{}ccc|ccc@{}}
        1 & 0 & 1 & 1 & -1 & 0 \\
        0 & 1 & \frac{1}{2} & 1 & \frac{1}{2} & \frac{1}{2} \\
        0 & 1 & -2 & -1 & 3 & 3
        \end{array}\right] \\
        &\sim
        \left[\begin{array}{@{}ccc|ccc@{}}
        1 & 0 & 1 & 1 & -1 & 0 \\
        0 & 1 & \frac{1}{2} & 1 & \frac{1}{2} & \frac{1}{2} \\
        0 & 0 & -\frac{5}{2} & -2 & \frac{5}{2} & \frac{5}{2}
        \end{array}\right] 
        \\&\sim
        \left[\begin{array}{@{}ccc|ccc@{}}
        1 & 0 & 1 & 1 & -1 & 0 \\
        0 & 1 & \frac{1}{2} & 1 & \frac{1}{2} & \frac{1}{2} \\
        0 & 0 & 1 & \frac{4}{5} & -1 & -1
        \end{array}\right]\\&\sim
        \left[\begin{array}{@{}ccc|ccc@{}}
        1 & 0 & 0 & \frac{1}{5} & 0 & 1 \\
        0 & 1 & 0 & \frac{3}{5} & 1 & 1 \\
        0 & 0 & 1 & \frac{4}{5} & -1 & -1
        \end{array}\right] 
        

    Það með er

    .. math:: \mathcal{P}_{\mathcal{C}\leftarrow\mathcal{B}}=
        \begin{bmatrix}
        \frac{1}{5} & 0 & 1 \\
        \frac{3}{5} & 1 & 1 \\
        \frac{4}{5} & -1 & -1
        \end{bmatrix} 


