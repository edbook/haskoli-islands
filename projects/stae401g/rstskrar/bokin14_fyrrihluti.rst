
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




