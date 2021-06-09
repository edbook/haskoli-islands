#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains a Sphinx extension to make text blocks toggleable. It defines two directives "begin-toggle" and "end-toggle".
'''

requires = ['Sphinx>=0.6', 'setuptools']


setup(name='toggleblock',
      version='0.5',
      description='Sphinx extension',
      author='Solrun Einarsdottir',
      author_email='solrun.einarsdottir@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      install_requires=requires,
      namespace_packages=['toggleblock'],
     )

