# -*- coding: utf-8 -*-

import io
from setuptools import setup, find_packages

long_desc = """
    Sphinx extension using KaTeX to render instead of MathJax with custom functionality. Based largely 
    on (https://github.com/hagenw/sphinxcontrib-katex) and the built in mathjax extension for Sphinx
    """

setup(
    name='katex-extension',
    license='MIT',
    author='Arnór Pétur Marteinsson',
    long_description=long_desc,
    zip_safe=False,
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires="sphinx>=1.7",
    namespace_packages=['katex'],
)
