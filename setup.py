#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from setuptools import setup, find_packages


setup(
    name="pyIGRF",
    version="0.3.4",
    author="beth, forked from zzyztyy",
    author_email="bethkirby@gmail.com",
    description="IGRF-14 Model by Python",
    long_description=open("README.md").read(),
    license="MIT",
    url="https://github.com/Beth1708/pyIGRF",
    packages=find_packages(),
    install_requires=[
        "NumPy"
    ],
    package_data={'': ['src/igrf13coeffs.txt', 'src/igrf14coeffs.txt']}
)
