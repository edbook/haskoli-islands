Upphafs- og jaðargildisverkefni fyrir breiðgerar (e. hyperbolic) hlutafleiðujöfnur
==================================================================================

Flutningur, dreifni og bylgjur
------------------------------

Við ætlum nú að fjalla um jöfnur úr flokki *breiðgerra* (e. hyperbolic)
hlutafleiðujafna. Við fylgjum greinum 11.1-3 í kennslubókinni í
umfjöllun okkar um þetta efni.

Við ætlum ekki að skilgreina flokk breiðgerra hlutafleiðujafna, en í
honum eru jöfnur sem lýsa flutningi efna í lofti og vökva og
bylgjujöfnur.

Þessar jöfnur eru almennt settar fram fyrir allar rúmvíddir, en við
munum einungis líta á jöfnur í einni rúmvídd.

Nokkur mikilvæg dæmi um fyrirbæri sem lýst er með jöfnum með einni
rúmvídd :

#. Efni rennur út í á og berst með straumnum.

#. Efni smitast í grunnvatn og flyst með grunnvatnsstraumi.

#. Reykjarstrók slær niður og hann berst undan vindi.

#. Úthafsalda fellur að langri strönd.

#. Sveiflur í fiðlustreng

#. Hljóðbylgjur í orgelpípu

Fróðleikur á Wikipedia
~~~~~~~~~~~~~~~~~~~~~~

Það er til fullt af útleiðslum á Wikipedia á einstökum jöfnum og þar eru
einnig niðustöður úteikninga settar fram með hreyfimyndum.

#. Bygjujafnan fyrir streng (e. vibrating string)

#. Flutnings-og-dreifnijafna (e. Convection–diffusion equation)

#. Bylgjujafna á grunnu vatni (e. shallow water equations).

#. Flóðbylgja við strönd (e. tsunami). Skoðið vel hreyfimyndirnar neðst
   í greininni.

10.0 Nokkur dæmi
~~~~~~~~~~~~~~~~

*Flutningsjafna:*

.. math::

   \dfrac{\partial u}{\partial t}
   +a(x,t,u)\dfrac{\partial u}{\partial x}=g(x,t,u).

*Flutnings-og-dreifnijafna:*

.. math::

   \dfrac{\partial u}{\partial t}
   +v(x,t)\dfrac{\partial u}{\partial x}=D
   \dfrac{\partial^2 u}{\partial x^2}.

 *Bylgjujafna:*

.. math::

   \dfrac{\partial^2 u}{\partial t^2}
   -c^2\dfrac{\partial^2 u}{\partial x^2}=0.

Í öllum þessum jöfnum er :math:`u=u(x,t)` fall af tveimur breytistærðum
þar sem við hugsum okkur að :math:`t` standi fyrir tíma.

Kennilínur (e. characteristics)
-------------------------------

Lítum á einföldu flutningsjöfnuna

.. math::

   \dfrac{\partial u}{\partial t}
   +a(x,t)\dfrac{\partial u}{\partial x}=g(x,t).

sem hefur lausnina :math:`u=u(x,t)`.

Takið eftir að við gerum ráð fyrir að föllin :math:`a` og :math:`g` séu
einungis háð :math:`(x,t)` en ekki :math:`u`.

Nú festum við einn punkt :math:`(x,t)` og lítum nú á lausn
:math:`\xi(\tau)` á upphafsgildisverkefninu

.. math:: \dfrac{d\xi}{d\tau}=a(\xi,\tau), \qquad \xi(t)=x.

Þessi jafna hefur ótvírætt ákvarðaða lausn og hún er skilgreind á opnu
bili sem inniheldur :math:`t`. Við höfum þar

.. math::

   \dfrac{d\xi}{d\tau}(\tau)= a(\xi(\tau),\tau), \qquad \tau \in I,
   \quad \text{ og } \quad \xi(t)=x.

Ferillinn :math:`\tau\mapsto (\xi(\tau), \tau)` með :math:`\xi(t)=x`
nefnist *kennilína* hlutafleiðujöfnunnar

.. math::

   \dfrac{\partial u}{\partial t}
   +a(x,t)\dfrac{\partial u}{\partial x}=g(x,t).

Ef við notfærum við okkur að fallið :math:`u(x,t)` uppfyllir þessa
jöfnu, þá gefur keðjuregla

.. math::

   \begin{aligned}
   \dfrac {d}{d\tau} u(\xi(\tau),\tau)&= 
   \dfrac{\partial u}{\partial x}(\xi(\tau),\tau) 
   \dfrac{d\xi}{d\tau}(\tau)+
   \dfrac{\partial u}{\partial t}(\xi(\tau),\tau)\\
   &=\dfrac{\partial u}{\partial t}(\xi(\tau),\tau)
   +a(\xi(\tau),\tau)
   \dfrac{\partial u}{\partial x}(\xi(\tau),\tau) \\
   &=g(\xi(\tau),\tau)  \end{aligned}

Ef bilið :math:`I` inniheldur punktinn :math:`\tau=0`, þá getum við
heildað síðustu jöfnu yfir bilið :math:`[0,t]` og þá fáum við

.. math:: u(x,t)=u(\xi(0),0)+\int_0^tg(\xi(\tau),\tau)\, d\tau.

Þessi jafna segir okkur að gildi lausnarinnar :math:`u` í punktinum
:math:`(x,t)` ræðst af gildi hennar í skurðpunkti kennilínunnar við
:math:`x`-ásinn, sem er sama og línan :math:`t=0`, og af heildi fallsins
:math:`g` yfir kennilínuna frá punktinum :math:`(\xi(0),0)` til
punktsins :math:`(x,t)`.

Almenna tilfellið
~~~~~~~~~~~~~~~~~

Lítum aftur á einföldu flutningsjöfnuna

.. math::

   \dfrac{\partial u}{\partial t}
   +a(x,t,u)\dfrac{\partial u}{\partial x}=g(x,t,u).

sem hefur lausnina :math:`u=u(x,t)`. Nú gerum við ráð fyrir að föllin
:math:`a` og :math:`g` séu háð öllum þremur breytunum :math:`(x,t,u)`.

Nú festum við einn punkt :math:`(x,t,u(x,t))` á grafi fallsins :math:`u`
og lítum á lausnina á upphafsgildisverkefninu

.. math:: \dfrac{d\xi}{d\tau}=a(\xi,\tau,u(\xi(\tau),\tau)), \qquad \xi(t)=x.

Þessi jafna hefur ótvírætt ákvarðaða lausn og hún er skilgreind á opnu
bili sem inniheldur :math:`t`.

Setjum nú :math:`v(\tau)=u(\xi(\tau),\tau)` og munum að fallið :math:`u`
er lausn hlutafleiðujöfnunnar

.. math::

   \dfrac{\partial u}{\partial t}
   +a(x,t,u)\dfrac{\partial u}{\partial x}=g(x,t,u).

Nú fáum við með sama hætti og áður að

.. math::

   \begin{aligned}
   \dfrac{dv}{d\tau}&=\dfrac {d}{d\tau} u(\xi(\tau),\tau)= 
   \dfrac{\partial u}{\partial x}(\xi(\tau),\tau) 
   \dfrac{d\xi}{d\tau}(\tau)+
   \dfrac{\partial u}{\partial t}(\xi(\tau),\tau)\\
   &=\dfrac{\partial u}{\partial t}(\xi(\tau),\tau)
   +a(\xi(\tau),\tau,v(\tau))
   \dfrac{\partial u}{\partial x}(\xi(\tau),\tau) \\
   &=g(\xi(\tau),\tau,v(\tau))  \end{aligned}

Ef bilið :math:`I` inniheldur punktinn :math:`\tau=0`, þá getum við
heildað síðustu jöfnu yfir bilið :math:`[0,t]` og þá fáum við

.. math:: u(x,t)=u(\xi(0),0)+\int_0^tg(\xi(\tau),\tau,v(\tau))\, d\tau.

Ferillinn :math:`\tau\mapsto (\xi(\tau),\tau,v(\tau))` þar sem

.. math::

   \begin{cases}
     \dfrac{d\xi}{d\tau}=a(\xi(\tau),\tau,v(\tau)),&\qquad \xi(t)=x,\\
   \dfrac{dv}{d\tau}=g(\xi(\tau),\tau,v(\tau)),& \qquad v(t)=u(x,t),
   \end{cases}

nefnist kennlína afleiðujöfnunnar gegnum punktinn :math:`(x,t,u(x,t))`

Kennilínan liggur í grafi lausnarinnar :math:`u` og gildi hennar í
punktinum :math:`(x,t)` ræðst af gildi hennar í skurðpunkti
kennilínunnar við planið :math:`t=0` í :math:`(x,t,u)`-hnitarúminu, en
það er punkturinn :math:`(\xi(0),0,u(\xi(0),0))`, og heildi :math:`g`
yfir kennilínuna frá þessum skurðpunkti til :math:`(x,t,u(x,t))`.

Flutningsjafna – Skipting á :math:`xt`-planinu
----------------------------------------------

Við innleiðum jafna skiptingu á :math:`xt`-planinu með því að taka
viðmiðunarpunkt :math:`a\in {\mathbb  R}`, látum :math:`\Delta x` tákna
billengdina í :math:`x`-skiptingunni og :math:`\Delta t` billengdina í
:math:`t`-skiptingunni. Skiptinpunktarnir eru :math:`x_j=a+j\, \Delta x`
og :math:`t_n=n\, \Delta t` Tölurnar :math:`j` og :math:`n` mega vera
hvaða heiltölur sem er.

Við ætlum að nálga lausnir :math:`u(x,t)` á flutnings-og-dreifnijöfnum
og bylgjujöfnum í punktunum :math:`(x_j,t_n)`. Við innleiðum því
nálgunargildin

.. math::

   \begin{gathered}
   w_j^{(n)}\approx u(x_j,t_n)=u_j^{(n)}, \quad
   a_j^{(n)}=a(x_j,t_n,w_j^{(n)}), \quad \\
   g_j^{(n)}=g(x_j,t_n,w_j^{(n)}), o.s.frv. \end{gathered}

Mismunakvótar fyrir flutningsjöfnu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lítum nú aftur á flutningsjöfnuna

.. math::

   \dfrac{\partial u}{\partial t}
   +a(x,t,u)\dfrac{\partial u}{\partial x}=g(x,t,u).

Hún jafngildir því að í sérhverjum punkti :math:`(x,t)` gildir

.. math::

   \begin{gathered}
   \dfrac{u(x,t+\Delta t)-u(x,t)}{\Delta t} +O(\Delta  t)\\
   +a(x,t,u)\dfrac{u(x,t)-u(x-\Delta x,t)}{\Delta x}+O(\Delta x)
   =g(x,t,u) \end{gathered}

ef við notum bakmismunakvóta til þess að reikna út :math:`\partial
u/\partial x` og ...

.. math::

   \begin{gathered}
   \dfrac{u(x,t+\Delta t)-u(x,t)}{\Delta t} +O(\Delta  t)\\
   +a(x,t,u)\dfrac{u(x+\Delta x,t)-u(x,t)}{\Delta x}+O(\Delta x)
   =g(x,t,u) \end{gathered}

ef við notum frammismunakvóta til þess að reikna út :math:`\partial
u/\partial x`.

Ef við setjum :math:`(x,t)=(x_j,t_n)`, þá jafngildir fyrri jafnan

.. math::

   u_j^{(n+1)}-u_j^{(n)}+O((\Delta t)^2)
   +a_j^{(n)}\dfrac{\Delta t}{\Delta
     x}\big(u_j^{(n)}-u_{j-1}^{(n)}\big)+\Delta tO(\Delta x)=\Delta
   t\, g_j^{(n)}

Nú skilgreinum við :math:`\lambda=a_j^{(n)}{\Delta t}/{\Delta x}` og
innleiðum nálgunarjöfnu með því að setja :math:`w_j^{(n)}` í stað
:math:`u_j^{(n)}` og fella niður leifarliðinn.

Nálgunarjafna fyrir flutningsjöfnu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   w_j^{(n+1)}-w_j^{(n)}
   +\lambda \big(w_j^{(n)}-w_{j-1}^{(n)}\big)=\Delta t\, g_j^{(n)}

Það er eðlilegra að setja þetta mismunasamnband fram sem rakningu fram í
tíma, frá :math:`t_n` til :math:`t_{n+1}=t_n+\Delta t`,

.. math::

   w_j^{(n+1)}=(1-\lambda) w_j^{(n)}+\lambda w_{j-1}^{(n)}+\Delta
   t\, g_j^{(n)}.

 Ef við notum frammismunakvóta til þess að reikna út
:math:`\partial u/\partial x` í stað bakmismunakvóta, þá fáum við í
staðinn rakningarformúluna

.. math::

   w_j^{(n+1)}=(1+\lambda) w_j^{(n)}-\lambda w_{j+1}^{(n)}+\Delta
   t\, g_j^{(n)}.

Uppstreymismismunaaðferð (e. upwind finite difference)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reikniritið sem út úr þessu kemur er

.. math::

   w_j^{(n+1)}=
   \begin{cases} 
   (1-\lambda) w_j^{(n)}+\lambda w_{j-1}^{(n)}+\Delta
   t\, g_j^{(n)},&a_j^{(n)}>0,\\
   (1+\lambda) w_j^{(n)}-\lambda w_{j+1}^{(n)}+\Delta
   t\, g_j^{(n)},&a_j^{(n)}<0.
   \end{cases}

Valið milli :math:`a_j^{(n)}>0` og :math:`a_j^{(n)}<0` er útskýrt út frá
kennilínunum.

Ef :math:`a_j^{(n)}>0`, þá fer kennilínan gegnum :math:`(x,t+\Delta t)`
frá vinstri til hægri í :math:`xt`-planinu. Ef :math:`\xi` er stikun á
henni, þá fáum við

.. math::

   u(x,t+\Delta t)=u(\xi(t),t)+\int_t^{t+\Delta t}
   g(\xi(\tau),\tau,v(\tau))\, d\tau.

Punkturinn :math:`\xi(t)` er vinstra megin við :math:`x` og því er
eðlilegt að taka bakmismun í þessu tilfelli. Ef :math:`a_j^{(n)}<0` þá
væri :math:`\xi(t)` hægra megin við :math:`x` og þá væri eðlilegra að
taka frammismun.

1. tilbrigði
^^^^^^^^^^^^

Lítum nú aftur á flutningsjöfnuna

.. math::

   \dfrac{\partial u}{\partial t}
   +a(x,t,u)\dfrac{\partial u}{\partial x}=g(x,t,u).

Afbrigði af þessari jöfnu er þegar :math:`a=a(x,t)` er óháð :math:`u` og
við höfum

.. math::

   \dfrac{\partial u}{\partial t}
   +\dfrac{\partial (au)}{\partial x}=g(x,t,u).

Reikniritið sem við fáum í þessu tilfelli er

.. math::

   w_j^{(n+1)}=
   \begin{cases} 
   w_j^{(n)}+\dfrac{\Delta t}{\Delta x} 
   \big(a_{j-1}^{(n)}w_{j-1}^{(n)}-a_j^{(n)}w_j^{(n)}\big)
   +\Delta t\, g_j^{(n)},&a_j^{(n)}>0,\\
   w_j^{(n)}+\dfrac{\Delta t}{\Delta x} 
   \big(a_{j}^{(n)}w_{j}^{(n)}-a_{j+1}^{(n)}w_{j+1}^{(n)}\big)
   +\Delta t\, g_j^{(n)}, &a_j^{(n)}<0.
   \end{cases}

2. afbrigði 
^^^^^^^^^^^^

Sum varðveislulögmál eru sett fram með jöfnu

.. math::

   \dfrac{\partial u}{\partial t}
   +\dfrac{\partial f(u)}{\partial x}=g(x,t,u).

Reikniritið sem við fáum í þessu tilfelli er

.. math::

   w_j^{(n+1)}=
   \begin{cases} 
   w_j^{(n)}+\dfrac{\Delta t}{\Delta x} 
   \big(f(w_{j-1}^{(n)})-f(w_j^{(n)})\big)
   +\Delta t\, g_j^{(n)},& \dfrac{\partial f}{\partial u}(w_j^{n})>0,\\
   w_j^{(n)}+\dfrac{\Delta t}{\Delta x} 
   \big(f(w_{j}^{(n)})-f(w_{j+1}^{(n)})\big)
   +\Delta t\, g_j^{(n)}, &\dfrac{\partial f}{\partial u}(w_j^{n})<0.
   \end{cases}

Flutningsjafna – MacCormack-aðferð
----------------------------------

Kostur við uppstreymiaðferðir er að þær byggja á kennilínuaðferðinni, en
hún er notuð til þess að sýna fræðilega fram á að afleiðujafnan hafi
lausn.

Ókostur er að hún er ekki nákvæm, aðeins með fyrsta stigs staðarskekkju,
og að erfitt er að fá hana til þess að virka fyrir hneppi.

Við lítum aftur á fyrstu flutningsjöfnuna okkar

.. math::

   \dfrac{\partial u}{\partial t}
   +a(x,t,u)\dfrac{\partial u}{\partial x}=g(x,t,u).

Við ætlum nú að reikna út nálgunargildið :math:`w_j^{n+1}` í tveimur
skrefum *forsagnarskrefi* og *leiðréttingarskrefi*. Við táknum gildið
sem út kemur eftir forsagnarskrefið með :math:`w_j^*`.

Forsagnarskref
~~~~~~~~~~~~~~

.. math::

   \dfrac{w_j^*-w_j^{(n)}}{\Delta t} 
   +a_j^{(n)}\dfrac{w_{j+1}^{(n)}-w_j^{(n)}}{\Delta x}=g_j^{(n)}

sem gefur okkur

.. math:: w_j^*=(1+\lambda) w_j^{(n)}-\lambda w_{j+1}^{(n)}+\Delta t\, g_j^{(n)},

þar sem :math:`\lambda=a_j^{(n)}\Delta t/\Delta x`.

Leiðréttingarskref
~~~~~~~~~~~~~~~~~~

.. math::

   \dfrac{w_j^{(n+1)}-w_j^{(n)}}{\Delta t}
   +\dfrac 12\bigg(a_j^{(n)}\dfrac{w_{j+1}^{(n)}-w_j^{(n)}}{\Delta x}
   +a_j^*\dfrac{w_j^*-w_{j-1}^*}{\Delta x}\bigg)
   =\dfrac  12\big(g_j^{(n)}+g_j^*\big)

þar sem :math:`a_j^*` er gildi fallsins :math:`a(x,t,u)` í punktinum
:math:`(x_j,t_n,w_j^*)` og :math:`g_j^*` er skilgreint með hliðstæðum
hætti.

Fyrri mismunakvótinn innan stóru sviganna kom fyrir í forsagnarskrefinu.
Með því að nýta okkur það fáum við með smá reikningum að

.. math::

   w_j^{(n+1)}=\tfrac 12
   \big(w_j^{(n)}+w_j^*-\lambda^*(w_j^*-w_{j-1}^*)\big)
   +\tfrac 12 \Delta t\, g_j^*,

þar sem :math:`\lambda^*=a_j^*\Delta t/\Delta x`.

1. tilbrigði
~~~~~~~~~~~~

Við getum sett upp sams konar mismunakvóta fyrir

.. math::

   \dfrac{\partial u}{\partial t}
   +\dfrac{\partial (au)}{\partial x}=g(x,t,u).

og leyfum nú fallinu :math:`a=a(x,t,u)`

.. math::

   w_j^*=w_j^{(n)}-\dfrac{\Delta t}{\Delta x}\big( 
   a_{j+1}^{(n)}w_{j+1}^{(n)}-a_j^{(n)}w_j^{(n)}\big)+\Delta t\, g_j^{(n)}.

.. math::

   w_j^{(n+1)}=\tfrac 12\big(w_j^{(n)} +w_j^*-\dfrac{\Delta t}{\Delta x}
   \big(a_j^*w_j^*-a_{j-1}^*w_{j-1}^*\big) \big)+\tfrac 12 \Delta t\, g_j^*

2. tilbrigði
~~~~~~~~~~~~

Við getum sett upp sams konar mismunakvóta fyrir

.. math::

   \dfrac{\partial u}{\partial t}
   +\dfrac{\partial f(x,t,u)}{\partial x}=g(x,t,u).

.. math::

   w_j^*=w_j^{(n)}-\dfrac{\Delta t}{\Delta x}\big( 
   f_{j+1}^{(n)}-f_j^{(n)}\big)+\Delta t\, g_j^{(n)}.

.. math::

   w_j^{(n+1)}=\tfrac 12\big(w_j^{(n)} +w_j^*-\dfrac{\Delta t}{\Delta x}
   \big(f_j^*-f_{j-1}^*\big) \big)+\tfrac 12 \Delta t\, g_j^*

MacCormack-aðferð fyrir hneppi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef hneppið er sett fram með formúlunni

.. math::

   \dfrac{\partial \mbox{${\bf U}$}}{\partial t}
   +\dfrac{\partial \mbox{${\bf F}$}(x,t,\mbox{${\bf U}$})}{\partial x}=\mbox{${\bf G}$}(x,t,\mbox{${\bf U}$}).

þar sem :math:`\mbox{${\bf U}$}=[u_1,\dots,u_m]`,
:math:`\mbox{${\bf F}$}=[f_1,\dots,f_m]`,
:math:`\mbox{${\bf G}$}=[g_1,\dots,g_m]`, með :math:`u_k=u_k(x,t)`
:math:`f_k=f_k(x,t,\mbox{${\bf U}$})` og
:math:`g_k=g_k(x,t,\mbox{${\bf U}$})`, og deildað er hnit fyrir hnit, þá
fæst:

.. math::

   \mbox{${\bf w}$}_j^*=\mbox{${\bf w}$}_j^{(n)}-\dfrac{\Delta t}{\Delta x}\big( 
   \mbox{${\bf F}$}_{j+1}^{(n)}-\mbox{${\bf F}$}_j^{(n)}\big)+\Delta t\, \mbox{${\bf G}$}_j^{(n)}.

.. math::

   \mbox{${\bf w}$}_j^{(n+1)}=\tfrac 12\big(\mbox{${\bf w}$}_j^{(n)} +\mbox{${\bf w}$}_j^*-\dfrac{\Delta t}{\Delta x}
   \big(\mbox{${\bf F}$}_j^*-\mbox{${\bf F}$}_{j-1}^*\big) \big)+\tfrac 12 \Delta t\, \mbox{${\bf G}$}_j^*

Kafli 10: Fræðilegar spurningar
-------------------------------

#. Hvernig eru *flutningsjafna*, *flutnings- og dreifnijafna* og
   *bylgjujafna* í einni rúmvídd?

#. Hvernig er kennilína fyrir flutningsjöfnu gegnum punktinn
   :math:`(x,t)` fundin?

#. Hvernig er lausnarformúla fyrir einfalda flutningsjöfnu fundin út frá
   gefninni kennilínu?

#. Hvernig er mismunajafna fyrir flutningsjöfnu leidd út ef rúmafleiðan
   er nálguð með bakmismunakvóta?

#. Hvernig er uppstreymismismunaaðferð fyrir einfalda flutningsjöfnu?

#. Hvernig er MacCormack-aðferð fyrir einfalda flutningsjöfnu
   :math:`\dfrac{\partial u}{\partial t}+a(x,t,u)\dfrac{\partial u}{\partial x}=g(x,t,u)`?
