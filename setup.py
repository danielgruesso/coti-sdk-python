from setuptools import setup, find_packages

setup(
    name='coti-sdk',
    description='COTI SDK for Confidential Preserving network',
    version='0.1.0',
    license='Apache2.0',
    author="gmesika-coti@COTI",
    author_email='support@coti.io',
    package_dir={'': '.'},
    url='https://github.com/coti-io/coti-sdk-python',
    keywords='COTI SDK Privacy',
    install_requires=[
        'pycryptodome==3.19.0', 'cryptography==3.4.8', 'eth-keys==0.4.0', 'eth-account==0.10.0', 'web3==6.11.2'
    ],
    python_requires=">=3.9",
)
