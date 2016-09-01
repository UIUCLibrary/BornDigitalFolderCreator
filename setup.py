from setuptools import setup, find_packages

import sys
from setuptools.command.test import test as TestCommand
class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        # self.pytest_args.append("--doctest-modules")
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='CreateFolders',
    version='0.0.2',
    packages=['BDCreateFolders', "tests"],
    # packages=['BDCreateFolders', "tests"],
    entry_points={'console_scripts': ['createfolders = BDCreateFolders.__main__:main']},
    test_suite="tests",
    tests_require=['pytest'],
    cmdclass = {'test': PyTest},
    url='',
    license='',
    author='Henry Borchers',
    author_email='',
    description='Generates folders based on a CSV exported from MEDUSA',
    zip_safe=False
)
