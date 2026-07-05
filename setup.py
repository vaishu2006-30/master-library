from setuptools import setup, find_packages

setup(
    name="calculator_master",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "calculator_basic @ git+https://github.com/vaishu2006-30/smaller-library.git@main"
    ],
)