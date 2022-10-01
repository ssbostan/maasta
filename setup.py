# MAASTA (MAAS Terraform Ansible)
# https://github.com/ssbostan/maasta

from os import environ

from setuptools import find_packages, setup

from maasta import __version__

if environ.get("ENV", "production") == "development":
    with open("requirements.dev.txt") as f:
        required_packages = f.readlines()
else:
    with open("requirements.txt") as f:
        required_packages = f.readlines()

with open("README.md") as f:
    readme = f.read()

setup(
    name="maasta",
    version=__version__,
    url="https://github.com/ssbostan/maasta",
    description="MAAS Terraform Ansible",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    author="Saeid Bostandoust",
    author_email="ssbostan@yahoo.com",
    packages=find_packages(),
    install_requires=required_packages,
    include_package_data=False,
    zip_safe=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Framework :: Ansible",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: System :: Installation/Setup",
    ],
)
