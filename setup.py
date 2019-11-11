import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="USEFULTOOL", # Replace with your own username
    version="0.0.1",
    author="xiaojueguan",
    author_email="xiaojueguan@gmail.com",
    description="A useful python cli tool suit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/albertjone/easy_platform",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)