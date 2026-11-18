Ójöfnur Markovs og Chebyshevs og lögmál mikils fjölda
=====================================================

Ójafna Markovs
~~~~~~~~~~~~~~

.. admonition:: Setning 17 (Ójafna Markovs).
   :class: box-theorem

   Ef :math:`X` er slembistærð þannig að :math:`X \geq 0`, þá gildir að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
                  \mathbb{P}(X > a) \leq \frac{\mathbb{E}[X]}a, \quad a >0.
      \end{aligned}
      \]

.. admonition:: Sönnun.
   :class: box-theorem

   Látum :math:`a >0` og skilgreinum slembistærðina :math:`Y := a \cdot 1_{\{X > a\}}`, þ.e.

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          Y = \begin{cases} a, & \text{ef $X > a$,} \\ 0, & \text{ef $X \leq a$.} \end{cases}
      \end{aligned}
      \]

   Samkvæmt skilgreiningu á væntigildi er

   .. math:: \mathbb{E}[Y] = a \cdot \mathbb{P}(X > a) + 0 \cdot \mathbb{P}(X \leq a) = a\mathbb{P}(X > a).

   Athugum að :math:`X \geq Y`. Þar sem væntigildi er einhalla fæst þá að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          \mathbb{E}[X] \geq \mathbb{E}[Y] = a \mathbb{P}(X > a).
      \end{aligned}
      \]

   Þar sem :math:`a>0` getum við loks ályktað að :math:`\mathbb{P}(X > a) \leq \dfrac{\mathbb{E}[X]}a`.

.. admonition:: Athugasemd.
   :class: box-remark

   Slembistærðin :math:`Y` er skilgreind svona fyrir sérhvert :math:`\omega \in \Omega`:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          Y(\omega) := \begin{cases} a, & \text{ef $X(\omega) > a$,} \\ 0, & \text{ef $X(\omega) \leq a$.} \end{cases}
      \end{aligned}
      \]

   Til að sýna formlega að :math:`X \geq Y` þurfum við að sýna að :math:`X(\omega) \geq Y(\omega)` fyrir sérhvert :math:`\omega \in \Omega`. Tökum tvö tilvik:

   (i)  Ef :math:`\omega \in \Omega` er þannig að :math:`X(\omega) > a`, þá er :math:`Y(\omega) = a` samkvæmt skilgreiningu á :math:`Y` og því er :math:`X(\omega) \geq Y(\omega)`.

   (ii) Ef :math:`\omega \in \Omega` er þannig að :math:`X(\omega) \leq  a`, þá er :math:`Y(\omega) = 0` samkvæmt skilgreiningu á :math:`Y`. Þar sem :math:`X(\omega) \geq 0` er :math:`Y(\omega) \leq X(\omega)`.

   Við höfum þá sýnt að :math:`X(\omega) \geq Y(\omega)` gildir fyrir sérhvert :math:`\omega \in \Omega`.

.. admonition:: Athugasemd 2.
   :class: box-remark

   Í sönnuninni á ójöfnu Markovs notuðum við skilgreininguna á væntigildi til að segja að

   .. math:: \mathbb{E}[Y] = a \cdot \mathbb{P}(X > a) + 0 \cdot \mathbb{P}(X \leq a) = a\mathbb{P}(X > a).

   Þar sem :math:`Y = a \cdot 1_{\{X>a\}}` hefðum við líka getað notað að væntigildi er línulegt og sagt að

   .. math:: \mathbb{E}[Y] = a \cdot \mathbb{E}[1_{\{X > a\}}] = a \mathbb{P}(X > a),

   þar sem við notum að :math:`\mathbb{E}[1_D] = \mathbb{P}(D)` fyrir atburð :math:`D`.

Ójafna Chebychevs
~~~~~~~~~~~~~~~~~

.. admonition:: Setning 18 (Ójafna Chebyshevs).
   :class: box-theorem

   Látum :math:`X` vera slembistærð með væntigildi :math:`\mu = \mathbb{E}[X]` og dreifni :math:`\sigma^2 = {\rm Var}[X] < \infty`. Þá gildir að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
                  \mathbb{P}(|X-\mu|> c) \leq \frac{\sigma^2}{c^2}, \quad c >0.
      \end{aligned}
      \]

.. admonition:: Athugasemd.
   :class: box-remark

   Önnur framsetning á Ójöfnu Chebyshevs er að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
                  \mathbb{P}(|X-\mathbb{E}[X]|> c) \leq \frac{{\rm Var}[X]}{c^2}, \quad c >0.
      \end{aligned}
      \]

   Við notum þessa framsetningu þegar við sönnum Lögmál mikils fjölda hér á eftir.

.. admonition:: Sönnun.
   :class: box-theorem

   Athugum fyrst að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
                  \mathbb{P}(|X-\mu|> c) = \mathbb{P}((X-\mu)^2> c^2).
      \end{aligned}
      \]

   Beitum nú ójöfnu Markovs á :math:`Y := (X-\mu)^2` og fáum svo samkvæmt skilgreiningu á dreifni:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
                  \mathbb{P}(|X-\mu|> c) \leq \frac{\mathbb{E}\left[(X-\mu)^2\right]}{c^2} = \frac{\sigma^2}{c^2}.
      \end{aligned}
      \]

.. admonition:: Athugasemd.
   :class: box-remark

   Þegar við segjum í sönnuninni að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
                  \mathbb{P}(|X-\mu|> c) = \mathbb{P}((X-\mu)^2> c^2)
      \end{aligned}
      \]

   erum við að nota að :math:`\{|X-\mu|> c\} = \{(X-\mu)^2> c^2\}`, þ.e. :math:`\{|X-\mu|> c\}` og :math:`\{(X-\mu)^2> c^2\}` eru sami atburðurinn. Þetta er vegna þess að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
                  |X-\mu|> c \Leftrightarrow (X-\mu)^2> c^2.
      \end{aligned}
      \]

   Við leyfum okkur að taka svona reikningsskref án rökstuðnings, en þurfum alltaf að gæta þess að skilyrðin tvö innan líkindanna séu jafngild. Í þessu tilviki fæst :math:`\Rightarrow` vegna þess að :math:`x \mapsto x^2` er stranglega vaxandi fyrir :math:`x \geq 0` og :math:`\Leftarrow` fæst vegna þess að :math:`x \mapsto \sqrt{x}` er stranglega vaxandi fyrir :math:`x \geq 0`.

Ef við setjum :math:`c := t\sigma` í ójöfnu Chebyshevs, þar sem :math:`t>0` og :math:`\sigma>0`, þá segir ójafnan að

.. math::
   :nowrap:

   \[
   \begin{aligned}
               \mathbb{P}(|X-\mu|> t\sigma) \leq \frac1{t^2}.
   \end{aligned}
   \]

Ef :math:`t=2` segir ójafnan að líkurnar á að slembistærðin :math:`X` taki gildi sem er meira en tveimur staðalfrávikum frá væntigildi sínu séu í mesta lagi :math:`1/4`. Ef :math:`t=3` segir ójafnan að líkurnar á að :math:`X` taki gildi meira en þremur staðalfrávikum frá væntigildi sínu séu í mesta lagi :math:`1/9`, og svo koll af kolli. Ein túlkun á ójöfnu Chebyshevs er þess vegna að hún setur efri mörk á líkurnar á því að slembistærð víki ákveðið mörgum staðalfrávikum frá væntigildi sínu.

.. _lögmál-mikils-fjölda-1:

Lögmál mikils fjölda
~~~~~~~~~~~~~~~~~~~~

Við setjum nú fram og sönnum *lögmál mikils fjölda*, sem er ein mikilvægasta og gagnlegasta setning líkindafræðinnar. Hún segir óformlega að :math:`\bar{X}_n` nálgist væntigildið :math:`\mu` eftir því sem :math:`n` stækkar, þ.e. :math:`\bar{X}_n \approx \mu` þegar :math:`n` er stórt. Í hermunarsamhengi segir lögmál mikils fjölda að ef við hermum óháð gildi fyrir einhverja slembistærð :math:`X`, og við reiknum meðaltal gildanna sem fást með hermuninni, þá nálgumst við væntigildið :math:`\mu = \mathbb{E}[X]` eftir því sem við hermum fleiri gildi.

.. admonition:: Setning 19 (lögmál mikils fjölda).
   :class: box-theorem

   Látum :math:`X_1,X_2,\ldots` vera óháðar slembistærðir sem allar hafa sama væntigildi :math:`\mu` og sömu dreifni :math:`\sigma^2<\infty`. Setjum :math:`\bar{X}_n := \frac1n \sum_{i=1}^n X_i`. Þá gildir fyrir sérhvert :math:`\varepsilon>0` að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              \lim_{n \to \infty} \mathbb{P}\left(\left|\bar{X}_n-\mu\right|>\varepsilon\right) = 0. \quad (\ast)
      \end{aligned}
      \]

.. admonition:: Athugasemd.
   :class: box-remark

   Fullyrðing af gerðinni :math:`(\ast)` kallast *samleitni í líkindum* (e. convergence in probability). Hana má líka skrifa svona:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              \lim_{n \to \infty} \mathbb{P}\left(\left|\bar{X}_n-\mu\right| \leq \varepsilon\right) = 1, \quad (\ast)
      \end{aligned}
      \]

   sem segir að fyrir sérhvert fast :math:`\varepsilon>0` getum við gert líkurnar á því að :math:`\left|\bar{X}_n-\mu\right| \leq \varepsilon` nægilega miklar ef við veljum :math:`n` nógu stórt.

Sönnunin á lögmáli mikils fjölda byggist á eftirfarandi fjórum staðreyndum:

#. Væntigildi er línulegt.

#. Ef :math:`X` er slembistærð og :math:`a` er rauntala, þá er

   .. math::
      :nowrap:

      \[
      \begin{aligned}
       {\rm Var}[aX] = a^2 {\rm Var}[X]
      \end{aligned}
      \]

#. Ef :math:`X_1,\ldots,X_n` eru óháðar, þá er

   .. math::
      :nowrap:

      \[
      \begin{aligned}
       {\rm Var}\left[\sum_{i=1}^n a_i X_i\right] = \sum_{i=1}^n a_i^2 {\rm Var}[X_i],
      \end{aligned}
      \]

   \ eins og fjallað var um í Lík&töl.

#. Ójafna Chebyshevs, sem segir að ef :math:`Y` er slembistærð með væntigildi :math:`\mathbb{E}[Y]` og dreifni :math:`{\rm Var}[Y]`, þá gildir fyrir sérhvert :math:`c>0`:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
       & \mathbb{P}\left(\left|Y-\mathbb{E}[Y]\right| > c\right) \leq \frac{{\rm Var}[Y]}{c^2}.
      \end{aligned}
      \]

.. admonition:: Sönnun.
   :class: box-theorem

   Þar sem væntigildi er línulegt og stærðirnar :math:`X_1,\ldots,X_n` hafa allar sama væntigildið :math:`\mu` gildir að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          \mathbb{E}[\bar{X}_n] = \mathbb{E}\left[\frac1n \sum_{i=1}^n X_i\right] = \frac1n \sum_{i=1}^n \mathbb{E}[X_i] = \frac{n \mu}{n} = \mu. \quad (\ast)
      \end{aligned}
      \]

   Þar sem :math:`X_1,X_2,\ldots,X_n` eru óháðar með sömu dreifni :math:`\sigma^2` fæst síðan að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          {\rm Var}[{\bar X}_n] &= {\rm Var}\left[\frac1n \sum_{i=1}^n  X_i\right] = \frac1{n^2} {\rm Var}\left[\sum_{i=1}^n  X_i\right]  \\
          &= \frac1{n^2} \sum_{i=1}^n {\rm Var}[X_i] = \frac{n\sigma^2}{n^2 } = \frac{\sigma^2}n. \quad (\ast\ast)
      \end{aligned}
      \]

   Látum nú :math:`\varepsilon>0` og fáum:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          \mathbb{P}\left(\left|\bar{X}_n-\mu\right|>\varepsilon\right) &= \mathbb{P}(|\bar{X}_n - \mathbb{E}[\bar{X}_n]| > \varepsilon) \quad (\text{skv.~$(\ast$)}) \\
          &\leq \frac{{\rm Var}[\bar{X}_n]}{\varepsilon^2} \quad (\text{ójafna Chebyshevs}) \\
          &= \frac{\sigma^2}{n \varepsilon^2}. \quad (\text{skv.~$(\ast\ast$)})
      \end{aligned}
      \]

   Þar sem :math:`\displaystyle 0 \leq \mathbb{P}\left(\left|\bar{X}_n-\mu\right|>\varepsilon\right) \leq \frac{\sigma^2}{n \varepsilon^2}` fyrir öll :math:`n \geq 1` og :math:`\dfrac{\sigma^2}{n \varepsilon^2} \to 0` þegar :math:`n \to \infty` gefur klemmureglan loks að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          \lim_{n \to \infty} \mathbb{P}\left(\left|\bar{X}_n-\mu\right|>\varepsilon\right) = 0.
      \end{aligned}
      \]


