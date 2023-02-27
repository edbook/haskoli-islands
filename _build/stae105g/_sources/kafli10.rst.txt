Veldaraðir
===========

.. admonition:: Nauðsynleg undirstaða
  :class: athugasemd

	- Föll

	- Markgildi

	- Runur

------

.. epigraph::

  *"When the memory of the fear and the darkness troubles you, this will bring you aid."*

  \– Arwen Evenstar, The Return of the King

Veldaraðir og föll
-------------------

Skilgreining: Veldaröð
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Röð á forminu

  .. math:: \sum_{n=0}^\infty c_n x^n = c_0 + c_1 x + c_2 x^2 + \dots

  nefnist *veldaröð með miðju í* :math:`x=0`. Röð á forminu

  .. math:: \sum_{n=0}^\infty c_n (x-a)^n = c_0 + c_1(x-a) + c_2(x-a)^2+\dots

  nefnist *veldaröð með miðju í* :math:`x=a`.

Setning: Samleitni veldaraða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Látum röðina :math:`\sum_{n=0}^\infty c_n(x-a)^n` vera gefna veldaröð. Hún uppfyllir nákvæmlega
  eitt af eftirfarandi eiginleikum:

    #. Röðin er samleitin fyrir :math:`x=a` og ósamleiti fyrir öll :math:`x \neq a`.

    #. Röðin er samleitin fyrir allar rauntölur :math:`x`.

    #. Til er rauntala :math:`R>0` þannig að röðin er samleitin ef :math:`|x-a|<R` og ósamleitin ef :math:`|x-a|>R`. Þegar :math:`|x-a|=R` getur röðin verið annað hvort samleitin eða ósamleitin.

Skilgreining: Samleitnibil og samleitnigeisli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Látum röðina :math:`\sum_{n=0}^\infty c_n(x-a)^n` vera gefna veldaröð. Rauntalnabilið
  sem röðin er samleitin á nefnist *samleitnibil*. Ef til er rauntala :math:`R>0`
  þannig að röðin sé samleitin fyrir :math:`|x-a|<R` og ósamleitin fyrir :math:`|x-a|>R`,
  þá er :math:`R` *samleitnigeilsi* raðarinnar. Ef röðin er aðeins samleitin í :math:`x=a`
  segjum við að samleitnigeisli raðarinnar sé :math:`R=0`. Ef röðin er samleitin fyrir allar rauntölur
  :math:`x` segjum við að samleitnigeislinn sé :math:`R = \infty`.

Dæmi: Samleitnibil og samleitnigeisli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Finnum samleitnigeisla raðarinnar

  .. math:: \sum_{n=0}^\infty \frac{x^m}{n!}.

.. admonition:: Lausn
  :class: daemi, dropdown

  Til að athuga hvort röðin sé samleitin notum við kvótaprófið. Fáum

  .. math::
    \begin{align}
      \rho &= \lim_{n \rightarrow \infty} \left| \frac{\frac{x^{n+1}}{(n+1)!}}{\frac{x^n}{n!}} \right|\\
      &= \lim_{n \rightarrow \infty} \left| \frac{x^{n+1}}{(n+1)!}\cdot \frac{n!}{x^n} \right|\\
      &= \lim_{n \rightarrow \infty} \left| \frac{x^{n+1}}{(n+1)\cdot n!} \cdot \frac{n!}{x^n} \right|\\
      &= \lim_{n \rightarrow \infty} \left| \frac{x}{n+1} \right|\\
      &= |x| \lim_{n \rightarrow \infty} \frac{1}{n+1}\\
      &= 0 < 1
    \end{align}

  fyrir öll gildi á :math:`x`. Þar með er röðin samleitin fyrir allar rauntölur :math:`x`.
  Samleitnibilið er því :math:`]–\infty, \infty[` og samleitnigeislinn :math:`R=\infty`.

Föll sem veldaraðir
~~~~~~~~~~~~~~~~~~~~

Mörgum föllum má lýsa með veldaröðum. Skoðum geómetrísku veldaröðina

.. math:: 1 + x + x^2 + x^3 + \dots = \sum_{n=0}^\infty x^n.

Munum að geómetrísk röð

.. math:: a + ar + ar^2 + ar^3 + \dots

er samleitin ef og aðeins ef :math:`|r|<1`. Í því tilfelli er það samleitið að
:math:`\frac{a}{1-r}`. Þar af leiðandi, ef :math:`|x|<1`, er röðin samleitin að
:math:`\frac{1}{1-x}` og við ritum að

.. math:: 1 + x + x^2 + x^3 + \dots = \frac{1}{1-x} \text{ fyrir } |x|<1.

Þar af leiðandi má segja að hægt sé að lýsa fallinu :math:`f(x)=\frac{1}{1-x}`
með veldaröðinni

.. math:: 1 + x + x^2 + x^3 + \dots \text{ þegar } |x|<1.

------

Eiginleikar veldaraða
----------------------

Setning: Sameining veldaraða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Gerum ráð fyrir að veldaraðirnar :math:`\sum_{n=0}^\infty c_n x^n` og :math:`\sum_{n=0}^\infty d_n x^n`
  séu hvor um sig samleitnar að föllunum :math:`f` og :math:`g` á sameiginlegu bili :math:`I`.

    #. Veldaröðin :math:`\sum_{n=0}^\infty (c_n \pm d_n) x^n` er samleitin að fallinu :math:`f+g` á :math:`I`.

    #. Fyrir hvaða heiltölu :math:`m>0` sem er og rauntölu :math:`b` er veldaröðin :math:`\sum_{n=0}^\infty b x^m c_n x^n` samleitin að :math:`bx^m f(x)` á :math:`I`.

    #. Fyrir hvaða heiltölu :math:`m>0` sem er og rauntölu :math:`b` er veldaröðin :math:`\sum_{n=0}^\infty c_n (bx^m)^n` samleitin að :math:`f(bx^m)` á :math:`I`.

Dæmi: Samleitni veldaraðar
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Gerum ráð fyrir að :math:`\sum_{n=0}^\infty a_n x^n` sé veldaröð með samleitnibilið :math:`]-1,1[`
  og að :math:`\sum_{n=0}^\infty b_n x^n` sé veldaröð með samleitnibilið :math:`]-2,2[`. Finnum
  samleitnibil veldaraðarinnar :math:`\sum_{n=0}^\infty (a_n+b_n) x^n`.

.. admonition:: Lausn
  :class: daemi, dropdown

  Þar sem :math:`]-1,1[` er sameiginleg samleitnibil beggja raða þá er :math:`\sum_{n=0}^\infty (a_n+b_n) x^n`
  samleitin á því bili.

Dæmi: Sameining veldaraða
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Notum að veldaröð fallsins :math:`g(x)=\frac{1}{1-x}` sé :math:`\sum_{n=0}^\infty x^n`
  til þess að ákvarða veldaröð fallsins

  .. math:: f(x) = \frac{3x}{1+x^2}

  auk þess að finna samleitnibil þess.

.. admonition:: Lausn
  :class: daemi, dropdown

  Byrjum á því að rita :math:`f(x)` sem

  .. math:: f(x) = 3x\left( \frac{1}{1-(-x^2)} \right).

  Notum nú veldaröð fallsin :math:`g(x)=\frac{1}{1-x}` og eiginleika veldaraða til þess að
  setja fallið :math:`f` fram með

  .. math:: \sum_{n=0}^\infty 3x (-x^2)^n = \sum_{n=0}^\infty 3(-1)^n x^{2n+1}.

  Þar sem samleitnibil veldaraðar :math:`\frac{1}{1-x}` er :math:`]-1,1[` er samleitnibil
  veldaraðar fallsins :math:`f` mengi þeirra rauntalna :math:`x` þannig að :math:`|x^2|<1`.
  Þ.a.l. er það einnig :math:`]-1,1[`.

Dæmi: Finna fall veldaraðar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Finnum fallið :math:`f` sem lýsir veldaröðinni :math:`\sum_{n=0}^\infty 2^n x^n`
  auk þess að ákvarða samleitnibil raðarinnar.

.. admonition:: Dæmi
  :class: daemi, dropdown

  Skrifum röðina sem

  .. math:: \sum_{n=0}^\infty 2^n x^n = \sum_{n=0}^\infty (2x)^n.

  Við sjáum að þetta er veldaröðin fyrir

  .. math:: f(x) = \frac{1}{1-2x}.

  Þar sem þetta er geómetrísk röð er hún samleitin ef og aðeins ef :math:`|2x|<1`.
  Þar með er samleitnibil raðarinnar :math:`]-\tfrac{1}{2}, \tfrac{1}{2}[`.

Setning: Margföldun veldaraða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Gerum ráð fyrir að veldaraðirnar :math:`\sum_{n=0}^\infty c_n x^n` og :math:`\sum_{n=0}^\infty d_n x^n`
  séu hvor um sig samleitnar að föllunum :math:`f` og :math:`g` á sameiginlegu bili :math:`I`. Látum

  .. math:: e_n = c_0 + c_1 d_{n-1} + c_2 d_{n-2} + \dots + c_{n-1}d_1 + c_n d_0 = \sum_{k=0}^\infty c_k d_{n-k}.

  Þá er

  .. math:: \left( \sum_{n=0}^\infty c_n x^n \right) \cdot \left( \sum_{n=0}^\infty d_n x^n \right) = \sum_{n=1}^\infty e_n x^n

  og

  .. math:: \sum_{n=0}^\infty e_n x^n \text{ er samleitin að } f(x)\cdot g(x) \text{ á } I.

  Röðin :math:`\sum_{n=0}^\infty e_n x^n` er þekkt sem *Cauchy margfeldi* raðanna
  :math:`\sum_{n=0}^\infty c_n x^n`  og :math:`\sum_{n=0}^\infty d_n x^n`.

Dæmi: Margföldun veldaraða
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Finnum Cauchy margfeldi raðanna :math:`\sum_{n=0}^\infty x^n` og :math:`\sum_{n=0}^\infty (x^2)^n`

  fyrir :math:`|x|<1` á bilinu :math:`]-1,1[`.

.. admonition:: Lausn
  :class: daemi, dropdown

  Þar sem röðina :math:`\sum_{n=0}^\infty x^n` má setja fram með fallinu :math:`\frac{1}{1-x}`
  og röðina :math:`\sum_{n=0}^\infty (x^2)^n` má setja fram með fallinu :math:`\frac{1}{1-x^2}`
  þá er margfeldi þeirra er fallið

  .. math:: g(x) = \frac{1}{1-x} \cdot \frac{1}{1-x^2} = \frac{1}{(1-x)(1-x^2)}.

  Veldaröð fallsins :math:`g(x)` er

  .. math:: 1 + x + 2x^2 + 2x^3 + 3x^4 + 3x^5 + \dots

  sem er samleitin bilinu :math:`]-1,1[`.

Setning: Afleiður og stofnföll veldaraða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Gerum ráð fyrir að röðin :math:`\sum_{n=0}^\infty c_n(x-a)^n` sé samleitin á bilinu
  :math:`]a-R,a+R[` fyrir eitthvað :math:`R>0`. Látum :math:`f` vera fallið sem
  lýsir veldaröðinni

  .. math::
    \begin{aligned}
      f(x) &= \sum_{n=0}^\infty c_n(x-a)^n\\
      &= c_0 + c_1(x-a) + c_2(x-1)^2 + c_3(x-a)^3 + \dots
    \end{aligned}

  fyrir :math:`|x-a|<R`. Þá er :math:`f` diffranlegt á bilinu :math:`]a-R,a+R[`
  og við getum fundið afleiðu :math:`f` með því að diffra röðina lið fyrir lið. Þá fæst

  .. math::
    \begin{aligned}
      f'(x) &= \sum_{n=0}^\infty nc_n(x-a)^{n-1}\\
      &= c_1 + 2c_2(x-a) + 2c_3(x-1)^2  + \dots
    \end{aligned}

  fyrir :math:`|x-a|<R`. Við getum einnig fundið stofnfall :math:`f(x)` með því
  að heilda röðina lið fyrir lið. Við það fæst röð sem er samleitin á
  bilinu :math:`]a-R,a+R[` og við höfum að

  .. math::
    \begin{aligned}
      F(x) &=  \int f(x) dx\\
      &=C + \sum_{n=0}^\infty c_n \frac{(x-a)^{n+1}}{n+1}\\
      &= C + c_0(x-a) + c_1 \frac{(x-a)^2}{2} + c_2 \frac{(x-a)^3}{3} + \dots
    \end{aligned}

  fyrir :math:`|x-a|<R`.

Dæmi: Afleiða veldaraðar
~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Notfærum okkur að

  .. math::
    \begin{aligned}
      f(x) &= \frac{1}{1-x}\\
      &= \sum_{n=0}^\infty x^n\\
      &= 1 + x + x^2 + x^3 + \dots
    \end{aligned}

  fyrir :math:`|x|<1` til að finna veldaröðina sem lýsir fallinu

  .. math:: g(x) = \frac{1}{(1-x)^2}

  á bilinu :math:`]-1,1[`. Ákvarðið svo að lokum hvort hún sé samleitin í
  endapunktum bilsins.

.. admonition:: Lausn
  :class: daemi, dropdown

  Þar sem :math:`f'(x) = \frac{1}{(1-x)^2} = g(x)` getum við fundið veldaröð
  fallsins :math:`g` með því að diffra veldaröð fallsins :math:`f` lið fyrir lið.
  Þá fæst

  .. math::
    \begin{aligned}
      g(x) &= \frac{1}{(1-x)^2}\\
      &= \frac{d}{dx} \left( \frac{1}{1-x} \right)\\
      &= \sum_{n=0}^\infty \frac{d}{dx}(x^n)\\
      &= \frac{d}{dx}(1+x+x^2+x^3+\dots)\\
      &= 0 + 1 + 2x + 3x^2 + 4x^3 + \dots\\
      &= \sum_{n=0}^\infty (n+1)x^n
    \end{aligned}

  fyrir :math:`|x|<1`. Að diffra röðina lið fyrir lið segir ekkert til um hegðun
  raðarinnar i endapunktum bilsins. Við getum skoðað hegðunina þar með því að nota
  sundurleitniprófið og séð þannig að röðin er sundurleitin í :math:`x = \pm 1`.

Dæmi: Stofnfall veldaraðar
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Finnum veldaröð fallsins

  .. math:: f(x) = \ln(1+x)

  með því að heilda veldaröð fallsins :math:`f'`. Finnum auk þess samleitnibil raðarinnar.

.. admonition:: Lausn
  :class: daemi, dropdown

  Fyrir fallið :math:`f(x) = \ln(1+x)` gildir að :math:`f'(x)=\frac{1}{1+x}`. Við
  vitum að

  .. math::
    \begin{aligned}
      \frac{1}{1+x}&=\frac{1}{1-(-x)}\\
      &= \sum_{n=0}^\infty (-x)^n\\
      &= 1 - x + x^2 - x^3 + \dots
    \end{aligned}

  fyrir :math:`|x|<1`. Til að finna veldaröð fallsins :math:`f(x)=\ln(1+x)` getum
  við heildað röðina lið fyrir lið.

  .. math::
    \begin{aligned}
      F(x) &= \int f(x) dx\\
      &= \int (1 - x + x^2 - x^3 + \dots) dx\\
      &= C + x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \dots
    \end{aligned}

  Þar sem :math:`f(x)=\ln(1+x)` er stofnfall fallsins :math:`\frac{1}{1+x}` þá er aðeins
  eftir að ákvarða fastann :math:`C`. Þar sem :math:`\ln(1+0)=0` höfum við að :math:`C=0`.
  Þar me ðfæst að veldaröð fallsins :math:`f(x)=\ln(1+x)` sé

  .. math::
    \begin{aligned}
      \ln(x) &= x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \dots\\
      &= \sum_{n=1}^\infty (-1)^{n+1} \frac{x^n}{n}
    \end{aligned}

  fyrir :math:`|x|<1`. Að heilda veldaröð lið fyrir lið segir ekkert um hegðun raðarinnar í
  endapunktun bilsins. Með niðurstöðum úr kafla 9 um runur og raðir getum við séð að
  röðin er samleitin í :math:`x=1` en ósamleitin í :math:`x=-1`. Svo samleitnibil raðarinnar
  er :math:`]-1,1]`.

Setning: Veldaraðir eru ótvírætt ákvarðaðar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Látum :math:`\sum_{n=0}^\infty c_n(x-a)^n` og :math:`\sum_{n=0}^\infty d_n(x-a)^n`
  vera tvær, samleitnar veldaraðir sem uppfylla að

  .. math:: \sum_{n=0}^\infty c_n(x-a)^n = \sum_{n=0}^\infty d_n(x-a)^n

  fyrir öll :math:`x` á opnu bili sem inniheldur :math:`a`. Þá er :math:`c_n = d_n`
  fyrir öll :math:`n \geq 0`.

------

Taylor- og Maclaurin-raðir
---------------------------

Skilgreining: Taylor- og Maclaurin-röð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Ef :math:`f` er óendanlega oft diffranlegt í :math:`x=a` þá er *Taylor-röð* fallsins
  :math:`f` í :math:`a` röðin

  .. math:: \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!} = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \dots + \frac{f^{(n)}(a)}{n!}(x-a)^n + \dots .

  Taylor-röð fallsins :math:`f` í :math:`x=0` er kölluð *Maclaurin-röð* fallsins :math:`f`.

Setning: Taylor-raðir eru ótvírætt ákvarðaðar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Ef fallið :math:`f` á sér veldaröð með miðju í :math:`a` sem er samleitin að :math:`f` á
  opnu bili sem inniheldur :math:`a` þá er sú röð Taylor-röð fallsins :math:`f` með miðju í :math:`a`.

Skilgreining: Taylor-margliða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Ef :math:`f` er :math:`n`-diffranlegt í :math:`x=a` þá er :math:`n`-ta *Taylor-margliða*
  fallsins :math:`f` í :math:`a`

  .. math:: p_n(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \dots + \frac{f^{(n)}(a)}{n!}(x-a)^n.

  Þá er :math:`n`-ta Taylor-margliða fallsins :math:`f` í :math:`x=0` kölluð :math:`n`-ta
  *Maclaurin-margliða* fallsins :math:`f`.

Dæmi: Að ákvarða Taylor-margliðu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Finnum :math:`p_0`, :math:`p_1`, :math:`p_2` og :math:`p_3` fyrir :math:`f(x)=\ln(x)`
  í :math:`x=1`.

.. admonition:: Lausn
  :class: daemi, dropdown

  Til að finna þessar Taylor-margliður þurfum við að finna fyrstu þrjár afleiður :math:`f` og
  meta þær í :math:`x=1`. Fáum

  .. math::
    \begin{aligned}
      f(x) &= \ln(x) & f(1) &= 0\\
      f'(x) &= \frac{1}{x} & f'(1) &= 1\\
      f''(x) &= -\frac{1}{x^2} & f''(1) &= -1\\
      f'''(x) &= \frac{2}{x^3} & f'''(1) &= 2.
    \end{aligned}

  Fáum því að

  .. math::
    \begin{aligned}
      p_0(x) &= f(1) =0\\
      p_1(x) &= f(1) + f'(1)(x-1) = x-1\\
      p_2(x)&= f(1) + f'(1)(x-1) + \frac{f''(1)}{2}(x-1)^2 = (x-1) - \tfrac{1}{2}(x-1)^2\\
      p_3(x)&= f(1) + f'(1)(x-1) + \frac{f''(1)}{2}(x-1)^2 + \frac{f'''(1)}{3!}(x-1)^3\\
      &= (x-1) - \tfrac{1}{2}(x-1)^2 + \tfrac{1}{3}(x-1)^3\\
    \end{aligned}

  .. figure:: ./myndir/kafli10/PMA_taylor_lnx.png
    :align: center
    :width: 75%

  Við sjáum af myndinni hér að ofan hversu vel nálgununum tekst að nálga :math:`\ln(x)`.

Setning: Setning Taylors um skekkju
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: Setning

  Látum :math:`f` vera fall sem er :math:`n+1` sinnum diffranlegt á bilinu :math:`I`
  sem inniheldur rauntöluna :math:`a`. Látum :math:`p_n` vera :math:`n`-tu Taylor-margliðu
  fallsins :math:`f` í :math:`a` og látum

  .. math:: R_n(x) = f(x) - p_n(x)

  vera :math:`n`-tu skekkjuna. Þá gildir að fyrir sérhvert :math:`x` á bilinu :math:`I`
  er til rauntala :math:`c` milli :math:`a` og :math:`x` þannig að

  .. math:: R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-1)^{n+1}.

  Ef til er rauntala :math:`M` þannig að :math:`\left|f^{(n+1)}(x) \right| \leq M`
  fyrir öll :math:`x \in I` þá gildir að

  .. math:: |R_n(x)| \leq \frac{M}{(n+1)!}|x-a|^{n+1}

  fyrir öll :math:`x \in I`.

Dæmi: Línulegar- og ferningsnálganir til að meta fallgildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Gefið er fallið :math:`f(x) = \sqrt[3]{x}`.

    a) Finnið fyrstu og aðra Taylor-margliðu fallsins í :math:`x=8`.

    b) Notið margliðurnar til þess að nálga :math:`\sqrt[3]{11}`.

    c) Notið setningu Taylors um skekkju til að finna efra marg á skekkjunni.

.. admonition:: Lausn
  :class: daemi, dropdown

    a) Lausn:
			Við þurfum að byrja á því að finna fyrstu og aðra afleiðu fallsins
			:math:`f(x) = \sqrt[3]{x}` og meta þær í :math:`x=8`. Fáum:

			.. math::
				\begin{aligned}
						f(x) &= \sqrt[3]{x} & f(8) &= 2\\
						f'(x) &= \frac{1}{3x^{2/3}} & f'(8) &= \frac{1}{12}\\
						f''(x) &= \frac{-2}{9x^{5/3}} & f''(8) &= -\frac{1}{144}\\
				\end{aligned}

			Þar með fæst að fyrsta og önnur Taylor-margliða fallsins séu

			.. math::
				\begin{aligned}
						p_1(x) &= f(8)+f'(8)(x-8)\\
						&= 2 + \tfrac{1}{12}(x-8)\\
						p_2 &= f(8)+f'(8)(x-8) + \frac{f''(8)}{2!}(x-8)^2\\
						&= 2 + \tfrac{1}{12}(x-8) - \tfrac{1}{288}(x-8)^2.
				\end{aligned}

    b) Lausn:
			Ef við notum fyrsta stigs Taylor-margliðuna fæst

			.. math:: \sqrt[3]{11} \approx p_1(11) = 2 + \tfrac{1}{12}(11-8)=2,25.

			Ef við notum annars stigs Taylor-margliðuna fæst

			.. math:: \sqrt[3]{11} \approx p_2(11) = 2 + \tfrac{1}{12}(11-8) - \tfrac{1}{288}(11-8)^2 = 2,21875.

    c) Lausn:
			Þar sem Taylor-raðir eru ótvírætt ákvarðaðar er til tala :math:`c` á bilinu
			:math:`]8,11[` þannig að skekkjan við að námunda :math:`\sqrt[3]{11}` með
			fyrsta stigs Taylor-margliðu uppfylli að

			.. math:: R_1(11) = \frac{f''(c)}{2!}(11-8)^2.

			Við vitum ekki hvert nákvæmt gildi :math:`c` er en við getum fundið efra mark á
			skekkjuna :math:`R_1(11)` með því að ákvarða hámarksgildi :math:`f''` á bilinu
			:math:`]8,11[`. Þar sem :math:`f''(x) = - \frac{2}{9x^{5/2}}` fæst að stærsta
			gildið sem :math:`|f''(x)|` tekur á bilinu sé í punktinum :math:`x=8`. Þar sem
			:math:`f''(8)=-\frac{1}{144}` fæst að

			.. math:: |R_1(11)| \leq \frac{1}{144 \cdot 2!} (11-8)^2 = 0,03125.

			Á svipaðan hátt getum við metið skekkjuna :math:`R_2(11) = \frac{f'''(c)}{3!}(11-8)^3`.

			Þar sem :math:`f'''(x) = \frac{10}{27x^{8/3}}` fæst að hámarksgildi :math:`f'''` á
			bilinu :math:`]8,11[` sé :math:`f'''(8)\approx 0,0014468` og þar með fæst

			.. math:: |R_2(11)| \leq \frac{0,0011468}{3!}(11-8)^3 \approx 0,0065104.

Dæmi: Að finna Taylor-röð falls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Finnum Taylor-röð fallsins :math:`f(x)=\frac{1}{x}` í :math:`x=1` auk þess að ákvarða
  samleitnibil raðarinnar.

.. admonition:: Lausn
  :class: daemi, dropdown

  Finnum fyrstu fjórar afleiður fallsins og metum þær í punktinum :math:`x=1`.

  .. math::
    \begin{aligned}
      f(x) &= \frac{1}{x} & f(1) &= 1\\
      f'(x) &= -\frac{1}{x^2} & f'(1) &= -1\\
      f''(x) &= \frac{2}{x^3} & f''(1) &= 2!\\
      f'''(x) &= -\frac{3\cdot 2}{x^4} & f'''(1) &= 3!\\
      f^{(4)}(x) &= \frac{4\cdot 3 \cdot 2}{x^5} & f^{(4)}(1) &= 4!.
    \end{aligned}

  Ef við skoðum hvernig þetta þróast sést að :math:`f^{(n)}(1)=(-1)^n n!` fyrir öll
  :math:`n \geq 0`. Þar  með er Taylor-röðin fyrir :math:`f` í :math:`x=1` gefin með

  .. math:: \sum_{n=0}^\infty \frac{f^{(n)}(1)}{n!}(x-1)^n = \sum_{n=0}^\infty (-1)^n(x-1)^n.

  Til að finna samleitnibilið getum við notað kvótaprófið. Fáum að

  .. math:: \frac{|a_{n-1}|}{|a_n|} = \frac{\left|(-1)^{n+1}(x-1)^{n+1}\right|}{\left| (-1)^n(x-1)^n \right|} = |x-1|.

  Þar með er röðin samleitin ef :math:`|x-1|<1`, þ.e. röðin er samleitin ef :math:`0<x<2`.
  Næst athugum við endapunktana. Við sjáum að

  .. math:: \sum_{n=0}^\infty (-1)^n(2-1)^n = \sum_{n=0}^\infty (-1)^n

  er ósamleitin skv. sundurleitniprófinu. Á svipaðan hátt má sjá að

  .. math:: \sum_{n=0}^\infty (-1)^n(0-1)^n = \sum_{n=0}^\infty (-1)^{2n} = \sum_{n=0}^\infty 1

  er ósamleitin. Þar með er samleitnibil raðarinnar :math:`]0,2[`.

Setning: Samleitni Taylor-raða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Gerum ráð fyrir að :math:`f` sé óendanlega oft diffranlegt á bili :math:`I` sem
  inniheldur :math:`a`. Þá er Taylor-röðin

  .. math:: \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(x-a)^n

  samleitin að :math:`f(x)`fyrir öll :math:`x\in I` ef og aðeins ef

  .. math:: \lim_{n \rightarrow \infty} R_n(x) = 0

  fyrir öll :math:`x \in I`.

-------

Hagnýting Taylor-raða
----------------------

Skilgreining: Tvíliðustuðullinn og tvíliðuröðin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Fyrir :math:`r,n\in \mathbb{N}_0` þar sem :math:`n \leq r` nefnist talan

  .. math:: \binom{r}{n} = \frac{r!}{n!(r-n)!}

  *tvíliðustuðullinn*. Ef :math:`k > n` er tvíliðustuðullinn skilgreindur sem 0.

  Hægt er að víkka tvíliðustuðulinn út þannig að hann gildi fyrir allar rauntölur :math:`r`
  og er hann þá skilgreindur sem

  .. math:: \binom{r}{n}=\frac{r(r-1)(r-2)\cdot \dots \cdot (r-n+1)}{n!}

  og nefnist þá *útvíkkaði tvíliðustuðullinn*.

  Maclaurin-röðin fyrir :math:`f(x)=(1+x)^r` þar sem :math:`r \in \mathbb{R}` nefnist
  *tvíliðuröð*. Hún er samleitin að :math:`f` ef :math:`|x|<1` og við skrifum að

  .. math::
    \begin{aligned}
      (1+x)^r &= \sum_{n=0}^\infty \binom{r}{n} x^n\\
      &= 1 + rx + \frac{r(r-1)}{2!}x^2 + \dots + \frac{r(r-1)\cdot \dots \cdot (r-n+1)}{n!} x^n + \dots
    \end{aligned}

  fyrir :math:`|x|<1`.


Dæmi: Að finna tvíliðuröð
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Finnum tvíliðuröð fallsins :math:`f(x)=\sqrt{1+x}`.


.. admonition:: Lausn
  :class: daemi, dropdown

  Athugum að :math:`\sqrt{1+x} = (1+x)^{1/2}` og því er :math:`r=1/2`. Fáum því að
  tvíliðuröð fallsins sé

  .. math:: \sum_{n=0}^\infty \binom{1/2}{n} x^n

  sem einnig mætti skrifa sem

  .. math:: 1 + \sum_{n=1}^\infty \frac{(-1)^{n+1}}{n!} \frac{1\cdot 3 \cdot 5 \cdot \dots \cdot (2n-3)}{2^n}x^n.

Ábending: Nokkur algeng föll og Maclaurin raðir þeirra
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Athugasemd
  :class: athugasemd

  .. list-table:: Nokkur algeng föll og Maclaurin raðir þeirra
    :widths: 20 15 15
    :header-rows: 1

    * - Fall
      - Maclaurin-röð
      - Samleitnibil
    * - :math:`f(x)=\tfrac{1}{1-x}`
      - :math:`\sum_{n=0}^\infty x^n`
      - :math:`-1 < x <1`
    * - :math:`f(x)=e^x`
      - :math:`\sum_{n=0}^\infty \frac{x^n}{n!}`
      - :math:`-\infty < x < \infty`
    * - :math:`f(x)=\sin(x)`
      - :math:`\sum_{n=0}^\infty (-1)^n \frac{x^{2n+1}}{(2n+1)!}`
      - :math:`-\infty < x < \infty`
    * - :math:`f(x)=\cos(x)`
      - :math:`\sum_{n=0}^\infty (-1)^n \frac{x^{2n}}{(2n)!}`
      - :math:`-\infty < x < \infty`
    * - :math:`f(x)=\ln(1+x)`
      - :math:`\sum_{n=0}^\infty (-1)^{n+1} \frac{x^n}{n}`
      - :math:`-1 < x < 1`
    * - :math:`f(x)=\tan^{-1}(x)`
      - :math:`\sum_{n=0}^\infty (-1)^{n} \frac{x^{2n+1}}{2n+1}`
      - :math:`-1 < x < 1`
    * - :math:`f(x)=(1+x)^r`
      - :math:`\sum_{n=0}^\infty \binom{r}{n} x^n`
      - :math:`-1 < x < 1`

Dæmi: Að finna eina Maclaurin-röð með annarri
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Notum einhverja þekkta Maclaurin-röð til að finna Maclaurin-röð fallsins
  :math:`f(x)=\cos(\sqrt{x})`.

.. admonition:: Lausn
  :class: daemi, dropdown

  Við vitum að :math:`\cos(x)` hefur Maclaurin-röðina :math:`\sum_{n=0}^\infty (-1)^n \frac{x^{2n}}{(2n)!}`.
  Við getum notað hana og stungið inn :math:`\sqrt{x}` í stað :math:`x` til að fá
  að Maclaurin-röð :math:`f` sé

  .. math::
    \begin{aligned}
      \sum_{n=0}^\infty \frac{(-1)^n (\sqrt{x})^{2n}}{(2n)!} &= \sum_{n=0}^\infty \frac{(-1)^n x^n}{(2n)!}\\
      &= 1 - \frac{x}{2!}+\frac{x^2}{4!}-\frac{x^3}{6!}+\frac{x^4}{8} \dots .
    \end{aligned}

  Þessi röð er samleitin að :math:`\cos(\sqrt{x})` fyrir öll :math:`x \geq 0`.

Dæmi: Að leysa diffurjöfnur með veldaröðum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Notum veldaraðir til að leysa upphafsgildisverkefnið

  .. math::
    \begin{cases}
      y' = y \\
      y(0) = 3
    \end{cases}

.. admonition:: Lausn
  :class: daemi, dropdown

  Gerum ráð fyrir að til sé lausn á forminu

  .. math:: y(x) = \sum_{n=0}^\infty c_n x^n = c_0 + c_1x + c_2 x`2 +c_3 x^3 + c_4 x^4 + \dots.

  Diffrum hvern lið fyrir sig og fáum að

  .. math:: y'(x) = \sum_{n=0}^\infty nc_n x^{n-1} = c_1 + 2c_2x + 3c_3 x^2 + 4c_4x^3 + \dots.

  Ef :math:`y` uppfyllir diffurjöfnuna gildir að

  .. math:: c_0 + c_1x + c_2 x^2 +c_3 x^3 + c_4 x^4 + \dots = c_1 + 2c_2x + 3c_3 x^2 + 4c_4x^3 + \dots.

  Við getum notfært okkur að veldaraðir eru ótvírætt ákvarðaðar og fengið að

  .. math::
    \begin{aligned}
      c_0 &= c_1\\
      c_1 &= 2c_2\\
      c_2 &= 3c_3\\
      c_3 &= 4c_4\\
      & \hspace{2mm} \vdots
    \end{aligned}

  Stingum nú upphafsgildinu :math:`y(0)=3` inn í :math:`y(x)=c_0 + c_1x + c_2 x`2 +c_3 x^3 + c_4 x^4 + \dots`
  og fáum að :math:`c_0=3`. Því fæst

  .. math::
    \begin{aligned}
      c_1 &= c_0 = 3 = \frac{3}{1!}\\
      c_2 &= \frac{c_1}{2} = \frac{3}{2} = \frac{3}{2!}\\
      c_3 &= \frac{c_2}{3} = \frac{3}{3\cdot 2} = \frac{3}{3!}\\
      c_4 &= \frac{c_3}{4} = \frac{3}{4\cdot 3\cdot 2} = \frac{3}{4!}\\
      & \hspace{2mm} \vdots
    \end{aligned}

  Þar með fæst að

  .. math::
    \begin{aligned}
    y &= 3\left(1 + \frac{1}{1!}x + \frac{1}{2!}x^2 + + \frac{1}{3!}x^3 + + \frac{1}{4!}x^4 + \dots \right)\\
    &= 3\sum_{n=0}^\infty \frac{x^n}{n!}\\
    &= 3e^x.
    \end{aligned}

Dæmi: Meta erfið heildi með veldaröðum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Reiknum óákveðna heildið

  .. math:: \int e^{-x^2} dx

  með því að nota veldaraðir. Notum það svo til að nálga ákveðna heildið

  .. math:: \int_0^\infty e^{-x^2} dx

  þannig að skekkjan sé innan við 0,01.

.. admonition:: Lausn
  :class: daemi, dropdown

  Maclaurin-röð :math:`e^{-x^2}` er gefin með

  .. math::
    \begin{aligned}
      e^{-x^2} &= \sum_{n=0}^\infty \frac{(-x^2)^n}{n!}\\
      &= 1 - x^2 + \frac{x^4}{2!} -\frac{x^6}{3!} + \dots + (-1)^n\frac{x^{2n}}{n!}\\
      &= \sum_{n=0}^\infty (-1)^n \frac{x^{2n}}{n!}.
    \end{aligned}

  Því fæst að

  .. math::
    \begin{aligned}
      \int e^{-x^2}dx &= \in \left(1 - x^2 + \frac{x^4}{2!} -\frac{x^6}{3!} + \dots + (-1)^n\frac{x^{2n}}{n!} \right) dx\\
      &= C + x - \frac{x^3}{3} + \frac{x^5}{5 \cdot 2!} - \frac{x^7}{7 \cdot 3!} + \dots + (-1)^n \frac{x^{2n+1}}{(2n+1)n!}\\
    \end{aligned}

  Notum þetta til að meta ákveðna heildið. Fáum

  .. math:: \int_0^1 e^{-x^2} dx = 1 - \frac{1}{3} + \frac{1}{10} - \frac{1}{42} + \frac{1}{216} - \dots.

  Summa fyrstu fjögurra liðanna er u.þ.b. 0,74. Ef við notum próf fyrir víxlmerkjaraðir fæst að þetta mat
  hefur skekkju sem er innan við :math:`\frac{1}{216} \approx 0,0046296 < 0,01`.

Dæmi: Maclaurin raðir til að nálga líkur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Gefið er að í stigafjöldi á prófi séu normaldreifður með meðaltalið :math:`\mu = 100` stig
  og staðalfrávikið :math:`\sigma = 50` stig. Reiknum líkurnar að gefinn nemandi fái
  á milli 100 og 200 stig á prófinu.

.. admonition:: Lausn
  :class: daemi, dropdown

  Notfærum okkur að ef :math:`X` er slembibreyta sem fylgir normaldreifingu má
  reikna líkurnar að :math:`a<X<b` með

  .. math:: \frac{1}{\sqrt{2\pi}}\int_{(a-\mu)/\sigma}^{(b-\mu)/\sigma} e^{-z^2/2} dz

  þar sem :math:`z=\frac{x-\mu}{\sigma}`. Notum Maclaurin-röð til að nálga útkomu fallsins.

  Þar sem :math:`\mu = 100` og :math:`\sigma = 50` auk þess sem að :math:`a=100` og
  :math:`b=200` fæst að heildið sem við viljum meta er

  .. math:: \frac{1}{\sqrt{2\pi}}\int_0^2 e^{-z^2/2}dz.

  Maclaurin-röð heildisstofnsins er gefin með

  .. math::
    \begin{aligned}
      e^{-x^2/2}&= \sum_{n=0}^\infty \frac{\left(-\tfrac{x^2}{2}\right)^n}{n!}\\
      &= 1 - \frac{x^2}{2^1 \cdot 1!} + \frac{x^4}{2^2 \cdot 2!}  - \frac{x^6}{2^3 \cdot 3!} + \dots + (-1)^n\frac{x^{2n}}{2^n \cdot n!}+\dots \\
      &= \sum_{n=0}^\infty (-1)^n \frac{x^{2n}}{2^n \cdot n!}.
    \end{aligned}

  Þar með fæst að

  .. math::
    \begin{aligned}
    \frac{1}{\sqrt{2\pi}} \int e^{-z^2/2} dz &= \frac{1}{\sqrt{2\pi}} \int \left( 1 - \tfrac{z^2}{2^1 \cdot 1!} + \tfrac{z^4}{2^2 \cdot 2!}  - \tfrac{z^6}{2^3 \cdot 3!} + \dots + (-1)^n\tfrac{z^{2n}}{2^n \cdot n!}+\dots \right) dz\\
    &= \frac{1}{\sqrt{2\pi}} \left(C + z - \tfrac{z^3}{3\cdot 2^1 \cdot 1!} + \tfrac{z^5}{5\cdot 2^2 \cdot 2!} - \tfrac{z^7}{7\cdot 2^3 \cdot 3!} + \dots + (-1)^n\tfrac{z^{2n+1}}{(2n+1)!2^n \cdot n!}+\dots\right)\\
    \frac{1}{\sqrt{2\pi}} \int_0^2 e^{-z^2/2} dz &= \frac{1}{\sqrt{2\pi}} \left( 2- \tfrac{8}{6}+\tfrac{32}{40}-\tfrac{128}{336} + \tfrac{512}{3456} - \tfrac{2^{11}}{11 \cdot 2^5 \cdot 5!}+ \dots \right).
    \end{aligned}

  Ef við notum fyrstu fimm liðina fáum við að líkurnar séu u.þ.b. 0,4922. Próf fyrir
  víxlmerkjaraðir gefur að skekkjan er innan við

  .. math:: \frac{1}{\sqrt{2\pi}}\frac{2^{13}}{13 \cdot 2^6 \cdot 6!} \approx 0,00546.
