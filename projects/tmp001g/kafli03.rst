Nýtt verkefni
=============


Nýtt verkefni búið til
----------------------

Ef allt hefur gengið að óskum og búið er að virkja ``edbook``-umhverfið í conda þá er hægt að búa til nýtt verkefni með skipuninni

.. code-block::

    edbook create 

Þá er beðið um *Course id* sem allajafna er númerið á námskeiðinu sem nóturnar tilheyra
 (hér er skynsamlegast að nota ekki séríslenska stafi), 
*Course name* sem er nafn á námskeiðinu og svo höfund ásamt netfangi.

Við þetta verður til mappa undir *projects* sem heitir námskeiðssnúmerinu og inniheldur allt sem þarf til að geta byrjað. 

.. note::

    Í möppunni er skrá sem heitir *config.yml* og heldur utanum upplýsingar um nóturnar. Ef það eru fleiri en einn
    höfundur þá er hægt að opna þá skrá og bæta þeim við. Til dæmis ef höfundar eru tveir: 

    .. code-block::

        authors: 
            - email: jon@hi.is 
              name: Jónmundur Gunnuson
            - email: gunna@hi.is
              name: Gunna Jónmundsdótir 

Nýt Git-grein
-------------

Það telst ekki góð latína að vinna á *main*-greininni á Git. Það er því ráðlagt að búa til 
nýja grein (branch) fyrir nýja verkefnið. Í VSCode er smellt á *Main* neðst til vinstri, 
skrifið nafnið á verkefninu (ef um er að ræða nótur fyrirnámskeið þá er númerið á því upplagt
nafn) og smellið á *Create new branch*. Framvegis er svo hægt að fylgjast með neðst til vinstri 
í hvaða grein er verið að vinna.

.. image:: myndir/vscode-branch.png

Unnið er með Git í VSCode
~~~~~~~~~~~~~~~~~~~~~~~~~

.. youtube:: i_23KUAEtUM

Edbook-skipunin
---------------

*Edbook*-skipunin sem við notuðum til að búa til nýtt verkefni getur gert fleira. 

.. code-block::

   edbook list

gefur lista með öllum verkefnunum.
 

.. code-block::
   edbook build bla001g

kompælar bla001g-verkefninu og setur útkomuna í möppuna *_build/bla001g*. 

Einnig er hægt að kompæla sjálfkrafa, þannig að útkoman er uppfærð í hvert skipti sem skrárnar í henni eru vistaðar. 
Til þess notum við

.. code-block::

   edbook build bla001g --auto

Með því að opna http://127.0.0.1:8000 í vafra þá sjáum við útkomuna. 

Að lokum er hægt að kompæla öll verkefnin með því að keyra 

.. code-block::

   edbook build-all

