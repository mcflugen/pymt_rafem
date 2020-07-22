#! /usr/bin/env python
import pkg_resources

__version__ = pkg_resources.get_distribution("pymt_rafem").version


from .bmi import Rafem

__all__ = [
    "Rafem",
]
