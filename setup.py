#!/usr/bin/env python
#

from setuptools import setup, find_packages

setup(name='hermes_keystoneauth',
      version='2.17.0',
      description='Fork of the OpenStack Swift Keystone Auth middleware that defaults to read-only for users rather than read-write',
      url='https://github.com/CAIDA/hermes-keystoneauth',
      author='Alistair King',
      author_email='alistair@caida.org',
      license='Apache 2.0',
      packages=find_packages(),
      requires=['swift'],
      entry_points={'paste.filter_factory':
	['hermes_keystoneauth=hermes_keystoneauth.middleware:filter_factory']}
      )
