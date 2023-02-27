Þýð föll og fágaðar varpanir
============================

*Bow ties are cool!*

\- The Doctor, Doctor Who

Þýð föll
--------

Skilgreining (Sjá §5.1) Nabla-virkinn í tveimur víddum er diffurvirki sem er skilgreindur sem vigur

.. math::

 \nabla=\Big(\frac{\partial}{\partial x},  \frac{\partial}{\partial y}\Big).

Ef :math:`\varphi(x,y)` er diffranlegt fall þá er stigull :math:`f` skilgreindur sem

.. math::

 \nabla f=\Big(\frac{\partial \varphi}{\partial x},  \frac{\partial \varphi}{\partial y}\Big),

og ef :math:`{\mathbf F}=(F_1, F_2)` er vigursvið þá er sundurleitni :math:`{\mathbf F}` skilgreind sem

.. math::

   \nabla\cdot{\mathbf F}=\frac{\partial F_1}{\partial x}+
   \frac{\partial F_2}{\partial y}.

   
Skilgreining (Sjá §5.1)
~~~~~~~~~~~~~~~~~~~~~~~

Laplace-virkinn í tveimur víddum er diffurvirki sem er skilgreindur með formúlunni

.. math::

 \Delta=\nabla^2 = \frac{\partial^2 }{\partial x^2}+\frac{\partial^2}{\partial y^2}

þannig að ef :math:`\varphi(x,y)` er diffranlegt fall þá er

.. math::

   \Delta\varphi=\frac{\partial^2 \varphi}{\partial x^2}
   +\frac{\partial^2\varphi}{\partial y^2}.

Laplace-jafnan er hlutafleiðujafnan :math:`\Delta\varphi=0` eða

.. math::

   \frac{\partial^2 \varphi}{\partial x^2}
   +\frac{\partial^2\varphi}{\partial y^2}=0.

Skilgreining
~~~~~~~~~~~~

Látum :math:`X` vera opið hlutmengi í :math:`{\mathbb{C}}`. Ritum :math:`z=x+iy`. Fall :math:`u:X\to {\mathbb{R}}` sem er þannig að allar 2. stigs hlutafleiður eru skilgreindar og samfelldar á öllu :math:`X` er sagt vera þýtt ef í öllum punktum :math:`z\in  X` er

.. math::

   \frac{\partial^2 u}{\partial x^2}(z)
   +\frac{\partial^2 u}{\partial y^2}(z)=0.

(Oft er hentugt að samsama :math:`{\mathbb{C}}` og :math:`{\mathbb{R}}^2` og hugsa um :math:`u` sem fall af tveimur raunbreytum.)

   
Setning (Sjá Setning 5.1.2) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`f` er fágað fall á opnu mengi :math:`X` í :math:`{\mathbb{C}}`, þá eru :math:`u=\operatorname{Re\, } f` og :math:`v=\operatorname{Im\, } f` þýð föll og stiglar þeirra eru hornréttir í sérhverjum punkti í :math:`X`. Ef :math:`X` er svæði og annað hvort :math:`u` eða :math:`v` er fastafall, þá er hitt fallið það líka. 
   

Skilgreining 
~~~~~~~~~~~

Svæði :math:`X` í :math:`{\mathbb{C}}` er sagt vera einfaldlega samanhangandi ef ekki er til einfaldur lokaður vegur í :math:`X` þannig að punktur úr :math:`{\mathbb{C}}\setminus X` er innan ferilsins. (Á mannamáli þá er mengi einfaldlega samanhangandi ef það hefur engin ,,göt‘‘.)


Setning (Sjá Setning 5.1.5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`X` vera einfaldlega samanhangandi svæði í :math:`{\mathbb{C}}` og :math:`u:{\mathbb{C}}\to {\mathbb{R}}` þýtt fall á :math:`X`. Þá er til fágað fall :math:`f` skilgreint á :math:`X` þannig að :math:`u=\operatorname{Re\, } f`. Fallið :math:`f` hefur formúlu

.. math::

 f(z)=u(a)+ic+2\int_{\gamma_z}\frac{\partial u}{\partial \zeta}(\zeta)\,d\zeta,

þar sem :math:`a\in X` er einhver fastur punktur, :math:`c` er rauntölufasti og :math:`\gamma_z` er einhver vegur í :math:`X` með upphafspunkt :math:`a` og lokapunkt :math:`\zeta`.

Ef :math:`X` er svæði í :math:`{\mathbb{C}}` sem er ekki einfaldlega samanhangandi þá er alltaf til þýtt fall :math:`u` skilgreint á :math:`X` þannig að ekki er til neitt fágað fall :math:`f` á :math:`X` með :math:`u=\operatorname{Re\, } f`. 
   

Fylgisetning 
~~~~~~~~~~~~

Látum :math:`x` vera opið mengi og :math:`u` þýtt fall á :math:`x`. Látum :math:`\alpha\in X`. Ef :math:`r>0` er tala þannig að :math:`S(\alpha, r)\subseteq X` þá er til fágað fall :math:`f`, skilgreint á :math:`S(\alpha, r)` þannig að fyrir öll :math:`z\in S(\alpha,r)` er :math:`u(z)=\operatorname{Re\, } f(z)`.

   

Meðalgildissetningin fyrir þýð föll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`u` vera þýtt fall skilgreint á opnu mengi :math:`X` og :math:`\alpha= x_0+iy_0\in X`. Látum :math:`\varrho>0` vera tölu þannig að :math:`{S}(\alpha, \varrho)\subseteq X`. Fyrir :math:`0<r<\varrho` er 

.. math::

 u(\alpha)=\frac{1}{2\pi}\int_0^{2\pi}u(\alpha+re^{it})\,dt.

Ef við samsömum tvinntalnaplanið við :math:`{\mathbb{R}}^2` þá verður formúlan
svona

.. math::

 u(x_0,y_0)=\frac{1}{2\pi}\int_0^{2\pi}u(x_0+r\cos t, y_0+r\sin t)\,dt.

   

Hágildislögmálið fyrir þýð föll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`u` vera þýtt fall skilgreint á svæði :math:`X`. Fallið :math:`u` tekur engin staðbundin útgildi á :math:`X`, nema þegar :math:`u` er fastafall. 

Hagnýtingar í straumfræði
-------------------------

Skilgreining (Sjá Stærðfræðigreiningu II) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`X` vera opið mengi í planinu :math:`{\mathbb{R}}^2`. Vigursvið :math:`{\mathbf V}(x,y)=(p(x,y), q(x,y))` er skilgreint á :math:`X` og við gerum ráð fyrir að allar þær hlutafleiður sem við munum þurfa á að halda séu skilgreindar og samfelldar á öllu :math:`X`.

Túlkun 
~~~~~~

Við hugsum okkur að vigursviðið lýsi vökvaflæði í planinu þannig að í punkti :math:`(x,y)` þá er :math:`{\mathbf V}(x,y)` hraðavigur agnar sem berst með vökvanum. Vökvaflæðið hér breytist ekki með tíma. 

Straumlínur 
~~~~~~~~~~~

Straumlína er ferill í :math:`{\mathbb{R}}^2` sem gefur braut agnar sem berst með vökvanum. Mest lýsandi fyrir straumlínur er að finna stikunn :math:`\gamma(t)` þannig að ef ögnin er í punktinum :math:`(x_0, y_0)=\gamma(0)` á tíma :math:`t=0` þá er hún í punktinum :math:`\gamma(t)` á tíma :math:`t`.

Ósamþjappanlegur vökvi
~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að vökvinn sé hvergi að þjappast saman eða þenjast út. Þetta segir að ef við látum :math:`\Omega` vera svæði í :math:`X` þannig að jaðar :math:`\Omega` er einfaldur lokaður ferill þá er ,,nettó‘‘flæðið út úr :math:`\Omega` jafnt of 0. Með vísan til Sundurleitnisetningarinnar þá má lýsa þessum eiginleika með því að :math:`{\mathbf V}` sé sundurleitnilaus, þ.e.a.s.

.. math::

 \frac{\partial p}{\partial x}+ \frac{\partial q}{\partial y}=0.

Engir hvirflar
~~~~~~~~~~~~~~

Gerum einnig ráð fyrir að engir hvirflar séu í vökvaflæðinu. Við viljum að hringstreymið eftir sérhverjum lokuðum einföldum ferli sé 0. Með vísan til Setningar Green (eða Setningar Stokes) þá er þetta jafngilt því að krefjast þess að vigursviðið sé rótlaust, þ.e.a.s.

.. math::

 \frac{\partial q}{\partial x}-\frac{\partial p}{\partial y}=0.

Mætti 
~~~~~

Fall :math:`\varphi:X\to {\mathbb{R}}` kallast (raun)mætti fyrir :math:`{\mathbf V}` ef :math:`{\mathbf V}(x,y)=\nabla\varphi(x,y)` í öllum punktum :math:`(x,y)\in X`.

   
Skipt um umhverfi 
~~~~~~~~~~~~~~~~~

Lítum nú á tvinntalnaplanið :math:`{\mathbb{C}}` og planið :math:`{\mathbb{R}}^2` sem sama hlutinn. Ritum nú :math:`z=x+iy` og :math:`{\mathbf V}(z)=p(z)+iq(z)`. Hér lítum við á :math:`{\mathbf V}` sem fall :math:`{\mathbf V}:X\to {\mathbb{C}}`.
  

Setning (Sjá §5.2)
~~~~~~~~~~~~~~~~~~~

Fallið :math:`\overline{\mathbf V}:X\to {\mathbb{C}}` þar sem :math:`\overline{\mathbf V}=p-iq` er fágað á :math:`X`.

Ef :math:`f=\varphi+i\psi` er fágað fall á :math:`X` þannig að :math:`f'=\overline{\mathbf V}` þá er :math:`\nabla \varphi={\mathbf V}`. Straumlínur :math:`{\mathbf V}` eru svo jafnhæðarlínur fallsins :math:`\psi`.

   
Skilgreining (Sjá §5.2)
~~~~~~~~~~~~~~~~~~~~~~~

Fallið :math:`f` kallast tvinnmætti fyrir :math:`{\mathbf V}`, fallið :math:`\varphi:X\to {\mathbb{R}}` kallast raunmætti fyrir :math:`{\mathbf V}` og fallið :math:`\psi:X\to {\mathbb{R}}` kallast streymisfall. 
