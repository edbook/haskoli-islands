Grundvallareiginleikar líkinda
==============================

Tilraun, útkomumengi og atburðir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hugsum okkur að tiltekin tilraun sem er háð tilviljun sé framkvæmd, t.d. að krónu eða teningi sé kastað. *Útkomumengi* tilraunarinnar :math:`\Omega` er mengi allra mögulegra útkoma úr tilrauninni. Ef krónu er kastað getum við táknað útkomurnar Þ (þorskur) og B (bergrisi) og þá er útkomumengið :math:`\Omega = \{\text{Þ},\text{B}\}`. Ef teningi er kastað er útkoman fjöldi punkta á þeirri hlið sem snýr upp og hægt er að skrifa útkomumengið sem :math:`\Omega = \{1,2,3,4,5,6\}`.

.. container:: center

   .. figure:: images/utkomur.svg
      :width: 268.6pt
      :align: center

*Atburður* er einfaldlega hlutmengi í :math:`\Omega`. Við lýsum atburðum oft í orðum, en atburð verður alltaf að vera unnt að skrifa sem mengi af mögulegum útkomum.

.. admonition:: Dæmi.
   :class: box-example

   - Í teningakasti er :math:`A = \{2,4,6\}` atburðurinn að slétt tala komi upp og :math:`B = \{1,3,5\}` er atburðurinn að oddatala komi upp.

   - Ef krónu er kastað tvisvar í röð er útkomumengið

     .. math:: \Omega = \{\text{ÞÞ},\text{ÞB},\text{BÞ},\text{BB}\},

     þar sem fyrra hnitið er sú hlið sem kemur upp í fyrra kastinu og seinna hnitið er sú hlið sem kemur upp í seinna kastinu. :math:`A = \{\text{ÞB},\text{BÞ}\}` er atburðurinn að þorskurinn komi nákvæmlega einu sinni upp í köstunum tveimur og :math:`B = \{\text{ÞB},\text{BÞ},\text{ÞÞ}\}` atburðurinn að þorskurinn komi a.m.k. einu sinni upp.

     .. container:: center

        .. figure:: images/utkomur_tvo_kronukost.svg
           :width: 361.11pt
           :align: center

   - Ef tveimur teningum er kastað, einum hvítum og einum svörtum, er útkomumengið

     .. math::
        :nowrap:

        \[
        \begin{aligned}
                \Omega = \{(i,j) \in \mathbb{Z}^2: 1 \leq i\leq 6 \;\text{og}\; 1 \leq j \leq 6\}.
        \end{aligned}
        \]

     Atburðurinn að summa gildanna á teningunum sé 8 er

     .. math::
        :nowrap:

        \[
        \begin{aligned}
                A = \{(2,6),(3,5),(4,4),(5,3),(6,2)\}.
        \end{aligned}
        \]

     .. container:: center

        .. figure:: images/tveir_teningar.svg
           :width: 246.8pt
           :align: center

Líkindi :math:`\mathbb{P}` eru fall sem úthlutar sérhverjum atburði :math:`A` tölu milli 0 og 1, sem við köllum líkindi atburðarins :math:`A` eða líkurnar á atburðinum :math:`A`. Í krónukasti eru líkurnar á þorski :math:`\mathbb{P}(\{\text{Þ}\}) = 1/2`. Í teningakasti eru líkurnar á að fá 6 :math:`\mathbb{P}(\{6\}) = 1/6` en líkurnar á að fá slétta tölu eru :math:`P(A) = 1/2`. Þetta er aðeins óformleg lýsing, við skilgreinum hugtökin útkomurúm, atburður og líkindi nákvæmlega hér að neðan. Fyrst þurfum við að skilgreina hugtakið *sundurlæga atburði*.

.. admonition:: Skilgreining 1.
   :class: box-definition

   - Mengi :math:`A` og :math:`B` kallast **sundurlæg** ef :math:`A \cap B = \varnothing`, þ.e. :math:`A` og :math:`B` hafa engin sameiginleg stök.

     .. container:: center

        .. figure:: images/sundurlaegir_tveir.svg
           :width: 167.36pt
           :align: center

   - Runa af mengjum :math:`A_1,A_2,\ldots` kallast **sundurlæg** ef mengin eru sundurlæg tvö og tvö, þ.e. :math:`A_i \cap A_j = \varnothing` ef :math:`i \neq j`.

     .. container:: center

        .. figure:: images/sundurlaegir_fleiri.svg
           :width: 243.65pt
           :align: center

.. admonition:: Athugasemd.
   :class: box-remark

   Óformlega eru tveir atburðir sundurlægir ef tilraunin getur aldrei farið þannig að báðir atburðirnir gerist í einu.

.. admonition:: Dæmi.
   :class: box-example

   - Í teningakasti eru atburðirnir :math:`A = \{2,4,6\}` að slétt tala komi upp og :math:`B = \{1,3,5\}` að oddatala komi upp sundurlægir atburðir, því við getum ekki í sama kastinu fengið bæði slétta tölu og oddatölu.

   - Atburðirnir :math:`A = \{2,4,6\}` að slétt tala komi upp og :math:`B = \{3,6\}` að upp komi tala sem er deilanleg með 3 eru **ekki** sundurlægir, því við **getum** í sama kastinu fengið tölu sem er bæði slétt og deilanleg með 3.

   - Ef tveimur teningum er kastað eru atburðirnir

     .. math::
        :nowrap:

        \[
        \begin{aligned}
            & A = \{(2,6),(3,5),(4,4),(5,3),(6,2)\}, \\
             &   B = \{(4,6),(5,5),(6,4)\},
        \end{aligned}
        \]

     annars vegar að summa gildanna sé átta og hins vegar að summa gildanna sé tíu, sundurlægir atburðir.

:math:`\sigma`-algebra og líkindarúm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við setjum nú fram fyrstu tilraun til skilgreiningar á hugtakinu *líkindum*.

.. admonition:: Ófullkomin skilgreining.
   :class: box-definition

   *Líkindi* eru fall :math:`\mathbb{P}` sem úthlutar sérhverjum atburði :math:`A` tölu :math:`\mathbb{P}(A)` og hefur eftirfarandi grundvallareiginleika:

   (I)   :math:`\mathbb{P}(\Omega) = 1`.

   (II)  :math:`\mathbb{P}(A) \geq 0` fyrir alla atburði :math:`A`.

   (III) Ef :math:`A_1,A_2,\ldots` eru sundurlægir atburðir gildir:

         .. math::
            :nowrap:

            \[
            \begin{aligned}
                    \mathbb{P}\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty \mathbb{P}(A_i).
            \end{aligned}
            \]

   .. container:: center

      .. figure:: images/sundurlaegir_fleiri.svg
         :width: 243.65pt
         :align: center

Þessi skilgreining er ófullkomin að því leyti að við höfum ekki skilgreint hugtakið atburður nákvæmlega. Hér að framan sögðum við að atburðir séu hlutmengi í :math:`\Omega` og sáum ýmis dæmi um atburði, en við ávörpuðum ekki hvort öll hlutmengi í :math:`\Omega` þurfi endilega að vera atburðir. Í líkindafræði viljum við geta skilgreint líkindi fyrir safn af hlutmengjum í :math:`\Omega` sem inniheldur ekki endilega öll hlutmengi í :math:`\Omega`. Með öðrum orðum viljum við geta skilgreint líkindi þar sem ekki öll hlutmengi í :math:`\Omega` eru atburðir. Ástæðan fyrir því kemur ekki fram fyrr en í STÆ402M Mál- og tegurfræði eða STÆ418M Grundvelli líkindafræðinnar. Við krefjumst þess hins vegar alltaf að safn allra atburða myndi svokallaða :math:`\sigma`-algebru. Það tryggir að við getum talað um líkur t.d. á fyllimengi atburðar og sammengi og sniðmengi atburða, sem er algjör lágmarkskrafa.

.. admonition:: Skilgreining 2.
   :class: box-definition

   Látum :math:`\Omega \neq \varnothing` vera mengi og :math:`{\cal F}` vera safn af hlutmengjum í :math:`\Omega`. :math:`{\cal F}` kallast :math:`\sigma`-algebra á :math:`\Omega` ef eftirfarandi skilyrði eru uppfyllt:

   (1) :math:`\Omega \in {\cal F}`.

   (2) ef :math:`A \in {\cal F}`, þá er :math:`A^c \in {\cal F}`.

   (3) ef :math:`A_1,A_2,\ldots \in {\cal F}`, þá er :math:`\bigcup_{i=1}^\infty A_i \in {\cal F}`.

.. admonition:: Athugasemd.
   :class: box-remark

   - Í fyrsta grundvallareiginleika líkinda viljum við geta talað um líkurnar á :math:`\mathbb{P}(\Omega)`. Ef safn allra atburða myndar :math:`\sigma`-algebru er þetta tryggt skv. þessari skilgreiningu.

   - Í þriðja grundvallareiginleika líkinda viljum við fyrir sundurlæga atburði :math:`A_1,A_2,\ldots` geta talað um líkurnar á :math:`\bigcup_{i=1}^\infty A_i`. Til þess þarf :math:`\bigcup_{i=1}^\infty A_i` að vera atburður. Ef safn allra atburða myndar :math:`\sigma`-algebru er þetta tryggt. Meira að segja er tryggt að :math:`\bigcup_{i=1}^\infty A_i` sé atburður jafnvel þótt :math:`A_1,A_2,\ldots` séu ekki sundurlægir atburðir.

.. admonition:: Dæmi.
   :class: box-example

   - Látum :math:`\Omega = \{1,2,3,4,5,6\}` vera útkomumengið fyrir teningakast. Eftirfarandi mengjasafn er dæmi um :math:`\sigma`-algebru á :math:`\Omega`:

     .. math:: {\cal F} = \{\varnothing, \Omega, \{1,3,5\}, \{2,4,6\}\}.

     Ef við skilgreinum líkindi fyrir þessa :math:`\sigma`-algebru þýðir það við getum bara talað um líkurnar á atburðunum að fá slétta tölu eða oddatölu (fyrir utan :math:`\Omega` og :math:`\varnothing`).

   - Almennt gildir að ef :math:`A` er hlutmengi í :math:`\Omega`, þá er mengjasafnið

     .. math:: {\cal F} = \{\varnothing, \Omega, A, A^c\}

     :math:`\sigma`-algebra á :math:`\Omega`.

   - Safn *allra* hlutmengja í :math:`\Omega`, :math:`{\cal F}(\Omega)`, er :math:`\sigma`-algebra á :math:`\Omega`.

   - Mengjasafnið

     .. math:: {\cal F} = \{\varnothing, \Omega, \{1,2\}, \{3,4\},  \{5,6\}\}.

     er ekki :math:`\sigma`-algebra á :math:`\Omega = \{1,2,3,4,5,6\}`. Hvaða hlutmengjum í :math:`\Omega` þyrfti að bæta við til að fá :math:`\sigma`-algebru?

.. admonition:: Athugasemd.
   :class: box-remark

   Látum :math:`{\cal F}` vera :math:`\sigma`-algebru á :math:`\Omega`.

   - Þar sem :math:`\Omega \in {\cal F}` gildir alltaf að :math:`\varnothing = \Omega^c \in {\cal F}` skv. (2).

   - Jafnframt gildir að ef :math:`A_1,A_2,\ldots \in {\cal F}`, þá er :math:`\bigcap_{i=1}^\infty A_i \in {\cal F}`. Ástæðan er sú að við getum skrifað (regla de Morgan)

     .. math::
        :nowrap:

        \[
        \begin{aligned}
               \textstyle \left(\bigcap_{i=1}^\infty A_i\right)^c = \bigcup_{i=1}^\infty A_i^c \quad\text{þ.e.}\quad \bigcap_{i=1}^\infty A_i = \left(\bigcup_{i=1}^\infty A_i^c\right)^c
        \end{aligned}
        \]

     og samkvæmt skilgreiningu á :math:`\sigma`-algebru gildir að

     - :math:`A_1,A_2,\ldots \in {\cal F}` :math:`\Rightarrow` :math:`A_1^c,A_2^c,\ldots \in {\cal F}` skv. skilyrði (2),

     - :math:`A_1^c,A_2^c,\ldots \in {\cal F}` :math:`\Rightarrow` :math:`\bigcup_{i=1}^\infty A_i^c \in {\cal F}` skv. skilyrði (3),

     - :math:`\bigcup_{i=1}^\infty A_i^c \in {\cal F}` :math:`\Rightarrow` :math:`\left(\bigcup_{i=1}^\infty A_i^c\right)^c \in {\cal F}` skv. skilyrði (2).

   - Sem sagt: Þó að skilgreiningin á :math:`\sigma`-algebru segi aðeins að óendanlegt sammengi atburða sé alltaf atburður, þá leiðir af henni að óendanlegt sniðmengi atburða sé alltaf atburður. Endanleg sammengi og sniðmengi atburða eru líka atburðir, vegna þess að

     .. math::
        :nowrap:

        \[
        \begin{aligned}
            A_1 \cup A_2 \cup \cdots \cup A_n = A_1 \cup A_2 \cup \cdots \cup A_n \cup \varnothing \cup \varnothing \cup \cdots, \\
            A_1 \cap A_2 \cap \cdots \cap A_n = A_1 \cap A_2 \cap \cdots \cap A_n \cap \Omega \cap \Omega \cap \cdots,
        \end{aligned}
        \]

     og við vitum að :math:`\varnothing` og :math:`\Omega` eru atburðir.

Núna þegar við höfum kynnt til sögunnar :math:`\sigma`-algebru getum við gefið hugtakinu atburður nákvæma merkingu og lagað óformlegu skilgreininguna á líkindum.

.. admonition:: Skilgreining 3.
   :class: box-definition

   Látum :math:`\Omega \neq \varnothing` vera mengi og :math:`{\cal F}` vera :math:`\sigma`-algebru á :math:`\Omega`. **Líkindi** eru fall :math:`\mathbb{P} : {\cal F} \to \mathbb{R}` sem uppfyllir eftirfarandi skilyrði:

   (I)   :math:`\mathbb{P}(\Omega) = 1`.

   (II)  :math:`\mathbb{P}(A) \geq 0` fyrir öll :math:`A \in {\cal F}`.

   (III) Ef :math:`A_1,A_2,\ldots \in {\cal F}` eru sundurlæg mengi gildir:

         .. math::
            :nowrap:

            \[
            \begin{aligned}
                    \mathbb{P}\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty \mathbb{P}(A_i).
            \end{aligned}
            \]

   Þrenndin :math:`(\Omega,{\cal F},\mathbb{P})` kallast líkindarúm, mengið :math:`\Omega` kallast útkomumengi, sérhvert stak :math:`\omega \in \Omega` kallast útkoma og sérhvert stak :math:`A \in {\cal F}` kallast atburður.

.. admonition:: Athugasemd.
   :class: box-remark

   Við tölum alltaf um töluna :math:`\mathbb{P}(A)` sem ,,líkurnar á atburðinum :math:`A`\ “.

Hér höfum við formlega skilgreint hvað átt er við með útkomumengi, útkomu, atburð og líkindum. Þessi skilgreining kom fyrst fram hjá Andrei Kolmogorov í grein sem kom út árið 1933. Takið eftir að þó að við höfum haft ákveðnar tilraunir í huga þegar við töluðum fyrst um útkomumengi, atburði og líkindi, þá vísar skilgreining Kolmogorovs á líkindarúmi ekki í neina tilraun. Hún er algjörlega óhlutbundin og gerir líkindafræði að hreinni stærðfræði. :math:`\Omega` er einfaldlega eitthvað ekki tómt mengi, atburðir eru tiltekin hlutmengi í :math:`\Omega` sem mynda :math:`\sigma`-algebru :math:`{\cal F}`, og líkindi eru fall frá :math:`{\cal F}` til :math:`\mathbb{R}` sem hafa eiginleikana þrjá í Skilgreiningu 3. Svo einfalt (eða flókið) er það.

Reiknireglur fyrir líkindi
~~~~~~~~~~~~~~~~~~~~~~~~~~

Skilgreiningin á líkindum felur einungis í sér þrjá grundvallareiginleika sem líkindi verða að hafa, en út frá þeim er hægt að leiða út ýmsar aðrar reiknireglur fyrir líkindi.

.. admonition:: Setning 1.
   :class: box-theorem

   Ef :math:`(\Omega,{\cal F},\mathbb{P})` er líkindarúm og :math:`A,B,A_1,A_2,\ldots \in {\cal F}`, þá gildir:

   (1) :math:`\mathbb{P}(\varnothing) = 0`.

   (2) Ef :math:`A_1,\ldots,A_n` eru sundurlægir atburðir, þá gildir að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \mathbb{P}\left(\bigcup_{i=1}^n A_i\right) = \sum_{i=1}^n \mathbb{P}(A_i).
          \end{aligned}
          \]

       Sér í lagi gildir fyrir sundurlæga atburði :math:`A` og :math:`B` að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B).
          \end{aligned}
          \]

       .. container:: center

          .. figure:: images/sundurlaegir_fleiri_n.svg
             :width: 243.65pt
             :align: center

   (3) :math:`\mathbb{P}(B \setminus A) = \mathbb{P}(B) - \mathbb{P}(A \cap B)`. Hér er :math:`B \setminus A = B \cap A^c` mengi allra staka í :math:`B` sem eru ekki í :math:`A`.

       .. container:: center

          .. figure:: images/atburdir_a_b_saman.svg
             :width: 166.6pt
             :align: center

   (4) :math:`\mathbb{P}(A) + \mathbb{P}(A^c) = 1` þ.e. :math:`\mathbb{P}(A^c) = 1-\mathbb{P}(A)`.

       .. container:: center

          .. figure:: images/atburður_a.svg
             :width: 166.6pt
             :align: center

   (5) Ef :math:`A \subseteq B`, þá er :math:`\mathbb{P}(A) \leq \mathbb{P}(B)`.

       .. container:: center

          .. figure:: images/a_hlutmengi_b.svg
             :width: 166.6pt
             :align: center

   (6) :math:`\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)`.

       .. container:: center

          .. figure:: images/atburdir_a_b_saman.svg
             :width: 166.6pt
             :align: center

   (7) (Endanlega Boole-ójafnan.) Fyrir öll :math:`n \geq 1` gildir að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \mathbb{P}\left(\bigcup_{i=1}^n A_i\right) \leq \sum_{i=1}^n \mathbb{P}(A_i).
          \end{aligned}
          \]

       .. container:: center

          .. figure:: images/ekki_sundurlaegir_fleiri_n_0.svg
             :width: 255.86pt
             :align: center

   (8) :math:`\mathbb{P}(A) \leq 1`.

Við sönnum nú þessar reiknireglur með því að nota staðreyndir úr mengjafræði og hina þrjá grundvallareiginleika líkinda sem koma fram í Skilgreiningu 3.

.. admonition:: Sönnun.
   :class: box-theorem

   (1) Við getum ritað :math:`\Omega = \Omega \cup \varnothing \cup \varnothing \cup \cdots` þar sem :math:`\Omega,\varnothing,\varnothing,\ldots` er sundurlæg runa af atburðum. Samkvæmt þriðja grundvallareiginleika líkinda fæst að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \mathbb{P}(\Omega ) = \mathbb{P}(\Omega ) + \mathbb{P}(\varnothing) + \mathbb{P}(\varnothing) + \cdots,
          \end{aligned}
          \]

       sem þýðir að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                   \mathbb{P}(\varnothing) + \mathbb{P}(\varnothing) + \cdots = 0.
          \end{aligned}
          \]

       Við ályktum að :math:`\mathbb{P}(\varnothing) = 0`.

.. admonition:: Athugasemd.
   :class: box-remark

   Þessi sönnun gæti virst einkennileg, en mikilvægt er að átta sig á því að

   .. math:: \Omega = \Omega \cup \varnothing \cup \varnothing \cup \cdots

   er staðhæfing um mengi, meðan

   .. math:: \mathbb{P}(\Omega ) = \mathbb{P}(\Omega ) + \mathbb{P}(\varnothing) + \mathbb{P}(\varnothing) + \cdots

   er staðhæfing um tölur (líkur). Við erum sem sagt að nota staðreynd úr mengjafræði og þriðja grundvallareiginleika líkinda til að sanna að :math:`\mathbb{P}(\varnothing) = 0`.

.. admonition:: Sönnun (framhald).
   :class: box-theorem

   (2) Ef :math:`A_1,\ldots,A_n` eru sundurlægir atburðir, þá eru :math:`A_1,A_2,\ldots,A_n,\varnothing,\varnothing,\ldots` líka sundurlægir atburðir. Samkvæmt þriðja grundvallareiginleika líkinda fæst að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  &\mathbb{P}\left(\bigcup_{i=1}^n A_i\right) \\
                  &= \mathbb{P}\left(A_1 \cup A_2 \cup \cdots \cup A_n \cup \varnothing \cup \varnothing \cup \cdots\right) \\
                  &= \mathbb{P}(A_1) + \mathbb{P}(A_2) + \cdots + \mathbb{P}(A_n) + \mathbb{P}(\varnothing) + \mathbb{P}(\varnothing) + \cdots.
          \end{aligned}
          \]

       Þar sem :math:`\mathbb{P}(\varnothing)=0` samkvæmt lið (1) getum við ályktað að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \mathbb{P}\left(\bigcup_{i=1}^n A_i\right) = \sum_{i=1}^n \mathbb{P}(A_i).
          \end{aligned}
          \]

   (3) Athugum að :math:`B = (B \setminus A) \cup (A \cap B)`, þar sem :math:`B \setminus A` og :math:`A \cap B` eru sundurlægir atburðir. Því fæst skv. lið (2):

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                      \mathbb{P}(B) = \mathbb{P}(B \setminus A) + \mathbb{P}(A \cap B),
          \end{aligned}
          \]

       sem gefur að :math:`\mathbb{P}(B \setminus A) = \mathbb{P}(B) - \mathbb{P}(A \cap B)`.

       .. container:: center

          .. figure:: images/atburdir_a_b_saman.svg
             :width: 166.6pt
             :align: center

   (4) Við getum skrifað :math:`\Omega = A \cup A^c`, þar sem :math:`A` og :math:`A^c` eru sundurlægir atburðir. Því fæst skv. lið (2):

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                      \mathbb{P}(\Omega) = \mathbb{P}(A) + \mathbb{P}(A^c).
          \end{aligned}
          \]

       Þar sem :math:`\mathbb{P}(\Omega)=1` skv. fyrsta grundvallareiginleika líkinda fæst loks að :math:`\mathbb{P}(A)+\mathbb{P}(A^c)=1` þ.e. :math:`\mathbb{P}(A^c)=1-\mathbb{P}(A)`.

       .. container:: center

          .. figure:: images/atburður_a.svg
             :width: 166.6pt
             :align: center

   (5) Ef :math:`A \subseteq B` er :math:`A \cap B = A`. Því fæst skv. lið (3) að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                      \mathbb{P}(B \setminus A) = \mathbb{P}(B) - \mathbb{P}(A \cap B) = \mathbb{P}(B) - \mathbb{P}(A).
          \end{aligned}
          \]

       Þar sem :math:`\mathbb{P}(B \setminus A) \geq 0` skv. öðrum grundvallareiginleika líkinda er þá :math:`\mathbb{P}(B) - \mathbb{P}(A) \geq 0` þ.e. :math:`\mathbb{P}(B) \geq \mathbb{P}(A)`.

   (6) Æfing.

   (7) Æfing.

   (8) Þar sem :math:`A \subseteq \Omega` fæst samkvæmt lið (5) að :math:`\mathbb{P}(A) \leq \mathbb{P}(\Omega)`. Þar sem :math:`\mathbb{P}(\Omega)=1` samkvæmt fyrsta grundvallareiginleika líkinda getum við ályktað að :math:`\mathbb{P}(A) \leq 1`.

Samkvæmt lið (6) í Setningu 1 gildir fyrir atburði :math:`A` og :math:`B` að

.. math:: \mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B).

Þessa jöfnu má alhæfa á eftirfarandi hátt fyrir þrjá atburði, eins og er auðvelt að sannfæra sig um með því að teikna mynd og túlka líkindi atburðar sem massa hans:

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{P}(A \cup B \cup C) = &\; \mathbb{P}(A) + \mathbb{P}(B) + \mathbb{P}(C) \\ &-\mathbb{P}(A \cap B) - \mathbb{P}(A \cap C) - \mathbb{P}(B \cap C) \\ &+\mathbb{P}(A \cap B \cap C).
   \end{aligned}
   \]

.. container:: center

   .. figure:: images/sammengi_thriggja.svg
      :width: 175.16pt
      :align: center

Almennt er unnt að sanna eftirfarandi jöfnu fyrir sammengi :math:`n` atburða, sem er enn frekari alhæfing á jöfnunum fyrir sammengi tveggja og þriggja atburða:

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb P \left( \bigcup_{i=1}^{n} A_i \right) =& \sum_{k=1}^{n} \sum_{1 \leq i_1 < \ldots < i_k \leq n} (-1)^{k+1} \mathbb P \left(A_{i_1} \cap \ldots \cap A_{i_k} \right).
   \end{aligned}
   \]

Summan í hægri hlið reiknast svona:

.. math::
   :nowrap:

   \[
   \begin{aligned}
       \sum_{k=1}^{n} \sum_{1 \leq i_1 < \ldots < i_k \leq n} (-1)^{k+1} \mathbb P \left(A_{i_1} \cap \ldots \cap A_{i_k}\right) =& \sum_{i=1}^n \mathbb{P}(A_i) \\
       &- \sum_{1 \leq i < j \leq n} \mathbb{P}(A_i \cap A_j) \\ &+ \sum_{1 \leq i < j < k \leq n} \mathbb{P}(A_i \cap A_j \cap A_k) \\ &- \cdots \\ &+ (-1)^{n+1} \mathbb{P}(A_1 \cap A_2 \cap \cdots \cap A_n).
   \end{aligned}
   \]

Við höfum þegar séð hvað þessi formúla segir fyrir :math:`n=2` og :math:`n=3`. Fyrir :math:`n=4` segir hún að

.. math::
   :nowrap:

   \[
   \begin{aligned}
           &\mathbb{P}(A_1 \cup A_2 \cup A_3 \cup A_4)  \\
           =\;& \mathbb{P}(A_1) + \mathbb{P}(A_2) + \mathbb{P}(A_3) + \mathbb{P}(A_4)\\
           &-\mathbb{P}(A_1 \cap A_2) - \mathbb{P}(A_1 \cap A_3) - \mathbb{P}(A_1 \cap A_4) - \mathbb{P}(A_2 \cap A_3) - \mathbb{P}(A_2 \cap A_4) - \mathbb{P}(A_3 \cap A_4)\\
           &+ \mathbb{P}(A_1 \cap A_2 \cap A_3) + \mathbb{P}(A_1 \cap A_2 \cap A_4) + \mathbb{P}(A_1 \cap A_3 \cap A_4) + \mathbb{P}(A_2 \cap A_3 \cap A_4)\\
           &-\mathbb{P}(A_1 \cap A_2 \cap A_3 \cap A_4).
   \end{aligned}
   \]

Þessi jafna kallast á ensku *inclusion-exclusion principle*. Eftir að við höfum kynnt til sögunnar *kenniföll* að neðan sýnum við hvernig hægt er að leiða þessa formúlu út.

Samfelldni líkinda
~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining 4.
   :class: box-definition

   Látum :math:`A_1,A_2,\ldots` vera runu af mengjum.

   (1) :math:`A_1,A_2,\ldots` er vaxandi mengjaruna sem stefnir á :math:`A` ef :math:`A_1 \subseteq A_2 \subseteq \cdots` og :math:`\bigcup_{i=1}^\infty A_i = A`. Þetta er táknað með :math:`A_n \uparrow A` eða :math:`A_n \nearrow A` þegar :math:`n \to \infty`.

       .. container:: center

          .. figure:: images/vaxandi_mengjaruna.svg
             :width: 249.22pt
             :align: center

   (2) :math:`A_1,A_2,\ldots` er minnkandi mengjaruna sem stefnir á :math:`A` ef :math:`A_1 \supseteq A_2 \supseteq \cdots` og :math:`\bigcap_{i=1}^\infty A_i = A`. Þetta er táknað með :math:`A_n \downarrow A` eða :math:`A_n \searrow A` þegar :math:`n \to \infty`.

       .. container:: center

          .. figure:: images/minnkandi_mengjaruna.svg
             :width: 249.22pt
             :align: center

.. admonition:: Athugasemd.
   :class: box-remark

   :math:`A_1 \subseteq A_2 \subseteq \cdots` ef og aðeins ef :math:`A_1^c \supseteq A_2^c \supseteq \cdots`. Þar sem

   .. math:: \bigcup_{i=1}^\infty A_i = \left(\bigcap_{i=1}^\infty A_i^c\right)^c \quad\text{þ.e.}\quad \bigcap_{i=1}^\infty A_i^c = \left(\bigcup_{i=1}^\infty A_i\right)^c

   fæst auðveldlega að :math:`A_n \uparrow A` ef og aðeins ef :math:`A_n^c \downarrow A^c`.

Við lýsum nú einum mikilvægasta eiginleika líkinda, sem segir að líkur á atburðum sem mynda vaxandi eða minnkandi mengjarunu stefna á líkurnar á atburðinum sem runan stefnir á.

.. admonition:: Setning 2 (samfelldni líkinda).
   :class: box-theorem

   Látum :math:`(\Omega,{\cal F},\mathbb{P})` vera líkindarúm og :math:`A_1,A_2,\ldots \in {\cal F}`.

   (1) Ef :math:`A_n \uparrow A`, þá gildir að :math:`\mathbb{P}(A_n) \to \mathbb{P}(A)` þegar :math:`n \to \infty`.

   (2) Ef :math:`A_n \downarrow A`, þá gildir að :math:`\mathbb{P}(A_n) \to \mathbb{P}(A)` þegar :math:`n \to \infty`.

.. admonition:: Athugasemd.
   :class: box-remark

   Mikilvægt er að átta sig á muninum á staðhæfingunum :math:`A_n \uparrow A` og :math:`\mathbb{P}(A_n) \to \mathbb{P}(A)` sem eru ólíkar í eðli sínu.

   - :math:`A_n \uparrow A` fjallar um **mengi** og segir að mengjarunan :math:`A_1,A_2,\ldots` sé vaxandi og stefni á :math:`A`, þ.e. að :math:`A_1 \subseteq A_2 \subseteq \cdots` og :math:`\bigcup_{i=1}^\infty A_i = A`.

   - :math:`\mathbb{P}(A_n) \to \mathbb{P}(A)` fjallar um **tölur** og segir að líkurnar á atburðunum :math:`A_n` stefni á líkurnar á atburðinum :math:`A`, þ.e. að :math:`\lim_{n \to \infty} \mathbb{P}(A_n) = \mathbb{P}(A)`.

.. admonition:: Sönnun.
   :class: box-theorem

   (1) Skilgreinum fyrst atburðina :math:`B_1,B_2,\ldots` með :math:`B_1 := A_1` og :math:`B_i := A_i \setminus A_{i-1}` fyrir :math:`i \geq 2` (:math:`B_i` inniheldur öll stök í :math:`A_i` sem hafa ekki komið fyrir í atburðunum :math:`A_1,A_2,\ldots,A_{i-1}`).

       .. container:: center

          .. raw:: html

             <div style="display:flex; justify-content:center; align-items:center; flex-wrap:wrap; gap:0.5rem;">
               <img src="_images/vaxandi_mengjaruna_B_1.svg" style="width:207.68pt; max-width:100%; height:auto;" />
               <img src="_images/vaxandi_mengjaruna_B_2.svg" style="width:207.68pt; max-width:100%; height:auto;" />
             </div>

          .. raw:: html

             <div style="display:flex; justify-content:center; align-items:center; flex-wrap:wrap; gap:0.5rem;">
               <img src="_images/vaxandi_mengjaruna_B_3.svg" style="width:207.68pt; max-width:100%; height:auto;" />
               <img src="_images/vaxandi_mengjaruna_B_4.svg" style="width:207.68pt; max-width:100%; height:auto;" />
             </div>

       Athugum að :math:`B_1,B_2,\ldots` eru sundurlægir atburðir með

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \bigcup_{i=1}^n B_i = A_n, \; n \geq 1, \quad\text{og}\quad \bigcup_{i=1}^\infty B_i = \bigcup_{i=1}^\infty A_i = A.
          \end{aligned}
          \]

       .. container:: center

          .. figure:: images/vaxandi_mengjaruna_B_1_B_2_B_3_B_4.svg
             :width: 249.22pt
             :align: center

       Samkvæmt þriðja grundvallareiginleika líkinda gildir að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \mathbb{P}(A) = \mathbb{P}\left(\bigcup_{i=1}^\infty B_i\right) = \sum_{i=1}^\infty \mathbb{P}(B_i). \quad (\ast)
          \end{aligned}
          \]

       Samkvæmt lið (2) í Setningu 1 gildir að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \mathbb{P}(A_n) = \mathbb{P}\left(\bigcup_{i=1}^n B_i\right) = \sum_{i=1}^n \mathbb{P}(B_i). \quad (\ast\ast)
          \end{aligned}
          \]

       Af :math:`(\ast)` og :math:`(\ast\ast)` leiðir að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \lim_{n \to \infty} \mathbb{P}(A_n) = \sum_{i=1}^\infty \mathbb{P}(B_i) = \mathbb{P}(A).
          \end{aligned}
          \]

   (2) Ef :math:`A_n \downarrow A`, þá gildir að :math:`A_n^c \uparrow A^c`. Samkvæmt lið (1) fæst að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \lim_{n \to \infty} \mathbb{P}(A_n^c) = \mathbb{P}(A^c). \quad (\ast)
          \end{aligned}
          \]

       Því fæst:

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                  \lim_{n \to \infty} \mathbb{P}(A_n) &= 1 - \lim_{n \to \infty} \mathbb{P}(A_n^c) \qquad(\text{skv.~lið (4) í Setningu 1}) \\
                  &= 1 - \mathbb{P}(A^c) \qquad\text{(skv.~$(\ast)$)} \\
                  &= \mathbb{P}(A) \qquad(\text{skv.~lið (4) í Setningu 1}).
          \end{aligned}
          \]

.. admonition:: Athugasemd.
   :class: box-remark

   Í lið (1) í sönnuninni á Setningu 2 var gagnlegt að umrita sammengi atburðanna :math:`A_1,A_2,\ldots` sem sammengi sundurlægu atburðanna :math:`B_1,B_2,\ldots`,

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              \bigcup_{i=1}^\infty A_i = \bigcup_{i=1}^\infty B_i.
      \end{aligned}
      \]

   Þetta gerði okkur kleift að nota þriðja grundvallareiginleika líkinda og lið (2) í Setningu 1, þ.e. að líkur á sammengi sundurlægra atburða séu summan af líkum hvers atburðar.

   Til að ná þessu fram létum við :math:`B_i` innihalda öll stök í :math:`A_i` sem höfðu ekki komið fyrir í atburðunum :math:`A_1,A_2,\ldots,A_{i-1}`. Þar sem mengjarunan var vaxandi gátum við einfaldlega sett :math:`B_i := A_i \setminus A_{i-1}` fyrir :math:`i \geq 2`, þ.e. látið :math:`B_i` innihalda öll stök í :math:`A_i` sem voru ekki í :math:`A_{i-1}`.

   Fyrir almenna mengjarunu :math:`A_1,A_2,\ldots` getum við með sömu hugmynd skilgreint :math:`B_1 = A_1` og

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              B_i := A_i \mathbin{\big\backslash} \left(\bigcup_{j=1}^{i-1} A_j\right),
      \end{aligned}
      \]

   þ.e. :math:`B_i` inniheldur öll stök í :math:`A_i` sem hafa ekki komið fyrir í neinum atburðanna :math:`A_1,A_2,\ldots,A_{i-1}`.

   .. container:: center

      .. figure:: images/boole_sonnun.svg
         :width: 377.93pt
         :align: center

   Þá eru :math:`B_1,B_2,\ldots` sundurlæg og

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              \bigcup_{i=1}^\infty A_i = \bigcup_{i=1}^\infty B_i,
      \end{aligned}
      \]

   sem gerir okkur kleift að skrifa sammengi atburðanna :math:`A_1,A_2,\ldots` sem sammengi sundurlægra atburða.

.. admonition:: Setning 3 (óendanlega Boole-ójafnan).
   :class: box-theorem

   Látum :math:`(\Omega,{\cal F},\mathbb{P})` vera líkindarúm og :math:`A_1,A_2,\ldots \in {\cal F}`. Þá gildir að

   .. math::
      :nowrap:

      \[
      \begin{aligned}
          \mathbb{P}\left(\bigcup_{i=1}^\infty A_i\right) \leq \sum_{i=1}^\infty \mathbb{P}(A_i).
      \end{aligned}
      \]

   .. container:: center

      .. figure:: images/ekki_sundurlaegir_fleiri_n.svg
         :width: 255.86pt
         :align: center

Óendanlegu Boole-ójöfnuna er hægt að sanna með því að skrifa :math:`\bigcup_{i=1}^\infty` sem sammengi sundurlægra atburða eins og lýst er í athugasemd að framan, eða með því að nota niðurstöðu Setningar 2 um samfelldni líkinda. Í skiladæmum eruð þið beðin um að setja fram báðar sannanir.

.. admonition:: Sönnun.
   :class: box-theorem

   Æfing.


