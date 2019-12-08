from setuptools import setup
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(ROOT_DIR, "README.md"), 'r') as file:
    README = file.read()

setup(
    name='pycope',
    version='0.1.1',
    license="Apache2",
    description='A Context-Oriented Programming Extension for Python.',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Jacob Waffle',
    author_email='thejakewaffle@gmail.com',
    url="http://www.github.com/pycope",
    packages=['pycope'],
    install_requires=['immutables'],
)
