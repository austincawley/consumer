#!/usr/bin/env python

import re
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand
from codecs import open


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


with open('consumer/__init__.py', 'r') as fd:
    contents = fd.read()
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        contents, re.MULTILINE).group(1)
    package_title = re.search(r'^__title__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        contents, re.MULTILINE).group(1)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

with open('requirements.txt', 'r', 'utf-8') as f:
    requirements = f.read().splitlines()

test_requirements = ['pytest>=2.8.0', 'pytest-cov']
# Remove test_requirements from install requirements
requirements = list(set(requirements) - set(test_requirements))

packages = [package_title]

setup(
    name=package_title,
    version=version,
    description='API consumption that gets you.',
    long_description=readme,
    author='Austin Cawley-Edwards',
    author_email='austin.cawley@gmail.com',
    url='https://github.com/austincawley/consumer',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'consumer': 'consumer'},
    include_package_data=True,
    install_requires=requirements,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),
    cmdclass={'test': PyTest},
    tests_require=test_requirements,
    extras_require={
        # 'socks': ['PySocks>=1.5.6, !=1.5.7'],
    },
)