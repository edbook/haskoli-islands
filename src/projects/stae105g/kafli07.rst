Aðferðir í heildun
===================

.. admonition:: Nauðsynleg undirstaða
	:class: athugasemd

	- Föll

	- Markgildi

	- Afleiður

	- Heildi 

------

.. epigraph::

  *May it be a light to you in dark places, when all other lights go out.*

  \– Galadriel, The Two Towers

------

Hlutheildun
------------

Í fyrri köflum höfum við lært að heilda með því að nota innsetningu. En innsetning
ræður aðeins við lítinn hluta mögulegra heilda. Innsetning með :math:`u=x^2` gerir okkur kleift
að reikna

.. math:: \int x \sin(x^2) dx

en getur okkur engar bjargir veitt þegar kemur að heildinu

.. math:: \int x \sin(x) dx.

Til þess þarf að grípa til annarra aðferða. Þar sem innsetningu þrýtur má oft
líta til hlutheildunar.

Setning: Hlutheildun
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Látum :math:`f(x)` og :math:`g(x)` vera föll sem samfelldar afleiður. Þá
	gildir að

	.. math:: \int f'(x)g(x) dx = f(x)g(x) - \int f(x)g'(x) dx.

	Þessi formúla er stundum stytt í

	.. math:: \int f'g = fg - \int fg'.

Dæmi: Hlutheildun
~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Notum hlutheildun til að meta heildið

	.. math:: \int x \sin(x) dx.

.. admonition:: Lausn
  :class: daemi, dropdown

	Látum

	.. math::
		\begin{aligned}
			f'(x)&=\sin(x) & g(x) &= x\\
			f(x)&=-\cos(x) & g'(x) &= 1.
		\end{aligned}

	Þá fæst

	.. math::
		\begin{align}
			\int x \sin(x) dx &= -\cos(x)x - \int -\cos(x) \cdot 1 dx\\
			&= -x\cos(x)+\int \cos(x)dx\\
			&= -x\cos(x) + \sin(x) + C.
		\end{align}

Stundum getur verið nauðsynelgt að beita hlutheildun oftar en einu sinni
til að leysa dæmi.

Dæmi: Hlutheildun beitt tvisvar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Metum heildið

	.. math:: \int x^2 e^{3x} dx.

.. admonition:: Lausn
  :class: daemi, dropdown

	Látum

	.. math::
		\begin{aligned}
			f'(x)&=e^{3x} & g(x) &= x^2\\
			f(x)&=\frac{1}{3}e^{3x} & g'(x) &= 2x.
		\end{aligned}

	Fáum að

	.. math:: \int x^2 e^{3x} dx = \frac{1}{3}e^{3x}x^2 - \int \frac{1}{3}e^{3x} 2x dx.

	Beitum nú hlutheildun aftur. Látum

	.. math::
		\begin{aligned}
			f'(x)&=\frac{1}{3}e^{3x} & g(x) &= 2x \\
		 f(x)&=\frac{1}{9}e^{3x} & g'(x) &= 2.
		\end{aligned}

	.. math::
		\begin{aligned}
			\int \frac{1}{3}e^{3x} 2x dx &= \frac{1}{9}e^{3x} 2x - \int \frac{1}{9}e^{3x} 2 dx\\
			&= \frac{1}{9}e^{3x} 2x - \frac{2}{27}e^{3x} + C.
		\end{aligned}

	Ef við tökum þetta saman fæst

	.. math::
		\begin{align}
			\int x^2 e^{3x} dx &= \frac{1}{3}e^{3x}x^2 - \left(\frac{1}{9}e^{3x} 2x - \frac{2}{27}e^{3x} + C\right)\\
			&= e^{3x}\left(\frac{1}{3} x^2 - \frac{2}{9} x + \frac{2}{27}\right) - C
		\end{align}

Hlutheildun fyrir ákveðin heildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við höfum nú séð hvernig á að nota hlutheildun fyrir óákveðin heildi. Aðferðin er
að flestu leyti sú sama fyrir ákveðin heildi.

Setning: Hlutheildun fyrir ákveðin heildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Látum :math:`f(x)` og :math:`g(x)` vera föll með samfelldar afleiður á bilinu
	:math:`[a,b]`. Þá gildir að

	.. math:: \int_a^b f'(x) g(x) dx = \left[ f(x)g(x) \right]_a^b  - \int_a^b f(x) g'(x)dx.

	Þessi formúla er stundum stytt í

	.. math:: \int_a^b f' g = \left[ fg \right]_a^b  - \int_a^b f g'.

Dæmi: Hlutheildun fyrir ákveðin heildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	H áfram með dæmið hér að ofan, þar sem við mátum heildið

	.. math:: \int x \sin(x) dx.

	Nú skulum við bæta við heilda það yfir bilið :math:`[0,\pi]`, þ.e.

	.. math:: \int_0^\pi x \sin(x) dx.

.. admonition:: Lausn
  :class: daemi, dropdown

	Látum

	.. math::
		\begin{aligned}
			f'(x)&=\sin(x) & g(x) &= x\\
			f(x)&=-\cos(x) & g'(x) &= 1.
		\end{aligned}

	Með hlutheildun fæst

	.. math::
		\begin{align}
			\int_0^\pi x \sin(x) dx &= [-\cos(x)x]_0^\pi - \int_0^\pi -\cos(x) \cdot 1 dx\\
			&= -\cos(\pi)\cdot \pi - (-\cos(0)\cdot 0 )  + \int_0^\pi \cos(x)dx\\
			&= \pi + [\sin(x)]_0^\pi\\
			&= \pi + (\sin(\pi)-\sin(0))\\
			&= \pi
		\end{align}

---------

Óeiginleg heildi
----------------

Skilgreining: Óeiginlegt heildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

		(i) Látum :math:`f(x)` vera samfellt á bilinu :math:`[a,\infty[`. Þá gildir að

			.. math:: \int_a^\infty f(x) dx = \lim_{t\rightarrow \infty } \int_a^t f(x) dx

		af því gefnu að markgildið sé til.

		(ii) Látum :math:`f(x)` vera samfellt á bilinu :math:`]-\infty,b]`. Þá gildir að

			.. math:: \int_{-\infty}^b f(x) dx = \lim_{t\rightarrow \infty } \int_t^b f(x) dx

		af því gefnu að markgildið sé til.
		Í báðum tilfellum er sagt að *óeiginlega heildið* sé samleitið. Ef markgildið
		er ekki til er það sagt vera ósamleitið.

		(iii) Látum :math:`f(x)` vera samfellt á :math:`]-\infty;\infty[`. Þá gildir að

			.. math:: \int_{-\infty}^\infty f(x)dx = \int_{-\infty}^0 f(x) dx + \int_0^\infty f(x) dx,

		af því gefnu að bæði :math:`\int_{-\infty}^0 f(x) dx` og :math:`\int_0^\infty f(x) dx`
		séu samleitin . Ef annað hvort þeirra er ósamleitið þá er heildið :math:`\int_{-\infty}^\infty f(x)dx`
		ósamleitið.

Dæmi: Óeiginlegt heildi
~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Ákvörðum flatarmál svæðiðisins sem myndast undir ferli fallsin :math:`f(x)=\frac{1}{x}`
	yfir :math:`x`-ásinum og hægra megin við línuna :math:`x=1`.

	.. image:: ./myndir/kafli07/PMA_oeiginleg_heildi.png
		:align: center
		:width: 60%

.. admonition:: Lausn
  :class: daemi, dropdown

	Við viljum með öðrum orðum reikna óeiginlega heildið

	.. math:: A = \int_1^\infty \frac{1}{x}dx.

	Höfum

	.. math::
		\begin{align}
			A &= \int_1^\infty\\
			&= \lim_{t \rightarrow \infty} \int_1^t \frac{1}{x} dx\\
			&= \lim_{t \rightarrow \infty} \left[|x|\right]_1^t\\
			&= \lim_{t \rightarrow \infty} (\ln|t|-\ln(1))\\
			&= \infty
		\end{align}

	Sjáum að heildið er ósamleitið sem þýðir að flatarmál svæðisins er óendanlega stórt.

Dæmi: Óeiginlegt heildi
~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Metum heildið

	.. math:: \int_{-\infty}^0 \frac{1}{x^2+4} dx.

.. admonition:: Lausn
  :class: daemi, dropdown

	Fáum

	.. math::
		\begin{align}
			\int_{-\infty}^0 \frac{1}{x^2+4}dx &= \lim_{x \rightarrow -\infty} \int_t^0 \frac{1}{x^2+4}dx\\
			&= \lim_{t \rightarrow -\infty } \left[\frac{1}{2}\tan^{-1}(\frac{1}{2})\right]_t^0\\
			&= \frac{1}{2}\lim_{t \rightarrow -\infty}(\tan^{-1}(0)-\tan^{-1}(t/2))\\
			&= \frac{\pi}{4}
		\end{align}

	Svo heildið er samleitið að :math:`\frac{\pi}{4}`.

--------

Ósamfelldur heilidsstofn
-------------------------

Skilgreining: Ósamfelldur heildisstofn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

		(i) Látum :math:`f(x)` vera samfellt á bilinu :math:`[a,b[`. Þá gildir

		.. math:: \int_a^b f(x) dx = \lim_{t \rightarrow b^-} \int_a^t f(x) dx.

		(ii) Látum :math:`f(x) vera samfellt á bilinu :math:`]a,b]`. Þá gildir

		.. math:: \int_a^b f(x) dx = \lim_{t \rightarrow a^+} \int_t^b f(x) dx.

		Í báðum tilfellum segjum við að óeiginlega heildið sé samleitið ef markgildið er til.
		Annars segjum við að það sé ósamleitið.

		(iii) Ef :math:`f(x)` er samfellt á :math:`[a,b]` nema í einum innripunkti :math:`c` þá gildir

		.. math:: \int_a^b f(x) dx = \int_a^c f(x) dx + \int_c^b f(x) dx,

		af því gefnu að bæði :math:`\int_a^b f(x) dx` og :math:`\int_c^b f(x) dx`
		séu samleitin. Annars er sagt að heildið :math:`\int_a^b f(x) dx` sé ósamleitið.

Dæmi: Ósamfelldur heildisstofn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Metum heildið

	.. math:: \int_0^4 \frac{1}{\sqrt{4-x}} dx.

.. admonition:: Lausn
  :class: daemi, dropdown

	Tökum eftir því að heildisstofninn er samfelldur alls staðar á :math:`[0,4]` nema
	í hægri endapunktinum. Við fáum því að

	.. math::
		\begin{align}
			\int_0^4 \frac{1}{\sqrt{4-x}} dx &= \lim_{t \rightarrow 4^-} \int_0^t \frac{1}{\sqrt{4-x}}\\
			&= \lim_{t \rightarrow 4^-} [(-2–\sqrt{4-x})]_0^t\\
			&= \lim_{t \rightarrow 4^-} (-2\sqrt{4-t}+4)\\
			&=4
		\end{align}

	Svo heildið er samleitið að 4.

------

Samanburðarpróf
----------------

Setning: Samanburðarpróf
~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

	Látum :math:`f(x)` og :math:`g(x)` vera samfelld á :math:`[a,\infty[`.
	Gerum ráð fyrir að :math:`0 \leq f(x)\leq g(x)` fyrir :math:`x \geq a`.

		(i) Ef

		.. math:: \int_a^{\infty} f(x) dx = \lim_{t \rightarrow \infty} \int_a^t f(x) dx = \infty

		þá gildir að

		.. math:: \int_a^{\infty} g(x) dx = \lim_{t \rightarrow \infty} \int_a^t g(x) dx = \infty

		(ii) Ef

		.. math:: \int_a^{\infty} g(x) dx = \lim_{t \rightarrow \infty} \int_a^t g(x) dx = L

		þar sem :math:`L` er rauntala, þá gildir að

		.. math:: \int_a^{\infty} f(x) dx = \lim_{t \rightarrow \infty} \int_a^t f(x) dx = M

		fyrir einhverja rauntölu :math:`M \leq L`.

Dæmi: Samanburðarpróf
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

	Notum samanburðarpróf til að sýna að heildið

	.. math:: \int_1^\infty \frac{1}{xe^x} dx

	sé samleitið.

.. admonition:: Lausn
  :class: daemi, dropdown

	Höfum að

	.. math:: 0 \leq \frac{1}{xe^x} \leq \frac{1}{e^x} = e^{-x}.

	Svo ef :math:`\int_1^\infty e^{-x} dx` er samleitið þá er :math:`\int_1^\infty \frac{1}{xe^x} dx` það einnig.
	Fáum að

	.. math::
	 	\begin{align}
			\int_1^\infty e^{-x}dx &= \lim_{t \rightarrow \infty} \int_1^t e^{-x} dx\\
			&= \lim_{t \rightarrow \infty} \left[e^{-x}\right]_1^t\\
			&= \lim_{t \rightarrow \infty} (-e^{-t}+e^{-1})\\
			&= e^{-1}.
		\end{align}

	Fyrst :math:`\int_1^\infty e^{-x}dx` er samleitið þá er :math:`\int_1^{\infty} \frac{1}{xe^x}`
	það einnig.
