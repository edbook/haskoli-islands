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


Sýnidæmi: Frjálsar og háðar breytur
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Skilgrining: Vigur
^^^^^^^^^^^^^^^^^^

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
  
Við feitletrum gajrnan breytur sem tákna vigra til að aðgreina þá frá rauntalnabreytum.
:math:`\textbf{u}, \textbf{v}, \textbf{v}_1, \textbf{v}_2, \textbf{b},` Önnur leið er að nota 
örvar: :math:`\vec{u}, \vec{v}, \vec{v}_1, \vec{v}_2, \vec{b}` eða strik:
:math:`\bar{u}, \bar{v}, \bar{v}_1, \bar{v}_2, \bar{b}`. 

Einnig má skrifa dálkvigra svona til að spara pláss: 

.. math:: \begin{bmatrix}
    1 & 2 & 3 & 4 & 5
    \end{bmatrix}^T 
    \text{ eða } 
    (1,2,3,4,5) 
    \text{ í staðinn fyrir }
    \begin{bmatrix}
    1 \\ 2 \\ 3 \\ 4 \\ 5
    \end{bmatrix}.

.. admonition:: Athugasemd
    :class: athugasemd

    Tveir vigrar eru jafnir ef þeir eru að sömu vídd og öll hnit þeirra eru þau sömu.

Sýnidæmi: Jafnir vigrar
^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    .. math:: \begin{bmatrix}
        3 \\ 4 
        \end{bmatrix}= \begin{bmatrix}
        3 \\ 4 
        \end{bmatrix}, \quad
        \begin{bmatrix}
        3 \\ 4 
        \end{bmatrix}\neq \begin{bmatrix}
        4 \\ 3 
        \end{bmatrix}, \quad \begin{bmatrix}
        1 \\ 1
        \end{bmatrix}\neq \begin{bmatrix}
        1
        \end{bmatrix} 

Samlagning vigra 
^^^^^^^^^^^^^^^^

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

Stikamargöfldun vigra 
^^^^^^^^^^^^^^^^^^^^^

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

Sýnidæmi: Stikamargföldun vigra
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    .. math:: 2\cdot\begin{bmatrix}
        -1\\3
        \end{bmatrix}
        =
        \begin{bmatrix}
        2\cdot(-1)\\2\cdot 3
        \end{bmatrix}=
        \begin{bmatrix}
        -2\\6
        \end{bmatrix}

Sýnidæmi: Stikamargföldun vigra, frh.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Ef við margföldum vigur með 1 fáum við alltaf sama vigurinn aftur:

    .. math:: 1\cdot\begin{bmatrix}
        3\\0
        \end{bmatrix}
        =
        \begin{bmatrix}
        1\cdot 3\\1\cdot 0
        \end{bmatrix}=
        \begin{bmatrix}
        3\\ 0
        \end{bmatrix}

    EF við margöfldum með 0 fáum við núllvigruinn:

    .. math:: 0\cdot\begin{bmatrix}
        2\\-7
        \end{bmatrix}
        =
        \begin{bmatrix}
        0\cdot 2\\0\cdot (-7)
        \end{bmatrix}=
        \begin{bmatrix}
        0\\ 0
        \end{bmatrix}.

Reiknireglur fyrir vigra
^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Ef **u**, **v**, **w** eru vigrar í :math:`\mathbb{R}^n` og  *c* og  *d* eru
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
    Við getum heldur ekki deilt einum við vigri upp í annan. Stærðirnar 
    :math:`\textbf{v}_1\textbf{v}_2` og :math:`\frac{\textbf{v}_1}{\textbf{v}_2}`
    eru því almennt ekki skilgreindar.


Myndræn framsetning vigra
-------------------------

Sýnidæmi: Myndræn framsetning vigra í :math:`\mathbb{R}^2`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Hér má sjá vigrana :math:`\textbf{v} = \begin{bmatrix}1\\2\end{bmatrix}` og :math:`\textbf{u} = \begin{bmatrix}-2\\1\end{bmatrix}`

    SETJA INN MYND!!!!

Sýnidæmi: Samlagning vigra í :math:`\mathbb{R}^2`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Til að leggja saman vigra **v** og **u** í :math:`\mathbb{R}^2` leggjum við 
    einfaldlega upphafspunkt **u** ofan endapunkt **v** og drögum ör á milli (0,0)
    og hins nýja endapunkt.

    Látum :math:`\textbf{v} = \begin{bmatrix}1\\2\end{bmatrix} \text{ og }\textbf{u} = \begin{bmatrix}-2\\1\end{bmatrix}`
    leggjum saman og fáum :math:`\textbf{u+v} = \begin{bmatrix}-1\\3\end{bmatrix}`.

    SETJA INN MYND!!!!

Sýnidæmi: Margföldun vigra í :math:`\mathbb{R}^2`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Þegar við margföldum vigurinn **v** með rauntölunni :math:`c` fáum við
    nýjan vigur :math:`c\textbf{v}` í sömu (eða gagnstæða) stefnu. 

    sjáum á mynd vigurinn :math:`\textbf{v} = \begin{bmatrix}1\\2\end{bmatrix}`
    ásamt vigrunum :math:`2\textbf{v} = \begin{bmatrix}2\\4\end{bmatrix} \text{ og } (-1) \textbf{v} = \begin{bmatrix}-1\\-2\end{bmatrix}`.
    Vigurinn :math:`(-1) \textbf{v}` er fenginn með því að snúa vigrinum **v** um 180 gráður.

    SETJA INN MYND!!!!!!

Sýnidæmi: Frádráttur vigra í :math:`\mathbb{R}^2`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Ef við höfum 

    .. math:: \textbf{v} = \begin{bmatrix}1\\2\end{bmatrix} \text{ og }
        \textbf{u} = \begin{bmatrix}-2\\1\end{bmatrix}
    
    Þá fáum við :math:`\textbf{v}-\textbf{u} = \textbf{v}+(-\textbf{u})` sem gefur 

    .. math:: \textbf{v}-\textbf{u} = \begin{bmatrix}1\\2\end{bmatrix}-  \begin{bmatrix}-2\\1\end{bmatrix} = \begin{bmatrix}3\\1\end{bmatrix}.
    
    SETJA INN MYND

    Önnur leið til að hugsa um :math:`\textbf{v}-\textbf{u}` er að skoða strikið á milli **v** og **u**. 
    Vigurinn :math:`\textbf{v}-\textbf{u}` þarf að vera þannig að ef við bætum honum
    við **u** fáum við **v**. 

    .. math:: \textbf{u}+(\textbf{v}-\textbf{u})=\textbf{v}


Línuleg samantekt
-----------------

Skilgreining: Línuleg samantekt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`\textbf{v}_1, \textbf{v}_2, \dots, \textbf{v}_p` vera vigra í :math:`\mathbb{R}^n` og :math:`c_1, c_2, \dots, c_p` vera rauntölur. 
    Við segjum að vigurinn 

    .. math:: \textbf{y}=c_1\textbf{v}_1 +c_2\textbf{v}_2+ \dots+ c_p\textbf{v}_p
    
    sé **línuleg samantekt** af vigrunum :math:`\textbf{v}_1, \textbf{v}_2, \dots, \textbf{v}_p` með **vogstuðla** :math:`c_1, c_2, \dots, c_p`.

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
    
    Svo vigurinn **y** er línuleg samanteky af :math:`\textbf{v}_1` og :math:`\textbf{v}_2` 
    með vogstuðlana 3 og 1.

.. admonition:: Athugasemd
    :class: athugasemd

    **1.** Vigur **v** er línuleg samantekt af sjálfum sér því við getum skrifað :math:`\textbf{v}=1 \cdot \textbf{v}`.

    **2.** Núllvigurinn **0** er línuleg samantekt af hvaða vigrum sem er því við 
           getum skrifað 

    .. math:: \textbf{0}=0 \cdot \textbf{v}_1+0 \cdot \textbf{v}_2+\dots+0 \cdot \textbf{v}_p

    **3.** Ef **m** er meðaltal vigranna :math:`\textbf{v}_1, \textbf{v}_2, \dots, \textbf{v}_p` þá er **m**
           línuleg samantekt af :math:`\textbf{v}_1, \textbf{v}_2, \dots, \textbf{v}_p` því

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
        \end{bmatrix}
    
    Er vigurinn **y** línuleg samantekt af :math:`\textbf{v}_1` og :math:`\textbf{v}_2`.

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
        \end{bmatrix}
    
    sem jafngildir jöfnuhneppinu

    .. math:: \begin{eqnarray*}
        x_1 &=&3\\
        x_1 +2x_2&=&7\\
        x_1+3x_2&=&9
        \end{eqnarray*}
    
    Skrifum út aukna fylkið og leysum

    .. math:: \begin{align*}
        \begin{bmatrix}
            1 & 0 & 3\\
            1 & 2 & 7\\
            1 & 3 & 9
        \end{bmatrix}
        \sim
        \begin{bmatrix}
            1 & 0 & 3\\
            0 & 2 & 4\\
            0 & 3 & 6
        \end{bmatrix} \sim
        \begin{bmatrix}
            1 & 0 & 3\\
            0 & 1 & 2\\
            0 & 1 & 2
        \end{bmatrix} 
        \sim
        \begin{bmatrix}
            1 & 0 & 3\\
            0 & 1 & 2\\
            0 & 0 & 0
        \end{bmatrix}
        \end{align*}

    er jafngild

    .. math::\begin{eqnarray*}
        x_1=3\\
        x_2=2\\
        \end{eqnarray*}
    
    svo 

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
    
    og **y** er línuleg samantekt af :math:`\textbf{v}_1` og :math:`\textbf{v}_2`.

Sýnidæmi: Línulegar samantektir
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Er vigurinn **y** línuleg samantekt af :math:`\textbf{v}_1` og :math:`\textbf{v}_2` þegar

    .. math::  \textbf{v}_1=
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
        5\\10\\5\\
        \end{bmatrix}?

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
        5\\10\\5\\
        \end{bmatrix}

    Skrifum þetta sem aukið fylki
        
    .. math:: \begin{align*}
        \begin{bmatrix}
        1 & 0 & 5\\
        1 & 2 & 10\\
        1 & 3 & 5
        \end{bmatrix}
        \sim
        \begin{bmatrix}
        1 & 0 & 5\\
        0 & 2 & 5\\
        0 & 3 & 0
        \end{bmatrix} \sim
        \begin{bmatrix}
        1 & 0 & 3\\
        0 & 1 & 2\\
        0 & 1 & 0
        \end{bmatrix} 
        \sim
        \begin{bmatrix}
        1 & 0 & 3\\
        0 & 1 & 2\\
        0 & 0 & -2
        \end{bmatrix}
        \end{align*}

    Aukna fylkið hefur vendidálk lengst til hægri svo jafnan hefur enga lausn.
    Vigurinn **y** er ekki línuleg samantekt af :math:`\textbf{v}_1` og :math:`\textbf{v}_2`.

Línuleg spönn
-------------

Skilgreining: Línulegar spönn
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    Ef :math:`\textbf{v}_1,\dots,\textbf{v}_p` eru vigrar í :math:`\mathbb{R}^n` þá skilgreinum við :math:`\text{span}\{\textbf{v}_1,\dots,\textbf{v}_p\}` sem mengi allra vigra í 
    :math:`\mathbb{R}^n` sem eru línuleg samantekt af :math:`\textbf{v}_1,\dots,\textbf{v}_p`. Með öðrum orðum er :math:`\text{span}\{\textbf{v}_1,\dots,\textbf{v}_p\}` mengi 
    allra vigra sem skrifa má á forminu

    .. math:: c_1\textbf{v}_1+\dots+c_p\textbf{v}_p

    þar sem :math:`c_1, \dots, c_p` eru einhverjar rauntölur.
    Við köllum mengið :math:`\text{span}\{\textbf{v}_1,\dots,\textbf{v}_p\}` **línulega spönn** mengisins :math:`\{\textbf{v}_1,\dots,\textbf{v}_p\}`.

Línulegar spönn í :math:`\mathbb{R}^2`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SETJA INN MYND !!!!

Myndin sýnir vigrana :math:`\textbf{v}_1` og :math:`\textbf{v}_2`.
Bleika svæðið (allt :math:`mathbb{R}^2` rúmið) er línuleg spönn þessara vigra.

SETJA INN MYND !!!!

Á mynd má sjá vigurinn **v**. Línuleg spönn þessa vigurs eru allir vigrar með endapunkt á línunni
sem er framhald vigursins **v**, í báðar áttir.

Línulegar spönn í :math:`\mathbb{R}^3`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Látum :math:`\textbf{v}_1` og :math:`\textbf{v}_2` vera tvo vigra í :math:`\mathbb{R}^3`. Í þessu dæmi myndar
spönn þeirra sléttu sem fer í gegnum upphafspunkt hnitakerfisins.

SETJA INN MYND !!!!

Línuleg spönn í :math:`\mathbb{R}^3` getur líka verið: bara núllpunkturinn, 
lína í gegnum núllpunkt eða allt :math:`\mathbb{R}^3` rúmið.

Margfeldi fylkis og vigurs 
--------------------------

Skilgreining: Fylkjajafnan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`A` vera :math:`m\times n` fylki þar sem :math:`\textbf{a}_1, \dots, \textbf{a}_n` eru dálkar þess. 
    Látum **x** vera dálkvigur í :math:`\mathbb{R}^n`. Við skilgreinum margfeldið :math:`A \textbf{x}` með eftirfarandi hætti:

    .. math:: A\textbf{x} = \begin{bmatrix}\textbf{a}_1 \dots \textbf{a}_n\end{bmatrix}
        \begin{bmatrix}
        x_1\\\dots\\x_n
        \end{bmatrix}
        =x_1\textbf{a}_1 +\dots x_n\textbf{a}_n.

Til að margföldunin :math:`A\textbf{x}` sé framkvæmaleg þar fjöldi dálka :math:`A` vera jafn fjöldi lína **x**.

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
        \end{bmatrix}\right\}n\text{ línur}

Margfeldið er þá

.. math:: \begin{bmatrix}
        a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n \\
        a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n \\
        \vdots    \\
        a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n
        \end{bmatrix}\quad \begin{bmatrix}
        \rightarrow\\\\
        \end{bmatrix}[\downarrow]

Sýnidæmi: Margfeldi fylkis og vigurs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Skoðum margfeldi fylkisins :math:`A` og vigursins **x**.

    .. math:: A = \begin{bmatrix}
        2 & 3 & -1 \\
        -1 & 4 & 6
        \end{bmatrix}
        \quad \text{, } \quad
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

.. admonition:: Launs
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
    :math:`I \textbf{x}=\textbf{x}` gildir fyrir alla vigra **x**.


Fylkjajafnan
------------

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki með dálkvigrum :math:`\textbf{a}_1,\dots,\textbf{a}_n` og **b** vera dálkvigur í :math:`\mathbb{R}^n`. Táknum :math:`\textbf{x} = [x_1,\dots x_n]^T`. 
    Fylkjajafnan

    .. math:: A\textbf{x} =  \textbf{b}

    hefur sömu lausnir og jafnan

    .. math:: x_1\textbf{a}_1 +\dots + x_n \textbf{a}_n = \textbf{b}

    sem hefur sömu lausnir og fást með því að leysa jöfnhneppið sem svarar til aukna fylkisins

    .. math:: \begin{bmatrix}
        \textbf{a}_1 &\dots &\textbf{a}_n &\textbf b 
        \end{bmatrix}

.. admonition:: Athugasemd
    :class: athugasemd

    Fylkjajafnan :math:`A\textbf{x} = \textbf{b}` hefur lausn þá og því aðeins að 
    :math:`\textbf{b}` er línuleg samantekt af dálkum fylkis :math:`A`.

Sýnidæmi: Fylkjajafnan
^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Fyrir hvaða :math:`b_1` og :math:`b_2` hefur eftirfarandi jöfnuhneppi lausn?

    .. math:: \begin{eqnarray*}
        x_1+x_2 = b_1\\
        x_1-x_2 = b_2
        \end{eqnarray*}

.. admonition:: Launs
    :class: daemi, dropdown

    Lítum á aukna fylkið og einföldum það með línuaðgerðum. Fáum

    .. math:: \begin{bmatrix}
        1 & 1 & b_1\\
        1& -1 & b_2
        \end{bmatrix}\sim 
        \begin{bmatrix}
        1 & 1 & b_1\\
        0& -2 & b_2-b_1
        \end{bmatrix}
    
    Með því að líta á vendistökin

    .. math:: \begin{bmatrix}
        \blacksquare & * & *\\
        0& \blacksquare & *
        \end{bmatrix}
    
    Má sjá að dálkurinn lengst til hægri er ekki vendidálkur svo jöfnuhneppið hefur alltaf lausn.

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

.. admonition:: Launs
    :class: daemi, dropdown

    Skoðum aukna fylkið og fáum

    .. math:: \begin{align*}
        \begin{bmatrix}
        1 & 2 & 3 &b_1\\
        4 & 5 & 6 &b_2\\
        7 & 8 & 9 &b_3\\
        \end{bmatrix}&\sim
        \begin{bmatrix}
        1 & 2 & 3& b_1\\
        0 & -3 & -6 &b_2 -4b_1\\
        0 & -6 & -12 &b_3-7b_1\\
        \end{bmatrix}\\&\sim
        \begin{bmatrix}
        1 & 2 & 3& b_1\\
        0 & -3 & -6 &b_2 -4b_1\\
        0 & 0 & 0 &b_3-7b_1-2(b_2-4b_1)\\
        \end{bmatrix}
        \end{align*}

    Einföldum stakið neðst til hægri og fáum :math:`b_3-7b_1-2(b_2-4b_1) = b_1-2b_2+b_3`.
    Við erum því með aukna fylkið

    .. math:: \begin{bmatrix}
        1 & 2 & 3& b_1\\
        0 & -3 & -6 &b_2 -4b_1\\
        0 & 0 & 0 &b_1-2b_2+b_3\\
        \end{bmatrix}

    Aukna fylkið á efri ruddri stallagerð hefur því formin

    .. math:: \begin{bmatrix}
        \blacksquare & * & *&*\\
        0& \blacksquare & * &*\\
        0& 0& 0& \blacksquare
        \end{bmatrix}
        \text{ eða }
        \begin{bmatrix}
        \blacksquare & * & *&*\\
        0& \blacksquare & * &*\\
        0& 0& 0& 0
        \end{bmatrix}  

    allt eftir því hvort stærðin :math:`b_1-2b_2+b_3` sé núll eða ekki. 
    Jöfnuhneppið okkar hefur lausn þá og því aðeins að dálkurinn lengst til hægri sé ekki vendidálkur.
    Jöfnuhneppið því því lausn þá og því aðeins að :math:`b_1-2b_2+b_3=0`.

Setning
^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki. Eftirfarandi fullyrðingar eru jafngildar.

        **1.** Jafnan :math:`A \textbf{x} = \textbf{b}` hefur lausn fyrir sérhvert :math:`\textbf{b} \in \mathbb{R}^m`.

        **2.** Sérhvert :math:`\textbf{b} \in \mathbb{R}^m` er línuleg samantekt af dálkum fylkisins :math:`A`.

        **3.** Dálkar fylkisins :math:`A` spanna :math:`\mathbb{R}^m`.

        **4.** :math:`A` hefur vendistak í hverri línu.

Setning
^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki, látum :math:`\textbf{u}` og :math:`\textbf{v}` vera 
    dálkvigra í :math:`\mathbb{R}^n` og látum :math:`c` vera rauntölu. Þá gildir:

        **1.** :math:`A(\textbf{u} + \textbf{v}) = A\textbf{u} + A\textbf{v}`.

        **2.** :math:`A(c\textbf{u}) = cA\textbf{u}`
