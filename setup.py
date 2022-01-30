import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="urb",
    version="0.1.3",
    description="a command line dictionary and wrapper for various dictionary APIs",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/addyett/urb",
    author="addyett",
    author_email="g.aditya2048@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: POSIX :: Linux",
    ],
    packages=["urb", "wrappers"],
    include_package_data=True,
    install_requires=["pyfiglet", "requests", "click"],
    entry_points={
        "console_scripts": [
            "urb=urb.__main__:main",
        ]
    },
)
