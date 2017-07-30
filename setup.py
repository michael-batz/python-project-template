"""
<sampleproject> setup

This is the setup of <sampleproject>


:license: MIT, see LICENSE for more details
:copyright: (c) 2017 by <name>, see AUTHORS for more details
"""

from setuptools import find_packages
from setuptools import setup

setup(
    # project metadata
    name="sampleproject",
    description="A sample project",
    url="https://github.com/michael-batz/python-project-template",
    author="<name>",
    author_email="<mail>",

    # version
    version="1.0.0",

    # license
    license="MIT",

    # classfication
    classifiers=[],

    # add packages and additional files
    packages=find_packages(),
    data_files=[]
)
