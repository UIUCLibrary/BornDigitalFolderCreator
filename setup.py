from setuptools import setup, find_packages

setup(
    name='CreateFolders',
    version='0.0.1',
    packages=['BDCreateFolders', "tests"],
    # packages=['BDCreateFolders', "tests"],
    entry_points={'console_scripts': ['createfolders = BDCreateFolders.__main__:main']},
    test_suite="tests",
    url='',
    license='',
    author='Henry Borchers',
    author_email='',
    description='Generates folders based on a CSV exported from MEDUSA',
    zip_safe=False
)
