Leifareikningur
===============

*Big flashy things have my name written all over them. Well... not yet, give me time and a crayon.*

\- The Doctor, Doctor Who


Laurent-raðir og sérstöðupunktar
--------------------------------

Skilgreining (Sjá §4.1) 
~~~~~~~~~~~~~~~~~~~~~~~

Mengi af gerðinni

.. math::

   A(\alpha,\varrho_1,\varrho_2)=\{z\in {\mathbb{C}}\mid
   \varrho_1<|z-\alpha|<\varrho_2\}

þar sem :math:`0\leq\varrho_1<\varrho_2\leq +\infty` kallast opinn hringkragi með miðju í :math:`\alpha`, innri geisla :math:`\varrho_1`, og ytri geisla :math:`\varrho_2`.

Setning  (Sjá Setningu 4.1.1) (Laurent) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`X` vera opið hlutmengi af :math:`{\mathbb{C}}` og gerum ráð fyrir að :math:`A(\alpha,\varrho_1,\varrho_2)\subset X`. Ef :math:`f\in {\cal O}(X)`, þá er unnt að skrifa :math:`f` sem

.. math::

   f(z)=\sum_{n=-\infty}^{+\infty}a_n(z-\alpha)^ n, \qquad z\in
   A(\alpha,\varrho_1,\varrho_2),

stuðlar raðarinnar :math:`a_n` eru gefnir með formúlunni

.. math::

   a_n=\dfrac 1{2\pi i}\int_{\partial S(\alpha,r)} \dfrac{f(\zeta)}
   {(\zeta-\alpha)^{n+1}} \, d\zeta,

og :math:`r` getur verið hvaða tala sem er á bilinu
:math:`]\varrho_1,\varrho_2[`. Röðin

.. math::

 
    \sum_{n=0}^{+\infty}a_n(z-\alpha)^ n

er samleitin ef :math:`|z-\alpha|<\varrho_2` og röðin

.. math::

 \sum_{n=-\infty}^{-1}a_n(z-\alpha)^ n

er samleitin ef :math:`|z-\alpha|>\varrho_1`. Báðar raðir eru
samleitnar á opna hringkraganum :math:`A(\alpha,\varrho_1, \varrho_2)`.

Skilgreining (Sjá Skilgreiningu 4.1.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Röð af gerðinni

.. math::

 
    \sum_{-\infty}^{+\infty}a_n(z-\alpha)^ n

kallast Laurent-röð. Innri samleitnigeisli raðarinnar :math:`\varrho_1` er skilgreindur sem neðra mark yfir :math:`\varrho=|z-\alpha|` þannig að

.. math::

    \sum_{-\infty}^{-1} a_n(z-{\alpha})^ n

er samleitin, ytri samleitnigeisli raðarinnar :math:`\varrho_2` er skilgreindur sem efra mark yfir öll :math:`\varrho=|z-\alpha|` þannig að

.. math::

    \sum_{n=0}^{+\infty}a_n(z-{\alpha})^ n

er samleitin. Ef :math:`\varrho_1<\varrho_2` þá segjum við að Laurent-röðin sé samleitin.

Skilgreining (Sjá §4.2)
~~~~~~~~~~~~~~~~~~~~~~~

Gefin er Laurent-röð

.. math::

 
    \sum_{-\infty}^{+\infty}a_n(z-\alpha)^ n

fyrir fágað fall :math:`f`. Stuðullinn :math:`a_{-1}` kallast leif Laurent-raðarinnar eða leif :math:`f` í :math:`\alpha` og er táknaður :math:`\operatorname{Res}(f,\alpha)` og röðin

.. math::

 
    \sum_{n=-\infty}^{-1}a_n(z-{\alpha})^ n

kallast höfuðhluti Laurent-raðarinnar eða höfuðhluti fallsins :math:`f` í punktinum :math:`\alpha`.

Skilgreining  (Sjá §4.2)
~~~~~~~~~~~~~~~~~~~~~~~~

Punktur :math:`\alpha` í mengi :math:`A` kallast einangraður punktur í :math:`A` ef til er opin hringskífa með miðju í :math:`\alpha` sem inniheldur engan punkt úr :math:`A` nema :math:`\alpha`.

Látum :math:`f\in{\cal O}(X)`. Ef :math:`\alpha\in\mathbb{C}\setminus X` er einangraður punktur í :math:`A=\mathbb{C}\setminus X` þá nefnist :math:`\alpha` einangraður sérstöðupunktur :math:`f`.

  

Skilgreining (Sjá §4.2)
~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`\alpha` vera einangraðan sérstöðupunkt fyrir fágað fall :math:`f`. Ritum Laurent-röð :math:`f` í :math:`\alpha` sem

.. math::

 \sum_{-\infty}^{+\infty}a_n(z-\alpha)^ n.

(i) :math:`\alpha` er sagður afmáanlegur sérstöðupunktur ef höfuðhluti Laurent-raðarinnar er :math:`0`, þ.e.a.s. \ :math:`a_n=0` fyrir öll :math:`n\leq -1`. 

(ii) :math:`\alpha` er sagt vera skaut ef höfuðhluti Laurent-raðarinnar er endanlegur en ekki 0. Skautið er sagt hafa stig :math:`m` ef :math:`a_{-m}\neq 0` en :math:`a_n=0` fyrir öll :math:`n<-m`. 

(iii) :math:`\alpha` er sagt vera verulegur sérstöðupunktur ef höfuðhluti Laurent-raðarinnar er óendanlegur.

   

Setning (Sjá §4.2 og Setningu 4.2.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Einangraður sérstöðupunktur :math:`{\alpha}` fágaða fallsins :math:`f` sem skilgreint er á opnu mengi :math:`X` er afmáanlegur ef og aðeins ef til er :math:`r>0` og :math:`g\in {\cal O}(S({\alpha},r))` þannig að :math:`S^*({\alpha},r)\subset X` og :math:`f(z)=g(z)` fyrir öll :math:`z\in S^*({\alpha},r)`.

Setning Riemanns.
~~~~~~~~~~~~~~~~~

Ef :math:`\alpha` er einangraður sérstöðupunktur
fágaða fallsins :math:`f`, og
:math:`\lim_{z\to \alpha}(z-\alpha)f(z)= 0`, þá er :math:`\alpha`
afmáanlegur sérstöðupunktur.

   

Setning (Sjá §4.2)
~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera fágað fall á opnu mengi :math:`X` og :math:`\alpha` vera einangraðan sérstöðupunkt fallsins :math:`f`. Sérstöðupunkturinn :math:`\alpha` er skaut af stigi :math:`m>0`, ef og aðeins ef til er fágað fall :math:`g\in {\cal O}(U)`, þar sem :math:`U` er grennd um :math:`\alpha`, þannig að :math:`g(\alpha)\neq 0` og 

.. math::

 f(z)=\dfrac{g(z)}{(z-\alpha)^ m}, \qquad z\in U\setminus\{\alpha\}.

Setning 
~~~~~~~

Fall :math:`f` hefur skaut í :math:`\alpha` ef og
aðeins ef :math:`|f(z)|\to +\infty` þegar :math:`z\to \alpha`.
   

Setning (Stóra Picard-setningin.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`\alpha` er verulegur sérstöðupunktur fágaðs falls :math:`f` þá gildir að fyrir sérhvert :math:`\delta>0` að mengið

.. math::

 f(S^*(\alpha, \delta))=\{f(z)\mid z\in S^*(\alpha, \delta)\}

er annaðhvort allt :math:`{\mathbb{C}}` eða til jafnt og :math:`{\mathbb{C}}\setminus\{z_0\}` þar sem :math:`z_0` er einhver föst tvinntala.

   
Setning (Sjá §4.4, jöfnur 4.4.3 og 4.4.4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera fágað fall og :math:`\alpha` skaut :math:`f`.

(i) Ef skautið er einfalt (af stigi 1) þá er

.. math::

 \operatorname{Res}(f,\alpha)=\lim_{z\to \alpha}(z-\alpha)f(z).

(ii) Ef skautið er af stigi :math:`m` og við ritum :math:`f(z)=g(z)/(z-\alpha)^m` þannig að :math:`g(\alpha)\neq 0` þá er

.. math::

 \operatorname{Res}(f,\alpha)=\dfrac{g^{(m-1)}(\alpha)}{(m-1)!}.

Leifasetningin
--------------

Leifasetningin (Sjá Setningu 4.3.1)  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`X` vera opið hlutmengi í :math:`{\mathbb{C}}` og látum :math:`\Omega` vera opið hlutmengi af :math:`X` sem uppfyllir sömu forsendur og í Cauchy-setningunni. Látum :math:`A` vera dreift hlutmengi af :math:`X` sem sker ekki jaðarinn :math:`\partial\Omega` á :math:`\Omega`. Ef :math:`f\in {\cal O}(X\setminus A)`, þá er

.. math::
	
	
   \int_{\partial\Omega}f(z)\, dz = 2\pi i \sum_{\alpha\in \Omega\cap A}
   \operatorname{Res}(f,\alpha).

(Sjá §4.4, jöfnur 4.4.3 og 4.4.4) Látum :math:`f` vera fágað fall og :math:`\alpha` skaut :math:`f`.

(i) Ef skautið er einfalt (af stigi 1) þá er

.. math::

 \operatorname{Res}(f,\alpha)=\lim_{z\to \alpha}(z-\alpha)f(z).

(ii) Ef skautið er af stigi :math:`m` og við ritum :math:`f(z)=g(z)/(z-\alpha)^m` fyrir :math:`z` í gataðri grennd um :math:`\alpha` þannig að :math:`g(\alpha)\neq 0` þá er

.. math::

 \operatorname{Res}(f,\alpha)=\dfrac{g^{(m-1)}(\alpha)}{(m-1)!}.

  

Setning (Sjá §4.4, jöfnur 4.4.6 og 4.4.7)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`f(z)=g(z)/h(z)` í grennd við punkt :math:`\alpha` þar sem :math:`g(\alpha)\neq 0` og :math:`\alpha` er :math:`m`-föld núllstöð fallsins :math:`h` og :math:`h(z)=(z-\alpha)^mh_1(z)` þar sem :math:`h_1(\alpha)\neq 0`. Þá er :math:`f` með skaut af stigi :math:`m` í :math:`\alpha`.

Ef :math:`m=1` þá er

.. math::

 \operatorname{Res}(f,\alpha)=\frac{g(\alpha)}{h'(\alpha)}.

Ef :math:`m>1` þá er

.. math::

   \operatorname{Res}(f,\alpha)=\dfrac 1{(m-1)!}\cdot
   \left.\dfrac {d^{m-1}}{dz^{m-1}}\bigg(\dfrac
   {g(z)}{h_1(z)}\bigg)\right|_{z=\alpha}. \label{11.1.7}

Setning (Sjá §4.5)
~~~~~~~~~~~~~~~~~~

Látum :math:`f(x,y)` vera fall af tveimur breytum sem er skilgreint á opnu mengi sem inniheldur einingarhringinn :math:`x^2+y^2=1`. Gerum ráð fyrir að til sé dreift mengi :math:`A` sem inniheldur enga punkta úr einingarhringnum :math:`\partial S(0,1)` og opið mengi :math:`X` sem inniheldur :math:`\overline{S}(0,1)` þannig að fallið

.. math::

 g(z)=f\left(\frac{z^2+1}{2z}, \frac{z^2-1}{2iz}\right)\frac{1}{iz}

sé fágað á :math:`X\setminus A`. Þá er

.. math::
	
	
   \int_0^{2\pi}f(\cos\theta, \sin\theta)\,d\theta
   =\int_{\partial S(0,1)}g(z)\,dz\\
   = 2\pi i\sum_{\alpha\in A\cap S(0,1)}\operatorname{Res}(g(z),\alpha).

 

Setning (Sjá §4.5) 
~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera fall sem er fágað á menginu :math:`{\mathbb{C}}\setminus A` þar sem :math:`A` er dreift mengi. Gerum ráð fyrir að í menginu :math:`A` séu engar rauntölur. Fyrir rauntölu :math:`r>0` látum við :math:`\gamma_r(\theta)=re^{i\theta}` með :math:`0\leq\theta\leq \pi` vera stikunn á hringboganum í efra hálfplaninu :math:`H_+` frá :math:`r` til :math:`-r`. Ef

.. math::

 \int_{\gamma_r}f(z)\,dz\xrightarrow[r\rightarrow\infty]{} 0

þá er

.. math::

 \int_{-\infty}^\infty f(x)\,dx=2\pi i\sum_{\alpha\in A\cap H_+}\operatorname{Res}(f,\alpha).

  

(Efra hálfplanið :math:`H_+` er mengi allra tvinntalna :math:`z` þannig
að :math:`\operatorname{Im\, } z>0`. Hægt er að setja fram álíka setningu þar sem er
tekinn sá hringbogi sem liggur í neðra hálfplaninu
:math:`H_-=\{z\in {\mathbb{C}}\mid \operatorname{Im\, } z<0\}`.)
