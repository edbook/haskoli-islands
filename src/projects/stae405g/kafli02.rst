Núllstöðvar
===========

*Build a man a fire, and he'll be warm for a day. Set a man on fire, and he'll 
be warm for the rest of his life.*

\- Terry Pratchett, Jingo

Nálgun á núllstöð
-----------------

.. index:: 
    núllstöð

Skilgreining
~~~~~~~~~~~~

Munum að talan :math:`p\in I` sögð vera *núllstöð* fallsins
:math:`f:I\to {\mathbb  R}` ef

.. math:: 
    f(p)=0.

Dæmi
~~~~
    
Það er auðvelt að finna núllstöðvar (**rót**) annars stigs margliðu 
:math:`ax^2+bx+c`, því 

.. math::
    ax^2+bx+c = 0
    
ef 

.. math::
    x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}.

Svipaðar formúlur eru til fyrir núllstöðvar þriðja og fjórða stigs margliða.
Einnig þekkjum við núllstöðvar hornafalla.


Athugasemd
~~~~~~~~~~

Almennt er hins vegar erfitt að finna núllstöðvar falla.
Til dæmis er ekki til almenn formúla fyrir núllstöðvar margliða af stigi 5 og hærra 
(sjá `Abel-Ruffini setningin <https://en.wikipedia.org/wiki/Abel–Ruffini_theorem>`_).

Eins er ekki hægt treysta á það að geta fundið nákvæmlega núllstöðvar almennra falla með því 
að nota þekkingu okkar á algebru og stærðfræðigreinginu. Hverjar (og hversu margar) eru t.d. núllstöðvar

.. math::
    e^x + x^3?
    
Aðferðirnar í þessum kafla ganga út á að finna nálgun á núllstöðvum falla og í sumum tilvikum
hjálpa þær okkur einnig að sýna fram á tilvist núllstöðva (sem er ekki alltaf sjálfgefin).
    
    
Helmingunaraðferð 
-----------------

Fyrsta aðferðin til að finna núllstöðvar sem við skoðum kallast
helmingunaraðferð (e. bisection method).

Milligildissetningin
~~~~~~~~~~~~~~~~~~~~

Ef :math:`f` er samfellt á :math:`[a,b]` og :math:`y` er einhver
tala á milli :math:`f(a)` og :math:`f(b)`, þá er til :math:`c`
þannig að :math:`a < c < b` og :math:`f(c) = y`.

   
Afleiðing
~~~~~~~~~

Svo ef við höfum :math:`a` og :math:`b` þannig að :math:`a < b` og
þannig að :math:`f(a)` og :math:`f(b)` hafi ólík formerki, þá hefur
:math:`f` núllstöð :math:`p` á bilinu :math:`[a,b]`.

.. index::
    helmingunaraðferð


Notum okkur þetta til þess að finna rætur.

#. Látum :math:`x = \frac 12(a+b)` vera miðpunkt :math:`[a,b]`.

#. Reiknum :math:`f(x)`, þá geta þrjú tilvik komið upp:

   #. :math:`f(x) = 0` og leitinni að rót er lokið.

   #. :math:`f(a)` og :math:`f(x)` hafa sama formerki, þannig að við
      leitum að rót á bilinu :math:`[x,b]`.

   #. :math:`f(x)` og :math:`f(b)` hafa sama formerki, þannig að við
      leitum að rót á bilinu :math:`[a,x]`.

Í tilviki (ii) segir milligildissetningin að :math:`f` hafi rót á bilinu
:math:`[x,b]`, og í tilviki (iii) er rótin á bilinu :math:`[a,x]`. Þá
getum við farið aftur í skref 1, nema með helmingi minna bil en áður.

Með því að ítreka þetta ferli :math:`n` sinnum fáum við minnkandi runu
af bilum

.. math:: 
    [a,b]=[a_1,b_1]\supset [a_2,b_2]\supset \cdots\supset [a_n,b_n].

Billengdin helmingast í hverju skrefi og milligildissetningin segir okkur að það sé núllstöð á öllum bilunum.

Rununa af bilunum

.. math:: 
    [a,b]= [a_1,b_1]\supset \cdots\supset [a_n,b_n]\supset \cdots

skilgreinum við með ítrun og notum til þess rununa :math:`x_n=\frac 12(a_n+b_n)`.

Setjum :math:`a_0=a`, :math:`b_0=b`, og :math:`x_0=\frac 12(a+b)`.

Gefið er :math:`x_0,\dots,x_n`. Reiknum :math:`f(x_n)`.

#. Ef :math:`f(x_n) = 0`, þá er núllstöð fundin og við hættum.

#. Ef :math:`f(x_n)` og :math:`f(a_n)` hafa sama formerki, þá setjum við :math:`a_{n+1}=x_n`, :math:`b_{n+1}=b_n`, og  :math:`x_{n+1}=\frac 12(a_{n+1}+b_{n+1})`

#. annars setjum við :math:`a_{n+1}=a_n`, :math:`b_{n+1}=x_n` og :math:`x_{n+1}=\frac 12(a_{n+1}+b_{n+1})`.   

    
Skekkjumat í helmingunaraðferð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef við látum miðpunktinn :math:`p_n=\frac 12(a_n+b_n)` vera
nálgunargildi okkar fyrir núllstöð fallsins :math:`f` í bilinu
:math:`[a_n,b_n]`, þá er skekkjan í nálguninni

.. math:: e_n=p-p_n

og við höfum skekkjumatið

.. math::
    |e_n|\leq  \dfrac{b_n - a_n}{2}\ 
    = \frac{b_{n-1}-a_{n-1}}{2^2} = \ldots = \dfrac{b_1-a_1}{2^{n}},

það er

.. math:: 
    |e_n| < \dfrac{b-a}{2^{n}}.

Fyrirframmat á skekkju
~~~~~~~~~~~~~~~~~~~~~~

Nú er auðvelt að meta hversu margar ítrekanir þarf að framkvæma til þess
að nálgunin lendi innan gefinna skekkjumarka.

Ef :math:`\varepsilon>0` er gefið og við viljum að
:math:`|e_n|< \varepsilon`, þá dugir að

.. math:: 
    |e_n|\leq \dfrac{b-a}{2^{n}} <\varepsilon.

Seinni ójafnan jafngildir því að

.. math:: 
    n>\dfrac{\ln\big((b-a)/\varepsilon\big)}{\ln 2}.

    
.. sagecell::
    :auto: 
    :hidecode:  
    :codefile: bisection.sage
    :img: bisection.png
    :imgwidth: 8 cm

.. index::
	fastapunktsaðferð
	fastapunktur

Fastapunktsaðferð 
-----------------

Næsta aðferð sem við skoðum kallast fastapunktsaðferð (e. fixed point method) og
er til að finna fastapunkta en ekki núllstöðvar. Það er hins vegar hægt að 
nota hana til þess að finna núllstöðvar, sjá athugasemd hér að :ref:`neðan <fastapunktar-nullstodvar>`.

Skilgreining
~~~~~~~~~~~~

Látum :math:`f : [a,b] \to \mathbb R` vera samfellt fall. Punktur
:math:`r \in [a,b]` þannig að

.. math:: f(r) = r

kallast *fastapunktur* fallsins :math:`f`.

.. note::
	Athugum að í fastapunktum skerast graf fallsins :math:`y=f(x)` og línan
	:math:`y=x`. Verkefnið að ákvarða fastapunkta fallsins :math:`r` er því
	jafngilt því að athuga hvar graf :math:`f` sker línuna :math:`y=x`.

.. _fastapunktar-nullstodvar:

Tenging við núllstöðvar
~~~~~~~~~~~~~~~~~~~~~~~

Verkefnið að finna fastapunkta fallsins :math:`g(x)` er jafngilt því að
finna núllstöðvar fallsins :math:`f(x)=g(x)-x`.

Þannig að ef við viljum t.d. finna núllstöð :math:`f(x) = e^x + x^3` þá er nóg að finna fastapunkt
fallsins :math:`g(x) = e^x + x^3 + x`.

Reiknirit
~~~~~~~~~

**Byrjunarskref:**	Valin er tala :math:`x_0\in [a,b]`.

**Ítrunarskref:**	Ef :math:`x_0,\dots,x_n` hafa verið valin, þá setjum við
	
	.. math:: x_{n+1}=f(x_n)

.. note::
	Til þess að þetta sé vel skilgreind runa, þá verðum við að gera ráð
	fyrir að :math:`f(x)\in [a,b]` fyrir öll :math:`x\in [a,b]`. Þetta
	skilyrði er einnig skrifað

	.. math:: f([a,b])\subset [a,b].

.. note::
	Ef :math:`f` er samfellt og runan er samleitin með markgildið :math:`r`, þá er
	
	.. math::
	   r=\lim_{n\to \infty}x_{n+1}=\lim_{n\to \infty}f(x_{n})
	   =f(\lim_{n\to \infty}x_{n})=f(r).

	Þetta segir okkur að *ef* við getum séð til þess að runan verði
	samleitin, þá er markgildið fastapunktur.

.. index::
	herping

Skilgreining: Herping
~~~~~~~~~~~~~~~~~~~~~

Fall :math:`f:[a,b]\to {\mathbb  R}` er sagt vera *herping* ef til er
fasti :math:`\lambda\in [0,1[` þannig að

.. math:: |f(x)-f(y)|\leq \lambda|x-y| \qquad \text{ fyrir öll } x,y\in [a,b].

.. note::
	Sérhver herping er samfellt fall.

Setning
~~~~~~~

Ef :math:`f` er deildanlegt fall á :math:`]a,b[`, þá gefur
meðalgildissetningin okkur til er :math:`\xi` milli :math:`x` og
:math:`y` þannig að

.. math:: f(x)-f(y)=f'(\xi)(x-y).

Ef til er :math:`\lambda\in[0,1[` þannig að :math:`|f'(x)|\leq \lambda`
fyrir öll :math:`x\in [a,b]`, þá er greinilegt að :math:`f` er herping.

.. index::
	fastapunktsaðferð; fastapunktssetningin

Fastapunktssetningin
~~~~~~~~~~~~~~~~~~~~

Látum :math:`f : [a,b] \to [a,b]` vera herpingu. Þá hefur :math:`f`
nákvæmlega einn fastapunkt :math:`r` á bilinu :math:`[a,b]` og runan
:math:`(x_n)` þar sem

.. math::
   \begin{aligned}
     x_0 &\in [a,b] \quad \text{ getur verið hvaða tala sem er  og } \\
     x_{n+1} &= f(x_n), \quad n \geq 0,\end{aligned}

stefnir á fastapunktinn.

.. begin-toggle::
	:label: Sönnun

Sönnunina brjótum við upp í nokkur skref.

**1. skref, herping hefur í mesta lagi einn fastapunkt**

Sönnum þetta með mótsögn.

Gerum ráð fyrir að :math:`r` og :math:`s` séu tveir ólíkir fastapunktar
á :math:`[a,b]`. Þá er

.. math::
   |r - s| = |f(r) - f(s)|
     \leq \lambda |r - s| < |r - s|

því :math:`\lambda < 1`. Þetta fær ekki staðist, þannig að fjöldi
fastapunkta er í mesta lagi einn

**2. skref, fallið** :math:`f` **hefur fastapunkt:**

Látum :math:`g(x) = f(x) - x`, þá eru núllstöðvar :math:`g` nákvæmlega
fastapunktar :math:`f`.

Þar sem :math:`a \leq f(x) \leq b` fyrir öll :math:`x \in [a,b]` er

.. math::
   \left\{ \begin{array}{c}
         g(a) = f(a) - a \geq 0 \\
         g(b) = f(b) - b \leq 0
     \end{array} \right.

Ef annað hvort :math:`g(a) = 0` eða :math:`g(b) = 0` höfum við fundið
fastapunkt fallsins :math:`f` og við getum hætt.

Ef hins vegar :math:`g(a) > 0` og :math:`g(b) < 0` þá hefur :math:`g`
ólík formerki í endapunktum bilsins :math:`[a,b]` og hefur því núllstöð
:math:`r` á bilinu skv. milligildissetninguninni. Þá er :math:`r`
jafnframt fastapunktur :math:`f`.

Skref 1 og 2 sýna því að fallið :math:`f` hefur nákvæmlega einn
fastapunkt á bilinu.

**3. skref, runan** :math:`(x_n)` **er samleitin**

Látum :math:`r` vera ótvírætt ákvarðaða fastapunktinn á :math:`[a,b]`.

Við notfærum okkur að :math:`f` er herping og að :math:`r` er
fastapunktur :math:`f`, þá fæst að fyrir sérhvert
:math:`k\in {\mathbb  N}` þá er

.. math:: |r - x_k| = |f(r) - f(x_{k-1})|  \leq \lambda |r - x_{k-1}|

það er :math:`|r - x_k| \leq \lambda |r - x_{k-1}|`.

Með því að nota þetta :math:`n`-sinnum þá fæst að

.. math::
    \begin{aligned}
        |r - x_n|   &\leq \lambda |r - x_{n-1}| & (k=n)\\
        &\leq \lambda^2 |r - x_{n-2}| & (k=n-1)\\
        &\vdots & \vdots\\
        &\leq \lambda^n |r - x_0| & (k=1).
    \end{aligned}

Þar sem :math:`\lambda < 1` er því

.. math::
    \lim\limits_{n \to +\infty} |r - x_n|
    \leq \lim\limits_{n \to +\infty} \lambda^n |r - x_0|
    = 0,

það er runan :math:`x_n` stefnir á :math:`r`.

.. end-toggle::

Fastapunktsaðferð er að minnsta kosti línulega samleitin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Af skilgreiningunni á rununni :math:`x_n` leiðir beint að

.. math:: |e_{n+1}|=|r-x_{n+1}|=|f(r)-f(x_n)|\leq \lambda|r-x_n|=\lambda|e_n|

sem segir okkur að fastapunktsaðferð sé að minnsta kosti línulega
samleitin ef :math:`f` er herping.

.. sagecell::
    :auto: 
    :hidecode:  
    :codefile: fixedpoint.sage
    :img: fixedpoint.png
    :imgwidth: 8 cm 


.. index::
	sniðilsaðferð

Sniðilsaðferð
-------------

Næst er aðferð til að finna núllstöðvar sem kallast *sniðilsaðferð* 
(e. `secant method <https://en.wikipedia.org/wiki/Secant_method>`_)

Gefið er fallið :math:`f:[a,b]\to {\mathbb  R}`. Við ætlum að ákvarða
núllstöð :math:`f`, þ.e.a.s. :math:`p\in [a,b]` þannig að

.. math:: f(p)=0.

\ Rifjum upp að *sniðill* við graf :math:`f` gegnum punktana
:math:`(\alpha,f(\alpha))` og :math:`(\beta,f(\beta))` er gefinn með
jöfnunni

.. math:: y=f(\alpha)+f[\alpha,\beta](x-\alpha)

þar sem hallatalan er

.. math::
   f[\alpha,\beta]=\dfrac{f(\beta)-f(\alpha)}{\beta-\alpha}
   =\dfrac{f(\alpha)-f(\beta)}{\alpha -\beta}.

Sniðillinn sker :math:`x`-ásinn í punkti :math:`s` þar sem

.. math::
   0=f(\alpha)+f[\alpha,\beta](s-\alpha) \quad  \text{sem jafngildir því að } \quad
   s=\alpha-\dfrac{f(\alpha)}{f[\alpha,\beta]}.

Reiknirit
~~~~~~~~~

**Byrjunarskref:** Giskað er á tvö gildi :math:`x_0` og :math:`x_1`.

**Ítrunarskref:** Fyrir :math:`n>1` þá er punkturinn :math:`x_{n+1}` 
skilgreindur sem skurðpunktur sniðilsins gegnum :math:`(x_{n-1},f(x_{n-1}))` og
:math:`(x_n,f(x_n))` við :math:`x`-ás, þ.e.

.. math:: x_{n+1}=x_n-\dfrac{f(x_n)}{f[x_n,x_{n-1}]}.

Samleitin runa stefnir á núllstöð :math:`f`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gefum okkur að runan :math:`(x_n)` sé samleitin að markgildinu
:math:`r`. Meðalgildissetningin segir okkur þá að til sé punktur
:math:`\eta_n` á milli :math:`x_{n-1}` og :math:`x_n` þannig að

.. math:: f[x_n,x_{n-1}]=f'(\eta_n),

og greinilegt er að :math:`\eta_n\to r`.

Við fáum því

.. math::
   r=\lim_{n\to \infty}x_{n+1}=\lim_{n\to \infty}
   \bigg(x_n-\dfrac{f(x_n)}{f'(\eta_n)}\bigg) =r-\dfrac{f(r)}{f'(r)}

Þessi jafna jafngildir því að :math:`f(r)=0`.

Skekkjumat í nálgun á :math:`f(x)` með :math:`p_n(x)`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sniðilinn sem við notum er graf 1. stigs margliðunnar

.. math::
   p_n(x) = f(x_n) + 
           \dfrac{f(x_{n-1})-f(x_n)}{x_{n-1}-x_n}(x-x_n)
           = f(x_n) + f[x_n,x_{n-1}](x-x_n)

Samkvæmt skilgreiningu er :math:`p_n(x_{n+1}) = 0` svo :math:`x_{n+1}`
uppfyllir jöfnuna

.. math:: x_{n+1} = x_n - \frac{f(x_n)}{f[x_n,x_{n-1}]}.

Við þurfum að vita hver skekkjan er á því að nálga :math:`f(x)` með
:math:`p_n(x)`.

Niðurstaðan er að fyrir sérhvert :math:`x \in [a,b]` er til
:math:`\xi_n` sem liggur í minnsta bilinu sem inniheldur :math:`x`,
:math:`x_n` og :math:`x_{n-1}` þannig að

.. math:: f(x) - p_n(x) = \frac{1}{2}f''(\xi_n)(x-x_n)(x-x_{n-1})

.. begin-toggle::
	:label: Sönnun

Ljóst er að matið gildir ef :math:`x=x_{n-1}` eða :math:`x=x_n`.

Festum því punktinn :math:`x` og gerum ráð fyrir að :math:`x\neq x_1` og
:math:`x\neq x_n`.

Skilgreinum fallið

.. math:: g(t)=f(t)-p_n(t)-\lambda(t-x_n)(t-x_{n-1})

þar sem :math:`\lambda` er valið þannig að :math:`g(x)=0`.

Látum nú :math:`\alpha<\beta<\gamma` vera uppröðun á punktunum
:math:`x_{n-1}`, :math:`x_n` og :math:`x`.

Fallið

.. math:: g(t)=f(t)-p_n(t)-\lambda(t-x_n)(t-x_{n-1})

hefur núllstöð í öllum punktunum þremur.

Meðalgildissetningin gefur þá að :math:`g'(t)` hefur eina núllstöð í
punkti á bilinu :math:`]\alpha,\beta[` og aðra í :math:`]\beta,\gamma[`.

Af því leiðir aftur að :math:`g''(t)` hefur núllstöð, :math:`\xi_n`, í
:math:`[\alpha,\gamma]`, sem er minnsta bilið sem inniheldur alla
punktana :math:`x_{n-1}`, :math:`x_n` og :math:`x`.

Af þessu leiðir

.. math::

   0=g''(\xi_n)=f''(\xi_n)-2\lambda \quad \text{þþaa} \quad
   \lambda=\tfrac 12 f''(\xi_n).

Nú var :math:`\lambda` upprunalega valið þannig að :math:`g(x)=0`. Þar
með er

.. math:: f(x) - p_n(x) = \frac{1}{2}f''(\xi_n)(x-x_n)(x-x_{n-1}).

.. end-toggle::

Skekkjumat í sniðilsaðferð
~~~~~~~~~~~~~~~~~~~~~~~~~~

Skoðum hvað af þessu leiðir:

Nú er :math:`f(r) = 0` og því

.. math:: -p_n(r) = \frac{1}{2}f''(\xi_n)e_n\cdot e_{n-1}.

Eins er

.. math:: -p_n(r) = -f[x_n,x_{n-1}]e_{n+1}=-f'(\eta_n)e_{n+1},

þar sem :math:`\eta_n` fæst úr meðalgildissetningunni og liggur á milli
:math:`x_n` og :math:`x_{n+1}`. Niðurstaðan verður því

.. math::

   e_{n+1} = \frac{-\frac{1}{2}f''(\xi_n)}
           {f[x_n, x_{n+1}]}   
       e_ne_{n-1} = \frac{-\frac{1}{2}f''(\xi_n)}
           {f'(\eta_n)}e_ne_{n-1}

það er

.. math::

   \lim_{n\to \infty}\dfrac{e_{n+1}}{e_ne_{n-1}}=
   \lim_{n \to \infty} \frac{-\frac{1}{2}f''(\xi_n)}
           {f'(\eta_n)}
   =
   \frac{-\frac{1}{2}f''(r)}
           {f'(r)}.

Setning
~~~~~~~

Ef sniðilsaðferð er samleitin, :math:`f\in C^2([a,b])` (tvisvar
diffranlegt) og :math:`f'(r)\neq 0`, þá er sniðilsaðferðin ofurlínuleg.

.. begin-toggle::
	:label: Sönnun

.. math::

   \lim_{n\to \infty}\dfrac{|e_{n+1}|}{|e_n|} =
   \lim_{n\to \infty}\dfrac{|e_{n+1}e_{n-1}|}{|e_ne_{n-1}|}=
   \lim_{n \to \infty} \frac{|e_{n-1}\frac{1}{2}f''(r)|}
           {|f'(r)|} = 0

.. end-toggle::


Raunar þá er sniðilsaðferðin samleitin af stigi
:math:`\alpha = (1+\sqrt 5)/2 \approx 1,618` og með
:math:`\lambda = \left(\frac{f''(r)}{2f'(r)}\right)^{\alpha -1}`.

.. index::
	aðferð Newtons
	snertill

Aðferð Newtons
--------------

Í sniðilsaðferðinni létum við :math:`x_{n+1}` vera skurðpunkt sniðils
gegnum :math:`(x_{n-1},f(x_{n-1}))` og :math:`(x_n,f(x_n))` við
:math:`x`-ás og fengum við rakningarformúluna

.. math:: x_{n+1} = x_n - \frac{f(x_n)}{f[x_n,x_{n-1}]}.

Aðferð Newtons er nánast eins, nema í stað sniðils tökum við snertil í
punktinum :math:`(x_n,f(x_n))`.

Rakningarformúlan er eins, nema hallatalan verður :math:`f'(x_n)` í stað
:math:`f[x_n,x_{n-1}]`

Reiknirit
~~~~~~~~~

**Byrjunarskref:** Giskað er á eitt gildi :math:`x_0`.

**Ítrunarskref:** Gefin eru :math:`x_0,\dots,x_n`. Punkturinn :math:`x_{n+1}` er
skurðpunktur snertils gegnum :math:`(x_n,f(x_n))` við :math:`x`-ás,

.. math:: x_{n+1}=x_n-\dfrac{f(x_n)}{f'(x_n)}.

Upprifjun
~~~~~~~~~

Munum að snertill við graf :math:`f` í punktinum :math:`x_n` er

.. math:: y=f(x_n) + f'(x_n)(x-x_n),

þessi lína sker :math:`x`-ásinn (:math:`y=0`) þegar
:math:`x=x_n - \frac{f(x_n)}{f'(x_n)}`.

Samleitin runa stefnir á núllstöð :math:`f`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gefum okkur að runan :math:`(x_n)` sé samleitin með markgildið
:math:`r`. Við fáum því

.. math::

   r=\lim_{n\to \infty}x_{n+1}=\lim_{n\to \infty}
   \bigg(x_n-\dfrac{f(x_n)}{f'(x_n)}\bigg) =r-\dfrac{f(r)}{f'(r)}

Þessi jafna jafngildir því að :math:`f(r)=0`.

Þannig að ef runan er samleitin þá fáum við núllstöð.

Skekkjumat í nálgun á :math:`f(x)` með :math:`p_n(x)`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Snertillinn við :math:`f` í punktinum :math:`x_n` er 1. stigs margliðan

.. math:: p_n(x) = f(x_n) + f'(x_n)(x-x_n)

Samkvæmt skilgreiningu er :math:`p_n(x_{n+1}) = 0` svo :math:`x_{n+1}`
uppfyllir jöfnuna

.. math:: x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}.

Athugum að :math:`p_n` er fyrsta Taylor nálgunin við fallið :math:`f`
kringum :math:`x_n`. Setning Taylors gefur að til er :math:`\xi_n` sem
liggur á milli :math:`r` og :math:`x_n` þannig að

.. math:: f(r) - p_n(r) = \frac{1}{2}f''(\xi_n)(r-x_n)^2.

Skekkjumat í aðferð Newtons
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú er :math:`f(r) = 0` og því

.. math:: -p_n(r) = \frac{1}{2}f''(\xi_n)e_n^2.

Eins er fæst af skilgreiningunni á :math:`p_n` að

.. math:: -p_n(r) = -f'(x_n)e_{n+1}

Niðurstaðan verður því

.. math::

   e_{n+1} = \frac{-\frac{1}{2}f''(\xi_n)}
           {f'(x_n)}e_n^2

.. sagecell::
	:auto:
	:hidecode:
	:codefile: newton.sage
	:img: newton.png
	:imgwidth: 8 cm


Setning
~~~~~~~

Ef aðferð Newtons fyrir fallið :math:`f` er samleitin,
:math:`f\in C^2([a,b])` og :math:`f'(r)\neq 0`, þá fáum við:

.. math::

   \lim_{n\to \infty}\dfrac{e_{n+1}}{e_n^2}=\frac{-\frac{1}{2}f''(r)}
           {f'(r)}

Það þýðir að aðferð Newtons er ferningssamleitin.

.. begin-toggle::
	:label: Sönnun

.. math::

   \lim_{n\to \infty}\dfrac{e_{n+1}}{e_n^2}=
   \lim_{n\to \infty}\frac{-\frac{1}{2}f''(\xi_n)}{f'(x_n)} =
   \frac{-\frac{1}{2}f''(r)}{f'(r)}

.. end-toggle::

.. note:: 
	Athugið að það er ekki sjálfgefið að aðferð Newtons sé samleitin.
	
	Auðvelt er að finna dæmi þar sem vond upphafságiskun :math:`x_0` skilar
	runu sem er ekki samleitin.

Samanburður á aðferðum
----------------------

+-------------------------------------------------------------------------------------+-----------------------------+-------------------------------------------------+
| Aðferð                                                                              | Samleitni                   | Stig samleitni                                  |
+=====================================================================================+=============================+=================================================+
| `Helmingunaraðferð`_                                                                | Já, ef :math:`f(a)f(b)<0`   | 1, línuleg                                      |
+                                                                                     +                             +                                                 +
| (e. `bisection method <https://en.wikipedia.org/wiki/Bisection_method>`_)           |                             |                                                 |
+-------------------------------------------------------------------------------------+-----------------------------+-------------------------------------------------+
| `Fastapunktsaðferð`_                                                                | Ekki alltaf. En saml.       | amk 1                                           |
+                                                                                     +                             +                                                 +
| (e. `fixed point iteration <https://en.wikipedia.org/wiki/Fixed-point_iteration>`_) | ef :math:`f` er herping     |                                                 |
+-------------------------------------------------------------------------------------+-----------------------------+-------------------------------------------------+
| `Sniðilsaðferð`_                                                                    | Ekki alltaf                 | :math:`\approx 1,618`, ef :math:`f'(r)\neq 0`   |
+                                                                                     +                             +                                                 +
| (e. `secant method <https://en.wikipedia.org/wiki/Secant_method>`_)                 |                             |                                                 |
+-------------------------------------------------------------------------------------+-----------------------------+-------------------------------------------------+
| `Aðferð Newtons`_                                                                   | Ekki alltaf                 | 2, ef :math:`f'(r)\neq 0`                       |
+                                                                                     +                             +                                                 +
| (e. `Newtons method <https://en.wikipedia.org/wiki/Newton%27s_method>`_)            |                             |                                                 |
+-------------------------------------------------------------------------------------+-----------------------------+-------------------------------------------------+

.. warning::
	Þó að aðferð Newtons sé samleitin af stigi 2, en sniðilsaðferðin af
	stigi u.þ.b. 1,618, þá er í vissum tilfellum hagkvæmara að nota
	sniðilsaðferðina ef það er erfitt að reikna gildin á afleiðunni
	:math:`f'`.