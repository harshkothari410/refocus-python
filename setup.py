import os
from setuptools import setup

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirements.txt') as f:
	required = f.read().splitlines()

setup(
	name="Refocus-Python",
	version="0.0.1",
	author="Harsh Kothari",
	author_email="hkothari@salesforce.com",
	install_requires=required,
	description=("Python API Libarary for Refocus"),
	license="BSD",
	keywords="refocus api library",
	url="",
	packages=['refocus', 'tests'],
	long_description=read('README.md'),
	classifiers=[
		"Development Status :: 4 - Beta",
		"Topic :: Utilities",
		"License :: OSI Approved :: BSD License",
	],
)
