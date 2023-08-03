from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pets/__init__.py
from pets import __version__ as version

setup(
	name="pets",
	version=version,
	description="pets",
	author="Itsystematic",
	author_email="sales@itsystematic.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
