import codecs
import glob
import os
import re

import setuptools.dist


def read(*directories):
    pathname = os.path.abspath(os.path.dirname(__file__))

    return codecs.open(os.path.join(pathname, *directories), "r").read()


def find_version(*pathnames):
    data = read(*pathnames)

    matched = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", data, re.M)

    if matched:
        return matched.group(1)

    raise RuntimeError("Unable to find version string.")

setuptools.setup(
    author="cellprofiler-dev",
    author_email="cellprofiler-dev@broadinstitute.org",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering"
    ],
    entry_points={
        "console_scripts": [
            "cellprofiler=cellprofiler.__main__:main"
        ]
    },
    extras_require={
        "build": [
            "pyinstaller",
            "twine"
        ],
        "test": [
            "pytest"
        ]
    },
    install_requires=[
        "centrosome==1.0.9",
        "docutils==0.14",
        "h5py==2.7.1",
        "inflect==0.2.5",
        "javabridge==1.0.14",
        "joblib",
        "mahotas==1.4.3",
        "matplotlib==2.0.2",
        "mysqlclient==1.3.9",
        "numpy==1.13.1",
        "prokaryote==2.3.0",
        "python-bioformats==1.3.1",
        "pyzmq==15.3.0",
        "raven==6.1.0",
        "requests==2.18.4",
        "scikit-image==0.13.1",
        "scikit-learn==0.19.0",
        "scipy==1.0.1"
        "zarr==2.3.2"
        "s3fs==0.2.2"
    ],
    license="BSD",
    name="CellProfiler",
    package_data={
        "images": glob.glob(os.path.join("data", "**", "*"))
    },
    packages=setuptools.find_packages(exclude=[
        "tests*"
    ]),
    python_requires=">=2.7, <3",
    setup_requires=[
        "pytest"
    ],
    url="https://github.com/CellProfiler/CellProfiler",
    version=find_version("cellprofiler", "__init__.py")
)
