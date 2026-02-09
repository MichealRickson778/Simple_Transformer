from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="language Translator",
    version="0.1",
    author="Micheal",
    packages=find_packages(),
    install_requires = requirements
)




