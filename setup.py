# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

requirements = [
    "pythainlp>=4.0",
    "sentence-transformers",
    "transformers",
    "sentencepiece"
]

with open('README.md','r',encoding='utf-8-sig') as f:
    readme = f.read()

setup(
    name="KhamYo",
    version="0.3.0",
    description="Thai abbreviation to full text library",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Wannaphong Phatthiyaphaibun",
    author_email="wannaphong@yahoo.com",
    url="https://github.com/wannaphong/KhamYo",
    packages=find_packages(exclude=["tests", "tests.*"]),
    test_suite="tests",
    python_requires=">=3.6",
    package_data={
        "khamyo": [
            "*",
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords=[
        "NLP",
        "natural language processing",
        "text analytics",
        "text processing",
        "localization",
        "computational linguistics",
        "ThaiNLP",
        "Thai NLP",
        "Thai language",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Thai",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing :: Linguistic",
    ],
    project_urls={
        "Source Code": "https://github.com/wannaphong/KhamYo",
        "Bug Tracker": "https://github.com/wannaphong/KhamYo/issues",
    },
)
