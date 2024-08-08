Eigingildi og eiginvigrar
==========================

Eigingildi og eiginvigur
------------------------

Skilgreining: Eigingildi og eiginvigur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`A` vera :math:`n \times n` fylki. Ef til er vigur 
    :math:`\textbf{x} \neq \textbf{0}` og tala :math:`\lambda` þannig að

    .. math:: A\textbf{x}=\lambda\textbf{x}
    
    Þá segjum við að :math:`\lambda` sé **eigingildi** (e. eigenvalue) :math:`A`
    og :math:`x` **eiginvigur** (e. eigenvector). Ef að :math:`x` og :math:`\lambda` uppfylla
    jöfnuna að ofan þá segjum við að :math:`x` sé eiginvigur við eigingildi :math:`\lambda`.
    Við þessar aðstæður segjum við að eigingildið :math:`\lambda` og eiginvigurinn :math:`x` 
    tilheyri hvort öðru.


Sýnidæmi: Eigingildi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi
    
    Látum :math:`A=\begin{bmatrix} 2&0\\0&1 \end{bmatrix}` og 
    :math:`\textbf{x} = \begin{bmatrix}1\\0\end{bmatrix}` finnum eigingildi.

.. admonition:: Lausn
    :class: daemi, dropdown

    Fáum
    
    .. math:: A\textbf{x} = \begin{bmatrix}
        2\\0\end{bmatrix} = 2 \begin{bmatrix}
        1\\0\end{bmatrix} = 2 \textbf{x}
    
    svo 2 er eigingildi :math:`A` og :math:`\textbf{x}` er tilsvarandi eiginvigur.


Setning: Eigingildi
~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`n \times n` fylki. Tala :math:`\lambda` er 
    eigingildi fylkis :math:`A` ef og aðeins ef :math:`\det(A-\lambda I)=0`.

Sýnidæmi: Eigingild og eiginvigrar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Finnið eigingildi og eiginvigra

    .. math:: A=\begin{bmatrix}2 & 1\\ 9 & 2\end{bmatrix}

.. admonition:: Lausn
    :class: daemi, dropdown

    Byrjum að finna eigingildin, til þess þarf

    .. math:: A-\lambda I = \begin{bmatrix}2-\lambda & 1 \\ 9 & 2-\lambda\end{bmatrix} (*)

    að vera óandhverfanlegt og hafa þannig ákveðuna 0. Höfum að

    .. math:: \begin{align*}
        \begin{vmatrix}
        2-\lambda & 1 \\ 9 & 2-\lambda
        \end{vmatrix}
        &= (2-\lambda)^2-9\\&= \lambda^2-4\lambda+4-9\\&=\lambda^2-4\lambda-5\\& =
        (\lambda-5)(\lambda+1)  
        \end{align*}

    svo ef :math:`A-\lambda I` er óandhverfanlegt þá er :math:`(\lambda-5)(\lambda+1)=0` 
    sem gefur að :math:`\lambda = 5` eða :math:`\lambda =-1`.

    Tökum :math:`\lambda=5` og þá fæst að við erum að reyna að leysa jöfnuhneppið (*) sem er þá

    .. math:: \begin{bmatrix}
        -3 & 1\\
        9 & -3
        \end{bmatrix} \sim \begin{bmatrix}
        1 & -1/3\\
        0 & 0
        \end{bmatrix}
    
    svo :math:`\textbf{x} = t\begin{bmatrix}1/3\\1\end{bmatrix}`.

    Nú má auðveldlega sannreyna að :math:`\begin{bmatrix} 1/3\\1\end{bmatrix}`
    er eiginvigur sem svarar til eigingildisins 5. 


Eiginrúm 
--------

Setning: Eiginrúm
~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`n\times n` fylki og :math:`\lambda`
    eigingildi þess. Mengi allra eiginvigra tilheyrandi eigingildinu :math:`\lambda`
    að viðbættum núllvigrinum :math:`\textbf{0}` er hlutrúm í :math:`\mathbb{R}^n`. 
    Þetta hlutrúm er kallað **eiginrúm** (e. eigenspace) tilheyrandi eigingildinu :math:`\lambda`
    og táknað með :math:`E(\lambda)`. Eiginrúmið er núllrúm fylkisins :math:`A-\lambda I`.

Sýnidæmi: Eiginrúm fylkis
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Gefið er að 3 og 4 eru eigingildi fylkisins :math:`A`. Finnið 
    eiginrúm :math:`A` með tilliti til eigingildanna.

    .. math:: A=\begin{bmatrix} 1 & 3 \\ -2 & 6 \end{bmatrix}
    
.. admonition:: Lausn
    :class: daemi, dropdown

    Við byrjum á að finna eiginrúmið sem tilheyrir eigingildinu :math:`\lambda=3`. 
    Til þess leysum við jöfnuna :math:`(A-3I)\textbf{x}=0`. Fáum

    .. math:: A-3I=
        \begin{bmatrix}
        -2 & 3\\
        -2 & 3
        \end{bmatrix}
        \sim \begin{bmatrix}
        -2 & 3\\
        0 & 0 
        \end{bmatrix}
    
    svo að :math:`\ve{x}=\begin{bmatrix}x_1\\x_2\end{bmatrix}=x_2\begin{bmatrix}3\\2\end{bmatrix}` er lausn á jöfnunni.
    Við getum því séð að :math:`\begin{bmatrix}3\\2\end{bmatrix}` er eiginvigur með eigingildi :math:`\lambda=3` og því er
    :math:`E(3)=\spn{\begin{bmatrix}3\\2\end{bmatrix}}`.
    
    Gerum nú það sama fyrir eigingildið :math:`\lambda=4`. Þá þurfum við að leysa :math:`(A-4I)\textbf{x}=0`.
    Fáum að

    .. math:: A-4I=
        \begin{bmatrix}
        -3 & 3\\
        -2 & 2
        \end{bmatrix}
        \sim \begin{bmatrix}
        1 & -1\\
        -2 & 2 \\
        \end{bmatrix}
        \sim \begin{bmatrix}
        1 & -1\\
        0 & 0 \\
        \end{bmatrix}
    
    svo að með sömu rökum er :math:`\begin{bmatrix}1\\1\end{bmatrix}` eiginvigur með eigingildi :math:`\lambda=4`
    og því er :math:`E(4)=\spn{\begin{bmatrix}1\\1\end{bmatrix}}`.


Setning: Eigingildi þríhyrningsfylkja
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Ef :math:`A` er :math:`n \times n` þríhyrningsfylki þá eru eigingildi :math:`A`
    stökin á hornalínunni.

Setning: Eiginvigrar línulega óháðir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`\textbf{v}_1, \dots \textbf{v}_r` vera eiginvigra sem svara til ólíkra eigingilda 
    :math:`\lambda_1,\dots, \lambda_r` fylkisins :math:`A`. Þá er mengið 
    :math:`\{\textbf{v}_1, \dots, \textbf{v}_r\}` línulega óháð.

.. admonition:: Aðvörun
    :class: advorun

    Einfaldar línuaðgerðir varðveita ekki eigingildi.

Setning: 0 sem eigingildi 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Talan 0 er eigingildi fylkisins :math:`A` þá og því aðeins að :math:`A` er óandhverfanlegt.

Kennijafnan
-----------

Setning: Kennijafnan
~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning 
    :class: setning 
    
    Jafnan :math:`\det(A-\lambda I)=0` kallast **kennijafna** (e. characteristic equation) fylkisins A. 

Sýnidæmi: Kennijafnan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Finnum eigingildi og eignvigra fylkisins

    .. math:: A = \begin{bmatrix}
        10 & 2 \\
        9 & 3
        \end{bmatrix}  

.. admonition:: Launs
    :class: daemi, dropdown

    Til að finna eiginvigra þarf að finna ekki-augljósa lausn á jöfnunni :math:`(A-\lambda I)\textbf{x} = \textbf{0}`. Til þess þarf að gilda 
    :math:`\det(A - \lambda I) = 0`.
    
    Reiknum

    .. math:: \begin{align*}
        \begin{vmatrix}
        10-\lambda & 2 \\
        9 & 3-\lambda
        \end{vmatrix} 
        &= (10-\lambda)(3-\lambda) - (2 \cdot 9) = \lambda^2 - 13\lambda + 12 = \\&= (\lambda-12)(\lambda -1).
        \end{align*}
    
    Þessi ákveða er jöfn :math:`0` þegar :math:`(\lambda-12)(\lambda -1)=0` við fáum því tvö eigingildi, :math:`\lambda = 1` og :math:`\lambda=12`.
    Skoðum fyrst eigingildið :math:`\lambda = 1`

    .. math:: (A - \lambda I)\textbf{x}= \begin{bmatrix}
        10-1 & 2 \\
        9 & 3-1
        \end{bmatrix} \begin{bmatrix}
        x_1 \\
        x_2
        \end{bmatrix} = \begin{bmatrix}
        9 & 2 \\
        9 & 2
        \end{bmatrix} \begin{bmatrix}
        x_1 \\
        x_2
        \end{bmatrix} = \begin{bmatrix}
        0 \\
        0
        \end{bmatrix}
    
    sem gefur lausnina 
    
    .. math:: \begin{bmatrix}
        x_1\\x_2
        \end{bmatrix}=\begin{bmatrix}
        (-2/9)x_2\\x_2
        \end{bmatrix}=x_2\begin{bmatrix}
        (-2/9)\\1
        \end{bmatrix}


    Eiginvigrar m.t.t. 1 eru því öll margfeldi :math:`[-2/9 \ 1]^T` þannig að við getum 
    líka skrifað að alla eiginvigra sem svara til :math:`\lambda=1` megi skrifa á forminu


    .. math:: t\begin{bmatrix}
        -2\\ 9
        \end{bmatrix}.

    Skoðum næst  :math:`\lambda = 12` 

    .. math:: (A - \lambda I)\textbf{x} = \begin{bmatrix}
        10-12 & 2 \\
        9& 3-12
        \end{bmatrix} \begin{bmatrix}
        x_1 \\
        x_2
        \end{bmatrix} = \begin{bmatrix}
        -2 & 2 \\
        9 & -9
        \end{bmatrix} \begin{bmatrix}
        x_1 \\
        x_2
        \end{bmatrix} = \begin{bmatrix}
        0 \\
        0
        \end{bmatrix}


    Auðvelt að sjá að allar tölur :math:`x_1,x_2` 
    sem uppfylla :math:`x_1=x_2` 
    eru lausnir svo eiginvigrar m.t.t. 12 eru allir á forminu:

    .. math:: 
        \begin{bmatrix}
        x_1\\x_2
        \end{bmatrix}=\begin{bmatrix}
        x_2\\x_2
        \end{bmatrix}=x_2\begin{bmatrix}
        1\\1
        \end{bmatrix}=t\begin{bmatrix}
        1\\1   
        \end{bmatrix}

.. admonition:: Athugasemd
    :class: athugasemd

    Kennijafnan getur í mesta lagi haft :math:`n` ólýkar núllstöðvar. 
    Ef að margliðan þéttast þannig að einhver núllstöð :math:`r` kemur fyirr í :math:`s`-ta veldi
    þáttun hennar þá segjum við að eigingildið :math:`r` hafi algebrulega margfeldni :math:`s` 
    (e. algrebraic multiplicity).

Sýnidæmi: Margfeldni eigingildis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Finnið eigingildin

    .. math:: A=\begin{bmatrix}
        1 & 3 & 0\\
        0  &-2 &1\\
        0& 0& 1\\
        \end{bmatrix}

.. admonition:: Dæmi
    :class: daemi

    Fáum

    .. math:: \begin{vmatrix}
        1-\lambda & 3 & 0\\
        0  &-2 -\lambda&1\\
        0& 0& 1 -\lambda \\
        \end{vmatrix}
        =
        (1-\lambda)^2(-2-\lambda)

    Þar með hefur eigingildið 1 margfeldnina 2 en eigingildið -2 hefur margfeldnina 1.

Ámóta fylki
-----------

Skilgreining: Ámóta
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Tvö :math:`n \times n` fylki :math:`A` og :math:`B` eru sögð **ámóta**
    (e. similar) ef til er andhverfanlegt fylki :math:`P` þannig að 

    .. math:: B=P^{-1}AP
    

.. admonition:: Athugasemd
    :class: athugasemd

    **1.** Ferningsfylki :math:`A` er ámóta sjálfu sér.

    **2.** Ef :math:`B=P^{-1}AP` þá er :math:`A=P^{-1}BP`

    **3.** Gerum ráð fyrir að fylki :math:`A` sé ámóta fylkinu :math:`B`
    og fylkið :math:`B` sé ámóta fylkinu :math:`C`. Þá er :math:`A` ámóta :math:`C`.

    Þessi þrjú atriði segja að það að vera ámóta er dæmi um það sem er kallað *jafngildisvensl*.

Setning: Kennijafna ámóta fylkja 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Ef :math:`A` og :math:`B` eru ámóta fylki þá hafa þau sömu kennijöfnur 
    og þar með sömu eigingildi (með sama margfeldni hvert).

.. admonition:: Sönnun
    :class: setning, dropdown

    Skrifum :math:`B=P^{-1}AP` fyrst :math:`A` og :math:`B` eru ámóta. Þá er

    .. math:: \begin{align*}
        P(A-\lambda I )P^{-1} 
        &=(PA - P\lambda I)P^{-1}= 
        (PA- \lambda PI)P^{-1} \\
        &=(PA- \lambda P)P^{-1}= 
        PAP^{-1}- \lambda PP^{-1}=
        B-\lambda I
        \end{align*}

    Þar með er líka 

    .. math:: \det(P(A-\lambda I )P^{-1})=\det(B-\lambda I)

    sem gefur

    .. math:: \det(P)\det(A-\lambda I )\det(P)^{-1}=\det(B-\lambda I)
    
    svo :math:`\det(A-\lambda I)=\det(B-\lambda I)` og :math:`A` og :math:`B` hafa sömu kennijöfnu.


.. admonition:: Aðvörun
    :class: advorun

    Mögulegt er að tvö fylki hafi nákvæmlega sömu eigingildi 
    með sömu margfeldni en séu samt ekki ámóta. 

Hornalínugjörningar
-------------------

Skilgreinig: Hornalínufylki
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreinig
    :class: skilgreining

    Við segjum að :math:`n \times n` fylki :math:`D` sé **hornalínufylki**
    (e. diagonal matrix) ef öll stök utan hornalínunnar eru 0.

    .. math:: D = \begin{bmatrix}
        d_1 & 0 & \cdots & 0 \\
        0 & d_2 & \cdots & 0 \\
        \vdots & \vdots & \ddots & \vdots \\
        0 & 0 & \cdots & d_n
        \end{bmatrix}


Skilgreinig: Hornalínugeranlegt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreinig
    :class: skilgreining

    Ferningsfylki :math:`A` sem er ámóta hornalínufylki er sagt **hornalínugeranlegt** (e. diagnoalizable). 
    Það er að segja, fylki :math:`A` er hornalínugeranlegt ef til er andhverfanlegt
    fylki :math:`P` þannig að :math:`A=PDP^{-1}` þar sem :math:`D` er hornlínufylki.
 


Að hornalínugera fylki

    **1.** Finnum eigingildi :math:`A`.

    **2.** Finnum :math:`n` línulega óháða eiginvigra :math:`A`.

    **3.** Smíðum fylkið :math:`P` úr eiginvigrnum í skrefi 2.

    **4.** Smiðum fylkið :math:`D` úr eigingildum í skrefi 1. 


Sýnidæmi: Hornalínugjörningar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Hornulínugerið fylkið :math:`A` ef hægt er

    .. math:: A=\begin{bmatrix} 
        3 & 2 & 1\\
        0 & 1 & 0\\
        0 & 0 & 1 
        \end{bmatrix}

.. admonition:: Launs
    :class: daemi, dropdown

    Þar sem :math:`A` er hornalínufylki eru eigingildi þess stökin
    á honralínunni, sem sagt :math:`\lambda = 3` og :math:`\lambda = 1`.
    Fyrir :math:`\lambda = 3` fæst

    .. math:: \begin{bmatrix}
        0 & 2 & 1\\
        0 & -2 & 0\\
        0 & 0 & -2\\
        \end{bmatrix}
        \sim \dots \sim
        \begin{bmatrix}
        0 & 1 & 0\\
        0 & 0 & 1\\
        0& 0& 0
        \end{bmatrix}
    
    sem svara til jöfnuhneppisins :math:`x_2=0, x_3=0` sem hefur lausn

    .. math:: \begin{bmatrix}
        x_1\\
        x_2\\
        x_3
        \end{bmatrix}=\begin{bmatrix}
        x_1\\
        0\\
        0\\
        \end{bmatrix}=x_1\begin{bmatrix}
        1\\
        0\\
        0
        \end{bmatrix}

    Fyrir :math:`\lambda = 1` fæst

    .. math:: \begin{bmatrix}
        2& 2 & 1\\
        0 & 0 & 0\\
        0& 0& 0
        \end{bmatrix}\sim
        \begin{bmatrix}
        1 & 1 & \frac{1}{2}\\
        0 & 0 & 0\\
        0& 0& 0
        \end{bmatrix}

    sem svarar til jöfnuhneppisins :math:`x_1+x_2+1/2x_3=0` sem hefur lausninirnar

    .. math:: \begin{bmatrix}
        x_1\\
        x_2\\
        x_3
        \end{bmatrix}=\begin{bmatrix}
        -x_2-\frac{1}{2}x_3\\
        x_2\\
        x_3\\
        \end{bmatrix}=x_2\begin{bmatrix}
        -1\\
        1\\
        0
        \end{bmatrix}+x_3\begin{bmatrix}
        -\frac{1}{2}\\
        0\\
        1
        \end{bmatrix} 

    Fylkið hefur því þrjá línulega áháða eiginvigra sem mynda fylkið 
    :math:`P`. Auk þess fáum við :math:`D`

    .. math:: P= \begin{bmatrix}
        1&   -1& -\frac{1}{2}\\
        0 &  1& 0\\
        0 &  0& 1
        \end{bmatrix}, \quad 
        D=\begin{bmatrix}
        3&   0 & 0\\
        0 &  1& 0\\
        0 &  0& 1
        \end{bmatrix}
    
    og :math:`A` er hornalínugeranlegt með :math:`A=PDP^{-1}`.


Setning: Hornalínugeranleg fylki
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`n \times n` fylki. Ef fylkið :math:`A` hefur :math:`n`
    ólík eigingildi þá er fylkið :math:`A` hornalínugeranlegt.

Sýnidæmi: Er fylkið hornalínugeranlegt 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Er fylkið :math:`A=\begin{bmatrix} 1 & 2 & 3\\ 0 & 4 & 5 \\ 0 & 0 & 6\end{bmatrix}` hornalínugeranlegt?

.. admonition:: Lausn
    :class: daemi, dropdown

    Kennimargliða :math:`A` er :math:`p(\lambda)=(1-\lambda)(4-\lambda)(6-\lambda)`.
    Eigingildin eru :math:`\lambda_1=1, \lambda_2=4` og :math:`\lambda_3=6`. Höfum hér :math:`3 \times 3`
    fylki með 3 ólík eigingildi. Fylkið er því hornalínugeranlegt.


Setning: Vídd eiginrúms
~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`A` vera :math:`n \times n` fylki sem hefur ólíku eigingildin :math:`\lambda_1, \dots, \lambda_p` (með :math:`p\leq n`). Þá gildir eftirfarandi.
    
        **1.** Vídd eiginrúmsins m.t.t. :math:`\lambda_k` er minni eða jöfn margfeldni eigingildisins :math:`\lambda_k`, fyrir :math:`1\leq k\leq p`.
    
        **2.** Fylkið :math:`A` er hornalínugeranlegt þá og því aðeins að summa vídda eiginrúma m.t.t. allra eigingildanna :math:`\lambda_k` er jöfn :math:`n`. 
        Til þess þarf kennijafnan að þáttast að fullu í línulega þætti og vídd eiginrúms m.t.t. til hvers eigingildis að vera jöfn margfeldni þess.
    
        **3.** Ef :math:`A` er hornalínugeranlegt og :math:`\mathcal{B}_k` er grunnur fyrir eiginrúm m.t.t :math:`\lambda_k` fyrir fyrir :math:`1\leq k\leq p` þá myndar sammengið
                
        .. math:: \mathcal{B}_1\cup \dots \cup \mathcal{B}_k
    
        grunn fyrir :math:`\mathbb{R}^n`.



Eiginvigrar línulegra varpana
-----------------------------

Skilgreining: Eigingildi og eiginvigrar línulegra varpana 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`V` vera vigurrúm og :math:`T\text{:}V \rightarrow V` vera
    línulega vörpun. Ef til er vigur :math:`\textbf{x} \neq \textbf{0}`
    í :math:`V` og tala :math:`\lambda` þannig að :math:`T(x)=\lambda\textbf{x}`
    þá kallast :math:`\lambda` eigingildi :math:`T` og :math:`\textbf{x}` kallast
    eiginvigur :math:`T` sem svara til :math:`\lambda`.


Sýnidæmi: Eiginvigrar línulegra varpana
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Skoðum vörpunina :math:`T\text{:}\mathbb{P}_1 \rightarrow \mathbb{P}_1`,
    :math:`T(a_1x+a_0)=2a_1x+2a_0` þar sem við skoðum margliðuna :math:`p(x)=x`
    og fáum 

    .. math:: T(p(x))=T(x)=2x=2p(x)
    
    svo margliðan :math:`p(x)=x` er eiginvigur :math:`T` og :math:`\lambda=2` er eigingildi :math:`T`.
    Einnig ef við tökum :math:`p(x)=1` fæst

    .. math:: T(p(x))=T(1)=2=2\cdot 1=2p(x)
    
    svo :math:`p(x)=1` er líka eiginvigur :math:`T` og hefur einnig eigingildið :math:`\lambda=2`.

Setning: Fylki línulegra varpana í :math:`V`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`T:\mathbb{R}^n\rightarrow\mathbb{R}^n` vera línulega vörpun með fylkið :math:`A`. Gerum ráð fyrir að 
    :math:`A` sé hornalínugeranlegt. Látum :math:`\mathcal{B}` vera grunn sem myndaður er að eiginvigrum 
    :math:`A` og :math:`P` vera fylkið sem hefur eiginvigra :math:`A` sem dálka. Hornalínufylkið 
    :math:`D=P^{-1}AP` er þá fylki vörpunarinnar m.t.t. grunnsins :math:`\mathcal{B}`.

Sýnidæmi: Fylki línulegra varpana í :math:`V`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Látum :math:`V` vera n-vítt vigurrúm og :math:`T\text{:}V \rightarrow V` vera línulega
    vörpun. Hvernig finnum við fylki sem táknar :math:`T`?

.. admonition:: Lausn
    :class: daemi, dropdown

    Við færum okkur yfir í :math:`\mathbb{R}^n`. Látum :math:`\mathcal{B}=\{\textbf{b}_1, \dots, \textbf{b}_n\}` vera einhvern grunn
    fyrir :math:`V`. Tökum :math:`\textbf{x} \in V`. Þá má skrifa

    .. math:: \textbf{x}=r_1\textbf{b}_1+\dots+r_n\textbf{b}_n

    og við skrifum 

    .. math:: [\textbf{x}]_\mathcal{B} = \begin{bmatrix}
        r_1\\\vdots\\r_n
        \end{bmatrix}

    Þá gildir líka 

    .. math:: T(\textbf{x})=T(r_1\textbf{b}_1+\dots+r_n\textbf{b}_n)=r_1T(\textbf{b}_1)+\dots+r_nT(\textbf{b}_n)

    Beitum hnitavörpunninni :math:`V\rightarrow\mathbb{R}^n, \textbf{x}\mapsto[\textbf{x}]_\mathcal{B}` á báðar hliðar og fáum

    .. math:: \begin{align*}
        [T(\textbf{x})]_\mathcal{B}
        &=r_1[T(\textbf{b}_1)]_\mathcal{B} + \dots +r_n[T(\textbf{b}_n)]_\mathcal{B}
        \\&= \begin{bmatrix}
        [T(\textbf{b}_1)]& \dots &[T(\textbf{b}_n)]_\mathcal{B}
        \end{bmatrix}
        \underbrace{\begin{bmatrix}
        r_1 \\ \vdots \\ r_n
        \end{bmatrix}}_{[\textbf{x}]_\mathcal{B}}
        \end{align*} 
    
    Skilgreinum nú fylkið

    .. math:: T_\mathcal{B}=\begin{bmatrix}
        [T(\textbf{b}_1)]& \dots &[T(\textbf{b}_n)]_\mathcal{B}
        \end{bmatrix}
    
    og þá fæst

    .. math:: [T(\textbf{x})]_\mathcal{B}=T_\mathcal{B}[\textbf{x}]_{\mathcal{B}}.


Sýnidæmi: Hornalínugjörningur
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Dæmi
    :class: daemi

    Látum :math:`\begin{bmatrix} 0 & 1\\ 5 & 6 \end{bmatrix}` vera venjulega fylkið
    fyrir línulega vörpun :math:`\mathbb{R}^2 \rightarrow \mathbb{R}^2`.
    finnið grunn :math:`\mathcal{B}` fyrir :math:`\mathbb{R}^2` þannig að 
    :math:`\mathcal{B}` -fylki :math:`T` sé hornalínufylki.

.. admonition:: Launs
    :class: daemi, dropdown

    Fyrst finnum við eigingildin og eiginvigrana:

    .. math:: \det(A-\lambda I)=\begin{vmatrix}
        -\lambda & 1 \\
        7 & 6 - \lambda
        \end{vmatrix} = \lambda^2 - 6\lambda - 7 = 0
    
    Þetta gefur :math:`(\lambda-7)(\lambda+1)=0` 
    og við fáum eigingildin: :math:`\lambda_1=7` og :math:`\lambda_2=-1`.
    Finnum eiginvigra fyrir :math:`\lambda_1=7` 

    .. math:: A-7I=\begin{bmatrix}
        -7 & 1 \\
        7 & -1
        \end{bmatrix}
        \sim \begin{bmatrix}
        7 & -1 \\
        0 & 0
        \end{bmatrix}

    Eiginvigur: :math:`\textbf{v}_1=\begin{bmatrix} 1 \\ 7 \end{bmatrix}`.
    Finnum eiginvigra fyrir :math:`\lambda_2=-1`

    .. math:: A-(-1)I=\begin{bmatrix}
        1 & 1 \\
        7 & 7
        \end{bmatrix}\sim\begin{bmatrix}
        1 & 1 \\
        0 & 0
        \end{bmatrix}\Rightarrow x + y = 0
    
    Eiginvigur: :math:`\textbf{v}_2=\begin{bmatrix} -1 \\ 1 \end{bmatrix}`
    Getum því skrifað

    .. math:: P=\begin{bmatrix}
        1 & -1 \\
        7 & 1
        \end{bmatrix} \text{ og } D=\begin{bmatrix}
        7 & 0 \\
        0 & -1
        \end{bmatrix}
    
    Þá gildir að :math:`A=PDP^{-1}` og :math:`\mathcal{B} = \left\{\begin{bmatrix} 1 \\ 7 \end{bmatrix},\begin{bmatrix} -1 \\ 1 \end{bmatrix}\right\}`.


