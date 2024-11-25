# 
# setup.py : pyvoro python interface to voro++
# 
# this extension to voro++ is released under the original modified BSD license
# and constitutes an Extension to the original project.
#
# Copyright (c) Joe Jordan 2012
# contact: <joe.jordan@imperial.ac.uk> or <tehwalrus@h2j9k.org>
#

import setuptools
from setuptools import setup, Extension
# Read the long description from the README file
# Read the long description from the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
# fall back to provided cpp file if Cython is not found
extensions = [
    Extension("pyvoro.voroplusplus",
              sources=["pyvoro/voroplusplus.cpp",
                       "pyvoro/vpp.cpp",
                       "src/voro++.cc"],
              include_dirs=["src"],
              language="c++",
              )
]

setup(
    name="pyvoro-bazan",
    version="1.0.2",
    description="2D and 3D Voronoi tessellations: a python entry point for the voro++ library.",
    author="Joe Jordan",
    author_email="joe.jordan@imperial.ac.uk",
    url="https://github.com/siyahkarga/pyvoro",
    #download_url="https://github.com/joe-jordan/pyvoro/tarball/v1.3.4",
    packages=["pyvoro",],
    package_dir={"pyvoro": "pyvoro"},
    ext_modules=extensions,
    keywords=["geometry", "mathematics", "Voronoi"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",  # Add Windows support
        "Operating System :: MacOS",                  # Add macOS support
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: BSD License",
    ],
    test_suite="test",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
