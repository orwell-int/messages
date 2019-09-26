#!/usr/bin/env python

import setuptools

setuptools.setup(name='orwell::messages',
      version='1.0',
      description='Orwell messages for python',
      author='Orwell',
      url='https://github.com/orwell-int/messages',
      packages=['orwell', 'orwell.messages'],
      install_requires=[
            "protobuf==3.8.0",
            "six==1.12.0",
      ],
     )