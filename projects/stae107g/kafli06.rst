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

    **1.** :math:`d(\ve u, \ve v) \geq 0` og :math:`d(\ve u, \ve v)=0` ef og aðeins ef :math:`\ve u= \ve v`