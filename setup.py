from setuptools import setup, Extension
from os import path

MAJOR = 0
MINOR = 3
MICRO = 0
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='pyLithoSurferAPI',
    setup_requires=[
        'setuptools>=18.0',
        ],
    version=VERSION,
    description='Python interface to LithoSurfer REST API',
    long_description=long_description,
    url='https://github.com/rbeucher/pyLithoSurferAPI.git',
    author='Romain Beucher',
    author_email='romain@rbeucher.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',

        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=["pyLithoSurferAPI"],
    keywords='geology thermochronology fission-tracks',
    install_requires=requirements,
)
