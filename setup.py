import codecs
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


def package_data():
    resources = []

    for root, _, filenames in os.walk(os.path.join("cellprofiler", "data")):
        resources += [
            os.path.relpath(os.path.join(root, filename), "cellprofiler")
            for filename in filenames
        ]

    for root, _, filenames in os.walk(os.path.join("cellprofiler", "gui")):
        resources += [
            os.path.relpath(os.path.join(root, filename), "cellprofiler")
            for filename in filenames
            if ".html" in filename
        ]

    return {"cellprofiler": resources}


setuptools.setup(
    author="cellprofiler-dev",
    author_email="cellprofiler-dev@broadinstitute.org",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering",
    ],
    entry_points={"console_scripts": ["cellprofiler=cellprofiler.__main__:main"]},
    extras_require={
        "build": ["pyinstaller", "twine"],
        "docs": ["Sphinx>=3.1.1", "sphinx-rtd-theme>=0.5.0", "markupsafe<2.0.1"],
        "test": ["pytest~=7.4.1"],
    },
    install_requires=[
        "boto3>=1.12.28",
        "cellprofiler-core==4.2.8",
        "centrosome~=1.2.3",
        "docutils==0.15.2",
        "h5py==3.6.0",
        "imageio==2.34.0",
        "inflect==2.1",
        "Jinja2==2.11.2",
        "joblib==1.1.0",
        "mahotas==1.4.13",
        "markupsafe==2.0.1",
        "matplotlib==3.1.3",
        "mysqlclient==2.0.3",
        "numpy==1.23.1",
        "opencv-python-headless==4.5.3.56",
        "Pillow==8.3.2",
        "prokaryote==2.4.4",
        "python-bioformats~=4.1.0",
        "python-javabridge==4.0.4",
        "pyzmq==22.3.0",
        "sentry-sdk==0.18.0",
        "requests==2.22",
        "scikit-image==0.18.3",
        "scikit-learn==0.24.1",
        "scipy==1.9.0",
        "six",
        "tifffile<2022.4.22",
        "wxPython>=4.1.0,<5",
    ],
    license="BSD",
    name="CellProfiler",
    package_data=package_data(),
    include_package_data=True,
    packages=setuptools.find_packages(exclude=["tests*"]),
    python_requires=">=3.8, <4.0",
    url="https://github.com/CellProfiler/CellProfiler",
    version=find_version("cellprofiler", "__init__.py"),
)
