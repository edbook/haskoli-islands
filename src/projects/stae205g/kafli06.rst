Diffur- og heildareikningur vigursviða
==================================================

*A reader lives a thousand lives before he dies. The man who never reads lives only one.*

\- George R.R. Martin, A Dance with Dragons 




grad, div og curl
-----------------

.. index::
  nabla-virkinn

Skilgreining 
~~~~~~~~~~~~~

Skilgreinum *nabla*-virkjann sem diffurvirkja

.. math:: \displaystyle \nabla=\mbox{${\bf i}$}\,\frac{\partial}{\partial x}+\mbox{${\bf j}$}\,\frac{\partial}{\partial y}+\mbox{${\bf k}$}\,\frac{\partial}{\partial z}.

.. index::
  sundurleitni
  rót

Skilgreining 
~~~~~~~~~~~~~

Látum
:math:`\mbox{${\bf F}$}(x,y,z)=F_1(x,y,z)\,\mbox{${\bf i}$}+F_2(x,y,z)\,\mbox{${\bf j}$}+F_3(x,y,z)\,\mbox{${\bf k}$}`
vera vigursvið og :math:`\varphi(x,y,z)` vera fall.

Skilgreinum :hover:`stigul,stigull` :math:`\varphi` sem vigursviðið

.. math:: \displaystyle

   \mbox{${\rm\bf grad\,}$}\varphi=\nabla\varphi=\frac{\partial \varphi}{\partial x}\,\mbox{${\bf i}$}+
   \frac{\partial \varphi}{\partial y}\,\mbox{${\bf j}$}+\frac{\partial \varphi}{\partial z}\,\mbox{${\bf k}$}.

Skilgreinum :hover:`sundurleitni` vigursviðsins
:math:`\mbox{${\bf F}$}` sem

.. math:: \displaystyle \mbox{${\rm\bf div\,}$}\mbox{${\bf F}$}=\nabla\cdot\mbox{${\bf F}$}=\frac{\partial F_1}{\partial x}+\frac{\partial F_2}{\partial y}+\frac{\partial F_3}{\partial z}.

Skilgreinum :hover:`rót` vigursviðsins :math:`\mbox{${\bf F}$}` sem

.. math:: \displaystyle

   \begin{aligned}
    \mbox{${\rm\bf curl\,}$}\mbox{${\bf F}$}&=\nabla\times\mbox{${\bf F}$}=\begin{vmatrix} \mbox{${\bf i}$}&\mbox{${\bf j}$}&\mbox{${\bf k}$}\\
    \frac{\partial} {\partial x}&\frac{\partial}{\partial y}&\frac{\partial}{\partial z}\\F_1&F_2&F_3\end{vmatrix} \\ &=\bigg(\frac{\partial F_3}{\partial y}-\frac{\partial F_2}{\partial z}\bigg)\,\mbox{${\bf i}$}+\bigg(\frac{\partial F_1}{\partial z}-\frac{\partial F_3}{\partial x}\bigg)\,\mbox{${\bf j}$}+\bigg(\frac{\partial F_2}{\partial x}-\frac{\partial F_1}{\partial y}\bigg)\,\mbox{${\bf k}$}. 
    \end{aligned}

.. warning::

   Ef :math:`\varphi(x,y,z)` er fall þá er :math:`\nabla \varphi(x,y,z)` stigullinn af :math:`\varphi(x,y,z)` en :math:`\varphi(x,y,z)\nabla` er :hover:`diffurvirki`.

.. warning::

   Sundurleitnin :math:`\mbox{${\rm\bf div\,}$}\mbox{${\bf F}$}` er fall :math:`{\mathbb  R}^3\rightarrow{\mathbb  R}` en rótið :math:`\mbox{${\rm\bf curl\,}$}\mbox{${\bf F}$}` er vigursvið :math:`{\mathbb  R}^3\rightarrow{\mathbb  R}^3`.

Skilgreining 
~~~~~~~~~~~~~

Látum
:math:`\mbox{${\bf F}$}(x,y)=F_1(x,y)\,\mbox{${\bf i}$}+F_2(x,y)\,\mbox{${\bf j}$}`
vera vigursvið. Skilgreinum :hover:`sundurleitni` :math:`\mbox{${\bf F}$}` sem

.. math:: \displaystyle

   \mbox{${\rm\bf div\,}$}\mbox{${\bf F}$}=\nabla\cdot\mbox{${\bf F}$}=\frac{\partial F_1}{\partial
     x}+\frac{\partial F_2}{\partial y}.

og :hover:`rót` :math:`\mbox{${\bf F}$}` skilgreinum við sem

.. math:: \displaystyle

   \mbox{${\rm\bf curl\,}$}\mbox{${\bf F}$}=\bigg(\frac{\partial F_2}{\partial x}-\frac{\partial
     F_1}{\partial y}\bigg)\,\mbox{${\bf k}$}.

Reiknireglur 
~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`\mbox{${\bf F}$}` og :math:`\mbox{${\bf G}$}`
séu vigursvið og :math:`\varphi` og :math:`\psi` föll. Gerum ráð fyrir
að þær hlutafleiður sem við þurfum að nota séu skilgreindar og
samfelldar.

(a) :math:`\nabla(\varphi\psi)=\varphi\nabla\psi+\psi\nabla\varphi`.

(b)
:math:`\nabla\cdot(\varphi\mbox{${\bf F}$})=(\nabla\varphi)\cdot\mbox{${\bf F}$}+\varphi(\nabla\cdot\mbox{${\bf F}$})`.

(c)
:math:`\nabla\times(\varphi\mbox{${\bf F}$})=(\nabla\varphi)\times\mbox{${\bf F}$}+\varphi(\nabla\times\mbox{${\bf F}$})`.

(d)
:math:`\nabla\cdot(\mbox{${\bf F}$}\times\mbox{${\bf G}$})=(\nabla\times\mbox{${\bf F}$})\cdot\mbox{${\bf G}$}-\mbox{${\bf F}$}\cdot(\nabla\times\mbox{${\bf G}$})`.

(e)
:math:`\nabla\times(\mbox{${\bf F}$}\times\mbox{${\bf G}$})=(\nabla\cdot\mbox{${\bf G}$})\mbox{${\bf F}$}+(\mbox{${\bf G}$}\cdot\nabla)\mbox{${\bf F}$}-(\nabla\cdot\mbox{${\bf F}$})\mbox{${\bf G}$}-(\mbox{${\bf F}$}\cdot\nabla)\mbox{${\bf G}$}`.

(f)
:math:`\nabla(\mbox{${\bf F}$}\cdot\mbox{${\bf G}$})=\mbox{${\bf F}$}\times(\nabla\times \mbox{${\bf G}$})+\mbox{${\bf G}$}\times(\nabla\times \mbox{${\bf F}$})+(\mbox{${\bf F}$}\cdot\nabla)\mbox{${\bf G}$}+(\mbox{${\bf G}$}\cdot\nabla)\mbox{${\bf F}$}`.

(g)
:math:`\nabla\cdot(\nabla\times \mbox{${\bf F}$})=0\qquad\qquad\mbox{${\rm\bf div\,}$}\mbox{${\rm\bf curl\,}$}=0`

(h)
:math:`\nabla\times(\nabla\varphi)=\mbox{${\bf 0}$}\qquad\qquad\mbox{${\rm\bf curl\,}$}\mbox{${\rm\bf grad\,}$}=\mbox{${\bf 0}$}`

(i)
:math:`\nabla\times(\nabla\times \mbox{${\bf F}$})=\nabla(\nabla\cdot\mbox{${\bf F}$})-\nabla^2\mbox{${\bf F}$}`.

.. index::
  sundurleitnilaus
  uppsprettulaus
  rótlaus
  
Skilgreining 
~~~~~~~~~~~~~

Látum :math:`\mbox{${\bf F}$}` vera vigursvið skilgreint á svæði
:math:`D`.

(a) Vigursviðið :math:`\mbox{${\bf F}$}` er sagt vera
:hover:`sundurleitnilaust,uppsprettulaus` eða *uppsprettulaust* ef
:math:`\mbox{${\rm\bf div\,}$}\mbox{${\bf F}$}=0` i öllum punktum
:math:`D`.

(b) Vigursviðið :math:`\mbox{${\bf F}$}` er sagt vera :hover:`rótlaust,rótlaus`
ef :math:`\mbox{${\rm\bf curl\,}$}\mbox{${\bf F}$}=\mbox{${\bf 0}$}` á öllu
:math:`D`.

.. note::
   Vigursvið :math:`\mbox{${\bf F}$}(x,y,z)=F_1(x,y,z)\,\mbox{${\bf i}$}+F_2(x,y,z)\,\mbox{${\bf j}$}+F_3(x,y,z)\,\mbox{${\bf k}$}` er rótlaust ef og aðeins ef

   .. math:: \displaystyle
      \frac{\partial F_1}{\partial y}=
      \frac{\partial F_2}{\partial x},\quad
      \frac{\partial F_1}{\partial z}=
      \frac{\partial F_3}{\partial x},\quad
      \frac{\partial F_2}{\partial z}=
      \frac{\partial F_3}{\partial y}.

Setning 
~~~~~~~~

(a) Rót vigursviðs er :hover:`sundurleitnilaus,uppsprettulaus`.

(b) Stigulsvið er :hover:`rótlaust,rótlaus`.


.. index::
  stjörnusvæði

Skilgreining 
~~~~~~~~~~~~~

Svæði :math:`D` í rúmi eða plani kallast :hover:`stjörnusvæði` ef til er
punktur :math:`P` í :math:`D` þannig að fyrir sérhvern annan punkt
:math:`Q` í :math:`D` þá liggur allt línustrikið á milli :math:`P` og
:math:`Q` í :math:`D`.


Setning 
~~~~~~~~

Látum :math:`\mbox{${\bf F}$}` vera samfellt diffranlegt vigursvið
skilgreint á :hover:`stjörnusvæði` :math:`D`. Ef :math:`\mbox{${\bf F}$}` er
rótlaust þá er :math:`\mbox{${\bf F}$}` stigulsvið. Með öðrum orðum, ef
vigursviðið :math:`\mbox{${\bf F}$}` er samfellt diffranlegt og
skilgreint á :hover:`stjörnusvæði` :math:`D` og uppfyllir jöfnurnar

.. math:: \displaystyle

   \frac{\partial F_1}{\partial y}=
   \frac{\partial F_2}{\partial x},\quad
   \frac{\partial F_1}{\partial z}=
   \frac{\partial F_3}{\partial x},\quad
   \frac{\partial F_2}{\partial z}=
   \frac{\partial F_3}{\partial y},

þá er :math:`\mbox{${\bf F}$}` stigulsvið.

Setning 
~~~~~~~~

Lát :math:`\mbox{${\bf F}$}` vera samfellt diffranlegt vigursvið
skilgreint á :hover:`stjörnusvæði` :math:`D`. Ef :math:`\mbox{${\bf F}$}` er
sundurleitnilaust þá er til vigursvið :math:`\mbox{${\bf G}$}` þannig að
:math:`\mbox{${\bf F}$}=\mbox{${\rm\bf curl\,}$}\mbox{${\bf G}$}`.
Vigursviðið :math:`\mbox{${\bf G}$}` kallast *vigurmætti* fyrir
:math:`\mbox{${\bf F}$}`.

.. index::
  sundurleitnisetning	

Sundurleitnisetningin I
-----------------------

Setning (Sundurleitnisetning I)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`\mbox{${\bf F}$}` vera samfellt diffranlegt vigursvið
skilgreint á opnu mengi :math:`D` í :math:`{\mathbb  R}^3`. Látum
:math:`P` vera punkt á skilgreiningarsvæði :math:`\mbox{${\bf F}$}` og
:math:`{\cal S}_\varepsilon` kúluskel með miðju í :math:`P` og geisla
:math:`\varepsilon`. Látum svo :math:`\mbox{${\bf N}$}` vera
einingarþvervigrasvið á :math:`{\cal S}_\varepsilon` þannig að
:math:`\mbox{${\bf N}$}` vísar út á við. Þá er

.. math:: \displaystyle

   \mbox{${\rm\bf div\,}$}\mbox{${\bf F}$}(P)=\lim_{\varepsilon\rightarrow 0^+}
   \frac{1}{V_\varepsilon}\int\!\!\!\int_{{\cal S}_\varepsilon}\mbox{${\bf F}$}\cdot\mbox{${\bf N}$}\,dS.

þar sem :math:`V_\varepsilon= 4\pi\varepsilon^3/3` er rúmmálið innan í
:math:`{\cal S}_\varepsilon`.

.. index::
  Stoke;setning


Setning (Setning Stokes I)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`\mbox{${\bf F}$}` vera samfellt diffranlegt vigursvið
skilgreint á opnu mengi :math:`D` í :math:`{\mathbb  R}^3`. Látum
:math:`P` vera punkt á skilgreiningarsvæði :math:`\mbox{${\bf F}$}` og
:math:`C_\varepsilon` vera hring með miðju í :math:`P` og geisla
:math:`\varepsilon`. Látum :math:`\mbox{${\bf N}$}` vera
einingarþvervigur á planið sem hringurinn liggur í. Áttum hringinn
jákvætt. Þá er

.. math:: \displaystyle

   \mbox{${\bf N}$}\cdot\mbox{${\rm\bf curl\,}$}\mbox{${\bf F}$}(P)=\lim_{\varepsilon\rightarrow 0^+}
   \frac{1}{A_\varepsilon}\oint_{C_\varepsilon}\mbox{${\bf F}$}\cdot d\mbox{${\bf r}$}.

þar sem :math:`A_\varepsilon= \pi\varepsilon^2` er flatarmálið sem
afmarkast af :math:`{\cal C}_\varepsilon`.

Túlkun 
~~~~~~~

Hugsum :math:`\mbox{${\bf F}$}` sem lýsingu á vökvastreymi í
:math:`{\mathbb  R}^3`.

:math:`\mbox{${\rm\bf div\,}$}\mbox{${\bf F}$}(P)` lýsir því hvort
vökvinn er að þenjast út eða dragast saman í punktinum :math:`P`.
Sundurleitnisetningin (næsti fyrirlestur) segir að samanlögð útþensla á
rúmskika :math:`R` er jöfn streymi út um jaðar svæðisins
:math:`\mathcal{S}`, eða

.. math:: \displaystyle \int\!\!\!\int\!\!\!\int_R\mbox{${\rm\bf div\,}$}\mbox{${\bf F}$}\,dV=\int\!\!\!\int_{\mathcal{S}} \mbox{${\bf F}$}\cdot\mbox{${\bf N}$}\,dS.

:math:`\mbox{${\rm\bf curl\,}$}\mbox{${\bf F}$}(P)` lýsir hringstreymi í
kringum punktinn :math:`P`. Setning Stokes (þar næsti fyrirlestur) segir
að samanlagt hringstreymi á fleti :math:`\mathcal{S}` er jafnt
hringstreymi á jaðri flatarins, sem við táknum með :math:`\mathcal{C}`,
eða

.. math:: \displaystyle \int\!\!\!\int_{\cal S} \mbox{${\rm\bf curl\,}$}\mbox{${\bf F}$}\cdot\mbox{${\bf N}$}\,dS=\oint_\mathcal{C} \mbox{${\bf F}$}\cdot d\mbox{${\bf r}$}.

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`R` vera svæði í :math:`{\mathbb  R}^2` og :math:`\cal C`
:hover:`jaðar` :math:`R`. Gerum ráð fyrir að :math:`\cal C` samanstandi af endanlega mörgum ferlum :math:`{\cal C}_1, \ldots, {\cal C}_n`. Jákvæð
:hover:`áttun` á ferlunum felst í því að velja fyrir hvert :math:`i` stikun :math:`\mbox{${\bf r}$}_i` á :math:`{\cal C}_i` þannig að ef labbað eftir :math:`{\cal C}_i` í stefnu stikunar þá er :math:`R` á vinstri hönd.

.. index::
  Green;setning

Setning Green 
~~~~~~~~~~~~~~

Látum :math:`R` vera svæði í planinu þannig að jaðar :math:`R`, táknaður
með :math:`\cal C`, samanstendur af endanlega mörgum samfellt
diffranlegum ferlum. Áttum :math:`\cal C` jákvætt. Látum
:math:`\mbox{${\bf F}$}(x,y)=F_1(x,y)\,\mbox{${\bf i}$}+F_2(x,y)\,\mbox{${\bf j}$}`
vera samfellt diffranlegt vigursvið skilgreint á :math:`R`. Þá er

.. math:: \displaystyle

   \oint_{\cal C}F_1(x,y)\,dx+F_2(x,y)\,dy=\int\!\!\!\int_R
   \frac{\partial  F_2}{\partial x}- 
   \frac{\partial  F_1}{\partial y}\,dA.

Fylgisetning 
~~~~~~~~~~~~~

Látum :math:`R` vera svæði í planinu þannig að jaðar :math:`R` táknaður
með :math:`\cal C`, samanstendur af endanlega mörgum samfellt
diffranlegum ferlum. Áttum :math:`\cal C` jákvætt. Þá er

.. math:: \displaystyle

   \mbox{Flatarmál } R=\oint_{\cal C}x\,dy= 
   -\oint_{\cal C}y\,dx=\frac{1}{2}\oint_{\cal C}x\,dy-y\,dx.

Sundurleitnisetningin í tveimur víddum 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`R` vera svæði í planinu þannig að jaðar :math:`R`, táknaður
með :math:`\cal C`, samanstendur af endanlega mörgum samfellt
diffranlegum ferlum. Látum :math:`\mbox{${\bf N}$}` tákna
einingarþvervigrasvið á :math:`\cal C` þannig að
:math:`\mbox{${\bf N}$}` vísar út úr :math:`R`. Látum
:math:`\mbox{${\bf F}$}(x,y)=F_1(x,y)\,\mbox{${\bf i}$}+F_2(x,y)\,\mbox{${\bf j}$}`
vera samfellt diffranlegt vigursvið skilgreint á :math:`R`. Þá er

.. math:: \displaystyle \int\!\!\!\int_R\mbox{${\rm\bf div\,}$}\mbox{${\bf F}$}\,dA=\oint_{\cal C} \mbox{${\bf F}$}\cdot\mbox{${\bf N}$}\,ds.

Sundurleitnisetningin II
------------------------

.. index::
  flötur;reglulegur

Skilgreining 
~~~~~~~~~~~~~

Flötur er sagður reglulegur ef hann hefur :hover:`snertiplan,snertislétta` í hverjum punkti.

Flötur :math:`\cal S` sem er búinn til með því að taka endanlega marga
reglulega fleti :math:`{\cal S}_1, \ldots, {\cal S}_n` og líma þá saman
á jöðrunum kallast *reglulegur á köflum*.

Þegar talað um einingarþvervigrasvið á slíkan flöt þá er átt við
vigursvið sem er skilgreint á fletinum nema í þeim punktum þar sem
fletir :math:`{\cal S}_i` og :math:`{\cal S}_j` hafa verið límdir saman.
Í slíkum punktum þarf flöturinn ekki að hafa snertiplan og því ekki
heldur þvervigur.

Flötur er sagður *lokaður* ef hann er yfirborð svæðis í
:math:`{\mathbb  R}^3` (t.d. er kúluhvel lokaður flötur).

Setning (Sundurleitnisetningin, Setning Gauss) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`\cal S` vera lokaðan flöt sem er reglulegur á köflum.
Táknum með :math:`D` rúmskikann sem :math:`\cal S` umlykur. Látum
:math:`\mbox{${\bf N}$}` vera einingarþvervigrasvið á :math:`\cal S` sem
vísar út úr :math:`D`. Ef :math:`\mbox{${\bf F}$}` er samfellt
diffranlegt vigursvið skilgreint á :math:`D` þá er

.. math:: \displaystyle \int\!\!\!\int\!\!\!\int_D \mbox{${\rm\bf div\,}$}\mbox{${\bf F}$}\,dV=\int\!\!\!\int_{\cal S} \mbox{${\bf F}$}\cdot\mbox{${\bf N}$}\,dS.

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`D` vera rúmskika í :math:`{\mathbb  R}^3`. Segjum að
rúmskikinn :math:`D` sé :math:`z`-*einfaldur* ef til er svæði
:math:`D_z` í planinu og samfelld föll :math:`f` og :math:`g` skilgreind
á :math:`D_z` þannig að

.. math:: \displaystyle D=\{(x,y,z)\mid (x,y)\in D_z\mbox{ og }f(x,y)\leq z\leq g(x,y)\}.

Það að rúmskiki sé :math:`x`- eða :math:`y`-einfaldur er skilgreint á
sama hátt.

Setning 
~~~~~~~~

Látum :math:`\cal S` vera lokaðan flöt sem er reglulegur á köflum.
Táknum með :math:`D` rúmskikann sem :math:`\cal S` umlykur. Látum
:math:`\mbox{${\bf N}$}` vera einingarþvervigrasvið á :math:`\cal S` sem
vísar út úr :math:`D`. Ef :math:`\mbox{${\bf F}$}` er samfellt
diffranlegt vigursvið skilgreint á :math:`D` og :math:`\varphi`
diffranlegt fall skilgreint á :math:`D` þá er

.. math:: \displaystyle \int\!\!\!\int\!\!\!\int_D\mbox{${\rm\bf curl\,}$}\mbox{${\bf F}$}\,dV=-\int\!\!\!\int_{\cal S}\mbox{${\bf F}$}\times\mbox{${\bf N}$}\,dS,

og

.. math:: \displaystyle \int\!\!\!\int\!\!\!\int_D\mbox{${\rm\bf grad\,}$}\varphi\,dV=\int\!\!\!\int_{\cal S}\varphi\mbox{${\bf N}$}\,dS.

Athugið að útkomurnar úr heildunum eru vigrar.

Setning Stokes
--------------

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`\cal S` vera áttanlegan flöt sem er reglulegur á köflum með
jaðar :math:`\cal C` og einingarþvervigrasvið :math:`\mbox{${\bf N}$}`.
Áttun :math:`\cal C` út frá :math:`\mbox{${\bf N}$}` finnst með að hugsa
sér að gengið sé eftir :math:`\cal C` þannig að skrokkurinn vísi í
stefnu :math:`\mbox{${\bf N}$}` og göngustefnan sé valin þannig að
flöturinn sé á vinstri hönd.

Setning (Setning Stokes)
~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`\cal S` vera áttanlegan flöt sem er reglulegur á köflum og
látum :math:`\mbox{${\bf N}$}` tákna einingarþvervigrasvið á
:math:`\cal S`. Táknum með :math:`\cal C` jaðar :math:`\cal S` og áttum
:math:`\cal C` með tilliti til :math:`\mbox{${\bf N}$}`. Ef
:math:`\mbox{${\bf F}$}` er samfellt diffranlegt vigursvið skilgreint á
:hover:`opnu mengi,opið mengi` sem inniheldur :math:`\cal S` þá er

.. math:: \displaystyle \int\!\!\!\int_{\cal S} \mbox{${\rm\bf curl\,}$}\mbox{${\bf F}$}\cdot\mbox{${\bf N}$}\,dS=\oint_{\cal C}\mbox{${\bf F}$}\cdot \mbox{${\bf T}$}\,ds.

Setning 
~~~~~~~~

Látum :math:`\mbox{${\bf F}$}` vera samfellt diffranlegt vigursvið
skilgreint á opnu mengi :math:`D` í :math:`{\mathbb  R}^3`. Látum
:math:`P` vera punkt á skilgreiningarsvæði :math:`\mbox{${\bf F}$}` og
:math:`C_\varepsilon` vera hring með miðju í :math:`P` og geisla
:math:`\varepsilon`. Látum :math:`\mbox{${\bf N}$}` vera
einingarþvervigur á planið sem hringurinn liggur í. Áttum hringinn
jákvætt. Þá er

.. math:: \displaystyle

   \mbox{${\bf N}$}\cdot\mbox{${\rm\bf curl\,}$}\mbox{${\bf F}$}(P)=\lim_{\varepsilon\rightarrow 0^+}
   \frac{1}{\pi\varepsilon^2}\oint_{C_\varepsilon}\mbox{${\bf F}$}\cdot d\mbox{${\bf r}$}.

Setning 
~~~~~~~~

Látum :math:`\cal S` vera lokaðan flöt sem er reglulegur á köflum.
Táknum með :math:`D` rúmskikann sem :math:`\cal S` umlykur. Látum
:math:`\mbox{${\bf N}$}` vera einingarþvervigrasvið á :math:`\cal S` sem
vísar út úr :math:`D`. Ef :math:`\mbox{${\bf F}$}` er samfellt
diffranlegt vigursvið skilgreint á opnu mengi sem inniheldur :math:`D`,
þá er

.. math:: \displaystyle \oint_{\cal S}\mbox{${\rm\bf curl\,}$}\mbox{${\bf F}$}\cdot\mbox{${\bf N}$}\,dS=0.

Hagnýtingar í eðlisfræði
------------------------

Vökvaflæði 
~~~~~~~~~~~

Skoðum vökvaflæði í rúmi. Hugsum okkur að vökvaflæðið sé líka háð tíma.
Látum :math:`\mbox{${\bf v}$}(x,y,z,t)` tákna hraðavigur agnar sem er í
punktinum :math:`(x,y,z)` á tíma :math:`t`. Látum
:math:`\delta(x,y,z,t)` tákna efnisþéttleika (massi per rúmmálseiningu)
í punktum :math:`(x,y,z)` á tíma :math:`t`. Þá gildir að

.. math:: \displaystyle \frac{\partial \delta}{\partial t}+\mbox{${\rm\bf div\,}$}(\delta\mbox{${\bf v}$})=0.

(Þessi jafna kallast samfelldnijafnan um vökvaflæðið.)

Vökvaflæði 
~~~~~~~~~~~

Til viðbótar við :math:`\mbox{${\bf v}$}` og :math:`\delta` þá
skilgreinum við :math:`p(x,y,z,t)` sem þrýsting og
:math:`\mbox{${\bf F}$}` sem utanaðkomandi kraft, gefinn sem kraftur per
massaeiningu. Þá gildir að

.. math:: \displaystyle \delta\frac{\partial \mbox{${\bf v}$}}{\partial t}+\delta(\mbox{${\bf v}$}\cdot\nabla)\mbox{${\bf v}$}=-\nabla p+\delta\mbox{${\bf F}$}.

(Þessi jafna er kölluð hreyfijafna flæðisins.)

Rafsvið - Lögmál Coulombs 
~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum punkthleðslu :math:`q` vera í punktinum
:math:`\mbox{${\bf s}$}=\xi\,\mbox{${\bf i}$}+\eta\,\mbox{${\bf j}$}+\zeta\,\mbox{${\bf k}$}`.
Í punktum
:math:`\mbox{${\bf r}$}=x\,\mbox{${\bf i}$}+y\,\mbox{${\bf j}$}+z\,\mbox{${\bf k}$}`
er rafsviðið vegna þessarar hleðslu

.. math:: \displaystyle \mbox{${\bf E}$}(\mbox{${\bf r}$})=\frac{q}{4\pi\varepsilon_0}\frac{\mbox{${\bf r}$}-\mbox{${\bf s}$}}{|\mbox{${\bf r}$}-\mbox{${\bf s}$}|^3}

þar sem :math:`\varepsilon_0` er *r*\ afsvörunarstuðull tómarúms.

Rafsvið - Lögmál Gauss (fyrsta jafna Maxwells)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`\rho(\xi,\eta,\zeta)` vera hleðsludreifingu og
:math:`\mbox{${\bf E}$}` rafsviðið vegna hennar. Þá gildir að

.. math:: \displaystyle \mbox{${\rm\bf div\,}$}\mbox{${\bf E}$}=\frac{\rho}{\varepsilon_0}.

Rafsvið 
~~~~~~~~

Látum :math:`\rho(\xi,\eta,\zeta)` vera hleðsludreifingu á takmörkuðu
svæði :math:`R` og :math:`\mbox{${\bf E}$}` rafsviðið vegna hennar. Ef
við setjum

.. math:: \displaystyle \varphi(\mbox{${\bf r}$}) = -\frac{1}{4 \pi \varepsilon_0} \iiint_R \frac{\rho(\mbox{${\bf s}$})}{|\mbox{${\bf r}$}-\mbox{${\bf s}$}|} dV

þá er :math:`\mbox{${\bf E}$}= \nabla \varphi` og þar með er

.. math:: \displaystyle \mbox{${\rm\bf curl\,}$}\mbox{${\bf E}$}= \mathbf{0}.

Segulsvið - Lögmál Biot-Savart 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum straum :math:`I` fara eftir ferli :math:`\cal F`. Táknum
segulsviðið með :math:`\mbox{${\bf H}$}` og látum
:math:`\mbox{${\bf s}$}=\xi\,\mbox{${\bf i}$}+\eta\,\mbox{${\bf j}$}+\zeta\,\mbox{${\bf k}$}`
vera punkt á ferlinum :math:`\cal F`. Þá gefur örbútur
:math:`d\mbox{${\bf s}$}` úr :math:`\cal F` af sér segulsvið

.. math:: \displaystyle d\mbox{${\bf H}$}(\mbox{${\bf r}$})=\frac{\mu_0 I}{4\pi}\frac{d\mbox{${\bf s}$}\times(\mbox{${\bf r}$}-\mbox{${\bf s}$})}{|\mbox{${\bf r}$}-\mbox{${\bf s}$}|^3}

þar sem :math:`\mu_0` er *s*\ egulsvörunarstuðull tómarúms. Af þessu
sést að

.. math:: \displaystyle

   \mbox{${\bf H}$}=\frac{\mu_0 I}{4\pi}\oint_{\cal F}
   \frac{d\mbox{${\bf s}$}\times(\mbox{${\bf r}$}-\mbox{${\bf s}$})}{|\mbox{${\bf r}$}-\mbox{${\bf s}$}|^3}

og sýna má að ef :math:`\mbox{${\bf r}$}\notin \mathcal{F}` þá er

.. math:: \displaystyle \mbox{${\rm\bf curl\,}$}\mbox{${\bf H}$}= \mathbf{0}.

Segulsvið - Lögmál Ampére
~~~~~~~~~~~~~~~~~~~~~~~~~

Hugsum okkur að straumur :math:`I` fari upp eftir :math:`z`-ás. Táknum
með :math:`\mbox{${\bf H}$}` segulsviðið og
:math:`H=|\mbox{${\bf H}$}|`. Í punkti
:math:`\mbox{${\bf r}$}=x\,\mbox{${\bf i}$}+y\,\mbox{${\bf j}$}+z\,\mbox{${\bf k}$}`
í fjarlægð :math:`a` frá :math:`z`-ás er
:math:`H=\frac{\mu_0 I}{2\pi a}` og ef :math:`\cal C` er lokaður
einfaldur ferill sem fer rangsælis einu sinni umhverfis :math:`z`-ásinn
þá er

.. math:: \displaystyle \oint_{\cal C} \mbox{${\bf H}$}\cdot d\mbox{${\bf r}$}=\mu_0 I.

Hugsum okkur að :math:`\mathbf{J}(\mbox{${\bf r}$})` sé straumþéttleiki
í punkti :math:`\mbox{${\bf r}$}` (straumur á flatareiningu). Þá er

.. math:: \displaystyle \mbox{${\rm\bf curl\,}$}\mbox{${\bf H}$}= \mu_0 \mathbf{J}.

Einnig gildir að ef við setjum

.. math:: \displaystyle

   \mbox{${\bf A}$}(\mbox{${\bf r}$})=\frac{\mu_0}{4\pi}\iiint_{R}
   \frac{\mathbf{J}(\mathbf{s})}{|\mbox{${\bf r}$}-\mbox{${\bf s}$}|}dV,

þá er :math:`\mbox{${\bf H}$}=\mbox{${\rm\bf curl\,}$}\mbox{${\bf A}$}`
og því er

.. math:: \displaystyle \mbox{${\rm\bf div\,}$}\mbox{${\bf H}$}=0.

Samantekt
~~~~~~~~~

.. math:: \displaystyle

   \begin{aligned}
     \mbox{${\rm\bf div\,}$}\mbox{${\bf E}$}&= \frac{\rho}{\varepsilon_0} \quad~ \mbox{${\rm\bf div\,}$}\mbox{${\bf H}$}= 0 \\
     \mbox{${\rm\bf curl\,}$}\mbox{${\bf E}$}&= \mathbf{0} \qquad \mbox{${\rm\bf curl\,}$}\mbox{${\bf H}$}= \mu_0 \mathbf{J}
    \end{aligned}

Jöfnur Maxwells

.. math:: \displaystyle

   \begin{aligned}
     \mbox{${\rm\bf div\,}$}\mbox{${\bf E}$}&= \frac{\rho}{\varepsilon_0} \qquad ~ \mbox{${\rm\bf div\,}$}\mbox{${\bf H}$}= 0 \\
     \mbox{${\rm\bf curl\,}$}\mbox{${\bf E}$}&= -\frac{\partial \mbox{${\bf H}$}}{\partial t} \quad \mbox{${\rm\bf curl\,}$}\mbox{${\bf H}$}= \mu_0 \mathbf{J} + \mu_0 \varepsilon_0  \frac{\partial\mbox{${\bf E}$}}{\partial t}
    \end{aligned}

*My old grandmother always used to say, Summer friends will melt away like summer snows, but winter friends are friends forever.*

\- George R.R. Martin, A Feast for Crows 

