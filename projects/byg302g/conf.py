from edbook.conf import *  # type: ignore
extensions.append('sphinxcontrib.bibtex')
extensions.remove('sphinxcontrib.hoverrole')
bibtex_bibfiles = ['refs.bib']
