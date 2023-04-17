![edbook](https://github.com/edbook/haskoli-islands/actions/workflows/push.yml/badge.svg)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/edbook/haskoli-islands?label=version)

# Instructions

This is a template for a web-based textbook/lecture notes for the University of Iceland's mathematics department, using sphinx (see sphinx-doc.org).

## Building projects

You can build all projects or a particular project by passing the folder name as an argument, like so:

```bash
edbook build-all
```


```bash
edbook build undirbuningur_stae
```

## Run development server

Run a dev server for local development. This will open a tab in your browser at http://localhost:8000 which will update each time you you save a document in the project being worked on in the [source](src/projects) directory. The build ends up in the `_build/your-project` where `your-project` is the project you are building.

```bash
edbook build undirbuningur_stae --auto

```

## Sagecell

All `*.sage` files should be added to `src/extensions/sagecell-extension/examples` directory so they can be reused across projects. You can continue to reference them by filename only.

## Contribute

The following rules should be followed when contributing:

- Create a branch (or fork the project if you are not already a contributor) from master
- Commit messages should follow the [Conventional Commits specs](https://www.conventionalcommits.org)

By using the _Conventional Commits specs_ the [semver](https://semver.org/) release tags _(major.minor.patch / 0.1.0)_ will be determined automatically based on the commit messages, e.g. `fix: changed some stuff` will bump the current version as a `patch` to `0.1.1`, as supposed to `feat: added a new chapter` will bump the current version as a `minor` to `0.2.0`.

Breaking changes, e.g. `BREAKING CHANGE: replacing RestructuredTEXT with Markdown in Sphinx` will bump the current version as a `major` release to `1.1.0`.

[Commitizen](https://commitizen-tools.github.io/commitizen/) already comes installed as a dev-dependency to help you out with this. Instead of using `git commit -a -m "feat: some feature"` you can use the _Committizen CLI_ which will prompt options in the terminal.

```sh
cz commit
```

**TODO: needs work**

When a pull request is opened a new [feature deployment](https://github.com/edbook/haskoli-islands/deployments) will be created and deployed to a custom url. It will be updated on each push to that pull request.

When the project owners merge the pull request to main an automatic release will be created and deployed to production.

## Install without virtualenv (not recommended)

For ubuntu based distros run the following commands in the terminal:

```bash
sudo apt-get install python3-sphinx
sudo apt-get install python3-sphinx-rtd-theme
sudo apt-get install python3-setuptools
sudo apt-get install python3-sagecell
sudo apt-get install git
sudo apt-get install pandoc
git clone https://github.com/edbook/template
```

There should now be a template folder in /home/user. The following folders are in the template folder:

- sagecell-extension
- toggleblock-extension
- ggbextension
- SphinxScrolldepth
- hoverrole

In each of these folders run the following commands:

```bash
python3 setup.py build
sudo python3 setup.py install
```

# Sphinx

Information on how to install sphinx can be found here: http://sphinx-doc.org/latest/install.html

Information on how to install sphinx can be found [here](http://sphinx-doc.org/latest/install.html)

Instructions for getting started with sphinx are [here](http://sphinx-doc.org/latest/tutorial.html)

# Pandoc

Sphinx generates html and latex files from rst files.
Pandoc can be used to convert files from tex to rst (and convert between many other filetypes)

Information on pandoc installation can be found in the [Pandoc installation guide](http://pandoc.org/installing.)html.

A command like the following can then be used to convert latex to rst, see the [Pandoc docs](http://pandoc.org):

```bash
pandoc -t rst filename.tex -o filename.rst
```

A few things to have in mind when using pandoc to convert latex to rst:

- The conversion ignores commands such as \block, \frame, \theorem, and \proof
  You might want to replace such commands with \section, \subsection, \subsubsection, \paragraph, \subaparagraph before conversion.

- math ($...$) within bold/italicized text sections

# Sphinx extensions

Many extensions have been written to add features and modifications to sphinx projects.
Several extensions come bundled with sphinx, see [Sphinx extensions](http://sphinx-doc.org/extensions.html).

Three custom extensions come with this framework (ggbextension to embed geogebra applets, toggleblock-extension for toggleable text sections and sagecell-extension to embed sage cells. See README files in the extension folders.)

## CI/CD

Pipelines are run on each push to a pull request. The checks must pass before merging to main is possible.
