#!/usr/bin/env python

from setuptools import setup

setup(name='Firmware_Slap',
      version='1.0',
      description='Tools to find bugs in firmware',
      author='Christopher Roberts',
      author_email='roberts.michael.christopher@gmail.com',
      url='https://github.com/ChrisTheCoolHut/Firmware_Slap',
      packages=['firmware_slap'],
      scripts=['bin/Vuln_Discover_Celery.py', 'bin/Vuln_Cluster_Celery.py',
          'bin/Discover_And_Dump.py', 'bin/Load_And_View_Results.py'],
      include_package_data=True,
      install_requires=[
          "tqdm",
          "python-magic",
          "matplotlib",
          "r2pipe",
          "psutil",
          "termcolor",
          "celery",
          "flower",
          "elasticsearch==7.8.0",
          "numpy==1.26.4",
          "scikit-learn",
          "ipython==7.19.0",
          "angr==8.20.7.6",
          "unicorn==1.0.2rc4",
          "capstone==5.0.6"
          ],
     )
