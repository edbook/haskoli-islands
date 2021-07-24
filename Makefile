# You can set these variables from the command line.
SPHINXOPTS    = -b dirhtml
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = _build
PROJECTSDIR   = src/projects

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean changes linkcheck autobuild

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  clean      purge $(BUILDDIR)" directory
	@echo "  autobuild  run development server with hot reload on changes, e.g. make autobuild project=undirbuningur_stae"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to check all external links for integrity"

install:
	poetry install
update:
	poetry update

build-all:
	poetry run cli build
clean:
	./scripts/cleanup.sh $(PROJECTSDIR)/$(project)/$(BUILDDIR)
autobuild: clean
	sphinx-autobuild $(PROJECTSDIR)/$(project) $(PROJECTSDIR)/$(project)/$(BUILDDIR) $(SPHINXOPTS) $(O)
build: clean
	$(SPHINXBUILD) $(PROJECTSDIR)/$(project) $(PROJECTSDIR)/$(project)/$(BUILDDIR) $(SPHINXOPTS) $(O)
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."
changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."
linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."
