#!/usr/bin/env python
import os
import sys

__version__ = "0.0.1"

try:
    from setuptools import setup
    from setuptools.command.test import test as TestCommand

    class PyTest(TestCommand):
        def finalize_options(self):
            TestCommand.finalize_options(self)
            self.test_args = []
            self.test_suite = True

        def run_tests(self):
            # import here, because outside the eggs aren't loaded
            import pytest
            errno = pytest.main(self.test_args)
            sys.exit(errno)

except ImportError:

    from distutils.core import setup

    def PyTest(x):
        x

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
long_description = f.read()
f.close()

setup(
    name='ofo_backend',
    version=__version__,
    description='Python backend modules for One For One',
    long_description=long_description,
    url='http://github.com/1For1/backend',
    author='One For One',
    author_email='info@1for.one',
    maintainer='One For One',
    maintainer_email='info@1for.one',
    keywords=['Mongo', 'Tesseract', 'PDF', 'NLTK'],
    license='Commercial',
    tests_require=['pytest>=2.5.0'],
    cmdclass={'test': PyTest},
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Commercial',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ]
)