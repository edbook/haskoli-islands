Monte Carlo hermanir
====================

*Chaos is found in greatest abundance wherever order is being sought. 
It always defeats order, because it is better organized.*
-- Terry Pratchett, Interesting Times: The Play

Inngangur
---------

Hér ætlum við að skoða hvernig hægt er að nota slembitölur til þess að heilda
tölulega og leysa verkefni tengd hermun. 

Við munum ekki skoða hvernig slembitölur eru fundnar í tölvum og hversu
slembnar þær í raun og veru eru. Það er töluvert efni um þetta á
netinu og í bókum. 

- https://en.wikipedia.org/wiki/Pseudorandom_number_generator

- https://www.random.org/randomness/

- D. E. Knuth. The Art of Computer Programming, Volume 2: Seminumerical Algorithms.

Í Matlab og Octave gefa skipanirnar  *rand*, *randn* og *randi* slembitölur með mismunandi 
eiginleika. *rand* gefur jafndreifðar slembitölur á bilinu :math:`[0,1]`, 
*randn* gefur normaldreifðar rauntölur og *randi* gefur heiltölur á ákveðnu bili.


Nálgun á pi
~~~~~~~~~~~

Byrjum á að skoða einfalt verkefni. Við ætlum að nota flatarmál hringskífu til að 
nálga :math:`pi`. Við vitum að flatarmál hringskífu með geisla :math:`r` er :math:`\pi r^2`. 
Setjum :math:`r=1` og punkt af handahófi í rétthyrningnum :math:`[-1,1]\times[-1,1]`, þá
eru líkurnar á að hann lendi á hringskífunni :math:`p=\pi/4`. Þannig að ef við
getum fundið líkurnar :math:`p` þá finnum við gildið á :math:`\pi`. Líkurnar er hægt að herma
með því að velja marga punkta af handahófi og athuga hversu hátt hlutfall þeirra
lendir á skífunni. Af samhverfuástæðum er nóg fyrir okkur að skoða fyrsta fjórðung
þannig að við veljum punkta :math:`(x_1,y_1),\ldots,(x_n,y_n) \in [0,1]\times[0,1]`
af handahófi og skilgreinum :math:`S_n` sem fjölda þeirra punkta sem lenda
innan hringskífunnar og þá mun

.. math::
     \lim_{n \to \infty} \frac{S_n}{n} = \frac{\pi}{4}.

Forrit fyrir nálgun á pi
~~~~~~~~~~~~~~~~~~~~~~~~

Forritum þetta í `Sage <https://www.sagemath.org>`_ sem er forritunarmál fyrir 
vísindalega útreikninga sem byggir á Python.
     
.. sagecell::
    :auto: 
    :codefile: pi.sage
    :img: pi.png
    :imgwidth: 8 cm

Byggt á. https://github.com/BC-Design/sage/blob/master/monte-carlo.html .

.. note::
    Prófið að breyta gildinu á n í forritinu og sjáið hvort ekki er hægt að 
    bæta nálgunina.
    
.. warning::
    Þar sem aðferðin er slembin þá fæst ekki alltaf sama svarið þegar forritið er keyrt fyrir sama
    gildið á n.

Heildi í einni breytistærð
--------------------------

Nálgun á heildi
~~~~~~~~~~~~~~~

Það er lítill vandi að nálga heildi með þessari aðferð. *Meðalgildi* falls :math:`f` á bilinu
:math:`[a,b]` er skilgreint sem 

.. math::
    \overline f = \frac{1}{b-a} \int_a^b f(x)\, dx,
   
þannig að ef við getum fundið nálgun á meðalgildinu þá getum við nálgað heildið. 
Ef við veljum af handahófi punkta :math:`x_1,x_2,\ldots,x_n \in [a,b]` þá er eðlilegt að 
ætla að meðaltal fallgildanna í þessum punktum stefni á meðalgildi fallsins, það er

.. math::   
    \lim_{n\to \infty} \frac 1n \sum_{i=1}^n f(x_i) = \overline f. 


Nálgun á heildi: Dæmi
~~~~~~~~~~~~~~~~~~~~~

Prófum að nálga heildið 

.. math::
    \int_0^2 x^2 - \frac 12 x^3 + \frac 1{10}x\, dx

með því að velja af handahófi 1000 punkta á bilinu :math:`[0,2]` og nálga meðalgildið með meðaltali 
fallgildanna. Athugið að rétt svar er :math:`13/15 \approx 0.86667`.
   
.. sagecell::
    :auto: 
    :lang: octave
    :codefile: heildi.sage


Margföld heildi og rúmmál
-------------------------

Margföld heildi
~~~~~~~~~~~~~~~

Aðferðin hér að ofan er ekki mjög góð til þess að nálga heildi, skekkjan er af stærðargráðunni
:math:`1/\sqrt n` samanborið við :math:`1/n^2` í `samsettu trapisureglunni <kafli05.html#id5>`_.
Helstu kostir þess að nota slembni til að nálga heildi koma fram þegar við þurfum að reikna 
heildi í mörgum breytistærðum. Þá þurfa hefðbundnar aðferðir eins og samsetta trapisureglan 
:math:`n^d` punkta, þar sem :math:`d` er fjöldi breytistærða. 
En helsti kostur Monte Carlo heildunar er að það er auðvelt að heilda yfir flókin svæði. Hefðbundnar
aðferðir þurfa stikun á svæðinu til þess að ákvarða mörkin á heildunum en Monte Carlo þarf bara
að geta ákvarðað hvort tiltekinn punktur er innan svæðisins eða ekki. 

Margföld heildi: Dæmi
~~~~~~~~~~~~~~~~~~~~~

Reiknum rúmmál hlutarins :math:`S \subset \mathbb R^3` sem samanstendur af öllum punktum í 
:math:`[0,1]^3` sem uppfylla eftirfarandi ójöfnur

.. math::   
    \begin{aligned}
    x^2 + \sin(y) &\leq z \\
    x-z+\exp(y) \leq 1
    \end{aligned}
    
Rúmmálið, :math:`V`, fæst með því að reikna eftirfarandi heildi

.. math::
    V = \int \int \int_S 1\, dx\, dy\, dz.

.. sagecell::
    :auto: 
    :lang: octave
    :codefile: rummal.sage
    
.. only:: latex
    dd
    \begin{verbatim}
    asdf
    ff
    \end{verbatim}    

Hermun
------

Skoðum að lokum einfalt dæmi sem er ekki auðvelt að leysa beint, en er auðvelt að herma með því 
að nota sömu hugmyndir og hér að ofan.

Nál Buffons
~~~~~~~~~~~

Nál af einingarlengd er hent af handahófi á blað með tveimur samsíða línum
og lengdin á milli línanna er 1.
Gefið að miðja nálarinnar lendi á milli línanna, hverjar eru líkurnar
á að nálin öll lendi á milli línanna?

.. sagecell::
    :auto: 
    :lang: octave
    :codefile: NalBuffons.sage
    
