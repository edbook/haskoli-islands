

Útgildisverkefni
================

*Old stories are like old friends, she used to say. You have to visit them from time to time.*

\-George R.R. Martin, A Storm of Swords 

.. index::
  útgildi
  lággildi;staðbundið lággildi
  hágildi;staðbundið hágildi
  útgildi;staðbundið útgildi
  hæsta gildi

Útgildi
-------

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`f` vera fall af tveim breytum skilgreint á mengi
:math:`{\cal D}(f)`.

Sagt er að :math:`f` hafi :hover:`staðbundið lággildi` í
punkti :math:`(a,b)` ef til er tala :math:`r>0` þannig að
:math:`f(a,b)\leq f(x,y)` fyrir alla punkta
:math:`(x,y)\in B_r(a,b)\cap{\cal D}(f)`.

Sagt er að :math:`f` hafi :hover:`staðbundið hágildi`  í
punkti :math:`(a,b)` ef til er tala :math:`r>0` þannig að
:math:`f(a,b)\geq f(x,y)` fyrir alla punkta
:math:`(x,y)\in B_r(a,b)\cap{\cal D}(f)`.

Í þeim punktum þar sem :math:`f` tekur annað hvort staðbundið lággildi
eða staðbundið hágildi er sagt að :math:`f` hafi :hover:`staðbundið útgildi`


Ef :math:`f(a,b)\leq f(x,y)` fyrir alla punkta
:math:`(x,y)\in {\cal D}(f)` þá er sagt að :math:`f` taki *lægsta gildi*
í :math:`(a,b)` (e. global minimum). Ef :math:`f(a,b)\geq f(x,y)` fyrir
alla punkta :math:`(x,y)\in {\cal D}(f)` þá er sagt að :math:`f` taki
:hover:`hæsta gildi` í :math:`(a,b)`.

.. index::
  útgildi;staðbundið útgildi
  stöðupunktur

Staðbundið útgildi
------------------

Upprifjun
~~~~~~~~~

Látum :math:`f` vera fall af einni breytu skilgreint á mengi
:math:`{\cal D}(f)\subseteq {\mathbb  R}`. Ef fallið :math:`f` hefur
staðbundið útgildi í punkti :math:`a` þá gildir eitt af þrennu um
:math:`a`:

#. :math:`f'(a)=0`. (punkturinn :math:`a` kallast :hover:`stöðupunktur`
   :math:`f`).

#. Afleiðan :math:`f'(a)` er ekki skilgreind.

#. Punkturinn :math:`a` er :hover:`jaðarpunktur` :math:`{\cal D}(f)`.

Setning 
~~~~~~~~

Látum :math:`f` vera fall af tveim breytum skilgreint á mengi
:math:`{\cal D}(f)\subseteq {\mathbb  R}^2`. Ef fallið :math:`f` hefur
:hover:`staðbundið útgildi` í punkti :math:`(a,b)` þá gildir eitt af þrennu um
:math:`a`

#. :math:`\nabla f(a,b)=\mbox{${\bf 0}$}`. (punkturinn :math:`(a,b)`
   kallast :hover:`stöðupunktur` :math:`f`)

#. :hover:`Stigullinn,stigull` :math:`\nabla f(a,b)` er ekki skilgreindur.

#. Punkturinn :math:`(a,b)` er :hover:`jaðarpunktur` :math:`{\cal D}(f)`.

Dæmi 
~~~~

Föll skilgreind á svæðinu :math:`-0.5 \leq x \leq 0.5`,
:math:`-0.5 \leq y \leq 0.5`. Hvar eru staðbundin hágildi?

.. image:: peak_smooth.png
  :width: 60%
  :align: center

..

:math:`z = f(x,y) = 1-x^2-y^2`.

.. image:: peak.png
  :width: 60%
  :align: center

..

:math:`z = f(x,y) = 1-\sqrt{x^2+y^2}`.

.. image:: max_bound.png
  :width: 60%
  :align: center


..

:math:`z= f(x,y) = x^2+y^2`.

Tilvist útgilda
---------------

Setning 
~~~~~~~~

Látum :math:`f` vera samfellt fall af tveim breytum skilgreint á lokuðu
og takmörkuðu mengi :math:`{\cal D}(f)`. Fallið :math:`f` tekur þá bæði
hæsta og lægsta gildi.

.. index::
  söðulpunktur
  


Söðulpunktur
------------

Skilgreining 
~~~~~~~~~~~~~

Punktur :math:`(x,y)\in  {\cal D}(f)` sem er ekki jaðarpunktur kallast
:hover:`söðulpunktur` ef :math:`\nabla f(x,y)=\mbox{${\bf 0}$}` en :math:`f`
hefur ekki staðbundið útgildi í :math:`(x,y)`.

Dæmi um föll með söðulpunkta.

.. image:: sodull1.png
   :width: 60%
   :align: center


..

:math:`z = f(x,y) = x^3`.

.. image:: sodull2.png
   :width: 60%
   :align: center


..

:math:`z = f(x,y) = x^3+y^3`.

Staðbundið útgildi
------------------

Upprifjun 
~~~~~~~~~~

Látum :math:`f` vera fall af einni breytistærð og gerum ráð fyrir að
:math:`f'` sé samfellt fall. Gerum einnig ráð fyrir að :math:`f'(a)=0`.
Þá gildir:

#. Ef :math:`f''(a)>0` þá hefur :math:`f` :hover:`staðbundið lággildi` í
   :math:`a`.

#. Ef :math:`f''(a)<0` þá hefur :math:`f` :hover:`staðbundið hágildi` í
   :math:`a`.

#. Ef :math:`f''(a)=0` þá gæti verið staðbundið lággildi í :math:`A`,
   það gæti verið staðbundið hágildi í :math:`a` eða það gætu verið
   beygjuskil í :math:`a`, alltsvo. ekkert hægt að segja.

Hesse-fylki
-----------

Skilgreining 
~~~~~~~~~~~~~

Látum :math:`f` vera fall af :math:`n` breytum
:math:`\mathbf{x} = (x_1,x_2,\ldots,x_n)` og gerum ráð fyrir að allar
2. stigs hlutafleiður :math:`f` séu skilgreindar í punktinum
:math:`\mathbf{x}`. Skilgreinum *Hesse-fylki* :math:`f` í punktinum
:math:`\mathbf{x}` sem :math:`n\times n`-fylkið

.. math::

   {\cal H}(\mathbf{x})=\begin{bmatrix} f_{11}(\mathbf{x})&f_{12}(\mathbf{x}) & \cdots & f_{1n}(\mathbf{x})\\
    f_{21}(\mathbf{x})&f_{22}(\mathbf{x}) & \cdots & f_{2n}(\mathbf{x}) \\
    \vdots & \vdots & \ddots & \vdots & \\
     f_{n1}(\mathbf{x})&f_{n2}(\mathbf{x}) & \cdots & f_{nn}(\mathbf{x})\end{bmatrix}.


.. index::
  ferningsform
     
Ferningsform (sjá kafla 10.7 í Adams)
-------------------------------------

Upprifjun 
~~~~~~~~~~

:hover:`Ferningsform` :math:`Q` af :math:`n`-breytum
:math:`x_1,x_2,\ldots, x_n` er einsleit margliða af stigi 2 gefin með

.. math:: Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}

þar sem :math:`A` er samhverft :math:`n \times n` fylki með tölu
:math:`a_{ij}` í sæti :math:`(i,j)` og
:math:`\mathbf{x} = [x_1,x_2,\ldots x_n]^T`.

Skilgreining 
~~~~~~~~~~~~~

Ferningsform :math:`Q` af :math:`n`-breytum er sagt vera :hover:`jákvætt ákvarðað,jákvætt ákveðinn` ef :math:`Q(\mbox{${\bf x}$})>0` fyrir
alla vigra :math:`\mbox{${\bf x}$}\neq \mbox{${\bf 0}$}` í
:math:`\mbox{${\bf R}^n$}`.

Sagt að ferningsformið :math:`Q` sé :hover:`neikvætt ákvarðað, neikvætt ákveðinn` ef :math:`Q(\mbox{${\bf x}$})<0` fyrir alla vigra
:math:`\mbox{${\bf x}$}\neq \mbox{${\bf 0}$}` í
:math:`\mbox{${\bf R}^n$}`.

Síðan er sagt að ferningsformið :math:`Q` sé :hover:`óákvarðað,óákvarðaður`
ef :math:`Q(\mbox{${\bf x}$})<0` fyrir einhvern vigur
:math:`\mbox{${\bf x}$}` og :math:`Q(\mbox{${\bf y}$})>0` fyrir einhvern
vigur :math:`\mbox{${\bf y}$}`.

Setning 
~~~~~~~~

Látum :math:`Q` vera fernings form af :math:`n` breytum og :math:`A`
samhverft :math:`n\times n` fylki þannig að
:math:`Q(\mbox{${\bf x}$})=\mbox{${\bf x}$}^TA\mbox{${\bf x}$}` fyrir
alla vigra :math:`\mbox{${\bf x}$}`,

#. Ferningsformið er jákvætt ákvarðað ef og aðeins ef öll :hover:`eigingildi`
   :math:`A` eru jákvæð.

#. Ferningsformið er neikvætt ákvarðað ef og aðeins ef öll :hover:`eigingildi`
   :math:`A` eru neikvæð.

#. Ferningsformið er óákvarðað ef og aðeins ef :math:`A` hefur bæði
   jákvæð og neikvæð :hover:`eigingildi`

Staðbundið útgildi
------------------

Setning 
~~~~~~~~

Látum :math:`f` vera fall af :math:`n` breytum
:math:`\mathbf{x} = (x_1,x_2,\ldots,x_n)` þannig að allar 1. og 2. stigs
hlutafleiður :math:`f` eru samfelldar. Látum :math:`\mathbf{a}` vera
innri punkt á skilgreiningarsvæði :math:`f` og gerum ráð fyrir að
:math:`\nabla
f(\mathbf{a})=\mbox{${\bf 0}$}`. Þá gildir: Ef
:math:`{\cal H}(\mathbf{a})` er

#. ...jákvætt ákvarðað þá hefur :math:`f` :hover:`staðbundið lággildi` í
   :math:`\mathbf{a}`.

#. ...neikvætt ákvarðað þá hefur :math:`f` :hover:`staðbundið hágildi` í
   :math:`\mathbf{a}`.

#. ...óákvarðað þá hefur :math:`f` :hover:`söðulpunkt,söðulpunktur` í :math:`\mathbf{a}`.

#. ...hvorki jákvætt ákvarðað, neikvætt ákvarðað né óákvarðað þá nægja
   upplýsingarnar sem felast í jöfnunni
   :math:`\nabla f(\mathbf{a})=\mbox{${\bf 0}$}` og Hesse-fylkinu ekki
   til að segja til um hvers eðlis stöðupunkturinn :math:`\mathbf{a}`
   er.

Fylgisetning 
~~~~~~~~~~~~~

Látum :math:`f` vera fall af tveim breytum þannig að 1. og 2. stigs
hlutafleiður :math:`f` eru samfelldar. Látum :math:`(a,b)` vera innri
punkt á skilgreiningarsvæði :math:`f` og gerum ráð fyrir að
:math:`\nabla
f(a,b)=\mbox{${\bf 0}$}`. Setjum

.. math::

   A=f_{11}(a,b),\qquad\quad B=f_{12}(a,b)=f_{21}(a,b)\qquad\quad
   C=f_{22}(a,b).

Þá gildir:

#. Ef :math:`B^2-AC<0` og :math:`A>0` þá hefur :math:`f` :hover:`staðbundið
   lággildi` í :math:`(a,b)`.

#. Ef :math:`B^2-AC<0` og :math:`A<0` þá hefur :math:`f` :hover:`staðbundið
   hágildi` í :math:`(a,b)`.

#. Ef :math:`B^2-AC>0` þá hefur :math:`f` :hover:`söðulpunkt,söðulpunktur` í :math:`(a,b)`.

#. Ef :math:`B^2-AC=0` þá er ekkert hægt að segja.

Ferningsform
------------

Regla 
~~~~~~

Ef :math:`A` er samhverft :math:`n \times n` fylki með tölu
:math:`a_{ij}` í sæti :math:`(i,j)` og

.. math::

   D_i = \begin{vmatrix}
           a_{11} & a_{12} & \cdots & a_{1i} \\
           a_{21} & a_{22} & \cdots & a_{2i} \\
           \vdots & \vdots & \ddots & \vdots \\ 
           a_{i1} & a_{i2} & \cdots & a_{ii} 
          \end{vmatrix}

þá gildir

#. Ef :math:`D_i > 0` fyrir :math:`1\leq i \leq n` þá er :math:`A`
   :hover:`jákvætt ákvarðað,jákvætt ákveðinn`.

#. Ef :math:`D_i > 0` fyrir slétt :math:`i` í :math:`\{1,2,\ldots,n\}`
   og :math:`D_i < 0` fyrir oddatölu :math:`i` í
   :math:`\{1,2,\ldots,n\}` þá er :math:`A` :hover:`neikvætt ákvarðað,neikvætt ákveðinn`.

#. Ef :math:`\det(A) = D_n \neq 0` en hvorki :math:`1` né :math:`2`
   gilda þá er :math:`A` :hover:`óákvarðað`.

#. Ef :math:`\det(A) = 0` þá er :math:`A` hvorki jákvætt né neikvætt
   ákvarðað en getur verið :hover:`óákvarðað,óákvarðaður`.

.. index::
  skorðujöfnur
   
Útgildi falla þar sem breytur uppfylla skorðujöfnur
---------------------------------------------------

Sértækar aðferðir 
~~~~~~~~~~~~~~~~~~

Finna skal útgildi falls :math:`f(x,y)` þegar skilgreiningarsvæði
:math:`f` er mengi þeirra punkta :math:`(x,y)` sem uppfylla jöfnu
:math:`g(x,y)=0`.

#. Er mögulegt að einangra :math:`x` eða :math:`y` í jöfnunni
   :math:`g(x,y)=0`?

   -  Ef hægt er að einangra :math:`y` og rita :math:`y=h(x)` þá snýst
      verkefnið nú um að finna útgildi falls :math:`f(x,h(x))` af einni
      breytu :math:`x`.

#. Er hægt að stika ferilinn :math:`g(x,y)=0`?

   -  Ef :math:`\mbox{${\bf r}$}` er stikun á ferlinum þá þurfum við að
      leita að útgildum fallsins :math:`f(\mbox{${\bf r}$}(t))` þar sem
      er bara ein breyta.

Dæmi
~~~~

.. image:: constraint.png
   :width: 60%
   :align: center

..  

*Hver eru hæstu og lægstu gildi fallsins* :math:`f(x,y) = x^2-y^2+4` *á
menginu* :math:`\{(x,y)~|~x^2+y^2=1\}`?

Setning 
~~~~~~~~

Látum :math:`f` og :math:`g` vera föll sem eru bæði diffranleg í
punktinum :math:`P_0=(x_0,y_0)` sem liggur á ferlinum :math:`g(x,y)=0`,
og er ekki endapunktur ferilsins. Gerum ráð fyrir að
:math:`\nabla g(x_0,y_0)\neq \mbox{${\bf 0}$}`. Gerum líka ráð fyrir að
ef við einskorðum fallið :math:`f` við ferilinn :math:`g(x,y)=0` þá hafi
:math:`f` staðbundið útgildi í :math:`P_0`. Þá eru stiglarnir
:math:`\nabla f(x_0,y_0)` og :math:`\nabla g(x_0,y_0)` samsíða.

.. image:: lagrange1.png
   :width: 40%
   :align: center

..

*Ef stiglarnir* :math:`\nabla g(P_0)` *og* :math:`\nabla f(P_0)` *eru ekki
samsíða þá vex* :math:`f` *eða minnkar þegar farið er eftir*
:math:`\mathcal{C}` *út frá punktinum* :math:`P_0`.

.. index::
  Lagrange-margfaldarar

Lagrange-margfaldarar
---------------------

Reikniaðferð 
~~~~~~~~~~~~~

Finna skal útgildi falls :math:`f(x,y)` þegar skilgreiningarsvæði
:math:`f` er mengi þeirra punkta :math:`(x,y)` sem uppfylla jöfnu
:math:`g(x,y)=0`.

Búum til *Lagrange-fallið*

.. math:: L(x,y,\lambda)=f(x,y)+\lambda g(x,y).

:hover:`Stöðupunktar,stöðupunktur` :math:`L`, þ.e.a.s. punktar :math:`(x_0,y_0,\lambda_0)` þar
sem :math:`\nabla L(x_0,y_0,\lambda_0)=\mbox{${\bf 0}$}`, gefa mögulega
punkta :math:`(x_0,y_0)` þar sem :math:`f` tekur útgildi.

Þessir punktar finnast með því að leysa jöfnuhneppið

.. math::

   \begin{aligned}
   f_1(x,y)+\lambda g_1(x,y)&=0\\
   f_2(x,y)+\lambda g_2(x,y)&=0\\
   g(x,y)&=0.\end{aligned}

Talan :math:`\lambda` nefnist *Lagrange-margfaldari*.

Regla 
~~~~~~

Finna skal :hover:`útgildi` falls :math:`f(x,y)` þegar skilgreiningarsvæði
:math:`f` er mengi þeirra punkta :math:`(x,y)` sem uppfylla jöfnu
:math:`g(x,y)=0`.

Athuga þarf punkta sem uppfylla eitt af eftirfarandi skilyrðum:

#. :hover:`Stöðupunktar,stöðupunktur` :math:`L(x,y,\lambda)`.

#. Punktar :math:`(x,y)` þar sem :math:`\nabla g(x,y)=\mbox{${\bf 0}$}`

#. Punktar :math:`(x,y)` þar sem annar eða báðir stiglanna
   :math:`\nabla g(x,y)` og :math:`\nabla f(x,y)` eru ekki skilgreindir.

#. ,,Endapunktar” ferilsins :math:`g(x,y)=0`.

Reikniaðferð 
~~~~~~~~~~~~~

Finna skal  :hover:`útgildi` falls :math:`f(x,y,z)` þegar skilgreiningarsvæði
:math:`f` er mengi þeirra punkta :math:`(x,y,z)` sem uppfylla jöfnurnar
:math:`g(x,y,z)=0` og :math:`h(x,y,z)=0`.

Búum til Lagrange-fallið

.. math:: L(x,y,z,\lambda,\mu)=f(x,y,z)+\lambda g(x,y,z)+\mu h(x,y,z).

:hover:`Stöðupunktar,stöðupunktur` :math:`L`, þ.e.a.s. punktar
:math:`(x_0,y_0,z_0,\lambda_0,\mu_0)` þar sem
:math:`\nabla L(x_0,y_0,z_0,\lambda_0,\mu_0)=\mbox{${\bf 0}$}` gefa
mögulega punkta :math:`(x_0,y_0,z_0)` þar sem :math:`f` tekur  :hover:`útgildi`.

Þessir punktar finnast með því að leysa jöfnuhneppið

.. math::

   \begin{aligned}
   f_1(x,y,z)+\lambda g_1(x,y,z)+\mu h_1(x,y,z)&=0\\
   f_2(x,y,z)+\lambda g_2(x,y,z)+\mu h_2(x,y,z)&=0\\
   f_3(x,y,z)+\lambda g_3(x,y,z)+\mu h_3(x,y,z)&=0\\
   g(x,y,z)&=0\\
   h(x,y,z)&=0.\end{aligned}


