from setuptools import setup



setup(
    name='CreateFolders',
    version='0.0.2',
    packages=['BDCreateFolders', "tests"],
    entry_points={'console_scripts': ['createfolders = BDCreateFolders.__main__:main']},
    test_suite="tests",
    url='https://github.com/UIUCLibrary/BornDigitalFolderCreator',
    license='',
    author='Henry Borchers',
    author_email='hborcher@illinois.edu',
    description='Generates folders based on a CSV exported from MEDUSA',
    zip_safe=False
)
