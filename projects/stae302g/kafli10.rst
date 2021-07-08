Laplace-ummyndunin
==================

*Think you've seen it all? Think again. Outside those doors, we might see anything. We could find new worlds, terrifying monsters, impossible things. And if you come with me... nothing will ever be the same again!*

\- The Doctor, Doctor Who


Laplace-ummyndunin
------------------

   

Skilgreining (Sjá §10.1) 
~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera fall sem skilgreint er á menginu :math:`\mathbb{R}_+=\{t\in \mathbb{R}; t\geq 0\}` með gildi í :math:`{\mathbb{C}}` og gerum ráð fyrir að :math:`f` sé heildanlegt á sérhverju lokuðu og takmörkuðu bili :math:`[0,b]`. Laplace–mynd :math:`f`, sem við táknum með :math:`{\cal L} f` eða :math:`{\cal L}\{f\}`, er skilgreind með formúlunni

.. math::

 {\cal L} f(s)=\int_0^ \infty e^{-st}f(t)\, dt.\label{7.1.1}

Skilgreiningarmengi fallsins :math:`{\cal L} f` samanstendur af öllum tvinntölum :math:`s` þannig að heildið í hægri hliðinni sé samleitið. Laplace-ummyndun er vörpunin :math:`{\cal L}` sem úthlutar falli :math:`f` Laplace-mynd sinni :math:`{\cal L} f`.

.. attention::

    Stundum er skilgreind ,,tvíhliða Laplace-mynd‘‘ falls þar sem heildið er reiknað frá :math:`-\infty` til :math:`\infty` og þá gæti maður kallað okkar Laplace-mynd ,,einhliða Laplace-mynd‘‘.

   

Skilgreining og setning  (Sjá Skilgreiningu 10.1.1) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við segjum að fallið :math:`f:\mathbb{R}_+\to {\mathbb{C}}` sé af veldisvísisgerð ef til eru jákvæðir fastar :math:`M` og :math:`c` þannig að

.. math::

 |f(t)|\leq Me^{c t}, \qquad t\in \mathbb{R}_+.\label{7.1.2}

Ef :math:`f` er þar að auki heildanlegt á sérhverju takmörkuðu bili :math:`[0,b]`, þá er :math:`{\cal L} f` skilgreint fyrir öll :math:`s\in {\mathbb{C}}` með :math:`\operatorname{Re\, } s>c`. Við fáum að auki vaxtartakmarkanir á :math:`{\cal L} f`,

.. math::

   |{\cal L} f(s) |\leq 
   \int_0^\infty e^{-\operatorname{Re\, } st} Me^{c t} \, dt =
   \dfrac M{\operatorname{Re\, }\,  s-c}, \qquad \operatorname{Re\, }\,  s>c.

Setning (Sjá §10.1) 
~~~~~~~~~~~~~~~~~~~

Laplace-ummyndunin er línuleg vörpun, en það þýðir að

.. math::

 {\cal L}\{\alpha f+\beta g\}(s)=\alpha{\cal L}\{f\}(s)+\beta{\cal L}\{g\}(s)

ef :math:`f` og :math:`g` eru föll af veldisvísisgerð, :math:`\alpha` og :math:`\beta` eru tvinntölur og :math:`s\in {\mathbb{C}}` liggur í skilgreiningarmengi fallanna :math:`{\cal L}\{f\}` og :math:`{\cal L}\{g\}`.

   

Setning (Sjá Setningu 10.1.6) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að föllin :math:`f,g\in C(\mathbb{R}_+)` séu bæði af veldisvísisgerð og að til sé fasti :math:`c` þannig að

.. math::

 {\cal L} f(s)={\cal L} g(s), \qquad s\in {\mathbb{C}}, \quad \operatorname{Re\, } s\geq c.

Þá er :math:`f(t)=g(t)` fyrir öll :math:`t\in \mathbb{R}_+`.

Setning (Sjá §10.1) 
~~~~~~~~~~~~~~~~~~~

(i) Ef :math:`\alpha\in \mathbb{R}` og :math:`\alpha>-1`, þá er

.. math::

 {\cal L}\{t^\alpha\}(s)=\dfrac {\Gamma(\alpha+1)}{s^{\alpha+1}},

og sér í lagi gildir ef :math:`\alpha` er heiltala að

.. math::

 {\cal L}\{t^\alpha\}(s)=\dfrac {\alpha!}{s^{\alpha+1}}.

(ii) Fyrir sérhvert :math:`\alpha\in {\mathbb{C}}` gildir

.. math::

 {\cal L}\{e^{\alpha t}\}(s)=\dfrac{1}{s-\alpha}.

Setning (Sjá Setningu 10.1.5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:math:`{\cal L}\{e^{\alpha t}f\}(s) = {\cal L}\{f\}(s-\alpha)`.

Tafla yfir Laplace-myndir (Sjá §10.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   \begin{aligned}
   {\cal L}\{\cos\beta t\}(s) &=
   \frac 12 {\cal L}\{e^{i\beta t}\}(s) +\frac 12{\cal L}\{e^{-i\beta t}\}(s)\\
   &=\frac 12\left[\dfrac 1{s-i\beta}+\dfrac 1{s+i\beta}\right]
   =\dfrac s{s^2+\beta^2},\\
   {\cal L}\{\sin\beta t\}(s) &=
   \frac 1{2i}{\cal L}\{e^{i\beta t}\}(s) -\frac 1{2i}{\cal L}\{e^{-i\beta t}\}(s)\\
   &=\frac 1{2i}\left[\dfrac 1{s-i\beta}-\dfrac 1{s+i\beta}\right]
   =\dfrac {\beta}{s^2+\beta^2},\\
   {\cal L}\{\cosh \beta t\}(s) &= 
   \frac 12 {\cal L}\{e^{\beta t}\}(s) +\frac 12{\cal L}\{e^{-\beta t}\}(s)\\
   &=\frac 12\left[\dfrac 1{s-\beta}+\dfrac 1{s+\beta}\right]
   =\dfrac s{s^2-\beta^2},\\
   {\cal L}\{\sinh \beta t\}(s) &= 
   \frac 1{2}{\cal L}\{e^{\beta t}\}(s) -\frac 1{2}{\cal L}\{e^{-i\beta t}\}(s)\\
   &=\frac 1{2}\left[\dfrac 1{s-\beta}-\dfrac 1{s+\beta}\right]
   =\dfrac \beta{s^2-\beta^2},\\
   {\cal L}\{e^{\alpha t}t^{\beta}\}(s)
   &=\dfrac{\Gamma(\beta+1)}{(s-\alpha)^{\beta+1}},\\
   {\cal L}\{e^{\alpha t}\cos \beta t\}(s)
   &=\dfrac{s-\alpha}{(s-\alpha)^2+\beta^2},\\
   {\cal L}\{e^{\alpha t}\sin \beta t\}(s)
   &=\dfrac{\beta}{(s-\alpha)^2+\beta^2},\\
   {\cal L}\{e^{\alpha t}\cosh \beta t\}(s)
   &=\dfrac{s-\alpha}{(s-\alpha)^2-\beta^2},\\
   {\cal L}\{e^{\alpha t}\sinh \beta t\}(s)
   &=\dfrac{\beta}{(s-\alpha)^2-\beta^2}.\end{aligned}

Setning (Sjá Setning 10.2.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`u\in C^ m(\mathbb{R}_+)` og :math:`u, u', u'', \dots, u^{(m-1)}`, eru af veldisvísisgerð, þá er :math:`{\cal L}\{u^{(m)}\}(s)` skilgreint fyrir öll :math:`s\in {\mathbb{C}}` með :math:`\operatorname{Re\, } s` nógu stórt og

.. math::

   {\cal L}\{u^{(m)}\}(s)=s^
   m{\cal L}\{u\}(s)-s^{m-1}u(0)-\cdots
   -su^{(m-2)}(0)-u^{(m-1)}(0).

Sér í lagi gildir að ef :math:`U(s)={\cal L}\{u(t)\}(s)`, þá er

.. math::

   {\cal L}\{u'\}(s)  = sU(s)-u(0),\qquad\mbox{og}\qquad
   {\cal L}\{u''\}(s) =s^2U(s)-su(0)-u'(0).

   

Reikniaðferð (Sjá §10.2) 
~~~~~~~~~~~~~~~~~~~~~~~~

Leysa á upphafsgildisverkefni af taginu:

.. math::

 a_mu^{(m)}+\cdots +a_1u'+a_0u=f(t), \qquad u(0)=b_0,\ u'(0)=b_1,\ldots,u^{(m-1)}(0)=b_{m-1}.

Skref 1: Reiknið Laplace-mynd hvorrar hliðar fyrir sig. Setning 10.1.7. gefur aðferð til að reikna Laplace-mynd vinstri hliðarinnar.

Skref 2: Notið jöfnuna sem kemur út úr Skrefi 1 til að fá formúlu fyrir :math:`U(s)={\cal L}\{u(t)\}(s)`.

Skref 3: Notið töflu eða andhverfa Laplace-ummyndun til að finna samfellt fall :math:`u(t)` sem hefur :math:`U(s)` sem fundið var í Skrefi 2 sem Laplace-mynd. Gætuð t.d. þurft að nota stofnbrotaliðun.

Skref 4: Fallið :math:`u(t)` sem fannst í Skrefi 3 er lausn upphafsgildisverkefnisins.

Notkun Laplace-ummyndunar
-------------------------

   
Skilgreining (Sjá §10.2) 
~~~~~~~~~~~~~~~~~~~~~~~~
Fyrir vigurgilt fall :math:`u(t)=\big(u_1(t), \ldots, u_m(t)\big)` má skilgreina Laplace-mynd þannig að tekin er Laplace-mynd í hverju hniti fyrir sig,

.. math::

 {\cal L}\{u(t)\}(s)=\big({\cal L}\{u_1(t)\}(s), \ldots,{\cal L}\{u_m(t)\}(s)\big).

Laplace-mynd fylkjagilds falls er reiknuð á sama hátt.

   

Setning (Sjá Setningu 10.2.4) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Um sérhvert :math:`m\times m` fylki :math:`A` gildir

.. math::

 {\cal L}\{e^{tA}\}(s) = (sI-A)^{-1}.

Upprifjun (Sjá §10.3 og §7.5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`P(D)=a_mD^ m+\cdots+a_1D+a_0` sé línulegur afleiðuvirki með fastastuðla. Látum :math:`g\in C^{\infty}(\mathbb{R})` vera fallið sem uppfyllir

.. math::

   P(D)g=0,\qquad \mbox{með }
   g(0)=g'(0)=\cdots=g^{(m-2)}(0)=0,\mbox{ og }
   g^{(m-1)}(0)=1/a_m.

Þá er :math:`G(t,\tau)=g(t-\tau)` Green-fall virkjans :math:`P(D)`.

Ef :math:`a` er einhver punktur þá hefur upphafsgildisverkefnið

.. math::

 P(D)u=f(t),

með

.. math::

 u(a)=u'(a)=\cdots=u^{(m-1)}(a)=0,

ótvírætt ákvarðaða lausn :math:`u_p\in C^m(I)` sem gefin er með
formúlunni

.. math::

 u_p(t) = \int_a^ t G(t,\tau)f(\tau) \, d\tau, \qquad t\in I,

og :math:`G(t,\tau)` er Green-fall virkjans :math:`P(D)`.

   

Setning (Sjá §10.3) 
~~~~~~~~~~~~~~~~~~~

Með sama táknmál og hér að ofan gildir að 

.. math::

 {\cal L}\{g\}(s)=\frac{1}{P(s)}.

Einnig gildir

.. math::

   {\cal L}\{u_p\}(s)={\cal L}\left\{\int_0^tg(t-\tau)f(\tau)\, d\tau\right\}(s)=
   {\cal L}\{g\}(s){\cal L}\{f\}(s).

Setning (Sjá Setning 10.3.1) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`f` og :math:`g` eru föll af veldisvísisgerð og heildanleg á sérhverju bili :math:`[0,b]`, þá er

.. math::

   {\cal L}\left\{\int_0^tf(t-\tau)g(\tau)\, d\tau\right\}(s)=
   {\cal L}\{f\}(s){\cal L}\{g\}(s).

Fylgisetning (Sjá Fylgisetningu 10.3.2) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`f` er af veldisvísisgerð og heildanlegt á sérhverju bili :math:`[0,b]`, þá er

.. math::

   {\cal L}\left\{\int_0^t f(\tau) \, d\tau\right\}(s) = \dfrac 1s
   {\cal L}\{f\}(s).

Setning (Sjá Setningu 10.2.1) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f:\mathbb{R}_+\to {\mathbb{C}}` vera fall af veldisvísigerð sem er heildanlegt á sérhverju bili :math:`[0,b]`. Þá er :math:`{\cal L}f` fágað á menginu :math:`\{s\in {\mathbb{C}}\mid \operatorname{Re\, } s>c\}` (þar sem :math:`c` er fastinn úr 10.1.2.) og

.. math::

 \frac{d^k}{ds^k}{\cal L}\{f\}(s)=(-1)^k{\cal L}\{t^kf(t)\}(s),\qquad \operatorname{Re\, } s>c.

   

Skilgreining og setning
~~~~~~~~~~~~~~~~~~~~~~~

Heaviside-fallið :math:`H(x)` er skilgreint þannig að :math:`H(t)=1` ef :math:`t\geq 0` og :math:`H(t)=0` ef :math:`t<0`.

Fallið :math:`H_a(t)=H(t-a)` er þannig að :math:`H_a(t)=1` ef :math:`t\geq a` og :math:`H(t)=0` ef :math:`t<a`.

Fyrir :math:`a\geq 0` er

.. math::

 {\cal L}\{H_a\}(s)=\frac{e^{-as}}{s}.

Setning
~~~~~~~

Látum :math:`f:\mathbb{R}_+\to {\mathbb{C}}` vera fall af veldisvísisgerð. Þá gildir um sérhvert :math:`a\geq 0` að

.. math::

 {\cal L}\{H(t-a)f(t-a)\}(s) = e^{-as}{\cal L}\{f\}(s).

þar sem fallið :math:`t\mapsto H(t-a)f(t-a)` tekur gildið :math:`0` fyrir öll :math:`t<a`.

Skilgreining og setning
~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`a` vera gefna rauntölu. Skilgreinum fall :math:`f_\epsilon(t)` þannig að :math:`f_\epsilon(t)=1/\epsilon` ef :math:`a<t<a+\epsilon` en :math:`f(t)=0` fyrir öll önnur gildi á :math:`t`. Athugið að ef :math:`a>0` þá er

.. math::

 \int_0^\infty f_\epsilon(t)\,dt=1.

Skilgreinum nú :math:`\delta_a` sem "markgildið" :math:`\lim_{\epsilon\to 0}f_\epsilon`. Sérstaklega skilgreinum við Dirac delta fallið sem :math:`\delta=\delta_0`. Athugið að :math:`\delta_a(t)=\delta(t-a)`. 


.. attention::

    Athugið að :math:`\delta_a` er ekki venjulegt fall heldur útvíkkuð gerð af falli sem er kölluð dreififall. 


Hægt er að reikna heildi af :math:`\delta_a` og við fáum að

.. math::

   \int_c^d \delta_a(t)\,dt=\left\{\begin{array}{ll}
   1 & \mbox{ef }c\leq a\leq d,\\
   0 & \mbox{annars.}
   \end{array}\right.

Auðvelt er að sjá að ef :math:`c\leq a\leq d` þá er :math:`\int_c^d f(t)\delta_a(t)\,dt=f(a)`. Sérstaklega gildir að

.. math::

 {\cal L}\{\delta_a\}(s)=e^{-as}.

Setning (Andhvefuformúla Fourier-Mellin)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`f:\mathbb{R}_+\to {\mathbb{C}}` er samfellt deildanlegt á köflum og uppfyllir :math:`|f(t)|\leq Me^{ct}`, :math:`t\in \mathbb{R}_+`, þar sem :math:`M` og :math:`c` eru jákvæðir fastar, þá gildir um sérhvert :math:`\xi>c` og sérhvert :math:`t>0` að

.. math::

   \begin{aligned}
   \tfrac 12(f(t+)+f(t-)) &= \lim_{R\to +\infty} \dfrac 1{2\pi}
   \int_{-R}^{+R}e^{(\xi+i\eta)t}{\cal L} f(\xi+i\eta) \, d\eta\\
   &= \lim_{R\to +\infty} \dfrac 1{2\pi i}
   \int_{\xi-iR}^{\xi+iR}e^{\zeta t}{\cal L} f(\zeta) \, d\zeta,\nonumber\end{aligned}

þar sem :math:`\int_{\xi-iR}^{\xi+iR}` táknar að heildað sé eftir línustrikinu með upphafspunktinn :math:`\xi-iR` og lokapunktinn :math:`\xi+iR`. Ef :math:`{\cal L} f(\xi+i\eta)` er í :math:`L^ 1(\mathbb{R})` sem fall af :math:`\eta`, þá er :math:`f` samfellt í :math:`t` og

.. math::

   \begin{aligned}
   f(t)&=  \dfrac 1{2\pi}
   \int_{-\infty}^{+\infty}e^{(\xi+i\eta)t}{\cal L} f(\xi+i\eta) \, d\eta\\
   &= \dfrac 1{2\pi i}
   \int_{\xi-i\infty}^{\xi+i\infty}e^{\zeta t}{\cal L} f(\zeta) \,
   d\zeta,\nonumber\end{aligned}

þar sem :math:`\int_{\xi-i\infty}^{\xi+i\infty}` táknar að heildað sé eftir línunni :math:`\{\xi+i\eta; \eta\in \mathbb{R}\}` í stefnu vaxandi :math:`\eta`.

   
Setning
~~~~~~~

Látum :math:`f:\mathbb{R}_+\to {\mathbb{C}}` vera samfellt deildanlegt á köflum og af veldisvísisgerð, með :math:`|f(t)|\leq Me^{ct}`, :math:`t>0`, og gerum ráð fyrir að hægt sé að framlengja :math:`{\cal L} f` yfir í fágað fall á :math:`{\mathbb{C}}\setminus A`, þar sem :math:`A` er endanlegt mengi. Ef :math:`\xi>c`, :math:`M_r` táknar hálfhringinn sem stikaður er með :math:`\gamma_r(\theta)=\xi+ire^{i\theta}`, :math:`\theta\in [0,\pi]` og

.. math::

 \max_{\zeta\in M_r}|{\cal L} f(\zeta)|\to 0, \qquad r\to +\infty,

þá er

.. math::

   \frac 12(f(t+)+f(t-))=
   \sum_{\alpha\in A}\operatorname{Res}(e^{\zeta t}{\cal L} f(\zeta),\alpha).

Ef :math:`f` er samfellt í :math:`t`, þá gildir

.. math::

 f(t)= \sum_{\alpha\in A}\operatorname{Res}(e^{\zeta t}{\cal L} f(\zeta),\alpha).

   

Fylgisetning
~~~~~~~~~~~~

Notum áfram táknmálið í 10.2.3. Táknum með :math:`A` núllstöðvamengi margliðunnar :math:`P(\zeta)`. Þá er

.. math::

   g(t)= \sum\limits_{\alpha\in A} 
   \operatorname{Res}\bigg( \dfrac {e^{t\zeta}}{P(\zeta)},\alpha\bigg).

---------------------------

*If it’s time to go, remember what you’re leaving. Remember the best.*

\- The Doctor, Doctor Who


