Kafli 3
=====================
Ákveða (e. determinant) er fall frá :math:`\mathbb{R}^{n \times n}\rightarrow \mathbb{R}` sem úthlutar :math:`n \times n` fylki :math:`A` tölu :math:`\det(A)`.
Ákveða er einungis skilgreind fyrir ferningsfylki og hana má nota t.d. til þess að segja til um hvort fylki sé andhverfanlegt. Ef ákveða fylkis er :math:`0` er fylkið ekki andhverfanlegt.

Ákveða :math:`2 \times 2` fylkis
---------------------------------

Skilgreining: Ákveða :math:`2 \times 2` fylkis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
    :class: skilgreining

        Ákveða :math:`2 \times 2` fylkis :math:`A=\begin{bmatrix}a & b\\ c & d \end{bmatrix}` er talan

        .. math:: \det(A) =\begin{vmatrix}
            a & b \\
            c & d 
            \end{vmatrix} =ad-bc.

.. admonition:: Athugasemd
    :class: athugasemd

    Athugið að ákveða :math:`2 \times 2` fylkis :math:`A` kemur fyrir í andhverfu fylkisins

     .. math:: A^{-1} =\frac{1}{ad-bc}\begin{bmatrix}
            d & -b \\
            -c & a 
            \end{bmatrix}.

    Við sjáum að fylkið :math:`A^{-1}` er ekki skilgreint fyrir :math:`ad-bc=0`, m.ö.o. fylkið :math:`A` er andhverfanlegt ef og aðeins ef :math:`\det(A)\neq 0`.  

Ákveða :math:`n \times n` fylkis
--------------------------------

Skilgreining: Hlutfylki
~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
    :class: skilgreining

        Látum :math:`A` vera :math:`n \times n` fylki. Fylkið sem fæst með því að fjarlægja :math:`i`-tu línu og :math:`j`-ta dálk kallast hlutfylk, :math:`A_{ij}`, og hefur stærð :math:`(n-1)\times (n-1)`.

Sýnidæmi: Hlutfylki
^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
  :class: daemi
    
    Hver eru hlutfylki, :math:`A_{ij}`, fylkisins

    .. math:: A =\begin{bmatrix}
            3 & 6 & 1\\
            5 & 2 & 0\\
            1 & 9 & 4\\
            \end{bmatrix}.
        
.. admonition:: Lausn
  :class: daemi, dropdown

    :math:`A` hefur eftirfarandi hlutfylki
    
    .. math::

Skilgreining: Ákveða :math:`n \times n` fylkis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. admonition:: Skilgreining
    :class: skilgreining

        Ákveða :math:`n \times n` fylkis :math:`A` er skilgreind

        .. math:: \det(A)=a_{11}\det(A_{11})-a_{12}det(A_{12})+...+ (-1)^{1+n} a_{1n}\det(A_{1n})
            = \sum_{j=1}^{n}(-1)^{1+j}a_{1j}\det(A_{1j})

..math:: A_{11}=\begin{}

.. math::A_{11} =\begin{bmatrix} 2 & 0\\ 9 & 4\\ \end{bmatrix},\quad
        A_{12} =\begin{bmatri}
            5 & 0\\
            1 & 4\\
            \end{bmatrix},\quad
            A_{13} =\begin{bmatrix}
            5 & 2 \\
            1 & 9\\
            \end{bmatrix},
            \newline
            A_{21} =\begin{bmatrix}
            6 & 1\\
            9 & 4\\
            \end{bmatrix}, \quad
            A_{22} =\begin{bmatrix}
            3 & 1\\
            1 & 4\\
            \end{bmatrix}, \quad
            A_{23} =\begin{bmatrix}
            3 & 6\\
            1 & 9\\
            \end{bmatrix}.
