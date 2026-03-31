from setuptools import setup, Extension
from Cython.Build import cythonize
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

extensions = [
    Extension("pyvoro.voroplusplus",
              sources=["pyvoro/voroplusplus.pyx",
                       "pyvoro/vpp.cpp",
                       "src/voro++.cc"],
              include_dirs=["src"],
              language="c++",
              )
]

setup(
    name="pyvoro-bazan",
    version="1.0.4",
    description="2D and 3D Voronoi tessellations: a python entry point for the voro++ library.",
    author="Joe Jordan",
    author_email="joe.jordan@imperial.ac.uk",
    url="https://github.com/siyahkarga/pyvoro",
    packages=["pyvoro"],
    package_dir={"pyvoro": "pyvoro"},
    ext_modules=cythonize(extensions, language_level="3"),
    keywords=["geometry", "mathematics", "Voronoi"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
