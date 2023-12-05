# setup.py

from setuptools import setup, find_packages

setup(
    name='pygrpcLibPoc',
    version='0.3',
    packages=[
        "todo",
    ],
    install_requires=[
       "psycopg2",
    ],
)
