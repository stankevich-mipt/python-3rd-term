from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        ['primes/primes_cython.pyx',     # Cython code file with primes() function
         'primes/primes_python.pyx'], 
        annotate=True),                 # enables generation of the html annotation file
)