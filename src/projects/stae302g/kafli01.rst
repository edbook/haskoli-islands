Tvinntölur
==========

*There's something that doesn't make sense. Let's go and poke it with a stick.*

\- The Doctor, Doctor Who

Tvinntölurnar
-------------

Skilgreining
~~~~~~~~~~~~

Skilgreinum margföldun á :math:`\mathbb{R}^2` þannig að

.. math::

 (a,b)(c,d)=(ac-bd, ad+bc).

Þegar hugsað er um :math:`\mathbb{R}^2` með þessari margföldun og venjulegri
samlagningu þá eru stökin í :math:`\mathbb{R}^2` kallaðar tvinntölur og mengi
þeirra er táknað með :math:`{\mathbb{C}}`. Þegar við viljum leggja áherslu á að
líta má á tvinntölu sem punkt í planinu :math:`\mathbb{R}^2` þá er talað um
tvinntalnaplanið.

Ritháttur. 
~~~~~~~~~~

Þegar fjallað er um tvinntölur þá er stakið :math:`(a,b)`
venjulega ritað sem :math:`a+ib`.

Hugsum okkur að :math:`i^2=-1`. Notum svo venjulega dreifireglu og að
:math:`i` víxlast við rauntölur til að reikna margfeldið

.. math::

 (a+ib)(c+id)=ac+iad+ibc+i^2bd=ac-bd+i(ad+bc).

Við höfum nú fengið aftur skilgreininguna á margfölduninni hér að ofan.

Setning
~~~~~~~

Eftirfarandi reiknireglur gilda um tvinntölur:

(i) :math:`\big((a+ib)+(c+id)\big)+(e+if)=(a+ib)+\big((c+id)+(e+if)\big)` (tengiregla fyrir samlagningu)

(ii) :math:`\big((a+ib)(c+id)\big)(e+if)=(a+ib)\big((c+id)(e+if)\big)` (tengiregla fyrir margföldun)

(iii) :math:`(a+ib)+(c+id)=(c+id)+(a+ib)` (víxlregla fyrir samlagningu)

(iv) :math:`(a+ib)(c+id)=(c+id)(a+ib)` (víxlregla fyrir margföldun)

(v) :math:`(a+ib)\big((c+id)+(e+if)\big)=(a+ib)(c+id)+(a+ib)(e+if)` (dreifiregla)

(vi) Talan :math:`0=0+i0` er samlagningarhlutleysa, þ.e.a.s. \ :math:`(a+ib)+0=a+ib`.

(vii) Talan :math:`1=1+i0` er margföldunarhlutleysa, þ.e.a.s. \ :math:`1(a+ib)=a+ib`.

Ritháttur.
~~~~~~~~~~ 

Þegar unnið er með tvinntölur þá er ekki gerður
greinarmunur á rauntölunni :math:`a` og tvinntölunni :math:`a+i0.` Því
getum við hugsað mengi rauntalna :math:`\mathbb{R}` sem hlutmengi í mengi
tvinntalna :math:`{\mathbb{C}}`. Sérhver rauntala er þannig líka tvinntala.

Setning
~~~~~~~

Ef :math:`z=a+ib\neq 0` er tvinntala þá á :math:`z` sér
margföldunarandhverfu sem er

.. math::

 z^{-1}=\frac{1}{z}=\frac{a}{a^2+b^2}+\frac{-b}{a^2+b^2}i.

   

Skilgreining og setning
~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`z` er tvinntala þá getum við
skilgreint heiltöluveldi :math:`z^n` af :math:`z` þannig að
:math:`z^0=1`, og ef :math:`n>0` þá er
:math:`z^n=z\cdot z\cdot\ldots\cdot z` (:math:`n` sinnum) og
:math:`z^{-n}=\big(z^{-1}\big)^n`. Venjulegar veldareglur gilda um
tvinntöluveldi, þ.e.a.s.

.. math::

   z^n\cdot z^m=z^{n+m}\qquad z^n/z^m=z^{n-m}\qquad z^n\cdot w^n=(zw)^{n}
   \qquad (z^n)^m=z^{nm}.

   

Skilgreining
~~~~~~~~~~~~

Ritum tvinntölu :math:`z` sem :math:`z=x+iy` þar sem
:math:`x` og :math:`y` eru rauntölur.

Talan :math:`x` kallast raunhluti :math:`z` og er táknaður með
:math:`\operatorname{Re\, } z`.

Talan :math:`y` kallast þverhluti :math:`z` og er táknaður með
:math:`\operatorname{Im\, } z`. (Athugið að þverhlutinn er rauntala.)

Sagt er að :math:`z` sé rauntala ef :math:`\operatorname{Im\, } z=0` en hrein þvertala ef
:math:`\operatorname{Re\, } z=0`.

Fyrir tvinntölu :math:`z=x+iy` skilgreinum við samok :math:`z` sem
tvinntöluna :math:`\overline{z}=x-iy`.

   

Reiknireglur. 
~~~~~~~~~~~~~

Um tvinntölu :math:`z=x+iy` gildir

.. math::

   \begin{aligned}
   \overline{(\overline{z})}&=z\\
   z\overline{z}&=(x+iy)(x-iy)=x^2+y^2\\
   z+\overline z&=2x=2\operatorname{Re\, } z\\
   z-\overline z&=2yi=(2\operatorname{Im\, } z)i\\
   \overline{z+w}&=\overline{z}+\overline{w}\\
   \overline{zw}&=\overline{z}\,\overline{w}\\
   \overline{z/w}&=\overline{z}/\overline{w}\end{aligned}

Skilgreining
~~~~~~~~~~~~

Lengd tvinntölu :math:`z=x+iy` er skilgreind sem
rauntalan :math:`|z|=\sqrt{x^2+y^2}=\sqrt{z\overline{z}}`.

Hugsum nú tvinntöluna :math:`z=x+iy` sem punkt :math:`(x,y)` í planinu.
Setjum :math:`r=\sqrt{x^2+y^2}=|z|`. Ritum nú punktinn :math:`(x,y)` sem
:math:`(x,y)=r(\cos \theta, \sin\theta)` (pólhnit). Þá er
:math:`z=|z|(\cos\theta+i\sin\theta)` og :math:`\theta` kallast
stefnuhorn tvinntölunnar :math:`z`. (Athugið að stefnuhorn er ekki
ótvírætt ákvarðað því ef :math:`\theta` er stefnuhorn þá er
:math:`\theta+k\cdot 2\pi` líka stefnuhorn.)

Formúla. 
~~~~~~~~

Lát :math:`z=x+iy\neq 0` vera tvinntölu í
:math:`{\mathbb{C}}\setminus \mathbb{R}_-` (:math:`\mathbb{R}_-` er mengi allra neikvæðra
rauntalna sem við samsömum við mengi allra tvinntalna á forminu
:math:`a+ib` með :math:`b=0` og :math:`a<0`). Stefnuhorn :math:`z` er
gefið með formúlunni

.. math::

 \theta=2\arctan\left(\tfrac{y}{|z|+x}\right).

Athugið að þessi formúla gefur gildi á :math:`\theta` þannig að
:math:`-\pi<\theta<\pi`.

Skilgreining
~~~~~~~~~~~~

Ef :math:`z` og :math:`w` eru tvær tvinntölur þá er
fjarlægðin á milli þeirra skilgreind sem rauntalan :math:`|z-w|`.

Setning
~~~~~~~

Fyrir sérhverjar tvinntölur :math:`z` og :math:`w` gildir
að

.. math::

 |z+w|\leq |z|+|w|.

Athugið að :math:`|z+w|=|z|+|w|` ef og aðeins ef til er jákvæð rauntala
:math:`a` þannig að :math:`w=az`.

Rúmfræðileg túlkun margföldunar. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ef :math:`z` og :math:`w` eru tvær
tvinntölur með lengdir :math:`|z|` og :math:`|w|` og stefnuhornin
:math:`\alpha` og :math:`\beta`, þá er

.. math::

 zw=|z||w|\big(\cos(\alpha+\beta)+i\sin(\alpha+\beta)\big).

Það segir okkur að lengd margfeldisins er margfeldi lengda :math:`z` og
:math:`w` (þ.e.a.s. :math:`|zw|=|z||w|`) og að stefnuhorn margfeldisins
sé summa stefnuhorna :math:`z` og :math:`w`.

Sérstaklega gildir Regla de Moivre sem segir að

.. math::

 (\cos \theta+i\sin\theta)^n=\cos(n\theta)+i\sin(n\theta).

Skilgreining
~~~~~~~~~~~~

Lína í tvinntalnaplaninu :math:`{\mathbb{C}}` er mengi allra
tvinntalna :math:`z=x+iy` sem uppfylla jöfnu af taginu
:math:`ax+by+c=0`, þar sem :math:`a,b,c` eru rauntölur.

Hringur í tvinntalnaplaninu er mengi allra punkta sem er í gefinni
fastri fjarlægð (geisli, radíus) frá gefnum föstum punkti :math:`m`
(miðjunni). Hringur með miðju í :math:`m` og geisla :math:`r` er mengið
:math:`\{z\mid |z-m|=r\}`.

Skilgreining
~~~~~~~~~~~~

Einingarhringurinn :math:`\mathbb{T}` í :math:`{\mathbb{C}}` er mengi
allra tvinntalna sem hafa lengd 1. (Einnig má lýsa honum sem mengi allra
tvinntalna sem eru í fjarlægð 1 frá :math:`0`. Einingarhringurinn er
hringur með miðju í 0 og geisla 1.)

Setning
~~~~~~~

Sérhverri línu og sérhverjum hring má lýsa með jöfnu af
taginu

.. math::

 \alpha|z|^2+\overline{\beta} z+\beta\overline{z}+\gamma=0,

þar sem :math:`\alpha` og :math:`\gamma` eru rauntölur og :math:`\beta`
er tvinntala.

Öfugt, ef við fáum slíka jöfnu þá lýsir hún:

(i) línu ef :math:`\alpha=0` og :math:`\beta \neq 0`

(ii) hring ef :math:`\alpha\neq 0` og :math:`|\beta|^2-\alpha\gamma>0` (og miðjan er :math:`m=-\beta/\alpha` og geislinn er :math:`r=\sqrt{|\beta|^2-\alpha\gamma}/|\alpha|`);

(iii) stökum punkti ef :math:`\alpha\neq 0` og :math:`|\beta|^2-\alpha\gamma=0` (punkturinn er :math:`m=-\beta/\alpha`)

(iv) tóma menginu ef :math:`\alpha\neq 0` og :math:`|\beta|^2-\alpha\gamma<0`;

(v) öllu planinu :math:`{\mathbb{C}}` ef :math:`\alpha=\beta=\gamma=0`.

Margliður, ræð föll og veldisvísisföll
--------------------------------------

   
Skilgreining (Sjá §1.4) 
~~~~~~~~~~~~~~~~~~~~~~~~

Getum skilgreint margliður með tvinntölustuðlum á sama hátt og margliður með rauntölustuðlum. Margliða
með tvinntölustuðlum er stærðtákn á forminu

.. math::

 P(z)=a_nz^n+a_{n-1}z^{n-1}+\cdots+a_1z+a_0,

þar sem stuðlarnir :math:`a_0, a_1, \ldots, a_{n-1}, a_n` eru
tvinntölur.

Þegar sett er inn ákveðin tvinntala í stað :math:`z` í þessari stæðu og
reiknað þá fæst út tvinntala. Margliðan gefur því fall
:math:`P:{\mathbb{C}}\rightarrow {\mathbb{C}}`.

Margliður. (Sjá §1.4)
~~~~~~~~~~~~~~~~~~~~~

Tvinntölumargliður hegða sér
um flest eins og rauntölumargliður. Sérstaklega þá virkar deiling
tvinntölumargliða eins og deiling rauntölumargliða.

Fáum að ef :math:`P` er margliða af stigi :math:`n` og :math:`Q` er
margliða af stigi :math:`m` þá eru til ótvírætt ákvarðaðar margliður
:math:`S` og :math:`R` þannig að stig :math:`R(z)` er minna en :math:`m`
og

.. math::

 P(z)=Q(z)S(z)+R(z).

Sagt er að :math:`Q` gangi upp í :math:`P` ef :math:`R` er
núllmargliðan.

Sérstaklega gildir að :math:`\alpha` er núllstöð eða rót margliðunnar
:math:`P` (þ.e.a.s. :math:`P(\alpha)=0`) ef og aðeins ef
:math:`z-\alpha` gengur upp í :math:`P`.

Setning (Undirstöðusetning algebrunnar) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sérhver margliða af stigi :math:`\geq 1` með tvinntölustuðla hefur núllstöð í
:math:`{\mathbb{C}}`.

Skilgreining og setning (Sjá §1.4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hugsum okkur að :math:`\alpha` sé núllstöð margliðu :math:`P` og :math:`j` sé hæsta talan þannig að
:math:`(z-\alpha)^j` gengur upp í :math:`P`,
þ.e.a.s. \ :math:`P(z)=(z-\alpha)^jQ(z)` þar sem
:math:`Q(\alpha)\neq 0`. Þá segjum við að :math:`\alpha` sé
:math:`j`-föld núllstöð og köllum :math:`j` margfeldni núllstöðvarinnar
:math:`\alpha`.

Það er afleiðing af Undirstöðusetningu algebrunnar að ef :math:`P` er
margliða af stigi :math:`m\geq 1` með núllstöðvar
:math:`\beta_1, \ldots, \beta_k` sem hafa margfeldni
:math:`m_1,\ldots, m_k` þá er :math:`m=m_1+\cdots+m_k` og

.. math::

 P(z)=A(z-\beta_1)^{m_1}\cdots(z-\beta_k)^{m_k},

þar sem :math:`A` er fasti.

Skilgreining og setning (Sjá §1.3) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(i) Jafnan :math:`z^n=1` hefur :math:`n` ólíkar lausnir sem kallast :math:`n`-tu einingarrætur og þær eru

.. math::

 z_k=\cos (k\cdot 2\pi/n)+i\sin (k\cdot 2\pi/n),\qquad k=0, 1, \ldots, n-1.

(ii) Jafna af taginu :math:`z^n=\alpha=|\alpha|(\cos\phi+i\sin\phi)` hefur :math:`n` ólíkar lausnir og þær eru

.. math::

   z_k=|\alpha|^{1/n}\big(\cos (\phi/n+k\cdot 2\pi/n)+
   i\sin (\phi/n+k\cdot 2\pi/n)\big),\qquad k=0, 1, \ldots, n-1.

(iii) Jafna af taginu :math:`z^2=w=u+iv` hefur tvær lausnir sem við köllum kvaðratrætur :math:`w`. Ef :math:`v\neq 0` má rita þær:

.. math::

  z= \pm\left(\sqrt{\tfrac{1}{2}(|w|+u)}+i\;\mathrm{sign}(v)\sqrt{\tfrac{1}{2}(|w|-u)}\right).

þar sem

.. math::

  {{\operatorname{sign}}}(t)=
   \begin{cases}
   1, &t\geq 0,\\
   -1,&t<0.
   \end{cases}

Ef :math:`v=0` fæst tilfellið í liðnum á undan.

(iv)  (Sjá §1.4)  Jafnan :math:`az^2+bz+c=0` með :math:`a\neq 0` (og :math:`a, b, c` tvinntölur) hefur lausnir

.. math::

    z_1=\frac{-b+\sqrt{D}}{2a}\qquad\mbox{ og }\qquad z_2=\frac{-b-\sqrt{D}}{2a}

þar sem :math:`D=b^2-4ac` og :math:`\sqrt{D}` táknar aðra lausn jöfnunnar :math:`z^2=D` (sjá aðvörun fyrir neðan). Ef :math:`D` er rauntala og :math:`D\geq 0` tökum við kvaðratrót eins og við erum vön en ef :math:`D<0` má rita lausnirnar

.. math::

    z_1=\frac{-b+i\sqrt{|D|}}{2a}\qquad\mbox{ og }\qquad z_2=\frac{-b-i\sqrt{|D|}}{2a}

.. warning::

  Ef :math:`z` er tvinntala hefur táknmálið :math:`\sqrt{z}` almennt ekki merkingu. Ef það er notað þarf ávallt að tilgreina fyrir hvað það stendur.

Skilgreining
~~~~~~~~~~~~

Rætt fall er kvóti tveggja margliða, :math:`R(z)=P(z)/Q(z)`.  

Stofnbrotaliðun. (Sjá §1 1.5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`R(z)=P(z)/Q(z)` vera rætt fall þar sem stig :math:`P(z)` er lægra en stig :math:`Q(z)`.  

Ef :math:`Q(z)=a(z-\alpha_1)\cdots(z-\alpha_m)` þar sem :math:`\alpha_1, \ldots, \alpha_k` eru ólíkar tvinntölur þá eru til fastar :math:`A_1, \ldots, A_k` þannig að 

.. math::

  R(z)=\frac{A_1}{z-\alpha_1}+\cdots+\frac{A_k}{z-\alpha_k}.

Stuðlarnir eru gefnir með

.. math::

  A_j = \frac{P(\alpha_j)}{Q'(\alpha_j)},
  
:math:`j=1,..k`. 

.. important::

  Við getum diffrað tvinngildar margliður líkt og raungildar margliður með því að nota

  .. math::

    \frac{dz^n}{dz} = n z^{n-1}

  ásamt því að diffrun er línuleg. Réttlæting kemur síðar. 
  
Ef :math:`Q(z)=a(z-\alpha_1)^{m_1}\cdots(z-\alpha_k)^{m_k}`  og :math:`\alpha_1, \ldots, \alpha_k` eru ólíkar tvinntölur þá eru til fastar
:math:`A_{11},\ldots, ,A_{m_11}, A_{12},\ldots, ,A_{m_12}, \ldots, A_{1k},\ldots, ,A_{m_1k}` þannig að 

.. math::

  \begin{aligned}
   \dfrac{P(z)}{Q(z)}&=
   \dfrac{A_{1,0}}{(z-\alpha_1)^{m_1}}+\cdots+\dfrac{A_{1,m_1-1}}{(z-\alpha_1)}\\
   &+\dfrac{A_{2,0}}{(z-\alpha_2)^{m_2}}+\cdots+\dfrac{A_{2,m_2-1}}{(z-\alpha_2)}
   \\
   &\qquad \vdots\qquad\qquad\vdots\qquad \qquad \vdots\\
   &+\dfrac{A_{k,0}}{(z-\alpha_k)^{m_k}}+\cdots+\dfrac{A_{k,m_k-1}}{(z-\alpha_k)}\end{aligned}

Stuðlarnir eru gefnir með 

.. math::

  A_{j,\ell}=\left.\dfrac 1{\ell!}
   \bigg(\dfrac {d}{dz}\bigg)^{\ell}\bigg(
   \dfrac{P(z)}{q_j(z)}\bigg)\right|_{z=\alpha_j},

:math:`j=1,\dots,k, \ell=0,\dots,m_k-1` þar sem :math:`q_j(z) = Q(z)/(z-\alpha_j)^{m_j}`.

Skilgreining (Sjá §1.6)
~~~~~~~~~~~~~~~~~~~~~~~

Ritum tvinntölu :math:`z` sem
:math:`z=x+iy` þar sem :math:`x` og :math:`y` eru rauntölur. Skilgreinum
veldisvísisfallið

.. math::

 e^z=e^{x+iy}=e^x(\cos y+i\sin y).

Reiknireglur. (Sjá §1.6) 
~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`z` og :math:`w` vera
tvinntölur. Þá gildir að

.. math::

 e^ze^w=e^{z+w}.

Ef :math:`k` er heiltala þá er :math:`e^{z+k\cdot(2\pi i)}=e^z`, þanng
að :math:`e^z` er lotubundið fall með lotu :math:`2\pi i`. Ennfremur
gildir að

.. math::

 \overline{e^z}=e^{\overline{z}}\qquad |e^z|=e^{\operatorname{Re\, } z}\qquad |e^{iy}|=1.

Fallegasta jafna stærðfræðinnar.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

    .. math::
        e^{i\pi}+1=0

Jöfnur Eulers. (Sjá §1.6)
~~~~~~~~~~~~~~~~~~~~~~~~~

 Fyrir rauntölu :math:`\theta` er

.. math::

   \cos\theta=\frac{e^{i\theta}+e^{-i\theta}}{2}\qquad\mbox{ og }\qquad
   \sin\theta=\frac{e^{i\theta}-e^{-i\theta}}{2i}.

Skilgreining  (Sjá §1.6)
~~~~~~~~~~~~~~~~~~~~~~~~

Hægt er að útvíkka hornaföllin og
breiðbogaföllin yfir á allt tvinntalnaplanið með formúlunum

.. math::

   \cos z=\frac{e^{iz}+e^{-iz}}{2}\qquad\mbox{ og }\qquad
   \sin z=\frac{e^{iz}-e^{-iz}}{2i},

 og

.. math::

   \cosh z=\frac{e^{z}+e^{-z}}{2}\qquad\mbox{ og }\qquad
   \sinh z=\frac{e^{z}-e^{-z}}{2},

og síðan eru :math:`\tan z, \cot z, \tanh z` og :math:`\coth z`
skilgreind á augljósan hátt. (Ef :math:`z` er rauntala þá fást sömu
gildi og við þekkjum.)

:math:`\mathbb{R}`- og :math:`{\mathbb{C}}`-línulegar varpanir
--------------------------------------------------------------  

Skilgreining og setning (Sjá §1.7) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vörpun :math:`L:{\mathbb{C}}\rightarrow {\mathbb{C}}` er sögð línuleg (nákvæmar,
:math:`\mathbb{R}`-línuleg) ef um sérhverjar tvinntölur :math:`z` og :math:`w`
og sérhverja rauntölu :math:`c` gildir að

.. math::

 L(z+w)=L(z)+L(w)\qquad \mbox{ og }\qquad L(cz)=cL(z).

Setning
~~~~~~~

Látum :math:`L:{\mathbb{C}}\rightarrow {\mathbb{C}}` vera
línulega vörpun. Samsömum tvinntölu :math:`x+iy` við vigur
:math:`(x,y)\in \mathbb{R}^2`. Nú má hugsa :math:`L` sem vörpun
:math:`\mathbb{R}^2\rightarrow \mathbb{R}^2`. Þá er :math:`L` línuleg vörpun og til eru
rauntölur :math:`a, b, c, d` þannig að fyrir allar rauntölur :math:`x`
og :math:`y` er (ef ekki er gerður munur á dálkvigrum og línuvigrum)

.. math::

   L(x,y)=(ax+by, cx+dy)=\begin{bmatrix}a&b\\c&d\end{bmatrix}
   \begin{bmatrix}x\\y\end{bmatrix}.

Ef við ritum :math:`A=\frac{1}{2}\big((a+d)+i(c-b)\big)` og
:math:`B=\frac{1}{2}\big((a-d)+i(c+b)\big)` þá gildir fyrir sérhverja
tvinntölu :math:`z=x+iy` að

.. math::

 L(z)=Az+B\overline{z}.

Skilgreining
~~~~~~~~~~~~

Vörpun :math:`L:{\mathbb{C}}\rightarrow {\mathbb{C}}` er sögð
:math:`{\mathbb{C}}`-línuleg ef um sérhverjar tvinntölur :math:`z` og :math:`w` og
sérhverja tvinntölu :math:`c` gildir að

.. math::

 L(z+w)=L(z)+L(w)\qquad \mbox{ og }\qquad L(cz)=cL(z).

(Athugið að sérhver :math:`{\mathbb{C}}`-línuleg vörpun er líka
:math:`\mathbb{R}`-línuleg, en ekki öfugt.)

Setning
~~~~~~~

Sérhverja :math:`{\mathbb{C}}`-línulega vörpun má
rita sem :math:`L(z)=Az` þar sem :math:`A` er tvinntala.

Skilgreining
~~~~~~~~~~~~

Vörpun :math:`{\mathbb{C}}\to {\mathbb{C}}` af gerðinni
:math:`z\mapsto z+a`, þar sem :math:`a\in {\mathbb{C}}` nefnist hliðrun.

Vörpun af gerðinni :math:`z\mapsto az`, nefnist snúningur, ef
:math:`a\in {\mathbb{C}}` og :math:`|a|=1`, hún nefnist stríkkun ef :math:`a\in
\mathbb{R}` og :math:`|a|>1` og herping, ef :math:`a\in \mathbb{R}` og :math:`|a|<1`, en
almennt nefnist hún snústríkkun ef :math:`a\in {\mathbb{C}}\setminus \{0\}`.

Vörpunin :math:`{\mathbb{C}}\setminus \{0\} \to {\mathbb{C}}\setminus \{0\}`,
:math:`z\mapsto 1/z` nefnist umhverfing.

Skilgreining
~~~~~~~~~~~~

Vörpun :math:`f:{\mathbb{C}}\rightarrow{\mathbb{C}}` af gerðinni

.. math::

 f(z)=\dfrac{az+b}{cz+d}, \qquad ad-bc\neq 0, \quad a,b,c,d\in {\mathbb{C}},

kallast brotin línuleg vörpun (eða brotin línuleg færsla eða
Möbiusarvörpun). Við sjáum að :math:`f(z)` er skilgreint fyrir öll
:math:`z\in {\mathbb{C}}`, ef :math:`c=0`, en fyrir öll :math:`z\neq -d/c`, ef
:math:`c\neq 0`.

Setning
~~~~~~~

Sérhver brotin línuleg vörpun er samskeyting af hliðrunum,
snústríkunum og umhverfingum.

Setning
~~~~~~~

Sérhver brotin línuleg vörpun varpar hring í :math:`{\mathbb{C}}` á
hring eða línu og hún varpar línu á hring eða línu.

.. ggb:: 2384599
  :width: 700
  :height: 364
  :img: stikaferill.png
  :imgwidth: 4cm
  :zoom_drag: true 


.. ggb:: bbhtpsvx
  :width: 700
  :height: 400
  :img: polarggb.png
  :imgwidth: 4cm
  :zoom_drag: true 

Hér má sjá hvert brotin línuleg vörpun :math:`f` með stika :math:`a,b,c,d` líkt og að ofan, varpar línunni Form1 og hringnum Form2 í tvinntalaplaninu. Hægt er að breyta gildum stikanna með því að draga þá til með músinni.
