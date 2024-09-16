Línuleg jöfnuhneppi
====================

Línuleg Algebra er sú grein innan stærðfræðinnar sem fæst við línuleg jöfnuhneppi,
vigra, vigurrúm, línulegar varpanir og önnur tengd viðfangsefni. Í þessu námskeiði 
verður farið yfir helstu hugtök í línulegri algebru. Farið verður yfir: línuleg 
jöfnuhneppi, fylki, ákveður, vigra og vigurrúm, eiginvigra og eigingildi og innfeldi. 
Hagnýtingar línulegrar algebru má meðal annars finna innan verkfræðinnar, innan 
eðlisfræðinnar, í tölvugrafík, fjármálum og í tengslum við gervigreind.

Línuleg jöfnuhneppi
-------------------

Skilgreining: Línuleg jafna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Jafna af taginu 

    .. math:: a_1x_1+a_2x_2+\dots+a_nx_n=b 

    kallast **línuleg jafna** (e. linear equation).

    :math:`a_1,a_2,\dots,a_n` kallast **stuðlar** (e. coefficients) jöfnunnar.
    :math:`x_1,x_2,\dots,x_n` eru óþekktar stærðir sem kallast **breytur** (e. variables).


Skilgreining: Línulegt jöfnuhneppi 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    **Línulegt jöfnuhneppi** (e. system of linear equations)
    er safn af einni eða fleiri línulegum jöfnum og er oft sett fram á forminu:

    .. math:: \begin{align}
        a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n &= b_1 \\
        a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n &= b_2 \\
        &\vdots \\
        a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n &= b_m
        \end{align}



Setning: Fjöldi lausna
~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 
    :class: setning

    Línulegt jöfnuhneppi getur haft:

        **a.** Enga lausn.

        **b.** Nákvæmlega eina lausn.

        **c.** Óendanlega margar lausnir.
    
    Jöfnuhneppi er sagt **ósamkvæmt** (e. inconsistent) ef það hefur enga lausn.

    Jöfnuhneppi er sagt **samkvæmt** (e. consistent) ef það hefur að minnsta kosti eina lausn.
    Jöfnuhneppi sem hefur nákvæmlega eina lausn er sagt hafa **ótvírætt ákvarðaða** lausn (e. unique solution).


Sýnidæmi: Jöfnuhneppi sem hefur enga lausn
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi

  Leysið jöfnuhneppið

  .. math:: \begin{align*}
    x-2y&=5 \\
    -2x+4y&= 6 
    \end{align*}

.. admonition:: Lausn
  :class: daemi, dropdown
  
  Margföldum efri jöfnuna með tveimur. Fáum
   
  .. math:: \begin{align*}
     2x-4y&=10 \\
     -2x+4y&= 6 
     \end{align*}

  Leggjum saman jöfnurnar og fáum :math:`0=16` svo jöfnuhneppið 
  hefur enga lausn, þ.e. ósamkvæmt.


Sýnidæmi: Jöfnuhneppi sem hefur eina lausn
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi
  
  Leysið jöfnuhneppið

    .. math:: \begin{aligned}
        x + 2y &= -3 \\
        x - y &= 6 
        \end{aligned}

.. admonition:: Lausn
  :class: daemi, dropdown
  
  Drögum neðri jöfnuna frá þeirri efri og fáum :math:`3y=-9` sem gefur
  :math:`y=-3`. Stingum inn í neðri jöfnuna og gefur :math:`x=3`. Þar 
  með er :math:`(x,y)=(3,-3)` lausn jöfnuhneppisins. 
  
  Jöfnuhneppið er samkvæmt og þar að auki hefur jöfnuhneppið aðeins eina lausn, m.ö.o.
  lausnin er ótvírætt ákvörðuð.

Sýnidæmi: Jöfnuhneppi sem hefur óendalega margar lausnir
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi

  Leysið jöfnuhneppið

  .. math:: \begin{align*}
        x+y&=2 \\
        2x+2y&= 4 
        \end{align*}

.. admonition:: Lausn
  :class: daemi, dropdown

   Deilum í neðri jöfnuna með tveimur. Fáum
   
   .. math:: \begin{align*}
      x+y&=2 \\
      x+y&=2 
      \end{align*}

   Ef við drögum efri jöfnuna frá þeirri neðri fæst:

    .. math:: \begin{align*}
       x+y&=2 \\
       0 &= 0
       \end{align*}
    
   Athugum þá hvort jafnan 
   :math:`x+y=2` hafi einhverja lausn. Já, :math:`(x,y)=(1,1)` og 
   :math:`(x,y)=(2,0)` eru dæmi um lausnir. Jöfnuhneppið er 
   samkvæmt en lausnin er ekki ótvírætt ákvörðuð. Ef við veljum 
   til dæmis :math:`y=t` fæst :math:`x=2-t`. Svo allar tvenndir af
   gerð :math:`(x,y)=(2-t,t)` eru lausnir jöfnuhneppisins. 



Skilgreining: Lausnamengi
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Mengi allra lausna jöfnuhneppis kallast **lausnamengi** þess (e. solution set).


Skilgreining: Jafngild
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Línuleg jöfnuhneppi sem hafa sama lausnamengið eru **jafngild** (e. equivalent).


Fylki
---------

Skilgreining: Stærð fylkis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`A` vera :math:`m\times n` fylki,

    .. math:: A = \begin{bmatrix}
        a_{11}  & \cdots & a_{1n}\\
        a_{21}  & \cdots & a_{2n}\\
        \vdots &  \ddots &\vdots \\
        a_{m1} & \cdots & a_{mn}
        \end{bmatrix}.

    Fylkið :math:`A` hefur :math:`m` **línur** (e. rows), sem liggja lárétt, og :math:`n` **dálka** (e. columns), sem liggja lóðrétt.
    Við segjum að **stærð fylkis** :math:`A` sé :math:`m\times n`.

    Fylki sem hefur jafn margar línur og dálka, :math:`n \times n`, kallast **ferningsfylki** (e. square matrix).

.. admonition:: Minnisregla fyrir :math:`m \times n`
    :class: athugasemd

    LSD = Lína Sinnum Dálkur.

Skilgreining: Stuðlafylki og aukið fylki
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Rita má sérhvert línulegt jöfnuhneppi
    
    .. math:: \begin{alignat*}{2}
            a_{11}x_{1}+&\dots+a_{1n}x_n &= b_1\\
            &\hspace{6.143162275pt}\vdots & \\
            a_{m1}x_{1}+&\dots+a_{mn}x_n &= b_m\\    
            \end{alignat*}
        
    á **fylkjaformi**
    
    .. math:: \begin{bmatrix}
        a_{11} & a_{12} & \cdots & a_{1n}\\
        a_{21} & a_{22} & \cdots & a_{2n}\\
        \vdots & \vdots & \ddots &\vdots \\
        a_{m1} & a_{m2} & \cdots & a_{mn}
        \end{bmatrix}
        \begin{bmatrix}
        x_1 \\ x_2 \\ \vdots \\ x_n
        \end{bmatrix}=
        \begin{bmatrix}
        b_1 \\ b_2 \\ \vdots \\ b_n
        \end{bmatrix}.

    Fylkin

    .. math:: \begin{bmatrix}
        a_{11} & a_{12} & \cdots & a_{1n}\\
        a_{21} & a_{22} & \cdots & a_{2n}\\
        \vdots & \vdots & \ddots &\vdots \\
        a_{m1} & a_{m2} & \cdots & a_{mn}
        \end{bmatrix}
        \text{ og }
        \left[\begin{array}{@{}cccc|c@{}}
        a_{11} & a_{12} & \cdots & a_{1n} & b_1\\
        a_{21} & a_{22} & \cdots & a_{2n} & b_2\\
        \vdots & \vdots & \ddots &\vdots & \vdots \\
        a_{m1} & a_{m2} & \cdots & a_{mn} & b_m
        \end{array}\right]
        
    kallast **stuðlafylki** (e. coefficient matrix) og **aukið fylki** (e. augmented matrix).
    

Einfaldar línuaðgerðir
----------------------
      
Eftirfarandi aðgerðir kallast **einfaldar línuaðgerðir** (e. elementary row operations) og 
þeim má beita á línuleg jöfnuhneppi án þess að lausnamengi jöfnuhneppisins breytist.


Setning: Einfaldar línuaðgerðir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

        **1.** **Umskipting** (e. replacement): að skipta út línu :math:`R_i` fyrir :math:`R_i+cR_j` þar sem :math:`R_j` er önnur lína og :math:`c` er fasti.

        **2.** **Víxlun** (e. interchange): að víxla á línum :math:`R_i` og :math:`R_j`.

        **3.** **Skölun** (e. scaling): að margfalda línu :math:`R_i` með fasta :math:`c\neq 0`

    Þessar aðgerðir eru andhverfanlegar og breyta ekki lausnamengi jöfnuhneppisins.

Sýnidæmi: Einfaldar línuaðgerðir 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi

  Beitið eftirfarandi línuaðgerðum :math:`\substack{R_1 \leftrightarrow R_2}, \substack{R_3 + 5R_1}` og :math:`\substack{-R_3-\frac{21}{4}R_2}` á fylkið

  .. math:: 
    \begin{bmatrix}
    0 & 4 & 1 \\
    -1 & 3 & 2 \\
    5 & 6 & -3
    \end{bmatrix}

  

.. admonition:: Lausn
  :class: daemi, dropdown

  Fáum

  .. math:: \begin{alignat*}{2}
    \begin{bmatrix}
    0 & 4 & 1 \\
    -1 & 3 & 2 \\
    5 & 6 & -3
    \end{bmatrix}
    &\overset{\substack{R_1 \leftrightarrow R_2}}{\sim} 
    &&\begin{bmatrix}
    -1 & 3 & 2 \\
    0 & 4 & 1 \\
    5 & 6 & -3
    \end{bmatrix} \\
    &\overset{\substack{R_3 + 5R_1}}{\sim} 
    &&\begin{bmatrix}
    -1 & 3 & 2 \\
    0 & 4 & 1 \\
    0 & 21 & 7
    \end{bmatrix}\\
    &\overset{\substack{-R_3-\frac{21}{4}R_2}}{\sim}
    &&\begin{bmatrix}
    -1 & 3 & 2 \\
    0 & 4 & 1 \\
    0 & 0 & \frac{7}{4}
    \end{bmatrix}
    \end{alignat*}



Skilgreining: Línujafngild
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Tvö jöfnuhneppi eru **línujafngild** (e. row equivalent) ef öðru má breyta í hitt
    með einföldum línuaðgerðum.

.. admonition:: Athugasemd
    :class: athugasemd

    Línujafngild jöfnuhneppi eru jafngild, en jafngild jöfnuhneppi eru ekki endilega línujafngild.
    
    Til dæmis eru eftirfarandi jöfnuhneppi jafngild

    .. math:: \left[\begin{array}{@{}cc|c@{}}
        1& 1 & 0\\ 
        0& 0 & 1
        \end{array}\right]
        \text{ og }
        \left[\begin{array}{@{}cc|c@{}} 
        1 &-1&0\\ 
        0&0 & 1
        \end{array}\right]

    því þau hafa sömu (engar) lausnir. Hins vegar eru þau ekki línujafngild, því ekki er hægt að breyta öðru þeirra í hitt með einföldum línuaðgerðum.


(Rudd) efra stallaform
----------------------

Öllum fylkjum má breyta í fylki af efri stallagerð með einföldum línuaðgerðum.


Skilgreining: Núlllínur og forystustuðlar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    **Núlllína** (e. zero row) er lína þar sem allir stuðlarnir eru núll,

    .. math:: \begin{bmatrix}
        0 & 0 & \cdots & 0 \end{bmatrix}.

    **Forystustuðull** (e. leading coeffcient) er fyrsti stuðull í hverri línu sem er ekki núll,

    .. math:: \begin{bmatrix}
        0 & \cdots & 0 & * & \cdots \end{bmatrix}.

    :math:`(*)` táknar hvaða tölu sem er

Skilgreining: Efri stallagerð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Fylki er sagt vera af **efri stallagerð**, eða **efra stallaformi**, (e. echelon form) ef það uppfyllir
    eftirfarandi skilyrði.

        **1.** Núlllínur liggja fyrir neðan aðrar línur.

        **2.** Forystustuðull hverrar línu er hægra megin við forystustuðul línunnar fyrir ofan.

        **3.** Allir stuðlar fyrir neðan forystustuðul eru núll.
    
.. admonition:: Athugasemd
    :class: athugasemd

    Efri stallagerð fylkis :math:`A` er oft táknuð með :math:`U`.    

Sýnidæmi: Efri stallagerð
^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi
  
  Breytum eftirfarandi :math:`{3\times 4}` fylki

    .. math:: A= \begin{bmatrix}
        1 & 2 & 3 & 4 \\
        5 & 6 & 7 & 8 \\
        9 & 10 & 11 & 12
        \end{bmatrix} 

  í fylki af efri stallagerð með einföldum línuaðgerðum.

.. admonition:: Lausn
  :class: daemi, dropdown

  Fáum

  .. math:: \begin{alignat*}{2}
    A= \begin{bmatrix}
    1 & 2 & 3 & 4 \\
    5 & 6 & 7 & 8 \\
    9 & 10 & 11 & 12
    \end{bmatrix} 
    &\overset{\substack{R_2 - 5R_1 \\
    R_3 - 9R_1}}{\sim} 
    &&\begin{bmatrix}
    1 & 2 & 3 & 4 \\
    0 & -4 & -8 & -12 \\
    0 & -8 & -16 & -24
    \end{bmatrix}\\  
    &\overset{\substack{R_3 - 2R_2}}{\sim}
    &&\begin{bmatrix}
    1 & 2 & 3 & 4 \\
    0 & -4 & -8 & -12 \\
    0 & 0 & 0 & 0
    \end{bmatrix}:= U
    \end{alignat*}
  
  Athugum nú skilyrðin:

  **1.** Núlllínur eru neðst. JÁ.

  **2.** Forystustuðull hverrar línu er hægra megin við forystustuðul línunnar fyrir ofan. JÁ.

  **3.** Allir stuðlar fyrir neðan forystustuðul eru núll. JÁ.

Skilgreining: Rudd efri stallagerð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Fylki er sagt vera af **ruddri efri stallagerð**  (e. reduced echeolon form) ef það er af efri 
    stallagerð og uppfyllir að auki eftirfarandi skilyrði:
    
        **1.** Forystustuðlar eru allir 1.

        **2.** Allir stuðlar fyrir ofan forystustuðul eru núll.

    Stundum eru forystustuðular í fylki af ruddri efri stallagerð kallaðir **vendistuðular**, og þeir dálkar sem innihalda slíka forystustuðla kallaðir **vendidálkar**.



Sýnidæmi: Rudd efri stallagerð
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi

  Nokkur dæmi um fylki af ruddri efri stallagerð

  .. math:: \begin{bmatrix}
    1 & 0 \\
    0 & 1 \\
    \end{bmatrix}, \quad
    \begin{bmatrix}
      1 & 4 & 0 \\
      0 & 0 & 1 \\
      0 & 0 & 0 \\
    \end{bmatrix}, \quad
    \begin{bmatrix}
      1 & 0 & * & 0 \\
      0 & 1 & * & 0 \\
      0 & 0 & 0 & 1 \\
    \end{bmatrix}, \quad
    \begin{bmatrix}
      1 & 0 & * & 0 & 1 \\
      0 & 1 & * & 0 & 2 \\
      0 & 0 & 0 & 1 & 3 \\
    \end{bmatrix}.    

  :math:`(*)` táknar hvaða tölu sem er.


Setning: Rutt efra stallaform er ótvírætt ákvarðað
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Sérhvert fylki er jafngilt einu og aðeins einu fylki á ruddu efra stallaformi.


Fjöldi lausna og frjálsar breytur
------------------------------------

Skilgreining: Frjálsar breytur og grunnbreytur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
  :class: skilgreining

  Þær breytur línulegs jöfnuhneppis á efri stallagerð sem ekki eru forystubreytur kallast **frjálsar breytur** (e. free variables). Breytur sem ekki eru frjálsar eru kallaðar **grunnbreytur** (e. leading variables).


Sýnidæmi: Frjálsar breytur, grunnbreytur og stikaframsetning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi

  Leysið jöfnuhneppið og setjið lausnina fram með stikaframsetningu.

  .. math:: \begin{align*}
    x_1+x_2+x_3 + x_4 + 2 x_5 =0\\
    x_2 + x_3 + 3 x_4 + x_5 = 4 \\
    -2 x_4 \qquad \ = 4
    \end{align*}

.. admonition:: Lausn
  :class: daemi, dropdown

  Ritum sem aukið fylki

  .. math:: \left[\begin{array}{@{}ccccc|c@{}}
    1 & 1 & 1  & 1 & 2  & 0\\
    0 & 1 & 1 & 3 & 1 & 4 \\
    0 & 0 & 0 & -2 & 0  & 4
    \end{array}\right].

  Við sjáum að :math:`x_1, x_2` og :math:`x_4`
  eru grunnbreytur, en :math:`x_3` og :math:`x_5` eru frjálsar því þar sitja aldrei forystustuðlar.
  Venja er að rita frjálsar breytur með öðrum bókstöfum, t.d. :math:`s := x_3` og :math:`t := x_5`.

  Neðsta jafnan í aukna fylkinu gefur :math:`-2 x_4 = 4`, þ.e. :math:`x_4 = -2`. Setjum svo inn í næst neðstu jöfnuna

  .. math:: x_2= 4 - x_3 - 3 x_4 - x_5 = 10 - s - t.

  Með þessum upplýsingum verður efsta jafnan

  .. math:: x_1 = - x_2 - x_3 - x_4 - 2 x_5 = -8 -t.

  Lausn jöfnuhneppisins á **stikaframsetningu** er því

  .. math:: \begin{bmatrix}
    x_2 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{bmatrix}=
    \begin{bmatrix}
    -8 - t\\
    10-s-t\\
    s\\
    -2\\
    t
    \end{bmatrix}=
    \begin{bmatrix}
    -8 \\ 10 \\ 0 \\ -2 \\ 0 \end{bmatrix} + 
    s \begin{bmatrix}
    0 \\ -1 \\ 1 \\ 0 \\ 0
    \end{bmatrix} + t \begin{bmatrix}
    -1 \\ -1 \\ 0 \\ 0 \\ 1 \end{bmatrix}

  þar sem :math:`s` og :math:`t` eru hvaða tölur sem er. Við sjáum meir um stikaframsetningu síðar.

Setning: Tilvist og fjöldi lausna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Jöfnuhneppi hefur lausn ef og aðeins ef dálkurinn lengst til hægri í efra stallaformi
  inniheldur ekki forystustuðul, þ.e.a.s. ef efra stallaform aukna
  fylkisins inniheldur ekki línu á forminu 

  .. math:: [0\ \dots \ 0 | \ b]

  þar sem :math:`b\neq 0`. 

  Ef jöfnuhneppið hefur lausn þá er annaðhvort

    **1.** Nákvæmlega eina lausn, ef það er engin frjáls breyta.

    **2.** Óendanlega margar lausnir, ef það eru ein eða fleiri frjálsar breytur.


.. admonition:: Dæmi
    :class: daemi

    Ef við umbreytum aukna fylki jöfnuhneppis yfir á (rudda) efri stallagerð getur eftirfarandi gerst:

    **1.** Engin lausn

    .. math:: \left[\begin{array}{@{}cc|c@{}}
        1 & * & 0 \\
        0 & 0 & 1 \\
        \end{array}\right].

    **2.** Nákvæmlega ein lausn 

    .. math:: \left[\begin{array}{@{}cc|c@{}}
        1 & 0 & * \\
        0 & 1 & * \\
        \end{array}\right].

    **3.** Óendanlega margar lausnir
    
    .. math:: \left[\begin{array}{@{}ccc|c@{}}
        1 & 0 & * & * \\
        0 & 1 & * & * \\    
        \end{array}\right].


Gauss-eyðing
------------

Línuleg jöfnuhneppi eru yfirleitt leyst með svokallaðri **Gauss-eyðingu** (e. Gauss-reduction), sem felst í því að beita línuaðgerðum á jöfnuhneppið
þar til fram kemur hneppi af efri stallagerð. Lausnamengi efri stallagerðar er hið sama og upphaflega fylkisins, og auðvelt er að leysa fylki af efri stallagerð með
**aftur-á-bak innsetningu** (e. back-substitution).
Einnig er hægt að koma fylkinu yfir á rudd efra stallaform og lesa lausnina beint út, þá er talað um **Gauss-Jordan eyðingu**.

Gauss-(Jordan) eyðing er undirstöðu atriði í þessu námskeiði og því **mikilvægt að tileinka sér vel**.

Aftur-á-bak innsetning
~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
  :class: skilgreining

  Línulegt jöfnuhneppi af efra stallaformi má leysa með aftur-á-bak innsetningu með því að byrja á neðstu jöfnu (sem ekki er núlllína)
  og lesa út formúlu fyrir forystubreytu hennar út frá frjálsu breytunum. Síðan er næsta lína fyrir ofan skoðuð og formúlan fyrir neðstu breytunni notuð. Þannig er haldið áfram "aftur á bak" þar til lausn
  fæst á jöfnuhneppinu.


Gauss-eyðing reiknirit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  **Gauss-eyðing**:

    **1.** Finnum dálkinn lengst til vinstri sem inniheldur ekki bara 0, og víxlum á línum þannig að þessi tala verði í efstu línu. 

    **2.** Eyðum stökunum fyrir neðan forystustuðulinn með því að draga margfeldi efstu línu frá línum fyrir neðan.

    **3.** Endurtökum skrefin hér að ofan fyrir línuna næst lengst til vinstri og svo koll af kolli.

  Nú höfum við umbreytt fylkinu yfir í fylki af efra stallaformi og getum notað aftur-á-bak innsetningu til þess að leysa jöfnuhneppið.

  **Gauss-Jordan eyðing** (áframhald)

    **4.** Eyðum stökunum fyrir ofan forystustuðalna þar til fylkinu er komið yfir á efra stallaform.
  
  Lausnin lesin beint.


Sýnidæmi: Gauss-eyðing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. admonition:: Dæmi
  :class: daemi

  Leysið jöfnuhneppið með Gauss-eyðingu

  .. math:: 
    \begin{aligned}
     x_1 -3x_2 + 4x_3 =-4,\\
     3x_1-7x_2+7x_3 =-8,\\
    -4x_1+6x_2+2x_3=4.
    \end{aligned}


.. admonition:: Lausn
  :class: daemi, dropdown
  
   Fáum
   
  .. math:: \begin{alignat*}{2}
    \left[\begin{array}{@{}ccc|c@{}}
    1 & -3 & 4 & -4\\
    3 & -7 & 7 & -8\\
    -4 & 6 & 2 & 4
    \end{array}\right] \quad
    &\overset{\substack{R_2-3R_1\\R_3+4R_1}}{\sim}
    &\quad&\left[\begin{array}{@{}ccc|c@{}}
    1 & -3 & 4 &-4\\
    0 & 2 & -5 & 4 \\
    0 & -6 & 18 & -12
    \end{array}\right] \\
    &\overset{\substack{-\frac{1}{6}R_3}}{\sim}
    &&\left[\begin{array}{@{}ccc|c@{}}
    1 & -3 & 4 &-4\\
    0 & 2 & -5 & 4 \\
    0 & 1 & -3 & 2
    \end{array}\right]  \\
    &\overset{\substack{
        R_2\leftrightarrow R_3}}{\sim}
    &&\left[\begin{array}{@{}ccc|c@{}}
    1 & -3 & 4 &-4\\
    0 & 1 & -3 & 2 \\
    0 & 2 & -5 & 4
    \end{array}\right] \\
    &\overset{\substack{R_1+3R_2\\ R_3-2R_2
    }}
    {\sim}
    &&\left[\begin{array}{@{}ccc|c@{}}
    1 & 0 & -5 & 2\\
    0 & 1 & -3 & 2 \\
    0 & 0 & 1 & 0
    \end{array}\right] \\
    &\overset{\substack{
    R_1+5R_3\\ R_2+3R_3}}{\sim}
    &&\left[\begin{array}{@{}ccc|c@{}}
    1 & 0 & 0 & 2\\
    0 & 1 & 0 & 2 \\
    0 & 0 & 1 & 0
    \end{array}\right]
    \end{alignat*}


  Svo við fáum

  .. math:: \begin{align*}
    x_1\phantom{+x_2+x_3} &= 2 \\
    \phantom{x_1+} x_2 \phantom{+x_3} &= 2 \\
    \phantom{x_1+x_2+} x_3 &= 0
    \end{align*}
  
  og línulega jöfnuhneppið hefur eina lausn: :math:`(x_1,x_2,x_3)=(2,2,0)`. 

  Hér hefði verið hægt að sleppa síðasta skrefinu, :math:`R_1+5R_3, R_2+3R_3`, og leysa með aftur-á-bak innsetningu í stað þess að lesa svarið beint með Gauss-Jordan.
  Nú skulum við nota þessa aðferð. Við höfum

  .. math:: \left[\begin{array}{@{}ccc|c@{}}
    1 & 0 & -5 & 2\\
    0 & 1 & -3 & 2 \\
    0 & 0 & 1 & 0
    \end{array}\right]

  Neðsta lína sem ekki er núll gefur lausn :math:`x_3 = 0`. Næst neðsta línan er því
  :math:`x_2 -3 x_3 = 2` svo :math:`x_2 = 2`. Að lokum er :math:`x_1 - 5 x_3 = 2` þ.e. :math:`x_1 = 2`. Sama niðurstaða fæst því með Gauss-eyðingu (viðbúið),
  :math:`(x_1,x_2,x_3)=(2,2,0)`.


Vigrar
------

Skilgreining: Vigur
~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Við köllum :math:`n \times 1` fylki **vigur** (e.vector).


Sýnidæmi: Dálkvigrar
^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    .. math:: \textbf{v}_1 = \begin{bmatrix}
        1 \\
        2 \\
        \end{bmatrix},
        \quad
        \textbf{v}_2 = \begin{bmatrix}
        -1 \\
        0 \\
        \end{bmatrix},
        \quad
        \textbf{v}_3 = \begin{bmatrix}
        4 \\
        -2 \\
        17\\
        \end{bmatrix},
        \quad
        \textbf{v}_4 = \begin{bmatrix}
        9
        \end{bmatrix}.
        
    Þetta eru allt dæmi um dálkvigra, vigra sem eru fylki sem eru bara einn dálkur.
  
.. admonition:: Ritháttur
    :class: athugasemd

        Við feitletrum gjarnan breytur sem tákna vigra til að aðgreina þá frá rauntalnabreytum.
        :math:`\textbf{u}, \textbf{v}, \textbf{v}_1, \textbf{v}_2, \textbf{b},`. Önnur leið er að nota 
        örvar: :math:`\vec{u}, \vec{v}, \vec{v}_1, \vec{v}_2, \vec{b}` eða strik:
        :math:`\bar{u}, \bar{v}, \bar{v}_1, \bar{v}_2, \bar{b}`. 

        Einnig má skrifa dálkvigra svona til að spara pláss: 

        .. math:: \begin{bmatrix}
            1 & 2 & 3 & 4 & 5
            \end{bmatrix}^T 
            \text{ eða } 
            (1,2,3,4,5) 
            \text{ í stað }
            \begin{bmatrix}
            1 \\ 2 \\ 3 \\ 4 \\ 5
            \end{bmatrix}.

.. admonition:: Setning
    :class: setning

    Tveir vigrar eru jafnir ef þeir hafa sömu vídd og öll hnit þeirra eru þau sömu.

Skilgreining: Samlagning vigra 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Ef **u** og **v** eru vigrar þannig að 

    .. math:: \textbf{u} = \begin{bmatrix}
        u_{1}\\
        \vdots\\
        u_{n}\\    
        \end{bmatrix}\quad
        \textbf{v} = \begin{bmatrix}
        v_{1}\\
        \vdots\\
        v_{n}\\    
        \end{bmatrix}

    þá er skilgreinum við vigurinn :math:`\textbf{u} + \textbf{v}` sem 

    .. math:: \textbf{u} + \textbf{v} =
        \begin{bmatrix}
        u_{1}+v_{1}\\
        \vdots\\
        u_{n}+v_{n}\\    
        \end{bmatrix}.


Skilgreining: Margföldun vigurs með tölu 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Ef :math:`c` er rauntala og **v** er vigur þannig að

    .. math:: \textbf{v} = \begin{bmatrix}
        v_{1}\\
        \cdots\\
        v_{n}\\    
        \end{bmatrix}

    þá skilgreinum við vigurinn :math:`c\textbf{v}` með

    .. math:: c\textbf{v}=
        \begin{bmatrix}
        cv_{1}\\
        \cdots\\
        cv_{n}\\    
        \end{bmatrix}.

Sýnidæmi: Samlagning vigra og margföldun vigurs með tölu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Margföldun vigurs með tölu:

    .. math:: 2\cdot\begin{bmatrix}
        -1\\3
        \end{bmatrix}
        =
        \begin{bmatrix}
        2\cdot(-1)\\2\cdot 3
        \end{bmatrix}=
        \begin{bmatrix}
        -2\\6
        \end{bmatrix}.

    Samlagning tveggja vigra:

    .. math:: \begin{bmatrix}
        1 \\ 2
        \end{bmatrix} +
        \begin{bmatrix} 
        -1 \\ 3
        \end{bmatrix}
        = \begin{bmatrix} 
        0 \\ 5
        \end{bmatrix}.


    Ef við margföldum vigur með 1, eða leggjum vigurinn saman með núllvigrinum, fáum við alltaf sama vigurinn aftur.

    .. math:: 1\cdot\begin{bmatrix}
        3\\0
        \end{bmatrix}
        =
        \begin{bmatrix}
        1\cdot 3\\1\cdot 0
        \end{bmatrix}=
        \begin{bmatrix}
        3\\ 0
        \end{bmatrix}, \quad
        \begin{bmatrix}
        3\\0
        \end{bmatrix}+\begin{bmatrix}
        0\\0
        \end{bmatrix} = \begin{bmatrix}
        3\\0
        \end{bmatrix}.

    Ef við margföldum vigur með tölunni 0, eða leggjum saman sama vigurinn með öfugu formerki, fáum við núllvigurinn:

    .. math:: 0\cdot\begin{bmatrix}
        2\\-7
        \end{bmatrix}
        =
        \begin{bmatrix}
        0\cdot 2\\0\cdot (-7)
        \end{bmatrix}=
        \begin{bmatrix}
        0\\ 0
        \end{bmatrix}, \quad
        \begin{bmatrix}
        2\\-7
        \end{bmatrix} + \begin{bmatrix}
        -2\\7
        \end{bmatrix}=\begin{bmatrix}
        0\\ 0
        \end{bmatrix}.


Reiknireglur fyrir vigra
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Ef **u**, **v**, **w** eru vigrar í :math:`\mathbb{R}^n` og  :math:`c` og :math:`d` eru
    rauntölur gildir eftirfarandi:

        **1.** :math:`\textbf{u} + \textbf{v}= \textbf{v} + \textbf{u}`

        **2.** :math:`(\textbf{u} + \textbf{v}) + \textbf{w} = \textbf{u} +  (\textbf{v} + \textbf{w})`

        **3.** :math:`\textbf{u} + \textbf{0}= \textbf{0} + \textbf{u} = \textbf{u}`

        **4.** :math:`\textbf{u} + (-\textbf{u})= \textbf{0}`

        **5.** :math:`c(\textbf{u} + \textbf{v})= c\textbf{u} + c\textbf{v}`

        **6.** :math:`(c+d)\textbf{u}= c\textbf{u} + d\textbf{u}`

        **7.** :math:`c(d\textbf{u})= (cd)\textbf{u}`

        **8.** :math:`1\textbf{u}= \textbf{u}`

.. admonition:: Aðvörun
    :class: advorun

    Almennt getum við ekki margfaldað saman tvo vigra og fengið nýjan vigur.
    Við getum heldur ekki deilt einum vigri upp í annan. Stærðirnar 
    :math:`\textbf{v}_1\textbf{v}_2` og :math:`\frac{\textbf{v}_1}{\textbf{v}_2}`
    eru því almennt ekki skilgreindar.

Línulegar samantektir
---------------------

Skilgreining: Línulegar samantektir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`\textbf{v}_1, \textbf{v}_2, \dots, \textbf{v}_p` vera vigra í :math:`\mathbb{R}^n` og :math:`c_1, c_2, \dots, c_p` vera rauntölur. 
    Vigurinn 

    .. math:: \textbf{y}=c_1\textbf{v}_1 +c_2\textbf{v}_2+ \dots+ c_p\textbf{v}_p
    
    kallast **línuleg samantekt** (e. linear combination) vigranna :math:`\textbf{v}_1, \textbf{v}_2, \dots, \textbf{v}_p` með **stuðla/vogstuðla** (e. coefficients, weights) :math:`c_1, c_2, \dots, c_p`.

Sýnidæmi: Línulegar samantektir
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Höfum vigrana 

    .. math:: \textbf{v}_1=
        \begin{bmatrix}
        1\\1\\
        \end{bmatrix}
        \text{ , }
        \textbf{v}_2 =
        \begin{bmatrix}
        0\\-1\\
        \end{bmatrix}
        \text{ og }
        \textbf{y}=\begin{bmatrix}
        3\\2\
        \end{bmatrix}

    Er vigurinn :math:`\textbf{y}` línuleg samantekt af :math:`\textbf{v}_1` og :math:`\textbf{v}_2`? 

.. admonition:: Lausn
    :class: daemi, dropdown

    Já, við getum skrifað

    .. math:: \textbf{y}=
        3\cdot\begin{bmatrix}
        1\\1\\
        \end{bmatrix}
        +1\cdot
        \begin{bmatrix}
        0\\-1\\
        \end{bmatrix}
    
    Svo vigurinn :math:`\ve y` er línuleg samantekt af :math:`\textbf{v}_1` og :math:`\textbf{v}_2` 
    með vogstuðlana 3 og 1.

.. admonition:: Athugasemd
    :class: athugasemd

    **1.**  Vigur :math:`\ve v` er línuleg samantekt af sjálfum sér því við getum skrifað :math:`\textbf{v}=1 \cdot \textbf{v}`.

    **2.**  Núllvigurinn er línuleg samantekt af hvaða vigrum sem er því við getum skrifað 

    .. math:: \textbf{0}=0 \cdot \textbf{v}_1+0 \cdot \textbf{v}_2+\dots+0 \cdot \textbf{v}_p

    **3.**  Ef :math:`\ve m` er meðaltal vigranna :math:`\textbf{v}_1, \textbf{v}_2, \dots, \textbf{v}_p` þá er :math:`\ve m` línuleg samantekt af :math:`\textbf{v}_1, \textbf{v}_2, \dots, \textbf{v}_p` því

    .. math:: \textbf{m}=\frac{1}{p} \textbf{v}_1 +\frac{1}{p} \textbf{v}_2 + \dots + \frac{1}{p} \textbf{v}_p

Sýnidæmi: Línulegar samantektir
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Höfum vigrana 

    .. math:: \textbf{v}_1=
        \begin{bmatrix}
        1\\1\\1\\
        \end{bmatrix}
        \text{ , }
        \textbf{v}_2 =
        \begin{bmatrix}
        0\\2\\3\\
        \end{bmatrix}
        \text{ og }
        \textbf{y}=\begin{bmatrix}
        3\\7\\9\\
        \end{bmatrix}.
    
    Er vigurinn :math:`\ve y` línuleg samantekt af :math:`\textbf{v}_1` og :math:`\textbf{v}_2`?

.. admonition:: Lausn
    :class: daemi, dropdown

    Leysum jöfnuna

    .. math:: x_1\begin{bmatrix}
        1\\1\\1\\
        \end{bmatrix}
        +x_2
        \begin{bmatrix}
        0\\2\\3\\
        \end{bmatrix}=\begin{bmatrix}
        3\\7\\9\\
        \end{bmatrix},
    
    sem jafngildir jöfnuhneppinu

    .. math:: \begin{eqnarray*}
        x_1 &=&3,\\
        x_1 +2x_2&=&7,\\
        x_1+3x_2&=&9.
        \end{eqnarray*}
    
    Skrifum út aukna fylkið og leysum

    .. math:: \begin{align*}
         \left[\begin{array}{@{}cc|c@{}}
            1 & 0 & 3\\
            1 & 2 & 7\\
            1 & 3 & 9\\
        \end{array}\right]
        &\overset{\substack{
        R_2-R_1\\ R_3-R_1}}{\sim}
        \left[\begin{array}{@{}cc|c@{}}
            1 & 0 & 3\\
            0 & 2 & 4\\
            0 & 3 & 6
        \end{array}\right]
        \overset{\substack{
        R_2/2\\ R_3/3}}{\sim}
        \left[\begin{array}{@{}cc|c@{}}
            1 & 0 & 3\\
            0 & 1 & 2\\
            0 & 1 & 2
        \end{array}\right] 
        \overset{\substack{
        R_2-R_3}}{\sim}
        \left[\begin{array}{@{}cc|c@{}}
            1 & 0 & 3\\
            0 & 1 & 2\\
            0 & 0 & 0
       \end{array}\right].
        \end{align*}

    Fáum :math:`x_1=3` og :math:`x_2=2`, svo 

    .. math:: \textbf{y}=
        \begin{bmatrix}
        3\\7\\9\\
        \end{bmatrix} = 3\begin{bmatrix}
        1\\1\\1\\
        \end{bmatrix}
        +2
        \begin{bmatrix}
        0\\2\\3\\
        \end{bmatrix}=3\textbf{v}_1+2\textbf{v}_2
    
    svo :math:`\ve y` er línuleg samantekt af :math:`\textbf{v}_1` og :math:`\textbf{v}_2`.


Spann vigra
-------------

Skilgreining: Spann vigra
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látu :math:`\textbf{v}_1,\dots,\textbf{v}_p` vera vigra í :math:`\mathbb{R}^n`. Mengi allra línulegra samantekta vigranna
    :math:`\textbf{v}_1,\dots,\textbf{v}_p` kallast **spann** (e. span) vigranna, og er táknað
    
    .. math:: \text{span}\{\textbf{v}_1,\dots,\textbf{v}_p\}\subseteq \R^n.
    
    Rita má :math:`\text{span}\{\textbf{v}_1,\dots,\textbf{v}_p\}=\{c_1 \ve v_1 + \cdots + c_p \ve v_p \ | \ c_1,\cdots, c_p \in \R \}`. 


Spann tveggja vigra í :math:`\mathbb{R}^2`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: myndir/linuleg_sponn.svg
    :align: center

Myndin sýnir vigrana :math:`\textbf{v}` og :math:`\textbf{u}`.
Bleika planið, allt :math:`\mathbb{R}^2` rúmið, er línuleg spönn þessa vigra.

.. figure:: myndir/linuleg_sponn_2.svg
    :align: center

Á mynd má sjá vigurinn :math:`\ve v`. Línuleg spönn þessa vigurs eru allir vigrar með endapunkt á línunni,
sem er framhald vigursins :math:`\ve v` í báðar áttir.

Spann tveggja vigra í :math:`\mathbb{R}^3`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`\textbf{v}_1` og :math:`\textbf{v}_2` vera tvo vigra í :math:`\mathbb{R}^3`. Í þessu dæmi myndar
spönn þeirra sléttu sem fer í gegnum upphafspunkt hnitakerfisins.

.. figure:: myndir/nysponn.png
    :align: center
    :scale: 55 %

Línuleg spönn í :math:`\mathbb{R}^3` getur líka verið: bara núllpunkturinn, 
lína í gegnum núllpunkt eða allt :math:`\mathbb{R}^3` rúmið.

Margfeldi fylkis og vigurs 
--------------------------

Skilgreining: Margfeldi fylkis og vigurs 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`A` vera :math:`m\times n` fylki þar sem :math:`\textbf{a}_1, \dots, \textbf{a}_n` eru dálkar þess. 
    Látum :math:`\ve{x}` vera dálkvigur í :math:`\R`. 
    Við skilgreinum margfeldið :math:`A \textbf{x}` með eftirfarandi hætti:

    .. math:: A\textbf{x} = \begin{bmatrix}\textbf{a}_1 \dots \textbf{a}_n\end{bmatrix}
        \begin{bmatrix}
        x_1\\\dots\\x_n
        \end{bmatrix}
        =x_1\textbf{a}_1 +\dots x_n\textbf{a}_n.

    Til að margföldunin :math:`A\textbf{x}` sé framkvæmanleg þarf fjöldi dálka :math:`A` að vera jafn fjöldi lína :math:`\ve{x}`,

    .. math:: \underbrace{\begin{bmatrix}
        a_{11} & a_{12} & \cdots & a_{1n} \\
        a_{21} & a_{22} & \cdots & a_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
        a_{m1} & a_{m2} & \cdots & a_{mn}
        \end{bmatrix}}_{n \text{ dálkar}}
        \left.\begin{bmatrix}
        x_1 \\
        x_2 \\
        \vdots \\
        x_n
        \end{bmatrix}\right\}\small{n\text{ línur}}

    Margfeldið er þá

    .. math:: \begin{bmatrix}
            a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n \\
            a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n \\
            \vdots    \\
            a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n
            \end{bmatrix}\\



.. admonition:: Minnisregla
    :class: athugasemd

    Hugsa má margfeldi fylkis :math:`A` með vigri :math:`\ve x` sem margfeldi sérhverrar línu í :math:`A` með dálkvigrinum :math:`\ve x`.

    .. math:: \begin{bmatrix}
        \rightarrow\\
        \vdots\\
        \rightarrow\\
        \end{bmatrix}\begin{bmatrix}
        \vdots\\
        \downarrow\\
        \vdots
        \end{bmatrix}


Sýnidæmi: Margfeldi fylkis og vigurs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Skoðum margfeldi fylkisins :math:`A` og vigursins :math:`\ve{x}`.

    .. math:: A = \begin{bmatrix}
        2 & 3 & -1 \\
        -1 & 4 & 6
        \end{bmatrix}
        \text{, } \quad
        \textbf{x} = \begin{bmatrix}
        5 \\
        -3 \\
        2
        \end{bmatrix}
        

.. admonition:: Lausn
    :class: daemi, dropdown

    Fáum

    .. math:: \begin{align*}
        A\textbf{x}
        =
        \begin{bmatrix}
        2 & 3 & -1 \\
        -1 & 4 & 6
        \end{bmatrix}
        \begin{bmatrix}
        5 \\
        -3 \\
        2
        \end{bmatrix}&=
        \begin{bmatrix}
        2 \cdot 5 + 3 \cdot (-3) + (-1) \cdot 2 \\
        (-1) \cdot 5 + 4 \cdot (-3) + 6 \cdot 2
        \end{bmatrix}
        \\&=
        \begin{bmatrix}
        10-9-2  \\
        -5-12+12
        \end{bmatrix}
        =
        \begin{bmatrix}
        -1  \\
        -5
        \end{bmatrix}
        \end{align*}


Sýnidæmi: Margfeldi fylkis og vigurs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Skoðum margfeldi eftirfarandi tveggja fylkja og vigurs:

    .. math:: A = \begin{bmatrix}
        0 & 0 \\
        0 & 0 
        \end{bmatrix}
        \text{ , }\quad
        I = \begin{bmatrix}
        1 & 0 \\
        0 & 1 
        \end{bmatrix}
        \text{ , }\quad
        \textbf{x} = \begin{bmatrix}
        2 \\
        -7 \\
        \end{bmatrix}

.. admonition:: Lausn
    :class: daemi, dropdown

    Fáum  

    .. math:: \begin{align*}
        A\textbf{x}
        =
        \begin{bmatrix}
        0 & 0 \\
        0 & 0 
        \end{bmatrix}
        \begin{bmatrix}
        2 \\
        -7 \\
        \end{bmatrix}=
        \begin{bmatrix}
        0\cdot 2 + 0\cdot (-7)\\
        0\cdot 2 + 0\cdot (-7)\\
        \end{bmatrix}=
        \begin{bmatrix}
        0\\
        0
        \end{bmatrix}
        \end{align*}

    og 

    .. math:: \begin{align*}
        I\textbf{x}
        =
        \begin{bmatrix}
        1 & 0 \\
        0 & 1 
        \end{bmatrix}
        \begin{bmatrix}
        2 \\
        -7 \\
        \end{bmatrix}=
        \begin{bmatrix}
        1\cdot 2 + 0\cdot (-7)\\
        0\cdot 2 + 1\cdot (-7)\\
        \end{bmatrix}=
        \begin{bmatrix}
        2\\
        -7
        \end{bmatrix}
        \end{align*}

    Fylkið :math:`I` kallast **einingarfylkið**. Það hefur þann eiginleika að 
    :math:`I \textbf{x}=\textbf{x}` gildir fyrir alla vigra :math:`\ve x`.


Fylkjajafnan
------------

Setning: Fylkjajafnan
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki með dálkvigrum :math:`\textbf{a}_1,\dots,\textbf{a}_n`, :math:`\ve{b}` vera vigur í :math:`\mathbb{R}^m`
    og :math:`\textbf{x}` vera vigur í :math:`\R^n`.
    Jafnan

    .. math:: A\textbf{x} =  \textbf{b}

    þ.e.

    .. math:: x_1\textbf{a}_1 +\dots + x_n \textbf{a}_n = \textbf{b}.

    hefur lausn ef og aðeins ef :math:`\ve b` er í spanni dálkvigra :math:`A`.

.. admonition:: Athugasemd
    :class: athugasemd

    Það er alltaf hægt að gá hvort víddirnar passi. Látum :math:`A` :math:`m\times n` fylki, :math:`\ve x` vera :math:`n \times 1` vigur og :math:`\ve b` vera :math:`m \times 1`

    .. math:: (m\times n) \cdot (n \times 1) = m \times 1.



Sýnidæmi: Fylkjajafnan
^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Fyrir hvaða :math:`b_1` og :math:`b_2` hefur eftirfarandi jöfnuhneppi lausn?

    .. math:: \begin{eqnarray*}
        x_1+x_2 = b_1\\
        x_1-x_2 = b_2
        \end{eqnarray*}

.. admonition:: Lausn
    :class: daemi, dropdown

    Lítum á aukna fylkið og einföldum það með línuaðgerðum. Fáum

    .. math:: \left[\begin{array}{@{}cc|c@{}}
        1 & 1 & b_1\\
        1& -1 & b_2
        \end{array}\right]\sim 
        \left[\begin{array}{@{}cc|c@{}}
        1 & 1 & b_1\\
        0& -2 & b_2-b_1
        \end{array}\right]
    
    Með því að líta á forystustuðlana, :math:`\blacksquare`, 

    .. math:: \left[\begin{array}{@{}cc|c@{}}
        \blacksquare & * & *\\
        0& \blacksquare & *
        \end{array}\right]
    
    Hér má sjá að dálkurinn lengst til hægri er ekki vendidálkur svo jöfnuhneppið hefur alltaf lausn.

Sýnidæmi: Fylkjajafnan
^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Fyrir hvaða :math:`b_1,b_2,b_3` hefur eftirfarandi jöfnuhneppi lausn?

    .. math:: \begin{eqnarray*}
        x_1+2x_2+3x_3 = b_1\\
        4x_1+5x_2+6x_3 = b_2\\
        7x_1+8x_2+9x_3 = b_3
        \end{eqnarray*}

.. admonition:: Lausn
    :class: daemi, dropdown

    Skoðum aukna fylkið og fáum

    .. math:: \begin{align*}
        \left[\begin{array}{@{}ccc|c@{}}
        1 & 2 & 3 &b_1\\
        4 & 5 & 6 &b_2\\
        7 & 8 & 9 &b_3\\
        \end{array}\right]&\sim
        \left[\begin{array}{@{}ccc|c@{}}
        1 & 2 & 3& b_1\\
        0 & -3 & -6 &b_2 -4b_1\\
        0 & -6 & -12 &b_3-7b_1\\
        \end{array}\right]\\&\sim
        \left[\begin{array}{@{}ccc|c@{}}
        1 & 2 & 3& b_1\\
        0 & -3 & -6 &b_2 -4b_1\\
        0 & 0 & 0 &b_3-7b_1-2(b_2-4b_1)\\
        \end{array}\right]
        \end{align*}

    Einföldum stakið neðst til hægri og fáum :math:`b_3-7b_1-2(b_2-4b_1) = b_1-2b_2+b_3`.
    Við erum því með aukna fylkið

    .. math:: \left[\begin{array}{@{}ccc|c@{}}
        1 & 2 & 3& b_1\\
        0 & -3 & -6 &b_2 -4b_1\\
        0 & 0 & 0 &b_1-2b_2+b_3\\
        \end{array}\right]

    Aukna fylkið á efri ruddri stallagerð hefur því formin

    .. math:: \left[\begin{array}{@{}ccc|c@{}}
        \blacksquare & * & *&*\\
        0& \blacksquare & * &*\\
        0& 0& 0& \blacksquare
        \end{array}\right]
        \text{ eða }
        \left[\begin{array}{@{}ccc|c@{}}
        \blacksquare & * & *&*\\
        0& \blacksquare & * &*\\
        0& 0& 0& 0
        \end{array}\right] 

    allt eftir því hvort stærðin :math:`b_1-2b_2+b_3` sé núll eða ekki. 
    Jöfnuhneppið okkar hefur lausn þá og því aðeins að dálkurinn lengst til hægri sé ekki vendidálkur.
    Jöfnuhneppið því því lausn þá og því aðeins að :math:`b_1-2b_2+b_3=0`.

Setning: Fullyrðingar um fylkjajöfnuna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki. Eftirfarandi fullyrðingar eru jafngildar.

        **1.** Jafnan :math:`A \textbf{x} = \textbf{b}` hefur lausn fyrir sérhvert :math:`\textbf{b} \in \mathbb{R}^m`.

        **2.** Sérhvert :math:`\textbf{b} \in \mathbb{R}^m` er línuleg samantekt af dálkum fylkisins :math:`A`.

        **3.** Dálkar fylkisins :math:`A` spanna :math:`\mathbb{R}^m`.

        **4.** :math:`A` hefur vendistak í hverri línu.

Setning: Um fylki og dálkvigur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki, látum :math:`\textbf{u}` og :math:`\textbf{v}` vera 
    dálkvigra í :math:`\mathbb{R}^n` og látum :math:`c` vera rauntölu. Þá gildir:

        **1.** :math:`A(\textbf{u} + \textbf{v}) = A\textbf{u} + A\textbf{v}`.

        **2.** :math:`A(c\textbf{u}) = cA\textbf{u}`


Skilgreining: Óhliðruð jöfnuhneppi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Línulegt jöfnuhneppi sem skrifa má á forminu :math:`A\textbf{x}=\textbf{0}` er sagt **óhliðrað** (e. homogeneous).
    Slíkt jöfnuhneppi hefur núlllausnina alltaf sem lausn því

    .. math:: A\left.\begin{bmatrix}
        0 \\ 0\\ \vdots \\ 0
        \end{bmatrix}\right\}n =\left. \begin{bmatrix}
        0 \\ \vdots \\ 0
        \end{bmatrix}\right\}m.

    Þessi lausn er kölluð **fáfengilega lausnin** (e. trivial solution). Ef aðrar lausnir eru til eru 
    þær kallaðar **ófáfengilegar** (e. nontrivial solutions). Stundum er fáfengilega lausnin kölluð **augljósa lausnin**.

Sýnidæmi: Óhliðrað jöfnuhneppi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Leysum

    .. math:: \begin{eqnarray*}
        x_1+2x_2+3x_3 = 0\\
        4x_1+5x_2+6x_3 =0\\
        7x_1+8x_2+9x_3 =0
        \end{eqnarray*}

.. admonition:: Lausn
    :class: daemi, dropdown

    Fáum

    .. math:: \left[\begin{array}{@{}ccc|c@{}}
        1 & 2 & 3 &0\\
        4 & 5 & 6 &0\\
        7 & 8 & 9 &0\\
        \end{array}\right]
        \sim
        \left[\begin{array}{@{}ccc|c@{}}
        1 & 2 & 3& 0\\
        0 & -3 & -6 &0\\
        0 & 0 & 0 &0\\
        \end{array}\right]
        \sim
        \left[\begin{array}{@{}ccc|c@{}}
        1 & 2 & 3& 0\\
        0 & 1 & 2 &0\\
        0 & 0 & 0 &0\\
        \end{array}\right]\\
        \sim
        \left[\begin{array}{@{}ccc|c@{}}
        1 & 0 & -1& 0\\
        0 & 1 & 2 &0\\
        0 & 0 & 0 &0\\
        \end{array}\right]
    
    Sem jafngildir

    .. math:: \begin{aligned}
        x_1 -x_3 =0,\\
        x_2+2x_3=0,
        \end{aligned}
    
    þ.e.

    .. math:: \begin{aligned}
        x_1 =x_3,\\
        x_2=-2x_3,
        \end{aligned}

    
    sem skrifa má

    .. math:: \textbf{x} =\begin{bmatrix}
        x_1\\x_2\\x_3
        \end{bmatrix}=\mathop{\begin{bmatrix}
        x_3\\-2x_3\\x_3
        \end{bmatrix}} =
        x_3\begin{bmatrix}
        1\\-2\\1
        \end{bmatrix}.
    
    Með því að setja :math:`x_3=t` má rita allar lausnir á forminu
    :math:`\textbf{x} = t \textbf{v}` þar sem 
    :math:`\textbf{v} = \begin{bmatrix} 1\\-2\\1 \end{bmatrix}\text{ og } t\in \mathbb{R}`.
    
    T.d. :math:`t=1` gefur lausnina :math:`\textbf{x} = \begin{bmatrix} 1\\-2\\1\end{bmatrix}`. Jöfnuhneppið hefur ófáfengilega lausn.

.. admonition:: Athugasemd
    :class: athugasemd

    **1.** Óhliðraða jöfnuhneppið :math:`A\textbf{x} = \textbf{0}` hefur alltaf lausn.

    **2.** Óhliðraða jöfnuhneppið :math:`A\textbf{x} = \textbf{0}` hefur ófáfengilega lausn þá og því aðeins að það hafi minnst eina frjálsa breytu.
 
Fólgin og stikaframsetning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Almenn leið til þess að rita lausnir á stikaframsetningu er að

    **1.** Koma aukna fylkinu á  (rudda) efri stallagerð.

    **2.** Rita háðu breyturnar með hinum frjálsum.

    **3.** Umrita lausnavigurinn og sýna hann sem samantekt af einhverjum vigrum, með frjálsu breytunum sem stika. 

Best er að lýsa þessum tveimur framsetningum með dæmum. 

.. admonition:: Dæmi
    :class: daemi

    **Fólgin framsetning** (e. implicit form)
        :math:`\qquad`    Slétta   :math:`\quad\quad\quad\quad\quad\quad\quad\begin{aligned} x_1-2x_2-3x_3=0\end{aligned}`
        
        :math:`\qquad`    Lína     :math:`\quad\quad\quad\quad\quad\quad\quad\begin{aligned} x_1+2x_2+3x_3 = 0\\ 4x_1+5x_2+6x_3 =0\\\end{aligned}`


    **Stikaframsetning** (e. parametric form)
        :math:`\qquad` Slétta
        
        .. math:: \textbf{x} = s\begin{bmatrix}
            2\\1\\0 
            \end{bmatrix} + t\begin{bmatrix}
            3\\0\\1 
            \end{bmatrix}, s,t\in \R.
        
   
        :math:`\qquad` Lína

        .. math:: \textbf{x} = t \begin{bmatrix}
            1\\-2\\1
            \end{bmatrix}, t\in \R. 
 

Sýnidæmi: Stikaframsetning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Leysið eftirfarandi jöfnuhneppi með einni jöfnu

    .. math:: \begin{align*}
        x_1-2x_2-3x_3=0\end{align*}
    
.. admonition:: Lausn
    :class: daemi, dropdown

    Fáum að :math:`x_1 = 2x_2 +3x_3` þar sem :math:`x_2` og :math:`x_3` eru frjálsar breytur. 
    Þannig fæst

    .. math:: \textbf{x} = \begin{bmatrix}
        x_1\\x_2\\x_3 
        \end{bmatrix}= 
        \begin{bmatrix}
        2x_2+3x_3\\x_2\\x_3 
        \end{bmatrix}=
        \begin{bmatrix}
        2x_2\\x_2\\0 
        \end{bmatrix}+
        \begin{bmatrix}
        3x_3\\0\\x_3 
        \end{bmatrix}
        =x_2\begin{bmatrix}
        2\\1\\0 
        \end{bmatrix}+
        x_3\begin{bmatrix}
        3\\0\\1 
        \end{bmatrix}

    Getum því skrifað :math:`\textbf{x} = s\text{u} + t \textbf{v}` með 
    :math:`\textbf{u} =\begin{bmatrix} 2&1&0 \end{bmatrix}^T`  og 
    :math:`\textbf{v}= \begin{bmatrix} 3&0&1 \end{bmatrix}^T` og 
    :math:`s,t \in \mathbb{R}`.
    Þetta er dæmi um stikaframsetningu á lausn.



Skilgreining: Hliðruð jöfnuhneppi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Jöfnuhneppi sem sett er fram á forminnu :math:`A \textbf{x}=\textbf{b}` 
    þar sem :math:`\textbf{b} \neq 0` kallast **hliðrað** (e. non-homogeneus).

Sýnidæmi: Hliðrað jöfnuhneppi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Leysum löfnuhneppið

    .. math:: \begin{eqnarray*}
        x_1+2x_2+3x_3 = 0\\
        4x_1+5x_2+6x_3 =1\\
        7x_1+8x_2+9x_3 =2
        \end{eqnarray*}

.. admonition:: Lausn
    :class: daemi, dropdown

    Fáum

    .. math:: \begin{align*}
        \left[\begin{array}{@{}ccc|c@{}}
        1 & 2 & 3 &0\\
        4 & 5 & 6 &1\\
        7 & 8 & 9 &2\\
        \end{array}\right] &\sim
        \left[\begin{array}{@{}ccc|c@{}}
        1 & 2 & 3& 0\\
        0 & -3 & -6 &1\\
        0 & -6 & -12 &2\\
        \end{array}\right]
        \sim 
        \left[\begin{array}{@{}ccc|c@{}}
        1 & 2 & 3& 0\\
        0 & -3 & -6 &1\\
        0 & 0 & 0 &0\\
        \end{array}\right]
        \\&\sim 
        \left[\begin{array}{@{}ccc|c@{}}
        1 & 2 & 3& 0\\
        0 & 1 & 2 &-\frac{1}{3}\\
        0 & 0 & 0 &0\\
        \end{array}\right]
        \sim 
        \left[\begin{array}{@{}ccc|c@{}}
        1 & 0 & -1& \frac{2}{3}\\
        0 & 1 & 2 &-\frac{1}{3}\\
        0 & 0 & 0 &0\\
        \end{array}\right]
        \end{align*} 
    
    svo 

    .. math:: \textbf{x} = \begin{bmatrix}
        x_1\\x_2\\x_3
        \end{bmatrix}
        = \begin{bmatrix}
        x_3+\frac{2}{3}\\-2x_3-\frac{1}{3}\\x_3
        \end{bmatrix}=
        x_3\begin{bmatrix}
        1\\-2\\1
        \end{bmatrix}+
        \begin{bmatrix}
        \frac{2}{3}\\-\frac{1}{3}\\0
        \end{bmatrix}
    
    Við sjáum við að lausnarmengið er það sama og fyrir óhliðraða 
    jöfnuhneppið nema að við bætist vigur :math:`\begin{bmatrix}\frac{2}{3}\\-\frac{1}{3}\\0\end{bmatrix}`.
    Við getum því skrifað allar lausnir á forminu :math:`\textbf{x} = t\textbf{v} + \textbf{p}` þar sem er almenn lausn 
    á óhliðruðu jöfnunni og  **p** ein lausn á þeirri hliðruðu.

Setning: Lausnamengi fylkjajöfnunnar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Gerum ráð fyrir að fylkjajafnan :math:`A\textbf{x} = \textbf{b}` 
    hafi lausn fyrir gefið :math:`\ve{b}` og látum :math:`\ve{p}` vera slíka lausn. 
    Þá gildir að öll stök í lausnamengi :math:`A\textbf{x} = \textbf{b}` 
    má rita á forminu :math:`\textbf{w} = \textbf{p} + \textbf{v}_h` þar sem :math:`\textbf{v}_h` 
    er lausn óhliðruðu jöfnunnar :math:`A\textbf{x} = \textbf{0}`.


Sýnidæmi: Lausnir prófaðar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Skoðum aftur jöfnuhneppið 

    .. math:: \begin{eqnarray*}
        x_1+2x_2+3x_3 = 0\\
        4x_1+5x_2+6x_3 =1\\
        7x_1+8x_2+9x_3 =2
        \end{eqnarray*}
    
    og hugsum það á forminu :math:`A \textbf{x}=\textbf{b}`. 
    Við fundum að lausnin var á forminu

    .. math:: \textbf{x} = 
        t\begin{bmatrix}
        1\\-2\\1
        \end{bmatrix}+
        \begin{bmatrix}
        \frac{2}{3}\\-\frac{1}{3}\\0
        \end{bmatrix}
    
    Prófið lausnina til að staðfesta að hún séu rétt.

.. admonition:: Lausn
    :class: daemi, dropdown

    Prófum lausnina

    .. math:: \begin{align*}
        A\textbf{x} &=
        A\left(t\begin{bmatrix}
        1\\-2\\1
        \end{bmatrix}+
        \begin{bmatrix}
        \frac{2}{3}\\-\frac{1}{3}\\0
        \end{bmatrix} \right) \\
        &=
        tA
        \begin{bmatrix}
        1\\-2\\1
        \end{bmatrix}
        +A
        \begin{bmatrix}
        \frac{2}{3}\\-\frac{1}{3}\\0\end{bmatrix}\\
        &=t
        \begin{bmatrix}
        1 & 2 & 3\\
        4 & 5 & 6\\
        7 & 8 & 9\\
        \end{bmatrix}
        \begin{bmatrix}
        1\\-2\\1
        \end{bmatrix}
        +
        \begin{bmatrix}
        1 & 2 & 3\\
        4 & 5 & 6\\
        7 & 8 & 9\\
        \end{bmatrix}
        \begin{bmatrix}
        \frac{2}{3}\\-\frac{1}{3}\\0
        \end{bmatrix}\\&=
        t     \begin{bmatrix}
        0\\0\\0
        \end{bmatrix}+
        \begin{bmatrix}
        0\\1\\2
        \end{bmatrix}=t\textbf{0} + \textbf{b}\ = \textbf{b}
        \end{align*}



Línulega óháðar upptalningar vigra
----------------------------------------

Skilgreining: Línulega óháðar upptalningar vigra
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    **(i)** Upptalning af vigrum :math:`\{\textbf{v}_1, \dots ,\textbf{v}_p\}` í :math:`\R^n` er sögð **línulega óháð** (e. linearly independent) ef jafnan
    
    .. math:: x_1\text{v}_1 +  x_2\text{v}_2+ \dots + x_p\textbf{v}_p = \textbf{0}

    hefur einungis fáfengilegu lausnina :math:`x_1 = x_2 = \dots = x_p =0`.


    **(ii)** Upptalning af vigrum :math:`\{\textbf{v}_1, \dots ,\textbf{v}_p\}` í :math:`\R^n` er sögð **línulega háð** (e. linearly dependent)
    ef til eru tölur :math:`c_1,\dots,c_p`, ekki allar jafnar 0, þannig að 

    .. math:: c_1\textbf{v}_1 + \dots+ c_p\textbf{v}_p = \textbf{0}.

    Við segjum oft að vigrarnir :math:`\ve v_1, \dots, \ve v_2` séu línulega óháðir ef upptalningin :math:`\{\ve v_1, \dots, \ve v_p\}` er línulega óháð.

.. admonition:: Athugasemd
    :class: athugasemd

    **1.** Upptalning þar sem :math:`\ve 0`-vigurinn kemur fyrir er alltaf línulega háð.

    **2.** Upptalning þar sem sami vigurinn kemur fyrir oftar en einu sinni er línulega háð.

    **3.** Upptalning með einum vigri :math:`\ve v` er línulega óháð ef og aðeins ef :math:`\ve v \neq \ve 0`.

    **4.** Upptalning :math:`\{\ve v_1, \ve v_2 \}` er línulega háð ef og aðeins ef annar vigurinn er margfeldi af hinum. Slík upptalning er línulega óháð ef hvorugur vigurinn er margfeldi af hinum.


Sýnidæmi: Línulega óháðir vigrar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Eru eftirfarandi vigrar línulega óháðir?

    .. math:: \textbf{v}_1 = \begin{bmatrix}
        1\\1
        \end{bmatrix},
        \textbf{v}_2=\begin{bmatrix}
        0\\1
        \end{bmatrix},
        \textbf{v}_3 = \begin{bmatrix}
        2\\1
        \end{bmatrix}.
    
    
.. admonition:: Lausn
    :class: daemi, dropdown

    Þar sem 

    .. math:: 2\begin{bmatrix}
        1\\1
        \end{bmatrix}
        -\begin{bmatrix}
        0\\1
        \end{bmatrix}
        - \begin{bmatrix}
        2\\1
        \end{bmatrix}=\textbf{0}

    eru vigrarnir þrír línulega háðir.


Sýnidæmi: Línulega óháðir vigrar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Eru vigrarnir 

    .. math:: \textbf{v}_1 = \begin{bmatrix}
        1\\0\\0
        \end{bmatrix},
        \textbf{v}_2=\begin{bmatrix}
        0\\1\\1
        \end{bmatrix},
        \textbf{v}_3 = \begin{bmatrix}
        2\\2\\1
        \end{bmatrix},

    línulega óháðir?

.. admonition:: Lausn
    :class: daemi, dropdown

    Athugum hvort 

    .. math:: x_1 \begin{bmatrix}
        1\\0\\0
        \end{bmatrix}+
        x_2\begin{bmatrix}
        0\\1\\1
        \end{bmatrix}+
        x_3 \begin{bmatrix}
        2\\2\\1
        \end{bmatrix} = \begin{bmatrix}
        0\\0\\0
        \end{bmatrix}
    
    hefur aðeins fáfengilegu lausnina. Fáum

    .. math:: \begin{bmatrix}
        1&0&2\\
        0&1&2\\
        0&1&1
        \end{bmatrix}
        \begin{bmatrix}
        x_1\\x_2\\x_3
        \end{bmatrix} = \begin{bmatrix}
        0\\0\\0
        \end{bmatrix}
    
    Fáum nú

    .. math:: \left[\begin{array}{@{}ccc|c@{}}
        1&0&2&0\\
        0&1&2&0\\
        0&1&1&0
        \end{array}\right]\sim
        \left[\begin{array}{@{}ccc|c@{}}
        1&0&2&0\\
        0&1&2&0\\
        0&0&-1&0
        \end{array}\right].

    Síðasta aukna fylkið er af efri stallagerð og hefur vendistak 
    í hverjum dálki nema þeim lengst til hægri. Því hefur þetta jöfnuhneppi
    aðeins eina lausn, fáfengilegu lausnina :math:`x_1=x_2=x_3=0` og vigrarnir 
    sem um ræðir eru línulega óháðir.


Setning: Dálkvigrar fylkis og línulegt óhæði
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Dálkvigrar fylkis :math:`A` eru línulega óháðir ef og aðeins ef jöfnuhneppið 
    :math:`A\textbf{x} = \textbf{0}` hafur einungis fáfengilegu lausnina, :math:`\ve x= \ve 0`.


Setning: Of margir vigrar = línulega háð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`\textbf{v}_1, \dots, \textbf{v}_p` vera upptalningu vigra í :math:`\mathbb{R}^n`. 
    Ef :math:`p>n` þá er upptalningin línulega háð.

Setningin segir að ef við höfum fleiri vigra en eru hnit í hverjum
vigri þá eru vigrarnir línulega háðir.

Setning: Línuleg samantekt og línulegt hæði
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Upptalning :math:`S=\{ \ve v_1, \dots, \ve v_p\}` af vigrum í :math:`\R^n` með :math:`\ve v_1  \neq \ve 0` er línulega háð ef og aðeins ef hægt er að rita einhvern vigranna
    :math:`\ve v_1, \dots, \ve v_p` sem línulega samantekt hinna vigranna.

    Hægt er að sýna að ef upptalningin er línulega háð og :math:`\ve v_1 \neq \ve 0` þá er til vigur :math:`\ve v_j` sem má rita sem línulega samantekt vigranna sem eru á
    undan honum í upptalningunni, þ.e.a.s. til eru tölur :math:`c_1, \dots, c_{j-1}` þannig að

    .. math:: \ve v_j = c_1 \ve v_1 + \dots + c_{j-1} \ve v_{j-1}.




Línulegar varpanir
------------------

**Vörpun** (e. map, mapping, transformation) frá mengi :math:`A` yfir í mengi :math:`B` er „regla" 
sem úthlutar sérhverju staki úr :math:`A` nákvmlega einu staki úr :math:`B`, yfirleitt táknað :math:`f: A \rightarrow B`. Mengið :math:`A` kallast **skilgreiningarmengi/formengi** (e. domain) og :math:`B` **ráðstöfunarmengi/bakmengi** (e. codomain) vörpunarinnar :math:`f`.


Látum :math:`A` vera :math:`m \times n` fylki. Skilgreinum vörpun :math:`T: \mathbb{R}^n \rightarrow \mathbb{R}^m`
þannig að fyrir :math:`\textbf{x} \in \mathbb{R}^n` þá er

.. math:: T(x)=A\textbf{x}.

Oft er hentugt að segja að vörpunin sé skilgreind sem :math:`\textbf{x} \mapsto A\textbf{x}`.
Ef vigur **x** varpast í :math:`T(\textbf{x})` þá segjum við að
:math:`T(\textbf{x})` sé **mynd** vigursins :math:`x` með tillit til :math:`T`. 
Mengi allra slíkra mynda kallast **myndmengi** :math:`T` (e. image). 

Skilgreining: Línulegar varpanir 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Vörpun :math:`T \colon \mathbb{R}^n\rightarrow\mathbb{R}^m` 
    er **línuleg vörpun** ef um öll :math:`\textbf{u}, \textbf{v} \in \mathbb{R}^n` og
    allar rauntölur :math:`c` gildir:
    
        **1.** :math:`T(\textbf{u} + \textbf{v})= T(\textbf{u}) + T(\textbf{v})`
        
        **2.** :math:`T(c\textbf{u}) = cT(\textbf{u})`.

Setning: Línulegar varpanir :math:`\mathbb{R}^n\rightarrow\mathbb{R}^m`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m \times n` fylki. Vörpunin :math:`T \colon \R^n \rightarrow \R^m` skilgreind með :math:`T(\ve x)= A \ve x` er línuleg.



Skilgreining: Eiginleikar línulegra varpana 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`T \colon \mathbb{R}^n\rightarrow\mathbb{R}^m` vera línulega vörpun. Þá gildir

        **1.** :math:`T(\textbf{0})=\textbf{0}`

        **2.** Ef :math:`\textbf{u},\textbf{v}` eru vigrar í :math:`\mathbb{R}^n` og :math:`c, d \in \R` þá er 
               
            .. math:: T(c\textbf{u}+d\textbf{v})=cT(\textbf{u})+dT(\textbf{v}).

        **3.** Ef :math:`\textbf{u}_1,\textbf{u}_2,\dots,\textbf{u}_p` 
        er rupptalning á vigrum og :math:`c_1, c_2, \dots, c_p`
        er upptalning á tölum þá er 

        .. math:: T(c_1\textbf{u}_1+c_2\textbf{u}_2+\cdots+c_p\textbf{u}_p)=c_1T(\textbf{u}_1)+c_2T(\textbf{u}_2)+\cdots+c_pT(\textbf{u}_p). 

Skilgreining: Venjulegi grunnurinn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Upptalningin

    .. math:: \ve e_1 = \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix},
        \quad \ve e_2 = \begin{bmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{bmatrix},
        \quad, \dots, \quad \ve e_n = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix},

    mynda svokallaðan **venjulega grunn** (e. standard basis) fyrir :math:`\R^n`. Sérhvern vigur í :math:`\R^n` má skri fa sem línulega samantekt af vigrum venjulega grunnsins á nákvæmlega einn hátt

    .. math:: \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix} = 
        x_1 \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix} + 
        x_2 \begin{bmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{bmatrix} + 
        \dots +
        x_n \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix}. 
         


Sýnidæmi Línuleg vörpun :math:`\mathbb{R}^2\rightarrow \mathbb{R}^2` 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Segjum að við höfum línulega vörpun  :math:`T \colon \mathbb{R}^2 \rightarrow \mathbb{R}^2`
    þannig að 

    .. math:: T(\textbf{e}_1)=T\left(\begin{bmatrix}
        1\\0
        \end{bmatrix}\right) = \begin{bmatrix}
        -2\\-1
        \end{bmatrix} \text { og }
        T(\textbf{e}_2) =T\left(\begin{bmatrix}
        0\\1
        \end{bmatrix}\right) = \begin{bmatrix}
        3\\0
        \end{bmatrix}.
    
    Hvað er :math:`T\left(\begin{bmatrix} 4\\5\end{bmatrix}\right)`?

.. admonition:: Lausn
    :class: daemi, dropdown

    Notum að vörpunin :math:`T` er línuleg og fáum

    .. math:: \begin{align*}
        T\left(\begin{bmatrix}
        4\\5
        \end{bmatrix}\right) &= T\left(4\begin{bmatrix}
        1\\0
        \end{bmatrix} +5\begin{bmatrix}
        0\\1
        \end{bmatrix}\right) =4T\left(\begin{bmatrix}
        1\\0
        \end{bmatrix}\right) +5T\left(\begin{bmatrix}
        0\\1
        \end{bmatrix}\right) \\&
        = 4\cdot \begin{bmatrix}
        -2\\-1
        \end{bmatrix}+5\cdot\begin{bmatrix}
        3\\0
        \end{bmatrix}=\begin{bmatrix}
        4(-2)+5\cdot 3\\ 4(-1) + 5\cdot 0
        \end{bmatrix}=\begin{bmatrix}
        7\\ -4
        \end{bmatrix}.
        \end{align*}

Setning: Venjulegi grunnurinn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Setning
    :class: setning

    Látum :math:`T \colon \mathbb{R}^n\rightarrow\mathbb{R}^m` vera línulega vörpun, og 
    :math:`A` vera :math:`m \times n` fylki með :math:`A=\begin{bmatrix} T(\textbf{e}_1) &\dots& T(\textbf{e}_n) \end{bmatrix}`.
    Þá gildir um öll :math:`\textbf{x} \in \mathbb{R}^n` að :math:`T(\textbf{x})=A\textbf{x}` og :math:`A` er eina fylkið með þennan eiginleika.
    Við köllum fylkið :math:`A` gjarnan **venjulega fylkið** (e. standard matrix) fyrir :math:`T`,
    og segjum að línulega vörpunin :math:`T` sé gefin með fylkinu :math:`A`.

Skoðum nú nokkrar varpanir og fylki þeirra myndrænt.

Speglanir
~~~~~~~~~

Speglun um x-ás: :math:`\begin{bmatrix} 1 & 0 \\ 0 &-1 \end{bmatrix}`

.. figure:: myndir/speglunx.svg
    :align: center
    :scale: 75%

Speglun um y-ás: :math:`\begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}`

.. figure:: myndir/spegluny.svg
    :align: center
    :scale: 60%

Speglun um línuna x=y :math:`\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}`

.. figure:: myndir/speglun_y=x.svg
    :align: center
    :scale: 75%

Speglun um línuna y=-x :math:`\begin{bmatrix} 0 & -1 \\ -1 & 0 \end{bmatrix}`

.. figure:: myndir/speglun_y=-x.svg
    :align: center
    :scale: 75%

Speglun um núllpunkturinn :math:`\begin{bmatrix} -1 & 0 \\ 0 &-1 \end{bmatrix}`

.. figure:: myndir/speglun_0.svg
    :align: center
    :scale: 75%

Stríkkanir
~~~~~~~~~~

Lárétt stríkkun :math:`\begin{bmatrix} k & 0 \\ 0 & 1 \end{bmatrix}`

.. figure:: myndir/larett_strikkun.svg
    :align: center
    :scale: 75%

og

.. figure:: myndir/larett_strikkun_2.svg
    :align: center
    :scale: 75%

Lóðrétt stríkkun :math:`\begin{bmatrix} 1 & 0 \\ 0 & k \end{bmatrix}`

.. figure:: myndir/lodrett_strikkun.svg
    :align: center
    :scale: 75%

og

.. figure:: myndir/lodrett_strikkun_2.svg
    :align: center
    :scale: 75%

Skekkingar
~~~~~~~~~~

Lárétt skekking :math:`\begin{bmatrix} 1 & k \\ 0 & 1 \end{bmatrix}`

.. figure:: myndir/latrett_skekking.svg
    :align: center
    :scale: 75%

Lóðrétt skekking :math:`\begin{bmatrix} 1 & 0 \\ k & 1 \end{bmatrix}`

.. figure:: myndir/lodrett_skekking.svg
    :align: center
    :scale: 75%

Ofanvörp
~~~~~~~~~

Ofanvarp á x-ás :math:`\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}`

.. figure:: myndir/ofanvarp_x.svg
    :align: center
    :scale: 75%

Ofanvarp á y-ás :math:`\begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}`

.. figure:: myndir/ovanvarp_y.svg
    :align: center
    :scale: 75%


Eintækar og átækar varpanir
---------------------------

Skilgreining: Eintækar og átækar varpanir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Vörpun :math:`f\colon X \rightarrow Y` er

        **(i)** **eintæk** (e. injective, one-to-one) ef hún varpar ólíkum stökum í ólík stök. Þ.e. ef :math:`x_1, x_2 \in X` og
        :math:`x_1 \neq x_2` þá er :math:`f(x_1) \neq f(x_2)`.

        **(ii)** **átæk** (e. surjective, onto) ef um sérhvert :math:`y \in Y` gildir að til er :math:`x \in X` þannig að :math:`y=f(x)`.

        **(iii)** **gagntæk** (e. bijective) ef hún er bæði eintæk og átæk.

Eintæk vörpun:

.. figure:: myndir/eintaek.svg
    :align: center
    :scale: 10%

Átæk vörpun:

.. figure:: myndir/ataek.svg
    :align: center
    :scale: 10%


.. admonition:: Athugasemd
    :class: athugasemd

    Við getum líka skilið eintækni og átækni út frá fjölda lausna. Vörpun :math:`f \colon X \rightarrow Y` er

        **(i)** eintæk ef of aðeins ef jafnan :math:`y = f(x)` hefur í *mesta lagi eina lausn* :math:`x \in X` fyrir sérhvert :math:`y \in Y`.

        **(ii)** átæk ef og aðeins ef :math:`y = f(x)` hefur að *minnsta kosti eina lausn*  :math:`x \in X` fyrir sérhvert :math:`y \in Y`.

        **(iii)** gagntæk ef og aðeins ef :math:`y = f(x)` hefur *nákvæmlega eina lausn* :math:`x \in X` fyrir sérhvert :math:`y \in Y`.


Sýnidæmi: Eintækar og átækar varpanir
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

        **1.** Dæmi um eintæka vörpun: :math:`f \colon \R \rightarrow \R`, :math:`x \mapsto e^x`.

        **2.** Dæmi um átæka vörpun: :math:`f \colon \R \rightarrow\R`, :math:`x \mapsto x (x^2 -3)`.

        **3.** Dæmi um gagntæka vörpun: :math:`f \colon \R \rightarrow \R`, :math:`x \mapsto 2x +1`.


        **4.** Dæmi um vörpun sem er hvorki eintæk, átæk né gagntæk: :math:`f \colon \R \rightarrow \R`, :math:`x \mapsto x^2`. Hins vegar ef við breytum skilgreiningar- og bakmenginu í :math:`[0,\infty)` þá væri fallið gagntækt.


Setning: Eintæk línuleg vörpun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m \times n` fylki og :math:`U` efra stallaform :math:`A`. Eftirfarandi skilyrði eru jafngild

        **1.** Það er forystustuðull í sérhverjum dálki :math:`U`.

        **2.** Jafnan :math:`A \ve x = \ve 0` hefur einungis fáfengilegu lausnina, :math:`\ve x = \ve 0`.

        **3.** Dálkvigrar fylkisins :math:`A` eru línulega óháðir.

        **4.** Vörpunin :math:`T \colon \R^n \rightarrow \R^m`, :math:`\ve x \mapsto A \ve x` er eintæk.


Setning: Átæk línuleg vörpun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m \times n` fylki og :math:`U` efra stallaform :math:`A`. Eftirfarandi skilyrði eru jafngild

        **1.** Það er forystustuðull í sérhverri línu :math:`U`.

        **2.** Fyrir sérhvert :math:`\ve b \in \R^m` þá hefur jafnan :math:`A \ve x = \ve b` lausn.

        **3.** Dálkvigrar fylkisins :math:`A` spanna allt :math:`\R^m`.

        **4.** Vörpunin :math:`T \colon \R^n \rightarrow \R^n`, :math:`\ve x \mapsto A \ve x` er átæk.
