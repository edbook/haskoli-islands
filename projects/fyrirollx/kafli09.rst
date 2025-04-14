Yfirlit
=======

.. _app.CharacteristicTTs:

Skilgreiningarsanntöflur
------------------------

================ =====================
:math:`\meta{A}` :math:`\enot\meta{A}`
================ =====================
T                F
F                T
\                
\                
================ =====================

+----------+----------+----------+----------+----------+----------+
| :math:`\ | :math:`\ | :math    | :mat     | :mat     | :math    |
| meta{A}` | meta{B}` | :`\meta{ | h:`\meta | h:`\meta | :`\meta{ |
|          |          | A}\eand\ | {A}\eor\ | {A}\eif\ | A}\eiff\ |
|          |          | meta{B}` | meta{B}` | meta{B}` | meta{B}` |
+==========+==========+==========+==========+==========+==========+
| T        | T        | T        | T        | T        | T        |
+----------+----------+----------+----------+----------+----------+
| T        | F        | F        | T        | F        | F        |
+----------+----------+----------+----------+----------+----------+
| F        | T        | F        | T        | T        | F        |
+----------+----------+----------+----------+----------+----------+
| F        | F        | F        | F        | T        | T        |
+----------+----------+----------+----------+----------+----------+

Þýðingar yfir á táknmál umsagnarökfræði
---------------------------------------

.. container:: center

   +-------------------------------+-------------------------------------+
   | Setningatengi                 |                                     |
   +-------------------------------+-------------------------------------+
   |                               |                                     |
   +-------------------------------+-------------------------------------+
   | Það er ekki satt að P         | :math:`\enot P`                     |
   +-------------------------------+-------------------------------------+
   | Annað hvort P eða Q           | :math:`(P \eor Q)`                  |
   +-------------------------------+-------------------------------------+
   | Hvorki P né Q                 | :math:`\enot(P \eor Q)` eða         |
   |                               |  :math:`(\enot P \eand \enot Q)`    |
   +-------------------------------+-------------------------------------+
   | Bæði P og Q                   | :math:`(P \eand Q)`                 |
   +-------------------------------+-------------------------------------+
   | Ef P, þá Q                    | :math:`(P \eif Q)`                  |
   +-------------------------------+-------------------------------------+
   | P bara ef Q                   | :math:`(P \eif Q)`                  |
   +-------------------------------+-------------------------------------+
   | P ef og aðeins ef Q           | :math:`(P \eiff Q)`                 |
   +-------------------------------+-------------------------------------+
   | P nema Q                      | :math:`(P \eor Q)`                  |
   +-------------------------------+-------------------------------------+
   |                               |                                     |
   +-------------------------------+-------------------------------------+
   | Umsagnir                      |                                     |
   +-------------------------------+-------------------------------------+
   |                               |                                     |
   +-------------------------------+-------------------------------------+
   | Öll Fs eru G                  | :math:`\forall x(Fx \eif Gx)`       |
   +-------------------------------+-------------------------------------+
   | Sum F eru G                   | :math:`\exists x(Fx \eand Gx)`      |
   +-------------------------------+-------------------------------------+
   | Ekki öll F eru G              | :mat                                |
   |                               | h:`\enot\forall x(Fx \eif Gx)` or : |
   |                               | math:`\exists x(Fx \eand \enot Gx)` |
   +-------------------------------+-------------------------------------+
   | Engin F eru G                 | :ma                                 |
   |                               | th:`\forall x(Fx \eif\enot Gx)` or  |
   |                               | :math:`\enot\exists x(Fx \eand Gx)` |
   +-------------------------------+-------------------------------------+
   |                               |                                     |
   +-------------------------------+-------------------------------------+
   | Samsemd                       |                                     |
   +-------------------------------+-------------------------------------+
   |                               |                                     |
   +-------------------------------+-------------------------------------+
   | Bara c er G                   | :math:`\forall x(Gx \eiff x=c)`     |
   +-------------------------------+-------------------------------------+
   | Allt nema c er G              | :ma                                 |
   |                               | th:`\forall x(\enot x = c \eif Gx)` |
   +-------------------------------+-------------------------------------+
   | F-ið er G                     | :math:`\exists x(Fx \ean            |
   |                               | d \forall y(Fy \eif x=y) \eand Gx)` |
   +-------------------------------+-------------------------------------+
   | Það er ekki satt að F-ið sé G | :math:`\enot\exists x(Fx \ean       |
   |                               | d \forall y(Fy \eif x=y) \eand Gx)` |
   +-------------------------------+-------------------------------------+
   | F-ið er ekki-G                | :math:`\exists x(Fx \eand \for      |
   |                               | all y(Fy \eif x=y) \eand \enot Gx)` |
   +-------------------------------+-------------------------------------+

Að nota samsemd til að tjá fjölda
---------------------------------

.. _summary.atleast:

Það eru að minnsta kosti  F.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: ekey

   :math:`\exists xFx`

   :math:`\exists x_1\exists x_2(Fx_1 \eand Fx_2 \eand \enot x_1  = x_2)`

   :math:`\exists x_1\exists x_2\exists x_3(Fx_1 \eand Fx_2 \eand Fx_3 \eand \enot x_1 = x_2 \eand\enot x_1 = x_3 \eand \enot x_2 = x_3)`

   | :math:`\exists x_1\exists x_2\exists x_3\exists x_4 (Fx_1 \eand Fx_2 \eand Fx_3 \eand Fx_4 \eand \phantom{x}`
   | :math:`\enot x_1 = x_2 \eand \enot x_1 = x_3 \eand \enot x_1 = x_4 \eand \enot x_2 = x_3 \eand \enot x_2 = x_4 \eand \enot x_3 = x_4)`

   :math:`\exists x_1\ldots\exists x_n(Fx_1 \eand\ldots\eand Fx_n \eand \enot x_1 = x_2 \eand\ldots\eand \enot x_{n-1} = x_n)`

.. _summary.atmost:

Það eru í mesta lagi  F.
~~~~~~~~~~~~~~~~~~~~~~~~

Ein leið til að tjá þá hugsun að „það séu í mesta lagi :math:`n` F“ er
að setja neitun fyrir framan samsvarandi setningu sem segir „Það eru að
minnsta kosti :math:`n+1`\ “. En við getum líka sagt:

.. container:: ekey

   :math:`\forall x_1\forall x_2\bigl[(Fx_1 \eand Fx_2) \eif x_1=x_2\bigr]`

   :math:`\forall x_1\forall x_2\forall x_3\bigl[(Fx_1 \eand Fx_2 \eand Fx_3) \eif (x_1=x_2 \eor x_1=x_3 \eor x_2=x_3)\bigr]`

   | :math:`\forall x_1\forall x_2\forall x_3\forall x_4\bigl[(Fx_1 \eand Fx_2 \eand Fx_3 \eand Fx_4) \eif \phantom{.}`
   | :math:`(x_1=x_2 \eor x_1=x_3 \eor x_1=x_4 \eor x_2=x_3 \eor x_2=x_4 \eor x_3=x_4)\bigr]`

   :math:`\forall x_1\ldots\forall x_{n+1}
   \bigl[(Fx_1\eand \ldots \eand Fx_{n+1}) \eif (x_1=x_2 \eor \ldots \eor x_n=x_{n+1})\bigr]`

.. _summary.exactly:

Það eru nákvæmlega  F.
~~~~~~~~~~~~~~~~~~~~~~

Til að segja að „það séu nákvæmlega :math:`n` F“ er einfaldlega hægt að
tengja saman tvær þýðingar sem segja að „það séu í mesta lagi :math:`n`
F“ og „það séu í mesta lagi :math:`n` F“ með samtengingu. En
eftirfarandi þýðingar eru styttri og að mörgu leyti fallegri:

.. container:: ekey

   :math:`\forall x\enot Fx`

   :math:`\exists x\bigl[Fx \eand \forall y(Fy \eif x= y)\bigr]`

   :math:`\exists x_1\exists x_2\bigl[Fx_1 \eand Fx_2 \eand \enot x_1 = x_2 \eand \forall y\bigl(Fy \eif (y= x_1 \eor y = x_2)\bigr) \bigr]`

   | :math:`\exists x_1\exists x_2\exists x_3\bigl[Fx_1 \eand Fx_2 \eand Fx_3 \eand \enot x_1 =  x_2 \eand \enot  x_1 = x_3 \eand \enot x_2 = x_3 \eand \phantom{.}`
   | :math:`\forall y\bigl(Fy \eif (y = x_1 \eor y = x_2 \eor y =  x_3)\bigr) \bigr]`

   | :math:`\exists x_1\ldots\exists x_n\bigl[Fx_1 \eand\ldots\eand Fx_n  \eand \enot x_1 = x_2 \eand\ldots\eand \enot x_{n-1}= x_n \eand \phantom{.}`
   | :math:`\forall y\bigl(Fy \eif (y= x_1 \eor \ldots \eor y= x_n)\bigr)\bigr]`

Grunnreglur fyrir setningarökfræði
----------------------------------

.. container:: multicols

   2

   .. rubric:: Samtenging
      :name: samtenging
      :class: unnumbered

   :math:`\begin{nd}
       \have[m]{a}{\meta{A}}
       \have[n]{b}{\meta{B}}
       \have[\ ]{c}{\meta{A}\eand\meta{B}} \ai{a, b}

       \have[m]{ab}{\meta{A}\eand\meta{B}}
   \\  \have[\ ]{a}{\meta{A}} \ae{ab}

       \have[m]{ab}{\meta{A}\eand\meta{B}}
   \\  \have[\ ]{b}{\meta{B}} \ae{ab}
   \end{nd}`

   .. rubric:: Mistenging
      :name: mistenging
      :class: unnumbered

   :math:`\begin{nd}
       \have[m]{a}{\meta{A}}
       \have[\ ]{ab}{\meta{A}\eor\meta{B}}\oi{a}

       \have[m]{a}{\meta{A}}
   \\  \have[\ ]{ba}{\meta{B}\eor\meta{A}}\oi{a}

       \have[m]{ab}{\meta{A}\eor\meta{B}}
   \\  \open
           \hypo[i]{a}{\meta{A}}
           \have[j]{c1}{\meta{C}}
       \close
       \open
           \hypo[k]{b}{\meta{B}}
           \have[l]{c2}{\meta{C}}
       \close
       \have[\ ]{c}{\meta{C}} \oe{ab,a-c1, b-c2}
   \end{nd}`

   .. rubric:: Skilyrðistengi
      :name: skilyrðistengi
      :class: unnumbered

   :math:`\begin{nd}
       \open
       \hypo[i]{a}{\meta{A}}
       \have[j]{b}{\meta{B}}
       \close
       \have[\ ]{ab}{\meta{A}\eif\meta{B}}\ci{a-b}
       
       \have[m]{ab}{\meta{A}\eif\meta{B}}
       \\  \have[n]{a}{\meta{A}}
       \have[\ ]{b}{\meta{B}} \ce{ab,a}
   \end{nd}`

   .. rubric:: Jafngildistengi
      :name: jafngildistengi
      :class: unnumbered

   :math:`\begin{nd}
       \open
           \hypo[i]{a1}{\meta{A}} 
           \have[j]{b1}{\meta{B}}
       \close
       \open
           \hypo[k]{b2}{\meta{B}}
           \have[l]{a2}{\meta{A}}
       \close
       \have[\ ]{ab}{\meta{A}\eiff\meta{B}}\bi{a1-b1,b2-a2}

       \have[m]{ab}{\meta{A}\eiff\meta{B}}
   \\  \have[n]{a}{\meta{A}}
       \have[\ ]{b}{\meta{B}} \be{ab,a}

       \have[m]{ab}{\meta{A}\eiff\meta{B}}
   \\  \have[n]{a}{\meta{B}}
       \have[\ ]{b}{\meta{A}} \be{ab,a}
   \end{nd}`

   .. rubric:: Neitun og mótsögn
      :name: neitun-og-mótsögn
      :class: unnumbered

   :math:`\begin{nd}
       \have[m]{a}{\meta{A}}
       \have[n]{na}{\enot\meta{A}}
       \have[ ]{bot}{\ered}\ri{a, na}
   \end{nd}`

   :math:`\begin{nd}
       \open
       \hypo[i]{a}{\meta{A}}
       \have[j]{nb}{\ered}
       \close
       \have[\ ]{na}{\enot\meta{A}}\ni{a-nb}
   \end{nd}`

   :math:`\begin{nd}
       \have[m]{bot}{\ered}
       \\\have[ ]{}{\meta{A}}\re{bot}
   \end{nd}`

   :math:`\begin{nd}
       \open
       \hypo[i]{a}{\meta{A}}
       \have[j]{c1}{\meta{B}}
       \close
       \open
       \hypo[k]{b}{\enot\meta{A}}
       \have[l]{c2}{\meta{B}}
       \close
       \have[\ ]{ab}{\meta{B}}\tnd{a-c1,b-c2}
   \end{nd}`

Afleiddar reglur fyrir setningarökfræði
---------------------------------------

.. container:: multicols

   2

   .. rubric:: Endurtekningarregla
      :name: endurtekningarregla
      :class: unnumbered

   :math:`\begin{nd}
           \have[m]{a}{\meta{A}}
           \have[\ ]{c}{\meta{A}} \by{R}{a}
       \end{nd}`

   .. rubric:: Eða-samliðuregla
      :name: eða-samliðuregla
      :class: unnumbered

   :math:`\begin{nd}
       \have[m]{ab}{\meta{A} \eor \meta{B}}
       \have[n]{nb}{\enot \meta{A}}
       \have[\ ]{con}{\meta{B}}\by{DS}{ab, nb}

       \have[m]{ab}{\meta{A} \eor \meta{B}}
   \\  \have[n]{nb}{\enot \meta{B}}
       \have[\ ]{con}{\meta{A}}\by{DS}{ab, nb}
   \end{nd}`

   .. rubric:: Modus Tollens
      :name: modus-tollens
      :class: unnumbered

   :math:`\begin{nd}
       \have[m]{ab}{\meta{A}\eif\meta{B}}
       \have[n]{a}{\enot\meta{B}}
       \have[\ ]{b}{\enot\meta{A}} \by{MT}{ab,a}
   \end{nd}`

   .. rubric:: Tvöföld neitunareyðing
      :name: tvöföld-neitunareyðing
      :class: unnumbered

   :math:`\begin{nd}
           \have[m]{dna}{\enot \enot \meta{A}}
           \have[ ]{a}{\meta{A}}\dne{dna}
       \end{nd}`

   .. rubric:: De Morgan-reglur
      :name: de-morgan-reglur
      :class: unnumbered

   :math:`\begin{nd}
       \have[m]{ab}{\enot (\meta{A} \eor \meta{B})}
       \have[\ ]{dm}{\enot \meta{A} \eand \enot \meta{B}}\dem{ab}

       \have[m]{ab}{\enot \meta{A} \eand \enot \meta{B}}
   \\  \have[\ ]{dm}{\enot (\meta{A} \eor \meta{B})}\dem{ab}

       \have[m]{ab}{\enot (\meta{A} \eand \meta{B})}
   \\  \have[\ ]{dm}{\enot \meta{A} \eor \enot \meta{B}}\dem{ab}

       \have[m]{ab}{\enot \meta{A} \eor \enot \meta{B}}
   \\  \have[\ ]{dm}{\enot (\meta{A} \eand \meta{B})}\dem{ab}
   \end{nd}`

Grunnreglur fyrir umsagnarökfræði
---------------------------------

.. container:: multicols

   2

   .. rubric:: Almagnaraeyðing
      :name: almagnaraeyðing
      :class: unnumbered

   :math:`\begin{nd}
       \have[m]{a}{\forall \meta{x}\meta{A}(\ldots \meta{x} \ldots \meta{x}\ldots)}
       \have[\ ]{c}{\meta{A}(\ldots \meta{c} \ldots \meta{c}\ldots)} \Ae{a}
   \end{nd}`

   .. rubric:: Almagnarainnleiðing
      :name: almagnarainnleiðing
      :class: unnumbered

   :math:`\begin{nd}
       \have[m]{a}{\meta{A}(\ldots \meta{c} \ldots \meta{c}\ldots)}
       \have[\ ]{c}{\forall \meta{x}\meta{A}(\ldots \meta{x} \ldots \meta{x}\ldots)} \Ai{a}
   \end{nd}`

   | má ekki kom fyrir í ólosaðri forsendu
   | má ekki koma fyrir í
     :math:`\meta{A}(\ldots \meta{c} \ldots \meta{c}\ldots)`

   .. rubric:: Tilvistarinnleiðing
      :name: tilvistarinnleiðing
      :class: unnumbered

   :math:`\begin{nd}
       \have[m]{a}{\meta{A}(\ldots \meta{c} \ldots \meta{c}\ldots)}
       \have[\ ]{c}{\exists \meta{x}\meta{A}(\ldots \meta{x} \ldots \meta{c}\ldots)} \Ei{a}
   \end{nd}`

   má ekki koma fyrir í
   :math:`\meta{A}(\ldots \meta{c} \ldots \meta{c}\ldots)`

   .. rubric:: Tilvistareyðing
      :name: tilvistareyðing
      :class: unnumbered

   :math:`\begin{nd}
       \have[m]{a}{\exists \meta{x}\meta{A}(\ldots \meta{x} \ldots \meta{x}\ldots)}
       \open   
           \hypo[i]{b}{\meta{A}(\ldots \meta{c} \ldots \meta{c}\ldots)}
           \have[j]{c}{\meta{B}}
       \close
       \have[\ ]{d}{\meta{B}} \Ee{a,b-c}
   \end{nd}`

   má ekki koma fyrir í ólosaðri forsendu, í
   :math:`\exists \meta{x}\meta{A}(\ldots \meta{x} \ldots \meta{x}\ldots)`,
   né í :math:`\meta{B}`

Samsemdarinnleiðing
~~~~~~~~~~~~~~~~~~~

:math:`\begin{nd}
    \have[\ \,\,\,]{x}{\meta{c}=\meta{c}} \by{=I}{}
\end{nd}`

Samsemdareyðing
~~~~~~~~~~~~~~~

.. container:: multicols

   2

   :math:`\begin{nd}
       \have[m]{e}{\meta{a}=\meta{b}}
       \have[n]{a}{\meta{A}(\ldots \meta{a} \ldots \meta{a}\ldots)}
       \have[\ ]{ea1}{\meta{A}(\ldots \meta{b} \ldots \meta{a}\ldots)} \by{=E}{e,a}
   \end{nd}`

   :math:`\begin{nd}
       \have[m]{e}{\meta{a}=\meta{b}}
       \have[n]{a}{\meta{A}(\ldots \meta{b} \ldots \meta{b}\ldots)}
       \have[\ ]{ea2}{\meta{A}(\ldots \meta{a} \ldots \meta{b}\ldots)} \by{=E}{e,a}
   \end{nd}`

Afleiddar reglur fyrir umsagnarökfræði
--------------------------------------

.. container:: multicols

   2

   :math:`\begin{nd}
       \have[m]{ab}{\forall \meta{x}\enot \meta{A}}
       \have[\ ]{ac}{\enot \exists \meta{x} \meta{A}}\cq{m}

       \have[m]{ab}{\enot \exists \meta{x}  \meta{A}}
   \\  \have[\ ]{ac}{\forall \meta{x}\enot\meta{A}}\cq{m}
   \end{nd}`

   :math:`\begin{nd}
       \have[m]{ab}{\exists \meta{x}\enot\meta{A}}
       \have[\ ]{ac}{\enot \forall \meta{x} \meta{A}}\cq{m}

       \have[m]{ab}{\enot \forall \meta{x}  \meta{A}}
   \\  \have[\ ]{ac}{\exists \meta{x}\enot \meta{A}}\cq{m}
   \end{nd}`
