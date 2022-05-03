# SPDX-License-Identifier: CECILL-2.1
"""
Init file for nllgrid.

:copyright:
    2013-2022 Claudio Satriano <satriano@ipgp.fr>,
              Natalia Poiata <poiata@ipgp.fr>
:license:
    CeCILL Free Software License Agreement v2.1
    (http://www.cecill.info/licences.en.html)
"""
from .NLLGrid import NLLGrid  #NOQA
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
