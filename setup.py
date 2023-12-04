# setup.py

from setuptools import setup, find_packages

setup(
    name='pygrpcLibPoc',
    version='0.2',
    packages=find_packages(),
    install_requires=[
       "psycopg2",
       "aiohttp-requests"
    ],
)
