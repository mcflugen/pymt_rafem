#! /usr/bin/env python
import os
import sys

from setuptools import Extension, find_packages, setup

entry_points = {"pymt.plugins": ["Rafem=pymt_rafem.bmi:Rafem",]}

setup(
    name="pymt_rafem",
    author="csdms",
    author_email="csdms@colorado.edu",
    description="PyMT plugin for rafem",
    long_description=open("README.rst", encoding="utf-8").read(),
    version="0.2",
    url="https://github.com/pymt-lab/pymt_rafem",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
    ],
    keywords=["bmi", "pymt"],
    install_requires=open("requirements.txt", "r").read().splitlines(),
    packages=find_packages(),
    entry_points=entry_points,
    include_package_data=True,
)
