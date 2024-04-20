# setup.py

from setuptools import setup, find_packages

setup(
    name="php_ast",
    version="1.1",
    packages=find_packages(),
    package_data={
        'php_ast': ['*.so'],
    },
    author="php_ast",
    author_email="20200120614@nxmu.edu.cn",
    description="A Python package for php_ast",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/php-ast/php_ast",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)