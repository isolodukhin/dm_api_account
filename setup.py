from setuptools import setup

REQUIRES = [
    'requests',
    'allure-pytest',
    'pydantic'
]

setup(
    name='dm_api_account',
    version='0.0.1',
    packages=['dm_api_account', 'dm_api_account.apis', 'dm_api_account.models'],
    url='https://github.com/isolodukhin/dm_api_account.git',
    license='MIT',
    author='Ilya',
    author_email='',
    install_requires=REQUIRES,
    description='Client for dm_api_account'
)