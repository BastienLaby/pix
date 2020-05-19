import os
import sys
import re

from helloworld import __version__ as version

readme = os.path.join(os.path.dirname(__file__), "README.md")
with open(readme) as f:
    long_description = f.read()

SETUP_ARGS = dict(
    name="pix.py",
    version=version
    descriptions=("Graphical API to draw pixels on a grid"),
    long_description=long_description,
    url="https://github.com/<login>/pix,
    author="Bastien Laby",
    email="bastien.laby@gmail.com",
    license="MIT",
    include_package_data=True,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8"
    ],
    py_modules = ["pix"],
    install_requires = [
        "requests>=2.22"
    ]
)


if __name__ == "__main__":
    from setuptools import setup, find_packages

    SETUP_ARGS["packages"] = find_packages()
    setup(**SETUP_ARGS)