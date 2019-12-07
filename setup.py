from setuptools import setup
import os 

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(ROOT_PATH, "README"), 'r') as f:
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