Samþéttleiki og veldisstærðir
=============================

Samdreifing tveggja slembistærða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Eins og rætt er í Lík&töl þurfum við oft að fjalla um samdreifingu tveggja slembistærða :math:`X_1` og :math:`X_2` sem tengjast sömu tilrauninni, þ.e. við viljum tala um líkindadreifingu slembivigursins :math:`(X_1,X_2)`. Segjum t.d. að við veljum nemanda af handahófi úr STÆ210G og látum :math:`X_1` tákna einkunn úr fyrri hluta lokaprófs og :math:`X_2` tákna einkunn úr seinni hluta prófsins. Þá gætum við haft áhuga á líkum eins og

.. math:: \mathbb{P}(X_1 \geq 5, X_2 \geq 5),

sem eru líkurnar á að nemandinn nái báðum prófunum. Við gerum almennt ráð fyrir að :math:`X_1` og :math:`X_2` séu skilgreindar á sama útkomumengi :math:`\Omega`, þ.e. :math:`X_1: \Omega \to \mathbb{R}` og :math:`X_2: \Omega \to \mathbb{R}`. Þá er :math:`{\bf X} = (X_1,X_2)` vörpun frá :math:`\Omega` til :math:`\mathbb{R}^2`. Umfjöllunina sem fylgir er einfalt að alhæfa fyrir :math:`n` slembistærðir :math:`X_1,\ldots,X_n`.

Í Lík&töl er fjallað um sammassafall tveggja strjálla slembistærða,

.. math::
   :nowrap:

   \[
   \begin{aligned}
    p(x_1,x_2) := \mathbb{P}(X_1=x_1,X_2=x_2).
   \end{aligned}
   \]

Ef sammassafall strjálla slembistærða :math:`X_1` og :math:`X_2` er þekkt, þá er einfalt að fá massafall t.d. :math:`X_1` svona:

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{P}(X_1 = x) = \sum_{i} \mathbb{P}(X_1=x,X_2=x_i), \quad (\ast)
   \end{aligned}
   \]

þar sem við leggjum saman yfir öll gildin sem :math:`X_2` tekur. Þegar sammassafallið er gefið með töflu fást jaðarmassaföllin með því að reikna raða- og dálksummur eins og við ræddum í Lík&töl.

Samþéttleiki tveggja slembistærða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við skilgreinum nú *samþéttleika*, sem er samfellda útgáfan af sammassafalli.

.. admonition:: Skilgreining 7.
   :class: box-definition

   Fallið :math:`F: \mathbb{R}^2 \to \mathbb{R}` sem skilgreint er með

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          F(x_1,x_2) := \mathbb{P}(X_1 \leq x_1, X_2 \leq x_2), \quad x_1,x_2 \in \mathbb{R},
      \end{aligned}
      \]

   kallast **samdreififall** slembistærðanna :math:`X_1` og :math:`X_2`.

.. admonition:: Skilgreining 8.
   :class: box-definition

   Látum :math:`F` vera samdreififall slembistærðanna :math:`X_1` og :math:`X_2`. Ef til er fall :math:`f: \mathbb{R}^2 \to \mathbb{R}` þannig að :math:`f(x_1,x_2) \geq 0` fyrir öll :math:`x_1,x_2 \in \mathbb{R}` og

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          F(x_1,x_2) = \int_{-\infty}^{x_1} \int_{-\infty}^{x_2} f(y_1,y_2) dy_2 dy_1,
      \end{aligned}
      \]

   þá kallast :math:`f` samþéttleiki slembistærðanna :math:`X_1` og :math:`X_2`.

.. admonition:: Athugasemd.
   :class: box-remark

   Þegar :math:`X_1` og :math:`X_2` hafa samþéttleika, þá er sagt á ensku að :math:`X_1` og :math:`X_2` séu ,,jointly continuous“ (,,samsamfelldar“?). Orðaskrá Stærðfræðafélagsins hefur ekki þýðingu á þessu hugtaki.

Í Stærðfræðigreiningu II lærið þið að

.. math::
   :nowrap:

   \[
   \begin{aligned}
    & \int_{-\infty}^{x_1} \int_{-\infty}^{x_2} f(y_1,y_2) dy_2 dy_1 \\ & = \int_{-\infty}^{x_1} \left(\int_{-\infty}^{x_2} f(y_1,y_2) dy_2\right) dy_1 \\ & = \int_{-\infty}^{x_2} \left(\int_{-\infty}^{x_1} f(y_1,y_2) dy_1\right) dy_2.
   \end{aligned}
   \]

Þegar við reiknum tvöfalda heildið í Skilgreiningu 8 skiptir sem sagt ekki máli hvort heildið er innra heildið. Ef fyrst er heildað yfir :math:`y_2` er litið á :math:`y_1` sem fasta og öfugt. Þegar víxlað er á röð á tvöföldu heildi þarf hins vegar alltaf að gæta þess að mörk heildanna séu uppfærð til samræmis.

.. admonition:: Dæmi
   :class: box-example

   Látum :math:`X_1` og :math:`X_2` vera slembistærðir með samþéttleikann

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              f(x,y) = \begin{cases}
                  \dfrac{xy^2}{72}, & 0<x<4, \; 0<y<3, \\ 0, & \text{annars.}
              \end{cases}
      \end{aligned}
      \]

   Reiknum

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              F(3,2) &= \mathbb{P}(X_1 \leq 3, X_2 \leq 2) \\
              &=  \int_{-\infty}^{3} \int_{-\infty}^{2} f(x,y) dy dx \\
              &= \frac1{72} \int_0^3 \int_0^2 x y^2 dy dx.
      \end{aligned}
      \]

   \ Fáum:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              F(3,2) &= \frac1{72} \int_0^3 \int_0^2 x y^2 dy dx = \frac1{72} \int_0^3 \left( \int_0^2 xy^2 dy\right) dx \\[6pt]
              &= \frac1{72} \int_0^3 x \left(\int_0^2 y^2dy\right) dx = \frac1{72} \int_0^3 x \left[\frac13y^3\right]_0^2 dx \\[6pt]
              &= \frac1{72} \int_0^3  \frac{8}3 x dx = \frac1{27} \int_0^3 x dx \\[6pt]
              &= \frac1{27} \left[\frac12 x^2\right]_0^3 = \frac1{27} \cdot \frac92 = \frac16.
      \end{aligned}
      \]

   Einnig væri hægt að víxla röð á heildunum:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              F(3,2) &= \frac1{72} \int_0^2 \int_0^3 x y^2 dx dy = \frac1{72} \int_0^2 \left( \int_0^3 xy^2 dx\right) dy \\[6pt]
              &= \frac1{72} \int_0^2 y^2 \left(\int_0^3 xdx\right) dy = \frac1{72} \int_0^2 y^2 \left[\frac12x^2\right]_0^3 dy \\[6pt]
              &= \frac1{72} \int_0^2  \frac{9}2 y^2 dy = \frac1{16} \int_0^2 y^2 dy \\[6pt]
              &= \frac1{16} \left[\frac13 y^3\right]_0^2 = \frac1{16} \cdot \frac83 = \frac16.
      \end{aligned}
      \]

Næsta setning segir að ef slembistærðir :math:`X_1` og :math:`X_2` hafa samþéttleika, þá má reikna líkurnar á að :math:`(X_1,X_2)` sé í gefnu mengi með því að heilda samþéttleikann yfir mengið.

.. admonition:: Setning 8.
   :class: box-theorem

   (1) Ef :math:`X_1` og :math:`X_2` hafa samþéttleika :math:`f` og :math:`C \subseteq \mathbb{R}^2` er t.d. rétthyrningur, hringur eða þríhyrningur, þá gildir að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \mathbb{P}\big((X_1,X_2) \in C\big) = \iint_{(x,y) \in C} f(x,y) dA.
          \end{aligned}
          \]

   (2) Ef :math:`X_1` og :math:`X_2` hafa samþéttleika :math:`f`, þá eru :math:`X_1` og :math:`X_2` samfelldar slembistærðir og þéttleiki t.d. :math:`X_1` er gefinn með

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  f_{X_1}(x) = \int_{-\infty}^\infty f(x,y) dy, \quad x \in \mathbb{R}.
          \end{aligned}
          \]

.. admonition:: Athugasemd.
   :class: box-remark

   Jafnvel þótt :math:`X_1` og :math:`X_2` séu samfelldar slembistærðir, þá hafa þær ekki endilega samþéttleika. Með öðrum orðum eru tvær samfelldar slembistærðir ekki endilega samsamfelldar.

.. admonition:: Athugasemd (til fróðleiks).
   :class: box-remark

   Hér sýnum við dæmi um samfelldar slembistærðir sem hafa ekki samþéttleika. Segjum að :math:`X_1` hafi jafna dreifingu á bilinu :math:`[0,1]` og setjum :math:`X_2 = X_1`. Ef til væri samþéttleiki :math:`f: \mathbb{R}^2 \to\mathbb{R}` fyrir :math:`X_1` og :math:`X_2`, þá þyrfti að gilda að :math:`f(x,y) = 0` fyrir :math:`x \neq y`, og við myndum fá:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
               \mathbb{P}(0 \leq X_1 \leq 1,0 \leq X_2 \leq 1) &= \int_{0}^1 \int_0^1 f(x,y) dy dx \\
               &= \int_0^1 \left(\int_{x}^x f(x,y) dy\right) dx \\
               &= 0,
      \end{aligned}
      \]

   sem er mótsögn. Ástæðan fyrir að slembistærðirnar hafa ekki samþéttleika er að þær eru háðar. Vigurinn :math:`(X_1,X_2)` gildi í einvíðu en ekki tvívíðu mengi, sem kemur í veg fyrir að hægt sé að reikna líkur fyrir vigurinn með tvöföldu heildi.

Heildi yfir þríhyrning
~~~~~~~~~~~~~~~~~~~~~~

Hér fyrir neðan þurfum við að reikna tvöfalt heildi yfir þríhyrninginn

.. math::
   :nowrap:

   \[
   \begin{aligned}
    C = \{(x,y): 0 \leq x < y\},
   \end{aligned}
   \]

sem er mengi allra punkta :math:`(x,y)` þannig að bæði hnitin séu :math:`\geq 0` og :math:`y`-hnitið sé stærra en :math:`x`-hnitið.

.. container:: center

   .. figure:: images/þríhyningur.svg
      :width: 177.28pt
      :align: center

Við getum skrifað mengið :math:`C` sem

.. math::
   :nowrap:

   \[
   \begin{aligned}
    C = \{(x,y): x \geq 0 \text{ og } y > x\},
   \end{aligned}
   \]

sem segir að :math:`x` uppfyllir :math:`x \geq 0`, og ef við festum gildið á :math:`x`, þá eru möguleg gildi á :math:`y` allar tölur frá :math:`x` og upp úr.

.. container:: center

   .. figure:: images/þríhyningur_1.svg
      :width: 177.28pt
      :align: center

Við getum líka skrifað mengið :math:`C` sem

.. math::
   :nowrap:

   \[
   \begin{aligned}
    C = \{(x,y): y > 0 \text{ og } 0 \leq x < y\},
   \end{aligned}
   \]

sem segir að :math:`y` uppfyllir :math:`y > 0`, og ef við festum gildið á :math:`y`, þá eru möguleg gildi á :math:`x` allar tölur frá og með 0 og upp í :math:`y`.

.. container:: center

   .. figure:: images/þríhyningur_2.svg
      :width: 177.28pt
      :align: center

Tvöfalda heildið af :math:`f` yfir mengið :math:`C` má þess vegna skrifa á eftirfarandi þrjá vegu:

.. math::
   :nowrap:

   \[
   \begin{aligned}
    & \iint_{(x,y) \in C} f(x,y) dA \\ &= \int_{0}^\infty \left(\int_{x}^\infty f(x,y) dy\right) dx \\ &= \int_0^\infty \left(\int_0^{y} f(x,y) dx\right) dy.
   \end{aligned}
   \]

Ef fyrst er heildað yfir :math:`y` (innra heildið), þá er fyrri framsetningin á menginu :math:`C` notuð. Horft er á :math:`x` sem fast í innra heildinu og möguleg gildi á :math:`y` eru frá :math:`x` og upp úr. Ef fyrst er heildað yfir :math:`x`, þá er seinni framsetningin á :math:`C` notuð. Horft er á :math:`y` sem fast í innra heildinu og möguleg gildi á :math:`x` eru frá 0 og upp í :math:`y`.

Strjál veldisdreifing
~~~~~~~~~~~~~~~~~~~~~

Munið úr Lík&töl að við sögðum að tvær **strjálar** slembistærðir :math:`X` og :math:`Y` væru óháðar ef

.. math:: \mathbb{P}(X=x_i, Y=y_j) = \mathbb{P}(X=x_i) \cdot \mathbb{P}(Y=y_j)

fyrir öll möguleg gildi :math:`x_i` fyrir :math:`X` og :math:`y_j` fyrir :math:`Y`. Til að skilgreina óhæði þannig að það nái líka yfir samfelldar slembistærðir notum við í staðinn líkurnar á að slembistærðirnar taki gildi á bilum.

.. admonition:: Skilgreining 9.
   :class: box-definition

   Slembistærðir :math:`X_1,\ldots,X_n` kallast **óháðar** ef fyrir öll bil :math:`I_1,\ldots,I_n` gildir að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              \mathbb{P}(X_1 \in I_1,\ldots,X_n \in I_n) = \mathbb{P}(X_1 \in I_1) \cdots \mathbb{P}(X_n \in I_n).
      \end{aligned}
      \]

.. admonition:: Setning 9.
   :class: box-theorem

   (1) Slembistærðir :math:`X_1,\ldots,X_n` eru óháðar ef og aðeins ef

       .. math::
          :nowrap:

          \[
          \begin{aligned}
              F(x_1,\ldots,x_n) = F_{X_1}(x_1) \cdots F_{X_n}(x_n)
          \end{aligned}
          \]

       fyrir öll :math:`x_1,\ldots,x_n \in \mathbb{R}`, þar sem :math:`F` er samdreififall :math:`X_1,\ldots,X_n` og :math:`F_{X_i}` er dreififall :math:`X_i` fyrir :math:`i=1,\ldots,n`.

   (2) Strjálar slembistærðir :math:`X_1,\ldots,X_n` eru óháðar ef og aðeins ef

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \mathbb{P}(X_1=x_1,\ldots,X_n=x_n) = \mathbb{P}(X_1=x_1) \cdots \mathbb{P}(X_n=x_n)
          \end{aligned}
          \]

       fyrir öll gildi :math:`x_1,\ldots,x_n` sem :math:`X_1,\ldots,X_n` taka.

   (3) Samfelldar slembistærðir :math:`X_1,\ldots,X_n` eru óháðar ef og aðeins ef þær hafa samþéttleikann

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  f(x_1,\ldots,x_n) = f_{X_1}(x_1) \cdots f_{X_n}(x_n),
          \end{aligned}
          \]

       þar sem :math:`f_{X_i}` táknar þéttleika :math:`X_i` fyrir :math:`i=1,\ldots,n`.

.. admonition:: Athugasemd.
   :class: box-remark

   - Við sáum áðan dæmi um samfelldar slembistærðir :math:`X_1` og :math:`X_2` sem hafa ekki samþéttleika. Í dæminu var :math:`X_2 = X_1` og slembistærðirnar því greinilega háðar.

   - Síðasta setning segir að ef við vitum að slembistærðirnar eru óháðar, þá hafa þær samþéttleika sem fæst með því að margfalda saman jaðarþéttiföllin.

Látum :math:`X_1,X_2,X_3,\ldots` tákna óháðar Bernoulli stærðir með stika :math:`p`, sem lýsa því að bjagaðri krónu sé kastað endurtekið. Látum :math:`N` vera fjölda kasta þar til við sjáum fyrsta þorskinn,

.. math::
   :nowrap:

   \[
   \begin{aligned}
    N := \min\{n \geq 1: X_n = 1\}.
   \end{aligned}
   \]

Ef til dæmis köstin fara eins og sýnt er að neðan er :math:`N=6`.

.. container:: center

   .. figure:: images/geometrisk.svg
      :width: 341.32pt
      :align: center

Við köllum :math:`N` **strjála veldisstærð** með stika :math:`p`.

.. admonition:: Setning 10.
   :class: box-theorem

   Látum :math:`X_1,X_2,\ldots` vera óháðar Bernoulli stærðir með stika :math:`p \in (0,1)`, þ.e. :math:`\mathbb{P}(X_i=1)=p` og :math:`\mathbb{P}(X_i=0)=1-p`. Skilgreinum

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              N := \min\{k \geq 1: X_k = 1\}.
      \end{aligned}
      \]

   Fyrir sérhverja heiltölu :math:`k \geq 1` gildir að

   .. math:: \mathbb{P}(N=k) = (1-p)^{k-1} p

   og

   .. math:: \mathbb{P}(N>k) = (1-p)^k.

.. admonition:: Skilgreining 10.
   :class: box-definition

   Slembistærðin :math:`N` í Setningu 10 kallast strjál veldisstærð með stika :math:`p`, táknað :math:`N \sim {\rm Geo}(p)` (e. geometric).

.. admonition:: Sönnun.
   :class: box-theorem

   Látum :math:`k \geq 1`. Þar sem :math:`X_1,X_2,\ldots,X_k` eru óháðar gildir samkvæmt lið (2) í Setningu 9 að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              \mathbb{P}(N=k) &= \mathbb{P}(X_1=0,\ldots,X_{k-1}=0,X_k=1) \\
              &= \mathbb{P}(X_1=0) \cdots \mathbb{P}(X_{k-1}=0) \mathbb{P}(X_k=1) \\
              &= (1-p)^{k-1}p
      \end{aligned}
      \]

   og

   .. math::
      :nowrap:

      \[
      \begin{aligned}
                      \mathbb{P}(N>k) &= \mathbb{P}(X_1=0,\ldots,X_{k-1}=0,X_k=0) \\
              &= \mathbb{P}(X_1=0) \cdots \mathbb{P}(X_{k-1}=0) \mathbb{P}(X_k=0) \\
              &= (1-p)^{k}.
      \end{aligned}
      \]

(Samfelld) veldisdreifing
~~~~~~~~~~~~~~~~~~~~~~~~~

Við skilgreinum næst samfelldu útgáfuna af veldisstærð. Hún er oft notuð til að lýsa endingartíma hluta, t.d. véla, tækja eða ljósapera. Við minntumst einnig á í Lík&töl að tíminn milli atburða í Poisson-ferli fylgir veldisdreifingu.

.. admonition:: Skilgreining 11.
   :class: box-definition

   Látum :math:`\lambda >0`. Samfelld slembistærð :math:`X` með þéttleika

   .. math::
      :nowrap:

      \[
      \begin{aligned}
                 f(x) = \begin{cases}
              \lambda e^{-\lambda x}, & x \geq 0, \\ 0, & x < 0,
          \end{cases}
          &&
      \end{aligned}
      \]

   .. container:: center

      .. figure:: images/veldisstaerd_thettleiki_unnid.svg
         :width: 165.62pt
         :align: center

   kallast veldisstærð með stika :math:`\lambda`. Við segjum líka að :math:`X` hafi veldisdreifingu með stika :math:`\lambda`, táknað :math:`X \sim {\rm Exp}(\lambda)`.

.. admonition:: Setning 11.
   :class: box-theorem

   Látum :math:`X` vera veldisstærð með stika :math:`\lambda>0`.

   (1) Fyrir sérhvert :math:`x \geq 0` gildir að :math:`\mathbb{P}(X>x) = e^{-\lambda x}`.

   (2) Dreififall :math:`X` er gefið með

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  F_X(x) = \begin{cases} 1-e^{-\lambda x}, & x \geq 0, \\ 0, & x < 0. \end{cases}
          \end{aligned}
          \]

   Sjá: `www.geogebra.org/m/cQeyMaaO <www.geogebra.org/m/cQeyMaaO>`__.

.. admonition:: Sönnun.
   :class: box-theorem

   (1) Athugum að fyrir :math:`x \geq 0` gildir að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \mathbb{P}(X>x) &= \int_x^\infty \lambda e^{-\lambda y} dy = \left[-e^{-\lambda y}\right]_x^\infty = e^{-\lambda x}.
          \end{aligned}
          \]

   (2) Þar sem :math:`\mathbb{P}(A^c) = 1-\mathbb{P}(A)` fyrir sérhvern atburð :math:`A` fæst fyrir :math:`x \geq 0` að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  F_X(x) &= \mathbb{P}(X \leq x) = 1-\mathbb{P}(X>x) = 1-e^{-\lambda x}.
          \end{aligned}
          \]

       Fyrir :math:`x<0` fæst síðan að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  F_X(x) = \int_{-\infty}^x f_X(y) dy = \int_{-\infty}^x 0 dy = 0,
          \end{aligned}
          \]

       sem gefur lið (2).

Einn helsti eiginleiki veldisstærðar er að hún er *minnislaus*, eins og við lýsum nú.

.. admonition:: Skilgreining 12.
   :class: box-definition

   Slembistærð :math:`X` sem uppfyllir :math:`\mathbb{P}(X \geq 0) = 1` kallast **minnislaus** ef fyrir sérhverjar rauntölur :math:`a,b \geq 0` gildir að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          \mathbb{P}(X>a+b \,|\, X>a) = \mathbb{P}(X>b).
      \end{aligned}
      \]

Segjum að endingartíma tækis sé hægt að lýsa með minnislausri slembistærð :math:`X`. Minnisleysið þýðir að ef við vitum að tækið hefur enst :math:`a` daga, þá eru líkurnar á að tækið endist :math:`b` daga til viðbótar jafnar líkunum á að nýtt tæki endist í :math:`b` daga. Með öðrum orðum: Alltaf þegar við spyrjum hverjar líkurnar eru á að tækið endist ákveðinn tíma til viðbótar, þá eru líkurnar óháðar aldri tækisins á þeim tíma sem við spyrjum. Þetta þýðir líka að ef við komum að tæki sem virkar ennþá, þá er meðaltíminn sem tækið endist til viðbótar sá sami og meðalendingartími nýs tækis, sama hversu gamalt tækið er (!).

.. admonition:: Setning 12.
   :class: box-theorem

   Veldisstærð með stika :math:`\lambda>0` er minnislaus.

.. admonition:: Sönnun.
   :class: box-theorem

   Látum :math:`a,b \geq 0`. Samkvæmt lið (1) í Setningu 11 fæst:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          \mathbb{P}(X>a+b | X>a) &= \frac{\mathbb{P}(X>a+b, X>a)}{\mathbb{P}(X>a)}= \frac{\mathbb{P}(X>a+b)}{\mathbb{P}(X>a)} \\
          &= \frac{e^{-\lambda(a+b)}}{e^{-\lambda a}} = \frac{e^{-\lambda a}e^{-\lambda b}}{e^{-\lambda a}} = e^{-\lambda b} \\
          &= \mathbb{P}(X>b).
      \end{aligned}
      \]

.. admonition:: Athugasemd.
   :class: box-remark

   Takið eftir að slembistærðin :math:`X` er minnislaus ef og aðeins ef

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          \mathbb{P}(X>a+b) = \mathbb{P}(X>a)\mathbb{P}(X>b)
      \end{aligned}
      \]

   fyrir öll :math:`a,b \geq 0`. Við höfum sýnt að þetta skilyrði er uppfyllt þegar :math:`\mathbb{P}(X>x) = e^{-\lambda x}` fyrir öll :math:`x \geq 0`. Raunar er unnt að sýna að *engin önnur dreifing* uppfyllir þetta skilyrði,

Minnisleysi veldisstærðarinnar einfaldar mjög greiningu á Poisson-ferlum, en minnisleysið leiðir líka til hegðunar sem virðist oft skrítin þegar fljótt er á litið. Sem dæmi: Ef við göngum inn í Poisson-ferli með stika :math:`\lambda>0`, þá hefur tíminn sem líður fram að næsta atburði veldisdreifingu með stika :math:`\lambda`, sama hversu langt er síðan síðasti atburður gerðist. Þið sýnduð fram á það með hermun í hermunarverkefninu. Þetta hefur í för með sér að bilið sem við göngum inn í er lengra en bil sem valið er af handahófi (raunar er það tvöfalt lengra). Þetta er oft kallað ,,skoðunarþversögnin“.

Dreifing :math:`\min\{X_1,X_2\}` fyrir óháðar veldisstærðir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Segjum að verksmiðja keyri á tveimur tækjum. Tækin eru óháð og endingartímar þeirra eru veldisdreifðir með stika :math:`\lambda_1>0` og :math:`\lambda_2>0`. Látum :math:`X_1` tákna endingartíma fyrra tækisins og :math:`X_2` tákna endingartíma seinna tækisins. Slembistærðin :math:`Z := \min\{X_1,X_2\}` lýsir tímanum sem líður þangað til annað af tækjunum tveimur bilar. Ef bilun á öðru tækinu þýðir framleiðslustöðvun, þá gæti verksmiðjueigandinn haft áhuga á líkindadreifingu :math:`Z`. Til dæmis: Hversu líklegt er að bilun verði yfir næsta árið? Fyrir veldisdreifingu hefur stærðin :math:`Z = \min\{X_1,X_2\}` mjög áhugaverða eiginleika, eins og næsta setning segir.

.. admonition:: Setning 13.
   :class: box-theorem

   Látum :math:`X_1` og :math:`X_2` vera óháðar veldisstærðir með stika :math:`\lambda_1>0` og :math:`\lambda_2>0`. Skilgreinum slembistærðina :math:`Z := \min\{X_1,X_2\}.`

   (1) :math:`Z` er veldisstærð með stika :math:`\lambda_1+\lambda_2`.

   (2) :math:`\mathbb{P}(Z = X_1) = \mathbb{P}(X_1 < X_2) = \dfrac{\lambda_1}{\lambda_1+\lambda_2}`.

.. admonition:: Sönnun.
   :class: box-theorem

   (1) Þar sem :math:`X_1` og :math:`X_2` eru óháðar gildir fyrir sérhvert :math:`x \geq 0` að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \mathbb{P}(Z>x) &= \mathbb{P}(X_1>x,X_2>x) = \mathbb{P}(X_1>x) \mathbb{P}(X_2>x).
          \end{aligned}
          \]

       Þá leiðir af lið (1) í Setningu 11 að fyrir :math:`x \geq 0`:

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \mathbb{P}(Z>x) = e^{-\lambda_1 x} e^{-\lambda_2 x} = e^{-(\lambda_1+\lambda_2)x}.
          \end{aligned}
          \]

       Með því að nota aftur lið (1) í Setningu 11 sjáum við að :math:`Z` hefur veldisdreifingu með stika :math:`\lambda_1+\lambda_2`.

.. admonition:: Athugasemd.
   :class: box-remark

   Tæknilega séð þarf að sanna að ef :math:`\mathbb{P}(Z>x) = e^{-(\lambda_1+\lambda_2)x}` fyrir öll :math:`x \geq 0`, þá hefur :math:`Z` veldisdreifingu með stika :math:`\lambda_1+\lambda_2`. Þar sem :math:`\mathbb{P}(A^c)=1-\mathbb{P}(A)` fyrir sérhvern atburð :math:`A` getum við sagt að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          \mathbb{P}(Z \leq x) = 1-e^{-(\lambda_1+\lambda_2)x}, \quad x \geq 0.
      \end{aligned}
      \]

   Þetta sýnir að :math:`Z` hefur sama dreififall og veldisstærð með stika :math:`\lambda_1+\lambda_2`, og við minntumst á í síðasta fyrirlestri að dreififall :math:`Z` ákvarðar dreifingu :math:`Z` fullkomlega. Það er hins vegar ekki sannað fyrr en í STÆ418M Grundvelli líkindafræðinnar.

.. admonition:: Sönnun (framhald).
   :class: box-theorem

   (2) Þar sem :math:`X_1` og :math:`X_2` eru óháðar gildir samkvæmt lið (3) í Setningu 9 að þær hafa samþéttleikann

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  f(x_1,x_2) = \lambda_1 e^{-\lambda_1 x_1} \cdot \lambda_2 e^{-\lambda_2 x_2} = \lambda_1 \lambda_2 e^{-\lambda_1x_1}e^{-\lambda_2x_2}
          \end{aligned}
          \]

       fyrir :math:`x_1,x_2 \geq 0`.

       Við fáum þá samkvæmt lið (1) í Setningu 8:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              \mathbb{P}(X_1 < X_2)
              &= \int_0^\infty \left(\int_{x}^\infty f(x,y) dy\right) dx \\
              &= \int_0^\infty  \left(\int_{x}^\infty \lambda_1\lambda_2 e^{-\lambda_1 x} e^{-\lambda_2 y}dy\right) dx  \\
                      &= \int_0^\infty \lambda_1 e^{-\lambda_1 x} \left(\int_{x}^\infty \lambda_2 e^{-\lambda_2 y}dy\right) dx \\
              &= \int_0^\infty \lambda_1 e^{-\lambda_1 x} \left[-e^{-\lambda_2 y}\right]_{x}^\infty dx\\
              &= \int_0^\infty \lambda_1 e^{-\lambda_1 x} e^{-\lambda_2 x} dx = \lambda_1 \int_0^\infty e^{-(\lambda_1+\lambda_2)x} dx \\
              &= \lambda_1 \left[-\frac1{\lambda_1+\lambda_2}e^{-(\lambda_1+\lambda_2)x}\right]_0^\infty = \frac{\lambda_1}{\lambda_1+\lambda_2}.
      \end{aligned}
      \]

.. admonition:: Athugasemd.
   :class: box-remark

   Við hefðum líka getað víxlað röðinni á heildunum, samanber glæru 17, en útreikningarnir eru leiðinlegri. Það er samt ágæt æfing að ganga úr skugga um að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              \mathbb{P}(X_1 < X_2) &= \mathbb{P}(X_2 \geq 0, 0 \leq X_1 < X_2) \\
              &= \int_0^\infty \left(\int_0^y f(x,y) dx\right) dy \\
              &= \cdots \\
              &= \frac{\lambda_1}{\lambda_1+\lambda_2}.
      \end{aligned}
      \]

Segjum aftur að endingartímar tækja í verksmiðju séu óháðar veldisstærðir :math:`X_1` og :math:`X_2` með stika :math:`\lambda_1>0` og :math:`\lambda_2>0`. Slembistærðin :math:`W := \max\{X_1,X_2\}` lýsir tímanum sem líður þangað til bæði tækin hafa bilað. Ef verksmiðjan getur starfað áfram á öðru tækinu (væntanlega með skertum afköstum), þá gæti verksmiðjueigandinn haft áhuga á líkindadreifingu :math:`W`. Við skoðum þessa slembistærð nánar í skiladæmum 3. Þar sem :math:`X_1` og :math:`X_2` eru óháðar getum við skrifað

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{P}(W \leq x) &= \mathbb{P}(X_1 \leq x, X_2 \leq x) = \mathbb{P}(X_1 \leq x) \mathbb{P}(X_2 \leq x),
   \end{aligned}
   \]

sem gerir okkur kleift að reikna dreififallið fyrir :math:`W`. Við getum síðan fengið þéttleikann fyrir :math:`W` með því að diffra dreififallið, eins og rætt var í Lík&töl. Í skiladæmunum fáið þið það verkefni að leiða út dreifi- og þéttifall slembistærðarinnar :math:`W`.

Sniðug væntigildisregla
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 14 (sniðug væntigildisregla).
   :class: box-theorem

   (1) Látum :math:`X` vera strjála slembistærð sem tekur gildi í :math:`\{0,1,2,\ldots\}`. Þá gildir að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \mathbb{E}[X] = \sum_{k=0}^\infty \mathbb{P}(X>k).
          \end{aligned}
          \]

   (2) Látum :math:`X` vera samfellda slembistærð með þéttleika :math:`f` sem uppfyllir :math:`f(x) = 0` fyrir :math:`x<0`. Þá gildir að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \mathbb{E}[X] = \int_0^\infty \mathbb{P}(X>x) dx.
          \end{aligned}
          \]

Niðurstaðan í lið (1) er alls ekki augljós við fyrstu sýn, en hún snýst í raun um að reikna summuna í hægri hlið á tvo ólíka vegu.

.. container:: center

   .. figure:: images/summuregla_vaentigildis.svg
      :width: 413.02pt
      :align: center

Segjum að við ætlum að leggja saman allar tölurnar í fylkinu að ofan. Leggjum fyrst saman niður hvern dálk, og leggjum svo saman dálksummurnar. Þannig fæst væntigildi slembistærðarinnar :math:`X`,

.. math:: \mathbb{E}[X] = \sum_{k=1}^\infty k\mathbb{P}(X=k).

Leggjum aftur saman allar tölurnar í fylkinu, en gerum það núna í annarri röð. Leggjum fyrst saman yfir hverja röð (línu) í fylkinu, og leggjum svo saman raðasummurnar. Þannig fæst :math:`\sum_{k=0}^\infty \mathbb{P}(X>k)`.

.. container:: center

   .. figure:: images/summuregla_vaentigildis_2.svg
      :width: 566.48pt
      :align: center

Með því að leggja tölurnar í fylkinu saman í mismunandi röð fæst sem sagt að

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{E}[X] = \sum_{k=1}^\infty k\mathbb{P}(X=k) = \sum_{k=0}^\infty \mathbb{P}(X>k).
   \end{aligned}
   \]

Þessir útreikningar gefa okkur tilfinningu fyrir því hvers vegna reglan gildir, en hér fyrir neðan setjum við fram nákvæma sönnun.

.. admonition:: Sönnun.
   :class: box-theorem

   (1) Tökum fyrst eftir að fyrir sérhverja heiltölu :math:`n \geq 0` gildir að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                      \sum_{k=0}^\infty 1_{\{k < n\}} = \sum_{k=0}^{n-1} 1 + \sum_{k=n}^\infty 0 = n. \quad (\ast)
          \end{aligned}
          \]

       Því fæst:

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                      \mathbb{E}[X] &= \mathbb{E}\left[\sum_{k=0}^\infty 1_{\{X>k\}}\right] \qquad \text{(skv.~$(\ast)$)} \\
                      &= \sum_{k=0}^\infty \mathbb{E}[1_{\{X>k\}}] \qquad \text{(væntigildi er línulegt)}\\
                      &= \sum_{k=0}^\infty \mathbb{P}(X>k).
          \end{aligned}
          \]

.. admonition:: Athugasemd.
   :class: box-remark

   Þessi sönnun er annað dæmi um hversu gagnleg kenniföll geta verið til að sanna staðreyndir um líkindi. Við hins vegar svindluðum aðeins í þessari sönnun, þar sem hér erum við að taka væntigildi af óendanlegri summu slembistærða. Til að réttlæta skrefið

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          \mathbb{E}\left[\sum_{k=0}^\infty 1_{\{X>k\}}\right] = \sum_{k=0}^\infty \mathbb{E}[1_{\{X>k\}}]
      \end{aligned}
      \]

   þarf almenna útgáfu af Fubini-setningunni sem fjallað er um í STÆ402M Mál- og tegurfræði eða STÆ418M Grundvelli líkindafræðinnar.

.. admonition:: Sönnun (framhald.)
   :class: box-theorem

   (2) Með því að nota að :math:`\mathbb{P}(X>x) = \int_x^\infty f(y)dy` fáum við

       .. math::
          :nowrap:

          \[
          \begin{aligned}
              \int_0^\infty \mathbb{P}(X>x) dx
              &= \int_0^\infty \left(\int_x^\infty f(y) dy\right) dx \\
              &= \int_0^\infty \left(\int_0^y f(y) dx\right) dy \\
              &= \int_0^\infty f(y) \left(\int_0^y dx\right) dy \\
              &= \int_0^\infty y f(y) dy \\
              &=  \mathbb{E}[X],
          \end{aligned}
          \]

       þar sem í öðru skrefinu víxluðum við röðinni á heildunum og í síðasta skrefinu notuðum við að :math:`f(x)=0` fyrir :math:`x<0`.

Við sýnum núna hvernig sniðuga væntigildisreglan getur nýst til að einfalda útreikninga.

.. admonition:: Setning 15.
   :class: box-theorem

   (1) Látum :math:`X` vera strjála veldisstærð með stika :math:`p \in (0,1)`. Þá gildir að :math:`\mathbb{E}[X]=1/p`.

   (2) Látum :math:`X` vera veldisstærð með stika :math:`\lambda>0`. Þá gildir að :math:`\mathbb{E}[X]=1/\lambda`.

.. admonition:: Sönnun.
   :class: box-theorem

   (1) Samkvæmt sniðugri væntigildisreglu

       og Setningu 10 fæst:

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \mathbb{E}[X] &= \sum_{k=0}^\infty \mathbb{P}(X>k) = \sum_{k=0}^\infty (1-p)^k = \frac1{1-(1-p)} = \frac1p.
          \end{aligned}
          \]

   (2) Samkvæmt sniðugri væntigildisreglu

       og lið (1) í Setningu 11 fæst:

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \mathbb{E}[X] &= \int_0^\infty \mathbb{P}(X>x) dx = \int_0^\infty e^{-\lambda x} dx = \frac1\lambda.
          \end{aligned}
          \]

.. admonition:: Athugasemd.
   :class: box-remark

   - Ef :math:`X` er strjál veldisstærð með stika :math:`p \in (0,1)`, þá gildir samkvæmt skilgreiningu á væntigildi að

     .. math::
        :nowrap:

        \[
        \begin{aligned}
                \mathbb{E}[X] = \sum_{k=1}^\infty k \cdot (1-p)^{k-1} p.
        \end{aligned}
        \]

     Liður (1) í Setningu 15 segir okkur þá að

     .. math::
        :nowrap:

        \[
        \begin{aligned}
                \sum_{k=1}^\infty k (1-p)^{k-1} p = \frac1p \quad\text{þ.e.}\quad \sum_{k=1}^\infty k (1-p)^{k-1} = \frac{1}{p^2}.
        \end{aligned}
        \]

     Það væri venjulega verkefni stærðfræðigreiningar að reikna :math:`\sum_{k=1}^\infty k (1-p)^{k-1}`. Hér sjáum við hvernig hægt er að reikna summuna með því að tengja hana við væntigildi strjállar veldisstærðar og reikna væntigildið á tvo ólíka vegu.

   - Ef :math:`X` er veldisstærð með stika :math:`\lambda>0`, þá gildir samkvæmt skilgreiningu á væntigildi að

     .. math::
        :nowrap:

        \[
        \begin{aligned}
                \mathbb{E}[X] = \int_0^\infty x \cdot \lambda e^{-\lambda x}dx.
        \end{aligned}
        \]

     Samkvæmt lið (2) í Setningu 15 fæst þá að

     .. math::
        :nowrap:

        \[
        \begin{aligned}
                \int_0^\infty x \cdot \lambda e^{-\lambda x}dx = \frac1\lambda \quad\text{þ.e.}\quad  \int_0^\infty x e^{-\lambda x}dx = \frac1{\lambda^2},
        \end{aligned}
        \]

     sem er samfellda útgáfan af formúlunni sem við fengum áðan fyrir strjálu veldisstærðina.


