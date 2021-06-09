Jaðargildisverkefni fyrir sporgerar (e. elliptic) hlutafleiðujöfnur
===================================================================

Almenn atriði um jaðargildisverkefni
------------------------------------

Við ætlum að skoða annars stigs línulegar hlutafleiðujöfnur á svæði
:math:`R` í :math:`{\mathbb  R}^2`, þetta eru jöfnur á forminu

.. math::

   \begin{gathered}
   A(x,y)\frac{{\partial}^2 u}{{\partial}x^2} + B(x,y)\frac{{\partial}^2 u}{{\partial}x{\partial}y} + C(x,y)\frac{{\partial}^2 u}{{\partial}y^2} +\\
   D(x,y)\frac{{\partial}u}{{\partial}x} + E(x,y)\frac{{\partial}u}{{\partial}y} + F(x,y)u = G(x,y).\end{gathered}

Skilgreining
~~~~~~~~~~~~

Annars stigs línuleg hlutafleiðujafna eins og að ofan kallast *sporger*
(e. elliptic) ef

.. math:: A(x,y)C(x,y) - B(x,y)^2 > 0,

fyrir öll :math:`(x,y) \in R`.

Sporgerar jöfnur
~~~~~~~~~~~~~~~~

Sporgerar jöfnur eru tímaóháðar og lýsa oft verkefnum þar sem verið er
að leita að jafnvægisástandi (lágmarksflötum, hitajafnvægi og þess
háttar).

Laplace/Poisson
~~~~~~~~~~~~~~~

Við ætlum að einskorða okkur við mikilvægasta tilvikið, *Laplace
jöfnuna*

.. math:: \frac{{\partial}^2 u}{{\partial}x^2} + \frac{{\partial}^2 u}{{\partial}y^2} = 0,

\ og hliðraða útgáfu hennar, *Poisson jöfnuna*

.. math:: \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = f(x,y).

Jaðarskilyrði
~~~~~~~~~~~~~

**Svæðið** :math:`R` Til einföldunar þá munum við eingöngu skoða
rétthyrninga á forminu

.. math:: R = \{ (x,y) \in {\mathbb  R}^2 ; a < x < b, c < y < d \}.

Eins og fyrir afleiðujöfnur með jaðarskilyrði (kafli 8) þá höfum við
þrjár gerðir af jaðarskilyrðum,

+--------------+------------------------------------------------------------------------------------------------------------+
| Dirichlet:   | :math:`u(x,y) = r(x,y)` á :math:`{\partial}R`.                                                             |
+--------------+------------------------------------------------------------------------------------------------------------+
| Neumann:     | :math:`\frac{{\partial}u}{{\partial}n}(x,y) = r(x,y)` á :math:`{\partial}R`.                               |
+--------------+------------------------------------------------------------------------------------------------------------+
| Robin:       | :math:`\alpha(x,y)u(x,y)+\beta(x,y)\frac{{\partial}u}{{\partial}n}(x,y) = r(x,y)` á :math:`{\partial}R`.   |
+--------------+------------------------------------------------------------------------------------------------------------+

Hér er :math:`{\partial}R` jaðar svæðisins :math:`R` og :math:`n` er
útvísandi þverill fyrir :math:`{\partial}R`.

Þýð föll
~~~~~~~~

**Skilgreining** Tvisvar sinnum samfellt diffranlegt fall :math:`u` á
svæði í :math:`{\mathbb  R}^2` sem uppfyllir Laplace jöfnuna

.. math:: \frac{{\partial}^2 u}{{\partial}x^2} + \frac{{\partial}^2 u}{{\partial}y^2} = 0,

kallast *þýtt*.

**Athugasemd** Tvisvar sinnum samfellt diffranlegt fall :math:`u` á
svæði :math:`R \subset {\mathbb  R}^2` er þýtt þá og því aðeins að

.. math:: u(x) = \frac{1}{\pi r^2} \int_{B(x,r)} u(y) dy

fyrir öll :math:`x \in R` og öll :math:`r` þannig að
:math:`B(x,r) \subset R`. Hér er :math:`B(x,r)` skífan með miðju
:math:`x` og geisla :math:`r`.

Með öðrum orðum, fallgildi þýðs falls :math:`u` í punkti :math:`x` er
jafnt ,,meðalfallgildi” :math:`u` umhverfis :math:`x`.

Poisson jafnan í rétthyrndu svæði – Dirichlet-jaðarskilyrði 
------------------------------------------------------------

Netið
~~~~~

Byrjum á að skipta rétthyrningnum :math:`R` í :math:`M \times N` net með
því að skipta bilinu :math:`[a,b]` í :math:`N` bil og bilinu
:math:`[c,d]` í :math:`M` bil. Til einföldunar þá gerum við ráð fyrir að
hlutfall hliðarlengdanna í :math:`R` sé ræð tala, því þá getum við
fundið :math:`M` og :math:`N` þannig að

.. math:: \frac{b-a}N = \frac{d-c}M = h.

Þar með er hver reitur í netinu er af stærðinni :math:`h \times h`.

Ef við köllum látum :math:`x_j` vera skiptipunktanna fyrir
:math:`[a,b]`,

.. math:: a=x_0 < x_1 < x_2 < \ldots x_{N-1} < x_N =b,

og :math:`y_k` vera skiptipunktanna fyrir :math:`[c,d]`,

.. math:: c=y_0 < y_1 < y_2 < \ldots y_{N-1} < y_M = d,

þá eru skiptipunktarnir í netinu :math:`(x_j,y_k)`.

Ritháttur
~~~~~~~~~

Við skoðum ætlum að skoða jöfnuna

.. math:: \frac{{\partial}^2 u}{{\partial}x^2} + \frac{{\partial}^2 u}{{\partial}y^2} = f(x,y),

á :math:`R = \{ (x,y) \in {\mathbb  R}^2 ; a < x < b, c < y < d \}` með
Dirichlet skilyrðin

.. math:: u(x,y) = g(x,y), \qquad \text{ á } {\partial}R.

Til að einfalda rithátt þá skrifum við

.. math::

   \begin{aligned}
    u_{j,k} &= u(x_j,y_k), \qquad j=0,\ldots,N, \quad k=0,\ldots,M,\\
    f_{j,k} &= f(x_j,y_k), \qquad j=0,\ldots,N, \quad k=0,\ldots,M,\\
    g_{j,k} &= g(x_j,y_k), \qquad j=0, j=N, k=0 \text{ eða } k=M,\end{aligned}

og nálgunargildin eru

.. math:: w_{j,k} \approx u_{j,k}.

Strjál útgáfa Poisson jöfnunar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Með því að nota miðsettan mismunakvóta fyrir aðra afleiðu :math:`u` þá
getum við skrifað

.. math::

   \begin{aligned}
     \frac{{\partial}^2 u}{{\partial}x^2}|_{x_j,y_k} &= \frac{u_{j-1,k} - 2u_{j,k} + u_{j+1,k}}{h^2}
     + O(h^2), \\
     \frac{{\partial}^2 u}{{\partial}y^2}|_{x_j,y_k} &= \frac{u_{j,k-1} - 2u_{j,k} + u_{j,k+1}}{h^2}
     + O(h^2), 
    \end{aligned}

þar sem :math:`j = 1,\ldots,N-1` og :math:`k=1,\ldots,M-1`.

Með því að setja þetta inn í

.. math:: \frac{{\partial}^2 u}{{\partial}x^2} + \frac{{\partial}^2 u}{{\partial}y^2} = f(x,y),

þá fæst,

.. math::

   \frac{u_{j-1,k} - 2u_{j,k} + u_{j+1,k}}{h^2} +
     \frac{u_{j,k-1} - 2u_{j,k} + u_{j,k+1}}{h^2}
     + O(h^2) = f_{j,k}.

Höfðum

.. math::

   \frac{u_{j-1,k} - 2u_{j,k} + u_{j+1,k}}{h^2} +
     \frac{u_{j,k-1} - 2u_{j,k} + u_{j,k+1}}{h^2}
     + O(h^2) = f_{j,k}.

Skiptum :math:`u` út fyrir nálgunargildin :math:`w_{j,k}`, hendum
skekkjuliðnum og margföldum í gegn með :math:`-h^2`, þá fæst

.. math:: -w_{j-1,k} - w_{j+1,k} - w_{j,k-1} - w_{j,k+1} + 4w_{j,k} = -h^2 f_{j,k},

fyrir :math:`j = 1,\ldots,N-1` og :math:`k=1,\ldots,M-1`.

Fjöldi jafna
~~~~~~~~~~~~

Hér á undan fengum við eina jöfnu fyrir hvern innri punkt netsins,
samtals :math:`(N-1)(M-1)` jöfnur. Þetta er fjöldi óþekktra
:math:`w_{j,k}`, því :math:`w_{j,k}` á jaðrinum eru þekkt, þar er

.. math:: w_{j,k} = g_{j,k}.

Við þurfum að því leysa jöfnuhneppið

.. math::

   \begin{aligned}
     -w_{j-1,k} - w_{j+1,k} - w_{j,k-1} - w_{j,k+1} + 4w_{j,k} &= -h^2 f_{j,k} \\ 
      \text{fyrir } j=1&,\ldots,N-1, \ \, k=1,\ldots,M-1\\
        \end{aligned}

Uppröðun á innri punktum
~~~~~~~~~~~~~~~~~~~~~~~~

Röðum í vigur :math:`\mbox{${\bf w}$}` tölunum :math:`w_{j,k}` fyrir
innri punkta netsins. Förum í gegnum netið frá vinstri til hægri, byrjum
á næst neðstu línunni og förum svo upp á við,

.. math::

   \mbox{${\bf w}$}= [ \underbrace{w_{1,1} \ w_{2,1} \ldots w_{N-1,1}}_{k=1} 
     \ \underbrace{w_{1,2} \ w_{2,2} \ldots w_{N-1,2}}_{k=2} \ 
     \underbrace{w_{1,3} \ldots  \ldots}_{k=3,\ldots,M-1} ]^T.

Fyrri vísirinn (:math:`j`) vísar til :math:`x`-hnitsins :math:`x_j` og
seinni vísirinn (:math:`k`) til :math:`y`-hnitsins :math:`y_k`.

Jöfnurnar aftur
~~~~~~~~~~~~~~~

Jöfnurnar sem við leiddum út eru

.. math:: -w_{j-1,k} - w_{j+1,k} - w_{j,k-1} - w_{j,k+1} + 4w_{j,k} = -h^2 f_{j,k}.

Ef :math:`j-1=0`, :math:`k-1 =0`, :math:`j+1=N` eða :math:`k+1=M` þá
erum við á jaðrinum og þar þekkjum við gildin, þau eru gefin með
:math:`g`.

T.d. ef :math:`j=1` og :math:`k=1` þá fæst

.. math::

   \begin{aligned}
     -h^2 f_{1,1} &= -w_{0,1} - w_{2,1} - w_{1,0} - w_{1,2} + 4w_{1,1} \\
     &= -g_{0,1} - w_{2,1} - g_{1,0} - w_{1,2} + 4w_{1,1}\\
    \end{aligned}

Það er

.. math::

   - w_{2,1} - w_{1,2} + 4w_{1,1} = 
     -h^2 f_{1,1}  + g_{0,1} + g_{1,0}.

Jöfnurnar fyrir :math:`k=1`, :math:`j=1`, :math:`k=M-1` og :math:`j=N-1`
þurfa því að taka mið af :math:`g`.

Jöfnuhneppið
~~~~~~~~~~~~

Jöfnuhneppið sem fæst er eftirfarandi

.. math:: A\mbox{${\bf w}$}= \mbox{${\bf b}$},

þar sem :math:`A` er :math:`(N-1)(M-1)\times (N-1)(M-1)` fylkið

.. math::

   A = \left[\begin{array}{cccccc}
   D & -I &   &   &   &  \\
   -I & D & -I &   &   &  \\
     & \cdot & \cdot & \cdot &   &  \\
     &   & \cdot & \cdot & \cdot &  \\
     &   &  & -I & D & -I\\
     &   &   &   & -I & D
         \end{array}\right].

Hér er :math:`I` er :math:`(N-1)\times (N-1)` einingafylkið og

.. math::

   D = \left[\begin{array}{cccccc}
   4 & -1 &   &   &   &  \\
   -1 & 4 & -1 &   &   &  \\
     & \cdot & \cdot & \cdot &   &  \\
     &   & \cdot & \cdot & \cdot &  \\
     &   &  & -1 & 4 & -1\\
     &   &   &   & -1 & 4
         \end{array}\right] \qquad ((N-1)\times (N-1) \text{ fylki}).

Hægri hliðin er gefin með summunni af :math:`-h^2 f_{j,k}` og gildunum í
þeim jaðarpunktum sem við rekumst þegar við förum gegnum innri punktanna
(í sömu röð og tilgreind var fyrir :math:`\mbox{${\bf w}$}`). Það er

Poisson jafnan í rétthyrndu svæði – Neumann- og Robin-jaðarskilyrði
-------------------------------------------------------------------

Blönduð jaðarskilyrði
~~~~~~~~~~~~~~~~~~~~~

Rifjum upp þær þrjár gerðir jaðarskilyrða sem við höfum áhuga

+--------------+------------------------------------------------------------------------------------------------------------+
| Dirichlet:   | :math:`u(x,y) = r(x,y)` á :math:`{\partial}R`.                                                             |
+--------------+------------------------------------------------------------------------------------------------------------+
| Neumann:     | :math:`\frac{{\partial}u}{{\partial}n}(x,y) = r(x,y)` á :math:`{\partial}R`.                               |
+--------------+------------------------------------------------------------------------------------------------------------+
| Robin:       | :math:`\alpha(x,y)u(x,y) + \beta(x,y)\frac{{\partial}u}{{\partial}n}(x,y) = r(x,y)` á :math:`{\partial}R`. |
+--------------+------------------------------------------------------------------------------------------------------------+

Hér er :math:`{\partial}R` jaðar svæðisins :math:`R` og :math:`n` er
útvísandi þverill fyrir :math:`{\partial}R`.

Dirichlet-skilyrði skoðuðum við í kafla 9.1.

Neumann og Robin skilyrði eru efni kafla 9.2. Aðferðin hér er sú sama og
í kafla 8.2,, við bætum við felugildum til þess að geta nálgað afleiðu
:math:`u` á jaðrinum. Þar sem jaðarinn er ferill í
:math:`{\mathbb  R}^2`, en ekki bil eins og í kafla 8, þá þarf að setja
felupunkta alls staðar þar sem afleiðan :math:`{\partial}u/{\partial}n`
er gefin. Þetta veldur því að útfærslan getur orðið nokkuð flókin,
bókarhöfundur skoðar því eingöngu ákveðin sértilvik.

Neumann skilyrði eftir botninum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skoðum svæðið

.. math:: R = \{ (x,y) \in {\mathbb  R}^2 ; a < x < b, c < y < d \}.

og tilvikið þegar jaðargildin eru gefin með falli :math:`g(x,y)` á
hliðunum (:math:`x=a` og :math:`x=b`) og toppnum (:math:`y=d`), og
afleiðan eftir botninum er gefin með

.. math:: \frac{{\partial}u}{{\partial}n} = \alpha(x)

(ath. staðsetningin þar er bara háð :math:`x`).

Útvísandi þverill eftir botninum er

.. math:: \frac{{\partial}}{{\partial}n} = -\frac{{\partial}}{{\partial}y}.

Mismunakvótar eftir botninum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum eins og áður ráð fyrir því að við höfum jafna skiptingu á bilinu
:math:`[a,b]`,

.. math:: a = x_0 < x_1 < \ldots < x_{N-1} < x_N = b,

með billlengd :math:`h`, og skiptingu á bilinu :math:`[c,d]` með sömu
billengd,

.. math:: c = y_0 < y_1 < \ldots < y_{M-1} < y_M = d.

Bætum við felupunktum :math:`(x_j,y_{-1})` fyrir :math:`j=1,\ldots,N-1`.
Samhverfir mismunakvótar fyrir :math:`\frac{{\partial}u}{{\partial}n}`
gefa þá

.. math:: - \left. \frac{{\partial}u}{{\partial}y} \right|_{x=x_j} = \alpha(x_j)

.. math:: -\frac{w_{j,1} - w_{j,-1} }{2h} \approx \alpha(x_j).

Það er

.. math:: w_{j,-1}  = w_{j,1} + 2h\alpha(x_j)

Jaðarskilyrðin sett inn í Poisson-jöfnuna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rifjum upp að lausnin okkar :math:`w_{j,k}` á :math:`\Delta u = f` á að
uppfylla

.. math::

   \begin{aligned}
    -w_{j-1,k} - w_{j+1,k} - w_{j,k-1} - w_{j,k+1} + 4w_{j,k} &= -h^2 f_{j,k} 
            \end{aligned}

Eftir botninum (:math:`k=0`, :math:`j=1,\ldots,N-1`) þýðir þetta að

.. math::

   \begin{aligned}
     - w_{2,0} - w_{1,-1} - w_{1,1} + 4w_{1,0} &= -h^2 f_{1,0} + g(0,0),\\
     -w_{j-1,0} - w_{j+1,0} - w_{j,-1} - w_{j,1} + 4w_{j,0} &= -h^2 f_{j,0}, 
     \quad {\color{gray} j=2,\ldots,N-2},\\
     -w_{N-2,0}  - w_{N-1,-1} - w_{N-1,1} + 4w_{N-1,0} &= -h^2 f_{N-1,0} + g(N,0) 
    \end{aligned}

það er

.. math::

   \begin{aligned}
   - w_{2,0}  - 2w_{1,1} + 4w_{1,0} &= -h^2 f_{1,0} + g(0,0) + 2h\alpha(x_1),\\
     -w_{j-1,0} - w_{j+1,0} - 2w_{j,1} + 4w_{j,0} &= -h^2 f_{j,0} + 2h\alpha(x_j), 
      \ \ {\color{gray} j=2,\ldots,N-2}\\
     -w_{N-2,0}  - 2w_{N-1,1} + 4w_{N-1,0} &= -h^2 f_{N-1,0} + g(N,0) + 2h\alpha(x_{N-1})
    \end{aligned}

Fjöldi jafna
~~~~~~~~~~~~

#. Dirichlet-jaðarskilyrði Fjöldi jafna í kafla 9.1 var
   :math:`(N-1)(M-1)`, það er fjöldi innri punkta því við þekktum gildin
   :math:`w_{j,k}` á jaðrinum.

#. Blönduð jaðarskilyrði Þegar við skoðum blönduð jaðarskilyrði þá
   þekkjum við ekki endilega gildi :math:`w_{j,k}` á jaðrinum og því
   erum við hugsanlega með fleiri jöfnur.

#. Blönduð jaðarskilyrði – Dæmið okkar Í þessu tilviki sem við erum að
   skoða þá bætast við jöfnur fyrir :math:`w_{j,0}`,
   :math:`j=1,\ldots,N-1`, eftir botninum. Það þýðir að jöfnuhneppið
   okkar inniheldur :math:`(N-1)M` jöfnur.

Fylkið :math:`A` er því :math:`(N-1)M \times (N-1)M`, og samanstendur af
:math:`M \times M` hlutfylkjum sem hvert um sig er
:math:`(N-1)\times (N-1)`.

Jöfnuhneppið :math:`A\mbox{${\bf w}$}= \mbox{${\bf b}$}`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Jöfnurnar fyrir :math:`k=0` voru

.. math::

   \begin{aligned}
   - w_{2,0}  - {\color{red}2}w_{1,1} + 4w_{1,0} &= -h^2 f_{1,0} + g(0,0) + 
   {\color{blue}2h\alpha(x_1)},\\
     -w_{j-1,0} - w_{j+1,0} - {\color{red}2}w_{j,1} + 4w_{j,0} &= -h^2 f_{j,0} + 
     {\color{blue}2h\alpha(x_j)}, 
      \ \ {\color{gray} j=2,\ldots,N-2}\\
     -w_{N-2,0}  - {\color{red}2}w_{N-1,1} + 4w_{N-1,0} &= -h^2 f_{N-1,0} + g(N,0) + 
     {\color{blue}2h\alpha(x_{N-1})}
    \end{aligned}

Þetta breytir fyrstu hlutfylkjalínunni í jöfnuhneppinu
:math:`A\mbox{${\bf w}$}= \mbox{${\bf b}$}`,

-  :math:`-I` í fyrsta hlutdálki verður :math:`-2I`.

-  Við efsta hluta :math:`\mbox{${\bf b}$}` (sem tilheyrir línunni
   :math:`k=0`) bætist við vigurinn

   .. math:: [2h\alpha(x_1),2h\alpha(x_2),\ldots,2h\alpha(x_{N-1})]^T.

Jöfnuhneppið sem fæst er því eftirfarandi

.. math:: A\mbox{${\bf w}$}= \mbox{${\bf b}$},

þar sem :math:`A` er :math:`(N-1)M\times (N-1)M` fylkið

.. math::

   A = \left[\begin{array}{cccccc}
   D & -2I &   &   &   &  \\
   -I & D & -I &   &   &  \\
     & \cdot & \cdot & \cdot &   &  \\
     &   & \cdot & \cdot & \cdot &  \\
     &   &  & -I & D & -I\\
     &   &   &   & -I & D
         \end{array}\right].

Hér er :math:`I` er :math:`(N-1)\times (N-1)` einingafylkið og

.. math::

   D = \left[\begin{array}{cccccc}
   4 & -1 &   &   &   &  \\
   -1 & 4 & -1 &   &   &  \\
     & \cdot & \cdot & \cdot &   &  \\
     &   & \cdot & \cdot & \cdot &  \\
     &   &  & -1 & 4 & -1\\
     &   &   &   & -1 & 4
         \end{array}\right] \qquad ((N-1)\times (N-1) \text{ fylki}).

  <presentation>

.. math::

   \begin{aligned}
     \mbox{${\bf b}$}= [ 
     &-h^2 f_{1,0} + g_{0,0} + 2h\alpha(x_1) & (\text{lína } k=0)\\
     &-h^2 f_{2,0} + 2h\alpha(x_2)  \\
     &\ldots \\
     &-h^2 f_{N-2,0} + 2h\alpha(x_{N-2}) \\
     &-h^2 f_{N-1,0} + g_{N,0} + 2h\alpha(x_{N-2}) \\
       &-h^2 f_{1,1} + g_{0,1}   & (\text{lína } k=1)\\
     &-h^2 f_{2,1} \\
     &\ldots \\
     &-h^2 f_{N-2,1}  \\
     &-h^2 f_{N-1,1} +  g_{N,1} \\
        & \ldots \ldots \ldots  & (\text{línur } k=2,\ldots,M-2)\\
     &-h^2 f_{1,M-1} + g_{1,M-1} + g_{0,M} & (\text{lína } k=M-1)\\
     &-h^2 f_{2,M-1} + g_{2,M} \\
     &\ldots \\
       &-h^2 f_{N-1,M-1} + g_{N,M-1} + g_{N-1,M} ]\\
     \end{aligned}

Fræðilegar spurningar
---------------------

#. | Hvað er átt við með því að lausn hlutafleiðujöfnu á svæði :math:`R`
   í plani uppfylli *Dirichlet-jaðarskilyrði*?
   | (Samheiti er *fallsjaðarskilyrði*.)

#. Hvernig er *útvísandi þverafleiða* :math:`\partial u/\partial n` af
   falli :math:`u` á svæði :math:`R` í plani skilgreind?

#. | Hvað er átt við með því að lausn hlutafleiðujöfnu á svæði :math:`R`
   í plani uppfylli *Neumann-jaðarskilyrði*?
   | (Samheiti eru *afleiðujaðarskilyrði* og *flæðisjaðarskilyrði*.)

#. | Hvað er átt við með því að lausn hlutafleiðujöfnu á svæði :math:`R`
   uppfylli *Robin-jaðarskilyrði*?
   | (Samheiti er *blandað jaðarskilyrði*.)

#. Hvernig er nálgunarjafna fyrir Poisson-jöfnu :math:`\Delta u=f` í
   innri skiptipunkti í ferningslaga neti í plani leidd út?

#. Hvernig eru *felupunktur* og *felugildi* notuð til þess að meðhöndla
   blandað jaðarskilyrði :math:`\alpha_1 u+\alpha_2\partial u/\partial n=\alpha_3` í jaðarpunkti svæðis :math:`R` í
   plani og hvernig verður nálgunarjafnan í þeim punkti?
