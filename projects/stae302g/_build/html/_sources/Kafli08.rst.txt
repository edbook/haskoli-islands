Veldaraðalausnir á afleiðujöfnum
================================

Rose: *If you are an alien, how come you sound like you're from the north?*

Doctor: *Lots of planets have a north!*

\- Doctor Who 

Veldaraðalausnir
----------------

Skilgreining (Sjá Skilgreiningu 8.1.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fall :math:`f:X\to {\mathbb{C}}` skilgreint á opnu mengi :math:`X` á raunásnum, er sagt vera raunfágað á :math:`X` ef fyrir sérhvern punkt :math:`a\in X` er til tala :math:`\rho>0` þannig að bilið :math:`]a-\rho, a+\rho[\subseteq X` og til er veldaröð :math:`\sum_{n=0}^\infty c_n(x-a)^n` þannig að fyrir öll :math:`x\in ]a-\rho, a+\rho[` er :math:`f(x)=\sum_{n=0}^\infty c_n(x-a)^n`.
   
Umræða (Sjá §8.1)
~~~~~~~~~~~~~~~~~

Mörg hugtök og skilgreiningar fyrir raunfáguð föll eru eins og fyrir fáguð föll af tvinntölubreytu. Látum nú :math:`f(x)` vera raunfágað fall skilgreint á opnu mengi :math:`X` í :math:`\mathbb{R}`.

Gerum ráð fyrir að :math:`f(a)=0` og :math:`f(x)=\sum_{n=0}^\infty c_n(x-a)^n`. Ef :math:`n` er minnsta tala þannig að :math:`c_n\neq 0` þá segjum við að :math:`f(x)` hafi núllstöð af stigi :math:`n` í :math:`a`.

Segjum að punktur :math:`a` sé einangraður sérstöðupunktur ef til er tala :math:`\delta>0` þannig að fallið :math:`f(x)` er skilgreint á öllu bilinu :math:`]a-\delta, a+\delta[` nema í punktinum :math:`a`.

Einangraður sérstöðupunktur :math:`a` er sagður afmáanlegur ef hægt er að gefa :math:`f(a)` gildi þannig að útvíkkaða fallið verði raunfágað á :math:`X\cup\{a\}`.

Skilgreining (Sjá Skilgreiningu 8.2.6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`a_0(x), a_1(x), a_2(x)` vera föll sem eru raunfáguð á bili :math:`I`. Segjum að punktur :math:`a\in I` sé venjulegur punktur fyrir afleiðujöfnuna

.. math::

 a_2(x)u''+a_1(x)u'+a_0(x)u=0,

ef :math:`a_2(a)\neq 0` eða ef :math:`a_2(a)=0` þá hafi föllin :math:`P(x)=a_1(x)/a_2(x)` og :math:`Q(x)=a_0(x)/a_2(x)` afmáanlegan sérstöðupunkt í :math:`a`.

Setning (Samanber Setning 8.2.8)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`a` sé venjulegur punktur afleiðujöfnunnar

.. math::

 a_2(x)u''+a_1(x)u'+a_0(x)u=0.

Þá er sérhver lausn :math:`u` á afleiðujöfnunni raunfáguð á bili umhverfis :math:`a`.

Reikniaðferð (Sjá §8.2)
~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`a` sé venjulegur punktur afleiðujöfnunnar

.. math::

 a_2(x)u''+a_1(x)u'+a_0(x)u=0.

---------------- 
 
Skref 0: Setjum :math:`P(x)=a_1(x)/a_2(x)` og :math:`Q(x)=a_0(x)/a_2(x)` og ritum afleiðujöfnuna sem

.. math::

 u''+P(x)u'+Q(x)u=0.

----------------
 
Skref 1: Finnum veldaraðir með miðju í :math:`a` fyrir föllin :math:`P(x)` og :math:`Q(x)`:

.. math::

   P(x)=\sum_{n=0}^\infty P_n(x-a)^n\qquad\mbox{ og }\qquad 
   Q(x)=\sum_{n=0}^\infty Q_n(x-a)^n.

----------------
   
Skref 2: Setjum inn í afleiðujöfnuna

.. math::

   u(x)=\sum_{n=0}^\infty c_n(x-a)^n,\quad
   u'(x)=\sum_{n=0}^\infty (n+1)c_{n+1}(x-a)^n,\quad
   u''(x)=\sum_{n=0}^\infty (n+2)(n+1)c_{n+2}(x-a)^n.

----------------
   
Skref 3: Tökum saman í eina veldaröð og fáum að

.. math::

   \sum_{n=0}^\infty 
   \bigg((n+2)(n+1)c_{n+2} +
   \sum_{k=0}^{n} \big((k+1)P_{n-k}c_{k+1}+
   Q_{n-k} c_k\big)\bigg)(x-a)^n=0.

----------------
   
Skref 4: Allir stuðlar í þessari síðustu veldaröð eru 0. Stuðlana :math:`c_0` og :math:`c_1` má velja frjálst og svo fæst rakningarformúla fyrir :math:`c_n` þannig að

.. math::

   c_{n+2} = \dfrac{-1}{(n+2)(n+1)}
   \sum_{k=0}^n \big[(k+1)P_{n-k}c_{k+1}+ Q_{n-k}c_k\big].

----------------
   
Skref 5: Þegar rakningarformúlan er fengin þá er oft hægt að átta sig á hvaða fall er lausn eða reikna má fyrstu stuðlana í veldaröðinni og fá þannig Taylor-margliðu fallsins :math:`u` sem má nota til að reikna nálgunargildi. Athugið einnig að :math:`c_0=u(a)` og :math:`c_1=u'(a)` þannig að oft ákvarðast því :math:`c_0` og :math:`c_1` af upphafsgildum.

Skilgreining (Sjá §8.3)
~~~~~~~~~~~~~~~~~~~~~~~

:math:`\Gamma`-fallið er skilgreint með formúlunni

.. math::

   \Gamma(z)=\int_0^\infty e^{-t}t^{z-1}\, dt, \quad z\in {\mathbb{C}}, \quad \operatorname{Re\, }
   z>0.

Nokkrar formúlur (Sjá §8.3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   \begin{aligned}
   \Gamma(z+1)&=z\Gamma(z)\\
   \Gamma(z+n)&=z(z+1)\cdots(z+n-1)\Gamma(z)\\
   \Gamma(1)&=1\\
   \Gamma(n)&=(n-1)!\\
   \Gamma(1/2)&=\sqrt{\pi}\\
   \Gamma(-1/2)&=2\sqrt{\pi}\\
   \Gamma(n+1/2)&=\frac{(2n-1)!}{2^{2n-1}(n-1)!}\sqrt{\pi}.\end{aligned}

Aðferð Frobeniusar
------------------

Umræða 
~~~~~~

Afleiðujafnan

.. math::

 x^2u''+xu'+(x^2-\alpha^2)u=0

kallast jafna Bessel. Besseljafnan og lausnir hennar, sem kallaðar eru Bessel-föll, koma upp í rafsegulfræði, varmafræði, skammtafræði, ...

Punkturinn :math:`a=0` er ekki venjulegur punktur. Aðeins í undantekningartilfellum fæst lausn með aðferðinni úr síðasta fyrirlestri við að prófa veldaraðarlausn með miðju í :math:`a=0` og í engu tilfelli fæst grunnur fyrir lausnarúmið. Samt er hægt að nota aðferð sem er áþekk því sem lýst var í síðasta fyrirlestri.

   

Skilgreining (Sjá Skilgreiningu 8.4.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera raunfágað fall á opnu mengi :math:`X` í :math:`\mathbb{R}`. Við segjum að einangraður sérstöðupunktur :math:`a` raunfágaða fallsins :math:`f` sé skaut af stigi :math:`m>0`, ef til er tala :math:`\varrho>0` og raunfágað fall :math:`g` skilgreint á bilinu :math:`\{x\mid |x-a|<\varrho\}`, þannig að :math:`\{x\mid 0<|x-a|<{\varrho}\}\subseteq X`, :math:`g(a)\neq 0` og 

.. math::

 f(x)=\dfrac {g(x)}{(x-a)^m}\qquad \mbox{ef }0<|x-a|<\varrho.

Skilgreining (Sjá Skilgreiningu 8.4.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við segjum að :math:`a` sé reglulegur sérstöðupunktur afleiðujöfnunnar 

.. math::
    a_2(x)u''+a_1(x)u'+a_0(x)u=0
    
ef :math:`a` er sérstöðupunktur jöfnunnar, fallið :math:`P=a_1(x)/a_2(x)` hefur annað hvort afmáanlegan sérstöðupunkt í :math:`a` eða skaut af stigi :math:`\leq 1` og :math:`Q=a_0(x)/a_2(x)` hefur annað hvort afmáanlegan sérstöðupunkt í :math:`a` eða skaut af stigi :math:`\leq 2`.

Skilgreining (Sjá Skilgreiningu 8.4.4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`a` sé reglulegur sérstöðupunktur afleiðujöfnu sem rituð er á forminu

.. math::

 (x-a)^2u''+(x-a)p(x)u'+q(x)u=0.\label{3.4.7}

Þá kallast margliðan

.. math::

 \varphi(\lambda)=\lambda(\lambda-1)+p(a)\lambda+q(a)

vísamargliða afleiðujöfnunnar í punktinum :math:`a`, og jafnan :math:`\varphi(\lambda)=0` kallast vísajafna afleiðujöfnunnar í punktinum :math:`a`. Núllstöðvarnar kallast vísar jöfnunnar í punkti :math:`a`.

Setning Frobeniusar (Sjá Setningu 8.4.5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir því að :math:`a` sé reglulegur sérstöðupunktur afleiðujöfnunnar

.. math::

 (x-a)^2u''+ (x-a)p(x)u'+q(x)u=0

og gerum ráð fyrir að föllin :math:`p` og :math:`q` séu sett fram með veldaröðunum

.. math::

   p(x)=\sum_{n=0}^\infty p_n(x-a)^n, \qquad\quad
   q(x)=\sum_{n=0}^\infty q_n(x-a)^n,

og að þær séu samleitnar ef :math:`|x-a|<\varrho`. Látum :math:`r_1` og :math:`r_2` vera núllstöðvar vísajöfnunnar

.. math::

 \varphi(\lambda)=\lambda(\lambda-1)+p(a)\lambda+q(a)=0

og gerum ráð fyrir að :math:`\operatorname{Re\, } r_1\geq \operatorname{Re\, } r_2`. Þá gildir:

(i) Til er lausn :math:`u_1` á jöfnunni sem gefin er með

.. math::

 u_1(x)=|x-a|^{r_1}\sum_{n=0}^\infty a_n(x-a)^n.

Röðin er samleitin fyrir öll :math:`x` sem uppfylla :math:`0<|x-a|<\varrho`. Valið á :math:`a_0` er frjálst, en hinir stuðlar raðarinnar fást með rakningarformúlunni

.. math::

   a_n=\dfrac{-1}{\varphi(n+r_1)}
   \sum_{k=0}^{n-1}((k+r_1)p_{n-k}+q_{n-k})a_k, \qquad n=1,2,3,\dots.



(ii) Ef :math:`r_1-r_2\neq 0,1,2,\dots`, þá er til önnur línulega óháð lausn :math:`u_2` á jöfnunni sem gefin er með

.. math::

 u_2(x)=|x-a|^{r_2}\sum_{n=0}^\infty b_n(x-a)^n.

Röðin er samleitin fyrir öll :math:`x` sem uppfylla :math:`0<|x-a|<\varrho`. Valið á :math:`b_0` er frjálst, en hinir stuðlar raðarinnar fást með rakningarformúlunni

.. math::

   b_n=\dfrac{-1}{\varphi(n+r_2)}
   \sum_{k=0}^{n-1}((k+r_2)p_{n-k}+q_{n-k})b_k, \qquad n=1,2,3,\dots.



(iii) Ef :math:`r_1-r_2=0`, þá er til önnur línulega óháð lausn :math:`u_2` á jöfnunni sem gefin er með

.. math::

   u_2(x)=|x-a|^{r_1+1}\sum_{n=0}^\infty b_n(x-a)^n+
   u_1(x)\ln|x-a|.

Röðin er samleitin fyrir öll :math:`x` sem uppfylla :math:`0<|x-a|<\varrho` og stuðlar raðarinnar fást með innsetningu í jöfnuna.

(iv) Ef :math:`r_1-r_2=N`, þar sem :math:`N` er jákvæð heiltala, þá er til önnur línulega óháð lausn :math:`u_2` á upphaflegu jöfnunni sem gefin er með

.. math::

   u_2(x)=|x-a|^{r_2}\sum_{n=0}^\infty b_n(x-a)^n+
   \gamma u_1(x)\ln|x-a|.

Röðin er samleitin fyrir öll :math:`x` sem uppfylla :math:`0<|x-a|<\varrho`. Stuðlar raðarinnar og :math:`\gamma` fást með innsetningu í jöfnuna.

Skilgreining (Sjá Skilgreiningu 8.5.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lausn á Bessel-jöfnunni :math:`x^2u''+xu'+(x^2-\alpha^2)u=0`, sem gefin er með formúlunni

.. math::

   J_\alpha(x)=\left|\dfrac x2\right|^\alpha\sum_{k=0}^\infty
   \dfrac{(-1)^k}{k!\Gamma(\alpha+k+1)}\left( \dfrac x2\right)^{2k}

er kölluð Bessel-fall af fyrstu gerð með vísi :math:`\alpha`.

Skilgreining (Sjá Skilgreiningu 8.5.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fallið :math:`Y_{\alpha}`, :math:`{\alpha}=1,2,3,\dots` sem skilgreint er með

.. math::

   \begin{aligned}
   Y_{\alpha}(x)=\dfrac 2{\pi}\bigg[&
   J_{\alpha}(x)\bigg(\ln \dfrac {|x|}2+{\gamma}\bigg)\\
   &+x^{\alpha}\sum\limits_{k=0}^{\infty}
   \dfrac{(-1)^{k-1}\big(h_k+h_{k+\alpha}\big)}
   {2^{2k+\alpha+1}k!(k+{\alpha})!} x^{2k}\\
   &-x^{-\alpha}\sum\limits_{k=0}^{\alpha-1}
   \dfrac{(\alpha-k-1)!}{2^{2k-\alpha+1}k!}x^{2k}\bigg],\end{aligned}

þar sem :math:`h_k=1+1/2+1/3+\cdots+1/k` og :math:`{\gamma}` táknar fasta Eulers, nefnist Bessel-fall af annarri gerð með vísi :math:`{\alpha}`.
