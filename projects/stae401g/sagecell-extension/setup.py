#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains a Sphinx extension for embedding sage cells.
It is based on Krzysztof Kajda's sage cell server extension (https://github.com/kriskda/sphinx-sagecell).

The extension defines a directive, "sagecell", for embedding sage cells.
'''

requires = ['Sphinx>=0.6', 'setuptools']


setup(name='sagecell',
      version='1.2',
      description='Sphinx sagecell extension',
      author='Solrun Einarsdottir',
      packages=find_packages(),
      include_package_data=True,
      install_requires=requires,
      namespace_packages=['sagecell'],
     )


#breyta
