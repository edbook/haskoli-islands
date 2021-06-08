Rúmmál, massi og massamiðja
===========================

*The fact that we live at the bottom of a deep gravity well, on the surface of a 
gas covered planet going around a nuclear fireball 90 million miles away and think 
this to be normal is obviously some indication of how skewed our perspective tends to be.*

\- Douglas Adams, The Salmon of Doubt: Hitchhiking the Galaxy One Last Time

.. todo::
    myndir/geogebra

.. index::
    rúmmál
    
Rúmmál, lengd og flatarmál
--------------------------

Rúmmál rúmskika
~~~~~~~~~~~~~~~~~~~~~~

Rúmskiki :math:`D` liggur á milli plananna :math:`x=a` og :math:`x=b`.
Táknum með :math:`A(x)` flatarmál þversniðs :math:`D` við plan sem sker
:math:`x`-ásinn í :math:`x` og er hornrétt á :math:`x`-ás. Ef fallið
:math:`A(x)` er heildanlegt yfir bilið :math:`[a, b]` þá er rúmmál
:math:`D` jafnt og

.. math:: V=\int_a^b A(x)\,dx.

.. index::
    rúmmál; keilu

Rúmmál keilu
~~~~~~~~~~~~~~~~~~~

Látum :math:`F` vera takmarkaðan samanhangandi bút af plani og látum
:math:`T` vera punkt sem liggur ekki í planinu. Látum :math:`A` tákna
flatarmál :math:`F` og :math:`h` tákna fjarlægð topppunktsins frá
planinu sem grunnflöturinn liggur í. :hover:`Keila` með grunnflöt :math:`F` og
topppunkt :math:`T` er rúmskiki sem afmarkast af grunnfletinum :math:`F`
og öllum strikum sem liggja frá punktum á jaðri :math:`F` til :math:`T`.
Rúmmál keilunnar er

.. math::

   V=\frac{1}{3}hA=\frac{1}{3}(\text{hæð})(\text{flatarmál
   grunnflatar}).

Formúlan gildir óháð lögun grunnflatarins :math:`F`.

.. index::
    rúmmál; snúðs, snúið um x-ás

Rúmmál snúðs, snúið um :math:`x`-ás
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera samfellt fall á bili :math:`[a, b]`. Rúmskikinn sem
myndast þegar svæðinu sem afmarkast af :math:`x`-ás, grafinu
:math:`y=f(x)` og línunum :math:`x=a` og :math:`x=b` er snúið
:math:`360^\circ` um :math:`x`-ás hefur rúmmálið

.. math:: V=\pi\int_a^b f(x)^2\,dx.

Sjá  `3D volume by rotation of a function <https://www.geogebra.org/m/40798>`_
eftir `George Katehos <https://www.geogebra.org/material/show/id/40798>`_ (CC-BY-SA).

.. index::
    rúmmál; snúðs með gati

Rúmmál snúðs með gati
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` og :math:`g` vera tvö samfelld föll skilgreind á bilinu
:math:`[a, b]`. Gerum ráð fyrir að um öll :math:`x\in [a, b]` gildi að
:math:`0\leq f(x)\leq
g(x)`. Þegar svæðinu milli grafa :math:`f` og :math:`g` er snúið
:math:`360^\circ` um :math:`x`-ás fæst rúmskiki sem hefur rúmmálið

.. math:: V=\pi\int_a^b g(x)^2-f(x)^2\,dx.

.. index::
    rúmmál; snúðs, snúið um y-ás

Rúmmál snúðs, snúið um :math:`y`-ás
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera samfellt fall skilgreint á bili :math:`[a, b]`, með
:math:`0\leq a<b`. Gerum ráð fyrir að :math:`f(x)\geq 0` fyrir öll
:math:`x\in [a, b]`. Rúmmál rúmskikans sem fæst með að snúa svæðinu sem
afmarkast af :math:`x`-ás, grafinu :math:`y=f(x)` og línunum :math:`x=a`
og :math:`x=b` um :math:`360^\circ` um :math:`y`-ás er

.. math:: V=2\pi\int_a^b xf(x)\,dx.

.. index::
    fall; lengd grafs

Sjá `Solids and volumes of revolution (rotation about y_axis) <https://www.geogebra.org/b/75281#material/18475>`_
eftir `George Katehos <https://www.geogebra.org/b/75281#material/18475>`_ (CC-BY-SA).


Lengd grafs
~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera fall skilgreint á bili :math:`[a, b]` sem
hefur samfellda afleiðu.
Lengd grafsins :math:`y=f(x)` milli :math:`x=a` og :math:`x=b` er
skilgreind sem

.. math:: s=\int_a^b\sqrt{1+(f'(x))^2}\,dx.

.. index::
    flatarmál; yfirborðsflatarmál snúðs, snúið um x-ás

Flatarmál snúðflatar, snúið um :math:`x`-ás
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera samfellt fall skilgreint á bili :math:`[a, b]`.
Grafinu :math:`y=f(x)` er snúið :math:`360^\circ` um :math:`x`-ás og
myndast við það flötur. Flatarmál flatarins er gefið með formúlunni

.. math:: S=2\pi\int_a^b|f(x)|\sqrt{1+(f'(x))^2}\,dx.

.. index::
    flatarmál; yfirborðsflatarmál snúðs, snúið um y-ás

Flatarmál snúðflatar, snúið um :math:`y`-ás
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera samfellt fall skilgreint á bili :math:`[a, b]`.
Grafinu :math:`y=f(x)` er snúið :math:`360^\circ` um :math:`y`-ás og
myndast við það flötur. Flatarmál flatarins er gefið með formúlunni

.. math:: S=2\pi\int_a^b|x|\sqrt{1+(f'(x))^2}\,dx.

.. index::
    massi

Massi
-----

.. index::
    massi; vírs
    massi; massafrymi

Massi vírs
~~~~~~~~~~~~~~~~~

Vír liggur eftir ferli :math:`y=f(x)` þar sem :math:`a\leq x\leq b`.
Efnisþéttleiki (eðlisþyngdin) í punkti :math:`(x, f(x))` er gefinn sem
:math:`\delta(x)`. *Massafrymi* vírsins (massi örbúts af lengd
:math:`ds`) er

.. math::

   dm 
   = \delta(x)\, ds 
   =\delta(x)\sqrt{1+(f'(x))^2}\, dx,

og massi alls vírsins er

.. math:: m=\int_a^b \delta(x)\,ds=\int_a^b \delta(x)\sqrt{1+(f'(x))^2}\, dx.

.. index::
    massi; plötu

.. _massi-plotu:

Massi plötu
~~~~~~~~~~~~~~~~~~

Plata afmarkast af :math:`x`-ás, grafinu :math:`y=f(x)` og línunum
:math:`x=a` og :math:`x=b`. Á línu sem er hornrétt á :math:`x`-ás og
sker :math:`x`-ásinn í :math:`x` er efnisþéttleikinn fastur og gefinn
með :math:`\delta(x)`.

Flatarmál örsneiðar milli lína hornréttra á :math:`x`-ás sem skera ásinn
í :math:`x` og :math:`x+dx` er :math:`dA=f(x)\,dx`.

Massafrymi fyrir plötuna (massi örsneiðarinnar) er

.. math:: dm =\delta(x)dA = \delta(x) f(x)\,dx,

og massi allrar plötunnar er

.. math:: m=\int_a^b \delta(x)f(x)\,dx.

.. index::
    massi; rúmskika

Massi rúmskika
~~~~~~~~~~~~~~~~~~~~~

Rúmskiki :math:`D` liggur á milli plananna :math:`x=a` og :math:`x=b`.
Táknum með :math:`A(x)` flatarmál þversniðs :math:`D` við plan sem sker
:math:`x`-ásinn í :math:`x` og er hornrétt á :math:`x`-ás. Gerum ráð
fyrir að efnisþéttleikinn sé fastur á hverju þversniði, og að á
þversniði :math:`D` við plan sem sker :math:`x`-ásinn í :math:`x` og er
hornrétt á :math:`x`-ás sé efnisþéttleikinn gefinn með
:math:`\delta(x)`.

Rúmmálsfrymi (rúmmál örsneiðar úr :math:`D` sem liggur á milli tveggja
plana sem eru hornrétt á :math:`x`-ásinn og skera :math:`x`-ásinn í
:math:`x` og :math:`x+dx`) er :math:`dV=A(x)\, dx`.

Massafrymi (massi örsneiðarinnar) er

.. math:: dm=\delta(x)\, dV = \delta(x) A(x)\, dx,

og massi rúmskikans :math:`D` er þá

.. math:: m=\int_a^b \delta(x)A(x)\, dx.

.. index::
    massi; massamiðja
    massi; vægi

Massamiðja
----------

Skilgreining: Massamiðja punktmassa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Punktmassar :math:`m_1, m_2, \ldots, m_n` eru staðsettir í punktunum
:math:`x_1,
x_2, \ldots, x_n` á :math:`x`-ásnum.

:hover:`Vægi` kerfisins um punktinn :math:`x=0` er skilgreint sem

.. math:: M_{x=0}=\sum_{i=1}^n x_im_i,

og :hover:`massamiðja,þyngdarmiðja` kerfisins er

.. math:: \overline{x}=\frac{M_{x=0}}{m} = \frac{\sum_{i=1}^n x_im_i}{\sum_{i=1}^n m_i}.

Skilgreining: Massamiðja
~~~~~~~~~~~~~~~~~~~~~~~~

Ef massi er dreifður samkvæmt þéttleika falli :math:`\delta(x)` um bil
:math:`[a, b]` á :math:`x`-ásnum þá er massi og vægi um punktinn
:math:`x=0` gefið með formúlunum

.. math::

   m=\int_a^b \delta(x)\,dx 
   \qquad\text{ og }\qquad 
   M_{x=0}= \int_a^b x\delta(x)\,dx.

Massamiðjan er gefin með formúlunni

.. math::

   \overline{x}=\frac{M_{x=0}}{m}   =
   \frac{\int_a^b x\delta(x)\,dx}{\int_a^b \delta(x)\,dx}.

   
.. index::
    massi; massamiðja plötu
   
Skilgreining: Massamiðja plötu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skoðum plötu af sömu gerð og í :ref:`7.2.2 <massi-plotu>`.

Vægi plötunnar um :math:`y`- og :math:`x`-ása eru gefin með formúlunum

.. math::

   M_{x=0}=\int_a^b x\delta(x)f(x)\,dx 
   \qquad\text{og}\qquad
   M_{y=0}=\frac{1}{2}\int_a^b \delta(x)f(x)^2\,dx,

og hnit massamiðju plötunnar, :math:`(\overline{x}, \overline{y})`, eru
gefin með jöfnunum

.. math::

   \overline{x}=\frac{M_{x=0}}{m}=
   \frac{\int_a^b x\delta(x)f(x)\,dx}{\int_a^b \delta(x)f(x)\,dx}

og

.. math::

   \overline{y}=\frac{M_{y=0}}{m}=
   \frac{\frac{1}{2}\int_a^b \delta(x)f(x)^2\,dx}{\int_a^b
   \delta(x)f(x)\,dx}.

.. index::
    setning Pappusar
   
Setning Pappusar, I
~~~~~~~~~~~~~~~~~~~

Látum :math:`R` vera svæði sem liggur í plani öðrum megin við línu
:math:`L`. Látum :math:`A` tákna flatarmál :math:`R` og
:math:`\overline{r}` tákna fjarlægð massamiðju :math:`R` frá :math:`L`.

Þegar svæðinu :math:`R` er snúið :math:`360^\circ` um :math:`L` myndast
snúðskiki með rúmmál

.. math:: V=2\pi\overline{r}A.

Setning Pappusar, II
~~~~~~~~~~~~~~~~~~~~

Látum :math:`C` vera feril sem liggur í plani og er allur öðrum
megin við línu :math:`L`. Látum :math:`s` tákna lengd :math:`C` og
:math:`\overline{r}` tákna fjarlægð massamiðju :math:`C` frá :math:`L`.
Þegar ferlinum :math:`C` er snúið :math:`360^\circ` um :math:`L` myndast
snúðflötur með flatarmál

.. math:: S=2\pi\overline{r}s.
