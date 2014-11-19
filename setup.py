#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


setup(
    name='dj-haystack-url',
    version='0.1.0',
    description='Haystack configuration from environment variable',
    long_description=readme + '\n\n' + history,
    author='Piper Merriam',
    author_email='piper@simpleenergy.com',
    url='https://github.com/simpleenergy/dj-haystack-url',
    py_modules=[
        'dj-haystack-url',
    ],
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords='dj-haystack-url',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
