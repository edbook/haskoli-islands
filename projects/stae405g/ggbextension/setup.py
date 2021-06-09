#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains a Sphinx extension to embed Geogebra applets. It defines a directive "ggb".
'''

requires = ['Sphinx>=0.6', 'setuptools']


setup(name='ggbextension',
      version='0.3',
      description='Sphinx geogebra applet extension',
      author='Solrun Einarsdottir',
      author_email='solrun.einarsdottir@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      install_requires=requires,
      namespace_packages=['ggbextension'],
     )
