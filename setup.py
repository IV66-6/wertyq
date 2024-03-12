#!/usr/bin/env python3

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="casl",
    version="1.0",
    author="Hiroyuki Ohsaki",
    author_email="ohsaki@lsnl.jp",
    description="a simple implementation of CASL assembler/COMET simulator in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/h-ohsaki/casl",
    packages=setuptools.find_packages(),
    install_requires=['perlcompat', 'tbdump'],
    scripts=['casl', 'comet'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
