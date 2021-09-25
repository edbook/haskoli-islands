.. include:: rst-include

Verkefni
========

Skila- og tímadæmin þar sem verkefnin eru notuð í Tölvunarfræði 1a 2021 eru sýnd í svigum.

1. Annars stigs jafna (S3)
~~~~~~~~~~~~~~~~~~~~~~~~~~
Skrifið forrit sem leysir annars stigs jöfnu

.. math:: a x^2 + b x + c = 0

Fallið á að lesa inn :math:`a`, :math:`b` og :math:`c` með ``input``-skipunum
(með viðeigandi beiðnum til notanda). Ef jafnan hefur tvær lausnir á forritið að
skrifa „Lausnirnar eru:“ og síðan lausnirnar, ef hún hefur eina lausn á að
skrifa hana með viðeigandi skýringu og ef engin lausn er skal skrifa skilaboð um
það. Lausn eða lausnir eru gefnar með formúlunni

.. math::
   x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}

Ef stærðin undir kvaðratrótinni er neikvæð þá er engin lausn, ef
hún er núll er ein lausn, annars tvær. Gerið auk þess ráð fyrir
þeim möguleika að :math:`a` sé 0. Ef :math:`b` er ekki líka 0 þá er jafnan fyrsta
stigs og forritið á að skrifa að svo sé, ásamt lausninni (sem er
þá ein). Látið :math:`b` og :math:`c` vera gefin með afmælisdegi ykkar (dagur og mánuður) og prófið forritið fyrir fjórar mismunandi jöfnur, fyrsta
stigs jöfnuna :math:`bx + c = 0` og annars stigs jöfnur sem hafa enga, eina og tvær
lausnir þar á meðal jöfnuna :math:`x^2 + bx + c = 0`. Setjið viðeigandi skjölunarstreng  fremst í forritið.

2. Simpsons-regla (S3)
~~~~~~~~~~~~~~~~~~~~~~
Skrifa skal forrit til að nálga heildi með svonefndri *Simpsons-regla*. Í trapisureglu er heildisbilinu skipt í :math:`n` hlutbil, fallið sem heilda skal nálgað með beinum línustrikum og heildi þess nálgað með flatarmálinu undir þessum línustrikum. Í Simpsonsreglu er fallið hinsvegar nálgað (eða *brúað* eins og það er kallað) með parabólum og heildið nálgað með flatarmálinu undir þeim. Skoðið endilega Wikipedíu-grein `um aðferðina <https://en.wikipedia.org/wiki/Simpson%27s_rule>`_.

Simpsons-formúlan er eftirfarandi:

.. math::
   \int_{a}^{b} f(x) \, dx \approx 
   \frac{\Delta x}{3}\left(f(x_0) + 4f(x_1)+2f(x_2)+
   4f(x_3)+2f(x_4)+\cdots+4f(x_{n-1}) + f(x_{n})\right)

þar sem :math:`\Delta x = \displaystyle{\frac{b-a}{n}}`, :math:`x_i=a+i\Delta x`, :math:`i = 0,\ldots, n` og :math:`n` er slétt tala.

Skrifið fall ``simpson(f,a,b,n)`` sem nálgar heildið af ``f`` frá ``a``
til ``b`` með samsettri Simpsons-reglu með ``n`` hlutbilum.

Prófið með heildunum:

.. math::  (*)\quad\int_1^2\frac{\sin(x)}{x} dx
           \qquad\quad\text{og}\qquad\quad
           (**)\quad\int_0^1\exp(x) dx

með 4 hlutbilum. Ef rétt er forritað ætti að fást :math:`(*)` 0.65933 og
:math:`(**)` 1.71832. Rétt gildi eru 0.65933 og 1.71828, og trapisuregla með 4
bilum gefur 0.65863 og 1.72722.

Heildið líka eitthvert sjálfvalið fall þar sem afmælisdagur ykkar kemur við sögu.

3. Viðsnúningur (S3)
~~~~~~~~~~~~~~~~~~~~
a) Skrifið fall ``hausaftast(L)`` sem færir haus L aftast. Ef kallað er með
   :code:`L=[1,2,3,4]` ætti að koma út :code:`L=[2,3,4,1]`. Prófið líka með
   lista búnum til útfrá afmælisdegi (t.d. 3.8.1999 :math:`\to` :code:`[3,8,99]`).

b) Skrifið fall ``snúavið(L)`` sem snýr við lista. Hér er reiknirit:

   .. code::

      fall snúavið(L)
          n := lengd L
          M := tómur listi
          fyrir i = n-1,n-2,...,0:
              setja i-ta stak L afast í M
          skila M
          
   Prófið að snúa við ``L=[1,2,3,4]`` sem ætti að skila ``[4,3,2,1]``
   og líka afmælisdagalistanum úr a-lið.

4. Orðaleikur (S4)
~~~~~~~~~~~~~~~~~~
Til að leysa þetta dæmi gæti gagnast að skoða lausn á T3.3

a) Skrifið fall ``telja(s)`` sem byrjar á nota ``s.split()`` til að búa til
   lista af einstökum orðum í ``s`` og telur síðan hve margir stafir eru í
   hverju orði. fallið á að skila lista með þessari talningu. Þannig ætti

   ``telja("Afi minn og amma mín")``

   að skila listanum ``[3,4,2,4,3]``. Prófið líka að telja stafi í nafninu
   ykkar (t.d. ``telja("Kristján Jónasson")``).

b) Búið til fall ``hrópa(s)`` sem skrifar ``s`` út með stórum stöfum og tveimur
   upphrópunarmerkjum. Hrópið svo nafnið ykkar :)

c) Til að athuga hvort stafur `c` sé hástafur má spyrja: ``c == c.upper()``.
   Skrifið fall ``stórir(s)`` sem skilar lista af rökgildum með i-ta gildið
   satt ef i-ta orðið í :code:`s` byrjar á stórum staf. Prófið.

5. Kvaðratrót (S4)
~~~~~~~~~~~~~~~~~~
Um útreikning kvaðratrótar er fjallað í kafla 7.5 í `Think Python <https://greenteapress.com/wp/think-python-2e/>`_ kennslubókinni.
Þar stendur að hægt sé að nota Newtons aðferð, og að ef byrjað er með einhverja
nálgun :math:`x` við :math:`\sqrt{a}` þá fáist betri nálgun, :math:`y` með því
að reikna:

.. math:: (*)\hspace{4cm} y = \frac{x + a/x}{2}

Formúluna má m.a. rökstyðja þannig að ef :math:`x` er nákvæmt gildi þá er :math:`x^2 =
a` svo að :math:`x = a/x`. Hinsvegar ef :math:`x` er aðeins minna en
kvaðratrótin þá þá verður :math:`a/x` aðeins stærra en hún (og öfugt) og því
ætti meðaltal :math:`x` og :math:`a/x` að vera betri nálgun. Svo má athuga hve
nálgunin er góð með því að skoða muninn á :math:`x` og :math:`y`. Ef t.d.

.. math:: (**)\hspace{4cm}|x - y| < \varepsilon

þar sem :math:`\varepsilon = 10^{-4}` er hún orðin nokkuð góð.

a. Skrifið Python-fall, ``krót(a)`` sem útfærir þessa hugmynd. Byrjið með
   upphafsgildið ``x = 1`` og finnið svo betri og betri lausn með því að nota
   while-lykkju sem reiknar :math:`(*)` aftur og aftur og heldur áfram þangað
   til :math:`(**)` er uppfyllt. Prófið að reikna :math:`\sqrt{9}` og
   :math:`\sqrt{10}` (rétt gildi 3.16227766017).

b. Búið nú til nýja útgáfu af fallinu sem er með tvo inntaksstika, töluna ``a`` og
   nákvæmnikröfu :code:`eps`, og telur auk þess hve margar ítrekanir eru teknar.
   Látið það skila bæði lokanálguninni og ítrekanafjöldanum (sbr. fyrra
   sýnidæmið í kafla :numref:`virka`). Skrifið niðurstöður með hæfilegum
   skýringartextum: lokanálgun, ítrekanafjölda, og muninn á réttri kvaðratrót og
   lokanálgun. Prófið með nokkrum mismunandi gildum á :math:`a` (m.a. eitthvað
   mjög stórt gildi) og :math:`\varepsilon`, (m.a. gildi sem er ekkert mjög
   lítið, t.d. 0.1 eða 0.01). Bætið við textareit og skrifið örfá orð um
   niðurstöðu þessarar prófunar.

6. Meðaltal og staðalfrávik (T4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Skrifið fall ``tölfræði(x)`` sem skilar pari ``(m, s)`` með meðaltali og staðalfráviki stakanna í listanum ``x`` með því að nota formúlurnar: 

.. math::
   m &= \frac{1}{n}\sum_{i=0}^{n-1}{x[i]}\\
   s &= \sqrt{\frac{1}{n-1}\sum_{i=0}^{n-1}(x[i] - m)^2}

Prófið með ``x = [3,7,7,1]`` (á að skila ``[4.5, 3.0]``) og líka með lista ``[d,m,á]`` búnum til úr fæðingardegi..

7. Bóluröðun (T4)
~~~~~~~~~~~~~~~~~
Hér er reiknirit sem raðar n-staka lista x með bóluröðun `bubble sort <https://en.wikipedia.org/wiki/bubble_sort>`_, sem snýst um að rúlla í gegn um stökin og ef tvö samliggjandi stök eru í öfugri röð þá er víxlað á þeim. Þetta er endurtekið þar til öll stökin eru í röð. Minnstu stökin bobbla smám saman eins og loftbólur fremst í listann.

.. code:: text
          
   víxlað = satt
   meðan víxlað
      víxlað = ósatt
      fyrir i=1,...,n-1:
         ef x[i-1] > x[i] þá
            víxla á x[i-1] og x[i]
            víxlað = satt
              
Þýðið þetta reiknirit yfir í Python-fall ``bóluröðun(x)``. Athugið að til að víxla á breytum ``x`` og ``y`` má nota :code:`(x,y) = (y,x)`. Prófið með því að raða listanum ``[3,8,1,2,5,4]``.

8. Pólhnit (T4)
~~~~~~~~~~~~~~~
Lesið aðeins um `pólhnit <https://en.wikipedia.org/wiki/Polar_coordinate_system>`_
á Wikipediu áður en þið spreytið ykkur á eftirfarandi verkefni.

a. Skrifið fall ``pol2rec(r,theta)`` sem skilar pari ``(x,y)``, til að breyta úr
   pólhnitum yfir í rétthyrnd hnit með eftirfarandi formúlum:

   .. math::
      x &= r \cos{\theta}\\
      y &= r \sin{\theta}

   Prófið að breyta :math:`(r,\theta) = (4,35°)` yfir í rétthyrnd hnit :math:`x`
   og :math:`y` (á að gefa :math:`x=3.277`, :math:`y=2.294`). Munið að nota
   ``math.radians`` til að breyta gráðum í radíana.

b. Skrifið svo annað fall, ``rec2pol(x,y)`` sem skilar ``(r,theta)`` og breytir
   í hina áttina með formúlunum:

   .. math::
      \theta &= \operatorname{atan2}(y,x)\\
      r &= \sqrt{x^2 + y^2}

   Prófið að breyta svarinu sem fékkst í a-lið aftur til baka í pólhnit.

   .. admonition:: Athugasemd
      :class: athugid

      Stærðfræðifallið `atan2 <https://en.wikipedia.org/wiki/Atan2>`_
      sem er líka til í Python er sérhannað til að breyta úr rétthyrndum hnitum
      í pólhnit. Það skilar horni :math:`\theta` á bilinu :math:`(-\pi,\pi]`
      þannig að :math:`\tan \theta = y/x`, nema ef :math:`x=0`, þá skilar fallið
      :math:`\pm\pi/2` með sama formerki og :math:`y`. Hornið er valið þannig að
      það sé stefnuhorn vigursins :math:`(x,y)`.

9. Uppflettitafla afturábak (T4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Hugsum okkur að ``ísl_ens`` sé uppflettitafla sem geymir ensk-íslenska orðabók.
Hún gæti t.d. innihaldið pörin:

- ``"reipi"`` :math:`\to` ``"rope"``
- ``"hús"`` :math:`\to` ``"house"`` og
- ``"rauður"`` :math:`\to` ``"red"``.

Ef við vilum búa til ensk-íslenska orðabók gætum við snúið töflunni við og
fengið pörin ``"rope"`` :math:`\to` ``"reipi"``, ``"house"`` :math:`\to`
``"hús"`` o.s.frv.

a. Skrifið fall ``snúavið(U)`` sem snýr uppflettitöflu við á þennan hátt. Gerið
   ráð fyrir að taflan ``U`` varpi engum tveimur lyklum í sama gildið. Prófið
   með orðaskránni að framan og búið til ``ens-ísl``.

b. Skrifið nýja útgáfu af fallinu, ``snúavið2(U)``, sem er ekki með slíkri
   einkvæmnitakmörkun. Það á að skila nýrri uppflettitöflu ``V`` sem er þannig að ef
   ``g`` er gildi sem tveir lyklar varpast í, ``U[x] = U[y] = g`` þá á ``V`` að
   varpa ``g`` í lista með ``x`` og ``y``, ``V[g] = [x,y]``. Bætið nú tveimur pörum:

   - ``"tómarúm"`` :math:`\to` ``"vaccum"``
   - ``"ryksuga"`` :math:`\to` ``"vaccum"``

   við ``ísl_ens`` og prófið ``snúavið2``.

10. Skrá með íslenskum orðum (S5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Þetta verkefni er lauslega byggt á verkefnum í 9. kafla `Think Python
<https://greenteapress.com/wp/think-python-2e/>`_ kennslubókarinnar. Þar er ekki
gert ráð fyrir að skrár séu lesnar beint af netinu, en það er hinsvegar hægt með
pakka sem heitir ``urllib`` og það verður gert hér. Auk pakkans þarf tvö
strengjaföll sem ekki eru nefnd í :numref:`söfn`. og :numref:`helstu-aðgerðir`.
kafla: ``s.strip()`` sem hendir línuskiptatákni aftan af s og
``s.decode`` sem umskrifar *utf-8*-streng sem Python-streng (sjá athugasemd
um utf-8 hér neðar).

Hér er forritsbútur, sem flytur inn ``urllib`` og skilgreinir jafnframt fall
``allarlínur`` sem nota má til að lesa inn textaskrá:

.. code:: Python
          
   from urllib.request import urlopen
   # f = urlopen("http://slóð/að/skrá") opnar skrá f á netinu

   def allarlínur(f):
      '''skilar lista með öllum línum skrár f, 
      utf-8 afkóðuðum og án línuskiptatákna'''
      return [l.decode('utf-8') for l in f.read().splitlines()]

Í skrá með veffang `cs.hi.is/t1a/ord.txt <http://cs.hi.is/t1a/ord.txt>`_ eru 217
þúsund íslensk orð. Þið getið skoðað skrána með því að smella á hlekkinn. Í
verkefninu sem hér fylgir þarf að nota ýmsar strengjaaðgerðir sem lýst er í
kafla :numref:`strengir`.

a. Lesið skrána inn og prentið út fyrstu 5 orðin og líka tíu þúsundasta hvert
   orð og öll orð sem eru lengri en 30 stafir.

b. Spegilorð (*palindrome*) er orð sem er eins lesið afturábak og áfram (t.d.
   kajak). Skrifið rökfall ``spegilorð(s)`` sem kannar hvort ``s`` sé spegilorð
   [rökfall er fall sem skilar ``True`` eða ``False`` og prófið. Skrifið í
   framhaldi út öll spegilorð í skránni, 10 á hverja línu.

      :code:`abba, afa, aga, agga, aka, ala, alla, ama, amma, ana, apa,`

   .. admonition:: Leiðbeiningar
      :class: python
   
      Til að snúa við streng ``s`` má nota ``s[::-1]``. Það þarf
      að nota ``end=`` í print-skipun sbr. kafla :numref:`útprentun`, og svo þarf
      að nota teljara sem fylgist með hvað er búið að prenta mörg orð á línuna og
      þegar þau eru orðin 10 er farið í nýja línu með ``print()`` og teljarinn
      núllstilltur. Fyrsta línan sem prentast ætti að vera:

c. **Aukadæmi:** Finnið það orð í skránni sem hefur hlutfallslega flesta samhljóða.         

.. admonition:: Athugasemd
   :class: athugid

   `UTF-8 <https://en.wikipedia.org/wiki/UTF-8>`_ er staðall til að geyma
   bókstafi og önnur rittákn í tölvum. Staðallinn hefur á síðasta áratug eða svo
   orðið alsráðandi í tölvuheiminum, og eru 97% allra vefsíðna skráð með honum.
   Hver stafur er geymdur í einu til fjórum bætum. Algengustu tákn og stafir,
   þ.m.t. allir enskir bókstafir nota eitt bæti, aðrir bókstafir allra evrópskra
   tungumála tungumála þurfa tvö bæti, en sjaldgæfari stafir og tákn þurfa þrjú
   eða fjögur bæti. Strengir forritunarmálum, þ.m.t. Python eru hinsvegar `ekki
   geymdir <https://dev.to/bplevin36/python-strings-are-not-utf-8-2dfj>`_ með
   UTF-8 sniði heldur ýmist sem *Latin-1*, *UTF-16* eða *UTF-32*. Þetta er gert
   til að öll tákn hvers strengs séu jafn mörg bæti, sem flýtir t.d. fyrir
   uppflettingu á *i*-ta sæti.
              
11. Fjöldi stafa í skrafli (S5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
a. Í þessu verkefni á að búa til töflu yfir hlutfallslega tíðni hvers stafs í
   skránni ``ord.txt`` úr verkefni 10, og jafnframt hvað sú tíðni samsvarar
   mörgum heilum stöfum af 98, sem er heildarfjöldi stafa í pokanum sem notaður
   er í borðspilinu skrafli (*scrabble*). Taflan ætti að byrja svona:

   .. code:: text

      stafur  tíðni  fjöldi
      –––––––––––––––––––––
        a     9.80%    10
        á     1.27%     1
        b     1.34%     1

   .. admonition:: Leiðbeiningar
      :class: python

      Byrjið á að skoða athugasemdina að neðan, þ.m.t. vefsíðu
      netskraflara. Skrána ord.txt má opna og lesa inn eins og í verkefni 10. Ef
      ``s`` er strengur og ``L`` er listi af strengjum þá má skeyta þeim saman
      aðskildum með ``s`` með því að rita ``s.join(L)``, til dæmis:

      .. code:: Python

         L = ["már", "mús", "mý"]
         s1 = ",".join(L)         # gefur "már,mús,mý
         s2 = "".join(L)          # gefur "mármúsmý"

      Þannig má fá langan streng ``öllorð`` með öllum orðum skrárinnar í runu
      með því beita ``join`` með tóma strengnum á útkomuna úr ``allarlínur``.
      Skoðið byrjunina á öllorð með ``print(öllorð[:40])``. Svo má t.d. finna
      hlutfallslega tíðni a með ``ta = öllorð.count("a")/n`` þar sem ``n =
      len(öllorð)``. Tilsvarandi heill fjöldi a-a af 98 fengist með
      ``round(ta*98)``. Hægt er að rúlla í gegn um alla stafina með for-lykkju
      og strengnum:

         :code:`stafróf = "aábcdðeéfghiíjklmnoópqrstuúvwxyýzþæö"`

b. **Aukaspurning:** Ef rétt er reiknað sést að allmargir stafir gefa fjöldann
   0. Í skrafli er hinsvegar amk. einn stafur af hverri gerð í pokanum. Ef við
   hækkum öll núllin upp í einn fást of margir stafir. Lýsum einni leið til að
   leiðrétta það. Byrjum á að búa til uppflettitöflu ``fj`` þannig að ``fj[c]``
   sé fjöldi af staf c skv. a-lið, nema við látum ``fj[c] = max(1,round(ta*98))``.
   Hér er tilvalið að nota yfirgrip. Við látum:
   
   .. code:: Python

      búnir = [c for c in stafróf if fj[c] == 1]
      eftir = [c for c in stafróf if fj[c] > 1]
      N = 98 - len(búnir)

   Nú má fara aftur í gegn um lykkju eins og í a-lið, nema hvað aðeins er rúllað
   í gegn um stafina í ``eftir``, í stað 98 kemur N, og svo þarf n að vera fjöldi
   stafa í skránni sem eru í ``eftir``. Aftur er hægt að nota yfirgrip:

      ``n = sum([öllorð.count(c) for c in eftir])``.

   Útfærið þessa hugmynd og athugið hver heildarfjöldi stafa verður.

.. admonition:: Athugasemd: Um skrafl
   :class: athugid

   Í skrafli eru mismargir stafir af hverri gerð í pokanum eins og skoða má á
   `vefsíðu netskraflara <https://netskrafl.is/help>`_: það eru t.d. ellefu a,
   og átta r, en ekki nema tvö ó og eitt h. Stafirnar gefa líka mismunandi mörg
   stig. Fjöldi eintaka af hverjum staf er nokkurnveginn í hlutfalli við tíðni
   stafanna í íslenskum orðalista svipuðum þeim sem er í skránni *ord.txt*, og
   gildi hvers stafs er líka tengt þessari tíðni.
