.. include:: rst-include

.. role:: matlab(code)
   :language: matlab
   :class: highlight


Inngangur: Um Python
====================

.. _inngangur:

Einfalt og auðlært mál
----------------------

Python er forritunarmál sem kom fram árið 1991 og hefur náð mikilli útbreiðslu. Það var hollenski tölvufræðingurinn Guido van Rossum sem bjó Python til og spilaði stórt hlutverk í þróun þess, en margir fleiri hafa lagt hönd á plóg. Málið heitir eftir grínistahópnum *Monty Python* (sem aftur dregur nafn af kyrkislöngum, *pythons*). 

.. figure:: myndir/monty-python.jpg
   :align: center
   :figwidth: 9cm

   Monty Python grínistarnir

Vinsælasta útgáfan af Python nefnist formlega CPython og er opin og ókeypis. Hana er að finna á `python.org <http://python.org>`_ og þar má líka lesa um *Python Software Foundation* sem hefur síðan 2001 séð um þróun málsins, leyfi, dreifingu, Python-ráðstefnur o.s.frv.

Frá upphafi var markmiðið að búa til einfalt og auðlært forritunarmál, sem væri þannig að oftast væri bara ein augljós og einföld leið til að útfæra tiltekna aðgerð eða reikninga. Forrit áttu að samanstanda af enskum orðum að mestu leyti en ekki samansuðu tákna eins og algengt er t.d. í Perl-forritum, sem minna á blótsyrði í Andrés-blaði.

.. figure:: myndir/perl.png
   :align: center
   :figwidth: 10cm

   Perl-forrit og Andrés Önd
.. _pakkar:

Fallasafn og pakkar
-------------------
Með Python fylgir viðamikið fallasafn (*standard library*) og auk þess eru til ótal viðbætur sem kallast **pakkar** (*packages*) og eru ekki hluti af hinu eiginlega forritunarmáli. Opinber `pakkavefur <https://pypi.org>`_ fyrir Python hefur 322.000 pakka í ágúst 2021, og hann fer ört vaxandi (voru 164.000 í janúar 2019). Fallasafnið samanstendur af mörgum **einingum** (*modules*), og það sama gildir um flesta pakka. Það er sama hvort ætlunin sé að tengjast Oracle gagnagrunni, búa til vefsíðu, skrifa tölvuleik eða leysa stærðfræðileg verkefni: maður getur alltaf fundið vandaðan og almennan Python-pakka í verkið. Síðar í þessum nótum verður fjallað um nokkra slíka m.a. NumPy (fyrir vigur- (*vector-*) og fylkjareikninga), SciPy (fyrir reiknifræði), Pandas (fyrir gagnavinnslu) og Matplotlib (til að teikna).

Útbreiðsla
----------
Ýmsir vefir mæla vöxt og vinsældir forritunarmála og mælist Python í efstu sætunum á þeim flestum, ásamt Javascript, Java, C, C# og C++. Á einum þeirra má t.d. finna eftirfarandi mynd:

.. figure:: myndir/python-vöxtur.png
   :align: center

   Vöxtur í vinsældum Python

Framkvæmd forrita
-----------------
Python er túlkað forritunarmál sem þýðir að forrit eru ekki þýdd fyrirfram á vélamál, heldur eru skipanir þess lesnar af Python túlkinum hver á fætur annarri og framkvæmdar jafnóðum. Hægt er að hugsa sér að túlkurinn hermi eftir ímynduðum gjörva sem hefur Python sem móðurmál. Þetta er reyndar nokkur einföldun, því Python er venjulega þýtt yfir á millimál sem er fljótlegra að túlka. Túlkuð forrit keyra hægar en þýdd, en á móti kemur að ekki þarf að bíða eftir þýðingu, og auk þess fylgja ýmsir kostir fyrir villuleit og þróun forrita skref fyrir skref.

Gildi eru töguð en breytur ekki
-------------------------------
Eitt sem skilur Python frá ýmsum öðrum forritunarmálum, t.d. Java og C, er að það er engin þörf á að skilgreina breytur fyrirfram og segja Python-kerfinu af hvaða tagi (*type*) þær séu. Vissulega hefur Python allskyns tög (*types*), heiltölur, kommutölur, strengi, vigra, mengi o.s.frv., en það eru gildin sem breyturnar fá sem hafa tög, en ekki breyturnar sjálfar. Forrit getur haft skipun :code:`x = 3.5`, og þá verður x kommutala, og neðar getur svo staðið :code:`x = {2, 5, 8}` og eftir það er x mengi.

.. _python-leiðbein-á-netinu:
     
Python-leiðbeiningar á netinu
-----------------------------
Fjölmargar leiðbeiningar um Python má finna á netinu, stuttar og langar, ókeypis og til sölu. Hér eru nokkrar gjaldfrjálsar:

- `Think Python <https://greenteapress.com/wp/think-python-2e/>`_ (ókeypis byrjendakennslubók sem hefur verið kennd í Tölvunarfræði 1a)
- `Google's Python Class <https://developers.google.com/edu/python/>`_ (líka fyrir byrjendur)
- `Learn Python <https://www.learnpython.org/>`_ (með reitum til að keyra forrit og skoða úttak)
- `The Python Tutorial <https://docs.python.org/3/tutorial/index.html>`_ (opinberar Python leiðbeiningar á python.org, fyrir svolítið lengra komna)
