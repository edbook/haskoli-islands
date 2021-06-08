Diffrun
=======

Skýringardæmi
-------------

Áður en við skilgreinum :hover:`afleiðu, afleiða` falls skulum við taka dæmi til þess að reyna að útskýra hver hugmyndin er.

Við skulum hugsa okkur bíl í spyrnukeppni á 500 metra braut.
Áður en bíllinn fer af stað er sett í hann nákvæmt staðsetningartæki sem getur teiknað upp graf sem lýsir staðsetningu hans á brautinni miðað við tímann sem er liðinn frá upphafi spyrnunnar.

Bíllinn fer af stað og keyrir brautina á nákvæmlega tíu sekúndum.
Eftir keppnina er staðsetningartækið skoðað og það sýnir að staðsetningu bílsins sem fall af tíma megi lýsa með formúlunni:

.. math::
    s(t) = 5t^2

.. image:: ./myndir/diffrun/bill.svg
    :align: center

þar sem :math:`t \in [0, 10]` táknar tímann frá upphafi spyrnunnar mældan í sekúndum og :math:`s(t)` er vegalengdin sem bíllinn var þá búinn að keyra mæld í metrum.

Þessi formúla segir okkur til dæmis að eftir fjórar sekúndur var bíllinn búinn að keyra 80 metra því :math:`s(4) = 5 \cdot 4^2 = 80`; og eftir átta sekúndur var bíllinn búinn að keyra :math:`320` metra þar eð :math:`s(8) = 5\cdot 8^2 =320`.

Eins og við má búast er :math:`s(0) = 0` sem þýðir að eftir núll sekúndur stóð bíllinn enn óhreyfður, og :math:`s(10) = 500`, í samræmi við að bíllinn hafi keyrt brautina sem var :math:`500` metrar á tíu sekúndum.

Úr formúlunni er þó hægt að fá meiri upplýsingar heldur en bara staðsetningu bílsins.
Þessi formúla dugar líka til þess að reikna út **hraða bílsins á sérhverjum tímapunkti**.
Skoðum hvernig það er gert og prófum að reikna nákvæman hraða bílsins að fjórum sekúndum liðnum í spyrnunni.

Athugum að *meðalhraði* bílsins yfir ákveðið tímabil er skilgreindur sem vegalengdin sem bíllinn fer á því tímabili deilt með lengdinni á tímabilinu.
Þannig var til dæmis meðalhraði bílsins í allri spyrnunni :math:`50` metrar á sekúndu því hann fór :math:`500` metra á :math:`10` sekúndum og :math:`\frac{500}{10} = 50`.

Áður en við getum reiknað út nákvæman hraða bílsins á tímanum :math:`t = 4` skulum við skoða meðalhraða bílsins á nokkrum tímabilum.

* Skoðum fyrst meðalhraða bílsins á tímabilinu frá fjórum upp í átta sekúndur. Á sekúndu átta er bíllinn kominn :math:`5 \cdot 8^2 = 320` metra.
  Á sekúndu fjögur er bíllinn kominn :math:`5 \cdot 4^2 = 80` metra.
  Vegalengdin sem hann færist á tímabilinu frá fjórum til átta sekúndur er þá :math:`320 − 80 = 240` metrar.
  Lengdin á þessu tímabili er fjórar sekúndur. Meðalhraði bílsins á tímabilinu frá fjórum upp í átta sekúndur er þá:

 .. math::
    \frac{230}{4} = 57.5 \text{ m/s}

 .. image:: ./myndir/diffrun/bill1.svg
    :align: center

 Hér er hallatala línunar á milli :math:`(4, s(4) = 80)` og :math:`(8, s(8) = 320)` jöfn :math:`57.5`.

* Skoðum næst meðalhraða bílsins frá fjórum upp í sex sekúndur.
  Vegalengdin sem hann fer á því tímabili er :math:`5 \cdot 6^2 −5 \cdot 4^2 = 100` metrar.
  Lengdin á tímabilinu er :math:`6 − 4 = 2` sekúndur. Meðalhraði bílsins er þá:

 .. math::
    \frac{100}{2} = 50 \text{ m/s}.


 .. image:: ./myndir/diffrun/bill2.svg
    :align: center

 Hér er hallatala línunnar á milli :math:`(4, s(4) = 80)` og :math:`(6, s(6) = 180)` jöfn :math:`50`.

* Skoðum meðalhraða bílsins frá fjórum upp í fimm sekúndur. Hann er:

 .. math::
    \frac{5 \cdot 5^2 - 5 \cdot 4^2}{5 -4} = \frac{45}{1} = 45 \text{ m/s}.


 .. image:: ./myndir/diffrun/bill3.svg
    :align: center

 Hér er hallatala línunar á milli :math:`(4, s(4) = 80)` og :math:`(5, s(5) = 125)` jöfn :math:`45`.

* Meðalhraði bílsins frá fjórum upp í fjórar og hálfa sekúndu er:

 .. math::
    \frac{5 \cdot4.5^2 - 5 \cdot 4^2}{ 4.5-4} = \frac{21.25}{0.5} = 42.5 \text{ m/s}.

* Meðalhraði bílsins frá fjórum upp í :math:`4.25` sekúndu er:

 .. math::
    \frac{5 \cdot4.25^2 - 5 \cdot 4^2}{ 4.25-4} = \frac{10.3125}{0.25} = 41.25 \text{ m/s}.


Nú eruð þið kannski farin að átta ykkur á hvað er að fara að gerast.
Með því að stytta tímabilið meira og meira þá verður meðalhraðinn nær og nær raunverulega hraðanum í tímanum :math:`t = 4`.

Þetta er farið að líkjast því að taka :hover:`markgildi`.
Almennt gildir að meðalhraði bílsins frá fjórum sekúndum upp í :math:`t` sekúndur er:

.. math::
    \frac{5t^2−5 \cdot 4^2}{ t−4}

Þegar við styttum tímabilið meir og meir þá erum við í raun að láta töluna hér að ofan stefna á fjóra.

Þess vegna fáum við að nákvæmur hraði bílsins á tímanum :math:`t = 4` er:

.. math::
    \begin{aligned}
    \lim_{t \to 4} \frac{5t^2−5 \cdot 4^2}{ t−4} & = \lim_{t \to 4} \frac{5(t^2−4^2)}{ t−4} \\
    & = \lim_{t \to 4} \frac{5(t+4)(t−4)}{t−4} \\
    & = \lim_{t \to 4} \frac{5(t+4)}{1} \\
    & = 5(4+4) = 40
    \end{aligned}

Það er að segja, nákvæmur hraði bílsins þegar akkúrat fjórar sekúndur eru liðnar er :math:`40` metrar á sekúndu.

Hér fór mikið púður í að reikna út hraða bílsins á einum tímapunkti.
Segjum að við viljum reikna út hraða bílsins í hundrað mismunandi tímapunktum, þá yrði þreytandi að þurfa að reikna út hundrað mismunandi markgildi.
Skynsamlegra væri að reyna að finna út nákvæma formúlu sem gefur upp hraða bílsins á sérhverjum tíma. Það er hægt!

Til þess að reikna út hraða bílsins á tímanum :math:`t=4` þá þurftum við að reikna út markgildið:

.. math::
    \lim_{t\to 4}\frac{5t^2-5\cdot 4^2}{t-4}

Ef við viljum reikna út hraða bílsins á einhverjum öðrum tíma :math:`t=t_0` þá reiknum við markgildið:

.. math::
    \lim_{t\to t_0}\frac{5t^2-5\cdot t_0^2}{t-t_0}.

En þetta er eitthvað sem að við getum reiknað út almennt fyrir hvert fall sem lýsir staðsetningu:

.. math::
    \begin{aligned}
    \lim_{t\to t_0}\frac{5t^2-5\cdot t_0^2}{t-t_0} &=\lim_{t\to t_0}\frac{5(t^2-t_0^2)}{t-t_0} \\
    &=\lim_{t\to t_0}\frac{5(t+t_0)(t-t_0)}{t-t_0}\\
    &=\lim_{t\to t_0}\frac{5(t+t_0)}{1} \\
    &=\frac{5(t_0+t_0)}{1}=10 t_0. \\
    \end{aligned}

Við höfum séð að á tímanum :math:`t=t_0` þá er hraði bílsins :math:`10t_0` m/s
Með öðrum orðum þá má lýsa hraða bílsins af tíma með fallinu sem gefið er með formúlunni

.. math::
    v(t)=10t.

Af þessu má lesa að hraði bílsins á sekúndu fjögur er :math:`4\cdot 10=40` m/s og hraði bílsins á sekúndu átta er :math:`8\cdot 10=80` m/s.
Munum að bíllinn byrjar kyrrstæður svo það kemur ekki á óvart að :math:`v(0)=0` sem má túlka sem svo að hraði bílsins á sekúndunni núll sé núll.


 .. image:: ./myndir/diffrun/bill4.svg
    :align: center

Hér sjáum við línu sem er með hallatöluna :math:`40` í punktinum :math:`(4, s(4) = 80)` sem gefur okkur línuna :math:`y = 40x -80`.

Aðferðin sem hér var notuð kallast  :hover:`diffrun` (deildun).
Þessi aðferð er ekki bundin við þetta einstaka fall, heldur má gera þetta almennt. Segjum að hraði bílsins hafi verið gefinn með einhverju öðru falli :math:`k(t)`.
Hraði bílsins í tímapunktinum :math:`t=t_0` verður þá fundinn með því að reikna markgildið

.. math::
    \lim_{t\to t_0}\frac{k(t)-k(t_0)}{t-t_0}.

Skilgreining
------------

Gerum ráð fyrir að :math:`f:\;I\to \mathbb{R}` sé fall sem er skilgreint á bili :math:`I`.
Látum :math:`a\in I`.
Fallið :math:`f` er sagt vera :hover:`diffranlegt, diffranleiki` (deildanlegt) í punktinum :math:`a` ef að markgildið

.. math::
   \lim_{x\to a}\frac{f(x)-f(a)}{x-a}

er skilgreint og jafnt einhverri rauntölu (*ekki plús eða mínus óendanlegt*).
Þessi rauntala er táknuð með :math:`f'(a)` og kallast afleiða fallsins :math:`f` í punktinum :math:`a`.

Þegar afleiða fallsins :math:`f` er reiknuð í ótilteknum punkti getur verið þægilegra að notast við umritaða skilgreiningu:

.. math::
    f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}



Ef fallið :math:`f` er deildanlegt í sérhverjum punkti bilsins :math:`I` þá segjum við að :math:`f` sé diffranlegt (deildanlegt) fall á :math:`I` og þá er afleiðan :math:`f'` fall á :math:`I`.
Aðgerðin að finna afleiðu falls kallast :hover:`diffrun` (deildun) falls og yfirleitt er talað um sögnina að :hover:`diffra` (deilda).


.. tip::
    Notið skilgreininguna á afleiðu til að reikna afleiðu fallanna.

    **1.** :math:`f(x) = 2x^2-16x+5`
     Notum skilgreininguna á afleiðu :math:`f'(x) = \lim_{h\to 0}\frac{f(x+h)-f(a)}{h}` sem gefur

     .. math::
        f'(x) = \lim_{h\to 0} \frac{\left(2(x+h)^2 - 16(x+h) +5\right)-\left(2x^2 - 16x + 5\right)}{h}

     Sjáum að við þurfum að umrita til að fá markgildi sem við getum reiknað, því við getum ekki sett :math:`h= 0` strax.

     .. math::
        \begin{aligned}
        f'(x) &= \lim_{h\to 0} \frac{\left(2(x+h)^2 - 16(x+h) +5\right)-\left(2x^2 - 16x + 5\right)}{h}\\
        &=\lim_{h\to 0} \frac{2x^2+4xh + 2h^2 - 16x -16h +5 -2x^2 + 16x-5}{h}\\
        &= \lim_{h\to 0} \frac{4xh + 2h^2 - 16h}{h}
        \end{aligned}

     Hér getum við tekið :math:`h` út fyrir sviga og stytt það út:

     .. math::
        \begin{aligned}
        f'(x) &= \lim_{h\to 0} \frac{4xh + 2h^2 - 16h}{h}\\
        &=\lim_{h\to 0} \frac{h(4x + 2h- 16)}{h}\\
        &=\lim_{h\to 0} 4x +2h - 16\\
        &= 4x + 2(0) -16\\
        &= 4x - 16
        \end{aligned}

     Þá er afleiðan :math:`f'(x) = 4x-16` .


    **2.** :math:`g(x) = \frac{x}{x+1}`
     Notum skilgreininguna á afleiðu :math:`g'(x) = \lim_{h\to 0}\frac{g(x+h)-g(a)}{h}` sem gefur

     .. math::
        g'(x) = \lim_{h\to 0} \frac{1}{h} \left(\frac{x+h}{x+h+1} - \frac{x}{x+1}\right)

     Hér þurfum við líka að umrita til að geta sett :math:`h=0`

     .. math::
        \begin{aligned}
        g'(x) &= \lim_{h\to 0} \frac{1}{h} \cdot \left(\frac{x+h}{x+h+1} - \frac{x}{x+1}\right) \\
        &= \lim_{h\to 0} \frac{1}{h} \cdot \left(\frac{(x+h)(x+1)- x(x+h+1)}{(x+h+1)(x+1)}\right) \\
        &= \lim_{h\to 0} \frac{1}{h} \cdot \left(\frac{x^2 +x +xh+h -(x^2+xh+x)}{(x+h+1)(x+1)}\right) \\
        &= \lim_{h\to 0} \frac{1}{h} \cdot \left(\frac{h}{(x+h+1)(x+1)}\right) \\
        &= \lim_{h\to 0} \frac{1}{(x+h+1)(x+1)} \\
        &= \frac{1}{(x+1)(x+1)}\\
        &= \frac{1}{(x+1)^2}
        \end{aligned}

     Þá er afleiðan :math:`g'(x)= \frac{1}{(x+1)^2}`.

.. warning::
    **Ritháttur**:
    Takið eftir að

     .. math::
        f'(x), \qquad f', \qquad \frac{df}{dx}, \qquad \frac{d}{dx} f(x), \text{ og } \qquad D_x f

    eru mismunandi rithættir fyrir "afleiða :math:`f(x)` m.t.t. :math:`x`."

Reiknireglur
------------

Gerum ráð fyrir að :math:`f,g` séu deildanleg föll á :math:`\mathbb{R}`.

Látum :math:`a\in \mathbb{R}` vera fasta.

Þá gildir:


.. math::
    \begin{aligned}
    1.& \quad (a\cdot f)'=af' \\
    &\\
    2.& \quad (f+g)'=f'+g' \\
    &\\
    3.& \quad (f-g)'=f'-g' \\
    &\\
    4.& \quad (f\cdot g)'=f'g+fg' \\
    &\\
    4.& \quad (f\circ g)'=(f'\circ g)\cdot g' \\
    \end{aligned}


Ef :math:`g(x)` er ekki jafnt núlli fyrir öll :math:`x\in I`, þá gildir einnig:

.. math::
    \begin{aligned}
    6.& \quad \left(\frac{1}{g}\right)'=\frac{-g'}{g^2} \\
    &\\
    7.& \quad \left(\frac{f}{g}\right)'=\frac{f'g-fg'}{g^2} \\
    \end{aligned}

Ef :math:`f` er andhverfanlegt og :math:`f(x_0)=y_0` þá er

.. math::
    8. (f^{-1})'\circ f=\frac{1}{f'}




Þekktar afleiður
----------------

1. Ef :math:`a` er fasti og :math:`f(x)=a` þá er

.. math::
    f'(x)=0

2. Ef :math:`n\in \mathbb{N}` og :math:`f(x)=x^n` þá er

.. math::
    f'(x)=nx^{n-1}

3. Ef :math:`n\in \mathbb{Z}\setminus\{0\}` og :math:`f(x)=x^{n}` þá er

.. math::
    f'(x)=nx^{n-1}

4. Ef :math:`n\in \mathbb{Q}\setminus\{0\}` og :math:`f(x)=x^n` þá er

.. math::
    f'(x)=nx^{n-1}

5. Ef :math:`n\in \mathbb{R}\setminus\{0\}` og :math:`f(x)=x^n` þá er

.. math::
    f'(x)=nx^{n-1}

6. Ef :math:`a\in \mathbb{R}_+` og :math:`f(x)=a^x` þá er

.. math::
    f'(x)=\ln(a)a^x

7. Ef :math:`a\in \mathbb{R}_+` og :math:`f(x)=\log_a(x)` þá er

.. math::
    f'(x)=\frac{1}{\ln(a)x}

8. Ef :math:`f(x) = \ln(x)` þá er

.. math::
    f'(x) = \frac{1}{x}

9. Ef :math:`f(x) = e^x` þá er

.. math::
    f'(x) = e^x

10. Ef :math:`f(x)=\cos(x)` þá er

.. math::
    f'(x)=-\sin(x)

11. Ef :math:`f(x)=\sin(x)` þá er

.. math::
    f'(x)=\cos(x)

12. Ef :math:`f(x)=\tan(x)` þá er

.. math::
    f'(x)=\frac{1}{\cos^2(x)}

13. Ef :math:`f(x)=\cot(x)` þá er

.. math::
    f'(x)=\frac{-1}{\sin^2(x)}

14. Ef :math:`f(x)=\text{arcsin(x)}` þá er

.. math::
    f'(x)=\frac{1}{\sqrt{1-x^2}}

15. Ef :math:`f(x)=\text{arccos(x)}` þá er

.. math::
    f'(x)=\frac{-1}{\sqrt{1-x^2}}

16. Ef :math:`f(x)=\text{arctan(x)}` þá er

.. math::
    f'(x)=\frac{1}{1+x^2}

17. Ef :math:`(x)=\text{arccot(x)}` þá er

.. math::
    f'(x)=\frac{-1}{1+x^2}

.. tip::
    Notum okkur nú reiknireglurnar og þekktar afleiður til að reikna eftirfarandi afleiður.

    **1.** :math:`f(x) = 2x^2-16x+5`

     Við vitum út frá reiknireglu 2, :math:`(f+g)'=f'+g'` sem þýðir að við getum horft á hvern lið sér og svo lagt þá saman að lokum.
     Byrjum á að nota okkur að :math:`f(x)=x^n` gefur :math:`f'(x)=nx^{n-1}` og reiknireglu 1, :math:`(a\cdot f)'=af'`

     * þá er afleiðan af :math:`2(x^2)` jöfn :math:`2(2x^{2-1}) = 4x`
     * þá er afleiðan af :math:`16x` jöfn :math:`16(1x^{1-1} )= 16`
     * munum líka að afleiða fastafalls er jafnt og núll, þ.e.a.s. afleiða :math:`5` er :math:`0`

     Leggjum alla liðina saman og fáum :math:`f'(x) = 4x + 16 + 0`

     Þá er afleiðan

     .. math::
        f'(x) = 4x + 16



    **2.** :math:`h(x) = \frac{x}{x+1}`

     Hér þurfum við að nota reiknireglu 7. :math:`\left(\frac{f}{g}\right)'=\frac{f'g-fg'}{g^2}`

     * nefnarinn  gefur okkur :math:`1` þar sem afleiða :math:`x` er :math:`1`

     * teljarinn gefur okkur líka :math:`1` þar sem afleiða :math:`x` er :math:`1` og afleiða :math:`1` er :math:`0`

     Setjum þessar niðurstöður inn í reikniregluna (í þessu tilfelli er :math:`f = x`, :math:`g = x+1`, :math:`f' = 1` og :math:`g' = 1`)

     .. math::
         \begin{aligned}
            \left(\frac{f}{g}\right)' &=\frac{f'g-fg'}{g^2}\\
            (\frac{x}{x+1})' &= \frac{(1) \cdot (x+1) - (x) \cdot (1)}{(x+1)^2}\\
            &= \frac{(x+1)- x}{(x+1)^2} \\
            &= \frac{1}{(x+1)^2}
         \end{aligned}

     Þá er

     .. math::
        h'(x)= \frac{1}{(x+1)^2}.

    **3.** :math:`g(x) = \cos(\ln(x))`

     Hér notum við reiknireglu 5, :math:`(f\circ g)'=(f'\circ g)\cdot g'`.
     Notum okkur líka þekktu afleiðurnar :math:`f(x)=\cos(x)` þá er :math:`f'(x)=-\sin(x)` og ef :math:`f(x) = \ln(x)` þá er :math:`f'(x) = \frac{1}{x}`. Fáum

     .. math::
        g'(x) = -\sin(\ln(x)) \cdot \frac{1}{x} = \frac{-\sin(\ln(x))}{x}.

    **4.** :math:`k(x) = 3^x \cdot \sin(x^5)`

     Hér þurfum við að nota tvær reiknireglur 5, :math:`(f\circ g)'=(f'\circ g)\cdot g'` og 4, :math:`(f\cdot g)'=f'g+fg'`. Notum okkur líka þekktu afleiðurnar :math:`f(x)=\sin(x)` þá er :math:`f'(x)=\cos(x)` og :math:`f(x)=a^x` þá er :math:`f'(x)=\ln(a)a^x`. Fáum

     .. math::
        g'(x) = ln(3) \cdot 3^x \cdot \sin(x^5) + 3^x \cdot cos(x^5) \cdot 5x^4.
