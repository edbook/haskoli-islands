Veldaraðir
==========

*What to do if you find yourself stuck in a crack in the ground underneath 
a giant boulder you can't move, with no hope of rescue. Consider how lucky 
you are that life has been good to you so far. Alternatively, if life hasn't 
been good to you so far, which given your current circumstances seems more 
likely, consider how lucky you are that it won't be troubling you much longer.*

-- Douglas Adams, The Original Hitchhiker Radio Scripts



.. todo::
    vantar myndir/geogebra, t.d. eins og Sage/Interact/Taylor

.. index::
    veldaröð
    röð; veldaröð
    
Veldaraðir
----------

Skilgreining
~~~~~~~~~~~~

Röð á forminu

.. math:: \sum_{n=0}^\infty a_n(x-c)^n=a_0+a_1(x-c)+a_2(x-c)^2+\cdots

kallast :hover:`veldaröð` með :hover:`miðju` í punktinum :math:`c`.

.. _setning-samleitnigeisli:

Setning
~~~~~~~

Um sérhverja veldaröð :math:`\sum_{n=0}^\infty a_n(x-c)^n` gildir eitt
af þrennu:

(i)   Röðin er aðeins samleitin fyrir :math:`x=c`.

(ii)  Til er jákvæð tala :math:`R` þannig að veldaröðin er alsamleitin
      fyrir öll :math:`x` þannig að :math:`|x-c|<R` og ósamleitin fyrir
      öll :math:`x` þannig að :math:`|x-c|>R`. 

(iii) Röðin er samleitin fyrir allar rauntölur :math:`x`.

.. index::
    veldaröð; samleitnigeisli
    veldaröð; miðja
    veldaröð; samleitnibil


Skilgreining: Miðja og samleitnigeisli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`\sum_{n=0}^\infty a_n(x-c)^n` vera veldaröð.

(i)   Talan :math:`c` kallast *miðja* eða *samleitnimiðja*
      veldaraðarinnar.

(ii)  Í tilviki 2. í setningunni hér á undan er röðin alsamleitin á opna bilinu
      :math:`(c-R, c+R)` og ósamleitin fyrir utan lokaða bilið 
      :math:`[c-R, c+R]`.
      
      Talan :math:`R` er kölluð :hover:`samleitnigeisli` raðarinnar.

      Mögulegt er að röðin sé samleitin (alsamleitin eða skilyrt
      samleitin) í öðrum eða báðum punktunum :math:`x=c-R` og
      :math:`x=c+R` (þetta þarf að athuga sérstaklega).

      Í tilfelli 1. í setningunni þegar röðin er bara samleitin fyrir :math:`x=c`
      setjum við :math:`R=0` og í tilfelli 3. þegar röðin er
      samleitin fyrir allar rauntölur :math:`x` þá setjum við
      :math:`R=\infty`.

(iii) :hover:`Samleitnibil` veldaraðarinnar
      :math:`\sum_{n=0}^\infty a_n(x-c)^n` er mengi allra gilda
      :math:`x` þannig að röðin er samleitin. Setning hér á undan sýnir að
      :þetta mengi er alltaf bil.

    
      - Þegar samleitnigeilsinn er 0 er samleitnibilið :math:`\{c\}`.
      
      - Þegar samleitnigeislinn er :math:`R>0` þá koma fjórir möguleikar 
        til greina eftir því hvort röðin er
        samleitin í hvorugum, öðrum eða báðum punktunum :math:`x=c-R` og
        :math:`x=c+R`. Samleitnibilið getur verið
        :math:`(c-R, c+R)`, :math:`[c-R, c+R)`, :math:`(c-R, c+R]` eða :math:`[c-R, c+R]`.

      - Þegar samleitnigeislinn er :math:`\infty` þá er samleitnibilið :math:`(-\infty, \infty)`.

.. index::
    veldaröð; samleitnipróf

Samleitnipróf
-------------

Setning
~~~~~~~

Látum :math:`\sum_{n=0}^\infty a_n(x-c)^n` vera veldaröð.

(i)  :hover:`Kvótapróf`: Gerum ráð fyrir að
     :math:`L=\lim_{n\rightarrow\infty}\left|\frac{a_{n+1}}{a_n}\right|`
     sé til eða :math:`\infty`.

     Þá hefur veldaröðin :math:`\sum_{n=0}^\infty a_n(x-c)^n`
     samleitnigeisla

     .. math::

        R= \left\{\begin{array}{ll}
        \infty & \text{ef }L=0,\\
        \frac{1}{L} & \text{ef }0<L<\infty,\\
        0 & \text{ef }L=\infty.\\ 
        \end{array} \right.

(ii) :hover:`Rótarpróf`: Gerum ráð fyrir að
     :math:`L=\lim_{n\rightarrow\infty}\sqrt[n]{|a_n|}` sé til eða
     :math:`\infty`. Þá hefur veldaröðin
     :math:`\sum_{n=0}^\infty a_n(x-c)^n` samleitnigeisla

     .. math::

        R= \left\{\begin{array}{ll}
        \infty & \text{ef }L=0,\\
        \frac{1}{L} & \text{ef }0<L<\infty,\\
        0 & \text{ef }L=\infty.\\
        \end{array}
        \right.

.. index::
    setning Abels
        
Setning Abels
~~~~~~~~~~~~~

Fallið :math:`f` skilgreint á samleitnibili með

.. math:: f(x)=\sum_{n=0}^\infty a_n(x-c)^n

er samfellt á öllu samleitnibili veldaraðarinnar.

Ef samleitnigeislinn er :math:`0<R<\infty` og röðin er samleitin í
punktinum :math:`x=c+R` þá er

.. math::

   \lim_{x\rightarrow (c+R)^-}f(x)=f(c+R)=\sum_{n=0}^\infty
   a_n((c+R)-c)^n=\sum_{n=0}^\infty a_nR^n.

Eins ef röðin er samleitin í punktinum :math:`x=c-R` þá er

.. math::

   \lim_{x\rightarrow (c-R)^+}f(x)=f(c-R)=\sum_{n=0}^\infty
   a_n((c-R)-c)^n=\sum_{n=0}^\infty a_n(-R)^n.


Setning: Diffrað lið fyrir lið
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`\sum_{n=0}^\infty a_n(x-c)^n=a_0+a_1(x-c)+a_2(x-c)^2+a_3(x-c)^3+\cdots`
vera veldaröð með miðju í :math:`c` og samleitnigeisla :math:`R`.

Fyrir :math:`x\in(c-R, c+R)` skilgreinum við

.. math:: f(x)=\sum_{n=0}^\infty a_n(x-c)^n.

Fallið :math:`f` er diffranlegt og

.. math:: f'(x)=\sum_{n=1}^\infty na_n(x-c)^{n-1}=a_1+2a_2(x-c)+3a_3(x-c)^2+\cdots

og röðin fyrir :math:`f'(x)` er samleitin fyrir öll
:math:`x\in(c-R, c+R)`.

Þetta þýðir að við getum diffrað veldaraðir lið fyrir lið.

Þar sem diffranleg föll eru samfelld þá fæst eftirfarandi.

Fylgisetning
~~~~~~~~~~~~

Fallið :math:`f` er samfellt á :math:`(c-R, c+R)`.

Setning: Heildað lið fyrir lið
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum
:math:`\sum_{n=0}^\infty a_n(x-c)^n=a_0+a_1(x-c)+a_2(x-c)^2+a_3(x-c)^3+\cdots`
vera veldaröð með miðju í :math:`c` og samleitnigeisla :math:`R`.

Fyrir :math:`x\in(c-R, c+R)` skilgreinum við
:math:`f(x)=\sum_{n=0}^\infty a_n(x-c)^n`.

Fallið :math:`f` hefur stofnfall

.. math::

   \begin{gathered}
   F(x)=\sum_{n=0}^\infty \frac{a_n}{n+1}(x-c)^{n+1} \\
   =a_0(x-c)+\frac{a_1}{2}(x-c)^2+\frac{a_2}{3}(x-c)^3+
   \frac{a_3}{4}(x-c)^4+\cdots\end{gathered}

og röðin fyrir :math:`F(x)` er samleitin fyrir öll
:math:`x\in(c-R, c+R)`.

Þetta þýðir að við getum heildað veldaraðir lið fyrir lið.

Setning
~~~~~~~

Látum :math:`\sum_{n=0}^\infty a_n(x-c)^n=a_0+a_1(x-c)+a_2(x-c)^2+a_3(x-c)^3+\cdots`
vera veldaröð með miðju í :math:`c` og samleitnigeisla :math:`R`.

Fyrir :math:`x\in(c-R, c+R)` skilgreinum við

.. math:: f(x)=\sum_{n=0}^\infty a_n(x-c)^n.

Fallið :math:`f` er :math:`k`-sinnum diffranlegt fyrir :math:`k=1, 2, 3, \ldots` og

.. math:: a_k=\frac{f^{(k)}(c)}{k!}.

.. index::
    veldaröð; fágað fall
    fall; fágað

Skilgreining: Fágað fall
~~~~~~~~~~~~~~~~~~~~~~~~

Fall :math:`f` þannig að til er veldaröð
:math:`\sum_{n=0}^\infty a_n(x-c)^n` með samleitnigeisla :math:`R>0`
þannig að

.. math:: f(x)=\sum_{n=0}^\infty a_n(x-c)^n

fyrir öll :math:`x\in(c-R, c+R)` kallast *fágað* (raunfágað) í punktinum
:math:`c`.

Athugasemd
~~~~~~~~~~

Dæmi um fáguð föll eru margliður, ræð föll, hornaföll, veldisföll og
lograr.

.. index::
    Taylorröð
    veldaröð; Taylorröð
    Taylorröð; Maclaurinröð

Taylorraðir
-----------

Skilgreining: Taylorröð
~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að fall :math:`f(x)` sé óendanlega oft diffranlegt í
punktinum :math:`x=c`, (það er :math:`f^{(k)}(c)` er til fyrir
:math:`k=0, 1, 2, \ldots`).

Veldaröðin

.. math::

   \begin{aligned}
   \sum_{n=0}^\infty \frac{f^{(n)}(c)}{n!}(x-c)^n = & f(c)+f'(c)(x-c)+
   \frac{f''(c)}{2}(x-c)^2 \\ & + \frac{f'''(c)}{3!}(x-c)^3 
   + \frac{f^{(4)}(c)}{4!}(x-c)^4 + \cdots \end{aligned}

kallast *Taylorröð* með miðju í :math:`x=c` fyrir :math:`f(x)`.

Ef svo vill til að :math:`c=0` þá er oft talað um *Maclaurinröð*.

.. ggb:: nVtCB2v9
    :width: 700
    :height: 400
    :img: 03_Taylorrod.png
    :imgwidth: 12cm
    :zoom_drag: true
      
Setning
~~~~~~~

Taylormargliða með miðju í :math:`c` fyrir :math:`f` er skilgreind sem
margliðan

.. math::

   \begin{aligned}
     P_n(x)& =\sum_{n=0}^n \frac{f^{(k)}(c)}{n!}(x-c)^n \\
     &=f(c)+f'(c)(x-c)+ \frac{f''(c)}{2}(x-c)^2+\cdots+\frac{f^{(n)}(c)}{n!}(x-c)^n.\end{aligned}

Skekkjan í :math:`n`-ta stigs Taylornálgun er
:math:`R_n(x)=f(x)-P_n(x)`.

Til er tala :math:`X` sem liggur á milli :math:`c` og :math:`x` þannig
að

.. math:: R_n(x)=\frac{f^{(n+1)}(X)}{(n+1)!}(x-c)^{n+1}.

Setning
~~~~~~~

Gerum ráð fyrir að :math:`f` sé fall sem er óendanlega oft diffranlegt í
punktinum :math:`c`.

Fyrir fast gildi á :math:`x` þá er Taylorröðin

.. math:: \sum_{n=0}^\infty \frac{f^{(n)}(c)}{n!}(x-c)^n

samleitin með summu :math:`f(x)` ef og aðeins ef

.. math:: \lim_{n\rightarrow\infty}R_n(x)=0.

.. index::
    Taylorröð; tvíliðuröð

Dæmi: Tvíliðuröðin
~~~~~~~~~~~~~~~~~~

Fyrir :math:`x` þannig að :math:`|x|<1` og rauntölu :math:`r` gildir að

.. math::

   \begin{aligned}
   (1+x)^r =& 1+rx+\frac{r(r-1)}{2!}x^2+ \frac{r(r-1)(r-2)}{3!}x^3 \\ 
   &+\frac{r(r-1)(r-2)(r-3)}{4!}x^4+\cdots\\
   =& 1+ \sum_{n=1}^\infty \frac{r(r-1)(r-2)\cdots(r-n+1)}{n!}x^n.\end{aligned}

Athugasemd
~~~~~~~~~~

Ef :math:`r \in {{\mathbb  N}}` þá gefur summan að ofan einfaldlega
stuðlanna þegar búið er að margfalda upp úr svigum, og summan er því
endanleg, því þegar :math:`n \geq r+1` þá verða stuðlarnir 0.

Ef hins vegar :math:`r\notin {{\mathbb  N}}` þá er enginn stuðlanna 0.

Taylorraðir nokkra falla
~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   \begin{aligned}
   e^x&=\sum_{n=0}^\infty\frac{x^n}{n!}
       =1+x+\frac{x^2}{2}+\frac{x^3}{3!}
       +\cdots
     &\text{fyrir öll }x\\
   \sin x&=  \sum_{n=0}^\infty\frac{(-1)^n}{(2n+1)!}x^{2n+1}
       =x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\cdots
       &\text{fyrir öll }x\\ 
   \cos x&=  \sum_{n=0}^\infty\frac{(-1)^n}{(2n)!}x^{2n}
       =1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+\cdots
       &\text{fyrir öll }x\\
   \frac{1}{1-x}&=\sum_{n=0}^\infty x^n
       =1+x+x^2+x^3+\cdots
   &\text{fyrir }-1<x<1\\
   \frac{1}{(1-x)^2}&=\sum_{n=1}^\infty nx^{n-1}
       =1+2x+3x^2+4x^3+\cdots
   &\text{fyrir }-1<x<1\\
   \ln(1+x)&=  \sum_{n=1}^\infty\frac{(-1)^{n-1}}{n}x^n
       =x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\cdots
       &\text{fyrir }-1<x\leq 1\\
   \tan^{-1} x&=  \sum_{n=0}^\infty\frac{(-1)^n}{2n+1}x^{2n+1}
       =x-\frac{x^3}{3}+\frac{x^5}{5}-\frac{x^7}{7}+\cdots
       &\text{fyrir }-1\leq x\leq 1\\\\
   \sinh x&=  \sum_{n=0}^\infty\frac{x^{2n+1}}{(2n+1)!}
       =x+\frac{x^3}{3!}+\frac{x^5}{5!}+\frac{x^7}{7!}+\cdots
       &\text{fyrir öll } x\\
   \cosh x&=  \sum_{n=0}^\infty\frac{x^{2n}}{(2n)!}
       =1+\frac{x^2}{2!}+\frac{x^4}{4!}+\frac{x^6}{6!}+\cdots
       &\text{fyrir öll } x\\\end{aligned}



*I may not have gone where I intended to go, but I think I have ended up where I needed to be.*

-- Douglas Adams, The Long Dark Tea-Time of the Soul

