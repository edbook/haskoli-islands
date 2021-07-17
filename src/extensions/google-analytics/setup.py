#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
A Sphinx Extension implementing Google Analytics and 
(optionally) a custom scroll depth extension.
'''

requires = ['Sphinx>=0.6', 'setuptools']


setup(name='google-analytics',
      version='1.0',
      description='Sphinx google-analytics extension',
      author='Simon Bodvarsson and Arnor Petur Marteinsson',
      author_email='simonb92@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      install_requires=requires,
      namespace_packages=['analytics'], 
     )
