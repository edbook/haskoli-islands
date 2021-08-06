Inngangur að línulegri algebru
==============================

.. admonition:: Nauðsynleg undirstaða
	:class: athugasemd

	- `Vigrar <https://edbook.hi.is/undirbuningur_stae/kafli08.html>`_

------

.. epigraph::

  **Pippin:** *I didn't think it would end this way.*

  **Gandalf:** *End? No, the journey doesn't end here. Death is just another path, one that we all must take. The grey rain-curtain of this world rolls back, and all turns to silver glass, and then you see it.*

  **Pippin:** *What? Gandalf? See what?*

  **Gandalf:** *White shores, and beyond, a far green country under a swift sunrise.*

  **Pippin:** *Well, that isn't so bad.*

  **Gandalf:** *No. No, it isn't.*

  \– Gandalf and Pippin, Return of the King (movie)

-------

Fylki
------

Fylki (e. *matrix*) er tafla af tölum. Tölurnar nefnast stök (e. *elements*) fylkisins.
Dæmi um fylki er :math:`2 \times 2` fylkið með 2 dálkum og 2 röðum:

.. math::
  \begin{bmatrix}
    a & b\\
    c & d\\
  \end{bmatrix}

Við notum oft vísinn (e. *index*) :math:`i` til að tákna röð fylkisins og :math:`j`
til að tákna dálk fylkisins. Við vísum fyrst í röð fylkis og svo dálk.

Fylki má almennt rita sem:

.. math::
  \mathbf{A}=\begin{bmatrix}
    a_{11} & a_{12} & \dots & a_{1n}\\
    a_{11} & a_{12} & \dots & a_{1n}\\
    \vdots & \vdots & \ddots & \vdots \\
    a_{m1} & a_{m2} & \dots & a_{mn}\\
  \end{bmatrix}

Þetta fylki hefur :math:`m` raðir og :math:`n` dálka og er kallað :math:`m \times n`
fylki. Til að vísa í stakið í röð :math:`i` og dálki :math:`j` fylkisins :math:`\mathbf{A}`
skrifum við :math:`(\mathbf{A})_{ij}=a_{ij}`.

Algengur flokkur fylkja er fylki með jafnmarga dálka og raðir, þ.e. :math:`m=n`.
Slík fylki kallast *ferningsfylki* (e. square matrix).

.. math::
  \mathbf{A}=\begin{bmatrix}
    a_{11} & a_{12} & \dots & a_{1n}\\
    a_{11} & a_{12} & \dots & a_{1n}\\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & a_{n2} & \dots & a_{nn}\\
  \end{bmatrix}

*Hornalína* fylkisins :math:`a_{11}, \dots ,a_{nn}` kallast *hornalínustök*.

Dæmi: Nokkur dæmi um fylki
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  (i) :math:`\begin{bmatrix} 1 & 2\\ 0 & 5 \end{bmatrix}`

  (ii) :math:`\begin{bmatrix} 1\\ 3\\ \end{bmatrix}`

  (iii) :math:`[1,2,3,4]`

  (iv) :math:`[2]`

Hornalínufylki (e. *diagonal matrix*) eru ferningsfylki þar sem stökin fyrir utan
hornalínuna (e. *diagonal*) eru núll. Hornalínustökin geta verið núll.

*Þríhyrningsfylki* (e. *triangular matrix*) er tegund af ferningsfylki þar sem
stökin fyrir ofan eða neðan hornalínuna hafa gildið núll.

Dæmi: Hornalínufylki
~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Eftirfarandi fylki eru dæmi um hornalínufylki.

  (i) :math:`\begin{bmatrix} 1 & 0 & 0\\ 0 & 5 & 0\\ 0 & 0 & 3 \end{bmatrix}`

  (ii) :math:`\begin{bmatrix} 5 & 0 & 0\\ 0 & 0 & 0\\ 0 & 0 & 7 \end{bmatrix}`

Dæmi: Þríhyrningsfylki
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Eftirfarandi fylki eru dæmi um þríhyrningsfylki.

  (i) :math:`\begin{bmatrix} 1 & 2 & 3\\ 0 & 5 & 7\\ 0 & 0 & 7 \end{bmatrix}`

  (ii) :math:`\begin{bmatrix} 5 & 0 & 0\\ 3 & 1 & 0\\ 1 & 2 & 7 \end{bmatrix}`

Samlagning og margföldun við fasta
-----------------------------------

Setning: Samlagning og margföldun við fasta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Tvö fylki :math:`\mathbf{A}` og :math:`\mathbf{B}` eru eins, þ.e. :math:`\mathbf{A}=\mathbf{B}` þá og því aðeins að
	þau séu af sömu stærð og innihaldi sömu stök.

	Ef :math:`\mathbf{A}` og :math:`\mathbf{B}` eru af sömu stærð má leggja þau saman: :math:`\mathbf{A}+\mathbf{B}=C`
	þar sem stak :math:`(i,j)` í :math:`C` er :math:`c_{ij} = a_{ij}+b_{ij}`.

	Ef :math:`k` er tala setjum við :math:`k\mathbf{A}=D` þar sem :math:`d_{ij}=ka_{ij}`.

Dæmi: Samlagning og margföldun við fasta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: Dæmi

  Lítum á fylkin :math:`\mathbf{A}=\begin{bmatrix} 1 & 3\\ 2 & 4\\\end{bmatrix}`,
  :math:`\mathbf{B}=\begin{bmatrix} 5 & 7\\ 6 & 8\\\end{bmatrix}` og
  :math:`\mathbf{C}=[1,2]`.

  Reiknum

    (i) :math:`\mathbf{A}+\mathbf{B}`

    (ii) :math:`\mathbf{A}+\mathbf{C}`

    (iii) :math:`2\mathbf{A}`

  eða tiltökum hví það er ekki hægt.

.. admonition:: Lausn
  :class: daemi, dropdown

    (i) .. math:: \mathbf{A}+\mathbf{B} =\begin{bmatrix} 1 + 5 & 3 + 7\\ 2 + 6 & 4 + 8\\ \end{bmatrix} = \begin{bmatrix} 6 & 10\\ 8 & 12\\ \end{bmatrix}

    (ii) :math:`\mathbf{A}+\mathbf{C}` er ekki hægt því fylkin eru ekki af sömu stærð.

    (iii) .. math:: 2\mathbf{A} = \begin{bmatrix} 2\cdot 1 & 2 \cdot 3\\ 2 \cdot 2 & 2 \cdot 4\\ \end{bmatrix} = \begin{bmatrix} 2 & 6\\ 4 & 8\\ \end{bmatrix}

Bylt fylki
-----------

Ef :math:`\mathbf{A}=(a_{ij})` er fylki skilgreinum við *bylta* fylkið (e. *matrix transpose*) :math:`\mathbf{A}'` (stundum :math:`\mathbf{A}^T`)
sem það fylki sem inniheldur stökin :math:`a_{ji}`, þ.e.a.s. stak í línu :math:`j`
og dálki :math:`i` er tekið úr línu :math:`i` og dálki :math:`j` í upphaflega
fylkinu.

Dæmi: Bylt fylki
~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Látum

  .. math::
    \mathbf{A}=\begin{bmatrix}
      1 & 2\\
      3 & 4\\
    \end{bmatrix}

  og

  .. math::
    \mathbf{B}=\begin{bmatrix}
      1 & 2 & 7\\
      3 & 4 & 8\\
    \end{bmatrix}.

  Finnum :math:`\mathbf{A}'` og :math:`\mathbf{B}'`.

.. admonition:: Lausn
  :class: daemi, dropdown

  Við víxlum öllum línum þannig þær verða dálkar og öllum dálkum þannig
  þeir verða raðir. Þá fæst

  .. math::
    \mathbf{A}'=\begin{bmatrix}
      1 & 3\\
      2 & 4\\
    \end{bmatrix}

  og

  .. math::
    \mathbf{B}'=\begin{bmatrix}
      1 & 3\\
      2 & 4\\
      7 & 8\\
    \end{bmatrix}.

Margföldun fylkja
------------------

Ef :math:`\mathbf{A}` er :math:`m \times r` fylki og :math:`\mathbf{B}` er :math:`r \times n` fylki
þá er :math:`\mathbf{A}\mathbf{B}` fylki þar sem stak í röð :math:`i` og dálki :math:`j` er reiknað
með því að para saman stökin í röð :math:`i` í :math:`\mathbf{A}` og dálki :math:`j` í
:math:`\mathbf{B}`.

Einfaldast  er að hugsa margfeldi fylkja þannig að byrjað er á að taka fyrsta dálk í
:math:`\mathbf{B}` og leggja hann yfir fyrstu línuna í :math:`\mathbf{A}` til að margfalda saman öll
stökin og finna summu þeirra margfelda.  Því næst er þessi dálkur færður niður,
línu fyrir línu, til að mynda allan fyrsta dálkinn í útkomunni.
Til að mynda næsta dálk er tekinn næsti dálkur úr :math:`\mathbf{B}` og aðgerðirnar endurteknar.


.. figure:: ./myndir/kafli_lalgebra/PMA_fylkja_margfoldun.png
  :width: 100%
  :align: center

Takið svo eftir að til að :math:`\mathbf{A}\mathbf{B}` sé skilgreint þarf fjöldi dálka í :math:`\mathbf{A}`
að vera jafn fjölda raða í :math:`\mathbf{B}`

Eiginleikar fylkja
-------------------

Hér munum við skoða ýmsa stærðfræðilega eiginleika fylka.

Setning: Reiknireglur fyrir fylki
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Reiknireglur fyrir fylki
  :class: setning

  Látum :math:`\mathbf{A}`, :math:`\mathbf{B}` og :math:`\mathbf{C}` vera fylki þannig að unnt sé að framkvæma
  aðgerðirnar í hverju tilviki og :math:`a,b,c` vera tölur:

    #. :math:`\mathbf{A} + \mathbf{B} = \mathbf{B} + \mathbf{A}`

    #. :math:`\mathbf{A} + (\mathbf{B} + \mathbf{C}) = (\mathbf{A} + \mathbf{B}) + \mathbf{C}`

    #. :math:`\mathbf{A}(\mathbf{B}\mathbf{C})=(\mathbf{A}\mathbf{B})\mathbf{C}`

    #. :math:`\mathbf{A}(\mathbf{B} + \mathbf{C}) = \mathbf{A}\mathbf{B} + \mathbf{A}\mathbf{C}`

    #. :math:`c(\mathbf{A}+\mathbf{B})=c\mathbf{A} + c\mathbf{B}`

    #. :math:`c(\mathbf{A}\mathbf{B}) = (c\mathbf{A})\mathbf{B} = \mathbf{A}(c\mathbf{B})`

    #. :math:`a(b\mathbf{C}) = (ab)\mathbf{C}`

Það gilda því margar helstu reikniaðgerðir fyrir fylki, miðað við þá skilgreiningu á
fylkjaaðgerðum sem hefur verið sett fram.

Víxregla gildir ekki almennt fyrir fylki, þ.e. :math:`\mathbf{A}\mathbf{B}` er yfirleitt ekki það
sama og :math:`\mathbf{B}\mathbf{A}`! Raunar er algengt að einungis annað margfeldið sé skilgreint.


Einingafylki
-------------

Einingafylki (e. *identity matrix*) eru sérlega áhugaverð fylki. Þau hafa jafnmarga línur
og dálka, hafa einn á hornalínunni en núll utan hennar:

.. math:: \begin{bmatrix} 1 & 0\\ 0 & 1\\ \end{bmatrix}, \begin{bmatrix} 1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1\\ \end{bmatrix}, \dots

Þessi fylki eru þannig að ef :math:`\mathbf{I}_n` er :math:`n \times n` einingafylki og
:math:`\mathbf{A}` er :math:`m \times n` fylki þá gildir að :math:`\mathbf{A}\mathbf{I}_n = \mathbf{A}`. Einnig gildir
að :math:`\mathbf{I}_m \mathbf{A} = \mathbf{A}`.

Andhverfa fylkis
-----------------

Þegar :math:`x \neq 0` er tala vitum við að unnt er að finna :math:`y` þannig að
:math:`xy=1`. Þetta er gert með því að setja :math:`x=1/x=x^{-1}`. Slíkt :math:`y`
er stundum nefnt margföldunarandhverfa :math:`x`.

Fyrir fylki höfum við skilgreint samlagningu og margföldun, en ekkert deilingarhugtak
er komið. Deiling á ekki að vera neitt annað en margföldun með margföldunarandhverfu.

Til að setja fram slíkt hugtak byrjum við á almennri skilgreiningu.

Skilgreining: Fylkjaandhverfa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
  :class: skilgreining

  Ef :math:`\mathbf{A}` er :math:`n \times n` fylki og :math:`\mathbf{B}` er jafnstórt fylki sem er þannig að
  :math:`\mathbf{A}\mathbf{B}=\mathbf{B}\mathbf{A}=\mathbf{I}`, þá er :math:`\mathbf{B}` nefnt *andhverfa* (e. *inverse*) :math:`\mathbf{A}` og
  er táknað :math:`\mathbf{A}^{-1}`.


Dæmi: Fylkjaandhverfa
~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi

  Ef :math:`\mathbf{H}` er fylkið

  .. math::
    \mathbf{H}=\begin{bmatrix}
      4 & 0 & 0\\
      0 & 3 & 0\\
      0 & 0 & 1\\
    \end{bmatrix}

  og :math:`\mathbf{J}` er fylkið

  .. math::
    \mathbf{H}=\begin{bmatrix}
      \tfrac{1}{4} & 0 & 0\\
      0 & \tfrac{1}{3} & 0\\
      0 & 0 & 1\\
    \end{bmatrix}

  þá er einfalt að sýna fram á að :math:`\mathbf{H}\mathbf{J} = \mathbf{J}\mathbf{H} = \mathbf{I}` svo :math:`\mathbf{J}` er andhverfa
  :math:`\mathbf{H}`, þ.e. :math:`\mathbf{J}=\mathbf{H}^{-1}`.

Andhverfur fylkja eru almennt ekki reiknaðar í höndunum, en þó má reikna andhverfu
:math:`2 \times 2` fylkja á einfaldan hátt í höndunum.

Setning: Andhverfa :math:`2 \times 2` fylkis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Höfum almennt :math:`2 \times 2` fylki

  .. math:: \mathbf{A}=\begin{bmatrix} a & b\\ c & d\\ \end{bmatrix}.

  Andhverfa fylkisins er

  .. math:: \mathbf{A}^{-1} = \frac{1}{ad-bc} \begin{bmatrix} d & -b\\ -c & a\\ \end{bmatrix}.

Línuleg jöfnuhneppi
-------------------

Jafna af taginu

.. math:: a_1 x_1 + a_2 x_2 + \dots a_n x_n = b

kallast *línuleg jafna* (e. *linear equation*). Það sem auðkennir línulegar
jöfnur er að breyturnar koma bara fyrir í 1. veldi og engin margfeldi tveggja eða
fleiri breyta koma fyrir í jöfnunni.

Línulega jöfnu eins og hér að ofan má líka rita sem :math:`\mathbf{a}\cdot \mathbf{x} = b`
þar sem :math:`\mathbf{a} = (a_1, a_2, \dots, a_n)` og :math:`\mathbf{x} = (x_1, x_2, \dots, x_n)`.

*Línulegt jöfnuhneppi* (e. *system of linear equations*) samanstendur af einni eða
fleiri línulegum jöfnum og er oft sett upp á forminu

.. math::
  \begin{aligned}
    a_{11} x_1 + a_{12} x_2 + \dots a_{1n} x_n &= b_1\\
    a_{21} x_1 + a_{22} x_2 + \dots a_{2n} x_n &= b_2\\
    \vdots &= \vdots \\
    a_{b1} x_1 + a_{b2} x_2 + \dots a_{mn} x_n &= b_m\\
  \end{aligned}

Lausn jöfnuhneppisins er vigur :math:`(x_1, x_2, \dots, x_n)` þannig að
allar jöfnurnar í jöfnuhneppinu eru uppfylltar. Það að leysa línulegt jöfnuhneppi
felst í því að finna öll möguleg gildi á vigrinum :math:`(x_1, x_2, \dots, x_n)`.

*Stuðlafylki* jöfnuhneppisins er fylkið

.. math::
  \mathbf{A}=\begin{bmatrix}
    a_{11} & a_{12} & \dots & a_{1n}\\
    a_{21} & a_{22} & \dots & a_{2n}\\
    \vdots & \vdots & \ddots & \vdots \\
    a_{m1} & a_{m2} & \dots & a_{mn}\\
  \end{bmatrix}

*Breytuvigur* jöfnuhneppisins er *dálkvigurinn* (e. *column vector*)

.. math:: \mathbf{x} = \begin{bmatrix} x_1 & x_2 & \dots & x_m \end{bmatrix}.

*Hægri hlið* jöfnuhneppisins er dálkvigurinn

.. math:: \mathbf{b} = \begin{bmatrix} b_1 & b_2 & \dots & b_m \end{bmatrix}.

Ef :math:`\mathbf{A}` er stuðlafylki jöfnuhneppis, :math:`\mathbf{x}` er breytuvigurinn og
:math:`\mathbf{b}` er hægri hliðin, þá samsvarar upphaflega jöfnuhneppið fylkjajöfnunni
:math:`\mathbf{A}\mathbf{x} = \mathbf{b}` eða

.. math::
  \mathbf{A}=\begin{bmatrix}
    a_{11} & a_{12} & \dots & a_{1n}\\
    a_{21} & a_{22} & \dots & a_{2n}\\
    \vdots & \vdots & \ddots & \vdots \\
    a_{m1} & a_{m2} & \dots & a_{mn}\\
  \end{bmatrix} \cdot \begin{bmatrix} x_1\\ x_2\\ \vdots\\ x_n \end{bmatrix} = \begin{bmatrix} b_1\\ b_2\\ \vdots\\ b_n \end{bmatrix}.

Upphaflega jöfnuhneppið og jafnan :math:`\mathbf{A}\mathbf{x} = \mathbf{b}` hafa
sömu lausnir.

Við lítum svo á að línulegt jöfnuhneppi og fylkjajafnan :math:`\mathbf{A}\mathbf{x} = \mathbf{b}` séu
jafngildar framsetningar á sama hlutnum.

Við kunnum að leysa jöfnuhneppi með því að leysa út eina breytu í einu. Gerum ráð fyrir
að fylkið :math:`\mathbf{A}` hafi andhverfu. Þá er hægt að leysa jöfnuhneppið
:math:`\mathbf{A}\mathbf{x} = \mathbf{b}` af því að

.. math::
  \begin{aligned}
     && \mathbf{A}\mathbf{x} &= \mathbf{b}\\
    \iff && \mathbf{A}^{-1}(\mathbf{A}\mathbf{x}) &= \mathbf{A}^{-1}\mathbf{b}\\
    \iff && (\mathbf{A}^{-1}\mathbf{A})\mathbf{x} &= \mathbf{A}^{-1}\mathbf{b}\\
    \iff && \mathbf{x} &= \mathbf{A}^{-1}\mathbf{b}\\
  \end{aligned}

Ákveða fylkis
--------------

*Ákveða* (e. *determinant*) fylkis er vörpun sem varpar :math:`n \times n` fylki
yfir í rauntölu. Ákveða fylkis :math:`\mathbf{A}` er táknuð með :math:`det(\mathbf{A})`.

Höfum almennt :math:`2 \times 2` fylki,

.. math::  \mathbf{A} =  \begin{bmatrix} a & b \\ c & d\\ \end{bmatrix}.

Ákveða fylkisins er

.. math:: det(\mathbf{A}) = ad - bc.

Ekki er hlaupið að því að reikna ákveður fylkja þar sem :math:`n>2` og gerum við það ekki í
höndunum. Þó er auðvelt að finna ákveður þríhyrningsfylkja.

Setning: Ákveða þríhyrningsfylkis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning

  Ef :math:`\mathbf{A}` er :math:`n \times n` þríhyrningsfylki fæst ákveða fylkisins með því að
  margfalda hornalínustök fylkisins, þ.e.

  .. math:: det(\mathbf{A}) = a_{11}\cdot a_{22} \cdot \dots \cdot a_{nn}.

Eiginleikar ákveðu
-------------------

Eftirfarandi jafngildi getur komið að góðum notum í útreikningum með fylkjum.

.. admonition:: Eiginleikar ákveðu
  :class: setning

  Ef :math:`\mathbf{A}` er :math:`n \times n` fylki er eftirfarandi jafngilt:

    #. :math:`det(\mathbf{A}) \neq 0`

    #. :math:`\mathbf{A}` hefur andhverfu

    #. :math:`\mathbf{Ax}=\mathbf{b}` hefur nákvæmlega eina lausn

Þetta segir okkur að :math:`det(\mathbf{A}) \neq 0` gildir þá og því aðeins að
:math:`\mathbf{A}` hafi andhverfu sem aftur gildir þá og því að eins að :math:`\mathbf{Ax}= \mathbf{b}`.
