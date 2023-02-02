#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

REQUIRED = [
    "Django",
    "pendulum",
]

setup(
    name="fantasy-football-catalog",
    description="Catalog your fantasy football teams!",
    python_requires=">=3.10.0",
    packages=find_packages(exclude=("tests*",)),
    setup_requires=[],
    tests_require=[],
    install_requires=REQUIRED,
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
    ],
)
