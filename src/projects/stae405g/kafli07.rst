.. index::
	jaðargildisverkefni

Jaðargildisverkefni 
===================

*The pen is mightier than the sword if the sword is very short, and the pen is very sharp.*
-- Terry Pratchett

Inngangur
---------

Jaðargildisverkefni
~~~~~~~~~~~~~~~~~~~

Við ætlum að finna nálgunarlausnir á verkefnum af gerðinni

.. math::

   \begin{gathered}
       y''=f(x,y,y'), \qquad a\leq x\leq b,\\
   \alpha_1y(a)+\alpha_2 y'(a)=\alpha_3,\\
   \beta_1 y(b)+\beta_2y'(b)=\beta_3.  
     \end{gathered}
     
Lausn á verkefninu er þá fall :math:`y(x):[a,b]\to \mathbb R` sem er þannig að :math:`y`
uppfyllir

* afleiðujöfnuna :math:`y''(x) = f(x,y(x),y'(x))`,
* jaðarskilyrðin :math:`\alpha_1y(a)+\alpha_2 y'(a)=\alpha_3` í :math:`x=a` og
* jaðarskilyrðin :math:`\beta_1 y(b)+\beta_2y'(b)=\beta_3` í :math:`x=b`.  


Afleiðujafnan er sögð vera línuleg ef :math:`f` er á forminu

.. math:: y''=p(x)y'+q(x)y+r(x), \qquad x\in [a,b].

.. index::
	jaðargildisverkefni; Dirichlet-jaðarskilyrði
	jaðargildisverkefni; Neumann-jaðarskilyrði
	jaðargildisverkefni; Robin-jaðarskilyrði

Þrjár tegundir jaðarskilyrða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Venjulega eru jaðarskilyrðin flokkuð í þrjá flokka.

+---------+----------------------------+------------------------------------------------+
| (i)     | Dirichlet-jaðarskilyrði:   | :math:`y(a)=\alpha`,    :math:`y(b)=\beta`     |
+         +                            +                                                +
|         | (Fallsjaðarskilyrði:)      |                                                |
+---------+----------------------------+------------------------------------------------+
| (ii)    | Neumann-jaðarskilyrði:     | :math:`y'(a)=\alpha`,    :math:`y'(b)=\beta`   |
+         +                            +                                                +
|         | (Afleiðujaðarskilyrði:)    |                                                |
+         +                            +                                                +
|         | (Flæðisjaðarskilyrði:)     |                                                |
+---------+----------------------------+------------------------------------------------+
| (iii)   | Robin-jaðarskilyrði:       | :math:`\alpha_1y(a)+\alpha_2 y'(a)=\alpha_3`   |
+         +                            +                                                +
|         | (Blandað jaðarskilyrði:)   | :math:`\beta_1 y(b)+\beta_2y'(b)=\beta_3`      |
+         +                            +                                                +
|         |                            | :math:`(\alpha_1,\alpha_2)\neq (0,0)`          |
+---------+----------------------------+------------------------------------------------+

.. note::
    Athugið að Robin jaðarskilyrði með :math:`\alpha_2=0` (eða
    :math:`\beta_2=0`) er Dirichlet skilyrði með :math:`\alpha=\alpha_3/\alpha_1` (eða
    :math:`\beta=\beta_3/\beta_1`).

    Athugið að Robin jaðarskilyrði með :math:`\alpha_1=0` (eða
    :math:`\beta_1=0`)
    er Neumann skilyrði með :math:`\alpha=\alpha_3/\alpha_2` (eða
    :math:`\beta=\beta_3/\beta_2`).

Dirichlet-jaðarskilyrði
-----------------------

.. index::
	jaðargildisverkefni; skiptipunktar

Skiptipunktar
~~~~~~~~~~~~~

Gefum okkur jafna skiptingu á bilinu :math:`[a,b]`, :math:`x_j=a+hj`,
:math:`j=0,\ldots,N` þar sem :math:`h=(b-a)/N`. Þá er

.. math:: a=x_0<x_1<x_2<\cdots<x_{N-1}<x_N=b.

Við nefnum :math:`x_j` *skiptipunkta* skiptingarinnar.

Punktarnir :math:`a=x_0` og :math:`b=x_N` nefnast *endapunktar*
skiptingarinnar og :math:`x_j`, með :math:`j=1,\dots,N-1`, nefnast
*innri punktar* skiptingarinnar.

Við ætlum aðeins að nálga lausnir á línulegum jöfnum

.. math:: y''=p(x)y'+q(x)y+r(x), \qquad x\in [a,b],

Við munum reiknum út nálgun á réttu lausninni :math:`y(x)` í skiptipunktunum :math:`x_j`.
Rétta gildið í punktinum :math:`x_j` táknum við með :math:`y_j` og
nálgunargildið með :math:`w_j`,

.. math:: y_j=y(x_j)\approx w_j.

Eins skrifum við

.. math:: p_j=p(x_j), \qquad q_j=q(x_j), \qquad  r_j=r(x_j).

.. warning::
	Ólíkt upphafsgildisverkefnunum í kaflanum á undan þá táknum við breytuna
	hér með :math:`x` og fallgildið með :math:`y`. Þetta er eðlilegur ritháttur
	hér því í jaðargildisverkefnum þá er :math:`y` oftast fall 
	af staðsetningu en ekki tíma, t.d. hiti í röri, sveigja burðarbita, o.s.fr. 

.. index::
	jaðargildisverkefni; línulegar afleiðujöfnur

Línulegar afleiðujöfnur
~~~~~~~~~~~~~~~~~~~~~~~

Nú leiðum við út nálgunarjöfnur, eina fyrir hvern innri skiptipunkt. Við
byrjum á því að stinga punkti :math:`x_j` inn í afleiðujöfnuna

.. math:: \big\{ y''(x)= p(x)y'(x)+q(x)y(x) + r(x)\big\}_{x=x_j}.

Næst skiptum við afleiðunum :math:`y''` og :math:`y'` út fyrir 
miðsettan mismunakvóta fyrir aðra afleiðuna og
miðsettan mismunakvóta fyrir fyrstu afleiðuna. Þá fæst

.. math::

   \dfrac{y_{j+1}-2y_j+y_{j-1}}{h^2} +O(h^2)
   =p_j\dfrac{y_{j+1}-y_{j-1}}{2h}+q_jy_j+r_j+ O(h^2).

Nú fellum við niður leifaliðina og setjum nálgunargildin í stað réttu
gildanna

.. math::

   \dfrac{w_{j+1}-2w_j+w_{j-1}}{h^2}
   =p_j\dfrac{w_{j+1}-w_{j-1}}{2h}+q_jw_j+r_j

Hér fáum við eina jöfnu fyrir sérhvern innri skiptipunkt
:math:`j=1,\dots,N-1`.

Dirichlet-jaðarskilyrði
~~~~~~~~~~~~~~~~~~~~~~~

Við erum komin með :math:`N-1` nálgunarjöfnu til þess að finna
:math:`N+1` nálgunargildi :math:`w_0,\dots,w_N` fyrir
:math:`y_0,\dots,y_N`.

Ef við erum að leysa línulegt jaðargildisverkefni með
Dirichlet-jaðarskilyrðum,

.. math::

   \begin{gathered}
       y''=p(x)y'+q(x)y+r(x), \qquad a\leq x\leq b,\\
   y(a)=\alpha \quad \text{ og } \quad y(b)=\beta,
     \end{gathered}

þá fæst nálgunin með því að leysa línulega jöfnuhneppið

.. math::

   \begin{aligned}
   w_0&=\alpha,\\
   \dfrac{w_{j+1}-2w_j+w_{j-1}}{h^2}
   &=p_j\dfrac{w_{j+1}-w_{j-1}}{2h}+q_jw_j+r_j, \qquad j=1,\dots,N-1,\\
   w_N&=\beta.  \end{aligned}

Jafngild framsetning á hneppinu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við lítum aftur á línulegu nálgunarjöfnurnar

.. math::

   \dfrac{w_{j+1}-2w_j+w_{j-1}}{h^2}
   =p_j\dfrac{w_{j+1}-w_{j-1}}{2h}+q_jw_j+r_j.

Margföldum alla liði með :math:`-h^2` og röðum síðan óþekktu stærðunum
vinstra mengin jafnaðarmerkisins. Þá fæst línulega jöfnuhneppið

.. math::

   \big(-1-\tfrac 12 h p_j\big)w_{j-1}
   +\big(2+h^2q_j\big) w_j
   +\big(-1+\tfrac 12 h p_j\big)w_{j+1}
   =-h^2\, r_j

fyrir :math:`j=1,2,3,\dots,N-1`.

Línulega jöfnuhneppið á fylkjaformi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nú er hægt að skrifa jöfnuhneppið á fylkjaformi

.. math:: A{\mbox{${\bf w}$}}={\mbox{${\bf b}$}}

Hér er 

.. math::

   A=\left[\begin{matrix}
     1&0\\
     l_1&d_1&u_1\\
     &l_2&d_2&u_2\\
     &&\cdot&\cdot&\cdot \\
     &&&\cdot&\cdot&\cdot \\
     &&&&\cdot&\cdot&\cdot \\
     &&&&&l_{N-2}&d_{N-2}&u_{N-2} \\
     &&&&&&l_{N-1}&d_{N-1}&u_{N-1} \\
     &&&&&&&0&1
     \end{matrix}\right]

þar sem stuðlarnir :math:`l_j`, :math:`d_j` og :math:`u_j` eru gefnir
með

.. math::

   \begin{aligned}
     l_j&=-1-\tfrac 12 hp_j\\
   d_j&=2+h^2q_j\\
   u_j&=-1+\tfrac 12 hp_j\end{aligned}

og vigrarnir eru

.. math::

   {\mbox{${\bf w}$}}=\left[
     \begin{matrix}
   w_0\\ w_1\\ w_2\\ \cdot\\ \cdot\\ \cdot\\ 
   w_{N-2}\\ w_{N-1}\\ w_N  
   \end{matrix}\right]
   \qquad \text{ og } \qquad 
   {\mbox{${\bf b}$}}=\left[
   \begin{matrix}
   \alpha \\ -h^2r_1\\ -h^2r_2\\ \cdot \\ \cdot\\ \cdot\\
   -h^2r_{N-2}\\ -h^2r_{N-1}\\ \beta
   \end{matrix}\right]


Við þekkjum allar tölurnar í :math:`A` og :math:`\bf b`, þannig að 
við getum leyst jöfnuhneppið og með því fundið 
nálgunargildin :math:`\bf w`.

.. index::
	jaðargildisverkefni; felugildi
	jaðargildisverkefni; felupunktar


Neumann og Robin -jaðarskilyrði
-------------------------------

Felugildi
~~~~~~~~~

Við skulum gera ráð fyrir að rétta lausnin :math:`y(x)` uppfylli blandað
jaðarskilyrði í :math:`x=a`,

.. math:: \alpha_1y(a)+\alpha_2 y'(a)=\alpha_3.

Til þess að líkja eftir afleiðujöfnunni í punktinum :math:`x=a` þá
hugsum við okkur að við bætum við einum skiptipunkti :math:`x_{-1}=a-h` og
látum :math:`w_f` tákna ímyndað gildi lausnarinnar í :math:`x_{-1}`.

Svona punktur :math:`x_{-1}` utan við skiptinguna er kallaður
*felupunktur* við skiptinguna og ímyndað gildi :math:`w_f` í felupunkti
er kallað *felugildi*.

Takið eftir því að lausnin er ekki til í felupunktinum, en við reiknum
eins og :math:`w_f` sé gildi hennar þar.

Mismunajafnan sem líkir eftir afleiðujöfnunni í punktinum :math:`x_0` er

.. math::

   \big(-1-\tfrac 12 hp_0\big)w_f+\big(2+h^2 q_0\big)w_0
   +\big(-1+\tfrac 12 hp_0\big)w_1=-h^2r_0

Mismunajafnan sem líkir eftir jaðarskilyrðinu er

.. math:: \alpha_1w_0+\alpha_2 \dfrac{w_1-w_f}{2h}=\alpha_3.

Jafna fyrir felugildið
~~~~~~~~~~~~~~~~~~~~~~

Jafnan sem líkir eftir jaðarskilyrðinu er:

.. math:: \alpha_1w_0+\alpha_2 \dfrac{w_1-w_f}{2h}=\alpha_3.

Út úr henni leysum við

.. math:: w_f=w_1-\dfrac{2h}{\alpha_2}\big(\alpha_3-\alpha_1w_0\big)

Við stingum síðan þessu gildi inn í jöfnuna sem líkir eftir
afleiðujöfnunni

.. math::

   \big(-1-\tfrac 12 hp_0\big)w_f+\big(2+h^2 q_0\big)w_0
   +\big(-1+\tfrac 12 hp_0\big)w_1=-h^2r_0

Út fæst fyrsta jafna hneppisins

.. math::

   \bigg(2+h^2q_0-\big(2+hp_0\big)h\dfrac{\alpha_1}{\alpha_2}\bigg)w_0
   -2w_1=-h^2r_0-\big(2+hp_0\big)h\dfrac{\alpha_3}{\alpha_2}.

Með því að innleiða felupunkt :math:`x_{N+1}=b+h` hægra megin við
skiptinguna, tilsvarandi felugildi :math:`w_f` og leysa saman tvær
jöfnur þá fáum við síðustu jöfnu hneppisins

.. math::

   -2w_{N-1}
   +\bigg(2+h^2q_N+\big(2-hp_N\big)h\dfrac{\beta_1}{\beta_2}\bigg)w_N
   =-h^2r_N-\big(2-hp_N\big)h\dfrac{\beta_3}{\beta_2}

Við erum því aftur komin með :math:`(N+1)\times (N+1)`-jöfnuhneppi.

Hneppið á fylkjaformi
~~~~~~~~~~~~~~~~~~~~~

.. math:: A{\mbox{${\bf w}$}}={\mbox{${\bf b}$}}

.. math::

   A=\left[\begin{matrix}
   a_{11}&a_{12}\\
   l_1&d_1&u_1\\
   &l_2&d_2&u_2\\
   &&\cdot&\cdot&\cdot \\
   &&&\cdot&\cdot&\cdot \\
   &&&&\cdot&\cdot&\cdot \\
   &&&&&l_{N-2}&d_{N-2}&u_{N-2} \\
   &&&&&&l_{N-1}&d_{N-1}&u_{N-1} \\
   &&&&&&&a_{N+1,N}&a_{N+1,N+1}
   \end{matrix}\right]

Þar sem stuðlarnir :math:`l_j`, :math:`d_j` og :math:`u_j` fyrir
:math:`j=1,2,3\dots,N-1` eru þeir sömu og áður.

.. math::

   \begin{aligned}
     l_j&=-1-\tfrac 12 hp_j\\
   d_j&=2+h^2q_j\\
   u_j&=-1+\tfrac 12 hp_j\end{aligned}

Fyrsta og síðasta lína hneppisins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   \begin{aligned}
   a_{11}&=
   \begin{cases}
     1,&\text{Dirichlet í } x=a: \alpha_1\neq 0, \alpha_2=0,\\
   d_0&\text{Neumann í } x=a:  \alpha_1=0, \alpha_2\neq 0,\\
   d_0+2hl_0\alpha_1/\alpha_2&\text{Robin í } x=a:  \alpha_2\neq 0.
   \end{cases} \\
   a_{12}&=
   \begin{cases}
     0,&\text{Dirichlet í } x=a: \alpha_1\neq 0, \alpha_2=0,\\
   -2,&\text{annars}.
   \end{cases}
   \\ 
   a_{N+1,N+1}&=
   \begin{cases}
     1,&\text{Dirichlet í } x=b: \beta_1\neq 0, \beta_2=0,\\
   d_N&\text{Neumann í } x=b:  \beta_1=0, \beta_2\neq 0,\\
   d_N-2hu_N\beta_1/\beta_2&\text{Robin í } x=a:  \beta_2\neq 0.
   \end{cases} 
   \\
   a_{N+1,N}&=
   \begin{cases}
     0,&\text{Dirichlet í } x=b: \beta_1\neq 0, \beta_2=0,\\
   -2&\text{annars}.
   \end{cases} 
     \end{aligned}

Hægri hlið hneppisins
~~~~~~~~~~~~~~~~~~~~~

.. math::

   {\mbox{${\bf b}$}}=\left[
   \begin{matrix}
   b_1 \\ -h^2r_1\\ -h^2r_2\\ \cdot \\ \cdot\\ \cdot\\
   -h^2r_{N-2}\\ -h^2r_{N-1}\\ b_{N+1}
   \end{matrix}\right]

.. math::

   b_{1}=
   \begin{cases}
     \alpha=\alpha_3/\alpha_1,
   &\text{Dirichlet í } x=a: \alpha_1\neq 0, \alpha_2=0,\\
   -h^2r_0+2hl_0\alpha_3/\alpha_2
   &\text{Neumann í } x=a:  \alpha_1=0, \alpha_2\neq 0,\\
   -h^2r_0+2hl_0\alpha_3/\alpha_2&\text{Robin í } x=a:  \alpha_2\neq 0.
   \end{cases}

.. math::

   b_{N+1}=
   \begin{cases}
     \beta=\beta_3/\beta_1,
   &\text{Dirichlet í } x=a: \beta_1\neq 0, \beta_2=0,\\
   -h^2r_N-2hu_N\beta_3/\beta_2&\text{Neumann í } x=a:  \beta_1=0, \beta_2\neq 0,\\
   -h^2r_N-2hu_N\beta_3/\beta_2&\text{Robin í } x=a:  \beta_2\neq 0.
   \end{cases}

.. index::
	jaðargildisverkefni; samantekt

Samantekt
~~~~~~~~~

Gildi lausnarinnar :math:`y(x)` á línulega jaðargildisverkefninu

.. math::

   \begin{gathered}
       y''=p(x)y'+q(x)y+r(x), \qquad a\leq x\leq b,\\
   \alpha_1y(a)+\alpha_2 y'(a)=\alpha_3,\\
   \beta_1 y(b)+\beta_2y'(b)=\beta_3  
     \end{gathered}

í punktunum :math:`x_j=a+jh`, þar sem :math:`h=(b-a)/N` og
:math:`j=0,\dots,N`, eru nálguð með

.. math:: w_j\approx y(x_j)=y_j

Dálkvigurinn

.. math:: {\mbox{${\bf w}$}}=[w_0,w_1,\dots,w_N]^T

er lausn á línulegu jöfnuhneppi
:math:`A{\mbox{${\bf w}$}}={\mbox{${\bf b}$}}`.

Stuðlum :math:`(N+1)\times(N+1)` fylkisins :math:`A` og
:math:`(N+1)`-dálkvigursins :math:`{\mbox{${\bf b}$}}` hefur verið lýst
hér að framan.
