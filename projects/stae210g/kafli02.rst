Dreififöll
==========

Dreififöll strjálla og samfelldra slembistærða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining 5.
   :class: box-definition

   Látum :math:`X` vera slembistærð. Fallið :math:`F: \mathbb{R} \to \mathbb{R}` sem skilgreint er með :math:`F(x) := \mathbb{P}(X \leq x)` kallast **dreififall slembistærðarinnar** :math:`X`. Við táknum dreififall :math:`X` oft með :math:`F_X`.

Dreififall slembistærðinnar :math:`X` gefur okkur gagnlega leið til að lýsa dreifingu :math:`X` með venjulegu rauntölufalli :math:`F: \mathbb{R} \to \mathbb{R}`. Með því að nota dreififallið getum við beitt öllum tólum sem við höfum lært í stærðfræðigreiningu til að rannsaka dreifingu :math:`X`. Jafnframt er hægt að sanna að dreififall slembistærðarinnar :math:`X` ákvarðar dreifingu :math:`X` fullkomlega (STÆ418M Grundvöllur líkindafræðinnar). Með öðrum orðum: Ef tvær slembistærðir :math:`X` og :math:`Y` hafa sama dreififall, þá hafa þær sömu dreifingu: :math:`\mathbb{P}(X \in A) = \mathbb{P}(Y \in A)` fyrir alla atburði :math:`A \in {\cal F}`.

.. admonition:: Dæmi.
   :class: box-example

   - | Bernoulli-stærð :math:`X` með stika :math:`p = 1/4`, þannig að :math:`\mathbb{P}(X=0) = 3/4` og :math:`\mathbb{P}(X=1)=1/4`, hefur eftirfarandi dreififall:

     .. container:: center

        .. figure:: images/dreififall_bernoulli.svg
           :width: 258.43pt
           :align: center

     Þar sem :math:`X` tekur aðeins gildin :math:`0` eða :math:`1` breytist fallgildið :math:`F(x) = \mathbb{P}(X \leq x)` aðeins í :math:`x=0` og :math:`x=1`. Við fáum svokallað **þrepafall** sem er fast á köflum.

   - Tvíkostastærð :math:`X` með stika :math:`n=3` og :math:`p = 1/2`, sem lýsir fjölda þorska sem kemur upp í þremur venjulegum krónuköstum, hefur eftirfarandi massafall:

     .. math::
        :nowrap:

        \[
        \begin{aligned}
                &\mathbb{P}(X=0)=1/8, \; \mathbb{P}(X=1)=3/8, \\
                &\mathbb{P}(X=2)=3/8, \; \mathbb{P}(X=3)=1/8.
        \end{aligned}
        \]

     Dreififall :math:`X` lítur svona út:

     .. container:: center

        .. figure:: images/dreififall_binomial.svg
           :width: 291.73pt
           :align: center

Látum :math:`U` tákna rauntölu á bilinu :math:`[0,1]` sem valin er af handahófi, sem þýðir að fyrir sérhvert :math:`a,b \in [0,1]` gildir:

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{P}(a \leq U \leq b) = b-a.
   \end{aligned}
   \]

.. container:: center

   .. figure:: images/jofn_dreifing.svg
      :width: 194.4pt
      :align: center

:math:`U` er sögð hafa **jafna dreifingu** á :math:`[0,1]`.

.. admonition:: Dæmi (framhald).
   :class: box-example

   Látum :math:`U` hafa jafna dreifingu á bilinu :math:`[0,1]`. Dreififallið fyrir :math:`U` lítur svona út:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          F(x) = \mathbb{P}(X \leq x) = \begin{cases}
              0, & x < 0, \\
              x, &0 \leq x \leq 1, \\
              1, & x > 1.
          \end{cases}
      \end{aligned}
      \]

   .. container:: center

      .. figure:: images/jofn_dreifing_dreififall_0_1.svg
         :width: 182.28pt
         :align: center

   Sjá líka: `www.geogebra.org/m/cQeyMaaO <www.geogebra.org/m/cQeyMaaO>`__.

   Almennt, ef :math:`X` hefur jafna dreifingu á :math:`[a,b]`, sem er fjallað um í Lík&töl, þá lítur dreififallið svona út:

   .. math::
        :nowrap:

        \[
        \begin{aligned}
            F(x) = \mathbb{P}(X \leq x) = \begin{cases}
                0, & x < a, \\
                \dfrac{x-a}{b-a}, &a \leq x \leq b, \\
                1, & x > b.
            \end{cases}
        \end{aligned}
        \]

   .. container:: center

      .. figure:: images/jofn_dreifing_dreififall.svg
         :width: 226.72pt
         :align: center

   Sjá líka: `www.geogebra.org/m/cQeyMaaO <www.geogebra.org/m/cQeyMaaO>`__.

Takið eftir að dreififallið fyrir jafna dreifingu er samfellt fall. Þetta er ekki tilviljun: Samfelldar slembistærðir, sem fjallað verður um í Lík&töl, hafa alltaf samfelld dreififöll. Í Lík&töl sjáum við fleiri dæmi um samfelldar slembistærðir, t.d. stærðir með veldisdreifingu og normaldreifingu.

Eiginleikar dreififalla
~~~~~~~~~~~~~~~~~~~~~~~

Munið úr Lík&töl að slembistærð er einfaldlega fall :math:`X: \Omega \to \mathbb{R}`. Munið líka að ef :math:`A` er bil, þá inniheldur atburðurinn :math:`\{X \in A\}` allar útkomur sem leiða til þess að :math:`X` tekur gildi innan bilsins :math:`A`. Formlega er

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \{X \in A\} := \{\omega \in \Omega: X(\omega) \in A\}.
   \end{aligned}
   \]

.. container:: center

   .. figure:: images/slembistaerd_atburdur_A.svg
      :width: 345.02pt
      :align: center

Við setjum nú fram og sönnum setningu sem lýsir helstu eiginleikum dreififalla.

.. admonition:: Setning 4.
   :class: box-theorem

   Um dreififall :math:`F: \mathbb{R} \to \mathbb{R}` fyrir slembistærð :math:`X` gildir:

   (1) Fyrir :math:`x < y` gildir að :math:`0 \leq F(x) \leq F(y) \leq 1`, þ.e. :math:`F` er vaxandi fall sem tekur gildi milli 0 og 1.

   (2) :math:`\lim_{x \to -\infty} F(x) = 0`.

   (3) :math:`\lim_{x \to \infty} F(x) = 1`.

   (4) :math:`F` er samfellt frá hægri, þ.e. fyrir sérhvert :math:`x \in \mathbb{R}` gildir að :math:`\lim_{y \to x^+} F(y) = F(x)`.

.. admonition:: Athugasemd.
   :class: box-remark

   Skoðið vel hvern og einn eiginleika þangað til ykkur finnst augljóst að dreififall hljóti að hafa þá. Hugsið um dæmin sem við höfum séð:

   .. container:: center

      .. figure:: images/dreififoll_daemi.svg
         :width: 422.77pt
         :align: center

   Sjá líka: `www.geogebra.org/m/cQeyMaaO <www.geogebra.org/m/cQeyMaaO>`__.

.. admonition:: Sönnun.
   :class: box-theorem

   (1) | Ef :math:`x < y` gildir að :math:`\{X \leq x\} \subseteq \{X \leq y\}`. Þá fæst skv. lið (5) í Setningu 1 að :math:`\mathbb{P}(X \leq x) \leq \mathbb{P}(X \leq y)` þ.e. :math:`F(x) \leq F(y)`.

       .. container:: center

          .. figure:: images/x_y_mynd.svg
             :width: 241.93pt
             :align: center

       :math:`F(x) \geq 0` gildir samkvæmt öðrum grundvallareiginleika líkinda og :math:`F(x) \leq 1` gildir samkvæmt lið (8) í Setningu 1.

.. admonition:: Athugasemd.
   :class: box-remark

   Munið að :math:`\{X \leq x\}` og :math:`\{X \leq y\}` eru eftirfarandi atburðir:

   .. math::
        :nowrap:

        \[
        \begin{aligned}
            & \{X \leq x\} := \{\omega \in \Omega: X(\omega) \leq x\}, \\
            & \{X \leq y\} := \{\omega \in \Omega: X(\omega) \leq y\}.
        \end{aligned}
        \]

   Ef við viljum sýna formlega að :math:`\{X \leq x\} \subseteq \{X \leq y\}` þurfum við að sýna að sérhvert stak (útkoma) í atburðinum :math:`\{X \leq x\}` sé líka stak í atburðinum :math:`\{X \leq y\}`. Þetta er einfalt mál: Ef :math:`\omega \in \Omega` er þannig að :math:`X(\omega) \leq x` og við vitum að :math:`x < y`, þá gildir líka að :math:`X(\omega) \leq y`, sem þýðir að :math:`\omega \in \{X \leq y\}`.

   Óformlega: Ef :math:`X \leq x` og :math:`x<y`, þá er :math:`X \leq y`.

.. admonition:: Sönnun (framhald).
   :class: box-theorem

   (2) Skv. lið (1) er :math:`F` vaxandi og takmarkað fall, sem þýðir að :math:`\lim_{x \to -\infty} F(x)` er til. Þá gildir að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \lim_{x \to -\infty} F(x) = \lim_{x \to -\infty} \mathbb{P}(X \leq x) = \lim_{n \to \infty} \mathbb{P}(X \leq -n),
          \end{aligned}
          \]

       þar sem í seinna markgildinu táknar :math:`n` jákvæða heiltölu. Athugum að :math:`\{X \leq -n\} \downarrow \varnothing` þegar :math:`n \to \infty`. Þess vegna gefur samfelldni líkinda og liður (1) í Setningu 1:

       .. math:: \lim_{n \to \infty} \mathbb{P}(X \leq -n) = \mathbb{P}(\varnothing) = 0.

       .. container:: center

          .. figure:: images/minus_n_mynd.svg
             :width: 241.93pt
             :align: center

   (3) Skv. lið (1) er :math:`F` vaxandi og takmarkað fall, sem þýðir að :math:`\lim_{x \to \infty} F(x)` er til. Þá gildir að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \lim_{x \to \infty} F(x) = \lim_{x \to \infty} \mathbb{P}(X \leq x) = \lim_{n \to \infty} \mathbb{P}(X \leq n)
          \end{aligned}
          \]

       þar sem í seinna markgildinu táknar :math:`n` jákvæða heiltölu. Athugum að :math:`\{X \leq n\} \uparrow \Omega` þegar :math:`n \to \infty`. Þess vegna gefur samfelldni líkinda og fyrsti grundvallareiginleiki líkinda:

       .. math:: \lim_{x \to \infty} F(x) = \lim_{n \to \infty} \mathbb{P}(X \leq n) = \mathbb{P}(\Omega) = 1.

       .. container:: center

          .. figure:: images/plus_n_mynd.svg
             :width: 241.93pt
             :align: center

   (4) Látum :math:`x \in \mathbb{R}`. Skv. lið (1) er :math:`F` vaxandi og takmarkað fall, sem þýðir að :math:`\lim_{y \to x^+} F(y)` er til. Þá gildir að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \lim_{y \to x^+} F(y) = \lim_{y \to x^+} \mathbb{P}(X \leq y) = \lim_{n \to \infty} \mathbb{P}(X \leq x+1/n)
          \end{aligned}
          \]

       þar sem í seinna markgildinu táknar :math:`n` jákvæða heiltölu. Athugum að :math:`\{X \leq x+1/n\} \downarrow \{X \leq x\}` þegar :math:`n \to \infty`. Samfelldni líkinda gefur þá að

       .. math:: \lim_{y \to x^+} F(y) = \lim_{n \to \infty} \mathbb{P}(X \leq x+1/n) = \mathbb{P}(X \leq x) = F(x).

       .. container:: center

          .. figure:: images/einnamotinmynd.svg
             :width: 241.93pt
             :align: center

.. admonition:: Athugasemd.
   :class: box-remark

   Ef við setjum :math:`A_n := \{X \leq x+1/n\}` fyrir :math:`n \geq 1`, þá er einfalt að sýna að :math:`(A_n)_{n \geq 1}` er minnkandi mengjaruna sem stefnir á :math:`\bigcap_{n=1}^\infty A_n = \bigcap_{n=1}^\infty \{X \leq x+1/n\}`. Til að sýna formlega að

   .. math:: \textstyle \bigcap_{n=1}^\infty \{X \leq x+1/n\} = \{X \leq x\}

   þarf að sýna að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          &\textstyle \bigcap_{n=1}^\infty \{X \leq x+1/n\} \subseteq \{X \leq x\} \\
          \text{og}\quad &\textstyle \{X \leq x\} \subseteq \bigcap_{n=1}^\infty \{X \leq x+1/n\}.
      \end{aligned}
      \]

   Seinni staðhæfingin er auðveld: Ef :math:`\omega \in \Omega` er þannig að :math:`X(\omega) \leq x`, þá er :math:`X(\omega) \leq x+1/n` fyrir öll :math:`n \geq 1`. Fyrir fyrri staðhæfinguna athugum við að ef :math:`\omega \in \Omega` er þannig að :math:`X(\omega) \leq x+1/n` fyrir öll :math:`n \geq 1`, þá fæst með því að senda :math:`n \to \infty` að :math:`X(\omega) \leq x`, þar sem :math:`x+ 1/n \to x` þegar :math:`n \to \infty`.

.. admonition:: Setning 5.
   :class: box-theorem

   Látum :math:`F: \mathbb{R} \to \mathbb{R}` vera fall með eiginleikana fjóra í Setningu 4. Þá er til slembistærð :math:`X` sem hefur fallið :math:`F` sem dreififall.

.. container:: center

   .. figure:: images/dreififall_almennt.svg
      :width: 242.9pt
      :align: center

Saman segja Setningar 4 og 5 að :math:`F: \mathbb{R} \to \mathbb{R}` er dreififall slembistærðar ef og aðeins ef það hefur eiginleikana fjóra í Setningu 4. Almennt getum við kallað föll sem hafa þessa fjóra eiginleika dreififöll án tilvísunar til tiltekinnar slembistærðar.

.. admonition:: Setning 6.
   :class: box-theorem

   Um dreififall :math:`F: \mathbb{R} \to \mathbb{R}` fyrir slembistærð :math:`X` gildir:

   (1) Fyrir sérhvert :math:`x \in \mathbb{R}` gildir að :math:`F` hefur markgildi frá vinstri í :math:`x` og :math:`F(x-) = \mathbb{P}(X < x)`, þar sem :math:`F(x-) := \lim_{y \to x^-} F(y)`.

   (2) Fyrir sérhvert :math:`x \in \mathbb{R}` gildir að :math:`\mathbb{P}(X = x) = F(x) - F(x-)`.

.. admonition:: Sönnun.
   :class: box-theorem

   Æfing.

Saman lýsa Setningar 4 og 6 helstu eiginleikum dreififalla. Eftirfarandi mynd dregur þessa eiginleika saman:

.. container:: center

   .. figure:: images/drefifall_mynd_in.svg
      :width: 489.16pt
      :align: center

Slembistærðir sem eru hvorki strjálar né samfelldar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Í þessu námskeiði gerum við almennt ráð fyrir að slembistærðir séu annaðhvort strjálar eða samfelldar. Hins vegar eru til slembistærðir sem eru hvorki strjálar né samfelldar. Til dæmis segir Setning 5 að til er slembistærð með eftirfarandi dreififall:

.. container:: center

   .. figure:: images/dreififall_almennt.svg
      :width: 242.9pt
      :align: center

Þessi slembistærð getur hvorki verið strjál né samfelld, þar sem dreififallið er hvorki þrepafall né samfellt fall. Við þurfum mál- og tegurfræði til að fjalla um slíkar slembistærðir, t.d. væntigildi þeirra, eins og gert er í STÆ418M Grundvelli líkindafræðinnar. Við getum hins vegar sett fram einfalt dæmi sem við gerum til fróðleiks.

.. admonition:: Dæmi
   :class: box-example

   Látum :math:`X` vera Bernoulli stærð með stika :math:`p = 1/2`, látum :math:`Y` vera slembistærð með jafna dreifingu á bilinu :math:`[1,4]` og látum :math:`Z` vera strjála slembistærð með :math:`\mathbb{P}(Z=2)=1/2` og :math:`\mathbb{P}(Z=3)=1/2`. Gerum ráð fyrir að :math:`X`, :math:`Y` og :math:`Z` séu óháðar og skilgreinum nýja slembistærð

   .. math::

        W = \begin{cases}
            Y, & \text{ef $X=1$,} \\ Z, & \text{ef $X=0$.}
        \end{cases}

   Við sem sagt köstum krónu upp á hvort :math:`W` er samfellda slembistærðin :math:`Y` eða strjála slembistærðin :math:`Z`.

   Látum :math:`x \in \mathbb{R}` og fáum samkvæmt skiptingarreglunni að

   .. math::
        :nowrap:

        \[
        \begin{aligned}
            \mathbb{P}(W \leq x) &= \mathbb{P}(W \leq x, X = 1) + \mathbb{P}(W \leq x, X = 0) \\
            &= \mathbb{P}(Y \leq x, X = 1) + \mathbb{P}(Z \leq x, X= 0), \\
            &= \mathbb{P}(Y \leq x) \mathbb{P}(X=1) + \mathbb{P}(Z \leq x) \mathbb{P}(X=0) \\
            &= \frac12 \cdot \mathbb{P}(Y \leq x) + \frac12 \cdot \mathbb{P}(Z \leq x), \\
            &= \frac12 \cdot \begin{cases} 0, & x < 2, \\ 1/2, & 2 \leq x < 3, \\ 1, & x \geq 3\\\end{cases} + \frac12 \cdot \begin{cases} 0, & x < 1, \\ (x-1)/3, & 1 \leq x \leq 4, \\ 1, & x > 4\\\end{cases} \\
            &= \begin{cases} 0, & x < 1, \\ (x-1)/6, & 1 \leq x < 2, \\ 1/4+(x-1)/6, & 2 \leq x  < 3, \\ 1/2 + (x-1)/6, & 3 \leq x  < 4, \\ 1, & x \geq 4. \end{cases}
        \end{aligned}
        \]


   Strjála slembistærðin :math:`Z` býr til stökkin í 2 og 3, meðan jafndreifða stærðin :math:`Y` gerir það að verkum að dreififallið er bein lína milli :math:`1` og :math:`4` ef horft er framhjá stökkunum.


