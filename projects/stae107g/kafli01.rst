Kafli
=====

Línuleg Algebra er sú grein innan stærðfræðinnar sem fæst við línuleg jöfnuhneppi,
vigra, vigurrúm, línulegar varpanir og önnur tengd viðfangsefni. Í þessu námskeiði 
verður farið yfir helstu hugtök í línulegri algebru. Farið verður yfir: línuleg 
jöfnuhneppi, fylki, ákveður, vigra og vigurrúm, eiginvigra og eigingildi og innfeldi. 
Hagnýtingar línulegrar algebru má meðal annars finna innan verkfræðinnar, innan 
eðlisfræðinnar, í tölvugrafík, fjármálum og í tengslum við gervigreind.

Línuleg jöfnuhneppi
-------------------

Sýnidæmi: línulegt jöfnuhneppi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi
  
  Leysið jöfuhneppið:  

    .. math:: \begin{aligned}
        x + 2y &= -3 \\
        x - y &= 6 
        \end{aligned}

.. admonition:: Lausn
  :class: daemi, dropdown
  
  Drögum neðri jöfnuna frá þeirri efri og fáum :math:`3y=-9` sem gefur
  :math:`y=-3`. Stingum inn í neðri jöfnuna og gefur :math:`x=3`. Þar 
  með er :math:`(x,y)=(3,-3)` lausn jöfnuhneppisins.

Skoðum jöfnuhneppið úr sýnidæminu að ofan. Þar sem jöfnuhneppið hefur lausn segjum við að
jöfnuhneppið sé **samkvæmt** (e. consistent). Þar sem jöfnuhneppið hefur aðeins eina lausn 
segjum við að lausnin sé **ótvírætt ákvörðuð** (e. unique). Við segjum að **stuðlar** 
(e. coefficients) jöfnuhneppisins eru: 

    .. math:: \begin{bmatrix}
        1 & 2  \\
        1 & -1 \\
        \end{bmatrix}

Skoðum annað jöfnuhneppi

Sýnidæmi: línulegt jöfnuhneppi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi

  Leysið jöfnuhneppið

  .. math:: \begin{align*}
    x-2y&=5 \\
    -2x+4y&= 6 
    \end{align*}

.. admonition:: Lausn
  :class: daemi, dropdown
  
   Margföldum efri jöfnuna með 2.
   
  .. math:: \begin{align*}
     2x-4y&=10 \\
     -2x+4y&= 6 
     \end{align*}

  Leggjum saman jöfnurnar og fáum :math:`0=16` svo jöfnuhneppið 
  hefur enga lausn. Við segjum því að jöfnuhneppið sé ósamkvæmt (e. inconsistent).

Sýnidæmi: línulegt jöfnuhneppi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi

  Leysið jöfnuhneppið

  .. math:: \begin{align*}
        x+y&=2 \\
        2x+2y&= 4 
        \end{align*}

.. admonition:: Lausn
  :class: daemi, dropdown

   Deilum í neðri jöfnuna með 2.
   
   .. math:: \begin{align*}
      x+y&=2 \\
      x+y&=2 
      \end{align*}

   Ef við drögum efri jöfnuna frá neðri jöfnunni fæst:

    .. math:: \begin{align*}
       x+y&=2 \\
       0 &= 0
       \end{align*}
    
   Lína :math:`0=0` kallast núllína. Athugum þá hvort jafnan 
   :math:`x+y=2` einhveja lausn. Já, :math:`(x,y)=(1,1)` og 
   :math:`(x,y)=(2,0)` eru dæmi um lausnir. Jöfnuhneppið er 
   samkvæmt en lausnin er ekki ótvírætt ákvörðuð. Ef við veljum 
   til dæmis :math:`y=t` fæst :math:`x=2-t`. Svo allar tvenndir af
   gerð :math:`(x,y)=(2-t,t)` eru lausnir jöfnuhneppisins. 



Skilgreining: Lausnamengi
^^^^^^^^^^^^^^^^^^^^^^^^^
.. admonition:: Skilgreining
    :class: skilgreining

        Mengi allra launsa jöfnuhneppis kallast **lausnamengi** þess (e. solution set).

Tökum saman sýnidæmin í töflu:

Ath. setja inn töflu með myndum!!!

.. admonition:: Athugasemd 
    :class: athugasemd

    Línulegt jöfnuhneppi með rauntölulausn getur haft:

        **(a)** Enga lausn

        **(b)** Nákvæmlega eina lausn

        **(c)** óendanlega margar lausnir


Jafngild jöfnuhneppi
--------------------

Skoðum jöfnuhneppið 

.. math:: \begin{aligned} 
    x-y &= 6 \\
    x+2y &= -3
    \end{aligned}

Þetta er mjög svipað jöfnuhneppinu

.. math:: \begin{aligned} 
    x+2y &= -3 \\
    x-y &= 6
    \end{aligned}

við getum búist við að lausnirnar séu þær sömu í báðum tilfellum.


Skilgreining: Jafngild
^^^^^^^^^^^^^^^^^^^^^^
.. admonition:: Skilgreining
    :class: skilgreining

    Tvö línuleg jöfnuhneppi kallast **jafngild** (e. equivalent) ef þau hafa sömu lausnir.

Einfaldar línuaðgerðir
----------------------      

Eftirfarandi aðgerðir kallast **einfaldar línuaðgerðir** (e. elementary row operations) og 
þeim má beita á jöfnur  í línulegum jöfnuhneppum (eða línur í fylkjum):

.. admonition:: Setning
    :class: setning

    **(1)** að skipta út línu :math:`R_i` fyrir :math:`R_i+cR_j` þar sem :math:`R_j` er önnur lína og :math:`c` er fasti.

    **(2)** að víxla á línum :math:`R_i` og :math:`R_j`.

    **(3)** að margfalda línu :math:`R_i` með fasta :math:`c\neq 0`

Þessar aðgerðir eru andhverfanlegar og breyta ekki lausnamengi jöfnuhneppsins.

Skilgreining: línujafngild
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. admonition:: Skilgreining
    :class: skilgreining

    Tvö jöfnuhneppi (eða fylki) eru eru **línujafngild** (e. row equivalent) ef öðru má breyta í hitt
    með einföldum línuaðgerðum.

.. admonition:: Dæmi
  :class: daemi

  Leysum jöfnuhneppið

  .. math:: 
    \begin{aligned}
     x_1 -3x_2 + 4x_3 =-4\\
     3x_1-7x_2+7x_3 =-8\\
    -4x_1+6x_2+2x_3=4
    \end{aligned}
    

.. admonition:: Lausn
  :class: daemi, dropdown
  
   Skrifum þetta á fylkjaformi.
   
  .. math:: \begin{aligned}\begin{bmatrix}
    1 & -3 & 4 & -4\\
    3 & -7 & 7 & -8\\
    -4 & 6 & 2 & 4
    \end{bmatrix} 
    \stackrel{\begin{matrix}R_2-3R_1\\R_3+4R_1\end{matrix}}
    {\sim}
    \begin{bmatrix}
    1 & -3 & 4 &-4\\
    0 & 2 & -5 & 4 \\
    0 & -6 & 18 & -12
    \end{bmatrix}
    \stackrel{\displaystyle\frac{R_3}{-6}}{\sim}
    \newline
    \begin{bmatrix}
    1 & -3 & 4 &-4\\
    0 & 2 & -5 & 4 \\
    0 & 1 & -3 & 2
    \end{bmatrix}  
    \stackrel{\displaystyle R_2\leftrightarrow R_3}{\sim}
    \begin{bmatrix}
    1 & -3 & 4 &-4\\
    0 & 1 & -3 & 2 \\
    0 & 2 & -5 & 4
    \end{bmatrix}
    \stackrel{\begin{matrix}
    R_1+3R_2\\ R_3-2R_2
    \end{matrix}}{\sim}
    \newline
    \begin{bmatrix}
    1 & 0 & -5 & 2\\
    0 & 1 & -3 & 2 \\
    0 & 0 & 1 & 0
    \end{bmatrix}
    \stackrel{\begin{matrix}
    R_1+5R_3\\ R_2+3R_3
    \end{matrix}}{\sim}
    \begin{bmatrix}
    1 & 0 & 0 & 2\\
    0 & 1 & 0 & 2 \\
    0 & 0 & 1 & 0
    \end{bmatrix}
    \end{aligned}

  Svo við fáum

  .. math:: \begin{aligned}
    x_1&&&=2\\
    &x_2&&=2\\
    &&x_3&=0
    \end{aligned}
  
  og línulega jöfnuhneppið hefur því eina lausn :math:`(x_1,x_2,x_3)=(2,2,0)`. 

Af hverju eru línulegar aðgerðir andhverfalegar?

    **(1)** Hvernig má snúa aðgerðinni við :math:`R_1\leftrightarrow R_2`?

    **Svar:** :math:`R_2\leftrightarrow R_1` 

    **(2)** Hvernig má snúa aðgerðinni við :math:`R_1\rightarrow \frac{R_2}{2}`?

    **Svar:** :math:`R_2\rightarrow R_1 \cdot 2` 

    **(3)** Hvernig má snúa aðgerðinni við :math:`R_1\rightarrow R_1-2\cdot R_2`?

            .. math:: \begin{bmatrix}
                4x+4y=3\\
                2x-y=4
                \end{bmatrix}\overset{R_1\rightarrow R_1 -2R_2}{\rightarrow}
                \begin{bmatrix}
                & 6y=-5\\
                2x & -y=4
                \end{bmatrix}
                \overset{?}{\rightarrow}
                \begin{bmatrix}
                4y+4y=3\\
                2x-y=4
                \end{bmatrix}

    **Svar:** :math:`R_1\rightarrow R_1 +2R_2` 

Jafngild vs. línujafngild

Ef jöfnuhneppi eru línujafngild þá hafa þau sömu lausnir. Til eru dæmi 
um jöfnuhneppi sem hafa sömu lausnir en eru ekki línujafngild. 

Línulegu jöfnuhneppin 

.. math::\begin{bmatrix} 
    x+y&=0\\ 
    0&=1
    \end{bmatrix} 
    \text{ og }
    \begin{bmatrix} 
    x-y&=0\\ 
    0&=1
    \end{bmatrix}

hafa sömu (engar) launsir en eru ekki línujafngild.


Stærð fylkis
------------

Látum 

.. math:: \begin{bmatrix}
    a_{11} &\dots &a_{1n}\\
    \vdots&&\vdots\\
    a_{m1}&\dots &a_{mn}\\  
    \end{bmatrix}

vera fylki. Við segjum að :math:`A` sé :math:`{m\times n}` fylki.
Jafnframt er :math:`m\times n` kallað **stærð fylkisins** :math:`A`.

Skilgreining: Stuðlafylki og aukið fylki
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

        Látum 

        .. math:: \begin{align*}
            a_{11}x_{1}+\dots+a_{1n}x_n=b_1\\
            \vdots&&\vdots\\
            a_{m1}x_{1}+\dots+a_{mn}x_n=b_m\\    
            \end{align*}
        
        vera línulegt jöfnuhneppi. Við köllum fylkin

        .. math:: \begin{bmatrix}
            a_{11} &\dots &a_{1n}\\
            \vdots&&\vdots\\
            a_{m1}&\dots &a_{mn}\\  
            \end{bmatrix}
            \text{ og }
            \begin{bmatrix}
            a_{11} &\dots &a_{1n} &b_1\\
            \vdots&&\vdots&\vdots\\
            a_{m1}&\dots &a_{mn} &b_m\\  
            \end{bmatrix}
        
        **Stuðlafylki** (e. coefficient matrix) og **aukið fylki** (e. augmented matrix) jöfnuhneppisins.

Efri stallagerð
---------------

**Línur** (e. rows) liggja lárétt og **dálkar** (e. columns) liggja lóðrétt.

Setja inn mynd!

**Núllína** (e. zero row) er lína þar sem allir stuðlarnir eru núll.

**Forustustuðull** (e. leading coeffcient) er fyrsti stuðull í hverrri línu sem er ekki núll.

Setja inn mynd!

Skoðum jöfnuhneppi

.. math:: \begin{array}{cccc}
        3x_1 &+ 7x_2 &- 2x_3 &= 9 \\
             & -5x_2 &+ 4x_3 &= 2 \\
             &        & 6x_3 &=-3 \\
      \end{array}

sjáum strax að jöfnuhneppið hefur lausn. 

.. math:: \begin{bmatrix}
    3 & 7 & -2 & 9 \\
    0 & -5 & 4 & 2 \\
    0 & 0 & 6 & -3 
    \end{bmatrix}

Aukna fylkið fyrir jöfnuhneppið er dæmi um fylki af *efri stallagerð* (e. echelon form).  

Skilgreining: Efri stallagerð
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. admonition:: Skilgreining
    :class: skilgreining

    Fylki er sagt vera af **efri stallagerð** (e. echelon form) ef það uppfyllir
    eftirfarandi skilyrði.

        **1.** Núllínur liggja fyrir neðan aðrar línur.

        **2.** Forustustuðull hverrar línu er hægra megin við forustustuðul línunnar fyrir ofan.

        **3.** Allir stuðlar fyrir neðan forustustuðul eru núll.
    
    Öllum fylkjum má breyta í fylki af efri stallagerð með einfölduum línuaðgerðum.

Sýnidæmi: Efri stallagerð
^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi
  
  Breytum eftirfarandi :math:`{3\times 4}` fylki í fylki af efri stallagerð:

  .. math:: \begin{eqnarray*}
    \begin{bmatrix}
    1 & 2 & 3 & 4 \\
    5 & 6 & 7 & 8 \\
    9 & 10 & 11 & 12
    \end{bmatrix} 
    &\sim 
    &\begin{bmatrix}
    1 & 2 & 3 & 4 \\
    0 & -4 & -8 & -12 \\
    0 & -8 & -16 & -24
    \end{bmatrix}
    \begin{matrix}\\
    R_2 - 5R_1 \\
    R_3 - 9R_1
    \end{matrix}\\  &\sim
    &\begin{bmatrix}
    1 & 2 & 3 & 4 \\
    0 & -4 & -8 & -12 \\
    0 & 0 & 0 & 0
    \end{bmatrix}\begin{matrix}
    \\
    \\R_3 - 2R_2
    \end{matrix}
    \end{eqnarray*}

  Er þetta fylki af neðri stallagerð?

  **1.** Núlllínur eru neðast. OK

  **2.** Forustustuðull hverrar línu er hægra megin við forustustuðul línunnar fyrir ofan. OK

  **3.** Allir stuðlar fyrir neðan forustustuðul eru núll. OK

Gauss-eyðing
------------

Gauess-eyðing er reiknirit sem umbreytir fylki í fylki af efri stallagerð.

    **1.** Finnum dálkinn lengst til vinstri er ekki núll. Köllum þennan dálk „fyrsta vendidálk".

    **2.** Víxlum, ef þarf, á línum svo að efsta stak fyrsta vendidálks (vendistak) sé ekki núll.

    **3.** Núllum út stökin fyrir neðan vendistakið með því að draga margfeldi efstu línu frá línum fyrir neðan.

    **4.** Lítum nú framhjá efstu línu í fylkinu og endurtökum skref 1-4 á línurnar fyrir neðan.

.. admonition:: Athugasemd
  :class: athugasemd

  Það er ekki bannað að deila/margfalda til að vendistuðullinn verði 1. Það er ekki nauðsynlegt en það má ef það 
  einfaldar útreikingana. Sama gildi um það að víxla á línum til að fá þægilegri tölur til að vinna með.

.. admonition:: Dæmi
  :class: daemi

  Notið Gauss-eyðingu til að koma fylkinu yfir á efri stallagerð

  .. math:: 
    \begin{bmatrix}
    0 & 4 & 1 \\
    -1 & 3 & 2 \\
    5 & 6 & -3
    \end{bmatrix}

.. admonition:: Lausn
  :class: daemi, dropdown

  Beitum Gauss-eyðingu til að umbreyta fylkinu í fylki af efri stallagerð.

  .. math:: \begin{eqnarray*}
    \begin{bmatrix}
    0 & 4 & 1 \\
    -1 & 3 & 2 \\
    5 & 6 & -3
    \end{bmatrix}
    &\sim 
    &\begin{bmatrix}
    -1 & 3 & 2 \\
    0 & 4 & 1 \\
    5 & 6 & -3
    \end{bmatrix}
    \begin{matrix}
    \\
    R_1 \leftrightarrow R_2 \\ 
    \end{matrix}\\
    &\sim 
    &\begin{bmatrix}
    -1 & 3 & 2 \\
    0 & 4 & 1 \\
    0 & 21 & 7
    \end{bmatrix}\begin{matrix}
    \\
    \\
    R_3 + 5R_1
    \end{matrix}\\
    &\sim  
    &\begin{bmatrix}
    -1 & 3 & 2 \\
    0 & 4 & 1 \\
    0 & 0 & \frac{7}{4}
    \end{bmatrix}\begin{matrix}
    \\
    \\
    -R_3-\frac{21}{4}R_2
    \end{matrix}
    \end{eqnarray*}


Skilgreining: Rudd efri stallagerð
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    Fylki er sagt vera af **ruddri efri stallagerð**  (e. reduced echeolon form) ef það er af efri 
    stallagerð og uppfyllir að auki eftirfarandi skilyrði:
    
    **1.** Forustustuðlar eru allir 1.

    **2.** Allir stuðlar fyrir ofan forustustuðul eru núll.


Sýnidæmi: Rudd efri stallagerð
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi

  .. math:: \begin{align*}
    \begin{bmatrix}
      1 & 0 \\
      0 & 1 \\
    \end{bmatrix}
    &
    \begin{bmatrix}
      1 & 4 & 0 \\
      0 & 0 & 1 \\
      0 & 0 & 0 \\
    \end{bmatrix}
    &
    \begin{bmatrix}
      1 & 0 & 3 & 0 \\
      0 & 1 & 4 & 0 \\
      0 & 0 & 0 & 1 \\
    \end{bmatrix}
    &
    \begin{bmatrix}
      1 & 0 & 2 & 0 & 1 \\
      0 & 1 & 3 & 0 & 2 \\
      0 & 0 & 0 & 1 & 3 \\
    \end{bmatrix}
    &
    \\
    \begin{bmatrix}
      1 & 0 \\
      0 & 1 \\
    \end{bmatrix}
    &
    \begin{bmatrix}
      1 & * & 0 \\
      0 & 0 & 1 \\
      0 & 0 & 0 \\
    \end{bmatrix}
    &
    \begin{bmatrix}
      1 & 0 & * & 0 \\
      0 & 1 & * & 0 \\
      0 & 0 & 0 & 1 \\
    \end{bmatrix}
    &
    \begin{bmatrix}
      1 & 0 & * & 0 & * \\
      0 & 1 & * & 0 & * \\
      0 & 0 & 0 & 1 & * \\
    \end{bmatrix}
    \end{align*}

Við köllum forustustuðul í fylki af ruddri efri stallagerð **vendistuðul**. 
Við köllum þá dálka **vendidálka** sem innhalda vendistuðla.

Við finnum rudda efri stallagerð með sama algóriþma og við finnum efri stallagerð. 
Nema að til viðbótar þá gerum við eftirfarandi:

    **1.** Skölum forustustuðla þar sem við á til að þeir verði 1.
 
    **2.** Eyðum út stuðlum fyrir ofan forustustuðla.

Sýnidæmi: Rudd efri stallagerð
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi

  Beitið reikniritinu til að koma fylkinu yfir á rudda efri stallagerð.

  .. math:: \begin{bmatrix}
    0 & 4 & 1 \\
    -1 & 3 & 2 \\
    5 & 6 & -3
    \end{bmatrix}

.. admonition:: Lausn
  :class: daemi, dropdown

  .. math:: \begin{eqnarray*}
    \begin{bmatrix}
    0 & 4 & 1 \\
    -1 & 3 & 2 \\
    5 & 6 & -3
    \end{bmatrix}
    &\sim
    \begin{bmatrix}
    -1 & 3 & 2 \\
    0 & 4 & 1 \\
    0 & 0 & \frac{7}{4}
    \end{bmatrix} \\
    &\sim
    \begin{bmatrix}
    1 & -3 & -2 \\
    0 & 1 & \frac{1}{4} \\
    0 & 0 & 1
    \end{bmatrix}\\ 
    &\sim
    \begin{bmatrix}
    1 & -3 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
    \end{bmatrix}
    \\&\sim\begin{bmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
    \end{bmatrix}
    \end{eqnarray*}
  
  og við fáum fylki af ruddri efri stallagerð.


Setning
^^^^^^^

.. admonition:: Setning
  :class: setning

  Gefið er fylki :math:`A`. Fylkinu :math:`A` má með einföldum línuaðgerðum 
  umbreyta í eitt og aðeins eitt fylki af ruddri efri stallagerð. Með öðrum 
  orðum er rudd efri stallagerð fylkis er ótvírætt ákvörðuð. 

.. admonition:: Dæmi
  :class: daemi

  Leysið línulega jöfnuhneppið

  .. math:: \begin{align*}
    x_1+2x_2+3x_3=4\\
    5x_1+6x_2+7x_3=8\\    
    9x_1+10x_2+11x_3=12
    \end{align*}

.. admonition:: Lausn
  :class: daemi, dropdown

  Skoðum línulega jöfnuhneppið
  
  .. math:: \begin{align*}
    x_1+2x_2+3x_3=4\\
    5x_1+6x_2+7x_3=8\\    
    9x_1+10x_2+11x_3=12
    \end{align*} 
  
  Skv. Sýnidæmi að ofan má umbreyta aukna fylki þess í
 
  .. math:: \begin{bmatrix}
    1 & 0 & -1 & -2 \\
    0 & 1 & 2 & 3 \\
    0 & 0 & 0 & 0
    \end{bmatrix} 
  
  sem jafngildir jöfnuhneppinu

  .. math::\begin{align*}
    x_1&-x_3=-2\\
    x_2&+2x_3=3
    \end{align*}

  Fáum að

  .. math:: \begin{align*}
    x_1&-x_3=-2\\
    x_2&+2x_3=3
    \end{align*}

  jafngildir

  .. math:: \begin{align*}
    x_1&=x_3-2\\
    x_2&=-2x_3+3
    \end{align*}
  
  svo

  .. math:: \begin{align*}
    \begin{pmatrix}
    x_1\\
    x_2\\
    x_3
    \end{pmatrix}=
    \begin{pmatrix}
    x_3-2\\
    -2x_3+3\\
    x_3
    \end{pmatrix}
    \end{align*}

  þar sem :math:`x_3` er **frjáls breyta** (e. free variable) .

  Jöfnuhneppið er samkvæmt en lausnin ekki ótvírætt ákvörðuð.
  Breyturnar :math:`x_1`, :math:`x_2` eru hér kallaðar **háðar breytur** (e. basic variable). 


Texti um að ryðja eða að ryðja ekki? skoða betur!

.. admonition:: Athugasemd
  :class: athugasemd

  Ef við umbreytum aukna fylki jöfnuhneppis yfir á (rudda) efri stallagerð getur eftirfarandi gerst:

  **1.** Dálkurinn lengst til hægri er vendidálkur. Í þeim tilfellum hefur jöfnuhneppið enga lausn. **Dæmi:**

  .. math:: \begin{bmatrix}
    1 & * & 0 \\
    0 & 0 & 1 \\
    \end{bmatrix}

 **2.** Allir dálkar nema dálkurinn lengst til hægri eru vendidálkar. Í þeim tilfellum hefur jöfnuhneppið nákvæmlega eina lausn. **Dæmi:**
    
 .. math:: \begin{bmatrix}
    1 & 0 & * \\
    0 & 1 & * \\
    \end{bmatrix}

 **3.** Dálkurinn lengst til hægri er ekki vendidálkur auk minnst eins annars til viðbótar. 
 Í þeim tilfellum hefur jöfnuhneppið óendanlega margar lausnir. **Dæmi:**
    
 .. math:: \begin{bmatrix}
    1 & 0 & * & * \\
    0 & 1 & * & * \\    
    \end{bmatrix}

.. admonition:: Setning
  :class: setning

  Línulegt jöfnuhneppi er samkvæmt þá og því aðeins að dálkurinn lengst til hægri í efri 
  stallagerð aukna fylkisins sé ekki vendidálkur, þ.e. er efri stallagerð aukna fylkisins 
  hefur enga línu af gerð :math:`[0\ \dots \ 0 \ b]` þar sem :math:`b\neq 0`. 
  Ef jöfnuhneppið er samkvæmt er lausnin ótvírætt ákvörðuð þá og því aðeins að allir 
  dálkar fylkisins aðrir en sá sem er lengst til hægri eru vendidálkar. Ef lausnin er 
  ekki ótvírætt ákvörðuð eru lausnirnar óendanlega margar.

Vigrar
------


Línuleg samantekt
-----------------


Línuleg spönn
-------------