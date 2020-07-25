import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mplus-python",
    version="0.0.1",
    author="Steffan Padel",
    author_email="git@steffanpadel.eu",
    description="Python data bindings for mangaplus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sthomasp/py_mplus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
