#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of twittergeo.
# https://github.com/fitnr/twittergeo

# Licensed under the GNU General Public License v3 (GPLv3) license:
# http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

from setuptools import setup, find_packages

try:
    readme = open('readme.rst').read()
except IOError:
    readme = ''

setup(
    name='twittergeo',
    version='0.1.0',
    description='Export twitter searches to geoJSON',
    long_description=readme,
    keywords='twitter geo cli',
    author='Neil Freeman',
    author_email='contact@fakeisthenewreal.org',
    url='https://github.com/fitnr/twittergeo',
    license='GNU General Public License v3 (GPLv3)',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3) License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        'twitter_bot_utils>=0.9,<0.10',
    ],

    extras_require={
        'tests': [
            'coverage',
            'tox',
        ],
    },

    entry_points={
        'console_scripts': [
            'twittergeo=twittergeo.cli:main',
        ],
    },
)
