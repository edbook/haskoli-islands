Runur og raðir
==============

*Would it save you a lot of time if I just gave up and went mad now?*

\- Douglas Adams, The Hitchhiker's Guide to the Galaxy

.. index::
    runa

Runur
-----

Skilgreining: Runa
~~~~~~~~~~~~~~~~~~

*Runa* er raðaður listi af tölum.

Runa hefur fyrsta stak en ekkert síðasta stak. Stökin í runu eru oft
númeruð með náttúrlegu tölunum :math:`1, 2, 3, \ldots`. Stökin eru þá

.. math:: a_1, a_2, a_3, a_4, a_5, \ldots

Runur eru táknaðar með :math:`\{a_n\}_{n\in {{{\mathbb  N}}}}`,
:math:`\{a_n\}_{n=1}^\infty` eða bara :math:`\{a_n\}`.

Oft er runa gefin með formúlu, :math:`a_n = f(n)`. Til dæmis
:math:`a_n = 3n + n^2`.

.. index::
    runa; takmörkuð

Skilgreining
~~~~~~~~~~~~

Runa :math:`\{a_n\}` er sögð *takmörkuð að neðan* ef til er tala
:math:`m` þannig að

.. math:: m\leq a_n

fyrir allar náttúrlegar tölur :math:`n`.

Runan er sögð *takmörkuð að ofan* ef til er tala :math:`M` þannig að

.. math:: a_n\leq M

fyrir allar náttúrlegar tölur :math:`n`.

Runa sem er bæði takmörkuð að ofan og neðan er sögð *takmörkuð*.

.. index::
    runa; vaxandi/minnkandi
    runa; einhalla

Skilgreining
~~~~~~~~~~~~

Runa :math:`\{a_n\}` er sögð

(i)   *vaxandi* ef :math:`a_n\leq a_{n+1}` fyrir öll :math:`n`,

(ii)  *stranglega vaxandi* ef :math:`a_n< a_{n+1}` fyrir öll :math:`n`,

(iii) *minnkandi* ef :math:`a_n\geq a_{n+1}` fyrir öll :math:`n`,

(iv)  *stranglega minnkandi* ef :math:`a_n> a_{n+1}` fyrir öll
      :math:`n`.

Runa kallast *einhalla* ef hún er annaðhvort vaxandi eða minnkandi.

.. index::
    runa; víxlmerkjaruna

Skilgreining: Víxlmerkjaruna
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Víxlmerkjaruna* er runa þannig að formerki skiptast á, annaðhvort
:math:`+, -, +, -, \ldots` eða :math:`-, +, -, +, \ldots`.

Einnig má lýsa þessu þannig að runa :math:`\{a_n\}` sé víxlmerkjaruna ef
:math:`a_na_{n+1}<0` fyrir öll :math:`n`.

.. index::
    runa; samleitin

Skilgreining
~~~~~~~~~~~~

Segjum að :math:`\{a_n\}` sé *samleitin* að tölu :math:`L` (eða *stefni
á* :math:`L`) ef fyrir sérhverja tölu :math:`\epsilon>0` má finna
náttúrlega tölu :math:`N` þannig að ef :math:`n\geq N` þá er

.. math:: |a_n-L|<\epsilon.

Ritað :math:`\lim_{n\rightarrow \infty}a_n=L` og talan :math:`L` kallast
*markgildi rununnar*.

Sagt er að runa sé *samleitin* ef :math:`\lim_{n\rightarrow \infty}a_n`
er skilgreint, en annars er runan sögð *ósamleitin*.

Setning
~~~~~~~

Látum :math:`f` vera fall skilgreint á :math:`{{\mathbb  R}}` og látum
:math:`\{a_n\}` vera runu þannig að :math:`a_n=f(n)` fyrir öll
:math:`n`. Ef :math:`\lim_{x\rightarrow
\infty}f(x)=L` þá er :math:`\lim_{n\rightarrow\infty}a_n=L`.

.. warning:: 
    Þetta gildir ekki í hina áttina, runan getur verið
    samleitin án þess að fallið sé það.

Setning
~~~~~~~

Látum :math:`\{a_n\}` vera runu. Eftirfarandi tvö skilyrði eru jafngild:

(i)  :math:`\lim_{n\rightarrow\infty}a_n=L`,

(ii) fyrir sérhvert :math:`\epsilon>0` eru aðeins endanlega margir liðir
     rununnar :math:`\{a_n\}` utan við bilið
     :math:`(L-\epsilon, L+\epsilon)`.

Fylgisetning
~~~~~~~~~~~~

Samleitin runa er takmörkuð.

Setning
~~~~~~~

Gerum ráð fyrir að runurnar :math:`\{a_n\}` og :math:`\{b_n\}` séu
samleitnar. Þá gildir:

(i)   :math:`\lim_{n\rightarrow\infty}(a_n\pm b_n)=
      \lim_{n\rightarrow\infty}a_n\pm\lim_{n\rightarrow\infty}b_n`,

(ii)  :math:`\lim_{n\rightarrow\infty}ca_n=
      c\lim_{n\rightarrow\infty}a_n`, þar sem :math:`c` er fasti,

(iii) :math:`\lim_{n\rightarrow\infty}(a_n b_n)=
      (\lim_{n\rightarrow\infty}a_n)(\lim_{n\rightarrow\infty}b_n)`,

(iv)  ef :math:`\lim_{n\rightarrow\infty}b_n\neq 0` þá er
      :math:`\lim_{n\rightarrow\infty}\frac{a_n}{b_n}=
      \frac{\lim_{n\rightarrow\infty}a_n}{\lim_{n\rightarrow\infty}b_n}`,

(v)   ef :math:`a_n\leq b_n` fyrir öll :math:`n` sem eru nógu stór, þá
      er

      .. math:: \lim_{n\rightarrow\infty}a_n\leq\lim_{n\rightarrow\infty}b_n,

      (frasinn *fyrir öll* :math:`n` *sem eru nógu stór* þýðir að til er
      einhver tala :math:`N` þannig að skilyrðið gildir fyrir öll
      :math:`n\geq N`),

(vi)  (Klemmuregla) ef :math:`a_n\leq c_n\leq b_n` fyrir öll :math:`n`
      sem eru nógu stór og
      :math:`\lim_{n\rightarrow\infty}a_n=L=\lim_{n\rightarrow\infty}b_n`
      þá er runan :math:`\{c_n\}` samleitin og

      .. math:: \lim_{n\rightarrow\infty}c_n=L.

Setning
~~~~~~~

Takmörkuð einhalla (vaxandi eða minnkandi) runa er samleitin.

.. index::
    röð

Raðir
-----

Skilgreining: Röð
~~~~~~~~~~~~~~~~~

Látum :math:`a_1, a_2, \ldots` vera gefna runu. :hover:`Röðin,röð`

.. math:: \sum_{n=1}^\infty a_n  = a_1+a_2+a_3+\cdots

er skilgreind sem formleg summa liðanna :math:`a_1, a_2, a_3, \ldots`.

.. index::
    röð; samleitin

Skilgreining
~~~~~~~~~~~~

Fáum í hendurnar röð :math:`\sum_{n=1}^\infty a_n` þar sem
:math:`a_1, a_2, \ldots` eru tölur. Skilgreinum

.. math:: s_n=a_1+a_2+\cdots+a_n

sem summa fyrstu :math:`n` liða raðarinnar. Segjum að röðin
:math:`\sum_{n=1}^\infty a_n` sé :hover:`samleitin með summu,samleitin röð` :math:`s` ef

.. math:: \lim_{n\rightarrow\infty}s_n=s.

Það er að segja, röðin er samleitin með summu :math:`s` ef

.. math:: \lim_{n\rightarrow \infty}(a_1+a_2+\cdots+a_n)=s.

Ritum þá

.. math:: \sum_{n=1}^\infty a_n=s.

Setning
~~~~~~~

Ef :math:`A=\sum_{n=1}^\infty a_n` og :math:`B=\sum_{n=1}^\infty b_n`,
þ.e. báðar raðirnar eru samleitnar, þá gildir að

(i)   ef :math:`c` er fasti þá er :math:`\sum_{n=1}^\infty ca_n=cA`,

(ii)  :math:`\sum_{n=1}^\infty (a_n\pm b_n)=A\pm B`,

(iii) ef :math:`a_n\leq b_n` fyrir öll :math:`n` þá er :math:`A\leq B`.

Setning
~~~~~~~

Ef röð :math:`\sum_{n=1}^\infty a_n` er samleitin þá er

.. math:: \lim_{n\rightarrow\infty}a_n=0.

Athugasemd
~~~~~~~~~~

Þó svo :math:`\lim_{n \to \infty} a_n = 0` þá er ekki víst að röðin
:math:`\sum_{n=1}^\infty a_n` sé samleitin.

.. index::
    röð; kvótaröð

Dæmi: Kvótaröð
~~~~~~~~~~~~~~

Röðin

.. math:: \sum_{n=0}^\infty a^n

kallast *kvótaröð*. Hún er samleitin ef :math:`-1<a<1` og þá er

.. math:: \sum_{n=0}^\infty a^n = \frac{1}{1-a}.

.. index::
    röð; kíkisröð
    
Dæmi: Kíkisröð
~~~~~~~~~~~~~~

Röðin

.. math:: \sum_{n=2}^\infty \frac{1}{n(n-1)}

kallast *kíkisröð*. Hún er samleitin og

.. math:: \sum_{n=2}^\infty \frac{1}{n(n-1)} =1.

.. index::
    röð; samleitnipróf

Samleitnipróf fyrir raðir
-------------------------

Setning
~~~~~~~

Ef :math:`\lim_{n\rightarrow\infty}a_n` er ekki til eða
:math:`\lim_{n\rightarrow\infty}a_n\neq 0` þá er röðin
:math:`\sum_{n=1}^\infty a_n` ekki samleitin.

Setning: Samleitnipróf I
~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`a_n\geq 0` fyrir allar náttúrlegar tölur
:math:`n`. Röðin :math:`\sum_{n=1}^\infty a_n` er þá annaðhvort
samleitin eða ósamleitin að :math:`\infty` (þ.e.a.s. hlutsummurnar
:math:`s_n=a_1+\cdots+a_n` stefna á :math:`\infty` þegar :math:`n`
stefnir á :math:`\infty`.)

Setning: Samleitnipróf II – Samanburðarpróf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`0\leq a_n\leq b_n` fyrir allar náttúrlegar
tölur :math:`n`.

(i)  Ef :math:`\sum_{n=1}^\infty b_n` er samleitin þá er
     :math:`\sum_{n=1}^\infty a_n` líka samleitin.

(ii) Ef :math:`\sum_{n=1}^\infty a_n` er ósamleitin þá er
     :math:`\sum_{n=1}^\infty b_n` líka ósamleitin.

Setning: Samleitnipróf III – Heildispróf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Látum :math:`f` vera **jákvætt, samfellt** og **minnkandi** fall sem er
skilgreint á bilinu :math:`[1, \infty)`. Fyrir sérhverja náttúrlega tölu
:math:`n` setjum við :math:`a_n=f(n)`. Þá eru röðin
:math:`\sum_{n=1}^\infty a_n` og óeiginlega heildið
:math:`\int_1^\infty f(x)\,dx` annaðhvort bæði samleitin eða bæði
ósamleitin.

Fylgisetning
~~~~~~~~~~~~

Röðin :math:`\sum_{n=1}^\infty\frac{1}{n^{p}}` er samleitin ef
:math:`p>1` en ósamleitin ef :math:`p\leq 1`.

Setning: Samleitnipróf IV – Markgildissamanburðarpróf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`a_n\geq 0` og :math:`b_n\geq 0` fyrir allar
náttúrlegar tölur :math:`n` og
:math:`\lim_{n\rightarrow\infty}\frac{a_n}{b_n}=L`, þar sem :math:`L` er
tala eða :math:`\infty`.

(i)  Ef :math:`L<\infty` og röðin :math:`\sum_{n=1}^\infty b_n` er
     samleitin þá er röðin :math:`\sum_{n=1}^\infty a_n` líka samleitin.

(ii) Ef :math:`L>0` og röðin :math:`\sum_{n=1}^\infty b_n` er ósamleitin
     þá er röðin :math:`\sum_{n=1}^\infty a_n` líka ósamleitin.

Setning: Samleitnipróf V – Kvótapróf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`a_n>0` fyrir öll :math:`n` og að markgildið
:math:`\rho=\lim_{n\rightarrow\infty}\frac{a_{n+1}}{a_n}` sé skilgreint
eða að það sé :math:`\infty`.

(i)   Ef :math:`0\leq\rho<1` þá er röðin :math:`\sum_{n=1}^\infty a_n`
      samleitin.

(ii)  Ef :math:`1<\rho\leq \infty` þá er röðin
      :math:`\sum_{n=1}^\infty a_n` ósamleitin.

(iii) Ef :math:`\rho=1` þá er ekkert hægt að fullyrða um hvort röðin
      :math:`\sum_{n=1}^\infty a_n` er samleitin eða ósamleitin, hvor
      tveggja kemur til greina og nota þarf aðrar aðferðir til að skera
      úr um það.

Setning: Samleitnipróf VI – Rótarpróf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að :math:`a_n>0` fyrir öll :math:`n` og að markgildið
:math:`\sigma=\lim_{n\rightarrow\infty}\sqrt[n]{a_n}` sé skilgreint eða
að það sé :math:`\infty`.

(i)   Ef :math:`0\leq\sigma<1` þá er röðin :math:`\sum_{n=1}^\infty a_n`
      samleitin.

(ii)  Ef :math:`1<\sigma\leq \infty` þá er röðin
      :math:`\sum_{n=1}^\infty a_n` ósamleitin.

(iii) Ef :math:`\sigma=1` þá er ekkert hægt að fullyrða um hvort röðin
      :math:`\sum_{n=1}^\infty a_n` er samleitin eða ósamleitin, hvor
      tveggja kemur til greina og nota þarf aðrar aðferðir til að skera
      úr um það.

.. _vixlmerkjaprof:

Setning: Samleitnipróf VII – Víxlmerkjaraðapróf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gerum ráð fyrir að

(i)   :math:`a_n\geq 0` fyrir öll :math:`n` (frekar jákvæðir liðir),

(ii)  :math:`a_{n+1}\leq a_n` fyrir öll :math:`n` (frekar minnkandi),

(iii) :math:`\lim_{n\rightarrow\infty} a_n=0` (stefnir á 0).

Þá er víxlmerkjaröðin

.. math:: \sum_{n=1}^\infty (-1)^{n-1}a_n=a_1-a_2+a_3-a_4+\cdots

samleitin.

Fylgisetning
~~~~~~~~~~~~

Gerum ráð fyrir að runa :math:`\{a_n\}` uppfylli skilyrðin sem gefin eru
í setningunni á undan :ref:`(9.3.9) <vixlmerkjaprof>`. 

Látum :math:`s_n` tákna summu :math:`n` fyrstu liða raðarinnar
:math:`\sum_{n=1}^\infty (-1)^{n-1}a_n` og táknum summu raðarinnar með
:math:`s`. Þá gildir að :math:`|s-s_n|\leq |a_{n+1}|`.


.. index::
    röð; alsamleitni

Alsamleitni
-----------

Skilgreining
~~~~~~~~~~~~

Röð :math:`\sum_{n=1}^\infty a_n` er sögð vera *alsamleitin* ef röðin
:math:`\sum_{n=1}^\infty |a_n|` er samleitin.

Setning
~~~~~~~

Röð sem er alsamleitin er samleitin.

Athugasemd
~~~~~~~~~~

Til eru samleitnar raðir, t.d. röðin
:math:`\sum_{n=1}^\infty \frac{(-1)^{n-1}}{n}`, sem eru ekki
alsamleitnar.

.. index::
    röð; skilyrt samleitni

Skilgreining
~~~~~~~~~~~~

Samleitin röð sem er ekki alsamleitin er sögð vera 
*skilyrt samleitin*, það er :math:`\sum_{n=1}^\infty a_n` er samleitin
en röðin :math:`\sum_{n=1}^\infty |a_n|` er ósamleitin.

Setning: Umröðun
~~~~~~~~~~~~~~~~

Dæmi um umröðun á liðum raðar :math:`\sum_{n=1}^\infty a_n` er

.. math::

   a_{10}+a_9+\cdots+a_1+a_{100}+a_{99}+\cdots+a_{11}+
   a_{1000}+a_{999}+\cdots.

(i)  Ef röðin :math:`\sum_{n=1}^\infty a_n` er alsamleitin þá skiptir
     engu máli hvernig liðum raðarinnar er umraðað, summan verður alltaf
     sú sama.

(ii) Ef röðin :math:`\sum_{n=1}^\infty a_n` er skilyrt samleitin og
     :math:`L` einhver rauntala, eða :math:`\pm\infty` þá er hægt að
     umraða liðum raðarinnar þannig að summan eftir umröðun verði
     :math:`L`.

.. note:: 
	Með öðrum orðum: 
	Liðum skilyrt samleitinnar raðar má umraða þannig að summan getur orðið
	hvað sem er, það skiptir því máli í hvaða röð við leggjum saman.
