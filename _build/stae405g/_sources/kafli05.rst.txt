.. _heildun:

.. index:: 
	töluleg heildun

Töluleg heildun
===============

*So much universe, and so little time.*
-- Terry Pratchett


Gerum ráð fyrir að :math:`x_0,x_1, \ldots, x_n` séu punktar á bilinu
:math:`[a,b]` og að við þekkjum gildi :math:`f` í þessum punktum. Þá
getum við fundið brúunarmargliðuna :math:`p_n` gegnum punktana
:math:`(x_k,f(x_k))` og skrifað

.. math:: f(x) = p_n(x) + r_n(x),

þar sem skekkjan :math:`r_n` er gefin með

.. math:: r_n(x) = f[x_0,\ldots,x_n,x](x-x_0)\cdots(x-x_n).

Nú er auðvelt að reikna heildi margliða, svo við nálgum heildi
:math:`f` með

.. math::

   \int\limits_a^b f(x) dx \approx 
     I_n(f) := \int\limits_a^b p_n(x) dx

og skekkjan í þessari nálgun er gefin með

.. math:: e_n = \int\limits_a^b r_n(x) dx.

Þessi aðferð er kölluð *Newton-Cotes-heildun*.

.. index::
	töluleg heildun; Newton-Cotes

Aðferðirnar
~~~~~~~~~~~

Newton-Cotes heildun
--------------------

Hugsum okkur að brúunarpunktarnir :math:`x_0, \ldots, x_n` séu ólíkir.
Þá getum við skrifað :math:`p_n` með Lagrange-margliðum

.. math::

   p_n(x) = \sum\limits_{k=0}^n f(x_k) \ell_k(x),
     \quad
     \ell_k(x) = \prod\limits_{\stackrel{j=0}{j \not= k}}^n
     \frac{(x-x_j)}{(x_k-x_j)},

og þá er heildi :math:`p_n` jafnt

.. math::

   \int\limits_a^b p_n(x) dx = 
     \sum\limits_{k=0}^n f(x_k) A_k,
     \quad \text{þar sem} \quad
     A_k = \int\limits_a^b \ell_k(x) dx.

Athugið að gildi :math:`A_k` veltur aðeins á brúunarpunktunum
:math:`x_0, \ldots,
x_n` en ekki gildum :math:`f(x_k)`. Ef það á að heilda mörg föll yfir
sama bil er því hægt að reikna gildi :math:`A_k` í eitt skipti fyrir öll
og endurnýta þau svo.

Sýnidæmi
--------

Metum heildi :math:`f(x) = e^{-x}\cos(x)` og
:math:`g(x) = \sin (\frac{x^2}{2})` yfir bilið :math:`[0,2]` með að nota
skiptipunktana :math:`x_0 = 0`, :math:`x_1 = 1` og :math:`x_2 = 2`.
Lagrange-margliðurnar sem við eiga eru

.. math::

   \ell_0(x) = \frac{(x-1)(x-2)}{2}, \quad
     \ell_1(x) = -x(x-2), \quad
     \ell_2(x) = \frac{x(x-1)}{2}

svo við fáum að

.. math::

   \begin{gathered}
     A_0 = \frac{1}{2} \int\limits_0^2 (x-1)(x-2) dx = \frac{1}{3},
     \qquad
     A_1 = -\int\limits_0^2 x(x-2) dx = \frac{4}{3}, \\
     A_2 = \frac{1}{2} \int\limits_0^2 x(x-1) dx = \frac{1}{3}.\end{gathered}

Nú eru stuðlarnir fundnir og því fáum við

.. math::

   \begin{aligned}
     \int\limits_0^2 f(x) dx &\approx
     f(0)\frac{1}{3} + f(1)\frac{4}{3} + f(2)\frac{1}{3}\\
     &= \frac{1 + 4e^{-1}\cos(1) + e^{-2}\cos(2)}{3}
     \approx 0.59581\end{aligned}

og

.. math::

   \begin{aligned}
     \int\limits_0^2 g(x) dx &\approx
     g(0)\frac{1}{3} + g(1)\frac{4}{3} + g(2)\frac{1}{3}\\
    & = \frac{4\sin(1/2) + \sin(2)}{3} 
     \approx 0.91972.\end{aligned}

Gildi heildanna eru :math:`\int\limits_0^2 f(x) dx \approx 0.58969` og
:math:`\int\limits_0^2 g(x) dx \approx 0.99762` með 5 réttum aukastöfum
svo nálgunargildin verða að teljast nokkuð góð miðað við hversu lítið
fór í þau.

.. index::
	töluleg heildun; trapisureglan

Trapisureglan
-------------

Nú ætlum við að leiða út formúlur fyrir helstu reglum fyrir nálgun á
heildum. Sú fyrsta er *trapisuregla*.

Veljum :math:`x_0 = a` og :math:`x_1 = b` sem skiptipunktana okkar. Þá
er graf :math:`p_1` línustrikið gegnum :math:`(a,f(a))` og
:math:`(b,f(b))`,

.. math::

   p_1(x) = f(a) \ell_0(x) + f(b) \ell_1(x)
     = f(a)\frac{b-x}{b-a} + f(b) \frac{x-a}{b-a}

og vigtirnar eru

.. math:: A_0 = \int\limits_a^b \ell_0(x) = \frac{b-a}{2} = A_1,

svo

.. math::

   \int\limits_a^b f(x) dx \approx 
     \frac{b-a}{2}\left(f(a)+f(b)\right).

Trapisureglan er kölluð þessu nafni því með henni nálgum við heildi
:math:`f` með flatarmáli trapisunnar sem hefur hornpunktana
:math:`(a,0)`, :math:`(b,0)`, :math:`(b,f(b))` og :math:`(a,f(a))`.

.. index::
	töluleg heildun; miðpunktsreglan

Miðpunktsreglan
---------------

Enn einfaldari er *miðpunktsreglan*, þá veljum við aðeins einn
skiptipunkt, :math:`x_0 = \frac{1}{2}(a+b)`, og brúunarmargliðan verður
fastamargliðan :math:`p_0(x) = f(x_0)`. Þá er

.. math:: \int\limits_a^b f(x) dx \approx (b-a)\, f\left(\frac{a+b}{2}\right)

.. index::
	töluleg heildun; regla Simpsons

Regla Simpsons
--------------

Nú veljum við þrjá skiptipunkta, :math:`x_0 = a`, :math:`x_1 = b` og
:math:`x_2 =
\frac{1}{2}(a+b)`. Til einföldunar skulum við hliðra fallinu :math:`f`
um miðpunkt bilsins :math:`m=\tfrac{1}{2}(a+b)`.

Við skilgreinum :math:`\alpha=\tfrac 12(b-a)` og
:math:`g(x) = f\big(x+m\big)`

Þá hliðrast :math:`a`, :math:`m` og :math:`b` yfir í :math:`-\alpha`,
:math:`0` og :math:`\alpha` og

.. math::

   \int\limits_{-\alpha}^{\alpha} g(x) dx = 
     \int\limits_a^b f(x) dx.

Lagrange margliðurnar og vigtirnar eru

.. math::

   \begin{aligned}
     l_0(x) &= \frac{(x-\alpha)x}{(-\alpha-\alpha)(-\alpha - 0)} 
     = \frac{(x-\alpha)x}{2\alpha^2} \\
     A_0 &= \int_{-\alpha}^{\alpha} l_0(x)\,dx = \frac{\alpha}{3} \\
     l_1(x) &= \frac{(x-(-\alpha))(x-0)}{(\alpha - ( -\alpha))(\alpha - 0)}
     = \frac{(x+\alpha)x}{2\alpha^2}\\
     A_1 &= \int_{-\alpha}^{\alpha} l_1(x)\,dx = \frac{\alpha}{3}\\
     l_2(x) &= \frac{(x-(\alpha))(x-\alpha)}{0-(-\alpha)(0-\alpha)}
     = \frac{(x+\alpha)(x-\alpha)}{-\alpha^2}\\
     A_2 &= \int_{\alpha}^{\alpha} l_2(x)\,dx = \frac{4\alpha}{3}\end{aligned}

Nálgunarformúlan verður þá

.. math::

   \begin{aligned}
     \int_a^b f(x) \, dx = \int\limits_{-\alpha}^{\alpha} g(x) \, dx
     &\approx \frac{\alpha}{3}g(-\alpha) + \frac{\alpha}{3}g(\alpha) 
     + \frac{4\alpha}{3}g(0)\\
     &=(b-a)\left( \frac{1}{6}f(a) + \frac{4}{6}f
       \left( \frac{a+b}{2}\right) + \frac{1}{6} f(b)  \right)\end{aligned}

Ef við tökum brúunarmargliðu gegnum :math:`a`, :math:`b` og
:math:`\frac{1}{2}(a+b)` með :math:`\frac{1}{2}(a+b)` tvöfaldan þá fáum
við 3. stigs brúunarmargliðu

.. math:: p_3(x) = p_2(x) + g[-\alpha, \alpha, 0, 0](x+\alpha)(x-\alpha)x

Heildið yfir seinni liðinn hægra megin er 0 því margliðan
:math:`(x+a)(x-a)x` er oddstæð, en heildið yfir fyrri liðinn er

.. math:: \frac \alpha3(g(-\alpha) + 4g(0) + g(\alpha)).

Út kemur því Simpson-regla.

.. ggb:: 2677051
    :width: 700
    :height: 400
    :img: ./heildun.png
    :imgwidth: 12cm

.. index::
	töluleg heildun; samsett 

Samsettar útgáfur
~~~~~~~~~~~~~~~~~

*Sometimes the truth is arrived at by adding all the little lies together and 
deducting them from the totality of what is known.*
-- Terry Pratchett, Going Postal

Inngangur
---------

Þar sem Newton-Cotes heildun notar brúunarmargliður fylgja henni nokkur
vandamál.

Ef okkur finnst nákvæmnin í nálguninni vera of lítil getum við ekki
búist við að hún batni við að fjölga skiptipunktum; þá hækkar stig
margliðunnar líklega sem orsakar sveiflukenndari hegðun.

Eins er ekki gott að halda sig við margliður af lægra stigi; ef bilið
sem á að heilda yfir er stórt væri mikil tilviljun að 1., 2. eða 3.
stigs brúunarmargliða nálgaði fallið vel á öllu bilinu.

Lausnin á þessu vandamáli er í sama anda og fyrir splæsibrúun. Við
veljum skiptingu

.. math:: a  =x_0 < x_1 < \ldots < x_n = b

á bilinu :math:`[a,b]`.

Um heildi gildir að

.. math:: \int\limits_a^bf(x)\, dx = \sum\limits_{k=1}^n \ \ \int\limits_{x_{k-1}}^{x_k} f(x) \, dx

svo við getum nálgað heildi :math:`f` á sérhverju litlu hlutbili
:math:`[x_{k-1},x_k]` með að heilda brúunarmargliðu af lágu stigi og
lagt öll gildin saman til að fá nálgun á heildi :math:`f` yfir allt
bilið.

Þegar ákveðin regla er notuð til að nálga heildi :math:`f` á sérhverju
hlutbili er þetta kölluð *samsetta* útgáfa reglunnar. Einfalt er að
leiða út samsettar útgáfur reglanna að ofan.

.. index::
	töluleg heildun; samsetta trapisureglan

Samsetta trapisureglan
----------------------

Á sérhverju hlutbili er

.. math::

   \int\limits_{x_{k-1}}^{x_k} f(x) \, dx
     \approx
     \frac{x_k-x_{k-1}}{2}(f(x_{k-1}) + f(x_k))

svo

.. math::

   \int\limits_a^b f(x) \, dx
     \approx
     \sum\limits_{k=1}^n \frac{x_k-x_{k-1}}{2}(f(x_{k-1}) + f(x_k)).

Ef öll hlutbilin eru jafn löng og :math:`h = x_k-x_{k-1}`, þá fæst

.. math::

   \begin{gathered}
     \int\limits_a^b f(x) \, dx \\
     \approx 
     h\left( \frac{1}{2}f(a) + f(a+h) + f(a+2h) 
       + \cdots + f(a+(n-1)h) + \frac{1}{2}f(b) \right).\end{gathered}

.. ggb:: 2687771
    :width: 700
    :height: 400
    :img: ./samsett_trapisuregla.png
    :imgwidth: 12cm

.. index::
	töluleg heildun; samsetta miðpunktsreglan

Samsetta miðpunktsreglan
------------------------

Fljótséð er að

.. math::

   \int\limits_a^b f(x) \, dx
     \approx
     \sum\limits_{k=1}^n (x_k-x_{k-1})f
     \left(
       \frac{x_{k-1}+x_k}{2}
     \right)

Ef öll hlutbilin eru jafn löng verður formúlan

.. math::

   \int\limits_a^b f(x) \, dx
     \approx
     h \sum\limits_{k=1}^n f \left(\frac{x_{k-1}+x_k}{2}\right)

.. index::
	töluleg heildun; samsett regla Simpsons

Samsett regla Simpsons
----------------------

Hér er venjan að velja :math:`2n+1` jafndreifða skiptipunkta og fá
:math:`n` jafn stór hlutbil. Þá er :math:`h = \frac{b-a}{2n}`,
:math:`x_k = a + kh` fyrir :math:`k =
0,\ldots,2n` og hlutbilin eru :math:`[x_{2k-2},x_{2k}]` fyrir
:math:`k = 1,
\ldots, n`.

Á hverju hlutbili er

.. math::

   \int\limits_{x_{2k-2}}^{x_{2k}} f(x) \, dx
     \approx
     2h \left(
       \frac{1}{6} f(x_{2k-2}) + \frac{4}{6} f(x_{2k-1}) 
       + \frac{1}{6} f(x_{2k})
     \right)

svo að

.. math::

   \begin{aligned}
     \int\limits_a^b f(x) \, dx
     \approx &
     \sum\limits_{k=1}^n
     \bigg(
       \frac{h}{3}
       \Big(
         f(x_{2k-2}) + 4f(x_{2k-1}) + f(x_{2k})
       \Big)
     \bigg) \\
     = &
     \frac{h}{3}
     \Big( 
       f(a) + 4f(a+h) + 2f(a+2h)+ 4f(a+3h) + 2f(a+4h) \\
       &+ \cdots + 2f(a+(2n-2)h) + 4f(a+(2n-1)h) + f(b).
     \Big)\end{aligned}

.. index::
	töluleg heildun; skekkjumat

Skekkjumat
~~~~~~~~~~

Inngangur
---------

Rifjum upp grunnhugmyndina að baki nálgunarformúlunum. Við veljum
brúunarpunkta :math:`x_0, \ldots, x_n` í :math:`[a,b]`, látum
:math:`p_n` vera tilsvarandi brúunarmargliðu og skrifum

.. math:: f(x) = p_n(x) + r_n(x)

þar sem :math:`r_n(x) = f[x_0, \ldots , x_n, x](x-x_0) \cdots (x-x_n)`.
Þá er nálgunin

.. math:: \int_a^b f(x)\,dx \approx \int_a^b p_n(x)\,dx

með skekkjuna

.. math:: \int_a^b r_n(x)\,dx

Nú viljum við meta skekkjuheildið.


.. index::
	Meðalgildissetningin fyrir heildi

Meðalgildissetningin fyrir heildi
---------------------------------

Við skekkjumatið í þessum kafla munum við þurfa að nota eftirafarandi
setningu nokkrum sinnum. 

Ef :math:`G:[a,b] \to {{\mathbb  R}}` er samfellt fall og
:math:`{\varphi}` er heildanlegt fall sem skiptir ekki um formerki á
bilinu :math:`[a,b]` þá er til tala :math:`\eta \in [a,b]` þannig að

.. math:: \int_a^b G(x){\varphi}(x)\, dx = G(\eta) \int_a^b {\varphi}(x)\, dx.

Trapisureglan
-------------

Við getum hliðrar sérhverju bili :math:`[a,b]` yfir í :math:`[-\alpha,\alpha]` 
þar sem :math:`\alpha = (b-a)/2`, því er nóg fyrir okkur að skoða samhverf
bil af gerðinni :math:`[-\alpha,\alpha]`. Þetta er það sama og við gerðum 
þegar `regla Simpsons <https://notendur.hi.is/~bsm/stae405/kafli05.html#regla-simpsons>`_
var leidd út. 

Samkvæmt `3.7.7 <https://notendur.hi.is/~bsm/stae405/kafli03.html#id9>`_ þá er

.. math:: r_1(x) = f[-\alpha, \alpha, x](x+\alpha)(x-\alpha)

Athugum að

.. math:: (x+\alpha)(x-\alpha) = (x^2 - \alpha^2)

skiptir ekki um formerki á bilinu :math:`]-\alpha, \alpha[`. Þá gefur
meðalgildissetningin fyrir heildi að til er :math:`\eta \in [a,b]`
þannig að\ 

.. math::

   \begin{aligned}
     \int_a^b r_1(x)\,dx 
     &= f[-\alpha, \alpha, \eta]
     \int_{-\alpha}^{\alpha}(x^2 - \alpha^2)\,dx\\
     &= \frac{f''(\xi)}{2!} \left( - \frac{4}{3}\alpha^3 \right)\\
     &= \frac{-f''(\xi)}{2!}\frac{(b-a)^3}{6}, \qquad \xi \in [a,b]\end{aligned}

Niðurstaða:

.. math::

   \int_a^b f(x)\,dx = (b-a)
     \left( \frac{1}{2} f(a) + \frac{1}{2}f(b) \right) 
     - \frac{1}{12} f''(\xi)(b-a)^3

Samsetta trapisureglan
----------------------

Ef við lítum á samsettu trapisuregluna með jafna skiptingu þar sem
hlutbilin eru :math:`[x_i,
x_{i+1}]`, þá fáum við fyrir hvert hlutbil skekkjuna

.. math:: - \frac{h^3}{12}f''(\xi_i), \qquad \xi_i \in [x_i, x_{i+1}]

Ef við leggjum skekkjurnar saman og beitum milligildissetningunni á 
:math:`f''` þá fæst að til er :math:`\xi \in [a,b]` þannig að 
:math:`f''(\xi) = \sum_{i=1}^n f''(\xi_i)/n`.
Þá fáum við a' 

.. math::

   \int_a^b f(x)\,dx = T(h) - \frac{h^2}{12}(b-a)f''(\xi), \qquad 
     \xi \in [a,b]

að því gefnu að :math:`f\in C^2 [a,b]`.

Athugið að hér er :math:`T(h)` útkoman úr samsettu Trapisureglunni með jafna
skiptingu :math:`h = \frac{b-a}n`.

Miðpunktsregla
--------------

Til einföldunar skoðum við áfram bilið :math:`[-\alpha,\alpha]`. Veljum
miðpunktinn sem tvöfaldan brúunarpunkt

.. math::

   \begin{aligned}
     &p_1(x) = f(0) + f'(0)x\\
     &r_1(x) = f[0,0,x]x^2\end{aligned}

Athugum að heildið af :math:`f'(0)x` yfir :math:`[-\alpha,\alpha]` er 0.
Nú skiptir :math:`x^2` ekki um formerki og því gefur meðalgildisreglan
fyrir heildi að til er :math:`\eta \in [-\alpha,\alpha]` þannig að

.. math::

   \begin{aligned}
     \int_a^b r_1(x)\,dx 
     &= \int_{-\alpha}^{\alpha} f[0,0,x]x^2 \,dx\\
     &= f[0,0,\eta]\int_{-\alpha}^\alpha x^2\,dx\\
     &= \frac{f''(\xi)}{2!}2\frac{\alpha^3}{3}\\
     &= \frac{(b-a)^3}{24}\cdot f''(\xi)\end{aligned}

Þar sem :math:`\xi` fæst úr `skekkjumatinu fyrir brúunarmargliður <https://notendur.hi.is/~bsm/stae405/kafli03.html#id9>`_.

Samsetta miðpunktsreglan
------------------------

Fyrir hvert bil fáum við skekkjulið:

.. math:: \frac{h^3}{24}\cdot f''(\xi_i)

Leggjum saman skekkjuliðina og beitum milligildissetningunni, þá fæst að
til er :math:`\xi` þannig að:

.. math::

   \int_a^b f(x)\,dx = h \sum_{i=1}^n 
     f\left(a+ (i - \frac{1}{2})h\right) + \frac{b-a}{24}f''(\xi)h^2

Regla Simpsons
--------------

.. math::

   \int_a^b f(x)\,dx \approx (b-a) 
     \left( 
       \frac{1}{6}f(a) + \frac{4}{6}f
       \left( \frac{1}{2}(a+b) \right) + \frac{1}{6}f(b)
     \right)

Leiddum út þessa formúlu með því að taka brúunarmargliðu :math:`p_3(x)`
með punktana :math:`-\alpha, \alpha, 0, 0`. Skekkjan er

.. math::

   f(x) - p_3(x) = f[-\alpha, \alpha, 0, 0, x]
     (x+\alpha)(x-\alpha)x^2

þar með er skekkjan í formúlu Simpsons:

.. math::

   \int_{-\alpha}^{\alpha}f[-\alpha, \alpha, 0, 0, x]
     (x+\alpha)(x-\alpha)x^2 \,dx

Fallið :math:`x\mapsto (x+\alpha)(x-\alpha)x^2 = (x^2 - \alpha^2)x^2` er
:math:`\leq 0` á :math:`[-\alpha, \alpha]`. Þar með gefur
meðalgildissetningin fyrir heildi að til er
:math:`\eta \in [-\alpha, \alpha]` þannig að skekkjan er

.. math::

   \begin{gathered}
     f[-\alpha, \alpha, 0, 0, \eta]
     \int_{-\alpha}^{\alpha}(x^2 - \alpha^2)x^2 \,dx \\
     = \frac{f^{(4)}(\xi)}{4!}\cdot \frac{(-4)}{15}\cdot \alpha^5
     = \frac{-f^{(4)}(\xi)}{90}\left(\frac{b-a}{2}\right)^5, \qquad 
     \xi \in [a,b]\end{gathered}

Þar sem :math:`\xi` fæst úr
`skekkjumatinu fyrir brúunarmargliður <https://notendur.hi.is/~bsm/stae405/kafli03.html#id9>`_.

Samsett regla Simpsons
----------------------

Skiptum :math:`[a,b]` í :math:`n` jafnlöng bil og látum :math:`h` vera
helming hlutbillengdarinnar,

.. math:: h = \frac{(b-a)}{2n}.

Þá er

.. math::

   \begin{aligned}
     \int\limits_a^b f(x) \, dx
     \approx &
     \sum\limits_{k=1}^n
     \bigg(
       \frac{h}{3}
       \Big(
         f(x_{2k-2}) + 4f(x_{2k-1}) + f(x_{2k})
       \Big)
     \bigg) \\
     = &
     \frac{h}{3}
     \Big( 
       f(a) + 4f(a+h) + 2f(a+2h)+ 4f(a+3h) + 2f(a+4h) \\
       &+ \cdots + 2f(a+(2n-2)h) + 4f(a+(2n-1)h) + f(b)
     \Big)\end{aligned}

Ef við beitum skekkjumatinu á sérhvert bilanna þá fáum við

.. math:: \frac{-f^{(4)}(\xi_i)}{90}h^5

sem skekkju með :math:`\xi_i \in [x_i, x_i+1]`. Heildarskekkjan verður

.. math::

   -\sum_{i=1}^n \frac{f^{(4)}(\xi_i)}{90}h^5 
     = \frac{-h^5}{90}\cdot \sum_{i=1}^n f^{(4)}(\xi_i)

Nú gefur meðalgildisreglan að til er :math:`\xi \in [a,b]` þannig að

.. math:: f^{(4)}(\xi) = \frac{1}{n} \sum_{i=1}^n f^{(4)}(\xi_i)

Nú er :math:`nh = \frac{(b-a)}{2}` þar með er skekkjan:

.. math::

   \frac{-h^5}{90}\cdot nf^{(4)}(\xi) 
     = \frac{-(b-a)}{180}f^{(4)}(\xi)\cdot h^4

Ef við táknum útkomuna úr samsettu Simpsonsreglunni fyrir
:math:`h=\frac{b-a}{2n}` með :math:`S(h)` þá fæst að til er
:math:`\xi \in [a,b]` þannig að

.. math:: \int_a^b f(x)\,dx = S(h) - \frac{(b-a)}{180}f^{(4)}(\xi)h^4

Romberg-útgiskun
~~~~~~~~~~~~~~~~

Á sama hátt og við gátum bætt nálgun okkar á afleiðu falls með að nota
`Richardson útgiskun <https://notendur.hi.is/~bsm/stae405/kafli04.html#richardson-utgiskun>`_ 
getum við bætt nálgun á heildi.

Aðferðin virkar í aðalatriðum eins fyrir heildi og afleiður, en til að
fá sem bestar upplýsingar um samleitni hennar skulum við leiða út
formúluna fyrir trapisureglunni aftur.

Euler-Maclauren-formúlan
------------------------

Fyrir samfellt fall :math:`f : [0,1] \to \mathbb R` sem er
:math:`2n`-sinnum samfellt deildanlegt gildir Euler-Maclauren formúlan

.. math::

   \begin{aligned}
     \int\limits_0^1 f(t) \, dt 
     =&  \frac{1}{2}\left( f(0) + f(1) \right) 
     + \sum\limits_{k=1}^{n-1} A_{2k}
     \left( f^{(2k-1)}(0) - f^{(2k-1)}(1)\right) \\
     & - A_{2n}f^{(2n)}(\xi), \qquad \xi \in [0,1]\end{aligned}

Hér eru stuðlarnir :math:`A_k` þannig að :math:`k!A_k` verði
Bernoulli-talan númer :math:`k`. Þessar tölur eru stuðlar í veldaröðinni

.. math:: \frac{x}{e^x -1} = \sum\limits_{k=0}^{\infty}A_kx^k

.. note::
	Það þarf að hafa töluvert fyrir því að sanna þessa formúlu og því sleppum
	við því hér.

Afleiðing af Euler-Maclaurin-formúlunni
---------------------------------------

Látum nú :math:`f : [a,b] \to \mathbb R` vera :math:`2n`-sinnum samfellt
deildanlegt fall. Ef við búum til skiptingu
:math:`a= x_0 < x_1 < \cdots <
x_n = b` með jöfn hlutbil :math:`h = x_{i+1} - x_i` og beitum síðan
Euler-Maclauren formúlunni á :math:`g(t) = f(x_i + ht)` fæst

.. math::

   \begin{aligned}
   \int_{x_i}^{x_{i+1}} f(x)\,dx 
   = & h\int_0^1 \underbrace{f(x_i + ht)}_{g(t)}\,dt \\
   = & h \left( \frac{1}{2}f(x_i) + \frac{1}{2}f(x_{i+1})\right) \\
   & +    \sum_{k=1}^{n-1}A_{2k}h^{2k}\left( f^{(2k-1)}(x_i) -
   f^{(2k-1)}(x_{i+1}) \right) - A_{2n}h^{2n+1}f^{(2n)}(\xi_i), \end{aligned}

þar sem :math:`\xi_i \in [x_i, x_{i+1}]`.

Nú innleiðum við

.. math::

   \begin{aligned}
   T(h) 
   &:= \sum_{i=0}^{n-1}
   h \left( \frac{1}{2} f(x_i) + 
   \frac{1}{2}f(x_{i+1}) \right)\\
   &= h\left( \frac{1}{2}f(a) + f(a+h) 
   + \cdots + f(a+(n-1)h) + \frac{1}{2}f(a+nh)\right)\end{aligned}

og fáum síðan:

.. math::

   \begin{aligned}
     \int\limits_a^b f(x)\, dx 
     = & T(h) + \sum_{k=1}^{n-1}A_{2k}h^{2k} 
     \left( f^{(2k-1)}(a) - f^{(2k-1)}(b) \right) \\
     & - A_{2n}h^{2n+1} \sum_{i=0}^{n-1} f^{(2n)}(\xi_i)\end{aligned}

Nú gefur milligildissetningin að til er :math:`\xi \in [a,b]` þannig að

.. math::

   \frac{1}{n} \sum\limits_{k=0}^{n-1} f^{(2n)}(\xi_i)
     = f^{(2n)}(\xi)

Notum okkur nú að :math:`nh = b-a` og fáum að

.. math::

   \begin{aligned}
     \int\limits_a^b f(x) \, dx 
     = & T(h) + \sum_{k=1}^{n-1}A_{2k}h^{2k} 
     \left( f^{(2k-1)}(a) - f^{(2k-1)}(b) \right) \\
     & - A_{2n} h^{2n}(b-a)f^{(2n)}(\xi).\end{aligned}

Niðurstaðan er að samsetta trapisureglan er

.. math::

   \int\limits_a^b f(x) \, dx 
     = T(h) + c_2h^2 + c_4h^4 + \cdots + c_{2m-2}h^{2m-2} 
     + c_{2n}h^{2m}f^{(2m)}(\xi)

Ítrekun á samsettu trapisureglunni með helmingun
------------------------------------------------

Hugsum okkur nú að við viljum reikna út :math:`T(h_j)` fyrir
:math:`h_j =(b-a)/
2^j`, :math:`j = 1,2,\ldots` og að við viljum nýta öll fallgildi í
:math:`T(h_{j-1})` til að reikna út :math:`T(h_j)`. Rakningarformúlan er

.. math:: T(h_j) = \frac{1}{2} T(h_{j-1}) + h_j \sum_{k=1}^{2^{j-1}} f(a+(2k-1)h_j)

Athugið að hér er bilinu :math:`[a,b]` skipt í :math:`2^j` hlutbil.

.. warning::
	Þetta er gott að nota ef forrita á Romberg-heildun til þess að 
	spara útreikninga þegar fyrsti dálkurinn er reiknaður. 
	Það er hins vegar ekki nauðsynlegt að nota þetta og þetta tengist ekki
	beint Romberg aðferðinni.

Reikniritið fyrir Romberg-heildun
---------------------------------

Romberg-heildun er hugsuð nákvæmlega eins og Richardson-útgiskunin: Við
reiknum út línu fyrir línu í töflunni:

.. math::

   \begin{array}{cccccc}
       i\\
       1 & R(1,1)\\
       2 & R(2,1) & R(2,2)\\
       3 & R(3,1) & R(3,2) & R(3,3)\\
       4 & R(4,1) & R(4,2) & R(4,3) & R(4,4)\\
       \vdots & \vdots & \vdots & \vdots & \vdots & \ddots
     \end{array}

þar sem

.. math::

   \begin{aligned}
     &R(i,1) = T(h_i) \qquad i = 1,2,\ldots\\
     &R(i,j) = \frac{4^{j-1} R(i,j-1) - R(i-1,j-1)}{4^{j-1} - 1}.\end{aligned}

Með þessu fæst
:math:`\int\limits_a^b f(x)\, dx = R(k,k) + O(h_k^{2k})`, þar sem
:math:`k` er síðasta línan sem við reiknum í töflunni að ofan.

Skekkjumat í Romberg heildun
----------------------------

Skekkjumatið er hægt að finna með nákvæmlega sama hætti í fyrir
Richardson útgiskuna. Þ.e. við getum notað síðustu viðbót sem eftirámat
fyrir skekkjuna, þetta mat er

.. math:: e \approx \frac{1}{4^{j-1}-1}\left( R(i,j-1) - R(i-1,j-1)\right)

þegar þessi stærð er komin niður fyrir fyrirfram gefin skekkjumörk er
hætt. 

Einnig er hægt að nota

.. math:: e \approx \frac{1}{2^{j-1}}\left( R(i,j-1) - R(i-1,j-1)\right),

sem gefur heldur varfærnislegra mat.

.. note:: 
    Athugið að það er ekki nauðsynlegt að hafa :math:`h_1` sem allt bilið
    :math:`[a,b]`, það er ekkert sem kemur í veg fyrir það að við byrjum
    með :math:`h_1 = \frac{b-a}{m}`, og helmingum svo;
    :math:`h_2 = \frac{b-a}{2m}`, :math:`h_3 = \frac{b-a}{4m}`,
    :math:`\ldots`.
    Þannig að almennt þá er :math:`h_j=\frac{b-a}{2^{j-1}m}`.

