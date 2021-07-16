Inngangur
============

*He was determined to discover the underlying logic behind the universe. Which was going to be hard, because there wasn't one.*

\- Terry Pratchett, Mort

Hvað er töluleg greining?
-------------------------

Tilraun að svari
~~~~~~~~~~~~~~~~

-  Fagið *töluleg greining* snýst um að búa til, greina og forrita
   aðferðir til þess að nálga á lausnum á stærðfræðilegum verkefnum.

-  Aðferðirnar eru settar fram með reikniritum sem síðan eru forrituð og
   það þarf góðan skilning á eiginleikum lausnanna sem verið er að nálga
   til þess að geta greint hvernig forritin munu virka.

-  Greining á reikniritum er aðallega fólgin í skekkjumati og mati á
   þeim aðgerðafjölda sem þarf til þess að ná að nálga lausn með
   fyrirfram gefinni nákvæmni, þ.e. hagkvæmni og nákvæmni reikniritsins.

-  Líkanagerð í raunvísindum og verkfræði felur yfirleitt í sér eftirfarandi skref:
   
   1. *Greina* kerfið sem um ræðir
   2. *Smíða líkan* sem útskýrir hvernig kerfið hegðar sér, þó yfirleitt með töluverðum einföldunum.
   3. *Herma* kerfið í tölvu eins vel og hægt er. Hér þarf að ná ásættanlegri námkvæmni á þeim tíma sem útreikningar mega taka. 
   4. *Túlka* niðurstöðurnar og bera saman við upphaflega kerfið.
   
   Töluleg greining kemur mikið við sögu í lið 3. og einnig í lið 4.
   
   
Dæmi: Eldflaug
--------------

Gerum ráð fyrir að við höfum eftirfarandi eldflaug undir höndum:

-  Eldsneytið dugir í 18 sek., þ.e. :math:`t\in [0,18]`.

-  Loftmótstaðan er :math:`d=0.1v^2`, þar sem :math:`v(t)` er hraðinn á tíma :math:`t`.

-  Krafturinn sem knýr flaugina er :math:`T=5000` N.

-  Massi eldsneytisins er :math:`m=180-10t` kg.

-  Massi flaugarinnar er :math:`M = 120 + m = 300 - 10t` kg.

Spurningin er: Í hvaða hæð er eldflaugin þegar eldsneytið klárast?

Úr öðru lögmáli Newtons fæst að :math:`F = (Mv)'`. Kraftarnir sem verka
á eldflaugina er :math:`T` upp á við og loftmótstaðan og
þyngdarkrafturinn niður á við. Þannig fæst

.. math:: (Mv)' = F = T - Mg - d

\ það er

.. math:: M'v + Mv' = T - Mg -d.

Þetta jafngildir því að

.. _eldflaug:

.. math::

   v' = \frac{T-Mg-d-M'v}{M} = \frac{5000-(300-10t)g-0,1v^2+10v}{300-10t},
   \label{eldflaug}

og upphafsskilyrðin eru :math:`v(0) =0`.

Þar sem :math:`h' = v`, þá er hæðin á tíma :math:`t` gefin með
:math:`h(t) =\int_0^t v(s)\, ds`. Þegar eldsneytið klárast þá er hæðin
:math:`h(18) = \int_0^{18} v(s)\, ds`.

Verkefnið er því að finna :math:`v`, og reikna svo heildið.

:ref:`Diffurjafnan <eldflaug>` hér að ofan er ólínuleg og ekki aðgreinanleg þannig 
að við getum ekki vænst
þess finna lausn með þeim aðferðum sem við höfum þegar lært. Eins er
ekki víst að við getum auðveldlega fundið stofnfall :math:`h` fyrir
:math:`v` til þess að reikna heildið, jafnvel þótt við hefðum :math:`v`.

Hins vegar getum við leyst diffurjöfnuna tölulega með aðferðunum úr 
:ref:`kafla 6 <upphafsgildisverkefni>`,
og heildið reiknum við svo tölulega með aðferðunum úr :ref:`kafla 5 <heildun>`.

Samleitni runa
--------------

Nokkur atriði um samleitni runa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mörg reiknirit til nálgunar á einhverri rauntölu eru hönnuð þannig að
reiknuð er runa :math:`x_0,x_1,x_2,\dots` sem á að nálgast lausnina
okkar.

.. index::
    runa
    samleitni
    samleitni; línuleg
    samleitni; ofurlínuleg
    samleitni; ferningssamleitni
    samleitni; af stigi α
    markgildi
    

Skilgreining: Samleitni
~~~~~~~~~~~~~~~~~~~~~~~

*Rauntalnaruna* :math:`(x_n)` er sögð vera *samleitin* (e. convergent)
að *markgildinu* :math:`r` ef um sérhvert :math:`\varepsilon>0` gildir
að til er :math:`N>0` þannig að

.. math:: |x_n-r|<\varepsilon, \qquad \text{ ef } \quad n\geq N.

Þetta er táknað annað hvort með

.. math::

   \lim_{n\to \infty}x_n=r \qquad \text{ eða } \qquad  x_n\to r
       \text{ ef } n\to \infty.

Ef runan :math:`(x_n)` er samleitin að markgildinu :math:`r` þá segjum
við einnig að hún *stefni á* :math:`r`.

Hugsum okkur nú að :math:`(x_n)` sé gefin runa sem stefnir á :math:`r`
og táknum skekkjuna með :math:`e_n=r-x_n`.

Runan er sögð vera *línulega samleitin* (e. linear convergence) ef til
er :math:`\lambda\in ]0,1[` þannig að

.. math:: \lim_{n\to \infty}\dfrac{|e_{n+1}|}{|e_n|}=\lambda,

*ofurlínulega samleitin* (e. superlinear convergence), ef

.. math:: \lim_{n\to \infty}\dfrac{|e_{n+1}|}{|e_n|}=0,

*ferningssamleitin* (e. quadratic convergence) ef til er :math:`\lambda>0` þannig að

.. math:: \lim_{n\to \infty}\dfrac{|e_{n+1}|}{|e_n|^2}=\lambda,

og *samleitin af stigi* :math:`\alpha` (e. convergence of order
:math:`\alpha`), þar sem :math:`\alpha> 1`, ef til er :math:`\lambda>0`
þannig að

.. math:: \lim_{n\to \infty}\dfrac{|e_{n+1}|}{|e_n|^\alpha}=\lambda.

.. note:: 
    Runa er ofurlínulega samleitin ef hún er samleitin af stigi :math:`\alpha>1`.
    
    Ferningssamleitin runa er samleitin af stigi 2 þannig að hún er einnig ofurlínulega samleitin.

Skilgreining
~~~~~~~~~~~~
    
Oft eru notuð veikari hugtök til þess að lýsa samleitni runa (t.d. ef
við getum ekki fundið :math:`\lambda` og :math:`\alpha` nákvæmlega).

Þannig segjum við að runan :math:`(x_n)` sé *að minnsta kosti línulega
samleitin* ef til er :math:`\lambda\in ]0,1[` og :math:`N >0` þannig að

.. math:: |e_{n+1}|\leq \lambda |e_n|, \qquad n\geq N,

ef til er :math:`\lambda>0` og :math:`N>0` þannig að

.. math:: |e_{n+1}|\leq \lambda |e_n|^2, \qquad n\geq N,

og *að minnsta kosti samleitin af stigi* :math:`\alpha`, þar sem
:math:`\alpha> 1`, ef til eru :math:`\lambda>0` og :math:`N>0` þannig að

.. math:: |e_{n+1}|\leq \lambda |e_n|^\alpha, \qquad n\geq N.


Setning Taylors
---------------

*Sometimes it's better to light a flamethrower than curse the darkness.*
\- Terry Pratchett, Men at Arms: The Play

.. index::
    föll; diffranlegt
    föll; afleiða
    föll; rúm samfelldra falla
    föll; rúm diffranlegra falla
    

Ritháttur fyrir diffranleg föll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum nú :math:`f : I \to {\mathbb  C}` vera fall á bili :math:`I` sem
tekur gildi í tvinntölunum. Ef :math:`f` er deildanlegt í sérhverjum
punkti í :math:`I`, þá táknum við afleiðuna með :math:`f'`. Ef
:math:`f'` er deildanlegt í sérhverjum punkti í :math:`I`, þá táknum við
*aðra afleiðu* :math:`f` með :math:`f''`, og svo framvegis.

Við skilgreinum með þrepun :math:`f^{(k)}` fyrir :math:`k = 0,1,2,
\ldots` þannig að :math:`f^{(0)} = f` og ef :math:`f^{(k-1)}` er
deildanlegt í sérhverjum punkti í :math:`I`, þá er
:math:`f^{(k)} = (f^{(k-1)})'`.

Við látum :math:`C^{k}(I)` tákna línulega rúmið sem samanstendur af
öllum föllum :math:`f :
I \to {\mathbb  C}` þannig að :math:`f', \ldots, f^{(k)}` eru til í
sérhverjum punkti í :math:`I` og :math:`f^{(k)}` er samfellt fall á
:math:`I`.

.. index::
    Taylor-margliða
    

Nálgun með Taylor-margliðu
~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`a \in I`, :math:`m` er jákvæð heiltala og
:math:`f \in C^{m}(I)`, þá nefnist margliðan

.. math:: p(x) = f(a) + f'(a)(x-a) + \ldots   + \frac{f^{(m)}(a)}{m!}(x-a)^m

Taylor-margliða fallsins :math:`f` í punktinum :math:`a` af stigi
:math:`m`, og er stundum táknuð með :math:`T_m f(x;a)`.

Athugið að stig margliðunnar :math:`p` er minna eða jafnt og :math:`m`.


.. index::
    setning Taylors

Setning Taylors
~~~~~~~~~~~~~~~

Látum :math:`I \subseteq {\mathbb  R}` vera bil, :math:`f : I \to
{\mathbb  C}` vera fall, :math:`m \geq 0` vera heiltölu og gerum ráð
fyrir að :math:`f \in
C^m(I)` og að :math:`f^{(m+1)}(x)` sé til í sérhverjum innri punkti
bilsins :math:`I`. Þá er til punktur :math:`\xi` á milli :math:`a` og
:math:`x` þannig að

.. math:: f(x) - T_mf(x;a)= \frac{f^{(m+1)}(\xi)}{(m+1)!}(x-a)^{m+1}.

Hægri hliðin er oft táknuð :math:`R_m(x)`.

.. note::
    Þetta þýðir að skekkjan í því að nálga fallið :math:`f(x)` með 
    Taylor-margliðu af stigi :math:`m` hagar sér eins og 
    :math:`(x-a)^{m+1}`.

Viðbót
~~~~~~

Ef :math:`f^{(m+1)}` er samfellt á lokaða bilinu með endapunkta
:math:`a` og :math:`x`, þá er

.. math::

   \begin{aligned}
     R_m(x) &= f(x) - T_mf(x;a) \\
     &= \int\limits_a^x \frac{(x-t)^m}{m!}f^{(m+1)}(t) dt \notag \\
     &= (x-a)^{m+1} \int\limits_0^1 \frac{(1-s)^m}{m!} f^{(m+1)}(a + s(x-a)) ds.
   \end{aligned}

Sýnidæmi: Nálgun á fallgildum :math:`x-\sin x`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vitum að :math:`x \approx \sin x` ef :math:`x` er lítið. Tökum
:math:`x=0.1` og hugsum okkur að við séum að reikna á vél með 8 stafa
nákvæmni. Hún gefur

.. math:: \sin 0.1 = 0.099833417

Af því leiðir

.. math:: 0.1 - \sin 0.1 = 1.66583\cdot 10^{-4}

Við höfum tapað tveimur markverðum stöfum í nákvæmni.

Ef við notum Taylor-nálgunina fyrir :math:`\sin(x)`,

.. math::

   \sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} 
       - \frac{x^7}{7!} \cdots

og tökum fyrstu þrjá liðina, þ.e. skoðum 6. stigs Taylor-margliðu
fallsins.

:math:`x-\sin(x)` er þá u.þ.b.

.. math:: x - \left(x - \frac{x^3}{3!} + \frac{x^5}{5!}\right) = \frac{x^3}{3!} - \frac{x^5}{5!}.

Fallgildið er þá

.. math:: \frac {0.1^3}{3!} - \frac{0.1^5}{5!} = 1.6658334 \cdot 10^{-4}.

Skekkjan er gefin með

.. math::

   |R_6(0.1)| = \left|\frac{\sin^{(7)}(\xi)}{7!}0.1^7\right|
       = \left|\frac{-\cos(\xi)}{7!}0.1^7\right| 
       \leq \frac{1}{7!}0.1^7 < 0.2\cdot 10^{-10}.

Sem þýðir að allir 8 stafir reiknivélarinnar eru markverðir, þ.e.
allir stafir :math:`1.6658334 \cdot 10^{-4}` eru réttir.

:math:`\sin^{(7)}` hér að ofan táknar 7. afleiðu :math:`\sin`, sem er
:math:`-\cos`.

Ef við tökum :math:`x = 0.01` er þetta enn greinilegra. Reiknivélin
gefur

.. math:: \sin(0.01) = 0.0099998333

Þannig að

.. math:: 0.01 - \sin 0.01 = 0.1667\cdot 10^{-7}

og við erum bara með 4 markverða stafi.

Hér dugir að taka aðeins þriðja stigs liðinn í Taylor-formúlunni

.. math::

   0.01 - \sin (0.01) \approx \frac{0.01^3}{3!} 
       = 0.16666667 \cdot 10^{-7},

því skekkjan er

.. math:: R_4(0.01) \leq \frac{0.01^5}{5!} < 10^{-12}

.. index::
    skekkja
    skekkja; mæliskekkja
    skekkja; aðferðarskekkja
    skekkja; reikningsskekkja
    skekkja; mannlegar villur

Skekkjur
--------

.. todo::
	Bæta við: :math:`plot(e^x-cos(x)-x) from -5*10^{-8} to 5*10^{-8}`.

Við allar úrlausnir á verkefnum í tölulegri greininingu þarf að fást við
skekkjur. Þær eru af ýmsum toga:

-  Gögn eru oft niðurstöður mælinga og þá fylgja þeim *mæliskekkjur*.
   Eins getum við þurft að notast við nálganir á föstum sem koma fyrir
   (t.d. :math:`\pi`, Avogadrosar talan, …).

-  Við nálganir á lausnum á stærðfræðilegum verkefnum verða til
   *aðferðarskekkjur*. Þær verða til þegar reikniritin eru hönnuð og
   greining á reikniritum snýst fyrst og fremst um mat á
   aðferðarskekkjum.

-  *Reikningsskekkjur* verða til í tölvum á öllum stigum, jafnvel þegar
   tölur eru lesnar inn í tugakerfi og þeim snúið yfir í tvíundarkerfi.
   Þær verða líka til vegna þess að tölvur geta einungis unnið með
   endanlegt mengi af tölum og allar útkomur þarf að nálga innan þess
   mengis. Þessar skekkjur nefnast oft *afrúningsskekkjur*.

-  *Mannlegar villur* eru óumflýjanlegar. Það sem við getum gert er
   temja okkur vinnubrögð sem lágmarka líkur á þeim og auðvelda okkur að
   finna villur sem við gerum. 
   
   *Real stupidity beats artificial intelligence every time.*
   -- Terry Pratchett

.. index::
    skekkja; algildi
    skekkja; hlutfallsleg

Skekkja í nálgun á rauntölu :math:`r`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við getum stillt upp jöfnunum svona

.. math::

   r \text{ (rétt gildi) } = x\text{ (nálgunargildi)} + 
       e \text{ (skekkja)}

þar sem talan :math:`x` er nálgun á tölunni :math:`r`, og þá nefnist

.. math:: e=r-x

*skekkjan (e. error) í nálgun á* :math:`r` *með* :math:`x` eða bara
*skekkja*.

*Algildi skekkju (e. absolute error)* er tölugildið :math:`|e|=|r-x|`

Ef vitað er að :math:`r\neq 0`, þá nefnist

.. math:: \dfrac{|e|}{|r|}=\dfrac{|r-x|}{|r|}

*hlutfallsleg skekkja (e. relative error)* í nálgun á :math:`r` með
:math:`x`.

.. warning::
    Auðvitað er talan :math:`r` sem við leitum að óþekkt (annars
    þyrftum við ekki að framkvæma alla þessa reikninga), sem þýðir að við
    getum hvergi notað hana í reikningum.

.. index::
    skekkja; fyrirframmat
    
Fyrirframmat á skekkju
~~~~~~~~~~~~~~~~~~~~~~

Metið er áður en reikningar hefjast hversu umfangsmikla reikninga þarf
að framkvæma til þess að nálgunin náist innan fyrirfram gefinna
skekkjumarka.

Ef lausnin er fundin með ítrekunaraðferð er yfirleitt metið hversu
margar ítrekarnir þarf til þess að nálgun verði innan skekkjumarka.

.. index::
    skekkja; eftirámat

Eftirámat á skekkju
~~~~~~~~~~~~~~~~~~~

Um leið og reikningar eru framkvæmdir er lagt mat á skekkju og
reikningum er hætt þegar matið segir að nálgun sé innan skekkjumarka.
Það gerist yfirleitt þegar gildið sem við reiknum út breytist orðið
lítið í hverju skrefi.

Hér þarf að skipta í tvö tilvik, fyrst skoðum við tilvikið þegar runan er ofurlínulega samleitin 
og seinna tilvikið er þegar við vitum aðeins að runan er línulega samleitin, en 
þá er matið aðeins flóknara.

.. index::
	samleitni; ofurlínuleg

Ofurlínuleg samleitni -- Eftirámat á skekkju
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hugsum okkur að við séum að nálga töluna :math:`r` með gildum rununnar
:math:`x_n`, að við höfum reiknað út :math:`x_0,\dots,x_n` og viljum fá
mat á skekkjunni :math:`e_n=r-x_n` í :math:`n`-ta skrefi.

Við reiknum næst út :math:`x_{n+1}` og skrifum
:math:`e_{n+1}=\lambda_ne_n`. Þá er

.. math::

   x_{n+1}-x_n = (r-x_n)-(r-x_{n+1})
       = e_n-e_{n+1} = (1-\lambda_n)e_n

og við fáum

.. math:: e_n = \dfrac{x_{n+1}-x_n}{1-\lambda_n}.

Ef við vitum að runan er *ofurlínulega samleitin*, þá stefnir
:math:`\lambda_n` á :math:`0` og þar með er

.. math:: e_n\approx x_{n+1}-x_n.

Við hættum því útreikningi þegar :math:`|x_{n+1}-x_n|<\varepsilon` þar
sem :math:`\varepsilon` er fyrirfram gefin tala, sem lýsir þeirri
nákvæmni sem við viljum ná.

.. index::
	samleitni; línuleg

Línuleg samleitni -- Eftirámat á skekkju
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skoðum nú tilvikið ef einu upplýsingarnar sem við höfum er 
að runan :math:`x_n` sé *að minnsta kosti
línulega samleitin*, þ.e. :math:`c\in [0,1)` og :math:`N\in \mathbb N`
þannig að 

.. math::
	|e_{n+1}|\leq c|e_n|, \qquad \text{fyrir } n \geq N.

Þá stefnir :math:`\lambda_n = e_{n+1}/e_n` á fasta :math:`\lambda \leq c` og við höfum

.. math::

   \lambda_n = \dfrac{e_{n+1}}{e_n} = 
       \dfrac{1-\lambda_n}{1-\lambda_{n+1}}
       \cdot\dfrac{x_{n+2}-x_{n+1}}{x_{n+1}-x_n}\approx 
       \dfrac{x_{n+2}-x_{n+1}}{x_{n+1}-x_n}

Nú þurfum við að átta okkur á því hvernig þetta er nýtt í útreikningum.

Hugsum okkur að við höfum reiknað út :math:`x_0,\dots,x_n` og viljum fá
mat á :math:`e_n`. Við reiknum þá út :math:`x_{n+1}` og :math:`x_{n+2}`
og síðan hlutfallið :math:`\kappa_n=(x_{n+2} - x_{n+1})/(x_{n+1} -
x_n)` sem við notum sem mat á :math:`\lambda_n`. Eftirámatið á
skekkjunni í ítrekunarskrefi númer :math:`n` verður síðan

.. math:: e_n\approx \dfrac{x_{n+1}-x_n}{1-\kappa_n}.

Ef stærðin í hægri hliðinni er komin niður fyrir fyrirfram gefin
skekkjumörk :math:`\varepsilon`, þá stöðvum við útreikningana.

Sýnidæmi
~~~~~~~~

Okkur er gefin runa af nálgunum á lausn jöfnunnar

.. math:: f(x) = e^x\sin x-x^2 = 0

og eigum að staðfesta hvort nálgunaraðferðin er ferningssamleitin:

+-------------+--------------------+-------------------------+-------------------------------------------------+
| :math:`n`   | :math:`x_n`        | :math:`|x_{n+1}-x_n|`   | :math:`\frac{|x_{n+1}-x_n|}{|x_n-x_{n-1}|^2}`   |
+=============+====================+=========================+=================================================+
| 0           | 3.00000000000000   |                         |                                                 |
+-------------+--------------------+-------------------------+-------------------------------------------------+
| 1           | 2.73251570951922   | 0.10052257507862        | 1.404                                           |
+-------------+--------------------+-------------------------+-------------------------------------------------+
| 2           | 2.63199313444060   | 0.01373904283351        | 1.359                                           |
+-------------+--------------------+-------------------------+-------------------------------------------------+
| 3           | 2.61825409160709   | 0.00024006192208        | 1.273                                           |
+-------------+--------------------+-------------------------+-------------------------------------------------+
| 4           | 2.61801402968501   | 0.00000007236005        | 1.256                                           |
+-------------+--------------------+-------------------------+-------------------------------------------------+
| 5           | 2.61801395732496   | 0.00000000000001        | 1.272                                           |
+-------------+--------------------+-------------------------+-------------------------------------------------+

Við metum :math:`e_n\approx |x_{n+1}-x_n|` og þar af leiðandi er

.. math::
    |e_n|/|e_{n-1}|^2\approx |x_{n+1}-x_n|/|x_n-x_{n-1}|^2.

Við sjáum að hlutfallið :math:`|x_{n+1}-x_n|/|x_n-x_{n-1}|^2` helst
stöðugt og því ályktum við að aðferðin sé ferningssamleitin.

Útreikningur á samleitnistigi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skoðum lítið dæmi um útreikninga á samleitnistigi.

Eftirfarandi runa stefnir á :math:`\sqrt 3`.

+-------------+---------------------+
| :math:`n`   | :math:`x_n`         |
+=============+=====================+
| 0           | 2.000000000000000   |
+-------------+---------------------+
| 1           | 1.666666666666667   |
+-------------+---------------------+
| 2           | 1.727272727272727   |
+-------------+---------------------+
| 3           | 1.732142857142857   |
+-------------+---------------------+
| 4           | 1.732050680431722   |
+-------------+---------------------+
| 5           | 1.732050807565499   |
+-------------+---------------------+

Er samleitnistigið :math:`1.618`?

Ef ekki, hvert er þá samleitnistigið?

.. begin-toggle:: 1264951
    :label: Lausn

Ef miðað er við að runan :math:`(x_n)` sé ofurlínulega
samleitin, þá er eðlilegt að taka :math:`e_n\approx x_{n+1}-x_n` sem mat
á skekkjunni :math:`e_n=\sqrt 3-x_n` í :math:`n`-ta ítrekunarskrefinu.

Við byrjum á því að kanna hvernig tilgátan um að samleitnistigið kemur
út á þessum tölum með :math:`e_n=x_{n+1}-x_n`:

+-------------+---------------------+---------------------------------+-----------------------------------+
| :math:`n`   | :math:`x_n`         | :math:`|e_n|`                   | :math:`|e_n|/|e_{n-1}|^{1.618}`   |
+=============+=====================+=================================+===================================+
| 0           | 2.000000000000000   | 3.3333\ :math:`\cdot 10^{-1}`   |                                   |
+-------------+---------------------+---------------------------------+-----------------------------------+
| 1           | 1.666666666666667   | 6.0606\ :math:`\cdot 10^{-2}`   | 3.5851\ :math:`\cdot 10^{-1}`     |
+-------------+---------------------+---------------------------------+-----------------------------------+
| 2           | 1.727272727272727   | 4.8701\ :math:`\cdot 10^{-3}`   | 4.5439\ :math:`\cdot 10^{-1}`     |
+-------------+---------------------+---------------------------------+-----------------------------------+
| 3           | 1.732142857142857   | 9.2177\ :math:`\cdot 10^{-5}`   | 5.0837\ :math:`\cdot 10^{-1}`     |
+-------------+---------------------+---------------------------------+-----------------------------------+
| 4           | 1.732050680431722   | 1.2713\ :math:`\cdot 10^{-7}`   | 4.3004\ :math:`\cdot 10^{-1}`     |
+-------------+---------------------+---------------------------------+-----------------------------------+
| 5           | 1.732050807565499   |                                 |                                   |
+-------------+---------------------+---------------------------------+-----------------------------------+

Tveimur síðustu tölunum í aftasta dálki ber ekki nógu vel saman, svo það
er vafasamt hvort talan :math:`1.618` er rétta samleitnistigið.

Ef :math:`(x_n)` er samleitin af stigi :math:`\alpha`, þá gildir
:math:`\lim_{n\to \infty}|e_{n+1}|/|e_n|^\alpha=\lambda`, þar sem
:math:`\lambda>0`. Þar með höfum við nálgunarjöfnu ef :math:`n` er nógu
stórt,

.. math::

   \dfrac{|e_{n+1}|}{|e_n|^\alpha} \approx
       \dfrac{|e_{n+2}|}{|e_{n+1}|^\alpha}
       \qquad \text{ þá og því aðeins að } \qquad 
       \dfrac{|e_{n+1}|}{|e_{n+2}|} \approx
       \bigg|\dfrac{e_{n}}{e_{n+1}} \bigg|^\alpha.

Ef við lítum á þetta sem jöfnu og leysum út :math:`\alpha`, þá fáum við

.. math::

   \alpha_n = 
       \dfrac{\ln(|e_{n+1}|/|e_{n+2}|)}{\ln(|e_{n}|/|e_{n+1}|)}.

Við getum reiknað út þrjú gildi á :math:`\alpha` úr þeim gögnum sem við
höfum, :math:`\alpha_0= 1.479`, :math:`\alpha_1 = 1.573` og
:math:`\alpha_2=1.660`.

Ef við endurtökum útreikninga okkar hér að framan með :math:`1.660` í
stað :math:`1.618`, þá fæst

+-------------+---------------------+---------------------------------+-----------------------------------+
| :math:`n`   | :math:`p_n`         | :math:`|e_n|`                   | :math:`|e_n|/|e_{n-1}|^{1.660}`   |
+=============+=====================+=================================+===================================+
| 0           | 2.000000000000000   | 3.3333\ :math:`\cdot 10^{-1}`   |                                   |
+-------------+---------------------+---------------------------------+-----------------------------------+
| 1           | 1.666666666666667   | 6.0606\ :math:`\cdot 10^{-2}`   | 3.7551\ :math:`\cdot 10^{-1}`     |
+-------------+---------------------+---------------------------------+-----------------------------------+
| 2           | 1.727272727272727   | 4.8701\ :math:`\cdot 10^{-3}`   | 5.1143\ :math:`\cdot 10^{-1}`     |
+-------------+---------------------+---------------------------------+-----------------------------------+
| 3           | 1.732142857142857   | 9.2177\ :math:`\cdot 10^{-5}`   | 6.3639\ :math:`\cdot 10^{-1}`     |
+-------------+---------------------+---------------------------------+-----------------------------------+
| 4           | 1.732050680431722   | 1.2713\ :math:`\cdot 10^{-7}`   | 6.3639\ :math:`\cdot 10^{-1}`     |
+-------------+---------------------+---------------------------------+-----------------------------------+
| 5           | 1.732050807565499   |                                 |                                   |
+-------------+---------------------+---------------------------------+-----------------------------------+

Tölunum neðst í aftasta dálki ber saman með fimm réttum stöfum og því
ályktum við að :math:`1.660` sé nær því að vera rétta samleitnistigið.


.. end-toggle::

Meira um skekkjur
-----------------

.. index::
    markverðir stafir

Skilgreining: Markverðir stafir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`r\neq 0`, þá segjum við að :math:`x` sé
*nálgun á* :math:`r` *með* :math:`t` *markverðum stöfum (e. significant
digits)* ef

.. math:: \frac{|r-x|}{|r|} \leq 10^{-t}.

Getum útfært þetta aðeins ítarlegra. Ef

.. math:: 10^{-(t+1)} < \frac{|r-x|}{|r|} \leq 10^{-t}.

þá segjum við að nálgunin á :math:`r` með :math:`x` sé rétt með að
minnsta kosti :math:`t` markverðum stöfum og að hámarki með :math:`t+1`
markverðum stöfum.

Athugið að ef :math:`e` er minnsta heila talan þannig að
:math:`|r|<10^e`, þá gefur seinni ójafnan matið

.. math:: |r-x| = 0.0\dots 0 a_t a_{t+1}\ldots \ \cdot\  10^e,

þar sem núllin aftan við punkt eru :math:`t` talsins.

Einnig er hægt að útfæra þetta fyrir aðrar grunntölur en 10.


.. index::
	skekkja; styttingarskekkja
	annars stigs jafna

Úrlausn annars stigs jöfnu
~~~~~~~~~~~~~~~~~~~~~~~~~~

Þegar núllstöðvar annars stigs jöfnunnar :math:`ax^2+bx+c=0` eru
reiknaðar út úr formúlunni

.. math:: x = \dfrac{-b\pm\sqrt{b^2-4ac}}{2a},

verður til styttingarskekkja ef :math:`b^2` er miklu stærra heldur en
:math:`4ac` vegna :math:`|b|\approx\sqrt{b^2-4ac}`. Við komumst hjá
þessum vandræðum með því að líta á margliðuna fullþáttaða
:math:`a(x-x_1)(x-x_2)` og notfæra okkur að núllstöðvarnar :math:`x_1`
og :math:`x_2` uppfylla :math:`x_1x_2=c/a`.

Ef :math:`b>0`, þá reiknum við :math:`x_1` fyrst út úr formúlunni

.. math::

   x_1 = \dfrac{-b-\sqrt{b^2-4ac}}{2a}
       \quad \text{ og  síðan } \quad
       x_2 = \dfrac{c/a}{x_1}.

Ef aftur á móti :math:`b<0`, þá reiknum við fyrst :math:`x_1` út úr
formúlunni

.. math::

   x_1 = \dfrac{-b+\sqrt{b^2-4ac}}{2a} 
       \qquad \text{ og síðan } \qquad 
       x_2 = \dfrac{c/a}{x_1}.

Ef :math:`b^2\approx 4ac` þá lendum við í styttingarskekkjum, en við
neyðumst til þess að lifa með þeim.

.. index::
	skekkja; gagnaskekkja

Áhrif gagnaskekkju
~~~~~~~~~~~~~~~~~~

Hugsum okkur að við séum að finna nálgun á núllstöð falls
:math:`x\mapsto f(x,\alpha)`. Við viljum finna nálgun :math:`x` á
lausninni :math:`r=r(\alpha)` sem uppfyllir

.. math:: f(r,\alpha) = 0

og við lítum á :math:`\alpha` sem stika (t.d. náttúrulegur fasti).

Gerum ráð fyrir að :math:`\alpha_0` sé nálgun á :math:`\alpha` og að við
þekkjum nálgun á :math:`r(\alpha_0)` sem er lausn á jöfnunni
:math:`f(x,\alpha_0)=0`.

Við viljum athuga hversu mikil áhrif nálgun á :math:`\alpha` með
:math:`\alpha_0` hefur á lausnina okkar, þ.e. við þurfum að meta
skekkjuna :math:`r(\alpha)-r(\alpha_0)`.

Ef við gefum okkur að :math:`f` sé samfellt deildanlegt í grennd um
punktinn :math:`(x_0,\alpha_0)`, þar sem :math:`x_0=r(\alpha_0)` og
:math:`{\partial}_xf(x_0,\alpha_0)\neq 0`, þá segir setningin um fólgin
föll að til sé grennd :math:`I` um punktinn :math:`\alpha_0` í
:math:`{\mathbb  R}` og samfellt deildanlegt fall
:math:`r:I\to {\mathbb  R}`, þannig að :math:`r(\alpha_0)=x_0` og
:math:`f(r(\alpha),\alpha)=0` fyrir öll :math:`\alpha\in I`.

Með öðrum orðum má segja að við getum alltaf leyst jöfnuna
:math:`f(x,\alpha)=0` með tilliti til :math:`x` þannig að út komi lausn
:math:`x=r(\alpha)` sem er samfellt diffranlegt fall af :math:`\alpha`.

Keðjureglan gefur okkur nú gildi afleiðunnar, því af jöfnunni
:math:`f(r(\alpha),\alpha)=0` leiðir að fallið
:math:`I \ni \alpha \mapsto f(r(\alpha),\alpha)` er fast, þannig að

.. math::

   0 =\frac {\partial}{\partial \alpha}f(r(\alpha),\alpha) = f_x'(r(\alpha), \alpha)\cdot r'(\alpha) 
       + f_{\alpha}'(r(\alpha),
       \alpha).

Þetta gefur

.. math::

   r'(\alpha) = \frac{-f_{\alpha}'(r(\alpha),\alpha)}
           {f_x'(r(\alpha),\alpha)}.

Nú látum við :math:`e` tákna skekkjuna í nálguninni á :math:`\alpha` með
:math:`\alpha_0`, :math:`e=\alpha-\alpha_0`. Þá fáum við skekkjumatið

.. math::

   r(\alpha) - r(\alpha_0) \approx r'(\alpha_0)\cdot e 
       = \frac{-f_{\alpha}'(r(\alpha_0),\alpha_0)}
           {f_x'(r(\alpha_0),\alpha_0)}\cdot e

og jafnframt mat á hlutfallslegri skekkju

.. math::

   \dfrac{|r(\alpha) - r(\alpha_0)|}
       {|r(\alpha)|} \approx \frac{|f_{\alpha}'(r(\alpha_0),\alpha_0)|}
       {|r(\alpha_0)f_x'(r(\alpha_0),\alpha_0)|}\cdot
       |e|.

Sýnidæmi
~~~~~~~~

Við skulum nú líta á það verkefni að finna nálgun á minnstu jákvæðu
lausn jöfnunnar :math:`\sin(\pi x)=1-e^{-x}`, þar sem við gerum ráð
fyrir því að þurfa að nálga :math:`\pi` með :math:`3.14`.

Okkur eru gefnar niðurstöður úr nálguninni með einhverri aðferð. Við
setjum :math:`f(x,\alpha)=1-e^{-x}-\sin(\alpha x)` og fáum

+-------------+--------------------+-------------------------+-------------------------------------------------+
| :math:`n`   | :math:`x_n`        | :math:`|x_{n+1}-x_n|`   | :math:`\frac{|x_{n+1}-x_n|}{|x_n-x_{n-1}|^2}`   |
+=============+====================+=========================+=================================================+
| 0           |                    |                         | 0.8                                             |
+-------------+--------------------+-------------------------+-------------------------------------------------+
| 1           | 0.81276894538752   | 0.00014017936338        | 0.8597                                          |
+-------------+--------------------+-------------------------+-------------------------------------------------+
| 2           | 0.81262876602414   | 0.00000001621651        | 0.8253                                          |
+-------------+--------------------+-------------------------+-------------------------------------------------+
| 3           | 0.81262874980763   | 0.00000000000000        | 0.8444                                          |
+-------------+--------------------+-------------------------+-------------------------------------------------+

Hér er :math:`\alpha=\pi` og :math:`\alpha_0=3.14` og þar með
:math:`|e|<0.0016`.

Hlutafleiðurnar eru :math:`f'_x(x,\alpha)=e^{-x}-\alpha\cos(\alpha x)`
og :math:`f'_\alpha(x,\alpha)=-x\cos(\alpha x)`.

Við stingum tölunum okkar inn í matið og notum punktinn
:math:`(x_3,\alpha_0)=(0.8126,3.14)`. Það gefur

.. math::

   \begin{aligned}
       r(\pi)-r(3.14)&\approx r'(3.14) \cdot e\\
       &\approx
       \dfrac{|0.8126\cdot \cos(0.8126\cdot 3.14)|}{|e^{-0.8126}-3.14
       \cdot \cos(0.8126 \cdot 3.14)|}\ 
       0.0016 \\
       &\approx 0.4\cdot 10^{-3}\end{aligned}

Þetta mat segir okkur að við eigum að gera ráð fyrir að áhrif
gagnaskekkjunnar séu þau að við fáum lausn með þremur réttum stöfum,
:math:`r(\pi) \approx 0.813`. Nálgun okkar á minnstu jákvæðu lausn
jöfnunnar :math:`\sin(\pi
x)=1-e^{-x}` er því :math:`0.813`.

.. index::
	O-ritháttur

:math:`O`-ritháttur
~~~~~~~~~~~~~~~~~~~

Látum :math:`f` og :math:`g` vera tvö föll sem skilgreind eru á bili
:math:`I \subset
\mathbb{R}` og látum :math:`c` vera tölu á :math:`I` eða annan hvorn
endapunkt :math:`I`.

Við segjum að :math:`f(t)` *sé stórt O af* :math:`g(t)` og skrifum

.. math:: f(t) = O(g(t)), \qquad t \rightarrow c,

ef til er fasti :math:`C>0` þannig að ójafnan

.. math:: |f(t)| \leq C|g(t)|

gildi fyrir öll :math:`t` í einhverri grennd um :math:`c`.

Athugið að grennd um :math:`c=+\infty` er bil af gerðinni
:math:`]\alpha,+\infty[` og grennd um :math:`c=-\infty` er bil af
gerðinni :math:`]-\infty,\alpha[`.

:math:`O`-ritháttur og skekkja í Taylor-nálgnum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Oft er :math:`O`-ritháttur notaður þegar fjallað er um skekkjur í
Taylor-nálgunum,

.. math::

   \begin{aligned}
       f(x) - T_n f(x;c) &= f(x) - f(c) - f'(x-c) - \cdots 
       - \frac{f^{(n)}(c)}{n!}(x-c)^n \\
       &= \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-c)^{n+1} =
       O\big((x-c)^{n+1}\big),  \quad x \to c\end{aligned}

Sýnidæmi
~~~~~~~~

Það eru til haugar af dæmum, sem við þekkjum vel.

Setning Taylors gefur okkur:

.. math::

   \begin{gathered}
       x - \sin x = O(x^3), \quad x \to 0\\
       x - \frac{x^3}{3!} - \sin x = O(x^5), \quad x \to 0\end{gathered}

.. index::
	O-ritháttur

:math:`O`-ritháttur fyrir runur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum nú :math:`(a_n)` og :math:`(b_n)` vera tvær talnarunur. Við segjum
að :math:`a_n` *sé stórt O af* :math:`b_n` og skrifum

.. math:: a_n = O(b_n),

ef til er fasti :math:`C>0` þannig að ójafnan

.. math:: |a_n| \leq C|b_n|

gildi fyrir öll :math:`n=0,1,2,3,\dots`.

Tvö sýnidæmi
~~~~~~~~~~~~

-  Út frá Taylor-röðinni fyrir :math:`\cos x` fáum við að

   .. math:: \cos(1/n)-1+1/(2n^2) = O(1/n^4)

-  Út frá

   .. math:: \sqrt{n+1}-\sqrt n = \dfrac{1}{\sqrt{n+1}+\sqrt n} \leq \frac{1}{2\sqrt n}

   sjáum við að

   .. math:: \sqrt{n+1}-\sqrt n = O\big(\dfrac 1{\sqrt n}\big)

Fleytitalnakerfið
-----------------

.. index::
	fleytitölur

Framsetning á tölum
~~~~~~~~~~~~~~~~~~~

Ef :math:`r` er rauntala frábrugðin :math:`0` og :math:`\beta` er
náttúrleg tala, :math:`2` eða stærri, þá er til einhlýtt ákvörðuð
framsetning á :math:`r` af gerðinni

.. math::

   r = 
       \pm (0.d_1d_2\dots d_kd_{k+1}\dots)_\beta\times \beta^e

þar sem :math:`e` er heiltala og :math:`d_j` eru heiltölur

-  :math:`1\leq d_1<\beta`,

-  :math:`0\leq d_j<\beta`, :math:`j=2,3,4,\dots`.

Tölvur reikna ýmist í *tvíundarkerfi* með :math:`\beta=2` eða í
*sextánundarkerfi* með :math:`\beta=16`, en við mannfólkið með okkar tíu
fingur reiknum í *tugakerfi* með :math:`\beta=10`.

.. index::
	fleytitölur; mantissa
	fleytitölur; markverðir stafir

Mantissa
~~~~~~~~

Formerkið og runan

.. math::

   \pm(0.d_1d_2\dots d_kd_{k+1}\dots)_\beta =
       \pm\sum_{j=1}^\infty \dfrac{d_j}{\beta^j}

nefnist *mantissa* tölunnar :math:`r`.

Við skrifum

.. math::

   (0.d_1d_2\dots d_k)_\beta = 
       \sum_{j=1}^k \dfrac{d_j}{\beta^j}

ef :math:`d_{k+1} = d_{k+2} = \cdots = 0` og segjum þá að talan
:math:`r` hafi :math:`k`-stafa mantissu.

Markverðir :math:`\beta`-stafir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef rauntalan :math:`x` er nálgun á :math:`r`, þá segjum við að :math:`x`
sé nálgun á :math:`r` með *að minnsta kosti* :math:`t` *markverðum*
:math:`\beta` *-stöfum* ef

.. math:: \dfrac{|r-x|}{|r|}\leq \beta^{-t}.

Ef við höfum að auki að

.. math:: \beta^{-t-1}<\dfrac{|r-x|}{|r|}\leq \beta^{-t}.

þá segjum við að :math:`x` sé nálgun á :math:`r` með :math:`t`
*markverðum* :math:`\beta` *-stöfum*.

Athugið að ef :math:`e` er minnsta heila talan þannig að
:math:`|r|<\beta^e`, þá gefur seinni ójafnan matið

.. math:: |r-x| = (0.0\dots 0a_ta_{t+1}\dots)_\beta \times \beta^e,

þar sem núllin aftan við punkt eru :math:`t` talsins.

.. index::
	afrúningur
	afskurður

Afrúningur talna
~~~~~~~~~~~~~~~~

Ef :math:`r` er sett fram á stöðluðu :math:`\beta`-fleytitöluformi, þá
nefnist talan

.. math:: x = (\pm 0.d_1d_2\dots d_k)_\beta\times \beta^e

*afskurður tölunnar* :math:`r` *við* :math:`k` *-ta aukastaf* :math:`r`, en
talan

.. math::

   x = \begin{cases} 
       \pm (0.d_1d_2\dots d_k)_\beta\times \beta^e, & 
       d_{k+1}<\beta/2,\\
       \pm ((0.d_1d_2\dots d_k)_\beta+\beta^{-k})\times \beta^e,
       &d_{k+1}\geq \beta/2.
       \end{cases}

nefnist *afrúningur tölunnar* :math:`r` *við* :math:`k` *-ta aukastaf*.

Við köllum þessar aðgerðir *afskurð* (e. chopping) og *afrúning*
(e. rounding).

Fleytitölukerfi
~~~~~~~~~~~~~~~

*Fleytitölukerfi* er endanlegt hlutmengi í :math:`{\mathbb  R}`, sem
samanstendur af öllum tölum

.. math:: \pm (0.d_1d_2\dots d_k)_\beta\times \beta^e

þar sem :math:`d_j` eru heiltölur eins og áður var lýst, :math:`k` er
föst tala og við höfum mörk á veldisvísinum :math:`m\leq e\leq M`.

Allar tölvur vinna með eitthvert fleytitölukerfi, oftast með grunntölu
:math:`\beta=2` eða :math:`\beta=16` eins og áður sagði.

Eftir hverja aðgerð í tölvunni þarf að nálga útkomuna með *afskurði* eða
*afrúningu*.

Ef við förum ekki varlega þá getur þetta magnað upp skekkju.

Sjá `Úrlausn annars stigs jöfnu`_.

IEEE staðlar
~~~~~~~~~~~~

-  Single: :math:`\beta = 2, k=24, m=-125` og :math:`M = 128`,

-  Double: :math:`\beta = 2, k=53, m=-1021` og :math:`M = 1024`.

Útreikningur í tugakerfi
~~~~~~~~~~~~~~~~~~~~~~~~

Þegar reiknað er í tugakerfi er tölurnar afrúnaðar við :math:`k`-ta
aukastaf ef skekkjan í nálgun á þeim er minni en
:math:`\frac 12\times 10^{-k}`. Ef

.. math:: \dfrac{|r-x|}{|r|}<10^{-k-1}

þá treystum við öllum :math:`k` stöfum mantissunnar, en ef

.. math:: \dfrac{|r-x|}{|r|}>10^{-k+q},

þá eru síðustu :math:`q` stafir mantissunnar marklausir auk þess sem
vænta má nokkurs fráviks í :math:`d_{k-q}`.
