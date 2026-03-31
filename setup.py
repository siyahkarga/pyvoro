import setuptools
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import sys, os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

ext = ".pyx" if USE_CYTHON else ".cpp"

extensions = [
    Extension("pyvoro.voroplusplus",
              sources=["pyvoro/voroplusplus" + ext,
                       "pyvoro/vpp.cpp",
                       "src/voro++.cc"],
              include_dirs=["src"],
              language="c++",
              )
]

if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions, language_level="3")

setup(
    name="pyvoro-bazan",
    version="1.0.5",
    description="2D and 3D Voronoi tessellations: a python entry point for the voro++ library.",
    author="Joe Jordan",
    author_email="joe.jordan@imperial.ac.uk",
    url="https://github.com/siyahkarga/pyvoro",
    packages=["pyvoro",],
    package_dir={"pyvoro": "pyvoro"},
    ext_modules=extensions,
    keywords=["geometry", "mathematics", "Voronoi"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: BSD License",
    ],
    test_suite="test",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
