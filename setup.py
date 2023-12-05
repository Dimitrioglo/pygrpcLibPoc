# setup.py

from setuptools import setup, find_packages

setup(
    name='todo',
    version='0.3',
    packages=[
        "todo",
    ],
    install_requires=[
       "psycopg2",
    ],
)
