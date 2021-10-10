import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

Project_Name = "Perceptron_Pypi_package"
Username = "Sagar-modelling"

setuptools.setup(
    name=f"{Project_Name}-{Username}",
    version="0.0.1",
    author=Username,
    author_email="sagariit.kanpur1@gmail.com",
    description="Implementation of Perceptron",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{Username}/{Project_Name}",
    project_urls={
        "Bug Tracker": "https://github.com/{Usename}/{Project_Name}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "numpy"
        "logging"
    ]
)