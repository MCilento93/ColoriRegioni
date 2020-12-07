import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ColoreRegioni",
    version="0.0.1",
    author="Mario Cilento",
    author_email="mario.cilento.93@gmail.com",
    description="Web-scraping del sito del governo italiano per la classificazione delle misure restrittive regionali",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MCilento93/ColoreRegioni",
    packages=setuptools.find_packages(),
    install_requires=['beautifulsoup4','urllib'],
    classifiers=[
        "Programming Language :: Python :: 3.8.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)