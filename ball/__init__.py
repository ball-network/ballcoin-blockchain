from __future__ import annotations

from pkg_resources import DistributionNotFound, get_distribution, resource_filename
# get_distribution("ballcoin-blockchain").version
try:
    __version__ = get_distribution("ballcoin-blockchain").version
except DistributionNotFound:
    # package is not installed
    __version__ = "unknown"

PYINSTALLER_SPEC_PATH = resource_filename("ball", "pyinstaller.spec")
