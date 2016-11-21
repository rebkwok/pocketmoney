from setuptools import setup

setup(
    name='pocketmoney',
    version='0.1',
    py_modules=['pocketmoney'],
    install_requires=[
        'Click',
        'google-api-python-client'
    ],
    entry_points='''
        [console_scripts]
        pocketmoney=pocketmoney:cli
    ''',
)
