Hlutafleiðujöfnur
=================

Inngangur
---------

Mörg verkefni í t.a.m. verkfræði og eðlisfræði krefjast þess að ákvarða fall af mörgum breytistærðum sem lýsir einhverjum eiginleika kerfis. Slíkum föllum er oft lýst með afleiðujöfnum þar sem hlutafleiður með tilliti til mismunandi breytistærða koma við sögu. Slíkar afleiðujöfnur nefnast *hlutafleiðujöfnur*.

Ef :math:`u` er fall af breytistærðunum :math:`x_1,x_2,\ldots,x_m` skrifum við hlutafleiður þess með tilliti til :math:`x_j` með
einhverjum eftirfarandi tákna

.. math::
    \partial_j u, \quad \frac{\partial u}{\partial x_j},\quad  \partial_{x_j} u, \quad u'_{x_j} \quad \text{eða}\quad  u_{x_j}.

Í sumum tilfellum hefur skapast venja að nota ákveðið táknmál fyrir breytistærðirnar. Til dæmis er :math:`t` gjarnan notað fyrir tíma og :math:`x,y,z` fyrir rúmvíddirnar þrjár.

Þegar breytistærðirnar eru margar getur verið þægilegt að nota eftirfarandi rithátt:

Ritháttur - Fjölvísir
~~~~~~~~~~~~~~~~~~~~~
Ef :math:`\alpha = (\alpha_1,\ldots,\alpha_m)` er vigur af ekki neikvæðum heiltölum skilgreinum við hlutafleiðuvirkjann :math:`\partial^\alpha` með

.. math::
    \partial^\alpha u = \partial_1^{\alpha_1}\cdots \partial_m^{\alpha_m} u.

Vigurinn :math:`\alpha` nefnist í þessu samhengi *fjölvísir*.

Ritháttur - Laplace-virki
~~~~~~~~~~~~~~~~~~~~~~~~~
Virkinn

.. math::
    \Delta = \partial_{x_1}^2+\cdots + \partial_{x_m}^2

kallast Laplace-virkinn í :math:`m` breytistærðum.





Skilgreining - Stig hlutafleiðu og hlutafleiðujöfnu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Hlutafleiðan :math:`\partial^\alpha u` hefur stig :math:`|\alpha| = \alpha_1 + \cdots + \alpha_m`.  Hæsta stig á afleiðu sem kemur fyrir í hlutafleiðujöfnu nefnist *stig* hlutafleiðujöfnunnar.


	Við munum skoða **dæmi um hlutafleiðujöfnur** og læra **mismunandi aðferðir við að leysa þær**. Í sumum tilfellum má leysa jöfnurnar og skrifa niður beina lausn en oft þarf að nota **tölulegar aðferðir** til að leysa verkefnin. Töluleg verkefni verða viðfangsefni síðara hluta námskeiðsins.



Línulegar hlutafleiðujöfnur
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við munum eingöngu fást við línulegar hlutafleiðujöfnur í þessu námskeiði. Hlutafleiðujafna er sögð vera **línulegt** ef hægt er að rita hana á forminu

.. math::
    \sum_{|\alpha|\leq m} a_\alpha(x) \partial^\alpha u(x) = f(x), \quad x\in X \subseteq \mathbb{R}^n.

Fallið :math:`u` er óþekkta stærðin sem við viljum reikna, :math:`a_\alpha(x)` eru stuðlar sem geta verið háðir :math:`x` og fallið :math:`f` er gefið. Ef :math:`f` er núllfallið segjum við að hlutafleiðujafan sé **óhliðruð** en annars að hún sé **hliðruð**.

Við munum einnig nota ritháttin

.. math::
    Lu = f

þar sem við lítum á

.. math::
    L = \sum_{|\alpha|\leq m} a_\alpha(x) \partial^\alpha

sem línulegan virkja :math:`L: C^m(X) \to C(X), X\subseteq \mathbb{R}^n` sem úthlutar falli línulegri samantekt af fallinu sjálfu og hlutafleiðum þess upp að stigi :math:`m`. Virkinn :math:`L` er línulegur því

.. math::
    L(au + bv) = aL(u) + bL(v)

fyrir hvaða tölur :math:`a` og :math:`b` sem er. **Kjarni** eða **núllrúm** virkjans :math:`L` er skilgreint sem mengi allra þeirra :math:`u\in C^m(X)` sem eru lausnir á óhliðruðu jöfnunni :math:`Lu=0`. Ef :math:`u_p` er lausn á :math:`Lu = f` þá er sérhver önnur lausn á forminu :math:`u = v+u_p` þar sem :math:`v` er í núllrúminu.



Dæmi um hlutafleiðujöfnur í eðlisfræði
--------------------------------------



Varmaleiðnijafnan
~~~~~~~~~~~~~~~~~
Ef :math:`T` er fall af :math:`m+1` breytistærðum :math:`x_1,\ldots,x_m,t` kallast jafnan

.. math::
    \frac{\partial T}{\partial t} - \kappa \Delta T = f(x_1,\ldots,x_m,t)

*varmaleiðnijafnan* í :math:`m` rúmvíddum. Talan :math:`\kappa` ákvarðast af eiginleikum þess kerfis sem fengist er við og fallið :math:`f` svarar til ytri áhrifa á kerfið.

Varmaleiðnijafnan lýsir því hvernig hitastig :math:`T` í hlut breytist með tíma. Þá svarar :math:`f` til áhrifa ytri varmagjafa. Jafnan getur einnig lýst dreifingu efnis sem leyst er upp í vökva og er þá gjarnan nefnd *sveimjafna*.

Bylgjujafnan
~~~~~~~~~~~~

Ef :math:`u` er fall af :math:`m+1` breytistærðum :math:`t, x_1,\ldots,x_m` kallast jafnan

.. math::
    \frac{\partial^2 u}{\partial t^2} - c^2 \Delta u = f(x_1,\ldots,x_m,t)

*bylgjujafnan* í :math:`m` rúmvíddum. Talan :math:`c` hefur einingu hraða og ákvarðast af eiginleikum þess kerfis sem fengist er við og fallið :math:`f` svarar til svarar til ytri áhrifa á kerfið.

Bylgjujafnan kemur mjög víða við sögu í eðlisfræði. Hún getur til dæmis lýst sveiflu á einvíðum streng eða tvívíðri trommu en þá táknar :math:`u` færslu strengsins eða trommuskinnsins frá jafnvægisstöðu og :math:`f` svarar til ytri krafts, t.d. ef strengurinn er plokkaður eða tromman slegin. Annað dæmi er lýsing á útbreiðslu rafsegulbylgna en í því tilfelli má leiða bylgjujöfnuna út frá jöfnum Maxwells.

Dæmi - Sveifla á einvíðum streng
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
	:class: daemi

	Hér má sjá lausn á bylgjujöfnunni

	.. math::
	    \frac{\partial^2 u(x,t)}{\partial t^2} - c^2  \frac{\partial^2 u(x,t)}{\partial x^2} = 0

	fyrir :math:`x` á bilinu :math:`[0,L]` með jaðarskilyrðunum :math:`u(0,t) = u(L,t)=0` (strengurinn er fastur í báða enda) og upphafsskilyrðunum :math:`u(x,0) = a(x),~\partial_t u(x,0) = b(x)`. Upphaflegu stillingarnar eru :math:`L=2\pi`, :math:`a(x) = \sin(2x)+\sin(3x)` og :math:`b(x) = \sin(x)`.


	.. ggb:: cfyvqajc
	  :width: 700
	  :height: 550
	  :img: polarggb.png
	  :imgwidth: 4cm
	  :zoom_drag: true

|
|

Hliðarskilyrði. Vel framsett verkefni
-------------------------------------

Skoðum verkefnið að ákvarða fall :math:`u` sem uppfyllir hlutafleiðujöfnu :math:`Lu = f` á mengi :math:`X \times I \in \mathbb{R}^{n+1}`, þar sem :math:`X\subseteq \mathbb{R}^n` er opið mengi og :math:`I \subseteq \mathbb{R}` er bil. Hugsum um breytuna :math:`x\in X` sem rúmbreytu og breytuna :math:`t\in I` sem tíma.



Til að ákvarða :math:`u`  ótvírætt þarf oft hliðarskilyrði á fallið. Þau geta verið á eftirfarandi formi.


Upphafsskilyrði
~~~~~~~~~~~~~~~
Þá eru gildi á fallinu :math:`u` og einhverjum tímaafleiðum þess :math:`\partial_t u,\partial_t^2 u,\ldots` gefin á ákveðnum upphafstíma. Nefnast einnig *Cauchy-skilyrði*.

Jaðarskilyrði
~~~~~~~~~~~~~

Skilgreinum stefnuafleiðu :math:`u` út um jaðar :math:`X` með

.. math::
    \frac{\partial u}{\partial n} = \nabla u \cdot \vec n

þar sem :math:`\nabla` er stigull með tilliti til rúmbreytanna og :math:`\vec n` er einingarþvervigur sem stefnir út úr :math:`X` (þegar það hefur merkingu).

Mikilvæg jaðarskilyrði sem koma upp víða í eðlisfræði eru á eftirfarandi formi

#. Lausnin :math:`u` er tilgreind á jaðri svæðisins. Nefnist *Dirichlet-skilyðri* eða *fallsjaðarskilyrði*.

#. Stefnuafleiðan :math:`\partial u/\partial n` er tilgreind á jaðri svæðisins. Nefnist *Neumann-skilyrði* eða *flæðisskilyrði*.

#. Línuleg samantekt af :math:`u` og :math:`\partial u/\partial n` er tilgreind á jaðri svæðis. Nefnist *Robin-skilyrði* eða *blandað jaðarskilyrði*.

Athugið að jaðarskilyrði fyrir venjulegar afleiðujöfnur eru yfirleitt í 1 eða 2 punktum en jaðar mengis :math:`X \subseteq \mathbb{R}` getur verið mjög almennur.



Vel framsett verkefni
~~~~~~~~~~~~~~~~~~~~~

Úrlausn á hlutafleiðujöfnu með hliðarskilyrðum nefnist *vel framsett verkefni*, ef eftirfarandi
þrjú skilyrði eru uppfyllt:

#. **Tilvist:** Til er lausn sem uppfyllir jöfnuna og öll hliðarskilyrðin.

#. **Ótvíræðni:** Aðeins ein lausn er til.

#. **Stöðugleiki:** Lausnin er stöðug í þeim skilningi að lítilsháttar frávik frá hliðarskilyrðum kemur fram í lítilsháttar fráviki frá lausninni. Í hverju verkefni um sig þarf að skigreina hvaða mælikvarði er lagður á frávik í hliðarskilyrðum og í lausn.

Við munum leggja mesta áherslu á skilyrðið **1. Tilvist** í þessu námskeiði.


Fyrsta stigs jöfnur
-------------------

Línuleg fyrsta stigs hlutafleiðujafna af tveimur breytistærðum :math:`(x,y)` er af gerðinni

.. math::
    a(x,y)\frac{\partial u}{\partial x} + b(x,y) \frac{\partial u}{\partial y} + c(x,y)u = f(x,y).

Skoðum aðferðir við að leysa slíkar jöfnur.

Kennilínuaðferðin
~~~~~~~~~~~~~~~~~

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

	Fall :math:`u\in C^1(\mathbb{R}^2)` er lausn á jöfnunni

	.. math::
	    a\frac{\partial u}{\partial x}+ b\frac{\partial u}{\partial y} = 0

	þar sem :math:`(a,b)\in\mathbb{R}^2` og :math:`(a,b)\neq (0,0)` þá og því aðeins að :math:`u` sé af gerðinni

	.. math::
	    u(x,y) = f(bx-ay)

	með :math:`f\in C^1(\mathbb{R})`.


Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

	Upphafsgildisverkefnið

	.. math::
	    \left\{\begin {array}{l}
	    a\frac{\partial u}{\partial x}+ b\frac{\partial u}{\partial y} = 0, \quad (x,y)\in \mathbb{R}^2, \\
	    u(x,0) = \phi(x),\quad x \in \mathbb{R}
	    \end{array}\right.

	þar sem :math:`\phi \in C^1(\mathbb{R})` er gefið fall og :math:`b\neq 0` hefur ótvírætt ákvarðaða lausn

	.. math::
	    u(x,y) = \phi(x-ay/b).

Skilgreining
~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Lína sem hefur stefnuvigur samsíða :math:`(a, b)` nefnist kennilína afleiðuvirkjans :math:`a\partial_x + b\partial_y`.


Skilgreining
~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Sérhver lausn  á afleiðujöfnuhneppinu

	.. math::
	    \xi' = a(\xi,\eta), \qquad \eta' = b(\xi,\eta),

	nefnist kenniferill eða kennilína afleiðuvirkjans

	.. math::
	    a(x,y)\frac{\partial}{\partial x} + b(x,y) \frac{\partial}{\partial y}

Reikniaðferð
~~~~~~~~~~~~

Finna skal lausn á upphafsgildisverkefninu

.. math::
    \left\{\begin {array}{l}
    a(x,y)\frac{\partial u}{\partial x}+ b(x,y)\frac{\partial u}{\partial y} = 0, \quad (x,y)\in \mathbb{R}^2, \\
    u(x,0) = \phi(x), \quad x \in \mathbb{R}.
    \end{array}\right.

1. Tökum punkt :math:`(x,y)` í :math:`(\xi,\eta)` plani. Leysum verkefnið

.. math::
     \xi' = a(\xi,\eta), \qquad \eta' = b(\xi,\eta), \qquad \xi(0) = x, \quad \eta(0) = y.

2. Ef til er ótvírætt ákvörðuð lausn :math:`(\xi(t),\eta(t))` á einhverju opnu bili fyrir sérhvert :math:`(x,y)` og ferillinn sker :math:`\xi`-ásinn í nákvæmlega einum punkti :math:`(s(x,y),0)` þá er lausnin gefin með formúlunni

.. math::
    u(x,y) = \phi(s(x,y)).

Úrlausn með Laplace-ummyndun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~



Laplace ummyndun er gagnleg þegar leysa skal upphafsgildisverkefni og virkar einnig þegar um hlutafleiðujöfnur er að ræða. Eftirfarandi reikniaðferð má beita á fyrsta stigs hlutafleiðujöfnu falls :math:`u(x,t)` þegar stuðlarnir eru ekki háðir :math:`t`.

1. Tökum Laplace-mynd af báðum hliðum miðað við breytistærðina :math:`t`. Gert er ráð fyrir að víxla megi á afleiðum og heildum þar sem þarf.


2. Þá fæst fyrsta stigs venjuleg afleiðujafna í :math:`x` fyrir fallið

.. math::
    U(x,s) = \mathcal{L}\{u(x,t)\}(s) = \int_{0}^\infty e^{-st}u(x,t) dt

sem má leysa með almennri lausnarformúlu.

3. Lausn upphaflega verkefnisins fæst með því að taka andhverfu Laplace-myndina af :math:`U(x,s)`.

Dæmi
~~~~

.. admonition:: Dæmi  
	:class: daemi

	Upphafsgildisverkefnið

	.. math::
	    \left\{\begin {array}{l}
	    \frac{\partial u}{\partial t}+ x\frac{\partial u}{\partial x} + u = f(x,t), x>0, t>0, \\
	    u(x,0) = u(0,t) = 0.
	    \end{array}\right.

	hefur lausnina

	.. math::
	    u(x,t) = x^{-1}\int_{0}^x H(t-\ln(x/\xi)) f(\xi,t-\ln(x/\xi)) d\xi

	þar sem :math:`H` táknar Heaviside-fallið.
