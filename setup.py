#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of twittergeo.
# https://github.com/fitnr/twittergeo

# Licensed under the GNU General Public License v3 (GPLv3) license:
# http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

from setuptools import setup

try:
    readme = open('readme.rst').read()
except IOError:
    readme = open('readme.md').read()

setup(
    name='twittergeo',
    version='0.1.1',
    description='Export Twitter searches to GeoJSON',
    long_description=readme,
    keywords='twitter geo cli',
    author='Neil Freeman',
    author_email='contact@fakeisthenewreal.org',
    url='https://github.com/fitnr/twittergeo',
    license='GNU General Public License v3 (GPLv3)',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
    ],

    packages=['twittergeo'],

    include_package_data=False,
    install_requires=[
        'twitter_bot_utils>=0.9.1,<0.10',
    ],

    test_suite="tests",

    tests_require=[
        'mock',
    ],

    entry_points={
        'console_scripts': [
            'twittergeo=twittergeo.cli:main',
        ],
    },
)
