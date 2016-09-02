from setuptools import setup



setup(
    name='CreateFolders',
    version='0.0.2',
    description='Generates folders based on a CSV exported from MEDUSA',
    packages=['BDCreateFolders', "tests"],
    url='https://github.com/UIUCLibrary/BornDigitalFolderCreator',
    author='Henry Borchers',
    author_email='hborcher@illinois.edu',
    # entry_points={'console_scripts': ['createfolders = BDCreateFolders.__main__:main']},
    license='',
)
