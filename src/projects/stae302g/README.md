# Instructions

This is a template for a web-based textbook/lecture notes for the University of Iceland's mathematics department, using sphinx (see sphinx-doc.org).

For ubuntu based distors run the following commands in the terminal:

```bash
sudo apt-get install python3-sphinx
sudo apt-get install python3-sphinx-rtd-theme
sudo apt-get install python3-setuptools
sudo apt-get install python3-sagecell
sudo apt-get install git
sudo apt-get install pandoc
git clone https://github.com/edbook/template
```
There should now be a template folder in /home/user.

For Windows users the packages from above can be downloaded using [pip](https://pypi.org/project/pip/)

Navigate to the template folder.
The following folders are in the template folder: 

* sagecell-extension
* toggleblock-extension
* ggbextension
* google-analytics
* hoverrole
* katex-extension
* panoptoextension
* datacamp-extension

In each of these folders run the following commands:

Mac/Linux: 
```bash
python3 setup.py build
sudo python3 setup.py install
```

Alternatively you can run the following to install every extension in one go, list of extensions can be found and modified in the file `extension_names`:
```bash
make extensioninstall
```

Or for each one
```bash
make singleinstall EX=name_of_extension
```

Windows:
```bash
python setup.py build
python setup.py install
```

Alternatively you can run the following to install every extension in one go, list of extensions can be found and modified in the file `extension_names`
```bash
make extensioninstall
```

Or for each one
```bash
make extensioninstall name_of_extension
```

Finally you should be able to run the command:
```bash
make html
```
You should be able to produce the html files according to the .rst documents.

If you get: `WARNING: extension 'sagecell.sagecell' has no setup() function; is it really a Sphinx extension module?`, go to sagecell-extension and run: 
```
sudo python3 setup.py install --user
```

You can now edit the template in /template/chapter01.rst and compile the html file with the make html command. The html pages are in /template/_build/html.

Once you have edited your content run `make clean` before you build again with `make html`

Sphinx
======
Information on how to install sphinx can be found here: http://sphinx-doc.org/latest/install.html

Instructions for getting started with sphinx are here: http://sphinx-doc.org/latest/tutorial.html

This template comes with a source directory, `conf.py` file with the values set as we found convenient for Mathematical Analysis I (the aprropriate project title and author name need to be inserted in certain places in the file), makefile, and a slightly modified version of the Read the Docs theme (https://docs.readthedocs.org/en/latest/theme.html) with Icelandic language settings and the Univeristy of Iceland and Raunvísindadeilds logos. It is therefore not necessary to run sphinx-quickstart to set up the project.


Pandoc
======
Sphinx generates html and latex files from rst files.
Pandoc can be used to convert files from tex to rst (and convert between many other filetypes) 

Information on pandoc installation can be found at http://pandoc.org/installing.html.

A command like the following can then be used to convert latex to rst (more info at http://pandoc.org):

pandoc -t rst filename.tex -o filename.rst

A few things to have in mind when using pandoc to convert latex to rst:

-   The conversion ignores commands such as \block, \frame, \theorem, and \proof
    You might want to replace such commands with \section, \subsection, \subsubsection, \paragraph, \subaparagraph before conversion.

-   math ($...$) within bold/italicized text sections


Sphinx extensions
=================
Many extensions have been written to add features and modifications to sphinx projects. 
Several extensions come bundled with sphinx: http://sphinx-doc.org/extensions.html

For the custom extensions see README in each folder.

