# setup.py

from setuptools import setup, find_packages

setup(
    name='my_grpc_poc',
    version='0.3',
    packages=find_packages(),
    install_requires=[
       "psycopg2",
       "asyncpg",
       "aiohttp-requests"
    ],
)
