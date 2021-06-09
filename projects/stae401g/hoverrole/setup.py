#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains a Sphinx extension to embed mouse-over translations of mathematical terms from
Icelandic to English (or vice versa). It defines a role :hover:
'''

requires = ['Sphinx>=0.6', 'setuptools']


setup(name='hoverroleextension',
      version='1.10',
      description='Sphinx mouse-over translation extension',
      author='Simon Bodvarsson',
      author_email='simonb92@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      install_requires=requires,
      namespace_packages=['hoverrole'], 
     )
