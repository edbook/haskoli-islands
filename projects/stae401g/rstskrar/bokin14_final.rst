
Eigingildisverkefni
===================

Eigingildi og eiginföll
-----------------------

Upprifjun úr línulegri algebru
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við skulum byrja á því að rifja upp nokkur hugtök úr línulegri algebru.
Látum :math:`V` vera vigurrúm með tvinntalanmargföldun og
:math:`T:V\to V` vera línulegan virkja. Tvinntalan :math:`\lambda` er
sögð vera *eigingildi* virkjans :math:`T` er til er :math:`v\neq 0` í
:math:`V` þannig að

.. math:: Tv=\lambda v.

Ef þessi jafna gildir, þá segjum við að :math:`v` sé eiginvigur, sem
svarar til eigingildisins :math:`\lambda`. Einnig segjum við að
:math:`v` sé eiginvigur með eigingildið :math:`\lambda`.

Fyrir sérhvert :math:`\lambda\in {{\mathbb  C}}` er mengið
:math:`E_\lambda=\{v\in V \,;\, Tv=\lambda v\}` hlutrúm í :math:`V`.
Talan :math:`\lambda` er eigingildi ef og aðeins ef þetta hlutrúm
samanstendur af fleiri stökum en núllvigrinum einum saman. Ef
:math:`\lambda` er eigingildi, þá nefnist :math:`E_\lambda` *eiginrúmið*
sem svarar til eigingildisins :math:`\lambda`. Ef :math:`V` er rúm sem
samanstendur af föllum, þá segjum við að :math:`v` sé *eiginfall* sem
svarar til eigingildisins :math:`\lambda`.

Mikilvægi eigingilda
~~~~~~~~~~~~~~~~~~~~

Eigingildi og eiginvigrar skipta miklu málið þegar verið að leysa alls
konar jöfnur. Hugsum okkur að við þurfum að leysa jöfnuna :math:`Tu=f`
þar sem hægt er að liða hægri hlið jöfnunnar í línulega samatekt
eiginvigra :math:`f=\sum_j c_j v_j`, þar sem :math:`Tv_j=\lambda_j v_j`
og :math:`\lambda_j\neq 0` fyrir öll :math:`j`. Þá fæst lausnin
:math:`u` með formúlunni

.. math:: u=\sum_j \dfrac{c_j}{\lambda_j} v_j.

Þetta sést einfaldlega með því að nýta það að :math:`T` er línulegur
virki og hann getur því verkað á summuna lið fyrir lið,

.. math::

  Tu=\sum_j \dfrac{c_j}{\lambda_j} Tv_j
   =\sum_j \dfrac{c_j}{\lambda_j} \lambda_jv_j
   =\sum_j c_jv_j=f.

Mikilvægi veldisvísisfallsins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við taka :math:`V=C^\infty({{\mathbb  R}})` og setja
:math:`u(x)=e^{\alpha x}` með :math:`\alpha\in {{\mathbb  C}}`. Ef við
látum deildavirkjana :math:`D`, :math:`D^2`, :math:`\dots` verka á
:math:`u(x)`, þá fáum við

.. math::

  \begin{aligned}
   Du(x)&=u'(x)=\alpha e^{\alpha x}=\alpha u(x),\\ 
   D^2u(x)&=u''(x)=\alpha^2 e^{\alpha x}=\alpha^2u(x),\\
   \vdots & \qquad \qquad \vdots \qquad \qquad \vdots\\
   D^ku(x)&=u^{(k)}(x)=\alpha^k e^{\alpha x}=\alpha^ku(x),\end{aligned}

sem segir okkur að :math:`u(x)` sé eiginfall virkjanna
:math:`D,D^2,\dots,D^k` með eigingildin
:math:`\alpha,\alpha^2,\dots,\alpha^k`.

Ef við tökum almennan afleiðuvirkja með fastastuðla
:math:`P(D)=a_mD^m+\cdots+a_1D+a_0`, þá fáum við

.. math::

  P(D)u(x)=(a_m\alpha^m+\cdots+a_1\alpha+a_0)e^{\alpha x}
   =P(\alpha)u(x),

sem segir okkur að fallið :math:`u` sé eiginfall virkjans :math:`P(D)`
með eigingildið :math:`\lambda=P(\alpha)`.

Þetta notuðum við til þess að finna sérlausnir á
afleiðujöfnum, en hugmyndin er að finna lausn á jöfnunni
:math:`P(D)u=f`, þar sem fallið :math:`f` er af gerðinni

.. math:: f(x)=\sum_j c_je^{\alpha_j x}

og :math:`P(\alpha_j)\neq 0` fyrir öll :math:`j`, með því að taka eins
summu

.. math:: u(x)=\sum_j \dfrac{c_j}{P(\alpha_j)} e^{\alpha_j x}

.. _sec14.2:

Eigingildisverkefni fyrir afleiðuvirkja
---------------------------------------

Það verkefni að leysa afleiðujöfnu af taginu

.. math::

  a_m(x)u^{(m)}+\cdots+a_1(x)u{{^{\prime}}}+a_0(x)u=\lambda u,
    \qquad x\in I,

þar sem :math:`\lambda` er tvinntala og :math:`I` er eitthvert bil á
rauntalnaásnum, með skilyrðum á lausnina í endapunktum bilsins
:math:`I`, kallast :hover:`eigingildisverkefni`.
Verkefnið er fólgið í því að finna öll :math:`\lambda\in {{\mathbb  C}}`
þannig að jafnan hafi lausn :math:`u_\lambda`, sem er ekki
núllfallið. Slík gildi :math:`\lambda` kallast :hover:`eigingildi` 
verkefnisins og lausnir
:math:`u_\lambda\neq 0` á jöfnunni kallast :hover:`eiginföll, eiginfall`.

Nú ætlum við að leysa nokkur eigingildisverkefni með virkjann
:math:`P(D)u=-u''` með mismunandi jaðarskilyrðum:

Fallsjaðarskilyrði í báðum endapunktum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _syfallsjadarskilyrdiibadumendapunktum:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Byrjum á verkefninu

.. math::

  \begin{cases}
   -X{{^{\prime\prime}}}(x) = \lambda X(x),& x\in ]0,L[\\
   X(0)=X(L)=0.
    \end{cases}

Kennijafna afleiðujöfnunnar er :math:`z^2+\lambda=0`. Ef
:math:`\lambda\neq 0` þá fáum við tvær tvinnlausnir
:math:`z=\pm i\beta`, þar sem :math:`\beta^2=\lambda` og við getum valið
:math:`{{\operatorname{Re\, }}}\beta \geq 0`. Því er almenn lausn
jöfnunnar

.. math:: X(x)=Ae^{i\beta x}+Be^{-i\beta x}.

Fyrra jaðarskilyrðið :math:`0=X(0)=A+B` gefur að :math:`B=-A`, svo við
getum skrifað

.. math:: X(x)=A(e^{i\beta x}-e^{-i\beta x})=2i A\sin(\beta x).

Seinna skilyrðið :math:`0=X(L)=2iA\sin(\beta L)` segir að
:math:`\lambda=\beta^2` sé eigingildi ef og aðeins ef :math:`\beta`
uppfyllir jöfnuna :math:`\sin(\beta L)=0`. Lausnir þessarar jöfnu eru
:math:`\beta_n=n\pi/L` með :math:`n=1,2,3,\dots`.

Í tilfellinu :math:`\lambda=0` fáum við almenna lausn afleiðujöfnunnar

.. math:: X(x)=A+Bx.

Jaðarskilyrðin :math:`0=X(0)=A` og :math:`0=X(L)=BL` segja að
:math:`A=B=0` og að :math:`\lambda=0` sé ekki eigingildi.

Niðurstaða útreikninga er því að eigingildin eru
:math:`\lambda_n=(n\pi/L)^2` og tilsvarandi eiginföll

.. math:: X(x)=C_n\sin((n\pi/L)x), \qquad n=1,2,3,\dots,

þar sem fastinn :math:`C_n\neq 0` getur verið hvaða tala sem er.
Línulegar samantektir eiginfallanna,

.. math:: u(x)=\sum_{n=1}^\infty B_n \sin\big(n\pi x/L\big),

eru Fourier-sínusraðir á bilinu [0,L].

.. end-toggle::

Afleiðujaðarskilyrði í báðum endapunktum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Nú breytum við verkefninu í

.. math::

  \begin{cases}
   -X{{^{\prime\prime}}}(x) = \lambda X(x),& x\in ]0,L[\\
   X'(0)=X'(L)=0.
    \end{cases}

Afgreiðum fyrst tilfellið :math:`\lambda=0`. Almenn lausn jöfnunnar er

.. math:: X(x)=C+Dx

Fyrra jaðarskilyrðið segir að :math:`0=X'(0)=D`. Þar með er
:math:`X(x)=C` sem uppfyllir bæði jaðarskilyrðin. Þar með er
:math:`\lambda=0` eigingildi og tilsvarandi eiginföll eru
:math:`X_0(x)=C_0` með :math:`C_0\neq 0`.

Við sáum í síðasta sýnidæmi að kennijafna afleiðujöfnunnar er
:math:`z^2+\lambda=0`. Í stað þess að velja :math:`e^{i\beta x}` og
:math:`e^{-i\beta x}` sem lausnagrunn, þá skulum við velja
:math:`cos(\beta x)` og :math:`\sin(\beta x)`. Almenn lausn er þá

.. math:: X(x)=C\cos(\beta x)+D\sin(\beta x).

Fyrra jaðarskilyrðið :math:`0=X'(0)=D\beta` gefur að :math:`D=0`, svo
við getum skrifað :math:`X(x)=C\cos(\beta x)`. og seinna jaðarskilyrðið
segir að :math:`0=X'(L)=-C\beta\sin(\beta L)`. Þar með fæst eigingildi
ef og aðeins ef :math:`\beta L=n\pi`, :math:`n=1,2,3,\dots`.

Niðurstaða er því að verkefnið hefur eigingildin
:math:`\lambda_n=(n\pi/L)^2` með eiginföllin

.. math:: X(x)=C_n\cos(n\pi x/L), \qquad n=0,1,2,\dots,

þar sem :math:`C_n\neq 0`. Línulegar samantektir eiginfallanna

.. math:: u(x)=\sum_{n=0}^\infty C_n \cos\big(n\pi x/L\big)

eru Fourier-kósínus-raðir á bilinu [0,L].

.. end-toggle::

Fallsjaðarskilyrði í öðrum endapunkti og afleiðuskilyrði í hinum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Næsta afbrigði jaðargildisverkefnisins er

.. math::

  \begin{cases}
   -X{{^{\prime\prime}}}(x) = \lambda X(x),& x\in ]0,L[\\
   X(0)=X'(L)=0.
    \end{cases}

Lítum fyrst á tilfellið :math:`\lambda=0`. Almenn lausn
afleiðujöfnunnar er :math:`X(x)=C+Dx` og jaðarskilyrðin gefa
:math:`0=X(0)=C` og :math:`0=X'(L)=D`, svo :math:`\lambda=0` er ekki
eigingildi.

Tökum nú :math:`\lambda\neq 0` og skrifum :math:`\lambda=\beta^2\neq 0`
með :math:`{{\operatorname{Re\, }}}\beta\geq 0`. Þá er Almenn lausn
:math:`X(x)=C\cos(\beta x)+D\sin(\beta x)`. Fyrra skilyrðið
:math:`0=X(0)=C` og hið síðara er :math:`0=D\beta\cos(\beta L)` sem
segir að :math:`\lambda` er eigingildi ef og aðeins ef
:math:`\cos(\beta L)=0`. Þetta gefur lausnirnar
:math:`\beta_n=(n-\tfrac 12)\pi/L` með :math:`n=1,2,3,\dots`.

Eigingildin eru því :math:`\lambda_n=\big((n-\tfrac 12)\pi/L\big)^2` og
tilsvarandi eiginföll

.. math:: X_n(x)=D_n \sin\big((n-\tfrac 12)\pi x/L\big)

þar sem :math:`D_n\neq 0`.

.. end-toggle::

Blönduð jaðarskilyrði í báðum endapunktum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Nú skulum við takast á við eigingildisverkefnið

.. math::

  -u{{^{\prime\prime}}}={\lambda}u, \quad \text{ á } [0,L], \qquad
   u{{^{\prime}}}(0)-a_0u(0)=0, \quad u{{^{\prime}}}(L)+a_Lu(L)=0.

**Jákvæð eigingildi:** Við leitum fyrst að skilyrði þess að :math:`{\lambda}=\beta^2`,
:math:`\beta>0` sé eigingildi. Almenn lausn jöfnunnar er

.. math:: u(x)=C\cos \beta x+D\sin \beta x

og jaðarskilyrðin segja að

.. math::

  \begin{aligned}
   u{{^{\prime}}}(0)-a_0u(0)&=\beta D-a_0C=0,\\ 
   u{{^{\prime}}}(L)+a_Lu(L)&=-\beta C\sin \beta L+\beta D\cos\beta L
   +a_L\big(C\cos\beta L+D\sin\beta L\big)\\
   &=\big(a_LC+\beta D\big)\cos\beta L+
   \big(-\beta C+a_LD\big)\sin\beta L=0.\end{aligned}

Við beitum fyrri jöfnunni til þess að leysa :math:`D` út úr þeirri
síðari og fáum

.. math:: C\big((a_0+a_L)\cos\beta L-(\beta-a_0a_L/\beta)\sin\beta L\big)=0.

Til þess að eiginfall fáist, þá þarf :math:`C\neq 0` að gilda, og við
fáum því jöfnuna

.. math:: \tan\beta L=\dfrac{(a_0+a_L)\beta}{\beta^2-a_0a_L}.

Það er ekki til nein bein formúla fyrir lausnir þessarar jöfnu, en með
aðferð Newtons og Raphsons er auðvelt að finna tölulegar nálganir á
þeim. Með því að teikna upp gröf fallanna í báðum hliðum jöfnunar hér að ofan
í tilfellinu :math:`a_0>0` og :math:`a_L>0`, þá sjáum við að til eru
óendanlega margar lausnir :math:`\alpha_2<\beta_2<\cdots\to+{\infty}`,
:math:`\beta_n\approx (n-1/2){\pi}` ef :math:`n\to +{\infty}`:

.. figure:: ./myndir/fig082.svg
    :align: center
    :alt: Runan :math:`(\beta_n)`. Stuðlarnir :math:`a_0` og :math:`a_L` hafa sama formerki.

    Mynd: Runan :math:`(\beta_n)`. Stuðlarnir :math:`a_0` og :math:`a_L` hafa sama formerki.

Í tilfellinu að :math:`a_0` og :math:`a_L` hafi ólík formerki og
:math:`0<(a_0+a_L)/|a_0a_L|<L`, þá fáum við gröfin:

.. figure:: ./myndir/fig083.svg
    :align: center
    :alt: Runan :math:`(\beta_n)`. Stuðlarnir :math:`a_0` og :math:`a_L` hafa ólík formerki.

    Mynd: Runan :math:`(\beta_n)`. Stuðlarnir :math:`a_0` og :math:`a_L` hafa ólík formerki.

Í öllum öðrum tilfellum er hægt að teikna upp gröf og sjá út frá þeim að
við höfum óendanlega mörg jákvæð eigingildi
:math:`{\lambda}_n=\beta_n^2`, :math:`n=1,2,\dots`. Tilsvarandi
eiginföll verða

.. math::

  u_n(x)= C_n\bigg(\cos\beta_nx+\dfrac
   {a_0}{\beta_n}\sin\beta_nx\bigg)
   \qquad x\in [0,L].

**Eigingildið** :math:`{\lambda}=0` **:** Nú er almenn lausn jöfnunnar

.. math:: u(x)=C+Dx

og jaðarskilyrðin segja að

.. math::

  \begin{aligned}
   u{{^{\prime}}}(0)-a_0u(0)&=D-a_0C=0,\\
   u{{^{\prime}}}(L)+a_Lu(L)&=D+a_L\big(C+DL\big)=0,\end{aligned}

Ef við beitum fyrri jöfnunni til þess að eyða :math:`D` úr þeirri
síðari, þá fæst

.. math:: C\big( (a_0+a_L)+a_0a_LL\big)=0

og skilyrði þess að :math:`{\lambda}=0` sé eigingildi er að

.. math:: L=-(a_0+a_L)/a_0a_L.

Tilsvarandi eiginfall verður þá

.. math:: u_0(x)=C_0\big(1+a_0x), \qquad x\in [0,L].

**Neikvæð eigingildi:** Við skrifum nú :math:`{\lambda}=-{\gamma}^2`,
:math:`{\gamma}>0`. Almenn lausn á jöfnunni er

.. math:: u(x)=C\cosh {\gamma} x+D\sinh{\gamma}x

og jaðarskilyrðin segja okkur að

.. math::

  \begin{aligned}
   u{{^{\prime}}}(0)-a_0u(0)&={\gamma}D-a_0C=0,\\
   u{{^{\prime}}}(L)+a_Lu(L)&={\gamma}C\sinh{\gamma}L+{\gamma}D\cosh{\gamma}L
   +a_L\big(C\cosh{\gamma}L+D\sinh{\gamma}L\big)\\
   &=\big(a_LC+{\gamma}D\big)\cosh{\gamma}L +
   \big({\gamma}C+a_LD\big)\sinh{\gamma}L=0.\end{aligned}

Við leysum :math:`D` út úr fyrri jöfnunni og stingum inn í þá síðari

.. math::

  C\big((a_0+a_L)\cosh{\gamma}L+({\gamma}+a_0a_L/{\gamma})\sinh{\gamma}L\big)
    =0.

Nú þarf :math:`C\neq 0` að gilda og því fáum við

.. math:: \tanh{\gamma}L=\dfrac{-(a_0+a_L){\gamma}}{{\gamma}^2+a_0a_L}.

Samfelldi ferillinn á myndinni hér að neðan er graf fallsins :math:`\tanh{\gamma}L`
sem fall af :math:`{\gamma}`. Ef :math:`a_0>0` og :math:`a_L>0`, þá fæst
ekkert neikvætt eigingildi, því í vinstri hliðinni stendur
jákvætt fall, en neikvætt í hægri hliðinni. Ef :math:`a_0` og
:math:`a_L` hafa ólík formerki og :math:`L<(a_0+a_L)/|a_0a_L|`, þá er
punktaferillinn á mynd 14.3 graf fallsins í hægri hliðinni.
Tilfellið að :math:`a_0` og :math:`a_L` hafi ólík formerki og
:math:`L>(a_0+a_L)/|a_0a_L|` er strikaferillinn á mynd hér að framan. Þá
fæst eitt neikvætt eigingildi :math:`{\lambda}_0=-{\gamma}_0^2`.

.. figure:: ./myndir/fig084.svg
    :align: center
    :alt: 14.3: Neikvæð eigingildi

    Mynd: 14.3: Neikvæð eigingildi

Í öðrum tilfellum fást ýmist ekkert, eitt eða tvö eigingildi. Í öllum
tilfellum er eiginfallið af gerðinni

.. math::

  u_0(x)=C_0\bigg(\cosh{\gamma}_0x+
   \dfrac{a_0}{{\gamma}_0}\sinh{\gamma}_0x\bigg)

.. end-toggle::

Aðskilnaður breytistærða
------------------------

Aðskilnaður breytistærða
~~~~~~~~~~~~~~~~~~~~~~~~

Algengt er að eigingildisverkefni komi upp þegar verið er að leysa
hlutafleiðujöfnur með aðferð, sem kallast *aðskilnaður breytistærða*. 
Það er lang best að skoða hana með dæmum:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Lítum á :ref:`sýnidæmi <Sveiflandistrengurframhald>` sem fjallar um sveiflandi streng og
leysum það með aðskilnaði breytistærða, 

.. math::

  \dfrac{{\partial}^2u}{{\partial}t^2}-
   c^2\dfrac{{\partial}^2u}{{\partial}x^2}=0, \qquad u(0,t)=u(L,t)=0,

.. math::
   u(x,0)=\varphi(x), \qquad {\partial}_tu(x,0)={\psi}(x), \qquad x\in
   ]0,L[.

Við byrjum á því að finna allar
lausnir á jöfnunni af gerðinni :math:`T(t)X(x)`. Við stingum þessu falli
inn í jöfnuna og fáum

.. math:: T{{^{\prime\prime}}}(t)X(x)-c^2T(t)X{{^{\prime\prime}}}(x)=0.

Með því að deila í gegnum þessa jöfnu með :math:`c^2T(t)X(x)`, þá sjáum
við að hún jafngildir

.. math:: \dfrac{T{{^{\prime\prime}}}(t)}{c^2T(t)} = \dfrac{X{{^{\prime\prime}}}(x)}{X(x)}.

Vinstra megin jafnaðarmerkisins stendur fall, sem er aðeins háð
:math:`t`, en hægra megin stendur fall, sem er aðeins háð :math:`x`.
Þessi stærð hlýtur því að vera fasti. Við skulum tákna hann með
:math:`-{\lambda}`, þar sem :math:`{\lambda}` er rauntala. Nú segir
jaðarskilyrðið að :math:`X(0)=X(L)=0` verði að gilda. Þar
með verður :math:`X` að vera lausn á eigingildisverkefninu

.. math:: -X{{^{\prime\prime}}}={\lambda} X, \qquad X(0)=X(L)=0.

Við fundum lausnina á þessu verkefni í 
:ref:`sýnidæmi <syfallsjadarskilyrdiibadumendapunktum>`.
Eigingildin eru :math:`{\lambda}_n=\big(n{\pi}/L\big)^2` og tilsvarandi
eiginföll má taka :math:`X_n(x)=\sin\big(n{\pi}x/L\big)`,
:math:`n=1,2,3,\dots`. Víkjum nú aftur að fallinu :math:`T`. 
Fyrir eigingildið :math:`\lambda_n` þarf
:math:`T` að uppfylla

.. math:: -T{{^{\prime\prime}}}= c^2{\lambda}_n T.

Almenn lausn þessarar jöfnu er
:math:`T_n(t)= A_n\cos\big(n{\pi}ct/L\big) + B_n\sin\big(n{\pi}ct/L\big)`. Niðurstaðan er nú að allar lausnir á bylgjujöfnunni af
gerðinni :math:`T(t)X(x)` með jaðarskilyrðinu
hér að ofan eru

.. math::

  T_n(t)X_n(x)=\big(A_n\cos\big(n{\pi}ct/L\big) +
   B_n\sin\big(n{\pi}ct/L\big)\big)
   \sin\big(n{\pi}x/L\big),

:math:`n=1,2,\dots`, þar sem velja má fastana :math:`A_n` og
:math:`B_n` frjálst. Það er ljóst að summa endanlega margra lausna
er lausn og sama gildir um óendanlegar raðir

.. math::

  u(x,t)=\sum\limits_{n=1}^{\infty}
   \big(A_n\cos\big(n{\pi}ct/L\big) +
   B_n\sin\big(n{\pi}ct/L\big)\big)
   \sin\big(n{\pi}x/L\big),

að því gefnu að þær séu nógu hratt samleitnar. Hér er Fourier–röðin úr
fyrra sýnidæminu komin. Stuðlarnir :math:`A_n` og :math:`B_n` ákvarðast
síðan af upphafsskilyrðum,

.. math:: u(x,0)=f(x), \qquad {\partial}_tu(x,0)=g(x),

þar sem :math:`f` og :math:`g` eru gefin föll á bilinu :math:`]0,L[`.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Til þess að sjá annað afbrigði af aðskilnaði breytistærða, skulum við
líta á jöfnuna

.. math:: a\partial_t^2u+b\partial_tu+cu-\Delta u=0,

þar sem :math:`\Delta=\partial_x^2+\partial_y^2+\partial_z^ 2` táknar
Laplace–virkjann og :math:`u` er fall af tíma :math:`t` og þremur
rúmbreytistærðum :math:`(x,y,z)`, :math:`u=u(t,x,y,z)`. Við leitum fyrst
að öllum lausnum á jöfnunni af gerðinni
:math:`u(x,y,z,t)=T(t)X(x)Y(y)Z(z)`, þar sem föllin :math:`T`,
:math:`X`, :math:`Y` og :math:`Z` eru hvert um sig háð einni
breytistærð. Við sjáum að

.. math::

  \begin{gathered}
   \dfrac 1u 
   \bigg(a\partial_t^2u+b\partial_tu+cu
   -\partial_x^2 u-\partial_y^2 u-\partial_z^2 u  \bigg) \\
   = \dfrac{aT{{^{\prime\prime}}}(t)+bT(t){{^{\prime}}}+cT(t)}{T(t)}-
   \dfrac{X{{^{\prime\prime}}}(x)}{X(x)}-\dfrac{Y{{^{\prime\prime}}}(y)}{Y(y)}-\dfrac{Z{{^{\prime\prime}}}(z)}{Z(z)}=0.\end{gathered}

Þessi jafna er jafngild

.. math::

  \dfrac{aT{{^{\prime\prime}}}(t)+bT(t){{^{\prime}}}+cT(t)}{T(t)}-
   \dfrac{X{{^{\prime\prime}}}(x)}{X(x)}-\dfrac{Y{{^{\prime\prime}}}(y)}{Y(y)}=\dfrac{Z{{^{\prime\prime}}}(z)}{Z(z)}.

Nú sjáum við að í hægri hlið jöfnunnar stendur fall sem er einungis háð
:math:`z`, en í vinstri hliðinni stendur fall sem er háð
:math:`(x,y,t)`. Þar með hlýtur :math:`Z{{^{\prime\prime}}}(z)/Z(z)`
að vera fastafall. Með nákvæmlega sömu rökum fáum við síðan að hinir
liðirnir í jöfnunni eru fastaföll og við fáum því

.. math::

  \begin{gathered}
   -X{{^{\prime\prime}}}(x)=\lambda X(x), \qquad -Y{{^{\prime\prime}}}(y)=\mu Y(y), \qquad
   -Z{{^{\prime\prime}}}(z)=\nu Z(z),\\
   aT{{^{\prime\prime}}}(t)+bT{{^{\prime}}}(t)+(c+\lambda+\mu+\nu)T=0, \label{1.6.10}\end{gathered}

þar sem :math:`\lambda`, :math:`\mu` og :math:`\nu` eru raun- eða
tvinntölur eftir því hvort við gerum ráð fyrir raun- eða tvinntölugildum
lausnum.

Hugsum okkur nú að við viljum leysa hlutafleiðujöfnuna

.. math:: a\partial_t^2u+b\partial_tu+cu-\Delta u=0,

á menginu

.. math:: \Omega=\{(x,y,z,t);  0<x<1, 0<y<1, 0<z<1\}

með því jaðarskilyrði að :math:`u(x,y,z,t)=0` ef :math:`(x,y,z,t)` er
punktur á jaðri :math:`\Omega`, en það þýðir að eitt hnitanna :math:`x`,
:math:`y` eða :math:`z` taki gildið :math:`0` eða :math:`1`. Ef við
beitum aðskilnaði breytistærða eins og áður var lýst, þá sjáum við að
föllin :math:`X`, :math:`Y` og :math:`Z` verða öll að vera lausnir á
eigingildisverkefninu í 
:ref:`sýnidæmi <syfallsjadarskilyrdiibadumendapunktum>`. 
Þar með sjáum við að
sérhver lausn á hlutafleiðujöfnunni af gerðinni
:math:`u(x,y,z,t)=T(t)X(x)Y(y)Z(z)` með þessum jaðarkilyrðum er af
gerðinni

.. math::

  u(x,y,z,t)=T_{\ell, m, n}(t) \sin (\ell \pi x) \sin (m\pi y) \sin
   (n\pi z), \qquad \ell, m, n=1,2,3,\dots,

þar sem :math:`T_{\ell, m,n}` er lausn jöfnunnar

.. math:: aT{{^{\prime\prime}}}+ bT{{^{\prime}}}+\big(c+\pi^2(\ell^2+m^2+n^2)\big)T=0.

.. end-toggle::

Virkjar af Sturm–Liouville–gerð 
--------------------------------

Virkjar af Sturm–Liouville–gerð 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við ætlum nú að fjalla um eigingildisverkefni fyrir annars stigs
línulega afleiðuvirkja :math:`L=P(x,D)` á lokuðu og takmörkuðu bili
:math:`[a,b]`

.. math:: Lu=P(x,D)u= a_2(x) u{{^{\prime\prime}}}+a_1(x)u{{^{\prime}}}+ a_0(x)u,

þar sem :math:`a_0,a_1,a_2\in C[a,b]` og :math:`a_2(x)\neq 0` fyrir öll
:math:`x\in [a,b]`. Í útreikningum okkar hentar betur að setja virkjann
fram með öðrum hætti,

.. math::

  Lu ={{\dfrac {1}{\varrho} 
   \bigg(-\dfrac d{dx}\bigg(p\dfrac {du}{dx}\bigg)+qu\bigg)}}.

Sambandið milli þessara tveggja framsetninga er einfalt. Við tökum

.. math::

  p(x)=\exp\bigg(C +\int_a^x\dfrac{a_1({\xi})}{a_2({\xi})}\, d{\xi}\bigg),
   \quad 
   q(x)=\dfrac{-a_0(x)p(x)}{a_2(x)}, \quad
   {\varrho}(x)=\dfrac{-p(x)}{a_2(x)},

þar sem :math:`C` er einhver ótiltekinn fasti. Það er rétt að rifja það
upp á þessu stigi að formúlan

.. math::

  W(t)=W(a)\exp\bigg(-\int_a^ t\dfrac{a_{1}(\tau)}{a_2(\tau)}\,
  d\tau\bigg)

segir okkur að fallið

.. math:: [a,b]\ni x\mapsto p(x)W(u_1,u_2)(x)

er fasti, ef :math:`u_1` og :math:`u_2` eru í núllrúmi virkjans
:math:`L`.

Skilgreining
^^^^^^^^^^^^

Við segjum að virkinn :math:`L` sé af Sturm–Liouville–gerð ef hann er
settur fram með formúlunni 

.. math::

  Lu ={{\dfrac {1}{\varrho} 
   \bigg(-\dfrac d{dx}\bigg(p\dfrac {du}{dx}\bigg)+qu\bigg)}}.

--------------

Við ætlum að takmarka okkur við að stuðlarnir séu raungildir. Fyrst
:math:`a_2(x)\neq 0` fyrir öll :math:`x\in [a,b]`, þá má gera ráð fyrir
að :math:`a_2(x)<0`. Það segir okkur að

.. math::

  p\in C^1[a,b], \quad p(x)>0, \quad q,{\varrho}\in C[a,b], \quad q(x)\in {{\mathbb  R}},
   \quad {\varrho}(x)>0, \quad x\in [a,b].

Skilgreining
^^^^^^^^^^^^

Við segjum að virki :math:`L` af Sturm–Liouville–gerð sé *reglulegur* ef
föllin :math:`p`, :math:`q` og :math:`{\varrho}` uppfylla þessi skilyrði.

--------------

Á rúmið :math:`C[a,b]` skilgreinum við formið

.. math::

  {{\langle u,v\rangle}} =\int_a^b u(x)\overline{v(x)}{\varrho}(x)\, dx, \qquad
   u,v\in C[a,b],

og á rúmið :math:`C^1[a,b]` skilgreinum við formið

.. math::

  {{\langle u,v\rangle}}_L =\int_a^b \bigg(p(x)u{{^{\prime}}}(x)\overline{v{{^{\prime}}}(x)}
   +q(x)u(x)\overline{v(x)}\bigg) \, dx, \qquad
   u,v\in C^1[a,b].

Bæði eru þessi form línuleg í fyrri breytistærðinni, en andlínuleg í
þeirri síðari. Það þýðir að

.. math::

  \begin{aligned}
    {{\langle \alpha u+\beta v,w\rangle}} &=
   \alpha{{\langle u,v\rangle}} + \beta{{\langle u,w\rangle}},\\
   {{\langle u,\alpha v+\beta w\rangle}}&=\bar\alpha{{\langle u,v\rangle}} +\bar\beta
   {{\langle u,w\rangle}},\end{aligned}

fyrir öll :math:`u,v\in C[a,b]`,
:math:`\alpha,\beta\in {{\mathbb  C}}`. Fyrst :math:`{\varrho}>0`, þá er
formið :math:`{{\langle \cdot,\cdot\rangle}}` innfeldi
og tilheyrandi :hover:`staðall` táknum við með :math:`\|\cdot\|`,

.. math:: \|u\|= {{\langle u,u\rangle}} ^{\frac 12}, \qquad u\in C[a,b].

Nú skulum við líta á sambandið á milli þessara tveggja forma. Með
hlutheildun fáum við

.. math::

  \begin{aligned}
   {{\langle Lu,v\rangle}} &=
   \int_a^b \dfrac {1}{\varrho(x)} 
   \bigg(-\dfrac d{dx}\bigg(p(x)\dfrac {du}{dx}(x)\bigg)+q(x)u(x)\bigg)
   \overline{v(x)}{\varrho}(x)\, dx  \\
   &=\bigg[-p(x)u{{^{\prime}}}(x)\overline{v(x)}\bigg]_a^b 
   + \int_a^b \bigg(p(x)u{{^{\prime}}}(x)\overline{v{{^{\prime}}}(x)}
   +q(x)u(x)\overline{v(x)}\bigg) \, dx\nonumber\\
   &=-\big(p(b)u{{^{\prime}}}(b)\overline{v(b)}
   -p(a)u{{^{\prime}}}(a)\overline{v(a)} \big)+{{\langle u,v\rangle}}_L,\nonumber\end{aligned}

.. math::

  \begin{aligned}
   {{\langle u,Lv\rangle}} &=
   \int_a^b u(x)\dfrac {1}{\varrho(x)} 
   \bigg(-\dfrac d{dx}\bigg(p(x)\dfrac {d\bar v}{dx}(x)\bigg)+q(x)\bar v(x)\bigg)
   {\varrho}(x)\, dx  \\
   &=\bigg[-p(x)u(x)\overline{v{{^{\prime}}}(x)}\bigg]_a^b 
   + \int_a^b \bigg(p(x)u{{^{\prime}}}(x)\overline{v{{^{\prime}}}(x)}
   +q(x)u(x)\overline{v(x)}\bigg) \, dx\nonumber\\
   &=-\big(p(b)u(b)\overline{v{{^{\prime}}}(b)}
   -p(a)u(a)\overline{v{{^{\prime}}}(a)} \big)+{{\langle u,v\rangle}}_L.\nonumber\end{aligned}

Við tökum nú mismuninn af þessum tveimur jöfnum og fáum *formúlu Greens*

.. math::

  \begin{aligned}
   {{\langle Lu,v\rangle}} -{{\langle u,Lv\rangle}} &=
   \left[p(x)\big(u(x)\overline{v{{^{\prime}}}(x)}-u{{^{\prime}}}(x)\overline{v(x)}\big)
   \right]_a^b \\
   &=p(b)\left|
   \begin{matrix} u(b) & u{{^{\prime}}}(b) \\ \bar v(b) &\bar v{{^{\prime}}}(b)
   \end{matrix}\right| -
   p(a)\left|
   \begin{matrix} u(a) & u{{^{\prime}}}(a) \\ \bar v(a) &\bar v{{^{\prime}}}(a)
   \end{matrix}\right|.\nonumber\end{aligned}

Jaðargildisvirkinn :math:`B` er af gerðinni

.. math::

  \begin{cases} B:C^1[a,b]\to {{\mathbb  C}}^2, \qquad Bu=(B_1u,B_2u),\\
   B_ju=\alpha_{j1}u(a)+\alpha_{j2}u{{^{\prime}}}(a)
   +\beta_{j1}u(b)+\beta_{j2}u{{^{\prime}}}(b), &j=1,2,
   \end{cases}

þar sem stuðlarnir :math:`\alpha_{jk}` og :math:`\beta_{jk}` eru
rauntölur. Við gerum ráð fyrir að þetta séu eiginleg skilyrði þannig að
í hvorum virkja sé að minnsta kosti einn stuðull frábrugðinn núlli.
Rúmið :math:`C^2_B[a,b]` er skilgreint sem mengi allra
:math:`u\in C^2[a,b]` sem uppfylla óhliðruðu jaðarskilyrðin
:math:`Bu=0`.

Skilgreining
^^^^^^^^^^^^

Við segjum að virkinn :math:`L` sé *samhverfur* á :math:`C^2_B[a,b]` eða
*samhverfur með tilliti til jaðarskilyrðanna* :math:`Bu=0` ef

.. math:: {{\langle Lu,v\rangle}} ={{\langle u,Lv\rangle}}, \qquad u,v\in C^2_B[a,b].

--------------

Út frá formúlu Greens sjáum við að :math:`L` er
samhverfur á :math:`C^2_B[a,b]` þá og því aðeins að

.. math::

  p(b)\left|
   \begin{matrix} u(b) & u{{^{\prime}}}(b) \\ \bar v(b) &\bar v{{^{\prime}}}(b)
   \end{matrix}\right| =
   p(a)\left|
   \begin{matrix} u(a) & u{{^{\prime}}}(a) \\ \bar v(a) &\bar v{{^{\prime}}}(a)
   \end{matrix}\right|

fyrir öll :math:`u,v\in C^2_B[a,b]`. Það eru einkum tvö tilfelli sem við
höfum áhuga á:

Setning
^^^^^^^

\(i) Ef :hover:`jaðarskilyrðin, jaðarskilyrði` eru *aðskilin* , þ.e.a.s.

.. math::

  B_1u=\alpha_1u(a)-\beta_1u{{^{\prime}}}(a), \qquad
   B_2u=\alpha_2u(b)+\beta_2u{{^{\prime}}}(b),

þar sem :math:`\alpha_1, \beta_1, \alpha_2, \beta_2\in {{\mathbb  R}}`,
:math:`(\alpha_1,\beta_1)\neq (0,0)` og :math:`(\alpha_2,\beta_2)\neq (0,0)`, þá er :math:`L` samhverfur á :math:`C^2_B[a,b]`.

\(ii) Ef :math:`p(a)=p(b)` og jaðarskilyrðin eru *lotubundin*, þ.e.a.s.

.. math:: B_1u=u(a)-u(b), \qquad B_2u=u{{^{\prime}}}(a)-u{{^{\prime}}}(b),

þá er :math:`L` samhverfur á :math:`C^2_B[a,b]`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

\(ii) er augljós afleiðing af 

.. math::

  p(b)\left|
   \begin{matrix} u(b) & u{{^{\prime}}}(b) \\ \bar v(b) &\bar v{{^{\prime}}}(b)
   \end{matrix}\right| =
   p(a)\left|
   \begin{matrix} u(a) & u{{^{\prime}}}(a) \\ \bar v(a) &\bar v{{^{\prime}}}(a)
   \end{matrix}\right|

og til þess að sanna (i) þá
tökum við :math:`u,v\in C^2_B[a,b]`. Jöfnurnar :math:`Bu=0` og
:math:`Bv=0` jafngilda því að vigrarnir :math:`(\alpha_1,\beta_1)` og
:math:`(\alpha_2,\beta_2)` uppfylli

.. math::

  \left[\begin{matrix}
   u(a) & u{{^{\prime}}}(a)\\ \bar v(a) & \bar v{{^{\prime}}}(a)
   \end{matrix}\right]
   \left[\begin{matrix}
   \alpha_1 \\ -\beta_1
   \end{matrix}\right]
   =\left[\begin{matrix}
    0 \\ 0
   \end{matrix}\right], \qquad
   \left[\begin{matrix}
   u(b) & u{{^{\prime}}}(b)\\ \bar v(b) & \bar v{{^{\prime}}}(b)
   \end{matrix}\right]
   \left[\begin{matrix}
   \alpha_2 \\ \beta_2
   \end{matrix}\right]
   =\left[\begin{matrix}
    0 \\ 0
   \end{matrix}\right].

Hvorugur vigranna er núllvigurinn, svo ákveður fylkjanna verða að vera
0. Þar með gildir 

.. math::

  p(b)\left|
   \begin{matrix} u(b) & u{{^{\prime}}}(b) \\ \bar v(b) &\bar v{{^{\prime}}}(b)
   \end{matrix}\right| =
   p(a)\left|
   \begin{matrix} u(a) & u{{^{\prime}}}(a) \\ \bar v(a) &\bar v{{^{\prime}}}(a)
   \end{matrix}\right|

og virkinn :math:`L` er samhverfur.

.. end-toggle::

Eigingildisverkefni af Sturm–Liouville–gerð
-------------------------------------------

Eigingildisverkefni af Sturm–Liouville–gerð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú tökum við fyrir eigingildisverkefnið

.. math:: Lu= {\lambda} u , \qquad Bu=0,

þar sem :math:`L` er virki af Sturm–Liouville–gerð og
:math:`B` er almennur jaðargildisvirki.
Talan :math:`{\lambda}\in {{\mathbb  C}}` kallast 
:hover:`eigingildi` virkjans :math:`L` á :math:`C^2_B[a,b]` ef til er
lausn :math:`u` á :math:`Lu = \lambda u` sem er ekki núllfallið og sérhver slík lausn
kallast :hover:`eiginfall`. Línulega rúmið sem spannað er af
öllum eiginföllum með tilliti til eigingildisins :math:`{\lambda}`
köllum við :hover:`eiginrúmið, eiginrúm` með tilliti til eigingildisins
:math:`{\lambda}` og við táknum það með :math:`E_{\lambda}`.

Skilgreining
^^^^^^^^^^^^

Ef :math:`L` er reglulegur virki af Sturm–Liouville–gerð, þá segjum við
að eigingildisverkefnið sé *reglulegt*.

Setning
^^^^^^^

Gerum ráð fyrir að virkinn :math:`L` af Sturm–Liouville–gerð sé
samhverfur á :math:`C^2_B[a,b]`. Þá eru öll eigingildin rauntölur og
eiginföllin sem svara til ólíkra eigingilda eru innbyrðis hornrétt.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Ef :math:`Lu={\lambda}u` og :math:`u` er ekki núllfallið, þá er

.. math::

  {\lambda}{{\langle u,u\rangle}} =
   {{\langle Lu,u\rangle}} =
   {{\langle u,Lu\rangle}} =
   {{\langle u,{\lambda}u\rangle}} =
   \bar{\lambda}{{\langle u,u\rangle}}.

Við getum nú stytt út :math:`{{\langle u,u\rangle}}` og fáum
:math:`{\lambda}=\bar {\lambda}`, sem segir að :math:`{\lambda}` sé
rauntala. Ef :math:`Lu={\lambda}u` og :math:`Lv={\mu}v` þá er

.. math::

  {\lambda}{{\langle u,v\rangle}} =
   {{\langle Lu,v\rangle}} =
   {{\langle u,Lv\rangle}} =
   {{\langle u,{\mu}v\rangle}} =
   \bar{\mu}{{\langle u,v\rangle}}.

Ef :math:`{\lambda}\neq {\mu}`, þá fær þessi jafna ekki staðist nema
:math:`{{\langle u,v\rangle}}=0`.

.. end-toggle::

Athugum nú að fyrir samhverfan virkja :math:`L` með eigingildi
:math:`{\lambda}` og eiginfall :math:`u=v+iw` gildir

.. math:: Lv+iLw=Lu={\lambda}u={\lambda}v+i{\lambda}w.

Þetta segir okkur að bæði raunhluti og þverhluti :math:`u` séu
eiginföll ef þeir eru báðir frábrugðnir núllfallinu. Við getum því
alltaf tekið raungild föll sem grunn fyrir eiginrúmið
:math:`E_{\lambda}`. Gerum nú ráð fyrir að :math:`u` sé raungilt
eiginfall sem svarar til eigingildisins :math:`{\lambda}` og gerum ráð
fyrir að :math:`\|u\|=1`. Þá fæst

.. math::

  \begin{aligned}
   {\lambda}& ={\lambda}{{\langle u,u\rangle}} =
   {{\langle Lu,u\rangle}} = \bigg[-p(x)u(x)u{{^{\prime}}}(x)\bigg]_a^b +{{\langle u,u\rangle}}_L \\
   &= p(a)u(a)u{{^{\prime}}}(a)-p(b)u(b)u{{^{\prime}}}(b) +{{\langle u,u\rangle}}_L\nonumber\end{aligned}

Ef jaðarskilyrðin eru aðskilin eins og í setningunni í síðustu grein, þá uppfyllir
:math:`u` jöfnurnar

.. math::

  \alpha_1u(a)-\beta_1u{{^{\prime}}}(a)=0, \qquad\text{ og } \qquad
   \alpha_2u(b)+\beta_2u{{^{\prime}}}(b)=0,

og þar með er

.. math::

  {\lambda}=\alpha p(a)u(a)^2+\beta p(b)u(b)^2
   +\int_a^b\bigg(p(x)u{{^{\prime}}}(x)^2+q(x)u(x)^2\bigg) \, dx,

þar sem við höfum sett :math:`\alpha=\alpha_1/\beta_1` ef
:math:`\beta_1\neq 0`, :math:`\alpha=0` ef :math:`\beta_1=0`,
:math:`\beta=\alpha_2/\beta_2` ef :math:`\beta_2\neq 0` og
:math:`\beta=0` ef :math:`\beta_2=0`. Athugið að :math:`\beta_1=0` hefur
í för með sér að :math:`u(a)=0` og :math:`\beta_2=0` hefur í för með sér
að :math:`u(b)=0`. Þessi útreikningur gefur:

Setning
^^^^^^^

Öll eigingildin eru :math:`\geq 0` í tilfellunum:

\(i) :math:`q(x)\geq 0` fyrir öll :math:`x\in [a,b]`, jaðarskilyrðin eru
aðskilin, :math:`B_1u=\alpha_1u(a)-\beta_1u{{^{\prime}}}(a)=0`,
:math:`B_2u=\alpha_2u(b)+\beta_2u{{^{\prime}}}(b)=0`,
:math:`\alpha_1\geq 0`, :math:`\beta_1\geq 0`, :math:`\alpha_2\geq 0` og
:math:`\beta_2\geq 0`.

\(ii) :math:`q(x)\geq 0` fyrir öll :math:`x\in [a,b]`, :math:`p(a)=p(b)`
og jaðarskilyrðin eru lotubundin, :math:`B_1u=u(a)-u(b)=0` og
:math:`B_2u=u{{^{\prime}}}(a)-u{{^{\prime}}}(b)=0`.

--------------

Meginniðurstaða kaflans er:

Setning
^^^^^^^

Gerum ráð fyrir að

.. math:: Lu={\lambda} u, \qquad Bu=0,

sé reglulegt Sturm–Liouville–eigingildisverkefni og að :math:`L` sé
samhverfur með tilliti til jaðarskilyrðanna :math:`Bu=0`. Þá er til
óendanleg runa :math:`{\lambda}_0<{\lambda}_1<{\lambda}_2\cdots \to +{\infty}` af eigingildum og tilsvarandi raungildum eiginföllum
:math:`u_0,u_1,u_2,\dots`, sem uppfylla

.. math:: {{\langle u_j,u_k\rangle}}=\begin{cases} 1, &j=k,\\0, &j\neq k,\end{cases}

og sérhvert fall :math:`u\in C^2_B[a,b]` er unnt að liða í eiginfallaröð

.. math:: u(x)=\sum\limits_{n=0}^{\infty} c_n(u)u_n(x), \qquad x\in [a,b],

sem er samleitin í jöfnum mæli á :math:`[a,b]` og stuðlarnir eru gefnir
með formúlunni

.. math:: c_n(u)={{\langle u,u_n\rangle}}= \int_a^bu(x)u_n(x){\varrho}(x)\, dx.

--------------

Þetta er erfið setning að sanna og við höfum engin tök á að gera það.

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Í :ref:`sýnidæmi <syfallsjadarskilyrdiibadumendapunktum>` sáum við að eigingildisverkefnið

.. math:: -u{{^{\prime\prime}}}={\lambda}u, \qquad u(0)=u(L)=0,

hefur eigingildin :math:`{\lambda}_n=(n{\pi}/L)^2`,
:math:`n=1,2,3,\dots`, og tilsvarandi eiginföll eru margfeldi af
:math:`u_n(x)=\sin(n{\pi}x/L)`. Með því að velja
:math:`p(x)={\varrho}(x)=2/L`, þá fáum við að 

.. math:: {{\langle u_j,u_k\rangle}}=\begin{cases} 1, &j=k,\\0, &j\neq k,\end{cases}

er uppfyllt
og :math:`c_n(u)` eru ekkert annað en Fourier–sínus–stuðlar fallsins
:math:`u`.

Ef við breytum randskilyrðunum og lítum á verkefnið

.. math:: -u{{^{\prime\prime}}}={\lambda}u, \qquad u{{^{\prime}}}(0)=u{{^{\prime}}}(L)=0,

þá fást eigingildin :math:`{\lambda}_n=(n{\pi}/L)^2`,
:math:`n=0,1,2,\dots`, og tilsvarandi eiginföll eru
:math:`u_n(x)=\cos(n{\pi}x/L)`. Með sama vali á :math:`p` og
:math:`{\varrho}` þá verða stuðlarnir :math:`c_n(u)`
Fourier–kósínus–stuðlar fallsins :math:`u`, ef :math:`n>0` og
:math:`c_0(u)=\frac 12 a_0(u)`.

.. end-toggle::

Skilgreining
^^^^^^^^^^^^

Fyrir sérhvert heildanlegt fall :math:`f` á :math:`[a,b]`, þá
skilgreinum við *Fourier–stuðul fallsins* :math:`f`  *með tilliti til
eiginfallsins* :math:`u_n` með

.. math:: c_n(f)= {{\langle f,u_n\rangle}} =\int_a^b f(x) u_n(x){\varrho}(x)\, dx

og *eiginfallaröðina af* :math:`f`  *með tilliti til eiginfallanna*
:math:`(u_n)_{n=0}^{\infty}` með

.. math:: \sum\limits_{n=0}^{\infty} c_n(f)u_n(x).

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Við skulum nú líta á jaðargildisverkefni fyrir 
:hover:`varmaleiðnijöfnuna, varmaleiðnijafna` með almennu jaðarskilyrði og upphafsskilyrði,

.. math::

  \begin{cases} {\partial}_tT-{\kappa}{\partial}_x^2T=f(x,t), &a<x<b, \quad
   t>0,\\
   B_1T(\cdot,t)=B_2T(\cdot,t)=0,  &t>0,\\
   T(x,0)=\varphi(x), &a<x<b.
   \end{cases}

Til þess að leysa þetta, skulum við gera ráð fyrir því að
:math:`{\lambda}_n`, :math:`n=1,2,3,\dots` séu eigingildin og að
:math:`u_n` séu tilsvarandi eiginföll með :math:`\|u_n\|=1` fyrir
verkefnið

.. math:: -{\kappa}u{{^{\prime\prime}}}={\lambda}u, \qquad B_1u=B_2u=0.

Við göngum út frá liðun fallsins :math:`T` í eiginfallaröð

.. math::

  T(x,t)=\sum\limits_{n=1}^{\infty} T_n(t)u_n(x), 
   \qquad
   T_n(t)=\int_a^bT(x,t)u_n(x){\varrho}(x)\, dx

og að hægri hlið jöfnunnar og upphafsgildin hafi hliðstæða liðun

.. math::

  f(x,t)=\sum\limits_{n=1}^{\infty} f_n(t)u_n(x), \qquad
   \varphi(x)=\sum\limits_{n=1}^{\infty} \varphi_nu_n(x).

Greinilegt er að jaðarskilyrðin eru uppfyllt, því allir liðir í eiginfallaröðinni uppfylla þau. Við stingum eiginfallaröðinni inn í
hlutafleiðujöfnuna og notum upphafsskilyrðin og jöfnuna
:math:`-{\kappa}u_n{{^{\prime\prime}}}={\lambda}_nu`

.. math::

  \begin{gathered}
   {\partial}_tT(x,t)-{\kappa}{\partial}_x^2T(x,t) =
   \sum\limits_{n=1}^{\infty} \big(T_n{{^{\prime}}}(t)+{\lambda}_nT_n(t)\big)u_n(x)
   =\sum\limits_{n=1}^{\infty} f_n(t)u_n(x)=f(x,t),\\
   T(x,0)=\sum\limits_{n=1}^{\infty}T_n(0)u_n(x)=
   \sum\limits_{n=1}^{\infty}\varphi_nu_n(x)=\varphi(x).\end{gathered}

Svarið verður því

.. math::

  T(x,t)=\sum\limits_{n=1}^{\infty}\bigg(\varphi_ne^{-{\lambda}_nt}
   +\int_0^te^{-{\lambda}_n(t-{\tau})}f_n({\tau})\, d{\tau}\bigg) u_n(x).

.. end-toggle::

Green-föll fyrir jaðargildisverkefni
------------------------------------

Green-föll fyrir jaðargildisverkefni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum nú :math:`P(x,D)` vera línulegan afleiðuvirkja af gerðinni

.. math:: P(x,D)=a_m(x)D^m+\cdots+a_1(x)D+a_0(x)

með :math:`a_0,\dots,a_m\in C[a,b]` og :math:`a_m(x)\neq 0` fyrir öll
:math:`x\in [a,b]`. Við athugum að það er alltaf hægt að stækka skilgreiningarsvæði
fallanna :math:`a_0,\dots,a_m, f\in C[a,b]` þannig að þau verði samfelld
á opnu bili :math:`I` sem inniheldur :math:`[a,b]` og :math:`a_m(x)\neq 0` fyrir öll :math:`x\in I`. Sérhver lausn á :math:`P(x,D)u=f` á opna bilinu :math:`]a,b[` er 
tvisvar samfellt deildanleg á grennd um lokaða bilið :math:`[a,b]` og
þar með eru gildin :math:`u(a)`,
:math:`u{{^{\prime}}}(a),\dots,u^{(m-1)}(a)`, :math:`u(b)`,
:math:`u{{^{\prime}}}(b),\dots,u^{(m-1)}(b)` vel skilgreind og óháð
því hvernig föllin eru skilgreind á :math:`I\setminus [a,b]`.

Við látum :math:`B` vera línulegan jaðargildisvirkja
á :math:`[a,b]` af gerðinni

.. math::

  \begin{cases}
   B:C^{m-1}[a,b]\to {{\mathbb  C}}^m, \qquad Bu=(B_1u,\dots,B_mu),\\
   B_ju=\sum\limits_{l=1}^m \alpha_{jl}u^{(l-1)}(a)+
   \beta_{jl}u^{(l-1)}(b).
   \end{cases}

Við gerum ráð fyrir því að fyrir sérhvert :math:`j` sé að minnsta kosti
ein talnanna :math:`\alpha_{jl}`, :math:`\beta_{jl}`,
:math:`l=1,\dots,m` frábrugðin :math:`0`. Við látum :math:`C^m_B[a,b]`
tákna rúm allra :math:`u\in C^m[a,b]` sem uppfylla óhliðruðu
jaðarskilyrðin :math:`Bu=0`. Við höfum séð fullkomna
lýsingu á því hvenær jaðargildisverkefnið :math:`P(x,D)u=f`,
:math:`Bu=c` hefur ótvírætt ákvarðaða lausn fyrir sérhvert
:math:`f\in C[a,b]` og sérhvert :math:`c\in {{\mathbb  C}}`.

Nú ætlum við að ákvarða lausnarformúlu fyrir lausn :math:`P(x,D)u=f` með
óhliðruðum jaðarskilyrðum :math:`Bu=0`. Við beitum hliðstæðum aðferðum
og þegar við reiknuðum út lausnarformúluna fyrir
lausn upphafsgildisverkefnisins :math:`P(x,D)u=f`,
:math:`u(a)=u{{^{\prime}}}(a)=\cdots=u^{(m-1)}(a)=0`. Við byrjum á
tveimur léttum sýnidæmum:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Við skulum taka fyrir verkefnið

.. math:: -u{{^{\prime\prime}}}=f(x), \qquad B_1u=u(0)=B_2u=u(1)=0,

þar sem :math:`f\in C[0,1]`. Almenn lausn fyrir óhliðruðu jöfnuna er
línuleg samantekt :math:`u_1(x)=1` og :math:`u_2(x)=x`, Green-fall
virkjans er :math:`G(x,\xi)=-(x-\xi)` og

.. math::

  \left|\begin{matrix}
   B_1u_1 & B_1u_2 \\ B_2u_1 & B_2u_2
   \end{matrix}
   \right| =
   \left|\begin{matrix}
   1&0\\ 1&1
   \end{matrix}
   \right| =1,

svo við höfum ótvírætt ákvarðaða lausn sem gefin er með formúlu af
gerðinni

.. math:: u(x)= c_1+c_2x-\int_0^x (x-\xi)f(\xi)\, d\xi.

Jaðarskilyrðin gefa okkur

.. math::

  \begin{aligned}
   0&=u(0)=c_1,\\
   0&=u(1)=c_1+c_2-\int_0^1 (1-\xi)f(\xi)\, d\xi,\end{aligned}

og því er

.. math::

  \begin{aligned}
   u(x)&=x\int_0^1 (1-\xi) f(\xi)\, d\xi - \int_0^x (x-\xi)f(\xi)\,
   d\xi\\
   &=\int_0^x (x(1-\xi)-(x-\xi))f(\xi)\, d\xi +
   \int_x^1 x(1-\xi)f(\xi)\, d\xi\\
   &=\int_0^x \xi(1-x)f(\xi)\, d\xi +
   \int_x^1 x(1-\xi)f(\xi)\, d\xi\\
   &=\int_0^1 G_B(x,\xi)f(\xi)\, d\xi,\end{aligned}

þar sem fallið :math:`G_B\in C([0,1]\times [0,1])` er gefið með
formúlunni

.. math::

  G_B(x,\xi)=\begin{cases}
   \xi(1-x),  & 0\leq \xi\leq x\leq 1,\\
   x(1-\xi),  & 0\leq x\leq \xi\leq 1.
   \end{cases}

Fallið :math:`G_B` kallast *Green-fallið fyrir jaðargildisverkefnið*

.. math:: -u{{^{\prime\prime}}}=f(x), \qquad B_1u=u(0)=B_2u=u(1)=0.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Áþekkt verkefni er

.. math:: -u{{^{\prime\prime}}}-{\omega}^2u=f(x), \qquad B_1u=u(0)=B_2u=u(1)=0.

Almenn lausn fyrir óhliðruðu jöfnuna er línuleg samantekt af
:math:`u_1(x)=\cos {\omega} x` og :math:`u_2(x)=\sin {\omega}x`,
Green-fall virkjans er
:math:`G(x,\xi)=-\sin \big({\omega}(x-\xi)\big)/{\omega}` og

.. math::

  \left|\begin{matrix}
   B_1u_1 & B_1u_2 \\ B_2u_1 & B_2u_2
   \end{matrix}
   \right| =
   \left|\begin{matrix}
   1&0\\ \cos {\omega}& \sin{\omega}
   \end{matrix}
   \right| =\sin{\omega}.

Við fáum ótvírætt ákvarðaða lausn þá og því aðeins að :math:`{\omega}`
sé ekki heiltölumargfeldi af :math:`{\pi}`. Lausn á eigingildisverkefninu er
því af gerðinni

.. math::

  u(x)= c_1\cos{\omega} x+c_2\sin{\omega} x-
   \int_0^x \dfrac{\sin ({\omega}(x-\xi))}{\omega}f(\xi)\, d\xi.

Jaðarskilyrðin gefa okkur

.. math::

  \begin{aligned}
   0&=u(0)=c_1,\\
   0&=u(1)=c_1\cos{\omega}+c_2\sin{\omega}-\int_0^1
   \dfrac{\sin({\omega}(1-\xi))}{\omega} f(\xi)\, d\xi.\end{aligned}

Við leysum út stuðlana og fáum

.. math::

  \begin{aligned}
   u(x)&=\dfrac{\sin {\omega}x}{\sin {\omega}}
   \int_0^1 \dfrac{\sin {\omega}(1-\xi)}{\omega}
    f(\xi)\, d\xi - \int_0^x \dfrac{\sin {\omega}(x-\xi)}{\omega}
   f(\xi)\, d\xi\\
   &=\int_0^x \bigg
   (\dfrac{\sin {\omega}x\sin {\omega}(1-\xi)}{{\omega}\sin {\omega}}
   -\dfrac{\sin {\omega}(x-\xi)}{\omega}\bigg)f(\xi)\, d\xi \\
   &+ \int_x^1 \dfrac {\sin {\omega}x\sin{\omega} (1-\xi)}
   {{\omega}\sin {\omega}} f(\xi)\, d\xi.\end{aligned}

Samlagningarformúlan fyrir sínus gefur okkur nú að

.. math::

  \sin ({\omega}x)\sin({\omega}(1-\xi))/\sin {\omega}
   -\sin({\omega}(x-\xi))
   =\sin ({\omega}\xi)\sin ({\omega}(1-x))/\sin {\omega}.

og þar með fáum við

.. math::

  \begin{aligned}
   u(x)&=
   \int_0^x \dfrac{\sin {\omega}\xi\sin {\omega}(1-x)}{{\omega}\sin
   {\omega}} f(\xi)\, d\xi +
   \int_x^1 \dfrac {\sin {\omega}x\sin {\omega}(1-\xi)}{{\omega}\sin {\omega}}
   f(\xi)\, d\xi\\
   &=\int_0^1 G_B(x,\xi)f(\xi)\, d\xi,\end{aligned}

þar sem fallið :math:`G_B\in C([0,1]\times [0,1])` er gefið með
formúlunni

.. math::

  G_B(x,\xi)=\begin{cases}
   \dfrac{\sin {\omega}\xi\sin {\omega}(1-x)}{{\omega}\sin {\omega}},  
   & 0\leq \xi\leq x\leq 1,\\
   \dfrac{\sin {\omega}x\sin {\omega}(1-\xi)}{{\omega}\sin {\omega}},  
   & 0\leq x\leq \xi\leq 1.
   \end{cases}

Fallið :math:`G_B` kallast *Green-fallið fyrir jaðargildisverkefnið*

.. math:: -u{{^{\prime\prime}}}-{\omega}^2u=f(x), \qquad B_1u=u(0)=B_2u=u(1)=0.

.. end-toggle::

Nú skulum við gera ráð fyir því að :math:`{\lambda}=0` sé ekki
eigingildi virkjans :math:`P(x,D)` á :math:`C_B[a,b]`. Samkvæmt tilvistarsetningu fyrir línulegar afleiðujöfnur hefur
jaðargildisverkefnið :math:`P(x,D)u=f`, :math:`Bu=0`
ótvírætt ákvarðaða lausn. Við getum við skrifað hana
á forminu

.. math::

  u(x)=c_1u_1(x)+\cdots+c_mu_m(x) +
   \int_a^x G(x,{\xi})f({\xi})\, d{\xi},

þar sem :math:`u_1,\dots,u_m` er grunnur í :math:`{\cal N}(P(x,D))` og
:math:`G` táknar Green-fall virkjans. Aleiðan af stigi :math:`k` er

.. math::

  u^{(k)}(x)=c_1u^{(k)}_1(x)+\cdots+c_mu^{(k)}_m(x)
   +\int_a^x {\partial}_x^{k}G(x,{\xi})f({\xi})\, d{\xi},

fyrir öll :math:`k=0,\dots,m-1`. Nú látum við jaðargildisvirkjana
:math:`B_1,\dots,B_m` verka á :math:`u` og fáum

.. math::

  B_ju=c_1B_ju_1+\cdots+c_mB_ju_m +
   \int_a^b \sum\limits_{l=1}^m \beta_{jl}{\partial_x^{l-1}}
   G(b,{\xi})f({\xi})\, d{\xi}=0.

Nú er hyggilegt að innleiða fallið

.. math::

  F(x,{\xi}) = \begin{cases} G(x,{\xi}), &a\leq{\xi}\leq x\leq b,\\
   0, &a\leq x\leq{\xi} \leq b.\end{cases}

.. figure:: ./myndir/fig081.svg
    :align: center
    :alt: :math:`F(x,\xi)`

    Mynd: :math:`F(x,\xi)`

Þá er greinilegt að :math:`{\partial}_x^{l-1}F(a,{\xi})=0` fyrir öll
:math:`l=1,\dots,m` og :math:`{\xi}\in ]a,b[`, svo 

.. math::

  B_ju=c_1B_ju_1+\cdots+c_mB_ju_m +
   \int_a^b \sum\limits_{l=1}^m \beta_{jl}{\partial_x^{l-1}}
   G(b,{\xi})f({\xi})\, d{\xi}=0

jafngildir jöfnuhneppinu

.. math::

  \big(B_ju_1\big)c_1+\cdots+\big(B_ju_m\big)c_m=
   -\int_a^b B_jF(\cdot,{\xi})f({\xi}) \, d{\xi},

þar sem :math:`B_jF(\cdot,{\xi})` táknar að :math:`B_j` verki á fallið
:math:`F` með tilliti til fyrri breytistærðarinnar. Við fáum nú:

Hjálparsetning
^^^^^^^^^^^^^^

Fallið :math:`F` sem skilgreint er með 

.. math::

  F(x,{\xi}) = \begin{cases} G(x,{\xi}), &a\leq{\xi}\leq x\leq b,\\
   0, &a\leq x\leq{\xi} \leq b.\end{cases}

uppfyllir:

\(i) Hlutafleiðurnar :math:`{\partial}_x^kF(x,{\xi})`,
:math:`k=0,\dots,m-2` eru til í sérhverjum punkti á
:math:`[a,b]\times [a,b]` og þær eru samfelldar.

\(ii) Hlutafleiðan :math:`{\partial}_x^{m-1}F(x,{\xi})` er til í öllum
punktum á :math:`[a,b]\times [a,b]` utan línunnar :math:`x={\xi}`. Í
punktum á línunni :math:`x={\xi}` tekur afleiðan stökkið
:math:`1/a_m({\xi})`. Nánar tiltekið, þá eru markgildin
:math:`{\partial}_x^{m-1}F({\xi}\pm,{\xi})=\lim\limits_{x\to{\xi}\pm} {\partial}_x^{m-1}F(x,{\xi})` til og

.. math::

  {\partial}_x^{m-1}F({\xi}+,{\xi})-
   {\partial}_x^{m-1}F({\xi}-,{\xi})=1/a_m({\xi}).

\(iii) :math:`P(x,D_x)F(x,{\xi})=0` ef :math:`x\neq {\xi}`.

--------------

Jöfnuhneppið

.. math::

  \left[\begin{matrix}
   B_1u_1 & B_1u_2 & \cdots & B_1u_m\\
   B_2u_1 & B_2u_2 & \cdots & B_2u_m\\
   \vdots& \vdots &\ddots & \vdots \\
   B_mu_1 & B_mu_2 & \cdots & B_mu_m\\
   \end{matrix}\right]
   \left[\begin{matrix}
   d_1({\xi}) \\ d_2({\xi}) \\ \vdots \\d_m({\xi})
   \end{matrix}\right]
   =\left[\begin{matrix}
   -B_1F(\cdot,{\xi}) \\
   -B_2F(\cdot,{\xi}) \\
   \vdots \\
   -B_mF(\cdot,{\xi}) \\
   \end{matrix}\right]

hefur ótvírætt ákvarðaða lausn :math:`d({\xi})=(d_1({\xi}),\dots,d_m({\xi}))`.
Hún er samfellt fall af :math:`{\xi}` á :math:`[a,b]`, því

.. math::

  B_jF(\cdot,{\xi}) = \sum\limits_{l=1}^m \beta_{jl}{\partial}_x^{l-1}
   G(b,{\xi}) 
   \qquad {\xi}\in ]a,b[

og við höfum markgildi af þessari stærð ef :math:`{\xi}\to a` og
:math:`{\xi}\to b`. Ef við setjum nú

.. math:: c_j=\int_a^b d_j({\xi})f({\xi})\, d{\xi},

og skilgreinum :math:`G_B` með formúlunni

.. math::

  G_B(x,{\xi}) = u_1(x)d_1({\xi})+\cdots+u_m(x)d_m({\xi})+
   F(x,{\xi}).

Þá er lausnin fundin:

Setning
^^^^^^^

Látum :math:`P(x,D)=a_m(x)D^m+\cdots+a_1(x)D+a_0(x)` vera afleiðuvirkja
á :math:`[a,b]` með samfellda stuðla, gerum ráð fyrir að
:math:`a_m(x)\neq 0` fyrir öll :math:`x\in [a,b]`, látum
:math:`B:C^{m-1}[a,b]\to {{\mathbb  C}}^m` vera jaðargildisvirkja og
gerum ráð fyrir að :math:`{\lambda}=0` sé ekki eigingildi :math:`P(x,D)`
á :math:`C^m_B[a,b]`. Þá hefur jaðargildisverkefnið

.. math:: P(x,D)u=f(x), \qquad Bu=0,

ótvírætt ákvarðaða lausn sem uppfyllir

.. math:: u(x) = \int_a^b G_B(x,{\xi})f({\xi})\, d{\xi},

þar sem fallið :math:`G_B` hefur eftirtalda eiginleika:

\(i) :math:`{\partial}_x^{k}G_B(x,{\xi})` er samfellt á
:math:`[a,b]\times [a,b]` fyrir :math:`k=0,\dots,m-2`.

\(ii)\ :math:`{\partial}_x^{m-1}G_B(x,{\xi})` er samfellt í öllum punktum
á :math:`[a,b]\times [a,b]` fyrir utan línuna :math:`x={\xi}` og tekur
stökkið :math:`1/a_m({\xi})` yfir hana.

\(iii) :math:`P(x,D_x)G_B(x,{\xi})=0` ef :math:`x\neq {\xi}`.

\(iv) :math:`BG_B(\cdot,{\xi})=0` ef :math:`{\xi}\in ]a,b[`,
þ.e. \ :math:`G_B` uppfyllir óhliðruð jaðarskilyrði, sem fall af fyrri
breytistærðinni.

Skilyrðin (i)-(iv) ákvarða fallið :math:`G_B` ótvírætt.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Í útreikningum okkar hér að framan sýndum við fram á að fallið
:math:`G_B` sem gefið er með 

.. math::

  G_B(x,{\xi}) = u_1(x)d_1({\xi})+\cdots+u_m(x)d_m({\xi})+
   F(x,{\xi}).

gefi okkur lausn á
jaðargildisverkefninu með formúlunni 

.. math:: u(x) = \int_a^b G_B(x,{\xi})f({\xi})\, d{\xi}

og að (iv) sé
uppfyllt. Skilyrðin (i)-(iii) leiða nú beint af hjálparsetningunni.

Til þess að sanna að :math:`G_B` sé ótvírætt ákvarðað, þá látum við
:math:`G^1_B` og :math:`G^2_B` vera tvö föll sem uppfylla (i)-(iv),
setjum :math:`H=G^1_B-G^2_B` og sýnum fram á að :math:`H` sé núllfallið.
Þá uppfyllir :math:`H` greinilega (i), (iii) og (iv). Samkvæmt (ii) er
hlutafleiðan :math:`{\partial}_x^{m-1}H(x,{\xi})` alls staðar til á
:math:`[a,b]\times [a,b]` fyrir utan línuna :math:`x={\xi}` og

.. math::

  \begin{gathered}
   {\partial}_x^{m-1}H({\xi}+,{\xi}) -
   {\partial}_x^{m-1}H({\xi}-,{\xi}) \\
   =  \big({\partial}_x^{m-1}G^1_B({\xi}+,{\xi}) -
   {\partial}_x^{m-1}G^1_B({\xi}-,{\xi})\big)
   -\big({\partial}_x^{m-1}G^2_B({\xi}+,{\xi})
   - \big({\partial}_x^{m-1}G^2_B({\xi}-,{\xi})\big)\\
   =1/a_m({\xi})-1/a_m({\xi})=0.\end{gathered}

Þar með er :math:`{\partial}_x^{m-1}H(x,{\xi})` samfellt á öllu
:math:`[a,b]\times [a,b]`. Nú segir (iii) okkur að

.. math::

  {\partial}_x^mH(x,{\xi})=\dfrac 1{a_m(x)}
   \bigg(-{\partial}_x^{m-1}H(x,{\xi})-\cdots-a_1(x){\partial}_x H(x,{\xi})
   -a_0(x)H(x,{\xi})\bigg)

ef :math:`x\neq {\xi}`. Í hægri hliðinni stendur fall, sem er samfellt
á öllu menginu :math:`[a,b]\times [a,b]`, svo
:math:`{\partial}_x^mH(x,{\xi})` er til í öllum punktum í
:math:`[a,b]\times [a,b]` og er samfellt þar. Þar með er
:math:`P(x,D_x)H(x,{\xi})=0` og :math:`BH(\cdot,{\xi})=0` fyrir öll
:math:`{\xi}\in ]a,b[`. Þetta gefur að :math:`H(x,{\xi})=0` fyrir öll
:math:`x\in [a,b]` og öll :math:`{\xi}\in]a,b[`. Fyrst :math:`H` er samfellt, þá
fáum við einnig :math:`H(x,a)=H(x,b)=0`.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Nú skulum við líta aftur á 
seinasta sýnidæmi og reikna út Green-fallið með
því að beita skilyrðunum (i)-(iv), sem einkenna það. Við byrjum á því að
finna tvær lausnir sem uppfylla jaðarskilyrðin í sitt hvorum endapunkti.
Þær eru :math:`\sin{\omega} x` og :math:`\sin {\omega}(1-x)`. Þá gefa skilyrðin (iii) og (iv)

.. math::

  G_B(x,{\xi})=\begin{cases} C({\xi})\sin{\omega}(1-x), &0\leq {\xi}<x\leq1,\\
   D({\xi})\sin{\omega}x, &0\leq x<{\xi}\leq 1.
   \end{cases}

Skilyrðið (i) segir að :math:`G_B` sé samfellt, svo

.. math:: C({\xi})\sin{\omega}(1-{\xi})=D({\xi})\sin{\omega}{\xi}

og (ii) segir að :math:`{\partial}_xG_B` taki stökkið :math:`-1` í
punktum þar sem :math:`x={\xi}` og því er

.. math::

  -{\omega}C({\xi})\cos{\omega}(1-{\xi})
   -{\omega}D({\xi})\cos{\omega}{\xi}=-1.

Stuðlarnir :math:`C({\xi})` og :math:`D({\xi})` uppfylla því
jöfnuhneppið

.. math::

  \left[\begin{matrix} \sin{\omega}(1-{\xi}) & -\sin{\omega}{\xi}\\
   \cos{\omega}(1-{\xi}) & \cos{\omega}{\xi}
   \end{matrix}\right]
   \left[\begin{matrix} C({\xi}) \\ D({\xi}) \end{matrix}\right] =
   \left[\begin{matrix} 0 \\ 1/{\omega} \end{matrix}\right].

Ákveða fylkisins er :math:`\sin{\omega}(1-{\xi})\cos{\omega}{\xi} +\sin{\omega}{\xi}\cos{\omega}(1-{\xi})=\sin{\omega}` og lausnin er því

.. math::

  \left[\begin{matrix} C({\xi}) \\ D({\xi})\end{matrix}\right]=
   \dfrac 1{\sin{\omega}} \left[\begin{matrix}
   \cos{\omega}{\xi} & \sin {\omega}{\xi}\\ 
   \cos{\omega}(1-{\xi}) & \sin{\omega}(1-{\xi})
   \end{matrix}\right]
   \left[\begin{matrix} 0\\ 1/{\omega}\end{matrix}\right].

Svarið er því fundið

.. math::

  G_B(x,{\xi}) =\begin{cases} 
   \dfrac{\sin{\omega}{\xi}\sin{\omega}(1-x)}{{\omega}\sin{\omega}}, 
   &0\leq {\xi}\leq x\leq 1,\\
   \dfrac{\sin{\omega}{x}\sin{\omega}(1-{\xi})}{{\omega}\sin{\omega}}, 
   &0\leq x\leq {\xi}\leq 1.\end{cases}

.. end-toggle::

Þetta dæmi er einfalt að alhæfa:

Setning
^^^^^^^

Látum :math:`P(x,D)=a_2(x)D^2+a_1(x)D+a_0(x)` vera annars stigs
afleiðuvirkja, þar sem :math:`a_2(x)\neq 0` fyrir öll
:math:`x\in [a,b]`, og gerum ráð fyrir að jaðarskilyrðin séu aðskilin, þ.e.a.s.

.. math::

  B_1u=\alpha_1u(a)-\beta_1u{{^{\prime}}}(a), \quad
   B_2u=\alpha_2u(b)+\beta_2u{{^{\prime}}}(b),

og :math:`(\alpha_1,\beta_1)\neq(0,0)`, :math:`(\alpha_2,\beta_2)\neq (0,0)`. Gerum ráð fyrir að :math:`u_1` og :math:`u_2` myndi grunn í
núllrúmi virkjans og

.. math:: B_1u_1=0, \qquad B_2u_2=0.

Þá er Green-fallið fyrir jaðargildisverkefnið

.. math:: P(x,D)u=f(x), \qquad Bu=0,

gefið með formúlunni

.. math::

  G_B(x,{\xi}) = \begin{cases} \dfrac{u_1({\xi})u_2(x)} 
   {a_2({\xi})W(u_1,u_2)({\xi})}, &a\leq {\xi}\leq x\leq b,\\
    \dfrac{u_1(x)u_2({\xi})} 
   {a_2({\xi})W(u_1,u_2)({\xi})}, &a\leq x\leq {\xi}\leq b,
   \end{cases}

þar sem :math:`W(u_1,u_2)` er Wronski-ákveða fallanna :math:`u_1` og
:math:`u_2`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

\(iii) og (iv) gefa að

.. math::

  G_B(x,{\xi}) = \begin{cases} C({\xi})u_2(x), &a\leq {\xi}< x\leq b,\\
    D({\xi})u_1(x), &a\leq x < {\xi}\leq b.
   \end{cases}

Skilyrðið (i) að :math:`G_B` sé samfellt á línunni :math:`x={\xi}`
gefur

.. math:: C({\xi})u_2({\xi})=D({\xi})u_1({\xi}).

og skilyrðið (ii) að afleiðan :math:`{\partial}_xG_B(x,{\xi})` taki
stökkið :math:`1/a_2({\xi})` yfir línuna :math:`x={\xi}` gefur

.. math:: C({\xi})u_2{{^{\prime}}}({\xi})-D({\xi})u_1{{^{\prime}}}({\xi})=1/a_2({\xi}).

Við getum nú sett þessi tvö skilyrði upp sem jöfnuhneppi

.. math::

  \left[\begin{matrix} u_2({\xi}) & -u_1({\xi}) \\
   u_2{{^{\prime}}}({\xi}) & -u_1{{^{\prime}}}({\xi})\end{matrix}\right]
   \left[\begin{matrix} C({\xi}) \\ D({\xi})\end{matrix}\right]
   =\left[\begin{matrix} 0 \\ 1/a_2({\xi})\end{matrix}\right].

Svarið verður því

.. math::

  \begin{aligned}
   \left[\begin{matrix} C({\xi}) \\ D({\xi})\end{matrix}\right]&=
   \dfrac 1{-u_2({\xi})u_1{{^{\prime}}}({\xi})+u_1({\xi})u_2{{^{\prime}}}({\xi})}
   \left[\begin{matrix} -u_1{{^{\prime}}}({\xi}) & u_1({\xi}) \\
   -u_2{{^{\prime}}}({\xi}) & u_2({\xi})\end{matrix}\right]
   \left[\begin{matrix} 0 \\ 1/a_2({\xi})\end{matrix}\right]\\
   &=\dfrac 1{a_2({\xi})W(u_1,u_2)({\xi})} 
   \left[\begin{matrix} u_1({\xi}) \\ u_2({\xi})\end{matrix}\right].\end{aligned}

.. end-toggle::

Eiginfallaliðun og Green–föll
-----------------------------

Eiginfallaliðun og Green–föll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Í greininni um eigingildisverkefni af Sturm-Liouville gerð sáum við að eiginfallaröð fallsins :math:`f` er
samleitin í jöfnum mæli á :math:`[a,b]` ef :math:`f\in C^2_B[a,b]`. Við
höfum einnig andhverfuformúlu fyrir eiginfallaraðir af föllum sem eru
samfellt deildanleg á köflum:

Setning
^^^^^^^

Ef :math:`f\in PC^1[a,b]`, þá er

.. math::

  \dfrac 12\big( f(x+)+f(x-)\big) =
   \sum\limits_{n=0}^{\infty}c_n(f)u_n(x), \qquad x\in]a,b[

og í punktum :math:`x` þar sem :math:`f` er samfellt gildir

.. math::

  f(x)=
   \sum\limits_{n=0}^{\infty}c_n(f)u_n(x), \qquad x\in]a,b[.

--------------

Með því að hliðra punktinum :math:`a` í :math:`0`, þá getum við alltaf
gert ráð fyrir að bilið sé :math:`[0,L]`. Þá fæst

Setning
^^^^^^^

(*Samleitnisetning Sturms*).   Látum
:math:`f` vera heildanlegt fall á bilinu :math:`[0,L]`, látum
:math:`c_n(f)` vera Fourier-stuðla :math:`f` með tilliti til
eiginfallarununnar :math:`(u_n)` og :math:`a_n(f)` tákna
Fourier–kósínus–stuðla :math:`f`. Þá eru raðirnar

.. math::

  \sum\limits_{n=0}^{\infty}c_n(f)u_n(x) \qquad \text{ og } \qquad
   \sum\limits_{n=0}^{\infty}a_n(f)\cos(n{\pi}x/L)

samleitnar í sömu punktum og í sérhverjum samleitnipunkti eru markgildi
þeirra þau sömu.

--------------

Það er mjög erfitt að sanna þessa setningu og við getum ekki fengist við
það hér.

Lítum nú aftur á jaðargildisverkefnið

.. math:: Lu=f(x), \qquad x\in ]a,b[, \qquad Bu=0,

þar sem :math:`L` er virki af Sturm–Liouville–gerð og gerum ráð fyrir að
hann sé reglulegur og samhverfur með tilliti til jaðarskilyrðanna
:math:`Bu=0`. Í því tilfelli að :math:`{\lambda}=0` er eigingildi, þá
gerum við ráð fyrir að :math:`f` sé hornrétt á eiginrúmið :math:`E_0`.
Við athugum nú að lausnin :math:`u` er gefin með formúlunni

.. math:: u(x)=\sum\limits_{n=0}^{\infty} \dfrac {c_n(f)}{\lambda_n}u_n(x)

ef þessi röð er nógu hratt samleitin til þess að við megum láta virkjann
:math:`L` verka lið fyrir lið í summunni. Þetta sjáum við með

.. math::

  Lu(x)=\sum\limits_{n=0}^{\infty} \dfrac{c_n(f)}{\lambda_n}Lu_n(x)
   =\sum\limits_{n=0}^{\infty} {c_n(f)}u_n(x)=f(x).

Í því tilfelli að :math:`{\lambda}_n=0` fyrir eitthvert :math:`n`, þá
setjum við inn :math:`0` í stað :math:`c_n(f)/{\lambda}_n` í
formúlunni fyrir :math:`u(x)`. Nú stingum við inn formúlunni fyrir stuðlana
:math:`c_n(f)` og skiptum á óendanlegu summunni og heildinu

.. math::

  \begin{aligned}
   u(x)&= \sum\limits_{n=0}^{\infty} \dfrac 1{\lambda_n}
   \bigg(\int_a^b f({\xi})u_n({\xi}){\varrho}({\xi})\, d{\xi}\bigg)
   u_n(x)\\
   &=\int_a^b{\varrho}({\xi})\bigg(\sum\limits_{n=0}^{\infty} \dfrac{u_n(x)u_n({\xi})} 
   {\lambda_n}\bigg) f({\xi})\, d{\xi}.\nonumber\end{aligned}

Við vitum að Green–fallið fyrir jaðargildisverkefnið er
ótvírætt ákvarðað, svo við höfum

.. math::

  G(x,{\xi})={\varrho}({\xi})\sum\limits_{n=0}^{\infty}
   \dfrac{u_n(x)u_n({\xi})}{\lambda_n}.

Æfingardæmi
-----------

Æfingardæmi
~~~~~~~~~~~

Dæmi
^^^^

Umritið eftirfarandi afleiðuvirkja yfir á Sturm–Liouville–gerð:

.. math::

  \begin{aligned}
   \text{(Bessel)}
   \qquad & \qquad
   P(x,D_x)u = -\dfrac{d^ 2 u}{dx^ 2} -\dfrac 1x \dfrac{du}{dx} - 
   \bigg(1-\dfrac {n^ 2}{x^ 2}\bigg)u \\ 
   \text{(Chebychev)}\qquad & \qquad
   P(x,D_x)u = -(1-x^2)\dfrac{d^ 2 u}{dx^ 2} +x\dfrac{du}{dx} - n^2u \\ 
   \text{(Hermite
   )}\qquad & \qquad
   P(x,D_x)u = -\dfrac{d^ 2 u}{dx^ 2} +2x \dfrac{du}{dx} - 2nu \\ 
   \text{(Laguerre)}\qquad & \qquad
   P(x,D_x)u = -x\dfrac{d^ 2 u}{dx^ 2} - (1-x)\dfrac{du}{dx} - nu \\ 
   \text{(Legendre)}
   \qquad & \qquad
   P(x,D_x)u = -(1-x^ 2)\dfrac{d^ 2 u}{dx^ 2} +2x \dfrac{du}{dx} -
   n(n+1)u \end{aligned}

Dæmi
^^^^

Látum :math:`L` vera virkja af Sturm-Liouville-gerð með
:math:`p(a)=p(b)`. Ákvarðið skilyrði, sem stuðlarnir :math:`\alpha`,
:math:`\beta`, :math:`{\gamma}` og :math:`{\delta}` þurfa að uppfylla,
til þess að :math:`L` sé samhverfur með tilliti til jaðarskilyrðanna

.. math::

  \begin{gathered}
   B_1u=\alpha u(a)+\beta u{{^{\prime}}}(a)+u(b)=0,\\ 
   B_2u={\gamma}u(a)+{\delta}u{{^{\prime}}}(a)+u{{^{\prime}}}(b)=0.\end{gathered}

Dæmi
^^^^

Látum :math:`L` tákna afleiðuvirkjann

.. math:: Lu=P(x,D)u=-x^{-2}u{{^{\prime\prime}}}+x^{-3}u{{^{\prime}}}.

Sýnið að :math:`Le^{i\beta x^2}=4\beta^2e^{i\beta x^2}` gildi um
sérhverja tvinntölu :math:`\beta`. Notið þetta til þess að finna almenna
lausn á jöfnunni :math:`Lu={\lambda}u` og leysið síðan
eigingildisverkefnið

.. math:: Lu={\lambda}u, \qquad u(1)=u(2)=0.

Í hvaða innfeldi eru eiginföllin innbyrðis hornrétt?

Dæmi
^^^^

Leysið eigingildisverkefnið

.. math:: -u{{^{\prime\prime}}}={\lambda}u, \qquad u{{^{\prime}}}(0)+u(0)=0, \qquad u{{^{\prime}}}(1)-u(1)=0.

[Það dugir að sýna fram á tilvist eigingilda með því að teikna mynd.]

Dæmi
^^^^

\(i) Leysið eigingildisverkefnið

.. math::

  \begin{cases}
   -(1+x)^ 2 u{{^{\prime\prime}}}= \lambda u, & 0<x<1,\\
   u(0)=u(1)=0.
   \end{cases}

\(ii) Notið lausnina úr (i) til þess að finna lausnarformúlu fyrir
jaðargildisverkefnið

.. math::

  \begin{cases}
   \partial_t^ 2w(x,t) -(1+x)^ 2\partial_x^ 2w(x,t)=f(x,t),
   &0<x<1,\quad t>0,\\
   w(x,0)=\varphi(x), \ \partial_tw(x,0)=\psi(x), 
   & 0<x<1,\\
   w(0,t)=w(1,t)=0, & t>0.
   \end{cases}

Dæmi
^^^^

\(i) Leysið eigingildisverkefnið

.. math::

  \begin{cases}
   -\dfrac d{dx}\bigg( (1+x)^ 2 \dfrac{du}{dx}\bigg) = \lambda u, & 0<x<1,\\
   u{{^{\prime}}}(0)=u(1)=0.
   \end{cases}

\(ii) Notið lausnina úr (i) til þess að finna lausnarformúlu fyrir
jaðargildisverkefnið

.. math::

  \begin{cases}
   \partial_t w(x,t) -\partial_x\big((1+x)^ 2 \partial_xw(x,t)\big) =f(x,t),
   &0<x<1,\quad t>0,\\
   w(x,0)=\varphi(x), & 0<x<1,\\
   \partial_xw(0,t)=w(1,t)=0, & t>0.
   \end{cases}

Dæmi
^^^^

Sýnið að jaðargildisverkefnin:

\(i) :math:`-u{{^{\prime\prime}}}={\lambda}u`,
:math:`B_1u=u(0)-u({\pi})=0`,
:math:`B_2u=u{{^{\prime}}}(0)+u{{^{\prime}}}({\pi})=0`,

\(ii) :math:`-u{{^{\prime\prime}}}={\lambda}u`,
:math:`B_1u=2u(0)-u({\pi})=0`,
:math:`B_2u=2u{{^{\prime}}}(0)+u{{^{\prime}}}({\pi})=0`,

séu ekki samhverf, að allar tvinntölur séu eigingildi í (i) og að (ii)
hafi engin eigingildi.

Dæmi
^^^^

Látum :math:`L=P(x,D)` vera afleiðuvirkja af Sturm-Liouville-gerð, sem
er samhverfur með tilliti til jaðarskilyrðanna :math:`Bu=0`, þar sem
:math:`B` er almennur jaðargildisvirki á bilinu :math:`[a,b]`. Notið
eiginfallaliðun til þess að finna lausnarformúlu fyrir eftirfarandi
verkefni, ef gefið er fall :math:`w(x,t)`, sem uppfyllir hliðruðu
jaðarskilyrðin,

.. math::

  \begin{cases}
   \dfrac{{\partial} u}{{\partial}t}+P(x,D_x)u=0, &a<x<b, \ t>0,\\
   u(x,0)=0, & a<x<b,\\
   B_1u(\cdot,t)=g(t), \quad B_2u(\cdot,t)=h(t).
   \end{cases}

Hér táknar :math:`B_ju(\cdot,t)` að jaðargildisvirkinn :math:`B_j` eigi
að verka á :math:`u` sem fall af :math:`x` fyrir fast :math:`t`.

Dæmi
^^^^

Beitið eiginfallaliðun til þess að finna lausn á jaðargildisverkefninu

.. math::

  \begin{cases}
   \dfrac{{\partial} u}{\partial t}
   -{\kappa}\dfrac{{\partial}^2 u}{\partial x^2}=0, &0<x<L, \ t>0,\\
   u(x,0)=\varphi(x), &0<x<L,\\
   {\partial}_xu(0,t)=hu(L,t)+{\partial}_xu(L,t)=0, &t>0, \ h>0.
   \end{cases}

Dæmi
^^^^

Beitið eiginfallaliðun til þess að finna lausn á jaðargildisverkefninu

.. math::

  \begin{cases}
   {\Delta}u=\dfrac{{\partial}^2 u}{\partial x^2}+
   \dfrac{{\partial}^2 u}{\partial y^2}=0, &0<x<L, \ 0<y<L,\\
   {\partial}_yu(x,0)=hu(x,L)+{\partial}_yu(x,L)=0, &0<x<L,\\
   u(L,y)=0, \, u(0,y)=g(y), &0<y<L.
   \end{cases}

Dæmi
^^^^

Ákvarðið Green-föllin til úrlausnar á jaðargildisverkefnunum:

\(i) :math:`-u{{^{\prime\prime}}}=f(x)`,
:math:`x\in [0,1]`, :math:`u(0)=u{{^{\prime}}}(1)=0`.

\(ii) :math:`-u{{^{\prime\prime}}}=f(x)`, :math:`x\in [0,1]`,
:math:`u(0)=u{{^{\prime}}}(1)+hu(1)=0`, :math:`h>0`.

\(iii) :math:`-u{{^{\prime\prime}}}-\omega^2u=f(x)`,
:math:`x\in [0,1]`, :math:`u(0)=u{{^{\prime}}}(1)=0`.

\(iv) :math:`-u{{^{\prime\prime}}}+\omega^2u=f(x)`, :math:`x\in [0,1]`,
:math:`u(0)=u(1)=0`.

\(v) :math:`-u{{^{\prime\prime}}}+\omega^2u=f(x)`, :math:`x\in [0,1]`,
:math:`u(0)=u{{^{\prime}}}(1)+hu(1)=0`, :math:`h>0`.

Dæmi
^^^^

Ákvarðið Green-fallið fyrir jaðargildisverkefnið

.. math:: u{{^{\prime\prime\prime}}}=f(x), \quad x\in [0,1], \qquad u(0)=u{{^{\prime\prime}}}(0)=u{{^{\prime}}}(1)=0.

Dæmi
^^^^

Ákvarðið Green-fallið fyrir jaðargildisverkefnið

.. math::

  u{{^{\prime\prime}}}-\dfrac 2xu{{^{\prime}}}+\dfrac 2{x^2}u=f(x), \quad x\in[1,2], \qquad
   u(1)=u(2)=0.

Dæmi
^^^^

(*Tvöfaldar eiginfallaraðir*.) Látum :math:`P(x,D_x)` og
:math:`Q(y,D_y)` vera tvo afleiðuvirkja af Sturm-Liouville gerð og lítum
á jaðargildisverkefnið

.. math::

  \begin{cases}
   \dfrac {\partial u}{{\partial}t}+P(x,{\partial}_x)u
   +Q(y,{\partial}_y)u=0,  &0<x<L, \ 0<y<M, \ t>0,\\
   B_1^1u(\cdot,y,t)=B_2^1u(\cdot,y,t)=0, &0<y<M,\ t>0,\\ 
   B_1^2u(x,\cdot,t)=B_2^2u(x,\cdot,t)=0, &0<x<L,\ t>0,\\ 
   u(x,y,0)={\varphi}(x,y), &0<x<L, \  0<y<M,
   \end{cases}

þar sem :math:`B^1=(B_1^1,B_2^1)` og :math:`B^2=(B_1^2,B_2^2)` eru
aðskildir jaðargildisvirkjar á bilunum :math:`[0,L]` og :math:`[0,M]`.
Finnið lausnarformúlu fyrir þetta verkefni með þeirri lausnartilgátu að
hægt sé að liða :math:`u` í tvöfalda eiginfallaröð með stuðlum sem eru
háðir :math:`t`.
