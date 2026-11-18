Kenniföll og væntigildi þeirra
==============================

Kennifall atburðar
~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining 6.
   :class: box-definition

   Látum :math:`(\Omega,{\cal F},\mathbb{P})` vera líkindarúm og :math:`A \in {\cal F}` vera atburð. Fallið :math:`1_A: \Omega \to \mathbb{R}` sem skilgreint er með

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          1_A(\omega) := \begin{cases} 1, & \omega \in A, \\ 0, & \omega \notin A, \end{cases}
      \end{aligned}
      \]

   kallast kennifall atburðarins :math:`A`.

   .. container:: center

      .. figure:: images/kennifall_atburdar.svg
         :width: 345.02pt
         :align: center

.. admonition:: Dæmi.
   :class: box-example

   Teningakast hefur útkomumengið :math:`\Omega = \{1,2,3,4,5,6\}`. Segjum að okkur sé sama nákvæmlega hvaða tala kemur upp, en að við viljum vita hvort slétt tala komi upp eða ekki. Látum :math:`A = \{2,4,6\}` vera atburðinn að slétt tala komi upp. Þá er kennifallið :math:`1_A: \Omega \to \mathbb{R}` gefið með

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              1_A(\omega) = \begin{cases} 1, & \omega \in \{2,4,6\}, \\ 0, & \omega \in \{1,3,5\}. \end{cases}
      \end{aligned}
      \]

   Við getum notað gildið á :math:`1_A` til að lýsa því hvort slétt tala komi upp í tilrauninni eða ekki.

.. admonition:: Athugasemd.
   :class: box-remark

   - Að nota kenniföll :math:`1_A` er almennt þægileg leið til að lýsa niðurstöðu úr tilraun ef við höfum aðeins áhuga á að vita hvort atburðurinn :math:`A` hefur gerst eða ekki.

   - Kenniföll geta jafnframt auðveldað okkur að sanna staðhæfingar um líkindi, eins og við ræðum hér á eftir.

   - Loks eru kenniföll hornsteinn mál- og tegurfræði, sem liggur til grundvallar kennilegri líkindafræði. Í mál- og tegurfræði eru margar setningar sem fjalla um raungild föll sannaðar með því að sýna fyrst að setningarnar gildi um kenniföll og nota síðan kenniföll til að nálga almenn raungild föll.

   - Kenniföll eru **slembistærðir**, sem er hugtak sem við kynnumst fljótlega í Lík&töl.

.. admonition:: Dæmi.
   :class: box-example

   Látum :math:`(\Omega,{\cal F},{\cal P})` vera líkindarúm og :math:`A,B \in {\cal F}`.

   (1) Sýnið að :math:`1_{A^c} = 1-1_A`.

   (2) Sýnið að :math:`1_{A \cap B} = 1_A 1_B = 1_A \cdot 1_B`.

   (3) Sýnið að :math:`1_{B \setminus A} = 1_B - 1_{A \cap B}`.

.. admonition:: Lausn.
   :class: box-example

   (1) | Við þurfum að sýna að :math:`1_{A^c}` og :math:`1-1_A` séu sama fallið frá :math:`\Omega` til :math:`\mathbb{R}`. Til þess þurfum við að sýna að

         .. math:: 1_{A^c}(\omega) = 1-1_A(\omega)

         fyrir sérhvert :math:`\omega \in \Omega`.

       Tökum tvö tilvik:

       (i)  Ef :math:`\omega \in A` þ.e. :math:`\omega \notin A^c`, þá er :math:`1_A(\omega) = 1` og :math:`1_{A^c}(\omega) = 0`. Þess vegna er :math:`1_{A^c}(\omega) = 0 = 1-1_A(\omega)`.

       (ii) Ef :math:`\omega \notin A` þ.e. :math:`\omega \in A^c`, þá er :math:`1_A(\omega) = 0` og :math:`1_{A^c}(\omega) = 1`. Þess vegna er :math:`1_{A^c}(\omega) = 1 = 1-1_A(\omega)`.

       Við höfum þá sýnt að :math:`1_{A^c}(\omega) = 1-1_A(\omega)` gildir fyrir sérhvert :math:`\omega \in \Omega`.

   (2) | Hér þurfum við að sýna að :math:`1_{A \cap B}(\omega) = 1_A(\omega) 1_B(\omega)` fyrir sérhvert :math:`\omega \in \Omega`.

       Tökum tvö tilvik:

       (i)  Ef :math:`\omega \in A \cap B`, þá er :math:`\omega \in A` og :math:`\omega \in B`. Þess vegna er :math:`1_{A \cap B}(\omega) = 1`, :math:`1_A(\omega) = 1` og :math:`1_B(\omega) = 1`, sem þýðir að :math:`1_{A \cap B}(\omega) = 1 = 1_A(\omega) 1_B(\omega)`.

       (ii) Ef :math:`\omega \notin A \cap B`, þá er :math:`1_{A \cap B}(\omega) = 0`. Þar sem :math:`\omega \notin A` eða :math:`\omega \notin B` gildir jafnframt að :math:`1_A(\omega) = 0` eða :math:`1_B(\omega) = 0`. Þess vegna er :math:`1_{A \cap B}(\omega) = 0 = 1_A(\omega) 1_B(\omega)`.

       Við höfum þá sýnt að :math:`1_{A \cap B}(\omega) = 1_A(\omega) 1_B(\omega)` gildir fyrir sérhvert :math:`\omega \in \Omega`.

   (3) | Hér þurfum við að sýna að :math:`1_{B \setminus A}(\omega) = 1_B(\omega) - 1_{A \cap B}(\omega)` fyrir sérhvert :math:`\omega \in \Omega`.
       | Tökum þrjú tilvik (gott getur verið að teikna mynd til að átta sig á því hvaða tilvik þarf að taka):

       (i)   Ef :math:`\omega \in A \cap B`, þá er :math:`1_{A \cap B}(\omega) = 1` og :math:`1_B(\omega) = 1`. Jafnframt er :math:`1_{B \setminus A}(\omega) = 0` þar sem :math:`\omega \in A` og þar með er :math:`\omega \notin B \setminus A`.

             Þess vegna er :math:`1_{B \setminus A}(\omega) = 0 = 1_B(\omega) - 1_{A \cap B}(\omega)`.

       (ii)  Ef :math:`\omega \in B \setminus A`, þ.e. :math:`\omega \in B` og :math:`\omega \notin A`, þá er :math:`1_{B \setminus A}(\omega) = 1`, :math:`1_B(\omega) = 1` og :math:`1_{A \cap B}(\omega) = 0`. Þess vegna er :math:`1_{B \setminus A}(\omega) = 1 = 1_B(\omega) - 1_{A \cap B}(\omega)`.

       (iii) Ef :math:`\omega \notin B`, þá er :math:`1_{B \setminus A}(\omega) = 0`, :math:`1_{B}(\omega) = 0` og :math:`1_{A \cap B}(\omega) = 0`. Þess vegna er :math:`1_{B \setminus A}(\omega) = 0 = 1_B(\omega) - 1_{A \cap B}(\omega)`.

       Við höfum þá sýnt að :math:`1_{B \setminus A}(\omega) = 1_B(\omega) - 1_{A \cap B}(\omega)` gildir fyrir sérhvert :math:`\omega \in \Omega`.

Væntigildi kennifalla
~~~~~~~~~~~~~~~~~~~~~

Í Lík&töl er fjallað um væntigildi strjálla og samfelldra slembistærða. Við setjum nú fram helstu eiginleika væntigildis:

.. admonition:: Setning 7.
   :class: box-theorem

   Fyrir öll :math:`a,a_1,a_2,\ldots,a_n \in \mathbb{R}` og allar slembistærðir :math:`X,Y,X_1,\ldots,X_n` gildir:

   (1) :math:`\mathbb{E}[a] = a`.

   (2) :math:`\mathbb{E}[aX] = a\mathbb{E}[X]`.

   (3) :math:`\mathbb{E}[X+Y] = \mathbb{E}[X]+\mathbb{E}[Y]`.

   (4) Væntigildi er línulegt:

       .. math:: \mathbb{E}[a_1X_1+\cdots+a_nX_n] = a_1 \mathbb{E}[X_1] + \cdots + a_n \mathbb{E}[X_n].

   (5) Væntigildi er einhalla: Ef :math:`X \leq Y`, þá er :math:`\mathbb{E}[X] \leq \mathbb{E}[Y]`.

Munið að fyrir atburð :math:`A` er kennifallið :math:`1_A: \Omega \to \mathbb{R}` slembistærð sem tekur gildið 1 þegar atburðurinn gerist og 0 annars:

.. math::
   :nowrap:

   \[
   \begin{aligned}
    1_A(\omega) = \begin{cases} 1, & \omega \in A, \\ 0, & \omega \notin A. \end{cases}
   \end{aligned}
   \]

Setjum :math:`X = 1_A`. Massafall :math:`X` er

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{P}(X=1) = \mathbb{P}(A) \quad\text{og}\quad \mathbb{P}(X=0) = \mathbb{P}(A^c).
   \end{aligned}
   \]

Væntigildi :math:`X` er þá

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{E}[X] = 1 \cdot \mathbb{P}(A) + 0 \cdot \mathbb{P}(A^c) = \mathbb{P}(A).
   \end{aligned}
   \]

Með öðrum orðum er

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{E}[1_A] = \mathbb{P}(A).
   \end{aligned}
   \]

Væntigildi gerir okkur þannig kleift að breyta kennifalli atburðar í líkur á atburðinum. Þessi staðreynd getur nýst til að leiða út jöfnur eða ójöfnur um líkindi, eins og við sjáum dæmi um núna.

.. admonition:: Dæmi
   :class: box-example

   Í skiladæmunum leidduð þið út eftirfarandi kennifallajöfnu:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              1_{A \cup B} = 1_A + 1_B - 1_{A \cap B}.
      \end{aligned}
      \]

   Tökum væntigildi báðum megin við jafnaðarmerkið og fáum:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              \mathbb{E}[1_{A \cup B}] = \mathbb{E}[1_A + 1_B - 1_{A \cap B}].
      \end{aligned}
      \]

   Notum núna að væntigildi er línulegt og fáum:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              \mathbb{E}[1_{A \cup B}] = \mathbb{E}[1_A] + \mathbb{E}[1_B] - \mathbb{E}[1_{A \cap B}].
      \end{aligned}
      \]

   Notum loks að :math:`\mathbb{E}[1_D] = \mathbb{P}(D)` fyrir sérhvern atburð :math:`D` og fáum loks:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              \mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B),
      \end{aligned}
      \]

   sem er jafna um líkindi sem við sönnuðum í skiladæmunum. Þetta myndi þó ekki teljast fullgild sönnun á lið (6) í Setningu 1 þar sem væntigildi var ekki þekkt þegar sú setning var sett fram. Hins vegar getum við notað þessa hugmynd til að sanna jöfnur og ójöfnur um líkindi sem við höfum ekki séð áður, eins og við sjáum dæmi um núna.

.. admonition:: Dæmi
   :class: box-example

   Við sýnum nú hvernig hægt er að sanna almenna reglu um líkindi samatburða með því að nota kenniföll. Reglan er:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              \mathbb P \left( \bigcup_{i=1}^{n} A_i \right)  = \sum_{k=1}^{n} \sum_{1 \leq i_1 < \ldots < i_k \leq n} (-1)^{k+1} \mathbb P \left(A_{i_1} \cap \ldots \cap A_{i_k} \right). \quad (\ast)
      \end{aligned}
      \]

   Í skiladæmunum sönnuðuð þið að fyrir atburði :math:`A_1,A_2,\ldots,A_n` og :math:`A = \bigcup_{i=1}^n A_i` gildir að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              1_A = 1 - \prod_{i=1}^n (1-1_{A_i}).
      \end{aligned}
      \]

   Með því að margfalda upp úr svigunum fæst eftirfarandi umritun á jöfnunni:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              1_A = \sum_{k=1}^{n} \sum_{1 \leq i_1 < \ldots < i_k \leq n} (-1)^{k+1} 1_{A_{i_1}} \cdots 1_{A_{i_k}}.
      \end{aligned}
      \]

   Við sönnuðum í sýnidæmi að :math:`1_{A \cap B} = 1_A 1_B` fyrir atburði :math:`A` og :math:`B`. Með þrepun má auðveldlega alhæfa þessa niðurstöðu og fá fyrir sérhvert :math:`k=1,\ldots,n`:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
            1_{A_{i_1} \cap \cdots \cap A_{i_k}} = 1_{A_{i_1}} \cdots 1_{A_{i_k}}.
      \end{aligned}
      \]

   Við höfum þá að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              1_A = \sum_{k=1}^{n} \sum_{1 \leq i_1 < \ldots < i_k \leq n} (-1)^{k+1}  1_{A_{i_1} \cap \cdots \cap A_{i_k}}. \quad (\ast\ast)
      \end{aligned}
      \]

   Út frá þessari kennifallajöfnu fæst líkindareglan í :math:`(\ast)` nánast beint með því að taka væntigildi. Tökum nú væntigildi í báðum hliðum :math:`(\ast\ast)` og fáum að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
            \mathbb{E}[1_A] = \mathbb{E}\!\left[\sum_{k=1}^{n} \sum_{1 \leq i_1 < \ldots < i_k \leq n} (-1)^{k+1}  1_{A_{i_1} \cap \cdots \cap A_{i_k}}\right].
      \end{aligned}
      \]

   Þar sem :math:`\mathbb{E}[1_A]=\mathbb{P}(A)` og væntigildi er línulegt fæst að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
            \mathbb{P}(A) &= \sum_{k=1}^{n} \sum_{1 \leq i_1 < \ldots < i_k \leq n} \mathbb{E}[(-1)^{k+1}  1_{A_{i_1} \cap \cdots \cap A_{i_k}}] \\
            &= \sum_{k=1}^{n} \sum_{1 \leq i_1 < \ldots < i_k \leq n} (-1)^{k+1} \mathbb{E}[  1_{A_{i_1} \cap \cdots \cap A_{i_k}}].
      \end{aligned}
      \]

   Athugum nú að :math:`\mathbb{E}[  1_{A_{i_1} \cap \cdots \cap A_{i_k}}] = \mathbb{P}(A_{i_1} \cap \cdots \cap A_{i_k})`. Þar sem :math:`A = \bigcup_{i=1}^n A_i` fáum við niðurstöðuna í :math:`(\ast)`:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
            \mathbb{P} \left( \bigcup_{i=1}^{n} A_i \right)  = \sum_{k=1}^{n} \sum_{1 \leq i_1 < \ldots < i_k \leq n} (-1)^{k+1} \mathbb{P} \left(A_{i_1} \cap \ldots \cap A_{i_k} \right).
      \end{aligned}
      \]


