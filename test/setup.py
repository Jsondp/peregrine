# cython: language_level=3
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('example_cython.pyx', language_level=3))