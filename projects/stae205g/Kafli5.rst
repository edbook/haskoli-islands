Vigursvið
=========

*Different roads sometimes lead to the same castle.*

\-George R.R. Martin, A Game of Thrones

Vigursvið
---------

.. index::
  vigursvið

Skilgreining 
~~~~~~~~~~~~~

:hover:`Vigursvið` á :math:`{\mathbb  R}^2` er vörpun

.. math:: \displaystyle \mbox{${\bf F}$}(x,y)=F_1(x,y)\,\mbox{${\bf i}$}+F_2(x,y)\,\mbox{${\bf j}$}.

Þegar talað er um vigursvið þá hugsum við vigurinn
:math:`\mbox{${\bf F}$}(x,y)` sem vigur í :math:`{\mathbb  R}^2` sem
hefur fótpunkt í punktinum :math:`(x,y)`.

Vigursvið
:math:`\mbox{${\bf F}$}(x,y)=F_1(x,y)\mbox{${\bf i}$}+F_2(x,y)\mbox{${\bf j}$}`
er sagt :hover:`samfellt,samfelldur` ef föllin :math:`F_1(x,y)` og :math:`F_2(x,y)` eru
samfelld.

Vigursvið á :math:`{\mathbb  R}^3` er vörpun

.. math:: \displaystyle \mbox{${\bf F}$}(x,y,z)=F_1(x,y,z)\,\mbox{${\bf i}$}+F_2(x,y,z)\,\mbox{${\bf j}$}+F_3(x,y,z)\,\mbox{${\bf k}$}.

Við hugsum :math:`\mbox{${\bf F}$}(x,y,z)` sem vigur með :math:`(x,y,z)`
sem fótpunkt. Skilgreiningin á því að vigursvið í :math:`{\mathbb  R}^3`
sé samfellt er eins og á samfeldni vigursvið í :math:`{\mathbb  R}^2` .

.. image:: vfield.png
   :width: 70%
   :align: center

..

*Vigursviðið* :math:`\mathbf{F}(x,y) = -y\mbox{${\bf i}$}+ x \mbox{${\bf j}$}`.

.. index::
  straumlína

Straumlína
----------

Skilgreining 
~~~~~~~~~~~~~

:hover:`Ferill` :math:`C` í planinu kallast :hover:`straumlína` fyrir :hover:`vigursvið` :math:`\mbox{${\bf F}$}(x,y)` ef í hverjum punkti
:math:`(x,y)` á ferlinum er vigurinn :math:`\mbox{${\bf F}$}(x,y)`
:hover:`snertivigur` við ferilinn.

.. image:: flowlines.png
   :width: 70%
   :align: center

..

*Vigursviðið* :math:`\mathbf{F}(x,y) = -y\mbox{${\bf i}$}+ x \mbox{${\bf j}$}`
*ásamt nokkrum straumlínum*.

.. index::
  vigursvið:geymið
  stigulsvið
  mætti
  
Stigulsvið
----------

Skilgreining 
~~~~~~~~~~~~~

Vigursvið :math:`\mbox{${\bf F}$}(x,y)` kallast *stigulsvið* eða *geymið
svið* (e. gradient field, conservative field) á mengi :math:`D` ef til
er fall :math:`\varphi(x,y)` þannig að

.. math:: \displaystyle \mbox{${\bf F}$}(x,y)=\nabla\varphi(x,y)

fyrir alla punkta :math:`(x,y)\in D`, það er að segja ef

.. math:: \displaystyle \mbox{${\bf F}$}(x,y)=F_1(x,y)\,\mbox{${\bf i}$}+F_2(x,y)\,\mbox{${\bf j}$}

þá er

.. math:: \displaystyle F_1(x,y)=\frac{\partial}{\partial x}\varphi(x,y) \quad \text{og}\quad  F_2(x,y)=\frac{\partial}{\partial y}\varphi(x,y).

Vigursvið :math:`\mbox{${\bf F}$}(x,y,z)` kallast *stigulsvið* eða
*geymið svið* ef til er fall :math:`\varphi(x,y,z)` þannig að
:math:`\mbox{${\bf F}$}(x,y,z)=\nabla\varphi(x,y,z)`.

Fallið :math:`\varphi` kallast :hover:`mætti`  fyrir vigursviðið
:math:`\mbox{${\bf F}$}`.

Setning 
~~~~~~~~

Látum
:math:`\mbox{${\bf F}$}(x,y)=F_1(x,y)\,\mbox{${\bf i}$}+F_2(x,y)\,\mbox{${\bf j}$}`
vera vigursvið þannig að föllin :math:`F_1(x,y)` og :math:`F_2(x,y)`
hafi samfelldar hlutafleiður. Ef :math:`\mbox{${\bf F}$}(x,y)` er
stigulsvið þá er

.. math:: \displaystyle

   \frac{\partial}{\partial y}F_1(x,y)=
   \frac{\partial}{\partial x}F_2(x,y).

.. note::
   Þó að hlutafleiðurnar séu jafnar þá er **ekki** hægt að álykta að :math:`\mbox{${\bf F}$}` sé stigulsvið. Þetta atriði verður rætt síðar.

Setning 
~~~~~~~~

Látum
:math:`\mbox{${\bf F}$}(x,y,z)=F_1(x,y,z)\,\mbox{${\bf i}$}+F_2(x,y,z)\,\mbox{${\bf j}$}+F_3(x,y,z)\,\mbox{${\bf k}$}`
vera vigursvið þannig að föllin :math:`F_1(x,y,z), F_2(x,y,z)` og
:math:`F_3(x,y,3)` hafi samfelldar hlutafleiður. Ef
:math:`\mbox{${\bf F}$}(x,y,z)` er stigulsvið þá er

.. math:: \displaystyle

   \begin{aligned}
   \frac{\partial}{\partial y}F_1(x,y,z) &=
   \frac{\partial}{\partial x}F_2(x,y,z), \\
   \frac{\partial}{\partial z}F_1(x,y,z) &=
   \frac{\partial}{\partial x}F_3(x,y,z) \quad \text{og} \\
   \frac{\partial}{\partial z}F_2(x,y,z)&=
   \frac{\partial}{\partial y}F_3(x,y,z).\end{aligned}

Reikniaðferð 
~~~~~~~~~~~~~

Finna á :hover:`mætti` :math:`\varphi(x,y)` fyrir stigulsvið
:math:`\mbox{${\bf F}$}(x,y)=F_1(x,y)\,\mbox{${\bf i}$}+F_2(x,y)\,\mbox{${\bf j}$}`.
Viljum finna fall :math:`\varphi(x,y)` þannig að

.. math:: \displaystyle

   \frac{\partial}{\partial x}\varphi(x,y)=F_1(x,y)\qquad
   \mbox{og}\qquad \frac{\partial}{\partial y}\varphi(x,y)=F_2(x,y).

Með því að heilda þessar jöfnur fæst að

.. math:: \displaystyle \varphi(x,y)=\int F_1(x,y)\,dx+C_1(y)

 og

.. math:: \displaystyle \varphi(x,y)=\int F_2(x,y)\,dy+C_2(x).

Þegar fyrra stofnfallið er reiknað þá er :math:`y` hugsað sem fasti og
því fæst heildunarfasti sem getur verið fall af :math:`y`. Lokaskrefið
er svo að horfa á jöfnurnar tvær hér að ofan og sjá hvort ekki er hægt
að finna gildi fyrir heildunarfastanna :math:`C_1(x)` og :math:`C_2(y)`
þannig að sama formúlan fyrir :math:`\varphi(x,y)` fáist.

.. index::
  ferilheildi

Heildi falls yfir feril
-----------------------

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`\cal C` vera feril í :math:`{\mathbb  R}^2` stikaðan af
samfellt diffranlegum stikaferli
:math:`\mbox{${\bf r}$}:[a,b]\rightarrow{\mathbb  R}^2`. Ritum
:math:`\mbox{${\bf r}$}(t)=(x(t),y(t))`. *Heildi falls* :math:`f(x,y)`
*yfir ferilinn* :math:`\cal C` *með tilliti til bogalengdar* er
skilgreint sem

.. math:: \displaystyle

   \begin{aligned}
   \int_{\cal C}f(x,y)\,ds&=\int_a^b f(\mbox{${\bf r}$}(t))\,|\mbox{${\bf r}$}'(t)|\,dt\\
   &=\int_a^b f(x(t),y(t))\,\sqrt{x'(t)^2+y'(t)^2}\,dt.\end{aligned}

Sama aðferð notuð til að skilgreina heildi falls yfir feril í
:math:`{\mathbb  R}^3`.

Setning 
~~~~~~~~

Látum :math:`\cal C` vera feril í :math:`{\mathbb  R}^2`. Gerum ráð
fyrir að :math:`\mbox{${\bf r}$}_1` og :math:`\mbox{${\bf r}$}_2` séu
tveir samfellt diffranlegir stikaferlar sem báðir stika ferilinn
:math:`\cal C`. Ef fall :math:`f(x,y)` er heildað yfir :math:`\cal C` þá
fæst sama útkoma hvort sem stikunin :math:`\mbox{${\bf r}$}_1` eða
stikunin :math:`\mbox{${\bf r}$}_2` er notuð við útreikningana.

Skilgreining 
~~~~~~~~~~~~~

Ferill :math:`\cal C` í plani er sagður *samfellt diffranlegur á köflum*
ef til er stikun
:math:`\mbox{${\bf r}$}:[a,b]\rightarrow {\mathbb  R}^2` á
:math:`\cal C` þannig að til eru punktar
:math:`a=t_0<t_1<t_2<\cdots<t_n<t_{n+1}=b` þannig að á hverju bili
:math:`(t_i,t_{i+1})` er :math:`\mbox{${\bf r}$}` :hover:`samfellt diffranlegur`
ferill og :hover:`markgildin,markgildi`

.. math:: \displaystyle

   \lim_{t\rightarrow t_i^+}\mbox{${\bf r}$}'(t)\qquad\mbox{og}\qquad 
   \lim_{t\rightarrow t_{i+1}^-}\mbox{${\bf r}$}'(t)

eru bæði til.

Líka sagt að stikaferillinn :math:`\mbox{${\bf r}$}` sé *samfellt
diffranlegur á köflum.*

Heildi vigursviðs eftir ferli
-----------------------------

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`\mbox{${\bf F}$}(x,y)` vera vigursvið og
:math:`\mbox{${\bf r}$}:[a,b]\rightarrow {\mathbb  R}^2` stikun á ferli
:math:`\cal C` og gerum ráð fyrir að stikaferillinn
:math:`\mbox{${\bf r}$}` sé samfellt diffranlegur á köflum. *Heildi
vigursviðsins* :math:`\mbox{${\bf F}$}(x,y)` *eftir ferlinum*
:math:`\cal C` er skilgreint sem

.. math:: \displaystyle

   \int_{\cal C} \mbox{${\bf F}$}\cdot d\mbox{${\bf r}$}= \int_{\cal C} \mbox{${\bf F}$}\cdot \mbox{${\bf T}$}\,ds
   =\int_a^b \mbox{${\bf F}$}(\mbox{${\bf r}$}(t))\cdot \mbox{${\bf r}$}'(t)\,dt.

Skilgreining 
~~~~~~~~~~~~~

Ritum
:math:`\mbox{${\bf F}$}(x,y)=F_1(x,y)\,\mbox{${\bf i}$}+F_2(x,y)\,\mbox{${\bf j}$}`.
Ritum líka
:math:`\mbox{${\bf r}$}(t)=x(t)\,\mbox{${\bf i}$}+y(t)\,\mbox{${\bf j}$}`.
Þá má rita :math:`dx=x'(t)\,dt,\, dy=y'(t)\,dt`. Með því að nota þennan
rithátt fæst að

.. math:: \displaystyle

   \begin{aligned}
   \int_{\cal C}\mbox{${\bf F}$}\cdot d\mbox{${\bf r}$}&=\int_a^b
   (F_1(x,y)\,\mbox{${\bf i}$}+F_2(x(t),y(t))\,\mbox{${\bf j}$})\cdot(x'(t)\,\mbox{${\bf i}$}+y'(t)\,\mbox{${\bf j}$})\,dt\\
   &=\int_a^b F_1(x(t),y(t))x'(t)\,dt+F_2(x(t),y(t))y'(t)\,dt\\
   &=\int_{\cal C} F_1(x,y)\,dx+F_2(x,y)\,dy.\end{aligned}

.. note::
   Látum :math:`\cal C` vera feril í :math:`{\mathbb  R}^2`. Gerum ráð fyrir að :math:`\mbox{${\bf r}$}_1:[a,b]\rightarrow {\mathbb  R}^2` og :math:`\mbox{${\bf r}$}_2:[a',b']\rightarrow {\mathbb  R}^2` séu tveir samfellt diffranlegir á köflum stikaferlar sem stika :math:`\cal C`. Gerum ennfremur ráð fyrir að :math:`\mbox{${\bf r}$}_1(a)=\mbox{${\bf r}$}_2(b')` og :math:`\mbox{${\bf r}$}_1(b)=\mbox{${\bf r}$}_2(a')` (þ.e.a.s. stikaferlarnir fara í sitthvora áttina eftir :math:`\cal C`). Þá gildir ef :math:`\mbox{${\bf F}$}(x,y)` er vigursvið að

   .. math:: \displaystyle \int_{\cal C} \mbox{${\bf F}$}\cdot d\mbox{${\bf r}$}_1=-\int_{\cal C} \mbox{${\bf F}$}\cdot d\mbox{${\bf r}$}_2.

   (Ef breytt er um stefnu á stikun á breytist formerki þegar vigursvið heildað eftir ferlinum.)

Ferilheildi og stigulsvið
-------------------------

Setning 
~~~~~~~~

Látum :math:`\mbox{${\bf F}$}(x,y)` vera samfellt stigulsvið skilgreint
á svæði :math:`D` í :math:`{\mathbb  R}^2` og látum :math:`\varphi` vera
fall skilgreint á :math:`D` þannig að
:math:`\mbox{${\bf F}$}(x,y)=\nabla \varphi(x,y)` fyrir alla punkta
:math:`(x,y)\in D`. Látum :math:`\mbox{${\bf r}$}:[a,b]\rightarrow D`
vera stikaferill sem er samfellt diffranlegur á köflum og stikar feril
:math:`\cal C` í :math:`D`. Þá er

.. math:: \displaystyle \int_{\cal C} \mbox{${\bf F}$}\cdot \,d\mbox{${\bf r}$}=\varphi(\mbox{${\bf r}$}(b))-\varphi(\mbox{${\bf r}$}(a)).

(Samsvarandi gildir fyrir vigursvið skilgreint á svæði
:math:`D\subseteq {\mathbb  R}^3`.)

Fylgisetning 
~~~~~~~~~~~~~

Látum :math:`\mbox{${\bf F}$}` vera samfellt stigulsvið skilgreint á
mengi :math:`D\subseteq {\mathbb  R}^2`. Látum
:math:`\mbox{${\bf r}$}:[a,b]\rightarrow D` vera stikaferil sem er
samfellt diffranlegur á köflum og lokaður (þ.e.a.s.
:math:`\mbox{${\bf r}$}(a)=\mbox{${\bf r}$}(b)`) og stikar feril
:math:`\mathcal{C}`. Þá er

.. math:: \displaystyle \oint_{\cal C}  \mbox{${\bf F}$}\cdot \,d\mbox{${\bf r}$}=0.

(Ath. að rithátturinn

.. math:: \displaystyle \oint_{\cal C}

er gjarnan notaður þegar heildað er yfir lokaðan feril :math:`\cal C`.)

Fylgisetning 
~~~~~~~~~~~~~

Látum :math:`\mbox{${\bf F}$}` vera samfellt stigulsvið skilgreint á
mengi :math:`D\subseteq {\mathbb  R}^2`. Látum
:math:`\mbox{${\bf r}$}_1:[a_1,b_1]\rightarrow D` og
:math:`\mbox{${\bf r}$}_2:[a_2,b_2]\rightarrow D` vera stikaferla sem
eru samfellt diffranlegir á köflum og stika ferlana
:math:`\mathcal{C}_1` og :math:`\mathcal{C}_2`. Gerum ráð fyrir að
:math:`\mbox{${\bf r}$}_1(a_1)=\mbox{${\bf r}$}_2(a_2)` og
:math:`\mbox{${\bf r}$}_1(b_1)=\mbox{${\bf r}$}_2(b_2)`,
þ.e.a.s. stikaferlarnir :math:`\mbox{${\bf r}$}_1` og
:math:`\mbox{${\bf r}$}_2` hafa sameiginlega upphafs- og endapunkta. Þá
er

.. math:: \displaystyle \int_{{\cal C}_1} \mbox{${\bf F}$}\cdot\,d\mbox{${\bf r}$}_1=\int_{{\cal C}_2} \mbox{${\bf F}$}\cdot\,d\mbox{${\bf r}$}_2.

Skilgreining 
~~~~~~~~~~~~~

Segjum að heildi vigursviðs :math:`\mbox{${\bf F}$}` sé *óháð
stikaferli* ef fyrir sérhverja tvo samfellt diffranlega á köflum
stikaferla :math:`\mbox{${\bf r}$}_1` og :math:`\mbox{${\bf r}$}_2` með
sameiginlega upphafs- og endapunkta sem stika ferlana
:math:`\mathcal{C}_1` og :math:`\mathcal{C}_2` gildir að

.. math:: \displaystyle

   \int_{{\cal C}_1} \mbox{${\bf F}$}\cdot\,d\mbox{${\bf r}$}_1=
   \int_{{\cal C}_2} \mbox{${\bf F}$}\cdot\,d\mbox{${\bf r}$}_2.

Setning 
~~~~~~~~

Ferilheildi samfellds vigursviðs :math:`\mbox{${\bf F}$}` er óháð
stikaferli ef og aðeins ef
:math:`\oint_{\cal C} \mbox{${\bf F}$}\cdot\,d\mbox{${\bf r}$}=0` fyrir
alla lokaða ferla :math:`\cal C` sem eru samfellt diffranlegir á köflum.

Upprifjun 
~~~~~~~~~~~~~

Segjum að mengi :math:`D\subseteq {\mathbb  R}^2` sé
*ferilsamanhangandi* (e. connected, path-connected) ef fyrir sérhverja
tvo punkta :math:`P, Q\in D` gildir að til er stikaferill
:math:`\mbox{${\bf r}$}:[0,1]\rightarrow D` þannig að
:math:`\mbox{${\bf r}$}(0)=P` og :math:`\mbox{${\bf r}$}(1)=Q`.


Setning 
~~~~~~~~

Látum :math:`D` vera :hover:`opið mengi` í :math:`{\mathbb  R}^2` sem er
ferilsamanhangandi. Ef :math:`\mbox{${\bf F}$}` er samfellt vigursvið
skilgreint á :math:`D` og ferilheildi :math:`\mbox{${\bf F}$}` eru óháð
vegi þá er :math:`\mbox{${\bf F}$}` stigulsvið.

Setning 
~~~~~~~~

Fyrir samfellt vigursvið :math:`\mbox{${\bf F}$}` skilgreint á opnu
ferilsamanhangandi mengi :math:`D\subseteq {\mathbb  R}^2` er
eftirfarandi jafngilt:

(a)  :math:`\mbox{${\bf F}$}` er stigulsvið,

(b)  :math:`\oint_{\cal C} \mbox{${\bf F}$}\cdot\,d\mbox{${\bf r}$}=0` fyrir alla samfellt diffranlega á köflum lokaða stikaferla :math:`\mbox{${\bf r}$}` í :math:`D`,

(c)  Ferilheildi :math:`\mbox{${\bf F}$}` er óháð vegi.

.. begin-toggle::
  :label: Sýna sönnun

(a) :math:`\Rightarrow` (b). Fylgisetning 5.6.2.
(b) :math:`\Leftrightarrow` (c). Setning 5.6.5.
(c) :math:`\Rightarrow` (a). Setning 5.6.7.

.. end-toggle::


.. index::
  flötur

Fletir
------

Óformleg skilgreining 
~~~~~~~~~~~~~~~~~~~~~~

:hover:`Flötur` :math:`\cal S` í :math:`{\mathbb  R}^3` er ,,tvívítt" hlutmengi í
:math:`{\mathbb  R}^3`.

Lýsing 
~~~~~~~

Flötum er aðallega lýst með formúlum á þrjá vegu:

#. Gefið er fall :math:`f(x,y,z)`. Fletinum :math:`\cal S` er lýst með
   jöfnu :math:`f(x,y,z)=C` (þ.e.a.s. :math:`\cal S` er :hover:`jafnhæðarflötur,hæðarflötur`
   fallsins :math:`f`). Þá er

   .. math:: \displaystyle {\cal S}=\{(x,y,z)\mid f(x,y,z)=C\}.

#. Gefið er fall skilgreint á ferilsamanhangandi svæði :math:`D` í
   :math:`{\mathbb  R}^2`. Fletinum :math:`\cal S` er lýst sem grafi
   fallsins :math:`f`. Þá er

   .. math:: \displaystyle {\cal S}=\{(x,y,z)\mid (x,y)\in D\mbox{ og } z=f(x,y)\}.

#. Með stikafleti (sjá næstu grein).

.. index::
  stikaflötur

Stikafletir
-----------

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`D` vera ferilsamanhangandi hlutmengi í
:math:`{\mathbb  R}^2`. Samfelld vörpun
:math:`\mbox{${\bf r}$}:D\rightarrow {\mathbb  R}^3; \mbox{${\bf r}$}(u,v)=\big(x(u,v), y(u,v), z(u,v)\big)`
þannig að

.. math:: \displaystyle {\cal S}=\{\mbox{${\bf r}$}(u,v)\mid (u,v)\in D\}

er flötur kallast *stikaflötur*. Segjum að :math:`\mbox{${\bf r}$}` sé
*stikun á fletinum* :math:`\cal S`. Viljum að :math:`\mbox{${\bf r}$}`
sé eintæk vörpun, nema hugsanlega á jaðri :math:`D`. Ritum einnig

.. math:: \displaystyle

   \frac{\partial \mbox{${\bf r}$}}{\partial u}=
   \bigg(\frac{\partial x}{\partial u}, \frac{\partial y}{\partial u},
   \frac{\partial z}{\partial u}\bigg)\quad\mbox{ og }\quad
   \frac{\partial \mbox{${\bf r}$}}{\partial v}=
   \bigg(\frac{\partial x}{\partial v}, \frac{\partial y}{\partial v},
   \frac{\partial z}{\partial v}\bigg).

Snertiplön
----------

Setning 
~~~~~~~~

#. Látum :math:`\cal S` vera flöt sem er gefinn sem :hover:`jafnhæðarflötur,hæðarflötur`
   :math:`f(x,y,z)=C`. Ef :math:`(a, b, c)` er punktur á fletinum og
   fallið :math:`f` er diffranlegt í punktinum :math:`(a, b,c)` þá er
   vigurinn :math:`\mbox{${\bf n}$}=\nabla f(a, b, c)` hornréttur á
   flötinn í punktinum :math:`(a,b, c)` og ef
   :math:`\nabla f(a, b, c)\neq \mbox{${\bf 0}$}` þá hefur flöturinn
   :hover:`snertiplan,snertislétta` í punktinum. Jafna snertiplansins er

   .. math:: \displaystyle f_1(a, b, c)x+f_2(a, b, c)y+f_3(a, b, c)z=D

   þar sem

   .. math:: \displaystyle

      D= f_1(a, b, c)a+f_2(a, b, c)b
      +f_3(a, b, c)c.

#. Látum :math:`\cal S` vera flöt sem er gefinn sem graf falls
   :math:`z=f(x,y)`. Ef :math:`(a, b, f(a,b))` er punktur á fletinum og
   fallið :math:`f` er diffranlegt í punktinum :math:`(a, b)` þá er
   vigurinn

   .. math:: \displaystyle \mbox{${\bf n}$}=\big(0 ,1 ,f_2(a, b)\big)\times\big(1 ,0 ,f_1(a, b)\big)=\big(f_1(a, b), f_2(a, b), -1\big)

   hornréttur á flötinn í punktinum :math:`(a,b, f(a,b))` og flöturinn
   hefur snertiplan í punktinum. Jafna snertiplansins er

   .. math:: \displaystyle z=f(a, b)+f_1(a, b)(x-a)+f_2(a, b)(y-b).

.. image:: xpart.png
   :width: 70%
   :align: center

..

*Snertivigur við skurðferil sléttunnar* :math:`y=b` *og yfirborðsins* :math:`z = f(x,y)` *í punktinum* :math:`(a,b,f(a,b))` *er* :math:`\mathbf{T}_1 = (1,0,f_1(a,b))`.

.. image:: ypart.png
   :width: 70%
   :align: center

..

*Snertivigur við skurðferil sléttunnar* :math:`x=a` *og yfirborðsins* :math:`z = f(x,y)` *í punktinum* :math:`(a,b,f(a,b))` *er* :math:`\mathbf{T}_2 = (0,1,f_2(a,b))`.

3. Látum
   :math:`\mbox{${\bf r}$}: D\subseteq {\mathbb  R}^2\rightarrow {\mathbb  R}^3`
   vera stikaflöt. Ef :math:`(x_0, y_0, z_0)=\mbox{${\bf r}$}(u_0, v_0)`
   er punktur á fletinum sem
   :math:`\mbox{${\bf r}$}(u,v)=\big(x(u,v), y(u,v), z(u,v)\big)` stikar
   og föllin :math:`x(u,v), y(u,v), z(u,v)` eru diffranleg í punktinum
   :math:`(x_0,
   y_0)` þá er vigurinn

   .. math:: \displaystyle

      \mbox{${\bf n}$}=\frac{\partial \mbox{${\bf r}$}}{\partial u}\times 
      \frac{\partial \mbox{${\bf r}$}}{\partial v}

   reiknaður með :math:`u=u_0` og :math:`v=v_0` þvervigur á flötinn í
   punktinum :math:`(x_0, y_0, z_0)`.

.. index::
  stikun;regluleg
   
Skilgreining 
~~~~~~~~~~~~~

Ef vigrarnir :math:`\frac{\partial \mbox{${\bf r}$}}{\partial u}(u,v)`
og :math:`\frac{\partial \mbox{${\bf r}$}}{\partial v}(u,v)` eru óháðir
fyrir alla punkta :math:`(u,v)\in D` þá er sagt að stikunin sé
*regluleg*.

.. note::
   Ef vigrarnir :math:`\frac{\partial \mbox{${\bf r}$}}{\partial u}(u_0,v_0)` og :math:`\frac{\partial\mbox{${\bf r}$}}{\partial v}(u_0,v_0)` eru óháðir þá spanna þeir snertiplan við flötinn í punktinum :math:`\mbox{${\bf r}$}(u_0,v_0)`. Snertiplanið hefur stikun

   .. math:: \displaystyle
      \Pi(u,v) = \mbox{${\bf r}$}(u_0,v_0)+u\frac{\partial \mbox{${\bf r}$}}{\partial u}(u_0,v_0)+v\frac{\partial \mbox{${\bf r}$}}{\partial v}(u_0,v_0).

.. index::
  flatarheildi
      
Flatarheildi
------------

Verkefni 
~~~~~~~~~

#. Flatarmál flata – sambærilegt við bogalengd ferla.

#. Heildi falls yfir flöt með tilliti til flatarmáls – sambærilegt við
   heildi falls eftir ferli með tilliti til bogalengdar.

#. Heildi vigursviðs yfir flöt – svipar til heildis vigursviðs eftir
   ferli.

Flatarmál flata
---------------

Formúla 
~~~~~~~~

Látum :math:`f(x,y)` vera diffranlegt fall skilgreint á mengi :math:`D`
í :math:`{\mathbb  R}^2`. Flatarmál grafsins :math:`z=f(x,y)` er gefið
með formúlunni

.. math:: \displaystyle

   A=\int\!\!\!\int_D dS=\int\!\!\!\int_D {\textstyle\sqrt{1+
   \big(\frac{\partial f}{\partial x}\big)^2+
   \big(\frac{\partial f}{\partial y}\big)^2}}\,\,dx\,dy.


Skilgreining 
~~~~~~~~~~~~~

Látum :math:`\mbox{${\bf r}$}:D\rightarrow {\mathbb  R}^3` vera
reglulegan stikaflöt sem stikar flöt :math:`\cal S`. Flatarmál
:math:`\cal S` er

.. math:: \displaystyle

   A=\int\!\!\!\int_D\,dS=\int\!\!\!\int_D \big|{\textstyle\frac{\partial \mbox{${\bf r}$}}{\partial u}
   \times\frac{\partial \mbox{${\bf r}$}}{\partial v}}\big|\,dudv.

Formúlur 
~~~~~~~~~

Ritum :math:`dS` fyrir flatarmálselement á fleti :math:`\cal S`.

-  Ef
   :math:`\mbox{${\bf r}$}:D\subseteq{\mathbb  R}^2\rightarrow {\mathbb  R}^3`
   er stikun á :math:`\cal S` þá er

   .. math:: \displaystyle

      dS=\bigg|\frac{\partial \mbox{${\bf r}$}}{\partial u}\times\frac{\partial
        \mbox{${\bf r}$}}{\partial v}\bigg|\,du\,dv.

-  Ef :math:`\cal S` er graf :math:`z=g(x,y)` þá er

   .. math:: \displaystyle dS=\sqrt{1+g_1(x,y)^2+g_2(x,y)^2}\,dx\,dy.



-  Gerum ráð fyrir að flöturinn :math:`\cal S` í :math:`{\mathbb  R}^3`
   hafi þann eiginleika að ofanvarp hans á :math:`xy`-planið sé eintækt
   eða með öðrum orðum hægt er að lýsa fletinum sem grafi
   :math:`z=f(x,y)`. Ef :math:`\mbox{${\bf n}$}` er þvervigur á flötinn
   og :math:`\gamma` er hornið sem :hover:`þvervigurinn,þvervigur` :math:`\mbox{${\bf n}$}`
   myndar við jákvæða hluta :math:`z`-ássins þá er

   .. math:: \displaystyle

      dS=\bigg|\frac{1}{\cos\gamma}\bigg|\,dx\,dy
      =\frac{|\mbox{${\bf n}$}|}{|\mbox{${\bf n}$}\cdot\mbox{${\bf k}$}|}\,dx\,dy.

   Í þessu tilviki gildir einnig að ef :math:`\cal S` er lýst sem
   hæðarfleti :math:`G(x,y,z)=C` þá er

   .. math:: \displaystyle dS=\bigg|\frac{\nabla G(x,y,z)}{G_3(x,y,z)}\bigg|\,dx\,dy.

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`\mbox{${\bf r}$}: D\rightarrow {\mathbb  R}^3` vera
reglulega stikun á fleti :math:`\cal S`. Heildi falls :math:`f(x,y,z)`
yfir flötinn :math:`\cal S` með tilliti til flatarmáls er

.. math:: \displaystyle

   \int\!\!\!\int_{\cal S} f\,dS=\int\!\!\!\int_D f(\mbox{${\bf r}$}(u,v)) \big|{\textstyle\frac{\partial
       \mbox{${\bf r}$}}{\partial u} 
   \times\frac{\partial \mbox{${\bf r}$}}{\partial v}}\big|\,dudv.

.. index::
  einingarþvervigrasvið
   
Einingarþvervigrasvið
---------------------

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`\cal S` vera flöt í :math:`{\mathbb  R}^3` sem hefur :hover:`snertiplan,snertislétta` í punkti :math:`P`.
*Einingarþvervigur* :math:`\mbox{${\bf n}$}` á flötinn :math:`\cal S` í
punktinum :math:`P` er :hover:`einingarvigur` hornréttur á snertiplan við flötinn
í punktinum :math:`P`.

*Einingarþvervigrasvið* á :math:`\cal S` er samfellt :hover:`vigursvið`
:math:`\mbox{${\bf N}$}` sem er skilgreint í öllum punktum
:math:`\cal S` þannig að fyrir :math:`(x,y,z)\in{\cal S}` er vigurinn
:math:`\mbox{${\bf n}$}(x,y,z)` einingarvigur sem er hornréttur á
snertiplan við flötinn í punktinum :math:`(x,y,z)`.

.. image:: normalfield.png
   :width: 50%
   :align: center

.. index::
  flötur;áttanlegur
  áttun
   
Áttanlegir fletir
-----------------

Skilgreining 
~~~~~~~~~~~~~

Flöturinn :math:`\cal S` er sagður :hover:`áttanlegur` ef til er
einingarþvervigrasvið :math:`\mbox{${\bf N}$}` á :math:`\cal S`.

:hover:`Áttun` á áttanlegum fleti felst í því að velja annað af tveimur mögulegum
einingaþvervigrasviðum.

.. image:: mobius.png
   :width: 40%
   :align: center

..

*Möbiusarborði er ekki áttanlegur.*

Umræða 
~~~~~~~

Ef áttanlegur flötur :math:`\cal S` hefur jaðar þá skilgreinir áttunin
stefnu á jaðri :math:`\cal S`. Venjan er að velja stefnu jaðarsins
þannig að þegar gengið er eftir honum sé einingarþvervigrasviðið á
vinstri hönd (hægri handar regla).

Ef tveir áttanlegir fletir hafa jaðar má splæsa þeim saman í áttanlegan
flöt með því að líma þá saman á (hluta af) jöðrunum og gæta þess að
jaðrarnir hafi andstæða stefnu á samskeytunum.

.. image:: joinsurf.png
   :width: 70%
   :align: center

Setning 
~~~~~~~~

Gerum ráð fyrir að :math:`\cal S` sé :hover:`áttanlegur` flötur og
:math:`\mbox{${\bf r}$}:D\subseteq{\mathbb  R}^2\rightarrow {\mathbb  R}^3`
sé regluleg stikun á :math:`\cal S` (það er,
:math:`\frac{\partial \mbox{${\bf r}$}}{\partial u}` og
:math:`\frac{\partial \mbox{${\bf r}$}}{\partial v}` eru samfelld föll
af :math:`u` og :math:`v` og vigrarnir
:math:`\frac{\partial \mbox{${\bf r}$}}{\partial u}` og
:math:`\frac{\partial \mbox{${\bf r}$}}{\partial v}` eru línulega
óháðir). Þá er

.. math:: \displaystyle

   \mbox{${\bf N}$}=
   \frac{\frac{\partial \mbox{${\bf r}$}}{\partial u}\times\frac{\partial
       \mbox{${\bf r}$}}{\partial v}}
   {|\frac{\partial \mbox{${\bf r}$}}{\partial u}\times\frac{\partial
       \mbox{${\bf r}$}}{\partial v}|}

einingarþvervigrasvið á :math:`\cal S`.

.. index::
  flæði

Heildi vigursviðs yfir flöt - Flæði
-----------------------------------

Skilgreining og ritháttur 
~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`\cal S` vera :hover:`áttanlegan,áttanlegur` flöt stikaðan af reglulegum
stikaferli
:math:`\mbox{${\bf r}$}:D\subseteq{\mathbb  R}^2\rightarrow {\mathbb  R}^3`
með samfelldar hlutafleiður. Látum :math:`\mbox{${\bf N}$}` tákna
einingarþvervigrasviðið sem gefið er í Setningu 5.13.3. Heildi vigursviðs
:math:`\mbox{${\bf F}$}` yfir flötinn :math:`\cal S` er skilgreint sem

..
  XXX ref

.. math:: \displaystyle

   \int\!\!\!\int_{\cal S} \mbox{${\bf F}$}\cdot\mbox{${\bf N}$}\,dS
   =\int\!\!\!\int_D \mbox{${\bf F}$}(\mbox{${\bf r}$}(u,v))\cdot \bigg(
   \frac{\partial \mbox{${\bf r}$}}{\partial u}\times\frac{\partial \mbox{${\bf r}$}}{\partial
     v}\bigg)\,
   du\,dv.

Slík heildi eru oft nefnd :hover:`flæði` vigursviðsins :math:`\mbox{${\bf F}$}`
gegnum flötinn :math:`\cal S`.

Ritum :math:`d\mbox{${\bf S}$}=\mbox{${\bf N}$}\,dS`. Þá er

.. math:: \displaystyle \int\!\!\!\int_{\cal S} \mbox{${\bf F}$}\cdot\mbox{${\bf N}$}\,dS=\int\!\!\!\int_{\cal S} \mbox{${\bf F}$}\cdot\,d\mbox{${\bf S}$}.

Samantekt 
~~~~~~~~~~

#. Ef
   :math:`\mbox{${\bf r}$}:D\subseteq{\mathbb  R}^2\rightarrow {\mathbb  R}^3`
   er stikun á :math:`\cal S` þá er

   .. math:: \displaystyle

      d\mbox{${\bf S}$}=\pm \bigg(\frac{\partial \mbox{${\bf r}$}}{\partial u}\times\frac{\partial
        \mbox{${\bf r}$}}{\partial v}\bigg)\,du\,dv.

#. Ef :math:`\cal S` er graf :math:`z=f(x,y)` þá er

   .. math:: \displaystyle

      d\mbox{${\bf S}$}=\pm\bigg(-\frac{\partial f}{\partial x},-\frac{\partial
        f}{\partial y},1\bigg)\,dx\,dy.

#. Gerum ráð fyrir að flöturinn :math:`\cal S` í :math:`{\mathbb  R}^3`
   hafi þann eiginleika að ofanvarp hans á :math:`xy`-planið sé eintækt
   eða með öðrum orðum hægt er að lýsa fletinum sem grafi
   :math:`z=f(x,y)`. Ef fletinum :math:`\cal S` er lýst sem hæðarfleti
   :math:`G(x,y,z)=C` þá er

   .. math:: \displaystyle

      d\mbox{${\bf S}$}=\pm\frac{\nabla G(x,y,z)}{|\nabla G(x,y,z)|}\,dS=
      \pm\frac{\nabla G(x,y,z)}{G_3(x,y,z)}\,dx\,dy.

Val á :hover:`áttun` felst í því að velja :math:`+` eða :math:`-` í formúlunum
hér að ofan.

Túlkun 
~~~~~~~

Hugsum okkur að vigursviðið :math:`\mbox{${\bf F}$}` lýsi streymi vökva.
Hugsum svo flötinn :math:`\cal S` sem himnu sem vökvinn getur streymt í
gegnum. Áttun á :math:`\cal S` gefur okkur leið til að tala um hliðar
flatarins og að vökvinn streymi í gegnum flötinn frá einni hlið til
annarrar. Streymi vökvans gegnum flötinn (rúmmál per tímaeiningu) er
gefið með heildinu
:math:`\int\!\!\!\int_{\cal S} \mbox{${\bf F}$}\cdot\mbox{${\bf N}$}\,dS`
þar sem streymi í stefnu :math:`\mbox{${\bf N}$}` reiknast jákvætt.

.. image:: flux.png
   :width: 40%
   :align: center 


