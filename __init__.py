'''
Border Tracing Package
----------------------
Provides algorithms for tracing the borders of polygonal tilings represented as adjacency graphs.

Author: Tonatiuh Matos-Wiederhold
License: MIT
'''

from .tracing import BorderTracer, BorderTracingError

__version__ = "0.1.0"
__author__ = "Tonatiuh Matos-Wiederhold"
__all__ = ["BorderTracer"]