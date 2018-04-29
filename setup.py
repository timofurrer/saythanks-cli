#!/usr/bin/env python
"""
saythanks-cli
~~~~~~~~~~~~~

Say Thanks via Command Line Interface.

Uses Kenneth's saythanks.io service.

:copyright: by Timo Furrer <tuxtimo@gmail.com>
:license: MIT, See LICENSE for more details.
"""

import os
import sys
import codecs
from shutil import rmtree

from setuptools import setup, Command


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel upload")
    sys.exit()

required = [
    'click',
    'requests'
]


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds...')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution...')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(
            sys.executable))

        self.status('Uploading the package to PyPi via Twine...')
        os.system('twine upload dist/*')

        sys.exit()


setup(
    name='saythanks-cli',
    version='1.0.0.a2',
    description='Say Thanks via Command Line Interface.',
    long_description=long_description,
    author='Timo Furrer',
    author_email='tuxtimo@gmail.com',
    url='https://github.com/timofurrer/saythanks-cli',
    install_requires=required,
    py_modules=['saythanks_cli'],
    entry_points={
        'console_scripts': [
            'thx = saythanks_cli:cli'
    ]},
    license='MIT',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
    cmdclass={
        'upload': UploadCommand,
    },
)
