from setuptools import setup, find_packages
import sys, os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="df",
    version="0.1",
    include_package_data=True,
    author="Simon So",
    author_email="sso4jc@gmail.com",
    packages=find_packages(),
    long_description=read('README.md')
)

