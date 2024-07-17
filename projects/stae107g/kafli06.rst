Innfeldi og hornrétt ofanvörp
==============================

Innfeldi
--------

Skilgreining: Innfeldi
~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`\textbf{u}=(u_1,u_2,\dots,u_n)` og :math:`\textbf{v}=(v_1,v_2,\dots,v_n)` vera vigra í :math:`\R^n`. 
    **Innfeldi** (e. inner product) er vörpun :math:`\R^n \times \R^n\ \rightarrow \R` sem tekur inn tvo vigra :math:`\bf u` og :math:`\bf v` og skilar tölunni :math:`\bf u^T v`.
    Oftast ritað
    
    .. math:: \textbf{u} \cdot \textbf{v}=\left(
        \begin{array}{cccc}
        u_1 & u_2 & \dots & u_n \\
        \end{array}
        \right)
        \cdot
        \left(
        \begin{array}{c}
        v_1 \\
        v_2 \\
        \dots \\
        v_n \\
        \end{array}
        \right)=
        u_1 v_1 + u_2 v_2 + ... u_n v_n.

Skilgreina má innfeldi fyrir almenn vigurrúm, ekki bara :math:`\R^n`. Stundum er innfeldið á :math:`\R^n` kallað *depilmargfeldi*.

Sýnidæmi: Innfeldi
^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi

  Látum :math:`\textbf{u}=\begin{bmatrix} 1 \\ 2 \end{bmatrix}` og
  :math:`\textbf{v}=\begin{bmatrix} 3 \\ 4 \end{bmatrix}` reiknið innfeldið.

.. admonition:: Lausn
  :class: daemi, dropdown

  .. math:: \textbf{u} \cdot \textbf{v} = 1 \cdot 3 + 2 \cdot 4 = 3+8=11


Reiknireglur um innfeldi á :math:`\R^n`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Setning
    :class: setning

    Látum :math:`\bf u,v` og :math:`\bf w` vera vigra í :math:`\R^n` og :math:`c \in \R`. Þá gildir

    **1.** :math:`\bf u \cdot v = \bf v \cdot u`.

    **2.** :math:`(\ve u+ \ve v)\cdot \ve w = \bf u \cdot w + v \cdot u`.

    **3.** :math:`(c \ve u)\cdot  \ve v = c ( \ve u\cdot \ve v)= \ve u \cdot (c \ve v)`.

    **4.** :math:`\ve u \cdot \ve u \geq 0`, og :math:`\ve u \cdot \ve u = 0` ef og aðeins ef :math:`\bf u=0`.

Lengd
-----

Skilgreining: Lengd
~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`\textbf{u}=(u_1,u_2,\dots,u_n)` vera vigur í :math:`\R^n`. **Lengd**, stundum kallað *staðall* eða *norm*, vigursins :math:`\bf u` er talan

    .. math:: ||\ve u||:=\sqrt{\ve u \cdot \ve u}=\sqrt{u_1^2+u_2^2+\dots + u_n^2}

Sýnidæmi: Lengd vigurs
^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi

  Reiknið lengd vigursins :math:`\textbf{u} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}`

.. admonition:: Lausn
  :class: daemi, dropdown 

  .. math:: ||\textbf{u}|| = ||(1,2,3)||=\sqrt{1^2+2^2+3^2}=\sqrt{1+4+9}=\sqrt{14}


Reiknireglur um lengd 
~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Setning
    :class: setning

    Látum :math:`\bf u` og :math:`\bf v` vera vigra í :math:`\R^n` og :math:`c \in \R`. Þá gildir

    **1.** :math:`||\ve u||\geq 0` og :math:`||\ve u||=0` ef og aðeins ef :math:`\ve u=\ve 0`.

    **2.** :math:`|| \ve u + \ve v || \leq ||\ve u|| + ||\ve v||`.

    **3.** :math:`|| c \ve u|| = |c| ||\ve u||`.

    **4.** :math:`|\ve u \cdot\ve v | \leq ||\ve u || || \ve v ||`

Skilgreining: Einingarvigur
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
    :class: skilgreining

    Vigur :math:`\ve u \in \R^n` sem hefur lengdina :math:`||\ve u||=1` kallast **einingarvigur** (e. unit vector). Stundum ritað :math:`\hat{\ve u}`.

Sérhvern vigur :math:`\ve u \in \R^n` (að undanskildum núllvigri) má *staðla*, þ.e. gera að einingarvigri, með því að deila með lengdinni, :math:`\hat{\ve u} = \ve u / || \ve u ||`.

Fjarlægðir í :math:`\R^n`
--------------------------

Skilgreining: Fjarlægð milli punkta í :math:`\R^n`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`\ve u` og :math:`\ve v` vera vigra í :math:`\R^n`. **Fjarlægðin** milli :math:`\ve u` og :math:`\ve v` er skilgreind sem lengdin á vigrinum :math:`\ve u- \ve v`, þ.e.

    .. math:: dist(\ve u, \ve v):=||\ve u - \ve v || = \sqrt{(u_1-v_1)^2 + (u_2-v_2)^2 + \dots + (u_n-v_n)^2}.

Í skilgreiningunni hér að ofan hugsum við um :math:`\ve u` og :math:`\ve v` ýmist sem vigra eða punkt í :math:`\R^n`. Á eftirfarandi mynd má sjá fjarlægð milli tveggja vigra.

MYND

Sýnidæmi: Fjarlægð milli punkta
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi

  Riknum fjarlæð milli :math:`\begin{bmatrix} 1 \\ 2 \end{bmatrix}` og  :math:`\begin{bmatrix} -3 \\ 4 \end{bmatrix}`

.. admonition:: Lausn
  :class: daemi, dropdown

  .. math:: \sqrt{(1-(-3))^2+(2-4)^2}=\sqrt{4^2+(-2)^2}=\sqrt{16+4}=\sqrt{20}

Reiknireglur um fjarlægðir 
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Setning
    :class: setning

    Látum :math:`\ve u, \ve v` og :math:`\ve w` vera puntka í :math:`\R^n`. Þá gildir

    **1.** :math:`dist(\ve u, \ve v) \geq 0` og :math:`dist(\ve u, \ve v)=0` ef og aðeins ef :math:`\ve u= \ve v`

    **2.** :math:`dist(\ve u, \ve v) = dist(\ve v, \ve u)`

    **3.** :math:`dist(\ve u, \ve w) \leq dist(\ve u + \ve v)+dist(\ve v + \ve w)` 

Hornréttir vigrar
-----------------

Skilgreining: Hornrétt
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Látum :math:`\ve u` og :math:`\ve v` vera vigra í :math:`\mathbb{R}^n`.
  Vigrarnir :math:`\ve u` og :math:`\ve v` eru sagðir **hornréttir** (á hvorn annan) (e. orthogonal)  
  ef :math:`\ve u \cdot \ve v=0`

Skilgreinig: Hornið milli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreinig
  :class: skilgreining

  Ef :math:`\ve u` og :math:`\ve v` eru vigrar í  :math:`\mathbb{R}^n`, sem er hvorugur núll, þá
  skilgerinum við **hornið milli** (e. angle between) þeirra sem töluna 

  .. math:: \theta = \arccos(\frac{\textbf{u}\cdot\textbf{v}}{||\textbf{u}|| ||\textbf{v}||})

Regla Pýþagórasar
~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Vigrarnir :math:`\ve u` og :math:`\ve v` eru hornréttir hvor á annan þá 
  og því aðeins að

  .. math:: ||\ve u||^2+||\ve v||^2=||\ve u + \ve v||^2

Hornrétt fyllirúm 
--------------------

Skilgreining: Hornrétt fyllirúm 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Við segjum að mengi allra staka sem eru hornrétt á :math:`W` 
  sé **hornrétt fyllirúm** (e. orthogonal complement) og táknum það með :math:`W^\perp`. 

Hornrétt fyllirúm er hlutrúm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`W` vera hlutrúm í :math:`\mathbb{R}^2`. Fáum að:

    **1.** Vigurinn :math:`\ve 0` er hornréttur á öll stök í :math:`W` svo :math:`\ve 0 \in W^\perp`.

    **2.** Látum :math:`\ve u, \ve v \in W^\perp` og látum :math:`\ve w` vera hvaða vigur sem er í :math:`W`. 
    Þá er 

    .. math::(\ve u + \ve v)\cdot\ve w = \ve u \cdot \ve w + \ve v \ cdot \ve w=0+0=0
    
    svo :math:`(\ve u+\ve v)` er hornrétt á alla vigra :math:`W` og því er :math:`(\ve u + \ve v) \in W^\perp`.

    **3.** Látum :math:`\ve u \in W^\perp`, :math:`\ve w` vera hvaða vigru sem er í :math:`W` og :math:`c` vera raunrölu. Þá er 

    .. math:: (c\textbf{u})\cdot \textbf{w} = c\ve u \cdot \ve w = c \cdot 0 = 0 
    
    svo :math:`c\ve u` er hornréttu á alla vigra í :math:`W` og því er :math:`c\ve u\in W^\perp`.

Þetta sýnir að :math:`W^\perp` er hlutrúm í :math:`\mathbb{R}^n`.

Setning: ????
~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Látum :math:`A` vera :math:`m \times n` fylki. Þá gildir 

    **1.** :math:`(Row A)^\perp = Nul A`

    **2.** :math:`(Col A)^\perp = Nul A^T` 

Þverstæð mengi
-----------------

Skilgreining: Þverstætt
~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Látum :math:`W` vera mengi vigra í :math:`\mathbb{R}^n`. Mengið er sagt 
  **þverstætt** (e. orthogonal) ef sérhverjir tveir vigrar í menginu eru hornréttir hvor á annan.

Sýnidæmi: Þverstætt mengi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi

  Mynda eftirfarandi vigrar þverstætt mengi?

  .. math:: \ve u=\begin{bmatrix} 1 \\ -2 \\ 0 \end{bmatrix}, 
    \ve v=\begin{bmatrix} 2 \\ 1 \\ 3 \end{bmatrix}, 
    \ve w=\begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix}

.. admonition:: Lausn
  :class: daemi, dropdown

  Skoðum hvort vigrarnir myndi þverstætt mengi

  .. math:: \ve u \cdot \ve v = (1)(2)+(-2)(1)+(0)(3)=0

  .. math:: \ve v \cdot \ve w = (2)(1)+(1)(1)+(3)(-1)=0
    
  .. math:: \ve u \cdot \ve w = (1)(1)+(-2)(1)+(0)(-1)=-1
  
  Þar sem innfeldið er ekki 0 í öllum tilfellum svo vigrarir mynda ekki þverstætt mengi.

Sýnidæmi: Þverstætt mengi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi

  Mynda eftirfarandi vigrar þverstætt mengi?

  .. math:: \ve u=\begin{bmatrix} 1 \\ -2 \\ 0 \end{bmatrix}, 
    \ve v=\begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}, 
    \ve w=\begin{bmatrix} 0 \\ 0 \\ 3 \end{bmatrix}

.. admonition:: Lausn
  :class: daemi, dropdown

  Skoðum hvort vigrarnir myndi þverstætt mengi

  .. math:: \ve u \cdot \ve v = (1)(2)+(-2)(1)+(0)(3)=0
    
  .. math:: \ve v \cdot \ve w = (2)(0)+(1)(0)+(0)(3)=0
    
  .. math:: \ve u \cdot \ve w = (1)(0)+(-2)(0)+(0)(3)=0
  
  Þar sem innfeldið er 0 í öllum tilfellum mynda vigrarnir þverstætt mengi.


MYND

Skilgreining: Þverstaðlað
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Látum :math:`W` vera mengi vigra í :math:`\mathbb{R}^n`. Mengið er sagt **þverstaðlað** (e. orthonormal) ef 
  það er þverstætt og allir vigrarnir í :math:`W` hafa lengdina 1.

.. admonition:: Athugasemd
    :class: athugasemd

    Athugið að sérhvert þverstaðlað mengi er líka þverstætt en til eru þverstæð mengi sem eru ekki þverstöðluð.

Setning: Þverstæð mengi
~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Þverstætt mengi :math:`S=\{\ve u_1, \cdots \ve u_p\}` af vigrum þar sem enginn vigur er núllvigur er línulega óháð.
  Þannig myndar þverstærr mengi grunn fyrir hlutrúmið sem :math:`S` spannar.

Þverstæður grunnur
-------------------

Skilgreining: Þverstæðir og þverstaðlaðir grunnar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Látum :math:`W` vera hlutrúm í :math:`\mathbb{R}^n` og í :math:`{\ve u_1 \cdots \ve u_p}` grunn fyrir í :math:`W`.
  
  **1.** Grunnurinn er kallaður **Þverstæður grunnur** (e. orthogonal basis) ef sérhverjir tveir ólíkir vigrar í grunninum eru hornréttir hvorn á annan.

  **2.** Grunnurinn er kallaður **þverstaðlaður grunnur** (e. orthonormal basis) ef sérhverjir tveir ólíkir vigrar í grunninum eru hornréttir hvor 
  á annan og vigrarnir eru einingarvigrar.
  
Setning: Þverstæðir grunnar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Ef :math:`\mathbb{B}=\{\ve u_1 \cdots \ve u_p\}` er þverstæður grunnur fyrir :math:`W` sem 
  er hlutrúm í :math:`\mathbb{R}^n` þá eru vogstuðlarnir fyrir línulegu samantektina (með öðrum oðrum, hnit :math:`\ve y` m.t.t. :math:`\mathbb{B}`)

  .. math:: \ve y = c_1\ve u_1+\cdots+c_p\ve u_p

  gefnir með

  .. math:: c_j=\frac{\ve y \cdot \ve u_j}{\ve u_j\cdot \ve u_j} \text{ fyrir } j=1,\cdots,p.

.. admonition:: Fylgisetning
  :class: setning

  Ef grunnurinn í setningunni að ofan er þverstaðlaður verður formúlan fyrir stuðlunum einfaldlega

  .. math:: c_j = \ve y \cdot \ve u_j \text{ fyrir } j=1,\cdots,p

Sýnidæmi: Þverstæður grunnur
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi

  Finnið hnit puktsins :math:`\ve y=(1,1,1)` með tilliti til þverstæða grunnsins

  .. math:: \mathcal{B}=
    \left\{
    \begin{bmatrix} 1 \\ -2 \\ 0 \end{bmatrix}, \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 0 \\ 3 \end{bmatrix}
    \right\}

.. admonition:: Lausn
  :class: daemi, dropdown

  Setning gefur

  .. math:: c_1 = \frac{(1,1,1)\cdot (1,-2,0)}{(1,-2,0)\cdot (1,-2,0)}=
    \frac{1-2+0}{1+(-2)^2+0^2}=-\frac{1}{5}

  .. math:: c_2 = \frac{(1,1,1)\cdot (2,1,0)}{(2,1,0)\cdot (2,1,0)}=
    \frac{2+1+0}{2^2+1^2+0^2}=\frac{3}{5}
  
  .. math:: c_3 = \frac{(1,1,1)\cdot (0,0,3)}{(0,0,3)\cdot(0,0,3)}=
    \frac{0+0+3}{0^2+0^2+3^2}=\frac{3}{9}=\frac{1}{3}
  
  Svo

  .. math:: [\ve y]_\mathcal{B}=\left(-\frac{1}{5}, \frac{3}{5}, \frac{1}{3}\right)

Hornrétt ofanvarp
-------------------

Skilgreining: Hornrétt ofanvarp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Látum :math:`\ve u \neq \ve 0` vera vigur í :math:`\mathbb{R}^n`. Látum nú
  :math:`\ve y` vera vigur í :math:`\mathbb{R}^n`. Vigurinn

  .. math:: \hat{\ve y} = \frac{\ve y \cdot \ve u}{\ve u \cdot \ve u}\cdot \ve u

  er kallaður **hornrétt ofanvarp vigursins y á vigurinn u** (e. orthogonal projection og  :math:`\ve y` on  :math:`\ve u`).
  Það að rita :math:`\ve y=\hat{\ve y}+\ve z` er kallað að liða vigurinn :math:`\ve y` upp í liði þannig að annar er samsíða
  :math:`\ve u` og hinn er hornréttur á :math:`\ve u`.  


Sýnidæmi: Hornrétt ofanvarp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi

  Látum :math:`\ve u=(3,1)` og :math:`\ve y=(1,3)`. Reiknið hornrétt 
  ofanvarp :math:`\ve u` á :math:`\ve y`

.. admonition:: Lausn
  :class: daemi, dropdown

  .. math:: \hat{\ve y} = \frac{\ve y \cdot \ve u}{\ve u \cdot \ve u}=\frac{(3,1)\cdot(1,3)}{(3,1)\cdot(3,1)}\begin{bmatrix} 3 \\ 1 \end{bmatrix}=\frac{6}{10}\begin{bmatrix} 3 \\ 1 \end{bmatrix}=\frac{3}{5}\begin{bmatrix} 3 \\ 1 \end{bmatrix}=\begin{bmatrix} \frac{9}{5} \\ \frac{3}{5} \end{bmatrix}

  og þverþátturinn er 

  .. math:: \ve z = \ve y - \hat{\ve y}=\begin{bmatrix}1 \\3 \end{bmatrix}-\begin{bmatrix} \frac{9}{5} \\ \frac{3}{5} \end{bmatrix}=\begin{bmatrix} -\frac{4}{5} \\ \frac{12}{5} \end{bmatrix}

  Í kjölfari er stundum gagnlegt að finna fjarlægð :math:`\ve y` frá rúminu sem :math:`\ve u` spannar.
  Það er :math:`||\ve z||`.

  .. math:: \sqrt{(-\frac{4}{5})^2+(\frac{12}{5})^2}=\sqrt{\frac{16}{25}+\frac{144}{25}}=\sqrt{32}

.. admonition:: Lausnir prófaðar
  :class: daemi, dropdown

  Fengum gefið :math:`\ve u=\begin{bmatrix} 3 \\1 \end{bmatrix}` og :math:`\ve y=\begin{bmatrix} 1 \\3 \end{bmatrix}`. Við fengum 
  :math:`\hat{\ve y}=\begin{bmatrix} \frac{9}{5} \\ \frac{3}{5} \end{bmatrix}` og 
  :math:`\hat{\ve z}=\begin{bmatrix} -\frac{4}{5} \\ \frac{12}{5} \end{bmatrix}`. Prófum þessar lasunir 
  
    :math:`\ve y` er summan að  :math:`\hat{\ve y}` og  :math:`\ve z`
    
    .. math:: \hat{\ve y}+\ve z =\begin{bmatrix} \frac{9}{5} \\ \frac{3}{5} \end{bmatrix}+\begin{bmatrix} -\frac{4}{5} \\ \frac{12}{5} \end{bmatrix}=\begin{bmatrix} 1 \\ 3 \end{bmatrix}
    
    :math:`\hat{\ve y}` er samsíða :math:`\ve u` því

    .. math:: \hat{\ve y} = \begin{bmatrix} \frac{9}{5} \\ \frac{3}{5} \end{bmatrix} = \frac{3}{5} \begin{bmatrix} 3 \\ 1 \end{bmatrix} = \frac{3}{5} \ve u
     
    :math:`\ve z` er hornrétt á :math:`\ve u`

    .. math:: \ve z \cdot \ve u = \begin{bmatrix} -\frac{4}{5} \\ \frac{12}{5} \end{bmatrix} \cdot \begin{bmatrix} 3 \\1 \end{bmatrix} = -\frac{12}{3}+\frac{12}{3}=0


Skilgreining: Hornrétta ofanvarpið
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Látum :math:`W` vera hlutrúm í :math:`\mathbb{R}^n`. Skilgreinum vörpun :math:`proj_w:\mathbb{R}^n \rightarrow \mathbb{R}^n`
  þannig að fyrir vigur :math:`\ve y \ in \mathbb{R}^n` er :math:`proj_w \ve y=\hat{\ve y}`. Þessi vörpun er kölluð **hornrétts ofanvarpið** á 
  hlutrúmið :math:`W`.

Eiginleikar ofanvarps
~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`W` vera hlutrúm í :math:`\mathbb{R}^n`.

    **1.** Fyrir sérhvern vigur :math:`\ve y \in \mathbb{R}^n` þá er :math:`proj_w(\ve y) \in W`.

    **2.** Ef :math:`\ve y \in W` þá er :math:`proj_w \ve y=\ve y`

    **3.** Ef :math:`\ve y \in W^\perp` þá er :math:`proj_w \ve y=\ve 0`

    **4.** Fyrir sérhvern vigur :math:`\ve y \in \mathbb{R}^n` gildir að :math:`proj_w(proj_w \ve y)=proj_w \ve y` 
    um vörpunina :math:`proj_w` gildir að :math:`proj_w \cdot  y=\ve y`


Rifjum upp að grunnur fyrir hlutrúm :math:`W` er sagður *þverstaðlaður* ef hann er *þverstæður* og sérhver
vigur í grunninum er einingarvigur (hefur lengs 1). Ef :math:`\{\ve u_1, \ve u_2, \cdots, \ve u_p \}` er þverst´'ur grunnur þá er 
grunnurinn :math:`\{ \frac{\ve u_1}{||\ve u_1||}, \frac{\ve u_2}{||\ve u_2||}, \cdots, \frac{\ve u_p}{||\ve u_p||} \}` þverstaðlaður.
Þar sem alltaf er til þverstæður grunnur fyrir hlutrúm fáum við nú að alltaf er til þverstaðlaður grunnur.

Setning: Ofavarp og þverstaðlaðir grunnar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Látum :math:`W` vera hlutrúm í :math:`\mathbb{R}^n`. Ef :math:`\{ \ve u_1, \ve u_2, \cdots, \ve u_p \}` er þverstaðlaður grunnur
  fyrir :math:`W` þá er 

  .. math:: proj_w \ve y=\hat{\ve y}=(\ve y \cdot \ve u_1)\ve u_1 + (\ve y \cdot \ve u_2)\ve u_2+ \cdots + (\ve y \cdot \ve u_p)\ve u_p

Setning: Fylki fyrir ofanvarp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Látum :math:`W` vera hlutrúm í :math:`\mathbb{R}^n` og gerum ráð fyrir að 
  :math:`\{ \ve u_1, \ve u_2, \cdots, \ve u_p \}` sé þverstaðlaður grunnur fyrir
  :math:`W`. Skilgreinum :math:`n \times p` fylkið 

  .. math:: U = \begin{bmatrix} \ve u_1 & \ve u_2 & \cdots & \ve u_p \end{bmatrix}

  Fyrir sérhvern vigur :math:`\ve y \in \mathbb{R}^n` er 

  .. math:: proj_w \ve y = UU^T \ve y.


Gram-Schmidt
--------------

Gram-Schmidt reikniritið
~~~~~~~~~~~~~~~~~~~~~~~~~

Við setjum okkur að leysa eftirfarandi verkefni:

Út frá tilteknum grunni :math:`\{\ve x_1, \cdots, \ve x_p \}` fyrir hlutrúm :math:`W` í :math:`\mathbb{R}^n` 
viljum við búa til þverstæðan grunn :math:`\{ \ve v_1, \cdots, \ve v_p\}` fyrir :math:`W`.
Þetta er gert með þeim hætti að fyrir sérhvert :math:`k=1, \cdots, n` ver'i :math:`\ve v_1, \cdots, \ve v_k`
þverstæð upptalning og 

.. math:: Span(\{\ve v_1, \cdots, \ve v_k\})=Span(\{\ve x_1, \cdots, \ve x_k\}).

Reikniritið sem við notum er oftast nefnt **Gram-Schmidt-aðferð**


Setning: Gram-Schmidt aðferð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Látum :math:`\{x_1, \cdots, x_p\}` vera grunn fyrir hlutrúm :math:`W` ( og :math:`W \neq {\ve 0}`)
  í :math:`\mathbb{R}^n`. setjum

  .. math:: \ve v_1 = \ve x_1

  .. math:: \ve v_2 = \ve x_2 - \frac{\ve x_2 \cdot \ve v_1}{\ve v_1 \cdot \ve v_1}\ve v_1

  .. math:: \ve v_3 = \ve x_3 - \frac{\ve x_3 \cdot \ve v_1}{\ve v_1 \cdot \ve v_1}\ve v_1 - \frac{\ve x_3 \cdot \ve v_2}{\ve v_2 \cdot \ve v_2}\ve v_2

  .. math:: \vdots
  
  .. math:: \ve v_p = \ve x_p- \frac{\ve x_p \cdot \ve v_1}{\ve v_1 \cdot \ve v_1}\ve v_1
     - \frac{\ve x_p \cdot \ve v_2}{\ve v_2 \cdot \ve v_2}\ve v_2 - 
     \cdots - \frac{\ve x_p \cdot \ve v_{p-1}}{\ve v_{p-1} \cdot \ve v_{p-1}}\ve v_{p-1}

  Þá er :math:`\{v_1, \cdots, v_p\}` þverstæður grunnur fyrir :math:`W` og 

  .. math:: Span(\{\ve v_1, \cdots, \ve v_p\})=Span(\{\ve x_1, \cdots, \ve x_p\})
  
  fyrir :math:`k=1, \cdots, p`.

Sýnidæmi: Gram-Schmidt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi

  Látum 
  
  .. math:: W=Span\left\{\begin{bmatrix} 1 \\ 3 \\ 1 \\ 1 \end{bmatrix}, 
    \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix}, \begin{bmatrix}
    -1 \\ 5 \\ 2 \\ 2 \end{bmatrix}\right\{ \in \mathbb{R}^4
  
  Finnið þverstæðan grunn fyrir :math:`V`.

.. admonition:: Lausn
  :class: daemi, dropdown

  Notum reikniaðferð Gram-Schmidt

  **Skref 1:** Sjáum að vigrarnir :math:`\ve x_1=(1,3,1,1), \ve x_2=(1,1,1,1) \text{ og } \ve x_3=(-1,5,2,2)` 
  eru línulega óháðir og mynda því þeir grunn fyrir :math:`W`.

  **Skref 2:** Setjum :math:`\ve v_1=\ve x_1=(1,3,1,1)`. Svo setjum við

  .. math:: \ve v_2 = \ve x_2 - \frac{\ve x_2 \cdot \ve v_1}{\ve v_1 \cdot \ve v_1}\ve v_1

  .. math:: = (1,1,1,1)- 
    \frac{(1,1,1,1) 
    \cdot (1,3,1,1)}{(1,3,1,1)
    \cdot (1,3,1,1)}
    (1,3,1,1)

  .. math:: (1,1,1,1) - \frac{6}{12}(1,3,1,1)
    = (1/2, -1/2, 1/2, 1/2)
    = \frac{1}{2}(1,-1,1,1).

  Prófun sýnir að :math:`\ve v_2` er hornréttur á :math:`\ve v_1`. Að lokum setjum við

  .. math:: \ve v_3 = \ve x_3 - \frac{\ve x_3 \cdot \ve v_1}{\ve v_1 \cdot \ve v_1}\ve v_1 - \frac{\ve x_3 \cdot \ve v_2}{\ve v_2 \cdot \ve v_2}\ve v_2 

  .. math:: = (-1,5,2,2)- 
    \frac{(-1,5,2,2) \cdot (1,3,1,1)}
    {(1,3,1,1) \cdot (1,3,1,1)}
    (1,3,1,1)
  
  .. math:: - \frac{(-1,5,2,2) \cdot \frac{1}{2}(1,-1,1,1)}
    {\frac{1}{2}(1,-1,1,1) \cdot \frac{1}{2}(1,-1,1,1)}
    \frac{1}{2}(1,-1,1,1)

  .. math:: = (-1,5,2,2)-(18/12(1,3,1,1)-\frac{1}{2}(1,-1,1,1))
    
  .. math:: =(-2,0,1,1)

  **Skref 3:** Prófun sýnir að :math:`\ve v_3` er hornréttur á :math:`\ve v_1` og :math:`\ve v_2`.
  
  Vigrarnir :math:`\ve v_1, \ve v_2, \ve v_3` mynda þverstæðan grunn fyrir :math:`W`.

  Höfum því sýnt að :math:`\{(1,3,1,1), \frac{1}{2}(1,-1,1,1), (-2,0,1,1)\}` er þverstæður
  frunnur fyrir :math:`W=Span\{(1,3,1,1),(1,1,1,1),(-1,5,2,2)\} \in \mathbb{R}^4`.
  Fáum þá þverstaðlaðan grunn fyrir :math:`W` sem er

  .. math:: \left\{\frac{(1,3,1,1)}{||(1,3,1,1)||}, \frac{\frac{1}{2}(1,-1,1,1)}{||(1,-1,1,1)||}, \frac{-2,0,1,1}{||(-2,0,1,1)||}\right\}
    
  .. math:: = \left\{\frac{(1,3,1,1)}{s\sqrt{3}}, \frac{1}{2}(1,-1,1,1), \frac{-2,0,1,1}{\sqrt{6}}\right\}

Hvernig finnum við þverstaðlaðan grunn?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Skref 1.** Byrjum á að finna einhvern grunn fyrir :math:`W`.

**Skref 2.** Notum aðferð Gram-Schmidt til að finna þverstæðan grunn fyrir :math:`W`.

**Skref 3.** Ef bið fengum þverstæðan grunninn :math:`\{\ve v_1, \ve v_2, \cdots, \ve v_p\}`
í skrefi 2 þá búum við til þverstaðlaða grunninn

.. math:: \left\{\frac{\ve v_1}{||\ve v_1||}, \frac{\ve v_2}{||\ve v_2||}, \cdots, \frac{\ve v_p}{||\ve v_p||}\right\}.


Aðferð minnstu kvaðrat 
-------------------------
