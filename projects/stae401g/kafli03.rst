Eigingildisverkefni
===================


Eigingildisverkefni
-------------------

Verkefnið að leysa afleiðujöfnu

.. math::
    Lu = \lambda u, \quad x\in I

þar sem

.. math::
    L = a_m(x) D^m + \cdots + a_1(x) D + a_0(x)

:math:`\lambda` er tvinntala og :math:`I` er bil, ásamt jaðalskilyrðum á :math:`u` á :math:`I`, kallast *eigingildisverkefni*. Verkefnið felst í að finna öll :math:`\lambda \in \mathbb{C}` þannig að afleiðujafnan hafi lausn, segjum :math:`u_\lambda`, sem uppfyllir gefin jaðarskilyrði og er ekki núllfallið. Slík gildi á :math:`\lambda` kallast eigingildi verkefnisins og tilsvarandi lausnir :math:`u_\lambda` kallast eiginföll.

.. admonition:: Athugasemd
	:class: athugasemd

	Athugið að ef við lítum á föll sem vigra og línulega virkja sem línulegar varpanir þá er greinileg samsvörun milli eigingildisverkefna og að finna eigingildi og eiginvigra fylkis eins og við þekkjum úr línulegri algebru.

Eigingildisverkefni koma til að mynda upp þegar hlutafleiðujöfnur eru leystar með aðskilnaði breytistærða eins og verður fjallað um síðar.

Hugmyndin að baki eigingildisverkefnum er sú að ef eiginföllinn mynda grunn í einhverju fallarúmi þá má rita sérhvert fall í því sem línulega (mögulega óendanlega) samantekt af eiginföllum. Lítum til dæmis á verkefnið

.. math::
    Lu = f

þar sem :math:`L` hefur eiginföll :math:`v_j` með tilssvarandi eigingildum :math:`\lambda_j`. Ef liða má :math:`f` í grunn eiginvigranna

.. math::
    f = \sum_{j} c_j v_j

þá fæst með losaralegum reikningum að

.. math::
    L \sum_{j} \frac{c_j}{\lambda_j} v_j =  \sum_{j} \frac{c_j}{\lambda_j} L v_j  = \sum_{j} \frac{c_j}{\lambda_j} \lambda_j v_j = f

og þar með er :math:`u = \sum_{j} \frac{c_j}{\lambda_j} v_j` lausn á verkefninu.

Dæmi
~~~~

.. admonition:: Dæmi
	:class: daemi

	Ef :math:`L = D` þá er sérhvert fall :math:`u_\alpha(x) = e^{\alpha x}` eiginfall með eigingildi :math:`\alpha` því

	.. math::
	    L u_\alpha(x) = D e^{\alpha x} = \alpha e^{\alpha x} = \alpha u_\alpha(x).

	Ef :math:`L = P(D)` þar sem :math:`P` er margliða með fasta stuðla þá er sérhvert fall :math:`u_\alpha(x)=e^{\alpha x}` eiginfall með eigingildi :math:`P(\alpha)` því

	.. math::
	    L u_\alpha(x) = P(D) e^{\alpha x} = P(\alpha) e^{\alpha x} = P(\alpha) u_\alpha(x).

	Í síðara tilfellinu er formleg lausn á verkefninu

	.. math::
	    Lu = f

	á forminu

	.. math::
	    u(x) = \sum_{j} \frac{c_n(f)}{P(\alpha_j)}e^{\alpha_j x}

	ef :math:`P(\alpha_j) \neq 0` fyrir öll :math:`j`, eins og við þekkjum úr umræðunni um Fourier-raðir.

	|
	|

	Eins og dæmið gefur til kynna má líta á Fourier-raðir sem sértilfelli af þeirri almennu hugmynd að liða föll í grunn eiginfalla afleiðuvirkja. Lítum nú nánar á það í næstu dæmum. Skoðum eigingildisverkefnið

	.. math::
	    Tu = \lambda u, \quad x\in ]0,L]

	þar sem :math:`T = -D^2` og :math:`L>0`, með ýmsum ólíkum jaðarskilyrðum. Tökum sérstaklega eftir því hvernig ólík jaðarskilyrði geta gefið ólík eigingildi og/eða ólík eiginföll.


Fallsjaðarskilyrði í báðum endapunktum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Lítum á jaðarskilyrðin

.. math::
    u(0) = u(L) = 0.

Ef :math:`\lambda = 0` er lausnin á forminu :math:`u(x) = A+ Bx` en jaðarskilyrðin ákvarða :math:`A=B=0` svo núllfallið er eina lausnin. Þar með er 0 ekki eigingildi.

Ef :math:`\lambda \neq 0` þá er lausnin á forminu :math:`u(x) = A \sin(\beta x) + B\cos(\beta x)` þar sem :math:`\beta` er tvinntala sem uppfyllir :math:`\beta^2 = \lambda` og má velja þannig að :math:`\operatorname{Re}(\beta)\geq 0`. Skilyrðið :math:`u(0) = 0` gefur :math:`B=0` en skilyrðið :math:`u(L) = 0` gefur

.. math::
    0 = \sin(\beta L)

en þessi jafna hefur lausn þegar :math:`\beta L` er heilt margfeldi af :math:`\pi` svo eigingildin eru

.. math::
    \lambda_n = \left(\frac{n\pi}{L}\right)^2, \quad n = 1,2,3,\ldots

og tilsvarandi eiginföll

.. math::
  u(x) = \sin(n\pi x/L).

Línulegar samantektir eiginfallanna

.. math::
    \sum_{n=1}^\infty C_n \sin(n\pi x/L)

eru Fourier-sínus-raðir á bilinu :math:`[0,L]`.

Afleiðuskilyrði í báðum endapunktum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lítum á jaðarskilyrðin

.. math::
    u'(0) = u'(L) = 0.

Með svipuðum hætti og áður fæst að eigingildin eru

.. math::
    \lambda_n = \left(\frac{n\pi}{L}\right)^2, \quad n=0,1,2,\ldots

(athugið að :math:`\lambda = 0` er núna með) og tilsvarandi eiginföll

.. math::
  u(x) = \cos(n\pi x/L).

Línulegar samantektir eiginfallanna

.. math::
    \sum_{n=0}^\infty C_n \cos(n\pi x/L)

eru Fourier-kósínus-raðir á bilinu :math:`[0,L]`.


Fallsjaðarskilyrði í öðrum endapunkti og afleiðuskilyrði í hinum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lítum á jaðarskilyrðin

.. math::
    u(0) = u'(L) = 0.

Með svipuðum hætti og áður fæst að eigingildin eru

.. math::
    \lambda_n = \left(\frac{(n-1/2)\pi}{L}\right)^2, \quad n=1,2,\ldots

og tilsvarandi eiginföll

.. math::
  u(x) = \sin((n-1/2)\pi x/L).

Í kennslubók má lesa eitt viðamikið sýnidæmi til viðbótar þar sem blönduð jaðarskilyrði eru í báðum endapunktum bilsins.

Aðskilnaður breytistærða
------------------------

Við lausn línulegra óhliðraðra hlutafleiðujafna þar sem breyturnar :math:`x_1,x_2,\ldots,x_k` koma við sögu getur verið gagnlegt að leita að lausnum sem eru á forminu :math:`X_1(x_1)X_2(x_2)\cdots X_k(x_k)`, þ.e.a.s. lausnir sem má þátta í föll sem hvert um sig er háð aðeins einni breytistærð. Línuleg samantekt lausna á slíku formi er einnig lausn en ekki endilega þáttanleg eins og gildir um sérhvern lið samantektarinnar. Í sumum tilfellum mynda lausnir á þessu formi grunn þannig að liða má föll upp í línulegar samantektir af grunnföllunum. Þannig má finna almenna lausn á hlutafleiðujöfnunni.

Þessi aðferð, að skoða lausnir sem þáttast, kallast *aðskilnaður breytistærða* og þegar henni er beitt fást venjulega eigingildisverkefni fyrir hvert fall í þáttuninni. Lítum á kunnuglegt dæmi.

Sveiflandi strengur - aftur
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lítum á einvíðan streng af lengd :math:`L` sem festur er í báða enda. Táknum frávik hans frá jafnvægi í punkti :math:`x` á tíma :math:`t` með :math:`u(x,t)`. Fallið :math:`u(x,t)` uppfyllir þá bylgjujöfnuna í einni rúmbreytu ásamt jaðarskilyrðunum

.. math::

  \dfrac{{\partial}^2u}{{\partial}t^2}-
   c^2\dfrac{{\partial}^2u}{{\partial}x^2}=0, \qquad u(0,t)=u(L,t)=0.

Leysum verkefnið með aðskilnaði breytistærða. Leitum að lausn á forminu :math:`u(x,t) = T(t)X(x)`. Stingum slíkri lausn inn í afleiðujöfnuna og fáum

.. math::
    T''(t) X(x) - c^2 T(t)X''(x) = 0

sem má umrita í

.. math::
    \frac{T''(t)}{c^2 T(t)} = \frac{X''(x)}{X(x)}.

Vinstri hliðin er aðeins háð :math:`t` og sú hægri aðeins háð :math:`x` og þar með hlýtur hvor um sig að vera jöfn fasta, köllum hann :math:`\lambda`. Fáum því afleiðujöfnu

.. math::
    -T''(t) = c^2 \lambda T

og eigingildisverkefni

.. math::
    -X''(x) = \lambda X \quad X(0) = X(L) = 0.

Eigingildisverkefnið hefur eigingildi :math:`\lambda_n = (n\pi/L)^2` og tilsvarandi eiginföll :math:`\sin(n\pi x/L)`, :math:`n=1,2,3,\ldots`. Afleiðujafnan fyrir :math:`T` hefur því lausn, fyrir :math:`\lambda = \lambda_n`, á forminu

.. math::
    A_n \cos(n\pi ct/L) + B_n \sin(n\pi c t/L).

Lausnin á hlutafleiðujöfnunni er því á forminu

.. math::
    T(t)X(x) = (A_n \cos(n\pi ct/L) + B_n \sin(n\pi c t/L))\sin(n\pi x/L).

Almenn lausn hlutafleiðujöfnunnar er línulega samantekt af svona liðum

.. math::
    u(x,t) = \sum_{n\geq 1} (A_n\cos(n\pi ct/L) + B_n \sin(n\pi c t/L))\sin(n\pi x/L)

og stuðlarnir :math:`A_n` og :math:`B_n` ákvarðast af upphafsskilyrðum

.. math::

  u(x,0)=\varphi(x), \qquad {\partial}_tu(x,0)={\psi}(x), \qquad x\in
   ]0,L[.


Annað dæmi
~~~~~~~~~~

.. admonition:: Dæmi
	:class: daemi

	Notum aðskilnað breytistærða til að leysa

	.. math:: a\partial_t^2u+b\partial_tu+cu-\Delta u=0, \quad x,y,z \in [0,1], t>0

	þar sem :math:`u` er fall af tíma :math:`t` og þremur
	rúmbreytum :math:`x,y` og :math:`z` og :math:`\Delta=\partial_x^2+\partial_y^2+\partial_z^ 2` er
	Laplace–virkinn miðað við rúmbreyturnar.  Gerum ráð fyrir jaðarskilyrðunum :math:`u(x,y,z,t) = 0` ef eitthvert hnitanna :math:`x,y,x` er jafnt 0 eða 1.

	Leitum að lausn á forminu
	:math:`u(x,y,z,t)=T(t)X(x)Y(y)Z(z)`. Stingum henni inn og umritum á formið

	.. math::

	  \dfrac{aT{{^{\prime\prime}}}(t)+bT(t){{^{\prime}}}+cT(t)}{T(t)}-
	   \dfrac{X{{^{\prime\prime}}}(x)}{X(x)}-\dfrac{Y{{^{\prime\prime}}}(y)}{Y(y)}=\dfrac{Z{{^{\prime\prime}}}(z)}{Z(z)}.

	Hægri hlið er háð :math:`z` en sú vinstri ekki. Ályktum að hægri hlið sé fasti og með sömu rökum að sérhver liður í jöfnunni sé fasti. Vegna jaðarskilyrða fáum við því þrjú eigingildisverkefni

	.. math::
	    \begin {align*}
	    -X''(x) &= \lambda X(x),\quad X(0) = X(1) = 0 \\
	    -Y''(y) &= \lambda Y(z),\quad Y(0) = Y(1) = 0 \\
	    -Z''(z) &= \lambda Z(z),\quad Z(0) = Z(1) = 0 \\
	    \end{align*}

	og afleiðujöfnu

	.. math::

	    aT{{^{\prime\prime}}}(t)+bT{{^{\prime}}}(t)+(c+\lambda+\mu+\nu)T=0,

	þar sem :math:`\lambda, \mu` og :math:`\nu` eru fastar. Við þekkjum lausnir eigingildisverkefnana og þáttanlega lausnin er á forminu

	.. math::
	    u_{\ell,m,n}(x) = T_{\ell, m, n}(t) \sin (\ell \pi x) \sin (m\pi y) \sin
	   (n\pi z), \qquad \ell, m, n=1,2,3,\dots,

	þar sem :math:`T_{\ell, m,n}` uppfyllir afleiðujöfnuna

	.. math:: aT{{^{\prime\prime}}}+ bT{{^{\prime}}}+\big(c+\pi^2(\ell^2+m^2+n^2)\big)T=0.


Virkjar af Sturm-Liouville-gerð
-------------------------------


Í þessari grein munum við skoða eigingildisverkefni virkja af tiltekinni gerð. Við byrjum á því að ræða virkjann og fjöllum því næst um jaðarskilyrðin sem skilgreina eigingildisverkefnið.

Við lítum á annars stigs afleiðuvirkja af eftirfarandi gerð

.. math:: Lu=P(x,D)u= a_2(x) u{{^{\prime\prime}}}+a_1(x)u{{^{\prime}}}+ a_0(x)u,

þar sem :math:`a_0,a_1,a_2` eru samfelld raungild föll á bili :math:`[a,b]` og :math:`a_2(x)\neq 0` fyrir öll
:math:`x\in [a,b]`. Í útreikningum hentar betur að setja virkjann fram á svokölluðu *Sturm-Liouville formi*

.. math::

  Lu ={{\dfrac {1}{\varrho}
   \bigg(-\dfrac d{dx}\bigg(p\dfrac {du}{dx}\bigg)+qu\bigg)}}.


.. admonition:: Athugasemd
	:class: athugasemd

	Sambandið milli framsetninganna tveggja er eftirfarandi. Veljum

	.. math::

	  p(x)=\exp\bigg(C +\int_a^x\dfrac{a_1({\xi})}{a_2({\xi})}\, d{\xi}\bigg),
	  \quad
	  q(x)=\dfrac{-a_0(x)p(x)}{a_2(x)}, \quad
	  {\varrho}(x)=\dfrac{-p(x)}{a_2(x)},

	þar sem :math:`C` er einhver ótiltekinn fasti.


Þar sem :math:`a_2(x)\neq 0` fyrir öll :math:`x\in [a,b]`, má gera ráð fyrir
að :math:`a_2(x)<0`. Þar með gildir

.. math::

  p\in C^1[a,b], \quad p(x)>0, \quad q,{\varrho}\in C[a,b], \quad q(x)\in {{\mathbb  R}},
   \quad {\varrho}(x)>0, \quad x\in [a,b].

Skilgreining
~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Við segjum að virki :math:`L` af Sturm–Liouville–gerð sé *reglulegur* ef
	föllin :math:`p`, :math:`q` og :math:`{\varrho}` uppfylla þessi skilyrði.


Skilgreining
~~~~~~~~~~~~
.. _ch-3.3.2:

.. admonition:: Skilgreining
	:class: skilgreining

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

	fyrir öll :math:`u,v\in C[a,b]`, :math:`\alpha,\beta\in {{\mathbb  C}}`. Fyrst :math:`{\varrho}>0`, þá er
	formið :math:`{{\langle \cdot,\cdot\rangle}}` innfeldi
	og tilheyrandi staðal táknum við með,

	.. math:: \|u\|= \sqrt{{{\langle u,u\rangle}}}.

.. admonition:: Athugasemd
	:class: athugasemd

	Við segjum að formið sé innfeldi á vigurrúmi samfelldra falla á :math:`[a,b]`, :math:`C[a,b]`, því það uppfyllir þær reiknireglur sem hið kunnuglega innfeldi endanlegra vigra uppfyllir. Við getum því unnið með það með sama hætti og gamla góða innfeldið.  Athugið einnig að þegar :math:`rho(x) = \frac{1}{b-a}` fæst sama innfeldi og sami staðall og við skilgreindum á :math:`L^2`. Almennt jákvætt fall :math:`rho` sem kemur fyrir í innfeldi af þessu tagi er oft kallað *vigt*.

Við munum nú skoða hvernig setja má fram jaðarskilyrði af tiltekinni gerð og athugum svo eigingildisverkefnin sem þau skilgreina ásamt virkjanum :math:`L` sem unnið er með. *Jaðargildisvirki* :math:`B` er vörpun sem úthlutar samfellt deildanlegu falli :math:`u\in C^1[a,b]` punkti :math:`Bu = (B_1 u , B_2)` þar sem

.. math::
   \begin{align*}
   B_1 u&=\alpha_{11}u(a)+\alpha_{12}u{{^{\prime}}}(a)
   +\beta_{11}u(b)+\beta_{12}u{{^{\prime}}}(b) \\
   B_1 u&=\alpha_{11}u(a)+\alpha_{12}u{{^{\prime}}}(a)
   +\beta_{11}u(b)+\beta_{12}u{{^{\prime}}}(b) \\
   \end{align*}

þar sem stuðlarnir :math:`\alpha_{jk}` og :math:`\beta_{jk}` eru
rauntölur. Við gerum ráð fyrir í hvorum virkjanna :math:`B_1` og :math:`B_2` sé að minnsta kosti einn stuðull frábrugðinn núlli.

Skilgreining
~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Rúmið :math:`C^2_B[a,b]` er skilgreint sem mengi allra
	:math:`u\in C^2[a,b]` sem uppfylla óhliðruðu jaðarskilyrðin
	:math:`Bu=0`.

Skilgreining
~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Við segjum að virkinn :math:`L` sé *samhverfur* á :math:`C^2_B[a,b]` eða
	*samhverfur með tilliti til jaðarskilyrðanna* :math:`Bu=0` ef

	.. math:: {{\langle Lu,v\rangle}} ={{\langle u,Lv\rangle}}, \qquad u,v\in C^2_B[a,b].


Formúla Greens
~~~~~~~~~~~~~~

Eftirfarandi formúla er kennd við Green

.. math::

  \begin{aligned}
   {{\langle Lu,v\rangle}} -{{\langle u,Lv\rangle}}    &=p(b)\left|
   \begin{matrix} u(b) & u{{^{\prime}}}(b) \\ \bar v(b) &\bar v{{^{\prime}}}(b)
   \end{matrix}\right| -
   p(a)\left|
   \begin{matrix} u(a) & u{{^{\prime}}}(a) \\ \bar v(a) &\bar v{{^{\prime}}}(a)
   \end{matrix}\right|.\nonumber\end{aligned}


Af formúlu Greens sést að virki er samhverfur þá og því aðeins

.. math::
    p(b)\left|
   \begin{matrix} u(b) & u{{^{\prime}}}(b) \\ \bar v(b) &\bar v{{^{\prime}}}(b)
   \end{matrix}\right| =
   p(a)\left|
   \begin{matrix} u(a) & u{{^{\prime}}}(a) \\ \bar v(a) &\bar v{{^{\prime}}}(a)
   \end{matrix}\right|

fyrir öll :math:`u,v\in C^2_B[a,b]`.


Við höfum einkum áhuga á eftirfarandi tveimur tilfellum sem hægt er að sannfæra sig um að eru samhverf með því að nota skilyrðið úr formúlu Greens.

Setning og skilgreining
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	\(i) Ef jaðarskilyrðin eru *aðskilin*, þ.e.a.s.

	.. math::

	  B_1u=\alpha_1u(a)-\beta_1u{{^{\prime}}}(a), \qquad
	   B_2u=\alpha_2u(b)+\beta_2u{{^{\prime}}}(b),

	þar sem :math:`\alpha_1, \beta_1, \alpha_2, \beta_2\in {{\mathbb  R}}`,
	:math:`(\alpha_1,\beta_1)\neq (0,0)` og :math:`(\alpha_2,\beta_2)\neq (0,0)`, þá er :math:`L` samhverfur á :math:`C^2_B[a,b]`.

	\(ii) Ef :math:`p(a)=p(b)` og jaðarskilyrðin eru *lotubundin*, þ.e.a.s.

	.. math:: B_1u=u(a)-u(b), \qquad B_2u=u{{^{\prime}}}(a)-u{{^{\prime}}}(b),

	þá er :math:`L` samhverfur á :math:`C^2_B[a,b]`.

Nú erum við reiðubúin að fjalla um eigingildisverkefni sem svara til virkja af Sturm-Liouville gerð með jaðarskilyrðum af þessu tagi.


Eigingildisverkefni af Sturm–Liouville–gerð
-------------------------------------------

Lítum á eigingildisverkefnið

.. math:: Lu= {\lambda} u , \qquad Bu=0,

þar sem :math:`L` er virki af Sturm–Liouville–gerð og
:math:`B` er almennur jaðargildisvirki.

Línulega rúmið sem spannað er af öllum eiginföllum með tilliti til eigingildisins :math:`{\lambda}`
köllum við :hover:`eiginrúmið, eiginrúm` með tilliti til eigingildisins
:math:`{\lambda}` og við táknum það með :math:`E_{\lambda}`.

Skilgreining
~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Ef :math:`L` er reglulegur virki af Sturm–Liouville–gerð, þá segjum við
	að eigingildisverkefnið sé *reglulegt*.

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

	Gerum ráð fyrir að virkinn :math:`L` af Sturm–Liouville–gerð sé
	samhverfur á :math:`C^2_B[a,b]`. Þá eru öll eigingildin rauntölur og
	eiginföllin sem svara til ólíkra eigingilda eru innbyrðis hornrétt. Að auki má velja grunn í eiginrúminu :math:`E_\lambda` sem samanstendur af raungildum föllum.

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

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

Eftirfarandi setning er meginniðurstaða þessarar umfjöllunar. Hún alhæfir það sem við höfum áður fjallað um með Fourier-röðum.

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

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

Skilgreining
~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Fyrir sérhvert heildanlegt fall :math:`f` á :math:`[a,b]`, þá
	skilgreinum við *Fourier–stuðul fallsins* :math:`f`  *með tilliti til
	eiginfallsins* :math:`u_n` með

	.. math:: c_n(f)= {{\langle f,u_n\rangle}} =\int_a^b f(x) u_n(x){\varrho}(x)\, dx

	og *eiginfallaröðina af* :math:`f`  *með tilliti til eiginfallanna*
	:math:`(u_n)_{n=0}^{\infty}` með

	.. math:: \sum\limits_{n=0}^{\infty} c_n(f)u_n(x).

.. admonition:: Athugasemd
	:class: athugasemd

	Við höfum einnig andhverfuformúlu fyrir eiginfallaraðir af föllum sem eru samfellt deildanleg á köflum sem er samhljóða andhverfuformúlu Fouriers.


Green-föll fyrir jaðargildisverkefni
------------------------------------



Lítum á línulegan jaðargildisvirkja  :math:`B`
á :math:`[a,b]` á forminu

.. math::

  \begin{cases}
   B:C^{m-1}[a,b]\to {{\mathbb  C}}^m, \qquad Bu=(B_1u,\dots,B_mu),\\
   B_ju=\sum\limits_{l=1}^m \alpha_{jl}u^{(l-1)}(a)+
   \beta_{jl}u^{(l-1)}(b).
   \end{cases}

Gerum ráð fyrir því að fyrir sérhvert :math:`j` sé að minnsta kosti
ein talnanna :math:`\alpha_{jl}`, :math:`\beta_{jl}`,
:math:`l=1,\dots,m` frábrugðin :math:`0`. Skilgreinum :math:`C^m_B[a,b]`
sem rúm allra :math:`u\in C^m[a,b]` sem uppfylla óhliðruðu
jaðarskilyrðin :math:`Bu=0`.

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

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



Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

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


Eiginfallaliðun og Green–föll
-----------------------------

Reikniaðferð
~~~~~~~~~~~~

Eftirfarandi losaralegu reikningar gera okkur kleift að finna Green-fall fyrir jaðargildisverkefnið

.. math:: Lu=f(x), \qquad x\in ]a,b[, \qquad Bu=0,

þar sem

- :math:`L` er virki af Sturm–Liouville–gerð
- :math:`L` er reglulegur og samhverfur með tilliti til jaðarskilyrðanna :math:`Bu=0`.


Nú fæst líkt og fyrir Fourier-raðir að

.. math:: u(x)=\sum\limits_{\substack{n=0 \\ \lambda_n\neq 0}}^{\infty} \dfrac {c_n(f)}{\lambda_n}u_n(x)

er lausn ef röðin er nógu hratt samleitin þannig að víxla megi á diffrun og óendanlegri röð.


Ef :math:`{\lambda}=0` er eigingildi, þá gerum við ráð fyrir að :math:`f` sé hornrétt á eiginrúmið :math:`E_0`.


Stingum inn formúlunni fyrir stuðlana :math:`c_n(f)` og fáum

.. math::

  \begin{aligned}
   u(x)&= \sum\limits_{n=0}^{\infty} \dfrac 1{\lambda_n}
   \bigg(\int_a^b f({\xi})u_n({\xi}){\varrho}({\xi})\, d{\xi}\bigg)
   u_n(x)\\
   &=\int_a^b{\varrho}({\xi})\bigg(\sum\limits_{n=0}^{\infty} \dfrac{u_n(x)u_n({\xi})}
   {\lambda_n}\bigg) f({\xi})\, d{\xi}.\nonumber\end{aligned}

Green–fallið fyrir jaðargildisverkefnið er ótvírætt ákvarðað, svo

.. math::

  G_B(x,{\xi})={\varrho}({\xi})\sum\limits_{n=0}^{\infty}
   \dfrac{u_n(x)u_n({\xi})}{\lambda_n}.



Úrlausn hlutafleiðujafa með eiginfallaröðum
-------------------------------------------

Við höldum nú áfram að fjalla um hvernig eigingildisverkefni koma við sögu í úrlausn hlutafleiðujafna. Við munum nálgast umfjöllunina með því að taka dæmi, sum þeirra kunnugleg en önnur ný. Það koma aðallega við sögu tvennskonar lausnaraðferðir

- Sett er fram lausnartilgáta á hlutafleiðujöfnu með hliðarskilyrðum í formi **eiginfallaraðar með tilliti til einnar breytistærðarinnar** þar sem stuðlarnir eru háðir hinni breytistærðinni.

    - Eiginfallaröðin er valin þannig að hún innihaldi **eiginföll** þess hluta virkjans í verkefninu sem svarar til breytunnar sem liðað er með tilliti til og þannig að **eiginföllin uppfylli jaðarskilyrðin**.
    - Tilgátunni er stungið inn í hlutafleiðujöfnuna og gert ráð fyrir að víxla megi á óendanlegu röðinni og þeim afleiðum sem koma við sögu.
    - Þá fæst (hlut)afleiðujafna fyrir stuðlana ásamt hliðarskilyrðum sem mögulega má leysa.

- **Aðskilnaði breytistærða er beitt** og þá fást eigingildisverkefni sem þarf að leysa og lausnir þeirra gefa fjölskyldu af ólíkum aðgreinanlegum lausnum, eina fyrir hvert eigingildi.  Lausn upphaflega verkefnisins má rita sem línulega samantekt af slíkum aðgreinanlegum lausnum.

Byrjum á að líta á dæmi um aðferðina sem líst er í fyrri punktinum.

Margar af mikilvægustu hlutafleiðujöfnum sem fengist er við til að mynda í eðlisfræði innihalda Laplace-virkjann og við byrjum á stuttri umfjöllun um Laplace-jöfnuna. Þegar Laplace-jafnan er leyst á gefnu mengi með fallsjaðarskilyrðum kallast verkefnið **Dirichlet-verkefnið**.

Dirichlet-verkefnið á rétthyrningi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Lítum á verkefnið

.. math::

  \begin{cases} \Delta u=0, &0<x<L, \ 0<y<M,\\
   u(x,0)=\varphi_1(x), \ u(x,M)=\varphi_2(x), &0<x<L,\\
   u(0,y)=\psi_1(y), \ u(L,y)=\psi_2(y), &0<y<M.
   \end{cases}

.. figure:: ./Drawings/dirichlet1.png
    :align: center
    :width: 65%
    :alt: Dirichlet verkefnið á rétthyrningi

    Mynd: Dirichlet verkefnið á rétthyrningi.

Skiptum því í fjóra hluta

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



Ef :math:`u_1`, :math:`u_2`, :math:`u_3` og :math:`u_4` eru lausnir þá er
:math:`u(x,y)=u_1(x,y)+u_2(x,y)+u_3(x,y)+u_4(x,y)` lausn upphaflega verkefnis.

Nóg er að leysa verkefnið fyrir :math:`u_1` því lausnina á hinum má skrifa niður út frá þeirri lausn.

- Vegna jaðarskilyrða :math:`u_1(0,y)=u_1(L,y)=0` liðum við :math:`u_1(x,y)` í Fourier-sínusröð í breytistærðinni :math:`x`, með stuðla sem eru háðir :math:`y`

.. math::
   u_1(x,y)=\sum\limits_{n=1}^\infty u_{1n}(y)\sin\big(n\pi x/L\big), \\


- Ákvörðum stuðlana :math:`u_{1n}(y)`, með því að víxla á óendanlegu röðinni og :math:`\Delta` og stingum svo inn jaðarskilyrðunum.


- Fáum þá að :math:`u_{1n}` er lausn á jaðargildisverkefninu

.. math::

  \begin{cases}
   u_{1n}{{^{\prime\prime}}}(y)-(n\pi/L)^2 u_{1n}(y)=0, &0<y<M,\\
   u_{1n}(0)=b_n(\varphi_1), \quad u_{1n}(M)=0.
   \end{cases}

þar sem :math:`b_n(\varphi_1)` er :math:`n`-ti Fourier-sínus-stuðull :math:`\varphi_1`. Lausn þessa verkefnis er

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

Fáum svo :math:`u_2` með því að skipta á
:math:`y` og :math:`M-y` og :math:`u_3` og :math:`u_4` með því að skipta á hlutverkum :math:`x` og
:math:`y`. Lokaniðurstaðn er því

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


.. admonition:: Athugasemd
	:class: athugasemd

	Það reyndist mikilvægt í þessari aðferð að föllin :math:`\sin(n{\pi}x/L)` uppfylla gefnu jaðarskilyrðin og eru eiginföll :math:`\partial_x^2`.

Dirichlet-verkefnið á skífu
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lítum á sama verkefni á hringskífu

.. math::

  \begin{cases} \Delta u=
   \dfrac{\partial^2u}{\partial x^2}+
   \dfrac{\partial^2u}{\partial y^2}=0, &x^2+y^2<a^2,\\
   u(x,y)=\varphi(x,y), &x^2+y^2=a^2.
   \end{cases}



Þar sem svæðið er skífa er eðlilegt að umrita verkefnið með því að nota **pólhnit**.
Laplace-virkjann er í pólhnitum

.. math::

  \Delta = \dfrac 1r\dfrac{\partial}{\partial r}
   \bigg(r\dfrac{\partial }{\partial r}\bigg)
   +\dfrac 1{r^2}\dfrac{\partial^2 }{\partial\theta^2},

og því má rita verkefnið á forminu

.. math::

  \begin{cases}
   \dfrac 1r\dfrac{\partial}{\partial r}
   \bigg(r\dfrac{\partial v}{\partial r}\bigg)
   +\dfrac 1{r^2}\dfrac{\partial^2 v}{\partial\theta^2}=0, &r<a,
   \ {\theta}\in {{\mathbb  R}},\\
   v(a,\theta)={\psi}(\theta), &{\theta}\in {{\mathbb  R}}.
   \end{cases}

með :math:`v(r,\theta) = u(x(r,\theta),y(r,\theta))`.


.. figure:: ./Drawings/dirichlet2.png
    :align: center
    :width: 75%
    :alt: Dirichlet verkefnið á skífu

    Mynd: Dirichlet verkefnið á skífu.





- Þar sem :math:`v` og :math:`{\psi}` eru :math:`2\pi`-lotubundin föll prófum við lausnartilgáta sem er Fourier-röðum með tilliti til :math:`{\theta}` með stuðlum sem geta verið háðir :math:`r`

.. math::

  v(r,\theta)=\sum\limits_{n=-\infty}^{+\infty}
   v_n(r)e^{in\theta}.

og liðum :math:`\psi` sömuleiðis í Fourier-röð

 .. math::

   {\psi}(\theta)=\sum\limits_{n=-\infty}^{+\infty}
   {\psi}_n e^{in\theta}.

- Ákvörðum stuðlana :math:`v_{n}(r)`, með því að víxla á óendanlegu röðinni fyrir :math:`v` og :math:`\Delta` og stingum svo inn jaðarskilyrðunum.

- Fáum þá að :math:`v_{n}` er lausn á jaðargildisverkefninu

.. math::

  \begin{cases}
   r\dfrac d{dr}\bigg(r\dfrac{dv_n}{dr}\bigg)-n^2v_n=0, &r<a,\\
   v_n(a)={\psi}_n, \quad v_n(r) \text{ takmarkað ef } r\to 0.
   \end{cases}

Þetta er Euler-jafna og því stingum við inn lausnartilgátu :math:`v_n(r)=r^\alpha`

.. math::

  r\dfrac d{dr}\bigg( r\dfrac d{dr}r^\alpha\bigg)=\alpha^2r^\alpha=
   n^2r^\alpha.

og sjáum að :math:`\alpha=\pm n`. Almenn lausn
afleiðujöfnunar er því

.. math::

  v_n(r)=
   \begin{cases}
   A_nr^{|n|}+B_nr^{-|n|}, &n\neq 0\\
   A_0+B_0\ln r, &n=0.
   \end{cases}

Til þess að lausnin geti verið takmörkuð í :math:`r=0`, þá útilokum við liðina með neikvæðum veldisvísi og logrann. Skilyrðið
:math:`v_n(a)={\psi}_n` gefur að :math:`A_n={\psi}_n/a^{|n|}`. Þar með
er lausnin fundin

.. math::

  v(r,\theta)=\sum\limits_{n=-\infty}^{+\infty}
   \psi_n \bigg(\dfrac r a\bigg)^{|n|}e^{in\theta}.



.. admonition:: Athugasemd
	:class: athugasemd

	Það reyndist mikilvægt í þessari aðferð að föllin :math:`e^{in\theta}` eru eiginföll :math:`\partial_\theta^2`.



Varmaleiðnijafnan með tímaháðum jaðarskilyrðum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reiknum hitastig í jarðvegi sem fall af tíma :math:`t` og dýpi :math:`x`.

Hitastigið á yfirborði er gefið sem fall af tíma :math:`f(t)` og gert ráð fyrir að það sé :math:`T`-lotubundið fall (t.d.vegna árstíðasveiflna). Ritum

.. math::

  f(t)=\sum\limits_{n=-\infty}^{+\infty}
   c_n(f)e^{in\omega t}, \qquad  \omega=2\pi/T.

Setjum upp jaðargildisverkefnið

.. math::

  \begin{cases}
   \dfrac{\partial u}{\partial t}-\kappa
   \dfrac{\partial^2 u}{\partial x^2}=0, &x>0, \ t\in {{\mathbb  R}},\\
   u(0,t)=f(t), &t\in {{\mathbb  R}},\\
   u(x,t) \text{ takmarkað ef } & x\to +\infty.
   \end{cases}

- Prófum lausn :math:`u(x,t)` sem er :math:`T`-lotubundið fall af :math:`t` fyrir fast :math:`x`. Liðum það í :math:`u` í Fourier-röð miðað við :math:`t` með stuðla sem geta verið háðir :math:`x`

.. math::

  u(x,t)=\sum\limits_{n=-\infty}^{+\infty}
   u_n(x)e^{in\omega t}.


- Ákvörðum stuðlana :math:`u_{n}(x)`, með því að víxla á óendanlegu röðinni fyrir :math:`v` og virkjanum :math:`\dfrac{\partial}{\partial t}-\kappa\dfrac{\partial^2}{\partial x^2}` og stingum svo inn jaðarskilyrðunum.

- Fáum þá að :math:`u_{n}` er lausn á

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



Áfram um eigingildisverkefni - aðskilnaður breytistærða
-------------------------------------------------------
Í þessum síðustu greinum kaflans munum við fara í gegnum fleiri reikniaðferðir sem beita má við lausn hlutafleiðujafna. Við reynum að koma almennum hugmyndum til skila en styðjumst þó að mestu við ákveðin dæmi til að skýra hugmyndirnar.


Dirichlet-verkefnið á rétthyrningi - aftur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Skoðum aftur Dirchlet-verkefnið á rétthyrningi. Lítum á jöfnu 2 af jöfnunum fjórum sem komu áður fyrir

.. math::

  \begin{cases} \Delta u={\partial}_x^2u+{\partial}_y^2u=0, &0<x<L, \ 0<y<M,\\
   u(0,y)=u(L,y)=0, &0<y<M,\\
   u(x,0)=0, \ u(x,M)=\varphi(x), &0<x<L,\\
   \end{cases}

þar sem :math:`\varphi` er gefið fall á :math:`[0,L]`.

- Leitum fyrst að öllum lausnum af gerðinni :math:`v(x,y)=X(x)Y(y)` sem uppfylla jöfnuna og óhliðruðu jaðarskilyrðin.

- Stingum næst :math:`v` inn í hlutafleiðu jöfnuna og fáum

.. math:: X{{^{\prime\prime}}}(x)Y(y)+X(x)Y{{^{\prime\prime}}}(y)=0.

- Deilum í gegnum jöfnuna með :math:`X(x)Y(y)` og fáum þá

.. math:: -\dfrac{X{{^{\prime\prime}}}(x)}{X(x)}=\dfrac{Y{{^{\prime\prime}}}(y)}{Y(y)}.

Fallið vinstra megin er einungis háð :math:`x`, en fallið hægra megin er einungis háð :math:`y`. Því hlýtur hvor hlið að vera föst. Við
höfum því

.. math:: -X{{^{\prime\prime}}}(x)=\lambda X(x) \qquad \text{ og } \qquad Y{{^{\prime\prime}}}(y)=\lambda Y(y),

þar sem :math:`\lambda` er fasti.

- Lítum nú á jaðarskilyrðin

.. math:: X(0)Y(y)=X(L)Y(y)=0, \qquad X(x)Y(0)=0,

og sjáum að :math:`X` er lausn á eigingildisverkefninu

.. math:: -X{{^{\prime\prime}}}=\lambda X, \qquad X(0)=X(L)=0.

Þetta höfum við leyst áður og fengum eigingildin
:math:`\lambda=\lambda_n=\big(n\pi/L\big)^2`, :math:`n=1,2,3,\dots`, og
tilsvarandi eiginföll

.. math:: X_n(x)=C_n \sin\big(n\pi x/L\big), \qquad n=1,2,3,\dots.

Leysum næst

.. math:: Y{{^{\prime\prime}}}(y)=\big(n\pi/L\big)^2 Y(y), \qquad Y(0)=0.

Þessi jafna hefur greinilega lausnina

.. math:: Y_n(y)=D_n \sinh\big(n\pi y/L\big), \qquad n=1,2,3,\dots.

Nú eru allar lausnir á Laplace-jöfnunni af gerðinni
:math:`v(x,y)=X(x)Y(y)` með óhliðruðu jaðarskilyrðunum gefnar með formúlunni

.. math::

  v(x,y)=C_nD_n \sin\big(n\pi x/L\big)\sinh\big(n\pi y/L\big), \qquad
   n=1,2,3,\dots.

Getum valið :math:`D_n=1`. Tökum óendanlega línulega samatekt af þessum lausnum

.. math::

  u(x,y)=\sum\limits_{n=1}^\infty
   C_n\sin\big(n\pi x/L\big)\sinh\big(n\pi y/L\big).

Síðasta jaðarskilyrðið,
:math:`u(x,M)=\varphi(x)` er uppfyllt ef

.. math::

  \begin{aligned}
   u(x,M)&= \sum\limits_{n=1}^\infty
   C_n \sin\big(n\pi x/L\big)\sinh\big(n\pi M/L\big)\\
   &= \sum\limits_{n=1}^\infty
   b_n(\varphi) \sin\big(n\pi x/L\big)=\varphi(x),\end{aligned}

þar sem :math:`b_n(\varphi)` er Fourier-sínusstuðull fallsins
:math:`\varphi`.

Samanburður á stuðlum gefur

.. math::

  u(x,y)=\sum_{n=1}^\infty
   b_n(\varphi)\dfrac{\sinh\big(n\pi y/L\big)}{\sinh\big(n\pi
   M/L\big)} \sin\big(n\pi x/L\big).



Dirichlet-verkefnið á skífu - aftur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Leysum aftur Dirichlet-verkefnið á hringskífu með aðskilnaði breytistærða,

.. math::

  \begin{cases}
   \dfrac 1r\dfrac{\partial}{\partial r}
   \bigg(r\dfrac{\partial v}{\partial r}\bigg)
   +\dfrac 1{r^2}\dfrac{\partial^2 v}{\partial\theta^2}=0, &r<a,
   \ {\theta}\in {{\mathbb  R}},\\
   v(a,\theta)={\psi}(\theta), &{\theta}\in {{\mathbb  R}},
   \end{cases}

þar sem föllin :math:`v` og :math:`\psi` eru :math:`2\pi`-lotubundin í
:math:`\theta`.

- Leitum fyrst að öllum lausnum af gerðinni :math:`w(r,\theta)=R(r)\Theta(\theta)`.

- Stingum tilgátunni inn í hlutafleiðujöfnuna og fáum

.. math::

  r \big(r R{{^{\prime}}}(r)\big){{^{\prime}}}\Theta(\theta)
   +R(r)\Theta{{^{\prime\prime}}}(\theta)=0.

- Deilum í gegn með :math:`R(r)\Theta(\theta)` og fáum

.. math::

  r\big(r R{{^{\prime}}}(r)\big){{^{\prime}}}/R(r)
   =-\Theta {{^{\prime\prime}}}(\theta)/\Theta (\theta).

Vinstri hliðin er eingöngu háð :math:`r` en hægri hliðin er eingöngu háð :math:`\theta`. Þar með eru báðar hliðar jafnar fasta, segjum :math:`\lambda`. Fáum þá jöfnurnar

.. math::

  -\Theta{{^{\prime\prime}}}(\theta)=\lambda\Theta(\theta),
   \qquad
   r\dfrac d{dr}\bigg(r\dfrac {d R}{dr}(r)\bigg)=\lambda {R(r)}.

- Almenn lausn á fyrri jöfnunni er

.. math::

  \Theta(\theta)=\begin{cases}
   Ae^{i\beta\theta}+Be^{-i\beta\theta},  &\lambda=\beta^2\neq 0,\\
   A_0+B_0\theta, &\lambda=0.
   \end{cases}

Þar sem fallið :math:`\Theta` er :math:`2\pi`-lotubundið fæst
að einu gildin sem :math:`\lambda` getur tekið eru
:math:`\lambda=\lambda_n=n^2`, :math:`n=0,1,2,\dots`, og :math:`B_0=0`.
Þar með er

.. math::

  \Theta(\theta)=\begin{cases}
   A_ne^{in\theta}+B_ne^{-in\theta},  &n=1,2,3,\dots,\\
   A_0, &\lambda=0.
   \end{cases}

- Lítum næst á afleiðujöfnuna fyrir :math:`R(r)` með :math:`\lambda=n^2`. Þetta er Euler-jafna. Með því að leita að lausn af gerðinni :math:`R(r)=r^\alpha` sjáum við að :math:`\alpha=\pm n`. Almenn lausn á seinni afleiðujöfnunni fyrir :math:`R(r)` með :math:`\lambda=n^2` er því

.. math::

  R(r)=\begin{cases}
   C_nr^n+D_nr^{-n}, &n=1,2,3,\dots,\\
   C_0+D_0\ln r, &n=0.
   \end{cases}

Þar sem lausnin verður að gilda í :math:`r=0` þarf :math:`D_n=0`, :math:`n=0,1,2,\dots`. Þar með er

.. math::

  R(r)=\begin{cases}
   C_nr^n, &n=1,2,3,\dots,\\
   C_0, &n=0.
   \end{cases}

- Allar lausnir á verkefninu af gerðinni :math:`w(r,\theta)=R(r)\Theta(\theta)`  eru þá

.. math::

  w(r,\theta)=
   C_nr^n\big(A_ne^{in\theta}+B_ne^{-in\theta}\big), \qquad n=0,1,2,\dots,

þar sem :math:`A_n`, :math:`B_n` og :math:`C_n` eru fastar. Veljum :math:`C_n=1`.

Almenn lausn hlutafleiðujöfnunnar er línuleg samantekt þessara lausna

.. math:: v(r,\theta)=\sum\limits_{-\infty}^{+\infty}A_nr^{|n|}e^{in\theta},

þar sem við höfum sett :math:`A_n=B_{-n}` ef :math:`n<0`.

- Notum nú jaðarskilyrðið í :math:`r=a`,

.. math::

  v(a,\theta)=\sum\limits_{-\infty}^{+\infty}A_na^{|n|}e^{in\theta}
   =\sum\limits_{-\infty}^{+\infty}c_n(\psi)a^{|n|}e^{in\theta}=\psi(\theta).

Með samanburði á stuðlum fæst að :math:`A_n=c_n(\psi)/a^{|n|}`
og þar með fæst

.. math::

  v(r,\theta)=\sum\limits_{-\infty}^{+\infty}
   c_n(\psi)\bigg(\dfrac ra\bigg)^{|n|} e^{in\theta}.



Tvöfaldar Fourier-raðir
-----------------------

Látum :math:`{\varphi}:\overline D\to {{\mathbb  C}}` vera samfellt
deildanlegt á :math:`D=\{(x,y); 0<x<L, 0<y<M\}` og samfellt á lokuninni
:math:`\overline  D`. Ef :math:`{\varphi}` er jafnt :math:`0` á jaðrinum
:math:`{\partial}D`, þá getum við liðað :math:`{\varphi}` í
Fourier-sínusröð með tilliti til :math:`y`

.. math::

  {\varphi}(x,y)= \sum\limits_{m=1}^{\infty}
   {\varphi}_m(x)\sin\big(m{\pi}y/M\big).


Fallið :math:`{\varphi}_m` er samfellt deildanlegt og tekur gildið
:math:`0` í :math:`x=0` og :math:`x=L`, svo við getum einnig liðað það í
Fourier-sínusröð

.. math::
    \varphi_m(x) = \sum_{n=1}^\infty b_{n,m} \sin(n\pi x/L).

Höfum því framsetningu á :math:`\varphi` með *tvöfaldri Fourier-röð*

.. math::

  {\varphi}(x,y)=\sum\limits_{n=1}^{{\infty}}
   \sum\limits_{m=1}^{{\infty}} b_{n,m}
   \sin\big(n{\pi}x/L\big)\sin\big(m{\pi}y/M\big).



Dæmi - Rétthyrnd tromma
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
	:class: daemi

	Himna er strekkt á rétthyrndan ramma með hliðarlengdir :math:`L` og :math:`M` og sveiflast þar. Lóðrétt færsla hennar frá jafnvægi
	í punkti :math:`(x,y)` á tíma :math:`t` er táknuð með :math:`u(x,y,t)` og uppfyllir tvívíðu bylgjujöfnuna. Ef staða og hraði
	trommunnar eru gefin við tímann :math:`t=0`, þá er :math:`u` lausn
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

	Lítum á lausnartilgátu á formi tvöfaldrar Fourier-raðar

	.. math::

	  u(x,y,t)=\sum\limits_{n=1}^{{\infty}}
	   \sum\limits_{m=1}^{{\infty}} u_{n,m}(t)
	   \sin\big(n{\pi}x/L\big)\sin\big(m{\pi}y/M\big).

	Stingum henni inni í hlutafleiðujöfnuna og víxlum á hlutafleiðuvirkjanum og óendanlegu röðinni. Fáum þá jöfnuna

	.. math:: u_{n,m}{{^{\prime\prime}}}(t)+c^2{\pi}^2(n^2/L^2+m^2/M^2)u_{n,m}=0,

	sem hefur almenna lausn

	.. math::

	  u_{n,m}(t)=A_{n,m}\cos\big(\sqrt{n^2/L^2+m^2/M^2}\, {\pi}ct\big)
	   +B_{n,m}\sin\big(\sqrt{n^2/L^2+m^2/M^2}\, {\pi}ct\big).

	Út frá upphafsskilyrðunum fæst

	.. math::

	  A_{n,m}=b_{n,m}({\varphi}) \qquad \text{ og } \qquad
	   B_{n,m}=\dfrac{b_{n,m}({\psi})}{\sqrt{n^2/L^2+m^2/M^2}\, {\pi}c}.

	Mögulegar tíðnir í sveiflunni eru því

	.. math:: \{\tfrac \pi 2\sqrt{n^2/L^2+m^2/M^2}\, c; n,m=1,2,3,\dots\}.

	Lægsta tíðnin :math:`\frac \pi 2\sqrt{1/L^2+1/M^2}\, c` nefnist
	*grunntíðni* og hinar tíðnirnar nefnast *yfirtíðnir*. Yfirtíðnirnar eru ekki heiltölumargfeldi af grunntíðninni eins og gildir fyrir sveiflandi streng.  Þetta er skýringin á því hvers vegna trommur gefa ekki frá sér hreinan tón eins og strengir.


Almennt um eiginfallaraðir
--------------------------

Við ljúkum umfjöllun þessa kafla á að taka dæmi sem undirstrikar það að lausnaraðferðirnar sem við höfum verið að beita þar sem eiginfallaraðir koma við sögu eru almennar og ekki bundnar við notkun hefbundinna Fourier-raða. Með þessa hugmynd að leiðarljósi er í sumum tilfellum hægt að komast langt í að skrifa niður lausn verkefnis án þess að þekkja eiginföllin og eigingildin.


Dæmi - Alhæft varmaleiðniverkefni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
	:class: daemi

	Látum :math:`P(x,D_x)` vera afleiðuvirkja af Sturm-Liouville gerð. Látum :math:`u = u(x,t)` vera fall af tveimur breytistærðum og :math:`B_1` og :math:`B_2` samhverfa jaðargildisvirkja. Skoðum verkefnið

	.. math::

	  \begin{cases}
	   \dfrac{\partial u}{\partial t}+P(x,\partial_x)u=f(x,t),
	   &x\in ]a,b[, \ t>0,\\
	   u(x,0)=\varphi(x), & x\in ]a,b[,\\
	   B_1u(\cdot,t)=B_2u(\cdot,t)=0, &t>0.
	   \end{cases}

	:math:`B_ju(\cdot,t)` táknar að :math:`B_j` verki með tilliti til fyrri breytistærðarinnar :math:`x`.

	Gerum eftirfarandi lausnartilgátu

	.. math:: u(x,t)=\sum\limits_{n=0}^{\infty} c_n(t)u_n(x),

	þar sem :math:`u_n(x)` eru eiginföll virkjans :math:`P` (ásamt jaðarskilyrðum) með tilsvarandi eigingildi eru :math:`\lambda_n` og :math:`c_n(t)` eru Fourier-stuðlar :math:`u(x,t)` með tilliti til eiginfallanna.

	Liðum föllin :math:`f` og :math:`\varphi` einnig í eiginfallaraðir

	.. math::

	  f(x,t)=\sum\limits_{n=0}^{\infty} f_n(t)u_n(x), \qquad
	   \varphi(x)=\sum\limits_{n=0}^{\infty} \varphi_nu_n(x).

	Stignum lausnatilgátunni inn í hlutafleiðujöfnuna og víxlum á hlutafleiðuvirkjanum og óendanlegu röðinni. Þá fæst

	.. math::

	  \begin{aligned}
	   \dfrac{{\partial}u}{{\partial} t}(x,t) +P(x,{\partial}_x)u(x,t)&= \sum\limits_{n=0}^{\infty}\bigg(
	   c_n{{^{\prime}}}(t)+{\lambda}_nc_n(t)\bigg)u_n(x)\nonumber\\
	   &=\sum\limits_{n=0}^{\infty} f_n(t)u_n(x)=f(x,t),\nonumber\\
	   \end{aligned}

	ásamt upphafsskilyrðinu

	.. math::

	    \begin{aligned}
	    u(x,0)&=\sum\limits_{n=0}^{\infty} c_n(0)u_n(x)
	   =\sum\limits_{n=0}^{\infty} {\varphi}_nu_n(x)={\varphi}(x).\nonumber\end{aligned}

	Með því að bera saman stuðlana í jöfnunum fæst upphafsgildisverkefni fyrir :math:`c_n(t)`,

	.. math::

	  \begin{cases}
	   c_n{{^{\prime}}}(t)+{\lambda}_nc_n(t)=f_n(t),\\
	   c_n(0)={\varphi}_n.
	   \end{cases}

	Þetta er fyrsta stigs jafna með fastastuðla, svo

	.. math::

	  c_n(t)={\varphi}_ne^{-{\lambda}_n t}+
	   e^{-{\lambda}_n t}\int_0^te^{{\lambda}_n {\tau}}f_n({\tau})\, d{\tau}.

	Athugið að við gátum skrifað niður lausn án þess að þekkja eiginföllin :math:`u_n` og tilsvarandi eigingildi :math:`\lambda_n`.
