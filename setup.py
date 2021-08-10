from io import open
from setuptools import setup, find_packages

from direct_api import __version__


def read(f):
    return open(f, "r").read()


setup(
    name="yandex-direct-api",
    version=__version__,
    packages=find_packages(exclude=("tests",)),
    install_requires=["requests>=2.22.0"],
    description="Api wrapper for YandexDirect API v5",
    author="bzdvdn",
    author_email="bzdv.dn@gmail.com",
    url="https://github.com/bzdvdn/yandex-direct-api-wrapper",
    license="MIT",
    python_requires=">=3.6",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
)
