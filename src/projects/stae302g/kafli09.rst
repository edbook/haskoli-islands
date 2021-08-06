Línuleg afleiðujöfnuhneppi
==========================

Leela: *"To be, or not to be, that is the question." That is a very stupid question!*

The Doctor: *It's Shakespeare.*

Leela: *And that is a very stupid name. You do not shake a spear, you throw it! Throwspeare, now that is a name.*


Línuleg afleiðujöfnuhneppi
--------------------------

Skilgreining (Sjá §9.1)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Afleiðujöfnuhneppi af gerðinni

	.. math::

	   \begin{aligned}
	   u_1'&=a_{11}(t)u_1+\cdots+a_{1m}(t)u_m+f_1(t),\\
	   u_2'&=a_{21}(t)u_1+\cdots+a_{2m}(t)u_m+f_2(t),\\
	   \vdots&\qquad \qquad \vdots\qquad \qquad \qquad \qquad \vdots\\
	   u_m'&=a_{m1}(t)u_1+\cdots+a_{mm}(t)u_m+f_m(t).\end{aligned}

	er kallað línulegt fyrsta stig afleiðujöfnuhneppi. Á fylkjaformi má rita þetta sem

	.. math::

	   \begin{bmatrix}u_1'\\u_2'\\\vdots\\u_m'\end{bmatrix}
	   =\begin{bmatrix}a_{11}(t)&a_{12}(t)&\cdots&a_{1m}(t)\\
	   a_{11}(t)&a_{12}(t)&\cdots&a_{1m}(t)\\
	   \vdots&\vdots&\ddots&\vdots\\
	   a_{m1}(t)&a_{m2}(t)&\cdots&a_{mm}(t)\end{bmatrix}
	   \begin{bmatrix}u_1 \\u_2 \\\vdots\\u_m\end{bmatrix}
	   +\begin{bmatrix}f_1(t) \\f_2(t) \\\vdots\\f_m(t)\end{bmatrix},

	og ef við notum :math:`u(t)` til að tákna vigurinn :math:`(u_1(t), u_2(t), \ldots, u_m(t))`, og svo :math:`A(t)` til að tákna fylkið og :math:`f(t)` til að tákna vigurinn :math:`(f_1(t), f_2(t), \ldots, f_m(t))` þá má rita jöfnuna hér að ofan sem :math:`u'=A(t)u+f(t)`.

	Hér er gert ráð fyrir að föllin sem koma fyrir í fylkinu :math:`A(t)` og sem hnit í :math:`f(t)` séu öll skilgreind á einhverju opnu bili :math:`I` í :math:`\mathbb{R}` og að þau séu öll samfelld.

	Í framhaldinu er gert ráð fyrir að :math:`u, A, f` séu á því formi sem lýst er hér að ofan.



Skilgreining (Sjá §9.1)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Afleiðujafna af taginu :math:`u'=A(t)u+f(t)` er sögð óhliðruð ef :math:`f(t)` er núllfallið
	(útkoman er alltaf vigurinn sem hefur 0 í öllum hnitum), en hliðruð annars. Talað er um jöfnuhneppi með fastastuðlum ef stuðlarnir í fylkinu :math:`A` eru allir fastar.

Setning (Sjá §9.1)
~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Upphafsgildisverkefnið

	.. math::

	 u'=A(t)u+f(t), \qquad u(a)=b,\label{5.1.2}

	hefur ótvírætt ákvarðaða lausn, þar sem :math:`a` er einhver gefinn punktur í :math:`I` og :math:`b` er einhver gefinn vigur í :math:`{\mathbb{C}}^m`. Sjá `Fylgisetningu 6.3.5 <./Kafli06.html#fylgisetning-sja-fylgisetningu-6-6-6>`_

Setning (Sjá §9.1)
~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`I` vera opið bil á rauntalnaásnum. Rifjum upp að :math:`C(I, {\mathbb{C}}^m)` er mengi allra samfelldra falla skilgreindra á :math:`I` með gildi í :math:`{\mathbb{C}}^m` og :math:`C^1(I, {\mathbb{C}}^m)` er mengi allra falla skilgreindra á :math:`I` með gildi í :math:`{\mathbb{C}}^m` sem hafa samfellda fyrstu afleiðu. Bæði :math:`C(I, {\mathbb{C}}^m)` og :math:`C^1(I, {\mathbb{C}}^m)` eru vigurrúm.

	Vörpunin :math:`L:C^1(I, {\mathbb{C}}^m)\to C(I, {\mathbb{C}}^m)` þannig að :math:`Lu=u'-A(t)u` er línuleg.

Fylgisetning (Sjá Setningu 9.1.3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Fylgisetning
	:class: setning

	(i) Lausnamengi óhliðraðar jöfnu :math:`u'=A(t)u` er hlutrúm í :math:`C^1(I, {\mathbb{C}}^m)` af vídd :math:`m`. Lausnamengið, eða núllrúm A, er táknað með :math:`{\cal N}(A)`.

	(ii) Sérhver lausn á :math:`u'=A(t)u+f(t)` er af gerðinni

	.. math::

	 u(t)=c_1u_1(t)+\cdots+c_mu_m(t)+u_p(t),

	þar sem :math:`u_1,\dots,u_m` er einhver grunnur :math:`{\cal N}(A)`, :math:`c_1,\dots,c_m\in{\mathbb{C}}` og :math:`u_p` er einhver lausn á hliðruðu jöfnunni.


Setning (Sjá Hjálparsetningu 9.3.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`u_1,\dots,u_m` vera föll í :math:`{\cal N}(A)`. Þá eru eftirfarandi skilyrði jafngild:

	(i) Vigurföllin :math:`u_1,\dots,u_m` eru línulega óháð á bilinu :math:`I`.

	(ii) Vigrarnir :math:`u_1(t),\dots,u_m(t)` eru línulega óháðir í :math:`\mathbb{R}^ m` (eða :math:`{\mathbb{C}}^ m`) fyrir sérhvert :math:`t\in I`.

	(iii) Vigrarnir :math:`u_1(a),\dots,u_m(a)` eru línulega óháðir í :math:`\mathbb{R}^ m` (eða :math:`{\mathbb{C}}^ m`) fyrir eitthvert :math:`a\in I`.

Setning (Sjá §9.1)
~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Línuleg afleiðujafna af taginu

	.. math::

	   P(t,D)v= v^{(m)}+a_{m-1}(t)v^{(m-1)}+\cdots+a_1(t)v'
	   +a_0(t)=g(t)

	er jafngild afleiðujöfnuhneppinu

	.. math::

	 u_1'=u_2,\quad u_2'=u_3,\quad  \ldots,\quad u_{m-1}'=u_m

	.. math::

	 u_m' =-a_0(t)u_1-a_1(t)u_2-\cdots-a_{m-1}(t)u_m+g(t).

	Þegar jöfnuhneppið ritað á fylkjaformi fæst

	.. math::

	   \begin{bmatrix}u_1'\\u_2'\\\vdots\\u_{m-1}'\\u_m'\end{bmatrix}
	   =\begin{bmatrix}
	   0&1&0&\dots&0\\
	   0&0&1&\dots&0\\
	   \vdots&\vdots&\vdots&\ddots&\vdots\\
	   0&0&0&\dots&1\\
	   -a_0(t)&-a_1(t)&-a_2(t)&\dots&-a_{m-1}(t)
	   \end{bmatrix}\begin{bmatrix}u_1 \\u_2 \\\vdots\\u_{m-1}\\u_m\end{bmatrix}
	   +\begin{bmatrix}0 \\0 \\\vdots\\0\\g(t)\end{bmatrix}.

	Ef við ritum :math:`P(t,D)=D^ m+a_{m-1}(t)D^{m-1}+\cdots+a_1(t)D+a_0(t)` og fylkið :math:`A(t)` er skilgreint eins og hér að ofan þá er

	.. math::

	 \det(\lambda I-A(t))=P(t,\lambda).

Setning (Sjá Hjálparsetningu 9.2.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`A` vera :math:`m\times m` fylki og :math:`\varepsilon` vera eiginvigur þess með tilliti til eigingildisins :math:`\lambda`. Þá uppfyllir vigurfallið :math:`u(t)=e^{\lambda t}\varepsilon` jöfnuna :math:`u'=Au`.

Setning (Sjá Setningu 9.2.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`A` vera :math:`m\times m` fylki og gerum ráð fyrir að :math:`\varepsilon_1,\dots,\varepsilon_\ell` séu eiginvigrar þess með tilliti til eigingildanna :math:`\lambda_1,\dots,\lambda_\ell`. Ef :math:`a \in I`, :math:`b\in {\mathbb{C}}^m` og unnt er að skrifa :math:`b=\beta_1\varepsilon_1+\cdots+\beta_\ell\varepsilon_\ell` og :math:`f(t)=g_1(t)\varepsilon_1+\cdots+g_\ell(t)\varepsilon_\ell`, þá er lausnin á upphafsgildisverkefninu

	.. math::

	 u'=Au+f(t), \qquad \qquad u(a)=b,

	gefin með :math:`u(t)=v_1(t)\varepsilon_1+\cdots+v_\ell(t)\varepsilon_\ell`, þar sem stuðullinn :math:`v_j` uppfyllir

	.. math::

	 v_j'(t)=\lambda_jv_j(t)+g_j(t), \qquad v_j(a)=\beta_j,

	og er þar með

	.. math::

	   v_j(t)=\beta_je^{\lambda_j(t-a)}+e^{\lambda_jt}\int_a^t e^{-\lambda_j
	   \tau}g_j(\tau) \, d\tau.



Skilgreining (Sjá §9.2)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Fyrir tölur :math:`t_1, t_2, \ldots, t_m` er :math:`{\operatorname{diag}}(t_1, t_2, \ldots, t_m)` skilgreint sem :math:`m\times m` hornalínufylkið sem hefur tölurnar :math:`t_1, t_2, \ldots, t_m` á hornalínunni.


Setning (Sjá §9.2.2)
~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`A` vera :math:`m\times m` fylki. Gerum ráð fyrir að :math:`T` sé :math:`m\times m` fylki þannig að :math:`T^{-1}AT=\Lambda` þar sem :math:`\Lambda` er hornalínufylki með stökin :math:`\lambda_1, \lambda_2, \ldots, \lambda_m` á hornalínunni. (Athugið að :math:`A=T\Lambda T^{-1}`.)

	Látum :math:`I` vera bil á :math:`\mathbb{R}`, :math:`a\in I`, :math:`f\in C(I,{\mathbb{C}}^m)` og :math:`b\in {\mathbb{C}}^m`. Þá hefur upphafsgildisverkefnið

	.. math::

	 u'=Au+f(t), \qquad u(a)=b

	ótvírætt ákvarðaða lausn á :math:`I`, sem gefin er með formúlunni

	.. math::

	   \begin{aligned}
	   u(t)&=T{\operatorname{diag}}(e^{\lambda_1(t-a)},\dots,e^{\lambda_m(t-a)})T^{-1}b\\
	   &+\int_a^t T{\operatorname{diag}}(e^{\lambda_1(t-\tau)},\dots,e^{\lambda_m(t-\tau)})
	   T^{-1}f(\tau)\, d\tau.\end{aligned}


Veldisvísisfylkið
-----------------


Skilgreining (Sjá Skilgreining 9.3.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Fylki af gerðinni

	.. math::

	 \Phi(t)=[u_1(t),\dots,u_m(t)], \qquad t\in I,

	þar sem dálkavigrarnir :math:`u_1,\dots,u_m` mynda grunn í núllrúminu :math:`{\cal N}(A)` fyrir afleiðujöfnuhneppið :math:`u'=A(t)u`, kallast grunnfylki fyrir afleiðujöfnuhneppið.

Setning (Sjá Setningu 9.3.3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Lát :math:`\Phi` og :math:`\Psi` vera tvö grunnfylki fyrir jöfnuhneppið :math:`u'=A(t)u`. Þá er til andhverfanlegt fylki :math:`B` þannig að

	.. math::

	 \Psi(t)=\Phi(t)B.\label{5.3.2}

Setning (Sjá Setningu 9.3.4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Lát :math:`\Phi(t)` vera grunnfylki fyrir jöfnuhneppið :math:`u' =A(t)u`.

	(i) Sérhvert stak í :math:`{\cal N}(A)` er af gerðinni :math:`u(t)=\Phi(t)c`, þar sem :math:`c` er vigur í :math:`{\mathbb{C}}^ m`.

	(ii) Vigurfallið :math:`u_p`, sem gefið er með formúlunni

	.. math::

	 u_p(t)=\Phi(t)\int_a^ t \Phi(\tau)^{-1}f(\tau)\, d\tau,

	uppfyllir :math:`u'=A(t)u+f(t)` og :math:`u(a)=0`.

	(iii) Lausnin á upphafsgildisverkefninu :math:`u'=A(t)u+f(t)`, :math:`u(a)=b` er gefin með formúlunni

	.. math::

	   u(t)=\Phi(t)\Phi(a)^{-1}b+
	   \Phi(t)\int_a^ t \Phi(\tau)^{-1}f(\tau)\, d\tau.



Skilgreining (Sjá §9.4)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Runa :math:`\{C_n\}_{n=0}^\infty`, af :math:`\ell\times m` fylkjum :math:`C_n=\big(c_{jkn}\big)_{j=1,k=1}^{\ell, m}` er sögð vera samleitin með markgildi :math:`C=\big(c_{jk}\big)_{j=1,k=1}^{\ell, m}` ef fyrir öll gildi á :math:`j, k` gildir að

	.. math::

	 \lim\limits_{n\to\infty}c_{jkn}=c_{jk}.

	Óendanleg summa :math:`\sum_{n=0}^\infty C_n` af :math:`\ell\times m` fylkjum er sögð vera samleitin, ef runan af hlutsummum :math:`\{\sum_{n=0}^N C_n\}_{N=0}^\infty` er samleitin.

Skilgreining (Sjá §9.4)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Fyrir :math:`m\times m`-fylki :math:`A` skilgreinum við

	.. math::

	 e^A=\sum_{n=0}^\infty \frac{1}{n!}A^n=I+A+\frac{1}{2}A^2+\frac{1}{3!}A^3+\cdots.

	.. attention::

	    Með tiltölulega lítilli fyrirhöfn (gert í hefti Ragnars) má sýna að röðin hér að ofan er samleitin fyrir öll :math:`m\times m` fylki :math:`A`. Einnig má skilgreina á sama hátt :math:`\sin A, \cos A, \ldots`.

Setning (Sjá §9.5)
~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	(i) Fyrir rauntölu :math:`t` er

	.. math::

	 \frac{d}{dt}e^{tA}=Ae^{tA}.

	(ii) (Sjá Setningu 9.5.1) Fylkjafallið :math:`\Phi(t)= e^{tA}` er hin ótvírætt ákvarðaða lausn upphafsgildisverkefnisins

	.. math::

	 \Phi'(t) = A\Phi(t), \qquad t\in \mathbb{R}, \qquad \Phi(0)=I.



Fylgisetning
~~~~~~~~~~~~

.. admonition:: Fylgisetning
	:class: setning

	Fylkið :math:`e^{tA}` er grunnfylki fyrir afleiðujöfnuhneppið :math:`u'=Au`.

Setning (Sjá Setningu 9.5.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	(i) Ef :math:`A` og :math:`B` eru :math:`m\times m` fylki og :math:`AB=BA`, þá er

	.. math::

	 e^{A+B}=e^ Ae^ B=e^Be^A.\label{5.5.1}

	(ii) Fylkið :math:`e^ {tA}` hefur andhverfuna :math:`e^{-tA}`.

Setning
~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`A` vera :math:`m\times m` fylki. Gerum ráð fyrir að að :math:`\varepsilon_1, \dots, \varepsilon_m` séu eiginvigrar tilheyrandi eigingildum :math:`\lambda_1, \dots \lambda_m` og að þessir vigrar myndi grunn. Látum :math:`T` vera fylkið sem hefur vigrana :math:`\varepsilon_1, \dots, \varepsilon_m` sem dálkvigra í þessari röð. Þá er

	.. math::

	 e^{tA}=T{\operatorname{diag}}(e^{\lambda_1t}, \ldots, e^{\lambda_mt})T^{-1}.

Útreikningur lausna
-------------------

Verkefni (Sjá §9.6)
~~~~~~~~~~~~~~~~~~~

Fyrir gefið :math:`m\times m` fylki :math:`A` skal reikna :math:`e^{tA}`.

Setning Cayley-Hamilton (Sjá §9.6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`A` vera :math:`m\times m` fylki. Kennimargliða :math:`A` er margliðan :math:`p(\lambda)=p_A(\lambda)=\det(\lambda I-A)`. Þá er :math:`p_A(A)=0`.

Afleiðing Setningar Cayley-Hamilton
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hægt er að finna föll :math:`f_0(t), f_1(t), \ldots, f_{m-1}(t)` þannig að

.. math::

 e^{tA}= f_0(t)I+f_1(t)A+\cdots+f_{m-1}(t)A^{m-1}.

Brúunarverkefni (Sjá §9.7)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f\in {\cal O}({\mathbb{C}})` vera gefið fall, látum :math:`\alpha_1,\dots,\alpha_\ell` vera ólíka punkta í :math:`{\mathbb{C}}`, látum :math:`m_1,\dots,m_\ell` vera jákvæðar heiltölur og setjum :math:`m=m_1+\cdots+m_\ell`. Viljum finna margliðu :math:`r` af stigi :math:`<m`, sem uppfyllir

.. math::

   f^{(j)}(\alpha_k) = r^{(j)}(\alpha_k), \qquad
    j=0,\dots,m_k-1, \quad
   k=1,\dots, \ell.

Þetta er alltaf hægt. Margliðan :math:`r` er ótvírætt ákvörðuð.

Skilgreining (Sjá §9.7)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Við skilgreinum rununa :math:`\lambda_1,\dots,\lambda_m` með því að telja :math:`\alpha_1,\dots,\alpha_\ell` með margfeldni, þannig að fyrstu :math:`m_1` gildin á :math:`\lambda_j` séu :math:`\alpha_1`, næstu :math:`m_2` gildin á :math:`\lambda_j` séu :math:`\alpha_2` o.s.frv. Svo er

	.. math::

	   p(z)=(z-\alpha_1)^{m_1}\cdots(z-\alpha_\ell)^{m_\ell}
	   =(z-\lambda_1)\cdots(z-\lambda_m).


Skilgreining (Sjá §9.7)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Látum :math:`\lambda_1,\dots,\lambda_m` vera talnarunu eins og hér að ofan.

	Mismunakvótar eru skilgreindir með formúlum

	.. math::

	 f[\lambda_i,\dots,\lambda_{i+j}]=\dfrac{f^{(j)}(\lambda_i)}{j!},

	ef :math:`\lambda_i=\cdots=\lambda_{i+j}`, og

	.. math::

	   f[\lambda_i,\dots,\lambda_{i+j}]=
	   \dfrac{f[\lambda_i,\dots,\lambda_{i+j-1}]-f[\lambda_{i+1},\dots,\lambda_{i+j}]}
	   {\lambda_i-\lambda_{i+j}},

	ef :math:`\lambda_i\neq \lambda_{i+j}`, fyrir :math:`i=1,\dots,m` og :math:`j=0,\dots,m-i` .

Setning (Sjá §9.7)
~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`f\in {\cal O}({\mathbb{C}})`, :math:`\alpha_1,\dots,\alpha_\ell` vera ólíka punkta í :math:`{\mathbb{C}}`, :math:`m_1,\dots,m_\ell` vera jákvæðar heiltölur, setjum :math:`m=m_1+\cdots+m_\ell` og skilgreinum :math:`p(z)` eins og hér að ofan. Þá er til margliða :math:`r` af stigi :math:`<m` og :math:`g\in {\cal O}({\mathbb{C}})` þannig að

	.. math::

	 f(z)=r(z)+p(z)g(z), \qquad z\in {\mathbb{C}}.

	Margliðan :math:`r` er lausn á brúunarverkefninu. Bæði :math:`r` og :math:`g` eru ótvírætt ákvörðuð og

	.. math::

	   \begin{aligned}
	   r(z)=f[\lambda_1]&+f[\lambda_1,\lambda_2](z-\lambda_1)+\cdots\\
	   &+ f[\lambda_1,\dots,\lambda_m](z-\lambda_1)\cdots(z-\lambda_{m-1})\end{aligned}

	og

	.. math::

	 g(z)=f[\lambda_1,\dots,\lambda_m,z](z-\lambda_1)\cdots(z-\lambda_m).

Reikniaðferð
~~~~~~~~~~~~

Þegar reikna þarf mismunakvóta þá er gott að fylgja sama skema og hér á eftir:

.. math::

   \begin{matrix}
   f[\lambda_1]\\
               &f[\lambda_1,\lambda_2]\\
   f[\lambda_2]&                       &f[\lambda_1, \lambda_2, \lambda_3]\\
           &f[\lambda_2,\lambda_3]& &f[\lambda_1,\lambda_2,\lambda_3,\lambda_4]\\
   f[\lambda_3]&                       &f[\lambda_2, \lambda_3, \lambda_4]\\
               &f[\lambda_3,\lambda_4]\\
   f[\lambda_4]
   \end{matrix}

Þegar :math:`\lambda_1=1=\lambda_2` og :math:`\lambda_3=-1=\lambda_4` og
:math:`f(z)=e^{tz}`:

.. math::

   \begin{matrix}
   \lambda_1=1 & e^t  \\
    & & te^t& \\
   \lambda_2=1 & e^t  &  & \tfrac 12(te^t-\sinh t)\\
    & & \sinh t & & \tfrac 12(t\cosh t-\sinh t) \\
   \lambda_3=-1 & e^{-t}  & & \tfrac 12(\sinh t -te^{-t})\\
    & & te^{-t}& \\
   \lambda_4=-1 & e^{-t}
   \end{matrix}



Reikniaðferð (Sjá §9.7)
~~~~~~~~~~~~~~~~~~~~~~~

Reikna á :math:`e^{tA}` fyrir :math:`m\times m` fylki :math:`A` og/eða lausn :math:`u'=Au` með ákveðið upphafsgildi :math:`u(0)=b`.

Skref 1: Reiknið eigingildi :math:`A` með margfeldni.

Skref 2: Setjið upp mismunatöflu líkt og sýnt er hér að ofan.

Skref 3: Setjið upp formúlu :math:`e^{tA}` með því að nota
brúunarmargliðuna :math:`r(z)`.

Skref 3: Ef beðið er um :math:`e^{tA}` þá reiknið þið upp úr formúlunni, en ef bara þarf að finna lausnina :math:`u` þá þarf ekki að reikna upp úr formúlunni fyrir :math:`e^{tA}` heldur er nóg að stilla upp formúlunni með fylkjum og svo margfalda í gegn með vigrinum þannig að maður margfaldar aldrei saman tvö fylki heldur er alltaf að margfalda fylki og vigur.
