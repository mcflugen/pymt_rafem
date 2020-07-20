from __future__ import absolute_import

import pkg_resources
from rafem import BmiRiverModule as Rafem

Rafem.__name__ = "Rafem"
Rafem.METADATA = pkg_resources.resource_filename(__name__, "data/Rafem")

__all__ = [
    "Rafem",
]
