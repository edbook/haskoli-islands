from setuptools import setup, find_packages

setup(
    name="edbook",
    version="0.2.0",
    author="Jon Levy",
    author_email="nonni@nonni.cc",
    license="MIT",
    description="desc",
    url="https://github.com/edbook",
    packages=find_packages(),
    python_requires=">=3.10.10",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    entry_points="""
        [console_scripts]
        edbook=edbook.main:app
    """,
)
