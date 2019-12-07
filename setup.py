import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='pycope',
    version='0.1.0',
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
