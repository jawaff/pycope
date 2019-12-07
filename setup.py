from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='pycope',
   version='1.0',
   license="Apache2",
   description='Tools for Context-Oriented Programming.',
   author='Jacob Waffle',
   author_email='thejakewaffle@gmail.com',
   url="http://www.github.com/pycope",
   long_description=long_description,
   packages=['pycope'],
)