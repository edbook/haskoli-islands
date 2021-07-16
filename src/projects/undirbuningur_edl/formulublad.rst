Formúlublað
===========
Vigrar
------
.. math::
  \begin{aligned}
    \bar{a} &= \begin{pmatrix} a_x \\ a_y \\ a_z \end{pmatrix} = a_x \hat{\imath} + a_y \hat{\jmath} + a_z \hat{k} \qquad & \text{Mismunandi táknmál}\\
    |\bar{a}| &= a = \sqrt{a_x^2 + a_y^2 + a_z^2} \qquad & \text{Lengd vigurs}\\
    \bar{a} + \bar{b} &= \begin{pmatrix}a_x+b_x \\ a_y+b_y \\ a_z+b_z \end{pmatrix} \qquad & \text{Samlagning vigra}\\
    c \cdot \bar{v} &= \begin{pmatrix}c \cdot v_x\\ c \cdot v_y \\ c \cdot v_z \end{pmatrix} \qquad & \text{Margföldun með fasta}\\
    \bar{a} \cdot \bar{b} &= a_x b_x + a_y b_y \\
    &= a b \cos{\phi} \qquad & \text{Innfeldi vigra}\\
    \bar{a} \times \bar{b} &= (a_x \hat{\imath} + a_y \hat{\jmath} + a_z \hat{k}) \times (b_x \hat{\imath} + b_y \hat{\jmath} + b_z \hat{k}) \\
    &= (a_y b_z - a_z b_y)\hat{\imath} + (a_z b_x - a_x b_z)\hat{\jmath} + (a_x b_y - a_y b_x)\hat{k} \qquad & \text{Krossfeldi}\\
    |\bar{a} \times \bar{b}| &= ab\sin \phi \qquad & \text{Lengd krossfeldis}\\
    \bar{a} \times \bar{b} &= -\bar{b} \times \bar{a} \qquad & \text{Regla um krossfeldi}
  \end{aligned}

Hraði
-----
.. math::
  \begin{aligned}
    v &= \frac{x_2-x_1}{t_2-t_1} = \frac{\Delta x}{\Delta t} \qquad & \text{Meðalhraði}\\
    v & = \lim_{h \to 0} \frac{x_{t+h}-x_{t}}{(t+h) - t} = \lim_{h\to 0}\frac{x_{t+h}-x_{t}}{h} = \frac{dx}{dt} \qquad & \text{Augnablikshraði} \\
  \end{aligned}

Hröðun
------
.. math::
  \begin{aligned}
    a &= \frac{v_2 - v_1}{t_2 - t_1} \qquad & \text{Meðalhröðun}\\
    a &= \lim_{h \to 0} \frac{v_{t+h}-v_{t}}{(t+h) - t} = \lim_{h\to 0}\frac{v_{t+h}-v_{t}}{h} = \frac{dv}{dt} \qquad &\text{Augnablikshröðun}\\
  \end{aligned}

Hreyfijöfnur
------------
.. math::
  \begin{aligned}
    v&=v_0+a\cdot t \qquad &\text{Hraði sem fall af tíma} \\
    x&=x_0 + v_0 \cdot t + \frac{1}{2} a\cdot t^2 \qquad & \text{Staðsetning sem fall af tíma} \\
    v^2 &=v_0^2+2a\cdot (x-x_0) \qquad & \text{Tímaóháða jafnan} \\
    x-x_0 &=\frac{1}{2}(v_0 + v)\cdot t \qquad & \text{Færsla}
  \end{aligned}

Tvívíð hreyfing
---------------
.. math::
  \begin{aligned}
    y&=\tan(\alpha_0) x - \frac{g}{2v_0\cos^2(\alpha_0)}x^2 \qquad & \text{Ferill kasthreyfingar} \\
    a &= \frac{v^2}{R} = \frac{4 \pi^2 R}{T^2} \qquad & \text{Jöfn hringhreyfing}
  \end{aligned}

Kraftar
-------
.. math::
  \begin{aligned}
    \Sigma \bar{F} = 0 &\Rightarrow v = \text{fasti} \qquad & \text{1. lögmál Newtons}\\
    \Sigma \bar{F} &= m\bar{a} \qquad & \text{2. lögmál Newtons} \\
    \bar{F}_{AB} &= -\bar{F}_{BA}\qquad & \text{3. lögmál Newtons} \\
  \end{aligned}

Orka
-----
.. math::
  \begin{aligned}
    W &=\bar{F}\cdot \bar{s} \qquad & \text{Vinna}\\
    P &= \frac{dW}{dt} \qquad & \text{Afl}\\
    K &=\frac{1}{2}mv^2 \qquad & \text{Hreyfiorka}\\
    U &= mgy \qquad & \text{Stöðuorka í þyngdarsviði}\\
    p &= mv \qquad & \text{Skriðþungi}\\
  \end{aligned}
