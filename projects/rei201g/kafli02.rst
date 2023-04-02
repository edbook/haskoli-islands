.. include:: rst-include

.. _línuleg-algebra:             
             
=================
 Línuleg algebra
=================

Línuleg algebra er undirgrein stærðfræði sem fjallar um vigra og fylki, vigurrúm,
línulegar jöfnur og jöfnuhneppi, t.d. :math:`5x + 3y = 13, x - y = 1`, og línuleg
föll (eða línulegar varpanir), t.d. :math:`f(x,y) = 2x + 3y`.
Meðal fleiri grunnhugtaka línulegrar algebru sem hér verða kynnt eru línulega
háð og óháð mengi vigra, grunnar, norm, horn milli vigra og tölfræðileg föll af vigrum.

Þessi kafli byrjar á að rifja upp efni sem fjallað er um í 10. og 11. kafla í
`Fyrirlestrarnótum um Python <https://cs.hi.is/python>`_ m.a. skilgreiningar á
vigrum og fylkjum, innfeldi og margföldun fylkis og vigurs. Nokkrum atriðum er
bætt við fyrri umfjöllun í þessari upprifjun sem er í greinum :numref:`vigrar og
fylki` til :numref:`margföldun fylkis og vigurs` en í grein :numref:`línuleg
föll og innfeldi` og framhaldinu kemur svo alveg nýtt efni.

.. _vigrar-og-fylki:

Vigrar og fylki
---------------

.. _skilgreining_vigurs:

.. admonition:: Skilgreining: Vigur
   :class: regla

   **Vigur** (*vector*) er runa af endanlega mörgum tölum sem notuð er sem ein
   heild og oft gefið nafn sem er lítill bókstafur (t.d. :math:`a`,
   :math:`b`...).

Vigur með tölunum 1, 2 og 4 er ritaður:

   .. math::
      (1,2,4)\,\text{ eða }\,[1,2,4]\,\text{ eða }\,\begin{pmatrix}1\\2\\4\end{pmatrix}.

Fjöldi talna í vigri er kölluð **vídd** (*dimension*, eða *size*) vigursins og
tölurnar í honum eru kallaðar **stök** hans (*elements*) eða **hnit**
(*coordinates*). Stakið í :math:`i`-ta sæti í vigri :math:`a` er táknað
:math:`a_i`. Vigur með :math:`n` stök er oft kallaður :math:`n`-vigur, og
mengi allra :math:`n`-vigra er táknað :math:`\Bbb{R}^n`. Ef :math:`a \in
\Bbb{R}^n` gildir sem sé

.. math::
   a = (a_1, a_2, \ldots, a_n)

.. attention:: Þegar hugtakið **vídd** er notað um tölvufræðilegt fylki (*array*),
   eins og rætt var í grein 10.1.2 í Fyrirlestrarnótum um Python merkir það fjölda vísa
   (*indices*) sem notaðir eru til að vísa í einstök stök (vigrar eru þannig
   einvíð fylki), en þegar hugtakið er notað um vigur (hvort sem er í tölvufræði
   eða stærðfræði) merkir það fjölda staka í honum. Í tölvufræði er reyndar
   algengt að nota **lengd** (*length*) um fjölda staka í lista eða vigri, en af
   því að það er líka notað um rúmfræðilega lengd vigurs höldum við okkur við
   orðið vídd.
   
.. note::
   Í NumPy er fyrsta stak vigurs númerað 0, þannig að um vigur a með n
   stök gildir |br| |sp| ``a = np.array([a[0], a[1], ..., a[n-1]])``

.. admonition:: Skilgreining: Fylki
   :class: regla

   **Fylki** (*matrix*) er tafla með tölum sem notuð er sem ein heild og oft
   gefið nafn sem er stór bókstafur (t.d. :math:`A`, :math:`B`...).

Taflan er ýmist sett innan sviga eða hornklofa:

   .. math::
      A = \begin{pmatrix}1 & 2 & 3\\6 & 7 & 8\end{pmatrix} =
      \begin{bmatrix}1 & 2 & 3\\6 & 7 & 8\end{bmatrix}\qquad
      B = \begin{pmatrix}5 & -1 \\ -1 & 6\end{pmatrix}
   
Fylki hafa tiltekinn fjölda af **línum** (eða **röðum**) og (**dálkum**) (*rows* og
*columns*) og fylki með :math:`m` línum og :math:`n` dálkum er sagt hafa **stærð**
(*size*) :math:`m \times n`: Fylkið :math:`A` að ofan er :math:`2 \times 3`
fylki (lesið 2 sinnum 3 fylki, eða á ensku *2 by 3* matrix). Fylki
með jafnmargar línur og dálka (t.d. fylkið :math:`B`) er kallað **ferningsfylki**.

Einstakar tölur í fylki eru kölluð **stök** og staðsetning þeirra er **sæti**
(*position*), þannig að talan 8 í fylkinu :math:`A` er sögð vera í sæti
:math:`(2,3)` (línan kemur á undan dálkinum). Stak í línu :math:`i` og dálki
:math:`j` í fylki :math:`A` er táknað :math:`a_{ij}`; fyrir :math:`A`-ið að ofan
gildir :math:`a_{23} = 8`.

.. note::
   Um fylki í NumPy var fjallað í 11. kafla í Fyrirlestrarnótum um Python. Þar
   var meðal annars útskýrt hvernig hægt er að búa til fylki og ná í einstök
   stök. Fylkið A að ofan væri búið til með :code:`A =
   np.array([[1,2,3],[6,7,8]])` og stakið :math:`a_{23}` fengist með
   :code:`A[1,2]` (munum að Python byrjar tölusetningu í 0).

.. admonition:: Sýnidæmi: Birgðastaða og blóðþrýstingur
   :class: synidaemi

   (1) Birgðastöðu af vörum mætti tákna með fylki, t.d. gætum við látið
       :math:`b_{ij}` tákna birgðir af vöru :math:`i` á degi :math:`j`; þá væri
       :math:`B` birgðafylki.
         
   (2) Blóðþrýsting :math:`n` einstaklinga mætti tákna með :math:`n \times 2`
       fylki :math:`P`, þar sem fyrri dálkurinn gefur slagþrýsting
       (*systolic*) og sá seinni aðfallsþrýsing (*diastolic*).

.. admonition:: Æfing: Blóðþrýstingur
   :class: aefing

   Blóðþrýstingur þriggja einstaklinga mældist 120/80, 140/90 og 105/65.
           
   1. Hvert er blóðþrýstingsfylkið :math:`P`?
   2. Hver er stærð þess?
   3. Hvað er :math:`p_{22}`?
   4. Í hvaða sæti er 80?

Vigra er hægt að leggja saman og draga hvern frá öðrum og einnig má margfalda
vigur með tölu. Þetta er gert með því að beita tilsvarandi aðgerðum á einstök
stök. 

.. admonition:: Skilgreining: Einfaldar viguraðgerðir
   :class: regla

   Ef :math:`x` og :math:`y` eru vigrar og :math:`c` er tala þá gildir:
   
   .. math::
      u &= x + y\text{ er vigur með }u_i = x_i + y_i\\
      v &= x - y\text{ er vigur með }v_i = x_i - y_i\\
      w &= cx\text{ er vigur með }w_i = cx_i\text{ í }i\text{-ta sæti}

Á sama hátt má leggja saman og draga frá fylki og margfalda þau með tölu:

.. admonition:: Skilgreining: Einfaldar fylkjaaðgerðir
   :class: regla

   Ef :math:`A` og :math:`B` eru fylki og :math:`c` er tala þá gildir:

   .. math::
      U &= A + B\text{ er fylki með }u_{ij} = a_{ij} + b_{ij}\\
      V &= A - B\text{ er fylki með }v_{ij} = a_{ij} - b_{ij}\\
      W &= cA\text{ er fylki með }w_{ij} = ca_{ij}

.. _vigur-og-fylkjaaðgerðir:

Um samlagningu og frádrátt vigra og fylkja gilda víxlregla og tengiregla
einnig gildir dreifiregla um margföldun með tölu:

.. admonition:: Reglur um vigur- og fylkjaaðgerðir
   :class: regla

   Ef :math:`x`, :math:`y` og :math:`z` eru vigrar, :math:`A`, :math:`B` og
   :math:`C` eru fylki og :math:`\alpha` er tala þá gildir:

   .. math::
      x + y &= y + x\\
      A + B &= B + A\\
      \alpha(x + y) &= \alpha x + \alpha y\\
      \alpha(A + B) &= \alpha A + \alpha B\\
      x + (y + z) &= (x + y) + z\\
      A + (B + C) &= (A + B) + C\\

   og í stað :math:`+` má setja :math:`-` í dreifireglunum:

   .. math::
      \alpha(x - y) &= \alpha x - \alpha y\\
      \alpha(A - B) &= \alpha A - \alpha B\\

.. _innfeldi:

Ýmis vigur- og fylkjahugtök
---------------------------
Eitt af grundvallarhugtökum í línulegri algebru er *innfeldi* eða
*skalarmargfeldi* (*dot product*, *scalar product*, *inner product*). Þetta
hugtak kemur víða við sögu, og er m.a. undirstaða í fylkjamargföldun og fræðum
um línulegar varpanir og vigurrúm. Innfeldi felur í sér að tveir vigrar eru
margfaldaðir saman til að fá út tölu.

.. rubric:: Innfeldi

.. admonition:: Skilgreining: Innfeldi
   :class: regla

   **Innfeldi** tveggja :math:`n`-vigra :math:`x` og :math:`y` er skilgreint sem

   .. math::
      x \cdot y = x_1 y_1 + \ldots + x_n y_n = \sum_{i=1}^n x_i y_i

Ef :math:`x = (3,2)` og :math:`y = (4,5)` fæst sem sé :math:`x \cdot y = 3 \cdot
4 + 2 \cdot 5 = 22`.

Hér er dæmi um reglu sem sýnir hvernig nýta má innfeldi.

.. admonition:: Regla: Innfeldi og horn milli rúmvigra
   :class: regla

   Ef :math:`x` og :math:`y` eru 2 eða 3-víðir rúmvigrar þá gildir:

    .. math::
       &x \cdot y = 0 \text{ þá og því aðeins að } x \text{ sé hornréttur á } y\\
       &x \cdot y > 0 \text{ þá og því aðeins að hornið á milli } x \text{ og } y
       \text{ sé hvasst }

.. figure:: myndir/innfeldi.png
   :figwidth: 9cm
   :align: center
                    
   Innfeldi vigra og horn milli þeirra
      
.. admonition:: Sýnidæmi: Einkunnir og söluverð
   :class: synidaemi

   (1) Lát

       .. math::
          v_i &= \text{vægi námskeiðs } i = \frac{\text{ECTS-einingar
          námskeiðs } i}{\text{heildareiningar}} \\
          e_i &= \text{einkunn í námskeiði } i
          
       Þá er vegin meðaleinkunn allra námskeiða gefin með innfeldinu :math:`v
       \cdot e`
       
   (2) Lát
       
       .. math::          
          s_i &= \text{söluverð á einingu af vöru } i\\ 
          m_i &= \text{selt magn af vöru } i

       Þá er heildarsöluverð gefið með innfeldinu :math:`s \cdot m`

.. admonition:: Æfing: Meðaleinkunn
   :class: aefing

   Einkunnir Jóns haustið 2019 voru sem hér segir

   .. list-table::
      :widths: auto
      :align: center
         
      * - Námskeið
        - Ein.
        - Einkunn          
                   
      * - Hagnýt stærðfræðigreining
        - 8
        - 6.5

      * - Tölvunarfræði 1
        - 6
        - 9.0

      * - Stærðfræðimynstur
        - 8
        - 7.0

      * - Vefforritun
        - 8
        - 8.0

   1. Ákvarðið vægisvigur :math:`v` og einkunnarvigur :math:`e`
   2. Notið innfeldi til að finna meðaleinkunn Jóns
          
Um innfeldi gilda víxlregla, tengiregla fyrir margfeldi með tölu og dreifiregla:

.. admonition:: Reglur um innfeldi
   :class: regla

   .. math::
      x\cdot y &= y\cdot x \\
      a(x\cdot y) &= ax\cdot y \\
      x\cdot(y \pm z) &= x\cdot y \pm x\cdot z

   hér eru :math:`x`, :math:`y` og :math:`z` vigrar og :math:`a` er tala.

.. note::
   
   Um reikning innfeldis með NumPy var talað 11. kafla í Fyrirlestrarnótum um Python.
   og útskýrt að það er hægt að reikna með virkjanum :code:`@`, fallinu :code:`np.dot` eða
   aðferðinni :code:`dot`.
       
.. _bylting:

.. rubric:: Hornalínur

.. admonition:: Skilgreining: Hornalína fylkis
   :class: regla

   **Hornalína** (*diagonal*) fylkis liggur frá horninu efst t.v. og niður á ská
   til hægri.

Þannig inniheldur hornalína fylkisins

.. math::
   \begin{pmatrix}1 & 2 & 3\\4 & 5 & 6\\7 & 8 & 9\end{pmatrix}

stökin 1, 5 og 9.

.. rubric:: Bylting

Svokölluð **bylting** (*transpose*) fylkis fæst með því að spegla
því um hornalínuna (þá speglast :math:`a_{ij}` í :math:`a_{ji}`, línur speglast
í dálka og öfugt). Bylting fylkis :math:`A` er táknuð með :math:`A^\text{T}`, lesið "A
bylt":

.. math::
   \begin{pmatrix}1 & 2 \\ 3 & 4\end{pmatrix}^\text{T} = \begin{pmatrix}1 & 3 \\ 2 & 4\end{pmatrix}

.. note::
   Í NumPy fæst hornalína fylkis A með :code:`np.diag(A)` og bylta fylkið með :code:`A.T`.

.. rubric:: Sérstök fylki

Ýmsis fylki með stök sem uppfylla sérstök skilyrði hafa fengið sérstök nöfn. 

   - **Hornalínufylki** (*diagonal matrix*) hefur öll stök utan hornalínunnar núll.
   - **Efra þríhyrningsfylki** (*upper triangular matrix*) hefur öll stök neðan hornalínu núll.
   - **Neðra þríhyrningsfylki** (*lower triangular matrix*) hefur öll stök ofan hornalínu núll.
   - **Núllfylki** (*zero matrix*) hefur öll stök núll.
   - **Samhverft fylki** (*symmetric matrix*) er fylki :math:`A` með :math:`a_{ij} = a_{ji}` fyrir öll :math:`i` og :math:`j`, með öðrum orðum er :math:`A = A^\text{T}`.

.. math::
   \begin{gathered}
   \begin{pmatrix}\text{x} & & \\ & \text{x} & \\ & & \text{x} \end{pmatrix} \qquad
   \begin{pmatrix}
   \text{x} & \text{x} & \text {x} \\
            & \text{x} & \text {x} \\
            &          & \text {x}
   \end{pmatrix} \qquad
   \begin{pmatrix}
   \text {x} & & \\
   \text {x} & \text {x} & \\
   \text{x} & \text {x} & \text {x}
   \end{pmatrix} \\[0.1cm]
   \text{Hornalínufylki, efra og neðra þríhyrningsfylki (núllin eru sýnd með eyðum)} \\[0.5cm]
   \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \qquad
   \begin{pmatrix} 1 & 5 & 10 \\ 5 & 2 & 7 \\ 10 & 7 & 3
   \end{pmatrix} \\[0.1cm]
   \text{Núllfylki og samhverft fylki}
   \end{gathered}

.. admonition:: Python: 
   :class: python

   Hornalínufylki með :math:`x_0, x_1,\ldots` á hornalínunni fæst með
   ``np.diag(x)``. Efri þríhyrningur fylkis ``A`` fæst með ``np.triu(A)`` og sá
   neðri með ``np.tril(A)``, og :math:`n \times m` núllfylki fæst með
   ``np.zeros(n,m)``.
   
.. _fylki-sinnum-vigur:

Margföldun fylkis og vigurs
---------------------------
Ef :math:`A` er :math:`m \times n` fylki og :math:`x` er :math:`n`-vigur þá er
margfeldi :math:`A` og :math:`x`, táknað :math:`Ax` eða :math:`A \cdot x`,
:math:`m`-vigur með :math:`i`-ta stak jafnt og innfeldi :math:`i`-tu línu
:math:`A` og :math:`x`. Nánar tiltekið gildir:

.. admonition:: Skilgreining: Margfeldi fylkis og vigurs
   :class: regla

   .. math::
      \text{ef}\;y = Ax\;\text{þá er}\;y_i = \sum_{j=1}^n a_{ij}x_j\;\:(i=1,...,m)

.. admonition:: Sýnidæmi: Margfeldi fylkis og vigurs
   :class: synidaemi

   Margfeldi fylkisins :math:`\,A = \begin{pmatrix}1 & 2 & 3\\4 & 5 &
   6\end{pmatrix}\,` og vigursins :math:`\,x = (3, 1, -2)\,` er

   .. math::
      Ax = \begin{pmatrix}
      1\cdot 3 + 2\cdot 1 - 3\cdot 2\\
      4\cdot 3 + 5\cdot 1 - 6\cdot 2\end{pmatrix} =
      \begin{pmatrix}
      3 + 2 - 6\\
      12 + 5 - 12
      \end{pmatrix} =
      \begin{pmatrix}
      -1\\
      5
      \end{pmatrix}

.. attention:: Stundum er gerður greinarmunur á dálkvigri (*column vector*) og
   línuvigri (*row vector*), t.d. :math:`\begin{pmatrix}1\\2\end{pmatrix}` og
   :math:`(1, 2)`. Þegar :math:`x` og :math:`y` eru báðir dálkvigrar þá er
   innfeldið :math:`x \cdot y` stundum táknað með :math:`x^\text{T}y`. Þá er
   nefnilega :math:`x^\text{T}` línuvigur og ef við lítum á hann sem :math:`1 \times n`
   fylki þá er margfeldi þess og vigursins :math:`y` einmitt jafnt og innfeldið
   :math:`x\cdot y`.

.. admonition:: Dreifireglur fyrir margfeldi fylkja og vigra
   :class: regla

   .. math::
      &A(x + y) = Ax + Ay\;\:\text{og}\\
      &(A + B)x = Ax + Bx

   þar sem :math:`A` og :math:`B` eru fylki og :math:`x` og :math:`y` vigrar.
   Hér má setja :math:`-` í stað :math:`+`.

.. note::
   Ef A er NumPy fylki og x er NumPy vigur þá fæst b = margfeldi A og x með :code:`b
   = A @ x`.  

.. Æfing
.. hint::
   Gefnir eru vigrarnir :math:`a = (2, 0, 3)`, :math:`b = (1, -1, 2)` og :math:`c
   = (1, 2, 3)` og fylkin

   .. math::
      A = \begin{pmatrix}1 & 2\\3 & 3\\1 & 4\end{pmatrix}\;\text{og}\;
      B = \begin{pmatrix}2 & 3 & 0\\1 & 2 & 3\end{pmatrix}

   Reiknið: |br| 
   1. :math:`a + b + c =` |br| 
   2. :math:`3a - 2b =` |br| 
   3. :math:`a\cdot b =` |br| 
   4. :math:`Bc =` |br| 
   5. :math:`A^\text{T}a =` |br| 
   6. :math:`2A + B^\text{T}`

.. _línuleg-föll-og-innfeldi:

Línuleg föll og innfeldi
------------------------
Í síðasta kafla var talað um tvívíð föll, sem eru föll frá planinu
:math:`\Bbb{R}^2` yfir í rauntölurnar :math:`\Bbb{R}`. Margvíð föll eru svo föll
frá :math:`n`-víðu rúmi :math:`\Bbb{R}^n` yfir í rauntölurnar :math:`\Bbb{R}`.
Varpmengið getur líka verið margvítt rúm. Ef það er :math:`m`-vítt getum við
ritað

.. math:: f:\Bbb{R}^n \to \Bbb{R}^m.

Þegar varpmengið er margvítt er oft talað um :math:`f` sem vörpun – hugtökin
fall og vörpun (*function* og *map*) eru í raun samheiti, en það er algengt er
að nota orðið **fall** þegar varpmengið er :math:`\Bbb{R}` en **vörpun** ef það
er :math:`\Bbb{R}^m`.

Síðar í kaflanum verður fjallað um hugtakið **línuleg vörpun** (*linear map*) sem
er ákveðin tegund af vörpun sem varðveitir samlagningu og margföldun með tölu,
og við munum komast að því að slíkar varpanir eru nátengdar fylkjum og margföldun með þeim.

Til að einfalda málið einskorðum við okkur til að byrja með við línuleg föll,
sem varpa vigrum í tölur. Þessari skorðu verður svo aflétt í grein um *línulegar varpanir* síðar í þessum kafla.

.. admonition:: Skilgreining: Línulegt fall
   :class: regla

   Fall :math:`f: \Bbb{R}^n \to \Bbb{R}` nefnist **línulegt** ef það uppfyllir:

   .. math::
      &f(x + y) = f(x) + f(y)\;\;\text{fyrir öll}\;x,y \in \Bbb{R}^n\;\;\text{og}\\
      &f(ax) = af(x)\;\;\text{fyrir öll}\;a \in \Bbb{R}\;\text{og}\; x\in\Bbb{R}^n
   
Það skiptir sem sé ekki máli hvort við leggjum saman vigra áður en við beitum
fallinu, eða hvort við leggjum saman útkomurnar úr fallinu, og sama á við um
margföldun með tölu.

.. admonition:: Sýnidæmi: Sönnun á að fall sé línulegt
   :class: synidaemi

   Fallið :math:`f:\Bbb{R}^2 \to \Bbb{R}` sem skilgreint er með :math:`f(x) =
   x_1 + 2x_2` er línulegt. Þetta má sjá með eftirfarandi útreikningum:

      Lát :math:`x` og :math:`y` vera tvívíða vigra og :math:`z = x + y`. Þá
      fæst
      
      .. math::
         &f(x + y) = f(z) = z_1 + 2z_2 = (x_1 + y_1) + 2(x_2 + y_2)\;\text{og}\\
         &f(x) + f(y) = x_1 + 2x_2 + y_1 + 2y_2 = x_1 + y_1 + 2(x_2 + y_2)

      svo fyrra skilyrði skilgreiningarinnar er uppfyllt. Ennfremur fæst með
      :math:`u = ax`:

      .. math::
         f(ax) = f(u) = u_1 + 2u_2 = ax_1 + 2ax_2 = a(x_1 + 2x_2) = af(x)

      svo seinna skilyrðið er líka uppfyllt.

   Fallið :math:`f:\Bbb{R}^2 \to \Bbb{R}` sem sendir :math:`x` í :math:`x\cdot
   x` (innifeldi :math:`x` með sjálfu sér) er hinsvegar ekki línulegt. Við
   sjáum til dæmis að ef :math:`x = (1,0)` þá er :math:`f(2x) = (2,0) \cdot
   (2,0) = 4` en :math:`2f(x) = 2\cdot (1,0)\cdot(1,0) = 2` svo seinna
   skilyrðið er ekki uppfyllt.

.. Æfing
.. hint::
   Hver eftirfarandi falla eru línuleg? Rökstyðjið svörin stuttlega ef þið
   getið.

   1. :math:`f(x) = \text{fyrsta stak } x`
   2. :math:`f(x) = \text{meðaltal staka }x`
   3. :math:`f(x) = \text{stærsta stak }x`
   4. :math:`f(x) = \text{summa staka }x`
   5. :math:`f(x) = x_2 - x_1`
   6. :math:`f(x) = 0` fyrir öll :math:`x`
   7. :math:`f(x) = 1` fyrir öll :math:`x`

   *Dæmi um stuttan rökstuðning:* |br|
   1. **Línulegt**, því að :math:`f(x+y)` =
   fyrsta stak :math:`(x + y)` =
   :math:`x_1 + y_1` =
   :math:`f(x) + f(y)`, og
   :math:`f(ax)` =
   fyrsta stak :math:`ax` =
   :math:`ax_1 = af(x)`

.. _reglur-um-línuleg-föll:
   
Um línuleg föll gilda ýmsar reglur, sem við látum duga að setja fram, en
sönnum ekki.

.. admonition:: Regla: Línulegt fall af línulegri samantekt
   :class: regla

   Ef :math:`f` er línulegt, :math:`a_1, a_2, \ldots, a_k` eru
   tölur og :math:`x_1, x_2, \ldots, x_k` eru vigrar, þá gildir:

   .. math::
      f(a_1 x_1 + \ldots + a_k x_k) = a_1f(x_1) + \ldots + a_kf(x_k)

Skilyrðin í skilgreiningunni á línulegu falli, þar sem lagðir voru saman
tveir vigrar, má sem sé útvíka í summu af fleiri vigrum, og sömuleiðis er
hægt að sameina skilyrðin tvö í eitt skilyrði þar sem bæði er lagt saman og
margfaldað með tölu.

.. admonition:: Regla: Innfeldi gefur línulegt fall
   :class: regla

   Ef :math:`c` er gefinn :math:`n`-vigur og :math:`f` er fall sem
   skilgreint er með :math:`f(x) = c\cdot x` þá er :math:`f` línulegt fall.

.. admonition:: Regla: Línuleg föll eru innfeldi
   :class: regla

   Ef :math:`f` er línulegt fall, :math:`f:\Bbb{R}^n \to \Bbb{R}` þá er til
   :math:`n`-vigur :math:`c` þannig að :math:`f(x) = c\cdot x` fyrir öll
   :math:`x`. Þetta er kallað **innfeldisframsetning** fallsins :math:`f`.

Innfeldi við fastan vigur gefur sem sé línulegt fall, og öll línuleg
föll eru af þessu tagi.

.. admonition:: Sýnidæmi: Innfeldisframsetning
   :class: synidaemi

   Línulega fallið :math:`f(x) = x_1 + 2x_2`, hefur innfeldisframsetningu
   :math:`f(x) = (1,2) \cdot x`.

.. admonition:: Æfing: Innfeldisframsetning
   :class: aefing

   Hver er innfeldisframsetning fallsins :math:`f(x) = 3x_3 - 2x_2 - x_1`?
         
.. admonition:: Sýnidæmi: Sig brúar
   :class: synidaemi

   Mörg föll sem koma við sögu í raunvísindum og verkfræði má
   nálga með línulegum föllum. Hér skoðum við eitt slíkt dæmi. Á
   brú verka kraftar :math:`w_1, w_2` og :math:`w_3` (þyngdir bíla í tonnum) á þremur
   gefnum stöðum. Þeir valda því að brúinn sígur um :math:`s` millimetra í
   miðjunni. Samband :math:`s` og :math:`w` er gefið með línulegu falli:

   .. math::
      s = c_1 w_1 + c_2 w_2 + c_3 w_3

   Með aðferðum burðarþolsfræði er hægt að ákvarða stuðlana :math:`c_i` útfrá
   nákvæmum upplýsingum um hönnun brúarinnar, en það er líka hægt
   að setja bíl af gefinni þyngd á staðina þrjá og mæla :math:`s`
   fyrir hvern stað og ákvarða þannig :math:`c_i`.

   .. figure:: myndir/bru.png
      :figwidth: 11cm
      :align: center

   Brú sígur þegar bílar keyra yfir hana

.. admonition:: Æfing: Bílar á brú
   :class: aefing

   1. Tveggja tonna bíll á stöðunum þremur sem merktir eru með :math:`w_1`,
      :math:`w_2` og :math:`w_3` á myndinni að ofan veldur sigi sem er 0.24 mm,
      0.31 mm og 0.26 mm. Ákvarðið stuðana :math:`c_i, i=1,2,3`
   2. Nú eru þrír bílar settir á staðina, 1.5 tonn, 0.8 tonn og 1.2
      tonn. Hve mikið sígur brúin í miðjunni?

.. _taylor-nálgun:      

Taylor-nálgun
-------------
Rifjum upp úr grein :numref:`margvíð föll` að stigull af :math:`n`-víðu falli
:math:`f` er skilgreindur með:

.. math::
   \nabla f(x) =
   \begin{pmatrix}
   \dfrac{\partial f(x)}{\partial x_1}\\
   \vdots\\
   \dfrac{\partial f(x)}{\partial x_n}
   \end{pmatrix}

Hér táknar :math:`\dfrac{\partial f(x)}{\partial x_i}` hlutafleiðuna af :math:`f`
með tilliti til :math:`x_i` (:math:`i`-ta staks :math:`x`). Stundum er
hlutafleiða :math:`f` í :math:`x` m.t.t. :math:`x_i` táknuð með :math:`f_i(x)`.
Ef :math:`x` vigur settur saman úr talnabreytum t.d. :math:`x = (u, v, w)` eru
hlutafleiðurnar líka stundum ritaðar með því að láta breytu vera lágvísi, t.d.
:math:`f_u`, í stað :math:`\dfrac{\partial f}{\partial u}`. Enn einn
rithátturinn fyrir afleiðu :math:`f` m.t.t. :math:`x` er :math:`D_x f(x,...)`.

.. admonition:: Sýnidæmi: Stigull
   :class: synidaemi

   Lát

   .. math::
      f(x,y,z) = xy^3 + (2x^2 - z)^2

   Þá er

   .. math::
      \nabla f(x,y,z) =
      \begin{pmatrix}
      y^3 + 2(2x^2 - z) 4x\\
      3xy^2 + 0\\
      0 + 2(2x^2 - z)(-1)
      \end{pmatrix} = 
      \begin{pmatrix}
      y^3 + 8x(2x^2 - z)\\
      3xy^2\\
      -4x^2 + 2z
      \end{pmatrix}

.. admonition:: Æfing: Afleiður og stiglar
   :class: aefing

   1. Finnið :math:`f'(x)`, :math:`g'(x)` og :math:`h'(x)` ef:

      .. math::
         f(x) &= 2x^3 + 5 \\
         g(x) &= 2ax^3 + b \\
         h(x) &= \frac{(2x-1)^3}{3}

   2. Lát
      
      .. math::
         f(x,y,z) = xyz + x^2y^2 - (z-x)^2
         
      Ákvarðið :math:`\nabla f(x,y,z)`
      
   3. Lát :math:`f(x) = \dfrac{\sin x_1}{x_2}`. Ákvarðið :math:`\nabla f(x)`
      
   4. Finnið :math:`D_z \dfrac{\exp(xyz)}{xyz}` (munið að :math:`D\dfrac{u}{v} =
      \dfrac{u'v-v'u}{v^2}`)

.. _taylor:
      
Ef :math:`f` er eitthvert gefið fall þá er ein leið til að nálga það með
línulegu falli sú að nota setningu Taylors. Einvíðu útgáfuna af
henni þekkja margir nemendur, en fyrir nálgun með beinni línu hljóðar hún svona:

.. admonition:: Regla: Einvíð Taylor-setning
   :class: regla

   Ef :math:`a` er gefin tala og :math:`f` er diffranlegt fall þá gildir fyrir
   :math:`x` nálægt :math:`a` að

   .. math::
      f(x) \approx f(a) + f'(a)(x-a) \;\;\; \text{(einvíð Taylor-setning)}

Ef :math:`f` er margvítt fall, :math:`f: \Bbb{R}^n \to \Bbb{R}`, og :math:`x` er
vigur nálægt vigrinum :math:`a` þá má líka nálga :math:`f(x)` línulega, en nú
kemur stigull í stað afleiðu, og innfeldi í stað margföldunar:

.. admonition:: Regla: Margvíð Taylor-setning
   :class: regla

   .. math::
      f(x) \approx f(a) + \nabla f(a) \cdot (x-a) \;\;\; \text{(margvíð Taylor-setning)}

.. admonition:: Skilgreining: Taylor-nálgun
   :class: regla
      
   Fallið :math:`\hat{f}(x) = f(a) + \nabla f(a) \cdot (x-a)` er nefnt
   **línuleg Taylor-nálgun** við :math:`f` í :math:`a`.

.. figure:: myndir/taylor1.png
   :figwidth: 6cm
   :name: taylor-lína
   :align: center

   Einvítt fall og línuleg Taylor-nálgun þess í :math:`a`

Athugið að þegar :math:`f` er einvítt
fall þá er Taylor-nálgunin jafna beinnar línu sem snertir ferilinn sem táknar
graf fallsins í :math:`(a,f(a))` (sbr. :numref:`taylor-lína`), og að
þegar :math:`f` er tvívítt þá er hún jafna plans sem snertir yfirborðið sem
táknar graf fallsins í :math:`(a,f(a))` (:numref:`snertiplan`).

.. figure:: myndir/snertiplan.png
   :figwidth: 8cm
   :name: snertiplan
   :align: center

   Flötur (graf tvíðvíðs falls) og snertiplan við hann.

.. admonition:: Sýnidæmi: Taylor nálgun
   :class: synidaemi

   Látum :math:`f(x) = x_1 + \exp(x_2 - x_1)` og skoðum línulega Taylor-nálgun
   þess í :math:`a = (1,2)`. Við fáum:

   .. math::
      f(a) = a_1 + \exp(a_2 - a_1) = 1 + \exp(1) = 3.718

   ef reiknað er með þremur aukastöfum. Diffrun gefur svo:

   .. math::
      \nabla f(x)
      &=
      \begin{pmatrix}
      1 - \exp(x_2 - x_1)\\
      \exp(x_2 - x_1)
      \end{pmatrix} \\
      \nabla f(a)
      &=
      \begin{pmatrix} 1 - \exp(2-1)\\ \exp(2-1) \end{pmatrix}\\
      &= (1 - \exp(1), \exp(1)) \\
      &= (-1.718, 2,718)

   Ef þetta er sett inn í margvíðu Taylor-setninguna fæst:

   .. math::
      \hat{f}(x) &= f(a) + \nabla f(a) \cdot (x - 1. \\
                 &= 3.718 + (-1.718, 2.718) \cdot (x_1 - 1, x_2 - 2) \\
                 &= 3.718 - 1.718(x_1 - 1) + 2.718(x_2 - 2) \\
                 &= -1.718x_1 + 2.718x_2
                 
   Eftirfarandi tafla sýnir :math:`f(x)` og :math:`\hat{f}(x)` fyrir nokkur
   gildi á :math:`x` í grennd við :math:`a`
      
        .. list-table::
           :header-rows: 1
           :widths: auto
           :align: center

           * - :math:`x`
             - :math:`f(x)`
             - :math:`\hat{f}(x)`

           * - :math:`(1,2)`
             - 3.7183
             - 3.7183

           * - :math:`(0.96, 1.98)`
             - 3.7332
             - 3.7326

           * - :math:`(0.85, 2.05)`
             - 4.17
             - 4.11

           * - :math:`(1.25, 1.41)`
             - 4.44
             - 4.40

   Við sjáum að nálgunin er bara ágæt.

.. admonition:: Æfing: Línuleg Taylor nálgun
   :class: aefing

   1. Ákvarðið :math:`\hat{f}(x)`, línulega Taylor-nálgun fallsins :math:`f(x) = 2\ln(x)+1`,
      í punktinum :math:`a=1`. Gerið töflu yfir :math:`f(x)` og
      :math:`\hat{f}(x)` fyrir :math:`x = 1, 1.1` og :math:`1.2`

   2. Finnið línulega Taylor-nálgun við tvívíða fallið
      :math:`f(x) = x_1^2 + x_1 x_2 + x_2^2` í punktinum :math:`a = (1,2)`. Ákvarðið gildi
      :math:`f(x)` og nálgunarinnar í punktinum :math:`x = (1.1, 2.1)`.

   3. Finnið Taylor-nálgun við þrívíða fallið :math:`f(x,y,z) = xyz + x`
      í punktinum :math:`(1,1,0)` [þetta er æfing í því tilviki að viðfang þrívíðs falls
      sé ritað sem vigur :math:`(x,y,z)`].

Norm, fjarlægðir og horn
------------------------
Í þessum kafla verður fjallað um norm, sem er mælikvarði á 
stærð vigurs, og skyld hugtök, fjarlægðir og horn milli vigra.

.. rubric:: Norm

Eins og áður hefur verið bent á er hægt að túlka tvívíða og þrívíða vigra sem
færslu í plani eða rúmi, eða ör sem hefur stefnu og lengd.

.. figure:: myndir/vigrar.png
   :figwidth: 8cm
   :align: center

   Tvívíðir vigrar sýndir sem örvar (eða færslur)

Það liggur beint við að leggja mælikvarða á stærð slíkra vigra með því að mæla
lengd þeirra í rúminu. Þessa lengd má líka reikna með Pýþagórasarreglu útfrá
hnitum vigranna og þá fæst:

.. math::
   \text{Lengd } x = \sqrt{x_1^2 + x_2^2}

Fyrir vigra í þrívíðu rúmi er hægt að beita Pýþagórasarreglu tvisvar til
að reikna lengdina og fá:

.. math::
   \text{Lengd } x = \sqrt{x_1^2 + x_2^2 + x_3^2}

Nú liggur beint við hvernig hægt er að útvíkka þessar formúlur fyrir almenna
:math:`n`-víða vigra. Hugtakið sem fæst er nefnt **Evklíðskt norm** (*Euclidean
norm*) eða 2-norm, og táknað með :math:`\|x\|`, eða stundum :math:`\|x\|_2` til
að aðgreina það frá öðrum aðferðum til að skilgreina norm sem verða reyndar ekki
á dagskrá hér:

.. admonition:: Skilgreining: Norm
   :class: regla

   Evklíðskt **norm** af :math:`n`-vigri :math:`x` er

    .. math::
       \|x\| = \sqrt{x_1^2 + \ldots + x_n^2}

Normið er kennt við gríska stærðfræðingnn Evklíð sem skrifaði mikil verk og
sannaði margar setningar um rúmfræði.

.. note:: Í NumPy má reikna norm vigurs :code:`x` með fallinu :code:`norm`
   í pakkanum :code:`numpy.linalg`, sem sé t.d. :code:`import numpy.linalg as
   la` og svo :code:`la.norm(x)`.

.. attention:: Í `Stærfræðiorðasafninu <http://stæ.is/os>`_ er *norm* þýtt með
   *staðall* eða *lengd*, en í þessum fyrirlestrarnótum er aðeins slakað
   á hreintungustefnunni.

.. admonition:: Æfing: Norm
   :class: aefing

   1. Reiknið :math:`\|(3, 4)\|`      
   2. Reiknið :math:`\|(2, -4, -5, 6)\|`
   3. Sýnið að fyrir öll horn :math:`\theta` gildir að :math:`\|(\sin \theta,
      \cos\theta)\| = 1`

Hægt er að leiða út fjölmargar reglur um norm, en hér verða örfáar látnar
duga. Í eftirfarandi reglum eru :math:`x` og :math:`y` einhverjir
:math:`n`-vigrar og :math:`\alpha` einhver rauntala:

.. admonition:: Reglur um norm
   :class: regla

   .. math::
      &\|\alpha x\| = |\alpha|\cdot \|x\| \\
      &\|x + y\| \leq \|x\| + \|y\| \text{ (þríhyrningsójafnan)} \\ 
      &\|x\| \geq 0 \\
      &\|x\| = 0 \text{ þ.þ.a.a } x = 0

   (þ.þ.a.a. er skammstöfun á "þá og því aðeins að").

.. admonition:: Æfing: Sönnun tveggja normreglna
   :class: aefing

   1. Sannið fyrstu regluna.
   2. Sannið þríhyrningsójöfnuna fyrir tvívíða vigra með því að teikna
      viðeigandi þríhyrning, og notfæra ykkur að stysta leið
      milli tveggja punkta er bein lína.

.. rubric:: Fjarlægðir
      
Snúum okkur þá að fjarlægðum í n-víðu rúmi. Oft eru orðin vigur og
punktur notuð sem samheiti, og það á við um okkar umfjöllun, þannig að það
er hægt að tala um hvort sem er fjarlægð milli vigra eða fjarlægð milli punkta.

Ef :math:`a` og :math:`b` eru tveir punktar í plani eða þrívíðu rúmi þá er vigur
frá :math:`a` til :math:`b` gefinn með :math:`b - a`:

.. figure:: myndir/fjarlægð.png
   :figwidth: 5cm
   :align: center

og þessvegna er fjarlægðin milli :math:`a` og :math:`b` gefin með
:math:`\|b-a\|`, eða :math:`\|a-b\|` sem er jafngilt. Því liggur beint við
að skilgreina fjarlægð milli almennra vigra á sama hátt.

.. admonition:: Skilgreining: Fjarlægð milli vigra
   :class: regla

   Ef :math:`a` og :math:`b` eru :math:`n`-vigrar þá er **fjarlægðin** milli
   :math:`a` og :math:`b` gefin með:

      .. math:: \|a-b\|

Ekki er erfitt að sjá að ef lítill munur er á tilsvarandi stökum tveggja vigra
þá verður fjarlægðin á milli þeirra lítil tala.

.. admonition:: Skilgreining: Fjarlægð milli vigra
   :class: regla

   Fjarlægðin á milli vigranna :math:`x = (2,3,5,5)` og :math:`y = (1,1,1,-5)` er  

   .. math::
      \|x-y\| &= \|(1,2,4,10)\| \\
      &= \sqrt{1^2 + 2^2 + 4^2 + 10^2}
      &= \sqrt{121}
      &= 11

Fjarlægðir milli vigra koma við sögu í ýmsum verkefnum í reiknifræði, og ýmsum
reikniritum, t.d. hinu velþekkta *k-means* reikniriti sem fjallað verður um
síðar í þessum fyrirlestrarnótum, og sömuleiðis í verkefnum í máltækni t.d. í
samanburði tveggja texta, eins og við skoðum nú.

.. _orðtíðni:

.. rubric:: Orðtíðni og fjarlægð milli vigra

Orðtíðnivigur fyrir skjal (eða vefsíðu) er gerður þannig að hvert orð
í skjalinu er fært yfir á staðalsnið (t.d. nefnifall eintölu fyrir
nafnorð), orðunum er raðað í stafrófsröð, og svo er talið hve oft hvert
orð kemur fyrir. Oft er algengum orðum (t.d. og, er, á, í) sleppt og líka
sjaldgæfum. Tökum sem dæmi vísupartinn:

    Ástin er eins og sinueldur. |br|
    Ástin er segulstál. |br|
    Af litlum neista verður oft mikið bál. |br|
    Ástin er eins og hvítigaldur, |br|
    gagntekur líkama’ og sál.

Orðtíðnirit fyrir hana gæti verið:

   .. list-table::
      :widths: auto
      :name: orðtíðnitafla
      :align: center
         
      * - ást
        - 3
        - 0.30
                   
      * - bál
        - 1
        - 0.10

      * - eins
        - 2
        - 0.20

      * - líkami
        - 1
        - 0.10

      * - lítill
        - 1
        - 0.10

      * - mikið
        - 1
        - 0.10

      * - neisti
        - 1
        - 0.10

og miðdálkurinn gefur orðtíðnivigur. Ef bera á saman tvö eða fleiri skjöl er
búinn til sameiginlegur orðalisti fyrir þau öll áður en orðin eru talin, og ef
skjölin eru mislöng þá er sennilega betra að reikna orðtíðnina hlutfallslega,
eins og í aftasta dálkinum í töflunni að ofan. Tvö skjöl sem fjalla um sama eða
svipuð efni eru líklegri til að hafa stutt á milli orðtíðnivigra sinna heldur en
skjöl um ólík efni.

.. admonition:: Skilgreining: Fjarlægðir milli Wikipedíugreina
   :class: regla

   Búnir voru til orðtíðnivigrar fyrir þrjár greinar á Wikipediu, um
   Óskarsverðlaunin, Golden-globe-verðlaunin, og ofurskálina, og fjarlægðirnar
   á milli þeirra reiknaðar. Niðurstaðan var:

   .. list-table::
      :widths: auto
      :align: center
         
      * - 
        - Óskarsverðlaun
        - Golden-globe
        - Ofurskál
                   
      * - Óskarsverðlaun
        - 0
        - 0.11
        - 0.17
                   
      * - Golden-globe
        - 0.11
        - 0
        - 0.18

      * - Ofurskál
        - 0.17
        - 0.18
        - 0

   Hér sést að fjarlægðin milli greinanna um verðlaunin er minni en fjarlægðin frá
   þeim yfir í ofurskálargreinina.

.. _horn-milli-vigra:   
   
.. rubric:: Horn milli n-vigra

Í tvívíðu og þrívíðu rúmi er hægt að reikna horn milli tveggja vigra
rúmfræðilega útfrá innfeldi og normum vigranna. Formúlan sem
hægt er að sanna fyrir :math:`n = 2` og :math:`n = 3`, er sú sem gefin er
í eftirfarandi skilgreininingu, sem útvíkkar sem sé hugtakið horn þegar
:math:`n > 3`:

.. admonition:: Skilgreining: Horn milli vigra
   :class: regla

   Ef :math:`x` og :math:`y` eru :math:`n`-vigrar þá er **hornið** milli þeirra
   gefið með

    .. math::
       \theta = \arccos \frac{x \cdot y}{\|x\|\, \|y\|}

.. admonition:: Python: 
   :class: python

   Í Python má nota fallið ``math.acos`` til að reikna arccos, ``@`` til að
   reikna innfeldi og ``la.norm`` til að reikna norm. Ef mæla skal
   :math:`\theta` í gráðum þarf auk þess að kalla á ``math.degrees`` í lokin.
   Ef ``x`` og ``y`` eru NumPy vigrar fæst hornið á milli þeirra með:

   ``theta = math.degrees(math.acos(x@y/(la.norm(x)*la.norm(y)))``
       
Í framhaldi af síðustu skilgreiningu og reglunni um innfeldi og horn milli
rúmvigra í kafla :numref:`ýmis vigur- og fylkjahugtök` liggur sú næsta beint við
að skilgreina hvenær almennir n-vigrar teljast hornréttir hvor á annan svo:

.. admonition:: Skilgreining: Hornréttir vigrar
   :class: regla

   Vigrarnir :math:`x` og :math:`y` eru sagðir **hornréttir** (*perpendicular*)
   hvor á annan, ritað :math:`x \perp y`, ef hornið á milli þeirra er 90°,
   þ.e.a.s. ef :math:`x \cdot y` = 0.

.. rubric:: **Horn og líkindi með vigrum**.

Í staðinn fyrir að mæla fjarlægð milli orðtíðnivigra er hægt að nota hornið á
milli þeirra til að meta líkindi með tveimur skjölum eða vefsíðum.

.. admonition:: Sýnidæmi: Horn milli Wikipedíugreina
   :class: synidaemi

   Í eftirfarandi töflu hafa hornin milli orðtíðnivigra Wikipedíuskjalanna úr
   síðasta sýnidæmi verið reiknuð.

   .. list-table::
      :widths: auto
      :align: center
         
      * - 
        - Óskarsverðlaun
        - Golden-globe
        - Ofurskál
                   
      * - Óskarsverðlaun
        - –
        - 59°
        - 87°
                   
      * - Golden-globe
        - 59°
        - –
        - 86°

      * - Ofurskál
        - 87°
        - 86°
        - –

   Við sjáum að eins og í sýnidæminu þar sem við notuðum fjarlægðir eru
   verðlaunagreinarnar mun nær hvor annarri en ofurskálargreininni samkvæmt
   hornmælikvarðanum. Öfugt við fjarlægðarkvarðann þá er óþarfi að reikna
   hlutfallslega orðtíðni því sömu horn fást með því að nota orðtíðnina beint
   (t.d. miðdálkinn í töflunni um tíðni orða í kvæðinu um ástina.

.. admonition:: Æfing: Horn milli vigra
   :class: aefing

   1. Reiknið hornið á milli vigranna :math:`(4,3)` og :math:`(1,0)`.
   
   2. Notið regluna um kósínus af mismun,

      .. math::
         \cos(a - 2. = \cos a\cos b + \sin a \sin b

      til að sýna að skilgreiningin á horni milli :math:`x` og :math:`y` að framan
      gefur rúmfræðilega hornið þegar vigrarnir eru tvívíðir.

          **Leiðbeining:** *Hornið á milli vigranna er mismunur stefnuhorna
          þeirra. Í pólhnitum verða hnit* :math:`x` *og* :math:`y`:

          .. math::
             x_1 &= r\cos a \qquad y_1 &= R \cos b\\
             x_2 &= r \sin a \qquad y_2 &= R \sin b

          *þar sem* :math:`r = \|x\|`, :math:`R = \|y\|`, :math:`a = {}`
          *stefnuhorn* :math:`x` *og* :math:`b = {}` *stefnuhorn* :math:`y`.

[efni í vinnslu]

Tölfræðileg föll af vigrum
--------------------------
   
.. rubric:: Meðaltal, dreifni og staðalfrávik

Meðaltal (*mean* eða *average*), dreifni (*variance*) og staðalfrávik (*standard deviation*). eru hugtök í tölfræði sem eru samt nátengd vigrum og línulegri algebru.

.. admonition:: Skilgreining: Meðaltal
   :class: regla

   **Meðaltal** :math:`n`-vigurs :math:`x` er gefið með
    
    .. math::
       \newcommand{\Var}{\operatorname{Var}}\newcommand{\std}{\operatorname{std}}
       \overline{x} = \frac{1}{n}\sum_{i=1}^n x_i

.. admonition:: Skilgreining: Dreifni
   :class: regla

   **Dreifni** :math:`n`-vigurs :math:`x` er gefin með
    
    .. math::
       \Var{x} = \frac{1}{n}\sum_{i=1}^n (x_i - \overline{x})^2

.. admonition:: Skilgreining: Staðalfrávik
   :class: regla

   **Staðaðfrávik** :math:`n`-vigurs :math:`x` er gefið með
    
    .. math::
       \std{x} = \sqrt{\Var{x}} = \sqrt{\frac{1}{n}\sum_{i=1}^n (x_i -
       \overline{x})^2}

Dreifni og staðalfrávik eru mælikvarði á það hve langt frá meðaltalinu einstök
stök vigursins eru að jafnaði. Í staðinn fyrir að leggja saman önnur veldi af
fráviki frá meðaltali væri mögulegt að leggja í saðinn saman tölugildi
frávikanna, :math:`\frac{1}{n}\sum_{i=1}^n |x_i - \overline{x}|`, en ýmsar
ástæður, bæði tölfræðilegar og reiknitæknilegar, mæla gegn því.

.. attention::
   Í tölfræði er algengt að skilgreina dreifni gagnasafns með formúlu þar sem
   deilt er með :math:`n-1` en ekki :math:`n`:

   .. math::
      \textrm{Dreifni gagnasafns} = \frac{1}{n-1}\sum_{i=1}^n (x_i - \overline{x})^2

   (og tilsvarandi fyrir staðalfrávik). Þá verður dreifnin óbjöguð (*unbiased*) eins
   og það er kallað. Í línulegri algebru er (líklega) algengara að deila með :math:`n`.

.. admonition:: Reglur um staðalfrávik
   :class: regla

   Ef :math:`x` er :math:`n`-vigur og :math:`a` er rauntala þá gilda
   eftirfarandi reglur um staðalfrávik:

   .. math::
      &{\bf 1.}\;\,\text{Ef } y_i = x_i + a \text{ fyrir öll } i \text{ þá er } \std(y) =
      \std(x)\\
      &{\bf 2.}\;\std(ax) = |a|\std(x)

Það breytir sem sagt ekki staðalfráviki að leggja fasta við öll stök
vigurs, og ef vigur er margfaldaður með tölu, þá margfaldast staðalfrávikið með
tölugildinu af tölunni.

.. note::
   Með NumPy má reikna meðaltal, dreifni og staðalfrávik :code:`x` með
   :code:`np.mean(x)`, :code:`np.var(x)` og :code:`np.std(x)`, eða með
   :code:`x.mean()`, :code:`x.var()` og :code:`x.std()`.

Stundum hentar að staðla (*standardize*) gögn, en þá er meðaltal þeirra dregið
frá og deilt með staðalfrávikinu, og þannig fæst útgáfa af gögnunum sem hefur
meðaltal 0 og staðalfrávik 1. Stöðluð útgáfa vigurs :math:`x` er stundum gefið
nafnið :math:`z` og/eða kölluð **z-stig** (*z-score*), sérstaklega ef :math:`x` er
vigur af normaldreifðum gögnum.

.. admonition:: Skilgreining: Stöðlun
   :class: regla

   **Stöðlun** (*standardization*) vigurs :math:`x` hefur :math:`i`-ta stak

   .. math::
      z_i = \frac{x_i - \overline{x}}{\std(x)}

Hægt er að hugsa sér að :math:`z_i` mæli hve mörgum staðalfrávikum fyrir ofan
eða neðan meðaltalið :math:`x_i` er. Skylt þessu er þegar búnir eru til
mælikvarðar með meðaltal og staðalfrávik sem eru rúnnaðar tölur, t.d.
greindarvísitala sem skv. skilgreiningu hefur meðaltal 100 og staðalfrávik 15.
         
.. admonition:: Æfing: Staðalfrávik og stöðlun
   :class: aefing

   1. Ákvarðið meðaltal, dreifni og staðalfrávik vigursins
      :math:`x = (0, 2, 3, 4, 6)`

   2. Ákvarðið í framhaldi staðlaða útgáfu af :math:`x`
   
   3. Notið lið 1 og reglur um staðalfrávik til að reikna staðalfrávik vigranna
      :math:`y = (2,4,5,6,8)` og :math:`z = -3x`

Fylgnistuðull eða fylgni (*correlation (coefficient)*) er líka tölfræðilegt
hugtak tengt línulegri algebru og vigrum. Reyndar eru til nokkrar leiðir til að
reikna fylgni, en sú langalgengasta er að nota fylgnistuðul Pearsons og það er
gert hér. Um hann má lesa nánar t.d. á
`Wikipedíu <https://en.wikipedia.org/wiki/Pearson_correlation_coefficient//>`_.
Fylgni mælir samband tveggja vigra, hann er á bilinu :math:`[-1,1]` og hann er
:math:`-1` eða :math:`1` ef skatterplot af vigrunum liggur á beinni línu, og
:math:`0` ef jafna bestu línu fyrir slíkt plot er lárétt.

.. admonition:: Skilgreining: Fylgni
   :class: regla

   **Fylgnistuðull** tveggja :math:`n`-vigra :math:`x` og
   :math:`y` er gefinn með:

    .. math:: r_{xy} = \frac{\sum_{i=1}^n (x_i - \overline{x})(y_i -
       \overline{y})}{\std(x) \std(y)}


.. note::
   Til að reikna fylgni í Python má nota tölfræðipakkann í Scipy, t.d.:

   .. code:: python
      
      import scipy.stats as st
      x = np.array([1, 2, 3])
      y = np.array([2, 3, 4])
      r,p = st.pearsonr(x,y)

   Hér skilar :code:`r` fylgnistuðlinum, og :code:`p` marktæknistigi hans eða
   :math:`p`-gildi, sem í grófum dráttum eru líkurnar á að fá fylgni sem er
   :math:`r` eða meiri að tölugildi fyrir tilviljun, ef vigrarnir tveir væru
   slembivigrar úr óháðum normaldreifingum.

.. hint::
   Eftirfarandi forritsbútur skilgreinir fall til að búa til tvo vigra sem hafa fylgni
   u.þ.b. r. Afritið forritsbútinn yfir í Júpíter og keyrið hann.

   .. code:: python
      
      import numpy as np, matplotlib.pyplot as plt, numpy.random as rnd
      np.set_printoptions(precision=2, floatmode='fixed', suppress=True)

      def tvinormal(r,n):
          """skilar tveimur n-vigrum með meðaltal 0, dreifni 1, 
             og fylgni r (um það bil)"""
          mu = np.array([0,0])
          Sig = np.array([[1,r],[r,1]])
          (x,y) = rnd.multivariate_normal(mu,Sig,n).T
          return x,y

   1. Bætið við forritið hér á undan skipunum sem búa til tvo tíu staka vigra
      með fylgni u.þ.b. 0.9 og reikna og prenta út raunverulega fylgni þeirra.
      Prentið líka út vigrana hlið við hlið (t.d. með ``print(np.c_[x,y])``).
      Keyrið nokkrum sinnum. Prófið líka 100-staka vigra. Takið eftir að ef
      :code:`x[i]` er stórt þá er :code:`y[i]` oftast stórt líka og öfugt.

   2. Búið líka til reit til að búa til 500-staka vigra með fylgni u.þ.b. 0.9 og
      teiknið þá með :code:`plt.scatter` (sbr. 9. kafla í
      Python-fyrirlestrarnótum). Hæfilegt er að nota punktastærð 5. Endurtakið
      fyrir nokkur mismunandi gildi á r (t.d. -0.99, 0, 0.4, 0.99).

Línulega háðir og óháðir vigrar
-------------------------------

.. _línulega-háðir:

.. admonition:: Skilgreining: Línuleg samantekt
   :class: regla

   Ef :math:`x_1`,..., :math:`x_k` eru vigrar og :math:`c_1`,..., :math:`c_k`
   eru tölur þá er vigurinn
          
   .. math::
      y = c_1 x_1 + \ldots + c_k x_k
       
   kallaður **línuleg samantekt** (*linear combination*) af vigrunum
   :math:`x_1`,..., :math:`x_k`

Mengi allra línulegra samantekta af vigrum :math:`x_1`,..., :math:`x_k`
er sagt vera **spannað** (*spanned*) af vigrunum.

.. admonition:: Sýnidæmi: Spann vigra
   :class: synidaemi

   Ef :math:`u = (1,1,0)` og :math:`v = (0,0,1)` þá er :math:`y = 3u + 2v`
   línuleg samantekt af :math:`u` og :math:`v`. Mengið sem :math:`u` og
   :math:`v` spanna er lóðrétta planið í gegn um línuna :math:`y = x`.
   Þetta mengi má rita:

   .. math::
      \{w \in \Bbb{R}^3 |\; w = au + bv \text{ fyrir einhver } a,b \in \Bbb{R}\}

   Hér er mynd sem sýnir þessa vigra og tilheyrandi spannplan:

   .. figure:: myndir/plotspan.png
      :figwidth: 11cm
      :align: center

Skilgreinum nú línulega háða (*linearly dependent*) vigra.
              
.. admonition:: Skilgreining: Línulega háðir vigrar
   :class: regla

   Vigrar :math:`x_1`,..., :math:`x_k` eru sagðir **línulega
   háðir** ef hægt er að rita einhvern þeirra sem línulega samantekt af hinum,
   þ.e.a.s. ef fyrir eitthvert :math:`j` eru til tölur :math:`c_i` þannig að:

   .. math::
      x_j = \sum_{i=1\\i \neq j}^k c_i x_i

Rauðu vigrarnir þrír á myndinni í sýnidæminu hér á undan eru sem sé línulega
háðir, því :math:`3u + 2v` er línuleg samantekt af :math:`u` og :math:`v`. Það
er ekki mjög erfitt að sjá að þrír vigrar í þrívíðu rúmi sem allir liggja í sama
plani hljóta að vera línulega háðir. Um tvo samsíða vigra (sem liggja þar með á
sömu línu), hvort sem er í tvívíðu eða þrívíðu rúmi, gildir að þeir eru línulega
háðir.

Ef :math:`A` er mengi af vigrum er talað um að það sé línulega háð ef vigrarnir
í því eru línulega háðir. Stundum er skilyrðið í skilgreiningunni orðað
öðruvísi, sbr. eftirfarandi setningu.

.. admonition:: Setning: Skilyrði fyrir að vigrar séu línulega háðir 
   :class: regla

   :math:`x_1`,..., :math:`x_k` eru línulega háðir þ.þ.a.a. til
   séu tölur :math:`c_1,\ldots, c_k` sem eru ekki allar :math:`0` þannig að
   :math:`c_1 x_1 + \ldots + c_k x_k = 0`

Vigrar eru sem sé línulega háðir þ.þ.a.a. til sé línuleg samantekt af þeim sem
er núllvigurinn, með samantektarstuðlum sem eru ekki allir 0.

Eitt í viðbót sem rétt er að benda á: Ef :math:`A = \{x_1, \ldots, x_k\}` er
mengi af línulega háðum vigrum og :math:`y \notin A` þá er :math:`A \cup
\{y\}` líka línulega háð. Skv. síðustu setningu höfum við :math:`c_1 x_1 +
\ldots + c_k x_k = 0` og við summuna má svo bæta :math:`0y`, og hún er ennþá
jöfn :math:`0`.

.. _línulega-óháðir:

.. admonition:: Skilgreining: Línulega óháðir vigrar
   :class: regla


   Vigrar :math:`x_1`,..., :math:`x_k` eru sagðir **línulega óháðir**
   (*lindearly independent*) ef þeir eru ekki línulega háðir.

Skv. setningunni að framan gildir sem sé að ef eina leiðin til að búa til
línulega samantekt af vigrum sem er núll er sú að velja alla samantektarstuðlana
sama sem núll þá eru vigrarnir línulega óháðir, en annars ekki.
Þetta gefur okkur aðferð til að sanna að mengi vigra sé línulega óháð:
Við byrjum á að rita:

    .. math::
       c_1 x_1 + \ldots + c_k x_k = 0

og sýnum að það leiði til :math:`c_1 = c_2 = \ldots = c_k = 0`

.. admonition:: Sýnidæmi: Sönnun á að vigrar séu línulega óháðir
   :class: synidaemi

   Sýnum að :math:`u=(1,2,3)`, :math:`v=(1,0,3)` og :math:`w=(0,1,1)` séu
   línulega óháðir. Gerum ráð fyrir að :math:`c_1u + c_2v + c_3w = 0` sem sé

   .. math::
      c_1\begin{pmatrix}1\\2\\3\end{pmatrix} + 
      c_2\begin{pmatrix}1\\0\\3\end{pmatrix} + 
      c_3\begin{pmatrix}0\\1\\1\end{pmatrix} =
      \begin{pmatrix}0\\0\\0\end{pmatrix}

   Þetta gefur

   .. math::
      &(1)\quad c_1 + c_2 = 0,\\
      &(2)\quad 2c_1 + c_3 = 0 \text{ og}\\
      &(3)\quad 3c_1 + 3c_2 + c_3 = 0.

   Af :math:`(3) - 3\cdot(1)` fæst :math:`c_3=0`, svo :math:`(2)` gefur
   :math:`c_1=0` sem með :math:`(1)` gefur að lokum :math:`c_2=0`. Þetta sýnir
   að :math:`u`, :math:`v` og :math:`w` eru línulega óháðir.

Tveir vigrar eru sagðir samsíða ef annar er margfeldi af hinum, og eins og að
framan segir er par af ekki-núll vigrum línulega háð ef þeir eru samsíða, en
annars er parið línulega óháð (þetta er bein afleiðing af skilgreiningu á
línulega háðum vigrum).

.. admonition:: Æfing: Línuleg samantekt og vigrapör
   :class: aefing

   1. Skrifið vigurinn :math:`(8,3)` sem línulega samantekt af :math:`(4,1)` og
      :math:`(0,1)`.
   2. Eru eftirfarandi pör vigra línulega óháð?
      
      .. math::
         &(1,2,3) \text{ og } (2,4,6) \\
         &(0,2,1) \text{ og } (1,4,2) \\
         &(0,-1,0) \text{ og } (0,4,0) \\
         &(1,2,3) \text{ og } (2,3,4) \\
         &(1,1,1) \text{ og } (7,7,7)

Hér er að lokum setning sem segir að ekki sé hægt að skrifa gefinn vigur sem
línulega samantekt óháðra vigra á fleiri en einn veg. Við breytum aðeins
útaf venjunni, að sleppa sönnunum, og látum sönnun á þessari fylgja.

.. admonition:: Setning: Einkvæmni línulegra samantekta
   :class: regla

   Ef :math:`x_1`,..., :math:`x_k` eru línulega óháðir og
    
   .. math::
      y &= c_1 x_1 + \ldots + c_k x_k \\
      &= d_1 x_1 + \ldots + d_k x_k \\

   þá er :math:`c_i = d_i` fyrir öll :math:`i`.

.. admonition:: Sönnun setningar
   :class: regla

   Gerum ráð fyrir að :math:`y = c_1 x_1 + \ldots + c_k x_k = d_1 x_1 + \ldots +
   d_k x_k`. Það má færa alla :math:`d`-liðina fram fyrir seinna jafnaðarmerkið
   og það gefur :math:`c_1 x_1 - d_1 x_1 + \ldots + c_k x_k - d_k x_k = 0`
   þ.e.a.s. :math:`(c_1 - d_1) x_1 + \ldots + (c_k - d_k) x_k = 0`. Þar sem
   :math:`x_i`-in eru línulega óháð þýðir þetta að allir samantektarstuðlarnir
   hljóta að vera 0, sem sé :math:`c_1 - d_1 = c_2 - d_2 = \ldots = c_k - d_k =
   0` sem gefur :math:`c_i = d_i` fyrir öll :math:`i`.

Grunnar og liðun
----------------

Grunnur (*basis*, fleirtala *bases*) er grunnhugtak í línulegri algebru.

.. admonition:: Skilgreining: Grunnur
   :class: regla

   **Grunnur** í :math:`n`-víðu rúmi er mengi af :math:`n` vigrum í rúminu,
   :math:`\{a_1, \ldots, a_n\}`, sem er línulega óháð.

Rúmið í skilgreiningunni getur verið :math:`\Bbb{R}^n` en það getur líka verið
svokallað hlutrúm, t.d. bein lína í gegn um :math:`(0,0)` í :math:`\Bbb{R}^2`
(sem er einvítt hlutrúm, :math:`n=1`) eða plan í gegn um :math:`(0,0,0)` í
:math:`\Bbb{R}^3`, eins og t.d. planið á myndinni í grein :numref:`línulega
háðir og óháðir vigrar` (tvívítt hlutrúm, :math:`n=2`).

Áður en við útskýrum mikilvægi hugtaksins grunnur setjum við fram
setningu um hámarksstærð línulega óháðra mengja, nefnilega:

.. admonition:: Setning: Hámarksstærð grunns
   :class: regla

   Ef :math:`a_1, a_2, \ldots, a_k` eru línulega óháðir vigrar
   :math:`n`-víðu rúmi þá er :math:`k \leq n`.

Línulega óháð mengi :math:`n`-vigra hefur sem sé í mesta lagi :math:`n` stök.
Setningin er bein afleiðing af velþekktri setningu í línulegri algebru sem
nefnist *mynd- og núllvíddarsetningin* (*rank-nullity theorem*), en það er líka
hægt að sanna hana beint með þrepun á :math:`n`, sem samt verður ekki gert hér.

Setningin segir til dæmis að þrír vigrar í plani hljóti að vera línulega háðir,
og sömuleiðis fjórir vigrar þrívíðu rúmi. Eftirfarandi mynd sýnir þrjá vigra í
:math:`\Bbb{R}^2`, :math:`x`, :math:`y` og :math:`z`, engir tveir samsíða.

.. figure:: myndir/mynd-og-núllvídd.png
   :align: center
   :figwidth: 5cm

   Línulega háðir vigrar

Á myndinni sést hvernig hægt er að skrifa einn vigurinn (nefnilega :math:`y`)
sem línulega samantekt af hinum tveimur, svo vigrarnir þrír eru línulega háðir.
Byrjað er á að teikna :math:`x` og :math:`z` út frá endunum á :math:`y` og svo
eru þeir framlengdir þar til þeir skerast. Það gildir greinilega að :math:`ax =
y + bz` svo :math:`y = ax - bz`. Ef einhverjir tveir vigranna væru samsíða þá
væru þeir, og þar með allir þrír, línulega háðir.

Snúum okkur á aftur að grunnum, og einni aðalsetningunni um þá, sem segir að
hægt sé að skrifa hvern vektor á einkvæman hátt sem línulega
samantekt af grunnvigrum. Sönnunin er auðveld og við látum hana fylgja.

.. admonition:: Regla: Einkvæmni grunnsamantektar
   :class: regla

   Sérhvern vigur :math:`b` í :math:`n`-víðu rúmi má rita sem línulega samantekt
   af grunni :math:`a_1, \ldots, a_n` fyrir rúmið á nákvæmlega einn veg.

.. admonition:: Sönnun: 
   :class: regla

   Skv. síðustu setningu er mengið :math:`\{a_1, \ldots, a_n, b\}`
   línulega háð svo til eru tölur :math:`c_i` og :math:`c` sem eru ekki allar
   núll, þannig að

   .. math::               
      c_1 a_1 + \ldots + c_n a_n + c b = 0

   :math:`c` getur ekki verið :math:`0` því þá væru einhver af :math:`c_i`-unum
   ekki 0 og með því væri komin línuleg samantekt af :math:`a_i`-unum sem er 0
   með samantektarstuðlum sem eru ekki allir 0, í mótsögn við að :math:`a_i`-in
   séu grunnur. Því má deila í gegn um jöfnuna með :math:`c` og það gefur:
    
   .. math::
      b = -\frac{c_1}{c}a_1 - \ldots - \frac{c_n}{c}a_n
      
   sem er línulega samantektin sem átti að búa til. Skv. setningunni aftast í
   grein :numref:`línulega háðir og óháðir vigrar` eru engar fleiri leiðir til að rita
   þessa samantekt.

Þegar vigur :math:`b` er skrifaður sem línuleg samantekt af grunnvigrum,

.. math::
   b = c_1 a_1 + \ldots + c_n a_n

er talað um **liðun** :math:`b` eða að :math:`b` hafi verið **liðaður**
með grunnvigrunum.

.. admonition:: Sýnidæmi: Sönnun á að vigramengi sé grunnur
   :class: synidaemi

   :math:`G = \{(1,1), (1,0)\}` er línulega óháð og hefur tvö stök og er þar með
   grunnur fyrir :math:`\Bbb{R}^2` því að ef

   .. math::
      c_1 \begin{pmatrix} 1\\1 \end{pmatrix} +
      c_2 \begin{pmatrix} 1\\0 \end{pmatrix} = 
      \begin{pmatrix} 0\\0 \end{pmatrix}

   þá er :math:`c_1 + c_2 = 0` og :math:`c_1 = 0` sem gefur :math:`c_1 = c_2 = 0`.

.. admonition:: Sýnidæmi: Liðun vigra
   :class: synidaemi
      
   Liðum tvo vigra með :math:`G` og notum smávegis mismunandi rithátt:

   1. :math:`\begin{pmatrix} 3\\2 \end{pmatrix} =
      c_1\begin{pmatrix} 1\\1 \end{pmatrix} +
      c_2\begin{pmatrix} 1\\0 \end{pmatrix}`
      gefur :math:`3 = c_1 + c_2` og :math:`2 = c_1`, þ.e.a.s. :math:`c_1 = 2` og
      :math:`c_2 = 1`.

   2. :math:`(-3,5) = \alpha(1,1) + \beta(1,0)` gefur :math:`\alpha = 5` og
      :math:`\beta = -8`, sem sé :math:`(-3,5) = 5(1,1) - 8(1,0)`.

.. admonition:: Æfing: Liðun vigra og sönnun á að mengi sé grunnur
   :class: aefing

   1. Liðið :math:`(5,4)` með grunnvigrunum :math:`(1,2)` og :math:`(2,1)`.
   2. Mynda vigrarnir :math:`(1,0,0)`, :math:`(0,1,0)` og
      :math:`(1,1,0)` grunn fyrir :math:`\Bbb{R}^3`? Rökstyðjið svarið.
   3. Hvað með :math:`(1,1,0)` og :math:`(1,2,0)`?
   4. En :math:`(1,0,0)`, :math:`(1,1,0)` og :math:`(1,1,1)`?

Venjulegir einingavigrar og grunnar þeirra
------------------------------------------

Vigur með lengdina 1 er kallaður **einingavigur** (*unit vector*). Í planinu
:math:`\Bbb{R}^2` eru vigrarnir :math:`(1,0)` og :math:`(0,1)`, sem stefna út
eftir :math:`x`-ás og :math:`y`-ás kallaðir **venjulegu einingavigrarnir**
(*standard unit vectors*) eða bara einingavigrarnir ef ekki er hætta á
misskilningi. Algengt er að tákna þessa vigra með :math:`e_1` og :math:`e_2` og
það verður gert hér (sjá :numref:`ein-vigrar` hér rétt fyrir neðan). Eftirfarandi skilgreining
útvíkkar þetta svo yfir í :math:`n`-vítt rúm.

.. admonition:: Skilgreining: Einingavigur
   :class: regla

   
   Vigur í :math:`\Bbb{R}^n` með :math:`i`-ta stak jafnt
   og :math:`1` og öll hin stökin :math:`0` er kallaður **(venjulegur)
   einingavigur** og táknaður :math:`e_i`.

.. admonition:: Sýnidæmi: Einingavigrar í :math:`\Bbb{R}^3`
   :class: synidaemi

   Í :math:`\Bbb{R}^3` eru þrír einingavigrar, nefnilega :math:`e_1 =
   (1,0,0)`, :math:`e_2 = (0,1,0)` og :math:`e_3 = (0,0,1)`.

Í :math:`\Bbb{R}^n` eru :math:`n` einingavigrar og það er ekki erfittð sanna
að þeir mynda grunn, :math:`G = \{e_1, \ldots, e_n\}` sem er kallaður **venjulegi
einingagrunnurinn** eða bara **einingagrunnurinn**. Það er sérstaklega auðvelt að
liða vigur með einingagrunnvigrunum. Ef :math:`x = (x_1, x_2, \ldots, x_n) \in
\Bbb{R}^n` þá gildir nefnilega:

.. math::
   x &= \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} =
        x_1 \begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix} +
        x_2 \begin{pmatrix} 0 \\ 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix} +
        \ldots +
        x_n \begin{pmatrix} 0 \\ \vdots \\ 0 \\ 1 \end{pmatrix} \\
     &= x_1 e_1 + x_2 e_2 + \ldots + x_n e_n

.. figure:: myndir/ein-vigrar.png
   :figwidth: 7cm
   :name: ein-vigrar
   :align: center
                    
   Venjulegu einingavigrarnir í :math:`\Bbb{R}^2` og liðun :math:`u = (2,3)` með þeim

.. admonition:: Æfing: Einingavigrar :math:`\Bbb{R}^4`
   :class: aefing

   1. Hver er venjulegi einingagrunnurinn fyrir :math:`\Bbb{R}^4`?
   2. Liðið :math:`(3,5,-1,2)` með honum.

Þverstaðlaðir grunnar
---------------------

Ef allir vigrar grunns eru hornréttir hver á annan er grunnurinn kallaður
**hornréttur** (*orthogonal*). Venjulegi einingagrunnurinn er hornréttur, og auk
þess eru allir vigrar hans með einingalengd því augljóslega gildir
:math:`\|e_i\| = 1` fyrir öll :math:`i`. Fleiri grunnar hafa þann eiginleika að
vera hornréttir og með vigra af einingalengd.

.. admonition:: Skilgreining: 
   :class: regla

   Grunnur :math:`\{a_1, \ldots, a_n \}` sem uppfyllir :math:`a_i \perp a_j`
   fyrir öll :math:`i \neq j` og :math:`\|a_i\| = 1` fyrir öll :math:`i` er
   kallaður **þverstaðlaður** (*orthonormal*) (stundum er notað orðið
   **einingaréttur**).

.. figure:: myndir/ein.réttir-vigrar.png
   :figwidth: 10cm
   :name: ein.réttir-vigrar
   :align: center

   Þverstaðlaður grunnur fyrir :math:`\Bbb{R}^2` og vigur sem hægt er
   að liða með honum. 
                    
Almennt er ekki auðvelt að finna liðun vigurs með tilteknum grunni, en í
síðustu grein sáum við að fyrir venjulega einingagrunninn er það
fyrirhafnarlaust. Með þverstöðluðum grunnum er það líka fremur einfalt
eins og eftirfarandi regla sýnir:

.. admonition:: Regla: Liðun með þverstöðluðum grunni
   :class: regla

   Ef :math:`\{a_1, \ldots, a_n\}` er þverstaðlaður grunnur og :math:`u` er
   :math:`n`-vigur þá gildir

   .. math::
      u = (a_1 \cdot u)a_1 + \ldots + (a_n \cdot u)a_n

Það er sem sé hægt að liða :math:`u` með grunnvigrunum :math:`a_1, \ldots, a_n` með
liðunarstuðlum sem gefnir eru með innfeldi þeirra og :math:`u`.

.. admonition:: Sýnidæmi: Þverstöðluð liðun
   :class: synidaemi

   Liðum vigurinn :math:`u = (2,3)` á :numref:`ein.réttir-vigrar` með
   :math:`a_1 = (\frac{\sqrt{3}}{2}, \frac{1}{2})` og
   :math:`a_2 = (-\frac{1}{2}, \frac{\sqrt{3}}{2})`.
   Við reiknum

   .. math::
      c_1 &= a_1 \cdot u = \frac{\sqrt{3}}{2} \cdot 2 + \frac{1}{2} \cdot 3 =
      \sqrt{3} + \frac{3}{2} \approx 3.232 \\
      c_2 &= a_2 \cdot u = -\frac{1}{2}\cdot 2 + \frac{\sqrt{3}}{2} \cdot 3
      = -1 + \frac{3}{2}\sqrt{3} \approx 1.598

   og þá gildir sem sé :math:`u = c_1 a_1 + c_2 a_2 \approx 3.232 a_1 + 1.598 a_2`

.. admonition:: Æfing: Sönnun á að mengi vigra sé þverstaðlaður grunnur
   :class: aefing

   1. Sýnið að vigrarnir :math:`a_1` og :math:`a_2` á
      :numref:`ein.réttir-vigrar` séu þverstaðlaður grunnur. Það þarf að sanna
      þrennt: (i) Að þeir séu grunnur, (ii) að þeir hafi einingalengd, og (iii)
      að þeir séu innbyrðis hornréttir.
   2. Sýnið að vigrarnir :math:`a_1 = (0.6, 0.8, 0)`, :math:`a_2 = (-0.8, 0.6,
      0)` og :math:`a_3 = (0, 0, 1)` gefi þverstaðlaðan grunn fyrir
      :math:`\Bbb{R}^3`.
   3. Liðið vigurinn :math:`(1,2,3)` með vigrunum í lið 2.

Reglan hér á undan gildir líka um þverstaðlaða vigra sem ekki spanna allt rúmið
í örlítið breyttri mynd.

.. admonition:: Regla: Liðun með mengi þverstaðlaðra vigra
   :class: regla

   Ef :math:`a_1, \ldots, a_k` eru þverstaðlaðir
   :math:`n`-vigrar með :math:`k < n` og :math:`u` er gefinn :math:`n`-vigur
   þá er hægt að skrifa :math:`u` sem línulega samantekt af :math:`a_1,\ldots,
   a_k` þ.þ.a.a.

   .. math::
      (*)\qquad\qquad u = (a_1 \cdot u)a_1 + \ldots + (a_k \cdot u)a_k
      \qquad\qquad{ }

Þessi regla gefur okkur sem sé aðferð til að kanna hvort tiltekinn vigur sé í
rúminu sem gefnir þverstaðlaðir vigrar spanna. Við tökum eftir að *þá*-hluti
setningarinnar er augljós, sem sé að ef :math:`(*)` gildir þá sé :math:`u`
línuleg samantekt af :math:`a_i`-unum, en hin áttin (*því-aðeins*\ -parturinn)
mundi þurfa smá sönnun.

.. admonition:: Sýnidæmi: Er punktur í gefnu plani?
   :class: synidaemi

   Vigrarnir :math:`a = (0.48, 0.64, 0.60)` og :math:`b = (0.8, -0.6, 0)` eru
   þverstaðlaðir (*Æfing: Sýnið það*) og skilgreina plan í :math:`\Bbb{R}^3`:

   .. math::
      P = \{x = s a + t b \, \| \, s,t \in \Bbb{R} \}

   1. Könnum hvort punkturinn :math:`A = (4, 2, 3)` sé í planinu með síðustu
      reglu. Við reiknum :math:`c_1 = A\cdot a = 4\cdot 0.48 + 2\cdot 0.64 + 3
      \cdot 0.6 = 5` og :math:`c_2 = A\cdot b = 4\cdot 0.8 - 2\cdot 0.6 = 2` og í
      framhaldi :math:`5a + 2b = (2.4, 3.2, 3) + (1.6, -1.2, 0) = (4, 2, 3)`.
      Þar sem útkoman er :math:`A` er niðurstaðan sú að :math:`A` er í planinu.
   2. Könnum með sama hætti punktinn :math:`B = (6, 3, 2)`. Við reiknum
      :math:`c_1 = 6`, :math:`c_2 = 3` og :math:`6a + 3b = (5.28, 2.04, 3.6)`.
      Útkoman er ekki :math:`B` svo :math:`B` er ekki í planinu.

Þverstaðlaðir grunnar eru náskyldir svonefndum hornréttum fylkjum og QR-þáttun,
sem vonandi kemst á dagskrá síðar í þessum fyrirlestranótum. Slík þáttun nýtist
í fjölbreyttum verkefnum í reiknifræði, t.d.:

   lausn línulegra jöfnuhneppa (*solution of linear equations*) |br|
   minnstu kvaðrata verkefnum (*ordinary least squares problems*) |br|
   eigingildisverkefnum (*eigenvalue problems*) og |br|
   kvaðratískri bestun (*quadratic programming*)

en lausn slíkra reiknifræðilegu verkefna nýtist aftur í fjölbreyttum verkefnum í
gagnavísindum, verkfræði og raunvísindum.

Línulegar samantektir, jöfnuhneppi og tilvist lausna
----------------------------------------------------
Áður en lengra er haldið ætti lesandi að skoða `kafla 11.3
<https://cs.hi.is/python/kafli11/#lausn-jofnuhneppa>`_ í Fyrirlestrarnótum um
Python, sem fjallar um lausn jöfnuhneppa.

Smá umhugsun leiðir í ljós að margföldun fylkis og vigurs jafngildir því að taka
línulega samantekt af dálkum fylkisins með samantektarstuðlum sem eru
stök vigursins. Hér er talnadæmi, en reglan gildir greinilega almennt:

.. math::
   \begin{pmatrix}
   2 & 3 & 4 \\
   1 & 0 & 2
   \end{pmatrix}
   \begin{pmatrix} 5 \\ 6 \\ 7 \end{pmatrix} &=
   5 \begin{pmatrix} 2 \\ 1 \end{pmatrix} + 
   6 \begin{pmatrix} 3 \\ 0 \end{pmatrix} +
   7 \begin{pmatrix} 4 \\ 2 \end{pmatrix}\\
   &=
   \begin{pmatrix} 10 \\ 5 \end{pmatrix} +
   \begin{pmatrix} 18 \\ 0 \end{pmatrix} +
   \begin{pmatrix} 28 \\ 14 \end{pmatrix} =
   \begin{pmatrix} 56 \\ 19 \end{pmatrix}

Af þessu leiðir er það að leysa jöfnuhneppið :math:`Ax = b` jafngildir því að
finna stuðla þar sem :math:`b` er skrifað sem línuleg samantekt af dálkum
:math:`A`. Við höfum séð að þetta er hægt á nákvæmlega einn veg ef dálkar
fylkisins eru línulega óháðir og mynda grunn fyrir :math:`\Bbb{R}^n`. Ef
dálkarnir eru línulega háðir þá er oftast engin lausn, en ef hún er til þá eru
til óendanlega margar lausnir.

.. admonition:: Setning: Jöfnuhneppi með einkvæma lausn
   :class: regla

   :math:`n \times n` jöfnuhneppi :math:`Ax = b` hefur nákvæmlega eina lausn
   þ.þ.a.a. dálkar fylkisins séu grunnur fyrir :math:`\Bbb{R}^n`. Annars er
   annaðhvort engin eða óendanlega margar lausnir.
   
Skoðum dæmi, nefnilega lausn á jöfnuhneppinu

.. math::
   x + 2y &= 3 \\
   2y + z &= 2 \\
   x - z &= 0

Hér er auðvelt að sjá, með því að draga jöfnu 2 frá jöfnu 1, að :math:`x - z =
1`, en hó, síðasta jafnan segir að :math:`x - z = 0` svo eitthvað verður erfitt
að leysa þetta hneppi, augljóst er að það hefur enga lausn. Fylki
jöfnuhneppisins er

.. math::
   \begin{pmatrix}
   1 & 2 & 0 \\
   0 & 2 & 1 \\
   1 & 0 & -1
   \end{pmatrix}

og fyrsti dálkurinn er hálfur miðdálkurinn mínus sá aftasti, :math:`(1, 0, 1)` =
:math:`\frac{1}{2}(2, 2, 0) - (0, 1, -1)`, svo dálkarnir eru línulega háðir. Ef
við breytum síðustu jöfnunni í :math:`x - z = 1` þá er fylkið óbreytt og nú
bregður svo við að það er til lausn, nefnilega :math:`x = 1, y = 1, z = 0`. En
það eru til fleiri lausnir, t.d. :math:`x = 2, y = \frac{1}{2}, z = 1` og :math:`x
= 3, y = 0, z = 2`, og samkvæmt setningunni að framan eru þær óendanlega margar.

Ferningsfylki með línulega háða dálka er kallað **sérstætt** (*singular*) en ef
dálkarnir eru línulega óháðir er fylkið kallað **andhverfanlegt** (*non-singular*).

Hér er svo setning sem sem segir að við getum alveg eins skoðað línur fylkis
eins og dálka þess til að finna út hve margar lausnir jöfnuhneppi hefur:

.. admonition:: Setning: Dálkar, línur og grunnar
   :class: regla

   Línur ferningsfylkis eru grunnur þ.þ.a.a. dálkar fylkisins séu grunnur

.. admonition:: Æfing: Jöfnuhneppi og grunnar
   :class: aefing

   1. Leysið jöfnuhneppið

      .. math::
         &x  + y\;+  &z\;&= 6 \\
         2&x + y  + 2&z\;&= 10 \\
         3&x + y\;+  &z\;&= 8

      með því að byrja á að draga fyrstu jöfnuna tvöfalda frá annarri jöfnunni
      og þrefalda frá þeirri þriðju. Eru vigrarnir :math:`(1,1,1)`,
      :math:`(2,1,2)` og :math:`(3,1,1)` grunnur? Rökstyðjið.

   2. Sýnið að vigrarnir :math:`(1, 2, 3)`, :math:`(1, 1, 1)` og :math:`(3, 4, 5)`
      séu línulega háðir (með því að skrifa einn þeirra sem línulega
      samantekt af hinum tveimur).

   3. Búið til jöfnuhneppi úr vigrunum í lið 2 sem hefur enga lausn.

   4. Búið til jöfnuhneppi úr sömu vigrum sem hefur óendanlega margar lausnir.

.. admonition:: Python: 
   :class: python

   Þó að jöfnuhneppi hafi enga stærðfræðilega lausn getur það gerst að NumPy
   finni lausn sem er með mjög stórum tölum, en stundum gefur það villumeldingu
   og segir :code:`LinAlgError: Singular matrix`.

.. admonition:: Æfing: Sérstætt jöfnuhneppi
   :class: aefing

   Prófið að nota NumPy til að leysa jöfnuhneppi :math:`Ax =
   \begin{pmatrix}1\\1\end{pmatrix}` með
   :math:`A = \begin{pmatrix}1&2\\5&10\end{pmatrix}` annarsvegar og
   :math:`A = \begin{pmatrix}1&2\\2&4\end{pmatrix}` hinsvegar.

Þegar NumPy þykist geta leyst jöfnu sem hefur enga lausn er það vegna tölulegrar
ónákvæmni í reikningum: NumPy reiknar ekki með óendanlega mörgum aukastöfum.

.. admonition:: Python: 
   :class: python

   Til að sjá hvort fylki sé tölulega sérstætt er hægt að nota fallið
   :code:`la.matrix_rank`, en það skilar **myndvídd** (*rank*) fylkisins, sem er
   vídd rúmsins sem dálkar þess spanna, að teknu tilliti til tölulegrar óvissu.
   Ef dálkar :math:`n`-dálka fylkis eru u.þ.b. línulega háðir skilar
   :code:`matrix_rank` tölu sem er minni en :math:`n`.

.. admonition:: Æfing: Myndvídd
   :class: aefing

   Reiknið myndvídd fylkisins :math:`\begin{pmatrix}1&2\\5&10\end{pmatrix}` með
   NumPy. Prófið líka að reikna myndvíddina ef stakinu :code:`5` er breytt í
   :code:`5 + 1e-15`, :code:`5 + 1e-14` og :code:`5 + 1e-13`.
         
Fylkjaalgebra
-------------
Hér að framan og í `11. kafla
<http://https://cs.hi.is/python/kafli11/#reikna-me-fylkjum>`_ í Python
fyrirlestrarnótunum höfum við séð ýmsar aðgerðir og reglur tengdar vigrum og
fylkjum sem minna á sambærilegar aðgerðir og reglur fyrir tölur: samlagningu
vigra, innfeldi, margföldun fylkis og vigurs, víxlreglur, tengireglur og
dreifireglur.

Umfjöllun um aðgerðir og reglur af slíku tagi tilheyrir undirgrein
stærðfræði sem kölluð er algebra. Stundum koma við sögu hugtök eins og
samlagningarandhverfa (*additive inverse*), margföldunarandhverfa
(*multiplicative inverse*), núllstak (*null element*) og einingarstak (*identity
element*), og um sum þessara hugtaka var talað í fyrrnefndum 11. kafla. Hér
verður umfjöllunin þar dýpkuð dálítið, þó án þess að farið verði út í nákvæma
stærðfræðilega umfjöllun.

Smávegis skoðun á fylkjaalgebru getur samt hjálpað til við að skilja fylki betur
og við byrjum á að rifja upp nokkur atriði úr köflum `11.1
<https://cs.hi.is/python/kafli11/#grunnreikniagerir>`_, `11.2
<https://cs.hi.is/python/kafli11/#nullfylki-og-einingafylki>`_ og `11.5
<https://cs.hi.is/python/kafli11/#andhverfur-og-akveur>`_ í Fyrirlestrarnótum um
Python.

.. admonition:: Skilgreining: Fylkjamargföldun
   :class: regla

   **Margfeldi** :math:`m \times p` fylkis :math:`A` og
   :math:`p \times n` fylkis :math:`B` er :math:`m \times n` fylkið
   :math:`C = AB` sem hefur :math:`(i,j)`-stak

   .. math::
      c_{ij} = \sum_{k=1}^p a_{ik} b_{kj}

.. admonition:: Sýnidæmi: Margfeldi fylkja
   :class: synidaemi

   Reiknum margfeldi tveggja :math:`2 \times 2` fylkja :math:`A` og :math:`B`: 

   .. math::
      \begin{pmatrix}1 & 2 \\ 3 & 4 \end{pmatrix}
      \begin{pmatrix}5 & 6 \\ 0 & -2 \end{pmatrix}

   og fáum :math:`c_{11} = 1 \cdot 5 + 2 \cdot 0 = 5`, :math:`c_{12} = 1 \cdot 6
   - 2 \cdot 2 = 2`, :math:`c_{21} = 3 \cdot 5 + 4 \cdot 0 = 15` og
   :math:`c_{22} = 3 \cdot 6 - 4 \cdot 2 = 10`, sem sé

   .. math::
      C = \begin{pmatrix}5 & 2 \\ 15 & 10 \end{pmatrix}

Skoðun á skilgreiningunni að framan sýnir að :math:`j`-ti dálkur :math:`C` fæst
með því að margfalda saman :math:`A` og :math:`j`-ta dálk :math:`B`, og
það er líka hægt að segja að :math:`c_{ij}` sé innfeldi af :math:`i`-tu línu
:math:`A` og :math:`j`-ta dálki :math:`B`.

.. admonition:: Sýnidæmi: Dálkar margfaldaðir hver fyrir sig
   :class: synidaemi

   (framhald af síðasta sýnidæmi) Margföldun A og fyrri dálks B gefur

   .. math::
      \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}
      \begin{pmatrix} 5\\0 \end{pmatrix} = \begin{pmatrix} 5\\15 \end{pmatrix}

   og innfeldi neðri línu :math:`A` og seinni dálks :math:`B` er

   .. math::
      \begin{pmatrix} 3, 4 \end{pmatrix} \cdot 
      \begin{pmatrix} 6, -2 \end{pmatrix} = 10
      
.. admonition:: Python: 
   :class: python

   Í NumPy fæst margfeldi ``A`` og ``B`` með ``A @ B``.

.. admonition:: Skilgreining: Núllfylki og einingafylki
   :class: regla

   **Núllfylki** (*zero matrix*) hefur öll stök = 0 og **einingafylki**
   (*identity matrix*) hefur hornalínustökin = 1 og öll önnur stök = 0.

Einingafylki er oftast táknað með :math:`I` og stærð þess ræðst yfirleitt af samhenginu. Núllfylki eru stundum táknuð með :math:`0` eða :math:`O` (núll eða bókstafurinn O), og stærðin ræðst líka af samhenginu.

**DÆMI.** |sp| Hér eru :math:`2 \times 2` og :math:`3 \times
3` einingafylki og :math:`2 \times 3` núllfylki:

.. math::
   \begin{pmatrix}1 & 0 \\ 0 & 1 \end{pmatrix} \quad
   \begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \quad
   \begin{pmatrix}0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}

.. admonition:: Python: 
   :class: python

   Í NumPy má búa til :math:`m \times n` núllfylki með :code:`np.zeros((m,n))`
   og :math:`n \times n` einingafylki með :code:`np.identity(n)` eða
   :code:`np.eye(n)` (*eye* er borið fram eins og *I* ).

.. _reglur-um-fylkjamargföldun:
         
Ef :math:`A` og :math:`B` eru jafn stór er hægt að leggja þau saman og ef dálkar
:math:`A` eru jafnmargir og línur :math:`B` er hægt að reikna margfeldið
:math:`AB`. Við segjum þá að fylkin hafa samræmdar (*compatible*) víddir.
Eftirfarandi reglur gilda um fylki með samræmdar víddir:

.. admonition:: Reglur um fylkjasamlagningu og -margföldun 
   :class: regla
   
   .. math::
      &A + B = B + A             &\text{(víxlregla samlagningar)} \\
      &A+(B+C) = (A+B)+C         &\text{(tengiregla samlagningar)} \\
      &A(BC) = (AB)C             &\text{(tengiregla margföldunar)} \\
      &A(B + C) = AB + AC        &\text{(dreifiregla)} \\
      &A + O = O + A = A         &\text{(regla um samlagningarhlutleysu)} \\
      &OA = AO = O               &\text{(regla um margföldun með núllfylki)} \\
      &IA = AI = A               &\text{(regla um margföldunarhlutleysu)}

Síðustu tvær reglurnar gilda líka um vigra: :math:`Ox = 0`
(núllvigurinn) og :math:`Ix = x` fyrir alla :math:`n`-vigra :math:`x`.   

Allar reglurnar gilda líka um tölur, með margföldunarhlutleysu 1 og
samlagningarhlutleysu 0. Eina venjulega talnareglan sem ekki gildir um
fylkjamargföldun er víxlreglan: Almennt er :math:`AB \neq BA`. Prófum til dæmis
að margfalda saman fylkin í sýnidæminu fremst í þessum kafla í öfugri röð miðað
við þar:

.. math::
   \begin{pmatrix}5 & 6 \\ 0 & -2 \end{pmatrix}
   \begin{pmatrix}1 & 2 \\ 3 & 4 \end{pmatrix} =
   \begin{pmatrix}23 & 34 \\ -6 & -8 \end{pmatrix},

sem sé allt annað fylki en :math:`C`-ið sem þar fékkst.

.. admonition:: Æfing: Fylkjareikningur í Python
   :class: aefing

   Búið til þrjú :math:`2 \times 2` handahófsfylki í NumPy
   með eftirfarandi skipunum:

   .. code:: python3

      import numpy as np, numpy.random as npr
      A = npr.rand(2,2)
      B = npr.rand(2,2)
      C = npr.rand(2,2)

   Bætið svo við skipunum til að búa til núll- og einingafylki, og
   sannreynið nokkrar af reglunum hér að ofan.

Í algebru gegna andhverfur mikilvægu hlutverki. Samlagningarandhverfa fylkis :math:`A` er fylkið :math:`-A` sem fæst með því að snúa við formerkjum allra staka :math:`A`. Um hana gildir að ef hún er lögð við A fæst samlagningarhlutleysan:

.. admonition:: Regla um samlagningarandhverfu
   :class: regla

   .. math::
      A + (-A) &= O \\
      (-A) + A &= O

Margföldunarandhverfa fylkis er mikilvægara hugtak og oftast kallað einfaldlega
andhverfa þess. Hér aðeins framar skilgreindum við andhverfanleg og sérstæð (=
ekki andhverfanleg) fylki. Andhverfanlegt fylki á sér andhverfu sem gefur
einingafylkið (margföldunarhlutleysuna) þegar upphaflega fylkið er margfaldað
með henni:

.. admonition:: Regla um (margföldunar)andhverfu fylkis
   :class: regla

   Ef A er andhverfanlegt (ekki sérstætt) þá er til fylki táknað :math:`A^{-1}`
   þannig að:

   .. math:: AA^{-1} = A^{-1}A = I

Eins og útskýrt er í kafla `11.5
<https://cs.hi.is/python/kafli11/#andhverfur-og-akveur>`_ í Python
fyrirlestrarnótunum er hægt að leysa jöfnuhneppi

.. math::
   Ax = b

með því að margfalda í gegn með :math:`A^{-1}`:

.. math::
   A^{-1}Ax &= A^{-1}b\\
   Ix       &= A^{-1}b\\
   x        &= A^{-1}b

Þar er líka lögð áhersla á að í praktískum reikningum í tölvu eigi frekar að
kalla á föll sem leysa jöfnuhneppi en að finna andhverfur og margfalda með þeim.

.. admonition:: Python: 
   :class: python

   Ef maður vill engu að síður reikna andhverfu fylkis ``A`` í NumPy má nota
   ``inv(A)``.

Þrjár gagnlegar og skemmtilegar reglur gilda um byltingu og andhverfu margfeldis
tveggja fylkja:

.. admonition:: Reglur um byltingu og andhverfu
   :class: regla
   
   .. math:: 
      (AB)^\text{T} &= B^\text{T}A^\text{T}\\
      (AB)^{-1}     &= B^{-1}A^{-1}\\
      (A^\text{T})^{-1} &= (A^{-1})^\text{T}

Fyrri tvær reglurnar segja að ef svigarnir eru teknir burtu víxlast röð
:math:`A` og :math:`B`, og það gildir sem sé bæði um byltingu og andhverfu.
Síðasta reglan segir svo að andhverfa af byltu fylki sé jöfn byltri andhverfu,
og fyrir vikið er niðurstaðan stundum táknuð :math:`A^{-\text{T}}`. Hér verða
ekki gefin mörg dæmi um notkun þessara reglna, en þeir sem lesa meira um
línulega algebru og tengd fræði munu rekast á notkun þeirra aftur og aftur.

.. admonition:: Æfing: Andhverfur og bylting
   :class: aefing
   
   Sannreynið þessar reglur með NumPy (bylt fylki :code:`A` fæst
   með :code:`A.T`).

.. _línulegar-varpanir:
   
Línulegar varpanir og fylkjamargföldun
--------------------------------------

.. _skilgreining-á-línulegri-vörpun:

Rifjum upp úr grein :numref:`línuleg föll og innfeldi` að línulegt fall er
fall frá :math:`\Bbb{R}^n \to \Bbb{R}` sem varðveitir samlagningu og margföldun
með tölu. Hér skoðum við hinsvegar varpanir sem senda vigra yfir í aðra vigra,
en eins og sagt var í fremst í kafla :numref:`línuleg föll og innfeldi` þá er
oft talað um vörpun (*map*) frekar en fall (*function*) þegar varpmengið er
:math:`\Bbb{R}^m` en ekki :math:`\Bbb{R}`.

.. admonition:: Skilgreining: Línuleg vörpun
   :class: regla

   Vörpun :math:`f: \Bbb{R}^n \to \Bbb{R}^m` kallast **línuleg** ef

   .. math::
      &f(x + y) = f(x) + f(y)\;\;\text{fyrir öll}\;x,y \in \Bbb{R}^n\;\;\text{og}\\
      &f(ax) = af(x)\;\;\text{fyrir öll}\;a \in \Bbb{R}\;\text{og}\; x\in\Bbb{R}^n
   
Við sjáum að skilgreiningin er samhljóða skilgreiningu á línulegu falli. Hægt er
að líta á línulega vörpun sem safn af :math:`m` línulegum föllum. Næsta sýnidæmi
sýnir þetta vel. Í síðasta sýnidæminu í grein :numref:`línuleg föll og innfeldi`
var búið til fall fyrir sig brúar í miðjunni. Ef sigið er skoðað í mörgum
punktum verður fallið að vörpun.

.. admonition:: Sýnidæmi: Sig brúar á mörgum stöðum
   :class: synidaemi

   Á brú verkar kraftar :math:`w_1, w_2` og :math:`w_3` (þyngdir bíla í tonnum)
   á þremur gefnum stöðum. Þeir valda því að brúinn sígur um :math:`s_1, s_2,
   s_3` og :math:`s_4` millimetra á öðrum fjórum gefnum stöðum.

   .. figure:: myndir/bru3.png
      :figwidth: 12cm
      :align: center

   Samband :math:`s` og :math:`w` er gefið með línulegri vörpun
   :math:`s = \operatorname{sig}(w)` sem rita mætti:

   .. math::
      s_1 &= c_{11} w_1 + c_{12} w_2 + c_{13} w_3\\
      s_2 &= c_{21} w_1 + c_{22} w_2 + c_{23} w_3\\
      s_3 &= c_{31} w_1 + c_{32} w_2 + c_{33} w_3\\
      s_4 &= c_{41} w_1 + c_{42} w_2 + c_{43} w_3
      
   Sambandið má líka setja fram með fylkjamargföldun:

   .. math::
      s = Cw
      
   Eins og í sýnidæminu í kafla :numref:`línuleg föll og innfeldi` mætti ákvarða
   stuðlana :math:`c_{ij}` annaðhvort með burðarþolsfræðireikningum eða með
   mælingum.

Í sýnidæminu hér á undan var hægt að rita línulegu vörpunina sem margföldun með
fylki og það gildir raunar um allar línulegar varpanir. Sömuleiðis gildir að
margföldun fylkis og vigurs gefur alltaf línulega vörpun:

.. admonition:: Setning: Línuleg vörpun er margföldun með fylki
   :class: regla

   Ef :math:`f` er línuleg vörpun, :math:`f:\Bbb{R}^n \to \Bbb{R}^m`
   þá er til :math:`m \times n` fylki :math:`C` þannig að :math:`f(x) = Cx` fyrir
   öll :math:`x`. :math:`C` er kallað *fylki vörpunarinnar* :math:`f`.

.. admonition:: Setning: Fylki sinnum vigur gefur línulega vörpun
   :class: regla

   Ef :math:`C` er :math:`m \times n` fylki og :math:`f` er vörpun sem
   skilgreind er með :math:`f(x) = Cx` þá er :math:`f` línuleg.

.. admonition:: Æfing: Línulegar varpanir og fylki
   :class: aefing

   1. Hvert er fylki vörpunarinnar :math:`f(x) = (3x_1 - 2x_2, x_1 - x_2)`?
   2. Línuleg vörpun hefur fylki

      .. math::
         \begin{pmatrix}2 & 3\\ 1 & 1\end{pmatrix}

      Reiknið :math:`f([2,4])`.
   3. Lýsið mælingum sem mætti gera til að ákvarða fylkið :math:`C` í
      sýnidæminu um brúna.

Hægt er að setja saman línulegar varpanir á sama hátt og önnur föll.

.. admonition:: Skilgreining: Samsett línuleg vörpun
   :class: regla

   Ef :math:`g` er línuleg vörpun frá :math:`\Bbb{R}^n` yfir í :math:`\Bbb{R}^p`
   og :math:`f` er línuleg vörpun frá :math:`\Bbb{R}^p` yfir í
   :math:`\Bbb{R}^m`:

   .. math::
      \Bbb{R}^n \underset{\large{g}} \longrightarrow \Bbb{R}^p
      \underset{\large{f}} \longrightarrow \Bbb{R}^m,

   þá er samsetta vörpunin :math:`f \circ g` skilgreind með:

   .. math::
      h(x) = (f \circ g)(x) = f(g(x)) \quad \text{fyrir öll }x \in \Bbb{R}^n

Auðvelt er að sjá að :math:`h` er línuleg vörpun frá :math:`\Bbb{R}^n` til
:math:`\Bbb{R}^m`. Ekki er heldur mjög erfitt að sýna að fylki samsettrar
línulegrar vörpunar fæst með því að margfalda saman fylki varpananna hvorrar
fyrir sig:

.. admonition:: Setning: Fylki samsettrar vörpunar 
   :class: regla

   Ef :math:`f` er vörpun með fylki :math:`A` og :math:`g` er vörpun með fylki
   :math:`B` þá er fylki :math:`f \circ g` gefið með :math:`C = AB`.

.. admonition:: Sýnidæmi: Sig brúar í þriðja sinn
   :class: synidaemi

   .. figure:: myndir/bru3.png
      :figwidth: 12cm
      :align: center

   Lítum aftur á brúna úr fyrri dæmum. Togið í vírunum fjórum sem halda
   henni uppi er mjög líklega línulega háð sigi brúarinnar á stöðunum sem
   merktir eru :math:`s_1, s_2, s_3` og :math:`s_4`, :math:`t =
   \operatorname{tog}(s)`, t.d. með fylki :math:`T`:

   .. math::
      t = \operatorname{tog}(s) = Ts

   Svo væri hægt að reikna togið beint út frá þyngdum bílanna, :math:`w`, með
   samsettu vörpuninni :math:`\operatorname{tog} \circ \operatorname{sig}`, með fylki
   :math:`S = TC`:

   .. math::
      t = \begin{pmatrix} t_1 \\ t_2 \\ t_3 \\ t_4 \end{pmatrix} =
      Sw = TCw = TC \begin{pmatrix} w_1 \\ w_2 \\ w_3 \end{pmatrix}

.. admonition:: Æfing: Stærð brúarfylkis og togfylkis
   :class: aefing

   Hve stór eru fylkin :math:`C`, :math:`T` og :math:`S` í sýnidæminu hér á
   undan?

.. admonition:: Athugasemd: 
   :class: athugid

   Myndavarpanirnar sem fjallað er um í kafla `12.1
   <https://cs.hi.is/python/kafli12/#fylkjamargfoldun-og-tolvugrafik>`_ í
   Fyrirlestrarnótum um Python eru dæmi um línulegar varpanir. Kaflinn talar
   líka um að fylkjamargföldun svari til samsetningar varpana, og gefur ágæt
   dæmi um hagnýtingu þeirrar staðreyndar.
