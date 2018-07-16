#! /usr/bin/env python
import os, sys

from setuptools import setup, find_packages

# from Cython.Build import cythonize
from distutils.extension import Extension
import numpy as np
import versioneer

from model_metadata.utils import get_cmdclass, get_entry_points


ext_modules = None
packages = None

pymt_components = [
    (
        "Rafem=rafem:BmiRiverModule",
        "meta",
    )
]

setup(
    name="pymt_rafem",
    author="Eric Hutton",
    description="Python interface to rafem",
    version=versioneer.get_version(),
    setup_requires=["cython"],
    ext_modules=ext_modules,
    packages=packages,
    cmdclass=get_cmdclass(pymt_components, cmdclass=versioneer.get_cmdclass()),
    entry_points=get_entry_points(pymt_components),
)
