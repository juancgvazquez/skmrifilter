# This file is part of the
#   Scikit-Learn MRI-Filter Project
#   (https://github.com/jencgvazquez/skmrifilter).
# Copyright (c) 2020, Jeremías Farrher - Juan Carlos Vázquez
# License: MIT
#   Full Text: https://github.com/juancgvazquez/skmrifilter/blob/master/LICENSE

from setuptools import setup, find_packages

# EXTERNAL DATA
# Description
with open('./README.md', 'r') as f:
    long_description = f.read()
# Version
version = {}
with open('./skmrifilter/__init__.py', 'r') as v:
    exec(v.read(), version)
# Requirements
requirements = ['numpy',
                'scikit-image',
                'sklearn']


# SETUP #
setup(name="skmrifilter",
      version=version['__version__'],
      author=['Jeremías Farrher', 'Juan Carlos Vázquez'],
      author_email='jerefarrher91@gmail.com',
      description='Package to select and chain filters for MRI Images',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/juancgvazquez/skmrifilter/',
      license='MIT',
      install_requires=requirements,
      packages=find_packages(),
      keywords=['computervision', 'images', 'mri', 'opencv', 'sklearn'],
      classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: GNU General Public License (GPL)",
                "Development Status :: 1 - Alpha",
                "Intended Audience :: Computer Vision",
                "Intended Audience :: Developers",
                "Topic :: Scientific/Engineering :: Computer Vision",
                "Topic :: Software Development :: Libraries :: Python Modules",
                  ]
      )
