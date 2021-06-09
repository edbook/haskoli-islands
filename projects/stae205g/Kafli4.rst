

Margföld heildi
===============

*A bruise is a lesson... and each lesson makes us better.*

\- George R.R. Martin, A Game of Thrones


.. index::
  skipting

Skiptingar
----------

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`R=[a,b]\times[c,d]` vera rétthyrning í planinu. *Skipting*
:math:`P` á rétthyrningnum :math:`R` felst í því að taka skiptingar

.. math:: \displaystyle

   a=x_0<x_1<\cdots<x_m=b\qquad\mbox{og}\qquad
   c=y_0<y_1<\cdots<y_n=d

á bilunum :math:`[a,b]` og :math:`[c,d]` og nota þær skiptingar til að
skipta :math:`R` upp í rétthyrninga
:math:`[x_i,x_{i+1}]\times [y_j,y_{j+1}]`. Ritum
:math:`\Delta x_i=x_{i+1}-x_i` og :math:`\Delta y_j=y_{j+1}-y_j`. *Norm*
skiptingarinnar :math:`P`, táknað með :math:`\|P\|`, er skilgreint sem
lengd lengstu hornalínu í rétthyrningunum
:math:`[x_i,x_{i+1}]\times [y_j,y_{j+1}]`.



.. image:: skipting.png
   :width: 50% 
   :align: center


*Skipting* :math:`P` *á rétthyrningi* :math:`R= [a,b]\times [c,d]`.

.. index::
  Riemann-summa


Riemann-summa
-------------

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`f` vera fall skilgreint á rétthyrningi
:math:`R=[a,b]\times[c,d]` og látum :math:`P` vera skiptingu á
:math:`R`. Veljum úr hverjum rétthyrningi
:math:`[x_i,x_{i+1}]\times [y_j,y_{j+1}]` punkt :math:`(x_i^*, y_j^*)`.
Skilgreinum *Riemann-summuna*

.. math:: \displaystyle

   \mathcal{R}(f,P)=\sum_{i=1}^m\sum_{j=1}^n f(x_i^*, y_j^*)\Delta x_i\Delta
     y_j.

.. image:: skipting2.png
   :width: 80% 
   :align: center 
   
.. image:: double.png
   :width: 75% 
   :align: center

.. index::
  heildi;tvöfalt heildi
   
   
Tvöfalt heildi yfir rétthyrning
-------------------------------

Skilgreining 
~~~~~~~~~~~~~

Sagt er að fall :math:`f` skilgreint á rétthyrningi
:math:`R=[a,b]\times [c,d]` sé :hover:`heildanlegt,heildanlegur` yfir :math:`R` með :hover:`heildi,tegur`
:math:`I` (hér stendur :math:`I` fyrir tölu) ef fyrir sérhvert
:math:`\varepsilon>0` er til tala :math:`\delta>0` þannig að
:math:`|\mathcal{R}(f,P)-I|<\varepsilon` fyrir allar skiptingar
:math:`P` með :math:`\|P\|<\delta` óháð vali á punktunum
:math:`(x_i^*, y_j^*)`.

Ritum þá

.. math:: \displaystyle \int\!\!\!\int_R f(x,y)dA=I.

Tvöfalt heildi yfir takmarkað svæði
-----------------------------------

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`D` vera takmarkað svæði í planinu. Fall :math:`f` er sagt
:hover:`heildanlegt,heildanlegur` yfir :math:`D` ef til er rétthyrningur :math:`R` sem
inniheldur :math:`D` og fallið

.. math:: \displaystyle

   \hat{f}(x,y)=\left\{\begin{array}{rcl}
   f(x,y)& & \mbox{ef }(x,y)\in D,\\
   0& & \mbox{ef }(x,y)\in R\setminus D
   \end{array}\right.

er heildanlegt yfir :math:`R`.

Setning 
~~~~~~~~

Látum :math:`f` vera samfellt fall skilgreint á lokuðu og takmörkuðu
svæði :math:`D` í planinu :math:`{\mathbb  R}^2`. Gerum ráð fyrir að
jaðar :math:`D` samanstandi af endanlega mörgum ferlum sem hafa
endanlega lengd. Þá er fallið :math:`f` :hover:`heildanlegt,heildanlegur` yfir :math:`D`.

Setning 
~~~~~~~~

Látum :math:`D` vera svæði í planinu og :math:`f` :hover:`takmarkað,takmarkaður` fall
skilgreint á :math:`D` og :hover:`heildanlegt,heildanlegur` yfir :math:`D`. Þá gildir:

#. :math:`\int\!\!\!\int_D f(x,y)\,dA=0` ef flatarmál :math:`D` er 0.

#. :math:`\int\!\!\!\int_D 1\,dA=` flatarmál :math:`D`.

#. Ef :math:`f(x,y)\geq 0` fyrir alla punkta :math:`(x,y)` í :math:`D`
   þá er :math:`\int\!\!\!\int_D f(x,y)\,dA` jafnt rúmmáli rúmskikans
   sem liggur milli :math:`D` og grafsins :math:`z=f(x,y)`.

#. Ef :math:`f(x,y)\leq 0` fyrir alla punkta :math:`(x,y)` í :math:`D`
   þá er :math:`\int\!\!\!\int_D f(x,y)\,dA` jafnt mínus rúmmáli
   rúmskikans sem liggur milli :math:`D` og grafsins :math:`z=f(x,y)`.

Setning 
~~~~~~~~

Ef :math:`D` er svæði í planinu og :math:`f` og :math:`g` heildanleg
föll yfir :math:`D` þá gildir:

#. Ef :math:`L` og :math:`M` eru fastar þá er

   .. math:: \displaystyle

      \int\!\!\!\int_D Lf(x,y)+Mg(x,y)\,dA=L\!\int\!\!\!\int_D f(x,y)\,dA+M\!\int\!\!\!\int_D
      g(x,y)\,dA.

#. Ef :math:`f(x,y)\leq g(x,y)` þá er

   .. math:: \displaystyle \int\!\!\!\int_D f(x,y)\,dA\leq \int\!\!\!\int_Dg(x,y)\,dA.

#. Þríhyrningsójafna: 

  .. math:: \bigg|\int\!\!\!\int_D f(x,y)\,dA\bigg|\leq \int\!\!\!\int_D |f(x,y)|\,dA.

#. Ritum :math:`D` sem sammengi af svæðum :math:`D_1,\ldots, D_k` sem
   skarast ekki nema mögulega í jaðarpunktum þá er

   .. math:: \displaystyle \int\!\!\!\int_D f(x,y)\,dA=\sum_{i=1}^k\int\!\!\!\int_{D_i}f(x,y)\,dA.

.. index::
  Fubini;setning Fubinis
   
Setning Fubinis 
~~~~~~~~~~~~~~~~

Látum :math:`f` vera jákvætt fall sem er :hover:`heildanlegt,heildanlegur` á rétthyrningi
:math:`R=[a,b]\times
[c,d]`. Setjum

.. math:: \displaystyle A(x)=\int_c^d f(x,y)\,dy\qquad\mbox{($x$ hugsað sem fasti þegar heildað)}.

Þá gildir að

.. math:: \displaystyle

   \int\!\!\!\int_R f(x,y)\,dA=\int_a^b A(x)\,dx=\int_a^b\!\!\int_c^d
   f(x,y)\,dy\,dx.

Sömuleiðis gildir þegar við setjum

.. math:: \displaystyle A(y)=\int_a^b f(x,y)\,dx\qquad\mbox{($y$ hugsað sem fasti þegar heildað)} \qquad \text{að}

.. math:: \displaystyle

   \int\!\!\!\int_R f(x,y)\,dA=\int_c^d A(y)\,dy=\int_c^d\!\!\int_a^b
   f(x,y)\,dx\,dy.

.. image:: ax1.png
   :width: 50% 
   :align: center

.. note::

  Setning Fubinis er stundum kölluð brauðsneiðareglan. Ef við ímyndum okkur að rúmskikinn sem liggur milli graf jákvæðs falls og :math:`xy`-sléttunnar sé brauðhleifur, þá má reikna rúmmál hans með því að skera hann í næfurþunnar brauðsneiðar sem liggja samsíða annað hvort :math:`x`-ás eða :math:`y`-ás, reikna svo rúmmál hverrar brauðsneiðar fyrir sig og leggja saman.
   
:math:`x`-einföld og :math:`y`-einföld svæði
--------------------------------------------

.. index::
  x-einfaldur
  y-einfaldur

Skilgreining 
~~~~~~~~~~~~~

Svæði :math:`D` í planinu er sagt vera :math:`y`\ *-einfalt* ef hægt er
að finna tölur :math:`a` og :math:`b` og föll :math:`c(x)` og
:math:`d(x)` þannig að

.. math:: \displaystyle D=\{(x,y)\mid a\leq x\leq b, c(x)\leq y\leq d(x)\}.

Svæði :math:`D` í planinu er sagt vera :math:`x`\ *-einfalt* ef hægt er
að finna tölur :math:`c` og :math:`d` og föll :math:`a(y)` og
:math:`b(y)` þannig að

.. math:: \displaystyle D=\{(x,y)\mid c\leq y\leq d, a(y)\leq x\leq b(y)\}.

.. image:: einfalt.png
   :width: 65% 
   :align: center

Regla 
~~~~~~

Lokað og takmarkað svæði :math:`D` í planinu er :math:`y`-einfalt ef og
aðeins ef sérhver lína af gerðinni :math:`x=x_0` sker :math:`D` í
línustriki.

Lokað og takmarkað svæði :math:`D` er :math:`x`-einfalt ef og aðeins ef
sérhver lína af gerðinni :math:`y=y_0` sker svæðið í línustriki.

Heildi yfir :math:`x`-einföld og :math:`y`-einföld svæði
--------------------------------------------------------

Setning 
~~~~~~~~

Látum :math:`D=\{(x,y)\mid a\leq x\leq b, c(x)\leq y\leq d(x)\}` vera
:math:`y`-einfalt svæði og :math:`f(x,y)` jákvætt fall sem er heildanlegt yfir
:math:`D`. Þá er

.. math:: \displaystyle \int\!\!\!\int_D f(x,y)\,dA=\int_a^b\!\!\!\int_{c(x)}^{d(x)}f(x,y)\,dy\, dx.

Látum :math:`D=\{(x,y)\mid c\leq y\leq d, a(y)\leq x\leq b(y)\}` vera
:math:`x`-einfalt svæði og :math:`f(x,y)` jákvætt fall sem er heildanlegt yfir
:math:`D`. Þá er

.. math:: \displaystyle \int\!\!\!\int_D f(x,y)\,dA=\int_c^d\!\!\!\int_{a(y)}^{b(y)}f(x,y)\,dx\, dy.

.. image:: einfalt2.png
   :width: 35% 
   :align: center

..

*Hér er svæðinu* :math:`D` *skipt í endanlega mörg* :math:`x`-*einföld* og :math:`y`-*einföld svæði sem skarast eingöngu í punktum á jaðrinum.*

.. index::
  heildi;óeiginlegt heildi

Óeiginleg heildi
----------------

Umræða 
~~~~~~~

Látum :math:`f(x,y)\geq 0` vera jákvætt fall sem er skilgreint á svæði
:math:`D` í sléttunni. Ef

#. :math:`D` er ótakmarkað svæði eða

#. :math:`f(x,y)` er ótakmarkað á :math:`D`

má í sumum tilfellum skilgreina tvöfalda heildið af :math:`f` yfir
:math:`D`.

Það er gert með því að finna fyrst runu af stækkandi lokuðum og
takmörkuðum mengjum
:math:`D_1 \subseteq D_2 \subseteq \cdots \subseteq D` sem ’stefnir á’
:math:`D`. Ef

.. math:: \displaystyle \int\!\!\!\int_{D_n} f(x,y)\,dA

er vel skilgreint fyrir öll :math:`n` og hefur markgildi þegar
:math:`n\to \infty` (fyrir allar ólíkar runur :math:`(D_n)_{n\geq 1}`)
þá skilgreinum við :hover:`óeiginlega heildið,óeiginlegt heildi`

.. math:: \displaystyle \int\!\!\!\int_{D} f(x,y)\,dA := \lim_{n\to \infty} \int\!\!\!\int_{D_n} f(x,y)\,dA .

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`f` vera fall sem er heildanlegt yfir svæði :math:`D` í
:math:`{\mathbb  R}^2`. *Meðalgildi* fallsins :math:`f` á :math:`D` er
skilgreint sem talan

.. math:: \displaystyle \bar{f}=\frac{1}{\mbox{flatarmál }D}\int\!\!\!\int_D f(x,y)\,dA.


.. index::
  samanhangandi
  ferilsamanhangandi

Skilgreining 
~~~~~~~~~~~~~

Segjum að mengi :math:`D\subseteq {\mathbb  R}^2` sé
*ferilsamanhangandi* (e. path-connected) ef fyrir sérhverja
tvo punkta :math:`P, Q\in D` gildir að til er stikaferill
:math:`\mbox{${\bf r}$}:[0,1]\rightarrow D` þannig að
:math:`\mbox{${\bf r}$}(0)=P` og :math:`\mbox{${\bf r}$}(1)=Q`.

.. warning:: 
   Í bók er orðið *connected* notað fyrir hugtakið *ferilsamanhangandi*. Venjulega er orðið *connected* notað yfir annað hugtak, skylt en samt ólíkt.


.. index::
  meðalgildissetning
   
Setning (:hover:`Meðalgildissetning` fyrir tvöföld heildi)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`f`
sé samfellt fall sem er skilgreint á lokuðu, takmörkuðu og ferilsamanhangandi
svæði :math:`D` í :math:`{\mathbb  R}^2`. Þá er til punktur
:math:`(x_0,y_0)` í :math:`D` þannig að

.. math:: \displaystyle \frac{1}{\mbox{flatarmál }D}\int\!\!\!\int_D f(x,y)\,dA=f(x_0,y_0).

.. index::
  breytuskipti

Breytuskipti
------------

Upprifjun 
~~~~~~~~~~

Látum :math:`P=(x,y)\neq \mbox{${\bf 0}$}` vera punkt í plani. :hover:`Pólhnit`
:math:`P` er talnapar :math:`[r,\theta]` þannig að :math:`r` er fjarlægð
:math:`P` frá :math:`O=(0,0)` og :math:`\theta` er hornið á milli
striksins :math:`\overline{OP}` og :math:`x`-ássins. (Hornið er mælt
þannig að rangsælis stefna telst jákvæð, og leggja má við :math:`\theta`
heil margfeldi af :math:`2\pi`.)

.. index::
  pólhnitarétthyrningur

Skilgreining 
~~~~~~~~~~~~~

*Pólhnitarétthyrningur* í :math:`xy`-planinu er svæði sem afmarkast af
tveimur hringbogum :math:`x^2+y^2=a^2` og :math:`x^2+y^2=b^2` og tveimur
hálflínum sem byrja í :math:`(0,0)` og mynda hornin :math:`\alpha` og
:math:`\beta` við :math:`x`-ásinn (Hornin eru mæld þannig að rangsælis
stefna telst jákvæð.)

.. image:: polarrett.png
   :width: 40% 
   :align: center

Gerum ráð fyrir að :math:`0\leq a\leq b` og að
:math:`0\leq\beta-\alpha\leq
2\pi`. Þá má lýsa pólhnitarétthyrningnum með því að nota pólhnit þannig
að

.. math:: \displaystyle D=\{[r,\theta]\mid 0\leq a\leq r\leq b, \alpha\leq \theta\leq\beta\}.

Setning 
~~~~~~~~

Ef :math:`f` er fall sem er :hover:`heildanlegt,heildanlegur` yfir pólhnitarétthyrning
:math:`D=\{[r,\theta]\mid 0\leq a\leq r\leq b, \alpha\leq \theta\leq\beta\}`
þá er

.. math:: \displaystyle

   \int\!\!\!\int_D f(x,y)\,dA=\int_\alpha^\beta\!\!\!\int_{a}^{b}
   f(r\cos\theta,r\sin\theta)\,r\,dr\, d\theta.

.. image:: polarelement.png
   :width: 90% 
   :align: center

.. index::
  pólhnitagraf
   
Upprifjun 
~~~~~~~~~~

Látum :math:`f` vera fall skilgreint á bili :math:`[\alpha,\beta]`.
Jafnan :math:`r=f(\theta)` lýsir mengi allra punkta í planinu sem hafa
:hover:`pólhnit` á forminu :math:`[f(\theta),\theta]` þar sem
:math:`\alpha\leq\theta\leq\beta`. Þetta mengi kallast *pólhnitagraf*
fallsins :math:`f`.

Setning 
~~~~~~~~

Látum :math:`D` vera svæði í :math:`xy`-plani sem afmarkast af
pólhnitalínum :math:`\theta=\alpha` og :math:`\theta=\beta` og tveimur
pólhnitagröfum :math:`r=a(\theta)` og :math:`r=b(\theta)`. Gerum ráð
fyrir að :math:`0\leq a(\theta)\leq
r\leq b(\theta)` og :math:`0\leq \beta-\alpha\leq 2\pi`. Ef :math:`f` er
heildanlegt fall yfir :math:`D` þá er

.. math:: \displaystyle

   \int\!\!\!\int_D\,f(x,y)\,dA=\int_\alpha^\beta\!\!\!\int_{a(\theta)}^{b(\theta)}
   f(r\cos\theta,r\sin\theta)\,r\,dr\, d\theta.

.. image:: polarsvaedi.png
   :width: 45% 
   :align: center

Regla 
~~~~~~

Hugsum okkur að :math:`f(x,y)` sé fall og hægt sé að rita
:math:`f(x,y)=g(x)h(y)`. Látum :math:`R=[a,b]\times [c,d]`. Þá er

.. math:: \displaystyle

   \begin{aligned}
   \int\!\!\!\int_R f(x,y)\,dA&=\int_a^b\!\!\!\int_{c}^{d}g(x)h(y)\,dy\, dx\\
   &=\bigg(\int_a^b g(x)\,dx\bigg)\bigg(\int_c^d h(y)\,dy\bigg).\end{aligned}

Setning (Almenn breytuskiptaregla fyrir tvöföld heildi)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`x=x(u,v)`, :math:`y=y(u,v)` vera gagntæka vörpun milli
svæðis :math:`S` í :math:`uv`-plani og svæðis :math:`D` í
:math:`xy`-plani. Gerum ráð fyrir að föllin :math:`x(u,v)`,
:math:`y(u,v)` hafi samfelldar fyrsta stigs hlutafleiður á :math:`S`. Ef
:math:`f` er heildanlegt fall yfir :math:`D`, þá er fallið
:math:`g(u,v)=f(x(u,v), y(u,v))` heildanlegt yfir :math:`S` og

.. math:: \displaystyle

   \int\!\!\!\int_D f(x,y)\,dx\,dy=\int\!\!\!\int_S g(u,v)
   \bigg|\frac{\partial(x,y)}{\partial(u,v)}\bigg|\,du\,dv.

.. image:: changevar.png
   :width: 90% 
   :align: center

.. index::
  heildi; þrefalt heildi
   
Þreföld heildi
--------------

Umræða 
~~~~~~~

:hover:`Heildi,tegur` falls :math:`f(x,y,z)` yfir kassa
:math:`K=[a,b]\times[c,d]\times[u,v]` í :math:`{\mathbb  R}^3` er
skilgreint á sambærilegan hátt og tvöfalt heildi er skilgreint.

Á sama hátt og fyrir tvöföld heildi má svo skilgreina heildi fyrir
almennari :hover:`rúmskika,rúmskiki~ í :math:`{\mathbb  R}^3`.

:hover:`Heildi,tegur` falls :math:`f(x,y,z)` yfir :hover:`rúmskika` :math:`R` er táknað með

.. math:: \displaystyle \int\!\!\!\int\!\!\!\int_R f(x,y,z)\,dV.

(:math:`dV` stendur fyrir að heildað er með tilliti til rúmmáls.)

Setning 
~~~~~~~~

Látum :math:`f(x,y,z)` vera fall sem er :hover:`heildanlegt,heildanlegur` yfir kassa
:math:`K=[a,b]\times[c,d]\times[u,v]` í :math:`{\mathbb  R}^3`. Þá er

.. math:: \displaystyle

   \int\!\!\!\int\!\!\!\int_K f(x,y,z)\,dV=
   \int_a^b\!\int_c^d\!\int_u^v f(x,y,z)\,dz\,dy\,dx.

Breyta má röð heilda að vild, t.d. er

.. math:: \displaystyle

   \int\!\!\!\int\!\!\!\int_K f(x,y,z)\,dV=
   \int_u^v\!\int_c^d\!\int_a^b f(x,y,z)\,dx\,dy\,dz.

Setning 
~~~~~~~~

Látum :math:`f(x,y,z)` vera fall sem er heildanlegt yfir rúmskika
:math:`R` og gerum ráð fyrir að :math:`R` hafi lýsingu á forminu

.. math:: \displaystyle R=\{(x,y,z)\mid a\leq x\leq b,\ c(x)\leq y\leq d(x),\ u(x,y)\leq z\leq v(x,y)\}.

Þá er

.. math:: \displaystyle

   \int\!\!\!\int\!\!\!\int_R f(x,y,z)\,dV=
   \int_a^b\!\int_{c(x)}^{d(x)}\!\int_{u(x,y)}^{v(x,y)} f(x,y,z)\,dz\,dy\,dx.

Breyturnar :math:`x, y, z` geta svo skipt um hlutverk.



Setning (Almenn breytuskiptaformúla fyrir þreföld heildi.) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum

.. math:: \displaystyle (u,v,w)\mapsto (x(u,v,w), y(u,v,w), z(u,v,w))

vera gagntæka vörpun milli rúmskika :math:`R` í :math:`xyz`-rúmi og
rúmskika :math:`S` í :math:`uvw`-rúmi. Gerum ráð fyrir að föllin
:math:`x(u,v,w), y(u,v,w), z(u,v,w)` hafi öll samfelldar fyrsta stigs
hlutafleiður. Ef :math:`f(x,y,z)` er fall sem er heildanlegt yfir
:math:`R` þá er

.. math:: \displaystyle

   \begin{aligned}
   \int\!\!\!\int\!\!\!\int_R& f(x,y,z)\,dV \\&=\int\!\!\!\int\!\!\!\int_S f(x(u,v,w), y(u,v,w), z(u,v,w))
   \bigg|\frac{\partial(x,y,z)}{\partial(u,v,w)}\bigg|\,du\,dv\,dw.\end{aligned}

   
.. index::
  sívalningshnit
  
   
Skilgreining 
~~~~~~~~~~~~~

Látum :math:`(x,y,z)` vera punkt í :math:`{\mathbb  R}^3`.
:hover:`Sívalningshnit` :math:`(x,y,z)` eru þrennd talna :math:`r, \theta, z`
þannig að

.. math:: \displaystyle x=r\cos\theta\qquad\qquad y=r\sin\theta\qquad\qquad z=z.

.. note:: 
   Athugið að :math:`[r,\theta]` eru pólhnit punktsins :math:`(x,y)`.
  
.. index::
  sívalningshnit;breytuskipti
  
  
Setning (Breytuskipti yfir í sívalningshnit.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`R` vera rúmskika í :math:`{\mathbb  R}^3` og látum
:math:`f(x,y,z)` vera heildanlegt fall yfir :math:`R`. Gerum ráð fyrir
að :math:`R` megi lýsa með eftirfarandi skorðum á sívalningshnit
punktanna sem eru í :math:`R`

.. math:: \displaystyle \alpha\leq \theta\leq \beta,\ a(\theta)\leq r\leq  b(\theta), u(r,\theta)\leq z\leq v(r,\theta),

þar sem :math:`0\leq \beta-\alpha\leq 2\pi`. Þá er

.. math:: \displaystyle

   \int\!\!\!\int\!\!\!\int_R f(x,y,z)\,dV= 
   \int_\alpha^\beta
   \!\int_{a(\theta)}^{b(\theta)}\int_{u(r,\theta)}^{v(r,\theta)}      
   f(r\cos\theta,r\sin\theta,z)r\,dz\,dr\,d\theta.


.. index::
  kúluhnit   
   
Kúluhnit
--------

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`(x,y,z)` vera punkt í :math:`{\mathbb  R}^3`. :hover:`Kúluhnit`
:math:`(x,y,z)` eru þrennd talna :math:`\rho, \varphi, \theta` þannig að

.. math:: \displaystyle x=\rho\sin\varphi\cos\theta\qquad\qquad y=\rho\sin\varphi\sin\theta\qquad\qquad z=\rho\cos\varphi.

Punktur sem hefur kúluhnit :math:`\rho, \varphi, \theta` er táknaður með
:math:`[\rho, \varphi, \theta]`.

.. image:: sphere.png
   :width: 80% 
   :align: center

Umræða 
~~~~~~~

Eftirfarandi jöfnur gefa aðferð til að finna :hover:`kúluhnit`:

-  :math:`\rho` er fjarlægðin frá :math:`(0,0,0)` til :math:`(x,y,z)`, það er að
   segja

   .. math:: \displaystyle \rho=\sqrt{x^2+y^2+z^2}.

-  :math:`\varphi` er hornið á milli jákvæða hluta :math:`z`-ássins og línustriksins frá
   :math:`(0,0,0)` til :math:`(x,y,z)`. Hornið :math:`\varphi` má
   ákvarða út frá jöfnunni

   .. math:: \displaystyle \tan\varphi=\frac{\sqrt{x^2+y^2}}{z}.

-  :math:`\theta` er hornið sem jákvæði hluti :math:`x`-ásins myndar við línustrikið
   frá :math:`(0,0,0)` til :math:`(x,y,0)` (sama horn og notað í
   sívalningshnitum (og pólhnitum)). Hornið :math:`\theta` má finna út
   frá jöfnunni

   .. math:: \displaystyle \tan\theta=\frac{y}{x}.

Um kúluhnit :math:`[\rho, \varphi, \theta]` fyrir punkt :math:`(x,y,z)`
gildir að velja má :math:`\rho, \varphi, \theta` þannig að
:math:`0\leq \rho`, :math:`0\leq\varphi\leq \pi` og
:math:`0\leq\theta\leq 2\pi`.

.. index::
  kúluhnit;breytuskipti


Breytuskipti í kúluhnit
-----------------------

Setning 
~~~~~~~~

Látum :math:`R` vera rúmskika þannig að þegar notuð eru :hover:`kúluhnit` þá fæst
eftirfarandi lýsing

.. math:: \displaystyle

   R=\{[\rho,\varphi,\theta]\mid \alpha\leq\theta\leq\beta, 
   c\leq\varphi\leq d, a\leq \rho\leq b\}.

Ef :math:`f` er fall sem er :hover:`heildanlegt,heildanlegur` yfir :math:`R` þá er

.. math:: \displaystyle

   \begin{aligned}
   &\int\!\!\!\int\!\!\!\int_R f(x,y,z)\,dV=\\ &\int_\alpha^\beta\!\int_c^d\!\int_a^b f(\rho\sin\varphi\cos\theta, \rho\sin\varphi\sin\theta,\rho\cos\varphi)
   \,\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta.\end{aligned}

.. index::
  massamiðja
  vægi
   
Massamiðja
----------

Regla 
~~~~~~

Látum :math:`D` tákna svæði í plani. Hugsum :math:`D` sem plötu þ.a. í
punkti :math:`(x,y)` er efnisþéttleikinn gefinn með falli
:math:`\delta(x,y)`. Massi plötunnar er

.. math:: \displaystyle m=\int\!\!\!\int_D \delta(x,y)\,dA.

*Vægi* plötunnar um línuna :math:`x=0` (þ.e. :math:`y`-ás) og um línuna
:math:`y=0` (þ.e. :math:`x`-ás) eru gefin með

.. math:: \displaystyle M_{x=0}=\int\!\!\!\int_D x\delta(x,y)\,dA \quad \text{og} \quad M_{y=0}=\int\!\!\!\int_D y\delta(x,y)\,dA.

Hnit *massamiðju* plötunnar eru :math:`(\overline{x}, \overline{y})` þar
sem

.. math:: \displaystyle \overline{x}=\frac{M_{x=0}}{m} \quad \text{og}\quad \overline{y}=\frac{M_{y=0}}{m}.

Regla 
~~~~~~

Látum :math:`R` tákna :hover:`rúmskika,rúmskiki`. Hugsum :math:`R` sem hlut þannig að í
punkti :math:`(x,y,z)` er efnisþéttleikinn gefinn með falli
:math:`\delta(x,y,z)`. Massi hlutarins er

.. math:: \displaystyle m=\int\!\!\!\int\!\!\!\int_R \delta(x,y,z)\,dV.

*Vægi* hlutarins um planið :math:`x=0` (þ.e. :math:`yz`-planið) er

.. math:: \displaystyle M_{x=0}=\int\!\!\!\int\!\!\!\int_R x\delta(x,y,z)\,dV.

Svipað skilgreinum við

.. math:: \displaystyle M_{y=0}=\int\!\!\!\int\!\!\!\int_R y\delta(x,y,z)\,dV \quad \text{og}\quad M_{z=0}=\int\!\!\!\int\!\!\!\int_R z\delta(x,y,z)\,dV.

Hnit *massamiðju* hlutarins eru
:math:`(\overline{x}, \overline{y}, \overline{z})` þar sem

.. math:: \displaystyle

   \overline{x}=\frac{M_{x=0}}{m}
   \qquad\mbox{og}\qquad
   \overline{y}=\frac{M_{y=0}}{m}
   \qquad\mbox{og}\qquad
   \overline{z}=\frac{M_{z=0}}{m}.

.. index::
  hverfitregða

   
Hverfitregða
------------

Regla 
~~~~~~

Látum :math:`R` tákna rúmskika. Hugsum :math:`R` sem hlut þannig að í
punkti :math:`(x,y,z)` er efnisþéttleikinn gefinn með falli
:math:`\delta(x,y,z)`. Látum :math:`L` tákna línu (snúningsás) í rúminu.
*Hverfitregða* hlutarins um :math:`L` er

.. math:: \displaystyle I=\int\!\!\!\int\!\!\!\int_R D^2 \,\delta\,dV

þar sem :math:`\delta=\delta(x,y,z)` og :math:`D=D(x,y,z)` er fjarlægð
punktsins :math:`(x,y,z)` frá :math:`L`.

Yfirborðsflatarmál
------------------

Regla 
~~~~~~

Látum :math:`D` vera svæði í plani og :math:`f(x,y)` diffranlegt fall
skilgreint á :math:`D`. Flatarmál grafsins :math:`z=f(x,y)` þar sem
:math:`(x,y)\in D` er gefið með formúlunni

.. math:: \displaystyle S=\int\!\!\!\int_D \sqrt{1+f_1(x,y)^2+f_2(x,y)^2}\,dA.


