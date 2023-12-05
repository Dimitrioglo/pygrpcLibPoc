# setup.py

from setuptools import setup, find_packages

setup(
    name='todo',
    version='0.3',
    packages=find_packages(),
    install_requires=[
       "psycopg2",
    ],
)
