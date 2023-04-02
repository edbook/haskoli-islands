Eigingildisverkefni
===================

- *You can't give her that! It's not safe!*
- *It's a sword. They're not meant to be safe.*
- *She's a child!*
- *It's educational.*
- *What if she cuts herself?*
- *That will be an important lesson.*

-- Terry Pratchett, `Hogfather <http://adi-fitri.tumblr.com/post/105355206099/its-a-sword-its-not-meant-to-be-safe-my>`_

.. index::
    eigingildi
    eiginvigur

Eigingildi og eiginvigrar
-------------------------

Nálgun á eigingildum og eiginvigrum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Skilgreining** Látum :math:`A` vera :math:`n\times n` fylki. Munum að
:math:`\lambda\in {{\mathbb  C}}` nefnist *eigingildi* fylkisins
:math:`A` ef til er
:math:`{\mbox{${\bf v}$}}\in {{\mathbb  C}}^n\setminus\{{\mbox{${\bf 0}$}}\}`
þannig að

.. math:: A{\mbox{${\bf v}$}}=\lambda{\mbox{${\bf v}$}}.

Vigurinn :math:`{\mbox{${\bf v}$}}` nefnist þá *eiginvigur* fylkisins
:math:`A` og við segjum að hann svari til eigingildisins
:math:`\lambda`.

.. note::
    Eigingildi fylkisins :math:`A` eru nákvæmlega núllstöðvar
    kennimargliðunnar

    .. math:: p_A(z)=\det(zI-A), \qquad z\in {{\mathbb  C}}.

.. note::
    Ef :math:`{\mbox{${\bf v}$}}` er eiginvigur fylkisins
    :math:`A`, þá er :math:`\alpha {\mbox{${\bf v}$}}` einnig eiginvigur
    fyrir sérhvert
    :math:`\alpha\in {{\mathbb  C}}\setminus \{{\mbox{${\bf 0}$}}\}`.

.. index::
    skífusetning Gerschgorins
    eigingildi; skífusetning Gerschgorins

Gróf staðsetning á eigingildum: Skífusetning Gerschgorins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skilgreinum

.. math:: r_i=\sum\limits_{{\substack{j=1 \\ j\neq i}}}^n|a_{ij}|,

sem er summan af tölugildum stakanna í línu :math:`i` *utan
hornalínunnar* og látum

.. math:: R_i=\{z\in {{\mathbb  C}}\,;\, |z-a_{ii}|\leq r_i\}

tákna skífuna með miðju í :math:`a_{ii}` og geislann :math:`r_i`. Þá
gildir

#. Öll eigingildi :math:`A` liggja í sammengi skífanna :math:`R_i`.

#. Ef :math:`k` af skífunum :math:`R_i` mynda samanhangandi svæði
   :math:`U` í :math:`{{\mathbb  C}}` sem er sundlægt við hinar
   :math:`n-k` skífurnar, þá inniheldur :math:`U` nákvæmlega :math:`k`
   eigingildi.

Fylgisetning
~~~~~~~~~~~~

Athugum fyrst að þar sem einingarfylkið er samhverft þá er 
:math:`\det(A^T-\lambda I) = \det(A-\lambda I)` og þar af leiðandi
eru eigingildi :math:`A^T` og :math:`A` þau sömu.

Með því að beita Skífusetningu Gerschgorins á fylkið :math:`A^T`
fæst að við getum notað skífur með geisla sem eru 
sumur tölugilda stakanna í hverjum dálki að hornalínunni
undanskilinni. Þetta fæst af því að 
summa yfir línu í :math:`A^T` jafngildir summu yfir dálk 
í :math:`A`.

Nánar tiltekið, ef 

.. math:: 
    c_i=\sum\limits_{{\substack{j=1 \\ j\neq i}}}^n|a_{ji}|,\\
    C_i=\{z\in {{\mathbb  C}}\,;\, |z-a_{ii}|\leq c_i\}

þá gildir að

#. Öll eigingildi :math:`A` liggja í sammengi skífanna :math:`C_i`.

#. Ef :math:`k` af skífunum :math:`C_i` mynda samanhangandi svæði
   :math:`U` í :math:`{{\mathbb  C}}` sem er sundlægt við hinar
   :math:`n-k` skífurnar, þá inniheldur :math:`U` nákvæmlega :math:`k`
   eigingildi.

Dæmi: Setning Gerschgorins
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sagecell::
    :auto: 
    :hidecode:  
    :codefile: gerschgorin.sage
    :img: gerschgorin.png
    :imgwidth: 8 cm


.. index::
    eiginvigur; grunnur
    hornalínugeranlegt
    

Eiginvigragrunnar
~~~~~~~~~~~~~~~~~

Nokkrar staðreyndir um eigingildi og eiginvigra:

#. Eiginvigrar sem svara til ólíkra eigingilda eru línulega óháðir.

#. Eiginvigrar sem svara til eins ákveðins eigingildis :math:`\lambda`
   spanna hlutrúm í :math:`{{\mathbb  C}}^n`.

#. Við segjum að fylkið :math:`A` sé *hornalínugeranlegt* ef til eru
   eigingildi :math:`\lambda_1,\lambda_2,\dots,\lambda_n` og tilsvarandi
   eiginvigrar
   :math:`{\mbox{${\bf v}$}}_1,{\mbox{${\bf v}$}}_2,\dots,{\mbox{${\bf v}$}}_n`
   sem mynda grunn í :math:`{{\mathbb  R}}^n`.Þá er hægt að skrifa

   .. math:: A=T\Lambda T^{-1}

   þar sem :math:`\Lambda` er hornalínufylki með eigingildin
   :math:`\lambda_1,\dots,\lambda_n` á hornalínunni og :math:`T` er
   :math:`n\times n` fylki þannig að dálkur nr. \ :math:`k` í því
   samanstendur af hnitum :math:`{\mbox{${\bf v}$}}_k` miðað við
   staðalgrunninn í :math:`{{\mathbb  R}}^n`.

#. Ef fylkið :math:`A` er samhverft, þá er það hornalínugeranlegt.

.. index::
    eigingildi; veldaaðferð

Veldaaðferð
-----------

Veldaaðferð
~~~~~~~~~~~

Hugsum okkur nú að við :math:`A` sé hornalínugeranlegt og að við röðum
eigingildunum á hornalínu :math:`\Lambda` í minnkandi röð eftir
tölugildi

.. math:: |\lambda_1|\geq |\lambda_2|\geq \cdots\geq |\lambda_n|

Tökum einhvern vigur :math:`{\mbox{${\bf x}$}}^{(0)}` og lítum á liðun
hans í eiginvigra

.. math:: {\mbox{${\bf x}$}}^{(0)}=\alpha_1{\mbox{${\bf v}$}}_1+\cdots+\alpha_n{\mbox{${\bf v}$}}_n

Skilgreinum síðan rununa :math:`\big({\mbox{${\bf x}$}}^{(m)}\big)` með
ítruninni

.. math:: {\mbox{${\bf x}$}}^{(m)}=A{\mbox{${\bf x}$}}^{(m-1)}.

Við fáum þá

.. math::

   \begin{aligned}
   {\mbox{${\bf x}$}}^{(1)} =A{\mbox{${\bf x}$}}^{(0)}&=\alpha_1A{\mbox{${\bf v}$}}_1+\cdots+\alpha_nA{\mbox{${\bf v}$}}_n\\
   &=\alpha_1\lambda_1{\mbox{${\bf v}$}}_1+\cdots+\alpha_n\lambda_n{\mbox{${\bf v}$}}_n,\end{aligned}

.. math::

   \begin{aligned}
   {\mbox{${\bf x}$}}^{(2)}=A{\mbox{${\bf x}$}}^{(1)}&=\alpha_1\lambda_1A{\mbox{${\bf v}$}}_1+\cdots+\alpha_n\lambda_nA{\mbox{${\bf v}$}}_n,\\
   &=\alpha_1\lambda_1^2{\mbox{${\bf v}$}}_1+\cdots+\alpha_n\lambda_n^2{\mbox{${\bf v}$}}_n\\ 
   \vdots & \\
   {\mbox{${\bf x}$}}^{(m)}&=\alpha_1\lambda_1^m{\mbox{${\bf v}$}}_1+\cdots+\alpha_n\lambda_n^m{\mbox{${\bf v}$}}_n\end{aligned}

Síðasti vigurinn gefur :math:`{\bf x}^{(m)} = A^m {\bf x}^{(0)}`

.. math::

   {\mbox{${\bf x}$}}^{(m)}=  \lambda_1^m 
   \big(\alpha_1{\mbox{${\bf v}$}}_1+(\lambda_2/\lambda_1)^m\alpha_2{\mbox{${\bf v}_2$}}_+\cdots+
   (\lambda_n/\lambda_1)^m \alpha_n{\mbox{${\bf v}$}}_n\big)

Hnit númer :math:`i` í þessum vigri er:

.. math::

   x_i^{(m)}=  \lambda_1^m 
   \big(\alpha_1v_{1,i}+(\lambda_2/\lambda_1)^m\alpha_2v_{2,i}+\cdots+
   (\lambda_n/\lambda_1)^m \alpha_nv_{n,i}\big)

Hugsum okkur nú að :math:`|\lambda_1|>|\lambda_2|`. Þá fæst:

.. math::

   \dfrac{x_i^{(m)}}{x_i^{(m-1)}}
   =
   \dfrac{\lambda_1^m\big(\alpha_1v_{1,i}+O((\lambda_2/\lambda_1)^m)\big)}
   {\lambda_1^{m-1}\big(\alpha_1v_{1,i}+O((\lambda_2/\lambda_1)^{m-1})\big)}

Ef við höfum :math:`\alpha_1v_{1,i}\neq 0`, þá er niðurstaðan

.. math::

   \dfrac{x_i^{(m)}}{x_i^{(m-1)}}
   =\lambda_1
   \dfrac{\big(1+O((\lambda_2/\lambda_1)^m)\big)}
   {\big(1+O((\lambda_2/\lambda_1))^{m-1}\big)} \to \lambda_1
   \quad \text{ þegar }  \quad m\to \infty.

Skoðum aftur

.. math::

   {\mbox{${\bf x}$}}^{(m)}=  \lambda_1^m 
   \big(\alpha_1{\mbox{${\bf v}$}}_1+(\lambda_2/\lambda_1)^m\alpha_2{\mbox{${\bf v}$}}_2+\cdots+
   (\lambda_n/\lambda_1)^m \alpha_n{\mbox{${\bf v}$}}_n\big)

Ef :math:`|\lambda_1|>|\lambda_2|`, þá gildir fyrir :math:`j > 1` að
:math:`(\lambda_j/\lambda_1)^m \to 0` þegar :math:`m \to \infty` og

.. math:: \lim_{m\to \infty} \frac{{\mbox{${\bf x}$}}^{(m)}}{\lambda_1^m} = \alpha_1 {\mbox{${\bf v}$}}_1.

Þannig að ef :math:`{\mbox{${\bf x}$}}^{(0)}` var valinn í upphafi
þannig að :math:`\alpha_1 \neq 0`, þá skilar þetta eiginvigrinum
:math:`\alpha_1{\mbox{${\bf v}$}}_1` fyrir eigingildið
:math:`\lambda_1`.

Reiknirit til þess að ákvarða stærsta eigingildi fylkis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Þegar við reiknum :math:`{\mbox{${\bf x}$}}^{m}` eins og hér að framan
þá er ekki ólíklegt að við lendum í undir- eða yfirflæðisvillum ef lengd
:math:`{\mbox{${\bf x}$}}` (skv. einhverjum staðli) stefnir á 0 eða
:math:`+\infty`. Til þess að ráða bót á þessu þá stöðlum við vigurinn í
hverju skrefi með :math:`\ell_\infty` staðlinum á eftirfarandi hátt.

Við veljum :math:`{\mbox{${\bf x}$}}^{(0)}` með einhverjum hætti og
skilgreinum síðan

.. math::

    {\bf x}^{(m)} = \frac{A{\bf x}^{(m-1)}}{\|A{\bf x}^{(m-1)}\|_\infty}.
    
Þetta jafngildir því að setja 

.. math::
   {\mbox{${\bf y}$}}^{(m)}=A{\mbox{${\bf x}$}}^{(m-1)}, \quad \text{ og svo } \quad
   {\mbox{${\bf x}$}}^{(m)}=\dfrac{{\mbox{${\bf y}$}}^{(m)}}{y_{p_m}^{(m)}} \qquad

þar sem :math:`p_m` er númerið á því hniti í vigrinum
:math:`{\mbox{${\bf y}$}}^{(m)}` sem hefur stærst tölugildi, það er hnit :math:`p_m` uppfyllir

.. math:: \|A{\bf x}^{m-1}\| = |y_{p_m}^{(m)}|=\|{\mbox{${\bf y}$}}^{(m)}\|_\infty=\max_{1\leq j\leq n}|y_j^{(m)}|.

Ef mörg númer uppfylla þetta skilyrði, þá tökum við bara :math:`p_m`
sem lægsta gildið á :math:`j` þar sem jafnaðarmerki gildir (það skiptir ekki máli
fyrir nálgunina á hvaða :math:`j` við veljum).

Þá fæst að 

.. math::
    \begin{aligned}
    {\bf x}^{(m)} 
    =& \frac{A{\bf x}^{(m-1)}}{y_{p_m}^{(m)}} \\
    =& \frac{A^2{\bf x}^{(m-2)}}{y_{p_m}^{(m)} \ y_{p_{m-1}}^{(m-1)}}\\
    =& \frac{A^3{\bf x}^{(m-3)}}{y_{p_m}^{(m)} \ y_{p_{m-1}}^{(m-1)} \ y_{p_{m-2}}^{(m-2)}}\\
    \vdots & \\
    =& \frac{A^m{\bf x}^{(0)}}{y_{p_m}^{(m)} \ \dots \ y_{p_{1}}^{(1)}}
    \end{aligned}

Með því að skrifa :math:`A^m{\bf x}^{(0)}` með eiginvigrum eins og hér fyrir ofan 

.. math::

   {\mbox{${\bf x}$}}^{(m)}=  \lambda_1^m 
   \big(\alpha_1{\mbox{${\bf v}$}}_1+(\lambda_2/\lambda_1)^m\alpha_2{\mbox{${\bf v}_2$}}_+\cdots+
   (\lambda_n/\lambda_1)^m \alpha_n{\mbox{${\bf v}$}}_n\big)

þá fæst

.. math::
    {\bf x}^{(m)} 
    = \frac{\lambda_1^m}{|y_{p_m}^{(m)}| \ \dots \ |y_{p_{1}}^{(1)}|}
   \big(\alpha_1{\mbox{${\bf v}$}}_1+(\lambda_2/\lambda_1)^m\alpha_2{\mbox{${\bf v}_2$}}_+\cdots+
   (\lambda_n/\lambda_1)^m \alpha_n{\mbox{${\bf v}$}}_n\big)

Stuðlarnir við :math:`{\bf v}_2,\ldots,{\bf v}_n` stefna allir á 0 þannig að það er ljóst að :math:`{\bf x}^{(m)}`
stefnir á eiginvigur sem tilheyrir :math:`\lambda_1`. Nánar tiltekið stefnir :math:`{\bf x}^{(m)}` á eiginvigur
sem hefur lengdina 1 í :math:`\ell_\infty` staðlinum, samkvæmt skilgreiningunni á :math:`{\bf x}^{(m)}`.

Þar sem :math:`{\bf x}^{(m)}` er um það bil eiginvigur þá er 
:math:`{\bf y}^{(m)} = A{\bf x}^{(m-1)} \approx \lambda_1 {\bf x}^{(m-1)}` sem segir okkur 
að ef við veljum :math:`p_{m-1}`-ta hnitið úr jöfnunni þá fæst 

.. math::
    y_{p_{m-1}}^{(m)} \approx \lambda_1
    
því :math:`p_{m-1}`-ta hnitið í :math:`{\bf x}^{(m-1)}` er 1. 

Samleitni
~~~~~~~~~

.. todo::
    Bæta við og laga undirkafla skiptingu

Nú kemur í ljós að :math:`y_{p_{m-1}}^{(m)}` stefnir á
:math:`\lambda_1`. Auk þess stefnir :math:`{\mbox{${\bf x}$}}^{(m)}` á
eiginvigur sem svarar til :math:`\lambda_1` og hefur lengdina :math:`1`
í :math:`l_\infty` staðlinum.

Í útreikningum skilgreinum við því rununa
:math:`\lambda^{(m)}=y_{p_{m-1}}^{(m)}`. Við gefum okkur síðan þolmörk á
skekkju :math:`TOL` og reiknum úr runurnar þar til eitt af
stoppskilyrðunum gildir:

.. math::

   \begin{aligned}
   |\lambda^{(m)}-\lambda^{(m-1)}|&<TOL \qquad \text{ eða } \\
   \|{\mbox{${\bf x}$}}^{(m)}-{\mbox{${\bf x}$}}^{(m-1)}\|&<TOL \qquad \text { eða } \\
   \|A{\mbox{${\bf x}$}}^{(m)}-\lambda^{(m)}{\mbox{${\bf x}$}}^{(m)}\|&<TOL.\end{aligned}

.. index::
    eigingildi; veldaaðferð fyrir samhverf fylki

Samhverf fylki
~~~~~~~~~~~~~~

Munum að ef :math:`A` er samhverft, þá hefur :math:`A` eiginvigragrunn
og eiginvigra sem svara til ólíkra eigingilda eru hornréttir.

Í þessu tilfelli er einfaldara að smíða reiknirit svona:

.. math::

   \begin{aligned}
     {\mbox{${\bf y}$}}^{(m)}&=A{\mbox{${\bf x}$}}^{(m-1)}\\
   \lambda^{(m)}&={{\mbox{${\bf x}$}}^{(m-1)}}^T{\mbox{${\bf y}$}}^{(m)}\\
   {\mbox{${\bf x}$}}^{(m)}&= \frac{{\mbox{${\bf y}$}}^{(m)}}{\sqrt{({\mbox{${\bf y}$}}^{(m)})^T{\mbox{${\bf y}$}}^{(m)}}}\end{aligned}

Samleitnin verður sú sama: :math:`\lambda^{(m)}` stefnir á stærsta
eigingildið og :math:`{\mbox{${\bf x}$}}^{(m)}` stefnir á tilsvarandi
eiginvigur.

Setning um eigingildi og eiginvigra 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum sem fyrr :math:`A` vera :math:`n\times n` fylki,
:math:`\lambda_1,\dots,\lambda_n` vera eigingildi og
:math:`{\mbox{${\bf v}$}}_1,\dots,{\mbox{${\bf v}$}}_n` vera tilsvarandi
eiginvigra.

#. Látum :math:`p(x)=a_0+a_1x+\cdots+a_mx^m` vera margliðu og
   skilgreinum :math:`n\times n` fylkið :math:`B` með því að stinga
   :math:`A` inn í :math:`p`,

   .. math:: B=p(A)=a_0I+a_1A+\cdots+a_mA^m

   Þá eru tölurnar :math:`p(\lambda_1),\dots,p(\lambda_n)` eigingildi
   fylkisins :math:`B=p(A)` með tilsvarandi eiginvigrum
   :math:`{\mbox{${\bf v}$}}_1,\dots,{\mbox{${\bf v}$}}_n`.

#. Ef :math:`A` er andhverfanlegt þá eru
   :math:`1/\lambda_1,\dots,1/\lambda_n` eigingildi :math:`A^{-1}` með
   tilsvarandi eiginvigrum
   :math:`{\mbox{${\bf v}$}}_1,\dots,{\mbox{${\bf v}$}}_n`.

Dæmi um veldaaðferð
~~~~~~~~~~~~~~~~~~~

Sjá vikublað 14.

.. todo:: Dæmi


.. index::
    eigingildi; andhverf veldaaðferð

Andhverf veldaaðferð
--------------------

Af síðustu setningu leiðir að fylkið :math:`B=(A-qI)^{-1}` hefur
eigingildin

.. math::

   \mu_1=\dfrac 1{\lambda_1-q},\ 
   \mu_2=\dfrac 1{\lambda_2-q},\ \cdots \  
   \mu_n=\dfrac 1{\lambda_n-q}.

Hugsum okkur nú að við viljum finna nálgunargildi fyrir eigingildið
:math:`\lambda_k` og að við vitum út frá setningu Gerschgorins skífunum
nokkurn veginn hvar það er staðsett.

Ef við erum með :math:`q` nógu nálægt :math:`\lambda_k`, þá verður
:math:`\mu_k` stærsta eigingildi fylkisins :math:`B=(A-qI)^{-1}`

Þá getum við beitt veldaaðferðinni til þess að búa til runu
:math:`\mu^{(m)}\to \mu_k` og við fáum að

.. math:: \lambda^{(m)}=\dfrac 1{\mu^{(m)}}+q\to \lambda_k.

Ef veldaaðferðinni er beitt á fylkið :math:`B=(A-qI)^{-1}` þá þurfum við
að reikna út
:math:`{\mbox{${\bf y}$}}^{(m)}=(A-qI)^{-1}{\mbox{${\bf x}$}}^{(m-1)}` í
hverju skrefi.

Þetta er gert þannig að fyrst framkvæmum við :math:`LU`-þáttun á fylkinu
:math:`LU=(A-qI)` og framkvæmum síðan for- og endurinnsetningu til þess
að leysa :math:`LU{\mbox{${\bf y}$}}^{(m)}=x^{(m-1)}`.

En tölulegar aðferðir fyrir LU-þáttun skoðuðum við í 
:ref:`kafla 8.2 <upphafsgildisverkefni>`.


Reiknirit til þess að nálga eigingildi og eiginvigra
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Takmarkið er að finna nálgun á eigingildinu :math:`\lambda_k`.

#. Finnum :math:`q\in {{\mathbb  R}}` sem liggur næst eigingildinu
   :math:`\lambda_k` af öllum eigingildum :math:`A`

#. Þáttum :math:`LU=A-qI`.

#. Við veljum :math:`{\mbox{${\bf x}$}}^{(0)}` með einhverjum hætti og
   leysum síðan :math:`{\mbox{${\bf y}$}}^{(m)}` út úr jöfnunni

   .. math:: LU{\mbox{${\bf y}$}}^{(m)}={\mbox{${\bf x}$}}^{(m-1)}.

#. Skilgreinum :math:`{\mbox{${\bf x}$}}^{(m)}={{\mbox{${\bf y}$}}^{(m)}}/{y_{p_m}^{(m)}}` þar sem :math:`p_m` er númerið á því hniti í
   :math:`{\mbox{${\bf y}$}}^{(m)}` sem hefur stærst tölugildi, sem
   þýðir að það hnit uppfyllir

   .. math:: |y_{p_m}^{(m)}|=\|{\mbox{${\bf y}$}}^{(m)}\|_\infty=\max_{1\leq j\leq n}|y_j^{(m)}|.

   Ef mörg númer uppfylla þetta skilyrði, þá tökum við bara :math:`p_m`
   sem lægsta gildið á :math:`j` þar sem jafnaðarmerki gildir.

Niðurstaðan verður að

.. math:: \lambda^{(m)}=\dfrac 1{y_{p_{m-1}}^{(m)}}+q \to \lambda_k

og :math:`{\mbox{${\bf x}$}}^{(m)}` stefnir á tilsvarandi eiginvigur.

Dæmi um öfuga veldaaðferð
~~~~~~~~~~~~~~~~~~~~~~~~~

Sjá vikublað 14.

.. todo:: Dæmi
