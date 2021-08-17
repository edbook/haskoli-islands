Fáguð föll
==========

*Come on, Rory! It isn't rocket science, it's just quantum physics!*

\- The Doctor, Doctor Who


Markgildi og samfelldni
-----------------------

Skilgreining (Sjá §2.1)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Opin skífa með miðju :math:`\alpha` og
	geisla :math:`\varrho` er skilgreind sem mengið

	.. math:: S(\alpha,\varrho)=\{z\in {\mathbb{C}}\mid |z-\alpha|<\varrho\},

	lokuð skífa með miðju :math:`\alpha` og geisla :math:`\varrho` er
	mengið

	.. math:: \overline S(\alpha,\varrho)=\{z\in {\mathbb{C}}\mid |z-\alpha|\leq\varrho\}

	og götuð opin skífa með miðju :math:`\alpha` og geisla :math:`\varrho`
	er mengið

	.. math:: S^*(\alpha,\varrho)=\{z\in {\mathbb{C}}\mid 0<|z-\alpha|<\varrho\}.

Skilgreining
~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Hlutmengi :math:`X` í :math:`{\mathbb{C}}` er sagt vera opið ef
	um sérhvern punkt :math:`a\in X` gildir að til er opin skífa
	:math:`S(a,r)`, með :math:`r>0` sem er innihaldin í :math:`X`.

	Hlutmengi :math:`X` í :math:`{\mathbb{C}}` er sagt vera lokað ef fyllimengi þess
	:math:`{\mathbb{C}}\setminus X` er opið.

	Jaðar hlutmengis :math:`X` í :math:`{\mathbb{C}}` samanstendur af öllum punktum
	:math:`a\in {\mathbb{C}}` þannig að sérhver opin skífa :math:`S(a,r)` með
	:math:`r>0` sker bæði :math:`X` og :math:`{\mathbb{C}}\setminus X`. Við táknum
	jaðar :math:`X` með :math:`\partial X`.

	Punktur :math:`a\in {\mathbb{C}}` nefnist þéttipunktur mengisins :math:`X` ef um
	sérhvert :math:`r>0` gildir að gataða opna skífan :math:`S^*(a,r)`
	inniheldur punkta úr :math:`X`.

	Opið hlutmengi í :math:`{\mathbb{C}}` kallast svæði ef það er samanhangandi.

Skilgreining
~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Látum :math:`X` vera hlutmengi í :math:`{\mathbb{C}}` og
	:math:`f:X\rightarrow {\mathbb{C}}` vera fall. Ef :math:`a` er þéttipunktur
	:math:`X` þá segjum við að :math:`f(z)` stefni á tvinntölu :math:`L`
	þegar :math:`z` stefnir á :math:`a`, og ritum

	.. math::

	 \lim_{z\rightarrow a} f(z)=L

	ef um sérhvert :math:`\epsilon>0` gildir að til er :math:`\delta >0`
	þannig að ef :math:`0<|z-a|<\delta` þá er :math:`|f(z)-L|<\epsilon`.

	Segjum að fallið :math:`f` sé samfellt í punkti :math:`a\in X` ef

	.. math::

	 \lim_{z\rightarrow a} f(z)=f(a).

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

	Ef :math:`f` og :math:`g` eru tvinntölugild föll sem
	skilgreind eru á menginu :math:`X\subseteq {\mathbb{C}}`,
	:math:`\lim_{z\to a}f(z)=L` og :math:`\lim_{z\to a}g(z)=M`, þá er

	.. math::

	   \begin{gathered}
	   \lim_{z\to a}(f(z)+g(z))=\lim_{z\to a}f(z)+\lim_{z\to a}g(z)=L+M,\\
	   \lim_{z\to a}(f(z)-g(z))=\lim_{z\to a}f(z)-\lim_{z\to a}g(z)=L-M,\\
	   \lim_{z\to a}(f(z)g(z))=\big(\lim_{z\to a}f(z)\big)\big(\lim_{z\to
	   a}g(z)\big)=LM\\
	   \lim_{z\to a}\dfrac{f(z)}{g(z)}=\dfrac{\lim_{z\to a}f(z)}{\lim_{z\to
	   a}g(z)}=\dfrac LM.\end{gathered}

	Í síðustu formúlunni þarf að gera ráð fyrir að :math:`M\neq 0`. Ef
	:math:`f` og :math:`g` eru föll á mengi :math:`X` með gildi í :math:`{\mathbb{C}}`
	sem eru samfelld í punktinum :math:`a\in X`, þá eru föllin :math:`f+g`,
	:math:`f-g`, :math:`fg` og :math:`f/g` samfelld í :math:`a` og

	.. math::

	   \begin{gathered}
	   \lim_{z\to a}(f(z)+g(z))=f(a)+g(a),\\
	   \lim_{z\to a}(f(z)-g(z))=f(a)-g(a),\\
	   \lim_{z\to a}(f(z)g(z))=f(a)g(a),\\
	   \lim_{z\to a}\dfrac{f(z)}{g(z)}=\dfrac{f(a)}{g(a)},
	   \qquad \text{ef } \ g(a)\neq 0.\end{gathered}

	Ef :math:`f:X\to {\mathbb{C}}` og :math:`g:Y\to {\mathbb{C}}` eru föll,
	:math:`f(X)\subset Y`, :math:`a` er þéttipunkur :math:`X`,
	:math:`b=\lim_{z\to a}f(z)` er þéttipunktur mengisins :math:`Y` og
	:math:`g` er samfellt í :math:`b`, þá er

	.. math::

	 \lim_{z\to a} g\circ f(z)=g(\lim_{z\to a}f(z)).

.. admonition:: Athugasemd
	:class: athugasemd
	
	Skilgreining 2.3 er sambærileg skilgreiningu á markgildi úr Stærðfræðigreiningu I og II og Setning 2.4 er sambærileg og reiknireglur fyrir markgildi raungildra falla í Stærðfræðigreiningu I og II.

Fáguð föll
----------

Ritháttur (Sjá §2.1)
~~~~~~~~~~~~~~~~~~~~

Til samræmis við nótur Ragnars notum við annan
rithátt fyrir hlutafleiður en í Stærðfræðigreiningu II. Ef :math:`f` er
fall af raunbreytistærðum :math:`x` og :math:`y`, þá skrifum við

.. math::

   {\partial}_xf=\dfrac{\partial f}{\partial x}, \qquad
   {\partial}_yf=\dfrac{\partial f}{\partial y}, \qquad
   {\partial}_x^2f=\dfrac{\partial^2f}{\partial x^2}, \qquad
   {\partial}_{xy}^2f=\dfrac{\partial^2f}{\partial x\partial y}, \qquad
   {\partial}_{xxy}^3f=\dfrac{\partial^3f}{\partial x^2\partial y}, \ \dots.



Skilgreining (Sjá §2.1)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Ef :math:`X` er opið hlutmengi í :math:`{\mathbb{C}}`
	þá látum við :math:`C(X)` tákna mengi allra samfelldra falla
	:math:`f:X\to {\mathbb{C}}`. Við látum :math:`C^m(X)` tákna mengi allra
	:math:`m` sinnum samfellt deildanlegra falla. Hér er átt við að allar
	hlutafleiður fallsins :math:`f` af stigi :math:`\leq m` eru til og þar
	að auki samfelldar. Við skrifum :math:`C^0(X)=C(X)` og táknum mengi
	óendanlega oft deildanlegra falla með :math:`C^{\infty}(X)`.

Skilgreining (Sjá Skilgreining 2.2.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Látum :math:`f:X\to {\mathbb{C}}` vera
	fall skilgreint á opnu hlutmengi :math:`X` af :math:`{\mathbb{C}}`. Við segjum að
	:math:`f` sé :math:`{\mathbb{C}}`–deildanlegt í punktinum :math:`a\in X` ef
	markgildið

	.. math::

	   \lim _{\substack{ h\to 0\\ h\in{\mathbb{C}}}}
	    \dfrac{f(a+h)-f(a)}h  \label{4.2.3}

	er til. Markgildið er táknað með :math:`f'(a)` og kallað
	:math:`{\mathbb{C}}`–afleiða fallsins :math:`f` í punktinum :math:`a`.

	Fall :math:`f:X\to {\mathbb{C}}` er sagt vera fágað á opna menginu :math:`X` ef
	:math:`f\in
	C^1(X)` og :math:`f` er :math:`{\mathbb{C}}`–deildanlegt í sérhverjum punkti í
	:math:`X`.

	Við látum :math:`{\cal O}(X)` tákna mengi allra fágaðra falla á :math:`X`.

	Við segjum að :math:`f` sé fágað í punktinum :math:`a` ef til er opin
	grennd :math:`U` um :math:`a` þannig að :math:`f` sé fágað í :math:`U`.

	Fallið :math:`f` er sagt vera heilt fall (e. entire function) ef það er
	fágað á öllu :math:`{\mathbb{C}}`.

Setning (Sjá Setningu 2.2.3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`f,g:X\to {\mathbb{C}}` vera föll,
	:math:`a\in X`, :math:`\alpha,\beta\in {\mathbb{C}}` og gerum ráð fyrir að
	:math:`f` og :math:`g` séu :math:`{\mathbb{C}}`–deildanleg í :math:`a`. Þá gildir

	(i) :math:`\alpha f+\beta g` er :math:`{\mathbb{C}}`–deildanlegt í :math:`a` og

	.. math::

	 (\alpha f+\beta g)'(a)=\alpha f'(a)+\beta g'(a).

	(ii) (Leibniz-regla). :math:`fg` er :math:`{\mathbb{C}}`–deildanlegt í :math:`a` og

	.. math::

	 (fg)'(a)=f'(a)g(a)+f(a)g'(a).

	(iii) Ef :math:`g(a)\neq 0`, þá er :math:`f/g` :math:`{\mathbb{C}}`–deildanlegt í :math:`a` og

	.. math::

	 (f/g)'(a)=\dfrac{f'(a)g(a)-f(a)g'(a)}{g(a)^2}.

Setning (Sjá Setningu 2.2.6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`X` og :math:`Y` vera opin
	hlutmengi af :math:`{\mathbb{C}}`. Lát :math:`f:X\to {\mathbb{C}}` og :math:`g:Y\to {\mathbb{C}}` vera
	föll, þannig að :math:`f(X)\subset Y`, :math:`a\in X`, :math:`b\in Y`,
	:math:`b=f(a)` og setjum

	.. math::

	 h=g\circ f.

	(i) Ef :math:`f` er :math:`{\mathbb{C}}`–deildanlegt í :math:`a` og :math:`g` er :math:`{\mathbb{C}}`–deildanlegt í :math:`b`, þá er :math:`h` líka :math:`{\mathbb{C}}`–deildanlegt í :math:`a` og

	.. math::

	 h'(a)=g'(b)f'(a).

	(ii) Ef :math:`g` er :math:`{\mathbb{C}}`–deildanlegt í :math:`b`, :math:`g'(b)\neq 0`, :math:`h` er :math:`{\mathbb{C}}`–deildanlegt í :math:`a` og :math:`f` er samfellt í :math:`a`, þá er :math:`f` einnig :math:`{\mathbb{C}}`–deildanlegt í :math:`a` og

	.. math::

	 f'(a)=h'(a)/g'(b).

Fylgisetning (Sjá Fylgisetningu 2.2.7)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Fylgisetning
	:class: setning

	Látum :math:`X` og :math:`Y` vera opin hlutmengi af :math:`{\mathbb{C}}`, og :math:`f:X\to Y` vera gagntækt fall. Ef :math:`f` er :math:`{\mathbb{C}}`–deildanlegt í :math:`a` og :math:`f'(a)\neq 0`, þá er andhverfa fallið :math:`f^{[-1]}` líka :math:`{\mathbb{C}}`–deildanlegt í :math:`b=f(a)` og

	.. math::

	 \left(f^{[-1]}\right)'(b)= \dfrac 1{f'(a)}.\label{4.2.4}

Setning (Sjá Setningu 2.2.8)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`f=u+iv:X\to {\mathbb{C}}` vera fall af :math:`z=x+iy` á opnu hlutmengi :math:`X` í :math:`{\mathbb{C}}`. Ef :math:`f` er :math:`{\mathbb{C}}`–deildanlegt í :math:`a\in X`, þá eru báðar hlutafleiðurnar :math:`\partial_xf(a)` og :math:`\partial_yf(a)` til og

	.. math::

	 f'(a)=\partial_xf(a)=-i\partial_yf(a).

	Þar með gildir Cauchy–Riemann–jafnan

	.. math::

	 \tfrac 12\big(\partial_xf(a)+i\partial_yf(a)\big)=0,

	og hún jafngildir hneppinu

	.. math::

	 \partial_xu(a)=\partial_yv(a), \qquad \partial_yu(a)=-\partial_xv(a).

Skilgreining (Sjá §2.2)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Við skilgreinum fyrsta stigs hlutafleiðuvirkjana :math:`{\partial}_z={\partial}/{\partial}z` og :math:`{\partial}_{\bar z}={\partial}/{\partial}\bar z` með

	.. math::

	   {\partial}_zf=\dfrac{{\partial}f}{{\partial} z}
	   =\tfrac 12\big({\partial}_xf-i{\partial}_yf\big) \quad \text{ og } \quad
	   {\partial}_{\bar z}f=\dfrac{{\partial}f}{{\partial}\bar z}
	   =\tfrac 12\big({\partial}_xf+i{\partial}_yf\big)
	   \label{4.2.14}

	Tölurnar :math:`{\partial}_zf(a)` og :math:`{\partial}_{\bar z}f(a)`
	nefnast Wirtinger–afleiður fallsins :math:`f` í punktinum :math:`a` og
	virkinn :math:`{\partial}_{\bar z}` nefnist Cauchy–Riemann–virki

Setning (Sjá Setningu 2.2.10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`X` vera opið hlutmengi í :math:`{\mathbb{C}}`, :math:`a\in X` og :math:`f:X\to {\mathbb{C}}` vera fall. Þá gildir:

	(i) :math:`f` er :math:`{\mathbb{C}}`–deildanlegt í :math:`a` þá og því aðeins að :math:`f` sé deildanlegt í :math:`a` og :math:`{\partial}_{\bar z}f(a)=0`. Þá er :math:`f'(a)={\partial}_zf(a)`.

	(ii) :math:`f` er fágað í :math:`X` þá og því aðeins að :math:`f` sé samfellt deildanlegt í :math:`X` og uppfylli Cauchy–Riemann–jöfnuna :math:`{\partial}_{\bar z}f=0` í :math:`X`. Við höfum þá

	.. math::

	   f'=\dfrac{df}{dz}=\dfrac{\partial f}{\partial z}=\dfrac 12\bigg(
	   \dfrac{\partial f}{\partial x}-i\dfrac{\partial f}{\partial y}\bigg).

Tenging við línulegar varpanir.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Afleiða samfellt deildanlegrar vörpunar
:math:`f:\mathbb{R}^2\rightarrow\mathbb{R}^2` í punkti :math:`a` er línuleg vörpun
:math:`Df(a):\mathbb{R}^2\rightarrow\mathbb{R}^2`. Ef við hugsum :math:`f` sem vörpun
:math:`{\mathbb{C}}\rightarrow{\mathbb{C}}` þá er :math:`Df(a)` almennt bara
:math:`\mathbb{R}`-línuleg vörpun en :math:`f` er :math:`{\mathbb{C}}`-deildanlegt í
:math:`a` nákvæmlega þegar :math:`Df(a)` er :math:`{\mathbb{C}}`-línuleg vörpun.

Veldaraðir, veldisvísisfallið og lograr
---------------------------------------

Upprifjun úr Stærðfræðigreiningu I
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Veldaraðir þar sem stuðlar og breyta eru tvinntölur ,,virka‘‘ eins og veldaraðir með rauntölustuðlum og rauntölubreytu. Það eina sem þarf að breyta er að í stað samleitnibils er talað um samleitniskífu.

----------------

(A) Fáum í hendurnar röð :math:`\sum_{n=1}^\infty a_n` þannig að :math:`a_1, a_2, \ldots` eru tölur. Skilgreinum

.. math::

 s_n=a_1+a_2+\cdots+a_n

(summa fyrstu :math:`n` liða raðarinnar). Segjum að röðin :math:`\sum_{n=1}^\infty a_n` sé samleitin með summu :math:`s` ef :math:`\lim_{n\rightarrow\infty}s_n=s`, það er að segja, röðin er samleitin með summu :math:`s` ef

.. math::

 \lim_{n\rightarrow \infty}(a_1+a_2+\cdots+a_n)=s.

Ritað :math:`\sum_{n=1}^\infty a_n=s`.

----------------

(B) Um sérhverja veldaröð :math:`\sum_{n=0}^\infty a_n(z-\alpha)^n` gildir eitt af þrennu:

(i) Röðin er aðeins samleitin fyrir :math:`z=\alpha`.

(ii) Til er jákvæð tala :math:`\varrho` þannig að veldaröðin er alsamleitin fyrir öll :math:`z` þannig að :math:`|z-\alpha|<\varrho` og ósamleitin fyrir öll :math:`z` þannig að :math:`|z-\alpha|>\varrho`. Talan :math:`\varrho` kallast samleitnigeisli veldaraðarinnar.

(iii) Röðin er samleitin fyrir allar tvinntölur :math:`z`.

----------------

(C) Stundum má reikna út samleitnigeislann með eftirfarandi aðferðum:

(i) Gerum ráð fyrir að :math:`L=\lim_{n\rightarrow\infty}\left|\frac{a_{n+1}}{a_n}\right|` sé til eða :math:`\infty`. Þá hefur veldaröðin :math:`\sum_{n=0}^\infty a_n(z-\alpha)^n` samleitnigeisla

.. math::

   \varrho=\left\{\begin{array}{ll}
   \infty & \text{ef }L=0,\\
   \frac{1}{L} & \text{ef }0<L<\infty,\\
   0 & \text{ef }L=\infty.\\
   \end{array}
   \right.

(ii) Gerum ráð fyrir að :math:`L=\lim_{n\rightarrow\infty}\sqrt[n]{|a_n|}` sé til eða :math:`\infty`. Þá hefur veldaröðin :math:`\sum_{n=0}^\infty a_n(z-\alpha)^n` samleitnigeisla

.. math::

   \varrho=\left\{\begin{array}{ll}
   \infty & \mbox{ef }L=0,\\
   \frac{1}{L} & \mbox{ef }0<L<\infty,\\
   0 & \mbox{ef }L=\infty.\\
   \end{array}
   \right.

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`X\subseteq {\mathbb{C}}` vera opið mengi og látum
	:math:`f` vera fall skilgreint á :math:`X`.

	(i) (Sjá Setningu 2.3.2) Ef fyrir sérhvert :math:`\alpha\in X` er til tala :math:`\varrho>0` þannig að fyrir öll :math:`z\in S(\alpha, \varrho)` er

	.. math::

	 f(z)= \sum_{n=0}^\infty a_n(z-\alpha)^n

	þá er fallið :math:`f` fágað á :math:`X` og fyrir :math:`z\in S(\alpha, \varrho)` er

	.. math::

	 f'(z)= \sum_{n=1}^\infty na_n(z-\alpha)^{n-1}.

	(ii) (Sjá Setningu 2.3.5) Ef fallið :math:`f` er fágað þá er til fyrir sérhvern punkt :math:`\alpha\in X` tala :math:`\varrho>0` og veldaröð :math:`\sum_{n=0}^\infty a_n(z-\alpha)^n` sem er alsamleitin á :math:`S(\alpha, \varrho)` þannig að um alla punkta :math:`z\in S(\alpha, \varrho)` gildir að :math:`f(z)=\sum_{n=0}^\infty a_n(z-\alpha)^n`.

Setning (Sjá Fylgisetningu 2.3.6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Ef :math:`f\in {\cal O}(X)` þá er :math:`f'\in {\cal O}(X)`.

Setning (Samsemdarsetning fyrir samleitnar veldaraðir)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Gerum ráð fyrir að :math:`f,g\in {\cal O}(S(\alpha,\varrho))` séu gefin með samleitnum veldaröðum

	.. math::

	   f(z)=\sum\limits_{n=0}^\infty a_n(z-\alpha)^n, \qquad
	   g(z)=\sum\limits_{n=0}^\infty b_n(z-\alpha)^n, \qquad
	   z\in S(\alpha,\varrho),

	og gerum ráð fyrir að til sé runa :math:`\{\alpha_j\}` af ólíkum punktum í :math:`S(\alpha,\varrho)` þannig að :math:`\alpha_j\to \alpha` og :math:`f(\alpha_j)=g(\alpha_j)` fyrir öll :math:`j`. Þá er :math:`a_n=b_n` fyrir öll :math:`n` og þar með :math:`f(z)=g(z)` fyrir öll :math:`z\in S(\alpha,\varrho)`.

Setning (Sjá §2.4)
~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Fyrir sérhverja tvinntölu :math:`z` er

	.. math::

	 e^z=\sum_{n=0}^\infty \frac{z^n}{n!}.

Skilgreining (Sjá Skilgreiningu 2.5.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Látum :math:`X` vera opið hlutmengi af :math:`{\mathbb{C}}`. Samfellt fall :math:`\lambda:X\to {\mathbb{C}}` kallast logri á :math:`X` ef

	.. math::

	 e^{\lambda(z)}=z, \qquad z\in X.

	Samfellt fall :math:`\varrho:X\to {\mathbb{C}}` kallast :math:`n`–ta rót á :math:`X` ef

	.. math::

	 \big(\varrho(z)\big)^n=z, \qquad z\in X.

	Samfellt fall :math:`\theta:X\to \mathbb{R}` kallast horn á :math:`X` ef

	.. math::

	 z=|z|e^{i\theta(z)}, \qquad z\in X.

Setning (Sjá Setningu 2.5.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	(i) Ef :math:`\lambda` er logri á :math:`X`, þá er :math:`0\not\in X`, :math:`\lambda\in {\cal O}(X)` og

	.. math::

	 \lambda'(z)=\frac 1z, \qquad z\in X.

	Föllin :math:`\lambda(z)+i2\pi k`, :math:`k\in \mathbb{Z}` eru einnig lograr á :math:`X`.

	(ii) Ef :math:`\lambda` er logri á :math:`X`, þá er

	.. math::

	   \lambda(z)=\ln
	   |z|+i\theta(z), \qquad z\in X,

	þar sem :math:`\theta:X\to \mathbb{R}` er horn á :math:`X`. Öfugt, ef :math:`\theta:X\to \mathbb{R}` er horn á :math:`X`, þá er :math:`\lambda(z)=\ln|z|+i\theta(z)` logri á :math:`X`.

	(iii) Ef :math:`\varrho` er :math:`n`–ta rót á :math:`X` þá er :math:`\varrho\in {\cal O}(X)` og

	.. math:: \varrho'(z)=\frac {\varrho(z)}{nz}, \qquad z\in X.

	(iv) Ef :math:`\lambda` er logri á :math:`X`, þá er :math:`\varrho(z)=e^{\lambda(z)/n}` :math:`n`–ta rót á :math:`X`.

Skilgreining og setning (Sjá §2.5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Fyrir sérhverja tvinntölu :math:`{\alpha}` er hægt að skilgreina fágað veldisfall með veldisvísi :math:`\alpha` með

	.. math::

	 z^\alpha=\exp(\alpha\lambda(z)), \qquad z\in X,

	þar sem :math:`\lambda` er gefinn logri á :math:`X`.

.. admonition:: Setning
	:class: setning

	Út frá skilgreiningunni hér að ofan fáum við að

	.. math::

	   \begin{aligned}
	   \dfrac d{dz}z^\alpha=&\dfrac d{dz}e^{\alpha\lambda(z)}=e^{\lambda(z)}\frac
	   \alpha z =\alpha e^{\alpha\lambda(z)}e^{-\lambda(z)}\\
	   =&
	   \alpha e^{(\alpha-1)\lambda(z)}=\alpha z^{\alpha-1}.\end{aligned}

Skilgreining og setning (Sjá §2.5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Ef :math:`\lambda` er logri á opið mengi :math:`X\subseteq {\mathbb{C}}` og :math:`\alpha \in X`, þá skilgreinum við veldisvísisfall með grunntölu :math:`\alpha` sem fágaða fallið á :math:`{\mathbb{C}}`, sem gefið er með

	.. math::

	 \alpha^z=e^{z\lambda(\alpha)}.

	Athugið að skilgreiningin er háð valinu á logranum.

.. admonition:: Setning
	:class: setning

	Út frá skilgreiningunni hér að ofan og keðjureglunni fæst að

	.. math::

	   \dfrac d{dz}\alpha^z=
	   \dfrac d{dz}e^{z\lambda(\alpha)}=e^{z\lambda(\alpha)}\cdot
	   \lambda(\alpha)=\alpha^z\lambda(\alpha).

Skilgreining (Sjá §2.5)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Lítum nú á mengið :math:`X={\mathbb{C}}\setminus \mathbb{R}_-`, sem fæst með því að skera neikvæða raunásinn og :math:`0` út úr tvinntalnaplaninu. Við skilgreinum síðan pólhnit í :math:`X` og veljum hornið :math:`\theta(z)` þannig að :math:`-\pi<\theta(z)<\pi`, :math:`z\in X`. Fallið

	.. math::

	   {\operatorname{Arg}} :{\mathbb{C}}\setminus \mathbb{R}_-\to \mathbb{R}, \qquad
	   {\operatorname{Arg}} z=\theta(z),\quad z\in X

	0 er kallað höfuðgrein hornsins og formúla þess er í grein 1.1.10 (og bók §1.2.6.2),

	.. math::

	 {\operatorname{Arg}}\, z=2\arctan\bigg(\dfrac y{|z|+x}\bigg), \qquad z=x+iy\in X.

	Fallið

	.. math::

	   {\operatorname{Log}} :{\mathbb{C}}\setminus \mathbb{R}_-\to {\mathbb{C}}, \qquad
	   {\operatorname{Log}} z=\ln |z| +i{\operatorname{Arg}}(z),\quad z\in X,

	er kallað höfuðgrein lografallsins. Fallið

	.. math::

	 z^\alpha = e^{\alpha{\operatorname{Log}} z}, \qquad z\in {\mathbb{C}}\setminus \mathbb{R}_-,

	kallast höfuðgrein veldisfallsins með veldisvísi :math:`\alpha`.
