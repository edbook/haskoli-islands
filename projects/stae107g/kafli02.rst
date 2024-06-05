Fylkjaaðgerðir
==============

TODO: bæta við einhverju um núllfylki, eingarfylki og hornalínufylki?????

Samlagning og skölun 
--------------------

Tvö fylki jafnstór eru lögð saman með því að að leggja saman stuðlana í báðum fylkjunum.
Ekki er hægt að leggja saman misstór fylki.

Sýnidæmi: samlagning fylkja
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi
    
    Reiknið :math:`A+B` og :math:`A+C` ef 

    .. math:: A=\begin{bmatrix}
            2 & 4 & 6 \\
            1 & 3 & 5
        \end{bmatrix}\text{, } B=\begin{bmatrix}
            7 & 9 & 11 \\
            6 & 8 & 10
        \end{bmatrix} \text{og } C=\begin{bmatrix}
            13 & 15 \\
            12 & 14
        \end{bmatrix}.
        
.. admonition:: Lausn
  :class: daemi, dropdown
    
    Höfum að

        .. math:: A+B=\begin{bmatrix}
            2+7 & 4+9 & 6+11 \\
            1+6 & 3+8 & 5+10 
            \end{bmatrix}=\begin{bmatrix}
            9 & 13 & 17 \\
            7 & 11 & 15 
            \end{bmatrix}

    en :math:`A+C` er ekki skilgreint því fylkin eru misstór.

Til að margfalda fylki :math:`A` með rauntölu :math:`c` margföldum við öll stök :math:`A` með :math:`c`. 
Til dæmis, ef :math:`A` er það sama og áður þá fæst:

.. math:: 3A=  3\cdot\begin{bmatrix}
        2 & 4 & 6 \\
        1 & 3 & 5 \\
      \end{bmatrix}=
    \begin{bmatrix}
        3\cdot 2 &3\cdot  4 &3\cdot  6 \\
        3\cdot 1 &3\cdot  3 &3\cdot  5 \\
      \end{bmatrix}
     = \begin{bmatrix}
        6&12&18 \\
       3 &9 &15 \\
      \end{bmatrix}


Sýnidæmi: Margföldun með tölu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi
    
    Reiknið :math:`3\cdot A` ef 

    .. math:: A=\begin{bmatrix}
            1 & 2 & 3 \\
            4 & 5 & 6
        \end{bmatrix}
        
.. admonition:: Lausn
  :class: daemi, dropdown
    
    Höfum að

        .. math:: 3A=  3\cdot\begin{bmatrix}
            1 & 2 & 3 \\
            4 & 5 & 6
            \end{bmatrix}=
            \begin{bmatrix}
            3\cdot 1 &3\cdot  2 &3\cdot  3 \\
            3\cdot 4 &3\cdot  5 &3\cdot  6 \\
            \end{bmatrix}
            = \begin{bmatrix}
            3 &6 &9 \\
            12 &15 &18 \\
            \end{bmatrix}

Við getum tekið þetta saman í eina setningu.

Reglur um fylkjasamlagningu og margföldun með fasta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 
    :class: setning

    Látum :math:`A`, :math:`B` og :math:`C` vera :math:`m\times n` fylki og :math:`r` og :math:`s` vera rauntölur. 
    Þá gildir:

        **1.** :math:`A+B=B+A`

        **2.** :math:`(A+B)+C = A+(B+C)`

        **3.** :math:`A+ 0 = A`, þar sem :math:`0` er núllfylkið

        **4.** :math:`r(A+B)=rA+rB`

        **5.** :math:`(r+s)A= rA+sA`

        **6.** :math:`r(sA)=(rs)A`

    **Rökstuðningur:** Auðveldast er að sanna með skoða með því að skoða hvern stuðul fyrir sig. 
    Tökum t.d. lið 1. Ef við skoðum stuðul í sæti :math:`(i,j)` fyrir fylkið :math:`A+B` fáum við :math:`a_{ij}+b_{ij}`. 
    En við vitum að það er sama og :math:`b_{ij}+a_{ij}` þar sem samlagning er víxlin fyrir rauntölur. 
    En :math:`b_{ij}+a_{ij}` er einmitt stuðull :math:`B+A` í sæti :math:`(j,i)`. 
    Þar sem stuðlar :math:`A+B` og :math:`B+A` eru alls staðar þeir sömu fylkin þau sömu einnig.

Fylkjamargföldun 
----------------

Lítum á tvær línulegar varpanir :math:`T\colon\mathbb{R}^n\to\mathbb{R}^p` og :math:`\mathbb{R}^p\to\mathbb{R}^m`. 
Fyrst :math:`T` og :math:`S` eru línulegar má tákna þau með fylkjum þannig að 
:math:`T(\textbf{x}) = B\textbf{x}` og :math:`S(\textbf{v}) = A\textbf{v}`. Út frá :math:`T` og :math:`S`
höfum við einnig nýja samsetta línulega vörpun :math:`S\circ T\colon\mathbb{R}^n\to\mathbb{R}^m` sem hefur þann eiginleika að
:math:`S\circ T=S(T(\textbf{x}))=S(B\textbf{x})=AB\textbf{x}`. Fylki þessarar nýju vörpunar er því :math:`AB`.

Skilgreining: Fylkjamargföldun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Gefið A sem er :math:`m\times p` fylki og B sem :math:`p\times n` fylki. Ef dálkvigrar :math:`B` eru 
    :math:`\textbf{b}_1,\ldots, \textbf{b}_n` þannig að :math:`B=[\textbf{b}_1 \ldots \textbf{b}_n]` þá 
    skilgreinum við :math:`AB=[A\textbf{b}_1 \ldots A\textbf{b}_n]`.


Sýnidæmi: Fylkjamargföldun
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi
    
    Reiknið :math:`AB` ef 

    .. math:: A=\begin{bmatrix}
            1 & 2 & 3 \\
            4 & 5 & 6
        \end{bmatrix} \text{ og } B=\begin{bmatrix}
            -1 & 0 \\
            0 & 1 \\
            1 & -1
        \end{bmatrix}
        
.. admonition:: Lausn
  :class: daemi, dropdown
    
    Höfum að

        .. math:: A\textbf{b}_1=\begin{bmatrix} 
            1 & 2 & 3 \\
            4 & 5 & 6
            \end{bmatrix}\cdot\begin{bmatrix}
            -1 \\
            0 \\
            1
            \end{bmatrix}=\begin{bmatrix}
            2 \\
            2
            \end{bmatrix} \text{ og } A\textbf{b}_2=\begin{bmatrix} 
            1 & 2 & 3 \\
            4 & 5 & 6
            \end{bmatrix}\cdot\begin{bmatrix}
            0 \\
            1 \\
            -1
            \end{bmatrix}=\begin{bmatrix}
            -1 \\
            -1
            \end{bmatrix}
        
    svo að

        .. math:: AB=[A\textbf{b}_1 \ A\textbf{b}_2]=\begin{bmatrix}
            2 & -1 \\
            2 & -1
            \end{bmatrix}

Skilgreining: Veldi af fylkjum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Ef :math:`A` er :math:`n\times n` ferningsfylki þá skilgreinum við :math:`A^0=I_n` 
    og svo :math:`A^n=A\cdot A^{n-1}` fyrir :math:`n>1`. Semsagt :math:`A^2=A\cdot A`,
    :math:`A^3=A\cdot A\cdot A` og svo framvegis.

Reikniaðferð fyrir fylkjamargföldun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Aðferð
    :class: skilgreining

    .. math:: A = \begin{bmatrix}
        a_{11} & \cdots & a_{1p} \\
        \vdots & \ddots & \vdots \\
        a_{m1} & \cdots & a_{mp}
        \end{bmatrix}
        \text{ og }
        B = \begin{bmatrix}
        b_{11} & \cdots & b_{1n} \\
        \vdots & \ddots & \vdots \\
        b_{p1} & \cdots & b_{pn}
        \end{bmatrix}

    Margfeldið er þá

    .. math:: AB = \begin{bmatrix}
        (AB)_{11} & \cdots & (AB)_{1n} \\
        \vdots & \ddots & \vdots \\
        (AB)_{m1} & \cdots & (AB)_{mn}
        \end{bmatrix}

    þar sem :math:`(AB)_{ij}` er summa af margfeldum stakanna í :math:`i`-tu línu :math:`A` og :math:`j`-ta dálki :math:`B`.
    **Munum:** 
    
    .. math:: \begin{bmatrix}
        \\\rightarrow\\\\
        \end{bmatrix}\textbf{[}\quad \downarrow \quad \textbf{]}.
    
Eiginleikar fylkjamargföldunar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 
    :class: setning

    Látum :math:`A` vera :math:`m\times n` fylki og :math:`B` og :math:`C` vera fylki með þannig stærðir að 
    hlutaðeigandi margfeldi séu skilgreind. 
    Þá gildir

        **1.** :math:`A(BC) = (AB)C`

        **2.** :math:`A(B+C) = AB+AC`

        **3.** :math:`(B+C)A = BA+CA`

        **4.** :math:`r(AB) = (rA)B = A(rB)`, þar sem :math:`r` er fasti.

        **5.** :math:`I_m A = A = AI_m`


    **Rökstuðningur:** Flesta liði má sanna með því að nota beint skilgreiningu á margfeldi fylkja. 
    Liður 1. er afleiðing þessa að líta megi á fylkin sem varpanir og samsetning varpana er ávallt tengin.


Bylt fylki 
----------

Skilgreining: Bylt fylki
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Ef :math:`A` er :math:`m\times n` fylki þá látum við *bylta fylkið* :math:`A^T`  (e. transpose) vera :math:`n\times m` fylkið 
    sem fæst með því að láta línur :math:`A` mynda dálka :math:`A^T`, í sömu röð og í upprunarlega fylkinu. 
    Höfum því :math:`A^T_{ij}=A_{ji}`.

Sýnidæmi: Bylt fylki
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi
    
    Byltið eftirfarandi fylkjum

    .. math:: A=\begin{bmatrix}
            2 & -1 \\
            0 & 3 \\
        \end{bmatrix} \text{ , } B=\begin{bmatrix}
            1 & 2 & 3 \\
            4 & 5 & 6 \\
        \end{bmatrix} \text{ og } C=\begin{bmatrix}
            1 & 2 & 3 & 4 \\
            5 & 6 & 7 & 8 \\
            9 & 10 & 11 & 12 \\
            13 & 14 & 15 & 16 \\
        \end{bmatrix}
        
.. admonition:: Lausn
  :class: daemi, dropdown
    
    Höfum að

        .. math:: A^T=\begin{bmatrix}
                2 & 0 \\
                -1 & 3 \\
            \end{bmatrix}\text{ , } B^T=\begin{bmatrix}
                1 & 4 \\
                2 & 5 \\
                3 & 6 \\
            \end{bmatrix}\text{ og } C^T=\begin{bmatrix}
                1 & 5 & 9 & 13 \\
                2 & 6 & 10 & 14 \\
                3 & 7 & 11 & 15 \\
                4 & 8 & 12 & 16 \\
            \end{bmatrix}

Reiknireglur fyrir bylt fylki
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 
    :class: setning

    Látum :math:`A` og :math:`B` vera fylki þannig að hlutaðeigandi margfeldi og summur séu skilgreind. Þá gildir

        **1.** :math:`(A^T)^T = A`

        **2.** :math:`(A+B)^T = A^T+B^T`

        **3.** :math:`(rA)^T = rA^T`, þar sem :math:`r` er fasti.

        **4.** :math:`(AB)^T = B^TA^T`

Sýnidæmi: Hegðun byltra fylkja
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi
    
    Reiknið :math:`\textbf{v}^T\textbf{v}` og :math:`\textbf{v}\textbf{v}^T` ef :math:`\textbf{v}=\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}`.

.. admonition:: Lausn
    :class: daemi, dropdown
    
    Höfum að

    .. math:: \textbf{v}^T\textbf{v} = \begin{bmatrix} 1 & 2 & 3\end{bmatrix} \begin{bmatrix} 1 \\ 2 \\ 3\end{bmatrix} = 1^2+2^2+3^3 = 14

    en hinsvegar er

    .. math:: \textbf{v}\textbf{v}^T = \begin{bmatrix} 1 \\ 2 \\ 3\end{bmatrix} \begin{bmatrix} 1 & 2 & 3\end{bmatrix} = 
        \begin{bmatrix}
            1 & 2 & 3 \\
            2 & 4 & 6 \\
            3 & 6 & 9 \end{bmatrix}

                    
Andhverfa fylkis 
----------------

Látum :math:`T\colon \mathbb{R}^n\to\mathbb{R}^n` vera gagntæka línulega vörpun með samsvarandi fylki :math:`A`. Fyrst :math:`T` er gagntæk á hún sér andhverfu :math:`T^{-1}`.
Hægt er að sýna að þessi andhverfa er líka línuleg og því má tákna hana með venjulegu fylki hennar sem við skulum kalla :math:`C`.
Við vitum að

.. math:: (CA)\textbf{x}=T(T^{-1}(\textbf{x}))=\textbf{x} \text{, fyrir öll } \textbf{x}

svo að :math:`(CA)` hlýtur að vera einingarfylkið. Það sama gildir um :math:`AC`. 

Skilgreining: Andhverfanleiki
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Almennt tölum við um að :math:`n\times n` fylki :math:`A` sé *andhverfanlegt* (e. invertible) ef til er fylki :math:`C` þannig að

    .. math:: AC = CA = I

    Fylkið :math:`C` kallast þá *andhverfa* :math:`A` (e. inverse). 
    Ef :math:`A` er ekki andhverfanlegt á segjum við það sé *óandhverfanlegt* (e. singular).

    Hvert fylki hefur aðeins eina andhverfu. Ef :math:`B` og :math:`C` er bæði andhverfur :math:`A` fæst: 

    .. math:: B = IB = (CA)B = CAB = C(AB) = CI = C 

    Við táknum því andhverfu :math:`A` með :math:`A^{-1}`. Þá er 

    .. math:: A\cdot A^{-1} = A^{-1}\cdot A = I
    
Sýnidæmi: Eru þau andhverfanleg?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi
    
    Eru eftirfarandi fylki andhverfanleg?

    .. math:: .. math:: \begin{bmatrix}
            0 & 0 \\
            0 & 0 \\
        \end{bmatrix} \text{ , } \begin{bmatrix}
            1 & 0 \\
            0 & 0 \\
        \end{bmatrix} \text{ , } \begin{bmatrix}
            1 & 0 \\
            0 & 2 \\
        \end{bmatrix}

.. admonition:: Lausn
    :class: daemi, dropdown
    
    Til að leita að andhverfum skulum við margfalda þessi fylki með almennu :math:`2\times 2` fylki og athuga
    hvað þarf að gilda til að það sé andhverfa.

    Höfum að

    .. math:: \begin{bmatrix}
            0 & 0 \\
            0 & 0 \\
        \end{bmatrix} \begin{bmatrix}
            a & b \\
            c & d \\
        \end{bmatrix} = \begin{bmatrix}
            0 & 0 \\
            0 & 0 \\
        \end{bmatrix} \neq I

    svo að núllfylkið getur ekki verið andhverfanlegt.

    .. math:: \begin{bmatrix}
            1 & 0 \\
            0 & 0 \\
        \end{bmatrix} \begin{bmatrix}
            a & b \\
            c & d \\
        \end{bmatrix} = \begin{bmatrix}
            a & b \\
            0 & 0 \\
        \end{bmatrix} \neq I 

    svo þetta fylki getur heldur ekki verið andhverfanlegt. Loks höfum við að

    .. math:: \begin{bmatrix}
            1 & 0 \\
            0 & 2 \\
        \end{bmatrix} \begin{bmatrix}
            a & b \\
            c & d \\
        \end{bmatrix} = \begin{bmatrix}
            a & b \\
            2c & 2d \\
        \end{bmatrix}

    svo ef við veljum :math:`a=1, b=c=0` og :math:`d=\frac{1}{2}` fáum við einingarfylkið út úr margfölduninni. 
    Því er fylkið

    .. math:: \begin{bmatrix}
            1 & 0 \\
            0 & 2 \\
        \end{bmatrix}
    
    andhverfanlegt og hefur andhverfu

    .. math:: \begin{bmatrix}
            1 & 0 \\
            0 & \frac{1}{2} \\
        \end{bmatrix}


Andhverfa :math:`2\times 2` fylkja
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 
    :class: setning

    Látum :math:`A=\begin{bmatrix} a & b \\ c & d \end{bmatrix}` vera :math:`2\times 2` fylki. Fylkið :math:`A` er 
    andhverfanlegt þá og því aðeins að :math:`ad-bc\neq 0` og í þeim tilfellum er andhverfan gefin með 

    .. math:: A^{-1} = \frac{1}{ad-bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}

    **Athugasemd:** Ef :math:`A=\begin{bmatrix} a & b \\ c & d \end{bmatrix}` kallast stærðin :math:`ad-bc` *ákveða* (e. determinant) fylkisins 
    :math:`A` og er táknuð :math:`\det(A)`. TODO setja hyperlink í þriðja kafla


Sýnidæmi: Andhverfur út frá formúlu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi
    
    Finnið andhverfu eftirfarandi fylkja ef til eru

    .. math:: A=\begin{bmatrix}
            -3 & 7 \\
            2 & 5 \\
        \end{bmatrix} \text{ , } B=\begin{bmatrix}
            -2 & 3 \\
            4 & -6 \\
        \end{bmatrix} 

.. admonition:: Lausn
    :class: daemi, dropdown
    
    Formúlan gefur okkur að :math:`\det(A)=-3\cdot5-2\cdot7=-15-14=-29` svo að :math:`A` á sér andhverfu og hún er

    .. math:: -\frac{1}{29}\begin{bmatrix} 5 & -7 \\ -2 & -3 \end{bmatrix}

    Svo höfum við að :math:`\det(B)=-2\cdot (-6)-4\cdot3=0` svo fylkið :math:`B` er óandhverfanlegt.

Lausnir fylkjajafna
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 
    :class: setning

    Látum :math:`A` vera andhverfanlegt :math:`n\times n` fylki. Þá hefur fylkjajafnan :math:`A\textbf{x}=\textbf{b}` 
    nákvæmlega eina lausn fyrir sérhvert :math:`\textbf{b}\in\mathbb{R}^n` og sú lausn er 

    .. math:: \textbf{x}=A^{-1}\textbf{b}.

Sýnidæmi: Fylkjajafna leyst með andhverfu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
  :class: daemi
    
    Leysið jöfnuna

    .. math:: \begin{bmatrix}
            -3 & 7 \\
            2 & 5 \\
        \end{bmatrix} \begin{bmatrix}
            x_1\\
            x_2
        \end{bmatrix} = \begin{bmatrix} 
            10 \\
            20
        \end{bmatrix}

.. admonition:: Lausn
    :class: daemi, dropdown
    
    Við reiknuðum út andhverfuna í sýnidæmi (TODO SETJA INN HYPERLINK). Fáum því að

    .. math:: \textbf{x}=-\frac{1}{29}\begin{bmatrix} 
        5 & -7 \\ 
        -2 & -3 
        \end{bmatrix}\begin{bmatrix}
        10 \\
        20 
        \end{bmatrix} = -\frac{1}{29}\begin{bmatrix} 
        50-140 \\
        -20-60 
        \end{bmatrix} = \frac{1}{29}\begin{bmatrix} 90 \\ 80 \end{bmatrix}

    **Athugasemd:** Setningin á undan er oftast ekki notuð beint þegar reikna á stórar fylkjajöfnur af 
    gerð :math:`A\textbf{x}=\textbf{b}`. Það er tímafrekt og að reikna andhverfur stórra fylkja og oftast fljótlega að leysa 
    jöfnuna beint með Gauss-eyðingu eða öðrum aðferðum.


Reiknireglur fyrir andhverfu fylkis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 
    :class: setning

    Látum :math:`A` og :math:`B` vera andhverfanleg :math:`n\times n` fylki. Þá gildir að

    **1.** :math:`A^{-1}` er andhverfanlegt fylki og 

    .. math:: (A^{-1})^{-1}=A

    **2.** :math:`AB` er andhverfanlegt fylki og 

    .. math:: (AB)^{-1}=B^{-1}A^{-1}

    **3.** :math:`A^T` er andhverfanlegt fylki og 

    .. math:: (A^T)^{-1}=(A^{-1})^T