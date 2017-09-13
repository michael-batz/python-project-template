#!/usr/bin/env python
"""
name - <short discription>

<long discription>

free software: you can redistribute it and/or modify
it under the terms of the MIT License as published by
the Massachusetts Institute of Technology

You should have received a copy of the MIT License along with core.
If not, see <https://opensource.org/licenses/MIT>.

@package sample
@author "name <email>"
@since date/version
"""

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='1.0.0',
    description='sample projecte',
    long_description=readme,
    author='author',
    author_email='email',
    url='https://github.com/michael-batz/python-project-template',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
