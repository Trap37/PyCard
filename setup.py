from setuptools import setup, find_packages

setup(
    name='PyCard',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'random',
        'itertools',
    ],
    author='Patrick Farrell',
    description='A card game library',
    url='https://github.com/Trap37/PyCard',
)
