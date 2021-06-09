
Hlutafleiður
=================



*“If you need help bark like a dog." - Gendry. "That's stupid. If I need help I'll shout help." - Arya”*

\- George R.R. Martin, A Clash of Kings 


Graf falls
----------


.. index::
  graf falls

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`f:{\mathbb  R}^2\rightarrow {\mathbb  R}` vera fall. *Graf*
fallsins er skilgreint sem mengið

.. math:: \displaystyle \{(x,y,f(x,y))\mid (x,y)\in{\mathbb  R}^2\}\subseteq {\mathbb  R}^3.

Ef :math:`f:{\mathbb  R}^3\rightarrow {\mathbb  R}` er fall, þá er
*graf* fallsins skilgreint sem mengið

.. math:: \displaystyle \{(x,y,z,f(x,y,z))\mid (x,y,z)\in{\mathbb  R}^3\}\subseteq {\mathbb  R}^4.


.. image:: ./surface.png
  :width: 60%
  :align: center
..
   
*Graf fallsins* :math:`f(x,y) = \sqrt{1-x^2-y^2}`, :math:`-0.5\leq x,y\leq 0.5`.

Jafnhæðarlínur
--------------


.. index::
  jafnhæðar-;lína
  jafnhæðar-;ferill
  jafnhæðar-;flötur

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`f:{\mathbb  R}^2\rightarrow {\mathbb  R}` vera fall. Ef
:math:`c` er fasti þá er mengið

.. math:: \displaystyle \{(x,y)\mid f(x,y)=c\}\subseteq {\mathbb  R}^2

kallað :hover:`jafnhæðarlína,hæðarlína` eða :hover:`jafnhæðarferill,hæðarferill` fallsins
:math:`f` fyrir fastann :math:`c`.

Látum :math:`f:{\mathbb  R}^3\rightarrow {\mathbb  R}` vera fall. Ef
:math:`c` er fasti þá er mengið

.. math:: \displaystyle \{(x,y,z)\mid f(x,y,z)=c\}

kallað :hover:`jafnhæðarflötur,hæðarflötur` fallsins :math:`f` fyrir
fastann :math:`c`.


.. image:: contour.png
  :width: 60%
  :align: center
   
..
   
*Nokkrar jafnæðarlínur fallsins* :math:`f(x,y) = \sqrt{1-x^2-y^2}`, :math:`-0.5\leq x,y\leq 0.5`.

Fjarlægð milli punkta
---------------------

.. index::
  fjarlægð

Skilgreining 
~~~~~~~~~~~~~

*Fjarlægðin* milli tveggja punkta
:math:`\mbox{${\bf x}$}=(x_1,x_2, \ldots,x_n)` og
:math:`\mbox{${\bf y}$}=(y_1,y_2, \ldots,y_n)` í
:math:`\mbox{${\bf R}^n$}` er skilgreind sem talan

.. math:: 
   \displaystyle 
   |\mbox{${\bf x}$}-\mbox{${\bf y}$}|=\sqrt{(x_1-y_1)^2+(x_2-y_2)^2+\cdots+(x_n-y_n)^2}.

Opnar kúlur
-----------

.. index::
  opin kúla

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`P=(p_1,p_2,\ldots,p_n)` vera punkt í
:math:`\mbox{${\bf R}^n$}`. Skilgreinum *opnu kúluna* með miðju í
:math:`P` og geisla :math:`r` sem mengið

.. math:: \displaystyle B_r(P)=\{Q\in\mbox{${\bf R}^n$}\mid |Q-P|<r\}.

Í :math:`{\mathbb  R}^2` er eðlilegra að tala um *opna skífu* eða *opinn
disk* í stað opinnar kúlu og í :math:`{\mathbb  R}` þá er talað um opin
bil.

Opin mengi
----------

.. index::
  opið mengi
  lokað mengi
  fyllimengi
  
Skilgreining 
~~~~~~~~~~~~~

Látum :math:`U` vera hlutmengi í :math:`\mbox{${\bf R}^n$}`.

Sagt er að :math:`U` sé :hover:`opið mengi` ef um sérhvern punkt :math:`P` í
:math:`U` gildir að til er tala :math:`r>0` þannig að
:math:`B_r(P)\subseteq U`.

Mengið :math:`U` er sagt :hover:`lokað,lokað mengi` ef :hover:`fyllimengið,fyllimengi` er opið. (*Fyllimengi*
:math:`U` er skilgreint sem mengið
:math:`\mbox{${\bf R}^n$}\setminus U=\{Q\in \mbox{${\bf R}^n$}\mid Q\mbox{$\;\not\in\;$}U\}`.)

Jaðarpunktur
------------

.. index::
  jaðarpunktur

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`U` vera mengi í :math:`\mbox{${\bf R}^n$}`. Punktur
:math:`P` í :math:`\mbox{${\bf R}^n$}` er sagður :hover:`jaðarpunktur`
:math:`U` ef sérhver opin kúla :math:`B_r(P)` með :math:`r>0` inniheldur
bæði punkt úr :math:`U` og punkt úr
:math:`\mbox{${\bf R}^n$}\setminus U`. (Athugið að bæði er mögulegt að
jaðarpunktur :math:`U` sé í :math:`U` og að hann sé ekki í :math:`U`.)

Skilgreiningarmengi
-------------------

.. index::
  skilgreiningarmengi

Skilgreining 
~~~~~~~~~~~~~

Fyrir fall :math:`f(x_1,x_2,\ldots,x_n)` þá táknar :math:`{\cal D}(f)`
:hover:`skilgreiningarmengi` fallsins :math:`f`. Ef fallið er gefið með formúlu
og ekkert sagt um :math:`{\cal D}(f)` þá lítum við svo á að
:math:`{\cal D}(f)` sé mengi allra punkta í :math:`\mbox{${\bf R}^n$}`
þannig að formúlan gefi vel skilgreinda tölu.

.. index::
  markgildi
  stefna á
  
Markgildi
---------


Skilgreining 
~~~~~~~~~~~~~

Látum :math:`f(x_1,x_2,\ldots,x_n)` vera fall af :math:`n` breytistærðum
með skilgreiningarmengi :math:`{\cal D}(f)\subseteq \mbox{${\bf R}^n$}`.
Látum :math:`P=(p_1,p_2,\ldots,p_n)` vera punkt í
:math:`\mbox{${\bf R}^n$}` þannig að sérhver opin kúla um :math:`P`
inniheldur meira en einn punkt úr :math:`{\cal D}(f)`.

Segjum að :math:`f(x_1,x_2,\ldots,x_n)` :hover:`stefni á,stefna á` tölu :math:`L` þegar
:math:`(x_1,x_2,\ldots,x_n)` stefnir á :math:`(p_1,p_2,\ldots,p_n)` ef
eftirfarandi gildir:

Fyrir sérhverja tölu :math:`\epsilon>0` er til tala :math:`\delta>0`
þannig að ef :math:`(x_1,x_2,\ldots,x_n)\in{\cal D}(f)` og  

.. math:: \displaystyle

  0<|(x_1,x_2,\ldots,x_n)-(p_1,p_2,\ldots,p_n)|<\delta 

þá er 

.. math:: \displaystyle
  |f(x_1,x_2,\ldots,x_n)-L|<\epsilon.

Ritháttur 
~~~~~~~~~~

Ef :math:`f(x_1,x_2,\ldots,x_n)` stefnir á tölu :math:`L` þegar
:math:`(x_1,x_2,\ldots,x_n)` stefnir á :math:`(p_1,p_2,\ldots,p_n)` þá
er ritað

.. math:: \displaystyle

   \lim_{(x_1,x_2,\ldots,x_n)\rightarrow (p_1,p_2,\ldots,p_n)}
   f(x_1,x_2,\ldots,x_n)=L.

og :math:`L` kallast :hover:`markgildi,markgildi` fallsins :math:`f` í punktinum :math:`(x_1,x_2,\ldots,x_n)`.

Ef við skrifum :math:`\mathbf x = (x_1,x_2,\ldots,x_n)` og 
:math:`\mathbf p = (p_1,p_2,\ldots,p_n)` þá getum við skrifað þetta svona

.. math:: \displaystyle 

   \lim_{\mathbf x \to \mathbf p} f(\mathbf x) = L.

..
  XXX reference
   
Skilgreining (Skilgreining 2.8.1 sett fram fyrir föll af tveimur breytum.) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f(x,y)` vera fall skilgreint á mengi
:math:`{\cal D}(f)\subseteq {\mathbb  R}^2`. Látum :math:`(a,b)` vera
punkt í :math:`{\mathbb  R}^2` þannig að sérhver opin skífa um
:math:`(a,b)` inniheldur meira en einn punkt úr :math:`{\cal D}(f)`.

Segjum að :math:`f(x,y)` stefni á tölu :math:`L` þegar :math:`(x,y)`
stefnir á :math:`(a,b)` ef eftirfarandi gildir:

Fyrir sérhverja tölu :math:`\epsilon>0` er til tala :math:`\delta>0`
þannig að ef :math:`(x,y)\in{\cal D}(f)` og  

.. math:: \displaystyle

  \delta > |(x,y)-(a,b)| = \sqrt{(x-a)^2+(y-b)^2} > 0

þá er 

.. math:: \displaystyle
  |f(x,y)-L|<\epsilon.

Reglur um markgildi
-------------------

Setning 
~~~~~~~~

Látum :math:`f` og :math:`g` vera föll af tveimur breytum. Gerum ráð
fyrir að

.. math:: \displaystyle

   \lim_{(x,y)\rightarrow (a,b)}f(x,y)=L\quad\mbox{og}\quad
   \lim_{(x,y)\rightarrow (a,b)}g(x,y)=M,

og að sérhver :hover:`grennd` um :math:`(a,b)` innihaldi fleiri en einn punkt þar
sem bæði föllin :math:`f` og :math:`g` eru skilgreind. Þá gildir

**(a)** :math:`\lim_{(x,y)\rightarrow (a,b)}(f(x,y)\pm g(x,y))=L\pm M`.

**(b)** :math:`\lim_{(x,y)\rightarrow (a,b)}f(x,y) g(x,y)=LM`.

**(c)** :math:`\lim_{(x,y)\rightarrow (a,b)}\frac{f(x,y)}{g(x,y)}=
\frac{L}{M}`, svo framarlega sem :math:`M\neq 0`.

**(d)** :math:`\lim_{(x,y)\rightarrow (a,b)}F(f(x,y))=F(L)` ef :math:`F`
er fall af einni breytistærð sem er samfellt í punktinum :math:`L`.


.. index::
  samfelldni

Samfelldni
----------


Skilgreining 
~~~~~~~~~~~~~

Látum :math:`f` vera fall af :math:`n` breytistærðum skilgreint á mengi
:math:`{\cal D}(f)` í :math:`\mbox{${\bf R}^n$}`. Fallið :math:`f` er
sagt *samfellt í punkti* :math:`(p_1,p_2,\ldots,p_n)` í
:math:`{\cal D}(f)` ef

.. math:: \displaystyle

   \lim_{(x_1,x_2,\ldots,x_n)\rightarrow (p_1,p_2,\ldots,p_n)}
   f(x_1,x_2,\ldots,x_n)=f(p_1,p_2,\ldots,p_n).

Sagt er að fallið sé :hover:`samfellt` ef það er samfellt í öllum punktum
skilgreiningarmengis síns.

Hlutafleiður
------------

.. index::
  hlutafleiða

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`f(x,y)` vera fall af tveimur breytum :math:`x` og :math:`y`
sem er skilgreint á opinni skífu með miðju í punktinum :math:`(a,b)`.

Skilgreinum :hover:`hlutafleiðu,hlutafleiða` m.t.t. :math:`x` í :math:`(a,b)` með

.. math:: \displaystyle f_1(a,b)=\lim_{h\rightarrow 0}\frac{f(a+h,b)-f(a,b)}{h}

og :hover:`hlutafleiðu,hlutafleiða` m.t.t. :math:`y` í :math:`(a,b)` með

.. math:: \displaystyle f_2(a,b)=\lim_{k\rightarrow 0}\frac{f(a,b+k)-f(a,b)}{k}

ef markgildin eru til.

.. image:: xpart.png
  :width: 60%
  :align: center
  
..

*Hlutafleiða m.t.t.* \ :math:`x` *fyrir* :math:`y=1`.

.. image:: ypart.png
   :width: 60%
   :align: center


..

*Hlutafleiða m.t.t.* \ :math:`y` *fyrir* :math:`x=1`.

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`f(x,y,z)` vera fall af þremur breytum :math:`x`, :math:`y`
og :math:`z` sem er skilgreint á opinni kúlu með miðju í punktinum
:math:`(a, b,c)`.

Skilgreinum *hlutafleiðu m.t.t.* :math:`x` í :math:`(a,b,c)` með

.. math:: \displaystyle f_1(a,b,c)=\lim_{h\rightarrow 0}\frac{f(a+h,b,c)-f(a,b,c)}{h},

*hlutafleiðu m.t.t.* :math:`y` í :math:`(a,b,c)` með

.. math:: \displaystyle f_2(a,b,c)=\lim_{k\rightarrow 0}\frac{f(a,b+k,c)-f(a,b,c)}{k}

og *hlutafleiðu m.t.t.* :math:`z` í :math:`(a,b,c)` með

.. math:: \displaystyle f_3(a,b,c)=\lim_{\ell\rightarrow 0}\frac{f(a,b,c+\ell)-f(a,b,c)}{\ell}

ef markgildin eru til.



Skilgreining 
~~~~~~~~~~~~~

Látum :math:`f` vera fall af :math:`n` breytum
:math:`x_1,x_2,\ldots,x_n` sem er skilgreint á opinni kúlu um punktinn
:math:`\mathbf{a}=(a_1, a_2, \ldots, a_n).`

Hlutafleiða :math:`f` með tilliti til breytunnar :math:`x_k` í punktinum
:math:`\mathbf{a}` er skilgreind sem markgildið

.. math:: \displaystyle f_k(\mathbf{a})=\lim_{h\rightarrow 0}\frac{f(\mathbf{a}+h\mbox{${\bf e}$}_k)-f(\mathbf{a})}{h}

ef markgildið er til. (Hér stendur :math:`\mbox{${\bf e}$}_k` fyrir
vigurinn sem er með 0 í öllum hnitum nema því :math:`k`-ta þar sem er
1.)


Ritháttur
~~~~~~~~~

Ritum :math:`z=f(x,y)`.  Ýmis konar ritháttur er fyrir hlutafleiður, m.a.

.. math:: \displaystyle 

  \begin{aligned}
  f_1(x,y)&=\frac{\partial z}{\partial x}=  \frac{\partial }{\partial x}f(x,y)
  =D_1f(x,y)=f_x(x,y)=D_xf(x,y)=\partial_xf(x,y) \\  
  f_2(x,y)&=\frac{\partial z}{\partial y}=  \frac{\partial }{\partial y}f(x,y)
  =D_2f(x,y)=f_y(x,y)=D_yf(x,y)=\partial_yf(x,y). \end{aligned}

Þegar við viljum tákna gildið á hlutafleiðu :math:`f` í ákveðnum punkti
:math:`(x,y)=(a,b)` þá eru líka ýmsir möguleikar, til dæmis 

.. math:: \displaystyle 

  \begin{aligned}
  \frac{\partial z}{\partial x}\bigg|_{(a,b)}&=
  \left(\frac{\partial }{\partial x}f(x,y)\right)\bigg|_{(a,b)}
  =f_1(a,b)=D_1f(a,b) \\
  \frac{\partial z}{\partial y}\bigg|_{(a,b)}&=
  \left(\frac{\partial }{\partial y}f(x,y)\right)\bigg|_{(a,b)}
  =f_2(a,b)=D_2f(a,b). \end {aligned}


.. warning::

  Strangt til tekið merkir rithátturinn :math:`\frac{\partial}{\partial x} f(a,b)` að við stingum fyrst
  inn tölunum :math:`a` og :math:`b` og diffrum síðan með tilliti til :math:`x`. En þar sem :math:`f(a,b)` er
  óháð :math:`x` er útkoman 0.
  
  
Snertiplan
----------

Látum :math:`f(x,y)` vera fall af tveimur breytistærðum þannig að
hlutafleiðurnar :math:`f_1(a,b)` og :math:`f_2(a,b)` séu skilgreindar.

.. image:: bothpart.png
   :width: 60%
   :align: center

Í punktinum :math:`(a,b,f(a,b))` er

:math:`\mbox{${\bf T}$}_1 = \mbox{${\bf i}$}+ f_1(a,b)\mbox{${\bf k}$}\qquad`
:hover:`snertivigur` við ferilinn :math:`f(x,b) = z` og

:math:`\mbox{${\bf T}$}_2 = \mbox{${\bf j}$}+ f_2(a,b)\mbox{${\bf k}$}\qquad`
:hover:`snertivigur` við ferilinn :math:`f(a,y) = z`.

Táknum með :math:`S` planið sem hefur stikunina

.. math:: \displaystyle (a,b,f(a,b))+s\mbox{${\bf T}$}_1+t\mbox{${\bf T}$}_2, \quad -\infty < s,t < \infty.

Vigurinn

.. math:: \displaystyle \mbox{${\bf n}$}=\mbox{${\bf T}$}_2\times \mbox{${\bf T}$}_1=f_1(a,b)\mbox{${\bf i}$}+f_2(a,b)\mbox{${\bf j}$}-\mbox{${\bf k}$}

er þvervigur á :math:`S` og jafna plansins :math:`S` er

.. math:: \displaystyle z=f(a,b)+f_1(a,b)(x-a)+f_2(a,b)(y-b).

:hover:`Þverlína` á :math:`S` hefur stikun

.. math:: \displaystyle (a,b,f(a,b)) + u \mbox{${\bf n}$}, \quad -\infty < u < \infty.

Ef :math:`f(x,y)` er ’nógu nálægt’ (skilgreint nánar síðar) planinu
:math:`S` þegar :math:`(x,y)` er nálægt punktinum :math:`(a,b)` þá
kallast :math:`S` :hover:`snertiplan,snertislétta` við grafið :math:`z=f(x,y)` í punktinum
:math:`(a,b,f(a,b))`.

.. ggb:: Tvv6bpU3
  :width: 700
  :height: 600
  :img: polarggb.png
  :imgwidth: 4cm
  :zoom_drag: true 



Hlutafleiður af hærra stigi
---------------------------

.. index::
  hlutafleiða;annars stigs
  hlutafleiða;hrein
  hlutafleiða;blönduð
  
Skilgreining 
~~~~~~~~~~~~~

Ritum :math:`z=f(x,y)`. *Annars stigs hlutafleiður* :math:`f` eru
skilgreindar með formúlunum

.. math:: \displaystyle

   \frac{\partial^2 z}{\partial x^2}=
   \frac{\partial}{\partial x} \frac{\partial z}{\partial x}
   =f_{11}(x,y)=f_{xx}(x,y),

.. math:: \displaystyle

   \frac{\partial^2 z}{\partial y^2}=
   \frac{\partial}{\partial y} \frac{\partial z}{\partial y}
   =f_{22}(x,y)=f_{yy}(x,y),

.. math:: \displaystyle

   \frac{\partial^2 z}{\partial x\partial y}=
   \frac{\partial}{\partial x} \frac{\partial z}{\partial y}
   =f_{21}(x,y)=f_{yx}(x,y),

.. math:: \displaystyle

   \frac{\partial^2 z}{\partial y\partial x}=
   \frac{\partial}{\partial y} \frac{\partial z}{\partial x}
   =f_{12}(x,y)=f_{xy}(x,y).

Hlutafleiðurnar :math:`f_{11}(x,y)` og :math:`f_{22}(x,y)` kallast
hreinar hlutafleiður og :math:`f_{12}(x,y)` og :math:`f_{21}(x,y)`
kallast blandaðar hlutafleiður.


Setning 
~~~~~~~~

Látum :math:`f(x,y)` vera fall sem er skilgreint á opinni skífu
:math:`D` með miðju í :math:`P=(a,b)` . Gerum ráð fyrir að
hlutafleiðurnar :math:`f_1(x,y)`, :math:`f_2(x,y)`, :math:`f_{12}(x,y)`
og :math:`f_{21}(x,y)` séu allar skilgreindar á :math:`D` og að þær séu
allar samfelldar á :math:`D`. Þá gildir að

.. math:: \displaystyle f_{12}(a,b)=f_{21}(a,b).

Hugmynd að skilgreiningu 
~~~~~~~~~~~~~~~~~~~~~~~~~

Skilgreiningu 5.6 má útvíkka á augljósan hátt til að skilgreina 2. stigs
hlutafleiður fyrir föll af fleiri en tveimur breytum. Einnig er augljóst
hvernig má skilgreina hlutafleiður af hærri stigum en 2, til dæmis ef
:math:`w=f(x,y,z)` þá

.. math:: \displaystyle

   \frac{\partial^3 w}{\partial x\partial y^2} \quad\quad\mbox{(diffra
       fyrst tvisvar m.t.t. }y\mbox{, svo einu sinni m.t.t. } x\mbox{)}

og

.. math:: \displaystyle

   \frac{\partial^3 w}{\partial y\partial z\partial y} \quad\quad\mbox{(diffra
       fyrst m.t.t. } y\mbox{, svo m.t.t. } z
   \mbox{ og að lokum m.t.t. }y\mbox{)}.
   
..
  XXX reference

Setning (Almenn útgáfa af Setningu 2.13.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera fall :math:`n` breytistærðum sem er skilgreint á
opinni kúlu með miðju í :math:`P=(x_1, x_2,\ldots, x_n)`.

Skoðum tvær hlutafleiður :math:`f` í punktum :math:`P` þar sem er
diffrað með tilliti til sömu breytistærða og jafn oft með tilliti til
hverrar breytistærðar. Ef þessar hlutafleiður eru samfelldar í punktinum
:math:`P` og allar hlutafleiður af lægra stigi eru skilgreindar á
:math:`D` og samfelldar á :math:`D` þá eru hlutafleiðurnar sem við erum
að skoða jafnar í :math:`P`.

Dæmi:
~~~~~

Ef :math:`w = f(x,y,z)` er fall af þremur breytistærðum þá er t.d. 

.. math:: \displaystyle \frac{\partial^4 w}{\partial x^2\partial y \partial z} = \frac{\partial^4 w}{\partial x \partial y \partial x \partial z}

ef skilyrðin í setningunni eru uppfyllt.

.. index::
  keðjuregla

Keðjuregla
-----------

.. index::
  keðjuregla;í einni breytistærð

Setning (Keðjureglan í einni breytistærð.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við munum nú skoða nokkrar útgáfur af :hover:`keðjureglu,keðjuregla` fyrir föll af mörgum breytistærðum. Gerum ráð fyrir að fallið :math:`f(u)` sé diffranlegt í punktinum
:math:`u=g(x)` og að fallið :math:`g(x)` sé diffranlegt í punktinum
:math:`x`. Þá er fallið :math:`(f\circ g)(x)=f(g(x))` diffranlegt í
:math:`x` og

.. math:: \displaystyle (f\circ g)'(x)=f'(g(x))g'(x).

Setning 
~~~~~~~~

Látum :math:`f(x,y)` vera fall þar sem :math:`x=x(t)` og :math:`y=y(t)`
eru föll af breytu :math:`t`. Gerum ráð fyrir að á opinni skífu um
punktinum :math:`(x(t),y(t))` séu báðar fyrsta stigs hlutafleiður
:math:`f` skilgreindar og samfelldar. Gerum enn fremur ráð fyrir að
föllin :math:`x(t)` og :math:`y(t)` séu bæði diffranleg í punktinum
:math:`t`. Þá er fallið

.. math:: \displaystyle g(t)=f(x(t),y(t))

diffranlegt í :math:`t` og

.. math:: \displaystyle g'(t)=f_1(x(t),y(t))x'(t)+f_2(x(t),y(t))y'(t).

Ritháttur 
~~~~~~~~~~

Ritum :math:`z=f(x,y)` þar sem :math:`x=x(t)` og :math:`y=y(t)` eru föll
af breytu :math:`t`. Þá er

.. math:: \displaystyle

   \frac{dz}{dt}=\frac{\partial z}{\partial x}\frac{dx}{dt}
   +\frac{\partial z}{\partial y}\frac{dy}{dt}.

.. image:: chain1.png
   :width: 27%
   :align: center

Setning 
~~~~~~~~

Látum :math:`f(x,y)` vera fall af breytistærðum :math:`x` og :math:`y`
sem aftur eru föll af breytum :math:`s` og :math:`t`, það er að segja
:math:`x=x(s,t)` og :math:`y=y(s,t)`. Ritum svo

.. math:: \displaystyle g(s,t)=f(x(s,t),y(s,t)).

..
  XXX reference
  
Þá gildir (að gefnum sambærilegum skilyrðum og í 2.14.2) að

.. math:: \displaystyle g_1(s,t)=f_1(x(s,t),y(s,t))x_1(s,t)+f_2(x(s,t),y(s,t))y_1(s,t),

 og

.. math:: \displaystyle g_2(s,t)=f_1(x(s,t),y(s,t))x_2(s,t)+f_2(x(s,t),y(s,t))y_2(s,t).

Ritháttur 
~~~~~~~~~~

Ritum :math:`z=f(x,y)` þar sem :math:`x=x(s,t)` og :math:`y=y(s,t)` eru
föll af breytum :math:`s` og :math:`t`. Þá er

.. math:: \displaystyle

   \frac{\partial z}{\partial s}=
   \frac{\partial z}{\partial x}\frac{\partial x}{\partial s}
   +\frac{\partial z}{\partial y}\frac{\partial y}{\partial s}, \quad \text{og}\quad \frac{\partial z}{\partial t}=
   \frac{\partial z}{\partial x}\frac{\partial x}{\partial t}
   +\frac{\partial z}{\partial y}\frac{\partial y}{\partial t}.

.. figure:: chain2.png
   :width: 30%
   :align: center


Ritháttur
~~~~~~~~~

Ritum :math:`z=f(x,y)` þar sem :math:`x=x(s,t)` og :math:`y=y(s,t)` eru
föll af breytum :math:`s` og :math:`t`. Þá er

.. math:: \displaystyle

   \begin{bmatrix}\frac{\partial z}{\partial s} 
   & \frac{\partial z}{\partial t}\end{bmatrix}
   =\begin{bmatrix}\frac{\partial z}{\partial x} 
   & \frac{\partial z}{\partial y}\end{bmatrix}
   \begin{bmatrix}\frac{\partial x}{\partial s} 
   & \frac{\partial x}{\partial t}\\
   \frac{\partial y}{\partial s} 
   & \frac{\partial y}{\partial t}
   \end{bmatrix}

Setning 
~~~~~~~~

Látum :math:`u` vera fall af :math:`n` breytum
:math:`x_1, x_2, \ldots, x_n` þannig að hvert :math:`x_i` má rita sem
fall af :math:`m` breytum :math:`t_1, t_2, \ldots, t_m`. Gerum ráð fyrir
að allar hlutafleiðurnar :math:`\frac{\partial u}{\partial x_i}` og
:math:`\frac{\partial x_i}{\partial t_j}` séu til og samfelldar. Þegar
:math:`u` er skoðað sem fall af breytunum :math:`t_1, t_2, \ldots, t_m`
fæst að

.. math:: \displaystyle

   \frac{\partial u}{\partial t_j}=
   \frac{\partial u}{\partial x_1}\frac{\partial x_1}{\partial t_j}
   +\frac{\partial u}{\partial x_2}\frac{\partial x_2}{\partial t_j}
   +\cdots+
   \frac{\partial u}{\partial x_n}\frac{\partial x_n}{\partial t_j}.

.. image:: chain3.png
   :width: 50%
   :align: center
 

Dæmi 
~~~~~

Látum :math:`T` vera fall af fall af :math:`x`, :math:`y` og :math:`t`,
og :math:`x` og :math:`y` föll af :math:`t`. Finnum
:math:`\frac{ dT}{dt}`.

.. image:: chain5.png
   :width: 40%
   :align: center
 

.. math:: \displaystyle \frac{d T}{d t} = \frac{\partial T}{\partial x} \frac{d x}{d t} +\frac{\partial T}{\partial y} \frac{d y}{d t} + \frac{\partial T}{\partial t} .

Dæmi 
~~~~~

Látum :math:`T` vera fall af fall af :math:`x`, :math:`y`, :math:`s` og
:math:`t`, og :math:`x` og :math:`y` föll af :math:`s` og :math:`t`.
Finnum :math:`\frac{ \partial T}{\partial t}`.

.. image:: chain6.png
   :width: 50%
   :align: center
 

.. math:: \displaystyle \frac{\partial T}{\partial t} = \frac{\partial T}{\partial x} \frac{\partial x}{\partial t} +\frac{\partial T}{\partial y} \frac{\partial y}{\partial t} + \left(\frac{\partial T}{\partial t}\right)_{x,y,s} .

Dæmi 
~~~~~

Látum :math:`z` vera fall af fall af :math:`u`, :math:`v` og :math:`r`,
:math:`u` og :math:`v` vera föll af :math:`x`, :math:`y` og :math:`r` og
:math:`r` vera fall af :math:`x` og :math:`y`. Skrifum niður
:math:`\frac{\partial z}{\partial x}`.

.. image:: chain4.png
   :width: 40%
   :align: center
 

.. math:: \displaystyle

   \displaystyle\frac{\partial z}{\partial x} = \frac{\partial z}{\partial u} \frac{\partial u}{\partial x} +\frac{\partial z}{\partial u} \frac{\partial u}{\partial r} \frac{\partial r}{\partial x} 
   + \frac{\partial z}{\partial v} \frac{\partial v}{\partial x} + \frac{\partial z}{\partial v} \frac{\partial v}{\partial r} \frac{\partial r}{\partial x} +\frac{\partial z}{\partial r} \frac{\partial r}{\partial x}.


Diffranleiki í einni breytistærð
--------------------------------

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`f` vera fall af einni breytistærð og gerum ráð fyrir að
:math:`f` sé skilgreint á opnu bili sem inniheldur punktinn :math:`a`.
Fallið :math:`f` er sagt vera :hover:`diffranlegt,diffranlegur` í punkti :math:`a` ef
markgildið

.. math:: \displaystyle f'(a)=\lim_{h\rightarrow 0}\frac{f(a+h)-f(a)}{h}

er til.


.. index::
  diffranleiki;falls af einni breytistærð

Diffranleiki í einni breytistærð - önnur lýsing
-----------------------------------------------

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`f` vera fall af einni breytistærð og gerum ráð fyrir að
:math:`f` sé skilgreint á opnu bili sem inniheldur punktinn :math:`a`.
Fallið :math:`f` er sagt vera :hover:`diffranlegt,diffranlegur` í punkti :math:`a` ef til er
tala :math:`m` þannig að ef :math:`L(x)=f(a)+m(x-a)` þá er

.. math:: \displaystyle \lim_{h\rightarrow 0}\frac{f(a+h)-L(a+h)}{h}=0.

(Talan :math:`m` verður að vera jöfn :math:`f'(a)`.)

Fallið :math:`f` er ’nálægt’ línunni :math:`L` nálægt punktinum
:math:`a`.

Diffranleiki
------------

.. index::
  diffranleiki;falls af tveimur breytistærðum

Skilgreining 
~~~~~~~~~~~~~

Fall :math:`f(x,y)` sem er skilgreint á opinni skífu umhverfis
:math:`(a,b)` er sagt vera :hover:`diffranlegt,diffranlegur` í punktinum :math:`(a,b)` ef
báðar fyrsta stigs hlutafleiður :math:`f` eru skilgreindar í
:math:`(a,b)` og ef

.. math:: \displaystyle

   \lim_{(h,k)\rightarrow (0,0)}
   \frac{f(a+h, b+k)-S(a+h,b+k)}{\sqrt{h^2+k^2}}=0

þar sem :math:`S(x,y) = f(a,b) + f_1(a,b)(x-a)+f_2(a,b)(y-b)`.

Fallið :math:`f` er ’nálægt’ sléttunni :math:`S` nálægt punktinum
:math:`(a,b)`.

.. index::
  snertiplan

Snertiplan
----------

Ef :math:`f` er diffranlegt í :math:`(a,b)` þá kallast planið :math:`S`
:hover:`snertiplan,snertislétta` við graf fallsins.

.. image:: bothpart.png
   :width: 60%
   :align: center
 

:math:`S(x,y) = f(a,b) + f_1(a,b)(x-a)+f_2(a,b)(y-b)`.

Diffranleiki
------------

.. index::
  meðalgildissetningin

Setning (Meðalgildissetningin)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fallið :math:`f` sé samfellt á lokaða bilinu
:math:`[a,b]` og diffranlegt á opna bilinu :math:`(a,b)`. Þá er til
punktur :math:`c` á opna bilinu :math:`(a,b)` þannig að

.. math:: \displaystyle f(b)-f(a)=f'(c)(b-a).

Setning 
~~~~~~~~

Látum :math:`f(x,y)` vera fall sem er skilgreint á opinni skífu
:math:`\cal D` með miðju í :math:`(a,b)` þannig að á þessari skífu eru
báðar fyrsta stigs hlutafleiður :math:`f` skilgreindar og samfelldar.
Gerum ráð fyrir að :math:`h` og :math:`k` séu tölur þannig að
:math:`(x+h, y+k)\in{\cal D}`. Þá eru til tölur :math:`\theta_1` og
:math:`\theta_2` á milli 0 og 1 þannig að

.. math:: \displaystyle f(a+h,b+k)-f(a,b)=hf_1(a+\theta_1h,b+k)+kf_2(a,b+\theta_2k).

Setning 
~~~~~~~~

Látum :math:`f(x,y)` vera fall sem er skilgreint á opinni skífu
:math:`\cal D` með miðju í :math:`(a,b)` þannig að á þessari skífu eru
báðar fyrsta stigs hlutafleiður :math:`f` skilgreindar og samfelldar. Þá
er fallið :math:`f` diffranlegt í :math:`(a,b)`.

Setning 
~~~~~~~~

Gerum ráð fyrir að :math:`f(x,y)` sé fall sem er diffranlegt í punktinum
:math:`(a,b)`. Þá er :math:`f` samfellt í :math:`(a,b)`.

Keðjuregla
~~~~~~~~~~~

Ritum :math:`z=f(x,y)` þar sem :math:`x=x(s,t)` og :math:`y=y(s,t)`.
Gerum ráð fyrir að

(i)   :math:`x(a,b)=p` og :math:`y(a,b)=q`;

(ii)  fyrsta stigs hlutafleiður :math:`x(s,t)` og :math:`y(s,t)` eru
      skilgreindar í punktinum :math:`(a,b)`;

(iii) fallið :math:`f` er diffranlegt í punktinum :math:`(p,q)`.

Þá eru fyrsta stigs hlutafleiður :math:`z` með tilliti til breytanna
:math:`s` og :math:`t` skilgreindar í punktinum :math:`(a,b)` og um þær
gildir að

.. math:: \displaystyle

   \frac{\partial z}{\partial s}=
   \frac{\partial z}{\partial x}\frac{\partial x}{\partial s}
   +\frac{\partial z}{\partial y}\frac{\partial y}{\partial s}

og

.. math:: \displaystyle

   \frac{\partial z}{\partial t}=
   \frac{\partial z}{\partial x}\frac{\partial x}{\partial t}
   +\frac{\partial z}{\partial y}\frac{\partial y}{\partial t}.

   
Diffur
------

.. index::
  diffur

Skilgreining 
~~~~~~~~~~~~~

Ritum :math:`z=f(x_1, x_2, \ldots, x_n)`. :hover:`Diffrið,diffur` af :math:`z` er
skilgreint sem

.. math:: \displaystyle

   dz=df=\frac{\partial z}{\partial x_1}dx_1
   +\frac{\partial z}{\partial x_2}dx_2
   +\cdots+\frac{\partial z}{\partial x_n}dx_n.

Diffrið er nálgun á

.. math:: \displaystyle

   \Delta f=f(x_1+dx_1, x_2+dx_2,\ldots,
   x_n+dx_n)-f(x_1,x_2,\ldots,x_n).

Varpanir :math:`\mbox{${\bf R}^n$}\rightarrow\mbox{${\bf R}^m$}`
----------------------------------------------------------------

Táknmál 
~~~~~~~~

Látum
:math:`\mbox{${\bf f}$}:\mbox{${\bf R}^n$}\rightarrow\mbox{${\bf R}^m$}`
tákna vörpun. Ritum :math:`\mbox{${\bf f}$}=(f_1,\ldots,f_m)` þar sem
hvert :math:`f_i` er fall
:math:`\mbox{${\bf R}^n$}\rightarrow{\mathbb  R}`. Fyrir punkt í
:math:`\mbox{${\bf R}^n$}` ritum við
:math:`\mbox{${\bf x}$}=(x_1,x_2,\ldots,x_n)`. Síðan ritum við
:math:`\mbox{${\bf y}$}=\mbox{${\bf f}$}(\mbox{${\bf x}$})` þar sem
:math:`\mbox{${\bf y}$}=(y_1,y_2,\ldots,y_m)` og
:math:`\mathbf f(\mathbf x) = (f_1(x_1,\ldots,x_n),\ldots,f_m(x_1,\ldots,x_n))`.

Jacobi-fylki
------------

.. index::
  Jacobi-;fylki

Skilgreining 
~~~~~~~~~~~~~

..
  XXX reference

Notum táknmálið úr 2.22.1. Ef allar hlutafleiðurnar :math:`\partial
y_i/\partial x_j` eru skilgreindar í punktinum :math:`\mbox{${\bf x}$}`
þá skilgreinum við *Jacobi-fylki* :math:`f` í punktinum
:math:`\mbox{${\bf x}$}` sem :math:`m\times n` fylkið

.. math:: \displaystyle

   D\mbox{${\bf f}$}(\mbox{${\bf x}$})=\begin{bmatrix}
   \frac{\partial y_1}{\partial x_1}&\frac{\partial y_1}{\partial x_2}&
   \cdots&\frac{\partial y_1}{\partial x_n}\\
   \frac{\partial y_2}{\partial x_1}&\frac{\partial y_2}{\partial x_2}&
   \cdots&\frac{\partial y_2}{\partial x_n}\\
   \vdots&\vdots&\ddots&\vdots\\
   \frac{\partial y_m}{\partial x_1}&\frac{\partial y_m}{\partial x_2}&
   \cdots&\frac{\partial y_m}{\partial x_n}
   \end{bmatrix}

.. index::
  diffranleiki;varpana
   
Diffranleiki varpana :math:`\mbox{${\bf R}^n$}\rightarrow\mbox{${\bf R}^m$}`
----------------------------------------------------------------------------

Skilgreining 
~~~~~~~~~~~~~

..
  XXX reference

Notum táknmálið úr 2.22.1 og 2.23.1. Látum
:math:`\mbox{${\bf a}$}=(a_1, a_2, \ldots, a_n)` vera fastan punkt í
:math:`\mbox{${\bf R}^n$}` og ritum
:math:`\mbox{${\bf h}$}=(h_1,h_2,\ldots,h_n)`. Vörpunin
:math:`\mbox{${\bf f}$}` er sögð diffranleg í punktinum
:math:`\mbox{${\bf a}$}` ef

.. math:: \displaystyle

   \lim_{\mbox{${\bf h}$}\rightarrow
     \mbox{${\bf 0}$}}\frac{|\mbox{${\bf f}$}(\mbox{${\bf a}$}+\mbox{${\bf h}$})-\mbox{${\bf f}$}(\mbox{${\bf a}$})-D\mbox{${\bf f}$}(\mbox{${\bf a}$})\mbox{${\bf h}$}|}{|\mbox{${\bf h}$}|}=0.

Vörpunin :math:`f` er ’nálægt’ línulegu vörpuninni
:math:`D\mbox{${\bf f}$}` nálægt punktinum :math:`\mbox{${\bf a}$}`.

Línulega vörpunin :math:`D\mbox{${\bf f}$}` kallast afleiða
:math:`\mbox{${\bf f}$}`.

`Keðjuregla`
-------------

Setning 
~~~~~~~~

Látum
:math:`\mbox{${\bf f}$}:\mbox{${\bf R}^n$}\rightarrow \mbox{${\bf R}^m$}`
og
:math:`\mbox{${\bf g}$}:\mbox{${\bf R}^m$}\rightarrow \mbox{${\bf R}^k$}`
vera varpanir. Gerum ráð fyrir að vörpunin :math:`\mbox{${\bf f}$}` sé
diffranleg í punkti :math:`\mbox{${\bf x}$}` og vörpunin
:math:`\mbox{${\bf g}$}` sé diffranleg í punktinum
:math:`\mbox{${\bf y}$}=\mbox{${\bf f}$}(\mbox{${\bf x}$})`. Þá er
samskeytta vörpunin
:math:`\mbox{${\bf g}$}\circ\mbox{${\bf f}$}:\mbox{${\bf R}^n$}\rightarrow\mbox{${\bf R}^k$}`
diffranleg í :math:`\mbox{${\bf x}$}` og

.. math:: \displaystyle D(\mbox{${\bf g}$}\circ\mbox{${\bf f}$})(\mbox{${\bf x}$})=D\mbox{${\bf g}$}(\mbox{${\bf f}$}(\mbox{${\bf x}$}))D\mbox{${\bf f}$}(\mbox{${\bf x}$}).

.. index::
  stigull

Stigull
-------

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`f(x,y)` vera fall og :math:`(x,y)` punkt þar sem báðar
fyrsta stigs hlutafleiður :math:`f` eru skilgreindar. Skilgreinum
:hover:`stigul,stigull` :math:`f` í punktinum :math:`(x,y)` sem vigurinn

.. math:: \displaystyle \nabla f(x,y)=f_1(x,y)\mbox{${\bf i}$}+f_2(x,y)\mbox{${\bf j}$}.

:hover:`Stigull` :math:`f` er stundum táknaður með **grad**\ :math:`\,f`.

Ritháttur 
~~~~~~~~~~

Oft hentugt að rita

.. math:: \displaystyle \nabla=\mbox{${\bf i}$}\frac{\partial}{\partial x}+ \mbox{${\bf j}$}\frac{\partial}{\partial y}.

Þá er litið svo á að :math:`\nabla` sé :hover:`diffurvirki`,
þ.e.a.s. \ :math:`\nabla` gefur fyrirmæli um hvað á að gera við
:math:`f` til að fá :math:`\nabla f(x,y)`.

Dæmi
----

.. image:: gradfurf.png
   :width: 60%
   :align: center


..

*Graf* :math:`z=1-x^2-y^2`

.. image:: gradient.png
   :width: 60%
   :align: center

..

*Jafnhæðarlínur* :math:`z=1-x^2-y^2`. *Stigull og snertilína við jafnhæðarlínuna* :math:`z=0.5` *í* :math:`(x,y) = (0.5,0.5)`.

Setning 
~~~~~~~~

Gerum ráð fyrir að fallið :math:`f(x,y)` sé diffranlegt í punktinum
:math:`(a,b)` og að :math:`\nabla f(a,b) \neq \mathbf{0}`. Þá er
vigurinn :math:`\nabla f(a,b)` hornréttur á þá jafnhæðarlínu :math:`f`
sem liggur í gegnum punktinn :math:`(a,b)`.

.. index::
  snertilína;við jafnhæðarferil

Snertilína við jafnhæðarferil
-----------------------------

Setning 
~~~~~~~~

Gerum ráð fyrir að fallið :math:`f(x,y)` sé diffranlegt í punktinum
:math:`(a,b)` og að :math:`\nabla f(a,b) \neq \mathbf{0}`. Jafna
:hover:`snertilínu,snertilína` við :hover:`jafnhæðarferil,hæðarferill` :math:`f` í punktinum :math:`(a,b)` er
gefin með formúlunni

.. math:: \displaystyle \nabla f(a,b)\cdot (x,y)=\nabla f(a,b)\cdot (a,b),

eða

.. math:: \displaystyle f_1(a,b)(x-a)+f_2(a,b)(y-b)=0.


.. index::
  stefnuafleiða

Stefnuafleiða
-------------


Skilgreining 
~~~~~~~~~~~~~

Látum :math:`\mbox{${\bf u}$}=u\mbox{${\bf i}$}+v\mbox{${\bf j}$}` vera
einingarvigur. :hover:`Stefnuafleiða` :math:`f` í punktinum :math:`(a,b)` í
stefnu :math:`\mbox{${\bf u}$}` er skilgreind sem

.. math:: \displaystyle D_{\mbox{${\bf u}$}}f(a,b)=\lim_{h\rightarrow 0^+}\frac{f(a+hu, b+hv)-f(a,b)}{h}

ef markgildið er skilgreint.


.. warning::

  Í skilgreiningunni á stefnuafleiðu er tekið einhliða markgildi. Berið það saman við skilgreiningu á hlutafleiðu þar sem markgildið er tvíhliða.


Setning
~~~~~~~~

Gerum ráð fyrir að fallið :math:`f` sé diffranlegt í :math:`(a,b)` og
:math:`\mbox{${\bf u}$}=u\mbox{${\bf i}$}+v\mbox{${\bf j}$}` sé
einingarvigur. Þá er stefnuafleiðan í punktinum :math:`(a,b)` í stefnu
:math:`\mbox{${\bf u}$}` skilgreind og gefin með formúlunni

.. math:: \displaystyle D_{\mbox{${\bf u}$}}f(a,b)=\mbox{${\bf u}$}\cdot \nabla f(a,b).

Setning 
~~~~~~~~

Látum :math:`f` vera gefið fall og gerum ráð fyrir að :math:`f` sé
diffranlegt í punktinum :math:`(a,b)`.

(a) Hæsta gildið á stefnuafleiðunni :math:`D_{\mbox{${\bf u}$}}f(a,b)`
fæst þegar :math:`\mbox{${\bf u}$}` er einingarvigur í stefnu
:math:`\nabla f(a,b)`, þ.e.a.s.
:math:`\mbox{${\bf u}$}=\frac{\nabla f(a,b)}{|\nabla f(a,b)|}`.

(b) Lægsta gildið á stefnuafleiðunni :math:`D_{\mbox{${\bf u}$}}f(a,b)`
fæst þegar :math:`\mbox{${\bf u}$}` er einingarvigur í stefnu
:math:`-\nabla f(a,b)`, þ.e.a.s.
:math:`\mbox{${\bf u}$}=-\frac{\nabla f(a,b)}{|\nabla f(a,b)|}`.

(c) Ef :math:`\cal C` er sú hæðarlína :math:`f` sem liggur í gegnum
:math:`(a,b)` og :math:`\mbox{${\bf u}$}` er einingarsnertivigur við
:math:`\cal C` í punktinum :math:`(a,b)` þá er
:math:`D_{\mbox{${\bf u}$}}f(a,b)=0`.

.. image:: contours.png
   :width: 50%
   :align: center
 

Setning 
~~~~~~~~

Látum :math:`f` vera gefið fall og gerum ráð fyrir að :math:`f` sé
diffranlegt í punktinum :math:`(a,b)`.

(a) Í punktinum :math:`(a,b)` þá vex :math:`f` hraðast ef haldið er í
stefnu :math:`\nabla f(a,b)`.

(b) Í punktinum :math:`(a,b)` þá minnkar :math:`f` hraðast ef haldið er
í stefnu :math:`-\nabla f(a,b)`.

(c) Ef :math:`\cal C` er sú hæðarlína :math:`f` sem liggur í gegnum
:math:`(a,b)` og :math:`\mbox{${\bf u}$}` er einingarsnertivigur við
:math:`\cal C` í punktinum :math:`(a,b)` þá er er vaxtarhraði :math:`f`
í stefnu :math:`\mbox{${\bf u}$}` jafn 0.

Stigull (aftur)
---------------

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`f` vera fall af þremur breytistærðum, þannig að allar þrjár
fyrsta stigs hlutafleiður :math:`f` í punktinum :math:`(x,y,z)` séu
skilgreindar. :hover:`Stigull` :math:`f` í punktinum :math:`(x,y,z)` er
skilgreindur sem vigurinn

.. math:: \displaystyle \nabla f(x,y,z)=f_1(x,y,z)\mbox{${\bf i}$}+f_2(x,y,z)\mbox{${\bf j}$}+f_3(x,y,z)\mbox{${\bf k}$}.

.. index::
  snertiplan;við jafnhæðarflöt
  
Snertiplan við jafnhæðarflöt
----------------------------

Setning 
~~~~~~~~

Látum :math:`f` vera fall af þremur breytistærðum þannig að fallið
:math:`f` er diffranlegt í punktinum :math:`(a,b,c)`. Látum
:math:`\cal F` tákna þann :hover:`jafnhæðarflöt,hæðarflötur` :math:`f` sem liggur um
:math:`(a,b,c)`. Stigullinn :math:`\nabla f(a,b,c)` er hornréttur á
flötinn :math:`\cal F` í punktinum :math:`(a,b,c)` og :hover:`snertiplan,snertislétta` (ef
:math:`\nabla f(a,b,c)\neq\mbox{${\bf 0}$}`) við jafnhæðarflötinn í
punktinum :math:`(a,b,c)` er gefið með jöfnunni

.. math:: \displaystyle \nabla f(a,b,c)\cdot(x,y,z)=\nabla f(a,b,c)\cdot(a,b,c)

eða með umritun

.. math:: \displaystyle f_1(a,b,c)(x-a)+f_2(a,b,c)(y-b)+f_3(a,b,c)(z-c)=0.

Fólgin föll og Taylor-nálganir
------------------------------

.. index::
  fólgið fall
  fall; fólgið fall
  
Upprifjun 
~~~~~~~~~~

Skoðum feril sem gefinn er með jöfnu :math:`F(x,y)=0` og gerum ráð fyrir
að báðar fyrsta stigs hlutafleiður :math:`F` séu samfelldar. Látum
:math:`(x_0,y_0)` vera punkt á ferlinum. Ef :math:`F_2(x_0,y_0)\neq 0`
þá má skoða :math:`y` sem fall af :math:`x` í grennd við punktinn
:math:`(x_0,y_0)` og fallið :math:`y=y(x)` er diffranlegt í punktinum
:math:`x_0` og afleiðan er gefin með formúlunni

.. math:: \displaystyle y'(x_0)=-\frac{F_1(x_0,y_0)}{F_2(x_0,y_0)}.

Sagt að jafnan :math:`F(x,y)=0` skilgreini :math:`y` sem :hover:`fólgið fall`
af :math:`x` í grennd við :math:`(x_0,y_0)`.

Setning 
~~~~~~~~

Látum :math:`F` vera fall af :math:`n`-breytum :math:`x_1, \ldots,
x_n` og gerum ráð fyrir að allar fyrsta stigs hlutafleiður :math:`F` séu
samfelldar. Látum :math:`(a_1,\ldots,a_n)` vera punkt þannig að
:math:`F(a_1,\ldots,a_n)=0`. Ef :math:`F_n(a_1,\ldots,a_n)\neq 0` þá er
til samfellt diffranlegt fall :math:`\varphi(x_1, \ldots, x_{n-1})`
skilgreint á opinni kúlu :math:`B` utan um :math:`(a_1,\ldots,a_{n-1})`
þannig að

.. math:: \displaystyle \varphi(a_1,\ldots,a_{n-1})=a_n

og

.. math:: \displaystyle F(x_1,\ldots, x_{n-1}, \varphi(x_1, \ldots, x_{n-1}))=0

fyrir alla punkta :math:`(x_1, \ldots, x_{n-1})` í :math:`B`.

Ennfremur gildir að

.. math:: \displaystyle

   \varphi_i(a_1,\ldots,a_{n-1})
   =-\frac{F_i(a_1,\ldots,a_n)}{F_n(a_1,\ldots,a_n)}.


.. index::
  Jacobi-;ákveða
   
Skilgreining 
~~~~~~~~~~~~~

:hover:`Jacobi-ákveða` tveggja falla :math:`u=u(x,y)` og :math:`v=v(x,y)` með
tilliti til breytanna :math:`x` og :math:`y` er skilgreind sem

.. math:: \displaystyle

   \frac{\partial(u,v)}{\partial(x,y)}=
   \begin{vmatrix} 
   \frac{\partial u}{\partial x}&\frac{\partial u}{\partial y}\\
   \frac{\partial v}{\partial x}&\frac{\partial v}{\partial y}
   \end{vmatrix}.

Ef :math:`F` og :math:`G` eru föll af breytum :math:`x,y,z,\ldots` þá
skilgreinum við, til dæmis,

.. math:: \displaystyle

   \frac{\partial(F,G)}{\partial(x,y)}=
   \begin{vmatrix} 
   \frac{\partial F}{\partial x}&\frac{\partial F}{\partial y}\\
   \frac{\partial G}{\partial x}&\frac{\partial G}{\partial y}
   \end{vmatrix}\quad \mbox{og}\quad
   \frac{\partial(F,G)}{\partial(y,z)}=
   \begin{vmatrix} 
   \frac{\partial F}{\partial y}&\frac{\partial F}{\partial z}\\
   \frac{\partial G}{\partial y}&\frac{\partial G}{\partial z}
   \end{vmatrix}.

Ef við höfum föll :math:`F, G, H` af breytum :math:`x,y,z,w,\ldots` þá
skilgreinum við, til dæmis,

.. math:: \displaystyle

   \frac{\partial(F,G,H)}{\partial(w,z,y)}=
   \begin{vmatrix} 
   \frac{\partial F}{\partial w}&\frac{\partial F}{\partial z}
   &\frac{\partial F}{\partial y}\\
   \frac{\partial G}{\partial w}&\frac{\partial G}{\partial z}
   &\frac{\partial G}{\partial y}\\
   \frac{\partial H}{\partial w}&\frac{\partial H}{\partial z}
   &\frac{\partial H}{\partial y}
   \end{vmatrix}.

.. index::
  Cramer
   
Setning (Upprifjun á reglu Cramers.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`A` vera andhverfanlegt :math:`n\times n` fylki og
:math:`\mbox{${\bf b}$}` vigur í :math:`\mbox{${\bf R}^n$}`. Gerum ráð
fyrir að :math:`\mbox{${\bf x}$}=(x_1, x_2, \ldots, x_n)` sé lausn á
:math:`A\mbox{${\bf x}$}=\mbox{${\bf b}$}`. Skilgreinum :math:`B_i` sem
:math:`n\times n` fylkið sem fæst með því að setja vigurinn
:math:`\mbox{${\bf b}$}` í staðinn fyrir dálk :math:`i` í :math:`A`. Þá
er

.. math:: \displaystyle x_i=\frac{\det B_i}{\det A}.

.. index::
  setning;um fólgin föll
  fólgið fall; setning

Setning (:hover:`Setningin um fólgin föll,setning um fólgin föll`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skoðum jöfnuhneppi

.. math:: \displaystyle

   \begin{aligned}
   F_{(1)}(x_1,\ldots,x_m, y_1, \ldots, y_n)&=0\\
   F_{(2)}(x_1,\ldots,x_m, y_1, \ldots, y_n)&=0\\
   \vdots\\
   F_{(n)}(x_1,\ldots,x_m, y_1, \ldots, y_n)&=0.\end{aligned}

Látum :math:`P_0=(a_1,\ldots, a_m, b_1,\ldots, b_n)` vera punkt sem
uppfyllir jöfnurnar. Gerum ráð fyrir að allar fyrsta stigs hlutafleiður
fallanna :math:`F_{(1)},\ldots, F_{(n)}` séu samfelldar á opinni kúlu
umhverfis :math:`P_0` og að

.. math:: \displaystyle

   \frac{\partial(F_{(1)}, \ldots, F_{(n)})}
   {\partial( y_1, \ldots, y_n)}\,\bigg|_{P_0}\neq 0.

| :math:`\text{Þá eru til föll} \qquad \varphi_1(x_1,\ldots,x_m),\ldots,\varphi_n(x_1,\ldots,x_m)`
| á opinni kúlu :math:`B` umhverfis :math:`(a_1,\ldots,a_m)` þannig að

.. math:: \displaystyle \varphi_1(a_1,\ldots,a_m)=b_1,\ldots,\varphi_n(a_1,\ldots,a_m)=b_n \qquad \text{og}

.. math:: \displaystyle

   \begin{aligned}
   F_{(1)}(x_1,\ldots,x_m, \varphi_1(x_1,\ldots,x_m),\ldots,
   \varphi_n(x_1,\ldots,x_m))&=0\\
   F_{(2)}(x_1,\ldots,x_m, \varphi_1(x_1,\ldots,x_m),\ldots,
   \varphi_n(x_1,\ldots,x_m))&=0\\
   \vdots\\
   F_{(n)}(x_1,\ldots,x_m, \varphi_1(x_1,\ldots,x_m),\ldots,
   \varphi_n(x_1,\ldots,x_m))&=0\end{aligned}

fyrir alla punkta :math:`(x_1,\ldots,x_m)` í :math:`B`. Enn fremur fæst
að

.. math:: \displaystyle
   
   \frac{\partial \varphi_i}{\partial x_j}
   =\frac{\partial y_i}{\partial x_j}
   =-\frac{\frac{\partial(F_{(1)}, \ldots, F_{(n)})}
   {\partial( y_1, \ldots,x_j,\ldots y_n)}}
   {\frac{\partial(F_{(1)}, \ldots, F_{(n)})}{\partial( y_1, \ldots, y_n)}}.

.. index::
  setning;um staðbundna andhverfu
   
Setning (Setningin um staðbundna andhverfu)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Látum

.. math:: \displaystyle

   \mbox{${\bf f}$}(x_1,\ldots,
   x_n)=(f_1(x_1,\ldots,x_n),\ldots,f_n(x_1,\ldots,x_n))

vera vörpun af :math:`n` breytistærðum sem tekur gildi í
:math:`\mbox{${\bf R}^n$}` og er skilgreind á opnu mengi í
:math:`\mbox{${\bf R}^n$}`. Gerum ráð fyrir að allar fyrsta stigs
hlutafleiður fallanna :math:`f_1, \ldots, f_n` séu samfelld föll. Ef
Jacobi-fylkið :math:`D\mbox{${\bf f}$}(\mbox{${\bf x}$}_0)` er
andhverfanlegt í punkti :math:`\mbox{${\bf x}$}_0` á skilgreiningarsvæði
:math:`\mbox{${\bf f}$}` þá er til opin kúla
:math:`B_{\mbox{${\bf x}$}}` utan um :math:`\mbox{${\bf x}$}_0` og opin
kúla :math:`B_{\mbox{${\bf y}$}}` utan um
:math:`\mbox{${\bf y}$}_0=f(\mbox{${\bf x}$}_0)` og vörpun
| :math:`\mbox{${\bf g}$}:B_{\mbox{${\bf y}$}}\rightarrow B_{\mbox{${\bf x}$}}`
þannig að
:math:`\mbox{${\bf g}$}(\mbox{${\bf f}$}(\mbox{${\bf x}$}))=\mbox{${\bf x}$}`
fyrir alla punkta :math:`\mbox{${\bf x}$}\in B_{\mbox{${\bf x}$}}` og
:math:`\mbox{${\bf f}$}(\mbox{${\bf g}$}(\mbox{${\bf y}$}))=\mbox{${\bf y}$}`
fyrir alla punkta :math:`\mbox{${\bf y}$}\in B_{\mbox{${\bf y}$}}`.

.. index::
  Taylor-;regla í einni breytistærð

Upprifjun (Taylor-regla í einni breytistærð.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera :math:`n+1`-diffranlegt fall af einni breytistærð.
Margliðan

.. math:: \displaystyle

   P_{(n)}(x)=f(a)+f'(a)(x-a)+\frac{f''(a)}{2!}(x-a)^2
   +\cdots+\frac{f^{(n)}(a)}{n!}(x-a)^n

kallast :math:`n`\ *-ta stigs Taylor-margliða* :math:`f` *með miðju í*
:math:`a`. Til er punktur :math:`s` á milli :math:`a` og :math:`x`
þannig að

.. math:: \displaystyle E_{(n)}(x)=f(x)-P_{(n)}(x)=\frac{f^{(n+1)}(s)}{(n+1)!}(x-a)^{n+1}.

Fáum svo að

.. math:: \displaystyle

   \begin{aligned}
   &f(x)=P_{(n)}(x)+E_{(n)}(x) \\
   &=f(a)+f'(a)(x-a)+\cdots+\frac{f^{(n)}(a)}{n!}(x-a)^n
   +\frac{f^{(n+1)}(s)}{(n+1)!}(x-a)^{n+1}, \end{aligned}

sem er kallað :math:`n`\ *-ta stigs Taylor-formúla.*

.. index::
  Taylor-;margliða

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`f(x,y)` vera fall þannig að fyrsta stigs hlutafleiður
:math:`f` eru skilgreindar og samfelldar. Margliðan

.. math:: \displaystyle P_{(1)}(x,y)=f(a,b)+f_1(a,b)(x-a)+f_2(a,b)(y-b)

kallast *fyrsta stigs Taylor-margliða* :math:`f` *með miðju í*
:math:`(a,b)`.

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`f(x,y)` vera fall þannig að fyrsta og annars stigs
hlutafleiður :math:`f` eru skilgreindar og samfelldar. Margliðan

.. math:: \displaystyle

   \begin{aligned}
   P_{(2)}&(x,y)=f(a,b)+f_1(a,b)(x-a)+f_2(a,b)(y-b)\\
   &+\frac{1}{2}\big(f_{11}(a,b)(x-a)^2+
   2f_{12}(a,b)(x-a)(y-b)+f_{22}(a,b)(y-b)^2\big)\end{aligned}

kallast *annars stigs Taylor-margliða* :math:`f` *með miðju í*
:math:`(a,b)`.

Skilgreining og athugasemd 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skilgreinum tvo :hover:`diffurvirkja,diffurvirki` :math:`D_1` og :math:`D_2` þannig að

.. math:: \displaystyle

   D_1f(a,b)=f_1(a,b)\qquad\mbox{og}\qquad
   D_2f(a,b)=f_2(a,b).

Athugið að ef hlutafleiður :math:`f` af nógu háum stigum eru allar
skilgreindar og samfelldar þá er :math:`D_1D_2=D_2D_1`, þ.e.a.s. ekki
skiptir máli í hvaða röð er diffrað, bara hve oft er diffrað með tilliti
til hvorrar breytu.

.. index::
  tvíliðuregla

Upprifjun (:hover:`Tvíliðuregla,tvíliðusetning`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skilgreinum

.. math:: \displaystyle {n\choose j}=\frac{n!}{j!(n-j)!}.

Talan :math:`{n\choose j}` (lesið :math:`n` yfir :math:`j`) er
:math:`j+1` talan í :math:`n+1` línu Pascals-þríhyrningsins. Höfum að

.. math:: \displaystyle (x+y)^n=\sum_{j=0}^n \textstyle{n\choose j}x^jy^{n-j}.

Regla 
~~~~~~

Ef :math:`f(x,y)` er fall þannig að allar hlutafleiður af :math:`n`-ta
og lægri stigum eru samfelldar þá gildir að

.. math:: \displaystyle

   (hD_1+kD_2)^nf(a,b)=\sum_{j=0}^n \textstyle{n\choose j}
   h^jk^{n-j}D_1^jD_2^{n-j}f(a,b).

Skilgreining 
~~~~~~~~~~~~~

Fyrir fall :math:`f(x,y)` þannig að allar hlutafleiður af :math:`n`-ta
og lægri stigum eru samfelldar þá er :math:`n`\ *-ta stigs
Taylor-margliða* :math:`f` *með miðju í punktinum* :math:`(a,b)`
skilgreind sem margliðan

.. math:: \displaystyle

   \begin{aligned}
   P_{(n)}(x,y)&= \sum_{m=0}^n \frac{1}{m!}((x-a)D_1+(y-b)D_2)^m f(a,b)\\
   &=\sum_{m=0}^n\sum_{j=0}^m \frac{1}{m!}\textstyle{m\choose j}
   D_1^jD_2^{m-j}f(a,b)(x-a)^j(y-b)^{m-j}\\
   &=\sum_{m=0}^n\sum_{j=0}^m \frac{1}{j!(m-j)!}
   D_1^jD_2^{m-j}f(a,b)(x-a)^j(y-b)^{m-j}.\end{aligned}

Setning 
~~~~~~~~

Fyrir fall :math:`f(x,y)` þannig að allar hlutafleiður af :math:`n+1`-ta
og lægri stigum eru samfelldar þá gildir um skekkjuna í :math:`n`-ta
stigs Taylor-nálgun að til er tala :math:`\theta` á milli 0 og 1 þannig
að ef :math:`h=x-a` og :math:`k=y-b` þá er

.. math:: \displaystyle

   f(x,y)-P_{(n)}(x,y)=\frac{1}{(n+1)!}(hD_1+kD_2)^{n+1}
   f(a+\theta h, b+\theta k).


