﻿"""
Python scripting interface for Comsol Multiphysics
"""

# Meta information
__title__     = 'MPh'
__version__   = '0.7.2'
__date__      = '2020–05–18'
__author__    = 'John Hennig'
__copyright__ = 'John Hennig'
__license__   = 'MIT'

# Public interface
from .model   import Model
from .client  import Client
from .server  import Server
from .backend import inspect
