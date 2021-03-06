#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
    'click'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='bilge',
    version='0.1.0',
    description="Get rid of useless file buildup without causing problems",
    long_description=readme + '\n\n' + history,
    author="Steven Brien",
    author_email='spbrien@gmail.com',
    url='https://github.com/spbrien/bilge',
    packages=[
        'bilge',
    ],
    package_dir={'bilge':
                 'bilge'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='bilge',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points='''
        [console_scripts]
        bilge=bilge.bilge:cli
    '''
)
