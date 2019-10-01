#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'OpenFisca-Interactive',
    version = '0.0.1',
    author = 'Christophe Benz',
    author_email = 'christophe.benz@jailbreak.paris',
    classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Information Analysis',
        ],
    description = 'A versatile microsimulation free software',
    keywords = 'benefit microsimulation social tax',
    license = 'https://www.fsf.org/licensing/licenses/agpl-3.0.html',
    url = 'https://github.com/cbenz/openfisca-interactive',

    # install_requires = {},
    packages = find_packages(),
)
