Fourier-ummyndun
================


Fourier-ummyndun. Reiknireglur. Plancerel-jafnan
------------------------------------------------

Skilgreining: :math:`L^1(\mathbb R)`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Við byrjum á að skilgreina rúm heildanlegra falla :math:`L^1(\mathbb R)`. Við táknum :math:`L^1(\mathbb R)` mengi allra falla :math:`f` þannig að :math:`|f|` er heildanlegt á :math:`\mathbb R`.

	.. math::
	    \int_{-\infty}^\infty |f(x)| dx < \infty\,.

	:math:`L^1(\mathbb R)` er vigurrúm, af því að

	1. Ef :math:`f \in L^1(\mathbb R)` og :math:`g \in L^1(\mathbb R)` þá er fallið :math:`f+g \in L^1(\mathbb R)`

	.. math::
	    \int_{-\infty}^\infty |f(x)+g(x)| dx \le  \int_{-\infty}^\infty |f(x)| dx < \infty\, +\int_{-\infty}^\infty |g(x)| dx < \infty\,.


	2. Ef :math:`f \in L^1(\mathbb R)` þá er :math:`\alpha f \in L^1(\mathbb R)`, þar sem :math:`\alpha \in\mathbb R`

	.. math::
	    \int_{-\infty}^\infty |\alpha f(x)| dx = |\alpha|\int_{-\infty}^\infty  |f(x)| dx <\infty\,.




Skilgreining: Fourier-ummyndun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Fyrir sérhvert fall :math:`f \in L^1(\mathbb R)` skilgreinum við fallið

	.. math::
	    \mathcal{F} f(k) = \int_{-\infty}^\infty e^{-i k x} f(x)dx\,, \qquad k \in\mathbb{R}\,.

	Við köllum fallið :math:`\mathcal{F} f` Fourier-mynd fallsins :math:`f` og við táknum hana með :math:`\mathcal{F}\{f\}` eða :math:`\widehat{f}`.

	Við köllum vörpun :math:`\mathcal{F}` Fourier-ummyndun.
	Hún er skilgreind á :math:`L^1(\mathbb R)` og varpar falli :math:`f\in L^1(\mathbb R)` á Fourier-mynd sína :math:`\mathcal{F} f`.

.. admonition:: Athugasemd
	:class: athugasemd

	Skilgreiningin á Fourier-ummyndun er ekki stöðluð.

Sýnidæmi
~~~~~~~~


Skilgreinum fall :math:`f_a` á eftifarandi hátt

.. math::
    f_a (x) = \begin{cases} 1, \qquad &|x|<a\,, \\ 0, \qquad & |x|\ge a \,  \end{cases} \,, \qquad f_a : \mathbb{R}\to \mathbb{R}\,,\quad a>0\,.

Við sjáum að :math:`f \in L^1(\mathbb R)`. Við reiknum nú Fourier-mynd fallsins :math:`f`

.. math::
    \widehat{f}_a(k)=\int_a^a e^{-i k x} dx= {e^{-i a k}-e^{i a k}\over -i k}=2 {\sin a k\over k}.

.. _example1:

Reiknireglur
~~~~~~~~~~~~

.. admonition:: Reiknireglur
	:class: setning

	Við byrjum á að skoða reiknireglur fyrir Fourier-ummyndanir.

	1. Látum :math:`f` og :math:`g` vera tvö föll í :math:`L^1(\mathbb R)`. Látum :math:`\alpha` og :math:`\beta` vera tvær tölur í :math:`\mathbb C`. Þá gildir

	.. math::
	    \mathcal{F}\left\{\alpha f+ \beta g\right\}(k) &=& \int_{-\infty}^\infty e^{-i k x}\left(\alpha f(x)+\beta g(x)\right)dx
	    = \alpha \int_{-\infty}^\infty e^{-i k x} f(x) dx+\beta \int_{-\infty}^\infty e^{-i k x} g(x) dx
	    \\ &=& \alpha\, \mathcal{F}\{f\}(k)+\beta\, \mathcal F\{g\}(k)\,,

	Þ.e.a.s. að Fourier-ummyndun er línuleg vörpun.

	2. Látum :math:`f \in L^1(\mathbb R)` og :math:`\alpha\in\mathbb R\smallsetminus\{0\}`. Þá gildir

	.. math::
	    \mathcal{F}\left\{f(\alpha x)\right\}(k) = {1\over |\alpha|} \mathcal F\{f(x)\}\left({k\over \alpha }\right)\,, \qquad k\in\mathbb R\,

	sem segir okkur hvernig Fourier-ummyndun breytist þegar :math:`x \to\alpha x`.

	3. Látum  :math:`f \in L^1(\mathbb R)` og :math:`\alpha\in\mathbb R`. Þá gildir

	.. math::
	    \mathcal{F}\left\{f(x-\alpha)\right\}(k) = e^{-i \alpha k} \mathcal F\{f(x)\}\left({k}\right)\,, \qquad k\in\mathbb R\,

	sem segir okkur hvernig Fourier-ummyndun breytist þegar  :math:`x \to x-\alpha`.

	4. Látum  :math:`f \in L^1(\mathbb R)` og :math:`\alpha\in\mathbb R`. Þá gildir

	.. math::
	    \mathcal{F}\left\{e^{i \alpha x}f(x)\right\}(k) = \mathcal F\{f(x)\}\left(k-\alpha\right)\,, \qquad k\in\mathbb R\,

	sem segir okkur hvernig Fourier-ummyndun breytist þegar  :math:`k \to k-\alpha`.

	5. Látum :math:`f \in L^1(\mathbb R)`. Þá gildir

	.. math::
	    \mathcal{F}\overline{\left\{f(x)\right\}}(k) = \overline{\mathcal F\{f(x)\}\left(-k\right)}\,, \qquad k\in\mathbb R\,.

	Athugum að ef :math:`f \in L^1(\mathbb R)` er raungilt, þ.e. :math:`f: \mathbb R\to\mathbb R`, þá gildir

	.. math::
	    \mathcal{F}\left\{f(x)\right\}(k) = \overline{\mathcal F\{f(x)\}\left(-k\right)}\,, \qquad k\in\mathbb R\,.

	6. Látum :math:`f \in L^1(\mathbb R)` vera jafnstætt. Þá gildir

	.. math::
	    \mathcal{F}\left\{f(x)\right\}(k) = 2 \int_0^\infty \cos(k\, x) f(x) dx \,, \qquad k\in\mathbb R\,.

	7. Látum :math:`f \in L^1(\mathbb R)` vera oddstætt. Þá gildir

	.. math::
	    \mathcal{F}\left\{f(x)\right\}(k) = - 2 i \int_0^\infty \sin(k\, x) f(x) dx \,, \qquad k\in\mathbb R\,.

	8. Látum :math:`f \in \mathcal{C}^1(\mathbb R)`. Gerum ráð fyrir að :math:`f`  og :math:`f'` séu í :math:`L^1(\mathbb R)`. Þá gildir

	.. math::
	    \mathcal{F}\left\{f'(x)\right\}(k)= i k \mathcal{F}\left\{f(x)\right\}(k)\,, \qquad k \in\mathbb R\,.

	Regla 8 tengir Fourier-mynd fallsins :math:`f` og Fourier-mynd afleiðu þess :math:`f'`.

	Ef :math:`f\in\mathcal{C}^m(\mathbb R)`  og  :math:`f, f', \dots, f^{(m)} \in L^1(\mathbb R)`, þá gildir

	.. math::
	    \mathcal{F}\left\{f^{(j)}(x)\right\}(k)= (i k)^j \mathcal{F}\left\{f(x)\right\}(k)\,, \qquad k \in\mathbb R\,, \quad j=0, 1, \dots\, m\,.

	9. Gerum ráð fyrir að föll :math:`f` og :math:`x f` séu í :math:`L^1(\mathbb R)`. Þá gildir

	.. math::
	    \mathcal{F}\left\{x f(x)\right\}(k)= i \frac{d}{dk}\mathcal{F}\left\{f(x)\right\}(k)\,, \qquad k \in\mathbb R\,.

Regla 9 segir okkur hver afleiða Fourier-myndar fallsins :math:`f` er.

Gerum ráð fyrir að föll :math:`f, x f, \dots, x^j f` séu í :math:`L^1(\mathbb R)`. Þá gildir

.. math::
    \mathcal{F}\left\{x^j f(x)\right\}(k)= i^j \frac{d^j}{dk^j}\mathcal{F}\left\{f(x)\right\}(k)\,, \qquad k \in\mathbb R\,.

.. _rulesFT:

Dæmi
~~~~

.. admonition:: Dæmi
	:class: daemi

	Við skoðum núna dæmi um hvernig nota má reiknireglurnar til þess að reikna Fourier-mynd falla.

	Athugum fall :math:`f(x)=e^{-a x^2/2}` þar sem  :math:`a>0`. Fallið :math:`f` uppfyllir afleiðujöfnu

	.. math::
	    f'(x)+a x f(x)=0\,.

	Ef við reiknum Fourier-myndina af þessari jöfnu og notum reiknireglur 9, þá fáum við

	.. math::
	        0= i k \widehat{f}(k)+i a {d\over dk}\widehat{f}(k)\,.

	Þetta er bara fyrsta stigs afleiðujafna fyrir Fourier-mynd fallsins :math:`f`, og lausnin er

	.. math::
	    \widehat{f}(k)= C e^{-{k^2\over 2 a}}\,, \qquad C\in \mathbb{R}\,.

	Til þess að finna fastann :math:`C`, getum notað

	.. math::
	    C=\widehat{f}(0)=\int_{-\infty}^{\infty} f(x) dx= \int_{-\infty}^{\infty} e^{-a x^2/2} dx= \sqrt{{2\pi}\over a}\,.

	Að lokum, fáum við

	.. math::
	    \mathcal{F}(e^{-a x^2/2})(k) = \sqrt{{2\pi}\over a}e^{-{k^2\over 2 a}}\,.

Eiginleikar Fourier-myndar
~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú viljum við skoða eiginleika Fourier-myndar. Gerum ráð fyrir að fall :math:`f` sé t.d. samfellt eða diffranlegt og svo framvegis, hvaða eiginleika hefur Fourier-mynd fallsins :math:`f`?

Setning
~~~~~~~

.. admonition:: Setning: Riemann-Lebesgue setning
	:class: setning


	Ef :math:`f\in L^1({{\mathbb R}})`, þá er :math:`{{\cal F}}f\in C({{\mathbb R}})` og

	.. math::
	    \lim_{\xi\to \pm \infty}{{\cal F}}f(\xi)=0.

	Ef við táknum mengi falla sem eru samfelld og stefna á núll þegar breytan stefnir á óendanlegt með :math:`C_0({{\mathbb R}})=\{F\in C({{\mathbb R}})\,;\, \lim_{|\xi|\to +\infty}F(\xi)=0\}`, þá þýðir setningin að Fourier-ummyndun :math:`\mathcal F` varpar rúminu :math:`L^1(\mathbb R)` í :math:`C_0(\mathbb R)`.

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

	Gerum ráð fyrir að fall :math:`f\in L^1(\mathbb R)` og að :math:`f` sé takmarkað. Gerum ráð fyrir að Fourier-mynd :math:`{{\cal F}}f` fallsins :math:`f` sé jákvæð fyrir öll :math:`k`, þ.e. :math:`{{\cal F}}f(k)\ge 0`. Þá er :math:`{{\cal F}}\in L^1(\mathbb R)`.

	Athugum að ef fall :math:`f\in L^1(\mathbb R)` er takmarkað (þ.e. :math:`|f|\le M`), þá er :math:`f\in L^2(\mathbb R)` (af því að :math:`|f|^2\le M|f|`).

Plancerel-jafnan
~~~~~~~~~~~~~~~~
Til þess að einfalda rithátt, táknum við hér Fourier-mynd falls :math:`f` með :math:`\widehat f`.

Gerum ráð fyrir að :math:`f\in L^1(\mathbb R)` og að :math:`f` sé takmarkað.
Þá gildir

.. math::
    \int_{-\infty}^\infty |f(x)|^2 dx= {1\over 2\pi} \int_{-\infty}^\infty |\widehat{f}(k)|^2 dk\,.

Þetta er Plancherel-jafnan. Hún er alhæfing af Parseval-jöfnu fyrir Fourier-ummyndunina.



Andhverfuformúla Fouriers. Afleiðujöfnur
----------------------------------------

Andhverfuformúla Fouriers
~~~~~~~~~~~~~~~~~~~~~~~~~
Við viljum nú finna fall :math:`f` ef við gerum ráð fyrir að Fourier-myndin :math:`\mathcal{F}f` sé gefin. Við munum skoða og reikna út Fourier-myndina af Fourier-mynd falls :math:`f`, þ.e.a.s. :math:`\mathcal{F}(\mathcal{F}f)`. Hugmyndin að baki er að Fourier-myndin af Fourier-mynd fallsins :math:`f` gefur fallið :math:`f`. Þetta er þó ekki svo einfalt. Fyrsta vandamál er að jafnvel þótt :math:`f\in L^1(\mathbb R)` þýðir það ekki nauðsynlega að :math:`\mathcal{F}f` sé í :math:`L^1(\mathbb R)` (svo Fourier-mynd hennar er ekki endilega vel skilgreind).

Ef við gerum ráð fyrir að bæði föllin :math:`f` og :math:`\mathcal{F}f` séu í :math:`L^1(\mathbb R)` og séu samfelld, þá er

.. math::
    ({{\cal F}}{{\cal F}}f)(x) &=
    \int_{-\infty}^{+\infty}e^{-ix\xi} \widehat{f}(\xi) d\xi =
    \int_{-\infty}^{+\infty}e^{-ix\xi}
    \bigg(\int_{-\infty}^{+\infty}e^{-iy\xi}f(y) \, dy\bigg)\, d\xi\\
    &=\int_{-\infty}^{+\infty}
    \bigg(\int_{-\infty}^{+\infty}e^{-i(x+y)\xi}f(y) \, dy\bigg)\, d\xi\,.

Vandamálið nú er að við getum ekki skipt á röð heildanna, við getum ekki heildað fyrst yfir :math:`\xi` og svo yfir :math:`y` af því að heildið :math:`\int_{-\infty}^{+\infty} e^{-i(x+y)\xi} d\xi` er ekki samleitið. Til að leysa málið, stingum við falli :math:`e^{-\varepsilon|\xi|}` inn í heildið og tökum síðan markgildi :math:`\varepsilon\to 0+`. Nú getum við reiknað út heildið að ofan og við fáum

.. math::
    ({{\cal F}}{{\cal F}}f)(x)&=\lim_{\varepsilon\to 0}
    \int_{-\infty}^{+\infty}e^{-\varepsilon|\xi|}
    \bigg(\int_{-\infty}^{+\infty}e^{-it\xi}f(t-x) \, dt\bigg)\, d\xi\\
    &=\lim_{\varepsilon\to 0} \int_{-\infty}^{+\infty}f(t-x)
    {{\cal F}}\{e^{-\varepsilon|\xi|}\}(t) \, dt\\
    &=\lim_{\varepsilon\to 0} \int_{-\infty}^{+\infty}f(t-x)
    {{\cal F}}\{e^{-|\xi|}\}(t/\varepsilon) \varepsilon^{-1}\, dt\\
    &=\lim_{\varepsilon\to 0} \int_{-\infty}^{+\infty}f(\varepsilon t-x)
    {{\cal F}}\{e^{-|\xi|}\}(t) \, dt\\
    &=f(-x)\int_{-\infty}^{+\infty}\dfrac 2{1+t^2} \, dt= 2\pi f(-x).

Að lokum getum við tekið þetta saman í eftirfarandi setningu

Setning
~~~~~~~

.. admonition:: Setning (Andhverfuformúla Fouriers)
	:class: setning

	Gerum ráð fyrir að fall :math:`f\in L^1(\mathbb R)\cap \mathcal{C}(\mathbb R)` og :math:`\widehat{f}\in L^1(\mathbb R)\cap \mathcal{C}(\mathbb R)`. Þá gildir

	.. math::
	    f(x) =\dfrac 1{2\pi}\int_{-\infty}^{+\infty}e^{ix\xi}\widehat f(\xi) \,
	    d\xi = \dfrac 1{2\pi}({{\cal F}}{{\cal F}}f)(-x), \qquad x\in {{\mathbb  R}}.


Setningin segir okkur að fallið :math:`f` sé samfelld samantekt (superposition á ensku) af veldisvísisföllum :math:`e^{ix\xi}`. Hún alhæfir framsetningu á lotubundnum föllum með Fourier-röðum til falla sem eru ekki lotubundin.

Fylgisetning
~~~~~~~~~~~~

.. admonition:: Fylgisetning
	:class: setning

	Ef :math:`\widehat{f}=\widehat{g}`, þá er :math:`f=g`.

Dæmi
~~~~

.. admonition:: Dæmi
	:class: daemi

	Andhverfuformúlan getur verið mjög gagnleg til þess að reikna Fourier-mynd. Við sjáum þetta með dæmi.
	Ef við viljum reikna Fourier-mynd falls :math:`f(x)={\sin a x\over x}`, getum við notað andhverfuformúlu Fouriers og sýnidæmi :ref:`4.1.3<example1>`, það er

	.. math::
	    \mathcal{F}\left({\sin a x\over x}\right) = \begin{cases} \pi\,, \qquad &|\xi|<a\\ 0\,, \qquad & \text{annars} \end{cases}\,.

Ef við viljum reikna Fourier-mynd fallsins :math:`f` beint út frá skilgreiningu þess, er það erfitt!


Skilgreining: Földun og Fourier-ummyndun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Látum :math:`f` og :math:`g` vera tvö föll á :math:`\mathbb  R`. Við skilgreinumn *földun* þeirra með

	.. math::
	    f\ast g(x)= \int_{-\infty}^{+\infty}f(x-t)g(t) \, dt,

	fyrir öll :math:`x\in {{\mathbb  R}}` þannig að heildið sé til.


.. admonition:: Eiginleikar
	:class: setning

	1. Gerum ráð fyrir að heildið að ofan sé til, þá er

	.. math::
	    f\ast g(x)= \int_{-\infty}^{+\infty}f(x-t)g(t) \, dt = \int_{-\infty}^{\infty} f(s)g(x-s)ds = g \ast f(x)\,,

	þar sem við höfum notað :math:`s=x-t`.

	2. Ef :math:`f\in L^1(\mathbb R)` og :math:`g` er takmarkað, þá er földun þeirra skilgreind á :math:`{{\mathbb  R}}`.

	3. Ef :math:`f\in L^1(\mathbb R)` og líka :math:`g\in L^1(\mathbb R)`, þá er földunin vel skilgreind, og ennfremur gildir að :math:`f\ast g` er í :math:`L^1(\mathbb R)`.


	4. Földunin uppfyllir sömu reglur og venjulegt margfeldi uppfyllir:

	.. math::
	    & f\ast (\alpha g +\beta h)= \alpha (f\ast g)+\beta (f\ast h)\,, \quad \forall \alpha, \beta \in\mathbb{R}\,.
	    \\
	    & f\ast g = g\ast f\,,
	    \\
	    & f\ast (g\ast h)= (f\ast g)\ast h\,,

	þar sem :math:`f, g, h` eru föll á :math:`\mathbb  R`, þ.a. földun þeirra sé vel skilgreind.

	5. Gerum ráð fyrir að fall :math:`f` sé diffranlegt og faldanir :math:`f\ast g` og :math:`f'\ast g` séu vel skilgreindar. Þá er :math:`f\ast g` diffranlegt og :math:`(f\ast g)'=f'\ast g`. Ef :math:`g` er líka diffranlegt, þá gildir :math:`(f\ast g)'= f\ast g'`.

	Við getum alhæft niðurstöðuna að ofan ef til dæmis fallið :math:`f` er :math:`m`-sinnum diffranlegt og :math:`f, f', \dots f^{(m)}` eru takmörkuð, þá er :math:`f\ast g \in\mathcal{C}^m(\mathbb{R})` og

	.. math::
	    (f\ast g)^{(k)}(x)= (f^{(k)}\ast g)(x)\,, \qquad x\in\mathbb{R}\, \quad k=0, \dots, m.

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

	Frá eiginleika 3, fáum við eftirfarandi setningu

	 Ef :math:`f\in L^1(\mathbb R)` og líka :math:`g\in L^1(\mathbb R)`, þá er földunin :math:`f\ast g` í :math:`L^1(\mathbb R)` og

	.. math::
	    {{\cal F}}\{f\ast g\}(\xi)={{\cal F}}f(\xi){{\cal F}}g(\xi), \qquad \xi\in {{\mathbb  R}}.





Afleiðujöfnur og Fourier-ummyndun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við byrjum á að skoða afleiðujöfnu með fasta stuðla

.. math::
    P(D)u=(a_mD^ m+\cdots+a_1D+a_0)u=f(x).

Til þess að finna lausn á jöfnunni getum við notað Fourier-ummyndun, ef t.d. :math:`f\in L^1(\mathbb R)`. Munið eftir reiknireglu 8, ef við gerum ráð fyrir að :math:`u` og afleiður þess séu í :math:`L^1(\mathbb R)`. Þá fáum við eftirfarandi niðurstöðu

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

	Gerum ráð fyrir að :math:`f\in L^1(\mathbb R)` og :math:`\widehat{f}\in L^1(\mathbb R)`.
	Gerum ráð fyrir að :math:`P(i\xi)\neq 0`. Þá hefur afleiðujafnan (ref) lausn :math:`u\in L^1(\mathbb R)\cap \mathcal{C}^m (\mathbb R)` sem gefin er með formúlunni

	.. math::
	    u(x)=\dfrac 1{2\pi}\int_{-\infty}^ {+\infty}
	    e^{ix\xi} \dfrac{\widehat f(\xi)}{P(i\xi)}\, d\xi, \qquad x\in {{\mathbb  R}}.

	Við sjáum að fallið :math:`u` sem skilgreint er að ofan uppfyllir jöfuna

	.. math::
	    P(D)u(x)&=\dfrac 1{2\pi}\int_{-\infty}^{+\infty}P(D_x)e^{ix\xi}
	    \dfrac{\widehat f(\xi)}{P(i\xi)}\, d\xi=
	    \dfrac 1{2\pi}\int_{-\infty}^{+\infty}P(i\xi)e^{ix\xi}
	    \dfrac{\widehat f(\xi)}{P(i\xi)}\, d\xi\\
	    &= \dfrac 1{2\pi}\int_{-\infty}^{+\infty}e^{ix\xi}
	    \widehat f(\xi)\, d\xi=f(x).


.. admonition:: Afleiðujöfnur, Fourier-ummyndun og földun
	:class: setning

	Gerum ráð fyrir að :math:`P(i\xi)\neq 0` fyrir öll :math:`\xi\in\mathbb R`.
	Ef við táknum andhverfu Fourier-mynd falls :math:`{1\over P(i\xi)}` (athugum að :math:`{1\over P(i\xi)} \in L^1(\mathbb{R})`) með


	.. math::
	    E(x)= {1\over 2\pi} \int_{-\infty}^{\infty} {e^{i x \xi}\over P(i\xi)} d\xi\,, \qquad x\in\mathbb R\,,

	þá fæst

	.. math::
	    E\ast f(x) &= \int_{-\infty}^{\infty} E(x-t) f(t)dt= \int_{-\infty}^{\infty}\left({1\over 2\pi} \int_{-\infty}^{\infty} {e^{i (x-t) \xi}\over P(i\xi)} d\xi\right)f(t) dt=\\
	    &={1\over 2\pi}\int_{-\infty}^{\infty}{e^{i x \xi}\over P(i\xi)}\left(\int_{-\infty}^\infty f(t) e^{-i \xi t} dt\right)d\xi= {1\over 2\pi}\int_{-\infty}^{\infty}{e^{ix\xi}\over P(i \xi)}\widehat f(\xi)\, d\xi =u(x).

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

	Gerum ráð fyrir að :math:`P` sé margliða af stigi :math:`m` með ólikar núllstöðvar :math:`\lambda_1, \dots, \lambda_{\ell}` með margfeldni :math:`m_1, \dots, m_{\ell}`, að :math:`P(i\xi)` hafi enga núllstöð á :math:`\mathbb{R}`, að :math:`Q` sé margliða af stigi :math:`\le m-1` og að stofnbrotaliðun á ræða fallinu :math:`Q/P` sé gefin með

	.. math::
	    \dfrac {Q(\zeta)}{P({\zeta})} =\sum\limits_{k=1}^\ell
	    \sum\limits_{j=1}^{m_k} \dfrac{A_{jk}}{({\zeta}-{\lambda}_k)^j}.

	Þá er andhverfa Fourier-mynd fallsins :math:`{\xi}\mapsto Q(i\xi)/P(i{\xi})` gefin með formúlunni

	.. math::
	    f(x)&=
	    \sum_{\substack{{{\operatorname{Re\, }}}{\lambda}_k<0}}
	    \sum\limits_{j=1}^{m_k} A_{jk}
	    \tfrac 1{(j-1)!}H(x)x^{j-1}e^{{\lambda}_kx}\\
	    &-\sum_{\substack{{{\operatorname{Re\, }}}{\lambda}_k>0}}
	    \sum\limits_{j=1}^{m_k} A_{jk} \tfrac 1{(j-1)!} H(-x)x^{j-1}e^{{\lambda}_kx},
	    \qquad x\neq 0.\nonumber

Dæmi
~~~~

.. admonition:: Dæmi
	:class: daemi

	Skoðum jöfnu

	.. math::
	    -u{{^{\prime\prime}}}+\omega^ 2u=e^{-|x|}=f(x), \qquad \omega^ 2 \neq 1,
	    \qquad x\in {{\mathbb  R}}.

	Við sjáum að :math:`P(X)=-X^2+\omega^2`, og :math:`P(i\xi)=\xi^2+\omega^2`. Fourier-mynd fallsins :math:`e^{-|x|}=f(x)` er :math:`\widehat f(\xi)={2 \over 1+\xi^ 2}`. Tökum Fourier-mynd jöfnunnar, þá fáum við

	.. math::
	    \xi^ 2 \widehat u(\xi)+\omega^ 2 \widehat u(\xi) = \dfrac
	    2{1+\xi^ 2}, \qquad \xi\in {{\mathbb  R}}.

	Þá er

	.. math::
	    \widehat u(\xi)=
	    \dfrac 2{(\omega^ 2+\xi^ 2)(1+\xi^ 2)} =\dfrac 1{1-\omega^ 2}\bigg(
	    \dfrac 1\omega {{\cal F}}\{e^{-\omega|x|}\}({\xi})-{{\cal F}}\{e^{-|x|}\}({\xi})
	    \bigg).

	Nú getum við notað andhverfuformúlu og þá fæst loks að

	.. math::
	    u(x)= \dfrac 1{1-\omega^ 2}\bigg( \dfrac 1\omega e^{-\omega|x|} - e^{-|x|} \bigg).


Úrlausn á hlutafleiðujöfnum með Fourier-ummyndun
------------------------------------------------

Einvíða bylgjujafnan og d'Alembert-formúla
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



Við skoðum einvíðu bylgjujöfnuna

.. math::
    \dfrac{\partial^2u}{\partial t^2}
    -c^2\dfrac{\partial^2u}{\partial x^2}=0,

þar sem fallið :math:`u(x,t)` er skilgreint fyrir öll :math:`x \in \mathbb{R}` og :math:`t \in \mathbb{R}`.
Leitum að slíkri lausn.

Skiptum um hnit með :math:`x = {\xi+\eta\over 2}` og :math:`t = {\xi-\eta\over 2 c}` og skrifum bylgjujöfnuna sem

.. math::
    \partial^2_{t} u(t,x)- c^2 \partial^2_x u (t,x)= -4 \,c^2 \partial^2_{\xi\eta} v(\eta,\xi)\, \qquad v(\eta,\xi) = u(x(\eta,\xi),t(\eta,\xi)).

Athugum að við notum að :math:`\partial^2_{t,x}=\partial^2_{x,t}`, sem gildir til dæmis ef lausnin er tvisvar sinnum samfellt deildanleg.

Almenn lausn á jöfnunni að ofan er :math:`u(\eta, \xi)=f(\xi)+g(\eta)`, þar sem föllin :math:`f(\xi)`, :math:`g(\eta)` eru ótiltekin. Þá er

.. math::
    u(x,t)=f(\xi(x,t))+g(\eta(x,t))= f(x+ct)+g(x-ct)\,.

Þá fæst eftirfarandi setning sem niðurstaða.

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

	Sérhver lausn :math:`u\in C^2({{\mathbb R}}^2)` á bylgjujöfnunni er af gerðinni :math:`u(x,t)=f(x+ct)+g(x-ct)`, þar sem :math:`f,g\in C^2({{\mathbb R}})`.
	Ef :math:`u(x,t)=f_1(x+ct)+g_1(x-ct)` er önnur slík framsetning á lausninni, þá er til fasti :math:`A` þannig að :math:`f_1(x)=f(x)+A` og :math:`g_1(x)=g(x)-A`.

Fyrir gefið :math:`t_0 > 0`, er graf fallsins :math:`g(x − ct_0)` næstum því eins og graf fallsins :math:`g(x)`, eini munurinn er að grafið :math:`g(x − ct_0)` er hliðrað um :math:`c t_0` til hægri. Við túlkum því fallið :math:`g(x − ct)` sem bylgju sem hreyfist til hægri með hraða :math:`c` og köllum það *framáttarbylgju*. Á svipaðan hátt er graf fallsins :math:`f(x+ct_0)` hliðrað um :math:`c t_0` til vinstri, fallið :math:`f(x + ct)` táknar bylgju sem hreyfist til vinstri með hraða :math:`c` og kallast það *bakáttarbylgja*.

Við skoðum nú bylgjujöfnuna með upphafsskilyrðum, það er

.. _UpphafBylgja:

.. math::
    \begin{cases}
    \dfrac{\partial^2u}{\partial t^2}
    -c^2\dfrac{\partial^2u}{\partial x^2}=0, &x\in {{\mathbb  R}},\ t>0, \\
    u(x,0)=\varphi(x), \quad \partial_tu(x,0)=\psi(x), &x\in {{\mathbb  R}}.
    \end{cases}

Við viljum finna lausn sem er í :math:`C^2({{\mathbb R}}^2)`, sem gefin er í setningunni að ofan. Þá þurfum við tengja :math:`f(x+ct), g(x-ct)` við :math:`\varphi(x), \psi(x)`.
Niðurstaðan er

Setning
~~~~~~~

.. admonition:: Setning: d'Albembert-formúlan
	:class: setning

	Upphafsgildisverkefnið :ref:`að ofan<UpphafBylgja>` hefur ótvírætt ákvarðaða lausn sem gefin er með formúlunni

	.. math::
	    u(x,t)=\dfrac 12\big(\varphi(x+ct)+\varphi(x-ct)\big)
	    +\dfrac 1{2c}\int_{x-ct}^{x+ct}\psi({\xi})\, d{\xi}.


Formúlan kallst d'Alembert-formúlan. Hún gefur almenna lausn í :math:`C^2({{\mathbb R}}^2)` á upphafsgildisverkefninu.


.. ggb:: m6xq5gqq
  :width: 700
  :height: 320
  :img: polarggb.png
  :imgwidth: 4cm
  :zoom_drag: true

|
|

Bylgjujafnan, Fourier-ummyndun og földun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við getum skrifað d'Alembert-formúluna sem földunarheildi: Skilgreinum fall :math:`E_t` sem

.. math::
    E_t(x)=E(x,t)= \begin{cases} 1/2c, &|x|\leq ct,\\ 0,
    &|x|>ct.\end{cases}

þá er

.. math::
    && \dfrac 1{2c}\int_{x-ct}^{x+ct}\psi(y)\, dy
    =\int_{-\infty}^{+\infty}E_t(x-y)\psi(y)\, dy = \big(E_t\ast \psi\big)(x),
    \\
    && \dfrac 12\big(\varphi(x+ct)+\varphi(x-ct)\big)
    =\dfrac{\partial}{\partial t}\bigg(
    \dfrac 1{2c}\int_{x-ct}^{x+ct}\varphi(y)\, dy
    \bigg) =\dfrac{\partial}{\partial t} E_t\ast \varphi(x),

og lausnin verður

.. math::
    u(x,t)=\dfrac{\partial}{\partial t}\big( E_t\ast \varphi\big)(x)+
    E_t\ast \psi(x).

--------------------------------------------

Við viljum nú leiða þessa formúlu út með því að nota Fourier-ummyndun. Tökum Fourier-mynd af öllum liðum sem koma fyrir í upphafsgildisverkefninu. Fyrst þurfum við að finna Fourier-myndir :math:`\partial_t u` og :math:`\partial_x u`.

.. math::
    {{\cal F}}\{\partial_t^2 u\}(\xi,t)
    =\int\limits_{-\infty}^{+\infty}e^{-ix\xi}\partial_t^2 u(x,t)\, dx
    =\partial_t^2\int\limits_{-\infty}^{+\infty}e^{-ix\xi}u(x,t)\, dx
    =\partial_t^2\widehat u(\xi,t).

.. math::
    {{\cal F}}\{{\partial}_x^2u\}({\xi},t)
    =\int\limits_{-\infty}^{+\infty}e^{-ix\xi}\partial_x^2u(x,t)\, dx
    =(i{\xi})^2\widehat u({\xi},t)=-{\xi}^2\widehat u({\xi},t),

þar sem við höfum notað reikniregluna 8 í :ref:`4.1.4<rulesFT>`.

Að lokum verður upphafsgildisverkefnið

.. math::
    \begin{cases}
    {\partial}_t^2\widehat u({\xi},t)+c^2{\xi}^2
    \widehat u({\xi},t)=0, &{\xi}\in {{\mathbb  R}},\ t>0,\\
    \widehat u({\xi},0)=\widehat\varphi({\xi}), \quad {\partial}_t\widehat
    u({\xi},t)=\widehat{\psi}({\xi}), &{\xi}\in {{\mathbb  R}}.
    \end{cases}

Athugum að :math:`{\partial}_t^2\widehat u({\xi},t)+c^2{\xi}^2\widehat u({\xi},t)=0` er annars stigs venjuleg afleiðujafna í :math:`t`, og :math:`\xi` er bara fasti. Þá er lausnin

.. math::
    \begin{aligned}
    \widehat u({\xi},t)&=
    \cos(ct{\xi})\widehat\varphi({\xi})
    +\dfrac{\sin(ct{\xi})}{c{\xi}}\widehat{\psi}({\xi})
    \end{aligned}

En, ef við reiknum Fourier-myndin fallsins :math:`E_t` sem við skilgreindum að ofan, þá er

.. math::
    \begin{aligned}
    \widehat E_t(\xi)&=\int_{-\infty}^{+\infty}e^{-ix\xi}E_t(x)\, dx
    =\dfrac 1{2c}\int_{-ct}^{ct}e^{-ix\xi}\, dx\\
     &=\dfrac 1{2c}\bigg[\dfrac{e^{-ix\xi}}{-i\xi}\bigg]_{-ct}^{ct}
    =\dfrac{\sin(ct\xi)}{c\xi}.\end{aligned}

Það þýðir að við getum umritað lausnina sem

.. math::
    \widehat u({\xi},t)=\dfrac{\partial}{\partial t}\widehat E_t({\xi})\widehat\varphi({\xi})+\widehat E_t({\xi})\widehat {\psi}({\xi}).

og niðurstaðan fyrir :math:`u` fæst svo með því að taka andhvefa Fourier-mynd og nota földunarreglur.

Hliðraða bylgjujafnan
~~~~~~~~~~~~~~~~~~~~~~

Við skoðum

.. math::
    \begin{cases}
    \dfrac{\partial^2u}{\partial t^2}
    -c^2\dfrac{\partial^2u}{\partial x^2}=f(x,t), &x\in {{\mathbb  R}}, \ t>0,\\
    u(x,0)=\partial_tu(x,0)=0, &x\in {{\mathbb  R}},
    \end{cases}

Leitum að sérlausn á þessu verkefni. Eins og áður notum við Fourier-ummyndun og fáum

.. math::
    \begin{cases}
    {\partial}_t^2\widehat u({\xi},t)+c^2{\xi}^2
    \widehat u({\xi},t)=\widehat f({\xi},t), &{\xi}\in {{\mathbb  R}},\ t>0,\\
    \widehat u({\xi},0)={\partial}_t\widehat u({\xi},0)=0, &{\xi}\in {{\mathbb  R}}.
    \end{cases}

Green-fall afleiðuvirkjans :math:`D_t^2+c^2{\xi}^2` er :math:`G_{\xi}(t,{\tau})=g({\xi},t-{\tau})=\sin(c(t-\tau){\xi})/c{\xi}`.
Athugum að :math:`g(ξ,t)=\widehat E_t({\xi})=\widehat E({\xi},t).`

Þá er Fourier-mynd lausnarinnar á jöfnunni

.. math::
    \widehat u({\xi},t)
    =\int_0^t  g({\xi},t-\tau)\widehat f({\xi},\tau)\, d{\tau}
    =\int_0^t\widehat E({\xi},t-\tau)\widehat f({\xi},\tau)\, d{\tau}.

Til þess að finna :math:`u` þurfum við að nota andhverfuformúlu Fouriers, þá er

.. math::
    \begin{aligned}
    u(x,t)&
    =\dfrac 1{2{\pi}}\int_{-\infty}^{+\infty}e^{ix{\xi}}
    \bigg(\int_0^t \widehat E({\xi},t-\tau)\widehat f({\xi},\tau)\, d{\tau}\bigg)
    \, d{\xi}\label{15.4.3}\\
    &=\int_0^t \bigg(\dfrac 1{2{\pi}}\int_{-\infty}^{+\infty}e^{ix{\xi}}
    \widehat E({\xi},t-\tau)\widehat f({\xi},\tau)\, d{\xi}\bigg)
    \, d{\tau}\nonumber\\
    &=\int_0^t \int_{-\infty}^{+\infty}
    E(x-y,t-\tau)f(y,\tau)\, dy\, d{\tau}.\nonumber\end{aligned}

Ef við viljum skrifa þetta sem földunarheildi þurfum við að framlengja föllin fyrir öll :math:`t`. Við höfum :math:`E(x,t) = 0` ef :math:`t < 0` og ef við skilgreinum :math:`f(x,t) = 0` fyrir :math:`t < 0`, þá fæst

.. math::
    u(x,t) = E\ast f(x,t), \qquad x\in\mathbb{R}, t>0

þar sem :math:`\ast` stendur hér fyrir földun falla af tveimur breytistærðum sem er skilgreind með sambærilegum hætti og áður.

Þetta má einnig rita sem

.. math::
    \begin{aligned}
    u(x,t)
    &=\int_0^t \int_{-\infty}^{+\infty} E(x-y,t-\tau)f(y,\tau)\, dy\,
    d{\tau}\\
    &=\dfrac 1{2c} \int_0^t \int_{x-c(t-\tau)}^{x+c(t-\tau)}
    f(y,{\tau})\, dyd{\tau}\nonumber\\
    &=\dfrac 1{2c}\iint\limits_{T(x,t)}f(y,{\tau})\, dyd{\tau},\nonumber\end{aligned}

þar sem :math:`T(x,t)` er þríhyrningurinn í :math:`(y,\tau)`-planinu með hornpunktana :math:`(x, t), (x − ct, 0)` og :math:`(x + ct, 0)`. Þríhyrningurinn kallast *ákvörðunarsvæði* punktins :math:`(x,t)`.


Varmaleiðnijafnan, Fourier-ummyndun og földun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við lítum nú á varmaleiðnijöfnuna með upphafsskilyrðum

.. _UpphafVarmi:

.. math::
    \begin{cases}
    \dfrac{{\partial}u}{\partial t}
    -{\kappa}\dfrac{\partial^2u}{\partial x^2}=0, &x\in {{\mathbb  R}}, \ t>0,\\
    u(x,0)={\varphi}(x), &x\in {{\mathbb  R}},
    \end{cases}

Eins og áður viljum við finna lausn með því að nota Fourier-ummmyndun. Tökum Fourier-mynd af öllum liðunum og þá fæst að Fourier-mynd fallsins :math:`u` þarf að uppfylla

.. math::
    \begin{cases}
    \partial_t\widehat u({\xi},t)
    +{\kappa}{\xi}^2\widehat u({\xi},t)=0, &{\xi}\in {{\mathbb  R}}, \ t>0,\\
    \widehat u({\xi},0)=\widehat {\varphi}({\xi}), &{\xi}\in {{\mathbb  R}}.
    \end{cases}

Nú verður jafnan :math:`\partial_t\widehat u({\xi},t)+{\kappa}{\xi}^2\widehat u({\xi},t)=0` einfaldlega fyrsta stigs afeiðujafna í :math:`t`, og lausn hennar er :math:`\widehat u({\xi},t)=e^{-{\kappa}t{\xi}^2}\widehat {\varphi}({\xi})`.

Við viljum finna lausn sem földunheildi. Athugum að

.. math::
    e^{-{\kappa}t{\xi}^2} = \mathcal{F}(E)(\xi)\,
    \qquad E(x,t)=E_t(x)=\begin{cases} \dfrac 1{\sqrt{4{\pi}{\kappa}t}}e^{-x^2/4{\kappa}t},
    &x\in {{\mathbb  R}}, \ t>0,\\
    0, &x\in {{\mathbb  R}}, \ t\leq 0.\end{cases}

Þá er :math:`\widehat u({\xi},t)=e^{-{\kappa}t{\xi}^2}\widehat {\varphi}({\xi})= \widehat{E_t} ({\xi})\widehat {\varphi}({\xi})`.

Fallið :math:`E` kallast *hitakjarni* eða *varmaleiðnikjarni*.

Til þess að skilja lausnina er gott að skoða eiginleika hitakjarnans :math:`E`:


.. math::
    \begin{aligned}
    1. & \lim\limits_{t\to 0+} E_t(x) =
    \begin{cases} +{\infty}, &x=0,\\
    0, &x\neq 0,\end{cases}
    \\
    2. &
    \int_{-{\infty}}^{+{\infty}} E_t(x)\, dx
    =\int_{-{\infty}}^{+{\infty}}
    \dfrac 1{\sqrt{\pi}}e^{-y^2}\, dy = 1\,,\\
    3. & \,({\partial}_t-{\kappa}{\partial}_x^2)E(x,t)=0, \qquad t>0\,.
    \end{aligned}


Þá getum við notað andhverfuformúlu Fouriers og við fáum:

.. math::
    u(x,t)=E_t\ast {\varphi}(x)=\int_{-{\infty}}^{+{\infty}}
    \dfrac 1{\sqrt{4{\pi}{\kappa}t}}e^{-(x-y)^2/4{\kappa}t}{\varphi}(y)\,
    dy, \qquad t>0.


Það er ekki erfitt að sjá að lausn  :math:`u(x,t)=E_t\ast {\varphi}(x)` uppfyllir :ref:`upphafsgildisverkefnið að ofan<UpphafVarmi>` með því að nota eingileika hitakjarnans :math:`E`:

.. math::
    ({\partial}_t-{\kappa}{\partial}_x^2)u(x,t)
    =\int_{-{\infty}}^{+{\infty}}
    ({\partial}_t-{\kappa}{\partial}_x^2)E(x-y,t) {\varphi}(y)\, dy=0.


.. math::
    \begin{aligned}
    \lim\limits_{t\to 0+} u(x,t) &=
    \lim\limits_{t\to 0+} E_t\ast {\varphi}(x)
    \\
    &=\int_{-{\infty}}^{+{\infty}}
    \dfrac 1{\sqrt{\pi}}e^{-y^2}\lim\limits_{t\to 0+}
    {\varphi}(x-\sqrt{4{\kappa}t}y)\, dy\\
    &={\varphi}(x)\int_{-{\infty}}^{+{\infty}}
    \dfrac 1{\sqrt{\pi}}e^{-y^2}\, dy ={\varphi}(x).\end{aligned}

Þá skiljum við eftirfarandi setningu

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning


	Gerum ráð fyrir að :math:`\varphi` sé samfellt og takmarkað fall á :math:`{{\mathbb R}}`.  Þá hefur  :ref:`upphafsgildisverkefnið að ofan<UpphafVarmi>` lausn :math:`u` sem gefin er með formúlunni

	.. math::
		u(x,t)=E_t\ast \varphi(x)=\int_{-\infty}^{+\infty}E_t(x-\xi)\varphi(\xi)\,
		d\xi, \qquad x\in {{\mathbb  R}}, \ t>0,

	þar sem hitakjarninn er gefinn með formúlunni

	.. math::
		E(x,t)=E_t(x)=H(t) \dfrac
		1{\sqrt{4{\pi}{\kappa}t}}e^{-x^2/4{\kappa}t},
		\qquad (x,t)\neq (0,0).


Hliðraða varmaleiðnijafnan með óhliðruðum upphafsskilyrðum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við lítum nú á hliðruðu varmaleiðnijöfnuna með óhliðruðu upphafsskilyrði, þ.e.

.. _UpphafVarmi2:

.. math::
    \begin{cases}
    \dfrac{{\partial}u}{\partial t}
    -{\kappa}\dfrac{\partial^2u}{\partial x^2}=f(x,t), &x\in {{\mathbb  R}}, \ t>0,\\
    u(x,0)=0, &x\in {{\mathbb  R}}.
    \end{cases}

Leitum að sérlausn á henni. Við tökum Fourier-myndina af öllum liðunum


.. math::
    \begin{cases}
    \partial_t\widehat u({\xi},t)
    +{\kappa}{\xi}^2\widehat u({\xi},t)=\widehat f({\xi},t), &{\xi}\in {{\mathbb  R}}, \ t>0,\\
    \widehat u({\xi},0)=0, &{\xi}\in {{\mathbb  R}}.
    \end{cases}

Skoðum jöfnuna að ofan: hún er fyrsta stigs hliðruð afleiðujafna í :math:`t`. Við getum notað Green-fall, og það er :math:`G_\xi(t,\tau)=e^{-\kappa(t-\tau)\xi^2}=\widehat E_{t-\tau}(\xi)`.

Eins og áður við skrifum við Fourier-mynd lausnar og eftir það tökum við andhverfu Fourier-myndina. Þá er


.. math::
    \widehat u({\xi},t)=\int_0^te^{-{\kappa}(t-{\tau})x^2}\widehat
    f({\xi},t)\, d{\tau} = \int_0^t\widehat E_{t-{\tau}}({\xi})\widehat
    f({\xi},t)\, d{\tau}.


.. math::
    \begin{aligned}
    u(x,t)&=\dfrac 1{2{\pi}}\int_{-\infty}^{+\infty}e^{ix{\xi}}
    \bigg(\int_0^t\widehat E_{t-{\tau}}({\xi})\widehat
    f({\xi},{\tau})\, d{\tau} \bigg)\, d{\xi}\\
    &=\int_0^t\bigg(
    \dfrac 1{2{\pi}}\int_{-\infty}^{+\infty}e^{ix{\xi}}
    \widehat E_{t-{\tau}}({\xi})\widehat
    f({\xi},{\tau})\, d{\xi}\bigg)\, d{\tau}\\
    &=\int_0^t \int_{-\infty}^{+\infty}
    E(x-y,t-\tau)f(y,{\tau})\, dy d{\tau} \\
    &= E\ast f(x,t) \end{aligned}


Við fáum eftirfarandi niðurstöðu.

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

	Gerum ráð fyrir að :math:`f` sé samfellt fall á opna efra hálfplaninu :math:`\{(x,t); t>0\}`, sé takmarkað á lokuninni :math:`\{(x,t); t\geq 0\}` og taki gildið 0 á neðra hálfplaninu :math:`\{(x,t); t<0\}`. Þá hefur :ref:`upphafsgildisverkefnið að ofan<UpphafVarmi2>` ótvírætt ákvarðaða lausn :math:`u`, sem gefin er með formúlunni

	.. math::
		u(x,t)=E\ast f(x,t), \qquad x\in {{\mathbb  R}},\ t>0,

	þar sem :math:`E` táknar hitakjarnann, sem skilgreindur er með formúlunni

	.. math::
		E(x,t)=H(t) \dfrac
		1{\sqrt{4{\pi}{\kappa}t}}e^{-x^2/4{\kappa}t},
		\qquad (x,t)\neq (0,0).


Hliðraða varmaleiðnijafnan með hliðruðu upphafsskilyrði
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upphafsgildisverkefnið er núna

.. math::
    \begin{cases}
    \dfrac{{\partial}u}{\partial t}
    -{\kappa}\Delta u=f(x,t), &x\in {{\mathbb  R}}^n, \ t>0,\\
    u(x,0)=\lim\limits_{t\to 0+}u(x,t)={\varphi}(x), &x\in {{\mathbb  R}}^n,
    \end{cases}

Við gerum ráð fyrir að :math:`f` sé samfellt fall á :math:`\{(x,t)\in {{\mathbb R}}^n\times {{\mathbb R}}; t\geq 0\}`, :math:`{\varphi}` sé samfellt fall á :math:`{{\mathbb R}}^n` og bæði :math:`f`` og :math:`{\varphi}` séu takmörkuð.

Hitakjarninn er

.. math::
    E(x,t)=E_t(x)=H(t) \dfrac
    1{\big(4{\pi}{\kappa}t\big)^{n/2}}e^{-x^2/4{\kappa}t},
    \qquad x\in {{\mathbb  R}}^n,\ (x,t)\neq (0,0),

og lausnin verður

.. math::
    u(x,t)=E_t\ast {\varphi}(x)+E\ast f(x,t), \qquad x\in {{\mathbb  R}}^n, t>0.


Fourier-ummyndun og leifareikningur
-----------------------------------

Við skoðum hér hvernig við getum reiknað Fourier-myndir og andhverfu þeirra með því að nota leifareikning.
Við byrjum á að setja fram fyrstu niðurstöðu fyrir Fourier-myndir.

Munið að við táknum með :math:`\mathcal O(X)` mengi allra fágaðra falla á :math:`X`.

Setning: Fourier-myndir reiknaðar með leifareikningi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum fall :math:`f\in L^1({{\mathbb R}})\cap {{\cal O}}({{\mathbb C}}\setminus A)`, þar sem :math:`A` er endanlegt mengi.
	Gerum ráð fyrir að :math:`\lim\limits_{r\to \infty}\max_{|z|=r}|f(z)|=0`.
	Táknum efra hálfplanið með :math:`H_+=\{z\in {{\mathbb C}}; {{\operatorname{Im\, }}}z>0\}` og neðra hálfplanið með :math:`H_-=\{z\in {{\mathbb C}}; {{\operatorname{Im\, }}}z<0\}`.
	Þá er

	.. math::
	    \widehat f(\xi) =
	    \begin{cases}  2\pi i\sum_{\alpha\in A\cap H_+}
	    {{\operatorname{Res}}}(e^{-iz\xi}f(z),\alpha), & \xi < 0,\\
	    -2\pi i\sum_{\alpha\in A\cap H_-}
	    {{\operatorname{Res}}}(e^{-iz\xi}f(z),\alpha),  & \xi > 0.
	    \end{cases}

Dæmi
~~~~

.. admonition:: Dæmi
	:class: daemi

	Skoðum fall :math:`f(x)=1/(1+x^2), x\in {{\mathbb R}}.` Athugum að fallið :math:`f` er jafnstætt, svo samkvæmt reglu 6 er Fourier-mynd þess jafnstæð. Þá getum við reiknað Fourier-mynd fyrir :math:`\xi<0`, og eftir það framlengjt hana samkvæmt því. Fallið :math:`f` hefur eitt skaut í :math:`x=i` á :math:`H_+` og :math:`\max_{|z|=r}|f(z)| \le {1\over r^2-1}` sem stefnir á 0 þegar :math:`r` stefnir á óendanlegt. Þá beitum við setningunni að ofan og fáum

	.. math::
	    \widehat f(\xi) = 2\pi i
	    {{\operatorname{Res}}}\bigg(\dfrac{e^{-iz\xi}}{1+z^2},i\bigg)
	    =\pi e^{\xi}, \qquad \xi<0.

	Að lokum fæst

	.. math::
	     \widehat f(\xi) =\pi e^{-|\xi|}, \qquad \xi\in {{\mathbb  R}}.


Andhverfar Fourier-myndir reiknaðar með leifareikningi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Á svipaðan hátt höfum við niðurstöðu fyrir andhverfar  Fourier-myndir.

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

	Gerum ráð fyrir því að :math:`f\in L^1({{\mathbb R}})\cap PC^1({{\mathbb R}})`, að það sé hægt að framlengja skilgreiningarsvæði Fourier–myndarinnar :math:`\widehat f`, þannig að :math:`\widehat f\in {{\cal O}}({{\mathbb C}}\setminus A)`, þar sem mengið :math:`A` er endanlegt og :math:`\lim\limits_{r\to +\infty}\max_{|\zeta|=r}|\widehat f(\zeta)|=0`. Þá er

	.. math::
	    \tfrac 12 (f(x+)+f(x-))=\begin{cases}
	    i\sum\limits_{\alpha\in A\cap H_+}{{\operatorname{Res}}}\big(e^{ix\zeta}\widehat
	    f(\zeta),\alpha\big), & x>0\\
	    -i\sum\limits_{\alpha\in A\cap H_-}{{\operatorname{Res}}}\big(e^{ix\zeta}\widehat
	    f(\zeta),\alpha\big), & x<0.
	    \end{cases}

Athugum að ef fallið :math:`f` er samfellt þá er :math:`\tfrac 12 (f(x+)+f(x-))= f(x)`.

Dæmi
~~~~

.. admonition:: Dæmi
	:class: daemi

	Lítum á :math:`\widehat f(\xi)=\xi/(\xi^2+4\xi+5)`. Fallið :math:`\widehat f` hefur tvö skaut í :math:`zeta_1 = -2+i\in H_+` og :math:`\zeta_2 = -2-i\in H_-`. Ennfremur er það hvorki jafnstætt né oddstætt, svo við þurfum að reikna báðar leifar:

	.. math::
	    \begin{gathered}
	    i{{\operatorname{Res}}}\bigg( \dfrac{e^{ix\zeta}\zeta}{\zeta^2+4\zeta+5},-2+i\bigg)
	    = (-1+i/2)e^{-x-2ix},\\
	    -i{{\operatorname{Res}}}\bigg( \dfrac{e^{ix\zeta}\zeta}{\zeta^2+4\zeta+5},-2-i\bigg)
	    = (-1-i/2)e^{x-2ix}.\end{gathered}

	Að lokum fáum við samkvæmt setningunni að ofan

	.. math::
	    f(x) =\begin{cases}
	    (-1+i/2)e^{-x-2ix}\,, \qquad & x>0\\
	    (-1-i/2)e^{x-2ix}\,, \qquad & x<0
	    \end{cases}

	sem við getum umskrifað líka sem :math:`f(x)=-(1-i{{\operatorname{sign}}}(x)/2)e^{-|x|-2ix}`, fyrir öll  :math:`x\in\mathbb{R}`.



Laplace-ummyndun og leifareikningur
-----------------------------------

Rifjum upp að

1. Ef fall :math:`f` á :math:`\mathbb{R_+}` er af veldisvísisgerð, þá eru til fastar :math:`M>0` og :math:`c>0` þ.a.

.. math::
    |f(t)|\leq Me^{c t}, \qquad t\in {{\mathbb  R}}_+.
    :label: eq.expo


2. Skilgreining á Laplace-mynd er

.. math::
    \mathcal L{f}(s)= \int_{0}^\infty e^{-s t} f(t) dt \,, \qquad s\in \mathbb C\,,
    :label: eq.test


þar sem :math:`f` er skilgreint á :math:`\mathbb{R_+}` með gildi í :math:`\mathbb C`, og er heildanlegt á sérhverju lokuðu og takmörkuðu bili á :math:`\mathbb{R_+}`.




Setning: Andhverfar Laplace-myndir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _FourierMellin:

.. admonition:: Setning: Andhverfuformúla Fourier-Mellin
	:class: setning

	Gerum ráð fyrir að fall :math:`f:{{\mathbb R}}_+\to {{\mathbb C}}` sé í :math:`PC^1 (\mathbb R)` og sé af veldisvísisgerð :eq:`eq.expo`. Þá gildir  um sérhvert :math:`\xi> c` og sérhvert :math:`t> 0` að

	.. math::
	    \begin{aligned}
	    \label{7.2.2}
	    \tfrac 12(f(t+)+f(t-))& = \lim_{R\to +\infty} \dfrac 1{2\pi}
	    \int_{-R}^{+R}e^{(\xi+i\eta)t}{{\cal L}}f(\xi+i\eta) \, d\eta \\
	    &= \lim_{R\to +\infty} \dfrac 1{2\pi i}
	    \int_{\xi-iR}^{\xi+iR}e^{\zeta t}{{\cal L}}f(\zeta) \, d\zeta. \nonumber\end{aligned}


	Ef :math:`\mathcal{L} f(\xi+i \eta)\in L^1(\mathbb R)` sem fall af :math:`\eta`, þá er :math:`f` samfellt í :math:`t` og

	.. math::
	    \begin{aligned}
	    f(t)&=  \dfrac 1{2\pi}
	    \int_{-\infty}^{+\infty}e^{(\xi+i\eta)t}{{\cal L}}f(\xi+i\eta) \, d\eta
	    \\
	    &= \dfrac 1{2\pi i}
	    \int_{\xi-i\infty}^{\xi+i\infty}e^{\zeta t}{{\cal L}}f(\zeta) \,
	    d\zeta. \nonumber\end{aligned}

	Athugum að :math:`\int_{\xi-i\infty}^{\xi+i\infty}` og :math:`\int_{\xi-iR}^{\xi+iR}` tákna heildi eftir línunni :math:`\{\xi+i \eta; \eta \in \mathbb{R}\}`.

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`f` og :math:`g` vera tvö samfelld föll af veldisvísisgerð á :math:`\mathbb{R_+}`, og gerum ráð fyrir að :math:`\mathcal{L}f(\alpha_j)=\mathcal{L}g(\alpha_j)`, þar sem :math:`\{\alpha_j\}` er runa af ólíkum punktum, :math:`\alpha_j\to\alpha, \operatorname{Re}\alpha_j>c, \operatorname{Re}\alpha>c`. Þá er :math:`f(t)=g(t)`fyrir öll :math:`t\in\mathbb{R}_+`.



Andhverfar Laplace-myndir reiknaðar með leifareikningi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _LaplaceRes:

Hér viljum við hafa praktiskar aðferðir til þess að reikna heildi í :ref:`setningunni<FourierMellin>`.
Við getum notað leifareikning og við byrjum á að skoða niðurstöðuna fyrst.


:math:`M_r` táknar hálfhringinn sem stikaður er með :math:`\gamma_r(\theta)=\xi+i r e^{i\theta}, \theta\in [0, \pi]`.

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

	Gerum ráð fyrir að fall :math:`f:{{\mathbb R}}_+\to {{\mathbb C}}` sé í :math:`PC^1 (\mathbb R)` og sé af veldisvísisgerð :eq:`eq.expo`.
	Gerum ráð fyrir að hægt sé að framlengja :math:`\mathcal{L}f` yfir í fágað fall á :math:`\mathbb C\setminus A`, þar sem :math:`A` er endanlegt mengi.
	Ef :math:`\xi>c` og :math:`\lim\limits_{r\to +\infty}\max_{\zeta\in M_r}|{{\cal L}}f(\zeta)|=0`,
	þá er

	.. math::
	    \frac 12(f(t+)+f(t-))=
	    \sum_{\alpha\in A}{{\operatorname{Res}}}(e^{\zeta t}{{\cal L}}f(\zeta),\alpha)
	    \qquad t>0.
	    :label: eq.LaplaceRes

	Ef :math:`f` er samfellt, þá er

	.. math::
	    f(t)= \sum_{\alpha\in A}{{\operatorname{Res}}}(e^{\zeta t}{{\cal L}}f(\zeta),\alpha).


Andhverfar Laplace-myndir og afleiðujöfnur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við skoðum afleiðujöfnu með fastastuðla

.. math::
    P(D)u=(D^m+a_{m-1}D^{m-1}+\cdots+a_1D+a_0)u=f(t).

Til þess að leysa jöfnuna getum við notað Green-fallið :math:`G(t,\tau)=g(t-\tau)`.
Munið að Laplace-mynd fallsins :math:`g` er gefin með


.. math::
    {{\cal L}}g(\zeta)=\dfrac 1{P(\zeta)}.


Nú samkvæmt :ref:`setningunni<LaplaceRes>`, getum við reiknað út Green-fallið :math:`g` með formúlunni :eq:`eq.LaplaceRes`. Þá er

.. math::
    g(t)= \sum\limits_{\alpha\in{\cal N}(P)}
    {{\operatorname{Res}}}\bigg( \dfrac {e^{t\zeta}}{P(\zeta)},\alpha\bigg).
    :label: eq.GreenLaplace


Dæmi
~~~~

.. admonition:: Dæmi
	:class: daemi

	Lítum á afleiðujöfnu

	.. math::
	    P(D)u=(D^4-2 D^3+2 D^2-2 D+1)u=f(t)

	með óhliðruðu upphafsskilyrðunum

	.. math::
	    u(0)=\dots=u^{(3)}(0)=0.


	Við reiknum út Green-fallið með því að nota Laplace-ummyndun og leifareikning. Samkvæmt formúlunni :eq:`eq.GreenLaplace`,  þurfum við að reikna kennimargliðuna :math:`P(\zeta)`. Þá er

	.. math::
	    P(\zeta)= \zeta^ 4-2\zeta^ 3+2\zeta^ 2-2\zeta+1 = (\zeta-1)^ 2(\zeta-i)(\zeta+i).

	:math:`{1\over P(\zeta)}` hefur skaut í :math:`1, i, -i`, og við fáum

	.. math::
	    \begin{aligned}
	    g(t)&= \sum\limits_{\alpha=1,i,-i} {{\operatorname{Res}}}\bigg(\dfrac{e^{\zeta t}}
	    {(\zeta-1)^ 2(\zeta-i)(\zeta+i)},\alpha\bigg)\\
	    &= \left.\dfrac d{d\zeta} \dfrac{e^{\zeta t}}{(\zeta-i)(\zeta+i)}
	    \right|_{\zeta=1} + \dfrac{e^{it}}{(i-1)^ 2(2i)} +
	    \dfrac{e^{-it}}{(-i-1)^ 2(-2i)}\\
	    &= \left.\dfrac{te^{\zeta t}}{\zeta^ 2+1}\right|_{\zeta=1}
	    +\left.\dfrac{e^{\zeta t}(-2\zeta)}{(\zeta^ 2+1)^ 2}\right|_{\zeta=1}
	    +\dfrac{e^{it}}4+\dfrac{e^{-it}}4\\
	    &=\tfrac 12 te^ t -\tfrac 12 e^ t +\tfrac 12\cos t.\end{aligned}


	Að lokum er lausnin gefin með

	.. math::
	    u(t) = \int_0^t G(t,\tau) f(\tau) d\tau = \int_0^t \left(\tfrac 12 (t-\tau)e^{(t-\tau)} -\tfrac 12 e^{(t-\tau)} +\tfrac 12\cos (t-\tau)\right) f(\tau) d\tau
