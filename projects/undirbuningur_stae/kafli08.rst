Vigrar
======
.. _s.Vigrar:

Skilgreining
------------
:hover:`Vigrar, vigur` er stærðfræðilegt hugtak fyrir stærð sem hefur bæði lengd og stefnu.
Þeir eru jafnan teiknaðir sem örvar í hnitakerfi og lýst með hnitum.
Hnit vigurs eru venjulegar tölur, líka kallaðar :hover:`skalarstærðir, tölustærð`, og lýsa staðsetningu endapunkts miðað við upphafspunkt.
Hvert hnit er tengt einum ás í hnitakerfinu sem notað er og stærð hnitsins (tölunnar) lýsir lengd vigursins í þá átt.

Vigrar eru oftast táknaðir með striki eða ör fyrir ofan bókstafinn, :math:`\overline{a}` , :math:`\vec{a}` , en sumir setja strikið undir, :math:`\underline{a}` .
Í kennslubókum eru vigrar stundum feitletraðir: :math:`\boldsymbol{a}`.

Lengd vigra er táknuð með lóðréttum strikum, algildismerkjum, :math:`|\overline{a}|` , eða einfaldlega bókstafnum án yfirstriksins, :math:`a` .
Þegar vísað er í lengd vigurs eftir einhverjum ás, :hover:`þátt, þáttur` hans, er það sýnt með því að merkja með heiti ássins í :hover:`lágvísi, lágvísir`; :math:`a_x` er lengd vigursins :math:`\overline{a}` í stefnu :math:`x` - áss.
Þættir vigra eru ekki vigrar sjálfir, heldur tölur.


.. figure:: ./myndir/rumfraedi/vigur.svg
   :width: 60%
   :align: center

Yfirleitt er notað rétthyrnt hnitakerfi (einnig nefnt :hover:`kartesískt, kartesk slétta`).
Vigurinn á myndinni hefur lengd 4 eftir x-ásnum og 3 eftir y-ásnum, svo hnit hans eru:

.. math::
  \overline{a} = (a_x,a_y) = (4,3) = \begin{pmatrix} 4 \\ 3 \end{pmatrix}

Lengd vigursins sjálfs er reiknuð með jöfnu Pýþagórasar, :math:`|\overline{a}| = a = \sqrt{a_x^2 + a_y^2}` .
Vigurinn á myndinni hefur því lengdina :math:`a = \sqrt{4^2 + 3^2} = 5` .

.. note::
  Stærð og stefna vigurs er óháð því hvar í hnitakerfinu hann er.

Algengt er að láta vigra liggja frá upphafspunkti hnitakerfisins (stöðu- eða staðarvigur) en það er hægt að reikna vigra á milli gefinna upphafs- og endapunkta.
Vigurinn frá punktinum :math:`A=(x_1,y_1)` til punktsins :math:`B=(x_2,y_2)` er

.. math::
  \overline{AB} = (x_2-x_1,y_2-y_1) = \begin{pmatrix} x_2-x_1 \\ y_2-y_1 \end{pmatrix}

.. tip::
  Reiknum vigurinn frá punktinum :math:`A=(-1,7)` til punktsins :math:`B=(5,2)` .

	.. math::
		\begin{aligned}
			\overline{AB} &= \begin{pmatrix} x_2-x_1 \\ y_2-y_1 \end{pmatrix}\\
			&= \begin{pmatrix} 5-(-1) \\ 2-7 \end{pmatrix} \\
			&= \begin{pmatrix} 6 \\ -5 \end{pmatrix}
		\end{aligned}

	.. figure:: ./myndir/vigurtveirpkt.svg
		:align: center
		:width: 60%

  Vigurinn :math:`\begin{pmatrix} 6 \\ -5 \end{pmatrix}` er sá sami, hvort sem hann liggur á milli :math:`A` og :math:`B` eða frá upphafspunktinum til punktsins :math:`(6,-5)` .


Stundum er talað um að vigur hafi :hover:`hallatölu, hallatala` : :math:`h=\frac{a_y}{a_x}` , ef :math:`a_x\neq 0` .
Tveir vigrar eru :hover:`samsíða` ef þeir hafa sömu hallatölu.

.. tip::
  Finnum vigur sem er samsíða :math:`\overline{a}=(-1,6)` og hefur lengdina 9.

  Hallatala :math:`\overline{a}` er :math:`h_{\bar{a}}=\frac{a_y}{a_x}=\frac{6}{-1}=-6` .
  Þá vitum við að vigurinn sem við leitum að, :math:`b` , uppfyllir það sama:

  .. math::
    h_{\bar{b}}=\frac{b_y}{b_x}=-6

  sem er jafngilt því að :math:`b_y=-6b_x` .

  Skilyrðið að :math:`\overline{b}` þurfi að hafa lengdina 9 gefur að:

  .. math::
    |\overline{b}| = \sqrt{b_x^2+b_y^2} =9

  Setjum :math:`b_y=-6b_x` inn og fáum:

  .. math::
    \begin{aligned}
      9 &= \sqrt{b_x^2+b_y^2}\\
      &=\sqrt{b_x^2+(-6b_x)^2} \\
      &= \sqrt{b_x^2+36b_x^2} \\
      &=\sqrt{37b_x^2} \\
      &=b_x\sqrt{37} \\
      b_x&=\frac{9}{\sqrt{37}} \approx 1.480\\
      b_y&= -6b_x = \frac{-54}{\sqrt{37}} \approx -8.878
    \end{aligned}

  Vigur sem er samsíða :math:`\overline{a}=(-1,6)` og hefur lengdina 9 er því

  .. math::
    \overline{b}= \begin{pmatrix} \frac{9}{\sqrt{37}} \\  \frac{-54}{\sqrt{37}} \end{pmatrix}

Að liða vigra
-------------
Vigra er líka hægt að tákna með lengd og stefnuhorni.
Hornið :math:`\theta` er skilgreint frá jákvæðum x-ás og að vigrinum.
Með þessum upplýsingum er hægt að liða vigurinn eftir x- og y-ás með því að nota hornaföll.

Þættir vigursins eru föll af stefnuhorninu sem er oft merkt :math:`\theta` eða :math:`\phi` :

.. math::
  a_x = a\cos(\theta) \\
  a_y = a\sin(\theta)

þar sem :math:`a=|\overline{a}|`.

Stefnuhorn vigurs :math:`\overline{a} = (a_x,a_y)` má því reikna:

.. math::

	\frac{a_y}{a_x} = \frac{a\sin(\theta)}{a\cos(\theta)} = \tan(\theta)


.. figure:: ./myndir/rumfraedi/mynd-vigur.svg
   :width: 60%
   :align: center

Einingarvigrar
--------------
Einingarvigrar eru vigrar sem hafa lengdina 1.
Vigrarnir

.. math::
 \begin{aligned}
 \hat{\imath} &= \begin{pmatrix} 1 \\0 \\0 \end{pmatrix} \\
 \hat{\jmath} &= \begin{pmatrix} 0 \\1 \\0 \end{pmatrix} \\
 \hat{k} &= \begin{pmatrix} 0\\0 \\1 \end{pmatrix} \\
 \end{aligned}

liggja samsíða :math:`x` - , :math:`y` - og  :math:`z` -  ásunum í rétthyrndu hnitakerfi .
Þeir eru líka táknaðir:

.. math::
 \begin{gather}
 \hat{e}_x, \quad \hat{e}_y, \quad \hat{e}_z
 \end{gather}

.. figure:: ./myndir/rumfraedi/einingarvigrar.svg
  :width: 60%
  :align: center

Einingarvigrarnir :math:`\hat{e}_x, \hat{e}_y` og :math:`\hat{e}_z` eru :hover:`línulega óháðir, línulega óháður`, sem þýðir að engan þeirra er hægt að mynda úr hinum tveimur með samlagningu þeirra eða margföldun með tölu.
Hvernig sem þú teygir á og raðar saman :math:`\hat{\imath}` og :math:`\hat{\jmath}` færðu aldrei út :math:`\hat{k}` .
Þessi eiginleiki kemur til vegna þess að einingarvigrarnir eru allir hornréttir á hvorn annan.

Alla vigra má skrifa sem skalarstærðir margfaldaðar við einingarvigrana:

.. math::
  \overline{a} = (a_x, \; a_y, \; a_z ) = a_x \hat{\imath} + a_y \hat{\jmath} + a_z \hat{k}

Samlagning vigra
----------------
Þegar vigrar eru lagðir saman eru hnit eftir hverjum ás fyrir sig lögð saman.
Summa tveggja vigra :math:`\overline{a} = (a_x,a_y)` og :math:`\overline{b} = (b_x,b_y)` er:

.. math::
  \overline{c} = \overline{a} + \overline{b} = (a_x + b_x, a_y +b_y) = \begin{pmatrix} a_x+b_x \\ a_y+b_y \end{pmatrix}

.. tip::
  Leggjum saman vigrana :math:`\overline{a}=(4,3)` og :math:`\overline{b}=(1,3)` :

  .. math::
    \overline{a}+\overline{b}=(4,3) + (1,3) = (4+1, 3+3) = (5,6)

Myndrænt má ímynda sér að upphafspunktur seinni vigursins sé settur í endapunkt fyrri vigursins,
og summa þeirra er frá upphafspunkti fyrri vigursins til endapunkts þess seinni.

.. figure:: ./myndir/rumfraedi/vigrasamlagning.svg
   :width: 60%
   :align: center

.. note::
  Þó að :math:`\overline{c} = \overline{a} + \overline{b}` þýðir það **ekki** að :math:`c = a + b`.

  Í dæminu hér á undan er til dæmis

  .. math::
    c = |\overline{c}| = \sqrt{5^2+6^2} \approx 7,8 \\
    a + b = \sqrt{4^2+3^2} + \sqrt{1^2+3^2} \approx 8,2

--------------------------------

Um samlagningu vigra gilda eftirfarandi reglur:

.. math::
  \begin{aligned}
    \overline{a} +\overline{b} &= \overline{b} + \overline{a} & \text{Víxlregla}\\
    (\overline{a}+\overline{b})+\overline{c} &= \overline{a} + (\overline{b}+\overline{c}) & \text{Tengiregla}
  \end{aligned}

--------------------------------

.. tip::
  Höfum þrjá punkta:

  .. math::
    \begin{aligned}
    A&=(x_1,y_1)=(1,2) \\
    B&=(x_2,y_2)=(4,5) \\
    C&=(x_3,y_3)=(3,-1)
    \end{aligned}

  Reiknum vigrana :math:`\overline{AB}, \overline{AC} \text{ og } \overline{BC}` :

  .. math::
    \begin{aligned}
      \overline{AB} &= \begin{pmatrix} x_2-x_1 \\ y_2-y_1 \end{pmatrix}\\
      &=\begin{pmatrix} 4-1 \\5-2\end{pmatrix} =\begin{pmatrix} 3 \\3\end{pmatrix} \\
      & \\
      \overline{AC} &= \begin{pmatrix}x_3-x_1\\ y_3-y_1 \end{pmatrix}\\
      &=\begin{pmatrix} 3-1 \\(-1)-2\end{pmatrix} =\begin{pmatrix} 2 \\-3\end{pmatrix} \\
      & \\
      \overline{BC} &= \begin{pmatrix}x_3-x_2\\ y_3-y_2 \end{pmatrix}\\
      &=\begin{pmatrix} 3-4 \\(-1)-5\end{pmatrix} =\begin{pmatrix} -1 \\-6\end{pmatrix} \\
    \end{aligned}

  .. figure:: ./myndir/rumfraedi/innskots.svg
    :align: center
    :width: 50%

  Hér eru punktarnir teiknaðir inn ásamt vigrunum :math:`\overline{AB}, \overline{AC} \text{ og } \overline{BC}` .

Af þessu dæmi má sjá *innskotsregluna* :

.. math::
  \overline{AC} = \overline{AB} + \overline{BC}


Margföldun vigra
----------------
Þegar vigur :math:`\overline{v}` er margfaldaður með tölu :math:`s` er hver þáttur vigursins margfaldaður með tölunni:

.. math::
    \begin{aligned}
        s\cdot\overline{v}  &= s\cdot(v_x, v_y, v_z)  \\
        &= (s \cdot v_x, s \cdot v_y, s \cdot v_z)
    \end{aligned}

Margfeldi vigra er tvenns konar, :hover:`innfeldi (punktfeldi), innfeldi`, og :hover:`krossfeldi`.

----------------

**Innfeldi** tveggja vigra er táknað með punkti og útkoman er *tala*: :math:`\overline{a} \cdot \overline{b}` .
Ef þættir vigranna eru þekktir er innfeldið:

.. math::
  \overline{a} \cdot \overline{b} = a_x b_x + a_y b_y

.. tip::
    Reiknum innfeldi vigranna :math:`\overline{a}=(7,8)` og :math:`\overline{b}=(-1,3)`

    **Lausn**

    .. math::
      \overline{a} \cdot \overline{b} = a_x b_x + a_y b_y = 7\cdot (-1)+ 8\cdot 3 = -7+24 =17

Ef vigrarnir eru gefnir með lengd og stefnuhorni er innfeldið:

.. math::
  \overline{a} \cdot \overline{b} = a b \cos{\phi}

þar sem :math:`\phi` er hornið milli :math:`\overline{a}` og :math:`\overline{b}` þegar þeir hafa sama upphafspunkt.

.. warning::
  **Tveir vigrar eru hornréttir ef innfeldi þeirra er núll.**

.. tip::
    Reiknum hornið á milli vigranna :math:`\overline{a}=(2,4)` og :math:`\overline{b}=(4,2)` :

    .. figure:: ./myndir/rumfraedi/innfeldi.svg
      :align: center
      :width: 60%

    **Lausn**

    Við vitum að :math:`\overline{a} \cdot \overline{b} = a b \cos{\phi}` , þar sem :math:`a` og :math:`b` eru lengdir vigranna.
    Lengdirnar eru:

    .. math::
      \begin{aligned}
        a = \sqrt{a_x^2 + a_y^2} = \sqrt{2^2 + 4^2} = \sqrt{20} \\
        b = \sqrt{b_x^2 + b_y^2} = \sqrt{4^2 + 2^2} = \sqrt{20}
      \end{aligned}

    Reiknum innfeldi vigranna:

    .. math::
      \overline{a} \cdot \overline{b} = a_x b_x + a_y b_y = 2\cdot 4+ 4\cdot 2 = 16

    Því er

    .. math::
      \begin{aligned}
        \overline{a} \cdot \overline{b} &= a b \cos{\phi} \\
        \cos{\phi} &= \frac{\overline{a} \cdot \overline{b}}{a b} = \frac{16}{\sqrt{20} \cdot \sqrt{20}} = \frac{16}{20}\\
        \phi &= 36.8 ° = 0.644
      \end{aligned}

------------------------------------------------------------

**Krossfeldi** tveggja vigra er táknað með krossi og útkoman er nýr *vigur*: :math:`\overline{c} = \overline{a} \times \overline{b}` .
:hover:`Krossfeldi, krossfeldi` eru reiknuð með þáttum vigranna, það er vigrum gefnum á forminu :math:`\overline{a} = a_x \hat{\imath} + a_y \hat{\jmath} + a_z \hat{k}` .

.. math::
  \begin{aligned}
  \overline{a} \times \overline{b} &= (a_x \hat{\imath} + a_y \hat{\jmath} + a_z \hat{k}) \times (b_x \hat{\imath} + b_y \hat{\jmath} + b_z \hat{k}) \\
  &= (a_y b_z - a_z b_y)\hat{\imath} + (a_z b_x - a_x b_z)\hat{\jmath} + (a_x b_y - a_y b_x)\hat{k} \\
  \end{aligned}

.. figure:: ./myndir/rumfraedi/krossfeldi.svg
   :width: 60%
   :align: center

Útkoma krossfeldisins er vigur sem er hornréttur á bæði :math:`a` og :math:`b`.
Til að ákvarða sefnu vigursins getum við notað **hægri** handar regluna.

.. figure:: ./myndir/rumfraedi/hhr.svg
    :width: 90%
    :align: center

Lengd krossfeldis :math:`\overline{a} \text{ og } \overline{b}` má reikna úr frá lengdum vigranna og horninu á milli þeirra.

.. math::
  |\overline{a} \times \overline{b}| = |\overline{a}| |\overline{b}| \sin(\phi)

.. note::
  Þegar krossfeldi er reiknað skiptir máli hvor vigurinn er á undan!

  .. math::
    \overline{a} \times \overline{b} = - \overline{b} \times \overline{a}


.. tip::
    Reiknum krossfeldi vigranna :math:`\overline{a}=(1,2,3)` og :math:`\overline{b}=(4,5,6)`.

    **Lausn**

    .. math::
      \begin{aligned}
        \overline{a} \times \overline{b} &= (a_y b_z - a_z b_y)\hat{\imath} + (a_z b_x - a_x b_z)\hat{\jmath} + (a_x b_y - a_y b_x)\hat{k} \\
        &= (2\cdot 6-3\cdot 5)\hat{\imath} + (3\cdot 4 - 1 \cdot 6) \hat{\jmath} + ( 1\cdot 5 - 2\cdot 4) \hat{k}\\
        &= -3 \hat{\imath} +6 \hat{\jmath} - 3\hat{k}\\
        &= (-3,6,-3)
      \end{aligned}


Flatarmyndir
------------

Ef hliðar þríhyrnings eru gefnar með vigrunum :math:`\overline{a}` og :math:`\overline{b}` er hægt að reikna hornið :math:`\theta` .
Flatarmálið er þá :math:`F=\frac{1}{2}|\overline{a}| \cdot |\overline{b}| \cdot \sin(\theta)` .

.. figure:: ./myndir/rumfraedi/fl_thri2.svg
	:align: center
	:width: 40%

Ef hliðar samsíðungs eru gefnar með vigrunum :math:`\overline{a}` og :math:`\overline{b}` er hægt að reikna hornið :math:`\theta` .
Flatarmálið er þá :math:`F=|\overline{a}| \cdot |\overline{b}| \cdot \sin(\theta)` og ummálið er :math:`U=2|\overline{a}|+2|\overline{b}|` .

.. figure:: ./myndir/rumfraedi/fl_sams2.svg
	:align: center
	:width: 40%
