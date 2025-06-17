from typing import List
from setuptools import find_packages,setup

def get_requirements(file_path:str)->List[str]:
    '''
    this function will give the requirements
    
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')


setup(
name= 'mlproject',
version='1.0.1',
author='Sudarshan',
author_email='patilsudarshan2123@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),

)