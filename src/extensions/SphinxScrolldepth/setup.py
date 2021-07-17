#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
A Sphinx Extension implementing the Scroll Depth extension for Google Analytics.
'''

requires = ['Sphinx>=0.6', 'setuptools']


setup(name='scrolldepthextension',
      version='1.0',
      description='Sphinx scroll-depth extension',
      author='Simon Bodvarsson',
      author_email='simonb92@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      install_requires=requires,
      namespace_packages=['scrolldepth'], 
     )
