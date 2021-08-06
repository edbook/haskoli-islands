Undirstöðuatriði um afleiðujöfnur
=================================

*I love humans. Always seeing patterns in things that aren’t there.”*

\- The Doctor, Doctor Who


Afleiðujöfnur
-------------

Skilgreining (Sjá §6.1)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Venjuleg afleiðujafna (eða bara afleiðujafna eða diffurjafna) er jafna sem lýsir sambandinu á milli gilda falls af einni breytistærð og gilda afleiðu þess.


Uppsetning (Sjá §6.1)
~~~~~~~~~~~~~~~~~~~~~

Sérhverja afleiðujöfnu má rita á forminu

.. math::

 F(t,u,u',u'',\dots,u^{(m)})=0

þar sem við hugsum okkur að :math:`t` sé breytistærð, sem tekur gildi í einhverju hlutmengi :math:`A` af :math:`\mathbb{R}` og að :math:`u` sé óþekkt fall sem skilgreint er á :math:`A` og tekur gildi í :math:`\mathbb{R}`, :math:`{\mathbb{C}}` eða jafnvel :math:`\mathbb{R}^m`.

Lausn á afleiðujöfnunni er fall :math:`u` skilgreint á opnu bili :math:`I` í :math:`A` þannig að fyrir öll :math:`t\in  I` er

.. math::

 F(t,u(t),u'(t),u''(t),\dots,u^{(m)}(t))=0.



Skilgreining (Sjá §6.1)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Stig afleiðujöfnu er hæsta stig á afleiðu, sem kemur fyrir í jöfnunni. Við segjum að :math:`m`-ta stigs afleiðujafna sé á staðalformi þegar hún hefur verið umrituð yfir í jafngilda jöfnu af taginu

	.. math::

	 u^{(m)}=G(t,u,u',\dots,u^{(m-1)}).



Grundvallarspurningar
~~~~~~~~~~~~~~~~~~~~~~

Ef gefin er afleiðujafna er þá endilega til lausn?

Er hægt að finna lausn sem uppfyllir tiltekin viðbótarskilyrði, t.d. lausn :math:`u` þannig að :math:`u(a)=b`?

Ef til er lausn er hún þá ótvírætt ákvörðuð? Hvernig viðbótarskilyrðum þarf að bæta við til að fá ótvírætt ákvarðaða lausn?

Hvernig finnur maður lausn?

Ef maður getur ekki fundið beina formúlu fyrir lausn er samt hægt að
álykta eitthvað um eiginleika lausnar?



Skilgreining (Sjá §6.1)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Afleiðujafna af gerðinni

	.. math::

	   a_m(t)u^{(m)}+a_{m-1}(t)u^{(m-1)}+\cdots+a_0(t)u
	    =f(t),

	þar sem föllin :math:`a_0,\dots,a_m,f` eru skilgreind á bili :math:`I\subset \mathbb{R}`, er sögð vera línuleg. Línuleg afleiðujafna er sögð óhliðruð ef fallið :math:`f(t)` í hægri hlið er fastafallið 0 en hliðruð annars.


Skilgreining (Sjá §6.3)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Afleiðujöfnuhneppi (nákvæmar, venjulegt afleiðujöfnuhneppi) er safn af jöfnum sem lýsa sambandi milli gilda óþekktra falla :math:`u_1, \ldots, u_k` af einni breytistærð og gilda á einstökum afleiðum þeirra. Venjulegt afleiðujöfnuhneppi er alltaf hægt að umrita yfir í jöfnur af gerðinni

	.. math::

	   F_j(t,u_1,\dots,u_k,u_1',\dots,u_k',\dots,
	   u_1^{(m)},\dots,u_k^{(m)})=0,\qquad
	   j=1,\dots,l,

	þar sem :math:`t` táknar breytistærðina, :math:`u_1,\dots,u_k` eru óþekktu föllin og föllin :math:`F_1,\dots,F_l` taka gildi í :math:`\mathbb{R}` eða :math:`{\mathbb{C}}`. Til þess að einfalda ritháttinn, þá skilgreinum við vigurgildu föllin :math:`u=(u_1,\dots,u_k)` og :math:`F=(F_1,\dots,F_l)`. Þá eru jöfnurnar hér að ofan jafngildar vigurjöfnunni

	.. math::
	    F(t,u,u',\dots,u^{(m)})=0.

	Lausn jöfnunnar er vigurfall :math:`u=(u_1,\dots,u_k)` þar sem föllin :math:`u_1, \cdots, u_k` eru öll skilgreind á opnu bili :math:`I`, þannig að vigurinn :math:`u(t)` er í skilgreiningarmengi fallsins :math:`F` fyrir öll :math:`t\in I` og uppfyllir jöfnuna.

	Stig afleiðujöfnuhneppis er skilgreint sem hæsta stig á afleiðu sem
	kemur fyrir í jöfnunni.



Skilgreining (Sjá §6.3)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Við segjum að hneppið sé á staðalformi, ef fjöldi jafna og fjöldi óþekktra falla er sá sami og það má rita á forminu

	.. math::

	   \begin{aligned}
	   u_1'&= G_1(t, u_1,\dots, u_m),\\
	   u_2'&= G_2(t, u_1,\dots, u_m),\\
	   &\quad \vdots\\
	   u_m'&= G_m(t, u_1,\dots, u_m),\end{aligned}

Skilgreining (Sjá §6.3)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Við segjum að fyrsta stigs afleiðujöfnuhneppi sé línulegt ef það má rita á forminu

	.. math::

	   \begin{aligned}
	   u_1'&=a_{11}(t)u_1+\cdots+a_{1m}(t)u_m+f_1(t),\\
	   u_2'&=a_{21}(t)u_1+\cdots+a_{2m}(t)u_m+f_2(t),\\
	   &\qquad \qquad \vdots\qquad \qquad \qquad \qquad \vdots\\
	   u_m'&=a_{m1}(t)u_1+\cdots+a_{mm}(t)u_m+f_m(t).\end{aligned}

	Við segjum að hneppið sé óhliðrað ef :math:`f_i` er núllfallið fyrir öll :math:`i` og við segjum að það sé hliðrað annars.

Setning (Sjá §6.3)
~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Sérhverja venjulega afleiðujöfnu á staðalformi

	.. math::

	 v^{(m)}=G(t,v,v',\dots,v^{(m-1)})

	má umrita sem jafngilt afleiðujöfnuhneppi (lausnir afleiðujöfnunnar gefa lausnir á hneppinu og öfugt) sem er fundið þannig að við setjum

	.. math::

	 u_1=v, \qquad u_2=u_1', \quad \ldots\quad u_m=v^{(m-1)},

	og jöfnuhneppið er

	.. math::

	   \begin{aligned}
	   u_1'&=u_2\\
	   u_2'&=u_3\\
	   &\ \,\vdots\\
	   u_m'&=G(t,u_1,u_2,\dots,u_m).\end{aligned}

Skilgreining (Sjá §6.4)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Upphafsgildisverkefni snúast um að leysa afleiðujöfnu eða afleiðujöfnuhneppi með því hliðarskilyrði að lausnin og einhverjar afleiður hennar taki fyrirfram gefin gildi í ákveðnum punkti.


Upphafsgildisverkefni fyrir línulega afleiðujöfnu (Sjá §6.4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upphafsgildisverkefni fyrir línulega :math:`m`-ta stigs afleiðujöfnu er sett fram sem

.. math::

   \begin{cases} a_m(t)v^{(m)}+\cdots+a_1(t)v'+a_0(t)v=g(t), & t\in I,\\
   v(a)=b_0, \quad v'(a)=b_1, \quad \dots \quad  v^{(m-1)}(a)=b_{m-1}.&
   \end{cases}

Það að leysa upphafgildis verkefnið felst í því að finna lausn :math:`v` á afleiðujöfnunni sem uppfyllir skilyrðin um gildi á :math:`v(a),\ldots, v^{(m-1)}(a)`.


Skilgreining (Sjá §6.5)
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Jaðargildisverkefni snúast um að leysa afleiðujöfnu

	.. math::

	 u^{(m)}=f(t,u,u',\dots,u^{(m-1)})

	af stigi :math:`m` á takmörkuðu bili :math:`I=[a,b]` með skilyrðum á einhver gildanna (ekki endilega öll)

	.. math::

	   u(a), \ u'(a),\dots,  \ u^{(m-1)}(a)\qquad \text{ og }
	   \qquad  u(b), \ u(b),\dots, \ u^{(m-1)}(b).



Útfærsla jaðargildisverkefna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skilyrði eru venjulega sett fram þannig að ákveðnar línulegar samantektir af þessum fallgildum og afleiðum eigi að taka fyrirfram gefin gildi. Fyrir annars stigs jöfnu geta jaðarskilyrðin til dæmis verið

.. math::

 u(a)=0, \qquad u'(b)=0.

Lotubundin jaðarskilyrði eru af gerðinni

.. math::

 u(a)=u(b), \qquad u'(a)=u'(b).



Skilgreining
~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Hlutafleiðujafna er jafna sem lýsir sambandinu á milli gilda falls af fleiri en einni breytistærð og einstakra hlutafleiða þess.

Upprifjun á lausnaaðferðum og hagnýtingar
-----------------------------------------

Línulegar fyrsta stigs jöfnur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Almenna línulega fyrsta stigs afleiðujöfnu má rita á forminu

.. math::

 u'+p(t)u=q(t).

Skilgreinum :math:`\mu(t)=\int p(t)\,dt` (eitthvert stofnfall). Þá er

.. math::

 u(t)=e^{-\mu(t)}\int e^{\mu(t)}q(t)\,dt

lausn á afleiðujöfnunni. (Þegar þið reiknið :math:`\mu(t)=\int p(t)\,dt` þá megið þið sleppa heildunarfasta, en ekki þegar þið reiknið heildið :math:`\int e^{\mu(t)}q(t)\,dt`.)

Fyrsta stigs aðgreinanlegar afleiðujöfnur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fyrsta stigs afleiðujafna sem hægt er að rita á forminu

.. math::

 \frac{du}{dt}=f(t)g(u)

kallast aðgreinanleg (e. seperable). (Hægri hlið má þátta þannig að annar þátturinn er bara fall af :math:`t` og hinn þátturinn er bara fall af :math:`u`.)

Umritum jöfnuna yfir á formið

.. math::

 \frac{du}{g(u)}=f(t)\,dt.

(Ekkert :math:`t` í vinstri hlið, ekkert :math:`u` í hægri hlið.) Síðan smellum við heildum á báðar hliðar og fáum að

.. math::

 \int\frac{du}{g(u)}=\int f(t)\,dt.

Reiknum stofnföll og munum eftir að setja inn heildunarfasta (einn er nóg). Þá höfum við jöfnu sem tengir saman :math:`t` og :math:`u` og út frá þeirri jöfnu má fá upplýsingar um eiginleika lausnarinnar :math:`u`.

Stundum er hægt að einangra :math:`u` og fá þannig formúlu fyrir lausn afleiðujöfnunnar.


Annars stigs óhliðraðar línulegar afleiðujöfnur með fastastuðlum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finna á lausn á afleiðujöfnu :math:`au''+bu'+cu=0`. Kennijafna hennar er :math:`a\lambda^2+b\lambda+c=0`.

(i) Kennijafnan :math:`a\lambda^2+b\lambda+c=0` hefur tvær ólíkar rauntölulausnir :math:`\lambda_1` og :math:`\lambda_2`. Fallið

.. math::

 u(t)=Ae^{\lambda_1t}+Be^{\lambda_2t}

er alltaf lausn sama hvernig fastarnir :math:`A` og :math:`B` eru valdir og sérhverja lausn má rita á þessu formi.

(ii) Kennijafnan :math:`a\lambda^2+b\lambda+c=0` hefur bara eina rauntölulausn :math:`k=-\frac{b}{2a}`. Fallið

.. math::

 u(t)=Ae^{kt}+Bte^{kt}

er alltaf lausn sama hvernig fastarnir :math:`A` og :math:`B` eru valdir og sérhverja lausn má rita á þessu formi.

(iii) Kennijafnan :math:`a\lambda^2+b\lambda+c=0` hefur engar rauntölulausnir. Setjum :math:`k=-\frac{b}{2a}` og :math:`\omega=\frac{\sqrt{4ac-b^2}}{2a}`. Rætur kennijöfnunnar eru :math:`\lambda_1=k+i\omega` og :math:`\lambda_2=k-i\omega`. Fallið

.. math::

 u(t)=Ae^{kt}\cos(\omega t)+Be^{kt}\sin(\omega t)

er alltaf lausn sama hvernig fastarnir :math:`A` og :math:`B` eru
valdir og sérhverja lausn má rita á þessu formi.

Tilvist og ótvíræðni lausna
---------------------------

Setning Peano (Sjá Setningu 6.6.1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Gerum ráð fyrir að :math:`\Omega` sé grennd um punktinn :math:`(a,b)\in \mathbb{R}\times\mathbb{R}^m` og að :math:`f\in C(\Omega,\mathbb{R}^m)`. Þá er til opið bil :math:`I` sem inniheldur punktinn :math:`a` og fall :math:`u:I\to \mathbb{R}^m`, þannig að :math:`(t,u(t))\in \Omega`, :math:`u'(t)=f(t,u(t))` fyrir öll :math:`t\in I` og :math:`u(a)=b`.


Dæmi (Sjá Sýnidæmi 6.6.2)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
	:class: daemi

	Athugum upphafsgildisverkefnið :math:`u'=3u^{2/3}`, :math:`u(0)=0`. Fyrir sérhvert :math:`\alpha>0` fáum við lausnina :math:`u_\alpha`, sem skilgreind er með

	.. math::

	   u_\alpha(t)=\begin{cases}
	   (t+\alpha)^3, &t<-\alpha,\\
	   0, &-\alpha\leq t<\alpha,\\
	   (t-\alpha)^3, &\alpha\leq t.
	   \end{cases}

	Þetta dæmi sýnir okkur að til þess að fá ótvírætt ákvarðaða lausn þurfum við að setja einhver strangari skilyrði á :math:`f` en samfelldni.


Skilgreining (Sjá Skilgreiningu 6.6.3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
	:class: skilgreining

	Látum :math:`f:\Omega\to\mathbb{R}^m` vera fall, þar sem :math:`\Omega\subset \mathbb{R}\times \mathbb{R}^m` og :math:`A\subset \Omega`. Ef til er fasti :math:`C` þannig að

	.. math::

	   |f(t,x)-f(t,y)|\leq C|x-y|,\qquad (t,x), (t,y)\in
	    A,

	þá segjum við að :math:`f` uppfylli Lipschitz–skilyrði í menginu :math:`A`.



Setning (Sjá Setningu 6.6.5) (Picard. Víðfeðm útgáfa.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`I\subset \mathbb{R}` vera opið bil, :math:`a\in I`, :math:`b\in \mathbb{R}^m`, :math:`f\in C(I\times \mathbb{R}^m,\mathbb{R}^m)` og gerum ráð fyrir að :math:`f` uppfylli Lipschitz–skilyrði í :math:`J\times \mathbb{R}^m` fyrir sérhvert lokað og takmarkað hlutbil :math:`J` í :math:`I`. Þá er til ótvírætt ákvörðuð lausn :math:`u\in C^1(I,\mathbb{R}^ m)` á upphafsgildisverkefninu

	.. math::

	 u'=f(t,u), \qquad u(a)=b.



Fylgisetning (Sjá Fylgisetningu 6.6.6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Fylgisetning
	:class: setning

	Látum :math:`I\subset \mathbb{R}` vera opið bil, :math:`a\in I`, :math:`b\in {\mathbb{C}}^m`, :math:`A\in C(I,{\mathbb{C}}^{m\times m})` og :math:`f\in C(I,{\mathbb{C}}^m)`. Þá er til ótvírætt ákvörðuð lausn :math:`u\in C^1(I,{\mathbb{C}}^ m)` á upphafsgildisverkefninu

	.. math::

	 u'=A(t)u+f(t) \qquad u(a)=b.

Fylgisetning. (Sjá Fylgisetningu 6.6.7)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Fylgisetning
	:class: setning

	Látum :math:`I\subset \mathbb{R}` vera opið bil, :math:`a\in I`, :math:`b_0,\dots,b_{m-1} \in {\mathbb{C}}`, :math:`a_0,\dots,a_m, g\in C(I)` og :math:`a_m(t)\neq 0` fyrir öll :math:`t\in I`. Þá er til ótvírætt ákvörðuð lausn :math:`u\in C^m(I)` á upphafsgildisverkefninu

	.. math::

	   \begin{gathered}
	   a_m(t)u^{(m)}+\cdots+a_1(t)u'+a_0(t)u=g(t),\\
	   u(a)=b_0, u'(a)=b_1,\dots, u^{(m-1)}(a)=b_{m-1}.\end{gathered}

Setning (Sjá Setningu 6.6.8) (Picard. Staðbundin útgáfa.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
	:class: setning

	Látum :math:`\Omega` vera opið hlutmengi í :math:`\mathbb{R}\times \mathbb{R}^{m}`, :math:`a\in \mathbb{R}`, :math:`b\in \mathbb{R}^m`, :math:`(a,b)\in \Omega` og :math:`f\in C(\Omega,\mathbb{R}^m)`. Gerum ráð fyrir að til sé grennd :math:`U` um punktinn :math:`(a,b)` innihaldin í :math:`\Omega` og að fallið :math:`f` uppfylli Lipschitz–skilyrði í :math:`U`. Þá er til opið bil :math:`I` á :math:`\mathbb{R}` sem inniheldur :math:`a` og ótvírætt ákvörðuð lausn :math:`u\in C^1(I, \mathbb{R}^m)` á upphafsgildisverkefninu

	.. math::

	 u'=f(t,u), \qquad u(a)=b.



Picard-nálgun (Sjá Sýnidæmi 6.6.10 og 6.6.11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(i) Upphafsgildisverkefnið

.. math::

 u'=f(t,u),\qquad u(a)=b,

er jafngilt heildisjöfnunni (lausn upphafsgildisverkefnis er lausn heildisjöfnu og öfugt)

.. math::

 u=b+\int_a^t f(\tau,u)\,d\tau.

(ii) Gerum ráð fyrir að fallið :math:`f(t,u)` uppfylli Lipschitz-skilyrði eins og í Skilgreiningu 15.3. Látum :math:`u_0(t)=b` fyrir öll :math:`t\in I`. Skilgreinum svo runu falla :math:`u_1, u_2, \ldots` með þrepun þannig að fyrir :math:`n\geq 1` er

.. math::

 u_n(t)=b+\int_a^t f(\tau, u_{n-1}(\tau))\,d\tau.

Runan :math:`u_0, u_1, u_2, \ldots` hefur sem markgildi fall :math:`u` sem er lausn á upphafsgildisverkefninu

.. math::

 u'=f(t,u),\qquad u(a)=b.



Merking tilvistar- og ótvíræðnisetninga
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skoðum upphafsgildisverkefni

.. math::

 u'=f(t,u),\qquad u(a)=b,

þar sem fallið :math:`f(t,u)` uppfyllir Lipschitz-skilyrði.  Hugsum okkur að afleiðujafnan lýsi ,,kerfi‘‘ og að við þekkjum ástand þess ,,núna‘‘ þegar tíminn er :math:`t=a`.

(i) Lausn er til!

(ii) Lausnin er ótvírætt ákvörðuð. Ef við vitum ástand kerfisins núna þá getum við sagt fyrir með ótvíræðum hætti fyrir um ástand þess í framtíðinni.

(iii) Upphafsgildið er oft fengið með mælingum og þá má búast við mæliskekkju. Aðferðina við að sanna ótvíræðni lausnar má nýta til að sýna að ,,lausnin breytist samfellt” ef upphafsgildi er breytt. Hundalógikin er að ,,lítil‘‘ skekkja í upphafsgildi leiðir til ,,lítillar‘‘ skekkju í lausn. (Athugið að þegar gildi lausna í punkti :math:`t` ,,langt‘‘ frá :math:`t=a` eru skoðuð þá getur verið mikill munur á ,,réttri‘‘ lausn og lausn sem fengin er út frá mæligildi.)

(iv) Alla jafna má líka segja að ,,lausnin breytist samfellt” með :math:`f(t,u)`. Stuðlar sem koma fyrir í :math:`f(u,t)` eru oft fengnir með mælingum. Þetta er flókið viðfangsefni og mögulegt að hegðun lausnar gjörbreytist við smá breytingu í stuðlum í afleiðujöfnu.
