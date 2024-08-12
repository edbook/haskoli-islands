Fylkjaaðgerðir
==============

Nokkrar gerðir fylkja
----------------------

.. admonition:: Skilgreining
  :class: skilgreining

  **Hornalínufylki** (e. diagonal matrix) er :math:`n \times n` fylki þar sem öll stök utan hornalínu eru 
  núll,

  .. math:: \begin{bmatrix}
        a_{11} & 0 & \cdots & 0 \\
        0 & a_{22} & \cdots & 0 \\
        \vdots & \vdots & \ddots & \vdots \\
        0 & 0 & \cdots & a_{nn}
        \end{bmatrix}.
  
  m.ö.o. :math:`D = [d_{ij}]` er hornalínyflki ef :math:`d_{ij}=0` fyrir öll :math:`i` og :math:`j` þannig að :math:`i \neq j`.


  **Einingarfylki** (e. identity matrix) :math:`I`, er hornalínufylki þar sem 
  öll stökin á hornalínu eru 1,

  .. math:: I=\begin{bmatrix}
        1 & 0 & 0 \\
        0 & 1 & 0 \\
        0 & 0 & 1
        \end{bmatrix}.

  stundum er einingarfylki merkt stærð sinni með vísi, t.d. hér :math:`I_3`.

  **Núllfylki** (e. zero matrix) er fylki þar sem öll stökin eru núll,

  .. math:: 0=\begin{bmatrix}
        0 & 0 & 0 \\
        0 & 0 & 0 \\
        0 & 0 & 0
        \end{bmatrix}.
    
  **Frumfylki** (e. elementary matrix) er fylki sem er fengið með því að beita einni einfaldri línuaðgerð á einingarfylkið,
  
  .. math:: \begin{bmatrix}
        1 & 0 & 0 \\
        0 & 0 & 1 \\
        0 & 1 & 0
        \end{bmatrix}.
    
  **Þríhyrningsfylki** (e. triangular matrix) eru fylki þar sem öll stökin eru núll öðru hvoru megin við hornalínuna. *Efra þríhyrningsfylki* en fylki þar sem öll stökin fyrir neðan hornalínu eru 0, 

  
  .. math:: \begin{bmatrix}
    a_{11} & a_{12} & a_{13} & \dots & a_{1n} \\
    0 & a_{22} & a_{23} & \dots & a_{2n} \\
    0 & 0 & a_{33} & \dots & a_{3n} \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & 0 & \dots & a_{nn} \\
    \end{bmatrix},
  
  og *neðra þríhyrningsfylki* er fylki þar sem öll stök fyrir ofan hornalínuna eru 0,

  .. math:: \begin{bmatrix}
    a_{11} & 0 & 0 & \dots & 0 \\
    a_{21} & a_{22} & 0 & \dots & 0 \\
    a_{31} & a_{32} & a_{33} & \dots & 0 \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & a_{n2} & a_{n3} & \dots & a_{nn} \\
    \end{bmatrix}.
    
  

Samlagning og skölun 
--------------------

Setning: Samlagning fylkja
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
  :class: setning
  
  Tvö jafnstór fylki eru lögð saman með því að að leggja saman stuðlana í báðum fylkjunum.
  Ekki er hægt að leggja saman misstór fylki.



Setning: Reglur um fylkjasamlagningu og margföldun með tölu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

.. admonition:: Rökstuðningur 
  :class: setning, dropdown
  
  Auðveldast er að sanna með skoða með því að skoða hvern stuðul fyrir sig. 
  Tökum t.d. lið 1. Ef við skoðum stuðul í sæti :math:`(i,j)` fyrir fylkið :math:`A+B` fáum við :math:`a_{ij}+b_{ij}`. 
  En við vitum að það er sama og :math:`b_{ij}+a_{ij}` þar sem samlagning er víxlin fyrir rauntölur. 
  En :math:`b_{ij}+a_{ij}` er einmitt stuðull :math:`B+A` í sæti :math:`(j,i)`. 
  Þar sem stuðlar :math:`A+B` og :math:`B+A` eru alls staðar þeir sömu fylkin þau sömu einnig.


Sýnidæmi: Samlagning fylkja
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


Sýnidæmi: Margföldun með tölu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi
    
  Reiknið :math:`3A` ef 
  
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
        \end{bmatrix}.

Fylkjamargföldun 
----------------

Lítum á tvær línulegar varpanir :math:`T\colon\mathbb{R}^n\to\mathbb{R}^p` og :math:`\mathbb{R}^p\to\mathbb{R}^m`. 
Fyrst :math:`T` og :math:`S` eru línulegar má tákna þau með fylkjum þannig að 
:math:`T(\textbf{x}) = B\textbf{x}` og :math:`S(\textbf{v}) = A\textbf{v}`. Út frá :math:`T` og :math:`S`
höfum við einnig nýja samsetta línulega vörpun :math:`S\circ T\colon\mathbb{R}^n\to\mathbb{R}^m` sem hefur þann eiginleika að
:math:`S\circ T=S(T(\textbf{x}))=S(B\textbf{x})=AB\textbf{x}`. Fylki þessarar nýju vörpunar er því :math:`AB`.

Skilgreining: Fylkjamargföldun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum  :math:`A` vera :math:`m\times p` fylki og :math:`B=[\textbf{b}_1 \ldots \textbf{b}_n]` vera :math:`p \times n` fylki. 
    Fylkjamargföldun þeirra er skilgreind :math:`AB=[A\textbf{b}_1 \ldots A\textbf{b}_n]`.

.. admonition:: Aðvörun
    :class: advorun

    Margfeldið :math:`AB` er aðeins skilgreint ef fjöldi dálka í fylkinu
    :math:`A` er jafn fjölda lína í fylkinu :math:`B`. Ef :math:`A` er :math:`m \times n` fylki og :math:`B` er :math:`n \times k`
    fylki þá er margfeldið skilgreint og stærð þess er :math:`m \times k`.

Sýnidæmi: Fylkjamargföldun
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Ef :math:`A` er :math:`n\times n` ferningsfylki þá skilgreinum við :math:`A^0=I_n` 
    og svo :math:`A^n=A\cdot A^{n-1}` fyrir :math:`n>1`. Semsagt :math:`A^2=A\cdot A`,
    :math:`A^3=A\cdot A\cdot A` og svo framvegis.

Reikniaðferð fyrir fylkjamargföldun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
    
Sýnidæmi: Fylkjamargföldun
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi
    
  Látum 
  
  .. math:: A=\begin{bmatrix}
    2 & 3 \\
    1 & 4 \\
    \end{bmatrix} \text, \quad B=\begin{bmatrix}
    5 & 6 \\
    7 & 8 \\
    \end{bmatrix} \text, \quad C=\begin{bmatrix}
    1 & 2 & 3 \\
    4 & 5 & 6 \\
    7 & 8 & 9  
    \end{bmatrix} \text{ og } D=\begin{bmatrix}
    12 & 11 \\
    10 & 9 \\
    8 & 7 
    \end{bmatrix}
    
  Reiknið :math:`AB` og :math:`CD`
        
.. admonition:: Lausn
  :class: daemi, dropdown
    
    .. math:: AB=\begin{bmatrix}
        2 \cdot 5 + 3\cdot 7 & 2 \cdot 6 + 3\cdot 8 \\
        1 \cdot 5 + 4\cdot 7 & 1 \cdot 6 + 4\cdot 8 \\
        \end{bmatrix}=\begin{bmatrix}
        31 & 36 \\
        33 & 38 \\
        \end{bmatrix}
        
    .. math:: CD=\begin{bmatrix}
        1 \cdot 12 + 2\cdot 10 +3\cdot 8 & 1\cdot 11 & 2 \cdot 9 + 3\cdot 7 \\
        4 \cdot 12 + 5\cdot 10 +6\cdot 8 & 4\cdot 11 & 5 \cdot 9 + 6\cdot 7 \\
        7 \cdot 12 + 8\cdot 10 +9\cdot 8 & 7\cdot 11 & 8 \cdot 9 + 9\cdot 7 \\
        \end{bmatrix}=\begin{bmatrix}
        56 & 50  \\
        146 & 131 \\
        236 & 212
        \end{bmatrix}
        


Setning: Eiginleikar fylkjamargföldunar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


Bylt fylki 
-----------

Skilgreining: Bylt fylki
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Ef :math:`A` er :math:`m\times n` fylki þá skilgreinum við *bylta fylkið* :math:`A^T`  (e. transpose) sem :math:`n\times m` fylkið 
    sem fæst með því að mynda dálvigra úr línuvigrum :math:`A` og öfugt. 
    Höfum því :math:`A^T_{ij}=A_{ji}`.

Sýnidæmi: Bylt fylki
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi
    
  Byltið eftirfarandi fylkjum
  
  .. math:: A=\begin{bmatrix}
    2 & -1 \\
    0 & 3 \\
    \end{bmatrix} \text, \quad B=\begin{bmatrix}
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
    \end{bmatrix}\text, \quad B^T=\begin{bmatrix}
    1 & 4 \\
    2 & 5 \\
    3 & 6 \\
    \end{bmatrix}\text{ og } C^T=\begin{bmatrix}
    1 & 5 & 9 & 13 \\
    2 & 6 & 10 & 14 \\
    3 & 7 & 11 & 15 \\
    4 & 8 & 12 & 16 \\
    \end{bmatrix}

Setning: Reiknireglur fyrir bylt fylki
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 
    :class: setning

    Látum :math:`A` og :math:`B` vera fylki þannig að hlutaðeigandi margfeldi og summur séu skilgreind. Þá gildir

        **1.** :math:`(A^T)^T = A`

        **2.** :math:`(A+B)^T = A^T+B^T`

        **3.** :math:`(rA)^T = rA^T`, þar sem :math:`r` er fasti.

        **4.** :math:`(AB)^T = B^TA^T`

.. admonition:: Aðvörun 
  :class: advorun

  Fylkjamargföldun er almennt ekki víxlin, þ.e. :math:`AB \neq BA`. Röðin á byltingu margföldunar skiptir máli!


Sýnidæmi: Hegðun byltra fylkja
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

                    
Andhverfur fylkja
-----------------

Látum :math:`T\colon \mathbb{R}^n\to\mathbb{R}^n` vera gagntæka línulega vörpun með samsvarandi fylki :math:`A`. Fyrst :math:`T` er gagntæk á hún sér andhverfu :math:`T^{-1}`.
Hægt er að sýna að þessi andhverfa er líka línuleg og því má tákna hana með venjulegu fylki hennar sem við skulum kalla :math:`C`.
Við vitum að

.. math:: (CA)\textbf{x}=T(T^{-1}(\textbf{x}))=\textbf{x}

fyrir öll :math:`x`, svo að :math:`(CA)` hlýtur að vera einingarfylkið. Það sama gildir um :math:`AC`. 

Skilgreining: Andhverfur fylkja
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreinig
    :class: skilgreining

    :math:`n\times n` fylki :math:`A` er **andhverfanlegt** (e. invertible) ef til er fylki :math:`C` þannig að

    .. math:: AC = CA = I.

    Fylkið :math:`C` kallast þá **andhverfa** :math:`A` (e. inverse), og er táknað með :math:`A^{-1}`. 
    Ef :math:`A` er ekki andhverfanlegt á segjum við það sé **óandhverfanlegt** (e. singular).


.. admonition:: Athugasemd
    :class: athugasemd

    Einungis ferningsfylki, :math:`n \times n`, geta verið andhverfanleg. Þó eru ekki öll ferningsfylki andhverfanleg.



Setning: Andhverfa er ótvírætt ákvörðuð
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Sérhvert fylki hefur aðeins eina andhverfu. Hugsum okkur að :math:`B` og :math:`C` séu tvær mismunandi andhverfur :math:`A`. Við fáum að 

    .. math:: B = IB = (CA)B = CAB = C(AB) = CI = C.

    Táknum andhverfu :math:`A` með :math:`A^{-1}`, þ.e.

    .. math:: A\cdot A^{-1} = A^{-1}\cdot A = I.
    
    Við sjáum að andhverfa fylkis er ótvírætt ákvörðuð.


Sýnidæmi: Eru fylkin andhverfanleg?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi
    
  Eru eftirfarandi fylki andhverfanleg?
  
  .. math::  A =\begin{bmatrix}
    0 & 0 \\
    0 & 0 \\
    \end{bmatrix}, \quad B= \begin{bmatrix}
    1 & 0 \\
    0 & 0 \\
    \end{bmatrix}, \quad C= \begin{bmatrix}
    1 & 0 \\
    0 & 2 \\
    \end{bmatrix}.

.. admonition:: Lausn
  :class: daemi, dropdown
    
  Til að leita að andhverfum skulum við margfalda þessi fylki með almennu :math:`2\times 2` fylki og athuga
  hvort mögulegt sé að finna andhverfu þeirra. Fáum
  
  .. math:: \begin{bmatrix}
    0 & 0 \\
    0 & 0 \\
    \end{bmatrix} \begin{bmatrix}
    a & b \\
    c & d \\
    \end{bmatrix} = \begin{bmatrix}
    0 & 0 \\
    0 & 0 \\
    \end{bmatrix} \neq I,

  svo að núllfylkið :math:`A` á sér ekki andhverfu. Því næst,
  
  .. math:: \begin{bmatrix}
    1 & 0 \\
    0 & 0 \\
    \end{bmatrix} \begin{bmatrix}
    a & b \\
    c & d \\
    \end{bmatrix} = \begin{bmatrix}
    a & b \\
    0 & 0 \\
    \end{bmatrix} \neq I, 

  svo fylkið :math:`B` getur heldur ekki verið andhverfanlegt. Loks höfum við að
  
  .. math:: \begin{bmatrix}
    1 & 0 \\
    0 & 2 \\
    \end{bmatrix} \begin{bmatrix}
    a & b \\
    c & d \\
    \end{bmatrix} = \begin{bmatrix}
    a & b \\
    2c & 2d \\
    \end{bmatrix},

  svo ef við veljum :math:`a=1, b=c=0` og :math:`d=\frac{1}{2}` fáum við einingarfylkið út úr margfölduninni. 
  Því er fylki :math:`C` andhverfanlegt og er andhverfa þess
  
  .. math:: \begin{bmatrix}
    1 & 0 \\
    0 & \frac{1}{2} \\
    \end{bmatrix}.


Setning: Andhverfa :math:`2\times 2` fylkja
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 
    :class: setning

    Látum :math:`A=\begin{bmatrix} a & b \\ c & d \end{bmatrix}` vera :math:`2\times 2` fylki. Fylkið :math:`A` er 
    andhverfanlegt ef og aðeins ef :math:`ad-bc\neq 0` og í þeim tilfellum er andhverfan gefin með 

    .. math:: A^{-1} = \frac{1}{ad-bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}.

    Stærðin :math:`ad-bc` kallast *ákveða* (e. determinant) fylkisins :math:`A` og er táknuð :math:`\text{det}(A)`. Meir um ákveður í kafla 3.


Sýnidæmi: Andhverfa :math:`2\times 2` fylkja
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi
    
  Finnið andhverfu eftirfarandi fylkja ef til eru
  
  .. math:: A=\begin{bmatrix}
    -3 & 7 \\
    2 & 5 \\
    \end{bmatrix}, \quad B=\begin{bmatrix}
    -2 & 3 \\
    4 & -6 \\
    \end{bmatrix}. 

.. admonition:: Lausn
  :class: daemi, dropdown
    
  Formúlan gefur okkur að :math:`\det(A)=-3\cdot5-2\cdot7=-15-14=-29` svo að :math:`A` á sér andhverfu og hún er
  
  .. math:: -\frac{1}{29}\begin{bmatrix} 5 & -7 \\ -2 & -3 \end{bmatrix}.

  Fáum að :math:`\det(B)=-2\cdot (-6)-4\cdot3=0` svo fylkið :math:`B` er á sér ekki andhverfu.

Setning: Lausnir fylkjajafna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 
    :class: setning

    Látum :math:`A` vera andhverfanlegt :math:`n\times n` fylki. Þá hefur fylkjajafnan :math:`A\textbf{x}=\textbf{b}` 
    nákvæmlega eina lausn fyrir sérhvert :math:`\textbf{b}\in\mathbb{R}^n` og sú lausn er 

    .. math:: \textbf{x}=A^{-1}\textbf{b}.

Sýnidæmi: Fylkjajafna leyst með andhverfu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
    \end{bmatrix}.

.. admonition:: Lausn
  :class: daemi, dropdown
    
  Andhverfa fylkisins var reiknuð í sýnidæmi :math:`2.5.3.1` hér að ofan. Fáum
  
  .. math:: \textbf{x}=-\frac{1}{29}\begin{bmatrix} 
    5 & -7 \\ 
    -2 & -3 
    \end{bmatrix}\begin{bmatrix}
    10 \\
    20 
    \end{bmatrix} = -\frac{1}{29}\begin{bmatrix} 
    50-140 \\
    -20-60 
    \end{bmatrix} = \frac{1}{29}\begin{bmatrix} 90 \\ 80 \end{bmatrix}.


.. admonition:: Athugasemd 
    :class: athugasemd

    Setningin á undan er oftast ekki notuð beint þegar reikna á stórar fylkjajöfnur af 
    gerð :math:`A\textbf{x}=\textbf{b}`. Það er tímafrekt og að reikna andhverfur stórra fylkja og oftast fljótlega að leysa 
    jöfnuna beint með Gauss-eyðingu eða öðrum aðferðum.


Setning: Reiknireglur andhverfa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 
    :class: setning

    Látum :math:`A` og :math:`B` vera andhverfanleg :math:`n\times n` fylki. Þá gildir að

    **1.** :math:`A^{-1}` er andhverfanlegt fylki og 

    .. math:: (A^{-1})^{-1}=A.

    **2.** :math:`AB` er andhverfanlegt fylki og 

    .. math:: (AB)^{-1}=B^{-1}A^{-1}.

    **3.** :math:`A^T` er andhverfanlegt fylki og 

    .. math:: (A^T)^{-1}=(A^{-1})^T.

Reiknirit andhverfa :math:`n \times n` fylkja
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Aðferð
    :class: skilgreining

    Látum :math:`A` vera :math:`n \times n` fylki og :math:`I_n` vera :math:`n \times n` einingarfylki. Setjum upp aukna fylkið

    .. math:: [A \ | \ I]

    og beitum Gauss-Jordan eyðingu til að breyta fylkinu :math:`A` yfir í einingarfylkið :math:`I_n`. Ef núlllína kemur upp á einhverjum tímapunkti í vinstri hliðinna þá 
    er fylkið :math:`A` ekki andhverfanleg. Ef tekst að breyta :math:`A` í einingarfylkið þá situr andhverfan eftir í hægri hliðinni,

    .. math:: [A  \ | \  I] \sim [I  \ | \  A^{-1}].

Sýnidæmi: Andhverfa :math:`3\times3` fylkis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi
    
  Reiknið andhverfu fylkisins
  
  .. math:: A=\begin{bmatrix}
    1 & 2 & 3\\
    0 & 1 & 4 \\
    5 & 6 & 0 
    \end{bmatrix}. 

.. admonition:: Lausn
  :class: daemi, dropdown
    
  Búum til aukna fylkið og beitum einföldum línuaðgerðum:

  .. math:: \begin{align} [A  \ | \  I_3] =
    \left[\begin{array}{@{}ccc|ccc@{}}
    1 & 2 & 3 & 1 & 0 & 0 \\
    0 & 1 & 4 & 0 & 1 & 0 \\
    5 & 6 & 0 & 0 & 0 & 1 \\
    \end{array}\right]
    &\overset{\substack{R_3-5R_1}}{\sim}
    \left[\begin{array}{@{}ccc|ccc@{}}
    1 & 2 & 3 & 1 & 0 & 0 \\
    0 & 1 & 4 & 0 & 1 & 0 \\
    0 &-4 &-15&-5 & 0 & 1 \\
    \end{array}\right] \\ 
    &\overset{\substack{R_3+4R_2}} \sim
    \left[\begin{array}{@{}ccc|ccc@{}}
    1 & 2 & 3 & 1 & 0 & 0 \\
    0 & 1 & 4 & 0 & 1 & 0 \\
    0 & 0 & 1 &-5 & 4 & 1 \\
    \end{array}\right]  \\ 
    &\overset{\substack{R_1-2R_2}} \sim
    \left[\begin{array}{@{}ccc|ccc@{}}
    1 & 0 &-5 & 1 &-2 & 0 \\
    0 & 1 & 4 & 0 & 1 & 0 \\
    0 & 0 & 1 &-5 & 4 & 1 \\
    \end{array}\right] \\ 
    &\overset{\substack{R_1+5R_3\\R_2-4R_3}}  \sim
    \left[\begin{array}{@{}ccc|ccc@{}}
    1 & 0 & 0 & -24 &18 & 5 \\ 
    0 & 1 & 0 & 20 & -15 & -4 \\
    0 & 0 & 1 &-5 & 4 & 1 \\
    \end{array}\right]
    \end{align}

  svo
  
  .. math:: A^{-1} = \begin{bmatrix}
    -24 &18 & 5 \\
    20 & -15 & -4 \\
    -5 & 4 & 1
    \end{bmatrix}.


Andhverfanlegar varpanir
---------------------------------

Skilgreining: Andhverfanlegar varpanir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreinig 
    :class: skilgreining

    Vörpun :math:`f: X \rightarrow Y` er andhverfanleg ef til er vörpun :math:`f^{-1}: Y \rightarrow X` þannig að

    .. math:: f(f^{-1}(y))=y \quad \text{og}\quad f^{-1}(f(x))=x

    fyrir öll :math:`y \in Y` og :math:`x \in X`. Þá kallast :math:`f^{-1}` andhverfa vörpunarinnar :math:`f`.

.. admonition:: Fylgisetning 
    :class: setning

    Vörpun :math:`f: X \rightarrow Y` er andhverfanleg ef og aðeins ef hún er gagntæk.


Setning: Andhverfanlegar línulegar varpanir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 
    :class: setning

    Látum :math:`T:\mathbb{R}^n \rightarrow \mathbb{R}^n` vera línulega vörpun með :math:`n \times n` fylki :math:`A`. 
    Ef fylkið :math:`A` er andhverfanlegt þá er vörpunin

    .. math:: \R^n \rightarrow \R^n, \ \ve x\mapsto A^{-1} \ve x

    andhverfa vörpunarinnar :math:`T`. Andhverfan er einnig línuleg vörpun. Vörpunin :math:`T` er andhverfanleg ef og aðeins ef :math:`A` er andhverfanlegt fylki.

Setning: Eintækni og átækni línulegra varpana
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 
    :class: setning

    Látum :math:`T \colon \R^n \rightarrow \R^n` vera línulega vörpun. Vörpunin :math:`T` er eintæk þá og því aðeins að hún er átæk.

.. admonition:: Rökstuðningur 
    :class: setning, dropdown
    
    Skrifum :math:`T(\textbf{x})=A\textbf{x}`. 
    Gerum ráð fyrir að :math:`T` sé eintæk. Fáum að :math:`A\textbf{x}=\textbf{0}` hefur aðeins augljósu lausnina.

    Skoðum efri stallagerð :math:`A`. Fyrst jafnan hefur aðeins augljósu lausnina þá hefur 
    efri stallagerðin forystustuðul í hverjum dálki (og engar frjálsar breytur), þ.e. :math:`n` forystustuðla.

    Þar með hefur stallagerðin líka forystustuðul í hverri línu (því fylkið er :math:`n\times n` fylki).

    Jafnan :math:`A \textbf{x} = \textbf{b}` hefur lausn fyrir alla vigra :math:`\textbf{b}\in\mathbb{R}^n` og
    því er vörpunin :math:`T(\textbf{x})=A\textbf{x}` átæk.

    Athugið að leiðingarnar hér gilda í báðar áttir.

.. admonition:: Aðvörun 
    :class: advorun

    Þessi setning gildir aðeins um **línulegar varpanir** :math:`\R^n \rightarrow \R^n`. Hún gildir ekki um varpanir sem eru ólínulegar né varpanir þar sem :math:`\R^n \rightarrow \R^m`, :math:`n \neq m`.

Eftirfarandi setning inniheldur jafngild skilyrði þess að ferningsfylki sé andhverfanlegt.

Setning: Langa setningin um andhverfanleg fylki
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 
    :class: setning

    Látum :math:`A` vera :math:`n\times n` fylki. 
    Þá eru eftirfarandi fullyrðingar annað hvort allar sannar eða allar ósannar.

    **1.** :math:`A` er andhverfanlegt.

    **2.** :math:`A` er línu-jafngilt (og þar með jafngilt) :math:`n\times n` einingarfylkinu :math:`I_n`.

    **3.** :math:`A` hefur :math:`n` forystustuðla (þ.e. efra stallaform :math:`A`).

    **4.** Jafnan :math:`A\textbf{x}=\textbf{0}` hefur aðeins augljósu lausnina :math:`\ve x = \ve 0`.

    **5.** Dálkvigrar :math:`A` eru línulega óháðir.

    **6.** Línulega vörpunin :math:`\textbf{x}\mapsto A\textbf{x}` er eintæk.

    **7.** Jafnan :math:`A\textbf{x}=\textbf{b}` hefur a.m.k eina lausn fyrir sérhvert :math:`\textbf{b} \in \mathbb{R}^n`.

    **8.** Dálkvigrar :math:`A` spanna allt :math:`\mathbb{R}^n`.

    **9.** Línulega vörpunin :math:`\textbf{x}\mapsto A\textbf{x}` er átæk.

    **10.** Til er :math:`n\times n` fylki :math:`C` þannig að :math:`CA=I_n`.

    **11.** Til er :math:`n\times n` fylki :math:`D` þannig að :math:`AD=I_n`.

    **12.** Bylta fylkið :math:`A^T` er andhverfanlegt.


Sýnidæmi: Er fylkið andhverfanlegt?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Er gefið fylkið :math:`A` andhverfanlegt? 
    
    .. math:: A=\begin{bmatrix} 
        2 & 3 & 5 \\
        0 & -1 & 4 \\
        0 & 1 & 2 \\
        \end{bmatrix}.

.. admonition:: Lausn
    :class: daemi, dropdown

    Sjáum að 

    .. math:: A=\begin{bmatrix} 
        2 & 3 & 5 \\
        0 & -1 & 4 \\
        0 & 1 & 2 \\
        \end{bmatrix}&\overset{\substack{ R_3+R_2}} \sim 
        \begin{bmatrix} 
        2 & 3 & 5 \\
        0 & -1 & 4 \\
        0 & 0 & 5 \\
        \end{bmatrix}
    
    svo fylkið hefur þrjá forystustuðla. Þar með er fylkið andhverfanlegt.

.. admonition:: Athugasemd
    :class: athugasemd

    **1.** Látum :math:`A` og :math:`B` vera :math:`n \times n` fylki þannig að :math:`AB=I` þá eru :math:`A` og :math:`B` andhverfanleg.
    
    **2.** Ef :math:`A` og :math:`B` eru andhverfanleg þá eru :math:`AB` og :math:`BA` það einnig.

    **3.** Ef :math:`A` og :math:`B` eru óandhverfanleg þá eru :math:`AB` og :math:`BA` það einnig.

LU-þáttun
----------

LU-þáttun er gagnleg þegar leysa á stór línuleg jöfnuhneppi, t.a.m. fyrir marga ólíka vigra :math:`\ve b`,

.. math:: A\textbf{x} = \textbf{b}_1, A\textbf{x} = \textbf{b}_2, \dots, A\textbf{x} = \textbf{b}_k.

Þessi aðferð t.a.m. sparar útreikninga í tölvu. Meir um LU-þáttun í áfanganum Töluleg Greining.

Skilgreining: LU-þáttun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`A` vera :math:`m \times n` fylki sem hægt er að koma á efra stallaform með því að nota einungis umskiptingar þar sem margfeldi af einni línu er lagt við línu neðar í fylkinu. Þá má þátta :math:`A` í margfeldi tveggja fylkja

    .. math:: A=LU

    þar sem :math:`L` er :math:`m\times m` neðra þríhyrningsfylki með :math:`1` á hornalínunni og
    U er :math:`m\times n` fylki af efri stallagerð. Þessi þáttun nefnist **LU-þáttun** (e. LU-factorization).

    Við sjáum þetta fyrir okkur svona
    
    .. math:: A= \begin{bmatrix}
        1 & 0 & 0 \\
        * & 1 & 0 \\
        * & * & 1
        \end{bmatrix}
        \begin{bmatrix}
        \blacksquare & * & * & * \\
        0 & \blacksquare & * & * \\
        0 & 0 & 0 & \blacksquare
        \end{bmatrix} = LU.


Reiknirit LU-þáttunar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Reiknirit
    :class: setning

    Aðferð til þess að finna LU-þáttun fylks :math:`A` og nota til þess að leysa fylkjajöfnu :math:`A \ve x = \ve b`.

      **1.** Finna :math:`U`: koma :math:`A` yfir á efri stallagerð með umskiptingum á borð við :math:`R_j\rightarrow R_j+cR_i` þar sem :math:`i<j`.

      **2.** Finna :math:`L`: búa til neðra þríhyrningsfylki með 1 á hornalínunni og fylla í það með föstunum :math:`c` sem notaðir voru í línuaðgerðunum í skrefinu á undan.

    Til að skoða hvort rétt sé reiknað er auðvelt að margfalda fylkin saman og athuga hvort :math:`A = LU`. Ef leysa á fylkjajöfnu höldum við áfram

      **3.** Skrifum :math:`A \ve x = \ve b` sem :math:`L (U \ve x) = \ve b` og látum :math:`\ve y = U \ve x`. Síðan leysum við :math:`L \ve y = \ve b` og köllum lausnina :math:`\ve z`.

      **4.** Leysum :math:`U \ve x = \ve z` með aftur-á-bak innsetningu.
    
.. admonition:: Athugasemd
    :class: athugasemd

    Ekki má nota hinar tvær línuaðgerðirnar í Skrefi 1, þ.e.
    margfalda línur með fasta (:math:`R_i \rightarrow c R_i`) eða víxla á línum (:math:`R_i\leftrightarrow R_j`). Oft verður ekki hjá því komist að víxla á línum. Í þeim tilfellum virkar reikniaðferðin ekki. 
    Til eru leiðir til að vinna sig fram hjá þessu en það verður ekki farið í þær nú.





Sýnidæmi: LU-þáttun
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi
    
  LU-þáttið eftirfarandi fylki
  
  .. math:: A=\begin{bmatrix}
    2 & 1 & 3\\
    4 & 2 & 8 
    \end{bmatrix}, \quad B=\begin{bmatrix}
    3 & 1 & -2\\
    -6 & 0 & 7 \\
    9 & 5 & 1 
    \end{bmatrix}.

.. admonition:: Lausn
  :class: daemi, dropdown
  
  Komum :math:`A` yfir á efri stallagerð með Gauss eyðingu
  
  .. math:: \begin{bmatrix}
        2 & 1 & 3\\
    	  4 & 2 & 8 
        \end{bmatrix} \overset{R_2-2R_1}{\longrightarrow} 
        \begin{bmatrix} 
        2 & 1 & 3 \\
        0 & 0 & 2
        \end{bmatrix}.
    
  Búum til fylki :math:`L` fylki með því að skoða hvaða línuaðgerðum var beitt (ath. við snúum þeim við í :math:`L` fylkinu),
  
  .. math:: L=\begin{bmatrix} 
        1 & 0 \\
        2 & 1 \\
        \end{bmatrix}.

  LU-þáttun á :math:`A` er gefin með
  
  .. math:: A=LU=\begin{bmatrix}
        1 & 0 \\
        2 & 1 
        \end{bmatrix}
        \begin{bmatrix}
        2 & 1 & 3 \\
        0 & 0 & 2
        \end{bmatrix}.
    
  Framkvæmum nú Gauss eyðingu á fylki :math:`B` til að koma því á efri stallagerð
  
  .. math:: \begin{bmatrix}
        3 & 1 & -2 \\
        -6 & 0 & 7 \\
        9 & 5 & 1
        \end{bmatrix} \overset{R_2+2R_1}{\longrightarrow}
        \begin{bmatrix}
        3 & 1 & -2 \\
        0 & 2 & 3 \\
        9 & 5 & 1
        \end{bmatrix} \overset{R_3-3R_1}{\longrightarrow}
        \begin{bmatrix}
        3 & 1 & -2 \\
        0 & 2 & 3 \\
        0 & 2 & 7
        \end{bmatrix}\\
        \overset{R_3-R_2}{\longrightarrow}
        \begin{bmatrix}
        3 & 1 & -2 \\
        0 & 2 & 3 \\
        0 & 0 & 4
        \end{bmatrix}.
    
  Finnum :math:`L` fylkið út frá aðgerðunum sem notaðar voru.

    .. math:: \begin{bmatrix}
        &\\\\
        \end{bmatrix} \overset{R_2+2R_1}{\longrightarrow}
        \begin{bmatrix}
        &\\\\
        \end{bmatrix} \overset{R_3-3R_1}{\longrightarrow}
        \begin{bmatrix}
        &\\\\
        \end{bmatrix} 
        \overset{R_3-R_2}{\longrightarrow}
        \begin{bmatrix}
        &\\\\
        \end{bmatrix},
    
  sjáum að

    .. math:: L=\begin{bmatrix}
        1 & 0 & 0 \\
        -2 & 1 & 0 \\
        3 & 1 & 1 \\
        \end{bmatrix}.
    
  LU-þáttun á :math:`B` er gefin með

    .. math:: B=LU=\begin{bmatrix}
        1 & 0 & 0 \\
        -2 & 1 & 0 \\
        3 & 1 & 1 \\
        \end{bmatrix}
        \begin{bmatrix}
        3 & 1 & -2 \\
        0 & 2 & 3 \\
        0 & 0 & 4 \\
        \end{bmatrix}.
        



Sýnidæmi: LU-þáttun til þess að leysa fylkjajöfnu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Skoðum fylki :math:`A` í sýnidæminu að ofan, 

    .. math:: A=LU=\begin{bmatrix}
        1 & 0 \\
        2 & 1 \\
        \end{bmatrix}
        \begin{bmatrix}
        2 & 1 & 3 \\
        0 & 0 & 2 \\
        \end{bmatrix}.
    
    Nota á LU-þáttun :math:`A` til þess að leysa :math:`A\textbf{x}=\ve b` þegar :math:`\textbf{b}=\begin{bmatrix} 4 \\ 6 \end{bmatrix}`

.. admonition:: Lausn
    :class: daemi, dropdown

    Leysum fyrir :math:`\ve y=(y_1,y_2)` í :math:`L \ve y = \ve b`
  
    .. math:: \begin{bmatrix}
        1 & 0 \\
        2 & 1 \\
        \end{bmatrix} 
        \begin{bmatrix}
        y_1 \\
        y_2 \\
        \end{bmatrix} =
        \begin{bmatrix}
        4 \\
        6 \\
        \end{bmatrix}.
    
    Fáum :math:`y_1 = 4` og :math:`2y_1+ y_2 = 6` sem gefur 

    .. math:: \textbf{y}=\begin{bmatrix}
        4 \\
        -2
        \end{bmatrix},
    
    við skulum kalla þessa lausn :math:`\ve z`. Leysum nú fyrir :math:`\textbf{x}` í jöfnunni :math:`U\textbf{x}=\textbf{z}`. Fáum

    .. math:: \begin{bmatrix} 
        2 & 1 & 3 \\
        0 & 0 & 2
        \end{bmatrix}
        \begin{bmatrix}
        x_1 \\
        x_2 \\
        x_3
        \end{bmatrix}=
        \begin{bmatrix}
        4 \\
        -2 
        \end{bmatrix}
    
    Sem gefur 

    .. math:: 2x_1+x_2+3x_3=4 \\
        2x_3=-2
    
    svo :math:`x_3=-1` og :math:`2x_1+x_2=7`, þar með 
    :math:`x_1=-(\frac{1}{2})x_2+\frac{7}{2}`
    . Fáum því:

    .. math:: \textbf{x}=\begin{bmatrix} 
        \frac{7}{2}-\frac{1}{2}x_2 \\
        x_2 \\
        -1
        \end{bmatrix}
    
    þar sem :math:`x_2` er frjáls breyta.



    