Undirbúningur
=============

Anaconda
--------

Fyrsta verk er að setja upp `Conda <https://conda.io>`_ sem er pakkastjóri 
fyrir Python og fleiri forritunarmál. Hentugast er að gera það 
með því að setja upp 
`Anaconda <https://anaconda.org>`_ eða 
`Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_. 
Miniconda er minni og dugar fínt hér. En fyrir þau sem ætla að nota 
Python í vísindalega útreikninga þá er Anaconda hugsanlega álitlegra, 
sjá `Anaconda vs. Miniconda <https://docs.conda.io/projects/conda/en/stable/user-guide/install/download.html#anaconda-or-miniconda>`_.

Hægt er að hlaða þeim niður hér:

* Miniconda: https://docs.conda.io/en/main/miniconda.html#latest-miniconda-installer-links

* Anaconda: https://docs.anaconda.com/anaconda/install/


Pakkastjórar
~~~~~~~~~~~~

Einnig er mögulegt að nota pakkastjóra til að setja upp Miniconda/Anaconda. 

Á Windows er hægt að nota `Winget <https://learn.microsoft.com/en-us/windows/package-manager/winget/>`_, 
þ.e. opna skjhermi (terminal) og skrifa

.. code-block::
   
    winget install --id=Anaconda.Miniconda3  -e

eða 

.. code-block::

   winget install -e --id Anaconda.Anaconda3

Sambærilegar skipanir eru til í flestum Linux-útgáfum. 

Ritill 
------

Við þurfum einhvern góðan textaritil, t.d. `Visual Studio Code <https://code.visualstudio.com/>`_.
En einnig má nota *Vim*, *Nvim*, *Emacs*, *Sublime* o.s.frv.

Git
---

Næsta mál er að setja upp `Git <https://git-scm.com/>`_. Það má gera það hvort sem er með 
því að hlaða forritinu niður hér, https://git-scm.com/download/win, eða með því að nota
pakkastjóra

.. code-block::

    winget install -e --id Git.Git

Sambærilegar skipanir eru til í flestum Linux-útgáfum:

.. code-block::

    apt-get install git

og þeir sem nota Homebrew á MacOS keyra:

.. code-block::

    brew install git

.. youtube:: 2ReR1YJrNOM
