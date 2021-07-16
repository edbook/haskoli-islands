.. _upphafsgildisverkefni:

.. index::
	upphafsgildisverkefni

Upphafsgildisverkefni
=====================

*In the beginning there was nothing, which exploded.*
-- Terry Pretchett

Inngangur
---------

.. index::
	upphafsgildisverkefni; fyrsta stigs

Fyrsta stigs afleiðujafna með upphafsgildi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gefið fall :math:`f` á einhverju svæði :math:`U` í
:math:`\mathbb{R}^2` sem inniheldur :math:`(t_0,x_0)` þá er 
*fyrsta stigs afleiðujafna með upphafsgildi* verkefni á forminu

.. math::

   \begin{cases}
   x' = f(t,x),\\
   x(t_0) = x_0.
   \end{cases}


Við segjum að fall :math:`x(t)` sé lausn á þessu verkefni ef :math:`x` er 
skilgreint á bili :math:`I`, sem er þannig að

-  :math:`t_0 \in I`,

-  :math:`(t,x(t)) \in U` fyrir öll :math:`t \in I`,

-  :math:`x'(t) = f(t,x(t))` fyrir öll :math:`t \in I`, og

-  :math:`x(t_0) = x_0`.

Útskýring og dæmi 
~~~~~~~~~~~~~~~~~
Ástæðan fyrir því að við notum :math:`t` fyrir breytuna og :math:`x` fyrir fall
hér, er að breytan :math:`t` lýsir oft tíma og lausnin getur þá t.d. verið staðsetning
sem fall af tíma.

Eðlilegt er að hugsa um afleiðujöfnuna þannig að fallið :math:`f` geymi upplýsingar
um þau lögmál sem kerfið að hagar sér eftir, upphafsskilyrðið :math:`x(t_0)=x_0` 
segir í hvaða stöðu kerfið er þegar það er sett af stað og 
lausnin :math:`x(t)` lýsir hegðun kerfisins með tíma. 

Í upphafi námskeiðsins, 
`dæmi 1.2 <https://notendur.hi.is/~bsm/stae405/kafli01.html#daemi-eldflaug>`_, skoðuðum
við dæmi um eldflaug sem skotið er á loft. Þar er notum við reyndar :math:`v` í stað
:math:`x` því jafnan lýsir hraða (e. velocity) en ekki staðsetningu.
Jafnan var

.. math::

	v' = \frac{5000-(300-10t)g-0,1v^2+10v}{300-10t},   \qquad v(0)=0.

Hér er því :math:`f(t,v) = \frac{5000-(300-10t)g-0,1v^2+10v}{300-10t}`, :math:`t_0=0` 
og :math:`x_0 = 0`.

.. index::
	upphafsgildisverkefni; tilvist og ótvíræðni

Tilvist og ótvíræðni lausna
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   \begin{cases}
   x' = f(t,x)\\
   x(t_0) = x_0
   \end{cases}

Ef :math:`f` er samfellt, þá er alltaf til lausn á einhverju bili
:math:`I`. (`Setning Peano <https://en.wikipedia.org/wiki/Peano_existence_theorem>`_)

Ef :math:`f` uppfyllir Lipschitz-skilyrði með tilliti til :math:`x`,
þ.e.a.s. til er fasti :math:`C` þannig að

.. math:: |f(t,x_1) - f(t,x_2)| \leq C|x_1 - x_2|

fyrir öll :math:`(t,x_1)` og :math:`(t,x_2)` í grennd um
:math:`(t_0, x_0)` þá er lausnin ótvírætt ákvörðuð. (`Setning Picard <https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem>`_)

Upphafsgildisverkefni fyrir hneppi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Með því að nota vigra og vigurgild föll má útfæra upphafsgildisverkefni fyrir hneppi:

.. math::

   \begin{cases}
   {\mbox{${\bf x}$}}' ={\mbox{${\bf f}$}}(t,{\mbox{${\bf x}$}})\\
   {\mbox{${\bf x}$}}(t_0) = {\mbox{${\bf x}$}}_0
   \end{cases}

þar sem

.. math::

   {\mbox{${\bf f}$}}: U \rightarrow {{\mathbb  R}}^n, \qquad U\subset \mathbb{R}^{n+1}, \quad
   (t_0,{\mbox{${\bf x}$}}_0) \in U.

Athugið að við skrifum :math:`{\mbox{${\bf x}$}}(t)` og
:math:`{\mbox{${\bf f}$}}(t,{\mbox{${\bf x}$}})` sem dálkvigra,

.. math::
   {\mbox{${\bf x}$}}(t) = [x_1(t), x_2(t), \ldots , x_n(t)]^T
   \quad \text{  og } \quad 
   {\mbox{${\bf f}$}}(t,{\mbox{${\bf x}$}}) = [f_1(t,{\mbox{${\bf x}$}}), \ldots , f_n(t, {\mbox{${\bf x}$}})]^T

.. index::
	upphafsgildisverkefni; jafngild hneppi

Jöfnur af stigi :math:`>1` og jafngild hneppi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aðferðirnar sem við munum skoða eru eingöngu fyrir fyrsta stigs afleiðujöfnur, 
sem þýðir að jöfnurnar sem við leysum 
innihalda bara :math:`x'` en ekki :math:`x'',x''',\ldots`. 
Hins vegar þá getum við leyst afleiðujöfnur af hærra stigi með því að umrita þær yfir í jafngilt
fyrsta stigs hneppi.

Ef við höfum
:math:`m`-stigs diffurjöfnu

.. math::

   \begin{aligned}
   u^{(m)} &= g(t,u, u',u'',\ldots , u^{(m-1)})\\
   u(t_0) &= u_0, \quad u'(t_0) = u_1, \quad \ldots, \quad  u^{m-1}(t_0) = u_{(m-1)}\end{aligned}

þar sem :math:`g` er gefið fall og :math:`t_, u_0, \ldots , u_{m-1}` eru
gefnar tölur þá er jafngilt hneppi er fengið með því að setja

.. math::

   \begin{aligned}
   x_1 =& u, \\
   x_2 =& u', \\
   x_3 =& u'', \\
   \vdots& \\
   x_m =& u^{(m-1)}\end{aligned}.

Þá fæst hneppið

.. math::
   {\bf x}' = 
   \begin{pmatrix}
   x_1' &= x_2 \\
   x_2' &= x_3 \\
   \vdots & \vdots\\
   x_{m-1}' &= x_m \\
   x_m' &= g(t,x_1, \ldots , x_m)
   \end{pmatrix} = 
   {\bf f}(t,{\bf x})

með upphafsskilyrðið :math:`{\bf x}(t_0)^T = [u_0,u_1,u_2,\ldots,u_m]^T`.

Fyrsta hnitið í lausn hneppisins, :math:`x_1`, gefur þá lausn, :math:`u` 
á upprunalegu :math:`m`-ta stigs afleiðujöfnunni.

Tilvist og ótvíræðni lausna á hneppum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tilvistar- og ótvíræðnisetningar Peanos og Picards eru þær sömu fyrir
hneppi

.. math::

   \begin{cases}
   {\mbox{${\bf x}$}}' ={\mbox{${\bf f}$}}(t,{\mbox{${\bf x}$}})\\
   {\mbox{${\bf x}$}}(t_0) = {\mbox{${\bf x}$}}_0
   \end{cases}

Við þurfum bara að setja norm :math:`\|\cdot\|` í stað tölugildis
:math:`|\cdot|` í öllum ójöfnum og þar með talið í Lipschitz-skilyrðinu.

.. index::
	upphafsgildisverkefni; nálgunargildi, tímaskref, skekkja

Ritháttur
~~~~~~~~~

Til einföldunar á rithætti skulum við skrifa lausnarvigurinn
:math:`{\mbox{${\bf x}$}}` og vörpunina :math:`{\mbox{${\bf f}$}}` sem
:math:`x` og :math:`f` og láta eins og við séum að leysa fyrsta stigs
afleiðujöfnu.

Við veljum gildi :math:`t_0 < t_1 < \cdots < t_j<\cdots` og reiknum út
*nálgunargildi* :math:`w_j` á gildi lausnarinnar :math:`x(t_j)` í
punktinum :math:`t_j`. Gildið :math:`w_0=x(t_0)` er rétta upphafsgildi
lausnarinnar

Talan :math:`t_j` kallast :math:`j`-ti *tímapunkturinn* og talan
:math:`h_j=t_j-t_{j-1}` nefnist :math:`j`-ta *tímaskrefið*.

*Skekkjan* á tíma :math:`t_j` er þá :math:`e_j = x(t_j)-w_j`.

Grunnhugmyndin í nálgunaraðferðum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef við heildum lausn afleiðujöfnunnar yfir tímabilið :math:`[t,t+h]`, þá
fáum við að hún uppfyllir jöfnuna

.. math::

   x(t+h)=x(t)+\int_t^{t+h}f(\tau,x(\tau))\, d\tau
   =x(t)+h\int_0^1f(t+sh,x(t+sh))\, ds.

Ef við setjum :math:`t=t_{j-1}` inn í þessa jöfnu, þá fáum við

.. math:: \dfrac{x(t_j)-x(t_{j-1})}{h_j}=\int_0^1f(t_{j-1}+sh_j,x(t_{j-1}+sh_j))\, ds

Nálgunaraðferðirnar snúast allar um að gera einhvers konar nálgun á
heildinu í hægri hliðinni

.. math::

   \int_0^1f(t_{j-1}+sh_j,x(t_{j-1}+sh_j))\, ds
     \approx \varphi(f,t_0,\dots,t_j,w_0,\dots,w_j)

og leysa síðan :math:`w_j` út úr jöfnunni

.. math:: \dfrac{w_j-w_{j-1}}{h_j}=\varphi(f,t_0,\dots,t_j,w_0,\dots,w_j)

.. index::
	upphafsgildisverkefni; beinar/óbeinar aðferðir

Beinar og óbeinar aðferðir
~~~~~~~~~~~~~~~~~~~~~~~~~~

Nálgunaraðferð sem byggir á jöfnunni

.. math:: \dfrac{w_j-w_{j-1}}{h_j}=\varphi(f,t_{0},\dots,t_j,w_{0},\dots,w_j)

er nefnist *bein aðferð* (e. explicit method) ef :math:`w_j` kemur ekki
fyrir í í hægri hliðinni.

Annars nefnist hún *óbein aðferð* eða *fólgin aðferð* (e. implicit
method).

Ef aðferðin er bein og við höfum reiknað út :math:`w_0,\dots,w_{j-1}`,
þá fáum við rakningarformúlu, þannig að :math:`w_j\approx x(t_j)` er
reiknað út

.. math:: w_j=w_{j-1}+h_j\varphi(f,t_{0},\dots,t_j,w_{0},\dots,w_{j-1})

.. index::
	upphafsgildisverkefni; skref

Eins skrefs aðferðir og fjölskrefaaðferðir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nálgunaraðferð sem byggir á jöfnunni

.. math:: \dfrac{w_j-w_{j-1}}{h_j}=\varphi(f,t_{j-1},t_j,w_{j-1},w_j)

er nefnist *eins skrefs aðferð* (e. one step method) og er þá vísað til
þess að fallið í hægri hliðinni er einungis háð gildum á síðasta
tímaskrefinu.

er af gerðinni

.. math:: \dfrac{w_j-w_{j-1}}{h_j}=\varphi(f,t_{j-2},t_{j-1},t_j,w_{j-2},w_{j-1},w_j)

Almennt er :math:`k` *-skrefa aðferð* af gerðinni

.. math:: \dfrac{w_j-w_{j-1}}{h_j}=\varphi(f,t_{j-k},\dots,t_j,w_{j-k},\dots,w_j)

*Fjölskrefaðferð* er :math:`k`-skrefa aðferð með :math:`k\geq 2`.


Aðferðir með fasta skrefastærð
------------------------------

.. index::
	upphafsgildisverkefni; aðferð Eulers

Aðferð Eulers
~~~~~~~~~~~~~

Rifjum upp að lausnin uppfyllir

.. math::

   \begin{aligned}
     x(t+h) - x(t) &= \int\limits_t^{t+h} x'(\tau) \, d\tau
     = \int\limits_t^{t+h} f(\tau,x(\tau)) \, d\tau\\
   &= h\int\limits_0^{1} f(t+sh,x(t+sh)) \, ds\end{aligned}

Billengdin í síðasta heildinu er :math:`1`, svo við tökum einföldustu
nálgum sem hugsast getur en það er gildið í vinstri endapunkti
:math:`f(t,x(t))`. Fyrir lítil :math:`h` fæst því

.. math:: x(t+h) \approx x(t) + hf(t,x(t)).

Við þekkjum :math:`w_0=x(t_0)`, svo með þessu getum við fikrað okkur
áfram og fengið runu nálgunargilda :math:`w_0, w_1, w_2, \ldots` þannig
að

.. math:: w_j = w_{j-1} + h_{j} f(t_{j-1},w_{j-1}).

Aðferð Eulers: Matlab-forrit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    function w = euler(f,t,alpha);  
    %   function w = euler(f,t,alpha) 
    % Aðferð Eulers fyrir afleiðujöfnuhneppi 
    %         x'(t)=f(t,x(t)), x(0)=alpha. 
    % Inn fara: f - fallið f 
    %           t - vigur með skiptingu á t-ás. 
    %           alpha - upphafsgildið í t(1). 
    % Út koma:  w - fylki með nálgunargildunum. 

    N = length(t);   
    m = length(alpha); 
    w = zeros(m,N);  
    w(:,1) = alpha; 
    for j=2:N 
       w(:,j) = w(:,j-1)+(t(j)-t(j-1))*f(t(j-1),w(:,j-1));
    end 

Aðferð Eulers: Dæmi
~~~~~~~~~~~~~~~~~~~~

Prófum aðferð Eulers á afleiðujöfnunni

.. math:: x' = \frac tx, \qquad x(0) = 1

Við sjáum að rétt lausn er :math:`x(t) = \sqrt{t^2+ 1}`.

Notum 101 jafndreifð tímagildi á bilinu [0,5]. Þá er skekkjan

::

     >> f = @(t,x) t./x;  
     >> t=linspace(0,5,101);
     >> w=euler(f,t,1);   
     >> plot(t,sqrt(t.^2+1) - w)
     >> title('Skekkja í aðferð Eulers'); xlabel('t'); ylabel('x-w');
     
.. image:: ./myndir/7euler.png

.. index::
	upphafsgildisverkefni; endurbætt aðferð Eulers

Endurbætt aðferð Eulers
~~~~~~~~~~~~~~~~~~~~~~~

Í aðferð Eulers nálguðum við heildið
:math:`\int_0^1 f(t+sh,x(t+sh))\, ds` með margfeldi af billengdinni og
fallgildinu í vinstri endapunkti.

Við getum endurbætt þessa nálgun með því að taka einhverja nákvæmari
tölulega nálgun á heildinu til dæmis miðpunktsaðferð

Nálgunarformúlan verður þá

.. math:: \int_0^1f(t+sh,x(t+sh))\, ds \approx f(t+\tfrac 12h,x(t+\tfrac 12 h)).

Nú er vandamálið að við höfum nálgað :math:`x(t_{j-1})` með
:math:`w_{j-1}` en höfum ekkert nálgunargildi á
:math:`x(t_{j-1}+\frac 12 h_j)`.

Við grípum þá til fyrsta stigs Taylor nálgunar

.. math::

   \begin{aligned}
   x(t_j+\tfrac 12 h_j)&=x(t_{j-1})+x'(t_{j-1})\big(\tfrac 12 h_j \big)
   +\tfrac 12x''(\xi)\big(\tfrac 12 h_j \big)^2\\
   &\approx w_{j-1}+\tfrac 12 h_jf(t_{j-1},w_{j-1}).\end{aligned}

Endurbætt aðferð Eulers er þá í tveim skrefum; við reiknum

.. math:: \tilde w_j = w_{j-1} + \tfrac 12 h_j f(t_{j-1},w_{j-1})

og fáum svo nálgunargildið

.. math::

   w_j = w_{j-1} + h_jf\left(
       t_{j-1}+\tfrac 12 h_j,\tilde w_j\right)

.. index::
	upphafsgildisverkefni; aðferð Heun

Aðferð Heun
~~~~~~~~~~~

Lítum nú á aðra aðferð þar sem við nálgum heildið með trapisuaðferð.

.. math::

   \int_0^1f(t+sh,x(t+sh))\, ds \approx 
   \tfrac 12 \big(f(t,x(t))+f(t+h,x(t+h))\big).

Af þessu leiðir að nálgunarformúlan á að vera

.. math:: w_j=w_{j-1}+\tfrac 12h_j\big(f(t_{j-1},w_{j-1})+f(t_j,w_j)\big)

Þetta er greinilega óbein aðferð svo við verðum að byrja á nálgun á
:math:`w_j`, með

.. math::

   w_j\approx x(t_j)=x(t_{j-1}+h_j)\approx x(t_{j-1})+h_jx'(t_{j-1})
   =x(t_{j-1})+h_jf(t_{j-1},w_{j-1})

Þetta nýja afbrigði af aðferð Eulers nefnist *aðferð Heun*. Hún er í
tveim skrefum: Við reiknum fyrst

.. math:: \tilde w_j = w_{j-1} + h_jf(t_{j-1},w_{j-1})

og fáum svo nálgunargildið

.. math::

   w_j = w_{j-1} + \tfrac 12h_j
   \big(f(t_{j-1},w_{j-1})+f(t_j,\tilde w_j)\big)

.. index::
	upphafsgildisverkefni; Runge-Kutta aðferðir
	upphafsgildisverkefni; forsagnar- og leiðréttingarskref

Forsagnar- og leiðréttingarskref
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Endurbætt aðferð Eulers og aðferð Heun eru leiðir til þess að vinna úr
óbeinum aðferðum, þar sem rakningarformúlan fyrir nálgunargildin er af
gerðinni

.. math:: w_j=w_{j-1}+h_j\varphi(f,t_{j-1},t_j,w_{j-1},w_j)

og okkur vantar eitthverja nálgun á :math:`w_j` til þess að stinga inn í
hægri hlið þessarar jöfnu. Við skiptum þessu tvö skref:

Við beitum einhverri beinni aðferð til þess að reikna út

.. math:: \tilde w_j=w_{j-1}+h_j\psi(f,t_{j-1},t_j,w_{j-1})

Setjum

.. math:: w_j=w_{j-1}+h_j\varphi(f,t_{j-1},t_j,w_{j-1},\tilde w_j).

Svona aðferðir kallast *Runge-Kutta aðferðir*. Fyrra skrefið, þegar 
:math:`\tilde w_j` er reiknað út kallast *forsagnarskref* og
seinna skrefið kallast *leiðréttingarskref*.

.. index::
	upphafsgildisverkefni; annars stigs Runge-Kutta

Annars stigs Runge-Kutta-aðferð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lítum aftur á verkefnið

.. math::

   \left\{
       \begin{array}{l}
         x'(t) = f(t,x(t)) \\
         x(t_0) = x_0
       \end{array}
     \right.

og skoðum 2. stigs Taylor liðun á lausninni :math:`x` í punkti
:math:`t`. Innleiðum fyrst smá rithátt til styttingar, setjum

.. math::

   x = x(t), \quad f'_t = \frac{\partial f}{\partial t}(t,x(t)), \quad
     f = f(t,x(t)), \quad f'_x = \frac{\partial f}{\partial x}(t,x(t)).

Keðjureglan gefur

.. math:: x''(t)=\dfrac d{dt}f(t,x(t))=f'_t+f'_xx'(t)=f'_t+f\,f'_x.

Taylor-liðun lausnarinnar er

.. math::

   \begin{aligned}
     x(t+h) &= x + hx'(t) + \frac{1}{2} h^2 x''(t) + O(h^3) \\
     &= x + hf + \frac{1}{2} h^2 ( f'_t + f f'_x ) + O(h^3) \\
     &= x + \frac{1}{2}hf + \frac{1}{2}h( f + hf'_t + (hf)f'_x) + O(h^3)\end{aligned}

Nú sjáum við að síðasti liðurinn er 1. stigs Taylor liðun :math:`f` með
miðju :math:`(t,x)` skoðuð í punktinum :math:`(t+h,x+hf)`, því

.. math:: f(t+h,x + hf) = f + hf'_t + (hf) f'_x + O(h^2)

og þar með er

.. math:: x(t+h) = x(t) + \frac{1}{2} hf(t,x) + \frac{1}{2} hf(t+h,x+hf) + O(h^3). 

Þessi formúla liggur til grundvallar 2. stigs Runge-Kutta-aðferð: Með
henni fáum við nálgunarrunu :math:`w_0, w_1, w_2, \ldots` þannig að
:math:`w_0=x(0)` og

.. math:: w_j = w_{j-1} + \tfrac{1}{2}(F_1 + F_2), \quad j = 1,2,\ldots

þar sem

.. math::

   F_1 = h_jf(t_{j-1},w_{j-1}),
     \quad \text{og} \quad
     F_2 = h_jf(t_j,w_{j-1}+F_1)

og eins og alltaf er :math:`w_j \approx x(t_j)`.

.. index::
	upphafsgildisverkefni; klassíska Runge-Kutta

Klassíska (fjórða stigs) Runge-Kutta aðferðin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Algengasta Runge-Kutta aðferðin er klassíska Runge-Kutta aðferðin. Þetta
er fjórða stigs aðferð, sem þýðir að staðarskekkjan er :math:`O(h^5)` og
heildarskekkjan er :math:`O(h^4)`, .

.. math:: w_{j} = w_{j-1} + \frac 16(k_1 + 2k_2 + 2k_3 + k_4),

þar sem

.. math::

   \begin{aligned}
     k_1 &= hf(t_{j-1},w_{j-1}) \\
     k_2 &= hf\left(t_{j-1} + \frac h2,w_{j-1}+ \frac{k_1}2\right) \\
     k_3 &= hf\left(t_{j-1} + \frac h2,w_{j-1}+ \frac{k_2}2\right) \\
     k_4 &= hf(t_{j-1} + h,w_{j-1}+ k_3).
    \end{aligned}

Ef :math:`f(t,x)` er bara fall af :math:`t`, þ.e. óháð :math:`x`, þá
svarar þetta til þess að meta heildið :math:`{\varphi}` með
Simpson-reglunni.

Klassíska Runge-Kutta aðferðin: Dæmi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skoðum nú sama dæmi og þegar við `prófuðum aðferð Eulers <Aðferð Eulers: Dæmi>`_.

Þá gefa eftirfarandi skipanir mynd af skekkjunni.

::

    >> f = @(t,x) t./x;
    >> [w,t]=rk4(f,0,1,5,100);
    >> plot(t,sqrt(t.^2+1) - w)

.. image:: ./myndir/7rk4.png

Þetta er töluvert betra en aðferð Eulers sem skilaði skekkju af stærðargráðunni
:math:`10^{-2}`.

Skekkjumat, samleitni og stöðugleiki
------------------------------------

::

    +++Mr. Jelly! Mr. Jelly!+++ 
    +++Error At Address: 14, Treacle Mine Road, Ankh-Morpork+++
    +++MELON MELON MELON+++
    +++Divide By Cucumber Error. Please Reinstall Universe And Reboot +++
    +++Whoops! Here Comes The Cheese! +++
    +++Oneoneoneoneoneoneone+++

--villuskilaboð tölvunnar Hex í Interesting Times eftir Terry Pratchett

.. index::
	upphafsgildisverkefni; staðarskekkja
	upphafsgildisverkefni; heildarskekkja

Skekkja
~~~~~~~
Fyrir eins skrefs aðferð skilgreinum við *staðarskekkju* við tímann
:math:`t_n` sem

.. math::

   \tau_n = \dfrac{x(t_n)-x(t_{n-1})}{h_n} - 
   \varphi(f,t_{n-1},t_n,x(t_{n-1}),x(t_{n}))

Hér er réttu lausninni stungið inn í nálgunarformúluna. Munum að hún
uppfyllir

.. math::

   \dfrac{x(t_n)-x(t_{n-1})}{h_n}
   =\int_0^1 f(t_{n-1}+sh_n,x(t_{n-1}+sh_n))\, ds

Viljum geta metið :math:`\tau_n` sem fall af :math:`h_n`, t.d.

.. math:: \tau_n = O(h_n^k)

Almennt batna aðferðir eftir því sem veldisvísirinn :math:`k` í
staðarskekkjunni verður stærri.

Staðarskekkja er hlutfallsleg skekkja við að fara úr :math:`w_{n-1}`
yfir í :math:`w_n`. Einnig má skoða uppsafnaða skekkju frá 
upphafstímanum :math:`t_0`, hún er skilgreind með
:math:`e_n = x(t_j)-w_j` og kallast *heildarskekkja*.

Staðarskekkja í aðferð Eulers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aðferð Eulers er sett fram með formúlunni

.. math:: w_n=w_{n-1}+h_nf(t_{n-1},w_{n-1})

Staðarskekkjan er því

.. math::

   \begin{aligned}
     \tau_n&=\dfrac{x(t_n)-x(t_{n-1})}{h_n}-f(t_{n-1},x(t_{n-1}))\\
   &=\dfrac{x(t_n)-x(t_{n-1})-x'(t_{n-1})h_n}{h_n}\\
   &=\dfrac{\tfrac 12 x''(\xi_{n})h_{n-1}^2}{h_n}
   =\tfrac 12 x''(\xi_{n})h_{n-1}=O(h_n)\end{aligned}

Aðferð Eulers er því fyrsta stigs aðferð.

Stýring á staðarskekkju og breytileg skrefastærð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hingað til þá höfum við ekki fengið neinar upplýsingar til að finna heppilegustu skrefastærð.
Eftir því sem skrefastærðin er minni er staðarskekkjan sennilega minni, en þá komumst við
hægar yfir og það er hætta á að heildarskekkjan hækki við að taka mörg skref. 
Í `Aðferðir með breytilega skrefastærð`_ munum við reyna að stilla 
skrefastærðina þannig að við tökum eins stór skref og mögulegt en þó 
þannig að staðarskekkjan sé ekki of há. 
Þá munum við þurfa eftirfarandi útleiðslu.

Hugsum okkur að við höfum tvær beinar nálgunaraðferðir

.. math:: w_{n} = w_{n-1} + h_n\varphi(f,t_{n-1},t_n,w_{n-1})

og

.. math:: \tilde w_{n} = w_{n-1} + h_n\tilde\varphi(f,t_{n-1},t_n,w_{n-1})

Skilgreinum tilsvarandi staðarskekkjur

.. math:: \tau_n(h_n) = k_1h_n^{\alpha_1} + o(h_i^{\alpha_1})

og

.. math:: \tilde\tau_n(h_n) = k_2h_n^{\alpha_2} + o(h_i^{\alpha_2}),

þar sem :math:`\alpha_2>\alpha_1`. Við tímann :math:`t_{n-1}` hafa
nálgunargildin :math:`w_0,\ldots,w_{n-1}` hafi verið valin samkvæmt
fyrri aðferðinni.

Meiningin að velja næsta tímapunkt :math:`t_n` og þar með tímaskref
:math:`h_n` þannig að :math:`\tau_n(h_n)\leq \delta`, en að
:math:`\tau_n(h_n)` haldi sig sem næst :math:`\delta`, þar sem
:math:`\delta` er gefið efra mark á staðarskekkjunni í fyrri
aðferðinni.

Stærðin :math:`\delta` er kölluð *þolmörk* (e. tolerance) fyrir
staðarskekkjuna og er oft táknuð með :math:`TOL`.

Við byrjum á að setja :math:`h=h_{n}` inn í báðar aðferðirnar og bera
útkomurnar saman

.. math:: w_{n} = w_{n-1} + h\varphi(f,t_{n-1},t_{n-1}+h,w_{n-1})

.. math::

   \tilde w_{n} = \tilde w_{n-1} + 
   h\tilde\varphi(f,t_{n-1},t_{n-1}+h,w_{n-1})

Við látum :math:`\hat w_{n}` tákna rétt gildi lausnarinnar á
upphafsgildisverkefninu

-  :math:`x'(t)=f(t,x(t))`,

-  :math:`x(t_{n-1})=w_{n-1}`,

í punktinum :math:`t_{n-1}+h`.

Þá höfum við

.. math::

   \begin{aligned}
    \tau_n(h)&=\dfrac{\hat
   w_{n}-w_{n-1}}{h}-\varphi(f,t_{n-1},t_{n-1}+h,w_{n-1})\\
   &=\dfrac{\hat
   w_{n}-w_{n-1}-h\varphi(f,t_{n-1},t_{n-1}+h,w_{n-1})}{h} 
   =\dfrac {\hat w_{n}-w_{n}}{h}\end{aligned}

og eins fæst

.. math::

   \begin{aligned}
   \tilde \tau_n(h)
   &=\dfrac{\hat
   w_{n}-w_{n-1}}{h}-\tilde \varphi(f,t_{n-1},t_{n-1}+h,w_{n-1})\\
   &=\dfrac{\hat
   w_{n}-w_{n-1}-h\tilde \varphi(f,t_{n-1},t_{n-1}+h,w_{n-1})}{h} 
   =\dfrac {\hat w_{n}-\tilde w_{n}}{h}. \end{aligned}

Nú tökum við mismuninn og skilgreinum

.. math::

   \begin{aligned}
   \varepsilon 
   &= \left|\frac{\tilde w_{n}-w_{n}}{h}\right|=|\tau_n(h)-\tilde
     \tau_n(h)|\\
   &=|k_1|h^{\alpha_1}+o(h^{\alpha_1}) \approx |k_1|h^{\alpha_1}  \end{aligned}

Munum að hér er skreflengdin :math:`h=h_{n}`. Þessi nálgunarformúla
gefur okkur möguleika á því að meta fastann

.. math::

   |k_1|\approx
   \dfrac\varepsilon{h_{n}^{\alpha_1}}.

Mat á skrefastærð
~~~~~~~~~~~~~~~~~

Segjum nú að við viljum halda staðarskekkjunni innan markanna
:math:`\delta/2` og hafa skreflengdina í næsta skrefi
:math:`h_{n}=qh_{n-1}`, þá höfum við nálgunarjöfnuna

.. math::

   |\tau_n(qh_{n-1})|\approx |k_1|(qh_{n-1})^{\alpha_1}=
   \varepsilon {q^{\alpha_1}} \approx  \frac{\delta} 2.

Við tökum

.. math:: q = \left(\frac{\delta}{2\varepsilon}\right)^{1/{\alpha_1}}

veljum síðan skrefstærðina :math:`h_n = qh_{n-1}` og reiknum út næsta
gildi

.. math:: w_{n} = w_{n-1} + h_n\varphi(f,t_{n-1},t_n,w_{n-1})

.. index::
	upphafsgildisverkefni; breytileg skrefastærð

Aðferðir með breytilega skrefastærð
-----------------------------------

Dæmi um aðferðir sem notast við breytilega skrefastærð.

-  Einfaldast væri að nota Heun aðferðina (annars stigs) til að meta
   skrefastærðina í Euler aðferðinni (fyrsta stigs).

-  Algengasta aðferðin er Runge-Kutta-Fehlberg (RKF45) sem notar
   5. stigs nálgun til þess að meta staðarskekkjuna í 4. stigs aðferð.

-  Endurbót á RKF45 er Runge-Kutta-Verner (RKV56) sem notar 6. stigs
   aðferð til að meta skekkjuna í 5. stigs aðferð.

-  Fleiri aðferðir: Bogacki–Shampine (3. og 2. stigs), Cash–Karp (5. og
   4. stigs) og Dormand–Prince (5. og 4. stigs).

.. index::
	upphafsgildisverkefni; Runge-Kutta-Fehlberg (RKF45)


Reiknirit fyrir Runge-Kutta-Fehlberg (RKF45)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   \begin{aligned}
     \tilde w_j &= w_{j-1} \frac{16}{135} k_1 + \frac{6656}{12825}k_3 + \frac{28561}{56430}k_4
     - \frac{9}{50}k_5 + \frac{2}{55}k_6\\
     w_j &= w_{j-1} + \frac{25}{216}k_1 + \frac{1408}{2565}k_3 + \frac{2197}{4104}k_4 - \frac 15 k_5
    \end{aligned}

þar sem

.. math::

   \begin{aligned}
     k_1 &= hf(t_{j-1},w_{j-1}) \\  
     k_2 &= hf\left( t_{j-1}+\frac 14h, w_{j-1}+\frac 14k_1          \right)\\
     k_3 &= hf\left( t_{j-1}+\frac 38h, w_{j-1}+\frac 3{32}k_1 + \frac 9{32}k_2\right)\\
     k_4 &= hf\left( t_{j-1}+\frac{12}{13}h, w_{j-1} + \frac{1932}{2197}k_1 
     - \frac{7200}{2197}k_2 + \frac{7296}{2197}k_3 \right)\\
     k_5 &= hf\left( t_{j-1} +h, w_{j-1} + \frac{439}{216}k_1 - 8k_2+\frac{3680}{513}k_3 
     -\frac{845}{4104}k_4\right)\\
     k_6 &= hf\left( t_{j-1} +\frac 12h, w_{j-1} - \frac 8{27}k_1 + 2k_2 -\frac{3544}{2565}k_3
     +\frac{1859}{4104}k_4 - \frac{11}{40}k_5\right)\\
    \end{aligned}

Runge-Kutte-Fehlberg (RKF45) prófuð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Höldum áfram með dæmi sem við beittum `aðferð Eulers <Aðferð Eulers: Dæmi>`_ og 
`klassísku Runge-Kutta <Klassíska Runge-Kutta aðferðin: Dæmi>`_ hér á undan

Þá gefur eftirfarandi mynd af skekkjunni. Hér er 0.01 minnsta leyfilega
skrefastærðin, 0.1 stærsta leyfilega skrefastærðin og þolmörkin eru
:math:`10^{-10}`.

::

    >> f = @(t,x) t./x;
    >> [w,t] = rkf45(f,0,1,5,[0.01,0.1,1E-10]);
    >> plot(t,sqrt(t.^2+1) - w)

.. image:: ./myndir/7rkf45.png


Hér á undan þá notðum við þolmörkin :math:`10^{-10}` sem skilaði okkur
103 misstórum tímagildum á bilinu :math:`[0,5]`. Svona getum við teiknað
upp stærðina á tímaskrefunum.

::

    >> plot(t(2:end)-t(1:end-1),'*')

.. image:: ./myndir/7rkf45t.png

.. index::
	upphafsgildisverkefni; fjölskrefaaðferðir

Fjölskrefaaðferðir
------------------

Þær aðferðir sem við höfum séð eiga allar sameiginlegt að ákvarða
nálgunargildi :math:`w_{n}` aðeins út frá gildinu :math:`w_{n-1}` næst á
undan. Hægt er að nota fleiri gildi :math:`w_{n-1}`, :math:`w_{n-2}`,
:math:`\ldots` og fá þannig betri nákvæmni, en aðferðirnar verða að sama
skapi flóknari í notkun.

Eins og alltaf höfum við verkefnið

.. math::

   \left\{
       \begin{array}{l}
         x'(t) = f(t,x(t)) \\
         x(t_0) = w_0
       \end{array}
     \right.

og viljum nálga gildi lausnarinnar :math:`x` á bili :math:`[a,b]` þar
sem :math:`a =t_0` eða :math:`b = t_0`. Látum :math:`t_0`, :math:`t_1`,
:math:`\ldots`, :math:`t_n` vera skiptingu á bilinu :math:`[a,b]` og
gerum til einföldunar ráð fyrir að hún hafi jafna billengd
:math:`h=t_{j} - t_{j-1}` fyrir :math:`j= 1, \ldots, n`.

.. index::
	upphafsgildisverkefni; Adams-Bashforth

:math:`k`-skrefa Adams-Bashforth aðferð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Við vitum að lausnin :math:`x` uppfyllir

.. math::

   x(t_{n}) - x(t_{n-1}) = 
     \int\limits_{t_{n-1}}^{t_n} f(t,x(t)) \, dt

Skrifum nú

.. math:: f(t,x(t)) = P_{k-1}(t) + R_{k-1}(t)

þar sem

.. math::

   P_{k-1}(t) = \sum\limits_{j=1}^k f(t_{n-j},x(t_{n-j})) \cdot
     \ell_{k-1,j}(t)

er brúunarmargliðan gegnum punktana :math:`(t_{n-k},x(t_{n-k}))`,
:math:`(t_{n+1-k},x(t_{n+1-k}))`, :math:`\ldots`,
:math:`(t_{n-1},x(t_{n-1}))`, þ.e. gegnum síðustu :math:`k` punkta á
undan :math:`(t_n,x(t_n))`.

Þetta eru :math:`k` punktar og því er aðferðin kölluð :math:`k`-skrefa
aðferð.

`Munum <kafli03.html#id9>`_ að til er :math:`\xi` þannig að

.. math::

   R_{k-1}(t) = \frac{f^{(k)}(\xi,x(\xi))}{k!}
     \prod\limits_{j=1}^m (t-t_{n-j}).

Við nálgum nú heildið af :math:`f` yfir bilið :math:`[t_{n-1},t_n]` með
heildi :math:`P_{k-1}` og fáum

.. math::

   w_{i+1} = w_i +
     \int\limits_{t_i}^{t_{i+1}} P_{k-1}(t) \, dt

og með beinum útreikningum má sjá að skekkjan í þessari nálgun er
:math:`O(h^{k+1})`. Þessir útreikninga flækjast auðvitað eftir því sem
:math:`k` stækkar.

Augljóslega getum við ekki notað :math:`k` skrefa Adams-Bashforth
aðferðir um leið og við sjáum upphafsgildisverkefni, því við þurfum
:math:`k` ágiskunargildi :math:`w_0, w_1, \ldots, w_{k-1}` til að byrja
að nota aðferðina. Þessi gildi má fá með hverri sem er af aðferðunum sem
við höfum séð hingað til.

Ákveðin sértilfelli Adams-Bashforth aðferðanna eru meira notuð en önnur,
það eru tveggja, þriggja og fjögurra skrefa aðferðirnar. Áhugasömum
verður ekki skotaskuld úr að leiða út formúlurnar fyrir þær, en við
birtum bara niðurstöðurnar.

Til styttingar skilgreinum við :math:`f_j = f(t_j,w_j)`.

Tveggja skrefa Adams-Bashforth-aðferð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Þegar gildin :math:`w_{n-1}` og :math:`w_{n-2}` hafa verið fundin fæst 
næsta nálgunargildi með

.. math:: w_{n} = w_{n-1} + h\big(\tfrac 32 f_{n-1} - \tfrac 12 f_{n-2}\big)

og skekkjan í nálguninni er :math:`O(h^3)`.

Forrit fyrir tveggja skrefa Adams-Bashforth-aðferð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aðferðin er útfærð í forritinu hér að neðan; það skýrir sig að mestu
sjálft en við skulum taka eftir þrennu:

(i) Við krefjumst þess að notandinn gefi nálgunargildi á x(t(2)), þetta
gerum við því til eru margar mismunandi aðferðir til að fá slíkt gildi
og þær henta mis vel hverju sinni.

(ii) Við gerum ekki sérstaklega ráð fyrir að jafnt bil sé á milli
stakanna í vigrinum t þó við höfum gert það hingað til. Það var aðeins
gert til að einfalda útreikninga; aðferðin virkar nákvæmlega eins ef það
er ekki jafnt bil á milli stakanna, svo sjálfsagt er að forrita hana
þannig.

(iii) Við lágmörkum fjölda skipta sem við reiknum gildi f með að geyma
alltaf gildið frá síðustu ítrun og nota það aftur, þetta getur sparað
nokkurn tíma í útreikningum ef f er flókið fall.

::

    function w = adams_bashforth_2(f,t,x1,x2)
    %   w = adams{_}bashforth{_}2(f,t,x1,x2)
    % Nálgar lausn upphafsgildisverkefnisins
    %   x' = f(t,x)
    %   x(t(1)) = x1
    % í punktunum í t með 2ja þrepa Adams-Bashforth aðferð.
    % Stakið x2 er nálgunargildi á x(t(2)).

    N = length(t);  M = length(x1); w = zeros(M,N);
    % Upphafsstillum gildi f(t,x) og w
    fx1 = f(t(1),x1); fx2 = f(t(2),x2);
    w(:,1) = x1; w(:,2) = x2;
    for i=3:N
      % Reiknum nálgunargildi
      h = t(i)-t(i-1);
      w(:,i) = w(:,i-1) + (h/2)*(3*fx2 - fx1);
      fx1 = fx2; fx2 = f(t(i),w(:,i));
    end

Þriggja skrefa Adams-Bashforth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gefin :math:`w_{n-1}`, :math:`w_{n-2}` og :math:`w_{n-3}` fæst næsta
nálgunargildi með

.. math::

   w_{n} = w_{n-1} + {h}(\tfrac{23}{12} f_{n-1} - \tfrac {16}{12}
     f_{n-2} + \tfrac 5{12} f_{n-2})

og staðarskekkjan er :math:`O(h^4)`

Fjögurra skrefa Adams-Bashforth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Þegar við þekkjum :math:`w_{n-1}`, :math:`w_{n-2}`, :math:`w_{n-3}` og
:math:`w_{n-4}` reiknum við næsta gildi með

.. math::

   w_{n} = w_{n-1} + h\big(\tfrac{55}{24}f_{n-1} - \tfrac{59}{24}f_{n-2} + 
   \tfrac {37}{24}f_{n-3} -\tfrac 9{24}f_{n-4}\big)

og skekkjan í nálguninni er :math:`O(h^5)`.

Greining á samleitni og stöðugleika
-----------------------------------

Lítum aftur á upphafsgildisverkefnið okkar

.. math::

   \begin{cases}
     x'(t)=f(t,x(t)),\\
   x(t_0)=w_0.
   \end{cases}

Við hugsum okkur að nálgun sé fundin í tímapunktunum

.. math:: a=t_0<t_1<t_2<\cdots<t_N=b.

Við táknum nálgunargildi á :math:`x(t_j)` með :math:`w_j`. Það er gefið
með

.. math:: w_n=w_{n-1}+h_n\varphi(f,t_{0},\dots,t_n,w_{0},\dots,w_{n})

þar sem fallið :math:`\varphi(f,t_{0},\dots,t_n,w_{0},\dots,w_{n})` er
skilgreint með einhverjum hætti.

Við köllum þetta *nálgunaraðferðina sem fallið* :math:`\varphi` *gefur af
sér.*

Skekkja
~~~~~~~

*Skekkja* (e. error) eða *heildarskekkja* (e. total error) í nálgun á
:math:`x(t_n)` með :math:`w_n` er

.. math:: e_n=x(t_n)-w_n,

og *staðarskekkja* (e. local truncation error) nálgunaraðferðarinnar við tímann :math:`t_n`
er

.. math::

   \tau_n=\dfrac{x(t_n)-x(t_{n-1})}{h_n}
   -\varphi(f,t_{0},\dots,t_n,x(t_{0}),\dots,x(t_{n}))

.. note:: 
	Munið að hér er *rétta lausnin* sett inn í nálgunaraðferðina.

.. index::
	upphafsgildisverkefni; samleitni

Samleitni
~~~~~~~~~

Hugsum okkur nú að fjöldi tímapunktanna :math:`N` stefni á óendanlegt.
Við segjum að nálgunaraðferðin :math:`\varphi` sé *samleitin* ef

.. math:: \lim_{N\to \infty} \max\limits_{1\leq n\leq N} |e_n|=0

þar sem :math:`e_n=x(t_n)-w_n` táknar skekkjuna í :math:`n`-ta
tímaskrefinu.

.. index::
	upphafsgildisverkefni; samræmi

Samræmi
~~~~~~~

Við segjum að nálgunaraðferðin :math:`\varphi` *samræmist*
upphafsgildisverkefninu ef um sérhvern tímapunkt :math:`t_{n-1}` gildir
að

.. math::

   \begin{gathered}
   \lim_{h_n\to 0}\tau_n\\
   =\lim_{t_n\to t_{n-1}}\bigg(\dfrac{x(t_n)-x(t_{n-1})}{t_n-t_{n-1}}
   -\varphi(f,t_{0},\dots,t_n,x(t_{0}),\dots,x(t_{n}))\bigg)
   =0  \end{gathered}

Samræmi endurbættu Euler-aðferðarinnar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Munum að endurbætta Euler-aðferðin er

.. math:: w_n=w_{n-1}+h_nf(t_{n-1}+\tfrac 12 h_n,w_{n-1}+\tfrac 12 hf(t_{n-1},w_{n-1}))

sem gefur staðarskekkjuna

.. math::

   \begin{gathered}
   \tau_n=\dfrac{x(t_{n-1}+h_n)-x(t_{n-1})}{h_n}\\
   -f(t_{n-1}+\tfrac 12 h_n,x(t_{n-1})+\tfrac 12 h_nf(t_{n-1},x(t_{n-1}))).
     \end{gathered}

Nú hugsum við okkur að :math:`t_{n-1}` sé haldið föstu og látum
billengdina :math:`h_n=t_n-t_{n-1}` stefna á :math:`0`. Þá fæst

.. math:: \lim_{h_n\to 0} \tau_n= x'(t_{n-1})-f(t_{n-1},x(t_{n-1}))=0

Þetta segir okkur að endurbætta Euler-aðferðin samræmist
upphafsgildisverkefninu.

Samræmi beinna eins skrefs aðferða
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Þessi röksemdafærla alhæfist á allar beinar eins skrefs aðferðir, því
staðarskekkja þeirra er

.. math::

   \tau_n=\dfrac{x(t_{n-1}+h_n)-x(t_{n-1})}{h_n}
   -\varphi(f,t_{n-1},t_{n-1}+h_n,x(t_{n-1}))

Nú er eðlilegt að gefa sér að :math:`\varphi` sé samfellt fall og þá
verður markgildið af staðarskekkjunni

.. math::

   \begin{gathered}
   x'(t_{n-1})-\varphi(f,t_{n-1},t_{n-1},x(t_{n-1}))\\
   =f(t_{n-1},x(t_{n-1}))-\varphi(f,t_{n-1},t_{n-1},x(t_{n-1})).\end{gathered}

Eins skrefs aðferðin sem fallið :math:`\varphi` gefur af sér er því
stöðug ef og aðeins ef

.. math::

   \varphi(f,t_{n-1},t_{n-1},x(t_{n-1}))
   =f(t_{n-1},x(t_{n-1})).

.. index::
	upphafsgildisverkefni; stöðugleiki

Stöðugleiki
~~~~~~~~~~~

Gerum nú ráð fyrir að upphafsgildinu :math:`w_0` sé breytt í
:math:`\tilde w_0` og að :math:`\tilde x(t)` uppfylli

.. math::

   \begin{cases}
     \tilde x'(t)=f(t,\tilde x(t)),\\
   \tilde x(t_0)=\tilde w_0.
   \end{cases}

Lítum síðan á tilsvarandi nálgunarrunu

.. math::

   \tilde w_n=\tilde w_{n-1}+h_n\varphi(f,t_0,\dots,t_n,\tilde
   w_0,\dots,\tilde w_n).

Við segjum að nálgunaraðferðin sem :math:`\varphi`
gefur af sér sé *stöðug* ef til er fall :math:`k(t)>0` þannig að

.. math:: |\tilde w_n-w_n|\leq k(t_n)|\tilde w_0-w_0|, \qquad n=1,2,3\dots.

.. index::
	Lipschitz-samfelldni

Lipschitz-samfelldni
~~~~~~~~~~~~~~~~~~~~

Rifjum nú upp að við gerum ráð fyrir að fallið :math:`f(t,x)` sé
skilgreint á svæði :math:`D` sem inniheldur

.. math:: \{(t,x)\in {{\mathbb  R}}^2 \, ;\, a\leq t\leq b, x\in {{\mathbb  R}}\}.

Við segjum að :math:`f` sé *Lipschitz samfellt á* :math:`D` *með tilliti
til* :math:`x` ef til er fasti :math:`C_f` þannig að

.. math:: |f(t,x)-f(t,y)|\leq C_f|x-y|, \qquad x,y\in {{\mathbb  R}}.

Hugsum okkur að :math:`\varphi(f,s,t,x)` sé fall sem gefur af sér beina
eins skrefs nálgunaraðferð fyrir upphafsgildisverkefnið
:math:`x'(t)=f(t,x(t))` með :math:`x(t_0)=w_0`.

Við segjum að :math:`\varphi` sé *Lipschitz-samfellt með tilliti til*
:math:`x` ef um sérhvert Lipschitz-samfellt fall :math:`f`, tölur
:math:`s,t\in [a,b]` og :math:`x,y\in {{\mathbb  R}}` gildir að til er
fasti :math:`L_\varphi` þannig að

.. math:: |\varphi(f,s,t,x)-\varphi(f,s,t,y)|\leq L_\varphi|x-y|, \qquad x,y\in {{\mathbb  R}}.

Setning um stöðugleika og samleitni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gefum okkur jafna skiptingu á tímabilinu :math:`[a,b]`,
:math:`t_n=a+nh`, þar sem :math:`n=0,1,2,\dots,N` og :math:`h=(b-a)/N`.

Ef fallið :math:`\varphi` er Lipschitz-samfellt með tilliti til
:math:`x` með Lipschitz-fastann :math:`L_\varphi`, þá gildir:

#. Eins skrefs aðferðin sem :math:`\varphi` gefur af sér er stöðug,

   .. math::

      |\tilde w_n-w_n|\leq e^{L_\varphi(t_n-a)}|\tilde w_0-w_0|, \qquad
      n=1,2,3,\dots.

#. Ef til eru fastar :math:`c` og :math:`p` þannig að staðarskekkjan
   uppfyllir :math:`|\tau_n|\leq c\, h^p`, fyrir öll
   :math:`n=1,2,3,\dots` og :math:`h\in ]0,h_0]`, þá er aðferðin
   samleitin og við höfum

   .. math::

      |e_n|=|x(t_n)-w_n|\leq \dfrac{ch^p}{L_\varphi}
      \bigg(e^{L_\varphi(t_n-a)}-1\bigg).

