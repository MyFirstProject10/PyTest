from setuptools import setup, find_packages

setup(
	name="firstlib",
	version="0.1",
	url="https://none",
	license="MIT",
	author="tmp",
	author_email="tmp@nomail.com",
	description="Just a test",
	packages=find_packages(exclude=["tests"]),
	long_description=open("README.md").read(),
	zip_safe=False,
	install_requires=[]
)
