#!/usr/bin/env python
# coding: utf-8

from setuptools import setup


setup(
    name='gandi',
    url='https://github.com/miracle2k/gandi',
    version='0.1',
    license='BSD',
    author=u'Michael Elsdörfer',
    author_email='michael@elsdoerfer.com',
    description=
        'Gandi API CLI client',
    py_modules=['gandi'],
    install_requires=['click>=2.4', 'requests>=2.3.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
    entry_points="""[console_scripts]\rgandi = gandi:cli\n""",
)
