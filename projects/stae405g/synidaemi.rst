| Háskóli Íslands vor 2014
| Töluleg greining STÆ405G kafli 3.1

--------------

Sýnidæmi

*Þetta er dæmi um jöfnuhneppi þar sem nauðsynlegt er að nota vendingu
til þess að fá nothæfa lausn. Við sjáum að það skiptir því miklu máli
hvernig við útfærum Gauss-eyðinguna. Jöfnuhneppið sem við ætlum að skoða
er*

.. math::

   \left[
   \begin{array}{ll}
   {\varepsilon}& 1 \\
   1 & 1 
   \end{array}\right]
   \left[
   \begin{array}{l}
   x_1\\
   x_2
   \end{array}\right]
   = \left[\begin{array}{l}
   1\\
   2
   \end{array}\right]

Nákvæm lausn
------------

Byrjum á því að finna nákvæma lausn með Gauss-eyðingu. Margföldum fyrstu
línuna með :math:`\frac 1{\varepsilon}` og drögum frá annarri línunni.

.. math::

   \left[
   \begin{array}{ll|l}
   {\varepsilon}& 1 & 1\\
   1 & 1 & 2
   \end{array}\right]
   \sim
   \left[
   \begin{array}{ll|l}
   {\varepsilon}& 1 & 1\\
   0 & 1-\frac 1{\varepsilon}& 2 -\frac 1{\varepsilon}\end{array}\right]

Af þessu sjáum við að
:math:`x_2 = \frac{2-\frac 1{\varepsilon}}{1-\frac 1{\varepsilon}} = 1 - \frac{{\varepsilon}}{1-{\varepsilon}}`,
og þá er
:math:`x_1 = \frac{1-1 x_2}{{\varepsilon}} = 1+ \frac{{\varepsilon}}{1-{\varepsilon}}`.

Lausn í tölvu, án vendingar
---------------------------

Athugum hvernig sömu reikningar eru framkvæmdir í tölvu, og gerum ráð
fyrir að :math:`{\varepsilon}` sé minna heldur en nákvæmnin í tölvunni.
Það þýðir að tölvan getur ekki gert greinarmun á tölunum
:math:`1-\frac 1{\varepsilon}` og :math:`-\frac 1{\varepsilon}`, og eins
á tölunum :math:`2-\frac 1{\varepsilon}` og
:math:`-\frac 1{\varepsilon}`, því :math:`\frac 1{\varepsilon}` er svo
miklu stærra en :math:`1` og :math:`2`. Gauss-eyðing út frá fyrstu línu
skilar eins og áður

.. math::

   \left[
   \begin{array}{ll|l}
   {\varepsilon}& 1 & 1\\
   1 & 1 & 2
   \end{array}\right]
   \sim
   \left[
   \begin{array}{ll|l}
   {\varepsilon}& 1 & 1\\
   0 & 1-\frac 1{\varepsilon}& 2 -\frac 1{\varepsilon}\end{array}\right]

En af ofangreindum ástæðum þá lítur tölvan á seinna hneppið sem

.. math::

   \left[
   \begin{array}{ll|l}
   {\varepsilon}& 1 & 1\\
   0 & -\frac 1{\varepsilon}& -\frac 1{\varepsilon}\end{array}\right]

 Þannig að
:math:`x_2 = \frac{-\frac 1{\varepsilon}}{-\frac 1{\varepsilon}} = 1`.
Þá er
:math:`x_1 = \frac{1-1x_2}{{\varepsilon}} = \frac{1-1}{{\varepsilon}} = 0`.
Sem er langt frá réttu lausninni.

Lausn í tölvu, með vendingu
---------------------------

Prófum að gera það sama, nema nú skulum við eyða út frá annarri línu.
Margföldum línu 2 með :math:`{\varepsilon}` og drögum frá fyrstu
línunni.

.. math::

   \left[
   \begin{array}{ll|l}
   {\varepsilon}& 1 & 1\\
   1 & 1 & 2
   \end{array}\right]
   \sim
   \left[
   \begin{array}{ll|l}
   0 & 1-{\varepsilon}& 1-2{\varepsilon}\\
   1 & 1 & 2
   \end{array}\right]

Tölvan sér ekki mun á :math:`1-{\varepsilon}` og 1, og eins á
:math:`1-2{\varepsilon}` og 1 þannig að í hennar augum verður þetta að

.. math::

   \left[
   \begin{array}{ll|l}
   0 & 1 & 1\\
   1 & 1 & 2
   \end{array}\right]

 Þannig að :math:`x_2 = 1`, og þá fæst
:math:`x_1 = \frac{2-1x_2}{1} = 1`. Þetta er ekki hárrétt lausn, en mun
betri en sú sem við fengum áður.

Matlab
------

Þið getið prófað að framkvæma þessa reikninga í Matlab. Það má gera með
eftirfarandi skipunum.

::

    >>[ 1/5 1 ; 1 1 ]\[1 ; 2]
    >>[ 1e-20 1 ; 1 1 ]\[ 1 ; 2]

Í fyrri skipuninni þá er :math:`{\varepsilon}= \frac 15`, þá sést
greinilega nákvæma lausnin að ofan. En í seinni skipuninni þá er
:math:`{\varepsilon}= 10^{-20}` og þá lendum við í því að lausnin okkar
er ekki alveg rétt. Matlab er hins vegar það skynsamt að það beita
skalaðri hlutvendingu þannig að lausnin okkar verður ekki alveg út úr
kú.

| Benedikt Magnússon
