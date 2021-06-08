Viðauki
=======

Þrepun
------
Þrepun er leið til þess að sanna setningar og formúlur.
Þá er fyrst sýnt fram á að setningin gildi um grunntilvik (upphafstilvik, núlltilvik).
Að því loknu er sýnt fram á að ef setningin gildir um eitthvert ótiltekið tilvik, þá gildir það um það næsta.

Þetta svipar til þess að ganga upp stiga: ef við getum komist upp fyrsta þrepið og frá hverju þrepi í það næsta, þá hljótum við að geta gengið upp allan stigann.

.. figure:: ./myndir/threpun.svg
    :align: center
    :width: 70%


Hér er til dæmis reglan um að summa allra heiltalna frá einum upp í :math:`n` er:

.. math::
  \sum_{i=1}^n = \frac{n(n+1)}{2}

Við ætlum að sýna fram á að þessi formúla gildi um allar jákvæðar heiltölur :math:`n=1,2,3, \dots` .
Sjáum til dæmis að hún gildir fyrir :math:`n=4` því

.. math::
  \sum_{i=1}^4 = 1+2+3+4 = 10

og

.. math::
  \frac{4\cdot(4+1)}{2} = \frac{20}{2} = 10

Sönnum setninguna með þrepun:

**Grunntilvik:**

Prófum að setja :math:`n=1` í setninguna:

.. math::
  \begin{aligned}
    \sum_{i=1}^n &= \frac{n(n+1)}{2}\\
    \sum_{i=1}^1 &= \frac{1(1+1)}{2}\\
    1&=\frac{1\cdot2}{2}=1
  \end{aligned}

Formúlan virkar því til þess að reikna summu allra talna frá einum upp í einn.

**Þrepun:**

Gerum núna ráð fyrir að formúlan virki fyrir eitthvert :math:`n` , þ.e. að

.. math::
  \sum_{i=1}^n = \frac{n(n+1)}{2}

sé sönn staðhæfing.

Þá ætlum við að sýna að hún gildi líka fyrir næsta skref :math:`n+1` .

.. math::
  \begin{aligned}
    \sum_{i=1}^{n+1} &= \sum_{i=1}^n + (n+1) \\
    &= \frac{n(n+1)}{2} + (n+1) \\
    &= \frac{n(n+1)}{2} + \frac{2(n+1)}{2} \\
    &=\frac{n(n+1)+2(n+1)}{2}\\
    &= \frac{(n+1)(n+2)}{2} \\
  \end{aligned}

Í síðustu línunni birtist formúlan eins og hún væri ef :math:`n+1` væri sett inn í formúluna og því gildir formúlan líka fyrir :math:`n+1` .

Því getum við ályktað að setningin gildi um öll :math:`n` .


Ritháttur
---------

* :math:`\mathbb{N} \quad` "Náttúrulegu tölurnar"
    * :math:`0,1,2,3, \dots` köllum við náttúrulegu tölurnar

* :math:`\mathbb{Z} \quad` "Heiltölur"
    * :math:`\dots ,-3, -2, -1, 0,1,2,3, \dots` köllum við heiltölurnar

* :math:`\mathbb{Q} \quad` "Ræðu tölurna"
    * :math:`\frac{p}{q}` þar sem :math:`p` og :math:`q` eru heilar tölur og :math:`q \neq 0`

* :math:`\mathbb{R} \quad` "Rauntölurnar"
    * mengi allra ræðra talna, auk óræðra talna

* :math:`:= \; \text{eða} \; \equiv \quad` "skilgreint sem"
    * notað til að skilgreina stærðir

* :math:`\in \quad` "stak í"
    * oft erum við að tala um stak í menginu :math:`x \in A` :math:`x` er stak í menginu :math:`A`

* :math:`\notin \quad` "ekki stak í"
    * :math:`x \notin A` :math:`x` er ekki stak í menginu :math:`A`

* :math:`\forall \quad` "fyrir öll"
    * :math:`\forall n \in \mathbb{N}` fyrir öll stök í mengi náttúrulegra talna

* :math:`\approx \quad` "um það bil"
    * :math:`\pi \approx 3.14`

* :math:`< \qquad`  "minna en"
    * :math:`3<4`

* :math:`> \qquad` "stærra en"
    * :math:`6>2`

* :math:`\leq \qquad` "minna en eða jafnt og"
    * :math:`a \leq x \leq b` lokað bil

* :math:`\geq \qquad` "stærra en eða jafnt og"
    * :math:`a \geq x \geq b` opið bil

* :math:`\sum_{n}^{m} \quad` "summa frá n upp í m"
    * við getum haf endanlegar og óendanlegar summur, þ.e.a.s. :math:`m= \infty` eða/og  :math:`n= -\infty`

* :math:`\prod_{n}^{m} \quad` "margfeldi frá n upp í m"
    * við getum haft endanleg og óendanleg margfeldi, þ.e.a.s. :math:`m= \infty` eða/og  :math:`n= -\infty`

* :math:`\parallel \quad` "samsíða"
    * sjá :ref:`kafla um samsíða <s.samsíða>` línur

* :math:`\perp  \quad` "hornrétt" eða "þverstætt"
    * sjá :ref:`kafla um þverstæð <s.þverstæð>` línur

* :math:`\subset \quad` "hlutmengi"
    * t.d. :math:`A \subset B`  :math:`B` er hlutmengi í :math:`A`

* :math:`| \quad \text{eða} \quad ; \quad` "þar sem"
    * oft þegar við erum að skilgreina mengi þá erum við með skilyrði :math:`p(x)`, t.d. :math:`A = \{x \in C \ | \ p(x)\}`. Þetta þýðir að í :math:`A` eru öll stök í :math:`C` **þar sem** :matH:`p(x)` gildir

* :math:`\cup \quad` "sammengi"
    * :math:`A \cup B` "sammengi :math:`A` og :math:`B`“

* :math:`\cap \quad` "sniðmengi"
    * :math:`A \cap B` "sniðmengi :math:`A` og :math:`B`“

* :math:`\setminus \quad` "mengjamismunur"
    * :math:`A\setminus B` ":math:`A` án :math:`B`“

* :math:`A^c \quad` "fyllimengi :math:`A`“
    * :math:`A^c \quad` "allt sem er ekki í :math:`A`“

* :math:`(a,b) \quad \text{eða} \quad ]a,b[ \quad` "opið bil"
    * :math:`(a,b)=\{x\in \mathbb{R}; a<x<b\}`

* :math:`[a,b] \quad` "lokað bil"
    * :math:`[a,b]=\{x\in \mathbb{R}; a\leq x\leq b\}`

* :math:`f(x)|_{x=a} \quad` "stingum in :math:`x=a`“
    * :math:`x^2+3x-1|_{x=3} = (3)^2+3(3)-1 = 17`

* :math:`! \qquad` "aðfeldi" eða "hrópmerkt"
    * :math:`6! = 1 \cdot 2\cdot 3\cdot 4 \cdot 5 \cdot 6 =720`

* :math:`°  \qquad`"gráður"
    * :math:`30°`

* :math:`Rad \quad` "radian" eða "bogaeining"
    * :math:`\frac{\pi}{6} Rad`

* :math:`\boldsymbol{a} \quad \vec{a} \quad \bar{a}  \quad` "vigurinn :math:`a`“
    * sjá  :ref:`Vigrar <s.Vigrar>`

* :math:`f'(x) \quad f' \quad \frac{df}{dx} \quad \frac{d}{dx} f(x) \quad D_x f \qquad` "afleiða :math:`f(x)`“
    * með tilliti til :math:`x`



Formúlublað
-----------
Samantekt af hentugum reglum og formúlum úr köflunum.

Algebra
~~~~~~~

Einfaldar reiknireglur
``````````````````````

.. math::
	\begin{aligned}
	&(a+b)+c=a+(b+c)   \qquad &\textit{ (tengiregla samlagningar)}\\
    \qquad \\
	&(ab)c=a(bc)  \qquad &\textit{ (tengiregla margföldunar)}\\
    \qquad \\
	&a+b=b+a  \qquad &\textit{ (víxlregla samlagningar)} \\
    \qquad \\
	&ab=ba  \qquad &\textit{ (víxlregla margföldunar)}\\
    \qquad \\
	&a(b+c)=ab+ac  \qquad &\textit{ (dreifiregla)}\\
    \qquad \\
	&1 \cdot a=a  \qquad &\textit{ (1 er margföldunarhlutleysa)}\\
    \qquad \\
	&a+0=a  \qquad &\textit{ (0 er samlagningarhlutleysa)}\\
    \qquad \\
	&0 \cdot a=0   \qquad &\textit{ (margföldun með núlli gefur núll)}\\
	\end{aligned}


Brotareiknireglur
`````````````````

.. math::
    \begin{aligned}
    & \frac{p}{q}+\frac{r}{s}=\frac{ps}{qs}+\frac{qr}{qs}=\frac{ps+qr}{qs} \\
    \qquad \\
    &\frac{p}{q}-\frac{r}{s}=\frac{ps-qr}{qs} \\
    \qquad \\
    & \frac{p}{q} \cdot \frac{r}{s}=\frac{pr}{qs} \\
    \qquad \\
    &\frac{p/q}{r/s} =\frac{ps}{qr} \\
    \end{aligned}


Veldareiknireglur
`````````````````

.. math::

	\begin{aligned}
    &a^0=1\\
    \qquad \\
    &a^n=a \cdot a \cdot \dots \cdot a \\
    \qquad \\
	&a^{-n}=\frac{1}{a^n} \\
    \qquad \\
    &a^n\cdot a^m=a^{n+m}\\
    \qquad \\
	&\dfrac {a^n}{a^m}=a^{n-m}\\
    \qquad \\
	&a^n\cdot b^n=(ab)^n\\
    \qquad \\
	&(a^n)^m=a^{nm}
    \qquad \\
    (-1)^n &= 1 \qquad \text{þegar } n \text{ er slétt tala} \\
    \qquad \\
	(-1)^n &= -1 \qquad \text{þegar } n \text{ er oddatala} \\
	\end{aligned}


Reiknireglur fyrir rætur
````````````````````````

.. math::

	\begin{aligned}
	  \sqrt[q]{ab} &=\sqrt[q]{a}\cdot \sqrt[q]{b} \\
    & \qquad \\
    \sqrt[q]{\dfrac ab}& =\dfrac{\sqrt[q]{a}}{\sqrt[q] {b}}\\
    & \qquad \\
    \sqrt[q]{a^p}& =(\sqrt[q]{a})^p\\
    & \qquad \\
    \sqrt[sq]{a^{sp}} &={\sqrt[q]{a^p}}\\
    & \qquad \\
    \sqrt[sq]{ a} &=\sqrt[s]{\sqrt[q]{a}}\\
  \end{aligned}



Jöfnur og ójöfnur
~~~~~~~~~~~~~~~~~

Lausnarformúla annars stigs jöfnu
`````````````````````````````````

Látum :math:`ax^2+bx+c=0` vera annars stigs jöfnu.

1. Ef :math:`d = b^2-4ac<0` þá hefur jafnan enga rauntölulausn.
2. Ef :math:`d  = b^2-4ac=0` þá hefur jafnan eina lausn:

.. math::
	x=\frac{-b}{2a}

3. Ef :math:`d = b^2-4ac>0` þá hefur jafnan tvær lausnir:

.. math::
	x_1=\frac{-b+\sqrt{b^2-4ac}}{2a} \qquad \text{og} \qquad x_2=\frac{-b-\sqrt{b^2-4ac}}{2a}

eða

.. math::
	x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}


Reiknireglur fyrir tölugildi
````````````````````````````

Látum :math:`a` og :math:`b` vera rauntölur. Þá gildir eftirfarandi:

.. math::
	\begin{aligned}
	& a \leq |a|  \qquad  &\text{(tölugildi getur aðeins stækkað tölu)}\\
    \qquad \\
	& |a|=|-a|  \qquad  &\text{(tölugildi eru óháð formerki)}\\
    \qquad \\
	& |a|\cdot|b|=|ab| \qquad  &\text{(tölugildi varðveitir margföldun)}\\
    \qquad \\
	& |a|^2=a^2 \qquad   &\text{(önnur veldi eyða tölugildi)}\\
	\end{aligned}



Regla Pýþagórasar
`````````````````

.. math::
	a^2+b^2=c^2


Fjarlægð milli punkta
`````````````````````
Fjarlægðin milli punktanna :math:`P_1=(x_1,y_1)` og :math:`P_2=(x_2,y_2)` í hnitakerfinu er

.. math::
	\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}

Hallatala línu
``````````````
Ef við höfum tvo punkta :math:`(x_1,y_1)` og :math:`(x_2,y_2)` fæst með formúlunni

.. math::
	h=\frac{y_2-y_1}{x_2-x_1}


Miðpunktsregla
``````````````
Reikna má miðpunkt striksins á milli :math:`A(x_1, x_2)` og :math:`B(x_2,y_2)` með:

.. math::
    M = \left( \frac{x_1+x_2}{2} , \frac{y_1+y_2}{2} \right)


Flatarmál
`````````

Flatarmál :hover:`rétthyrnings, rétthyrningur` er :math:`F=a\cdot b` og ummálið er :math:`U=2a+2b` .

.. figure:: ./myndir/rumfraedi/fl_rett.svg
	:align: center
	:width: 40%

Flatarmál :hover:`samsíðungs, samsíðungur` er :math:`F=g\cdot h`.

.. figure:: ./myndir/rumfraedi/fl_sams.svg
	:align: center
	:width: 40%

Flatarmálið er þá :math:`F=|\bar{a}| \cdot |\bar{b}| \cdot \sin(\theta)` og ummálið er :math:`U=2|\bar{a}|+2|\bar{b}|` .

.. figure:: ./myndir/rumfraedi/fl_sams2.svg
	:align: center
	:width: 40%

Flatarmál hrings er :math:`F=r^2\cdot\pi` og ummálið er :math:`U=2r\pi` .

.. figure:: ./myndir/rumfraedi/fl_hring.svg
	:align: center
	:width: 40%

Flatarmál sporöskju er :math:`F=a\cdot b\cdot\pi` .

.. figure:: ./myndir/rumfraedi/fl_spor.svg
	:align: center
	:width: 40%

Flatarmál :hover:`þríhyrnings, þríhyrningur` er :math:`F=\frac{1}{2}g\cdot h` .

.. figure:: ./myndir/rumfraedi/fl_thri1.svg
	:align: center
	:width: 40%

Flatarmálið er þá :math:`F=\frac{1}{2}|\bar{a}| \cdot |\bar{b}| \cdot \sin(\theta)` .

.. figure:: ./myndir/rumfraedi/fl_thri2.svg
	:align: center
	:width: 40%


Föll
~~~~

Oddstætt og jafnstætt
`````````````````````
Látum :math:`f: \mathbb{R} \to \mathbb{R}` vera fall.

:hover:`Jafnstætt, jafnstæður` ef :math:`f(-x)=f(x)` fyrir öll :math:`x \in \mathbb{R}`.

:hover:`Oddstætt, oddstæður` ef :math:`f(-x)=-f(x)` fyrir öll :math:`x \in \mathbb{R}`.

Lograreglur
```````````

Fyrir :math:`a,b,x,y\in \mathbb{R}_+` og :math:`r \in \mathbb{R}` gildir:

1. :math:`\qquad \log_a(1)=0`
2. :math:`\qquad \log_a(1/x)=-\log_a(x)`
3. :math:`\qquad \log_a(xy)=\log_a(x)+\log_a(y)`
4. :math:`\qquad \log_a(x/y)=\log_a(x)-\log_a(y)`
5. :math:`\qquad \log_a(x^r)=r\log_a(x)`
6. :math:`\qquad \log_a(x)=\dfrac{\log_b(x)}{\log_b(a)}`.

Stofnbrotaliðun
```````````````
.. math::
	\begin{aligned}
	&\frac{ax+b}{(x-\alpha)(x-\beta)} = \frac{A}{(x-\alpha)}+ \frac{B}{(x-\beta)} \\
	&\qquad \text{þar sem} \\
	& \alpha \neq \beta, \quad A= \frac{a\alpha + b}{\alpha - \beta} \quad \text{og} \quad B= \frac{a\beta + b}{\beta - \alpha}
	\end{aligned}


Margliður
~~~~~~~~~

Nokkrar liðanir
```````````````

.. math::
   	(a + b)^0 = 1

.. math::
    (a + b)^1 = a + b

.. math::
    (a + b)^2 = a^2 + 2ab + b^2

.. math::
    (a + b)^3 = a^3 + 3a^2 b + 3a b^2 + b^3

.. math::
    (a + b)^4 = a^4 + 4 a^3 b + 6a^2 b^2 + 4ab^3 + b^4

.. math::
    (a + b)^5 = a^5 + 5a^4 b + 10a^3b^2 + 10a^2 b^3 + 5 ab^4 +b^5



Hornaföll
~~~~~~~~~

Gráður og bogaeiningar
``````````````````````

.. math::
	x \text{Rad} = \left(x \cdot \frac{360}{2 \pi}\right)° \qquad og \qquad  x°=\left( x \cdot \frac{2 \pi}{360}\right) \text{Rad}


Hliðar þríhyrnings
``````````````````

.. math::
    \begin{aligned}
    \sin(\alpha) = \frac{b}{c} \\
    \qquad \\
    \cos(\alpha) = \frac{a}{c} \\
    \qquad \\
    \tan(\alpha) = \frac{b}{a} \\
    \qquad \\
    \end{aligned}

.. image:: ./myndir/horna/sohcahtoa2.svg
    :width: 40%
    :align: center


Grunnreglan
```````````

.. math::
	\sin^2(x) + \cos^2(x) = 1


Hliðrunarreglur
```````````````

.. math::
	\begin{aligned}
	& \qquad \cos(-\theta)=\cos \theta\\
	\qquad \\
    & \qquad \sin(-\theta)=-\sin\theta\\
	\qquad \\
    & \qquad \cos(\pi-\theta)=-\cos \theta\\
	\qquad \\
    & \qquad \sin(\pi-\theta)=\sin \theta\\
	\qquad \\
    & \qquad \cos(\theta+\pi)=-\cos \theta\\
	\qquad \\
	& \qquad \sin(\theta+\pi)=-\sin \theta\\
	\qquad \\
	& \qquad \cos\left(\frac{\pi}{2}-\theta\right)=\sin\theta\\
	\qquad \\
	& \qquad \sin\left(\frac{\pi}{2}-\theta\right)=\cos\theta
	\end{aligned}


Summuformúlur
`````````````

**1.**

.. math::
	\sin( u + v ) = \sin(u)  \cos(v) + \cos(u) \sin(v)

**2.**

.. math::
	\sin( u - v ) = \sin(u) \cos(v) - \cos(u) \sin(v)

**3.**

.. math::
	\cos( u + v ) = \cos(u)  \cos(v) - \sin(u)  \sin(v)

**4.**

.. math::
	\cos( u - v ) = \cos(u)  \cos(v) + \sin(u)  \sin(v)

**5.**

.. math::
	\tan(u-v) = \frac{\tan(u) - \tan(v)}{1 + \tan(u)  \tan(v)}

**6.**

.. math::
	\tan(u+v) = \frac{\tan(u) + \tan(v)}{1 - \tan(u)  \tan(v)}


Tvöföldunarformúlur
```````````````````
**1.**

.. math::
	\sin(2u) = 2\sin(u)\cos(u)

**2.**

.. math::
	\begin{aligned}
	\cos(2x)&= \cos^2(x)-\sin^2(x) \\
	&= 2\cos^2(x)-1 \\
	&= 1-2 \sin^2(x)
	\end{aligned}

**3.**

.. math::
	\tan(2u) = \frac{2\tan(u)}{1-\tan^2(u)}


Helmingunarformúlur
```````````````````

**1.**

.. math::
	\sin^2(u) = \frac{1- \cos(2u)}{2} \qquad \text{eða} \qquad \sin\left(\frac{u}{2}\right) = \pm \sqrt{\frac{1- \cos(u)}{2} }

**2.**

.. math::
	\cos^2(u) = \frac{1+ \cos(2u)}{2} \qquad \text{eða} \qquad \cos\left(\frac{u}{2}\right) = \pm \sqrt{\frac{1+ \cos(u)}{2} }

**3.**

.. math::
	\tan^2(u) = \frac{1- \cos(2u)}{1+\cos(2u)} \qquad \text{eða} \qquad \tan\left(\frac{u}{2}\right) = \pm \sqrt{\frac{1- \cos(u)}{1+\cos(u)} }



Summu- og margfeldisformúlur
````````````````````````````

**Margfeldisritháttur í summurithátt**

 **1.**

 .. math::
	\sin(u)\sin(v) = \frac{1}{2}\left(\cos(u-v) - \cos(u+v)\right)

 **2.**

 .. math::
	\cos(u)\cos(v) = \frac{1}{2}\left(\cos(u-v) + \cos(u+v)\right)

 **3.**

 .. math::
	\sin(u)\cos(v) = \frac{1}{2}\left(\sin(u+v) + \sin(u-v)\right)

 **4.**

 .. math::
	\cos(u)\sin(v) = \frac{1}{2}\left(\sin(u+v) - \sin(u-v)\right)


**Summuritháttur í margfeldisrithátt**

 **1.**

 .. math::
	\sin(u) + \sin(v) = 2\sin\left(\frac{u+v}{2}\right)\cos\left(\frac{u-v}{2}\right)

 **2.**

 .. math::
	\sin(u) - \sin(v) = 2\cos\left(\frac{u+v}{2}\right)\sin\left(\frac{u-v}{2}\right)

 **3.**

 .. math::
	\cos(u) + \cos(v) = 2\cos\left(\frac{u+v}{2}\right)\cos\left(\frac{u-v}{2}\right)

 **4.**

 .. math::
	\cos(u) - \cos(v) = -2\sin\left(\frac{u+v}{2}\right)\sin\left(\frac{u-v}{2}\right)


Kósínusreglan
`````````````
Í :math:`\triangle ABC` gildir

.. math::
	\begin{aligned}
	a^2 &= b^2+c^2-2\cdot b \cdot c \cdot \cos(A) \\
	b^2 &= a^2+c^2-2\cdot a \cdot c \cdot \cos(B) \\
	c^2 &= b^2+a^2-2\cdot b \cdot a \cdot \cos(C) \\
	\end{aligned}



Sínusreglan
```````````
Í :math:`\triangle ABC` gildir

.. math::
	\frac{a}{\sin(A)} = \frac{b}{\sin(B)} = \frac{c}{\sin(C)}

Þar sem :math:`A`, :math:`B` og :math:`C` eru horn þríhyrningsins og :math:`a`, :math:`b` og :math:`c` eru lengdir hliðanna




Vigrar
~~~~~~

Reiknireglur
````````````

.. math::
    \begin{aligned}
    & |\bar{a}| = a = \sqrt{a_x^2 + a_y^2 + a_z^2} \\
    \qquad \\
    & \bar{a} + \bar{b} = (a_x+b_x, a_y+b_y, a_z+b_z) \\
    \qquad \\
    & c \cdot \bar{v} = (c \cdot v_x, c \cdot v_y, c \cdot v_z) \\
    \qquad \\
    & \bar{a} \cdot \bar{b} = a b \cos{\phi} \\
    \qquad \\
    & \bar{a} \times \bar{b} = (a_y b_z - a_z b_y)\hat{\imath} + (a_z b_x - a_x b_z)\hat{\jmath} + (a_x b_y - a_y b_x)\hat{k} \\
    \qquad \\
    & \bar{a} \times \bar{b} = - \bar{b} \times \bar{a}
    \end{aligned}

Markgildi
~~~~~~~~~

Reiknireglur fyrir markgildi
````````````````````````````

Gerum ráð fyrir að :math:`f` og :math:`g` séu föll og að :math:`c\in \mathbb{R} \cup\{-\infty,\infty\}`
Gerum ráð fyrir að bæði markgildin

.. math::
    \lim_{x\to c}f(x)\qquad \text{og}\qquad \lim_{x\to c}g(x)


séu skilgreind og að hvorugt þeirra sé jafnt plús eða mínus óendanlegu.
Gerum ráð fyrir að :math:`k\in\mathbb{R}` sé fasti.
Þá gildir:

.. math::

    1. & \qquad \lim_{x\to c}k=k

    2. & \qquad \lim_{x\to c} \left(kf(x) \right)=k \cdot \left(\lim_{x\to c}f(x)\right)

    3. & \qquad \lim_{x\to c} \left(f(x)+g(x)\right)=\lim_{x\to c}f(x)+\lim_{x\to c}g(x)

    4. & \qquad \lim_{x\to c} \left(f(x)-g(x)\right)=\lim_{x\to c}f(x)-\lim_{x\to c}g(x)

    5. & \qquad \lim_{x\to c} \left(f(x)\cdot g(x)\right)= \left( \lim_{x\to c}f(x) \right)\cdot \left(\lim_{x\to c}g(x) \right)

    6. & \qquad \lim_{x\to c} \left( \frac{f(x)}{g(x)} \right)=\frac{\lim_{x\to c}f(x)}{\lim_{x\to c}g(x)} \qquad \text{ef} \qquad \lim_{x\to c}g(x)\not=0

Diffrun
~~~~~~~

Reiknireglur
````````````

Gerum ráð fyrir að :math:`f,g` séu deildanleg föll á :math:`\mathbb{R}`.

Látum :math:`a\in \mathbb{R}` vera fasta.

Þá gildir:

1. :math:`(a\cdot f)'=af'`

2. :math:`(f+g)'=f'+g'`

3. :math:`(f-g)'=f'-g'`

4. :math:`(f\cdot g)'=f'g+fg'`

5. :math:`(f\circ g)'=(f'\circ g)\cdot g'`

Ef :math:`g(x)` er ekki jafnt núlli fyrir öll :math:`x\in I`, þá gildir einnig:

6. :math:`\left(\frac{1}{g}\right)'=\frac{-g'}{g^2}`

7. :math:`\left(\frac{f}{g}\right)'=\frac{f'g-fg'}{g^2}`

Ef :math:`f` er andhverfanlegt gildir einnig:

8. Ef :math:`f(x_0)=y_0` þá er :math:`(f^{-1})'\circ f=\frac{1}{f'}`

Þekktar afleiður
````````````````

1. Ef :math:`a` er fasti og :math:`f(x)=a` þá er

.. math::
    f'(x)=0

2. Ef :math:`n\in \mathbb{R}\setminus\{0\}` og :math:`f(x)=x^n` þá er

.. math::
    f'(x)=nx^{n-1}

3. Ef :math:`a\in \mathbb{R}_+` og :math:`f(x)=a^x` þá er

.. math::
    f'(x)=\ln(a)a^x

4. Ef :math:`a\in \mathbb{R}_+` og :math:`f(x)=\log_a(x)` þá er

.. math::
    f'(x)=\frac{1}{\ln(a)x}

5. Ef :math:`f(x) = \ln(x)` þá er

.. math::
    f'(x) = \frac{1}{x}

6. Ef :math:`f(x) = e^x` þá er

.. math::
    f'(x) = e^x

7. Ef :math:`f(x)=\cos(x)` þá er

.. math::
    f'(x)=-\sin(x)

8. Ef :math:`f(x)=\sin(x)` þá er

.. math::
    f'(x)=\cos(x)
