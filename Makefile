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
	@echo "  autobuild  run development server with hot reload on changes, e.g. make autobuild project=undirbuningur_stae"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to check all external links for integrity"

install:
	poetry install
update:
	poetry update

build-all:
	poetry run cli build $(SPHINXOPTS) $(O)
autobuild:
	sphinx-autobuild $(PROJECTSDIR)/$(project) $(BUILDDIR)/$(project) $(SPHINXOPTS) $(O)
build:
	$(SPHINXBUILD) $(PROJECTSDIR)/$(project) $(BUILDDIR)/$(project) $(SPHINXOPTS) $(O)
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."
latex:
	$(SPHINXBUILD) $(PROJECTSDIR)/$(project) $(BUILDDIR)/$(project)/latex -v -b latex $(O)
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/$(project)/latex."
	@echo "Run \`make' in that directory to run these through (pdf)latex" \
		  "(use \`make latexpdf' here to do that automatically)."
latexpdf:
	$(SPHINXBUILD) $(PROJECTSDIR)/$(project) $(BUILDDIR)/$(project)/latex -v -b latex $(O)
	@echo "Running LaTeX files through pdflatex..."
	$(MAKE) -C $(BUILDDIR)/$(project)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/$(project)/latex."
changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."
linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
		  "or in $(BUILDDIR)/linkcheck/output.txt."
