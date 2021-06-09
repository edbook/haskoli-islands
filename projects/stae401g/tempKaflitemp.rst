
Fourier-raðir
=============

Inngangur
---------

Lítum nú enn einu sinni á það verkefni að finna 
:hover:`sérlausn` á afleiðujöfnu

.. math::

  P(D)u=(a_mD^ m+a_{m-1}D^{m-1}+\cdots+a_1 D
   +a_0)u=f(x),

með fastastuðla. Fallið :math:`f:{{\mathbb  R}}\to {{\mathbb  C}}` er
sagt vera *lotubundið með lotuna* :math:`T\neq 0` 
eða :math:`T`-*lotubundið*, ef :math:`f(x+T)=f(x)`
fyrir öll :math:`x\in {{\mathbb  R}}`. Það er einmitt mjög algengt að
það sé áhugavert að leysa jöfnuna með :math:`T`-lotubundið fall
:math:`f` fyrir eitthvert :math:`T>0`. Fallið
:math:`f(x)=e^{in\omega x}` með :math:`\omega=2\pi/T` er dæmi um slíkt
fall og við vitum að sérlausn er auðfundin, ef
:math:`P(in\omega)\neq 0`, en hún er

.. math:: u_n(x)= \dfrac {e^{in\omega x}}{P(in\omega)}.

Ef við gerum ráð fyrir að hægt sé að setja fallið :math:`f` fram með
óendanlegri röð

.. math::

  f(x)=
   \sum\limits_{n=-\infty}^{+\infty} c_n e^{in\omega x}
   =\lim_{N\to +\infty}
   \sum\limits_{n=-N}^{N} c_n e^{in\omega x}

og :math:`P(in\omega)\neq 0` fyrir öll :math:`n=0,\pm 1,\pm 2,\dots`, þá
getum við tekið sams konar óendanlega línulega samantekt á sérlausnunum
:math:`u_n` og fengið sérlausn

.. math::

  u(x)=\sum\limits_{n=-\infty}^{+\infty}
   \dfrac{c_n}{P(i n\omega )} e^{i n \omega x}.

Ef þessi röð er það vel samleitin að það megi deilda hana lið fyrir lið,
þá fáum við

.. math::

  \begin{aligned}
   P(D)u(x)&=\sum\limits_{n=-\infty}^{+\infty}
   \dfrac{c_n}{P(i n\omega )}  P(D)e^{in\omega x}\\
   &= \sum\limits_{n=-\infty}^{+\infty} c_n e^{in\omega x} =
   f(x),\nonumber\end{aligned}

svo (:math:`u(x)` er sérlausn á jöfnunni. Viðfangsefni
þessa kafla er að finna skilyrði á lotubundið fall :math:`f` sem tryggir
að til sé framsetning á :math:`f` með röð eins og hér að framan.

Fourier–raðir af :math:`2\pi`-lotubundnum föllum
------------------------------------------------

Athugið að um sérhvert :math:`T`–lotubundið fall :math:`f` gildir

.. math:: f(x)=f(x\pm T)=f(x\pm 2T)=\cdots.

Ef :math:`f` er :math:`T`-lotubundið og :math:`S>0` þá er fallið
:math:`g(x)=f(Tx/S)` :math:`S`-lotubundið, því

.. math:: g(x+S)=f(T(x+S)/S)=f(Tx/S+T)=f(Tx/S)=g(x).

Þessi einfalda staðreynd segir okkur að allar upplýsingar, sem við
getum fundið um :math:`T`–lotubundin föll, sé hægt að yfirfæra á
:math:`S`–lotubundin föll með því að setja :math:`Tx/S` sem nýja breytu
í stað :math:`x`.

:math:`2\pi`-lotubundin föll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við ætlum fyrst að líta á föll með lotuna :math:`T=2\pi` og horntíðnina
:math:`\omega=2\pi/T=1` og nota formúlurnar hér að framan til þess að
yfirfæra þekkingu okkar á almenn :math:`T`-lotubundin föll. Föllin

.. math::

  \begin{gathered}
   1,\quad \cos x, \quad \sin x, \quad \cos 2x, \quad \sin 2x, \quad
   \cos 3x, \quad \sin 3x, \quad \dots\\
   e^{ix}, \quad e^{-ix}, \quad e^{2ix}, \quad e^{-2ix}, \quad e^{3ix},
   \quad e^{-3ix}, \quad \dots,\end{gathered}

eru öll :math:`2\pi`–lotubundin. Sama er að segja um föll :math:`f` sem
eru línulegar samantektir af þeim og föll :math:`f` sem eru sett fram
með samleitnum röðum af gerðinni

.. math::

  \begin{aligned}
   f(x)&= \tfrac 12 a_0+\sum\limits_{n=1}^\infty \big( a_n \cos nx + b_n
   \sin nx\big )\\
   &= \sum\limits_{n=-\infty}^{+\infty} c_n e^{inx} =
   \lim\limits_{N\to \infty} \sum\limits_{n=-N}^{N} c_n e^{inx}.\nonumber\end{aligned}

Athugum nú að

.. math::

  \int_{-\pi}^\pi e^{imx}e^{-inx}\, dx =
   \int_{-\pi}^\pi e^{i(m-n)x} \, dx =
   \begin{cases}
   2\pi, & m=n,\\
   \left[ \dfrac{e^{i(m-n)x}}{i(m-n)}\right]_{-\pi}^\pi=0, &m\neq n.
   \end{cases}

Ef fallið :math:`f` er gefið með óendanlegum röðum eins og hér að framan
og raðirnar eru samleitnar í jöfnum mæli, þá getum við
víxlað á heildi og óendanlegri summu, og það gefur okkur

.. math::

  \int_{-\pi}^\pi f(x) e^{-inx}\, dx =
   \sum\limits_{m=-\infty}^{+\infty} 
   c_m\int_{-\pi}^\pi e^{imx}e^{-inx}\, dx = 2\pi c_n.

Þetta segir okkur að stuðullinn :math:`c_n` sé *ótvírætt ákvarðaður* af
formúlunni

.. math:: c_n= \dfrac 1{2\pi}\int_{-\pi}^\pi f(x)e^{-inx}\, dx.

Formúlurnar

.. math::

  \begin{aligned}
     \cos(mx)\cos(nx)
   &=\tfrac12\big(\cos((m-n)x)+\cos((m+n)x)\big),\\
     \sin(mx)\sin(nx)
   &=\tfrac12\big(\cos((m-n)x)-\cos((m+n)x)\big),\\
     \sin(mx)\cos(nx)
   &=\tfrac12\big(\sin((m-n)x)+\sin((m+n)x)\big),\end{aligned}

gefa okkur

.. math::

  \begin{gathered}
   \int_{-\pi}^\pi \cos nx \, dx = 
   \int_{-\pi}^\pi \sin nx \, dx =0, \qquad n=1,2,\dots,\\
   \int_{-\pi}^\pi \cos mx \cos nx \, dx = 
   \int_{-\pi}^\pi \sin mx \sin nx \, dx = \begin{cases} \pi, & m=n,\\ 0, &
   m\neq n,\end{cases}, \ \  n,m=1,2,\dots,\\
   \int_{-\pi}^\pi \cos mx \sin nx \, dx = 0, \qquad n,m=1,2,\dots.\end{gathered}

Með því að heilda fyrri röðina :math:`\tfrac 12 a_0+\sum\limits_{n=1}^\infty \big( a_n \cos nx + b_n \sin nx\big )` lið fyrir lið og
notfæra okkur þessar formúlur, þá fáum við að stuðlarnir :math:`a_n` og
:math:`b_n` eru einnig ótvírætt ákvarðaðir

.. math::

  \begin{gathered}
   a_n=\dfrac 1\pi\int_{-\pi}^\pi f(x) \cos nx \, dx, \quad
   n=0,1,2,\dots 
   \\
   b_n=\dfrac 1\pi\int_{-\pi}^\pi f(x) \sin nx \, dx, \quad n=1,2,3,\dots.\label{8.2.5}\end{gathered}

Skilgreining á Fourier-stuðlum og Fourier-röðum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skilgreining
^^^^^^^^^^^^

Ef :math:`f\in L^1([-\pi,\pi])` er :math:`2\pi`–lotubundið, þá
skilgreinum við *Fourier–stuðla* fallsins
:math:`f` með

.. math::

  c_n= c_n(f)=
   \dfrac 1{2\pi}\int_{-\pi}^{\pi}e^{-in x}f(x)\, dx,
   \qquad n=0, \pm 1, \pm 2, \dots,

*Fourier–kósínus–stuðla* :math:`f` með

.. math::

  a_n=a_n(f) =\dfrac 1{\pi}\int_{-\pi}^\pi f(x)\cos nx \, dx, 
   \qquad n=0,1,2, \dots,

og *Fourier–sínus–stuðla* :math:`f` með

.. math::

  b_n=b_n(f) =\dfrac 1{\pi}\int_{-\pi}^\pi f(x)\sin nx \, dx, 
   \qquad n=1,2, \dots.

Raðirnar

.. math::

  \sum\limits_{n=-\infty}^{+\infty}c_n e^{inx} \qquad \text{ og } \qquad
   \tfrac 12 a_0 + \sum\limits_{n=1}^{\infty}
   \big(a_n\cos nx+b_n \sin nx\big)

kallast *Fourier–raðir* fallsins :math:`f`. Til
aðgreiningar köllum við síðari röðina :hover:`hornafallaröð`.

--------------

Athugið að fyrir :math:`T`–lotubundið fall :math:`f` þá er sama yfir
hvaða bil af lengdinni :math:`T` heildað er,

.. math::

  \int_{-T/2}^{T/2} f(x) \, dx = \int_0^T f(x) \, dx
   =\int_{\alpha}^{\alpha+T}f(x) \, dx, \qquad \text{ fyrir öll }
   \alpha\in {{\mathbb  R}}.

.. figure:: ./myndir/fig071.svg
    :align: center
    :alt: Heildi yfir eina lotu

    Mynd: Heildi yfir eina lotu

Þessa staðhæfingu er mjög auðvelt að sanna ef við gefum okkur að fallið
:math:`f` sé samfellt

.. math::

  \dfrac d{d\alpha}\bigg(\int_\alpha^{T+\alpha}f(x)\, dx\bigg)
   =\dfrac d{d\alpha}\bigg(\int_0^{T+\alpha}f(x)\, dx
   -\int_0^{\alpha}f(x)\, dx\bigg)
   =f(T+\alpha)-f(\alpha)=0.

Þetta segir okkur að í skilgreiningunni á Fourier–stuðlunum má heilda
yfir hvaða bil sem er af lengdinni :math:`2\pi`.

Reiknireglur fyrir Fourier–stuðla
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setning
^^^^^^^

Látum :math:`f, g\in L^ 1([-\pi,\pi])` vera :math:`2{\pi}`–lotubundin
föll.

\(i) Fourier–stuðlarnir eru línulegar varpanir á :math:`L^ 1([-\pi,\pi])`,

.. math::

  \begin{gathered}
   a_n(\alpha f+\beta g)= \alpha a_n(f)+\beta a_n(g), \qquad
   b_n(\alpha f+\beta g)= \alpha b_n(f)+\beta b_n(g), \\ 
   c_n(\alpha f+\beta g)= \alpha c_n(f)+\beta c_n(g).\end{gathered}

\(ii) Sambandið milli stuðlanna :math:`a_n(f)`, :math:`b_n(f)` og
:math:`c_n(f)` er gefið með

.. math::

  \begin{gathered}
   a_0 = 2c_0, \qquad a_n= c_n+c_{-n}, \qquad b_n=i(c_n-c_{-n}),\\
   c_0 = \tfrac 12 a_0, \qquad 
   c_n=\tfrac 12(a_n-ib_n), \qquad c_{-n}=\tfrac 12 (a_n+ib_n).\end{gathered}

\(iii) Ef :math:`g(x)=f(x+\alpha)`, þar sem
:math:`\alpha\in {{\mathbb  R}}`, þá er
:math:`c_n(g)=e^{in\alpha}c_n(f)` fyrir öll
:math:`n=0,\pm 1,\pm 2,\dots`.

\(iv) Ef :math:`f` er raungilt fall, þá eru :math:`a_n(f)` og
:math:`b_n(f)` rauntölur og :math:`c_{-n}(f)=\overline{c_n(f)}`.

\(v) Ef :math:`f` er jafnstætt fall, þá er :math:`b_n(f)=0` fyrir öll
:math:`n=1,2,3,\dots`, og

.. math:: a_n(f)=\dfrac 2\pi\int_0^ \pi f(x) \cos nx\, dx.

\(vi) Ef :math:`f` er oddstætt fall, þá er :math:`a_n(f)=0` fyrir öll
:math:`n=0,1,2,\dots` og

.. math:: b_n(f)= \dfrac 2\pi \int_0^ \pi f(x) \sin nx \, dx

\(vii) Ef :math:`f` og :math:`f{{^{\prime}}}` eru í
:math:`L^ 1([-\pi,\pi])`, þá er

.. math:: c_n(f{{^{\prime}}})= inc_n(f), \qquad n\in {{\mathbb  Z}}.

Ef :math:`f, f{{^{\prime}}}, \dots, f^{(m)}` eru í
:math:`L^ 1([-\pi,\pi])`, þá er

.. math:: c_n(f^{(k)})= (in)^ kc_n(f), \qquad 0\leq k\leq m, \qquad n\in {{\mathbb  Z}},

og um sérhvern afleiðuvirkja :math:`P(D)=a_mD^ m+\cdots+a_1D+a_0` með
fastastuðla gildir

.. math:: c_n(P(D)f)= P(in)c_n(f), \qquad n\in {{\mathbb  Z}}.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Allar þessar reglur leiða beint af skilgreiningunni, til dæmis (iii),

.. math::

  \begin{aligned}
   c_n(g)&=\dfrac 1{2\pi}\int_{-\pi}^\pi f(x+\alpha) e^{-inx}\, dx
   =\dfrac 1{2\pi}\int_{-\pi+\alpha}^{\pi+\alpha} f(t) e^{-in(t-\alpha)}\, dt\\
   &=e^{in\alpha}\dfrac 1{2\pi}\int_{-\pi}^{\pi} f(t) e^{-in t}\, dt
   =e^{in\alpha} c_n(f).\end{aligned}

Regla (vii) er hlutheildun

.. math::

  \begin{aligned}
   c_0(f{{^{\prime}}})&= \dfrac 1{2\pi}\int_{-\pi}^\pi f{{^{\prime}}}(x)\, dx
   =\dfrac 1{2\pi}(f(\pi)-f(-\pi)) = 0 =i0c_0(f),\\
   c_n(f{{^{\prime}}})&= \dfrac 1{2\pi}\int_{-\pi}^\pi f{{^{\prime}}}(x)e^{-inx}\, dx
   =\dfrac 1{2\pi}\left[f(x)e^{-inx}\right]_{-\pi}^\pi
   -\dfrac 1{2\pi}\int_{-\pi}^\pi f(x)(-in)e^{-inx}\, dx\\
   &=inc_n(f).\end{aligned}

Reglan fyrir hærri afleiður leiðir nú af þessu tilfelli með þrepun og
síðasta staðhæfingin er augljós afleiðing af henni.

.. end-toggle::

Nokkur sýnidæmi
~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Lítum á :math:`2\pi`–lotubundna fallið :math:`f` sem skilgreint er með

.. math::

  f(x)=\begin{cases}
   -1, &-\pi<x<0,\\
   1, &0<x<\pi,\\
   0, &x=0,\pi.
   \end{cases}

.. figure:: ./myndir/fig074.svg
    :align: center
    :alt: Kassabylgja

    Mynd: Kassabylgja

Þetta er oddstætt fall, svo :math:`a_n(f)=0` fyrir öll
:math:`n=0,1,2,\dots` og við höfum

.. math::

  \begin{aligned}
   b_n(f)&=\dfrac 2\pi \int_0^ \pi \sin (nx)\, dx 
   = \dfrac 2\pi\left[\dfrac{-\cos nx}n\right]_0^ \pi
   = \dfrac{2((-1)^ {n+1}+1)}{\pi n}\\
   &=\begin{cases} \dfrac 4{\pi n}, &\text{ef $n$ er oddatala},\\
   0, &\text{ef $n$ er slétt tala}.
   \end{cases}\end{aligned}

Nú er :math:`c_n=\frac 12(a_n-ib_n)=-ib_n/2` ef :math:`n>0` og
:math:`c_{-n}=\overline{c_n}`, svo við getum skrifað Fourier–röð
fallsins sem

.. math::

  \sum_{\substack{n=-\infty\\n\neq 0}}^ {+\infty}
   \dfrac {-i((-1)^{n+1}+1)}{\pi n}e^{inx} \qquad \text{ og }
   \qquad
   \sum\limits_{k=0}^ \infty \dfrac 4{(2k+1)\pi}\sin (2k+1)x.

Á eftirfarandi mynd sjáum við nokkrar hlutsummur Fourier–raðarinnar:

.. figure:: ./myndir/fig074b.svg
    :align: center
    :alt: Hlutsumma kassabylgju, :math:`N=3`

    Mynd: Hlutsumma kassabylgju, :math:`N=3`

.. figure:: ./myndir/fig074d.svg
    :align: center
    :alt: Hlutsumma kassabylgju, :math:`N=7`

    Mynd: Hlutsumma kassabylgju, :math:`N=7`

.. figure:: ./myndir/fig074e.svg
    :align: center
    :alt: Hlutsumma kassabylgju, :math:`N=25`

    Mynd: Hlutsumma kassabylgju, :math:`N=25`

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Lítum nú á fallið :math:`f` sem er :math:`2\pi`–lotubundið og skilgreint
er með formúlunni

.. math::

  f(x)=\begin{cases}
   x, & -\pi<x<\pi,\\
   0, & x=\pi.
   \end{cases}

.. figure:: ./myndir/fig075.svg
    :align: center
    :alt: Sög

    Mynd: Sög

Þetta er oddstætt fall, svo við fáum :math:`a_n=0` og

.. math::

  b_n=\dfrac 2\pi \int_0^ \pi x\sin nx\, dx
   =\dfrac 2\pi\left[ \dfrac{x(-\cos nx)}{n}\right]_0^ \pi
   +\dfrac 2{\pi n} \int_0^ \pi \cos nx \, dx =\dfrac {2(-1)^{n+1}}n.

Við getum skrifað Fourier–röð fallsins sem

.. math::

  \sum_{\substack{n=-\infty\\n\neq 0}}^ {+\infty}
   \dfrac {i(-1)^{n}}{n}e^{inx} \qquad \text{ og }
   \qquad
   \sum\limits_{n=1}^ \infty \dfrac {2(-1)^ {n+1}}n\sin n x.

Á eftirfarandi mynd sjáum við nokkrar hlutsummur Fourier–raðarinnar:

.. figure:: ./myndir/fig075b.svg
    :align: center
    :alt: Hlutsumma sagarinnar, :math:`N=2`

    Mynd: Hlutsumma sagarinnar, :math:`N=2`

.. figure:: ./myndir/fig075d.svg
    :align: center
    :alt: Hlutsumma sagarinnar, :math:`N=4`

    Mynd: Hlutsumma sagarinnar, :math:`N=4`

.. figure:: ./myndir/fig075e.svg
    :align: center
    :alt: Hlutsumma sagarinnar, :math:`N=20`

    Mynd: Hlutsumma sagarinnar, :math:`N=20`

.. end-toggle::

Þessi tvö sýnidæmi gefa okkur vísbendingar um að hlutsummur
Fourier-raðar fallsins :math:`f` stefni á :math:`f(x)` í flestum punktum
:math:`x`. Nú snúum við okkur að því að rannsaka samleitni Fourier-raða.

Innfeldi og Bessel–ójafnan
--------------------------

Innfeldi á :math:`L^2[-\pi,\pi]`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rifjum upp að :math:`L^2[-\pi,\pi]` samanstendur af öllum föllum
:math:`u` á :math:`[-\pi,\pi]` þannig að

.. math:: \int_{-\pi}^{\pi} |u(x)|^2\, dx <+\infty.

Cauchy-Schwarz-ójafna segir að fyrir föllin
:math:`u,v\in L^2[-\pi,\pi]` gildi

.. math::

  \int_{-\pi}^\pi|u(x)v(x)|\, dx \leq
   \bigg(\int_{-\pi}^{\pi} |u(x)|^2\, dx\bigg)^{\frac 12}
   \bigg(\int_{-\pi}^{\pi} |v(x)|^2\, dx\bigg)^{\frac 12}

Ef :math:`u, v\in L^2[-\pi,\pi]`, þá skilgreinum við innfeldið af
:math:`u` og :math:`v` með formúlunni

.. math::

  {{\langle u,v\rangle}} = \dfrac 1{2\pi}\int_{-\pi}^\pi u(x)\overline{v(x)}\,
   dx.

Við segjum að :math:`u` og :math:`v` séu :hover:`hornrétt, hornréttur`
ef :math:`{{\langle u,v\rangle}}=0`. Helstu
reiknireglur fyrir innfeldi eru

.. math::

  \begin{gathered}
   {{\langle \alpha u + \beta v,w\rangle}}= \alpha{{\langle u,w\rangle}} + \beta {{\langle v,w\rangle}},\\
   {{\langle u,\alpha v + \beta w\rangle}}= \overline\alpha {{\langle u,v\rangle}} + \overline
   \beta {{\langle u,w\rangle}},\\
   {{\langle u,v\rangle}} = \overline{{{\langle v,u\rangle}}},\\
   {{\langle u,u\rangle}}\geq 0.\end{gathered}

Síðasta reglan leyfir okkur að skilgreina :hover:`lengd`
eða :hover:`staðall` fallsins :math:`u` sem

.. math:: \| u\|= \sqrt{{{\langle u,u\rangle}}}.

Af Cauchy-Schwarz-ójöfnunni leiðir

.. math:: |{{\langle u,v\rangle}}|\leq \|u\|\|v\|.

Regla Pýþagórasar á :math:`L^2[-\pi,\pi]` og Bessel-ójafna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setning
^^^^^^^

(*Pýþagóras*).   Ef
:math:`u, v\in L^2[-\pi,\pi]` eru hornrétt, þá er

.. math:: \| u+v\|^2 = \|u\|^2 + \| v\|^2.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Þetta leiðir beint af reiknireglunum fyrir innfeldi

.. math::

  \|u+v\|^2 = {{\langle u+v,u+v\rangle}}={{\langle u,u\rangle}} +{{\langle u,v\rangle}} + {{\langle v,u\rangle}}
   +{{\langle v,v\rangle}}= \|u\|^2+\|v\|^2,

því :math:`{{\langle u,v\rangle}}={{\langle v,u\rangle}}=0`.

.. end-toggle::

Fjölskylda :math:`{\cal F}` af innbyrðis hornréttum föllum á
:math:`[-\pi,\pi]` er sögð vera *einingarrétt* 
ef :math:`\|u\|=1` fyrir öll :math:`u\in {\cal F}`. Sem dæmi getum við tekið

.. math::

  {\cal F}=\{e_n(x)=e^{inx} \, ; \, n\in {{\mathbb  Z}}\}
   \qquad \text{ og } \qquad 
   {\cal F}=\{1\}\cup \{\tfrac 12 \cos(nx), \tfrac 12\sin(nx)
   \, ; \, n=1,2,3,\dots\}.

Athugum að fyrir :math:`2\pi`–lotubundið fall
:math:`f\in L^1([-\pi,\pi])` gildir

.. math:: c_n(f)=\dfrac 1{2\pi}\int_{-\pi}^\pi f(x) e^{-inx}\, dx = {{\langle f,e_n\rangle}}.

Nú ætlum við að kanna samleitni á Fourier–röðum 
og byrjum á því að líta á hlutsummuna

.. math:: s_N(x)= \sum_{n=-N}^N c_n e^{inx}, \qquad c_n=c_n(f).

Ef :math:`-N\leq n\leq N`, þá er

.. math::

  {{\langle f-s_N,e_n\rangle}}={{\langle f,e_n\rangle}}-\sum\limits_{m=-N}^N
   c_m{{\langle e_m,e_n\rangle}} = c_n-c_n=0,

og af þessu leiðir síðan að

.. math::

  {{\langle f-s_N,s_N\rangle}}=\sum\limits_{n=-N}^N
   \overline{c_n}{{\langle f-s_N,e_n\rangle}}=0.

Athugum einnig að

.. math::

  \begin{aligned}
   \|s_N\|^2&
   ={{\langle \sum_{n=-N}^N c_n e^{inx},\sum_{m=-N}^N c_m e^{imx}\rangle}}\\
   &=\sum_{n=-N}^N \sum_{m=-N}^N c_n \overline {c_m} {{\langle 
   e^{inx},e^{imx}\rangle}}
   = \sum_{n=-N}^N |c_n|^2.\end{aligned}

Fyrst :math:`s_N` og :math:`f-s_N` eru innbyrðis hornrétt, þá gefur
setning Pýþagórasar

.. math::

  \sum\limits_{n=-N}^N |c_n|^2  
   = \|s_N\|^2 \leq \|s_N\|^2+\|f-s_N\|^2 = \|f\|^2
   =\dfrac 1{2\pi}\int_{-\pi}^\pi |f(x)|^2 \, dx.

Með því að láta :math:`N\to +\infty`, þá fæst

Setning
^^^^^^^

(*Bessel–ójafnan*).   Ef
:math:`f\in L^2([-\pi,\pi])` er :math:`2\pi`–lotubundið og hefur
Fourier-stuðla :math:`c_n=c_n(f)`, þá er

.. math::

  \sum\limits_{n=-\infty}^{+\infty}|c_n|^2 \leq \dfrac
   1{2\pi}\int_{-\pi}^\pi |f(x)|^2\, dx.

Fourier-raðir af föllum í :math:`PC^1({{\mathbb  R}})\cap C({{\mathbb  R}})`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við gera ráð fyrir því að
:math:`f\in PC^1({{\mathbb  R}})\cap C({{\mathbb  R}})`, þ.e. að
:math:`f` sé samfellt deildanlegt á köflum og samfellt á
:math:`{{\mathbb  R}}`, og að fallið :math:`f` sé einnig
:math:`2\pi`–lotubundið. Þá er til skipting

.. math:: -\pi=a_0<a_1<\cdots < a_m=\pi

á bilinu :math:`[-\pi,\pi]` þannig að :math:`f` er samfellt deildanlegt
á opnu bilunum :math:`(a_{j-1},a_j)` og hefur afleiðu frá hægri og
vinstri í punktunum :math:`a_j`. Með hlutheildun fáum við

.. math::

  \begin{aligned}
   c_n(f{{^{\prime}}}) &
   =\dfrac 1{2\pi} \int_{-\pi}^\pi f{{^{\prime}}}(x) e^{-inx}  \, dx
   =  \sum\limits_{j=1}^m \dfrac 1{2\pi} \int_{a_{j-1}}^{a_j} f{{^{\prime}}}(x)
   e^{-inx}\, dx\\ 
   &=  \sum\limits_{j=1}^m \bigg[
   \dfrac 1{2\pi} \bigg( f(a_j)e^{-ina_{j}} - f(a_{j-1})e^{-ina_{j-1}}\bigg)
   +\dfrac {in}{2\pi} \int_{a_{j-1}}^{a_j} f(x) e^{-inx}\, dx\bigg]\\ 
   &= \dfrac 1{2\pi}\bigg(f(\pi)(-1)^n-f(-\pi)(-1)^n\bigg) +in c_n(f)
   = in c_n(f).\end{aligned}

Af þessum útreikningi leiðir síðan:

Setning
^^^^^^^

Ef :math:`f\in PC^1({{\mathbb  R}})\cap C({{\mathbb  R}})` er
:math:`2\pi`–lotubundið, þá er :math:`c_n(f{{^{\prime}}})=inc_n(f)`,

.. math:: \sum\limits_{n=-\infty}^{+\infty} |c_n(f)|< +\infty,

og þar með er Fourier–röðin
:math:`\sum_{-\infty}^{+\infty}c_n(f)e^{inx}` samleitin í jöfnum mæli á
:math:`{{\mathbb  R}}`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Við erum búin að staðfesta formúluna
:math:`c_n(f{{^{\prime}}})=inc_n(f)`. Cauchy–Schwarz–ójafnan gefur

.. math::

  \begin{aligned}
   \sum\limits_{n=-N}^N |c_n(f)|&=
   |c_0(f)|+\sum\limits_{\substack{n=-N\\n\neq 0}}^N 
   |c_n(f{{^{\prime}}})|\cdot\dfrac 1{|n|}\\
   &\leq |c_0(f)|+\bigg(\sum\limits_{\substack{n=-N\\n\neq 0}}^N
   |c_n(f{{^{\prime}}})|^2\bigg)^{1/2}
   \bigg(\sum\limits_{\substack{n=-N\\ n\neq 0}}^N
   \dfrac 1{n^2}\bigg)^{1/2}\\
   &\leq |c_0(f)|+\bigg(\sum\limits_{n=-\infty}^{+\infty}
   |c_n(f{{^{\prime}}})|^2\bigg)^{1/2}
   \bigg(2\sum\limits_{n=1}^\infty
   \dfrac 1{n^2}\bigg)^{1/2}.\end{aligned}

Í hægri hliðinni standa samleitnar raðir, svo
:math:`\sum_{n=-\infty}^{+\infty}|c_n(f)|<+\infty`. Við höfum

.. math::

  \big|
   \sum_{-\infty}^{+\infty} c_n(f)e^{inx}
   -\sum_{-N}^{N} c_n(f)e^{inx}\big| \leq
   \sum_{|n|\geq N}|c_n(f)|.
   \big|

Hægri hliðin stefnir á :math:`0` ef :math:`N\to \infty` og því gildir
síðasta staðhæfingin.

.. end-toggle::

Andhverfuformúla Fouriers
-------------------------

Andhverfuformúla Fouriers
~~~~~~~~~~~~~~~~~~~~~~~~~

Nú erum við komin að meginniðurstöðu kaflans:

Setning
^^^^^^^

(*Andhverfuformúla Fouriers*).   Ef
:math:`f\in PC^1({{\mathbb  R}})` er :math:`2\pi`–lotubundið fall með
Fourier–stuðla :math:`c_n=c_n(f)`, Fourier-kósínus–stuðla
:math:`a_n=a_n(f)` og Fourier–sínus–stuðla :math:`b_n=b_n(f)`, þá gildir

.. math::

  \begin{aligned}
   \tfrac 12\big(f(x+)+f(x-)\big) &=
   \sum\limits_{n=-\infty}^{+\infty} c_ne^{inx} =
   \lim\limits_{N\to+\infty}\sum\limits_{n=-N}^{N} c_ne^{inx}\\
   &=\tfrac 12 a_0 + \sum\limits_{n=1}^\infty \big(a_n \cos nx + b_n\sin
   nx\big).\end{aligned}

Í punktum :math:`x` þar sem :math:`f` er samfellt gildir
:math:`f(x)=\tfrac 12\big(f(x+)+f(x-)\big)` og þar með er

.. math::

  f(x)=
   \sum\limits_{n=-\infty}^{+\infty} c_ne^{inx} 
   =\tfrac 12 a_0 + \sum\limits_{n=1}^\infty \big(a_n \cos nx + b_n\sin
   nx\big).

Ef :math:`f\in PC^1({{\mathbb  R}})\cap C({{\mathbb  R}})`, þá eru
raðirnar samleitnar í jöfnum mæli á :math:`{{\mathbb  R}}`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Við sönnum þetta í fjórum skrefum:

*Skref (i):* Gerum fyrst ráð fyrir því að :math:`x=0`, :math:`f` sé
samfellt í :math:`x` og :math:`f(0)=0`. Þá þurfum við að sanna að

.. math:: \lim_{N\to +\infty}\sum\limits_{n=-N}^{N} c_n(f)=0.

Við skilgreinum :math:`g(x)=  {f(x)}/{(1-e^{ix})}`,
:math:`x\in {{\mathbb  R}}`, :math:`x\neq 2\pi k` og
:math:`g(2\pi k)=0`, :math:`k\in {{\mathbb  Z}}`. Greinilegt er að
:math:`g` er :math:`2\pi`–lotubundið fall. Ef :math:`x\to 2\pi k`, þá
stefna bæði teljari og nefnari á :math:`0`, því :math:`f(0)=0` og
:math:`f` er :math:`2\pi`–lotubundið. Til þess að sanna að
:math:`g\in L^1([-\pi,\pi])`, þá dugir að sanna að :math:`g` hafi
markgildi bæði frá hægri og vinstri í :math:`x=0`. Það er auðvelt, því
:math:`f` er samfellt deildanlegt á köflum, samfellt í :math:`x=0` og
:math:`f(0)=0`, svo markgildin

.. math::

  f{{^{\prime}}}(0\pm) =\lim\limits_{x\to 0\pm}\dfrac {f(x)-f(0)}x =
   \lim\limits_{x\to 0\pm}\dfrac {f(x)}x

eru bæði til og það hefur í för með sér að

.. math::

  g(0\pm)= \lim\limits_{x\to 0\pm}\dfrac {f(x)}{1-e^{ix}} =
   \lim\limits_{x\to 0\pm}\dfrac {f(x)-f(0)}x
   \dfrac{x}{1-e^{ix}}=if{{^{\prime}}}(0\pm)

eru bæði til. Nú er

.. math::

  \begin{aligned}
   c_n(f)&= \dfrac 1{2\pi}\int_{-\pi}^\pi 
   (1-e^{ix})g(x) e^{-inx}\, dx\\
   &= \dfrac 1{2\pi}\int_{-\pi}^\pi
   g(x) e^{-inx}\, dx
   - \dfrac 1{2\pi}\int_{-\pi}^\pi 
   g(x) e^{-i(n-1)x}\, dx
   = c_n(g)-c_{n-1}(g).\end{aligned}

Þar með er

.. math::

  \sum\limits_{n=-N}^{N} c_n(f)=
   \sum\limits_{n=-N}^{N}
   \big(c_n(g)-c_{n-1}(g)\big)= c_{N}(g)-c_{-N-1}(g).

Nú segir ójafna Bessels okkur að :math:`c_n(g)\to 0` ef
:math:`|n|\to +\infty` og þar með er markgildið :math:`0`.

*Skref (ii):* Gerum ráð fyrir því að :math:`x=0` og :math:`\frac 12(f(0+)+f(0-))=0`. Við setjum :math:`\alpha=f(0+)` og
:math:`h(x)=f(x)-\alpha\varphi(x)`, þar sem :math:`\varphi` er
kassabylgjan í sýnidæminu hér að framan. Þá er

.. math::

  \begin{gathered}
   \lim_{x\to 0+}h(x)=\lim_{x\to 0+}(f(x)-\alpha\varphi(x))
   =\alpha-\alpha=0\\
   \lim_{x\to 0-}h(x)=\lim_{x\to 0-}(f(x)-\alpha\varphi(x))
   =-\alpha+\alpha=0\\\end{gathered}

svo :math:`h` uppfyllir skilyrðin í skrefi (i). Greinilega er
:math:`\sum_{n=-N}^{N} c_n(\varphi)=0`, svo

.. math::

  \frac 12(f(0+)+f(0-))=0=h(0)
   =\lim_{N\to +\infty} \sum_{n=-N}^{N} c_n(f)-\alpha c_n(\varphi)=
   \lim_{N\to +\infty} \sum_{n=-N}^{N} c_n(f).

*Skref (iii):* Gerum ráð fyrir að :math:`x=0` setjum
:math:`\alpha=\frac 12(f(0+)+f(0-))` og skilgreinum :math:`j(x)=f(x)-\alpha`. Fallið
:math:`j` uppfyllir skilyrðin í skrefi (ii) og við höfum
:math:`c_n(j)=c_n(f)`, ef :math:`n\neq 0`, og
:math:`c_0(j)=c_0(f)-\alpha`. Því er

.. math::

  0=\lim_{N\to +\infty} \sum_{n=-N}^{N} c_n(j)
   =\lim_{N\to +\infty} \sum_{n=-N}^{N} c_n(f)-\alpha.

og niðurstaðan verður

.. math::

  \frac 12(f(0+)+f(0-))=\alpha
   =\lim_{N\to +\infty} \sum_{n=-N}^{N} c_n(f).

*Skref (iv):* Látum nú :math:`\alpha` vera einhvern punkt í
:math:`{{\mathbb  R}}` og setjum :math:`k(x)=f(x+\alpha)`. Samkvæmt
reiknireglu (iii) er :math:`c_n(k)=e^{in\alpha} c_n(f)` og skref (iii)
gefur því

.. math::

  \begin{aligned}
   \frac 12(f(\alpha+)+f(\alpha-))
   &=\frac 12(k(0+)+k(0-))\\
   &=\lim_{N\to +\infty} \sum_{n=-N}^{N} c_n(k)
   =\lim_{N\to +\infty} \sum_{n=-N}^{N} e^{in\alpha} c_n(f).\end{aligned}

Síðasta staðhæfingin leiðir beint af setningunni um samleitni Fourier-raða í jöfnum mæli.

.. end-toggle::

Fourier-raðir :math:`T`-lotubundinna falla
------------------------------------------

Fourier-raðir :math:`T`-lotubundinna falla
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum nú ráð fyrir að :math:`T>0` og að fallið :math:`f` sé
:math:`T`–lotubundið og heildanlegt á sérhverju lokuðu og takmörkuðu
bili. Þá er fallið :math:`g(x)=f(Tx/2\pi)` lotubundið með lotuna
:math:`2\pi` og Fourier–stuðlar þess verða

.. math::

  c_n= \dfrac 1{2\pi} 
   \int\limits_{-\pi}^ \pi f((T/2\pi)x) e^{-inx} \, dx
   = \dfrac 1{T} 
   \int\limits_{-T/2}^{T/2} f(x) e^{-i(2\pi/T)nx} \, dx.

Út frá þessari formúlu skilgreinum við Fourier–stuðla fyrir :math:`f`:

Skilgreining
^^^^^^^^^^^^

Látum :math:`T>0` og setjum :math:`\omega=2\pi/T`. Ef
:math:`f\in L^1([-T/2,T/2])` er :math:`T`–lotubundið, þá skilgreinum við
*Fourier–stuðla* fallsins :math:`f` með

.. math::

  c_n=c_n(f) =\dfrac 1{T}\int_{-T/2}^{T/2} f(x)e^{-in\omega x}\, dx, 
   \qquad n=0, \pm 1, \pm 2, \dots,

*Fourier–kósínus–stuðla* :math:`f` með

.. math::

  a_n=a_n(f) =\dfrac 2{T}\int_{-T/2}^{T/2} f(x)\cos\big(
   n\omega x\big) \, dx,  
   \qquad n=0,1,2, \dots,

og *Fourier–sínus–stuðla* :math:`f` með

.. math::

  b_n=b_n(f) =\dfrac 2{T}\int_{-T/2}^{T/2} f(x)\sin\big(
   n\omega x\big)  \, dx, 
   \qquad n=1,2, \dots.

Raðirnar

.. math::

  \sum\limits_{n=-\infty}^{+\infty}c_n e^{in\omega x}
   \quad \text{ og } \quad
   \tfrac 12 a_0 +\sum\limits_{n=1}^{\infty}
   \big(a_n\cos\big(n\omega x\big)+b_n \sin \big( n\omega x\big)\big)

kallast *Fourier–raðir* fallsins :math:`f` og
til aðgreiningar köllum við þá síðari :hover:`hornafallaröð`.

--------------

Nú beitum við andhverfusetningu Fouriers á fallið :math:`g` reiknað í
punktinum :math:`\omega x`, :math:`f(x)=g(\omega x)`, og fáum þá að
fyrir :math:`f\in PC^ 1({{\mathbb  R}})` gildir

.. math::

  \tfrac 12\big(f(x+)+f(x-)\big) =
   \sum\limits_{n=-\infty}^{+\infty} c_ne^{in\omega x} 
   =\tfrac 12 a_0 + \sum\limits_{n=1}^\infty 
   \big(a_n\cos\big(n\omega x\big)+b_n \sin \big(n\omega x\big)\big),

ef :math:`f` er samfellt í :math:`x`, þá er

.. math::

  f(x)=
   \sum\limits_{n=-\infty}^{+\infty} c_ne^{in\omega x}
    = \tfrac 12 a_0 + \sum\limits_{n=1}^\infty \big(a_n \cos \big(
   n\omega x\big) + b_n\sin \big(n\omega x\big)\big)

og fyrir :math:`f\in PC^1({{\mathbb  R}})\cap C({{\mathbb  R}})`, þá
eru raðirnar samleitnar í jöfnum mæli á :math:`{{\mathbb  R}}`.
Reiknireglurnar eru nánast eins of fyrir :math:`2{\pi}`–lotubundin föll. Þær sem breytast eru:

Setning
^^^^^^^

Látum :math:`f,g\in L^1([-T/2,T/2])` vera :math:`T`–lotubundin föll og
:math:`\omega=2\pi/T`.

\(iii)' Ef :math:`g(x)=f(x+\alpha)`, þar sem
:math:`{\alpha}\in {{\mathbb  R}}`, þá er
:math:`c_n(g)=e^{i\alpha n\omega}c_n(f)`.

\(v)' Ef :math:`f` er jafnstætt fall, þá er
:math:`b_n(f)=0` fyrir öll :math:`n=1,2,3,\dots` og

.. math:: a_n(f)=\dfrac 4T\int_0^ {T/2} f(x) \cos(n\omega x)\, dx.

\(vi)' Ef :math:`f` er oddstætt fall, þá er
:math:`a_n(f)=0` fyrir öll :math:`n=0,1,2,\dots` og

.. math:: b_n(f)= \dfrac 4 T \int_0^ {T/2} f(x) \sin(n \omega x) \, dx.

\(vii)' Ef :math:`f` og :math:`f{{^{\prime}}}`
eru í :math:`L^ 1([-T/2,T/2])`, þá er

.. math:: c_n(f{{^{\prime}}})= (in\omega)c_n(f).

Ef :math:`f, f{{^{\prime}}}, \dots, f^{(m)}` eru í
:math:`L^ 1([-T/2,T/2])`, þá er

.. math:: c_n(f^{(k)})= \big(i n\omega \big)^ kc_n(f)

og um sérhvern afleiðuvirkja :math:`P(D)=a_mD^ m+\cdots+a_1D+a_0` með
fastastuðla gildir

.. math:: c_n(P(D)f)= P(i n\omega )c_n(f).

Parseval–jafnan
---------------

Parseval–jafnan
~~~~~~~~~~~~~~~

Látum nú :math:`f` vera :math:`T`–lotubundið fall í
:math:`L^1[-\tfrac 12 T,\tfrac 12 T]`. Við höfum séð að Fourier–röðin er
samleitin og hefur markfallið :math:`f`, ef
:math:`f\in PC^1({{\mathbb  R}})\cap C({{\mathbb  R}})`. Ef :math:`f` er
ekki samfellt í :math:`x`, þá er ekki víst að Fourier–röðin stefni á
:math:`f(x)`. Í framhaldi af þessu er hægt að spyrja sig hvort engu að
síður geti gilt

.. math:: f(x)=\sum\limits_{n=-\infty}^{+\infty}c_n(f) e^{in \omega x},

í einhverjum öðrum skilningi, en að

.. math::

  f(x)=\lim_{N\to +\infty}\sum\limits_{n=-N}^{N}c_n(f) e^{in \omega x},
   \qquad \text{ fyrir öll } x\in {{\mathbb  R}}.

Hér að framan skilgreindum við innfeldi og lengd af föllum í
:math:`L^2([-\pi, \pi])` og við sáum að setning Pýþagórasar segir okkur
að

.. math::

  \begin{gathered}
   \sum\limits_{n=-N}^N |c_n(f)|^2+
   \dfrac 1{2\pi}\int_{-\pi}^\pi |f(x)-s_N(x)|^2\, dx\\
   =\|s_N\|^2+\|f-s_N\|^2 = \|f\|^2
   =\dfrac 1{2\pi}\int_{-\pi}^\pi |f(x)|^2 \, dx,\end{gathered}

þar sem við skilgreindum hlutsummuna með formúlunni

.. math:: s_N(x)= \sum_{n=-N}^N c_n e^{inx}, \qquad c_n=c_n(f).

Nú ætlum við að sýna að :math:`\|f-s_N\|\to 0` ef :math:`N\to +\infty`.
Til þess þurfum við:

Hjálparsetning
^^^^^^^^^^^^^^

Látum :math:`V` vera vigurrúm með tvinntalnamargföldun og innfeldi sem
við táknum með :math:`{{\langle u,v\rangle}}`, :math:`u,v\in V`, gerum
ráð fyrir að :math:`M` sé endanlegt mengi og að fjölskyldan
:math:`{{\cal F}}=\{e_k; k\in M\}` sé einingarrétt. Fyrir sérhvert
:math:`u\in V` eru til ótvírætt ákvarðaðir vigrar :math:`u_1` og
:math:`u_2`, þannig að :math:`u_1` sé línuleg samantekt af vigrunum í
:math:`{{\cal F}}`, :math:`u=u_1+u_2` og :math:`u_2` sé hornréttur á
alla vigrana í :math:`{{\cal F}}`. Vigurinn :math:`u_1` er gefinn með
formúlunni

.. math:: u_1=\sum_{k\in M}{{\langle u,e_k\rangle}}e_k.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Við skilgreinum :math:`u_1` með þessari formúlu og setjum
:math:`u_2=u-u_1`. Þá er augljóslega :math:`u=u_1+u_2` og

.. math:: {{\langle u_2,e_m\rangle}} = {{\langle u,e_m\rangle}} -\sum\limits_{k\in M}{{\langle u,e_k\rangle}}{{\langle e_k,e_m\rangle}} = {{\langle u,e_m\rangle}}-{{\langle u,e_m\rangle}}=0,

sem segir okkur að :math:`u_2` sé hornréttur á :math:`e_m`. Hugsum
okkur nú að við höfum einhverja aðra framsetningu :math:`u=v_1+v_2`, þar
sem :math:`v_1=\sum_{k\in M}a_ke_k` og :math:`v_2` er hornréttur á
:math:`e_m` fyrir öll :math:`m`. Þá er

.. math::

  {{\langle u,e_m\rangle}} = {{\langle v_1,e_m\rangle}}= \sum\limits_{k\in M}
   a_k{{\langle e_k,e_m\rangle}} = a_m.

Þetta segir okkur að :math:`u_1=v_1` og af því leiðir :math:`u_2=v_2`.

.. end-toggle::

Hjálparsetning
^^^^^^^^^^^^^^

Ef :math:`V` er vigurrúm með tvinntalnamargföldun og innfeldi, :math:`M`
er endanlegt mengi og :math:`{{\cal F}}=\{e_k; k\in M\}` er einingarrétt
fjölskylda af vigrum í :math:`V`, þá tekur fallið

.. math:: \| u-\sum\limits_{k\in M}a_ke_k\|

lægsta hugsanlega gildi þegar stuðlarnir eru valdir sem
:math:`a_k={{\langle u,e_k\rangle}}`, :math:`k\in M`.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Við setjum :math:`v=\sum_{k\in M}a_ke_k` og skrifum :math:`u=u_1+u_2`
eins og í sönnun á hjálparsetningu hér að framan. Þá er :math:`u_2` hornréttur á
:math:`u_1-v` og þar með gefur setning Pýþagórasar

.. math::

  \|u-v\|^ 2
   =\|u_1-v\|^ 2+\|u_2\|^ 2\geq \|u_2\|^ 2=\|u-\sum\limits_{k\in
   M}{{\langle u,e_k\rangle}}e_k\|^ 2.

.. end-toggle::

Í því tilfelli að :math:`V` samanstendur af öllum heildanlegum föllum á
bilinu :math:`[-\pi,\pi]`, með innfeldið

.. math:: {{\langle u,v\rangle}} = \dfrac 1{2\pi}\int_{-\pi}^ \pi u(x)\overline{v(x)}\, dx,

mengið :math:`M` er valið sem
:math:`M=\{n\in {{\mathbb  Z}}; -N\leq n\leq N\}` og
:math:`e_n(x)=e^{inx}`, þá segir hjálparsetningin að
heildið

.. math::

  \dfrac 1{2\pi}\int_{-\pi}^ \pi |f(x)-\sum\limits_{n=-N}^ N
   a_ne^{inx}|^ 2 \, dx

taki lægsta gildi ef stuðlarnir :math:`a_n` eru valdir sem
Fourier–stuðlar fallsins :math:`f`,

.. math:: a_n=c_n(f)=\dfrac 1{2\pi}\int_{-\pi}^ \pi f(x)e^{-inx}\, dx.

Nú vitum við að í því tilfelli að
:math:`f\in PC^1({{\mathbb  R}})\cap C({{\mathbb  R}})`, þá er
Fourier–röð fallsins :math:`f` samleitin í jöfnum mæli á
:math:`{{\mathbb  R}}` með markgildið :math:`f(x)`. Fyrir almennt fall
:math:`f` í :math:`L^1([-\pi,\pi])` þurfum við að gera nálgun með
föllum, sem eru samfellt deildanleg á köflum:

Hjálparsetning
^^^^^^^^^^^^^^

Ef :math:`f\in L^2([-\pi,\pi])` er :math:`2\pi`–lotubundið og
:math:`\varepsilon>0`, þá er til
:math:`f_\varepsilon\in PC^1({{\mathbb  R}})\cap C({{\mathbb  R}})`
þannig að

.. math::

  \dfrac 1{2\pi}\int_{-\pi}^\pi |f(x)-f_\varepsilon(x)|^2 \, dx
   <\varepsilon.

--------------

Við eftirlátum lesandanum sönnunina, en hún felst í því að nálga grafið
af :math:`f` með samfelldum ferli sem samanstendur af línustrikum.

Parseval-jafnan
~~~~~~~~~~~~~~~

Setning
^^^^^^^

Látum :math:`T>0` og :math:`\omega=2\pi/T`. Ef
:math:`f\in L^2[-T/2,T/2]` er :math:`T`–lotubundið, þá gildir

.. math::

  \|f-s_N\|^2=\dfrac 1{T}\int_{-T/2}^{T/2} |f(x)-\sum_{n=-N}^{N}
   c_n(f) e^{in \omega x}|^2\, dx \to 0, \qquad N\to +\infty.

og af þessu leiðir Parseval–jafna

.. math::

  \sum_{n=-\infty}^{+\infty} |c_n(f)|^2 = \dfrac 1{T}\int_{-T/2}^{T/2}
   |f(x)|^2 \, dx.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Það dugir að sanna setninguna fyrir :math:`2\pi`-lotubundin föll. Látum
:math:`\varepsilon>0` vera gefið og veljum :math:`f_\varepsilon\in PC^1({{\mathbb  R}})\cap C({{\mathbb  R}})` þannig að næst síðasta hjálparsetning gildi og veljum :math:`N_\varepsilon` það stórt að

.. math::

  \dfrac 1{2\pi}\int_{-\pi}^\pi |f_\varepsilon(x)-\sum_{n=-N}^{N}
   c_n(f_\varepsilon) e^{inx}|^2 \, dx <\varepsilon,
   \qquad N\geq N_{\varepsilon}.

Þá gefur sama hjálparsetning að

.. math::

  \begin{aligned}
   \|f(x)-\sum_{n=-N}^{N}c_n(f)e^{inx}\|^2
   &\leq \|f(x)-\sum_{n=-N}^{N}c_n(f_\varepsilon)e^{inx}\|^2\\
   &\leq \|f-f_\varepsilon\|^2 +
   \|f_\varepsilon(x)-\sum_{n=-N}^{N}c_n(f_\varepsilon)e^{inx}\|^2\leq
   2\varepsilon.\end{aligned}

Þegar samleitnin er komin þá leiðir Parseval-formúlan af

.. math::

  \sum\limits_{n=-N}^N |c_n|^2 +\|f-s_N\|^2 
   =\|s_N\|^2+\|f-s_N\|^2
   = \|f\|^2
   =\dfrac 1{2\pi}\int_{-\pi}^\pi |f(x)|^2 \, dx

.. end-toggle::

Kósínus– og sínus–raðir á endanlegum bilum
------------------------------------------

Jafnstæð lotubundin framlenging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú ætlum við líta á fall :math:`f:[0,L]\to {{\mathbb  C}}` á takmörkuðu
bili og fjalla um það hvernig hægt er að setja :math:`f` fram með
Fourier–röðum. Það er gert með því að framlengja skilgreiningarsvæði
:math:`f` yfir á allan rauntalnaásinn, þannig að út komi
:math:`2L`–lotubundið fall. Við skilgreinum

.. math::

  f_J(x)=\begin{cases} f(x), & x\in [0,L],\\  f(-x), & x\in
    [-L,0],\end{cases}

og setjum :math:`f_J(x)=f_J(x-2nL)` ef :math:`x\in [(2n-1)L,(2n+1)L]`.
Þá er :math:`f_J` greinilega jafnstætt fall og :math:`T`–lotubundið með
:math:`T=2L`.

.. figure:: ./myndir/fig076.svg
    :align: center
    :alt: 

.. figure:: ./myndir/fig076b.svg
    :align: center
    :alt: Jafnstæð :math:`2L`-lotubundin framlenging :math:`f`.

    Mynd: Jafnstæð :math:`2L`-lotubundin framlenging :math:`f`.

Fourier-stuðlar :math:`f_J` eru gefnir með

.. math::

  \begin{aligned}
   a_n(f_J)&=\dfrac 1L \int_{-L}^L f_J(x)\cos \dfrac {n\pi}L
   x \, dx\\
   &=\dfrac 2L \int_{0}^L f_J(x)\cos \dfrac {n\pi}L
   x \, dx\\
   &=\dfrac 2L \int_{0}^L f(x)\cos\dfrac {n\pi}L
   x \, dx, \qquad n=0,1,2,\dots,\\
   b_n(f_J)&=0 \qquad \qquad \qquad\qquad n=1,2,3,\dots.\end{aligned}

Oddstæð lotubundin framlenging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við getum einnig skilgreint oddstætt :math:`T`–lotubundið fall
:math:`f_O` með formúlunni

.. math::

  f_O(x)=\begin{cases} f(x), & x\in ]0,L[,\\ -f(-x), & x\in ]-L,0[,\\
   0, & x=nL, \quad n\in {{\mathbb  Z}}.\end{cases}

og :math:`f_O(x)=f_O(x-2nL)` ef :math:`x\in [(2n-1)L,(2n+1)L]`. Þá er
:math:`f_O` oddstætt og :math:`T`–lotubundið.

.. figure:: ./myndir/fig077.svg
    :align: center
    :alt: 

.. figure:: ./myndir/fig077b.svg
    :align: center
    :alt: Oddstæð :math:`2L`-lotubundin framlenging :math:`f`.

    Mynd: Oddstæð :math:`2L`-lotubundin framlenging :math:`f`.

Fourier–stuðlarnir eru

.. math::

  \begin{aligned}
   a_n(f_O)&=0 \qquad\qquad\qquad \qquad n=0,1,2,\dots,\\
   b_n(f_O)&=\dfrac 1L \int_{-L}^L f_O(x)\sin \dfrac {n\pi}L
   x  \, dx\\
   &=\dfrac 2L \int_{0}^L f_O(x)\sin \dfrac {n\pi}L
   x  \, dx\\
   &=\dfrac 2L \int_{0}^L f(x)\sin \dfrac {n\pi}L
   x  \, dx, \qquad n=1,2,\dots.\\\end{aligned}

Skilgreining á Fourier-stuðlum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skilgreining
^^^^^^^^^^^^

Látum :math:`f:[0,L]\to {{\mathbb  C}}` vera heildanlegt fall. Við
skilgreinum *Fourier–kósínus–stuðla* 
fallsins :math:`f` með

.. math::

  a_n=a_n(f)=\dfrac 2L \int_{0}^L 
   f(x)\cos \dfrac {n\pi}Lx \, dx

og *Fourier–sínus–stuðla* :math:`f` með

.. math::

  b_n=b_n(f)=\dfrac 2L \int_{0}^L 
   f(x)\sin \dfrac {n\pi}Lx  \, dx.

Röðin

.. math:: \tfrac 12 a_0 + \sum_{n=1}^\infty a_n \cos  \dfrac {n\pi} L x

kallast *Fourier–kósínus–röð* fallsins
:math:`f` og röðin

.. math:: \sum_{n=1}^\infty b_n\sin \dfrac {n\pi} L x

kallast *Fourier–sínus–röð* fallsins :math:`f`.

Andhverfuformúla Fouriers
~~~~~~~~~~~~~~~~~~~~~~~~~

Með því að beita andhverfusetningu Fouriers annars vegar á fallið
:math:`f_J` og hins vegar á fallið :math:`f_O`, þá fáum við:

Setning
^^^^^^^

(*Andhverfuformúla Fouriers*).   Ef :math:`f\in PC^1([0,L])` hefur
Fourier–kósínus–stuðla :math:`a_n=a_n(f)` og Fourier–sínus–stuðla
:math:`b_n=b_n(f)`, þá er

.. math::

  \tfrac 12(f(x+)+f(x-)) = \tfrac 12 a_0 +\sum\limits_{n=1}^\infty a_n
   \cos  \dfrac {n\pi} L x  = \sum\limits_{n=1}^\infty
   b_n \sin  \dfrac {n\pi} L x , \qquad x\in ]0,L[.

Ef :math:`x\in ]0,L[` og :math:`f` er samfellt í :math:`x`, þá er

.. math::

  f(x) = \tfrac 12 a_0 +\sum\limits_{n=1}^\infty a_n
   \cos  \dfrac {n\pi} L x  = \sum\limits_{n=1}^\infty
   b_n \sin  \dfrac {n\pi} L x .

Ef :math:`f\in PC^1([0,L])\cap C([0,L])`, þá er Fourier–kósínus–röðin
samleitin í jöfnum mæli á :math:`[0,L]`. Ef að auki gildir
:math:`f(0)=f(L)=0`, þá er Fourier–sínus–röðin einnig samleitin í jöfnum
mæli á :math:`[0,L]`.

Sýnidæmi um lotubundnar framlengingar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Lítum á fallið :math:`f(x)=x`, :math:`x\in [0,L]`. Kósínus-stuðlar þess
eru

.. math::

  \begin{aligned}
   a_0&= \dfrac 2L \int_0^L x\, dx = L,\\
   a_n&= \dfrac 2L \int_0^L x\cos  \dfrac {n\pi}L x  \, dx 
   =\dfrac 2L\left[\dfrac {xL}{n\pi} \sin \dfrac {n\pi} L 
   x \right]_0^L
   -\dfrac 2{n\pi}\int_0^L \sin \dfrac {n\pi}L x  \, dx\\
   &= 0 -\dfrac 2{n\pi}\left[-\dfrac L{n\pi}
   \cos \dfrac {n\pi}L x \right]_0^L
   =\dfrac {2L(\cos n\pi-1)}{n^2\pi^2} =\dfrac {2L((-1)^n-1)}{n^2\pi^2}.\end{aligned}

Niðurstaðan verður því að

.. math::

  x= \dfrac L2 +\dfrac {2L}{\pi^2}\sum_{n=1}^{\infty}\dfrac{(-1)^n-1}{n^2}
   \cos \dfrac{n\pi}L x, \qquad x\in ]0,L[.

Fourier–kósínus–röðin í hægri hlið jöfnunnar stefnir síðan á
:math:`2L`–lotubundnu framlenginguna :math:`f_J` á fallinu :math:`f`.

.. figure:: ./myndir/fig078.svg
    :align: center
    :alt: 

.. figure:: ./myndir/fig078b.svg
    :align: center
    :alt: Jafnstæð :math:`2L`-lotubundin framlenging :math:`f`.

    Mynd: Jafnstæð :math:`2L`-lotubundin framlenging :math:`f`.

Lítum nú á sínus–stuðlana

.. math::

  \begin{aligned}
   b_n&= \dfrac 2L\int_0^L x\sin \dfrac{n\pi}L x  \, dx
   =\dfrac 2L\left[-\dfrac{xL}{n\pi}\cos  \dfrac {n\pi}L x  \right]_0^L
   +\dfrac 2{n\pi}\int_0^L \cos  \dfrac {n\pi}L x  \, dx\\
   &= \dfrac {2L(-1)^{n+1}}{n\pi}+
   \dfrac {2L}{n^2\pi^2}\left[\sin \dfrac{n\pi}L x \right]_0^L
   = \dfrac {2L(-1)^{n+1}}{n\pi}.\end{aligned}

Andhverfuformúlan gefur nú

.. math::

  x=\sum_{n=1}^\infty \dfrac{2L(-1)^{n+1}}{n\pi}
   \sin \dfrac{n\pi}L x , \qquad x\in ]0,L[,

og Fourier–sínus–röðin stefnir á oddstæðu :math:`2L`–lotubundnu
framlenginguna :math:`f_O` á :math:`f`.

.. figure:: ./myndir/fig079.svg
    :align: center
    :alt: Sögin: Oddstæð :math:`2L`-lotubundin framlenging :math:`f`

    Mynd: Sögin: Oddstæð :math:`2L`-lotubundin framlenging :math:`f`

.. end-toggle::

Fourier–raðir og afleiðujöfnur
------------------------------

Fourier–raðir og afleiðujöfnur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú skulum við líta aftur á verkefnið að finna sérlausn á jöfnunni

.. math::

  P(D)u=(a_mD^ m+a_{m-1}D^{m-1}+\cdots+a_1 D
   +a_0)u=f(x),

þar sem fallið :math:`f` er :math:`T`–lotubundið. Til
einföldunar skulum við setja :math:`\omega=2\pi/T` og jafnframt gera ráð
fyrir því að í punktum :math:`x` þar sem :math:`f` er ósamfellt gildi
:math:`f(x)=\tfrac 12(f(x+)+f(x-))`. Ef :math:`f\in PC^1({{\mathbb  R}})`, þá gefur
andhverfuformúla Fouriers

.. math:: f(x)=\sum_{n=-\infty}^{+\infty} c_n(f)e^{in\omega x}, \qquad x\in {{\mathbb  R}}

Ef til er :math:`T`–lotubundin sérlausn :math:`u` á (8.1.1), þá fæst
sambandið milli Fourier–stuðla fallanna :math:`f` og :math:`u` úr
formúlunni

.. math:: c_n(f)=c_n(P(D)u) = P(in\omega)c_n(u).

Þetta segir okkur að til þess að :math:`T`–lotubundin lausn sé til, þá
verði :math:`P(in\omega)\neq 0` að gilda, ef :math:`c_n(f)\neq 0`.

Setning
^^^^^^^

Látum :math:`P` vera margliðu af stigi :math:`m` og lítum á jöfnuna

.. math:: P(D)u=(a_mD^m+a_{m-1}D^{m-1}+\cdots+a_1 D +a_0)u=f(x),

þar sem :math:`f\in PC^1({{\mathbb  R}})\cap C({{\mathbb  R}})` er
:math:`T`–lotubundið fall og setjum :math:`\omega=2\pi/T`. Ef
:math:`c_n(f)=0` fyrir öll :math:`n` þannig að :math:`P(in\omega)=0`, þá
fæst :math:`T`–lotubundin lausn af gerðinni

.. math::

  u(x)=\sum_{\substack{n=-\infty\\ P(in\omega)\neq 0}}^{+\infty}
   \dfrac{c_n(f)} {P(in\omega)} e^{in\omega x}, \qquad x\in {{\mathbb  R}}.

Sönnun
^^^^^^

.. begin-toggle:: :label: Sýna sönnun

Fyrst :math:`P` er margliða af stigi :math:`m`, þá er til fasti
:math:`C>0` þannig að

.. math:: \dfrac{|c_n(f)|}{|P(in\omega)|} \leq C\dfrac{|c_n(f)|}{|n|^m},

ef :math:`n` er nógu stórt. Fyrst
:math:`f\in PC^1({{\mathbb  R}})\cap C({{\mathbb  R}})`, þá er
:math:`\sum_{n=-\infty}^{+\infty}|c_n(f)|<+\infty` og með því að nota
Weierstrass–prófið, þá sjáum við að það má taka afleiður af :math:`u`
upp að stigi :math:`m` með því að deilda röðina lið fyrir lið. Við fáum
því

.. math::

  P(D)u= \sum_{\substack{n=-\infty\\ P(in\omega)\neq 0}}^{+\infty}
   \dfrac{c_n(f)} {P(in\omega)} P(D)e^{in\omega x}
   =\sum_{\substack{n=-\infty\\ P(in\omega)\neq 0}}^{+\infty}
   c_n(f) e^{in\omega x}=f(x).

.. end-toggle::

Skilgreining
^^^^^^^^^^^^

Látum :math:`f\in L^1([-T/2,T/2])` vera :math:`T`–lotubundið fall og
setjum :math:`\omega=2\pi/T`. Ef :math:`c_n(f)=0` fyrir öll :math:`n`
þannig að :math:`P(in\omega)= 0`, þá kallast fallið :math:`u`, í setningunni hér að ofan, *formlega lotubundna lausnin á* afleiðujöfnunni.

Sýnidæmi: Deyfðar sveifur með lotubundnum krafti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Deyfð sveifla; framhald

Lítum nú á hreyfikerfið, þar sem massi :math:`m` er tengdur við gorm með
fjaðurstuðulinn :math:`k` og höggdeyfi með deyfingarstuðulinn :math:`c`,
og gerum ráð fyrir að á massann verki :math:`T`–lotubundinn kraftur sem
gefinn er með fallinu :math:`f`.

.. figure:: ./myndir/fig0710.svg
    :align: center
    :alt: Deyfð sveifla með ytri krafti

    Mynd: Deyfð sveifla með ytri krafti

Hreyfijöfnan fyrir deifðan sveifil er

.. math:: mu{{^{\prime\prime}}}+ c u{{^{\prime}}}+ ku=f(t),

þar sem :math:`u(t)` er færsla massans frá jafnvægisstöðu.
Kennimargliða afleiðuvirkjans er

.. math:: P(\lambda)=m\lambda^2+c\lambda+k,

og þar með er

.. math::

  P(in\omega)= -mn^2\omega^2+cin\omega+k=
   m\big(\omega_0^2-n^2\omega^2+i(c/m)n\omega\big),

þar sem :math:`\omega_0^2=k/m`. Við höfum að :math:`c>0`, svo
:math:`P(in\omega)\neq 0` fyrir öll :math:`n\in {{\mathbb  Z}}`. Setningin hér fyrir framan segir
okkur að til sé :math:`T`–lotubundin lausn. Nú skulum við gera ráð fyrir
því að :math:`f` sé jafnstætt fall

.. math:: f(t)= \tfrac 12 a_0 + \sum_{n=1}^\infty a_n \cos\big(n\omega t\big).

Við höfum þá samkvæmt reiknireglu (ii) um Fourier-stuðla gildir að
:math:`c_n=c_{-n}=\tfrac 12 a_n` og því er

.. math::

  \begin{aligned}
   c_n(u) &= \dfrac {a_n(f)}{2P(in\omega)} 
   = \dfrac{a_n(f)}{2m\big((\omega_0^2-n^2\omega^2)+i(c/m)n\omega\big)} \\
   &= \dfrac
   {(\omega_0^2-n^2\omega^2)a_n(f)-i(cn\omega/m) a_n(f)}
   {2m\big((\omega_0^2-n^2\omega^2)^2+(cn\omega/m)^2)\big)}.\end{aligned}

Hornafallaröðin fyrir :math:`u` er því lesin út úr formúlunni
:math:`c_n(u)=\tfrac 12(a_n(u)-ib_n(u))`

.. math::

  \begin{aligned}
   u(t)= \dfrac {a_0}{2k}
    &+ \sum_{n=1}^\infty  
   \dfrac{(\omega_0^2-n^2\omega^2)a_n(f)}
   {2m\big((\omega_0^2-n^2\omega^2)^2+(cn\omega/m)^2\big)}
    \cos\big(n\omega t\big)\\
   &+  \sum_{n=1}^\infty  \dfrac{(cn\omega/m) a_n(f)}
   {2m\big((\omega_0^2-n^2\omega^2)^2+(cn\omega/m)^2\big)}
   \sin\big(n\omega t\big).\end{aligned}

Í því tilfelli að við höfum enga deyfingu, :math:`c=0`, þá verður þessi
formúla

.. math::

  u(t)= \dfrac {a_0}{2k} + \dfrac 1{2m}\sum_{n=1}^\infty
   \dfrac {a_n(f)}{\omega_0^2-n^2\omega^2} \cos\big(n\omega t\big),

og hún hefur aðeins merkingu ef :math:`a_N(f)=0` þegar
:math:`\omega_0=N\omega` fyrir eitthvert :math:`N`. Hugsum okkur nú að
:math:`\omega_0=N\omega` og að :math:`a_N(f)\neq 0`. Þá eru allar
lausnir á óhliðruðu jöfnunni :math:`P(D)u=0` línulegar samantektir
fallanna :math:`\cos \omega_0 t` og :math:`\sin \omega_0 t`. Hliðraða
jafnan :math:`P(D)u=\cos \omega_0 t` getur því ekki haft lausn af
þessari gerð. Við höfum séð hvernig hægt er að finna sérlausn af
svona jöfnu þegar :math:`i\omega_0` er núllstöð kennijöfnunnar af fyrsta
stigi,

.. math::

  u_p(t)= \dfrac {te^{i\omega_0 t}}{2P{{^{\prime}}}(i\omega_0)} +
   \dfrac {te^{-i\omega_0 t}}{2P{{^{\prime}}}(-i\omega_0)} 
   = \dfrac {t}{4i\omega_0}
   \bigg( e^{i\omega_0 t} - e^{-i\omega_0 t}\bigg) = 
   \dfrac{t\sin \omega_0t}{2\omega_0}.

Við fáum nú sérlausn á :math:`P(D)u=f`, með því að finna sérlausnir á
:math:`P(D)u_n=a_n(f)\cos n\omega t` liðunum í Fourier–röð :math:`f` og
leggja þær saman. Það gefur lausnina

.. math::

  u(t)= \dfrac {a_N(f)}{2mN\omega} t\sin \big(N\omega t\big) +
   \dfrac 1{2m}\sum_{\substack{n=1\\ n\neq N}}^{+\infty}
   \dfrac{a_n(f)}{\omega_0^2-n^2\omega^2} \cos\big(n\omega t\big).

Liðurinn :math:`a_N(f)\cos\big(N \omega t\big)` í Fourier–röð kraftsins
:math:`f(t)` veldur því að útstlagið :math:`u(t)` verður ótakmarkað.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi

Lítum nú á jaðargildisverkefnið

.. math:: u{{^{\prime\prime}}}+{\omega}^2 u=f(x), \qquad u(0)=u(1)=0.

Það hafur ótvírætt ákvarðaða lausn
fyrir sérhvert :math:`f` ef og aðeins ef :math:`{\omega}` er ekki
heiltölumargfeldi af :math:`{\pi}`. Hægt er að setja lausnina fram með
sínus–röð

.. math::

  u(x)=\sum\limits_{n=1}^{\infty} u_n \sin(n{\pi} x), \qquad
   u_n=b_n(u)=2\int_0^1 u(x)\sin(n{\pi} x)\, dx.

Ljóst er að jaðarskilyrðin eru uppfyllt. Við skulum nú ganga út frá því
að sínus–röð fallsins :math:`f` sé þekkt :math:`f_n=b_n(f)`. Þá fáum við
sambandið milli :math:`u_n` og :math:`f_n` með því að stinga röðinni
fyrir :math:`u` inn í afleiðujöfnuna

.. math::

  \begin{aligned}
   u{{^{\prime\prime}}}(x)+{\omega}^2u(x) 
   &=\sum\limits_{n=1}^{\infty} u_n\big(-n^2{\pi}^2+{\omega}^2\big)
   \sin(n{\pi}x) \\
   &=\sum\limits_{n=1}^{\infty} f_n
   \sin(n{\pi}x)=f(x).\end{aligned}

Stuðlarnir eru því :math:`u_n=f_n/({\omega}^2-n^2{\pi}^2)` og svarið
verður

.. math::

  u(x)=\sum\limits_{n=1}^{\infty} \dfrac{f_n}{{\omega}^2-n^2{\pi}^2}
   \sin (n{\pi}x).

.. end-toggle::

Sveiflandi strengur
~~~~~~~~~~~~~~~~~~~

.. _sysveiflandistrengurframhald:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Sveiflandi strengur; framhald

Við leiddum út einvíðu 
:hover:`bylgjujöfnuna, bylgjujafna`, sem lýsir hreyfingu sveiflandi strengs sem festur
er niður í báðum endapunktum. Við skulum nú leysa hana með náttúrulegu
jaðarskilyrðunum

.. math::

  \dfrac{{\partial}^2u}{{\partial}t^2}-
   c^2\dfrac{{\partial}^2u}{{\partial}x^2}=0, \qquad u(0,t)=u(L,t)=0,

og gera jafnframt ráð fyrir því að upphafsstaðan og hraðinn séu þekkt

.. math::

  u(x,0)=\varphi(x), \qquad {\partial}_tu(x,0)={\psi}(x), \qquad x\in
   ]0,L[.

Aðferðin byggir á því að skrifa upp liðun á :math:`u(x,t)` í sínus–röð
með tilliti til :math:`x`

.. math::

  u(x,t)=\sum\limits_{n=1}^{\infty} u_n(t)\sin(n{\pi}x/L), \qquad
   u_n(t)= \dfrac 2L\int_0^L u(x,t)\sin(n{\pi}x/L)\, dx,

og ganga út frá því að sínus–stuðlar fallanna :math:`\varphi` og
:math:`{\psi}` séu þekktir

.. math::

  \varphi(x)=\sum\limits_{n=1}^{\infty} \varphi_n \sin(n{\pi}x/L), \qquad
   {\psi}(x)=\sum\limits_{n=1}^{\infty} {\psi}_n \sin(n{\pi}x/L).

Jaðarskilyrðin eru greinilega uppfyllt. Til þess að
ákvarða óþekktu föllin :math:`u_n(t)`, þá stingum við röðinni
fyrir :math:`u(x,t)` inn í bylgjujöfnuna og notum upphafsskilyrðin,

.. math::

  \begin{gathered}
   {\partial}_t^2u(x,t)-c^2{\partial}_x^2u(x,t)=
   \sum\limits_{n=1}^{\infty}\big(u_n{{^{\prime\prime}}}(t)+(cn{\pi}/L)^2u_n(t)\big)
   \sin(n{\pi}x/L)=0,\\
   u(x,0)=\sum\limits_{n=1}^{\infty}u_n(0)\sin(n{\pi}x/L)=
   \sum\limits_{n=1}^{\infty}\varphi_n\sin(n{\pi}x/L)=\varphi(x),\\
   {\partial}_tu(x,0)=\sum\limits_{n=1}^{\infty}u_n{{^{\prime}}}(0)\sin(n{\pi}x/L)=
   \sum\limits_{n=1}^{\infty}{\psi}_n\sin(n{\pi}x/L)={\psi}(x).\end{gathered}

Af þessum þremur jöfnum drögum við þá ályktun að fallið :math:`u_n` sé
lausnin á upphafsgildisverkefninu

.. math::

  u_n{{^{\prime\prime}}}+\big(n{\pi}c/L\big)^2u_n=0, \qquad
   u_n(0)=\varphi_n, \quad u_n{{^{\prime}}}(0)={\psi}_n.

Svarið verður því

.. math::

  u(x,t)=\sum\limits_{n=1}^{\infty}
   \bigg(\varphi_n\cos\big(n{\pi}ct/L\big) +
   \dfrac{{\psi}_nL}{n{\pi}c} \sin\big(n{\pi}ct/L\big)\bigg)
   \sin(n{\pi}x/L).

Ef við skilgreinum nú sveifluvíddina

.. math:: C_n=\sqrt{\varphi_n^2+({\psi}_nL/n{\pi}c)^2}

og veljum fasahliðrunina :math:`{\alpha}_n` þannig að

.. math::

  \cos{\alpha}_n= \varphi_n/C_n, \qquad
   \sin{\alpha}_n= ({\psi}_nL)/(n{\pi}cC_n),

þá verður lausnin

.. math::

  u(x,t)=\sum\limits_{n=1}^{\infty}
   C_n\cos\big(n{\pi}ct/L-{\alpha}_n\big)
   \sin(n{\pi}x/L).

.. end-toggle::

Sveiflandi festi
~~~~~~~~~~~~~~~~

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Festi; framhald

Við höfum reiknað út hreyfingu perlufestar með :math:`n`
perlum í tilfellinu :math:`n=2` og :math:`n=3`. Við sáum þá að sveifla
festarinnar er samsett úr :math:`n` óháðum liðum sem við nefndum
sveifluhætti hennar. Tíðnir þessara sveifluhátta 
eru gefnar með formúlunni

.. math::

  {\omega}_j=\sqrt{n(n+1)} \sqrt{{\mu}_j}\,  c/L, \qquad
   j=1,2,\dots,n,

þar sem :math:`{\mu}_j` eru eigingildi fylkisins

.. math::

  B=
   \left[\begin{matrix}
   2 & -1 & 0 & \dots & 0 & 0\\
   -1& 2  & -1& \dots & 0 & 0\\
   0 & -1 & 2 & \dots & 0 & 0\\
   \vdots &\vdots&\vdots& \ddots &\vdots & \vdots\\
   0 & 0  & 0 & \dots & -1 & 2
   \end{matrix}\right].

Við getum einnig túlkað jöfnuna 
:math:`u(x,t)=\sum\limits_{n=1}^{\infty} C_n\cos\big(n{\pi}ct/L-{\alpha}_n\big) \sin(n{\pi}x/L)`
þannig að útslag strengsins
:math:`u(x,t)` samanstandi af óháðum liðum
:math:`C_j\cos\big(j{\pi}ct/L-{\alpha}_j\big)\sin(j{\pi}x/L)`, sem við
nefnum *sveifluhætti*. Tíðni sveifluháttarins er :math:`j{\pi}c/L`. Í
eftirfarandi töflu berum við saman tölurnar :math:`j{\pi}` og þáttinn
:math:`\sqrt{n(n+1)}\sqrt{{\mu}_j}` í sveiflutíðni festarinnar fyrir
mismunandi gildi á :math:`n`.

.. math::

  \begin{matrix}
   n=2 & n=3 & n=4 & n=8 & n=12 & j\pi \\
   2.45 & 2.65 & 2.76 & 2.95 & 3.01 & 3.14 \\
   4.24 & 4.90 & 5.26 & 5.80 & 5.98 & 6.28 \\
     & 6.40 & 7.24 & 8.49 & 8.86 & 9.42 \\
     &   & 8.51 & 10.91 & 11.61 & 12.57 \\
     &   &   & 13.00 & 14.19 & 15.71 \\
     &   &   & 14.70 & 16.56 & 18.85 \\
     &   &   & 15.95 & 18.70 & 21.99 \\
     &   &   & 16.71 & 20.56 & 25.13 \\
     &   &   &   & 22.12 & 28.27 \\
     &   &   &   & 23.36 & 31.42 \\
     &   &   &   & 24.25 & 34.56 \\
     &   &   &   & 24.80 & 37.70
   \end{matrix}

Á eftirfarandi myndum sjáum við fjóra fyrstu sveifluhættina í festi með
:math:`4`, :math:`8` og :math:`12` perlum borna saman við föllin
:math:`\sin(j{\pi}x/L)`. Útslagið er valið þannig í öllum tilfellum að
fallið :math:`\varphi` sem samanstendur af brotnu línustrikunum hafi
Fourier–stuðulinn :math:`b_j(\varphi)=1`.

.. figure:: ./myndir/fig0711.svg
    :align: center
    :alt: Sveifluhættir festar með 4 perlum

    Mynd: Sveifluhættir festar með 4 perlum

.. figure:: ./myndir/fig0712.svg
    :align: center
    :alt: Lægstu sveifluhættir festar með 8 perlum

    Mynd: Lægstu sveifluhættir festar með 8 perlum

.. figure:: ./myndir/fig0713.svg
    :align: center
    :alt: Lægstu sveifluhættir festar með 12 perlum

    Mynd: Lægstu sveifluhættir festar með 12 perlum

.. end-toggle::

Varmaleiðni
~~~~~~~~~~~

.. _syvarmaleidnistangar:

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Varmaleiðni

Við skulum nú líta á hliðruðu 
:hover:`varmaleiðnijöfnuna, varmaleiðnijafna` og reikna út hitastig í stöng af lengd
:math:`L`, sem er einangruð í báðum endapunktunum. Það þýðir að
varmaflæðið er núll í báðum endapunktunum og við þurfum því að leysa
jaðargildisverkefnið

.. math::

  \begin{cases} \dfrac{{\partial} u}{{\partial}t}-{\kappa}
   \dfrac{{\partial}^2 u}{{\partial}x^2}=f(x,t), &0<x<L, \quad t>0,\\
   {\partial}_xu(0,t)={\partial}_xu(L,t)=0, &t>0
   \end{cases}

með upphafsskilyrðinu

.. math:: u(x,0)=\varphi(x), \qquad x\in ]0,L[.

Úrlausnaraðferðin sem við beitum er sú sama og í sýnidæminu fyrir
sveiflandi streng, en við liðum :math:`u` nú í kósínus–röð til þess að
rétt jaðarskilyrði verði uppfyllt,

.. math::

  \begin{gathered}
   u(x,t)=\sum\limits_{n=0}^{\infty} u_n(t)\cos(n{\pi}x/L),\label{8.7.11}\\
   u_n(t) =\dfrac 2L\int_0^L u(x,t)\cos(n{\pi}x/L)\, dx, \quad n>0,
   \qquad u_0(t)=\dfrac 1L\int_0^L u(x,t)\, dx,\nonumber\end{gathered}

og við göngum út frá því að kósínus–raðir fallanna :math:`f` og
:math:`\varphi` séu þekktar

.. math::

  f(x,t)=\sum\limits_{n=0}^{\infty} f_n(t)\cos(n{\pi}x/L), 
   \qquad
   \varphi(x)=\sum\limits_{n=0}^{\infty} \varphi_n\cos(n{\pi}x/L).

Við stingum nú röðinni fyrir :math:`u(x,t)` inn í varmaleiðnijöfnuna og
setjum inn upphafsskilyrðin

.. math::

  \begin{aligned}
   {\partial}_tu-{\kappa}{\partial}_x^2u
   &=\sum\limits_{n=0}^{\infty}
   \big(u_n{{^{\prime}}}(t)+{\kappa}(n{\pi}/L)^2u_n(t)\big)
   \cos(n{\pi}x/L)\\
   &=\sum\limits_{n=0}^{\infty}f_n(t)\cos(n{\pi}x/L)=f(x,t),\end{aligned}

.. math::

  u(x,0)=\sum\limits_{n=0}^{\infty}u_n(0)\cos(n{\pi}x/L)=
   \sum\limits_{n=0}^{\infty}\varphi_n\cos(n{\pi}x/L)=\varphi(x).

Út úr þessum jöfnum lesum við að stuðullinn :math:`u_n(t)` er lausnin á
upphafsgildisverkefninu

.. math:: u_n{{^{\prime}}}(t)+{\kappa}(n{\pi}/L)^2u_n(t)=f_n(t), \qquad u_n(0)=\varphi_n.

og svarið verður því

.. math::

  u(x,t)=\sum\limits_{n=0}^{\infty}
   \bigg(\varphi_ne^{-{\kappa}(n{\pi}/L)^2t}+
   \int_0^te^{-{\kappa}(n{\pi}/L)^2(t-{\tau})}f_n({\tau})\, d{\tau}\bigg)
   \cos(n{\pi}x/L).

.. end-toggle::

Æfingardæmi
-----------

Æfingardæmi
~~~~~~~~~~~

Dæmi
^^^^

Ákvarðið Fourier-stuðla fallanna:

a) :math:`f(x)=\cos^2 x`,

b) :math:`f(x)=\sin x`,

c) :math:`f(x)=\cos^4 x`,

d) :math:`f(x)=\sin^2x\cos^2x`

e) :math:`f(x)=\cos^{20} x`.

Dæmi
^^^^

Ákvarðið :math:`2{\pi}`-lotubundna fallið sem hefur Fourier-stuðlana

.. math:: c_n=\begin{cases} ne^{-n}, &n\geq 0,\\ 0, &n<0.\end{cases}

Dæmi
^^^^

Ákvarðið öll tvisvar samfelld deildanleg föll, sem eru
:math:`2{\pi}`-lotubundin og uppfylla

.. math:: u{{^{\prime\prime}}}(x)=u(x+{\pi}), \qquad x\in{{\mathbb  R}}.

Dæmi
^^^^

Sýnið að:

a) :math:`x\sin x=1-\frac 12\cos x-2\sum\limits_{k=2}^{\infty} \dfrac {(-1)^k}{k^2-1}\cos kx`,  :math:`|x|\leq{\pi}`.

b) :math:`|\sin x|=\dfrac 2{\pi}\bigg(1+\big(\frac 13 -1\big)\cos 2x+ \big(\frac 15-\frac 13\big)\cos 4x +\big(\frac 17-\frac 15\big)\cos 6x +\cdots\bigg)`.

Dæmi
^^^^

Látum :math:`u` tákna :math:`2{\pi}`-lotubundna fallið, sem gefið er með
formúlunni

.. math:: u(x)=\dfrac 12\big(e^x+e^{-x}\big)=\cosh x, \qquad  |x|\leq {\pi}.

Liðið fallið :math:`u` í Fourier-röð og notið hana til þess að reikna
út summuna

.. math:: \sum\limits_{k=1}^{\infty} \dfrac 1{k^2+1}.

Dæmi
^^^^

Látum :math:`u` tákna :math:`2{\pi}`-lotubundna fallið, sem gefið er með
formúlunni

.. math:: u(x)=x^2, \qquad |x| \leq {\pi}.

Liðið :math:`u` í Fourier-röð og setjið inn heppilegt gildi á :math:`x`
inn röðina til þess að sanna að

.. math::

  \sum_{n=1}^{\infty} \dfrac {(-1)^{n+1}}{n^2}=
   1-\dfrac 14+\dfrac 19-\dfrac 1{16}+\dfrac 1{25}-\cdots
   =\dfrac {{\pi}^2}{12}.

Dæmi
^^^^

Látum :math:`{\alpha}` vera jákvæða rauntölu :math:`{\alpha}\neq 1,2,3,\dots`, og lítum á :math:`2{\pi}`-lotubundna fallið

.. math:: f(x)=\cos {\alpha}x, \qquad |x|\leq {\pi}.

Liðið :math:`f` í Fourier-röð og notið röðina til þess að sýna að

.. math::

  \sum\limits_{n=1}^{\infty} \dfrac 1{n^2-{\alpha}^2}
   =\dfrac{1-{\pi}{\alpha}\cot {\pi}{\alpha}}{2{\alpha}^2}.

Dæmi
^^^^

Liðið fallið

.. math:: f(x)=\max\{\cos x, 0\}, \qquad x\in {{\mathbb  R}},

í Fourier-röð og notið röðina til þess að reikna út

.. math::

  \sum\limits_{k=1}^{\infty}\dfrac{(-1)^k}{4k^2-1}
   \qquad \text{ og } \qquad
   \sum\limits_{k=1}^{\infty}\dfrac{1}{4k^2-1}.

Dæmi
^^^^

Beitið Parseval-jöfnunni á :math:`2{\pi}`-lotubundna fallið, sem gefið
er með formúlunni

.. math:: f(x)=x^2, \qquad |x|\leq {\pi},

og notið niðurstöðuna til þess að ákvarða

.. math:: \sum\limits_{n=1}^{\infty}\dfrac 1{n^4}.

Dæmi
^^^^

Liðið :math:`2{\pi}`-lotubundna fallið :math:`f`, sem gefið er með

.. math:: f(x)=x(x^2-{\pi}^2), \qquad |x|\leq {\pi},

í Fourier-röð og ákvarðið síðan

.. math:: \sum\limits_{n=1}^{\infty}\dfrac 1{n^6}.

Dæmi
^^^^

Látum :math:`{\alpha}` vera jákvæða rauntölu, :math:`{\alpha}\neq 1,2,3,\dots`, og :math:`f` vera :math:`2{\pi}`-lotubundna fallið, sem
gefið er með

.. math:: f(x)=e^{i{\alpha} x}, \qquad 0\leq x\leq 2{\pi}.

Ákvarðið Fourier-stuðla :math:`f` og notið þá
til þess að sýna fram á að

.. math::

  \sum\limits_{-{\infty}}^{+{\infty}} \dfrac{(-1)^n}{{\alpha}-n}
   =\dfrac {\pi}{\sin {\pi}{\alpha}} \qquad\text { og } \qquad
   \sum\limits_{-{\infty}}^{+{\infty}} \dfrac{1}{({\alpha}-n)^2}
   =\dfrac {\pi^2}{\sin^2 {\pi}{\alpha}}.

Dæmi
^^^^

Í hægri hliðum jafnanna standa lotubundin föll. Liðið þau í
Fourier-raðir og notið raðirnar til þess að finna sérlausnir með sömu
lotu:

a) :math:`u{{^{\prime\prime}}}+u =\cos^4 t`.

b) :math:`u{{^{\prime\prime}}}-u=\sin\big(2{\pi} t\big)`.

c) :math:`u{{^{\prime\prime}}}-2u{{^{\prime}}}+u=f(t)`, :math:`f(t)=|t|`, ef :math:`|t|\leq 1` og :math:`f` hefur lotu :math:`2`.

d) :math:`u{{^{\prime\prime\prime}}}+u{{^{\prime\prime}}}-u{{^{\prime}}}-u=f(t)`, :math:`f(t)=2t`, ef :math:`0\leq t\leq \frac 12`, :math:`f(t)=2-2t`, ef :math:`\frac 12\leq t\leq 1`, :math:`f` er oddstætt og :math:`2`-lotubundið.

Dæmi
^^^^

Fyrir hvaða gildi á :math:`{\omega}` hefur jafnan

.. math:: u{{^{\prime\prime}}}+{\omega}^2u=\sin^2 t\cos ^2 t, \qquad t\in {{\mathbb  R}},

:math:`2{\pi}`-lotubundna sérlausn?

Dæmi
^^^^

Liðið föllin :math:`f`, sem gefin eru í Fourier-sínus-röð eða
Fourier-kósínus-röð, eftir því sem við á, og finnið síðan lausn á
jaðargildisverkefnunum.

a) :math:`u{{^{\prime\prime}}}+u =f(x)`, :math:`u(0)=u(1)=0`, :math:`f(x)=4x(1-x)`, :math:`0\leq x\leq 1`,

b) :math:`u^{(4)}+u{{^{\prime\prime}}}+u =f(x)`, :math:`u(0)=u{{^{\prime\prime}}}(0)=u(1)=u{{^{\prime\prime}}}(1)=0`, :math:`f(x)=\sin({\pi} x)`, :math:`0\leq x\leq 1`,

c) :math:`u{{^{\prime\prime}}}+u =f(x)`, :math:`u{{^{\prime}}}(0)=u{{^{\prime}}}(1)=0`, :math:`f(x)=1-x^2`, :math:`0\leq x\leq 1`,

d) :math:`u^{(4)}-u{{^{\prime\prime}}}+u =f(x)`, :math:`u{{^{\prime}}}(0)=u{{^{\prime\prime\prime}}}(0)=u{{^{\prime}}}(1)=u{{^{\prime\prime\prime}}}(1)=0`, :math:`f(x)=\cos^2({\pi} x)`, :math:`0\leq x\leq 1.`

Dæmi
^^^^

Látum :math:`P` vera fjórða stigs margliðu og
:math:`f\in PC^1([0,L])\cap C([0,L])` vera fall sem uppfyllir
:math:`f(0)=f(L)=0`. Finnið skilyrði á :math:`P`, :math:`L` og
:math:`b_n(f)`, sem tryggja að jaðargildisverkefnið

.. math::

  P(D)u=f(x), \quad x\in ]0,L[, 
   \qquad u(0)=u{{^{\prime\prime}}}(0)=u(L)=u{{^{\prime\prime}}}(L)=0,

hafi ótvírætt ákvarðaða lausn sem hægt er að setja fram með
Fourier-sínus-röð.

Dæmi
^^^^

Liðið fallið

.. math::

  \varphi(x)=\begin{cases} 2x, & 0\leq x\leq 1/2,\\ 
   2-2x, & 1/2\leq x\leq 1, \end{cases}

í sínus–röð og notið röðina til þess að finna lausn á verkefninu

.. math::

  \begin{cases}
   {\partial}_t^2u+2{\partial}_tu-{\partial}_x^2u=0, &0<x<1,\  t>0,\\
   u(x,0)=\varphi(x), \quad {\partial}_tu(x,0)=0, & 0<x<1,\\
   u(0,t)=u(1,t)=0, & t>0.
   \end{cases}

Dæmi
^^^^

Leysið verkefnið

.. math::

  \begin{cases}
   \dfrac{\partial u}{\partial t}
   -{\kappa}\dfrac{\partial^2u}{\partial x^2}=0, &0<x<L,\\
   {\partial}_xu(0,t)={\partial}_xu(L,t)=0, &t>0,\\
   u(x,0)=T_0+(T_1-T_0)x/L, &0<x<L.
   \end{cases}

með Fourier-röð. Leysið sama verkefni með upphafsskilyrðin

.. math:: u(x,0)=T_0+(T_1-T_0)\big(1-|1-2x/L|\big).


