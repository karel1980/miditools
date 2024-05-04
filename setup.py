import setuptools

long_description = """# Midi-tools"""

with open("requirements.txt", "r") as req_file:
	requirements = req_file.readlines()

setuptools.setup(
	name="midi-tools",
	version="0.0.1",
	author="Karel Vervaeke",
	author_email="karel@vervaeke.info",
	description="midi-tools",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/karel1980/midi-tools",
	packages=setuptools.find_packages(),
	classifiers=[],
	python_requires='>=3.6',
	install_requires=requirements,
	entry_points={
		'console_scripts': [
			'mt-highlight-tracks = miditools.highlight:main'
		],
	}
)

