# read version from installed package
from importlib.metadata import version

from .qmsspkg import catbind

__version__ = version("qmsspkg")
