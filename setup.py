from setuptools import setup, find_packages

setup(
    name="mcsmapi",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "aiohttp"
    ],
    author="molanp",
    author_email= "luotian233@foxmail.com",
    description="A Pypi package based on MCSManager, designed to simplify interaction with MCSM API.",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/molanp/mcsmapi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
