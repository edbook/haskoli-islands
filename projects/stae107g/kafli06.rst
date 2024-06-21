Kafli 6
=========

Innfeldi
--------

Skilgreining: Innfeldi
~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`\textbf{u}=(u_1,u_2,\dots,u_n)` og :math:`\textbf{v}=(v_1,v_2,\dots,v_n)` vera vigra í :math:`\R^n`. *Innfeldi* (e. inner product) er vörpun :math:`\R^n \times \R^n\ \rightarrow \R` sem tekur inn tvo vigra :math:`\bf u` og :math:`\bf v` og skilar tölunni :math:`\bf u^T v`.
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

    Látum :math:`\textbf{u}=(u_1,u_2,\dots,u_n)` vera vigur í :math:`\R^n`. *Lengd*, stundum kallað *staðall* eða *norm*, vigursins :math:`\bf u` er talan

    .. math:: ||\ve u||:=\sqrt{\ve u \cdot \ve u}=\sqrt{u_1^2+u_2^2+\dots + u_n^2}


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

    Vigur :math:`\ve u \in \R^n` sem hefur lengdina :math:`||\ve u||=1` kallast *einingarivigur* (e. unit vector). Stundum ritað :math:`\hat{\ve u}`.

Sérhvern vigur :math:`\ve u \in \R^n` (að undanskildum núllvigri) má *staðla*, þ.e. gera að einingarvigri, með því að deila með lengdinni, :math:`\hat{\ve u} = \ve u / || \ve u ||`.

Fjarlægðir í :math:`\R^n`
------------------------

Skilgreining: Fjarlægð milli punkta í :math:`\R^n`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`\ve u` og :math:`\ve v` vera vigra í :math:`\R^n`. *Fjarlægðin* milli :math:`\ve u` og :math:`\ve v` er skilgreind sem lengdin á vigrinum :math:`\ve u- \ve v`, þ.e.

    .. math:: d(\ve u, \ve v):=||\ve u - \ve v || = \sqrt{(u_1-v_1)^2 + (u_2-v_2)^2 + \dots + (u_n-v_n)^2}.

Í skilgreiningunni hér að ofan hugsum við um :math:`\ve u` og :math:`\ve v` ýmist sem vigra eða punkt í :math:`\R^n`. Á eftirfarandi mynd má sjá fjarlægð milli tveggja vigra.

MYND

Reiknireglur um fjarlægðir 
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Setning
    :class: setning

    Látum :math:`\ve u, \ve v` og :math:`\ve w` vera puntka í :math:`\R^n`. Þá gildir

    **1.** :math:`d(\ve u, \ve v) \geq 0` og :math:`d(\ve u, \ve v)=0` ef og aðeins ef :math:`\ve u= \ve v`.

    **2.** :math:`d(\ve u, \ve v)=d(\ve v,\ve u)`.

    **3.** :math:`d(\ve u,\ve w) \leq d(\ve u, \ve v)+d(\ve v, \ve w)`.

Fall :math:`d: \R^n \times \R^n \rightarrow \R` sem uppfyllir þessi þrjú skilyrði kallast *firð* (e. metric).

Hornréttir vigrar
-----------------

Skilgreining: Hornréttir vigrar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`u` og :math:`v` vera vigra í :math:`\R^n`. Vigrarnir eru *hornréttir* (e. orthogonal) hvor á annan ef :math:`u \cdot v = 0`.


Skilgreining: Horn milli vigra
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`u` og :math:`v` vera vigra í :math:`\R^n`, sem hvorugur er núll. *Horn milli* (e. angle between) vigranna er talan

    .. math:: \theta=\text{arccos}\Big(\frac{\ve u \cdot \ve v}{|| \ve u || || \ve v ||} \Big)

Skilgreining: Hornrétt fyllirúm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`W` vera mengi vigra í :math:`\R^n`. *Hornrétt fyllirúm* (e. orthogonal complement) er mengi :math:`W^{\perp}` allra þeirra vigra í :math:`\R^n` sem eru hornréttir á sérhvern vigur í :math:`W`, þ.e.

    .. math:: W^{\perp}=\{ z \in \R^n : z \cdot w =0\ \text{fyrir alla vigra}\ w \in W \}


Setning: Hornrétt fyllirúm
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Setning
    :class: setning

    **a.** Látum :math:`W` vera hlutmengi í :math:`\R^n`. Hornrétta fyllirúmið :math:`W^{\perp}` er hlutrúm í :math:`\R^n`.

    **b.** Ef :math:`W` er hlutrúm í :math:`\R^n` þá :math:`W \cap W^{\perp}=\{\ve 0\}` og :math:`(W^{\perp})^{\perp}=W`.

    **c.** Látum :math:`W=\text{Span}\{v_1,...,v_p\}`. Vigur :math:`x` er í :math:`W^{\perp}` ef og aðeins ef hann er hornréttur á sérhvern vigranna :math:`v_1,...,v_p`.

    **d.** Látum :math:`A` vera :math:`m \times n` fylki. Þá er :math:`\text{Row}(A)^{\perp}=\text{Nul}(A)` og :math:`\text{Col}(A)^{\perp}=\text{Nul}(A^{T})`.


Þverstæð og þverstöðluð mengi
-----------------------------

Skilgreining: Hornrétt fyllirúm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
    :class: skilgreining

    Mengi :math:`W` í :math:`\R^n` er *þverstætt* (e. orthogonal) ef sérhverjir tveir vigrar í menginu eru hornréttir hvor á annan.
    Mengið er sagt *þverstaðlað* (e. orthonormal) ef það er þverstætt og allir vigrarnir í :math:`W` hafa lengdina 1.



Sýnidæmi: Þverstæð og þverstöðluð mengi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. admonition:: Dæmi
  :class: daemi
  
  **1.** Venjulegi grunnurinn :math:`\{\ve e_1, \dots, \ve e_n \}` í :math:`\R^n` er þverstaðlað mengi. Þeir hafa allir lengdina einn þar sem þeir eru einingarvigrar og þeir eru hornréttir samkvæmt skilgreiningu.

  **2.** :math:`\{v_1, v_2, v_3 \}` þar sem :math:`v_1=(3,1,1), v_2=(-1,2,1)` og :math:`v_3=(-1/2,-2,7/2)` er þverstætt mengi. Það má auðveldlega sannfæra sig að svo sé með því að sýna fram á að öll infeldin :math:`v_1 \cdot v_2, v_1 \cdot v_3` og :math:`v_2 \cdot v_3` séu núll, og lengdir vigranna eru ekki 1.


Setning: Þverstætt mengi er línulega óháð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Setning
    :class: setning

    Látum :math:`S=\{\ve u_1, \dots, \ve u_p\}` vera þverstætt hlutmengi í :math:`\R^n` sem inniheldur engan núllvigur. Þá er :math:`S` línulega óháð og er því grunnur fyrir hlutmengið spannað af :math:`S`.


Skilgreining: Þverstæðir og þverstaðlaðir grunnar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`W` vera hlutrúm í :math:`\R^n` og :math:`\{\ve u_1, \dots, \ve u_p \}` vera grunn fyrir :math:`W`.
    
    **1.** Grunnurinn fyrir :math:`W` er *þverstæður* (e. orthogonal basis) ef sérhverjir tveir ólíkir vigrar í grunninum eru hornréttir hvor á annan, m.o.ö.

        .. math:: u_i \cdot u_j =0\  \forall \ i \neq j.
    
    **2.** Grunnurinn  fyrir :math:`W` er *þverstaðlaður* (e. orthonormal basis) ef sérhverjir tveir vigrar í grunninum eru hornréttir hvor og annan og allir vigrarnir eru einingarvigrar, m.ö.o.

        .. math:: u_i \cdot u_j = \begin{cases}
            0\ \forall \ i \neq j \\
            1\ \forall \ i = j
            \end{cases}

Sýnidæmið um þverstæð og þverstöðluð mengi er einnig dæmi um þverstæða og þverstaðlaða grunna.


.. admonition:: Athugasemd
    :class: athugasemd

    Ef mengið :math:`\{\ve v_1, \dots, \ve v_p \}` er þverstæður grunnur fyrir hlutrúm :math:`W` í :math:`\R^n` þá er mengið 

    .. math:: \Big\{ \frac{\ve v_1}{|| \ve v_1 ||}, \dots, \frac{\ve v_p}{|| \ve v_p ||} \Big\}
    
    þverstaðlaður grunnur fyrir :math:`W`. Niðurstaðan er sú að ef við höfum þverstæðan grunn er hægt að búa til þverstaðlaðan grunn.



Skilgreining: Hnit m.t.t. þverstæðra og þverstaðlaða grunna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`W` vera hlutrúm í :math:`\R^n` og :math:`\mathcal{B}=\{\ve u_1, \dots, \ve u_p \}` vera grunn fyrir :math:`W`.

    **1.** Ef :math:`\ve y \in W` og :math:`\mathcal{B}` er þverstaæður þá er 

    .. math:: \ve y = c_1 \ve u_1 + \dots + c_p \ve u_p

    þar sem 

    .. math:: c_j = \frac{\ve y \cdot \ve u_j}{\ve u_j \cdot \ve u_j},\ \text{fyrir}\ j=1,...,p.
    
    Þ.e., hnitavigur :math:`\ve y` m.t.t. grunnsins :math:`\mathcal{B}` er

    .. math:: [\ve y]_{\mathcal{B}} = \Big(\frac{\ve y \cdot \ve u_1}{\ve u_1 \cdot \ve u_1}, \dots, \frac{\ve y \cdot \ve u_p}{\ve u_p \cdot \ve u_p} \Big).
    
    **2.** Ef :math:`\ve y \in W` og :math:`\mathcal{B}` er þverstaðlaður þá er

    .. math:: \ve y = c_1 \ve u_1 + \dots + c_p \ve u_p

    þar sem 

    .. math:: c_j = \ve y \cdot \ve u_j,\ \text{fyrir}\ j=1,...,p.

    Þ.e., hnitavigur :math:`\ve y` m.t.t. grunnsins :math:`\mathcal{B}` er

    .. math:: [\ve y]_{\mathcal{B}} = \Big(\ve y \cdot \ve u_1, \dots, \ve y \cdot \ve u_p \Big).
    

Sýnidæmi: 
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. admonition:: Dæmi
  :class: daemi

  Reikna á hint vigursins :math:`\ve v = (3,-2)` m.t.t. grunnanna :math:`\mathcal{B}=\{(1,1),(-1,1) \}` og :math:`\mathcal{C}=\{\frac{1}{\sqrt{2}}(1,1), \frac{1}{\sqrt{2}}(-1,1) \}` fyrir :math:`\R^2`.

.. admonition:: Lausn
  :class: daemi, dropdown

  **1.** Hnit :math:`\ve v` m.t.t. þverstæða grunnsins :math:`\mathcal{B}` eru
  
  .. math:: c_1 = \frac{(3,-2)\cdot (1,1)}{(1,1)\cdot (1,1)}=\frac{1}{2},

  og

  .. math:: c_2 = \frac{(3,-2)\cdot(-1,1)}{(-1,1)\cdot (-1,1)}=\frac{-5}{2},

  svo

  .. math:: (3,-2)=c_1 (1,1)+ c_2 (-1,1)=\frac{1}{2}(1,1) - \frac{5}{2}(-1,1)

  svo

  .. math:: [(3,-2)]_{\mathcal{B}}=(\frac{1}{2},\frac{-5}{2}).


  **2.** Hnit :math:`\ve v` m.t.t. þverstaðlaða grunnsins :math:`\mathcal{C}` eru

  .. math:: c_1 = (3,-2)\cdot \big(\frac{1}{\sqrt{2}}(1,1) \big)= \frac{1}{\sqrt{2}}

  og

  .. math:: c_2 = (3,-2)\cdot \big(\frac{1}{\sqrt{2}}(-1,1) \big)= \frac{-5}{\sqrt{2}}

  svo

  .. math:: [(3,-2)]_{\mathcal{C}}=(\frac{1}{\sqrt{2}},\frac{-5}{\sqrt{2}}).
  

Hornrétt ofanvarp
-----------------


.. figure:: myndir/ofanvarp.png
    





