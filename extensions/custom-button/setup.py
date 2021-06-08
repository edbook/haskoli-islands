#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_namespace_packages

long_desc = """
TODO: write description
"""

requires = ["Sphinx>=0.6", "setuptools"]


setup(
    name="custom-button",
    version="0.1",
    description="Unknow",
    author="Unknow",
    author_email="Unknow",
    # packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    packages=find_namespace_packages(include=["custom_button.*"]),
    namespace_packages=["custom_button"],
)
