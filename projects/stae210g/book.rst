.. sectnum::
   :depth: 2

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

Poisson-ferli og Gamma-dreifingin
=================================

Skilgreining á Poisson-ferli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við kynntum Poisson-ferli óformlega til sögunnar í Lík&töl. Poisson-ferli lýsir streymi atburða, t.d. fjölda koma á bráðamóttökuna eða fjölda bíla sem fara framhjá ákveðnum punkti á þjóðveginum, sem er þannig að í mesta lagi einn atburður verði yfir hvert stutt tímabil, litlar líkur séu á atburði á hverju stuttu tímabil, og atburðir séu óháðir milli tímabila. Poisson-ferli má óformlega smíða með því að kasta krónum. Við skiptum þá tímaásnum niður í stutt tímabil og köstum krónu á hverju tímabili til að ákvarða hvort atburður gerist á tímabilinu eða ekki, á þann veg að útkomur krónukastanna séu óháðar milli tímabila.

Poisson-ferli með stika :math:`\lambda>0` má formlega skilgreina þannig að tímarnir sem líða milli atburða séu óháðar veldisstærðir með stika :math:`\lambda`. Við sjáum líka í umfjöllun okkar um hermun að ef Poisson-ferli er skilgreint þannig, þá hefur fjöldi atburða sem gerist á tímabilinu :math:`[0,T]` Poisson-dreifingu með stika :math:`\lambda T`. Munum að slembistærð :math:`Y` sem hefur Poisson-dreifingu með stika :math:`\mu>0` hefur líkindafall

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{P}(Y=k) = e^{-\mu} \frac{\mu^k}{k!}, \quad k=0,1,2,\ldots.
   \end{aligned}
   \]

Við ætlum nú að setja Poisson-ferli fram á skipulegri hátt og lýsa helstu eiginleikum þess. Fyrst kynnum við til sögunnar helstu hugtökin á mynd.

.. container:: center

   .. figure:: images/poisson_ferli_hermun.svg
      :width: 301.98pt
      :align: center

Látum :math:`X_1,X_2,\ldots` vera óháðar veldisstærðir með stika :math:`\lambda>0`. Poisson-ferli er skilgreint þannig að tíminn sem líður fram að fyrsta atburði er :math:`S_1 = X_1`, tíminn sem líður fram að öðrum atburði er :math:`S_2 = X_1+X_2`, og svo koll af kolli. Almennt eru atburðatímarnir táknaðir með :math:`S_1,S_2,\ldots`, þar sem :math:`S_n = X_1+X_2+\cdots+X_n` fyrir :math:`n \geq 1` er tíminn sem :math:`n`-ti atburðurinn gerist á. :math:`X_1,X_2,\ldots` eru tímarnir sem líða milli atburða. Fjölda atburða sem gerist fram að tíma :math:`t` má lýsa svona:

.. math::
   :nowrap:

   \[
   \begin{aligned}
    N(t) &= \max\{n \geq 0: S_n \leq t\}.
   \end{aligned}
   \]

Á myndinni að ofan er til dæmis :math:`N(t)=4`. Setjum nú skilgreininguna formlega fram.

.. admonition:: Skilgreining 15.
   :class: box-definition

   Látum :math:`X_1,X_2,\ldots` vera óháðar veldisstærðir með stika :math:`\lambda>0`. Setjum :math:`S_0 := 0` og skilgreinum fyrir sérhvert :math:`n \geq 1`:

   .. math:: S_n := X_1 + X_2 + \cdots +X_n.

   Skilgreinum jafnframt fyrir sérhvert :math:`t \geq 0`:

   .. math::
      :nowrap:

      \[
      \begin{aligned}
              N(t) :=  \max\{n \geq 0: S_n \leq t\}.
      \end{aligned}
      \]

   Safnið :math:`\big(N(t)\big)_{t \geq 0}` af slembistærðunum :math:`N(t)` fyrir :math:`t \geq 0` kallast Poisson-ferli með stika :math:`\lambda`. Slembistærðirnar :math:`S_1,S_2,\ldots` kallast **atburðatímar** ferlisins og slembistærðin :math:`N(t)` er túlkuð sem fjöldi atburða sem gerist fram að tíma :math:`t`.

Munum að veldisstærð :math:`X` með stika :math:`\lambda>0` er **minnislaus**, sem þýðir að fyrir sérhverjar rauntölur :math:`a,b \geq 0` gildir að

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{P}(X>a+b \,|\, X>a) = \mathbb{P}(X>b).
   \end{aligned}
   \]

Ef við segjum að :math:`X` lýsi endingartíma tækis, þá þýðir minnisleysið að alltaf þegar við spyrjum hverjar líkurnar eru á að tækið endist ákveðinn tíma til viðbótar, þá eru líkurnar óháðar aldri tækisins á þeim tíma sem við spyrjum.

Minnisleysi veldisstærðarinnar einfaldar mjög greiningu á Poisson-ferlum, en minnisleysið leiðir líka til hegðunar sem virðist oft skrítin þegar fljótt er á litið. Sem dæmi: Ef við göngum inn í Poisson-ferli með stika :math:`\lambda>0`, þá hefur tíminn sem líður fram að næsta atburði veldisdreifingu með stika :math:`\lambda`, sama hversu langt er síðan síðasti atburður gerðist. Þetta hefur í för með sér að bilið sem við göngum inn í er lengra en bil sem valið er af handahófi (raunar er það tvöfalt lengra). Þetta er oft kallað ,,skoðunarþversögnin“, sem nánar er fjallað um í hermunarverkefninu.

Helstu eiginleikar Poisson-ferlis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 20.
   :class: box-theorem

   Látum :math:`\big(N(t)\big)_{t \geq 0}` vera Poisson-ferli með stika :math:`\lambda`.

   (1) Fyrir sérhvert :math:`n \geq 1` og :math:`0 < t_1 < t_2 < \cdots < t_n` gildir að

       .. math:: N(t_1), N(t_2)-N(t_1), \ldots, N(t_n)-N(t_{n-1})

       eru óháðar slembistærðir.

   (2) Setjum :math:`t_0:=0`. Fyrir sérhvert :math:`i=1,\ldots,n` hefur slembistærðin :math:`N(t_i)-N(t_{i-1})` Poisson-dreifingu með stika :math:`\mu_i := \lambda (t_i-t_{i-1})`. Þetta þýðir að

       .. math::
          :nowrap:

          \[
          \begin{aligned}
                      \mathbb{P}\big(N(t_i)-N(t_{i-1}) = k\big) &=  e^{-\mu_i} \frac{\left(\mu_i\right)^k}{k!} \\
                      &= e^{-\lambda (t_i-t_{i-1})} \frac{\big(\lambda (t_i-t_{i-1})\big)^k}{k!}
          \end{aligned}
          \]

       fyrir sérhvert :math:`k=0,1,2,\ldots`.

   (3) Látum :math:`n \geq 1`, látum :math:`U_1,U_2,\ldots,U_n` vera óháðar slembistærðir með jafna dreifingu á bilinu :math:`[0,T]` og látum :math:`U_{(1)},\ldots,U_{(n)}` tákna sömu stærðir eftir að þeim hefur verið raðað í (vaxandi) stærðarröð. Ef skilyrt er með :math:`\{N(T)=n\}`, þá hafa atburðatímarnir :math:`S_1,S_2,\ldots,S_n` sömu dreifingu og :math:`U_{(1)},\ldots,U_{(n)}`.

.. admonition:: Athugasemd.
   :class: box-remark

   Þar sem :math:`N(t_i)` er fjöldi atburða sem gerist fram að tíma :math:`t_i`, þá er :math:`N(t_i)-N(t_{i-1})` einfaldlega fjöldi atburða sem gerist á tímabilinu :math:`(t_{i-1},t_i]` fyrir :math:`i=1,\ldots,n`. Athugum að ef við setjum :math:`t_0 := 0`, þá er :math:`N(t_1)-N(t_0) = N(t_1)`.

   .. container:: center

      .. figure:: images/poisson_independent_increments.svg
         :width: 378.37pt
         :align: center

   | Liður (1) í Setningu 20 segir óformlega að fjöldi atburða sem gerist á tilteknu tímabili er óháður fjölda atburða sem gerist á öðrum tímabilum. Þetta er mjög eðlilegt ef við hugsum Poisson-ferli þannig að óháðum krónum sé kastað til að ákvarða hvenær atburðir gerast. Einnig er þetta afleiðing af minnisleysi veldisstærðarinnar, sem við fjölluðum um í Fyrirlestri 3. Liður (2) segir að fjöldi atburða á tímabilinu :math:`(t_{i-1},t_i]` hafi Poisson-dreifingu með stika sem er í réttu hlutfalli við lengd tímabilsins. Aftur er eðlilegt að fjöldi atburða sem gerist á tilteknu tímabili sé háður lengd tímabilsins.
   | Liðir (3) í Setningu 20 að ef við vitum að :math:`n` atburðir gerast fram að tíma :math:`T` í Poisson-ferli, þá má fá atburðatímana :math:`S_1,S_2,\ldots,S_n` með því að velja :math:`n` punkta af handahófi milli :math:`0` og :math:`T` og láta :math:`S_1` vera lægsta punktinn, :math:`S_2` næstlægsta punktinn, og svo koll af kolli. Ef við vitum fjölda atburða á tímabilinu :math:`[0,T]` er þess vegna enginn hluti tímabilsins líklegri til að innihalda atburð en einhver annar hluti þess. Þetta er aftur eðlilegt ef við höfum í huga að Poisson-ferli má hugsa þannig að óháðum krónum sé kastað til að ákvarða hvenær atburðirnir gerast.

Gamma-dreifingin
~~~~~~~~~~~~~~~~

Tíminn sem líður fram að :math:`n`-ta atburði í Poisson-ferli er gefinn með

.. math::
   :nowrap:

   \[
   \begin{aligned}
       S_n = X_1+X_2+\cdots+X_n
   \end{aligned}
   \]

þar sem :math:`X_1,X_2,\ldots,X_n` eru óháðar veldisstærðir með sama stikann :math:`\lambda`. Í hermunarverkefninu sýnum við að stærðin :math:`S_n` hefur svokallaða *Gamma-dreifingu* með stika :math:`n` og :math:`\lambda`, sem er samfelld dreifing með þéttleikann

.. math::
   :nowrap:

   \[
   \begin{aligned}
           f(x) = \begin{cases}
               \dfrac{\lambda^n}{(n-1)!} x^{n-1} e^{-\lambda x}, & x \geq 0, \\ 0, & x<0.
           \end{cases}
   \end{aligned}
   \]



Þegar :math:`n=1` fæst þéttleikinn

.. math::
   :nowrap:

   \[
   \begin{aligned}
           f(x) = \begin{cases}
               {\lambda} e^{-\lambda x}, & x \geq 0, \\ 0, & x<0.
           \end{cases}
   \end{aligned}
   \]

sem er þéttleiki veldisdreifingar. Þar sem væntigildi er línulegt gildir að

.. math:: E[S_n] = \mathbb{E}[X_1]+\mathbb{E}[X_2] + \cdots + \mathbb{E}[X_n] = n/\lambda.

Hermun
======

Hvað er hermun og af hverju er hún gagnleg?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Óformlega höfum við hugsað um slembistærð svona: Gildið sem hún tekur fer eftir útkomunni úr einhverri tilraun sem er háð tilviljun eins og krónukasti eða teningakasti. Til dæmis, ef krónu er kastað og líkurnar á að þorskurinn komi upp eru :math:`p \in (0,1)`, þá höfum við kynnt til sögunnar Bernoulli-stærð :math:`X` sem tekur gildið :math:`X=1` þegar þorskurinn kemur upp og :math:`X=0` þegar bergrisinn kemur upp. Hingað til höfum við fjallað um líkurnar á að slembistærð taki eitthvert gildi (strjál slembistærð) eða að hún taki gildi á einhverju bili (samfelld slembistærð), en við höfum ekki fjallað um hvernig á að ,,raungera“ slembistærðina.

Að *herma* slembistærð er að gefa henni gildi með aðferð sem tryggir að líkurnar á að gildið komi upp samræmist líkindadreifingu slembistærðarinnar. Við segjum líka að við ,,búum til“, ,,framleiðum“ eða ,,raungerum“ slembistærðina. Í umfjölluninni sem fylgir gerum við ráð fyrir að við getum raungert jafna dreifingu á bilinu :math:`(0,1)`, þ.e. að við getum valið tölu af handahófi milli 0 og 1. Ýmsum aðferðum má beita til þess sem eru utan umfjöllunarefnis þessa námskeiðs. Við ætlum hins vegar að sýna hvernig hægt er að nota tölur sem valdar eru af handahófi milli 0 og 1 til að búa til slembistærðir með þekktar líkindadreifingar.

Hermun er mjög gagnleg þegar við vinnum með slembistærð eða slembiferli sem við þekkjum lítið og við viljum skilja hegðun t.d. slembiferlisins betur. Oftast er fljótlegra að herma slembiferlið og sjá hvað gerist en að leiða hegðunina út stærðfræðilega. Einnig getur hermunin verið vegvísir fyrir stærðfræðilegu greininguna. Hermun er loks gagnleg þegar unnið er með mjög flókið slembiferli sem erfitt er að greina stærðfræðilega. Hermunarlíkön geta t.d. verið notuð til að spá fyrir um hraunflæði á Reykjanesskaga og leggja mat á hversu líklegar tilteknar sviðsmyndir eru, þau eru notuð innan verkfræði til að skilja og hanna flókin kerfi og þau eru mjög vinsæl innan fjármálageirans þar sem þau eru kennd við *Monte Carlo* aðferðir.

Hermun á krónukasti
~~~~~~~~~~~~~~~~~~~

Fyrir jafndreifða stærð :math:`U` á bilinu :math:`(0,1)` og :math:`p \in (0,1)` gildir að

.. math:: \mathbb{P}(U < p) = \mathbb{P}(U \leq p) = p.

Skilgreinum slembistærðina :math:`X` þannig að hún sé háð gildinu á :math:`U` á eftirfarandi hátt:

.. math::
   :nowrap:

   \[
   \begin{aligned}
    X = \begin{cases} 1, & \text{ef $U < p$}, \\ 0, & \text{ef $U \geq p$.} \end{cases}
   \end{aligned}
   \]

Takið eftir að :math:`X` er Bernoulli-stærð með stika :math:`p`, vegna þess að

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{P}(X = 1) = \mathbb{P}(U < p) = p
   \end{aligned}
   \]

og :math:`\mathbb{P}(X=0)=\mathbb{P}(U \geq p) = 1-p`. Við getum þess vegna raungert Bernoulli-stærð út frá tölu sem er valin af handahófi milli 0 og 1, eins og við sýnum í R hér að neðan. Munið síðan úr Lík&töl að tvíkostastærð með stika :math:`n` og :math:`p` er hægt að hugsa sem summu af Bernoulli-stærðum,

.. math::
   :nowrap:

   \[
   \begin{aligned}
    X = X_1+X_2+\cdots+X_n,
   \end{aligned}
   \]

þar sem :math:`X_1,X_2,\ldots,X_n` eru óháðar Bernoulli-stærðir með stika :math:`p`. Þetta gefur einfalda aðferð til að herma tvíkostastærð.

Lögmál mikils fjölda
~~~~~~~~~~~~~~~~~~~~

Látum :math:`X` vera gefna slembistærð og látum :math:`X_1,X_2,\ldots` vera óháðar slembistærðir sem allar hafa sömu dreifingu og :math:`X`. Skilgreinum :math:`\bar{X}_n := \frac1n \sum_{i=1}^n X_i` sem meðalgildið sem fyrstu :math:`n` slembistærðirnar taka. *Lögmál mikils fjölda* segir óformlega að :math:`\bar{X}_n` nálgist væntigildið :math:`\mu = \mathbb{E}[X]` eftir því sem :math:`n` stækkar. Í hermunarsamhenginu segir lögmál mikils fjölda að ef við hermum óháð gildi fyrir slembistærðina :math:`X`, og reiknum meðaltal gildanna sem fást með hermuninni, þá nálgumst við væntigildið :math:`\mu` eftir því sem við hermum fleiri gildi.

Látum :math:`X_1,X_2,\ldots` vera óháðar Bernoulli-stærðir með stika :math:`p \in (0,1)`. Í þessu tilviki lýsir :math:`\bar{X}_n = \frac1n \sum_{i=1}^n X_i` hlutfallstíðni atburðarins að þorskurinn komi upp yfir fyrstu :math:`n` köstin. Væntigildi Bernoulli-stærðar með stika :math:`p` er

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{E}[X_1] = p \cdot 1 + (1-p) \cdot 0 = p.
   \end{aligned}
   \]

Fyrir Bernoulli-stærð með stika :math:`p` segir lögmál mikils fjölda að ef við hermum óháð krónuköst aftur og aftur, þá nálgast hlutfallstíðni atburðarins að þorskurinn komi upp einfaldlega líkurnar :math:`p` á atburðinum. Til að fá betri tilfinningu fyrir lögmáli mikils fjölda hermum við Bernoulli-stærðina í R.

.. rubric:: Hermun á krónukasti

.. code-block:: r

   #Fall sem hermir Bernoulli-stærð (krónukast) N sinnum.
   #p eru líkurnar á að þorskurinn komi upp.
   kronukast_hermun <- function(N,p){
     #results_vec er vigur sem geymir hermdu gildin.
     results_vec <- c(1:N)
     #Hermum N gildi fyrir Bernoulli stærð með stika p.
     for (j in 1:N){
         #Veljum tölu u af handahófi milli 0 og 1.
         u <- runif(1,0,1)
         #Búum til Bernoulli-stærð með stika p með því að nota gildið á u.
         #(u<p) gefur gildið TRUE ef u<p og gildið FALSE annars,
         #sem breytist í 1/0 þegar við vistum í vigurinn results_vec.
         results_vec[j] <- (u<p)
     }
     #Skilum vigrinum með hermdu gildunum.
     return(results_vec)
   }

Búum síðan til fall sem tekur inn hermd gildi fyrir Bernoulli-stærð með stika :math:`p` og teiknar samanburðarmynd sem ber saman hlutfallstíðnir gildanna sem hermunin gefur og massafall Bernoulli-dreifingar með stika :math:`p`. Samkvæmt lögmáli mikils fjölda eiga hlutfallstíðnirnar að nálgast massafallið eftir því sem við hermum fleiri gildi.

.. rubric:: Samanburður á hermdri hlutfallstíðni og massafalli Bernoulli-dreifingar

.. code-block:: r

   #Notum ggplot2 til að teikna.
   library(ggplot2)
   #Þessi valkostur sýnir tölur eins og 10^5 sem 100000.
   options(scipen=999)
   #Fall sem tekur inn hermd gildi og teiknar mynd sem ber saman hlutfallstíðni
   #gildanna í hermuninni við massafall Bernoulli-dreifingar með stika p.
   teikna_kronukast <- function(results_vec,p){
     #Finnum stærsta gildið sem kom út úr hermuninni.
     max_gildi <- max(results_vec)
     #Reiknum hlutfallstíðni hermdu gildanna.
     #hist býr til tíðnitöflu (e. histogram) þar sem (-1:y)+0.5
     #skilgreinir bilin sem notuð eru til að útbúa tíðnitöfluna.
     #"plot = FALSE" segir R að teikna ekki stuðlaritið (við gerum það síðar).
     tidnirit <- hist(results_vec, breaks = (-1:max_gildi)+0.5, plot = FALSE)
     #Búum til gagnasafn sem geymir gögnin fyrir hermdu hlutfallstíðnirnar.
     hlutfallstidni <- data.frame(
       x_gildi = 0:max_gildi,
       #tidnirit$density gefur hlutfallstíðnirnar
       y_gildi = tidnirit$density, 
       audkenni="Hermd hlutfallstíðni"
     )
     #Búum til gagnasafn sem geymir massafall Bernoulli-dreifingar með stika p.
     bernoulli_massafall <- data.frame(
       x_gildi = 0:max_gildi,
       y_gildi = dbinom(0:max_gildi, 1, p),
       audkenni="Massafall Bernoulli-dreifingar"
     )
     #Sameinum gagnasöfnin
     sameinud_gogn <- rbind(hlutfallstidni, bernoulli_massafall)
     #Teiknum samanburðarmyndina.
     ggplot(sameinud_gogn,aes(x=x_gildi,y=y_gildi,fill=audkenni)) + 
       #geom_bar teiknar stöplarit.
       #position = "dodge" teiknar tvö stöplarit hlið við hlið.
       #alpha = 0.8 stjórnar hversu ógegnsær liturinn er.
       geom_bar(stat = "identity", position = "dodge", alpha = 0.8) + 
       labs(title = paste("Niðurstöður fyrir p =",p,"og N =",N), caption = paste("Samanburður á hermdri hlutfallstíðni fyrir Bernoulli-stærð með stika p =",p,"\nog massafalli Bernoulli-dreifingar með stika p =",p), x = "Gildi slembistærðarinnar", y ="") +
       scale_fill_manual(name="", values = c("Hermd hlutfallstíðni" = 'steelblue3', "Massafall Bernoulli-dreifingar" = 'brown3')) + 
       theme(plot.caption=element_text(size=11, hjust=0, face="italic", color="black"))
   }

.. rubric:: Gagnvirkur R-leikvöllur

.. raw:: html

   <div data-datacamp-exercise data-lang="r" data-height="600">
     <code data-type="pre-exercise-code">
       try(Sys.setlocale(&#39;LC_CTYPE&#39;, &#39;C.UTF-8&#39;), silent=TRUE)

       #Fall sem hermir Bernoulli-st\u00E6r\u00F0 (kr\u00F3nukast) N sinnum.
       #p eru l\u00EDkurnar \u00E1 a\u00F0 \u00FEorskurinn komi upp.
       kronukast_hermun &lt;- function(N,p){
         #results_vec er vigur sem geymir hermdu gildin.
         results_vec &lt;- c(1:N)
         #Hermum N gildi fyrir Bernoulli st\u00E6r\u00F0 me\u00F0 stika p.
         for (j in 1:N){
             #Veljum t\u00F6lu u af handah\u00F3fi milli 0 og 1.
             u &lt;- runif(1,0,1)
             #B\u00FAum til Bernoulli-st\u00E6r\u00F0 me\u00F0 stika p me\u00F0 \u00FEv\u00ED a\u00F0 nota gildi\u00F0 \u00E1 u.
             #(u&lt;p) gefur gildi\u00F0 TRUE ef u&lt;p og gildi\u00F0 FALSE annars,
             #sem breytist \u00ED 1/0 \u00FEegar vi\u00F0 vistum \u00ED vigurinn results_vec.
             results_vec[j] &lt;- (u&lt;p)
         }
         #Skilum vigrinum me\u00F0 hermdu gildunum.
         return(results_vec)
       }

       #Notum ggplot2 til a\u00F0 teikna.
       library(ggplot2)
       #\u00DEessi valkostur s\u00FDnir t\u00F6lur eins og 10^5 sem 100000.
       options(scipen=999)
       #Fall sem tekur inn hermd gildi og teiknar mynd sem ber saman hlutfallst\u00ED\u00F0ni
       #gildanna \u00ED hermuninni vi\u00F0 massafall Bernoulli-dreifingar me\u00F0 stika p.
       teikna_kronukast &lt;- function(results_vec,p){
         #Finnum st\u00E6rsta gildi\u00F0 sem kom \u00FAt \u00FAr hermuninni.
         max_gildi &lt;- max(results_vec)
         #Reiknum hlutfallst\u00ED\u00F0ni hermdu gildanna.
         #hist b\u00FDr til t\u00ED\u00F0nit\u00F6flu (e. histogram) \u00FEar sem (-1:y)+0.5
         #skilgreinir bilin sem notu\u00F0 eru til a\u00F0 \u00FAtb\u00FAa t\u00ED\u00F0nit\u00F6fluna.
         #&quot;plot = FALSE&quot; segir R a\u00F0 teikna ekki stu\u00F0lariti\u00F0 (vi\u00F0 gerum \u00FEa\u00F0 s\u00ED\u00F0ar).
         tidnirit &lt;- hist(results_vec, breaks = (-1:max_gildi)+0.5, plot = FALSE)
         #B\u00FAum til gagnasafn sem geymir g\u00F6gnin fyrir hermdu hlutfallst\u00ED\u00F0nirnar.
         hlutfallstidni &lt;- data.frame(
           x_gildi = 0:max_gildi,
           #tidnirit$density gefur hlutfallst\u00ED\u00F0nirnar
           y_gildi = tidnirit$density, 
           audkenni=&quot;Hermd hlutfallst\u00ED\u00F0ni&quot;
         )
         #B\u00FAum til gagnasafn sem geymir massafall Bernoulli-dreifingar me\u00F0 stika p.
         bernoulli_massafall &lt;- data.frame(
           x_gildi = 0:max_gildi,
           y_gildi = dbinom(0:max_gildi, 1, p),
           audkenni=&quot;Massafall Bernoulli-dreifingar&quot;
         )
         #Sameinum gagnas\u00F6fnin
         sameinud_gogn &lt;- rbind(hlutfallstidni, bernoulli_massafall)
         #Teiknum samanbur\u00F0armyndina.
         ggplot(sameinud_gogn,aes(x=x_gildi,y=y_gildi,fill=audkenni)) + 
           #geom_bar teiknar st\u00F6plarit.
           #position = &quot;dodge&quot; teiknar tv\u00F6 st\u00F6plarit hli\u00F0 vi\u00F0 hli\u00F0.
           #alpha = 0.8 stj\u00F3rnar hversu \u00F3gegns\u00E6r liturinn er.
           geom_bar(stat = &quot;identity&quot;, position = &quot;dodge&quot;, alpha = 0.8) + 
           labs(title = paste(&quot;Ni\u00F0urst\u00F6\u00F0ur fyrir p =&quot;,p,&quot;og N =&quot;,N), caption = paste(&quot;Samanbur\u00F0ur \u00E1 hermdri hlutfallst\u00ED\u00F0ni fyrir Bernoulli-st\u00E6r\u00F0 me\u00F0 stika p =&quot;,p,&quot;\nog massafalli Bernoulli-dreifingar me\u00F0 stika p =&quot;,p), x = &quot;Gildi slembist\u00E6r\u00F0arinnar&quot;, y =&quot;&quot;) +
           scale_fill_manual(name=&quot;&quot;, values = c(&quot;Hermd hlutfallst\u00ED\u00F0ni&quot; = &#39;steelblue3&#39;, &quot;Massafall Bernoulli-dreifingar&quot; = &#39;brown3&#39;)) + 
           theme(plot.caption=element_text(size=11, hjust=0, face=&quot;italic&quot;, color=&quot;black&quot;))
       }
     </code>
     <code data-type="sample-code">
       # Velji\u00F0 N og p og keyri\u00F0 hermunina.
       N &lt;- 10000
       p &lt;- 0.5
       gildi &lt;- kronukast_hermun(N, p)
       teikna_kronukast(gildi, p)
     </code>
   </div>

Látum :math:`(\Omega,{\cal F},\mathbb{P})` vera líkindarúm. Munið að kennifall atburðar :math:`A \in {\cal F}` var slembistærðin :math:`1_A: \Omega \to \mathbb{R}` sem skilgreind var svona:

.. math::
   :nowrap:

   \[
   \begin{aligned}
    1_A(\omega) := \begin{cases} 1, & \text{ef $\omega \in A$,} \\ 0, & \text{ef $\omega \notin A$.} \end{cases}
   \end{aligned}
   \]

Takið eftir að :math:`1_A` er Bernoulli-stærð með stika :math:`p = \mathbb{P}(A)`. Ímyndum okkur að atburðurinn :math:`A` sé tengdur einhverri tilraun eins og teningakasti. Ef við beitum lögmáli mikils fjölda á stærðina :math:`1_A`, þá segir lögmálið að ef við endurtökum tilraunina aftur og aftur, þá nálgast hlutfallstíðni þess að atburðurinn :math:`A` gerist einfaldlega líkurnar á atburðinum :math:`\mathbb{P}(A)`. Hermum tvíkostastærð í R og sjáum að hlutfallstíðnir gildanna nálgist líkurnar á að stærðin taki hvert gildi.

.. rubric:: Hermun á tvíkostastærð

.. code-block:: r

   #Fall sem hermir tvíkostastærð N sinnum.
   #n og p eru stikar tvíkostastærðarinnar.
   tvikostastaerd_hermun <- function(N,n,p){
     #results_vec er vigur sem geymir hermdu gildin.
     results_vec <- c(1:N)
     #Hermum N gildi fyrir tvíkostastærð með stika n og p.
     for (j in 1:N){
         #Hermum n Bernouli-stærðir með stika p 
         #með kóðanum sem við bjuggum til að ofan.
         x <- kronukast_hermun(n,p)
         #Búum til tvíkostastærð með því að leggja saman gildi Bernoulli-stærðanna.
         results_vec[j] <- sum(x)
     }
     #Skilum vigrinum með hermdu gildunum.
     return(results_vec)
   }

Búum síðan til fall sem tekur inn hermd gildi fyrir tvíkostastærð með stika :math:`n` og :math:`p` og teiknar samanburðarmynd sem ber saman hlutfallstíðnir gildanna sem hermunin gefur og massafall tvíkostadreifingar með stika :math:`n` og :math:`p`. Athugið að kóðinn er mjög svipaður og kóðinn sem við notuðum fyrir Bernoulli-dreifinguna að ofan.

.. rubric:: Samanburður á hermdri hlutfallstíðni og massafalli tvíkostdreifingar

.. code-block:: r

   #Notum ggplot2 til að teikna.
   library(ggplot2)
   #Þessi valkostur sýnir tölur eins og 10^5 sem 100000.
   options(scipen=999)
   #Fall sem tekur inn hermd gildi og teiknar mynd sem ber saman hlutfallstíðni
   #gilda í hermuninni við massafall tvíkostadreifingar með stika n og p.
   teikna_tvikostastaerd <- function(results_vec,n,p){
     #Finnum stærsta gildið sem kom út úr hermuninni.
     max_gildi <- max(results_vec)
     #Reiknum hlutfallstíðni hermdu gildanna.
     tidnirit <- hist(results_vec, breaks = (-1:max_gildi)+0.5, plot = FALSE)
     #Búum til gagnasafn sem geymir gögnin fyrir hermdu hlutfallstíðnirnar.
     hlutfallstidni <- data.frame(
       x_gildi = 0:max_gildi,
       #tidnirit$density gefur hlutfallstíðnirnar
       y_gildi = tidnirit$density, 
       audkenni="Hermd hlutfallstíðni"
     )
     #Búum til gagnasafn sem geymir massafall tvíkostadreifingar með stika n og p.
     tvikosta_massafall <- data.frame(
       x_gildi = 0:max_gildi,
       y_gildi = dbinom(0:max_gildi, n, p),
       audkenni="Massafall tvíkostadreifingar"
     )
     #Sameinum gagnasöfnin
     sameinud_gogn <- rbind(hlutfallstidni, tvikosta_massafall)
     ggplot(sameinud_gogn,aes(x=x_gildi,y=y_gildi,fill=audkenni)) + 
       #Notum geom_bar til að teikna stöplarit.
       geom_bar(stat = "identity", position = "dodge", alpha = 0.8) + 
       labs(title = paste("Niðurstöður fyrir p =",p,"og N =",N), caption = paste("Samanburður á hermdri hlutfallstíðni fyrir tvíkostastærð með stika n =",n,"og p =",p,"\nog massafalli tvíkostadreifingar með stika n =",n,"og p =",p), x = "Gildi slembistærðarinnar", y ="") +
       scale_fill_manual(name="", values = c("Hermd hlutfallstíðni" = 'steelblue3', "Massafall tvíkostadreifingar" = 'brown3')) + 
     theme(plot.caption=element_text(size=11, hjust=0, face="italic", color="black"))
   }

.. rubric:: Gagnvirkur R-leikvöllur

.. raw:: html

   <div data-datacamp-exercise data-lang="r" data-height="600">
     <code data-type="pre-exercise-code">
       try(Sys.setlocale(&#39;LC_CTYPE&#39;, &#39;C.UTF-8&#39;), silent=TRUE)

       #Fall sem hermir Bernoulli-st\u00E6r\u00F0 (kr\u00F3nukast) N sinnum.
       #p eru l\u00EDkurnar \u00E1 a\u00F0 \u00FEorskurinn komi upp.
       kronukast_hermun &lt;- function(N,p){
         #results_vec er vigur sem geymir hermdu gildin.
         results_vec &lt;- c(1:N)
         #Hermum N gildi fyrir Bernoulli st\u00E6r\u00F0 me\u00F0 stika p.
         for (j in 1:N){
             #Veljum t\u00F6lu u af handah\u00F3fi milli 0 og 1.
             u &lt;- runif(1,0,1)
             #B\u00FAum til Bernoulli-st\u00E6r\u00F0 me\u00F0 stika p me\u00F0 \u00FEv\u00ED a\u00F0 nota gildi\u00F0 \u00E1 u.
             #(u&lt;p) gefur gildi\u00F0 TRUE ef u&lt;p og gildi\u00F0 FALSE annars,
             #sem breytist \u00ED 1/0 \u00FEegar vi\u00F0 vistum \u00ED vigurinn results_vec.
             results_vec[j] &lt;- (u&lt;p)
         }
         #Skilum vigrinum me\u00F0 hermdu gildunum.
         return(results_vec)
       }

       #Fall sem hermir tv\u00EDkostast\u00E6r\u00F0 N sinnum.
       #n og p eru stikar tv\u00EDkostast\u00E6r\u00F0arinnar.
       tvikostastaerd_hermun &lt;- function(N,n,p){
         #results_vec er vigur sem geymir hermdu gildin.
         results_vec &lt;- c(1:N)
         #Hermum N gildi fyrir tv\u00EDkostast\u00E6r\u00F0 me\u00F0 stika n og p.
         for (j in 1:N){
             #Hermum n Bernouli-st\u00E6r\u00F0ir me\u00F0 stika p 
             #me\u00F0 k\u00F3\u00F0anum sem vi\u00F0 bjuggum til a\u00F0 ofan.
             x &lt;- kronukast_hermun(n,p)
             #B\u00FAum til tv\u00EDkostast\u00E6r\u00F0 me\u00F0 \u00FEv\u00ED a\u00F0 leggja saman gildi Bernoulli-st\u00E6r\u00F0anna.
             results_vec[j] &lt;- sum(x)
         }
         #Skilum vigrinum me\u00F0 hermdu gildunum.
         return(results_vec)
       }

       #Notum ggplot2 til a\u00F0 teikna.
       library(ggplot2)
       #\u00DEessi valkostur s\u00FDnir t\u00F6lur eins og 10^5 sem 100000.
       options(scipen=999)
       #Fall sem tekur inn hermd gildi og teiknar mynd sem ber saman hlutfallst\u00ED\u00F0ni
       #gilda \u00ED hermuninni vi\u00F0 massafall tv\u00EDkostadreifingar me\u00F0 stika n og p.
       teikna_tvikostastaerd &lt;- function(results_vec,n,p){
         #Finnum st\u00E6rsta gildi\u00F0 sem kom \u00FAt \u00FAr hermuninni.
         max_gildi &lt;- max(results_vec)
         #Reiknum hlutfallst\u00ED\u00F0ni hermdu gildanna.
         tidnirit &lt;- hist(results_vec, breaks = (-1:max_gildi)+0.5, plot = FALSE)
         #B\u00FAum til gagnasafn sem geymir g\u00F6gnin fyrir hermdu hlutfallst\u00ED\u00F0nirnar.
         hlutfallstidni &lt;- data.frame(
           x_gildi = 0:max_gildi,
           #tidnirit$density gefur hlutfallst\u00ED\u00F0nirnar
           y_gildi = tidnirit$density, 
           audkenni=&quot;Hermd hlutfallst\u00ED\u00F0ni&quot;
         )
         #B\u00FAum til gagnasafn sem geymir massafall tv\u00EDkostadreifingar me\u00F0 stika n og p.
         tvikosta_massafall &lt;- data.frame(
           x_gildi = 0:max_gildi,
           y_gildi = dbinom(0:max_gildi, n, p),
           audkenni=&quot;Massafall tv\u00EDkostadreifingar&quot;
         )
         #Sameinum gagnas\u00F6fnin
         sameinud_gogn &lt;- rbind(hlutfallstidni, tvikosta_massafall)
         ggplot(sameinud_gogn,aes(x=x_gildi,y=y_gildi,fill=audkenni)) + 
           #Notum geom_bar til a\u00F0 teikna st\u00F6plarit.
           geom_bar(stat = &quot;identity&quot;, position = &quot;dodge&quot;, alpha = 0.8) + 
           labs(title = paste(&quot;Ni\u00F0urst\u00F6\u00F0ur fyrir p =&quot;,p,&quot;og N =&quot;,N), caption = paste(&quot;Samanbur\u00F0ur \u00E1 hermdri hlutfallst\u00ED\u00F0ni fyrir tv\u00EDkostast\u00E6r\u00F0 me\u00F0 stika n =&quot;,n,&quot;og p =&quot;,p,&quot;\nog massafalli tv\u00EDkostadreifingar me\u00F0 stika n =&quot;,n,&quot;og p =&quot;,p), x = &quot;Gildi slembist\u00E6r\u00F0arinnar&quot;, y =&quot;&quot;) +
           scale_fill_manual(name=&quot;&quot;, values = c(&quot;Hermd hlutfallst\u00ED\u00F0ni&quot; = &#39;steelblue3&#39;, &quot;Massafall tv\u00EDkostadreifingar&quot; = &#39;brown3&#39;)) + 
         theme(plot.caption=element_text(size=11, hjust=0, face=&quot;italic&quot;, color=&quot;black&quot;))
       }
     </code>
     <code data-type="sample-code">
       # Velji\u00F0 stika tv\u00EDkostadreifingarinnar og keyri\u00F0 hermunina.
       N &lt;- 10000
       n &lt;- 10
       p &lt;- 0.35
       gildi &lt;- tvikostastaerd_hermun(N, n, p)
       teikna_tvikostastaerd(gildi, n, p)
     </code>
   </div>

Hermun á veldsstærð
~~~~~~~~~~~~~~~~~~~

Hermum næst slembistærð sem hefur veldisdreifingu með stika :math:`\lambda`. Hún er samfelld slembistærð með þéttleikann

.. math::
   :nowrap:

   \[
   \begin{aligned}
    f(x) = \begin{cases} \lambda e^{-\lambda x}, & x \geq 0, \\ 0,& x<0. \end{cases}
   \end{aligned}
   \]

.. container:: center

   .. figure:: images/veldisstaerd_thettleiki_unnid.svg
      :width: 207.02pt
      :align: center

Eins og gildir fyrir Bernoulli- og tvíkostastærðir er hægt að herma veldisstærð með því að velja fyrst tölu af handahófi milli 0 og 1. Nánar tiltekið, ef :math:`U` hefur jafna dreifingu á :math:`(0,1)`, þá er tiltölulega einfalt að sýna að

.. math:: X := -\ln(U)/\lambda

hefur veldisdreifingu með stika :math:`\lambda`. Hvernig er hægt að komast að því hvort svona fullyrðing sé rétt? Ein leið er að sanna það stærðfræðilega, sem þið gerið í skiladæmunum. En hér er hermun líka fljótleg og gagnleg leið til að kanna hvort fullyrðingin sé rétt. Förum í R til að herma.

.. rubric:: Hermun á veldisstærð

.. code-block:: r

   #Fall sem hermir veldisstærð N sinnum.
   #lambda er stiki veldisstaerdarinnar.
   veldisstaerd_hermun <- function(N,lambda){
     #results_vec er vigur sem geymir hermdu gildin.
     results_vec <- c(1:N)
     for(j in 1:N){
       #Veljum tölu u af handahófi milli 0 og 1.
       u <- runif(1, 0, 1)
       #Búum til veldisstærð með stika p með því að nota gildið á u.
       #Athugið að log gefur náttúrulega logrann í R.
       results_vec[j] <- -log(u)/lambda
       }
     #Skilum vigrinum með hermdu gildunum.
     return(results_vec)  
   }

Þar sem við erum núna að vinna með samfellda slembistærð höfum við ekki áhuga á hlutfallstíðni einstakra gilda heldur höfum við áhuga á þéttleika gildanna. Við notum ``geom_density`` í R til að áætla þéttleika gildanna sem hermunin gefur og berum hann síðan saman við þéttleika veldisdreifingarinnar með stika :math:`lambda`.

.. rubric:: Samanburður á hermdri hlutfallstíðni og þéttleika veldisdreifingar

.. code-block:: r

   #Notum ggplot2 til að teikna.
   library(ggplot2)
   #Þessi valkostur sýnir tölur eins og 10^5 sem 100000.
   options(scipen=999)
   #Fall sem tekur inn hermd gildi og teiknar mynd sem ber saman hermdan þéttleika
   #við þéttleika veldisdreifingar með stika lambda.
   teikna_veldisstaerd <- function(results_vec,lambda){
     #Teiknum mynd.
     ggplot(data.frame(results_vec), aes(x = results_vec)) + 
     #geom_density tekur gildin í results_vec og notar þau til að reikna þéttleika.
     #bounds = c(0,Inf) segir geom_density að slembistærðin tekur aðeins jákvæð rauntölugildi.
     geom_density(linewidth = 2, bounds = c(0,Inf), aes(color = 'Hermdur þéttleiki')) + 
     #Notum stat_function til að teikna þéttleika veldisdreifingarinnar með stika lambda.
     #fun = dexp segir stat_function að nota þéttleika veldisdreifingarinnar.
     #args = list(rate = 2) segir stat_function að stiki dreifingarinnar sé lambda.
     stat_function(linewidth = 3, aes(color = 'Þéttleiki veldisdreifingar'),fun = dexp, args = list(rate = lambda), linetype="dotted") +
     labs(title = paste("Niðurstöður fyrir lambda =",lambda,"og N =",N), caption = paste("Samanburður á hermdum þéttleika fyrir -log(U)/lambda og\nþéttleika veldisdreifingar með stika lambda = ",lambda), x = "Gildi slembistærðarinnar", y ="") +
     scale_color_manual(name='', values = c('Hermdur þéttleiki' = 'steelblue3', 'Þéttleiki veldisdreifingar' = 'black')) + 
     theme(plot.caption=element_text(size=11, hjust=0, face="italic", color="black"))
   }

.. rubric:: Gagnvirkur R-leikvöllur

.. raw:: html

   <div data-datacamp-exercise data-lang="r" data-height="600">
     <code data-type="pre-exercise-code">
       try(Sys.setlocale(&#39;LC_CTYPE&#39;, &#39;C.UTF-8&#39;), silent=TRUE)

       #Fall sem hermir veldisst\u00E6r\u00F0 N sinnum.
       #lambda er stiki veldisstaerdarinnar.
       veldisstaerd_hermun &lt;- function(N,lambda){
         #results_vec er vigur sem geymir hermdu gildin.
         results_vec &lt;- c(1:N)
         for(j in 1:N){
           #Veljum t\u00F6lu u af handah\u00F3fi milli 0 og 1.
           u &lt;- runif(1, 0, 1)
           #B\u00FAum til veldisst\u00E6r\u00F0 me\u00F0 stika p me\u00F0 \u00FEv\u00ED a\u00F0 nota gildi\u00F0 \u00E1 u.
           #Athugi\u00F0 a\u00F0 log gefur n\u00E1tt\u00FArulega logrann \u00ED R.
           results_vec[j] &lt;- -log(u)/lambda
           }
         #Skilum vigrinum me\u00F0 hermdu gildunum.
         return(results_vec)  
       }

       #Notum ggplot2 til a\u00F0 teikna.
       library(ggplot2)
       #\u00DEessi valkostur s\u00FDnir t\u00F6lur eins og 10^5 sem 100000.
       options(scipen=999)
       #Fall sem tekur inn hermd gildi og teiknar mynd sem ber saman hermdan \u00FE\u00E9ttleika
       #vi\u00F0 \u00FE\u00E9ttleika veldisdreifingar me\u00F0 stika lambda.
       teikna_veldisstaerd &lt;- function(results_vec,lambda){
         #Teiknum mynd.
         ggplot(data.frame(results_vec), aes(x = results_vec)) + 
         #geom_density tekur gildin \u00ED results_vec og notar \u00FEau til a\u00F0 reikna \u00FE\u00E9ttleika.
         #bounds = c(0,Inf) segir geom_density a\u00F0 slembist\u00E6r\u00F0in tekur a\u00F0eins j\u00E1kv\u00E6\u00F0 raunt\u00F6lugildi.
         geom_density(linewidth = 2, bounds = c(0,Inf), aes(color = &#39;Hermdur \u00FE\u00E9ttleiki&#39;)) + 
         #Notum stat_function til a\u00F0 teikna \u00FE\u00E9ttleika veldisdreifingarinnar me\u00F0 stika lambda.
         #fun = dexp segir stat_function a\u00F0 nota \u00FE\u00E9ttleika veldisdreifingarinnar.
         #args = list(rate = 2) segir stat_function a\u00F0 stiki dreifingarinnar s\u00E9 lambda.
         stat_function(linewidth = 3, aes(color = &#39;\u00DE\u00E9ttleiki veldisdreifingar&#39;),fun = dexp, args = list(rate = lambda), linetype=&quot;dotted&quot;) +
         labs(title = paste(&quot;Ni\u00F0urst\u00F6\u00F0ur fyrir lambda =&quot;,lambda,&quot;og N =&quot;,N), caption = paste(&quot;Samanbur\u00F0ur \u00E1 hermdum \u00FE\u00E9ttleika fyrir -log(U)/lambda og\n\u00FE\u00E9ttleika veldisdreifingar me\u00F0 stika lambda = &quot;,lambda), x = &quot;Gildi slembist\u00E6r\u00F0arinnar&quot;, y =&quot;&quot;) +
         scale_color_manual(name=&#39;&#39;, values = c(&#39;Hermdur \u00FE\u00E9ttleiki&#39; = &#39;steelblue3&#39;, &#39;\u00DE\u00E9ttleiki veldisdreifingar&#39; = &#39;black&#39;)) + 
         theme(plot.caption=element_text(size=11, hjust=0, face=&quot;italic&quot;, color=&quot;black&quot;))
       }
     </code>
     <code data-type="sample-code">
       # Velji\u00F0 lambda og keyri\u00F0 hermunina.
       N &lt;- 10000
       lambda &lt;- 2
       gildi &lt;- veldisstaerd_hermun(N, lambda)
       teikna_veldisstaerd(gildi, lambda)
     </code>
   </div>

Í hermunarverkefninu sjáum við að Poisson-dreifinguna er líka hægt að herma með því að velja tölur af handahófi milli 0 og 1. Nánar tiltekið: Ef við látum :math:`U_1,U_2,\ldots` vera óháðar slembistærðir með jafna dreifingu á bilinu :math:`(0,1)` og látum :math:`\lambda > 0`, þá hefur slembistærðin

.. math::
   :nowrap:

   \[
   \begin{aligned}
    X := \max\left\{n \geq 0: \prod_{i=1}^{n} U_i \geq e^{-\lambda}\right\}
   \end{aligned}
   \]

Poisson-dreifingu með stika :math:`\lambda`. Þetta er annað dæmi um gagnsemi hermunar: Það er alls ekki augljóst fyrirfram að þessi stærð hafi Poisson-dreifingu, en hermun er fljótleg leið til að staðfesta það.

Innbyggðar skipanir í R
~~~~~~~~~~~~~~~~~~~~~~~

Hingað til höfum við búið til okkar eigin hermunarkóða með því að velja tölur af handahófi milli 0 og 1 og nota þær til að herma slembistærðir t.d. með Bernoulli-, tvíkosta- og veldisdreifinguna. Hins vegar eru líka til innbyggðar skipanir í R sem herma beint slembistærðir með þekktar líkindadreifingar. Förum í R og tökum dæmi um tvíkosta- og veldisdreifinguna.

.. container:: center

   ========================== ===========================
   Dreifing                   Skipun til að herma N gildi
   ========================== ===========================
   :math:`{\rm Ber}(p)`       ``rbinom(N,1,p)``

   :math:`{\rm Bin}(n,p)`     ``rbinom(N,n,p)``

   :math:`{\rm Poi}(\lambda)` ``rpois(N,lambda)``

   :math:`{\rm Unf}[a,b]`     
                              ``runif(N,a,b)``

   :math:`{\rm Exp}(\lambda)` ``rexp(N,lambda)``

   :math:`N(\mu,\sigma)`      ``rnorm(N,mu,sigma)``
   ========================== ===========================

Hermun á Poisson-ferlum
~~~~~~~~~~~~~~~~~~~~~~~

Í Lík&töl settum við fram líkan fyrir komur á bráðamóttökuna yfir eina klukkustund. Hugmyndin var að búta eina klukkustund niður í stutt hlutbil af lengdinni :math:`1/n`, þannig að í mesta lagi ein koma verði á hverju hlutbili, og gera ráð fyrir að líkurnar á komu væru :math:`p = \lambda/n` fyrir hvert og eitt hlutbil, þar sem :math:`\lambda>0` var einhver jákvæð rauntala. Við getum hugsað stikann :math:`\lambda` sem meðalfjöldi koma sem verður yfir eina klukkustund.

.. container:: center

   .. figure:: images/poisson_dreifing_2.svg
      :width: 251.44pt
      :align: center

.. container:: center

   .. figure:: images/poisson_dreifing_3.svg
      :width: 294.2pt
      :align: center

Fjölda koma er hægt að lýsa með tvíkostastærð þar sem fjöldi tilrauna er :math:`n` og líkur á að tilraunin heppnist eru :math:`p = \lambda/n` í hvert skipti. Í skiladæmunum sönnuðuð þið að þegar :math:`n \to \infty` má lýsa fjölda koma með Poisson-dreifingu.

.. container:: center

   .. figure:: images/poisson_dreifing_4.svg
      :width: 367.75pt
      :align: center

Við minntumst líka á í Lík&töl að tíminn sem líður milli koma hefur veldisdreifingu með stika :math:`\lambda` þegar :math:`n` er stórt. Ef við keyrum þetta komulíkan endalaust og látum :math:`N(t)` vera fjölda koma yfir tímabilið :math:`[0,t]`, þá fæst svokallað **slembiferli** sem kallast Poisson-ferli með stika :math:`\lambda`.

Formlega má skilgreina Poisson-ferli með stika :math:`\lambda>0` þannig að tímarnir sem líða milli atburða séu óháðar veldisstærðir með stika :math:`\lambda`. Ef ferlið hefst á tíma :math:`0` er tíminn sem líður fram að fyrsta atburði :math:`S_1 = X_1`, tíminn sem líður fram að öðrum atburði er :math:`S_2 = X_1+X_2`, og svo koll af kolli, þar sem :math:`X_1,X_2,\ldots` eru óháðar veldisstærðir með stika :math:`\lambda`.

.. container:: center

   .. figure:: images/poisson_ferli_hermun.svg
      :width: 301.98pt
      :align: center

Í Poisson-ferli táknum við atburðatímana með :math:`S_1,S_2,\ldots` þar sem :math:`S_n = X_1+X_2+\cdots+X_n` fyrir :math:`n \geq 1`. Látum :math:`t \geq 0` og látum :math:`N(t)` tákna fjölda atburða sem gerast fram að tíma :math:`t`. Setjum :math:`S_0 := 0`. Þá má lýsa :math:`N(t)` svona:

.. math::
   :nowrap:

   \[
   \begin{aligned}
    N(t) &= \max\{n \geq 0: S_n \leq t\}.
   \end{aligned}
   \]

Á myndinni að ofan er :math:`N(t)=4`. Við ætlum núna að herma Poisson-ferli og það verður síðan skoðað frekar í hermunarverkefninu. Poisson-ferli með stika :math:`\lambda` má herma svona yfir tímabilið :math:`[0,T]`:

   #. Setjum :math:`t=0` og :math:`n=0`. Breytan :math:`t` heldur utan um tímann sem hefur liðið og breytan :math:`n` heldur utan um fjölda atburða.

   #. Hermum tímann :math:`x` sem líður fram að næsta atburði, sem hefur veldisdreifingu með stika :math:`\lambda`.

   #. Setjum :math:`t \leftarrow t+x` til að uppfæra tímann sem hefur liðið.

   #. Ef :math:`t \leq T` setjum við :math:`n \leftarrow n+1`. Annars erum við komin út fyrir tímabilið :math:`[0,T]` og við hættum hermuninni.

   #. Endurtökum skref 2–4 eins oft og þarf.

   #. Þegar hermuninni er lokið er :math:`n` fjöldi atburða sem gerðist á tímabilinu :math:`[0,T]`.

Hægt er að sýna að í Poisson-ferli með stika :math:`\lambda` hefur fjöldi atburða sem gerist á tímabilinu :math:`[0,T]` Poisson-dreifingu með stika :math:`\lambda T`. Staðfestum þetta með því að herma Poisson-ferli.

.. rubric:: Hermun á Poisson-ferli

.. code-block:: r

   #Fall sem hermir Poisson-ferli N sinnum yfir tímabilið [0,T].
   #lambda er stiki Poisson-ferlisins.
   poisson_ferli_hermun <- function(N,lambda,T){
     #results_vec er vigur sem geymir hermdu gildin.
     results_vec <- c(1:N)
     #Hermum Poisson-ferli N sinnum yfir tímabilið [0,T].
     for (j in 1:N){
       #Byrjum á að núllstilla tímann (t) og fjölda atburða (n)
       t <- 0
       n <- 0
       #Breytan exit er notuð til að hætta hermuninni þegar það er viðeigandi.
       exit = 0
       while(exit == 0){
         #Hermum tímann sem líður fram að næsta atburði.
         x <- rexp(1,lambda)
         #Uppfærum tímann sem hefur liðið.
         t <- t + x
         #Athugum hvort við erum komin út fyrir endapunkt tímabilsins. 
         #Ef svo er hættum við, annars hækkum við fjölda atburða
         #á tímabilinu um einn og höldum áfram.
         if (t > T ){
           exit <- 1
         }
         else{
           n <- n+1 
         }
       }
       #Vistum hermdan fjölda atburða á tímabilinu [0,T].
       results_vec[j] <- n
     }

     #Skilum vigrinum með hermdu gildunum.
     return(results_vec)
   }

Búum síðan til fall sem tekur inn hermd gildi fyrir fjölda atburða á tímabilinu [0,T] og teiknar samanburðarmynd sem ber saman hlutfallstíðnir gildanna sem hermunin gefur og massafall Poisson-dreifingar með stika :math:`\lambda T`. Athugið að kóðinn er mjög svipaður og kóðarnir sem við notuðum að ofan fyrir Bernoulli- og tvíkostastærðirnar.

.. rubric:: Samanburður á hermdri hlutfallstíðni og massafalli Poisson-dreifingar

.. code-block:: r

   #Notum ggplot2 til að teikna.
   library(ggplot2)
   #Þessi valkostur sýnir tölur eins og 10^5 sem 100000.
   options(scipen=999)
   #Fall sem tekur inn hermd gildi og teiknar mynd sem ber saman hlutfallstíðni
   #gilda í hermuninni við massafall Poisson-dreifingar með stika lambda*T.
   teikna_poisson_ferli <- function(results_vec,lambda,T){
     #Finnum stærsta gildið sem kom út úr hermuninni.
     max_gildi <- max(results_vec)
     #Reiknum hlutfallstíðni hermdu gildanna.
     tidnirit <- hist(results_vec, breaks = (-1:max_gildi)+0.5, plot = FALSE)
     #Búum til gagnasafn sem geymir gögnin fyrir hermdu hlutfallstíðnirnar.
     hlutfallstidni <- data.frame(
       x_gildi = 0:max_gildi,
       #tidnirit$density gefur hlutfallstíðnirnar
       y_gildi = tidnirit$density, 
       audkenni="Hermd hlutfallstíðni"
     )
     #Búum til gagnasafn sem geymir massafall Poisson-dreifingar með stika lambda*T.
     poisson_massafall <- data.frame(
       x_gildi = 0:max_gildi,
       y_gildi = dpois(0:max_gildi, lambda*T),
       audkenni="Massafall Poisson-dreifingar"
     )
     #Sameinum gagnasöfnin
     sameinud_gogn <- rbind(hlutfallstidni, poisson_massafall)
     ggplot(sameinud_gogn,aes(x=x_gildi,y=y_gildi,fill=audkenni)) + 
       #Teiknum stöplarit með geombar.
       geom_bar(stat = "identity", position = "dodge", alpha = 0.8) + 
       labs(title=paste("Niðurstöður fyrir lambda =",lambda,", T =",T," og N =",N), caption = paste("Samanburður á hermdri hlutfallstíðni fyrir fjölda atburða\nfram að tíma T =",T,"í Poisson-ferli með stika lambda =",lambda,"\nog massafalli Poisson-dreifingar með stika lambda*T =",lambda*T), x = "Gildi slembistærðarinnar", y ="") +
       scale_fill_manual(name="",values = c("Hermd hlutfallstíðni" = 'steelblue3', "Massafall Poisson-dreifingar" = 'brown3')) + 
       theme(plot.caption=element_text(size=11, hjust=0, face="italic", color="black"))
   }

.. rubric:: Gagnvirkur R-leikvöllur

.. raw:: html

   <div data-datacamp-exercise data-lang="r" data-height="600">
     <code data-type="pre-exercise-code">
       try(Sys.setlocale(&#39;LC_CTYPE&#39;, &#39;C.UTF-8&#39;), silent=TRUE)

       #Fall sem hermir Poisson-ferli N sinnum yfir t\u00EDmabili\u00F0 [0,T].
       #lambda er stiki Poisson-ferlisins.
       poisson_ferli_hermun &lt;- function(N,lambda,T){
         #results_vec er vigur sem geymir hermdu gildin.
         results_vec &lt;- c(1:N)
         #Hermum Poisson-ferli N sinnum yfir t\u00EDmabili\u00F0 [0,T].
         for (j in 1:N){
           #Byrjum \u00E1 a\u00F0 n\u00FAllstilla t\u00EDmann (t) og fj\u00F6lda atbur\u00F0a (n)
           t &lt;- 0
           n &lt;- 0
           #Breytan exit er notu\u00F0 til a\u00F0 h\u00E6tta hermuninni \u00FEegar \u00FEa\u00F0 er vi\u00F0eigandi.
           exit = 0
           while(exit == 0){
             #Hermum t\u00EDmann sem l\u00ED\u00F0ur fram a\u00F0 n\u00E6sta atbur\u00F0i.
             x &lt;- rexp(1,lambda)
             #Uppf\u00E6rum t\u00EDmann sem hefur li\u00F0i\u00F0.
             t &lt;- t + x
             #Athugum hvort vi\u00F0 erum komin \u00FAt fyrir endapunkt t\u00EDmabilsins. 
             #Ef svo er h\u00E6ttum vi\u00F0, annars h\u00E6kkum vi\u00F0 fj\u00F6lda atbur\u00F0a
             #\u00E1 t\u00EDmabilinu um einn og h\u00F6ldum \u00E1fram.
             if (t &gt; T ){
               exit &lt;- 1
             }
             else{
               n &lt;- n+1 
             }
           }
           #Vistum hermdan fj\u00F6lda atbur\u00F0a \u00E1 t\u00EDmabilinu [0,T].
           results_vec[j] &lt;- n
         }

         #Skilum vigrinum me\u00F0 hermdu gildunum.
         return(results_vec)
       }

       #Notum ggplot2 til a\u00F0 teikna.
       library(ggplot2)
       #\u00DEessi valkostur s\u00FDnir t\u00F6lur eins og 10^5 sem 100000.
       options(scipen=999)
       #Fall sem tekur inn hermd gildi og teiknar mynd sem ber saman hlutfallst\u00ED\u00F0ni
       #gilda \u00ED hermuninni vi\u00F0 massafall Poisson-dreifingar me\u00F0 stika lambda*T.
       teikna_poisson_ferli &lt;- function(results_vec,lambda,T){
         #Finnum st\u00E6rsta gildi\u00F0 sem kom \u00FAt \u00FAr hermuninni.
         max_gildi &lt;- max(results_vec)
         #Reiknum hlutfallst\u00ED\u00F0ni hermdu gildanna.
         tidnirit &lt;- hist(results_vec, breaks = (-1:max_gildi)+0.5, plot = FALSE)
         #B\u00FAum til gagnasafn sem geymir g\u00F6gnin fyrir hermdu hlutfallst\u00ED\u00F0nirnar.
         hlutfallstidni &lt;- data.frame(
           x_gildi = 0:max_gildi,
           #tidnirit$density gefur hlutfallst\u00ED\u00F0nirnar
           y_gildi = tidnirit$density, 
           audkenni=&quot;Hermd hlutfallst\u00ED\u00F0ni&quot;
         )
         #B\u00FAum til gagnasafn sem geymir massafall Poisson-dreifingar me\u00F0 stika lambda*T.
         poisson_massafall &lt;- data.frame(
           x_gildi = 0:max_gildi,
           y_gildi = dpois(0:max_gildi, lambda*T),
           audkenni=&quot;Massafall Poisson-dreifingar&quot;
         )
         #Sameinum gagnas\u00F6fnin
         sameinud_gogn &lt;- rbind(hlutfallstidni, poisson_massafall)
         ggplot(sameinud_gogn,aes(x=x_gildi,y=y_gildi,fill=audkenni)) + 
           #Teiknum st\u00F6plarit me\u00F0 geombar.
           geom_bar(stat = &quot;identity&quot;, position = &quot;dodge&quot;, alpha = 0.8) + 
           labs(title=paste(&quot;Ni\u00F0urst\u00F6\u00F0ur fyrir lambda =&quot;,lambda,&quot;, T =&quot;,T,&quot; og N =&quot;,N), caption = paste(&quot;Samanbur\u00F0ur \u00E1 hermdri hlutfallst\u00ED\u00F0ni fyrir fj\u00F6lda atbur\u00F0a\nfram a\u00F0 t\u00EDma T =&quot;,T,&quot;\u00ED Poisson-ferli me\u00F0 stika lambda =&quot;,lambda,&quot;\nog massafalli Poisson-dreifingar me\u00F0 stika lambda*T =&quot;,lambda*T), x = &quot;Gildi slembist\u00E6r\u00F0arinnar&quot;, y =&quot;&quot;) +
           scale_fill_manual(name=&quot;&quot;,values = c(&quot;Hermd hlutfallst\u00ED\u00F0ni&quot; = &#39;steelblue3&#39;, &quot;Massafall Poisson-dreifingar&quot; = &#39;brown3&#39;)) + 
           theme(plot.caption=element_text(size=11, hjust=0, face=&quot;italic&quot;, color=&quot;black&quot;))
       }
     </code>
     <code data-type="sample-code">
       # Velji\u00F0 lambda, T og fj\u00F6lda hermana.
       N &lt;- 10000
       lambda &lt;- 3
       T &lt;- 5
       gildi &lt;- poisson_ferli_hermun(N, lambda, T)
       teikna_poisson_ferli(gildi, lambda, T)
     </code>
   </div>

Til gamans: Að reikna heildi með hermun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Segjum að við viljum reikna heildið

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \int_0^1 g(x) dx \qquad (\ast)
   \end{aligned}
   \]

fyrir eitthvert fall :math:`g: (0,1) \to \mathbb{R}`. Veljum óháðar tölur :math:`U_1,U_2,\ldots` af handahófi milli 0 og 1 og skilgreinum slembistærðirnar

.. math:: X_1 := g(U_1), \; X_2 := g(U_2), \; X_3 := g(U_3), \;\text{o.s.frv.}

Athugið að :math:`X_1,X_2,X_3,\ldots` eru óháðar slembistærðir sem hafa allar sömu dreifingu.

Setjum

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \bar{X}_n := \frac1n \sum_{i=1}^n X_i = \frac1n \sum_{i=1}^n g(U_i).
   \end{aligned}
   \]

Samkvæmt lögmáli mikils fjölda gildir að :math:`\bar{X}_n` nálgast :math:`\mathbb{E}[X_1] = \mathbb{E}[g(U_1)]` eftir því sem :math:`n` stækkar. En nú gildir skv. lögmáli ómeðvitaða tölfræðingsins að

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{E}[g(U_1)] &= \int_{-\infty}^\infty g(x) f(x) dx = \int_0^1 g(x) dx.
   \end{aligned}
   \]

Við getum þess vegna nálgað heildið í :math:`(\ast)` með því að velja tölur af handahófi milli 0 og 1, reikna fallgildi :math:`g` fyrir hverja og eina tölu, og taka meðaltal.

Segjum að við viljum reikna tvöfalda heildið

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \int_0^1 \int_0^1 g(x,y) dx dy \quad (\ast)
   \end{aligned}
   \]

fyrir eitthvert fall :math:`g: (0,1)^2 \to \mathbb{R}`. Veljum óháða punkta

.. math:: (U_1,V_1),(U_2,V_2),(U_3,V_3),\ldots

af handahófi úr einingakassanum og skilgreinum slembistærðirnar

.. math:: X_1 := g(U_1,V_1), \; X_2 := g(U_2,V_2), \; X_3 := g(U_3,V_3), \;\text{o.s.frv.}

Athugið að :math:`X_1,X_2,X_3,\ldots` eru óháðar slembistærðir sem hafa allar sömu dreifingu.

Setjum

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \bar{X}_n := \frac1n \sum_{i=1}^n X_i = \frac1n \sum_{i=1}^n g(U_i,V_i).
   \end{aligned}
   \]

Samkvæmt lögmáli mikils fjölda gildir að :math:`\bar{X}_n` nálgast :math:`\mathbb{E}[X_1] = \mathbb{E}[g(U_1,V_1)]` eftir því sem :math:`n` stækkar. En nú gildir skv. lögmáli ómeðvitaða tölfræðingsins að

.. math::
   :nowrap:

   \[
   \begin{aligned}
    \mathbb{E}[g(U_1,V_1)] &= \int_{-\infty}^\infty \int_{-\infty}^{\infty} g(x,y) f(x,y) dx dy \\ &= \int_0^1 \int_0^1 g(x,y) dx dy.
   \end{aligned}
   \]

Við getum þess vegna reiknað tvöfalda heildið í :math:`(\ast)` með því að velja punkta af handahófi úr einingakassanum, reikna falligildi :math:`g` í punktunum, og taka meðaltal.

Hermun er ekki endilega fljótlegasta leiðin til að reikna ein- og tvívíð heildi, en hún getur orðið gagnleg þegar reikna þarf yfir tugi eða hundruði vídda, sem kemur t.d. fyrir þegar verið er að greina flókin gagnasöfn.