Fjölvalsspurningar í Sphinx
===========================

Hér hefur mér loksins tekist að setja inn embedded fjölvalsspurningar (og embedded myndbönd!).

Í extension-inu eqt.py er hægt að setja inn fjölvalsspurningar (og opnar spurningar).
Það er hægt að gera það þannig að sé rangt svar sett inn kemur útskýringar á því hvers vegna valkosturinn er réttur eða rangur eftir að spurningunni hefur verið svarað rétt. Það væri auðvitað flottara ef sú útskýring ranga möguleikans birtist þegar hann er valinn, en það virkar ekki alveg. Mér sýnist það vera einhver smávilla í ``dynsite.js`` skránni.  Meira bil er á milli svarmöguleikanna þegar þessi fítus er nýttur svo e.t.v. er fallegra að sleppa því alfarið að nota hann (tekið eftir mun á dæmum 1 og 2).

Það er líka hægt að bæta við takkanum "Sýna lausn" sem birtir hvert rétta svarið er þegar sóst er eftir því. Það er gert með því að breyta 'none' í 'inline' í línu 264 í ``dynsite.js``.

Til þess að virkja eqt pakkann þurfti að gera hitt og þetta, m.a. að uppfæra Sphinx og uppfæra nokkrar skriptur úr Python2 í Python3 og bæta við nokkrum línum í ``layout.html`` (sjá readme fyrir viðbæturnar). Meðal afleiðinga þessa fikts var að toggleblock og geogebra hættu að virka tímabundið, en það er komið í lag.

----------------

.. eqt:: daemi-hradi1

  **Æfingadæmi 1** Hversu langt kemst maður sem gengur á hraðanum :math:`v=3 \text{ m/s}` á einni mínútu?

  1) :eqt:`I` 300 metra
     :expl:`Þetta er ekki rétt svar, því það eru ekki 100 sekúndur í einni mínútu.`
  #) :eqt:`I` 3 metra
     :expl:`Lastu dæmið rétt? Hvað eru margar sekúndur í einni mínútu?`
  #) :eqt:`C` 180 metra
     :expl:`Já! Staðsetning er margfeldi hraða og tíma.`
  #) :eqt:`I` None of the above (engin útskýring)
     :expl:`Nei, reyndu aftur`

  .. eqt-solution::
    Þetta er lausn verkefnisins.
    Hún á ekki að birtast fyrr en beðið hefur verið um hana eða rétt svar hefur verið sett inn.

    Það er hægt að setja inn stærðfræði eins og manni lystir.

    .. math::

      2+2=4

----------------

.. eqt:: daemi-hradi2

  **Æfingadæmi 2** Hversu langt kemst maður sem gengur á hraðanum :math:`v=3 \text{ m/s}` á einni mínútu?

  A) :eqt:`I` 300 metra

  #) :eqt:`I` 3 metra

  #) :eqt:`C` 180 metra

  #) :eqt:`I` Ekkert af ofangreindu

  .. eqt-solution::
    Í einni mínútu eru 60 sekúndur. Við margföldum saman hraðann og tímann og fáum:

    .. math::
      60\text{ s} \cdot 3 \text{ m/s} = 180 \text{ m}


---------------

.. eqt:: daemi-hradi3

   **Æfingadæmi 3** Er mynd með þessu dæmi?

   .. figure:: ./myndir/einingar/sol.svg
     :align: center
     :alt: texti með mynd

   A) :eqt:`I` nei

   #) :eqt:`I` nei

   #) :eqt:`C` já

   #) :eqt:`I` nei
