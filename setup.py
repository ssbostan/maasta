from setuptools import setup
from setuptools import find_packages

with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

setup(
    name="maasta",
    version="0.0.1",
    author="Saeid Bostandoust",
    author_email="ssbostan@linuxmail.org",
    packages=find_packages(),
    zip_safe=False,
    install_requires=required_packages,
    exclude_package_data={
        "": ["*.pyc"]
    }
)
