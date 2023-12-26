from setuptools import find_packages, setup

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="Pycard",
    version="0.0.1",
    description="A free library for all things cards",
    packages=find_packages(),
    long_description=LONG_DESCRIPTION,
    url="https://github.com/Trap37/Pycard",
    author="Trap37",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires=[""],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0"],
    },
    python_requires=">=3.11",
)
