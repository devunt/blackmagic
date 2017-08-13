#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import with_statement


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='blackmagic',
    packages=['blackmagic'],
    version='0.0.2',
    description='A Python black magic library.',
    url='https://github.com/devunt/blackmagic',
    download_url='',
    author='Bae Junehyeon',
    author_email='devunt' '@' 'gmail.com',
    license='MIT License (MIT)',
    py_modules=['blackmagic'],
    keywords=['magic', 'hack'],
    install_requires=[],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Debuggers',
    ],
)
