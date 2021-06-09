
Raðalausnir á hlutafleiðujöfnum
===============================

Inngangur
---------

Í þessum kafla kynnumst við ýmsum aðferðum til þess að leiða út formúlur
fyrir lausnir á hlutafleiðujöfnum með hliðarskilyrðum. Aðferðirnar eiga
það sammerkt að gengið er út frá lausnartilgátum sem segja að hægt sé að
liða lausnina í eiginfallaröð með tilliti til einnar breytistærðar með
stuðlum sem eru háðir öðrum breytistærðum. Eiginfallaröðin ákvarðast af
hliðarskilyrðunum, sem oftast eru jaðarskilyrði, en gildin á stuðlum
raðarinnar ákvarðast af hlutafleiðujöfnunni og einhverjum
hliðarskilyrðum, sem ýmist eru upphafs- eða jaðarskilyrði.

Hugmyndin að baki þessara lausnaraðferða hefur þegar komið fram í
nokkrum sýnidæmum í kaflanum um Fourier-raðir. Í :ref:`sýnidæmi <sysveiflandistrengurframhald>` fjölluðum við um
sveiflur strengs, þar sem frávikið frá jafnvægisstöðu :math:`u(x,t)`
uppfyllir bylgjujöfnuna,

.. math::

  \dfrac{{\partial}^2u}{{\partial}t^2}-
   c^2\dfrac{{\partial}^2u}{{\partial}x^2}=0, 
   \qquad 0<x<L, \quad t>0.

Ef strengurinn er festur niður í báðum endapunktum, þá fáum við
jaðarskilyrðið

.. math:: u(0,t)=u(L,t)=0, \qquad t\geq 0.

Þetta segir okkur að eðlileg lausnartilgáta sé að hægt sé að liða
:math:`u(x,t)` í Fourier-sínusröð með tilliti til :math:`x` með stuðlum
sem eru háðir tíma,

.. math::

  u(x,t)=\sum\limits_{n=1}^{\infty} u_n(t)\sin(n{\pi}x/L), \quad
   u_n(t)= \dfrac 2L\int_0^L u(x,t)\sin(n{\pi}x/L)\, dx.

Með því að láta bylgjuvirkjann :math:`{\partial}_t^2-c^2{\partial}_x^2`
verka lið fyrir lið summunni og setja ákveðin
upphafsskilyrði um stöðu og hraða strengsins við tímann :math:`t=0`,
sáum við að Fourier-stuðullinn :math:`u_n(t)` væri lausn á ákveðnu
upphafsgildisverkefni sem auðvelt var að leysa.

Í :ref:`sýnidæmi <syvarmaleidnistangar>` fjölluðum við um hitastig :math:`u(x,t)` í stöng af
lengd :math:`L`, þar sem varmamyndun á massa- og lengdareiningu er
:math:`f(x,t)`, en :math:`u(x,t)` uppfyllir þá varmaleiðnijöfnuna

.. math::

  \dfrac{{\partial} u}{{\partial}t}-{\kappa}
   \dfrac{{\partial}^2 u}{{\partial}x^2}=f(x,t), \qquad 0<x<L, \quad t>0.

Ef gert er ráð fyrir að endar stangarinnar séu einangraðir, þá fáum við
jaðarskilyrðið

.. math:: {\partial}_xu(0,t)={\partial}_xu(L,t)=0, \qquad t>0.

Á því sjáum við að eðlilegt er að setja fram þá lausnartilgátu að hægt
sé að liða :math:`u(x,t)` í Fourier-kósínusröð með tilliti til :math:`x`

.. math:: u(x,t)=\sum\limits_{n=0}^{\infty} u_n(t)\cos(n{\pi}x/L),

og gefa sér að Fourier-kósínusstuðlar fallsins :math:`f` séu þekktir

.. math:: f(x,t)=\sum\limits_{n=0}^{\infty} f_n(t)\cos(n{\pi}x/L).

Með því að beita varmaleiðnivirkjanum
:math:`{\partial}_t-{\kappa}{\partial}_x^2` lið fyrir lið í summunni
fyrir :math:`u(x,t)`, þá fengum við að :math:`u_n` verður að uppfylla jöfnuna
:math:`u_n{{^{\prime}}}(t)+{\kappa}(n{\pi}/L)^2u_n(t)=f_n(t)` og út
frá henni ákvarðast :math:`u_n(t)`.

Við ætlum nú að útfæra þessa hugmynd í mörgum afbrigðum til þess að
leiða út lausnarformúlur fyrir ýmsar hlutafleiðujöfnur eins og
bylgjujöfnuna, varmaleiðnijöfnuna og Laplace-jöfnuna með
hliðarskilyrðum.

Laplace-virkinn í rétthyrndum hnitum
------------------------------------

*Dirichlet-verkefni* fyrir Laplace-virkjann
í plani er:

.. math::

  \begin{cases}
   \Delta u=\dfrac{\partial^2u}{\partial x^2}+
   \dfrac{\partial^2u}{\partial y^2}=0, &(x,y)\in X,\\
   u(x,y)={\varphi}(x,y), &(x,y)\in {\partial}X,
   \end{cases}

þar sem :math:`X` er opið svæði í :math:`{{\mathbb  R}}^2` með jaðar
:math:`{\partial}X` og :math:`{\varphi}` er gefið fall á
:math:`{\partial}X`. Í eðlisfræðinni er þetta verkefni mjög mikilvægt.
Lausnin getur til dæmis verið hitastig í þunnri plötu, sem er í
varmajafnvægi, (:math:`{\partial}u/{\partial}t=0`). Fallið :math:`u`
getur einnig verið rafstöðumætti í þunnri leiðandi plötu. Nú skulum við
líta á tilfellið þegar :math:`X` er rétthyrnd plata:

.. math::

  \begin{cases} \Delta u=0, &0<x<L, \ 0<y<M,\\
   u(x,0)=\varphi_1(x), \ u(x,M)=\varphi_2(x), &0<x<L,\\
   u(0,y)=\psi_1(y), \ u(L,y)=\psi_2(y), &0<y<M.
   \end{cases}

.. figure:: ./myndir/fig141.svg
    :align: center
    :alt: Dirichlet verkefnið á ferhyrningi

    Mynd: Dirichlet verkefnið á ferhyrningi

Við skiptum verkefninu í fjóra hluta

.. math::

  \begin{cases} \Delta u_1=0,\\
   u_1(x,0)=\varphi_1(x), \ u_1(x,M)=0,\\
   u_1(0,y)=u_1(L,y)=0,
   \end{cases}\qquad
   \begin{cases} \Delta u_2=0,\\
   u_2(x,0)=0, u_2(x,M)=\varphi_2(x),\\
   u_2(0,y)=u_2(L,y)=0,
   \end{cases}

.. math::

  \begin{cases} \Delta u_3=0,\\
   u_3(x,0)=u_3(x,M)=0,\\
   u_3(0,y)=\psi_1(y), \ u_3(L,y)=0,
   \end{cases} \qquad
   \begin{cases} \Delta u_4=0,\\
   u_4(x,0)=u_4(x,M)=0,\\
   u_4(0,y)=0, u_4(L,y)=\psi_2(y).
   \end{cases}

.. figure:: ./myndir/fig142.svg
    :align: center
    :alt: Liðun á Dirichlet verkefninu í fernt

    Mynd: Liðun á Dirichlet verkefninu í fernt

Ef við getum sýnt fram á að lausnirnar :math:`u_1`, :math:`u_2`,
:math:`u_3` og :math:`u_4` á þessum verkefnunum eru til og leitt út
formúlur fyrir þeim, þá segir samlagningarlögmálið að lausnin :math:`u`
á Dirichlet-verkefninu á ferhyrningi sé :math:`u(x,y)=u_1(x,y)+u_2(x,y)+u_3(x,y)+u_4(x,y)`.

Nú snúum við okkur að verkefnunum fjórum. Skilyrðin
:math:`u_1(0,y)=u_1(L,y)=0` segja okkur að eðlilegt sé að ganga út frá
þeirri lausnartilgátu að hægt sé að liða :math:`u_1(x,y)` í
Fourier-sínusröð,

.. math::

  \begin{gathered}
   u_1(x,y)=\sum\limits_{n=1}^\infty u_{1n}(y)\sin\big(n\pi x/L\big), \\
   u_{1n}(y)=b_n(u_1(\cdot,y))
   =\dfrac 2L\int_0^Lu_1(x,y)\sin\big(n\pi x/L\big)\, dx.\end{gathered}

Til þess að ákvarða stuðlana :math:`u_{1n}(y)`, þá látum við
Laplace-virkjann verka lið fyrir lið í summunni og stingum inn
jaðarskilyrðunum,

.. math::

  \begin{aligned}
   \Delta u_1(x,y)&=
   \sum\limits_{n=1}^\infty 
   \bigg(\dfrac{\partial^2}{\partial x^2}+
   \dfrac{\partial^2}{\partial y^2}\bigg) u_{1n}(y)\sin\big(n\pi x/L\big)\\
   &=
   \sum\limits_{n=1}^\infty 
   \big(-(n\pi/L)^2 u_{1n}(y)+ u_{1n}{{^{\prime\prime}}}(y)
   \big)\sin\big(n\pi x/L\big)=0,\\
   u_1(x,0)&=\sum\limits_{n=1}^\infty
   u_{1n}(0)\sin\big(n\pi x/L\big)\\
   &=\sum\limits_{n=1}^\infty b_n(\varphi_1) \sin\big(n\pi x/L\big)
   =\varphi_1(x),\\
   u_1(x,M)&=\sum\limits_{n=1}^\infty
   u_{1n}(M)\sin\big(n\pi x/L\big)=0.\end{aligned}

Út úr þessum jöfnum lesum við nú að :math:`u_{1n}` verður að vera lausn
á jaðargildisverkefninu

.. math::

  \begin{cases}
   u_{1n}{{^{\prime\prime}}}(y)-(n\pi/L)^2 u_{1n}(y)=0, &0<y<M,\\
   u_{1n}(0)=b_n(\varphi_1), \quad u_{1n}(M)=0.
   \end{cases}

Almenn lausn á þessari afleiðujöfnu er

.. math:: u_{1n}(y)=A_n\cosh\big(n\pi y/L\big)+B_n\sinh\big(n\pi y/L\big),

og jaðarskilyrðin gefa

.. math::

  \begin{aligned}
   u_{1n}(0)&=A_n=b_n(\varphi_1),\\
   u_{1n}(M)&=A_n\cosh\big(n\pi M/L\big)+B_n\sinh\big(n\pi M/L\big)=0.\end{aligned}

Þar með er

.. math::

  \begin{aligned}
   u_{1n}(y)&=b_n(\varphi_1)\cosh\big(n\pi y/L\big)- b_n(\varphi_1)
   \dfrac{\cosh\big(n\pi M/L\big)}{\sinh\big(n\pi M/L\big)} 
   \sinh\big(n\pi y/L\big)\\
   &=b_n(\varphi_1)\dfrac
   {\sinh\big(n\pi M/L\big) \cosh\big(n\pi y/L\big)
   -\cosh\big(n\pi M/L\big) \sinh\big(n\pi y/L\big)}
   {\sinh\big(n\pi M/L\big)}\\
   &=b_n(\varphi_1)\dfrac
   {\sinh\big(n\pi (M-y)/L\big)}
   {\sinh\big(n\pi M/L\big)}.\end{aligned}

Við höfum því ákvarðað fyrsta liðinn :math:`u_1` í framsetningu okkar á
:math:`u`. Til þess að finna :math:`u_2` skiptum við einungis á
:math:`y` og :math:`M-y` og til þess að ákvarða :math:`u_3` og
:math:`u_4`, þá skiptum við einfaldlega á hlutverkum :math:`x` og
:math:`y`. Útkoman verður því

.. math::

  \begin{aligned}
   u(x,y)&=\sum\limits_{n=1}^\infty
   b_n(\varphi_1)
   \dfrac{\sinh\big(n\pi(M-y)/L\big)}{\sinh\big(n\pi M/L\big)}
   \sin\big(n\pi x/L\big)\\
   &+\sum\limits_{n=1}^\infty
   b_n(\varphi_2)
   \dfrac{\sinh\big(n\pi y/L\big)}{\sinh\big(n\pi M/L\big)}
   \sin\big(n\pi x/L\big)\nonumber\\
   &+\sum\limits_{n=1}^\infty
   b_n(\psi_1)
   \dfrac{\sinh\big(n\pi (L-x)/M\big)}{\sinh\big(n\pi L/M\big)}
   \sin\big(n\pi y/M\big)\nonumber\\
   &+\sum\limits_{n=1}^\infty
   b_n(\psi_2)
   \dfrac{\sinh\big(n\pi x/M\big)}{\sinh\big(n\pi L/M\big)}
   \sin\big(n\pi y/M\big).\nonumber\end{aligned}

Hér er rétt að lesandinn staldri við og sannfæri sig um að föllin, sem
summurnar fjórar skilgreina séu lausnirnar á jaðargildisverkefnunum
fjórum hér að ofan.

Í þessari úrlausn sáum við að það er mikilvægt að föllin
:math:`x\mapsto \sin(n{\pi}x/L)` uppfylla gefnu jaðarskilyrðin í
:math:`x=0` og :math:`x=L` og jafnframt að það er lykilatriði að þau eru
*eiginföll* fyrri liðarins í Laplace-virkjanum, þ.e.

.. math::

  -\dfrac{d^2}{dx^2} \sin(n{\pi} x/L)=
   \big(n{\pi}/L\big)^2 \sin(n{\pi} x/L).

Laplace-virkinn í pólhnitum
---------------------------

Í þessari grein höldum við áfram með Dirichlet-verkefnið fyrir
Laplace-virkjann, en nú leysum við það á hringskífu

.. math::

  \begin{cases} \Delta u=
   \dfrac{\partial^2u}{\partial x^2}+
   \dfrac{\partial^2u}{\partial y^2}=0, &x^2+y^2<a^2,\\
   u(x,y)=\varphi(x,y), &x^2+y^2=a^2.
   \end{cases}

Hér er :math:`\varphi` gefið fall á jaðri hringskífunnar
:math:`D_a=\{(x,y); x^2+y^2<a^2\}`. Til þess að leysa verkefnið skiptum
við yfir í pólhnit og setjum
:math:`v(r,\theta)=u(r\cos \theta,r\sin \theta)` og
:math:`{\psi}(\theta)=\varphi(a\cos \theta,a\sin \theta)`. Í viðauka D
er leidd út formúla fyrir Laplace-virkjann í pólhnitum,

.. math::

  \Delta = \dfrac 1r\dfrac{\partial}{\partial r}
   \bigg(r\dfrac{\partial }{\partial r}\bigg)
   +\dfrac 1{r^2}\dfrac{\partial^2 }{\partial\theta^2},

svo verkefnið verður

.. math::

  \begin{cases}
   \dfrac 1r\dfrac{\partial}{\partial r}
   \bigg(r\dfrac{\partial v}{\partial r}\bigg)
   +\dfrac 1{r^2}\dfrac{\partial^2 v}{\partial\theta^2}=0, &r<a,
   \ {\theta}\in {{\mathbb  R}},\\
   v(a,\theta)={\psi}(\theta), &{\theta}\in {{\mathbb  R}}.
   \end{cases}

Nú er ljóst að bæði :math:`v` og :math:`{\psi}` eru
:math:`2\pi`-lotubundin föll af :math:`\theta` og því er eðlileg
lausnartilgáta að setja þau fram með Fourier-röðum með tilliti til
:math:`{\theta}`

.. math::

  v(r,\theta)=\sum\limits_{n=-\infty}^{+\infty}
   v_n(r)e^{in\theta}, \qquad
   {\psi}(\theta)=\sum\limits_{n=-\infty}^{+\infty}
   {\psi}_n e^{in\theta},

þar sem :math:`v_n(r)=c_n(v(r,\cdot))` er Fourier-stuðull :math:`v`,
þar sem litið er á :math:`v` sem fall af :math:`\theta` fyrir fast
:math:`r` og :math:`{\psi}_n=c_n({\psi})`. Nú látum við Laplace-virkjann
verka lið fyrir lið í röðinni fyrir :math:`v` og lítum einnig á
jaðarskilyrðin:

.. math::

  \begin{aligned}
   \Delta v(r,\theta)&=\dfrac 1{r^2}\sum\limits_{n=-\infty}^{+\infty}
   \bigg(r\partial_r\big(r\partial_r\big)
   +\partial_\theta^2\bigg)v_n(r)e^{in\theta}\\
   &=\dfrac 1{r^2}\sum\limits_{n=-\infty}^{+\infty}
   \bigg(r\big(rv_n{{^{\prime}}}(r)\big){{^{\prime}}}-n^2v_n(r)\bigg)e^{in\theta}=0,\\
   v(a,\theta)&=\sum\limits_{n=-\infty}^{+\infty}v_n(a)e^{in{\theta}}=
   \sum\limits_{n=-\infty}^{+\infty} {\psi}_ne^{in\theta}={\psi}(\theta).\end{aligned}

Af þessum tveimur jöfnum sjáum við að stuðlafallið :math:`v_n` verður að
vera lausn á jaðargildisverkefninu

.. math::

  \begin{cases}
   r\dfrac d{dr}\bigg(r\dfrac{dv_n}{dr}\bigg)-n^2v_n=0, &r<a,\\
   v_n(a)={\psi}_n, \quad v_n(r) \text{ takmarkað ef } r\to 0.
   \end{cases}

Þetta er Euler-jafna og því leitum
við að lausn af gerðinni :math:`v_n(r)=r^\alpha` og sjáum að
:math:`\alpha` verður þá að uppfylla

.. math::

  r\dfrac d{dr}\bigg( r\dfrac d{dr}r^\alpha\bigg)=\alpha^2r^\alpha=
   n^2r^\alpha.

Þetta segir okkur að :math:`\alpha=\pm n` og að almenn lausn
afleiðujöfnunar sé

.. math::

  v_n(r)=
   \begin{cases}
   A_nr^{|n|}+B_nr^{-|n|}, &n\neq 0\\
   A_0+B_0\ln r, &n=0.
   \end{cases}

Til þess að lausnin geti verið takmörkuð í :math:`r=0`, þá verðum við
að útiloka liðina með neikvæðum veldisvísi og logrann. Skilyrðið
:math:`v_n(a)={\psi}_n` gefur að :math:`A_n={\psi}_n/a^{|n|}`. Þar með
er lausnin fundin

.. math::

  v(r,\theta)=\sum\limits_{n=-\infty}^{+\infty}
   c_n({\psi}) \bigg(\dfrac r a\bigg)^{|n|}e^{in\theta}.

Það er auðveld æfing að sannfæra sig um að þetta sé lausn á
Laplace-jöfnunni með gefnum jaðarskilyrðum. Hér er mikilvægt að taka
eftir því að ástæðan fyrir því að þessi lausnaraðferð virkar svona vel
er að fallið :math:`e^{in\theta}` er *eiginfall* seinni liðarins í
Laplace-virkjanum, þ.e.

.. math::

  -\dfrac{d^2}{d\theta^2}e^{in\theta}=n^2 e^{in\theta}, \qquad
   \theta\in {{\mathbb  R}}.

Varmaleiðniverkefni og Fourier-raðir
------------------------------------

Við skulum nú reikna út hitastig í jarðvegi sem fall af tíma :math:`t`
og dýpi :math:`x` með hitastigið á yfirborði gefið sem fall af tíma
:math:`f(t)`. Það er eðlilegt að gefa sér að :math:`f` sé
:math:`T`-lotubundið fall, þar sem lotan :math:`T` getur til dæmis verið
:math:`1` ár. Við þurfum þá að leysa jaðargildisverkefnið

.. math::

  \begin{cases}
   \dfrac{\partial u}{\partial t}-\kappa
   \dfrac{\partial^2 u}{\partial x^2}=0, &x>0, \ t\in {{\mathbb  R}},\\
   u(0,t)=f(t), &t\in {{\mathbb  R}},\\
   u(x,t) \text{ takmarkað ef } & x\to +\infty.
   \end{cases}

Það er eðlileg lausnartilgáta að gefa sér að :math:`u(x,t)` sé
:math:`T`-lotubundið fall af :math:`t` fyrir fast :math:`x`. Við liðum
því :math:`u` í Fourier-röð

.. math::

  u(x,t)=\sum\limits_{n=-\infty}^{+\infty}
   u_n(x)e^{in\omega t}, \qquad \omega=2\pi/T,

því :math:`f` er af sömu gerð

.. math::

  f(t)=\sum\limits_{n=-\infty}^{+\infty}
   c_n(f)e^{in\omega t}.

Til þess að ákvarða stuðlana :math:`u_n(x)`, þá stingum við röðinni
fyrir :math:`u` inn í varmaleiðnijöfnuna og setjum fram jaðarskilyrðið
með röðum,

.. math::

  \begin{aligned}
   \dfrac{\partial u}{\partial t}-\kappa
   \dfrac{\partial^2 u}{\partial x^2}&=
   \sum\limits_{n=-\infty}^{+\infty}\bigg(
   \dfrac{\partial }{\partial t}-\kappa
   \dfrac{\partial^2 }{\partial x^2}\bigg)u_n(x)e^{in\omega t}\\
   &= \sum\limits_{n=-\infty}^{+\infty}\bigg(
   in\omega  u_n(x)-{\kappa}u_n{{^{\prime\prime}}}(x)\bigg)e^{in\omega t}=0,\\
   u(0,t)&=\sum\limits_{n=-\infty}^{+\infty} u_n(0)e^{in\omega t}
   =\sum\limits_{n=-\infty}^{+\infty} c_n(f)e^{in\omega t}=f(t).\end{aligned}

Þar með verður :math:`u_n` að uppfylla

.. math::

  \begin{cases}
   u_n{{^{\prime\prime}}}(x)-\dfrac{in\omega}\kappa u_n(x)=0,\\
   u_n(0)=c_n(f),\\
   u_n(x) \text{ er takmarkað ef } x \to +\infty.
   \end{cases}

Kennijafna afleiðujöfnunnar er

.. math:: \lambda^2-\dfrac{in\omega}\kappa=0

og núllstöðvar hennar eru :math:`\lambda=\pm k_n`, þar sem

.. math::

  k_n=
   \begin{cases}
   \bigg(\dfrac 1{\sqrt 2}+\dfrac i{\sqrt 2}\bigg)
   \sqrt{n\omega/\kappa}, &n>0,\\
   0, &n=0,\\
   \bigg(\dfrac 1{\sqrt 2}-\dfrac i{\sqrt 2}\bigg)
   \sqrt{|n|\omega/\kappa}, &n<0.
   \end{cases}

Lausnin er því

.. math::

  u_n(x)=\begin{cases}
   A_ne^{-k_nx}+B_ne^{k_nx}, &n\neq 0\\
   A_0+B_0x, &n=0.
   \end{cases}

Til þess að lausnin haldist takmörkuð ef :math:`x\to +\infty`, þá
verður :math:`B_n=0` að gilda fyrir öll :math:`n`. Jaðarskilyrðið
:math:`u_n(0)=c_n(f)` gefur að :math:`A_n=c_n(f)`. Við höfum því að

.. math::

  u_n(x)=c_n(f)e^{-\sqrt{|n|\omega/2\kappa}\, x}
   e^{-i{{\operatorname{sign}}}(n)\sqrt{|n|\omega/2\kappa}\, x},

og þar með er lausnin fundin

.. math::

  u(x,t)=\sum\limits_{n=-\infty}^{+\infty}
   c_n(f)e^{-\sqrt{|n|\omega/2\kappa}\, x}
   e^{i(n\omega t-{{\operatorname{sign}}}(n)\sqrt{|n|\omega/2\kappa}\, x)}.

Við sjáum að sveifluvíddin og fasahliðrunin í liðnum
:math:`u_n(x)e^{in\omega t}` í lausninni eru háð dýpi og tíðninni
:math:`n\omega`.

Aðskilnaður breytistærða
------------------------

Aðskilnaður breytistærða
~~~~~~~~~~~~~~~~~~~~~~~~

Í öllum þeim sýnidæmum sem við höfum fjallað um í þessum kafla höfum við
gengið út frá lausnartilgátum sem segja að hægt sé að liða lausn á
hlutafleiðujöfnu með hliðarskilyrðum í einhvers konar röð. Annað
sjónarhorn á þessar lausnaraðferðir er oft nefnt *aðskilnaður
breytistærða*. Við skulum nú leysa nokkur verkefni með þeirri aðferð.

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Strengur; framhald

Í :ref:`sýnidæmi <sysveiflandistrengurframhald>` leiddum við út formúlu fyrir sveiflandi streng en
frávik hans :math:`u(x,t)` frá jafnvægisstöðu uppfyllir bylgjujöfnuna

.. math::

  \dfrac{\partial^2 u}{\partial t^2}-
   c^2\dfrac{\partial^2 u}{\partial x^2}=0, \qquad c=\sqrt{T/\varrho},

þar sem :math:`T` táknar spennuna í strengnum og :math:`{\varrho}`
táknar massa á lengdareiningu. Ef við gefum okkur að strengurinn sé
festur niður í báðum endapunktum, þá fáum við náttúruleg jaðarskilyrði

.. math:: u(0,t)=u(L,t)=0.

Þegar *aðskilnaði breytistærða* er beitt, er byrjað á að ákvarða allar
lausnir á jöfnunni af gerðinni :math:`v(x,t)=T(t)X(x)`. Við stingum
þessu falli inn í bylgjujöfnuna og fáum

.. math::

  \dfrac{\partial^2 v}{\partial t^2}-
   c^2\dfrac{\partial^2 v}{\partial x^2}=
   T{{^{\prime\prime}}}(t)X(x)-c^2T(t)X{{^{\prime\prime}}}(x)=0.

Með því að deila í gegnum þessa jöfnu með :math:`c^2T(t)X(x)`, þá sjáum
við að hún jafngildir

.. math:: \dfrac{T{{^{\prime\prime}}}(t)}{c^2T(t)} = \dfrac{X{{^{\prime\prime}}}(x)}{X(x)}.

Vinstra megin jafnaðarmerkisins stendur fall, sem er aðeins háð
:math:`t`, en hægra megin stendur fall, sem er aðeins háð :math:`x`.
Þessi stærð hlýtur því að vera fasti. Við skulum tákna hann með
:math:`-{\lambda}`. Nú segir jaðarskilyrðið að
:math:`X(0)=X(L)=0` verði að gilda. Þar með verður :math:`X` að vera
lausn á eigingildisverkefninu

.. math:: -X{{^{\prime\prime}}}={\lambda} X, \qquad X(0)=X(L)=0.

Við fundum lausnina á þessu verkefni í :ref:`sýnidæmi <syfallsjadarskilyrdiibadumendapunktum>`. Eigingildin eru
:math:`{\lambda}_n=\big(n{\pi}/L\big)^2` og tilsvarandi eiginföll má
taka :math:`X_n(x)=\sin\big(n{\pi}x/L\big)`, :math:`n=1,2,3,\dots`.
Víkjum nú aftur að jöfnunni

.. math:: \dfrac{T{{^{\prime\prime}}}(t)}{c^2T(t)} = \dfrac{X{{^{\prime\prime}}}(x)}{X(x)}.

til þess að ákvarða fallið :math:`T`.
Fyrir hin ólíku eigingildi þarf :math:`T` að uppfylla

.. math:: -T{{^{\prime\prime}}}= c^2{\lambda}_n T.

Almenn lausn þessarar jöfnu er
:math:`T_n(t)= A_n\cos\big(n{\pi}ct/L\big) + B_n\sin\big(n{\pi}ct/L\big)`. Niðurstaðan er nú að allar lausnir af
gerðinni :math:`T(t)X(x)` á bylgjujöfnunni með jaðarskilyrðinu

.. math:: u(0,t)=u(L,t)=0.

eru

.. math::

  T_n(t)X_n(x)=\big(A_n\cos\big(n{\pi}ct/L\big) +
   B_n\sin\big(n{\pi}ct/L\big)\big)
   \sin\big(n{\pi}x/L\big), \qquad n=1,2,\dots,

þar sem velja má fastana :math:`A_n` og :math:`B_n` frjálst. Það er
ljóst að summa endanlega margra lausna 
er lausn og sama gildir um hratt samleitnar óendanlegar
raðir

.. math::

  u(x,t)=\sum\limits_{n=1}^{\infty}
   \big(A_n\cos\big(n{\pi}ct/L\big) +
   B_n\sin\big(n{\pi}ct/L\big)\big)
   \sin\big(n{\pi}x/L\big).

Við fáum því Fourier-sínusröð. Til þess
að ákvarða stuðlana :math:`A_n` og :math:`B_n` þarf að bæta við fleiri
hliðarskilyrðum. Eðlilegt er að það séu upphafsskilyrði af gerðinni

.. math:: u(x,0)={\varphi}(x), \qquad {\partial}_tu(x,0)={\psi}(x),

þar sem :math:`{\varphi}` og :math:`{\psi}` eru gefin föll á bilinu
:math:`(0,L)`. Ef við göngum út frá því að sínusstuðlar fallanna
:math:`\varphi` og :math:`{\psi}` séu þekktir

.. math::

  \varphi(x)=\sum\limits_{n=1}^{\infty} \varphi_n \sin(n{\pi}x/L), \qquad
   {\psi}(x)=\sum\limits_{n=1}^{\infty} {\psi}_n \sin(n{\pi}x/L),

þá gefa upphafsskilyrðin

.. math::

  \begin{gathered}
   u(x,0)=\sum\limits_{n=1}^{\infty}A_n\sin(n{\pi}x/L)=
   \sum\limits_{n=1}^{\infty}\varphi_n\sin(n{\pi}x/L)=\varphi(x),\\
   {\partial}_tu(x,0)=\sum\limits_{n=1}^{\infty}
   B_n(n{\pi}c/L)\sin(n{\pi}x/L)=
   \sum\limits_{n=1}^{\infty}{\psi}_n\sin(n{\pi}x/L)={\psi}(x).\end{gathered}

Af þessum þremur jöfnum drögum við þá ályktun að

.. math::

  A_n={\varphi}_n \qquad \text{ og } \qquad 
   B_n={\psi}_n L/(n{\pi}c).

Lausnin :math:`u(x,t)` er þá fundin

.. math::

  u(x,t)=\sum\limits_{n=1}^{\infty}
   \bigg(\varphi_n\cos\big(n{\pi}ct/L\big) +
   \dfrac{{\psi}_nL}{n{\pi}c} \sin\big(n{\pi}ct/L\big)\bigg)
   \sin(n{\pi}x/L).

Þetta er að sjálfsögðu sama lausnarformúla og við leiddum út í :ref:`sýnidæmi <sysveiflandistrengurframhald>`.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Dirichlet-verkefnið á ferhyrningi

Tökum nú aftur fyrir verkefni númer 2 á fjórskiptu myndinni um liðun á Dirichlet verkefninu í fernt hér að ofan og leysum það út frá
sjónarhóli aðskilnaðar breytistærða.

.. math::

  \begin{cases} \Delta u={\partial}_x^2u+{\partial}_y^2u=0, &0<x<L, \ 0<y<M,\\
   u(0,y)=u(L,y)=0, &0<y<M,\\
   u(x,0)=0, \ u(x,M)=\varphi(x), &0<x<L,\\
   \end{cases}

þar sem :math:`\varphi` er gefið fall á :math:`[0,L]`. Við byrjum
samkvæmt forskrift í aðskilnaði breytistærða á því að finna allar
lausnir :math:`v` af gerðinni :math:`v(x,y)=X(x)Y(y)` sem uppfylla
jöfnuna og óhliðruðu jaðarskilyrðin. Fyrst stingum við :math:`v` inn í
jöfnuna og fáum

.. math:: X{{^{\prime\prime}}}(x)Y(y)+X(x)Y{{^{\prime\prime}}}(y)=0.

Nú deilum við í gegnum þessa jöfnu með :math:`X(x)Y(y)` og sjáum að

.. math:: -\dfrac{X{{^{\prime\prime}}}(x)}{X(x)}=\dfrac{Y{{^{\prime\prime}}}(y)}{Y(y)}.

Fallið sem stendur vinstra megin jafnaðarmerkisins er einungis háð
:math:`x`, en það sem stendur hægra megin er einungis háð :math:`y`. Við
höfum því

.. math:: -X{{^{\prime\prime}}}(x)=\lambda X(x) \qquad \text{ og } \qquad Y{{^{\prime\prime}}}(y)=\lambda Y(y),

þar sem :math:`\lambda` er fasti. Nú lítum við á óhliðruðu
jaðarskilyrðin

.. math:: X(0)Y(y)=X(L)Y(y)=0, \qquad X(x)Y(0)=0,

og sjáum að :math:`X` verður að vera lausn á eigingildisverkefninu

.. math:: -X{{^{\prime\prime}}}=\lambda X, \qquad X(0)=X(L)=0.

Þetta verkefni leystum við í ref:`sýnidæmi <syfallsjadarskilyrdiibadumendapunktum>` og komumst að þeirri
niðurstöðu að eigingildin eru
:math:`\lambda=\lambda_n=\big(n\pi/L\big)^2`, :math:`n=1,2,3,\dots`, og
tilsvarandi eiginföll

.. math:: X_n(x)=C_n \sin\big(n\pi x/L\big), \qquad n=1,2,3,\dots.

Nú snúum við okkur að seinni afleiðujöfnunni og leysum hana
með seinna jaðarskilyrðinu,

.. math:: Y{{^{\prime\prime}}}(y)=\big(n\pi/L\big)^2 Y(y), \qquad Y(0)=0.

Þessi jafna hefur greinilega lausnina

.. math:: Y_n(y)=D_n \sinh\big(n\pi y/L\big), \qquad n=1,2,3,\dots.

Nú eru allar lausnir á Laplace-jöfnunni af gerðinni
:math:`v(x,y)=X(x)Y(y)` með óhliðruðu jaðarskilyrðunum gefnar með formúlunni

.. math::

  v(x,y)=C_nD_n \sin\big(n\pi x/L\big)\sinh\big(n\pi y/L\big), \qquad
   n=1,2,3,\dots.

Hér höfum við tvo frjálsa fasta sem við margföldum saman og því er
greinilegt að við getum valið :math:`D_n=1`. Nú myndum við óendanlega
línulega samatekt af þessum lausnum

.. math::

  u(x,y)=\sum\limits_{n=1}^\infty
   C_n\sin\big(n\pi x/L\big)\sinh\big(n\pi y/L\big).

Þetta er fall sem uppfyllir Laplace-jöfnuna með óhliðruðum
jaðarskilyrðum. Nú er eitt jaðarskilyrði eftir,
:math:`u(x,M)=\varphi(x)`. Til þess að það verði uppfyllt þurfum við að
hafa

.. math::

  \begin{aligned}
   u(x,M)&= \sum\limits_{n=1}^\infty
   C_n \sin\big(n\pi x/L\big)\sinh\big(n\pi M/L\big)\\
   &= \sum\limits_{n=1}^\infty
   b_n(\varphi) \sin\big(n\pi x/L\big)=\varphi(x),\end{aligned}

þar sem :math:`b_n(\varphi)` er Fourier-sínusstuðull fallsins
:math:`\varphi`,

.. math:: b_n(\varphi)=\dfrac 2L\int_0^L\varphi(x)\sin\big(n\pi x/L\big)\,  dx

Með því að bera saman stuðlana í summunum tveimur, þá fáum við
lausnina,

.. math::

  u(x,y)=\sum_{n=1}^\infty
   b_n(\varphi)\dfrac{\sinh\big(n\pi y/L\big)}{\sinh\big(n\pi
   M/L\big)} \sin\big(n\pi x/L\big).

Athugið að þetta er önnur óendanlega summan í formúlunni
fyrir lausninni á Dirichlet-verkefni á rétthyrningi.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Dirichlet-verkefnið á hringskífu

Við skulum nú leysa aftur Dirichlet-verkefnið á hringskífu,

.. math::

  \begin{cases}
   \dfrac 1r\dfrac{\partial}{\partial r}
   \bigg(r\dfrac{\partial v}{\partial r}\bigg)
   +\dfrac 1{r^2}\dfrac{\partial^2 v}{\partial\theta^2}=0, &r<a,
   \ {\theta}\in {{\mathbb  R}},\\
   v(a,\theta)={\psi}(\theta), &{\theta}\in {{\mathbb  R}},
   \end{cases}

þar sem föllin :math:`v` og :math:`\psi` eru :math:`2\pi`-lotubundin í
:math:`\theta`. Við beitum aðskilnaði breytistærða og leitum fyrst að
öllum lausnum af gerðinni :math:`w(r,\theta)=R(r)\Theta(\theta)`. Ef við
stingum þessu falli inn í afleiðujöfnuna, þá fáum við að

.. math::

  r \big(r R{{^{\prime}}}(r)\big){{^{\prime}}}\Theta(\theta)
   +R(r)\Theta{{^{\prime\prime}}}(\theta)=0.

Nú deilum við í gegnum jöfnuna með :math:`R(r)\Theta(\theta)` og fáum
þá jafngilda jöfnu

.. math::

  r\big(r R{{^{\prime}}}(r)\big){{^{\prime}}}/R(r)
   =-\Theta {{^{\prime\prime}}}(\theta)/\Theta (\theta).

Vinstri hlið þessarar jöfnu er aðeins háð :math:`r` en hægri hliðin er
aðeins háð :math:`\theta`. Þar með sjáum við að þessi föll eru jöfn sama
fastanum :math:`\lambda`. Við getum þá skrifað jöfnurnar upp aftur

.. math::

  -\Theta{{^{\prime\prime}}}(\theta)=\lambda\Theta(\theta),
   \qquad 
   r\dfrac d{dr}\bigg(r\dfrac {d R}{dr}(r)\bigg)=\lambda {R(r)}.

Almenn lausn á fyrri jöfnunni er

.. math::

  \Theta(\theta)=\begin{cases}
   Ae^{i\beta\theta}+Be^{-i\beta\theta},  &\lambda=\beta^2\neq 0,\\
   A_0+B_0\theta, &\lambda=0.
   \end{cases}

Fallið :math:`\Theta` á að vera :math:`2\pi`-lotubundið og því fáum við
að einu gildin sem :math:`\lambda` getur tekið eru
:math:`\lambda=\lambda_n=n^2`, :math:`n=0,1,2,\dots`, og :math:`B_0=0`.
Þar með er

.. math::

  \Theta(\theta)=\begin{cases}
   A_ne^{in\theta}+B_ne^{-in\theta},  &n=1,2,3,\dots,\\
   A_0, &\lambda=0.
   \end{cases}

Nú ráðumst við á seinni afleiðjujöfnuna fyrir :math:`R(r)` með
:math:`\lambda=n^2`. Þetta er Euler-jafna. Með því að leita að lausn af gerðinni :math:`R(r)=r^\alpha` sjáum
við að :math:`\alpha=\pm n`. Almenn lausn á seinni afleiðujöfnunni 
fyrir :math:`R(r)` með :math:`\lambda=n^2` er því

.. math::

  R(r)=\begin{cases}
   C_nr^n+D_nr^{-n}, &n=1,2,3,\dots,\\
   C_0+D_0\ln r, &n=0.
   \end{cases}

Við erum að leysa Dirichlet-verkefnið á hringskífu og jafnan á að gilda í :math:`r=0`.
Því verður hún að vera takmörkuð og við ályktum að :math:`D_n=0`,
:math:`n=0,1,2,\dots`. Þar með er

.. math::

  R(r)=\begin{cases}
   C_nr^n, &n=1,2,3,\dots,\\
   C_0, &n=0.
   \end{cases}

Við erum nú búin að ákvarða allar lausnir á verkefninu af gerðinni
:math:`w(r,\theta)=R(r)\Theta(\theta)` og þær eru

.. math::

  w(r,\theta)=
   C_nr^n\big(A_ne^{in\theta}+B_ne^{-in\theta}\big), \qquad n=0,1,2,\dots,

þar sem :math:`A_n`, :math:`B_n` og :math:`C_n` eru frjálsir fastar.
Það er greinilegt að við megum alltaf velja :math:`C_n=1`. Nú er hlutafleiðujafnan
línuleg og óhliðruð, svo línuleg samantekt af lausnum er
lausn og sama gildir um hratt samleitnar óendanlegar summur. Ef við
tökum lausnirnar saman, þá er greinilegt að við getum skrifað
óendanlegar línulegar samantektir sem

.. math:: v(r,\theta)=\sum\limits_{-\infty}^{+\infty}A_nr^{|n|}e^{in\theta},

þar sem við höfum sett :math:`A_n=B_{-n}` ef :math:`n<0`. Hér er
Fourier-röðin komin. Við eigum eftir að notfæra okkur jaðarskilyrðið í
:math:`r=a`, en það segir

.. math::

  v(a,\theta)=\sum\limits_{-\infty}^{+\infty}A_na^{|n|}e^{in\theta}
   =\sum\limits_{-\infty}^{+\infty}c_n(\psi)a^{|n|}e^{in\theta}=\psi(\theta).

Með samanburði á stuðlum fáum við nú að :math:`A_n=c_n(\psi)/a^{|n|}`
og við endum á sömu lausnarformúlu og áður

.. math::

  v(r,\theta)=\sum\limits_{-\infty}^{+\infty}
   c_n(\psi)\bigg(\dfrac ra\bigg)^{|n|} e^{in\theta}.

.. end-toggle::

Tvöfaldar Fourier-raðir
-----------------------

Tvöfaldar Fourier-raðir
~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`{\varphi}:\overline D\to {{\mathbb  C}}` vera samfellt
deildanlegt á :math:`D=\{(x,y); 0<x<L, 0<y<M\}` og samfellt á lokuninni
:math:`\overline  D`. Ef :math:`{\varphi}` er jafnt :math:`0` á jaðrinum
:math:`{\partial}D`, þá getum við liðað :math:`{\varphi}` í
Fourier-sínusröð með tilliti til :math:`y`

.. math::

  {\varphi}(x,y)= \sum\limits_{m=1}^{\infty} 
   {\varphi}_m(x)\sin\big(m{\pi}y/M\big),

þar sem :math:`{\varphi}_m` er :math:`m`-ti Fourierstuðull fallsins
:math:`y\mapsto {\varphi}(x,y)`,

.. math::

  {\varphi}_m(x)= \dfrac 2M \int_0^M
   {\varphi}(x,y)\sin\big(m{\pi}y/M\big)\, dy.

Nú er fallið :math:`{\varphi}_m` samfellt deildanlegt og tekur gildið
:math:`0` í :math:`x=0` og :math:`x=L`, svo við getum liðað það í
Fourier-sínusröð. Ef við látum :math:`b_{n,m}` tákna :math:`n`-ta
Fourier-sínusstuðul fallsins :math:`{\varphi}_m`,

.. math::

  b_{n,m}({\varphi}) = \dfrac 4{LM} \int_0^L\int_0^M
   {\varphi}(x,y) \sin\big(n{\pi}x/L\big)\sin\big(m{\pi}y/M\big)
   \, dxdy,

þá fáum við framsetningu á :math:`{\varphi}` með tvöfaldri Fourier-röð,

.. math::

  {\varphi}(x,y)=\sum\limits_{n=1}^{{\infty}}
   \sum\limits_{m=1}^{{\infty}} b_{n,m}({\varphi})
   \sin\big(n{\pi}x/L\big)\sin\big(m{\pi}y/M\big).

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Poisson-jafnan á ferhyrningi

Leysum nú Poisson-jöfnuna á rétthyrningi með óhliðruðum jaðarskilyrðum

.. math::

  \begin{cases}
   \Delta u=f(x,y),
   &0<x<L, 0<y<M, \\
   u(0,y)=u(L,y)=0,
   &0<y<M,\\
   u(x,0)=u(x,M)=0,
   &0<x<L.
   \end{cases}

Vegna jaðarskilyrðanna göngum við út frá liðun á lausninni í tvöfalda
Fourier-sínusröð,

.. math::

  u(x,y)=\sum\limits_{m=1}^{\infty}\sum\limits_{n=1}^{\infty}
   u_{n,m} \sin\big(n{\pi}x/L\big)\sin\big(m{\pi}y/M\big).

Við gefum okkur einnig að við þekkjum Fourier-stuðla fallsins :math:`f`,

.. math::

  f(x,y)=\sum\limits_{m=1}^{\infty}\sum\limits_{n=1}^{\infty}
   f_{n,m} \sin\big(n{\pi}x/L\big)\sin\big(m{\pi}y/M\big).

Nú látum við Laplace-virkjann verka lið fyrir lið í summunni
fyrir :math:`u(x,y)`

.. math::

  \begin{aligned}
   \Delta u=&
   \sum\limits_{m=1}^{\infty}\sum\limits_{n=1}^{\infty}
   u_{n,m}\bigg(\dfrac{\partial^2u}{\partial x^2}
   +\dfrac{\partial^2u}{\partial y^2}\bigg) 
   \sin\big(n{\pi}x/L\big)\sin\big(m{\pi}y/M\big)\\
   &=
   \sum\limits_{m=1}^{\infty}\sum\limits_{n=1}^{\infty}
   u_{n,m}\big(-n^2{\pi}^2/L^2-m^2{\pi}^2/M^2\big) 
   \sin\big(n{\pi}x/L\big)\sin\big(m{\pi}y/M\big)\\
   &=
   \sum\limits_{m=1}^{\infty}\sum\limits_{n=1}^{\infty}
   f_{n,m}\sin\big(n{\pi}x/L\big)\sin\big(m{\pi}y/M\big)=f(x,y).\end{aligned}

Með því að bera saman stuðlana í þessum tveimur röðum, þá fáum við
lausnarformúluna

.. math::

  u(x,y)=\dfrac{-1}{\pi^2}
   \sum\limits_{m=1}^{\infty}\sum\limits_{n=1}^{\infty}
   \dfrac{f_{n,m}}{n^2/L^2+m^2/M^2}
    \sin\big(n{\pi}x/L\big)\sin\big(m{\pi}y/M\big).

.. end-toggle::

Ef við breytum jaðarskilyrðinu þannig að
:math:`{\partial}\varphi/{\partial} n=0` á öllum jaðrinum nema í hornpunktunum, þá er hægt með nákvæmlega
sömu röksemdafærslu og hér að framan að liða :math:`\varphi` í tvöfalda
Fourier-kósínusröð,

.. math::

  {\varphi}(x,y)=\sum\limits_{n=0}^{{\infty}}
   \sum\limits_{m=0}^{{\infty}} a_{n,m}({\varphi})
   \cos\big(n{\pi}x/L\big)\cos\big(m{\pi}y/M\big),

þar sem

.. math::

  a_{n,m}({\varphi}) = \dfrac {{\alpha}_{n,m}}{LM} \int_0^L\int_0^M
   {\varphi}(x,y) \cos\big(n{\pi}x/L\big)\cos\big(m{\pi}y/M\big)
   \, dxdy.

og :math:`{\alpha}_{0,0}=1`, :math:`{\alpha}_{0,m}={\alpha}_{n,0}=2`,
:math:`{\alpha}_{n,m}=4`, :math:`n,m=1,2,3,\dots`.

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Varmaleiðni í plötu

Við skulum nú leysa varmaleiðnijöfnuna á ferhyrningi með
Neumann-skilyrði á jaðrinum, en þau segja að jaðarinn sé einangraður,

.. math::

  \begin{cases}
   \dfrac{{\partial} u}{{\partial} t}
   -{\kappa}\bigg(\dfrac{\partial^2u}{\partial x^2}
   +\dfrac{\partial^2u}{\partial y^2}\bigg)=0,
   &0<x<L, 0<y<M, t>0,\\
   {\partial}_xu(0,y,t)={\partial}_xu(L,y,t)=0,
   &0<y<M, t>0,\\
   {\partial}_yu(x,0,t)={\partial}_yu(x,M,t)=0,
   &0<x<L, t>0,\\
   u(x,y,0)=\varphi(x,y), 
   &0<x<L, 0<y<M,
   \end{cases}

þar sem :math:`\varphi` er gefið fall á
:math:`D=\{(x,y); 0<x<L, 0<y<M\}`. Við úrlausn á þessu verkefni göngum
við út frá liðun á fallinu :math:`u` í Fourier-kósínusröð með stuðlum
sem eru háðir tíma,

.. math::

  u(x,y,t)=\sum\limits_{n=0}^{{\infty}}
   \sum\limits_{m=0}^{{\infty}} u_{n,m}(t)
   \cos\big(n{\pi}x/L\big)\cos\big(m{\pi}y/M\big),

og setjum upphafsskilyrðin einnig fram með sams konar Fourier-röð. Til
einföldunar skulum við skrifa
:math:`v_{n,m}(x,y)=\cos\big(n{\pi}x/L\big)\cos\big(m{\pi}y/M\big)`. Við
sjáum nú strax að :math:`u_{n,m}(0)=a_{n,m}({\varphi})`. Við látum
varmaleiðnivirkjann verka lið fyrir lið í röðinni fyrir :math:`u` og
fáum þá

.. math::

  \begin{aligned}
   \big({\partial}_t-{\kappa}\Delta \big)u&=
   \sum\limits_{n=0}^{\infty}\sum\limits_{m=0}^{\infty}
   \big({\partial}_t-{\kappa}
   {\partial^2_x}-{\kappa}
   {\partial^2_y}\big)u_{n,m}(t) 
   v_{n,m}(x,y)\\
   &=
   \sum\limits_{n=0}^{\infty}\sum\limits_{m=0}^{\infty}
   \big(u_{n,m}{{^{\prime}}}(t)+{\kappa}(n^2{\pi}^2/L^2+m^2{\pi}^2/M^2)
   \big)u_{n,m}(t) v_{n,m}(x,y)=0.\end{aligned}

Fourier-stuðlar fallsins :math:`u` verða því að uppfylla

.. math::

  u_{n,m}{{^{\prime}}}(t)+{\kappa}(n^2{\pi}^2/L^2+m^2{\pi}^2/M^2)u_{n,m}(t)=0,
   \quad \text{ og } \qquad u_{n,m}(0)=a_{n,m}({\varphi}).

Lausnin verður því

.. math::

  u(x,y,t)=\sum\limits_{n=0}^{{\infty}}
   \sum\limits_{m=0}^{{\infty}} 
   a_{n,m}({\varphi})e^{-{\kappa}{\pi}^2(n^2/L^2+m^2/M^2)t}
   \cos\big(n{\pi}x/L\big)\cos\big(m{\pi}y/M\big).

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Rétthyrnd tromma

Nú hugsum við okkur að himna sé strekkt á rétthyrndan ramma
:math:`D=\{(x,y); 0<x<L, 0<y<M\}` og að hún sveiflist þar. Í :ref:`sýnidæmi <sytrommabylgjujafnaitveimurrumviddum>`
sáum við að færsla efnispunkts :math:`(x,y)` frá jafnvægisstöðu
:math:`u(x,y,t)` uppfyllir tvívíðu bylgjujöfnuna. Ef staða og hraði
trommunnar er gefinn við tímann :math:`t=0`, þá er :math:`u` lausn
verkefnisins

.. math::

  \begin{cases}
   \dfrac{{\partial^2} u}{{\partial} t^2}
   -c^2\bigg(\dfrac{\partial^2u}{\partial x^2}
   +\dfrac{\partial^2u}{\partial y^2}\bigg)=0,
   &0<x<L, 0<y<M, t>0,\\
   u(0,y,t)=u(L,y,t)=0,
   &0<y<M, t>0,\\
   u(x,0,t)=u(x,M,t)=0,
   &0<x<L, t>0,\\
   u(x,y,0)=\varphi(x,y), \ {\partial}_tu(x,y,0)={\psi}(x,y), 
   &0<x<L, 0<y<M.
   \end{cases}

Við liðum lausnina í tvöfalda Fourier-röð

.. math::

  u(x,y,t)=\sum\limits_{n=1}^{{\infty}}
   \sum\limits_{m=1}^{{\infty}} u_{n,m}(t)
   \sin\big(n{\pi}x/L\big)\sin\big(m{\pi}y/M\big).

Við látum bylgjuvirkjann verka lið fyrir lið í summunni og sjáum þá að
:math:`u_{n,m}` verður að uppfylla annars stigs jöfnuna

.. math:: u_{n,m}{{^{\prime\prime}}}(t)+c^2{\pi}^2(n^2/L^2+m^2/M^2)u_{n,m}=0,

en almenn lausn hennar er

.. math::

  u_{n,m}(t)=A_{n,m}\cos\big(\sqrt{n^2/L^2+m^2/M^2}\, {\pi}ct\big)
   +B_{n,m}\sin\big(\sqrt{n^2/L^2+m^2/M^2}\, {\pi}ct\big).

Út frá upphafsskilyrðunum sjáum við síðan að

.. math::

  A_{n,m}=b_{n,m}({\varphi}) \qquad \text{ og } \qquad
   B_{n,m}=\dfrac{b_{n,m}({\psi})}{\sqrt{n^2/L^2+m^2/M^2}\, {\pi}c}.

Leyfilegar tíðnir í sveiflunni eru því

.. math:: \{\tfrac 12\sqrt{n^2/L^2+m^2/M^2}\, c; n,m=1,2,3,\dots\}.

Lægsta tíðnin :math:`\frac 12\sqrt{1/L^2+1/M^2}\, c` nefnist
*grunntíðni* og hinar tíðnirnar nefnast *yfirtíðnir*. Greinilegt er að
yfirtíðnirnar eru ekki heiltölumargfeldi af grunntíðninni eins og við
sáum í hliðstæðu verkefni fyrir sveiflandi streng. Þetta fyrirbæri er
einnig eiginleiki hringlaga tromma, en það er miklu erfiðara að sýna
fram á það. Þetta er skýringin á því hvers vegna trommur gefa ekki frá
sér hreinan tón eins og strengir.

.. end-toggle::

Eiginfallaraðir
---------------

Eiginfallaraðir
~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`P(x,D_x)` sé venjulegur afleiðuvirki af
Sturm-Liouville-gerð á bilinu :math:`[a,b]`,

.. math::

  P(x,D_x)v=\dfrac 1{\varrho(x)}\bigg(
   -\dfrac d{dx}\bigg(p(x)\dfrac{dv}{dx}\bigg)+q(x)v \bigg),\qquad x\in [a,b],

að :math:`B=(B_1,B_2)` sé almennur jaðargildisvirki á :math:`[a,b]`,

.. math::

  B_jv=\alpha_{j1}v(a)+\alpha_{j2}v{{^{\prime}}}(a)+
   \beta_{j1}v(b)+\beta_{j2}v{{^{\prime}}}(b), \qquad j=1,2,

að :math:`P(x,D_x)` sé samhverfur með tilliti til jaðarskilyrðanna
:math:`Bv=0` og að :math:`P(x,D_x)` sé reglulegur virki, samkvæmt
skilgreiningum okkar í síðasta kafla. Þá hefur
eigingildisverkefnið

.. math:: P(x,D_x)v=\lambda v, \qquad Bv=0,

óendanlega runu af eigingildum

.. math:: \lambda_0<\lambda_1<\lambda_2\cdots \to +\infty

og tilsvarandi runu af raungildum eiginföllum

.. math:: u_0,u_1,u_2,\dots.

Eiginföllin eru innbyrðis hornrétt í þeim skilningi að

.. math::

  {{\langle u_j,u_k\rangle}}=\int_a^bu_j(x)u_k(x)\varrho(x)\, dx=0, 
   \qquad j\neq k.

Ef :math:`v` er tvisvar samfellt deildanlegt og uppfyllir óhliðruðu
jaðarskilyrðin :math:`Bv=0`, þá er

.. math:: v(x)=\sum\limits_{n=0}^{\infty} c_nu_n(x),

þar sem Fourier-stuðlar :math:`v` með tilliti til eiginfallanna eru

.. math::

  c_n=\int_a^bv(x)u_n(x)\varrho(x)\, dx \bigg/
   \int_a^bu_n(x)^2\varrho(x)\, dx.

Oft er hægt að leysa hlutafleiðujöfnur með jaðarskilyrðum með því að
gefa sér liðun á lausninni í eiginfallaröð með tilliti til einnar
breytistærðar með stuðlum sem eru háðir hinum.

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Varmaleiðni

Við skulum nú líta á alhæft varmaleiðniverkefni

.. math::

  \begin{cases}
   \dfrac{\partial u}{\partial t}+P(x,\partial_x)u=f(x,t), 
   &x\in ]a,b[, \ t>0,\\
   u(x,0)=\varphi(x), & x\in ]a,b[,\\
   B_1u(\cdot,t)=B_2u(\cdot,t)=0, &t>0.
   \end{cases}

Hér er :math:`u` fall af tveimur breytistærðum :math:`(x,t)` og
:math:`B_ju(\cdot,t)` táknar að jaðargildisvirkinn :math:`B_j` verki með
tilliti til fyrri breytistærðarinnar :math:`x`. Við ákvörðum lausnina
:math:`u` með þeirri lausnartilgátu að hægt sé að liða hana í
eiginfallaröð

.. math:: u(x,t)=\sum\limits_{n=0}^{\infty} c_n(t)u_n(x),

þar sem Fourier-stuðlarnir með tilliti til eiginfallanna eru tímaháðir
og gefnir með formúlunni

.. math::

  c_n(t)=\int_a^bu(x,t)u_n(x)\varrho(x)\, dx \bigg/
   \int_a^bu_n(x)^2\varrho(x)\, dx.

Fyrst öll eiginföllin uppfylla jaðarskilyrðin, þá er augljóst að fallið
:math:`u` uppfyllir þau einnig, því við megum láta jaðargildisvirkjana
verka lið fyrir lið í summunni fyrir :math:`u`. Nú hugsum við okkur
einnig að föllin :math:`f` og :math:`\varphi` séu sett fram með
eiginfallaröðum

.. math::

  f(x,t)=\sum\limits_{n=0}^{\infty} f_n(t)u_n(x), \qquad
   \varphi(x)=\sum\limits_{n=0}^{\infty} \varphi_nu_n(x).

Ef við látum síðan hlutafleiðuvirkjann verka lið fyrir lið í
eiginfallaröð :math:`u`, notum upphafsskilyrðin og jöfnuna
:math:`P(x,D_x)u_n={\lambda}_nu_n`, þá fáum við

.. math::

  \begin{aligned}
   \dfrac{{\partial}u}{{\partial} t}(x,t) +P(x,{\partial}_x)u(x,t)&=
   \sum\limits_{n=0}^{\infty}\bigg( 
   \dfrac{{\partial}}{{\partial} t} +P(x,{\partial}_x)\bigg)c_n(t)u_n(x)
   \label{13.7.6}\\
   &=\sum\limits_{n=0}^{\infty}\bigg( 
   c_n{{^{\prime}}}(t)u_n(x)+c_n(t)P(x,D_x)u_n(x)\bigg)\nonumber\\
   &=\sum\limits_{n=0}^{\infty}\bigg( 
   c_n{{^{\prime}}}(t)+{\lambda}_nc_n(t)\bigg)u_n(x)\nonumber\\
   &=\sum\limits_{n=0}^{\infty} f_n(t)u_n(x)=f(x,t),\nonumber\\
   u(x,0)&=\sum\limits_{n=0}^{\infty} c_n(0)u_n(x)
   =\sum\limits_{n=0}^{\infty} {\varphi}_nu_n(x)={\varphi}(x).\nonumber\end{aligned}

Með því að bera saman stuðlana í jöfnunum, þá fáum við
upphafsgildisverkefni fyrir :math:`c_n(t)`,

.. math::

  \begin{cases}
   c_n{{^{\prime}}}(t)+{\lambda}_nc_n(t)=f_n(t),\\
   c_n(0)={\varphi}_n.
   \end{cases}

Þetta er fyrsta stigs jafna með fastastuðla, svo

.. math::

  c_n(t)={\varphi}_ne^{-{\lambda}_n t}+
   e^{-{\lambda}_n t}\int_0^te^{{\lambda}_n {\tau}}f_n({\tau})\, d{\tau}.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Bylgjujafna

Nú skulum við líta á hliðstætt dæmi fyrir alhæfða bylgjujöfnu

.. math::

  \begin{cases}
   \dfrac{\partial^2 u}{\partial t^2}+P(x,\partial_x)u=f(x,t), 
   &x\in ]a,b[, \ t>0,\\
   u(x,0)=\varphi(x),\ {\partial}_tu(x,0)={\psi}(x), & x\in ]a,b[,\\
   B_1u(\cdot,t)=B_2u(\cdot,t)=0, &t>0.
   \end{cases}

Við hugsum okkur nákvæmlega sams konar framsetningu á :math:`u`,
:math:`f` og :math:`{\varphi}` og í síðasta sýnidæmi og bætum
við liðun á :math:`{\psi}`,

.. math:: {\psi}(x)=\sum\limits_{n=0}^{\infty}{\psi}_nu_n(x).

Við látum hlutafleiðuvirkjann verka lið fyrir lið í eiginfallasummunni

.. math::

  \begin{aligned}
   \dfrac{{\partial}^2u}{{\partial} t^2}(x,t) +P(x,{\partial}_x)u(x,t)&=
   \sum\limits_{n=0}^{\infty}\bigg( 
   \dfrac{{\partial}^2}{{\partial} t^2} +P(x,{\partial}_x)\bigg)c_n(t)u_n(x)
   \\
   &=\sum\limits_{n=0}^{\infty}\bigg( 
   c_n{{^{\prime\prime}}}(t)u_n(x)+c_n(t)P(x,D_x)u_n(x)\bigg)\nonumber\\
   &=\sum\limits_{n=0}^{\infty}\bigg( 
   c_n{{^{\prime\prime}}}(t)+{\lambda}_nc_n(t)\bigg)u_n(x)\nonumber\\
   &=\sum\limits_{n=0}^{\infty} f_n(t)u_n(x)=f(x,t),\nonumber\\
   u(x,0)&=\sum\limits_{n=0}^{\infty} c_n(0)u_n(x)
   =\sum\limits_{n=0}^{\infty} {\varphi}_nu_n(x)={\varphi}(x),\nonumber\\
   {\partial}_tu(x,0)&=\sum\limits_{n=0}^{\infty} c_n{{^{\prime}}}(0)u_n(x)
   =\sum\limits_{n=0}^{\infty} {\psi}_nu_n(x)={\psi}(x).\nonumber\end{aligned}

Eftir stuðlasamanburð fáum við að :math:`c_n(t)` verður að uppfylla

.. math::

  \begin{cases}
   c_n{{^{\prime\prime}}}(t)+{\lambda}_nc_n(t)=f_n(t),\\
   c_n(0)={\varphi}_n, \quad c_n{{^{\prime}}}(0)={\psi}_n.
   \end{cases}

Nú er lausnarformúlan fyrir :math:`c_n` háð því hvert formerkið er á
eigingildinu :math:`{\lambda}_n`:

\(i) :math:`{\lambda}_n>0`, :math:`{\lambda}_n={\beta}_n^2`,
:math:`{\beta}_n>0`. Hér mynda :math:`\cos {\beta}_nt` og
:math:`\sin {\beta}_nt` lausnagrunn fyrir óhliðruðu jöfnuna og
Green-fall virkjans er :math:`\sin({\beta}_n(t-{\tau}))/{\beta}_n`. Þar
með er

.. math::

  c_n(t)={\varphi}_n\cos({\beta}_nt)+\dfrac {{\psi}_n}{{\beta}_n}
   \sin({\beta}_nt)+\int_0^t\dfrac{\sin({\beta}_n(t-{\tau}))}{{\beta}_n}
   f_n({\tau}) \, d{\tau}.

\(ii) :math:`{\lambda}_n=0`. Í þessu tilfelli mynda :math:`1` og
:math:`t` lausnagrunn fyrir óhliðruðu jöfnuna og Green-fallið er
:math:`t-{\tau}`. Þar með er

.. math:: c_n(t)={\varphi}_n+{\psi}_nt+\int_0^t(t-{\tau})f_n({\tau})\, d{\tau}.

\(iii) :math:`{\lambda}_n<0`, :math:`{\lambda}_n=-{\gamma}_n^2`,
:math:`{\gamma}_n>0`. Hér fáum við lausnagrunninn
:math:`\cosh({\gamma}_nt)` og :math:`\sinh({\gamma}_nt)` og Green-fallið
:math:`\sinh({\gamma}_n(t-{\tau}))/{\gamma}_n`. Lausnin er því

.. math::

  c_n(t)={\varphi}_n\cosh({\gamma}_nt)+\dfrac {{\psi}_n}{{\gamma}_n}
   \sinh({\gamma}_nt)+\int_0^t\dfrac{\sinh({\gamma}_n(t-{\tau}))}{{\gamma}_n}
   f_n({\tau}) \, d{\tau}.

.. end-toggle::

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Laplace-jafna

Með eiginfallaliðun er oft hægt að leysa Laplace- og Poisson-jöfnurnar
með almennum jaðarskilyrðum á ferhyrningi. Við tökum eitt dæmi til þess
að útskýra þetta,

.. math::

  \begin{cases}
   \Delta u=0, &a<x<b, \ 0<y<L,\\
   B_1u(\cdot,y)=B_2u(\cdot,y)=0, &0<y<L,\\
   u(x,0)=0, \ u(x,L)=\varphi(x), &a<x<b,
   \end{cases}

þar sem :math:`B_1` og :math:`B_2` eru almennir jaðargildisvirkjar á
:math:`[a,b]` og :math:`\varphi` er gefið fall á :math:`[a,b]`. Við
gefum okkur nú sömu forsendur og rithátt og í síðustu tveimur 
sýnidæmum með :math:`P(x,D_x)=-D_x^2` og göngum út frá þeirri
lausnartilgátu að hægt sé að liða lausnina :math:`u(x,y)` í
eiginfallaröð

.. math:: u(x,y)=\sum\limits_{n=0}^{\infty} c_n(y)u_n(x).

Þá er greinilegt að jaðarskilyrðin :math:`B_1u(\cdot,y)=B_2u(\cdot,y)=0`
eru uppfylllt. Ef við látum nú :math:`-\Delta` verka lið fyrir lið í
summunni og setjum inn hin jaðarskilyrðin, þá fáum við

.. math::

  \begin{aligned}
   -\Delta u(x,y)
   &=\sum\limits_{n=0}^{\infty} 
   \bigg(-\dfrac{{\partial}^2}{{\partial}x^2}
   -\dfrac{{\partial}^2}{{\partial}y^2}\bigg)c_n(y)u_n(x)\\
   &=\sum\limits_{n=0}^{\infty} 
   \big(-c_n(y)u_n{{^{\prime\prime}}}(x)-c_n{{^{\prime\prime}}}(y)u_n(x)\big)\\
   &=\sum\limits_{n=0}^{\infty} 
   \big({\lambda}_nc_n(y)-c_n{{^{\prime\prime}}}(y)\big)u_n(x)=0,\\
   u(x,0)
   &=\sum\limits_{n=0}^{\infty} c_n(0)u_n(x)=0,\\
   u(x,L)
   &=\sum\limits_{n=0}^{\infty} c_n(L)u_n(x)
   =\sum\limits_{n=0}^{\infty} \varphi_nu_n(x)=\varphi(x).\end{aligned}

Út úr þessum jöfnum lesum við að stuðlarnir þurfa að uppfylla

.. math:: c_n{{^{\prime\prime}}}(y)={\lambda}_nc_n(y),\qquad c_n(0)=0, \qquad c_n(L)=\varphi_n.

Ef öll eigingildin eru jákvæð og við skrifum
:math:`{\lambda}_n={\beta}_n^2`, þá er :math:`c_n` gefið með formúlunni

.. math:: c_n(y)=\varphi_n\dfrac{\sinh({\beta}_ny)}{\sinh({\beta}_nL)}

og lausnarformúlan verður

.. math::

  u(x,y)=\sum\limits_{n=0}^{\infty} \varphi_nu_n(x)
   \dfrac{\sinh({\beta}_ny)}{\sinh({\beta}_nL)}.

.. end-toggle::

Látum :math:`P(x,D_x)`, :math:`x\in [a,b]`, og :math:`Q(y,D_y)`,
:math:`y\in [c,d]`, vera tvo afleiðuvirkja af Sturm-Liouville gerð og
:math:`B^1=(B_1^1,B_2^1)` og :math:`B^2=(B_1^2,B_2^2)` vera almenna
jaðargildisvirkja á bilunum :math:`[a,b]` og :math:`[c,d]`. Gerum ráð
fyrir að virkjarnir séu reglulegir og samhverfir með tilliti til
jaðarskilyrðanna. Lítum síðan á eigingildisverkefnin

.. math::

  \begin{gathered}
   P(x,D_x)u={\lambda}u, \quad x\in [a,b], \qquad  
   B_1^1u=B_2^1u=0, 
   \\
   Q(y,D_y)v={\mu}v, \quad y\in [c,d], \qquad 
   B_1^2v=B_2^2v=0.\end{gathered}

Við táknum eigingildin og eiginföllin úr þeim með
:math:`({\lambda}_n,u_n)` og :math:`({\mu}_n,v_n)` og gerum ráð fyrir að
þeir myndi einingarréttan grunn með tilliti til innfeldanna sem
virkjarnir skilgreina og lýst er í síðasta kafla. Táknum vægisföllin í þessum
innfeldum með :math:`{\varrho}` og :math:`{\sigma}`. Látum nú
:math:`{\varphi}` vera tvisvar samfellt deildanlegt á rétthyrningnum
:math:`D=\{(x,y); a<x<b, c<y<d\}`, samfellt deildanlegt á lokuninni
:math:`\overline D` og gerum ráð fyrir að :math:`{\varphi}` uppfylli
jaðarskilyrðin

.. math::

  \begin{gathered}
   B_1^1{\varphi}(\cdot,y)=B_2^1{\varphi}(\cdot,y)=0, \qquad y\in [c,d],\\
   B_1^2{\varphi}(x,\cdot)=B_2^2{\varphi}(x,\cdot)=0, \qquad x\in [a,b]. \end{gathered}

Þá gefur sama röksemdafærsla og við beittum á tvöföldu
Fourier-raðirnar að hægt er að liða :math:`{\varphi}` í tvöfalda
eiginfallröð

.. math::

  {\varphi}(x,y)=\sum\limits_{n=1}^{\infty}\sum\limits_{m=1}^{\infty}
   c_{n,m}({\varphi})u_n(x)v_m(y),

þar sem stuðlarnir eru gefnir með formúlunni

.. math::

  c_{n,m}({\varphi})
   =\int_a^b\int_c^d {\varphi}(x,y)u_n(x)v_m(y){\varrho}(x){\sigma}(y)\, dxdy.

Sýnidæmi
^^^^^^^^

.. begin-toggle:: :label: Sýna dæmi: Varmaleiðni

Lítum nú á verkefnið

.. math::

  \begin{cases}
   \dfrac {\partial u}{{\partial}t}+P(x,{\partial}_x)u
   +Q(y,{\partial}_y)u=0,  &a<x<b, \ c<y<d, \ t>0,\\
   B_1^1u(\cdot,y,t)=B_2^1u(\cdot,y,t)=0, &c<y<d,\ t>0,\\ 
   B_1^2u(x,\cdot,t)=B_2^2u(x,\cdot,t)=0, &a<x<b,\ t>0,\\ 
   u(x,y,0)={\varphi}(x,y), &a<x<b, \  c<y<d,
   \end{cases}

þar sem forsendurnar eru þær sömu og lýst er hér að framan. Við finnum
lausnarformúlu fyrir þetta verkefni með því að liða :math:`u` í tvöfalda
eiginfallaröð með stuðlum :math:`w_{n,m}` sem eru háðir tíma. Með því að
láta virkjann verka lið fyrir lið í eiginfallaröðinni, þá fáum við að
:math:`w_{n,m}` verður að uppfylla
:math:`w_{n,m}{{^{\prime}}}(t)+({\lambda}_n+{\mu}_m)w_{n,m}(t)=0` með
upphafsskilyrðinu :math:`w_{n,m}(t)=c_{n,m}({\varphi})`. Svarið verður
því

.. math::

  u(x,y,t)=\sum\limits_{n=1}^{\infty}\sum\limits_{m=1}^{\infty}
   c_{n,m}({\varphi})e^{-({\lambda}_n+{\mu}_m)t} u_n(x)v_n(y).

.. end-toggle::

Æfingardæmi
-----------

Æfingardæmi
~~~~~~~~~~~

Dæmi
^^^^

Leysið hliðruðu bylgjujöfnuna með óhliðruðum hliðarskilyrðum,

.. math::

  {\partial}^2_tu-c^2 {\partial}^2_x u=f(x,t), \qquad
   u(0,t)=u(L,t)=0, \qquad
   u(x,0)={\partial}_tu(x,0)=0,

:math:`0<x<L`, :math:`t>0`, með því að liða fallið :math:`f` í
Fourier-sínusröð með tilliti til :math:`x` og ganga út frá sams konar
liðun á lausninni :math:`u`. [*Leiðbeining*: Skoðið :ref:`sýnidæmi <sysveiflandistrengurframhald>` og
:ref:`sýnidæmi <syvarmaleidnistangar>`.]

Dæmi
^^^^

Leysið bylgjujöfnuna með hliðruðum jaðarskilyrðum og óhliðruðum
upphafsskilyrðum

.. math::

  {\partial}^2_t u-c^2
   {\partial}^2_x u=0, \qquad
    u(0,t)=g(t), \ u(L,t)=h(t), \qquad 
   u(x,0)={\partial}_tu(x,0)=0,

:math:`0<x<L`, :math:`t>0`, þar sem föllin :math:`g` og :math:`h` eru
tvisvar samfellt deildanleg á :math:`{{\mathbb  R}}_+`. Gangið út frá
því að gefið sé fall :math:`w(x,t)`, sem uppfyllir jaðarskilyrðin,
þ.e. \ :math:`w(0,t)=g(t)` og :math:`w(L,t)=h(t)`. Skrifið
:math:`u(x,t)=w(x,t)+v(x,t)` og sýnið fram á að þá uppfylli :math:`v`
hliðraða bylgjujöfnu með hliðruðum upphafsskilyrðum, en óhliðruðum
jaðarskilyrðum. Notið síðan niðurstöðuna úr dæmi 1 og :ref:`sýnidæmi <sysveiflandistrengurframhald>` til
þess að skrifa upp lausnarformúlu fyrir :math:`u`.

Dæmi
^^^^

\(i) Skrifið upp lausnarformúluna í síðasta dæmi í því sértilfelli að
:math:`w(x,t)=g(t)(L-x)/L+h(t)x/L`. Reiknið út Fourier-sínusraðir
fallanna :math:`x\mapsto x/L` og :math:`x\mapsto (L-x)/L`.

\(ii) Skoðið sértilfellið þegar föllin :math:`g` og :math:`h` eru fastar.

Dæmi
^^^^

Leysið dæmi 2 í því sértilfelli að :math:`g(t)=0` og :math:`h(t)=\sin ({\omega} t)`. Fyrir hvaða gildi á :math:`{\omega}` fæst herma í
sveiflunni?

Dæmi
^^^^

Leysið verkefnið í dæmi 1 í því sértilfelli að :math:`f` er einungis háð
:math:`x` en ekki :math:`t` með eftirfarandi aðferð: Finnið fyrst
lausnina :math:`w` sem uppfyllir
:math:`-c^2w{{^{\prime\prime}}}(x)=f(x)`, :math:`w(0)=0` og
:math:`w(L)=0`. Skrifið :math:`u(x,t)=w(x)+v(x,t)` og sýnið að :math:`v`
sé þá lausn á verkefni, sem leyst var í :ref:`sýnidæmi <sysveiflandistrengurframhald>`. Notið þá
lausnarformúlu til þess að ákvarða :math:`u`.

Dæmi
^^^^

Ákvarðið lausnarformúlu fyrir varmaleiðniverkefni með hliðruðum
jaðarskilyrðum

.. math::

  {\partial}_t u-{\kappa}
   {\partial}^2_x u =0, \quad 
   {\partial}_x u(0,t)=g(t), \quad  {\partial}_xu(L,t)=h(t), \quad 
   u(x,0)=0,

:math:`0<x<L`, :math:`t>0`, þar sem föllin :math:`g` og :math:`h` eru
samfellt deildanleg á :math:`{{\mathbb  R}}_+`. Gangið út frá því að
gefið sé fallið :math:`w(x,t)` sem uppfylli jaðarskilyrðin
:math:`{\partial}_xw(0,t)=g(t)` og :math:`{\partial}_xw(L,t)=h(t)`.
Skrifið :math:`u(x,t)=w(x,t)+v(x,t)` og sýnið fram á að :math:`v`
uppfylli hliðraða varmaleiðnijöfnu með hliðruðum upphafsgildum en
óhliðruðum jaðargildum. Notið niðurstöðuna úr :ref:`sýnidæmi <syvarmaleidnistangar>` til þess að
skrifa upp lausnarformúlu fyrir :math:`u`.

Dæmi
^^^^

\(i) Skrifið upp lausnarformúluna í síðasta dæmi í því sértilfelli að
:math:`w(x,t)=g(t)x(L-x)^2/L^2-h(t)(L-x)x^2/L^2`. Reiknið út
Fourier-kósínusraðir fallanna :math:`x\mapsto x(L-x)^2/L^2` og
:math:`x\mapsto (L-x)x^2/L^2`.

\(ii) Skoðið sértilfellið þegar föllin :math:`g` og :math:`h` eru fastar.

Dæmi
^^^^

Liðið fallið :math:`{\varphi}` sem skilgreint er með
:math:`\varphi(x)=2x`, ef :math:`0\leq x\leq 1/2`, og
:math:`{\varphi}(x)=2-2x`, ef :math:`1/2\leq x\leq 1`, í sínusröð og
notið röðina til þess að finna lausn á verkefninu

.. math::

  {\partial}_t^2u+2{\partial}_tu-{\partial}_x^2u=0, \quad
   u(x,0)=\varphi(x), \quad {\partial}_tu(x,0)=0, \quad 
   u(0,t)=u(1,t)=0,

þar sem :math:`0<x<1`, :math:`t>0`.

Dæmi
^^^^

Leysið jaðargildisverkefnið

.. math::

  {\partial}_x^2u+{\partial}_y^2u=0, \quad
   u(0,y)=u(L,y)=0, \quad 
   u(x,0)=0, \quad u(x,M)=x(L-x),

þar sem :math:`0<x<L`, :math:`0<y<M`, :math:`L>0` og :math:`M>0`.

Dæmi
^^^^

Notið Fourier-raðir til þess að leysa verkefnið

.. math::

  \partial^2_xu
   +\partial^2_yu+u=0, \quad 
   u(0,y)=0, \quad  u(\pi,y)=y(\pi-y), \quad  
   u(x,0)=0, \quad  u(x,\pi)=0,

þar sem :math:`0<x<\pi` og :math:`0<y<\pi`.

Dæmi
^^^^

Leysið jaðargildisverkefnið

.. math::

  \Delta u=0,  \quad 
   u(0,y)=u(L,y)=0, \quad 
   \lim\limits_{y\to +{\infty}} u(x,y)=0,\quad 
   u(x,0)=\varphi(x),

þar sem :math:`0<x<L`, :math:`y>0` og :math:`\varphi` er gefið fall á
:math:`[0,L]`.

Dæmi
^^^^

Leysið Dirichlet-verkefnið í hringkraga með því að skipta yfir í pólhnit
og setja lausnina fram með Fourier-röð:

.. math::

  \begin{cases}
   \Delta u=0, &0<a^2<x^2+y^2<b^2,\\
   u(x,y)={\varphi}(x,y), &x^2+y^2=a^2,\\
   u(x,y)={\psi}(x,y), &x^2+y^2=b^2.
   \end{cases}

Dæmi
^^^^

Leysið Dirichlet-verkefnið utanvert við hring og setjið lausnina fram
með Fourier-röð:

.. math::

  \begin{cases}
   \Delta u=0, &x^2+y^2>a^2>0,\\
   u(x,y)={\varphi}(x,y), &x^2+y^2=a^2,\\
   u(x,y) \text{ takmarkað í ${\infty}$}.
   \end{cases}

Dæmi
^^^^

Finnið lausnina á Robin-verkefninu

.. math::

  \Delta u=0,   \quad \text{ á } D_a, \qquad
   \dfrac{{\partial}u}{{\partial} n}+{\alpha}u=h, \quad \text{ á }
   {\partial} D_a,

þar sem :math:`D_a=\{(x,y); x^2+y^2<a^2\}`, :math:`{\alpha}` er fasti
og :math:`h` er gefið samfellt fall á jaðri skífunnar.

Dæmi
^^^^

Ákvarðið lausn á jaðargildisverkefninu

.. math::

  \begin{cases}
   \Delta  u=
   \dfrac 1r\dfrac{{\partial}}{{\partial} r}
   \bigg(r\dfrac{{\partial}u}{{\partial} r}\bigg)
   +\dfrac 1{r^2}\dfrac{{\partial}^2u}{{\partial}{\theta}^2}=0,
   & 1<r<2, \ 0<{\theta}<{\pi}/4,\\
   u(1,{\theta})=0, \ u(2,{\theta})={\theta}({\pi}/4-{\theta}), 
   &0\leq {\theta}\leq {\pi}/4,\\
   u(r,0)=u(r,{\pi}/4)=0, &1\leq r\leq 2,
   \end{cases}

með því að ganga út frá þeirri lausnartilgátu að hægt sé að setja
lausnina fram með Fourier-sínusröð í :math:`\theta` með stuðlum sem eru
háðir :math:`r`.

Dæmi
^^^^

Látum fallið :math:`f` vera gefið með formúlunni

.. math::

  f(t)=\tfrac 12(T_0+T_1)+\tfrac 12(T_1-T_0)\cos\big({\omega} t\big),
   \qquad t\in {{\mathbb  R}},

þar sem :math:`{\omega}=2{\pi}/T`, :math:`T_1>T_0`. Reiknið út lausnina
:math:`u(x,t)` á 

.. math::

  \begin{cases}
   \dfrac{\partial u}{\partial t}-\kappa
   \dfrac{\partial^2 u}{\partial x^2}=0, &x>0, \ t\in {{\mathbb  R}},\\
   u(0,t)=f(t), &t\in {{\mathbb  R}},\\
   u(x,t) \text{ takmarkað ef } & x\to +\infty.
   \end{cases}

í þessu tilfelli.

Dæmi
^^^^

Látum :math:`f` vera gefið með formúlunni í síðasta dæmi og gefum okkur
gildin :math:`T=1\text{ár}\approx \,3\cdot 10^7 s`,
:math:`{\kappa}= 10^6` fyrir klöpp og :math:`{\kappa}= 1.5\cdot 10^6`
fyrir sand, :math:`T_1=11^\circ C`, :math:`T_0=-1^\circ C`. Teiknið upp
lausnina :math:`u(x,t)` á verkefninu í síðasta dæmi yfir eina lotu með
tilliti til tíma fyrir nokkur gildi á :math:`x`. Fyrir hvaða gildi á
:math:`x` er fasahliðrunin :math:`\frac 12` ár? Fyrir hvaða gildi á
:math:`x` er árssveiflan í hitastiginu orðin :math:`1\%` af
árssveiflunni á yfirborðinu?

Dæmi
^^^^

Beitið aðskilnaði breytistærða til þess að ákvarða sveiflur strengs, þar
sem tekið er tillit til núnings,

.. math::

  {\partial}^2_tu-c^2{\partial}^2_xu+a{\partial}_tu=0, 
   \qquad u(0,t)=u(L,t)=0,  \qquad u(x,0)={\varphi}(x),

:math:`0<x<L` og :math:`t>0`.

Dæmi
^^^^

Beitið aðskilnaði breytistærða til þess að ákvarða sveiflur strengs, þar
sem tekið er tillit til fjöðrunar,

.. math::

  {\partial}^2_tu-c^2{\partial}^2_xu+ku=0, 
   \qquad u(0,t)=u(L,t)=0,  \qquad u(x,0)={\varphi}(x),

:math:`0<x<L` og :math:`t>0`.

Dæmi
^^^^

Beitið aðskilnaði breytistærða til þess að leysa bitajöfnuna með
einfaldlega undirstuddum endum, en það er verkefnið

.. math::

  \begin{gathered}
   {\partial}^2_tu+a^4{\partial}_x^4u=0, \quad
   u(x,0)={\varphi}(x), \quad {\partial}_tu(x,0)={\psi}(x),
   \\
   u(0,t)={\partial}^2_xu(0,t)=u(L,t)={\partial}_x^2u(L,t)=0, \quad\end{gathered}

þar sem :math:`0<x<L`, :math:`t>0` og
:math:`a=\root 4 \of {EI/{\varrho}A}` og stærðirnar eru skilgreindar í
:ref:`sýnidæmi <sysveifluribitumbitajafna>`. Hver er grunntíðni sveiflunnar?

Dæmi
^^^^

Leysið bitajöfnuna í dæmi 3, en gerið ráð fyrir því að bitinn sé
einfaldlega undirstuddur í punktinum :math:`x=0` en innspenntur í
:math:`x=L`. Það þýðir að jaðarskilyrðin breytast í

.. math:: u(0,t)={\partial}^2_xu(0,t)=u(L,t)={\partial}_xu(L,t)=0.

Athugið að hér fæst eigingildisverkefni þar sem afleiðujafnan er af
stigi :math:`4`. Gefið ykkur að eiginföllin myndi grunn þannig að hægt
sé að liða sérhvert fall, sem er samfellt deildanlegt á köflum og
samfellt, í eiginfallaröð.

Dæmi
^^^^

Leysið bitajöfnuna í dæmi 3, en gerið ráð fyrir því að bitinn sé
einfaldlega undirstuddur í punktinum :math:`x=0` en frjáls í punktinum
:math:`x=L`. Það þýðir að jaðarskilyrðin breytast í

.. math:: u(0,t)={\partial}^2_xu(0,t)={\partial}_x^2u(L,t)={\partial}_x^3u(L,t)=0.

Dæmi
^^^^

Leysið hliðruðu bylgjujöfnuna á ferhyrningi

.. math::

  \begin{cases}
   \dfrac{{\partial}^2 u}{{\partial} t^2}
   -c^2\bigg(\dfrac{\partial^2u}{\partial x^2}
   +\dfrac{\partial^2u}{\partial y^2}\bigg)=f(x,y,t),
   &0<x<L, 0<y<M, t>0,\\
   u(0,y,t)=u(L,y,t)=0,
   &0<y<M, t>0,\\
   u(x,0,t)=u(x,M,t)=0,
   &0<x<L, t>0,\\
   u(x,y,0)={\partial}_tu(x,y,0)=0, 
   &0<x<L, 0<y<M.
   \end{cases}

Dæmi
^^^^

Færsla efnispunkta í rétthyrndri þunnri plötu, sem er einfaldlega
undirstudd á jaðrinum uppfyllir jaðargildisverkefnið

.. math::

  \begin{cases}
   \dfrac{{\partial}^2 w}{{\partial} t^2}
   +a^4\Delta ^2w=0,\\
   w(0,y,t)=w(L,y,t)={\partial}^2_xw(0,y,t)={\partial}^2_xw(L,y,t)=0,\\
   w(x,0,t)=w(x,M,t)={\partial}^2_yw(x,0,t)={\partial}^2_yw(x,M,t)=0,\\
   w(x,y,0)=\varphi(x,y), \quad {\partial}_tw(x,y,0)={\psi}(x,y), 
   \end{cases}

þar sem :math:`0<x<L`, :math:`0<y<M` og :math:`t>0`. Athugið að
jaðarskilyrðin segja að færslan og beygjuvægið séu núll á jaðrinum.
Finnið formúlu fyrir lausn þessa verkefnis.

Dæmi
^^^^

(*Dirichlet-verkefni á teningi.*) Setjum
:math:`D=\{(x,y); 0<x<L, 0<y<M\}` og látum :math:`T` vera teninginn
:math:`\{(x,y,z); 0<x<L, 0<y<M, 0<z<N\}`. Finnið formúlu fyrir lausn
verkefnisins

.. math::

  \begin{cases}
   \Delta u=
   \dfrac{{\partial}^2u}{{\partial}x^2}+
   \dfrac{{\partial}^2u}{{\partial}y^2}+
   \dfrac{{\partial}^2u}{{\partial}z^2}=0
   &(x,y,z)\in T,\\
   u(x,y,0)=0,\  u(x,y,N)=\varphi(x,y), &(x,y)\in D,\\
   u(x,y,z)=0, &(x,y)\in {\partial}D, \ 0<z<N.
   \end{cases}

með því að ganga út frá þeirri lausnartilgátu að hægt sé að liða
:math:`u` í tvöfalda Fourier-röð með Fourier-stuðla, sem eru háðir
:math:`z`. Hvernig verður lausnarformúlan ef sett eru almenn Dirichlet
skilyrði á allan jaðarinn?

Dæmi
^^^^

(*Þrefaldar Fourier-raðir.*) Látum :math:`T` vera teninginn
:math:`\{(x,y,z); 0<x<L, 0<y<M, 0<z<N\}` og
:math:`{\varphi}:\overline T\to {{\mathbb  C}}` vera fall sem er
samfellt deildanlegt á :math:`T`. Sýnið að ef :math:`{\varphi}` tekur
gildið :math:`0` á :math:`{\partial} T`, þá sé hægt að liða
:math:`{\varphi}` í þrefalda Fourier-sínusröð. Ákvarðið formúlu fyrir
stuðlana í röðinni.

Dæmi
^^^^

(*Poisson-jafnan á teningi.*) Látum :math:`T` vera teninginn
:math:`\{(x,y,z); 0<x<L, 0<y<M, 0<z<N\}`. Finnið formúlu fyrir lausn
verkefnisins

.. math::

  \begin{cases}
   \Delta u=
   \dfrac{{\partial}^2u}{{\partial}x^2}+
   \dfrac{{\partial}^2u}{{\partial}y^2}+
   \dfrac{{\partial}^2u}{{\partial}z^2}=f(x,y,z)
   &(x,y,z)\in T,\\
   u(x,y,z)=0,  &(x,y,z)\in {\partial}T,
   \end{cases}

með því að ganga út frá þeirri lausnartilgátu að hægt sé að liða
:math:`u` í þrefalda Fourier-sínusröð.

Dæmi
^^^^

Leysið bylgjujöfnuna með hliðarskilyrðum

.. math::

  \begin{cases}
   \dfrac{{\partial}^2u}{{\partial}t^2}
   -c^2\dfrac{{\partial}^2u}{{\partial}x^2}=f(x,t), &0<x<L, \ t>0,\\
   u(x,0)={\varphi}(x),\ {\partial}_tu(x,0)={\psi}(x), &0<x<L,\\
   u(0,t)={\partial}_xu(L,t)=0, &t>0.
   \end{cases}

Dæmi
^^^^

Leysið verkefnið

.. math::

  \begin{cases}
   \dfrac{{\partial}u}{{\partial} t}-{\kappa}
   \dfrac{{\partial}^2u}{{\partial}x^2}=f(x,t), &x\in ]0,L[, \ t>0,\\
   u(x,0)={\varphi}(x), &x\in ]0,L[,\\
   u(0,t)={\partial}_xu(0,t)=0, &t>0.
   \end{cases}

Dæmi
^^^^

Leysið jaðargildisverkefnið

.. math::

  \begin{cases}
   {\partial}_x^2u+{\partial}_y^2u=0, &0<x<L, \ 0<y<M,\\
   u(0,y)={\partial}_xu(L,y)=0, &0<y<M,\\
   u(x,0)=0, \quad u(x,M)=x(2L-x), &0<x<L,
   \end{cases}

þar sem :math:`L` og :math:`M` eru jákvæðar rauntölur.

Dæmi
^^^^

Látum :math:`L=P(x,D_x)` vera afleiðuvirkja af Sturm-Liouville-gerð, sem
er samhverfur með tilliti til jaðarskilyrðanna :math:`Bu=0`, þar sem
:math:`B` er almennur jaðargildisvirki á bilinu :math:`[a,b]`. Notið
eiginfallaliðun til þess að finna lausnarformúlu fyrir eftirfarandi
verkefni, ef gefið er fall :math:`w(x,t)`, sem uppfyllir hliðruðu
jaðarskilyrðin,

.. math::

  \begin{cases}
   \dfrac{{\partial} u}{{\partial}t}+P(x,D_x)u=0, &a<x<b, \ t>0,\\
   u(x,0)=0, & a<x<b,\\
   B_1u(\cdot,t)=g(t), \quad B_2(\cdot,t)=h(t).
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
   {\partial}_xu(0,t)=hu(L,t)+{\partial}_xu(L,t)=0, &t>0.
   \end{cases}

Dæmi
^^^^

Leysið eigingildisverkefnið

.. math::

  \begin{cases}
   -(1+x)^2v{{^{\prime\prime}}}={\lambda}v,  &0<x<1,\\
   v(0)=v(1)=0,
   \end{cases}

og notið lausnina til þess að finna formúlu fyrir lausn verkefnisins

.. math::

  \begin{cases}
   \dfrac{{\partial}^2u}{{\partial}t^2}
   -(1+x)^2\dfrac{{\partial}^2u}{{\partial}x^2}=0, &0<x<1, \ t>0,\\
   u(x,0)={\varphi}(x),\ {\partial}_tu(x,0)={\psi}(x), &0<x<1,\\
   u(0,t)=u(1,t)=0, &t>0.
   \end{cases}

Dæmi
^^^^

Látum :math:`L` tákna afleiðuvirkjann, sem skilgreindur er með

.. math:: Lu=P(x,D)u=-(1+x^2)\dfrac{d}{dx}\bigg((1+x^2)\dfrac{du}{dx}\bigg).

Sýnið að :math:`L e^{i{\beta}\arctan x}={\beta}^2e^{i{\beta}\arctan x}`
og notið niðurstöðuna til þess að ákvarða lausn á eiginigildisverkefninu

.. math:: Lu={\lambda}u, \qquad u(0)=0, \quad u{{^{\prime}}}(1)=0.

Notið síðan eiginföllin til þess að ákvarða formúlu fyrir lausnina á
verkefninu

.. math::

  \begin{cases}
   \dfrac{{\partial}^2 w}{{\partial} t^2}+P(x,{\partial}_x)w=0,
   &0<x<1, \ t>0,\\
   w(0,t)={\partial}_xw(1,t)=0, 
   &t>0,\\
   w(x,0)={\varphi}(x), 
   &0<x<1,\\
   {\partial}_tw(x,0)={\psi}(x), 
   &0<x<1.
   \end{cases}

Dæmi
^^^^

Leysið æstæðu varmaleiðnijöfnuna :math:`-{\kappa}\Delta u=f` á
:math:`D=\{(x,y);0<x<L, 0<y<M\}` þar sem hitastigið :math:`u(x,y)` er
:math:`T_0`, ef :math:`x=0`, og sá hluti jaðarsins, sem gefinn er með
jöfnunum :math:`x=L`, :math:`y=0` og :math:`y=M`, er varmaeinangraður.

Dæmi
^^^^

Leysið varmaleiðnijöfnuna :math:`{\partial}_tu-{\kappa}\Delta u=0` á
:math:`D=\{(x,y);0<x<L, 0<y<M\}` og fyrir :math:`t>0` með
upphafsgildunum :math:`{\varphi}(x,y)` og þeim jaðarskilyrðum að
hitastigið :math:`u(x,y)` sé :math:`T_0`, ef :math:`x=0` eða
:math:`y=0`, og að sá hluti jaðarsins, sem gefinn er með jöfnunum
:math:`x=L` og :math:`y=M`, sé varmaeinangraður.
