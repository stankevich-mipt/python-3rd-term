from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("fibonacci/fib.pyx"), language_level = "2"
)