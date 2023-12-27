from setuptools import find_packages, setup

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

PROJECT_NAME = "pycard"
VERSION_NUMBER = "0.0.1"
DESCRIPTION = "A free library for all things cards"

setup(
    name=PROJECT_NAME,
    version=VERSION_NUMBER,
    description=DESCRIPTION,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/Trap37/pycard",
    author="Trap37",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0"],
    },
    python_requires=">=3.11",
)
