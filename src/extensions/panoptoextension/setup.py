#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains a Sphinx extension to embed Panopto applets. It defines a directive "panopto".
'''

requires = ['Sphinx>=0.6', 'setuptools']


setup(name='panoptoextension',
      version='1.0',
      description='Sphinx panopto applet extension',
      author='Solrun Einarsdottir',
      author_email='solrun.einarsdottir@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      install_requires=requires,
      namespace_packages=['panoptoextension'],
     )
