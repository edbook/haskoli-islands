Skammtafræði
==============

Rafeindaskipan
--------------

Rafeindir raða sér ekki tilviljunarkennt kringum kjarnann, heldur skipa þau sér á *rafeindahvolf* (e. shell) þar sem þau eru fyllt eftir orkulegri hagkvæmni. Efni reynir alltaf að stefna að *orkulægsta* ástandandinu, enda er það stöðugast. Þá er mikilvægt að geta greint hvað er orkulægsta ástandið.
Frumefni hafa allt að 7 rafeindahvolf og eru þau númeruð með *n* eða *höfuðskammtatölunni* (e. `principal quantum number <https://en.wikipedia.org/wiki/Principal_quantum_number>`_)
Rafeindahvolfið skiptist svo í undirhvolf (e. subshells). Þessi fjögur undirhvolf eru númeruð með :math:`\ell` eða *hverfiþungaskammtatölunni* (e. `Azimuthal quantum number <https://en.wikipedia.org/wiki/Azimuthal_quantum_number>`_) frá {0,1,2,3}. Þau eru þó betur þekkt sem {s,p,d,f} svigrúm.
Undirhvolfin eru einnig fyllt eftir orkulegri hagkvæmni, þ.e. *orkulægstu* svigrúmin eru fyllt fyrst. Röðin á þeim má sjá hér á myndinni fyrir neðan en þau eru fyllt á sama hátt og örvarnar stefna ofan frá og niður.

.. figure:: ./myndir/atom/rafskipan.png
  :align: center
  :width: 50%

Hafa ber í huga, eins og sjá má á mynd að orkuþrep **3d** er orkuhærra en **4s**, o.s.fr.

Hvernig skal finna rafeindaskipan frumefnis?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fjöldi rafeinda er jafn sætistölu frumefnis. Þá er hægt að byrja efst vinstra megin og fylla rafsvigrúmin eins og þau koma fyrir á eftirfarandi mynd, unnið til hægri og niður, að frumefninu sem leitast er eftir rafeindaskipan að. Fjöldi rafeinda á hverju svigrúmi
er jafn fjölda frumefna í hverju undirsvigrúmi, þ.e. það fara 2 rafeindir í s svigrúm, 6 rafeindir í p sigrúm, 10 rafeindir í d svigrúm og að lokum 14 rafeindir í f svigrúm.

.. figure:: ./myndir/atom/svigrum.png
  :align: center
  :width: 80%

.. tip::
  **Hver er rafeindaskipan brennisteins (S)? En hjá blýi (Pb)?**

  Brennisteinn hefur sætistöluna 16 og því 16 rafeindir. Byrjum á vetni í 1s og vinnum okkur að svigrúmi 3p, þar sem brennisteinn er. Þá er rafeindaskipanin:

  .. math::
      1s^2 2s^2 2p^6 3s^2 3p^{\textbf{4}}

  Eins og sjá má eru einungis 4 rafeindir í 3p svigrúminu þar sem samanlagður fjöldi þarf að vera 16 (:math:`2+2+6+2+4 = 16`).

  Hægt er að beita sömu aðferðarfræði á blý, en núna koma d og f svigrúm til leiks. Blý hefur sætistöluna 82 og því 82 rafeindir. Blý liggur í svigrúmi 6p í lotukerfinu og er það því lokastöðin. Með því að vinna sig hægri og niður fæst:

  .. math::
      1s^2 2s^2 2p^6 3s^2 3p^6 4s^2 3d^{10} 4p^6 5s^2 4d^{10} 5p^6 6s^2 5d^{10} 4f^{14} 6p^2

  Þá sést að heildarfjöldi rafeinda er :math:`2+2+6+2+6+2+10+6+2+10+6+2+10+14+2 =82`

.. warning::
  Þetta er ekki algilt, en fyrir suma hliðarmálma er þessi röð undirsvigrúmanna ekki endilega orkulega hagkvæmust. Þegar ákvarða á rafeindaskipan þeirra þarf að taka tillit til sértilvika fyrir hverja rafeindahýsingu.

.. _s.gildisrafeindir:

Gildisrafeindir
---------------

Gildisrafeindir (e. valence electrons) eru þær rafeindir sem eru á ysta hveli frumefnis, þ.e. þær rafeindir sem koma á eftir eðalgastegund í lotunni á undan. Þessar rafeindar eru einkum þýðingarmiklar í hvarfgirni efna þar sem frumefni
leitast eftir að hafa 8 gildisrafeindir í ysta hvoli. Þetta heitir *áttureglan* (e. octate rule).
Atóm geta komið fjölda gildisrafeinda í átta með nokkrum leiðum: þau geta t.d. myndað *sameind* þar sem þau deila gildisrafeindum með öðrum atómum í *efnatengjum*, eða *jónast* (e. ionize) þar sem þau kasta af sér umframrafeindum.

.. note::
 Eðalgastegundir eru einstaklega stöðugar, vegna þess að þær uppfylla átturegluna. Þær eru því mjög óhvargjarnar eða óvirkar (e. inert)

Þegar rita á rafeindaskipan stórra frumefna er vaninn að telja ekki upp öll hvolfin og rafeindirnar sem þar eru, heldur einungis gildisrafeindirnar og tákn eðalgastegundarinnar fyrir framan í hornklofa. Þetta er gert til að einfalda ritháttin auk þess sem gildisrafeindir koma mun oftar við sögu en þær sem eru innar.

.. tip::

 Hver er rafeindaskipan blýs, skrifað með þessum styttri rithátt?

 Nú er Xenon eðalgastegundin í lotunni fyrir ofan blý. Því er byrjað þar og þá fæst:

  .. math::
    [Xe] 6s^2 5d^{10} 4f^{14} 6p^{2}

Rafeindaskipan áframhald
------------------------

Rafeindir hafa fjórar skammtatölur, þ.e. *n*, :math:`\ell` en einnig *m*:math:`_{\ell}` og *m*:math:`_S`. *m*:math:`_{\ell}` er *segulskammtatalan* (e. `magnetic quantum number <https://en.wikipedia.org/wiki/Magnetic_quantum_number>`_) og segir til um í hvaða átt svigrúmið snýr. *m*:math:`_S`  eða *spunaskammtatalan* (e. `spin quantum number <https://en.wikipedia.org/wiki/Spin_quantum_number>`_) segir aftur á móti til um *spuna* rafeindarinnar.
Ekki verður farið nánar út í það hér en gott að vita að engar tvær rafeindir á atómi hafa sömu fjórar skammtatölur, og skammtatölurnar er hægt að tilgreina á myndrænan hátt.
Þá fær hvert hvolf og undirhvolf línu eða kassa sem rafeindir eru svo merktar inn á. Fjöldi kassa fer eftir gerð undirhvolfa, sem stjórnar segulskammtatölunni, og er tvöfalt færri en fjöldi rafeinda á fullu undirhvolfi.
Að lokum eru svo rafeindirnar táknaðar sem örvar sem snúa upp eða niður. Þetta tilgreinir spuna rafeindarinnar. Fullt hvolf hefur þá rafeind bæði upp og niður í hverjum kassa.

.. tip::

 **Tilgreindu fulla rafeindaskipan brennisteins**

 Brennisteinn hefur 5 gildisrafeindir, og þar af 2 á 3s og 4 á 4p. Byrjum á að teikna upp kassana fyrir svigrúmin.

  .. figure:: ./myndir/atom/syni1.svg
    :align: center
    :width: 40%

 Byrjum á því að fylla inn í 3s svigrúmið:

  .. figure:: ./myndir/atom/syni2.svg
    :align: center
    :width: 40%

 Með einungis 4 rafeindir er 3p svigrúmið ekki fullt og því þarf að passa hvernig fylla skal í það. Það skal ávallt fyrst fylla í alla kassana með einungis einni ör, og eftirstandandi rafeindir fylltar inn eftir það. Þ.e. *ekki setja tvær örvar í kassa, meðan það eru enn tómir kassar*.
 Það er gert til að fylgja eftir svokallaðari *reglu Hund's*.

  .. figure:: ./myndir/atom/syni3.svg
    :align: center
    :width: 40%

  .. figure:: ./myndir/atom/syni4.svg
    :align: center
    :width: 40%

.. begin-toggle::
  :label: Hund's regla
  :starthidden: False

*Regla Hund's* segir til um að það sé orkulega hagkvæmast og þannig stöðugast þegar rafeindir skipa sér stakar á svigrúm, meðan kostur er. Þær hafa þá sama spuna.

Þessi regla er oft kölluð *strætisvagnareglan*, þar sem vaninn er að setjast ekki í sætisröð með öðrum, ef það er tóm sætisröð í vagninum.

.. end-toggle::
