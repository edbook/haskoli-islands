Línulegar afleiðujöfnur
=======================

*This,’ whispered the Doctor to Romana, ‘is going to be like trying to find a book about needles in a room full of books about haystacks.*

\- The Doctor, Doctor Who

Línulegar afleiðujöfnur
-----------------------

Athugasemd
~~~~~~~~~~

.. admonition:: Athugasemd
	:class: athugasemd

	Umfjöllun á þessu efni verður skýrari ef við leyfum
	föllunum sem fengist er við að taka ekki bara rauntölugildi heldur líka
	tvinntölugildi. Fastar og stuðlar sem koma fyrir geta því verið
	tvinntölur og þurfa ekki að vera rauntölur. Breytistæðirnar i föllunum,
	oftast táknaðar með :math:`t` eða :math:`x`, eru hinsvegar alltaf
	rauntölur.



Skilgreining (Sjá §7.1)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Afleiðujafna af gerðinni

	.. math::

	 a_m(t)u^{(m)}+a_{m-1}(t)u^{(m-1)}+\cdots+a_1(t)u'+a_0(t)u=f(t),

	þar sem föllin :math:`a_0,\dots,a_m,f` eru skilgreind á bili :math:`I\subset \mathbb{R}`, er sögð vera línuleg afleiðujafna. Við segjum að jafnan sé óhliðruð ef :math:`f` er núllfallið, annars er sagt að hún sé hliðruð.

	Fyrir sérhvern punkt :math:`t\in I` fæst margliða í einni breytistærð :math:`\lambda`

	.. math::

	   P(t,\lambda)= a_m(t)\lambda^{m}+a_{m-1}(t)\lambda^{m-1}+
	   \cdots+a_1(t)\lambda+a_0(t),

	sem er kölluð kennimargliða jöfnunnar.



Skilgreining og setning (Sjá §7.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`a_0(t), \ldots, a_m(t)` vera samfelld föll sem eru öll skilgreind á bili :math:`I`. Rifjum upp að mengi samfelldra falla sem eru skilgreind á :math:`I` er táknað :math:`C(I)` og mengi falla á :math:`I` sem eru :math:`m`-sinnum diffranleg með samfellda :math:`m`-tu afleiðu er táknað :math:`C^m(I)`. Skilgreinum afleiðuvirkja :math:`L:C^m(I)\to C(I)` þannig að fyrir fall :math:`u(t)\in C^m(I)` er

	.. math::

	   Lu(t)=a_m(t)u^{(m)}(t)+a_{m-1}(t)u^{(m-1)}(t)+\cdots+a_1(t)u'(t)+
	   a_0(t)u(t).

	Þegar mengin :math:`C(I)` og :math:`C^m(I)` eru skoðuð sem vigurrúm yfir :math:`{\mathbb{C}}` þá er vörpunin :math:`L` línuleg.



Skilgreining (Sjá §7.1)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Skilgreinum virkja :math:`D:C^1(I)\to C(I)` þar sem :math:`I` er bil þannig að :math:`Du=u'`. Látum :math:`a_0(t), \ldots, a_m(t)` vera samfelld föll sem eru öll skilgreind á bili :math:`I` og setjum

	.. math::

	   P(t,D)= a_m(t)D^{m}+a_{m-1}(t)D^{m-1}+
	   \cdots+a_1(t)D+a_0(t).

	Ef :math:`L` er afleiðuvirkinn sem er skilgreindur hér að ofan þá er :math:`Lu=P(t,D)u` fyrir öll föll :math:`u\in C^m(I)`.



Setning (Sjá §7.1)
~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Kjarni eða núllrúm virkjans :math:`P(t,D)` samanstendur af öllum lausnum :math:`u` á óhliðruðu jöfnunni :math:`P(t,D)u=0`. Fyrst :math:`P(t,D)` er línulegur virki, þá er núllrúmið vigurrúm yfir tvinntölurnar. Við táknum það með :math:`{\cal N}(P(t,D))`.

Fylgisetning (Sjá Setningu 7.1.3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Fylgisetning
	:class: setning

	Látum :math:`a_0(t), \ldots, a_m(t)` vera samfelld föll sem eru öll skilgreind á bili :math:`I`. Gerum ráð fyrir að :math:`a_m(t)\neq 0` fyrir öll :math:`t\in I`. Til eru föll :math:`u_1, \ldots, u_m` skilgreind á :math:`I` þannig að sérhverja lausn á afleiðujöfnunni

	.. math::

	 a_m(t)u^{(m)}+a_{m-1}(t)u^{(m-1)}+\cdots+a_1(t)u'+a_0(t)u=0,

	má rita sem :math:`u=c_1u_1+\cdots+c_mu_m` þar sem :math:`c_1, \ldots, c_m` eru fastar. Föllin :math:`u_1, \ldots, u_m` mynda grunn fyrir núllrúm virkjans :math:`P(t,D)`.



Fylgisetning (Sjá Setningu 7.1.4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Fylgisetning
	:class: setning

	Látum :math:`a_0(t), \ldots, a_m(t), f(t)` vera samfelld föll sem eru öll skilgreind á bili :math:`I`. Ef :math:`v(t)` er einhver ein lausn (,,sérlausn‘‘) afleiðujöfnunnar

	.. math::

	 a_m(t)u^{(m)}+a_{m-1}(t)u^{(m-1)}+\cdots+a_1(t)u'+a_0(t)u=f(t),

	þá má rita sérhverja lausn sem :math:`u=c_1u_1+\cdots+c_mu_m+v` þar sem :math:`c_1, \ldots, c_m` eru fastar og föllin :math:`u_1, \ldots, u_m` mynda grunn fyrir núllrúm virkjans :math:`P(t,D)`.

	Línulega samantektin :math:`c_1u_1+\cdots+c_mu_m` gefur almenna lausnarformúlu fyrir afleiðujöfnuna

	.. math::

	 a_m(t)u^{(m)}+a_{m-1}(t)u^{(m-1)}+\cdots+a_1(t)u'+a_0(t)u=0.

	Sérhverja lausn má því rita sem (lausn óhliðraðar)+(ákveðin sérlausn).




Skilgreining  (Sjá §7.2)
~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Afleiðujafna á forminu

	.. math::

	 a_mu^{(m)}+\cdots + a_1u'+a_0u=f(t)

	þar sem :math:`a_0, a_1, \ldots, a_m` eru fastar kallast línuleg :math:`m`-ta stigs afleiðujafna með fastastuðla. Kennimargliða hennar er

	.. math::

	 P(\lambda)=a_m\lambda^{m}+\cdots + a_1\lambda+a_0.



Setning (Sjá Setningu 7.2.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Gerum ráð fyrir að :math:`P(D)` sé línulegur afleiðuvirki af :math:`m` með fastastuðla og að kennimargliðan :math:`P(\lambda)` hafi :math:`\ell` ólíkar núllstöðvar :math:`\lambda_1,\dots,\lambda_\ell\in {\mathbb{C}}` með margfeldnina :math:`m_1,\dots,m_\ell`. Þá mynda föllin

	.. math::

	   \begin{gathered}
	   e^{\lambda_1t}, te^{\lambda_1t},\dots, t^{m_1-1}e^{\lambda_1t},\\
	   e^{\lambda_2t}, te^{\lambda_2t},\dots, t^{m_2-1}e^{\lambda_2t},\\
	   \quad \vdots\qquad \vdots \qquad \qquad \vdots\\
	   e^{\lambda_\ell t}, te^{\lambda_\ell t},\dots, t^{m_\ell-1}e^{\lambda_\ell t},\end{gathered}

	grunn í núllrúmi virkjans :math:`P(D)` og sérhvert stak í núllrúminu má rita sem

	.. math::

	 q_1(t)e^{\lambda_1t}+\cdots+q_\ell(t)e^{\lambda_\ell t},

	þar sem :math:`q_j` eru margliður af stigi :math:`<m_j`,
	:math:`1\leq j\leq \ell`.

Athugasemd
~~~~~~~~~~

.. admonition:: Athugasemd
	:class: athugasemd

	Látum :math:`a_0, \ldots, a_m` vera rauntölur. Viljum
	finna raungildar lausnir

	.. math::

	 a_nu^{(n)}+\cdots+a_1u'+a_0u=0.

	Hugsum okkur að :math:`\lambda=\alpha+i\beta` sé :math:`m`-föld rót kennimargliðu afleiðujöfnunar. Þá er :math:`\mu=\overline{\lambda}=\alpha-i\beta` líka :math:`m`-föld rót kennijöfnu. Þegar grunnur fyrir lausnarúmið er skrifaður má í stað

	.. math::

	   e^{\lambda t}, te^{\lambda t},\dots, t^{m-1}e^{\lambda t},
	   e^{\mu t}, te^{\mu t},\dots, t^{m-1}e^{\mu t}

	hafa í grunninum raungildu föllin

	.. math::

	   e^{\alpha t}\cos(\beta t), te^{\alpha t}\cos(\beta t), \ldots,
	   t^{m-1}e^{\alpha t}\cos(\beta t), e^{\alpha t}\sin(\beta t),
	   te^{\alpha t}\sin(\beta t), \ldots, t^{m-1}e^{\alpha t}\sin(\beta t).



Skilgreining (Sjá §7.3)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Afleiðujafna af gerðinni

	.. math::

	 a_mx^mu^{(m)}+\cdots+a_1xu'+a_0u=0,

	þar sem stuðlarnir :math:`a_0,\ldots, a_m` eru tvinntölur, kallast :math:`m`-ta stigs Euler-jafna (sumsstaðar kallaðar Cauchy-Euler jöfnur).



Setning (Sjá Setningu 7.3.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Gefin er afleiðujafna

	.. math::

	 a_mx^mu^{(m)}+\cdots+a_1xu'+a_0u=0,

	Skilgreinum margliðu

	.. math::

	 Q(r)=a_m r(r-1)\cdots(r-m+1)+\cdots+a_1r+a_0.

	Almenn lausn afleiðujöfnunnar á jákvæða raunásnum er línuleg samantekt fallanna

	.. math::

	   \begin{gathered}
	   x^{r_1}, \big(\ln x \big) x^{r_1}, \dots,
	   \big(\ln x\big)^{m_1-1}x^{r_1},\\
	   x^{r_2}, \big(\ln x\big)x^{r_2}, \dots,
	   \big(\ln x \big)^{m_2-1} x^{r_2},\\
	   \vdots \qquad \qquad \qquad \vdots \qquad \qquad \qquad \vdots\\
	   x^{r_\ell}, \big(\ln x \big)x^{r_\ell}, \dots,
	   \big(\ln x\big)^{m_\ell-1} x^{r_\ell},\end{gathered}

	þar sem :math:`r_1,\dots,r_\ell` eru ólíkar núllstöðvar margliðunnar :math:`Q` með margfeldni :math:`m_1,\dots,m_\ell`.



Athugasemd
~~~~~~~~~~

.. admonition:: Athugasemd
	:class: athugasemd

	Gerum nú ráð fyrir að :math:`a_0, \ldots, a_m` séu rauntölur. Hugsum okkur að :math:`\lambda=\alpha+i\beta` sé :math:`m`-föld rót margliðunni :math:`Q(r)`. Þá er :math:`\mu=\overline{\lambda}=\alpha-i\beta` líka :math:`m`-föld rót :math:`Q(r)`. Þegar grunnur fyrir lausnarúmið er skrifaður má í stað

	.. math::

	   x^{\lambda}, (\ln x)x^{\lambda},\dots, (ln x)^{m-1}x^{\lambda},
	   x^{\mu}, (\ln x)x^{\mu},\dots, (\ln x)^{m-1}x^{\mu}

	hafa í grunninum raungildu föllin

	.. math::

	   x^{\alpha}\cos(\ln(\beta x)), (\ln x)x^{\alpha}\cos(\ln(\beta x)), \ldots,
	   (\ln x)^{m-1}x^{\alpha}\cos(\ln(\beta x)),

	.. math::

	   x^{\alpha}\sin(\ln(\beta x)),
	   (\ln x)x^{\alpha t}\sin(\ln(\beta x)), \ldots, (\ln x)^{m-1}x^{\alpha}\sin(\ln(\beta x)).

Sérlausnir og Green-föll
------------------------

Upprifjun
~~~~~~~~~

Viljum leysa afleiðujöfnu af taginu

.. math::

 a_m(t)u^{(m)}+a_{m-1}(t)u^{(m-1)}+\cdots+a_1(t)u'+a_0(t)u=f(t).

Fyrst er að finna grunn fyrir lausnarúm óhliðruðu jöfnunnar

.. math::

 a_m(t)u^{(m)}+a_{m-1}(t)u^{(m-1)}+\cdots+a_1(t)u'+a_0(t)u=0.

Svo finnum við einhverja eina lausn (,,sérlausn‘‘)

.. math::

 a_m(t)u^{(m)}+a_{m-1}(t)u^{(m-1)}+\cdots+a_1(t)u'+a_0(t)u=f(t).

Þá getum við lýst öllum lausnum afleiðujöfnunnar.

Það að finna sérlausnina getur verið erfitt.



Ágiskun (Sjá §7.4)
~~~~~~~~~~~~~~~~~~

Giskum á sérlausn sem er fall af ,,sömu gerð‘‘ og fallið :math:`f(t)`, nema hvað ekki settar inn ákveðnar tölur fyrir stuðla sem koma fyrir. Stungið inn í jöfnu og reynt að ákvarða stuðla.



Góðar ágiskanir
~~~~~~~~~~~~~~~

Höfum línulega afleiðujöfnu með fastastuðlum

.. math::

 a_mu^{(m)}+a_{m-1}u^{(m-1)}+\cdots+a_1u'+a_0u=f(t).

Látum :math:`P_n(t)` standa fyrir einhverja :math:`n`-ta stigs margliðu og látum :math:`A_n(t)` og :math:`B_n(t)` tákna :math:`n`-ta stigs margliður með óákveðnum stuðlum.

Ef :math:`f(t)=P_n(t)` þá giskað á :math:`u_{\rm p}(t)=t^lA_n(t)`.

Ef :math:`f(t)=P_n(t)e^{rt}` þá giskað á :math:`u_{\rm p}(t)=t^lA_n(t)e^{rt}`.

Ef :math:`f(t)=P_n(t)e^{rt}\sin(kt)` þá giskað á :math:`u_{\rm p}(t)=t^le^{rt}[A_n(t)\cos(kt)+B_n(t)\sin(kt)]`.

Ef :math:`f(t)=P_n(t)e^{rt}\cos(kt)` þá giskað á :math:`u_{\rm p}(t)=t^le^{rt}[A_n(t)\cos(kt)+B_n(t)\sin(kt)]`.

Hér táknar :math:`l` minnstu töluna af tölunum :math:`0, 1, \ldots, m-1` sem tryggir að enginn liður í ágiskuninni sé lausn á óhliðruðu jöfnunni :math:`a_mu^{(m)}+a_{m-1}u^{(m-1)}+\cdots+a_1u'+a_0u=0`.

Dæmi - Deyfð sveifla með drifkrafti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lítum á diffurjöfnuna :math:`mx''+cx'+kx=A\cos(\omega t)`.




.. ggb:: sexg37mt
  :width: 700
  :height: 400
  :img: polarggb.png
  :imgwidth: 4cm
  :zoom_drag: true


Sérlausnir fundnar með virkjareikningi (Sjá §7.4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aðferðin snýst um að nýta sér ákveðin mynstur sem koma upp þegar línulegum afleiðuvirkja með fastastuðla er beitt á ákveðnar gerðir falla. Lykilformúlur eru:

.. math::

 P(D)e^{\alpha t}=P(\alpha)e^{\alpha t}.

.. math::

   (D-\alpha)v(t)e^{\alpha t}=v'(t)e^{\alpha t}\quad\mbox{og
     almennar}\quad (D-\alpha)^kv(t)  e^{\alpha t}=v^{(k)}(t)e^{\alpha
     t},

.. math::

   \mbox{ef } P(D)=Q(D)(D-\alpha)^k\mbox{ þá }
   P(D)\frac{t^ke^{\alpha t}}{k!Q(\alpha)}=e^{\alpha t}.



Hjálparsetning (Sjá Hjálparsetningu 7.5.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Hjálparsetning
	:class: hjálparsetning

	Ef :math:`I` er bil á raunásnum, :math:`a\in I`, :math:`f\in C(I)` og :math:`g\in C(I\times I)`, er samfellt deildanlegt fall af fyrri breytistærðinni, þ.e. \ :math:`{\partial}_tg\in C(I\times I)`, þá er fallið :math:`h`, sem gefið er með formúlunni

	.. math::

	 h(t)=\int_a^t g(t, \tau)f(\tau) \, d\tau, \qquad t\in I,

	í :math:`C^1(I)` og afleiða þess er

	.. math::

	   h'(t)=g(t,t)f(t)+\int_a^t \partial_tg(t,\tau)f(\tau) \, d\tau,
	   \qquad t\in I.



Skilgreining og umræða (Sjá §7.5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Skoðum afleiðujöfnu

	.. math::

	 P(t,D)u=\big(a_m(t)D^m+\cdots+a_1(t)D+a_0(t)\big)u=f(t)

	þar sem föllin :math:`a_0(t),\dots,a_m(t),f(t)` eru í :math:`C(I)` og :math:`a_m(t)\neq 0` fyrir öll :math:`t\in I`.

	Samkvæmt `Fylgisetningu 6.3.6. <./Kafli06.html#fylgisetning-sja-fylgisetningu-6-6-7>`_  gildir fyrir sérhvern punkt :math:`\tau\in I` að til er ótvírætt ákvörðuð lausn

	:math:`u_\tau` á upphafsgildisverkefninu :math:`P(t,D)u=0` þannig að

	.. math::

	   u_\tau(\tau)=u_\tau'(\tau)=\cdots=u_\tau^{(m-2)}(\tau)=0\qquad\mbox{og}\qquad
	   u_\tau^{(m-1)}(\tau)=1/a_m(\tau).

	Skilgreinum Green-fall virkjans :math:`P(t, D)` sem fallið
	:math:`G(t,\tau)` þannig að fyrir öll :math:`t,\tau\in I` er
	:math:`G(t,\tau)=u_\tau(t)`.



Setning (Sjá §7.5)
~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Um Green-fall línulegs afleiðuvirkja

	.. math::

	 P(t,D)=a_m(t)D^m+\cdots+a_1(t)D+a_0(t)

	þar sem föllin :math:`a_0(t),\dots,a_m(t),f(t)` eru í :math:`C(I)` og :math:`a_m(t)\neq 0` fyrir öll :math:`t\in I` gildir:

	.. math::

	 P(t,D_t)G(t,\tau)=0,  \qquad \mbox{fyrir öll }t,\tau\in I,\label{2.5.2}

	.. math::

	   \begin{gathered}
	   G(\tau,\tau)=\partial_tG(\tau,\tau)=\cdots=
	   \partial_t^{(m-2)}G(\tau,\tau)=0,\\
	   \partial_t^{(m-1)}G(\tau,\tau)=1/a_m({\tau})\label{2.5.3}.
	   \end{gathered}

	Green-fallið ákvarðast ótvírætt af þessum skilyrðum.

	Fallið :math:`G(t,\tau)` er :math:`m`-sinnum samfellt deildanlegt fall af :math:`t` fyrir sérhvert :math:`\tau\in I` og :math:`\partial_t^jG\in C(I\times I)` fyrir :math:`j=0,\dots,m`.

Setning (Sjá Setningu 7.5.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`P(t,D)` vera línulegan afleiðuvirkja á forminu

	.. math::

	 P(t,D)u=(a_m(t)D^m+\cdots+a_1(t)D+a_0(t))u

	þar sem föllin :math:`a_0(t),\dots,a_m(t),f(t)` eru í :math:`C(I)` og :math:`a_m(t)\neq 0` fyrir öll :math:`t\in I`.

	Ef :math:`a` er einhver punktur í :math:`I` þá hefur upphafsgildisverkefnið

	.. math::

	 P(t,D)u=f(t),

	með

	.. math::

	 u(a)=u'(a)=\cdots=u^{(m-1)}(a)=0,

	ótvírætt ákvarðaða lausn :math:`u_p\in C^m(I)` sem gefin er með formúlunni

	.. math::

	 u_p(t) = \int_a^t G(t,\tau)f(\tau) \, d\tau, \qquad t\in I,

	og :math:`G(t,\tau)` er Green-fall virkjans :math:`P(t, D)`.



Fylgisetning (Sjá Fylgisetningu 7.5.4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Fylgisetning
	:class: setning

	Gerum ráð fyrir að :math:`P(D)=a_mD^m+\cdots+a_1D+a_0` sé línulegur afleiðuvirki með fastastuðla. Látum :math:`g\in C^{\infty}(\mathbb{R})` vera fallið sem uppfyllir

	.. math::

	   P(D)g=0,\  \text{með }
	   g(0)=g'(0)=\cdots=g^{(m-2)}(0)=0,\mbox{ og }
	   g^{(m-1)}(0)=1/a_m.

	Þá er :math:`G(t,\tau)=g(t-\tau)` Green-fall virkjans :math:`P(D)`.

Green-föll og Wronski-ákveður
-----------------------------

Reikniaðferð
~~~~~~~~~~~~

Finna skal Green-fall :math:`G(t,\tau)` fyrir :math:`m`-ta stigs línulegan afleiðuvirkja :math:`P(t,D)`.

--------------------

(A) Stuðlar afleiðuvirkjans eru fastar, þ.e.a.s. \ :math:`P(D)=a_mD^m+\cdots+a_1D+a_0`.

Fyrst er fundinn grunnur :math:`u_1(t), \ldots, u_m(t)` fyrir lausnarúm jöfnunnar :math:`P(D)u=0`. Almenna lausnin er á á forminu

.. math::

 u=c_1u_1+\cdots+c_mu_m,

þar sem :math:`c_1, \ldots, c_m` eru fastar.

Næst er fundin ein ákveðin lausn :math:`g(t)` á jöfnunni :math:`P(D)u=0` sem uppfyllir skilyrðin :math:`g(0)=\cdots=g^{(m-2)}(0)=0` og :math:`g^{(m-1)}(0)=1/a_m`.

Green-fallið er svo gefið með formúlunni :math:`G(t,\tau)=g(t-\tau)`.

--------------------

(B) Stuðlar í :math:`P(t,D)` eru föll :math:`a_0(t), \ldots, a_m(t)` skilgreind á bili :math:`I` þannig að

.. math::
    P(t,D)=a_m(t)D^m+\cdots+a_1(t)D+a_0(t).

Fyrst er fundinn grunnur :math:`u_1(t), \ldots, u_m(t)` fyrir lausnarúm :math:`P(t,D)u=0`. Almenna lausnin er á forminu

.. math::



 u=c_1u_1+\cdots+c_mu_m,

þar sem :math:`c_1, \ldots, c_m` eru fastar.

Svo finnum við fyrir almennan punkt :math:`\tau\in I` gildi á fastana :math:`c_1(\tau), \ldots, c_m(\tau)` þannig að um lausnina :math:`u_\tau(t)= c_1(\tau)u_1(t)+\cdots+c_m(\tau)u_m(t)` á :math:`P(t,D)u=0` gildi að

.. math::

   u_\tau(\tau)=u_\tau'(\tau)=\cdots=u_\tau^{(m-2)}(\tau)=0\qquad\mbox{og}\qquad
   u_\tau^{(m-1)}(\tau)=1/a_m(\tau).

Green-fallið er þá gefið með formúlunni :math:`G(t,\tau)=u_\tau(t)`.



Skilgreining (Sjá §7.6)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Látum :math:`u_1, \ldots, u_m` vera vera :math:`(m-1)`-sinni deildanleg föll skilgreind á bili I. Wronski-fylki fallanna :math:`u_1, u_2, \ldots, u_m` er skilgreint sem fylkið

	.. math::

	   V(u_1, u_2, \ldots, u_m)=\begin{bmatrix}
	   u_1(t)&u_2(t)&\cdots&u_m(t)\\
	   u_1'(t)&u_2'(t)&\cdots&u_m'(t)\\
	   \vdots&\vdots&\dots&\vdots\\
	   u_1^{(m-1)}(t)&u_2^{(m-1)}(t)&\cdots&u_m^{(m-1)}(t)
	   \end{bmatrix}.

	Ákveða þessa fylkis er kölluð Wronski-ákveða fallanna :math:`u_1, u_2, \ldots, u_m`.

	.. attention::

	    Stuðlarnir í Wronski-fylkinu eru föll af breytunni :math:`t` og sömuleiðis er Wronski-ákveðan fall af breytunni :math:`t`.



Setning (Sjá Setningu 7.6.3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`P(t,D)=a_m(t)D^m+\cdots+a_1(t)D+a_0(t)` vera afleiðuvirkja með samfellda stuðla, :math:`u_1,\dots,u_m` vera lausnir á óhliðruðu jöfnunni :math:`P(t,D)u=0` og táknum Wronski-ákveðu þeirra með :math:`W(t)`. Þá uppfyllir :math:`W` fyrsta stigs afleiðujöfnuna

	.. math::

	 a_m(t) W'+a_{m-1}(t)W=0

	og þar með gildir formúlan

	.. math::

	   W(t)=W(a)\exp\bigg(-\int_a^t\dfrac{a_{m-1}(\tau)}{a_m(\tau)}\,
	   d\tau\bigg)

	fyrir öll :math:`a` og :math:`t` á bili :math:`J` þar sem :math:`a_m` er núllstöðvalaust.



Setning (Sjá Setningu 7.6.3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`u_1,\dots,u_m` vera lausnir á óhliðruðu jöfnunni :math:`P(t,D)u=0`, þar sem

	.. math::
	    P(t,D)=a_m(t)D^m \cdots+a_1(t)D+a_0(t)

	og föllin :math:`a_0(t), \ldots, a_m(t)` eru skilgreind og samfelld á bili :math:`I` og við gerum ráð fyrir að :math:`a_m` sé núllstöðvalaust á opnu bili :math:`J\subseteq I`. Þá eru eftirfarandi skilyrði jafngild:

	(i) Föllin :math:`u_1,\dots,u_m` eru línulega óháð á bilinu :math:`J`.

	(ii) :math:`W(u_1,\dots,u_m)(t)\neq 0` fyrir sérhvert :math:`t\in J`.

	(iii) :math:`W(u_1,\dots,u_m)(a)\neq 0` fyrir eitthvert :math:`a\in J`.



Setning (Sjá Setningu 7.6.4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`P(t,D)=a_m(t)D^m+\cdots+a_1(t)D+a_0(t)` vera afleiðuvirkja með stuðla sem eru samfelld föll skilgreind á bili :math:`I` og :math:`u_1,\dots,u_m` vera grunn í :math:`{\cal N}(P(t,D))`. Green-fall virkjans er gefið með formúlunni

	.. math::

	 G(t,\tau)=c_1(\tau)u_1(t)+\cdots+c_m(\tau)u_m(t), \qquad t,\tau\in I,

	þar sem vigurinn :math:`a_m({\tau})(c_1(\tau),\dots,c_m(\tau))` myndar aftasta dálkinn í andhverfu Wronski-fylkisins :math:`V(u_1,\dots,u_m)(\tau)`,

	.. math::

	   c_j(\tau)=(-1)^{m+j} \dfrac{\det V_{mj}(u_1,\dots,u_m)(\tau)}
	   {a_m({\tau})W(u_1,\dots, u_m)(\tau)},

	þar sem :math:`V_{mj}(u_1,\dots,u_m)(\tau)` táknar :math:`(m-1)\times (m-1)` fylkið sem fæst með því að fella niður neðstu línuna og dálk númer :math:`j` í :math:`V(u_1,\dots,u_m)(\tau)`.


Fylgisetning (Er hluti af Setningu 7.6.4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Fylgisetning
	:class: setning

	Sérlausn á afleiðujöfnunni :math:`P(t,D)u=f(t)` er gefin með formúlunni

	.. math::

	 u_p(t)=v_1(t)u_1(t)+\cdots+v_m(t)u_m(t), \qquad  t\in I,

	þar sem stuðlaföllin :math:`v_j` eru gefin með formúlunni

	.. math::

	 v_j(t)=\int_a^t c_j(\tau)f(\tau) \, d\tau.


Fylgisetning (Sjá Fylgisetning 7.6.5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Fylgisetning
	:class: setning

	Látum :math:`P(t,D)=a_2(t)D^2+a_1(t)D+a_0(t)` vera annars stigs afleiðuvirkja á bilinu :math:`I` með samfellda stuðla og :math:`a_2(t)\neq 0` fyrir öll :math:`t\in I`. Gerum nú ráð fyrir að :math:`u_1` og :math:`u_2` séu línulega óháðar lausnir á óhliðruðu jöfnunni :math:`P(t,D)u=0`. Þá er

	.. math::

	   G(t,\tau)
	   =a_2(\tau)^{-1}
	   \left|\begin{matrix}
	   u_1(\tau) & u_1(t)\\
	   u_2(\tau) & u_2(t)
	   \end{matrix}\right|\bigg /
	   \left|\begin{matrix}
	   u_1(\tau) & u_2({\tau})\\
	   u_1'(\tau) & u_2'({\tau})
	   \end{matrix}\right|.
