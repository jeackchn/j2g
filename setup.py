from setuptools import setup, find_packages

import jg

setup(
    name="jg",
    version=jg.__version__,
    author=jg.__author__,
    author_email=jg.__author__,
    packages=find_packages(),
    install_requires=['graphviz'],
    license='Apache',
    url=jg.__url__,
)
