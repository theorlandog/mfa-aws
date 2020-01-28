#!/usr/bin/env python3
import codecs
import os.path
import re
import sys

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


install_requires = [
  'botocore',
  'boto3'
]


setup_options = dict(
    name='mfa-aws',
    version=find_version("bin", "mfa-aws"),
    description='MFA helper script for AWS',
    long_description=read('README.rst'),
    author='Theorlandog',
    url='https://github.com/theorlandog/mfa-aws',
    scripts=['bin/mfa-aws'],
    zip_safe=False,
    install_requires=install_requires,
    license="Apache License 2.0",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    data_files=[
      ("mfa-aws/config", ["config/mfa-config"]),
    ]
)



setup(**setup_options)