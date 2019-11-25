#!/usr/bin/python3
# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-16 13:47
# @Author   : 病虎
# @E-mail   : victor.xsyang@gmail.com
# @File     : setup.py
# @User     : ora
# @Software: PyCharm
#Reference:**********************************************
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TextSimilarScore",
    version="0.0.4",
    author="Ora",
    author_email="victor.xsyang@gmail.com",
    description="compute similar scores of two text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shawshany/TextSimilarScore",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.*',
)