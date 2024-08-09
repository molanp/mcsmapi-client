from setuptools import setup, find_packages

setup(
    name='mcsmapi-client',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    author='molanp',
    author_email='',
    description='A Pypi package based on MCSManager, designed to simplify interaction with MCSM API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/molano/mcsmapi-client',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
