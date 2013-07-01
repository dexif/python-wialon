#!/usr/bin/env python
from setuptools import setup, find_packages

import wialon

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
    ]

KEYWORDS = 'wialon remote api wrapper'

setup(name='python-wialon',
      version=wialon.__version__,
      description="""Wialon Remote API wrapper for Python.""",
      long_description=open('README.md').read(),
      author=wialon.__author__,
      url='https://github.com/wialon/python-wialon',
      packages=find_packages(),
      download_url='http://pypi.python.org/pypi/python-wialon/',
      classifiers=CLASSIFIERS,
      keywords=KEYWORDS,
      zip_safe=True,
      install_requires=['simplejson'],
      py_modules=['python-wialon']
)