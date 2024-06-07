Kafli
==========

Eigingildi og eiginvigur
------------------------


Eigingildi og eiginvigur
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`A` vera :math:`n \times n` fylki. Ef til er vigur 
    :math:`\textbf{x} \neq \textbf{0}` og tala :math:`\lambda` þannig að

    .. math:: A\textbf{x}=\lambda\textbf{x}
    
    Þá segjum við að :math:`\lambda` sé **eigingildi** (e. eigenvalue) :math:`A`
    og **x** **eiginvigur** (e. eiginvector). Ef að **x** og :math:`\lambda` uppfylla
    jöfnuna að ofan þá segjum vip að **x** sé eiginvigur við eigingildi :math:`\lambda`.
    Við þessar aðstæður segjum við að eigingildið :math:`\lambda` og eiginvigurinn :math:`x` 
    tilheyri hvort öðru.


Sýnidæmi: Eigingildi og eiginvigur
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi
    
    Látum :math:`A=\begin{bmatrix} 2&0\\0&1 \end{bmatrix}` og 
    :math:`\textbf{x} = \begin{bmatrix}1\\0\end{bmatrix}` þá er
    
    .. math:: A\textbf{x} = \begin{bmatrix}
        2\\0\end{bmatrix} = 2 \begin{bmatrix}
        1\\0\end{bmatrix} = \textbf{x}
    
    svo 2 er eigingildi :math:`A` og :math:`\textbf{x}` er tilsvarandi eiginvigur.

Eigingildi fylkja fundin
------------------------

Við finnum eigingildi með :math:`A-\lambda I`

.. admonition:: Dæmi
    :class: daemi

    Finnið eigingildi og eiginvigra

    .. math:: A=\begin{bmatrix}2 & 1\\ 9 & 2\end{bmatrix}

.. admonition:: Lausn
    :class: daemi, dropdown

    Byrjum að finna eigingildin, til þess þarf

    .. math:: A-\lambda I = \begin{bmatrix}2-\lambda & 1 \\ 9 & 2-\lambda\end{bmatrix} (*)

    að vera óandhverfanlegt og hafa þannig ákveðuna 0. Þá er

    .. math:: \begin{align*}
        \begin{vmatrix}
        2-\lambda & 1 \\ 9 & 2-\lambda
        \end{vmatrix}
        &= (2-\lambda)^2-9\\&= \lambda^2-4\lambda+4-9\\&=\lambda^2-4\lambda-5\\& =
        (\lambda-5)(\lambda+1)=0  
        \end{align*}

    sem gefur að :math:`\lambda = 5` eða :math:`\lambda =-1`.

    Tökum :math:`\lambda=5` og þá fæst að við erum að reyna að leysa jöfnuhneppið (*) sem er þá

    .. math:: \begin{bmatrix}
        -3 & 1\\
        9&-3
        \end{bmatrix} \sim \begin{bmatrix}
        1 & -1/3\\
        0 & 0
        \end{bmatrix}
    
    svo :math:`\textbf{x} = t\begin{bmatrix}1/3\\1\end{bmatrix}`.

    Nú má auðveldlega sannreyna að :math:`\begin{bmatrix} 1/3\\1\end{bmatrix}`
    er eiginvigur sem svarar til eigingildisins 5. 


Eiginrúm 
--------

Setning
^^^^^^^

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`n\times n` fulki og :math:`\lambda`
    eigingildi þess. Mengi allra eiginvigra tilheyrandi eigingildinu :math:`\lambda`
    að viðbættum núllvigrinum :math:`\textbf{0}` er hlutrúm í :math:`\mathbb{R}^n`. 
    Þetta hlutrúm er kallað **eiginrúm** (e. eigenspace) tilheyrandi eigingildinu :math:`\lambda`
    og táknað með :math:`E(\lambda)`. Eiginrúmið er núllrúm fylkisins :math:`A-\lambda I`.

Sýnidæmi: Eiginrúm fylkis
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Gefið er að 2 er eigingildi fylkisins :math:`A`. Finnið 
    eiginrúm :math:`A` m.t.t. eigingildisins 2.

    .. math:: A\begin{bmatrix} 2 & -2 & -2 \\ 0 & 0 & -2\\ 0 & 0 & -2 \end{bmatrix}
    
.. admonition:: Lausn
    :class: daemi, dropdown

    Við viljum þá leysa :math:`(A-2I)\textbf{x}=0`. Fáum

    .. math:: A-2I=
        \begin{bmatrix}
        0 & -2 & -2\\
        0 & -2 & -2\\
        0 & 0 & 0
        \end{bmatrix}
        \sim \dots \sim \begin{bmatrix}
        0 & 1& 1\\
        0 & 0 & 0\\
        0 & 0 & 0
        \end{bmatrix}
    
    sem gefur :math:`x_2+x_3=0` og :math:`x_1` er frjáls breyta. 
    Fáum að almenn lausn er 

    .. math:: \begin{bmatrix}
        x_1\\
        x_2\\
        x_3
        \end{bmatrix}
        =
        \begin{bmatrix}
        x_1\\
        -x_3\\
        x_3
        \end{bmatrix}=
        x_1\begin{bmatrix}
        1\\
        0\\
        0
        \end{bmatrix}+
        x_3\begin{bmatrix}
        0\\
        -1\\
        1
        \end{bmatrix} 
    
    svo eiginrúmið er

    .. math:: Span \left\{\begin{bmatrix}
        1\\
        0\\
        0
        \end{bmatrix},
        \begin{bmatrix}
        0\\
        -1\\
        1
        \end{bmatrix}\right\}


Setning
^^^^^^^^^

.. admonition:: Setning
    :class: setning

    Ef :math:`A` er :math:`n \times n` þríhyrningsfylki þá eru eigingildi :math:`A`
    stökin á hornalínunni.



:math:``

Skilgreining: Línuleg vörpun
^^^^^^^^^^^^^^^^^^^^^^^^^^^^