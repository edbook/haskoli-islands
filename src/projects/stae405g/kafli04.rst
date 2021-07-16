Töluleg diffrun
===============

*Nanny's philosophy of life was to do what seemed like a good idea at the time, and do it as hard as possible. It had never let her down.*
-- Terry Pratchett, Maskerade

Inngangur
---------

.. index::
	töluleg diffrun
	töluleg heildun

Töluleg diffrun og heildun 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deildun og heildun eru meginaðgerðir stærðfræðigreiningarinnar.

Þess vegna er nauðsynlegt að geta nálgað

.. math::

   f'(a),f''(a),f'''(a),\dots \quad 
     \text{ og } \quad
     \int_a^b f(x)\, dx,

þar sem :math:`f` er fall sem skilgreint er á bili :math:`I` sem
inniheldur :math:`a` og :math:`b`.

Meginhugmynd í öllum nálgunaraðferðunum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`p` vera margliðu sem nálgar :math:`f`, og látum
:math:`r(x)=f(x)-p(x)` tákna skekkjuna í nálgun á :math:`f(x)` með
:math:`p(x)`. Þá er

.. math:: f'(x)=p'(x)+r'(x), \quad f''(x)=p''(x)+r''(x), \dots

og

.. math:: \int_a^b f(x)\, dx=\int_a^b p(x)\, dx+\int_a^b r(x)\, dx.

Nú þurfum við að gera tvennt:

#. Finna heppilegar nálgunarmargliður og reikna út

   .. math:: p'(a), \ p''(a),\dots, \qquad \int_a^b p(x)\, dx

#. Meta skekkjurnar

   .. math:: r'(a), \ r''(a), \dots \int_a^b r(x)\, dx

Byrjum á að leiða út nokkrar nálgunarformúlur með skekkjumati.

.. index::
	afleiður
	töluleg diffrun; frammismunur

Aðferðirnar
-----------

Látum :math:`f : I \to \mathbb R` vera fall á bili
:math:`I \subset \mathbb R` og :math:`a` vera punkt í :math:`I`. Afleiða
:math:`f` í punktinum :math:`a` er skilgreind með

.. math::

   f'(a) = \lim\limits_{h \to 0}
     \frac{f(a+h)-f(a)}{h}

ef markgildið er til. Við skrifum því oft

.. math:: f'(a) \approx \frac{f(a+h)-f(a)}{h}

Þessi nálgun er kölluð *frammismunur* því oftast hugsar maður sér að
:math:`h > 0` og þá er :math:`a+h` lítið skref áfram frá :math:`a`.

Við þurfum skekkjumat fyrir þessa formúlu ef við eigum að geta notað
hana.

Frammismunur
~~~~~~~~~~~~

Við fáum mat á skekkjuna í nálguninni með að skoða Taylor-margliðu
:math:`f` í :math:`a`. Samkvæmt setningu Taylors er til :math:`\xi` á
milli :math:`a` og :math:`a+h` þannig að

.. math:: f(a+h) = f(a) + f'(a)h + \frac{1}{2} f''(\xi)h^2.

Þá fæst að skekkjan í nálgun á :math:`f'(a)` með

.. math:: \frac{f(a+h)-f(a)}{h} = f[a,a+h]

er

.. math:: e = f'(a) - \frac{f(a+h)-f(a)}{h} = -\frac{1}{2} f''(\xi) h

Með öðrum orðum

.. math::

   \min_{t\in [0,h]} -\frac 12 f''(t)h \leq e \leq 
   \max_{t\in [0,h]} -\frac 12 f''(t)h.

Við sjáum því að :math:`e=O(h)` þegar :math:`h \to 0`.

.. index::
	töluleg diffrun; bakmismunur

Bakmismunur
~~~~~~~~~~~

Við getum sett :math:`a-h` í stað :math:`a+h` í skilgreininguna á
afleiðu. Þá fæst svokallaður *bakmismunur*

.. math:: f'(a) \approx \frac{f(a)-f(a-h)}{h}

og ljóst er að sama skekkjumat gengur fyrir þessa nálgun og fyrir nálgun
með frammismun.

.. index::
	töluleg diffrun; miðsettur mismunakvóti

Miðsettur mismunakvóti
~~~~~~~~~~~~~~~~~~~~~~

Lítum nú á þriðja stigs Taylor nálgun

.. math::

   \begin{aligned}
     f(a+h)&=f(a)+f'(a)h+\tfrac 12 f''(a)h^2+\tfrac 16 f'''(\alpha)h^3,\\
     f(a-h)&=f(a)-f'(a)h+\tfrac 12 f''(a)h^2-\tfrac 16 f'''(\beta)h^3,\end{aligned}

þar sem :math:`\alpha` er á milli :math:`a` og :math:`a+h` og
:math:`\beta` er á milli :math:`a` og :math:`a-h`.

Tökum nú mismuninn og fáum

.. math:: f(a+h)-f(a-h)=f'(a)\cdot 2h+\tfrac 16\big(f'''(\alpha)+f'''(\beta)\big)h^3

Ef :math:`f'''` er samfellt fall, þá gefur milligildissetningin okkur að
til er :math:`\xi` á milli :math:`\alpha` og :math:`\beta` þannig að
:math:`f'''(\xi)=\tfrac 12 (f'''(\alpha)+f'''(\beta))`

Niðurstaðan verður

.. math:: f'(a)=\dfrac{f(a+h)-f(a-h)}{2h}-\tfrac 16f'''(\xi)h^2.

Þannig að skekkjan er

.. math:: e = -\frac 16 f'''(\xi) h^2,

og jafnframt er :math:`e = O(h^2)` þegar :math:`h\to 0`.

.. ggb:: 2501721
    :width: 700
    :height: 400
    :img: ./afleida.png
    :imgwidth: 12cm

.. index::
	töluleg diffrun; miðsetttur mismunakvóti fyrir aðra afleiðu

Miðsettur mismunakvóti fyrir aðra afleiðu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við getum útfært þessa sömu hugmynd til þess að reikna út aðra afleiðu,
en þá byrjum við með fjórða stigs Taylor-nálgun

.. math::

   \begin{aligned}
     f(a+h)&=f(a)+f'(a)h+\tfrac 12 f''(a)h^2+\tfrac 16 f'''(a)h^3
   +\tfrac 1{24}f^{(4)}(\alpha)h^4,\\
     f(a-h)&=f(a)-f'(a)h+\tfrac 12 f''(a)h^2-\tfrac 16 f'''(a)h^3
   +\tfrac 1{24}f^{(4)}(\beta)h^4,\end{aligned}

þar sem :math:`\alpha` er á milli :math:`a` og :math:`a+h` og
:math:`\beta` er á milli :math:`a` og :math:`a-h`.

Nú leggjum við saman og fáum

.. math::

   f(a+h)+f(a-h)=2f(a) +f''(a)h^2+\tfrac
   1{24}\big(f^{(4)}(\alpha)+f^{(4)}(\beta)\big)h^4.

Nú þurfum við að gefa okkur að :math:`f^{(4)}` sé samfellt fall, þá
gefur milligildissetningin okkur að til er :math:`\xi` á milli
:math:`\alpha` og :math:`\beta` þannig að
:math:`f^{(4)}(\xi)=\tfrac 12 (f^{(4)}(\alpha)+f^{(4)}(\beta))`.

Niðurstaðan verður

.. math:: f''(a)=\dfrac{f(a+h)+f(a-h)-2f(a)}{h^2}-\tfrac 1{12}f^{(4)}(\xi)h^2

Með Taylor-margliðum má leiða út fleiri nálgunarformúlur fyrir afleiður.

Við ætlum ekki að halda lengra í þessa átt heldur snúa okkur að almennu
aðferðinni.

Skekkjumat
----------

Almennt um nálganir á afleiðum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`x_0,\ldots, x_n` eru punktar í :math:`I` (hugsanlega með
endurtekningum) og :math:`p` er margliðan sem brúar :math:`f` í þeim, þá
er

.. math:: f(x) = p(x) + r(x),

þar sem skekkjuliðurinn :math:`r(x)` er gefinn með formúlunni

.. math:: r(x)=f[x_0,\ldots,x_n,x](x-x_0)\cdots(x-x_n)

Ef við tökum :math:`p'(a)` sem nálgun á :math:`f'(a)` er skekkjan

.. math:: r'(a) =  f'(a) - p'(a).

.. index::
	töluleg diffrun; skekkjumat

Skekkjumat
~~~~~~~~~~

Munið að formúlan fyrir afleiðu af margfeldi margra þátta er

.. math::

   \begin{gathered}
     (\varphi_1\varphi_2\varphi_3\cdots\varphi_m)'(a)\\
   =\varphi_1'(a)\varphi_2(a)\varphi_3(a)\cdots\varphi_m(a)
   +\varphi_1(a)\varphi_2'(a)\varphi_3(a)\cdots\varphi_m(a)
   +\cdots\\
   \cdots+\varphi_1(a)\varphi_2(a)\cdots \varphi_{m-1}(a)\varphi_m'(a)\\\end{gathered}

Horfum nú á skekkjuliðinn :math:`r(x)`. Hann er svona margfeldi með
:math:`\varphi_1(x)=f[x_0,\dots,x_n,x]`, :math:`\varphi_2(x)=x-x_0`,
:math:`\varphi_3(x)=x-x_1` o.s.frv.

Athugum nú að ef :math:`a` er einn af gefnu punktunum :math:`x_k`, þá er
:math:`\varphi_{k+2}(x)=(x-x_k)` sem gefur :math:`\varphi_{k+2}(x_k)=0`
og :math:`\varphi_{k+2}'(x_k)=1`.

Þetta segir okkur að ef við tökum :math:`a=x_k`, þá eru allir liðirnir í
summunni í hægri hliðinni :math:`0` nema einn, þ.e. við sitjum eftir með
þann sem inniheldur :math:`{\varphi}_{k+2}'`.

Niðurstaðan verður því að skekkjan í nálgun á :math:`f'(a)` með
:math:`p'(a)` er

.. math::

   \begin{aligned}
     f'(a) - p'(a) &= r'(a)
   =f[x_0,\dots,x_n,x_k]
   \prod_{\stackrel{j=0}{j \not= k}} (x_k-x_j)\\
   &=\dfrac{f^{(n+1)}(\xi)}{(n+1)!}
     \prod_{\stackrel{j=0}{j \not= k}} (a-x_j)\end{aligned}

þar sem :math:`a=x_k`.

Hér notuðum við skekkjumatið fyrir Newton aðferðina sem
segir að til er :math:`\xi` á minnsta bilinu sem inniheldur
:math:`x_0,\ldots,x_n,x_k` sem uppfyllir

.. math:: f[x_0,\ldots,x_n,x_k] = \frac{f^{(n+1)}(\xi)}{(n+1)!}.

Frammismunur
~~~~~~~~~~~~

Nálgum :math:`f` með fyrsta stigs brúunarmargliðunni gegnum punktana
:math:`(a,f(a))` og :math:`(a+h,f(a+h))` (þ.e. :math:`x_0 = a` og
:math:`x_1 = a+h`),

.. math:: f(x)=f[a]+f[a,a+h](x-a)+f[a,a+h,x](x-a)(x-a-h)

Af þessu leiðir formúlan sem við vorum áður komin með

.. math::

   f'(a)=f[a,a+h]+f[a,a+h,a](a-a-h)
     =\dfrac{f(a+h)-f(a)}h-\tfrac 12 f''(\xi)h

Þar sem :math:`\xi` er á milli :math:`a` og :math:`a+h` og uppfyllir að
:math:`f[a,a+h,a]=f[a,a,a+h]=\tfrac 12f''(\xi)`. Hér erum við að
notafæra okkur aftur skekkjumatið sem við sönnuðum í kaflanum um
brúunarmargliður.

Miðsettur mismunakvóti
~~~~~~~~~~~~~~~~~~~~~~

Tökum þriggja punkta brúunarformúlu með :math:`a-h`, :math:`a+h` og
:math:`a`. Þá er

.. math::

   \begin{aligned}
     f(x)&=f[a-h]+f[a-h,a+h](x-a+h)\\
     &+f[a-h,a+h,a](x-a+h)(x-a-h)\\
     &+f[a-h,a+h,a,x](x-a+h)(x-a-h)(x-a)\end{aligned}

Athugum að afleiðan af annars stigs þættinum

.. math:: x\mapsto (x-a+h)(x-a-h)=(x-a)^2-h^2

er :math:`0` í punktinum :math:`a` og því er

.. math::

   \begin{aligned}
     f'(a)&=f[a-h,a+h]+f[a-h,a+h,a,a](-h^2)\\
     &=\dfrac{f(a+h)-f(a-h)}{2h}-\tfrac 16 f'''(\xi)h^2 \end{aligned}

Hér nýttum við okkur að til er :math:`\xi` á milli :math:`a-h` og
:math:`a+h` þannig að :math:`f[a-h,a+h,a,a]=\tfrac 16 f'''(\xi)`.

Miðsettur mismunakvóti fyrir aðra afleiðu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Áfram heldur leikurinn. Nú skulum við leiða aftur út formúluna fyrir
nálgun á :math:`f''(a)` með miðsettum mismunakvóta

Þá tökum við þriggja punkta brúunarformúlu með :math:`a-h`, :math:`a+h`
og :math:`a` með :math:`a` tvöfaldan. Þá er

.. math::

   \begin{aligned}
     f(x)&=f[a-h]+f[a-h,a+h](x-a+h)\\
     &+f[a-h,a+h,a](x-a+h)(x-a-h)\\
     &+f[a-h,a+h,a,a](x-a+h)(x-a-h)(x-a)\\
     &+f[a-h,a+h,a,a,x](x-a+h)(x-a-h)(x-a)^2\end{aligned}

Gætum þess að halda liðnum :math:`(x-a)`. Þá fáum við

.. math::

   \begin{aligned}
     f(x)&=f[a-h]+f[a-h,a+h](x-a+h)\\
     &+f[a-h,a+h,a]\big((x-a)^2-h^2)\big)\\
     &+f[a-h,a+h,a,a]\big((x-a)^3-h^2(x-a))\big)\\
     &+f[a-h,a+h,a,a,x]\big((x-a)^4-h^2(x-a)^2)\big)\end{aligned}

Nú þurfum við að reikna aðra afleiðu í punktinum :math:`a`. Athugum að
önnur afleiða af annars stigs þættinum

.. math:: x\mapsto (x-a+h)(x-a-h)=(x-a)^2-h^2

er fastafallið :math:`2`, önnur afleiða af þriðja stigs liðnum

.. math:: x\mapsto (x-a)^3-h^2(x-a)

er :math:`0` í punktinum :math:`a` og önnur afleiða af fjórða stigs
liðnum

.. math:: x\mapsto (x-a)^4-h^2(x-a)^2

er fastafallið :math:`-2h^2`.

Við höfum því

.. math:: f''(a)=2f[a-h,a+h,a]+f[a-h,a+h,a,a,a](-2h^2)

Nú er til punktur :math:`\xi` á minnsta bili sem inniheldur :math:`a-h`,
:math:`a+h` og :math:`a` þannig að :math:`f[a-h,a+h,a,a,a]=\tfrac
1{24}f^{(4)}(\xi)`.

Við þurfum að reikna út fyrri mismunakvótann

.. math::

   \begin{aligned}
     f[a-h,a+h,a]&=f[a-h,a,a+h]=\dfrac{f[a,a+h]-f[a-h,a]}{2h}\\
     &=\dfrac 1{2h}\bigg(\dfrac{f(a+h)-f(a)}h-\dfrac{f(a)-f(a-h)}h\bigg)\\
     &=\dfrac{f(a+h)+f(a-h)-2f(a)}{2h^2}  \end{aligned}

Við höfum því leitt aftur út formúluna

.. math::

   f''(a)=\dfrac{f(a+h)+f(a-h)-2f(a)}{h^2}-\tfrac
     1{12}f^{(4)}(\xi)h^2

.. index::
	töluleg diffrun; Richardson útgiskun

Richardson útgiskun
-------------------

Það ætti að vera ljóst að töluleg deildun er nokkuð óstöðug aðferð því
ef skrefastærðin :math:`h` er lítil eru tölurnar
:math:`f(a+h), f(a), f(a-h)` nálægt hver annarri og við getum lent í
styttingarskekkjum.

Því er ekki hægt að búast við að fá alltaf betri nálgun á :math:`f'(a)`
við að minnka skrefalengdina :math:`h`.

Leiðin er Richardson útgiskun (e. extrapolation), sem er aðferð til að
bæta nálganir.

Til eru mjög almennar útgáfur þessarar aðferðar en við munum aðeins
skoða þau sértilfelli sem nýtast okkur mest.

Útleiðsla á miðsettum mismunakvóta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við skulum byrja á að að leiða aftur út formúluna fyrir miðsettann
mismunakvóta til að fá betri upplýsingar um skekkjuliðinn. Fyrir fall
:math:`f` sem er nógu oft deildanlegt má beita Taylor til að skrifa

.. math::

   \begin{aligned}
     f(a+h) &= f(a) + f'(a)h   + \ldots
     + \frac{f^{(2n)}(a)}{(2n!)}h^{2n}
     + \frac{f^{(2n+1)}(a)}{(2n+1)!)}h^{2n+1} + O(h^{2n+2}) \\
     f(a-h) &= f(a) - f'(a)h 
       + \ldots
     + \frac{f^{(2n)}(a)}{(2n!)}h^{2n}
     - \frac{f^{(2n+1)}(a)}{(2n+1)!)}h^{2n+1} + O(h^{2n+2})\end{aligned}

Ef við drögum seinni jöfnuna frá þeirri fyrri fæst

.. math::

   f(a+h)-f(a-h) = 2f'(a)h + 2\frac{f'''(a)}{3!}h^3
     + \ldots + 2\frac{f^{(2n+1)}(a)}{(2n+1)!}h^{2n+1} + O(h^{2n+2})

svo ef við einangrum :math:`f'(a)` sjáum við að

.. math::

   f'(a) = R_1(h) 
     + a_2 h^2 + a_4 h^4 + \ldots + a_{2n} h^{2n} + O(h^{2n+1})

þar sem

.. math::

   R_1(h) = \frac{f(a+h)-f(a-h)}{2h}
     \quad \text{og} \quad
     a_k = -\frac{f^{(k+1)}(a)}{(k+1)!},
     \quad k = 2,4,\ldots,2n.

Helmingun á skrefinu
~~~~~~~~~~~~~~~~~~~~

Hér er minnsta veldi í skekkjuliðnum :math:`h^2`, svo nálgunin
:math:`f'(a)
\approx R_1(h)` er :math:`O(h^2)`, eins og við höfum reyndar séð áður.
Helmingum nú skrefalengdina :math:`h`, þá fæst

.. math::

   f'(a) = R_1(h/2) + a_2 \left(\frac{h}{2}\right)^2
     + a_4 \left(\frac{h}{2}\right)^4 + \ldots
     + a_{2n} \left(\frac{h}{2}\right)^{2n} + O(h^{2n+1}).

Nú berum við saman þessi tvö skref:

.. math::

   \begin{aligned}
     f'(a) &= R_1(h/2) + \tfrac 14 a_2 h^2
     + a_4 \left(\frac{h}{2}\right)^4 + \ldots
     + a_{2n} \left(\frac{h}{2}\right)^{2n} + O(h^{2n+1}),\\
     f'(a) &= R_1(h) 
     + a_2 h^2 + a_4 h^4 + \ldots + a_{2n} h^{2n} + O(h^{2n+1})\\\end{aligned}

Margföldum efri jöfnuna með :math:`4` og drögum þá síðari frá. Þá
stendur eftir

.. math::

   \begin{aligned}
     3f'(a) &= 4 R_1(h/2) - R_1(h) 
     + a_4 \left( \frac{4}{2^4} - 1 \right)h^4 \\
     &+ a_6 \left( \frac{4}{2^6} - 1 \right)h^6
     + \ldots
     + a_{2n} \left( \frac{4}{2^{2n}} - 1 \right)h^{2n}
     + O(h^{2n+1})\end{aligned}

Fjórða stigs nálgun
~~~~~~~~~~~~~~~~~~~

Nú erum við komin með nýja formúlu:

.. math::

   f'(a) = R_2(h) + b_4 h^4 + b_6 h^6 + \ldots + b_{2n} h^{2n}
     + O(h^{2n+1})

þar sem

.. math::

   R_2(h) = \frac{4 R_1(h/2) - R_1(h)}{3}
     \quad \text{og} \quad
     b_k = \frac{a_k}{3} \cdot \left(\frac{4}{2^k}-1\right),
     \  k = 4,6,\ldots,2n.

Ef við berum þetta saman við jöfnuna sem við byrjuðum með

.. math::

   f'(a) = R_1(h) 
     + a_2 h^2 + a_4 h^4 + \ldots + a_{2n} h^{2n} + O(h^{2n+1})

þá sjáum við að minnsta veldi í skekkjuliðnum er :math:`h^4`, svo
nálgunin :math:`f'(a)
\approx R_2(h)` uppfyllir

.. math:: f'(a) - R_2(h) = O(h^4)

og er því betri nálgun en áður.

Þetta ferli heitir *Richardson útgiskun*.

Hægt er að halda áfram útgiskun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Næsta takmark er að eyða liðnum :math:`b_4h^4` úr þessari formúlu með
því að líta á

.. math::

   f'(a) = R_2(h/2) + b_4 \left(\frac{h}{2}\right)^4 
     + b_6 \left(\frac{h}{2}\right)^6 + \ldots
     + b_{2n} \left(\frac{h}{2}\right)^{2n} + O(h^{2n+1})

Síðan stillum við þessari jöfnu upp með þeirri síðari

.. math::

   \begin{aligned}
     f'(a) &= R_2(h/2) + \tfrac 1{16}b_4 h^4 
     + \tfrac 1{64}b_6 h^6 + \ldots
     + \tfrac 1{2^{2n}}b_{2n} h^{2n} + O(h^{2n+1})\\
     f'(a) &= R_2(h) + b_4 h^4 + b_6 h^6 + \ldots + b_{2n} h^{2n}
     + O(h^{2n+1})\end{aligned}

Margföldum fyrri jöfnuna með :math:`16` og drögum þá síðari frá

.. math::

   \begin{aligned}
     15f'(a) &= 16 R_2(h/2) - R_2(h) 
     + b_6 \left( \frac{16}{2^6} - 1 \right) h^6 \\
     &+ b_8 \left( \frac{16}{2^8} - 1 \right) h^8
     + \ldots
     + b_{2n} \left( \frac{16}{2^{2n}} - 1 \right) h^{2n}
     + O(h^{2n+1}).\end{aligned}

Sjötta stigs skekkja
~~~~~~~~~~~~~~~~~~~~

.. math::

   \begin{aligned}
     15f'(a) &= 16 R_2(h/2) - R_2(h) 
     + b_6 \left( \frac{16}{2^6} - 1 \right) h^6 \\
     &+ b_8 \left( \frac{16}{2^8} - 1 \right) h^8
     + \ldots
     + b_{2n} \left( \frac{16}{2^{2n}} - 1 \right) h^{2n}
     + O(h^{2n+1}).\end{aligned}

Því er

.. math::

   f'(a) = R_3(h) + c_6 h^6 + c_8 h^8 \ldots + c_{2n} h^{2n}
     + O(h^{2n+1})

þar sem

.. math::

   R_3(h) = \frac{16 R_2(h/2) - R_2(h)}{15},
     \quad \text{og} \quad
     c_k = \frac{b_k}{15} \cdot \left( \frac{16}{2^k} - 1 \right),
     \quad k = 6,8,\ldots,2n.

Nýja nálgunin uppfyllir

.. math:: f'(a) - R_3(h) = O(h^6)

og er því enn betri en áður, en við þurfum líka að reikna út
:math:`R_1(h/4)` til að reikna :math:`R_2(h/2)`.

Almenn rakningarformúla
~~~~~~~~~~~~~~~~~~~~~~~

Richardson-útgiskunin heldur áfram og út kemur

.. math::

   R_{i+1}(h) = \frac{4^i R_i(h/2) - R_i(h)}{4^i-1}
     = R_i(h/2) + \frac{R_i(h/2)-R_i(h)}{4^i-1}

fyrir :math:`(i+1)`-tu Richardson útgiskun og :math:`R_{i+1}(h)`
uppfyllir að

.. math:: f'(a) - R_{i+1}(h) = O(h^{2i+2}),

en á móti kemur að til að reikna út :math:`R_{i+1}(h)` þurfum við að
hafa reiknað út tölurnar

| :math:`R_1(h)`, :math:`R_1(h/2)`, :math:`\ldots`, :math:`R_1(h/2^i)`
  auk
| :math:`R_2(h)`, :math:`R_2(h/2)`, …, :math:`R_2(h/2^{i-1})` og svo
  framvegis að
| :math:`\qquad \vdots`
| :math:`R_i(h)` og :math:`R_i(h/2)`.

Eins og áður sagði fara styttingarskekkjur á endanum að segja til sín í
útreikningum á :math:`R_1(h)`, svo einhver takmörk eru fyrir hversu
margar Richardson útgiskanir er hægt að framkvæma.

Reiknirit
~~~~~~~~~

Útreikningarnir að ofan eru yfirleitt settir fram í töflu

.. math::

   \begin{array}{ccccc}
       D(1,1) &   &   &   &   \\
       D(2,1) & D(2,2) &  &  &  \\
       D(3,1) & D(3,2) & D(3,3) & & \\
       \vdots & \vdots & \vdots & \ddots & \\
       D(n,1) & D(n,2) & D(n,3) & \ldots & D(n,n)
     \end{array}

þar sem :math:`D(i,j) = R_j(h/2^{i-j})` og þar með

.. math::

   D(i,j) = \begin{cases}
       \dfrac{f(a+h/2^{i-1})-f(a-h/2^{i-1})}{2\cdot h/2^{i-1}}, & j = 1 \\
       D(i,j-1) + \dfrac{D(i,j-1)-D(i-1,j-1)}{4^{j-1}-1}, & j > 1
     \end{cases}

sem gerir okkur auðvelt að forrita Richardson útgiskun.

Skekkjumat
~~~~~~~~~~

Finnum nú eftirámat fyrir :math:`D(i,j)` með stærðunum
:math:`D(i,j-1)` og :math:`D(i-1,j-1)`. Hér á eftir er
:math:`R_j(h/2)` í hlutverki :math:`D(i,j-1)` og :math:`R_i(h)` í
hlutverki :math:`D(i-1,j-1)`
(:math:`h` er helmingað þegar við förum niður um eina línu).

Munum að :math:`R_i(h)` uppfyllir að

.. math:: f'(a) = R_j(h) + Kh^{2j} + O(h^{2j+1})

fyrir eitthvert :math:`K` í :math:`\mathbb R` og að

.. math::

   f'(a) = R_j(h/2) + K \left( \frac{h}{2} \right)^{2j}
     + O(h^{2j+1})

Ef við tökum mismun á hægri og vinstri hliðum þessara jafna, þá fáum við

.. math::

   0 = R_j(h) - R_j(h/2) + K \left(1 - \frac{1}{2^{2j}}\right)h^{2j}
     + O(h^{2j+1})

og ef við einangrum :math:`K` fæst

.. math::

   K = -\frac{4^{j}}{h^{2j}} \cdot \frac{R_j(h)-R_j(h/2)}{4^{j}-1} +
   O(h^{2j+1}).

Útleiðsla á fyrirframmati
~~~~~~~~~~~~~~~~~~~~~~~~~

Þá er skekkjan í nálgun á :math:`f'(a)` með :math:`R_j(h/2)` jöfn

.. math::

   \begin{aligned}
     e_j(h/2) &= f'(a) - R_j(h/2) \\
     &= K\left(\frac{h}{2}\right)^{2j} + O(h^{2j+1}) \\
     &= -\frac{R_j(h)-R_j(h/2)}{4^{j}-1} + O(h^{2j+1}) \\
     &\approx -\frac{R_j(h)-R_j(h/2)}{4^{j}-1}.\end{aligned}

Þar sem :math:`R_j(h/2)` er nálgun á :math:`f'(a)` af stigi
:math:`O(h^{2j+1})`, en :math:`R_{j+1}(h)` er nálgun á :math:`f'(a)` af
stigi :math:`O(h^{2i+3})` getum við slegið á :math:`e_{j+1}(h)` með
:math:`e_j(h/2)`. Ef við lækkum vísinn :math:`j+1` um einn gefur það
okkur matið

.. math::

   e_j(h) \approx \frac{R_{j-1}(h)-R_{j-1}(h/2)}{4^{j-1}-1} =
     \frac{D(i,j-1)-D(i-1,j-1)}{4^{j-1}-1}

sem er einmitt liðurinn í rakningarformúlunni fyrir :math:`D(i,j)`.

Sýnidæmi
~~~~~~~~

Látum :math:`f(x)=x/(x^2+4)^{2/3}` og :math:`a=-1`. Byrjum með
:math:`h=1` og notum svo rakningarformúluna til þess að fylla út
útgiskunartöfluna.

+-------------+------------------+------------------+------------------+------------------+
| :math:`h`   | :math:`D(i,1)`   | :math:`D(i,2)`   | :math:`D(i,3)`   | :math:`D(i,4)`   |
+=============+==================+==================+==================+==================+
| 1 .         | 0.25000000       |                  |                  |                  |
+-------------+------------------+------------------+------------------+------------------+
| 0.5         | 0.25151838       | 0.25202451       |                  |                  |
+-------------+------------------+------------------+------------------+------------------+
| 0.25        | 0.25104655       | 0.25088928       | 0.25081360       |                  |
+-------------+------------------+------------------+------------------+------------------+
| 0.125       | 0.25086355       | 0.25080254       | 0.25079676       | 0.25079649       |
+-------------+------------------+------------------+------------------+------------------+

Niðustaðan er: :math:`f'(-1)\approx   0.2507964`, með eftirámat á
skekkju :math:`-3\cdot 10^{-7}`.

Rétt gildi er :math:`0.25079647217924889177`.

