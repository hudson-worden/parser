import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="parser",
    version="0.0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.7",
    package_dir={"math_parser": ""},
)
