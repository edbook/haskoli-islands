Cauchy-setningin og Cauchy-formúlan
===================================


*A straight line may be the shortest distance between two points, but it is by no means the most interesting.*

\- The Doctor, Doctor Who

Vegheildi
---------

Upprifjun úr Stærðfræðigreiningu II
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Heildun eftir ferlum (vegum) er mjög mikilvæg í tvinnfallagreiningu. Fjallað var um ferilheildi í Stærðfræðigreiningu II. Hér er sú umfjöllun rifjuð upp og sett í samhengi.

----------------

(A) Samfelld vörpun :math:`\gamma:[a,b]\rightarrow {\mathbb{C}}` kallast stikaferill. Myndmengi stikaferils, mengið :math:`\mbox{mynd}(\gamma)=\{\gamma(t)\mid t\in [a,b]\}`, kallast ferill.

    Stikaferill sem er samfellt deildanlegur á köflum kallast vegur. (Stikaferill er samfellt deildanlegur á köflum ef til eru tölur :math:`a=b_0<b_1<\cdots<b_n=b` þannig að stikaferillinn er samfellt diffranlegur á opnu bilunum :math:`(b_i, b_{i+1})` og báðar einhliða afleiður eru skilgreindar í punktunum :math:`b_i`.)

    Stikaferill :math:`\gamma:[a,b]\rightarrow {\mathbb{C}}` er sagður lokaður ef :math:`\gamma(a)=\gamma(b)`. Lokaður ferill, eða stikaferill, er sagður einfaldur ef hann sker ekki sjálfan sig nema í endapunktunum, þ.e.a.s. ekki eru til ólíkar tölur :math:`t_1\in (a,b)` og :math:`t_2\in [a,b]` þannig að :math:`\gamma(t_1)=\gamma(t_2)`.

--------

(B) Ef :math:`\gamma:[a,b]\rightarrow {\mathbb{C}}` er vegur sem stikar feril :math:`C` þá má skilgreina lengd ferilsins með formúlunni

    .. math::



        L(C)=L(\gamma)=\int_a^b|\gamma'(t)|\,dt.

    Ef :math:`f` er samfellt tvinntölugilt fall á :math:`C` þá er heildi :math:`f` með tilliti til bogalengdar skilgreint sem

    .. math::


     \int_C f\,ds=\int_a^b f(\gamma(t))|\gamma'(t)|\,dt.

    Líka táknað

    .. math::


        \int_\gamma f\,ds, \qquad \int_C f\,|dz|,\qquad \int_\gamma f\,|dz|.

    Heildi með tilliti til bogalengdar eru óháð vali á stikun og stefnu stikunar.

--------

(C) Heildi vigursviðs :math:`\mathbf{F}:{\mathbb R}^2\rightarrow {\mathbb R}^2` eftir veg :math:`\gamma:[a,b]\rightarrow {\mathbb R}^2` er skilgreint sem heildið

    .. math::


        \int_\gamma \mathbf{F}\cdot d\gamma=\int_a^b\mathbf{F}(\gamma(t))\cdot \gamma'(t)\,dt.

    Ef við ritum :math:`\mathbf{F}(x,y)=(f(x,y),g(x,y))` og :math:`\gamma(t)=(\alpha(t), \beta(t))` þá má líka rita heildið sem

    .. math::

        \int_C f\,dx+g\,dy=\int_a^b f(\alpha(t), \beta(t))\alpha'(t)\,dt+g(\alpha(t), \beta(t))\beta'(t)\,dt.

    Heildi vigursviðs yfir veg er háð stikun að því marki að ef stefnu stikunar er breytt breytist formerki heildis.

Skilgreining (Sjá §3.1)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Ritum :math:`z=x+iy` og látum :math:`f` vera fall af :math:`z`. Látum :math:`\gamma: [a,b]\rightarrow {\mathbb{C}}` vera veg sem stikar feril :math:`C` og ritum
	:math:`\gamma(t)=\alpha(t)+i\beta(t)`. Heildi :math:`f` yfir :math:`C` er skilgreint sem

	.. math::


	    \int_C f\,dz=\int_\gamma f\,dz=\int_a^b f(\gamma(t))\gamma'(t)\,dt.

	Einnig má rita

	.. math::

	   \begin{aligned}
	   \int_C f\,dz&=\int_a^b f(\gamma(t))\gamma'(t)\,dt\\
	   &=\int_a^b f(\gamma(t)(\alpha'(t)+i\beta'(t))\,dt\\
	   &=\int_a^b f(\gamma(t))\alpha'(t)\,dt
	   +if(\gamma(t))\beta'(t)\,dt\\
	   &= \int_C f\,dx+if\,dy.\end{aligned}

	Athugið að ef stefnu stikunar er breytt þá breytist formerki á heildi.

Dæmi
~~~~~

.. admonition:: Dæmi
	:class: daemi

	(i) Línustrikið frá :math:`z_0` til :math:`z_1` má stika með stikaferli :math:`\gamma:[0,1]\rightarrow {\mathbb{C}}` þannig að

	.. math::


	    \gamma(t)=z_0+t(z_1-z_0)=(1-t)z_0+tz_1.

	(ii) Hring með miðju í punkti :math:`m` og geisla :math:`r` má stika með stikaferli :math:`\gamma:[0,2\pi]\rightarrow {\mathbb{C}}` þannig að

	.. math::


	    \gamma(t)=m+re^{it}=m+r(\cos t+i\sin t).

Setning (Sjá §3.1)
~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	.. math::

	   \left|\int_C f(z)\,dz\right|\leq \int_C |f(z)|\, |dz|\leq
	   \max_{z\in C}|f(z)|\int_C|dz|= \max_{z\in C}|f(z)|L(C).

Setning (Sjá Setningu 3.1.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Gerum ráð fyrir að :math:`X` sé opið mengi og :math:`f\in C(X)`. Ef :math:`f` hefur stofnfall :math:`F`, þ.e.a.s. ef til er fall :math:`F\in {\cal O}(X)` þannig að :math:`F'=f`, þá er

	.. math::


	    \int_\gamma f(z)\, dz = F(e_\gamma)-F(u_\gamma)

	fyrir sérhvern veg :math:`\gamma` í :math:`X` þar sem :math:`u_\gamma` er upphafspunktur :math:`\gamma` og :math:`e_\gamma` er endapunkturinn. Sérstaklega gildir

	.. math::


	    \int_\gamma f(z)\, dz = 0

	fyrir sérhvern lokaðan veg :math:`\gamma` í :math:`X`.

Fylgisetning. (Sjá Setning 3.1.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Fylgisetning
	:class: setning

	Látum :math:`X` vera svæði í :math:`{\mathbb{C}}` (:math:`X` er opið samanhangandi hlutmengi í :math:`{\mathbb{C}}`). Ef :math:`f` er fágað á :math:`X` og :math:`f'(z)=0` fyrir öll :math:`z\in X`, þá er :math:`f` fastafall.

Setning Green (Upprifjun úr Stærðfræðigreiningu II)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`\Omega` vera opið mengi í planinu með jaðar :math:`\partial \Omega` sem við gerum ráð fyrir að samanstandi af endanlega mörgum lokuðum ferlum sem hver um sig er samfellt deildanlegur á köflum. Áttum jaðarinn jákvætt þannig að ef gengið er eftir jaðri samkvæmt gefinni stefnu þá er :math:`\Omega` á vinstri hönd. Ef :math:`f` og :math:`g` eru samfellt deildanleg föll þá er

	.. math::


	    \int_{\partial \Omega} f\,dx+g\,dy=\int\!\!\int_\Omega \left(\partial_x g-\partial_y f\right)\,dx\,dy.

	Föllin :math:`f` og :math:`g` mega líka vera tvinntölugild því þá reiknar maður raun- og þverhluta heildis sitt í hvoru lagi og setningin gildir um hvort tveggja.

Skilgreining og upprifjun. (Sjá §2.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Ritum :math:`z=x+iy` og :math:`f=u+iv`. Setjum nú

	.. math::

	   \partial_x f=\partial_x u+i\partial_xv\qquad\mbox{ og }\qquad
	   \partial_y f=\partial_y u+i\partial_yv.

	Rifjum upp að Wirtinger-afleiðurnar eru skilgreindar með formúlunum

	.. math::

	   \partial_z f=\tfrac{1}{2}(\partial_xf-i\partial_yf)\qquad\mbox{ og }\qquad
	   \partial_{\overline{z}} f=\tfrac{1}{2}(\partial_xf+i\partial_yf).

	Cauchy-Riemann jöfnurnar :math:`\partial_xu=\partial_yv` og :math:`\partial_yu=-\partial_xv` jafngilda því að

	.. math::


	    \partial_{\overline{z}} f=\tfrac{1}{2}(\partial_xf+i\partial_yf)=0.

Cauchy-setning (Sjá Setning 3.3.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`X` vera opið hlutmengi í :math:`{\mathbb{C}}`. Gerum ráð fyrir að :math:`\Omega` sé opið hlutmengi af :math:`X` og að :math:`\partial \Omega\subseteq X`. Gerum enn fremur ráð fyrir að jaðarinn :math:`\partial \Omega` samanstandi af endanlega mörgum sundurlægum lokuðum einföldum vegum sem eru áttaðir jákvætt með tilliti til :math:`\Omega`. Ef :math:`f\in C^1(X)`, þá er

	.. math::

	   \int_{\partial\Omega}f\, dz = i\iint_\Omega
	   (\partial_xf+i\partial_yf)\, dxdy.

	Ef :math:`f\in {\cal O}(X)`, þá er

	.. math::


	    \int_{\partial\Omega}f\, dz = 0.

Skilgreining (Sjá Skilgreiningu 3.3.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Opið mengi :math:`X` kallast stjörnusvæði með tilliti til punktsins :math:`\alpha\in X`, ef línustrikið :math:`\langle \alpha, z \rangle` er innihaldið í :math:`X` fyrir sérhvert :math:`z\in X`. Við segjum að :math:`X` sé stjörnusvæði ef það er stjörnusvæði með tilliti til einhvers punkts.

Setning (Sjá Setningu 3.3.3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Ef :math:`X` er stjörnusvæði með tilliti til punktsins :math:`\alpha`, þá hefur sérhvert :math:`f\in {\cal O}(X)` stofnfall :math:`F` (þ.e.a.s. :math:`F'=f`), sem gefið er með formúlunni

	.. math::


	    F(z)=\int_{\langle \alpha, z\rangle} f(\zeta)\, d\zeta, \qquad z\in X.

	og þar með gildir

	.. math::


	    \int_\gamma f\, dz =0

	fyrir sérhvern lokaðan veg :math:`\gamma` í :math:`X`.

Cauchy-formúlan. (Sjá Setningu 3.3.4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Gerum ráð fyrir sömu forsendum og í Cauchy-setningunni. Ef :math:`f\in C^1(X)`, þá gildir um sérhvert :math:`z\in \Omega` að

	.. math::

	   \begin{aligned}
	   f(z)=&\dfrac 1{2 \pi i}\int_{\partial\Omega}\dfrac
	   {f(\zeta)}{\zeta-z}\, d\zeta \\
	   &-\dfrac 1{2\pi}\iint_{\Omega}
	   \dfrac{(\partial_\xi+i\partial_\eta)f(\zeta)}
	   {\zeta-z}\, d\xi d\eta,
	   \end{aligned}

	þar sem breytan í heildinu er :math:`{\zeta}={\xi}+i\eta`. Ef
	:math:`f\in {\cal O}(X)`, þá er

	.. math::

	   f(z)=\dfrac 1{2 \pi i}\int_{\partial\Omega}\dfrac
	   {f(\zeta)}{\zeta-z}\, d\zeta.

Afleiðingar Cauchy-setningarinnar
---------------------------------

Meðalgildissetning (Sjá Setningu 3.3.5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`X` vera opið mengi í :math:`{\mathbb{C}}`, :math:`f\in {\cal O}(X)`, :math:`z\in X` og gerum ráð fyrir að :math:`\overline S(z,r)\subset X`. Þá gildir

	.. math::


	    f(z)=\dfrac 1{2\pi} \int_0^{2\pi}f(z+re^{it})\, dt.

Setning (Sjá Setningu 3.3.6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Gerum ráð fyrir að forsendur Cauchy-setningarinnar séu uppfylltar og að :math:`Q` sé margliða með einfaldar núllstöðvar :math:`\alpha_1,\dots,\alpha_m` og að engin þeirra liggi á :math:`\partial\Omega`. Þá er

	.. math::

	   \int_{\partial\Omega} \dfrac{f(z)}{Q(z)} \, dz =
	   2\pi i\sum_{\alpha_j\in \Omega}
	   \dfrac{f(\alpha_j)}{Q'(\alpha_j)}.


.. Þetta er comment og sést ekki :)
	Setning Goursat
	~~~~~~~~~~~~~~~

	.. admonition:: Setning
		:class: setning

		Látum :math:`f` vera tvinntölugilt fall skilgreint á opnu mengi :math:`X` í :math:`{\mathbb{C}}`. Gerum ráð fyrir að :math:`f` sé :math:`{\mathbb{C}}`-deildanlegt í sérhverjum punkti í :math:`X`. Þá er :math:`f` fágað á :math:`X`.


Cauchy-formúlur fyrir afleiður. (Sjá Setningu 3.4.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`X` og :math:`\Omega` vera eins og í Cauchy-setningunni og tökum :math:`z\in \Omega`. Þá er sérhvert :math:`f` í :math:`{\cal O}(X)` óendanlega oft deildanlegt á :math:`X`, allar hlutafleiður af :math:`f` eru fáguð föll og

.. math::

   f^{(n)}(z)=
   \dfrac {n!}{2\pi i}\int_{\partial\Omega}
   \dfrac {f(\zeta)}{(\zeta-z)^ {n+1}}\, d\zeta.

Cauchy-ójöfnur. (Sjá Fylgisetningu 3.4.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`X` er opið hlutmengi af :math:`{\mathbb{C}}`, :math:`\bar S(\alpha,\varrho)\subset X`, :math:`f\in {\cal O}(X)` og :math:`|f(z)|\leq M` fyrir öll :math:`z\in \partial
S(\alpha,\varrho)`, þá er

.. math::

   |f^{(n)}(\alpha)|\leq
   Mn!/\varrho^ n.

Setning Liouville (Sjá Setningu 3.4.6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`f\in {\cal O}({\mathbb{C}})` og gerum ráð fyrir að :math:`f` sé takmarkað fall (þ.e.a.s. til er fasti :math:`M` þannig að :math:`|f(z)|\leq M` fyrir öll :math:`z\in {\mathbb{C}}`) . Þá er :math:`f` fasti.

Undirstöðusetning algebrunnar (Sjá Setningu 3.4.7)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Sérhver margliða af stigi :math:`\geq 1` hefur núllstöð í :math:`{\mathbb{C}}`.



Setning Morera (Sjá Setningu 3.4.5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`X` vera opið mengi í :math:`{\mathbb{C}}`, :math:`f\in C(X)` og gerum ráð fyrir að

	.. math::


	    \int_{\partial\Omega} f\, dz =0

	fyrir sérhvert þríhyrningssvæði :math:`\Omega` þannig að :math:`\Omega\cup \partial \Omega\subset X`. Þá er :math:`f\in {\cal O}(X)`.

Fleiri afleiðingar Cauchy-setningarinnar
----------------------------------------

Fræðilegur bakgrunnur (Sjá §3.5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú munum við fást við spurninguna um hvenær má víxla röðinni á diffrun og summu og heildun og summu þegar fengist er við veldaraðir. Svarið er ekki augljóst og til að gera þetta almennilega þarf ný hugtök og þónokkra vinnu.

---------

(A) Látum :math:`A\subseteq {\mathbb{C}}` og :math:`f_n:A\rightarrow{\mathbb{C}}` vera föll.

    Segjum að :math:`f_n\rightarrow f` með :math:`f:A\rightarrow{\mathbb{C}}` ef fyrir sérhvert :math:`z\in A` gildir að :math:`f_n(z)\rightarrow f(z)`, þ.e.a.s. ef :math:`z\in A` þá er til fyrir sérhvert :math:`\epsilon>0` tala :math:`N_z` (hugsanlega háð :math:`z`) þannig að ef :math:`n\geq N_z` þá er :math:`|f(z)-f_n(z)|<\epsilon`.

    Segjum að :math:`f_n\rightarrow f` í jöfnum mæli þar sem :math:`f:A\rightarrow{\mathbb{C}}` ef fyrir sérhvert :math:`\epsilon>0` er til tala :math:`N` þannig að ef :math:`n\geq N` þá er :math:`|f(z)-f_n(z)|<\epsilon` fyrir öll :math:`z\in A`. (Sama :math:`N` dugar fyrir öll :math:`z\in A`.)

---------

(B) Látum nú :math:`X` vera opið mengi í :math:`{\mathbb{C}}` og :math:`f_n:X\rightarrow {\mathbb{C}}` vera föll. Ef :math:`f_n\rightarrow f` í jöfnum mæli á sérhverju lokuðuð takmörkuðu hlutmengi í :math:`X` og föllin :math:`f_n` eru öll samfelld þá er markgildið :math:`f` líka samfellt á :math:`X`.

    Ef :math:`\gamma` er vegur í :math:`X` þá er

    .. math::

       \lim_{n\rightarrow \infty}\int_\gamma f_n(z)\,dz=
       \int_\gamma \left(\lim_{n\rightarrow \infty}f_n(z)\right)\,dz=\int_\gamma f(z)\,dz.

    Ef föllin :math:`f_n` eru öll fáguð þá er markgildið :math:`f` líka fágað og :math:`f_n'\rightarrow f'` (í jöfnum mæli á lokuðum takmörkuðum hlutmengjum í :math:`X`).

---------

(C) (:math:`M`-próf Weierstrass) Látum :math:`f_n` vera runu falla sem öll eru skilgreind á mengi :math:`A`. Gerum ráð fyrir að :math:`M_k` sé tala þannig að :math:`|f_k(z)|\leq M_k` fyrir öll :math:`z\in A` og að röðin :math:`\sum_{n=0}^\infty M_k` sé samleitin. Þá er röðin :math:`\sum_{n=0}^\infty f_n` samleitin í jöfnum mæli á :math:`A` að fallinu :math:`f(z)=\sum_{n=0}^\infty f_n(z)`. (Þ.e.a.s. fallarunan :math:`g_k=\sum_{n=0}^k f_n` stefnir á :math:`f` í jöfnum mæli á :math:`A`.)

Setning Abels
~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Skoðum veldaröð :math:`\sum_{n=0}^\infty a_n(z-\alpha)^n` með samleitnigeisla :math:`\varrho>0`. Ef :math:`0<r<\varrho` þá er veldaröðin samleitin í jöfnum mæli á opnu hringskífunni :math:`{S}(\alpha,r)`.

---------

Samkvæmt ofangreindu gildir að ef :math:`f(z)=\sum_{n=0}^\infty a_n(z-\alpha)^n` þá er

.. math::


    f'(z)=\sum_{n=1}^\infty na_n(z-\alpha)^{n-1}

fyrir öll :math:`x\in S(\alpha,\varrho)` og ef :math:`\gamma` er vegur í :math:`S(\alpha, \varrho)` þá er

.. math::

   \int_\gamma f(z)\,dz
   =\int_\gamma \left(\sum_{n=0}^\infty a_n(z-\alpha)^n\right)\,dz
   =\sum_{n=0}^\infty\int_\gamma a_n(z-\alpha)^n\,dz.



.. Látum nú :math:`f_n` vera runu fágaðra falla sem eru skilgreind á opnumengi :math:`X`. Ef :math:`\sum_{k=0}^n f_k\rightarrow f` í jöfnum mæli á lokuðum takmörkuðum hlutmengjum í :math:`X` þá er

.. .. math::

    f'(z)=\sum_{n=0}^\infty f_n'(z)

.. og ef :math:`\gamma` er vegur í :math:`X` þá er

.. .. math::

    \int_\gamma f(z)\,dz=\sum_{n=0}^\infty\int_\gamma f_n(z)\,dz.

Skilgreining (Sjá Skilgreiningu 3.6.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Ef :math:`X` er opið hlutmengi af :math:`{\mathbb{C}}`, :math:`\alpha\in X` og :math:`f\in {\cal O}(X)`, þá kallast veldaröðin

	.. math::


	    \sum\limits_{n=0}^\infty \dfrac{f^{(n)}(\alpha)}{n!}(z-\alpha)^n,

	Taylor-röð fágaða fallsins :math:`f` í punktinum :math:`\alpha`. Ef :math:`\alpha=0`, þá kallast hún Maclaurin-röð fágaða fallsins :math:`f`.

Setning (Sjá Setningu 3.6.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`X` vera opið hlutmengi af :math:`{\mathbb{C}}`, :math:`\alpha\in X`, :math:`\overline S(\alpha,\varrho)\subset X` og :math:`f\in {\cal O}(X)`, þá er unnt að setja :math:`f` fram með samleitinni veldaröð á skífunni :math:`S(\alpha,\varrho)`,

	.. math::

	   f(z)=\sum_{n=0}^ \infty a_n(z-\alpha)^ n,
	   \qquad z\in S(\alpha,\varrho),

	þar sem stuðlarnir :math:`a_n` eru ótvírætt ákvarðaðir og eru gefnir með

	.. math::


	    a_n=\dfrac {f^{(n)}(\alpha)}{n!}.

	Samleitnigeisli raðarinnar er stærri en eða jafn fjarlægðinni frá :math:`\alpha` út á jaðar :math:`X`.

	Fyrir :math:`z\in S(\alpha, \varrho)` er

	.. math::


	    f'(z)= \sum_{n=1}^\infty na_n(z-\alpha)^{n-1}.

Skilgreining (Sjá Skilgreiningu 3.6.3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Látum :math:`f\in {\cal O}(X)`. Segjum að :math:`\alpha` sé núllstöð :math:`f` af stigi :math:`m` (eða núllstöð af margfeldni :math:`m`) ef :math:`f(\alpha)=f'(\alpha)=\cdots=f^{(m-1)}(\alpha)=0` en :math:`f^{(m)}(\alpha)\neq 0`.

Setning (Sjá Setningu 3.6.4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Fall :math:`f\in {\cal O}(X)` hefur núllstöð af stigi :math:`m>0` í punktinum :math:`\alpha\in X` þá og því aðeins að til sé :math:`g\in {\cal O}(X)` þannig að :math:`g(\alpha)\neq 0` og

	.. math::


	    f(z)=(z-\alpha)^ mg(z), \qquad z\in X.

Samsendarsetning I (Sjá Setningu 3.7.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Ef :math:`X` er svæði í :math:`{\mathbb{C}}`, :math:`f,g\in {\cal O}(X)` og til er punktur :math:`{\alpha}` í :math:`X` þannig að :math:`f^{(n)}({\alpha})=g^{(n)}({\alpha})` fyrir öll :math:`n\geq 0`, þá er :math:`f(z)=g(z)` fyrir öll :math:`z\in X`.

Fylgisetning (Sjá Setningu 3.7.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Fylgisetning
	:class: setning

	Ef :math:`X` er svæði og :math:`f\in {\cal O}(X)` er ekki núllfallið, þá er núllstöðvamengi :math:`{\cal N}(f)=\{z\in X; f(z)=0\}` fallsins :math:`f` dreift hlutmengi af :math:`X`. (Þ.e.a.s. fyrir sérhvern punkt :math:`\alpha\in X` er til tala :math:`\varrho>0` þannig að hringskífan :math:`S(\alpha,\varrho)` inniheldur enga núllstöð :math:`f`, nema hugsanlega :math:`\alpha`.)

Samsemdarsetning II. (Sjá Setningu 3.7.3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Ef :math:`X` er svæði, :math:`f,g\in {\cal O}(X)` og :math:`f(a_j)=g(a_j)` þar sem :math:`\{a_j\}` er runa af ólíkum punktum, sem hefur markgildi :math:`a\in X`, þá er :math:`f(z)=g(z)` fyrir öll :math:`z\in X`.

Hágildislögmál I (Sjá Setningu 3.8.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Ef :math:`X` er svæði og :math:`f\in {\cal O}(X)`, þá getur :math:`|f(z)|` ekki haft staðbundið hágildi í :math:`X` nema :math:`f` sé fastafall.

Hágildislögmál II (Sjá Setning 3.8.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`X` vera takmarkað svæði og :math:`f\in {\cal O}(X)\cap C(\overline X)` (samfellt á lokuninni :math:`\overline X`). Þá tekur :math:`|f(z)|` hágildi á jaðri svæðisins :math:`\partial X`.
