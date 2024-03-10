from typing import List
from setuptools import find_packages,setup

HYPEN_E_DOT='-e .'
def get_requirement(filepath:str)->List[str]: 
    with open("requirements.txt",'r') as file:
        requirement = file.readlines()

        requirement = [req.replace("\n","") for req in requirement]
        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)

    return requirement

setup(
name='ML_project',
version='0.0.1',
author='Niket',
author_email='krishnaik06@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)

