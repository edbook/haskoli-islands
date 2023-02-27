.. include:: rst-include

Reiknað með fylkjum
===================

**Línuleg algebra** (*linear algebra*) er undirgrein stærðfræði sem fjallar meðal annars um vigra og fylki, vigurrúm (*vector spaces*), línuleg jöfnuhneppi (*systems of linear equations*) og línuleg föll. Hægt er að beita línulegri algebru bæði fræðilega og tölulega, og þegar það er gert tölulega koma fylkjareikningar oftar en ekki við sögu, og þá er NumPy ómissandi. Oft tengjast reikningarnir því að vigrar og fylki eru notuð til að vinna með talnagögn (*data*).

Í nýlegri kennslubók um línulega algebru eru talin upp fjölbreytt
notkunarsvið hennar, svo sem leikjafræði, skógrækt, tölvugrafík, sneiðmyndatöku,
dulmálsfræði, erfðafræði, stofnstærðarspár, líkön af heyrn, netleit og andlitskennsl.

Í :numref:`%s. kafla<Dæmi um hagnýtingu fylkjareikninga>` verður fjallað um nokkur notkunarsvið fylkjareikninga, en í þessum kafla höldum við okkur að mestu við útskýringar á NumPy vigur- og fylkjaaðgerðum, og hvernig hægt er að leysa jöfnuhneppi með NumPy.

.. _samlagning-fylkja:

Grunnreikniaðgerðir
-------------------
Í grein :numref:`reiknað-með-vigrum` var rætt hverning hægt er að leggja saman tvo vigra, draga annan frá hinum og margfalda vigur með tölu. Þessum aðgerðum má líka beita á fylki, og þá verka þær á tilsvarandi stök, eins og fyrir vigrana. Þannig gildir:

.. math::
   \begin{pmatrix}1 & 2\\3 & 4\end{pmatrix} +
   \begin{pmatrix}2 & 2\\5 & 5\end{pmatrix} =
   \begin{pmatrix}3 & 4\\8 & 9\end{pmatrix}

og

.. math::
   2\cdot\begin{pmatrix}2 & 2\\5 & 6\end{pmatrix} =
   \begin{pmatrix}4 & 4\\10 & 12\end{pmatrix}

.. admonition:: Python: Stakvísar fylkjaaðgerðir
   :class: python

   Í Python eru venjulegu reikniaðgerðirnar, :math:`+` :math:`-` og :math:`*`
   notaðar til að reikna með öllum stökum fylkis samtímis, og auk þess má beita
   :math:`*` til að margfalda saman tvö fylki sem gefur það stærðfræðilega
   óvenjulega svar að tilsvarandi stök eru margfölduð saman. Og eins og hægt var
   með vigrana er líka hægt að beita stærðfræðiföllum stakvíst á fylki með því
   að nota ``np.``-útgáfur af þeim í staðinn fyrir að nota math-eininguna.

.. admonition:: Sýnidæmi: Stakvís margföldun og logri
   :class: synidaemi

   Ef eftirfarandi forritsbútur er framkvæmdur:

   .. code:: Python

      A = np.array([[1,2],
                    [3,4]])
      B = np.array([[1,  10  ],
                    [100,1000]])
      C = A*B
      print(C)
      print(np.log10(B))

   þá prentast út:

   .. code:: text
             
      [[   1   20]
       [ 300 4000]]
      [[0. 1.]
       [2. 3.]]             

Eins og fyrr segir er það óvenjulegt í stærðfræði að margföldun með fylkjum sé
framkvæmd stakvís. Í línulegri algebru er slík margföldun nefnilega skilgreind
sem útvíkkun á innfeldi og felur í sér margföldun staka og samlagningu í
kjölfarið. Þetta á bæði við um margföldun fylkis og vigurs og margföldun tveggja
fylkja.

.. admonition:: Skilgreining: Margföldun fylkis og vigurs
   :class: regla
           
   Ef :math:`A` er :math:`m \times n` fylki og :math:`x` er :math:`n`-vigur þá
   er margfeldi :math:`A` og :math:`x`, táknað :math:`Ax` eða :math:`A \cdot x`,
   :math:`m`-vigur með :math:`i`-ta stak jafnt og innfeldi :math:`i`-tu línu
   :math:`A` og :math:`x`. Nánar tiltekið gildir að

   .. math::
      \text{ef}\;y = Ax\;\text{þá er}\;y_i = \sum_{j=1}^n a_{ij}x_j\;\:(i=1,...,m)

.. admonition:: Sýnidæmi: Fylki sinnum vigur handreiknað
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

Stundum er gerður greinarmunur á dálkvigri (*column vector*) og línuvigri (*row
vector*), t.d. :math:`\begin{pmatrix}1\\2\end{pmatrix}` og :math:`(1, 2)`. Þegar
:math:`x` og :math:`y` eru báðir dálkvigrar þá er innfeldið :math:`x \cdot y`
stundum táknað með :math:`x^\text{T}y`. Þá er nefnilega :math:`x^\text{T}`
línuvigur og ef við lítum á hann sem :math:`1 \times n` fylki þá er margfeldi
þess og vigursins :math:`y` einmitt jafnt og innfeldið :math:`x\cdot y`.

.. admonition:: Reglur: Dreifireglur
   :class: regla

   Um margfeldi fylkja og vigra gilda dreifireglurnar

   .. math::
      &A(x + y) = Ax + Ay\;\:\text{og}\\
      &(A + B)x = Ax + Bx

   þar sem :math:`A` og :math:`B` eru fylki og :math:`x` og :math:`y` vigrar.
   Hér má setja :math:`-` í stað :math:`+`.

.. admonition:: Python: @-virkinn
   :class: python

   Í **NumPy** fæst margfeldi fylkis og vigurs með aðgerðinni **@**, t.d.
   reiknar ``y = A @ x`` margfeldi fylkisins A og vigursins x.

.. admonition:: Æfing: Reiknað með Python
   :class: aefing

   Gefnir eru vigrarnir :math:`a = (2, 0, 3)`, :math:`b = (1, -1, 2)` og :math:`c
   = (1, 2, 3)` og fylkin

   .. math::
      A = \begin{pmatrix}1 & 2\\3 & 3\\1 & 4\end{pmatrix}\;\text{og}\;
      B = \begin{pmatrix}2 & 3 & 0\\1 & 2 & 3\end{pmatrix}

   Reiknið með NumPy:
   
   1. :math:`a + b + c`
   2. :math:`3a - 2b`
   3. :math:`a\cdot b`
   4. :math:`Bc`
   5. :math:`A^\text{T}a`
   6. :math:`2A + B^\text{T}`
      
.. admonition:: Skilgreining: Fylkjamargföldun
   :class: regla

   Margfeldi :math:`m \times p` fylkis :math:`A` og :math:`p \times n` fylkis
   :math:`B` er :math:`m \times n` fylkið :math:`C = AB` sem hefur
   :math:`(i,j)`-stak

   .. math::
      c_{ij} = \sum_{k=1}^p a_{ik} b_{kj}

Samkvæmt skilgreiningunni fæst :math:`(i,j)` stak margfeldisins :math:`C` með
því að taka innfeldi af :math:`i`-tu línu :math:`A` og :math:`j`-ta dálki B.

Önnur leið til að lýsa fylkjamargfeldi er að segja að :math:`j`-ti dálkur
útkomunnar sé margfeldi af :math:`A` og :math:`j`-ta dálki :math:`B`. Ef
:math:`B = [b_1|b_2|\ldots|b_n]` gildir sem sé að:

.. math:: C = [c_1|c_2|\ldots|c_n]

þar sem :math:`c_i = Ab_i`.

.. Sýnidæmi
.. important::
   Reiknum margfeldi tveggja :math:`2 \times 2` fylkja :math:`A` og :math:`B`: 

   .. math::
      \begin{pmatrix}1 & 2 \\ 3 & 4 \end{pmatrix}
      \begin{pmatrix}5 & 6 \\ 0 & -2 \end{pmatrix}

   og fáum :math:`c_{11} = 1 \cdot 5 + 2 \cdot 0 = 5`, :math:`c_{12} = 1 \cdot 6
   - 2 \cdot 2 = 2`, :math:`c_{21} = 3 \cdot 5 + 4 \cdot 0 = 15` og
   :math:`c_{22} = 3 \cdot 6 - 4 \cdot 2 = 10`, sem sé

   .. math::
      C = \begin{pmatrix}5 & 2 \\ 15 & 10 \end{pmatrix}

**Veldi** af ferningsfylkjum eru skilgreind með endurtekinni margföldun: :math:`A^2`
er :math:`A \cdot A = AA`, :math:`A^3 = AAA` o.s.frv. Í kafla
:numref:`fylki og net` verður sýnd skemmtileg hagnýting á fylkjaveldum.

.. admonition:: Python: Fylkjamargföldun og -veldi
   :class: python

   Í NumPy má margfalda saman fylki með virkjanum **@** og fallið
   :code:`la.matrix_power` má nota til að hefja fylki í veldi, t.d.

   .. code:: python3

      import numpy as np
      A = np.array([[1,2],[3,4]])
      B = np.array([[5,6],[0,-2]])
      C = A @ B
      D = la.matrix_power(A,2)
      print(C); print(D)
      # ---prentar [[ 5  2]  
      #             [15 10]]
      #            [[ 7 10]
      #             [15 22]]

.. admonition:: Python: Samanburður vigra og fylkja
   :class: python

   Til að kanna hvort tveir vigrar eða tvö fylki séu eins er ekki hægt að nota
   virkjann == því hann verkar stakvíst og gefur auk þess villu ef vigrarnir eða
   fylkin eru misstór. NumPy er með séstakt fall sem er ætlað í svona samanburð,
   ``np.array_equal``. Ef

   .. code::

      A = [[2 2]     og   B = [[4 4]
           [2 2]]              [4 4]]

      þá skilar :code:`np.array_equal(A + A, B)` gildinu ``True``.        

Núllfylki og einingafylki
-------------------------
.. admonition:: Skillgreining: Núllfylki og einingafylki
   :class: regla

   **Núllfylki** (*zero matrix*) hefur öll stök = 0 og **einingafylki**
   (*identity matrix*) hefur hornalínustökin = 1 og öll önnur stök = 0.

Einingafylki er oftast táknað með :math:`I` og stærð þess ræðst yfirleitt af
samhenginu. Núllfylki eru stundum táknuð með :math:`0` eða :math:`O` (núll eða
bókstafurinn O), og stærðin ræðst líka af samhenginu.

Hér eru :math:`2 \times 2` og :math:`3 \times 3` einingafylki og :math:`2 \times
3` núllfylki:

.. math::
   \begin{pmatrix}1 & 0 \\ 0 & 1 \end{pmatrix} \quad
   \begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \quad
   \begin{pmatrix}0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}

Núllfylkið er **samlagningarhlutleysa** (*neutral element*) og eingarfylkið
er **margföldunarhlutleysa** (*identity element*) því :math:`O + A = A + O =
A` og :math:`I\cdot A = A\cdot I = A` fyrir öll A

.. admonition:: Python: zeros og eye
   :class: python

   Í NumPy má búa til :math:`m \times n` núllfylki með :code:`np.zeros((m,n))`
   og :math:`n \times n` einingafylki með :code:`np.identity(n)` eða
   :code:`np.eye(n)` (*eye* er borið fram eins og *I* ).

.. admonition:: Æfing: Hlutleysur
   :class: aefing
           
   Búið til fylkið: :math:`A = \begin{pmatrix}1.2 & 3.4 \\ 5.6 & 7.8
   \end{pmatrix}` |br|
   og auk þess :math:`2 \times 2` núllfylki og einingarfylki. Notið fallið
   ``np.array_equal`` til að sannreyna það sem sagt er um hlutleysur að ofan.

Lausn jöfnuhneppa
-----------------
Ein mikilvæg hagnýting fylkja er að leysa saman margar jöfnur í mörgum línulegum
jöfnum. Það er nefnilega hægt að setja slíkar jöfnur fram sem **fylkja- og
vigurjöfnu**. Ef jöfnurnar eru jafn margar og óþekktu stærðirnar er yfirleitt
til nákæmlega ein lausn.

.. admonition:: Sýnidæmi: Tvær jöfnur í tveimur óþekktum
   :class: synidaemi

   Leysum jöfnurnar:

   .. math::
      2 x_1 + 3 x_2 &= 8 \\
      5 x_1 - 2 x_2 &= 1

   Við margföldum fyrri jöfnuna með :math:`2` og þá seinni með :math:`3` og
   leggjum saman (til að losna við :math:`x_2`) og fáum :math:`19x_1 = 19` svo
   :math:`x_1=1`. Seinni jafnan gefur svo :math:`2x_2 = 5x_1 - 1 = 4` svo
   :math:`x_2=2`. Til að undirstrika að hér var miðað við lausn með blaði og
   blýanti voru stök :math:`x` og `y` tölusett með 1 og 2 í staðinn fyrir 0 og 1.

Jöfnurnar í þessu sýnidæmi má líka rita með fylki og vigrum:

.. math::
   A x = b

þar sem :math:`A = \begin{pmatrix}2 & 3\\5 & -2\end{pmatrix}` og :math:`b =
\begin{pmatrix}8\\1\end{pmatrix}`, sbr. kafla :numref:`grunnreikniaðgerðir`.

.. admonition:: Æfing: Fylkjaframsetning
   :class: aefing

   Gefnar eru jöfnurnar
   
   .. math::
      x + 2y &= z + t + 8 \\
      z – x &= 3 \\
      x + y + z + t &= 12 \\
      y + 3 &= 2x

   Ákvarðið tilsvarandi fylki :math:`A` og vigur :math:`b` þannig að þessar
   jöfnur svari til :math:`Av = b` þar sem :math:`v = (x, y, z, t)`

.. admonition:: Python: Lausn jöfnuhneppis
   :class: python

   Fylkjaframsetning á jöfnuhneppi einfaldar kannski ekki mikið lausn með blaði
   og blýanti en með því að nota fallið **la.solve** verður lausnin beint af
   augum:

   .. code:: python

      import numpy as np, numpy.linalg as la
      A = np.array([[2, 3], [5, -2]])
      b = np.array([8, 1])
      x = la.solve(A, b)
      print(x)
      #--- prentar [1., 2.]

Það sem NumPy gerir bak við tjöldin er að umrita jöfnurnar með svipuðum hætti og
gert var í sýnidæminu hér á undan og einangra þannig óþekktu stærðirnar hverja á
fætur annari og ákvarða gildi þeirra.

.. admonition:: Æfing: Hollur matur
   :class: aefing

   Sigga hefur ákveðið að borða bara skyr, rúgbrauð og kæfu, en þessar
   fæðutegundir innihalda næringarefni í 100 g sem hér segir:

         .. list-table::
            :widths: auto
         
            * -
              - **Skyr**  
              - **Rúgbrauð**
              - **Kæfa**         

            * - Kolvetni
              - 3.7
              - 36
              - 2.4

            * - Prótein
              - 11
              - 8.6
              - 12.8

            * - Fita
              - 0.2
              - 6.7
              - 29.3

   Notið NumPy til að ákvarða hvað hún á að borða mikið af hverju á dag ef hún
   vill fá 100 g af kolvetnum, 150 g af próteini og 150 g af fitu úr matnum?

.. figure:: myndir/matur.png
   :width: 16cm
   :align: center

.. danger::
   Sigga ætti að borða eitthvað grænmeti líka.

Jöfnuhneppi með n óþekktum
--------------------------
Til að átta sig á sambandi jöfnuhneppa og fylkja getur gagnast að skoða eftirfarandi algenga framsetningu almenns :math:`n \times n` jöfnuhneppis:

.. math::
   &a_{11} x_1 + a_{12} x_2 + \ldots + a_{1n} x_n =\; &b_1 \\
   &\vdots                                            &\vdots \\
   &a_{n1} x_1 + a_{n2} x_2 + \ldots + a_{nn} x_n =\; &b_n

Á fylkjaformi verður þetta:

.. math::
   \begin{pmatrix}
   a_{11} & a_{12} & \cdots & a_{1n} \\
   \vdots &        &        & \vdots \\
   a_{n1} & a_{n2} & \cdots & a_{nn}
   \end{pmatrix} &
   \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}\;&= 
   \begin{pmatrix} b_1 \\ \vdots \\ b_n \end{pmatrix}\\
   \\
   A & x& = b

Hér hefur verið byrjað að telja í einum eins og algengast er í stærðfræði. Til að reikna í NumPy þarf að taka tillit til þess að það byrjar að telja í núll.

.. admonition:: Sýnidæmi: Jöfnunheppi byggt í skrefum
   :class: synidaemi

   Í raunverulegum verkefnum eru jöfnuhneppi oftast gefin með því að setja fram
   einstakar jöfnur í þeim, sem þarf svo að stinga inn á réttan stað í fylki sem
   búið er til smám saman. Hér er einfalt dæmi:

   Um :math:`x_1, x_2,\ldots x_n` gildir

   .. math:: 2x_{i+1} - x_i &= 0\quad(i=1,...,n-1)\\
             \sum_{i=1}^n x_i  &= 3n

   Skrifum Python-fall sem leysir þessar jöfnur. Byrjum á að endurskrifa
   jöfnurnar miðað við að fyrsta breytan heiti :math:`x_0`:
   
   .. math:: 2x_{i+1} - x_i &= 0\quad(i=0,...,n-2)\\
             \sum_{i=0}^{n-1} x_i  &= 3n

   Svo byrjum við með :math:`n \times n` núllfylki og núll í hægri hlið, og
   tökum eftir að fyrir :math:`i<n-1` verður lína nr. :math:`i` í fylkinu:

   .. math::
      (0,\ldots,0,-1&,2,0,\ldots,0)\\
      \uparrow&\\
      i\text{-ta}&\text{ sæti}

   og neðsta línan er svo full af ásum. Hægri hlið hneppisins er núll, nema í
   neðsta sætinu, þar stendur :math:`3n`. Við fáum því fallið:

   .. code:: Python

      def leysa(n):
         A = np.zeros((n,n))
         b = np.zeros(n)
         for i in range(n-1):
            A[i,(i,i+1)] = [-1, 2]  # setjum tvö stök í einu
         for j in range(n):
            A[n-1,j] = 1            # ásar í neðstu línu
         b[n-1] = 3*n
         x = la.solve(A, b)
         return x

Til að skýra betur hvað er að gerast í sýnidæminu fylgir jöfnuhneppið í
tilfellinu :math:`n = 5` hér:

   .. math::
      \begin{pmatrix}
      -1 & 2 & 0 & 0 & 0\\
      0 & -1 & 2 & 0 & 0\\
      0 & 0 & -1 & 2 & 0\\
      0 & 0 & 0 & -1 & 2\\
      1 & 1 & 1 & 1 & 1
      \end{pmatrix}
      \begin{pmatrix} x_0\\x_1\\x_2\\x_3\\x_4 \end{pmatrix}
      \begin{pmatrix} 0\\0\\0\\0\\15 \end{pmatrix}

.. admonition:: Æfing: Jöfnuhneppi búin til í lykkju
   :class: aefing

   1. Leysið jöfnuhneppið í sýnidæminu fyrir :math:`n=4` (ætti að gefa :math:`x
      = (6.4, 3.2, 1.6, 0.8)`).

   2. Búið til fall ``lausn(a,n)`` sem leysir jöfnurnar

      .. math:: - a\sum_{j=1}^{i-1}x_j + x_i = 1\quad(i=1,...,n)
      
      Prófið með ``leysa(2,4)`` sem ætti að gefa :math:`(1,3,9,27)`.

Andhverfur og ákveður
---------------------
Flest fylki eru það sem kallað er **andhverfanleg** (*nonsingular*), og eins og
ráða má af orðinu er hægt að reikna **andhverfu** (*inverse*) slíkra fylkja,
nánar tiltekið margföldunarandhverfu.

.. admonition:: Skilgreining: Andhverfa
   :class: regla

   Andhverfa fylkis :math:`A` er annað fylki :math:`B` sem uppfyllir

   .. math:: AB = BA = I

   þar sem :math:`I` er einingafylkið úr kafla :numref:`Núllfylki og
   einingafylki`.

Andhverft fylki :math:`A` er táknað :math:`A^{-1}`. Ef andhverfa
fylkis :math:`A` er þekkt, þá er hægt að leysa jöfnuhneppi

.. math::
   Ax = b

með því að margfalda í gegn með :math:`A^{-1}`:

.. math::
   A^{-1}Ax &= A^{-1}b\\
   Ix       &= A^{-1}b\\
   x        &= A^{-1}b

Annar eiginleiki fylkis sem kemur við sögu í línulegri algebru er **ákveða**
þess (*determinant*), táknuð :math:`\det A`, sem reyndar verður ekki mikið
notuð í þessum fyrirlestrarnótum.

.. admonition:: Python: 
   :class: python

   Það er fremur flókið að reikna andhverfur og ákveður með blaði og blýanti, en
   talsvert einfaldara með NumPy:

   .. code::

      import numpy as np, numpy.linalg as la
      A = np.array([[2,3,4], [2,4,8], [3,4,9]])
      B = la.inv(A)
      d = la.det(A)
   
.. admonition:: Æfing: Andhverfa og ákveða
   :class: aefing

   Sláið inn eða afritið forritið hér á undan og ákvarðið með því andhverfu og
   ákveðu fylkisins :math:`\begin{pmatrix}2&3&4\\2&4&8\\3&4&9\end{pmatrix}`.
   
.. danger::
   
   Það er bæði nákvæmara og hraðvirkara að leysa jöfnuhneppi með
   :code:`np.solve` heldur en með því að reikna andhverfu. Í útreikningum
   fyrir raunveruleg verkefni ætti alltaf að reyna að umrita reiknirit
   með fylkjaandhverfum yfir í reiknirit sem leysa jöfnuhneppi.
