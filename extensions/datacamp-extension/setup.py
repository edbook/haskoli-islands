from setuptools import setup, find_packages

long_desc = """
Sphinx extension which enables embedding Datacamp windows to demonstrate Python and R capabilities
"""

requires = ["Sphinx>=0.6", "setuptools"]


setup(
    name="datacamp",
    version="1.0",
    description="Sphinx datacamp extension",
    author="Arnór Pétur Marteinsson",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=["datacamp"],
)


# breyta
