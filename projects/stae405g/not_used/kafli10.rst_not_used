Parbólskar hlutafleiðujöfnur
============================

Almenn atriði um parabólsk verkefni
-----------------------------------

Eins og í kafla 9 þá ætlum við hér að skoða annars stigs línulegar
hlutafleiðujöfnur á svæði :math:`R` í :math:`{\mathbb  R}^2`, þetta eru
jöfnur á forminu

.. math::

   \begin{gathered}
   A(x,y)\frac{{\partial}^2 u}{{\partial}x^2} + B(x,y)\frac{{\partial}^2 u}{{\partial}x{\partial}y} + C(x,y)\frac{{\partial}^2 u}{{\partial}y^2} +\\
   D(x,y)\frac{{\partial}u}{{\partial}x} + E(x,y)\frac{{\partial}u}{{\partial}y} + F(x,y)u = G(x,y).\end{gathered}

Skilgreining
~~~~~~~~~~~~

Annars stigs línuleg hlutafleiðujafna eins og að ofan kallast
*parabólsk* ef

.. math:: A(x,y)C(x,y) - B(x,y)^2 = 0,

fyrir öll :math:`(x,y) \in R`.

Við ætlum að láta aðra breytuna vera tímabreytu. Þannig fæst tímaháð
verkefni, en parabólskar jöfnur lýsa oft verkefnum þar hlutur fer úr
upphafsástandi í jafnvægisástand.

Hagnýtingar
~~~~~~~~~~~

-  Dreifing hita og styrkleiki lausna

-  Black-Scholes módelið í fjármálastærðfræði

-  Brownhreyfing

Hitajafnan
~~~~~~~~~~

Við ætlum að einskorða okkur við mikilvægasta tilvikið, *Hitajöfnuna*

.. math:: \frac{{\partial}u}{{\partial}t} =  D \Delta u,

\ í einni rúmbreytu þá þýðir þetta,

.. math:: \frac{{\partial}u}{{\partial}t} =  D\frac{{\partial}^2 u}{{\partial}x^2}.

Svæðið
~~~~~~

Þar sem við höfum aðeins eina rúmbreytu þá er svæðið sem við skoðum
einfaldlega bil :math:`[a,b]`

Jaðarskilyrði
~~~~~~~~~~~~~

Eins og fyrir sporgerar hlutafleiðujöfnur (kafli 9) þá getum við haft
þrjár gerðir af jaðarskilyrðum: Dirichlet, Neumann og Robin.

Verkefnið
~~~~~~~~~

Við munum byrja á því að skoða Dirichlet-jaðarskilyrði:

Gefin föll :math:`u_a(t)`, :math:`u_b(t)` fyrir :math:`t\geq 0` og fall
:math:`f(x)` á :math:`[a,b]` þá viljum við finna fall :math:`u(x,t)`
þannig að

-  :math:`\frac{{\partial}u}{{\partial}t} =  D \frac{{\partial}^2 u}{{\partial}x^2}`,

-  :math:`u(a,t) = u_a(t)` og :math:`u(b,t) = u_b(t)`,

-  :math:`u(x,0) = f(x)`.

Talan :math:`D` kallast dreifnistuðull.

Hitajafnan og þýð föll
~~~~~~~~~~~~~~~~~~~~~~

**Hitajafnan**

.. math:: \frac{{\partial}u}{{\partial}t} = D\  \Delta u,

**Athugasemd** Þegar hluturinn sem við erum að skoða er kominn í
jafnvægisástand þá þýðir það að
:math:`\frac{{\partial}u}{{\partial}t} = 0`. Þetta þýðir að

.. math:: 0 =  D\ \Delta u,

það er,jafnvægisástandið uppfyllir meðalgildiseiginleikann (sjá glæru
9.6).

Hitajafnan – Dirichlet-jaðarskilyrði 
-------------------------------------

Rúmbreytan gerð strjál 
~~~~~~~~~~~~~~~~~~~~~~~

Byrjum á að skipta bilinu :math:`[a,b]` í :math:`N` hlutbil, hvert um
sig með lengdina :math:`h=(b-a)/N`:

.. math:: a = x_0 < x_1 < \ldots < x_{N-1} < x_N = b.

Látum :math:`v_j(t)` vera nálgunargildið á :math:`u(x_j,t)`.

Með því að skipta annarri afleiðunni í

.. math:: \frac{{\partial}u}{{\partial}t} =  D\ \Delta u,

út fyrir samhverfan mismunakvóta þá fæst

.. math::

   \frac{d v_j(t)}{d t} =  D\  \frac{v_{j-1}(t) -2 v_j(t) + v_{j+1}(t)}{h^2}, \qquad
    \text{fyrir } j=1,\ldots,N-1.

Athugið að þetta er fyrsta stigs afleiðujafna eins og við fengumst við
í kafla 7.

Afleiðujöfnuhneppi stillt upp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Jöfnuhneppið

.. math::

   \frac{d v_j(t)}{d t} =  D\  \frac{v_{j-1}(t) -2 v_j(t) + v_{j+1}(t)}{h^2}, \qquad
    \text{fyrir } j=1,\ldots,N-1.

með upphafsskilyrðunum :math:`v_j(0) = f(x_j)`, má svo skrifa

.. math:: \frac{d \mbox{${\bf v}$}(t)}{d t} =  -\frac{D}{h^2}\  (A\mbox{${\bf v}$}(t) + \mbox{${\bf b}$}(t)), \qquad \mbox{${\bf v}$}(0)=\mbox{${\bf f}$}

þar sem

.. math::

   \begin{aligned}
     \mbox{${\bf v}$}(t) &= [v_1(t) \ v_2(t) \ \cdots \ v_{N-1}(t) ]^T\\
     \mbox{${\bf f}$}&= [ f(x_1) \ f(x_2) \ \cdots \ f(x_{N-1}) ]^T\\
     \mbox{${\bf b}$}(t) &= [ -u_a(t) \ \ 0 \ \cdots \ 0 \ \ -u_b(t) ]^T \\
     A &=  \left[\begin{array}{cccccc}
   2 & -1 &   &   &   &  \\
   -1 & 2 & -1 &   &   &  \\
     & \cdot & \cdot & \cdot &   &  \\
     &   & \cdot & \cdot & \cdot &  \\
     &   &  & -1 & 2 & -1\\
     &   &   &   & -1 & 2
         \end{array}\right]
    \end{aligned}

Tímabreytan gerð strjál
~~~~~~~~~~~~~~~~~~~~~~~

Til þess að leysa afleiðujöfnuhneppið hér á undan þá beytum við
aðferðunum úr 7. kafla. Hægt er að nota hvort sem er aðferðir með fasta
skrefastærð (aðferð Eulars, Heun og Runge-Kutta) og aðferðir með
breytilega skrefastærð (RKF45 og RKV56).

Við munum notast við fastaskrefstærð :math:`k`. Tímaskrefin eru því
:math:`t_n = n k`, fyrir :math:`n=0,1,2,\ldots,`.

Táknum nálgunargildið við :math:`v_j(t_n)` með :math:`w_j^{(n)}`, og
látum

.. math:: \mbox{${\bf w}$}^{(n)} = [w_1^{(n)}(t) \ w_2^{(n)} \ \cdots \ w_{N-1}^{(n)} ]^T.

FTCS – Fram í tíma, miðsett í rúmi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skiptum afleiðunni í

.. math:: \frac{d \mbox{${\bf v}$}(t)}{d t} =  -\frac{D}{h^2}\  (A\mbox{${\bf v}$}(t) + \mbox{${\bf b}$}(t)), \qquad \mbox{${\bf w}$}^{(0)}=\mbox{${\bf f}$}

út fyrir frammismun. Þá fæst

.. math::

   \frac{\mbox{${\bf w}$}^{(n+1)} - \mbox{${\bf w}$}^{(n)}}{ k} =  -\frac{D}{h^2}\  (A\mbox{${\bf w}$}^{(n)} + \mbox{${\bf b}$}(t_n)), 
    \qquad \mbox{${\bf w}$}^{(0)}=\mbox{${\bf f}$}.

\ Þetta er jafngilt því að heilda efstu jöfnuna frá :math:`t=t_n` upp í
:math:`t=t_{n+1}` og nálga heildið af hægri hliðinni með margfeldinu af
gildinu í vinstri endapunktinum :math:`t_n` og billengdinni :math:`k`.

Þetta er aðferð Eulers úr kafla 7.2.

Jöfnuhneppið

.. math:: \frac{\mbox{${\bf w}$}^{(n+1)} - \mbox{${\bf w}$}^{(n)}}{ k} =  -\frac{D}{h^2}\  (A\mbox{${\bf w}$}^{(n)} + \mbox{${\bf b}$}(t_n)),

má svo umrita sem

.. math::

   \begin{aligned}
    \mbox{${\bf w}$}^{(n+1)} &= \mbox{${\bf w}$}^{(n)} -\lambda A\mbox{${\bf w}$}^{(n)} - \lambda \mbox{${\bf b}$}(t_n) \\
    & = (I-\lambda A) \mbox{${\bf w}$}^{(n)} - \lambda \mbox{${\bf b}$}(t_n),\end{aligned}

þar sem :math:`\lambda = k\frac{D}{h^2}`.

Upphafsgildið :math:`\mbox{${\bf w}$}^{(0)}` er þekkt og hér er komin
rakningarformúlu fyrir lausninni.

Skekkjan
^^^^^^^^

Samhverfi mismunakvótinn í rúmbreytunni hefur skekkjuna :math:`O(h^2)`
og frammismunurinn fyrir tímabreytuna hefur skekkjuna :math:`O(k)`.
Skekkjan í þessari aðferð er því :math:`O(h^2 + k)`.

BTCS – Aftur í tíma, miðsett í rúmi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef við skiptum afleiðunni í

.. math:: \frac{d \mbox{${\bf v}$}(t)}{d t} =  -\frac{D}{h^2}\  (A\mbox{${\bf v}$}(t) + \mbox{${\bf b}$}(t)), \qquad \mbox{${\bf w}$}^{(0)}=\mbox{${\bf f}$}

út fyrir bakmismun. Þá fæst

.. math::

   \frac{\mbox{${\bf w}$}^{(n+1)} - \mbox{${\bf w}$}^{(n)}}{ k} =  -\frac{D}{h^2}\  (A\mbox{${\bf w}$}^{(n+1)} + \mbox{${\bf b}$}(t_{n+1})), 
    \qquad \mbox{${\bf w}$}^{(0)}=\mbox{${\bf f}$}.

\ Þetta er jafngilt því að heilda efstu jöfnuna frá :math:`t=t_n` upp í
:math:`t=t_{n+1}` og nálga heildið af hægri hliðinni með margfeldinu af
gildinu í hægri endapunktinum :math:`t_{n+1}` og billengdinni :math:`k`.

Jöfnuhneppið

.. math:: \frac{\mbox{${\bf w}$}^{(n+1)} - \mbox{${\bf w}$}^{(n)}}{ k} =  -\frac{D}{h^2}\  (A\mbox{${\bf w}$}^{(n+1)} + \mbox{${\bf b}$}(t_{n+1})),

má svo umrita sem

.. math::

   \begin{aligned}
    (I+\lambda A)\mbox{${\bf w}$}^{(n+1)} &= \mbox{${\bf w}$}^{(n)}  - \lambda \mbox{${\bf b}$}(t_{n+1}), \end{aligned}

þar sem :math:`\lambda = k\frac{D}{h^2}`.

Upphafsgildið :math:`\mbox{${\bf w}$}^{(0)}` er þekkt og hér er komin
önnur rakningarformúla fyrir lausninni :math:`\mbox{${\bf w}$}`.

Skekkjan
^^^^^^^^

Samhverfi mismunakvótinn í rúmbreytunni hefur skekkjuna :math:`O(h^2)`
og bakmismunurinn fyrir tímabreytuna hefur skekkjuna :math:`O(k)`.
Skekkjan í þessari aðferð er því :math:`O(h^2 + k)`.

Fjöldi aðgerða
^^^^^^^^^^^^^^

Þar sem :math:`I+\lambda A` er þríhornalínufylki þá þarf aðeins tvöfalt
fleiri aðgerðir til þess að leysa þetta jöfnuhneppi heldur en þarf til
þess að framkvæma margföldunina í FTCS-aðferðinni.

Crank-Nicolson aðferð – Aftur í tíma, miðsett í rúmi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: \frac{d \mbox{${\bf v}$}(t)}{d t} =  -\frac{D}{h^2}\  (A\mbox{${\bf v}$}(t) + \mbox{${\bf b}$}(t)),

Í bæði FTCS og BTCS þá var skekkjan sem tilheyrði tímabreytunni
:math:`O(k)`. Ef við viljum bæta þetta þá er einfaldast að nota
Trapisuregluna því skekkjan í henni er :math:`O(k^2)`.

Svo ef við heildum jöfnuna að ofan frá :math:`t=t_n` upp í
:math:`t=t_{n+1}` og nálgum heildið af hægri hliðinni með meðaltalinu af
gildunum í endapunktunum margfaldað við billengdina þá fæst

.. math::

   \mbox{${\bf w}$}^{(n+1)} - \mbox{${\bf w}$}^{(n)} =  -\frac{kD}{2h^2}\  
    \big( (A\mbox{${\bf w}$}^{(n)} + \mbox{${\bf b}$}(t_{n})) +  
    (A\mbox{${\bf w}$}^{(n+1)} + \mbox{${\bf b}$}(t_{n+1})) \big).

Jöfnuhneppið

.. math::

   \mbox{${\bf w}$}^{(n+1)} - \mbox{${\bf w}$}^{(n)} =  -\frac{kD}{2h^2}\  
    \big( (A\mbox{${\bf w}$}^{(n)} + \mbox{${\bf b}$}(t_{n})) +  
    (A\mbox{${\bf w}$}^{(n+1)} + \mbox{${\bf b}$}(t_{n+1})) \big),

má svo umrita sem

.. math::

   \begin{aligned}
    (I+\lambda A)\mbox{${\bf w}$}^{(n+1)} &= (I-\lambda A) \mbox{${\bf w}$}^{(n)}  - \lambda (\mbox{${\bf b}$}(t_{n}) 
    + \mbox{${\bf b}$}(t_{n+1})), \end{aligned}

þar sem :math:`\lambda = \frac{kD}{2h^2}`.

Upphafsgildið :math:`\mbox{${\bf w}$}^{(0)}` er þekkt og hér er því
komin þriðja rakningarformúlun fyrir lausninni :math:`\mbox{${\bf w}$}`.

Skekkjan
^^^^^^^^

Samhverfi mismunakvótinn í rúmbreytunni hefur skekkjuna :math:`O(h^2)`
og bakmismunurinn fyrir tímabreytuna hefur skekkjuna :math:`O(k^2)`.
Skekkjan í þessari aðferð er því :math:`O(h^2 + k^2)`.

Fjöldi aðgerða
^^^^^^^^^^^^^^

Fjöldi reikniaðgerða hér er u.þ.b. summan af fjölda reikniaðgerða fyrir
FTCS og BTCS.

Stöðugleiki
-----------

Lausnin sem fæst úr aðferðunum hér á undan geta verið viðkvæmar fyrir
skrefstærðinni :math:`k` sem við veljum fyrir tímabreytuna.

Rifjum upp að aðferð kallast samleitin ef að nálgunarlausnin stefnir á
réttu lausnina þegar :math:`t\to \infty`.

Skilgreining
~~~~~~~~~~~~

Við segjum að aðferð sé

-  *óskilyrt stöðug* (unconditionally stable) ef aðferðin er samleitin
   fyrir öll :math:`k`,

-  *skilyrt stöðug* (conditionally stable) ef aðferðin er samleitin
   fyrir nógu lítil :math:`k`,

-  *óskilyrt óstöðug* (unconditionally unstable) ef aðferðin er
   ósamleitin fyrir öll :math:`k`.

Stöðugleiki
~~~~~~~~~~~

Allar þrjár aðferðirnar sem við skoðuðum hér á undan er hægt að setja
fram sem

.. math:: \mbox{${\bf w}$}^{(n+1)} = E\mbox{${\bf w}$}^{(n)} + \mbox{${\bf c}$}^{(n)},

fyrir ákveðið fylki :math:`E` og vigra :math:`\mbox{${\bf c}$}^{(n)}`.

Gefið :math:`\mbox{${\bf w}$}^{(0)}`, þá þýðir þetta að

.. math::

   \begin{aligned}
     \mbox{${\bf w}$}^{(1)} &= E\mbox{${\bf w}$}^{(0)} + \mbox{${\bf c}$}^{(0)} \\
     \mbox{${\bf w}$}^{(2)} &= E\mbox{${\bf w}$}^{(1)} + \mbox{${\bf c}$}^{(1)} = E^2 \mbox{${\bf w}$}^{(0)} + (\mbox{${\bf c}$}^{(1)} + E\mbox{${\bf c}$}^{(0)}) \\
     &\vdots \\
     \mbox{${\bf w}$}^{(m)} &= E\mbox{${\bf w}$}^{(m-1)} + \mbox{${\bf c}$}^{(m-1)} = E^m \mbox{${\bf w}$}^{(0)} + \hat{\mbox{${\bf c}$}}, \\
     \end{aligned}

þar sem
:math:`\hat\mbox{${\bf c}$}= \mbox{${\bf c}$}^{(m-1)} + E\mbox{${\bf c}$}^{(m-2)} + \ldots E^{m-1} \mbox{${\bf c}$}^{(0)}`.

Til þess að aðferðin sé stöðug þá þarf :math:`\|E\| \leq 1`. Með því að
skoða eigingildi :math:`E` (bls. 819-820) þá fæst eftirfarandi
niðurstaða:

#. FTCS FTCS er skilyrt stöðug, og er stöðug ef

   .. math:: k \leq \frac{h^2}{2D}.

#. BTCS BTCS er óskilyrt stöðug.

#. Crank-Nicolson Crank-Nicolson er óskilyrt stöðug.

**Athugasemd** Þar sem Crank-Nicolson er óskilyrt stöðug, ekki mjög
tímafrek og með annars stigs skekkjulið bæði í rúm- og tímabreytunni þá
er hún vænlegasti kosturinn af aðferðunum þremur.

Almenn parabólsk verkefni
-------------------------

Hingað til höfum við bara skoðað jöfnur á forminu

.. math:: \frac{{\partial}u}{{\partial}t} = \frac{{\partial}^2 u}{{\partial}x^2}.

Nú ætlum við skoða aðeins almennari verkefni, en það eru jöfnur á
forminu

.. math:: \frac{{\partial}u}{{\partial}t} = \frac{{\partial}^2 u}{{\partial}x^2} -\beta(x,t)u + s(x,t).

Hér er lýsir :math:`s` uppspretta og :math:`-\beta(x,t)u` lýsir hrörnun
(sem er háð :math:`u`).

Uppspretta
~~~~~~~~~~

Byrjum á að bæta við uppsprettu. Verkefnið er þá að finna fall
:math:`u(x,t)` þannig að

-  :math:`\frac{{\partial}u}{{\partial}t} =  D \frac{{\partial}^2 u}{{\partial}x^2} + s(x,t)`,

-  :math:`u(a,t) = u_a(t)` og :math:`u(b,t) = u_b(t)`,

-  :math:`u(x,0) = f(x)`.

Hér er :math:`D` dreifnistuðull og :math:`u_a`, :math:`u_b`, :math:`f`
og :math:`s` eru gefin föll.

Eins og áður þá festum við jafna skiptingu á bilinu :math:`[a,b]` í
:math:`N` hlutbil, hvert um sig með lengdina :math:`h = (b-a)/N`.

Mismunajafnan í :math:`x` fyrir fast :math:`t` er þá

.. math::

   \frac{d v_j(t)}{d t} =  D\  \frac{v_{j-1}(t) -2 v_j(t) + v_{j+1}(t)}{h^2} + s(x_j,t), \qquad
    \text{fyrir } j=1,\ldots,N-1

með upphafsskilyrðunum :math:`v_j(0) = f(x_j)`. Þetta má svo skrifa sem

.. math:: \frac{d \mbox{${\bf v}$}(t)}{d t} =  -\frac{D}{h^2}\  (A\mbox{${\bf v}$}(t) + \mbox{${\bf b}$}(t)) + \mbox{${\bf s}$}(t), \qquad \mbox{${\bf v}$}(0)=\mbox{${\bf f}$}

þar sem

.. math::

   \begin{aligned}
     \mbox{${\bf v}$}(t) &= [v_1(t) \ v_2(t) \ \cdots \ v_{N-1}(t) ]^T\\
     \mbox{${\bf f}$}&= [ f(x_1) \ f(x_2) \ \cdots \ f(x_{N-1}) ]^T\\
     \mbox{${\bf s}$}(t) &= [ s(x_1,t) \ s(x_2,t) \ \cdots \ s(x_{N-1},t) ]^T\\
     \mbox{${\bf b}$}(t) &= [ -u_a(t) \ \ 0 \ \cdots \ 0 \ \ -u_b(t) ]^T \\
     A &=  \left[\begin{array}{cccccc}
   2 & -1 &   &   &   &  \\
   -1 & 2 & -1 &   &   &  \\
     & \cdot & \cdot & \cdot &   &  \\
     &   & \cdot & \cdot & \cdot &  \\
     &   &  & -1 & 2 & -1\\
     &   &   &   & -1 & 2
         \end{array}\right] 
    \end{aligned}

Uppspretta – FTCS
^^^^^^^^^^^^^^^^^

Með því að heilda jöfnuna á undan frá :math:`t=t_n` upp í
:math:`t=t_{n+1}` og nálga heildið af hægri hliðinni með margfeldinu af
gildinu í vinstri endapunktinum og tímaskrefstærðinni :math:`k` þá fæst

.. math:: \mbox{${\bf w}$}^{(n+1)} = (I-\lambda A)\mbox{${\bf w}$}^{(n)} - \lambda \mbox{${\bf b}$}^{(n)} + k\mbox{${\bf s}$}^{(n)},

þar sem :math:`\lambda = \frac{Dk}{h^2}` og :math:`w_j^{(n)}` er
nálgunargildið á :math:`v_j(t_n)`.

Þetta sambærilegt við útleiðsluna á FTCS í kafla 10.1.

Uppspretta – BTCS
^^^^^^^^^^^^^^^^^

Með því að heilda jöfnuna á undan frá :math:`t=t_n` upp í
:math:`t=t_{n+1}` og nálga heildið af hægri hliðinni með margfeldinu af
gildinu í hægri endapunktinum og tímaskrefstærðinni :math:`k` þá fæst

.. math:: (I+\lambda A)\mbox{${\bf w}$}^{(n+1)} = \mbox{${\bf w}$}^{(n)} - \lambda \mbox{${\bf b}$}^{(n+1)} + k\mbox{${\bf s}$}^{(n+1)},

þar sem :math:`\lambda = \frac{Dk}{h^2}`.

Þetta sambærilegt við útleiðsluna á BTCS í kafla 10.1.

Uppspretta – Crank-Nicolson
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Með því að heilda jöfnuna á undan frá :math:`t=t_n` upp í
:math:`t=t_{n+1}` og nálga heildið af hægri hliðinni með trapisureglunni
þá fæst

.. math::

   (I+\lambda A)\mbox{${\bf w}$}^{(n+1)} = (I-\lambda A)\mbox{${\bf w}$}^{(n)} 
        - \lambda (\mbox{${\bf b}$}^{(n)}+\mbox{${\bf b}$}^{(n+1)}) + \frac k2(\mbox{${\bf s}$}^{(n)}+\mbox{${\bf s}$}^{(n+1)}),

þar sem :math:`\lambda = \frac{Dk}{2h^2}`.

Þetta sambærilegt við útleiðsluna á Crank-Nicolson í kafla 10.1.

Athugasemd um stöðugleika
~~~~~~~~~~~~~~~~~~~~~~~~~

Fylkið í rakningarformúlan í aðferðunum hér á undan eru þau sömu og í
kafla 10.1. Þetta þýðir að :math:`s` hefur engin áhrif á stöðugleika
aðferðanna.

Við höfum því eins og áður að FTCS er skilyrt stöðug, en fyrir hana þá
þarf :math:`\lambda < \frac 12`, en bæði BTCS og Crank-Nicolson eru
óskilyrt stöðugar.

Uppspretta og hrörnun
~~~~~~~~~~~~~~~~~~~~~

Bætum nú einnig við hrörnunarlið :math:`\beta(x,t)u`. Verkefnið er þá að
finna fall :math:`u(x,t)` þannig að

-  :math:`\frac{{\partial}u}{{\partial}t} =  D \frac{{\partial}^2 u}{{\partial}x^2} + s(x,t) - \beta(x,t)u`,

-  :math:`u(a,t) = u_a(t)` og :math:`u(b,t) = u_b(t)`,

-  :math:`u(x,0) = f(x)`.

Hér er :math:`D` dreifnistuðull og :math:`u_a`, :math:`u_b`, :math:`f`,
:math:`s` og :math:`\beta` eru gefin föll.

Mismunajafnan í :math:`x` fyrir fast :math:`t` er þá

.. math::

   \frac{d v_j(t)}{d t} =  D\  \frac{v_{j-1}(t) -2 v_j(t) + v_{j+1}(t)}{h^2} + 
    s(x_j,t) - \beta(x_j,t)v_j(t)

með upphafsskilyrðunum :math:`v_j(0) = f(x_j)`. Þetta má svo skrifa sem

.. math::

   \frac{d \mbox{${\bf v}$}(t)}{d t} =  -\frac{D}{h^2}\  (A\mbox{${\bf v}$}(t) + \mbox{${\bf b}$}(t)) 
    -B(t)\mbox{${\bf v}$}(t) + \mbox{${\bf s}$}(t), \qquad \mbox{${\bf v}$}(0)=\mbox{${\bf f}$}

þar sem :math:`B(t)` er hornalínufylkið með
:math:`\beta(x_1,t), \beta(x_2,t),\ldots,\beta(x_{N-1},t)` á
hornalínunni, og :math:`\mbox{${\bf v}$}(t)`, :math:`\mbox{${\bf f}$}`,
:math:`\mbox{${\bf s}$}(t)`, :math:`\mbox{${\bf b}$}(t)` og :math:`A`
eru eins og áður.

Með sömu aðferðum og áður við að nálga heildið frá :math:`t=t_n` upp í
:math:`t=t_{n+1}` fást svo eftirfarandi rakningarformúlur.

#. FTCS

   .. math::

      \mbox{${\bf w}$}^{(n+1)} = (I-\lambda A - kB^{(n)})\mbox{${\bf w}$}^{(n)} 
           - \lambda \mbox{${\bf b}$}^{(n)} + k\mbox{${\bf s}$}^{(n)}.

#. BTCS

   .. math::

      (I+\lambda A + kB^{(n+1)})\mbox{${\bf w}$}^{(n+1)} = \mbox{${\bf w}$}^{(n)} 
           - \lambda \mbox{${\bf b}$}^{(n+1)} + k\mbox{${\bf s}$}^{(n+1)}.

#. Crank-Nicolson

   .. math::

      \begin{aligned}
           (I+\lambda A + kB^{(n)})\mbox{${\bf w}$}^{(n+1)}  = &
           (I-\lambda A - kB^{(n)})\mbox{${\bf w}$}^{(n)}\\ 
           & - \lambda (\mbox{${\bf b}$}^{(n)}+\mbox{${\bf b}$}^{(n+1)}) + \frac k2(\mbox{${\bf s}$}^{(n)}+\mbox{${\bf s}$}^{(n+1)}).
          \end{aligned}

Uppspretta og hrörnun – Athugasemdir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :math:`\lambda` Fyrir FTCS og BTCS þá er
   :math:`\lambda = \frac{Dk}{h^2}`, en í Crank-Nicolson aðferðinni þá
   er :math:`\lambda = \frac{Dk}{2h^2}`.

-  Stöðugleiki Hér hefur :math:`\beta` áhrif á fylkin í
   rakningarformúlunum þannig að við getum ekki fullyrt að stöðugleiki
   aðferðanna sé sami og áður, en við förum ekki nánar út í þá sálma
   hér.

Blönduð jaðarskilyrði
---------------------

Næst skulum við skoða hvað gerist þegar við höfum Neumann eða Robin
jaðarskilyrði á jöðrunum :math:`x=a` og :math:`x=b`.

Aðferðin er sú sama og við notuðum í kafla 8 og kafla 9, við bætum við
felupunktum til þess að geta nálga afleiðurnar á jaðrinum.

Við ætlum eingöngu að skoða einfalt tilvik, það er þegar við höfum
Dirichlet skilyrði í :math:`x=b` og Neumann skilyrði í :math:`x=a`.
Aðferðin við önnur tilvik er sú sama.

Verkefnið
~~~~~~~~~

Verkefnið er þá að finna fall :math:`u(x,t)` þannig að

-  :math:`\frac{{\partial}u}{{\partial}t} =  D \frac{{\partial}^2 u}{{\partial}x^2} + s(x,t) - \beta(x,t)u`,

-  :math:`\frac{{\partial}u}{{\partial}n}|_{(a,t)} = \alpha(t)`,

-  :math:`u(b,t) = u_b(t)`,

-  :math:`u(x,0) = f(x)`.

Hér er :math:`D` dreifnistuðull og :math:`u_a`, :math:`u_b`, :math:`f`,
:math:`s`, :math:`\beta` og :math:`\alpha` eru gefin föll.

Neumann jaðarskilyrði
~~~~~~~~~~~~~~~~~~~~~

Fyrir fast :math:`t` þá gefa skilyrðin
:math:`\frac{{\partial}u}{{\partial}n}|_{(a,t)} = \alpha(t)` að

.. math:: -\frac{v_1(t) - v_{-1}(t)}{2h} = \alpha(t),

það er :math:`v_{-1} = 2h\alpha(t) + v_1(t)`.

Jafnan fyrir :math:`v_0(t)` verður þá

.. math::

   \begin{aligned}
    \frac{d v_0(t)}{d t} 
    &= D\  \frac{v_{-1}(t) -2 v_0(t) + v_{1}(t)}{h^2} + s(a,t) - \beta(a,t)v_0(t) \\
    &= D\  \frac{-2 v_0(t) + 2v_{1}(t) + 2h\alpha(t) }{h^2} + s(a,t) - \beta(a,t)v_0(t) 
    \end{aligned}

En jöfnurnar fyrir :math:`v_1,\ldots,v_{N-1}` eru óbreyttar.

Jöfnuhneppið
~~~~~~~~~~~~

Jöfnurnar fyrir fast :math:`t` er því hægt að skrifa

.. math::

   \frac{d \mbox{${\bf v}$}(t)}{d t} =  -\frac{D}{h^2}\  (A'\mbox{${\bf v}$}(t) + \mbox{${\bf b}$}'(t)) 
    -B'(t)\mbox{${\bf v}$}(t) + \mbox{${\bf s}$}'(t), \qquad \mbox{${\bf v}$}(0)=\mbox{${\bf f}$}'

þar sem

.. math::

   \begin{aligned}
     \mbox{${\bf v}$}(t) &= [v_0(t) \ v_1(t) \ v_2(t) \ \cdots \ v_{N-1}(t) ]^T\\
     \mbox{${\bf f}$}' &= [ f(x_0) \ f(x_1) \ f(x_2) \ \cdots \ f(x_{N-1}) ]^T\\
     \mbox{${\bf s}$}'(t) &= [ s(x_0,t) \ s(x_1,t) \ s(x_2,t) \ \cdots \ s(x_{N-1},t) ]^T\\
     \mbox{${\bf b}$}'(t) &= [ -2h\alpha(t) \ \ 0 \ \cdots \ 0 \ \ -u_b(t) ]^T \\
     B'(t) &= diag(\beta(x_0,t)\ \beta(x_1,t) \ \cdots \ \beta(x_{N-1},t) )\\
     A' &=  \left[\begin{array}{cccccc}
   2 & -2 &   &   &   &  \\
   -1 & 2 & -1 &   &   &  \\
     & \cdot & \cdot & \cdot &   &  \\
     &   & \cdot & \cdot & \cdot &  \\
     &   &  & -1 & 2 & -1\\
     &   &   &   & -1 & 2
         \end{array}\right] 
    \end{aligned}

Athugið að núna eru jöfnurnar :math:`N+1` en ekki :math:`N` eins og
áður, þar sem fyrsta :math:`x`-hnitið sem við þurfum að skoða er
:math:`x_0=a`.

Rakningarformúlan
~~~~~~~~~~~~~~~~~

Með sömu aðferðum og áður við að nálga heildið frá :math:`t=t_n` upp í
:math:`t=t_{n+1}` fást svo eftirfarandi rakningarformúlur.

#. FTCS

   .. math::

      \mbox{${\bf w}$}^{(n+1)} = (I-\lambda A' - kB'^{(n)})\mbox{${\bf w}$}^{(n)} 
           - \lambda \mbox{${\bf b}$}'^{(n)} + k\mbox{${\bf s}$}'^{(n)}.

#. BTCS

   .. math::

      (I+\lambda A' + kB'^{(n+1)})\mbox{${\bf w}$}^{(n+1)} = \mbox{${\bf w}$}^{(n)} 
           - \lambda \mbox{${\bf b}$}'^{(n+1)} + k\mbox{${\bf s}$}'^{(n+1)}.

#. Crank-Nicolson

   .. math::

      \begin{aligned}
           (I+\lambda A' + kB'^{(n)})\mbox{${\bf w}$}^{(n+1)}  = &
           (I-\lambda A' - kB'^{(n)})\mbox{${\bf w}$}^{(n)}\\ 
           & - \lambda (\mbox{${\bf b}$}'^{(n)}+\mbox{${\bf b}$}'^{(n+1)}) + \frac k2(\mbox{${\bf s}$}'^{(n)}+\mbox{${\bf s}$}'^{(n+1)}).
          \end{aligned}

Fræðilegar spurningar
---------------------

#. Sýnið að hitajafnan er parabólsk.

#. Hvernig er jafnvægisástand fyrir hitajöfnuna í einni rúmbreytu, ef
   :math:`s=0` og :math:`\beta=0`?

#. Hvernig er jafnvægisástand fyrir hitajöfnuna í einni rúmbreytu, ef
   :math:`\beta=0`?

#. Hver er munurinn á stöðugleika FTCS, BTCS og Crank-Nicolson
   aðferðanna?

#. Hver eru felupunktarnir staðsettir ef við höfum Neumann jaðarskilyrði
   vinstra megin, þ.e. í :math:`x=a`?

#. Hver eru felupunktarnir staðsettir ef við höfum Robin jaðarskilyrði
   hægra megin, þ.e. í :math:`x=b`?

#. Hvernig er nálgunarjafna fyrir lausn á
   :math:`\frac{{\partial}u}{{\partial}t}=\frac{{\partial}^2 u}{{\partial}x^2}`
   fyrir fast :math:`t` leidd út?
