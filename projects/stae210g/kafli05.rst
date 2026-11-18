Skilyrt væntigildi
==================

Skilyrt væntigildi: Skilgreining
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`(\Omega,{\cal F},\mathbb{P})` vera líkindarúm og látum :math:`A,B \in {\cal F}` vera atburði þannig að :math:`\mathbb{P}(B)>0`. Munið úr Lík&töl að skilyrtu líkurnar á :math:`A` gefið :math:`B` eru skilgreindar með

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{P}(A|B) := \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}.
   \end{aligned}
   \]

Hugmyndin er sú að við reiknum líkurnar á :math:`A` eins og :math:`B` sé útkomurúmið, þ.e. við skoðum bara þann hluta :math:`A` sem er innan :math:`B` og við reiknum líkurnar sem hlutfall af :math:`\mathbb{P}(B)`.

.. container:: center

   .. figure:: images/skilyrt_likindi.svg
      :width: 208.25pt
      :align: center

.. admonition:: Skilgreining 13.
   :class: box-definition

   Látum :math:`X` og :math:`Y` vera strjálar slembistærðir og látum :math:`y \in \mathbb{R}` vera þannig að :math:`\mathbb{P}(Y=y)>0`. Skilyrt væntigildi :math:`X` gefið :math:`Y=y` er táknað með :math:`\mathbb{E}[X|Y=y]` og skilgreint með

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              \mathbb{E}[X|Y=y] := \sum_{i} x_i \mathbb{P}(X=x_i|Y=y),
      \end{aligned}
      \]

   þar sem summan nær yfir öll gildin sem :math:`X` tekur.

Munið að væntigildi strjállar slembistærðar :math:`X` er skilgreint með

.. math::
   :nowrap:

   \[
   \begin{aligned}
           \mathbb{E}[X] = \sum_i x_i \mathbb{P}(X=x_i).
   \end{aligned}
   \]

Skilgreiningin á skilyrtu væntigildi er algjörlega hliðstæð nema nú eru líkindin skilyrt með atburðinum :math:`\{Y=y\}`.

.. admonition:: Dæmi.
   :class: box-example

   Látum :math:`X_1`, :math:`X_2` og :math:`X_3` vera óháðar Bernoulli-stærðir með stika :math:`p \in (0,1)` og setjum

   .. math::
      :nowrap:

      \[
      \begin{aligned}
             S_3 := X_1+X_2+X_3.
      \end{aligned}
      \]

   :math:`X_1`, :math:`X_2` og :math:`X_3` lýsa útkomunum úr óháðum krónuköstum og :math:`S_3` hefur tvíkostadreifingu með stika :math:`n=3` og :math:`p`. Sýnum að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
             \mathbb{E}[X_1|S_3=2] = 2/3.
      \end{aligned}
      \]

   Takið eftir að niðurstaðan er óháð gildinu á :math:`p`.

.. admonition:: Lausn.
   :class: box-example

   Samkvæmt skilgreiningunni á skilyrtu væntigildi er

   .. math::
      :nowrap:

      \[
      \begin{aligned}
            \mathbb{E}[X_1|S_3=2] &= 1 \cdot \mathbb{P}(X_1=1|S_3=2) + 0 \cdot \mathbb{P}(X_1=0|S_3=2) \\
            &= \mathbb{P}(X_1=1|S_3=2).
      \end{aligned}
      \]

   Til að reikna líkurnar :math:`\mathbb{P}(X_1=1|S_3=2)` er einfaldast að taka eftir að þrjár leiðir eru til að fá tvo þorska í fyrstu þremur köstunum: :math:`(1,1,0)`, :math:`(1,0,1)` og :math:`(0,1,1)`. Þar sem sérhver af þessum útkomum er jafnlíkleg (líkurnar eru :math:`p^2(1-p)`), og tvær þeirra fela í sér að þorskurinn komi upp í fyrsta kasti, þá er

   .. math::
      :nowrap:

      \[
      \begin{aligned}
            \mathbb{P}(X_1=1|S_3=2) = 2/3,
      \end{aligned}
      \]

   óháð gildinu á :math:`p`, sem þýðir að :math:`\mathbb{E}[X_1|S_3=2] = 2/3`.

.. admonition:: Athugasemd.
   :class: box-remark

   Athugið að væntigildi :math:`X_1` (óskilyrt) er

   .. math::
      :nowrap:

      \[
      \begin{aligned}
            \mathbb{E}[X_1] &= 1 \cdot \mathbb{P}(X_1=1) + 0 \cdot \mathbb{P}(X_1=0) = p.
      \end{aligned}
      \]

   Segjum til dæmis að :math:`p=1/2`, þ.e. að venjulegri krónu sé kastað. Í sérhverju krónukasti eru þá helmingslíkur á að þorskurinn komi upp. Ef við hins vegar vitum að krónunni var kastað þrisvar og að þorskurinn kom tvisvar upp, þá aukast líkurnar á að þorskurinn hafi komið upp í fyrsta kastinu. Þess vegna hækkar væntigildi :math:`X_1` þegar við skilyrðum með :math:`S_3=2`.

Lykilsetning um skilyrt væntigildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rifjum upp **skiptingarregluna** úr Lík&töl sem fjallaði um skilyrtar líkur: Ef atburðirnir :math:`B_1,B_2,\ldots,B_n` mynda skiptingu á :math:`\Omega`, þá gildir að

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{P}(A) & = \sum_{i=1}^n \mathbb{P}(A|B_i) \mathbb{P}(B_i).
   \end{aligned}
   \]

.. container:: center

   .. figure:: images/skipting_mynd_A.svg
      :width: 206.74pt
      :align: center

Hliðstæð regla gildir um skilyrt væntigildi, nema hún fjallar um væntigildi í staðinn fyrir líkur og atburðirnir sem mynda skiptingu á :math:`\Omega` eru á forminu :math:`\{Y=y_j\}` þar sem :math:`y_j` getur verið sérhvert af mögulegum gildum :math:`Y`.

.. admonition:: Lykilsetning um skilyrt væntigildi: Fyrsta útgáfa.
   :class: box-example

   Látum :math:`X` og :math:`Y` vera strjálar slembistærðir. Þá gildir að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
             \sum_j \mathbb{E}[X|Y=y_j]\mathbb{P}(Y=y_j) = \mathbb{E}[X],
      \end{aligned}
      \]

   þar sem summan nær yfir öll gildin sem :math:`Y` tekur.

.. admonition:: Dæmi.
   :class: box-example

   Segjum að við ætlum að reikna meðaleinkunn nemenda í STÆ210G. Skiptingin milli námsbrauta er eftirfarandi:

   .. container:: center

      ======== ================== ======
      Hópnúmer Námsbraut          Fjöldi
      ======== ================== ======
      1        Hagnýtt stærðfræði 15
      2        Stærðfræði         15
      3        Aðrar námsbrautir  9
      Alls                        39
      ======== ================== ======

   Látum :math:`X` tákna einkunn nemanda sem valinn er af handahófi og látum :math:`Y` tákna hópnúmer nemandans sem valinn er. Athugum að :math:`\mathbb{E}[X]` er einfaldlega meðaleinkunn nemenda í námskeiðinu og :math:`\mathbb{P}(Y=n)` er hlutfall nemenda sem er í hópi númer :math:`n`, þ.e. :math:`\mathbb{P}(Y=1) = 15/39`, :math:`\mathbb{P}(Y=2)=15/39` og :math:`\mathbb{P}(Y=3)=9/39`. Skilyrta væntigildið :math:`\mathbb{E}[X|Y=n]` er einfaldlega meðaleinkunn nemenda í hópi númer :math:`n`. Setningin

   .. math::
      :nowrap:

      \[
      \begin{aligned}
             \sum_{n=1}^3 \mathbb{E}[X|Y=n]\mathbb{P}(Y=n) = \mathbb{E}[X]
      \end{aligned}
      \]

   segir þá að ef við reiknum fyrst meðaleinkunn nemenda í hverjum hópi fyrir sig, og vegum síðan meðaleinkunn hvers hóps með hlutfallsstærð hópsins, þá fáum við meðaleinkunn allra nemenda í námskeiðinu. Setningin lýsir þess vegna einni aðferð við að reikna meðaleinkunn nemendanna í námskeiðinu: Að skipta nemendum í hópa og reikna meðaleinkunnir einstakra hópa áður en niðurstöðurnar eru teknar saman í eitt meðaltal.

.. admonition:: Sönnun.
   :class: box-theorem

   Munum að ef við þekkjum sammassafall :math:`X` og :math:`Y`, þá má fá massafall :math:`X` svona:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          \mathbb{P}(X=x) = \sum_j \mathbb{P}(X=x,Y=y_j). \quad (\ast)
      \end{aligned}
      \]

   Notum fyrst skilgreininguna á skilyrtu væntigildi og skilyrtum líkum til að fá:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
             & \sum_j \mathbb{E}[X|Y=y_j]\mathbb{P}(Y=y_j) \\
             &= \sum_j \left(\sum_i x_i \mathbb{P}(X=x_i|Y=y_j)\right) \mathbb{P}(Y=y_j) \\
             &= \sum_j \left(\sum_i x_i \mathbb{P}(X=x_i|Y=y_j)\mathbb{P}(Y=y_j)\right) \\
             &= \sum_j \left(\sum_i x_i \mathbb{P}(X=x_i,Y=y_j)\right).
      \end{aligned}
      \]

   Víxlum nú á summunum tveimur og fáum:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
                 & \sum_j \mathbb{E}[X|Y=y_j]\mathbb{P}(Y=y_j) \\
             &= \sum_i \left(\sum_j x_i \mathbb{P}(X=x_i, Y=y_j)\right) \\
             &= \sum_i x_i \left(\sum_j \mathbb{P}(X=x_i, Y=y_j)\right) \\
             &= \sum_i x_i \mathbb{P}(X=x_i) \qquad (\text{samkvæmt $(\ast)$}) \\
             &= \mathbb{E}[X]. \qquad (\text{samkvæmt skilgreiningu á væntigildi})
      \end{aligned}
      \]

.. admonition:: Athugasemd.
   :class: box-remark

   Skilyrt væntigildi er líka einfalt að skilgreina fyrir samfelldar slembistærðir. Mun flóknara er að skilgreina skilyrt væntigildi fyrir slembistærðir sem eru hvorki strjálar né samfelldar. Fræðin bakvið það eru hins vegar skemmtileg eins og fjallað er um í STÆ418M Grundvelli líkindafræðinnar.

Dæmi um notkun lykilsetningar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi.
   :class: box-example

   Mús byrjar í miðju völundarhúss. Alltaf þegar hún er í miðjunni velur hún einhverja af þremur mögulegum dyrum af handahófi. Ef hún velur fyrstu dyrnar endar hún aftur í miðjunni eftir 5 mínútur. Ef hún velur aðrar dyrnar endar hún aftur í miðjunni eftir 7 mínútur. Ef hún velur þriðju dyrnar kemst hún út úr völundarhúsinu á 3 mínútum. Hver er væntur tími sem tekur músina að komast út úr völundarhúsinu?

   .. container:: center

      .. figure:: images/mus_mynd.svg
         :width: 192.74pt
         :align: center

.. admonition:: Lausn.
   :class: box-example

   Látum :math:`X` tákna tímann sem tekur músina að komast út úr völundarhúsinu og látum :math:`Y` vera númer dyranna sem músin velur fyrst. Ef :math:`Y=1` tekur músina 5 mínútur að komast aftur í miðjuna og ekkert hefur áunnist, því að sama ferlið tekur við aftur (hún byrjar í raun upp á nýtt). Ef :math:`Y=2` tekur músina 7 mínútur að komast aftur í miðjuna og við byrjum upp á nýtt. Ef :math:`Y=3` kemst músin út á þremur mínútum. Þess vegna gildir að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          & \mathbb{E}[X|Y=1] = 5 + \mathbb{E}[X], \\
          & \mathbb{E}[X|Y=2] = 7 + \mathbb{E}[X], \\
          & \mathbb{E}[X|Y=3] = 3.
      \end{aligned}
      \]

   Þá fæst skv. lykilsetningunni um skilyrt væntigildi:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          \mathbb{E}[X]
          &= \textstyle
          \mathbb{E}[X|Y=1] \mathbb{P}(Y=1) + \mathbb{E}[X|Y=2] \mathbb{P}(Y=2) \\
          &\quad + \mathbb{E}[X|Y=3] \mathbb{P}(Y=3) \\
          &= (5+\mathbb{E}[X]) \cdot \frac13+ (7+\mathbb{E}[X]) \cdot \frac13 + 3 \cdot \frac13 \\
          &= \frac{2}3 \mathbb{E}[X] + 5,
      \end{aligned}
      \]

   sem gefur :math:`\frac13 \mathbb{E}[X] = 5` þ.e. :math:`\mathbb{E}[X] = 15` mínútur.

Fjöldi krónukasta sem þarf til að sjá ákveðna runu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi.
   :class: box-example

   Venjulegri krónu er kastað aftur og aftur. Látum :math:`X_0` tákna fjölda kasta sem þarf til að runan ,,ÞÞ“ sjáist í fyrsta skipti og látum :math:`Y_0` tákna fjölda kasta sem þarf til að runan ,,ÞB“ sjáist í fyrsta skipti. Ef til dæmis köstin fara

   .. math::
        :nowrap:

        \[
        \begin{aligned}
            \text{BBÞBBÞÞ},
        \end{aligned}
        \]

   þá er :math:`X_0 = 7` og :math:`Y_0 = 4`.

   Ljóst er að ef við köstum krónu tvisvar eru ÞÞ og ÞB jafnlíklegar útkomur, en ef við köstum aftur og aftur, þurfum við að jafnaði að bíða jafn lengi eftir að fá þessar tvær runur? Til að svara því reiknum við væntan fjölda kasta sem þarf til að sjá hvora runu, :math:`\mathbb{E}[X_0]` og :math:`\mathbb{E}[Y_0]`.

.. admonition:: Lausn.
   :class: box-example

   Finnum fyrst :math:`\mathbb{E}[X_0]`. Látum :math:`I` vera Bernoulli-stærð sem lýsir niðurstöðu fyrsta krónukastsins og látum :math:`X_{\text{Þ}}` tákna fjölda kasta sem þarf til að fá ef við byrjum með Þ. Athugum að

   .. math::
        :nowrap:

        \[
        \begin{aligned}
            & \mathbb{E}[X_0 | I = 1] = 1 + \mathbb{E}[X_{\text{Þ}}], \\
            & \mathbb{E}[X_0 | I=0] = 1 + \mathbb{E}[X_0].
        \end{aligned}
        \]

   Þá fæst samkvæmt lykilsetningunni um skilyrt væntigildi:

   .. math::
        :nowrap:

        \[
        \begin{aligned}
             \mathbb{E}[X_0] &= \mathbb{E}[X_0 | I=1] \mathbb{P}(I=1) + \mathbb{E}[X_0 | I=0] \mathbb{P}(I=0) \\
            &= (1+\mathbb{E}[X_{\text{Þ}}]) \cdot \frac12 + (1+\mathbb{E}[X_0]) \cdot \frac12,
        \end{aligned}
        \]

   sem gefur að

   .. math::
        :nowrap:

        \[
        \begin{aligned}
            \frac12 \mathbb{E}[X_0] - \frac12 \mathbb{E}[X_\text{Þ}] = 1.
        \end{aligned}
        \]

   Segjum nú að við byrjum með Þ og látum :math:`J` tákna niðurstöðu næsta krónukasts. Þá er

   .. math::
        :nowrap:

        \[
        \begin{aligned}
            & \mathbb{E}[X_\text{Þ} | J = 1] = 1, \\
            & \mathbb{E}[X_\text{Þ} | J=0] = 1  + \mathbb{E}[X_{0}].
        \end{aligned}
        \]

   Því fæst samkvæmt lykilsetningunni um skilyrt væntigildi:

   .. math::
        :nowrap:

        \[
        \begin{aligned}
             \mathbb{E}[X_\text{Þ}] &= \mathbb{E}[X_\text{Þ} | J=1] \mathbb{P}(J=1) + \mathbb{E}[X_\text{Þ} | J=0] \mathbb{P}(J=0) \\
            &= 1 \cdot \frac12 + (1+\mathbb{E}[X_\text{0}]) \cdot \frac12,
        \end{aligned}
        \]

   sem gefur að

   .. math::
        :nowrap:

        \[
        \begin{aligned}
            - \frac12 \mathbb{E}[X_0] + \mathbb{E}[X_\text{Þ}] = 1.
        \end{aligned}
        \]

   Við höfum þess vegna jöfnuhneppi með tveimur jöfnum:

   .. math::

        \begin{array}{llll}
                \displaystyle \frac12\mathbb{E}[X_0] &\displaystyle-\frac12 \mathbb{E}[X_\text{Þ}] & = & 1  \\[12pt]
                 \displaystyle-\frac12 \mathbb{E}[X_0] & \displaystyle+ \mathbb{E}[X_{\text{Þ}}]  & = & 1.
            \end{array}

   Með því að leggja saman jöfnurnar fæst

   .. math::
        :nowrap:

        \[
        \begin{aligned}
            \frac12 \mathbb{E}[X_\text{Þ}] = 2,
        \end{aligned}
        \]

   sem gefur að :math:`\mathbb{E}[X_\text{Þ}] = 4`. Síðan fæst að

   .. math::
        :nowrap:

        \[
        \begin{aligned}
            \frac12 \mathbb{E}[X_0] - \frac12 \cdot 4 = 1,
        \end{aligned}
        \]

   sem gefur að :math:`\mathbb{E}[X_0] = 6`. Því tekur að jafnaði 6 köst að fá ÞÞ.

   Finnum næst :math:`\mathbb{E}[Y_0]`. Látum :math:`Y_{\text{Þ}}` tákna fjölda kasta sem þarf til að fá ef við byrjum með Þ. Með því að styðjast við mynd er fljótlegt að sjá að

   .. math::
        :nowrap:

        \[
        \begin{aligned}
             \mathbb{E}[Y_0] &= \frac12 (1+\mathbb{E}[Y_\text{Þ}]) + \frac12 (1+\mathbb{E}[Y_0]) \\
            &= 1 + \frac12 \mathbb{E}[Y_\text{Þ}] + \frac12 \mathbb{E}[Y_0], \\
             \mathbb{E}[Y_\text{Þ}] &= \frac12 (1+\mathbb{E}[Y_\text{Þ}]) + \frac12 \cdot 1 = 1 + \frac12 \mathbb{E}[Y_\text{Þ}],
        \end{aligned}
        \]

   sem gefur jöfnuhneppið

   .. math::

        \begin{array}{llll}
                \displaystyle \frac12\mathbb{E}[Y_0] &\displaystyle-\frac12 \mathbb{E}[Y_\text{Þ}] & = & 1  \\[12pt]
                 \displaystyle & \displaystyle \frac12 \mathbb{E}[Y_{\text{Þ}}]  & = & 1.
            \end{array}

   Seinni jafnan gefur að :math:`\mathbb{E}[Y_\text{Þ}] = 2` og fyrri jafnan gefur síðan að

   .. math::
        :nowrap:

        \[
        \begin{aligned}
            \frac12 \mathbb{E}[Y_0] = 1 + \frac12 \mathbb{E}[Y_\text{Þ}],
        \end{aligned}
        \]

   sem gefur að :math:`\mathbb{E}[Y_0] = 4`. Því tekur að jafnaði 4 köst að fá ÞB.

   Þetta dæmi sýnir að við þurfum að jafnaði færri köst til að sjá rununa ÞB en ÞÞ. Hvers vegna er það?

.. admonition:: Dæmi.
   :class: box-example

   Venjulegri krónu er kastað aftur og aftur. Finnum væntan fjölda kasta sem þarf til að sjá rununa ÞÞB.

.. admonition:: Lausn.
   :class: box-example

   Teiknum mynd til að hjálpa okkur að stilla upp jöfnuhneppinu:

   .. container:: center

      .. figure:: images/kedja.svg
         :width: 279.97pt
         :align: center

.. admonition:: Lausn.
   :class: box-example

   Með lykilsetningunni um skilyrt væntigildi fáum við jöfnurnar:

   .. math::
        :nowrap:

        \[
        \begin{aligned}
             \mathbb{E}[X_0] &= \frac12 (1+\mathbb{E}[X_{\text{Þ}}]) + \frac12 (1+ \mathbb{E}[X_0]) \\
            &=  1 + \frac12 \mathbb{E}[X_{\text{Þ}}] + \frac12 \mathbb{E}[X_0] , \\
             \mathbb{E}[X_\text{Þ}] &= \frac12(1+\mathbb{E}[X_\text{ÞÞ}]) + \frac12 (1+\mathbb{E}[X_0]) \\
             &= 1 + \frac12\mathbb{E}[X_\text{ÞÞ}] + \frac12 \mathbb{E}[X_0], \\
             \mathbb{E}[X_\text{ÞÞ}] &= \frac12 (1+\mathbb{E}[X_\text{ÞÞ}]) + \frac12 \cdot 1 \\
             &= 1+ \frac12\mathbb{E}[X_\text{ÞÞ}].
        \end{aligned}
        \]

   Þetta gefur jöfnuhneppið:

   .. math::

        \begin{array}{lllll}
                \displaystyle \frac12\mathbb{E}[X_0] &\displaystyle-\frac12 \mathbb{E}[X_\text{Þ}] & & = & 1  \\[12pt]
                 \displaystyle-\frac12 \mathbb{E}[X_0] & \displaystyle+ \mathbb{E}[X_{\text{Þ}}] & \displaystyle- \frac12 \mathbb{E}[X_\text{ÞÞ}] & = & 1 \\[12pt]
                 &  & \displaystyle  \frac12 \mathbb{E}[X_\text{ÞÞ}] & = & 1.
            \end{array}

   Þriðja jafnan gefur :math:`\mathbb{E}[X_\text{ÞÞ}]=2` og við fáum þá jöfnuhneppið

   .. math::

        \begin{array}{llll}
                \displaystyle \mathbb{E}[X_0]  &\displaystyle- \mathbb{E}[X_\text{Þ}] &  = & 2  \\[12pt]
                 \displaystyle- \mathbb{E}[X_0] & \displaystyle+ 2\mathbb{E}[X_{\text{Þ}}] &  = & 4.
            \end{array}

   Með því að leggja jöfnurnar saman fæst :math:`\mathbb{E}[X_\text{Þ}]=6` og efri jafnan gefur síðan að :math:`\mathbb{E}[X_0] = \mathbb{E}[X_\text{Þ}] + 2 = 8`. Við þurfum því að jafnaði að kasta 8 sinnum til að sjá rununa ÞÞB.

   Á svipaðan hátt má sýna að við þurfum að jafnaði að kasta 8 sinnum til að sjá ÞBB, 10 sinnum til að sjá ÞBÞ og 14 sinnum til að sjá ÞÞÞ.

.. admonition:: Athugasemd.
   :class: box-remark

   Ferlið sem við vorum að skoða er dæmi um **Markov-keðju**, sem færist milli mögulegra ,,ástanda“ samkvæmt gefnum líkum. Við getum lýst þeim með ,,örvaritum“ eins og að neðan.

   .. container:: center

      .. figure:: images/kedja.svg
         :width: 251.98pt
         :align: center

   Markov-keðjur skilgreinast af þeim eiginleika að alltaf þegar keðjan er í tilteknu ástandi, þá er framtíðarþróun keðjunnar aðeins háð núverandi ástandi, ekki því hverju gerðist í fortíðinni.

   Fyrir Markov-keðju getum við alltaf sett upp línulegt jöfnuhneppi sem gerir okkur kleift að reikna út væntan fjölda skrefa sem þarf til að komast úr einu ástandi í annað. Þið lærið meira um þetta ef þið takið STÆ415M Slembiferli.

Önnur framsetning á lykilsetningu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining 14.
   :class: box-definition

   Látum :math:`X` og :math:`Y` vera strjálar slembistærðir. Fyrir sérhvert gildi :math:`y_j` sem :math:`Y` tekur skilgreinum við fallið

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          g(y_j) := \mathbb{E}[X|Y=y_j].
      \end{aligned}
      \]

   Skilyrt væntigildi :math:`X` gefið :math:`Y` er slembistærðin :math:`Z` sem táknuð er með :math:`\mathbb{E}[X|Y]` og skilgreind er með :math:`Z := g(Y)`.

.. admonition:: Athugasemd.
   :class: box-remark

   Ef :math:`\omega \in \Omega` er þannig að :math:`Y(\omega) = y_j`, þá er

   .. math:: Z(\omega) = g(Y(\omega)) = g(y_j) = \mathbb{E}[X|Y=y_j].

.. admonition:: Athugasemd.
   :class: box-remark

   Skrifum :math:`\mathbb{E}[X|Y] = g(Y)`. Samkvæmt lögmáli ómeðvitaða tölfræðingsins gildir að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
      \mathbb{E}\big[\mathbb{E}[X|Y]\big] &= \mathbb{E}[g(Y)] \\
          &= \sum_j g(y_j) \mathbb{P}(Y=y_j) \\
          &= \sum_j \mathbb{E}[X|Y=y_j] \mathbb{P}(Y=y_j).
      \end{aligned}
      \]

   Samkvæmt lykilsetningunni um skilyrt væntigildi gildir síðan að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          \sum_j \mathbb{E}[X|Y=y_j] \mathbb{P}(Y=y_j) = \mathbb{E}[X].
      \end{aligned}
      \]

   Önnur framsetning á lykilsetninguni um skilyrt væntigildi er þess vegna eftirfarandi:

   .. math::
        :nowrap:

        \[
        \begin{aligned}
            \mathbb{E}\big[\mathbb{E}[X|Y]\big] = \mathbb{E}[X].
        \end{aligned}
        \]

   Þessi jafna kallast á ensku ,,law of total expectation“, ,,law of iterated expectation“ eða ,,tower property“.

   Við setjum nú lykilsetninguna aftur fram þar sem við höfum með nýju framsetninguna.

.. admonition:: Setning 16 (lykilsetning um skilyrt væntigildi).
   :class: box-theorem

   Látum :math:`X` og :math:`Y` vera strjálar slembistærðir. Þá gildir að

   

   .. math::
        :nowrap:

        \[
        \begin{aligned}
               \sum_j \mathbb{E}[X|Y=y_j]\mathbb{P}(Y=y_j) = \mathbb{E}[X],
        \end{aligned}
        \]

   þar sem summan nær yfir öll gildin sem :math:`Y` tekur.

   Setninguna má einnig setja fram svona:

   .. math::
        :nowrap:

        \[
        \begin{aligned}
                \mathbb{E}\big[\mathbb{E}[X|Y]\big] = \mathbb{E}[X].
        \end{aligned}
        \]

.. admonition:: Dæmi.
   :class: box-example

   Skál hefur :math:`h` hvítar og :math:`s` svartar kúlur. Jafnar líkur eru á að draga sérhverja kúlu. Ef hvít kúla er dregin er henni skilað aftur í skálina. Ef svört kúla er dregin er henni skipt út fyrir hvíta kúlu úr annarri skál. Látum :math:`H_n` vera fjölda hvítra kúlna í skálinni eftir að dregið hefur verið :math:`n` sinnum.

   (i)  Notum fyrst skilyrt væntigildi til að leiða út eftirfarandi rakningarformúlu:

        .. math::
           :nowrap:

           \[
           \begin{aligned}
                   \mathbb{E}[H_{n+1}] = 1 + \left(1-\frac1{h+s}\right)\mathbb{E}[H_n], \quad n \geq 0.
           \end{aligned}
           \]

   (ii) Notum síðan þrepun til að sýna að

        .. math:: \mathbb{E}[H_n] = h + s - s\left(1-\frac1{h+s}\right)^n, \quad n \geq 0.

.. admonition:: Lausn.
   :class: box-example

   (i)  Finnum fyrst skilyrta væntigildið :math:`\mathbb{E}[H_{n+1}|H_n=k]` þar sem :math:`n \geq 0` og :math:`k \leq h+s`. Ef gefið er að :math:`H_n=k`, þá eru :math:`k` hvítar kúlur í skálinni, og heildarfjöldi kúlna er :math:`h+s`. Slembistærðin :math:`H_{n+1}` getur annaðhvort tekið gildið :math:`k` eða :math:`k+1` eftir því hvort hvít eða svört kúla er dregin. Líkurnar á að draga hvíta kúlu eru :math:`k/(h+s)` og líkurnar á að draga svarta kúlu eru :math:`1-k/(h+s)`. Skilyrt væntigildi :math:`H_{n+1}` gefið :math:`H_n=k` er þess vegna

        .. math::
           :nowrap:

           \[
           \begin{aligned}
               \mathbb{E}[H_{n+1}|H_n=k] &= k \cdot \frac{k}{h+s} + (k+1) \cdot \left(1-\frac{k}{h+s}\right) \\
               &= \frac{k^2}{h+s} + k + 1 - \frac{k^2}{h+s} - \frac{k}{h+s} \\
               &= 1 + k - \frac{k}{h+s}.
           \end{aligned}
           \]

        Skilyrt væntigildi :math:`H_{n+1}` gefið :math:`H_n` er þá

        .. math::
           :nowrap:

           \[
           \begin{aligned}
               \mathbb{E}[H_{n+1}|H_{n}] = 1 + H_n - \frac{H_n}{h+s}. \quad (\ast)
           \end{aligned}
           \]

        Samkvæmt lykilsetningunni um skilyrt væntigildi er

        .. math::
           :nowrap:

           \[
           \begin{aligned}
               \mathbb{E}\big[\mathbb{E}[H_{n+1}|H_n]\big] = \mathbb{E}[H_{n+1}].
           \end{aligned}
           \]

        Ef við tökum væntigildi báðum megin við jafnaðarmerkið í :math:`(\ast)` og notum að væntigildi er línulegt fæst því að

        .. math::
           :nowrap:

           \[
           \begin{aligned}
               \mathbb{E}[H_{n+1}] &= 1 + \mathbb{E}[H_n] - \frac{\mathbb{E}[H_n]}{h+s} \\
               &= 1 + \left(1-\frac1{h+s}\right) \mathbb{E}[H_n], \quad n \geq 0.
           \end{aligned}
           \]

   (ii) | Viljum sýna með þrepun að fyrir öll :math:`n \geq 0` gildi:

          .. math:: \mathbb{E}[H_n] = h + s - s\left(1-\frac1{h+s}\right)^n, \quad (\ast\ast)

          Jafnan gildir fyrir :math:`n = 0` þar sem

          .. math:: h+s-s\left(1-\frac1{h+s}\right)^0 = h+s-s=h,

          og :math:`\mathbb{E}[H_0] = h` er fjöldi hvítra kúlna í skálinni í byrjun.

        Gerum nú ráð fyrir að jafnan :math:`(\ast\ast)` gildi fyrir gefið :math:`n` (þrepunarforsendan) og sýnum að jafnan gildi líka fyrir :math:`n+1`. Samkvæmt lið (i) og þrepunarforsendunni fæst:

          .. math::
             :nowrap:

             \[
             \begin{aligned}
                 \mathbb{E}[H_{n+1}] &= 1 + \left(1-\frac1{h+s}\right) \mathbb{E}[H_n] \\
                 &= 1 + \left(1-\frac1{h+s}\right) \left(h+s- s\left(1-\frac1{h+s}\right)^n\right) \\
                 &= 1 + (h+s)\left(1-\frac1{h+s}\right) -  s\left(1-\frac1{h+s}\right)^{n+1} \\
                 &= h + s -  s\left(1-\frac1{h+s}\right)^{n+1}.
             \end{aligned}
             \]

        Við höfum þá sýnt með þrepun að :math:`(\ast\ast)` gildir fyrir öll :math:`n \geq 0`.


