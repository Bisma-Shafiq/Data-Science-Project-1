from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT='-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]  # Strip newline and remove empty strings
        if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
                
    return requirements

setup(
    name='DS_Project',
    version='0.0.1',
    author='Bisma',
    author_email='shafiqbisma648@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)
