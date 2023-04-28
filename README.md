![edbook](https://github.com/edbook/haskoli-islands/actions/workflows/push.yml/badge.svg)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/edbook/haskoli-islands?label=version)

# Edbook

This is a framework for a web-based textbook/lecture notes for the University of Iceland. It uses Sphinx (https://sphinx-doc.org) with custom extensions and configurations. The notes are hosted on https://edbook.hi.is and they are automatically compiled by Github and uploaded to https://edbook.hi.is on merge.  

The notes share common configuration, [settings.py](cli/edbook/conf/settings.py), but individual settings can be inserted into conf.py in each project. Every project has a config.yml file which contains it variables (name, author, etc). 

# Usage

For detailed instroctions on how to add notes see https://edbook.hi.is/tmp001g/. 


The boiled down versions it the following: 

After cloning the repository. Setup a Conda virtual environment:

```bash
conda env create -f environment.yml
```
Note you have to install Conda (Miniconda3/Anaconda) first, see https://docs.conda.io/en/main/miniconda.html. 

## Building projects

You can build all projects or a particular project by passing the folder name as an argument, like so:

```bash
edbook build-all
```

```bash
edbook build undirbuningur_stae
```

## Run development server

Run a dev server for local development. This will open a tab in your browser at http://localhost:8000 which will update each time you you save a document in the project being worked on in the [source](projects) directory. The build ends up in the `_build/your-project` where `your-project` is the project you are building. For example

```bash
edbook build undirbuningur_stae --auto
```

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

When the project owners merge the pull request to main an automatic release will be created and deployed to production, that is compiled and uploaded to https://edbook.hi.is.

## Sphinx

Instructions for getting started with sphinx are [here](http://sphinx-doc.org/latest/tutorial.html)

Many Sphinx extensions have been written to add features and modifications to sphinx projects, they can be found at https://github.com/edbook/. 

Other extensions used come bundled with sphinx, see [Sphinx extensions](http://sphinx-doc.org/extensions.html), or are hosted at [Sphinx-contrib](https://github.com/sphinx-contrib).

## Pandoc

Sphinx generates html and latex files from rst files.
Pandoc can be used to convert files from tex/pptx/odt/... to rst (and convert between many other filetypes).

Information on Pandoc installation can be found in the [Pandoc installation guide](http://pandoc.org/installing.)html.

A command like the following can then be used to convert latex to rst, see the [Pandoc docs](http://pandoc.org):

```bash
pandoc -t rst filename.tex -o filename.rst
```

A few things to have in mind when using pandoc to convert latex to rst:

- The conversion ignores commands such as \block, \frame, \theorem, and \proof
  You might want to replace such commands with \section, \subsection, \subsubsection, \paragraph, \subaparagraph before conversion.

- math ($...$) within bold/italicized text sections

## CI/CD

Pipelines are run on each push to a pull request. The checks must pass before merging to main is possible.
