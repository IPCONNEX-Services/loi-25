# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable 
from module_loi25 import __version__ as version

setup(
	name='ipconnex_module_loi25',
	version=version,
	description='A frappe module adapted for law 25',
	author='Frappe',
	author_email='voip@ipconnex.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)