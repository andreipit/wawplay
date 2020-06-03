from setuptools import setup, Extension
from setuptools import find_packages

import wawplay


with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


if __name__ == "__main__":
    setup(
        name="wawplay",
        version=wawplay.__version__,
        description="WAWPLAY: What a wonderfull playground! from wawplay.engine import Engine; Engine.train('smth')",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Andrei Pit",
        author_email="developing.basis@gmail.com",
        url="https://github.com/andreipit/wawplay",
        license="MIT License",
        packages=find_packages(),
        include_package_data=True,
        platforms=["linux", "unix"],
        python_requires=">3.5.2",
        install_requires=["scikit-learn>=0.22.1"],
    )
