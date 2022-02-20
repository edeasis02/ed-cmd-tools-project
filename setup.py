import setuptools

long_description = ""
with open("README.md", "r") as fh:
	long_description = fh.read()
	
setuptools.setup(
	name="bigcorp-cmd_tools",
	version="0.0.1",
	author="Juan Dela Cruz",
	author_email="juan@delacruz.com",
	description="A collection of command line utilities.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://vcs.bigcorp.xyz/devops/cmd_tools_project",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: Other/Proprietary License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
	install_requires=(
		'requests',
	),
)