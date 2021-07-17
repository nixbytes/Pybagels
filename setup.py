from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='PyBagels',
    version='2021.07.17',
    author='nixbytes',
    author_email='real8686@gmail.com',
    description='A guessing Game from project from the book "The big Book of Small Python Projects"',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nixbytes/pybagels',
    packages=find_packages('bagels')
)