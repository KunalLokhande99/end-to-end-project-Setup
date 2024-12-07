from setuptools import find_packages,setup
from typing import List

# this part of code is used to sort out requirements and installs the necessary one
'''
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
'''
    
setup(
    name='SamplePrediction',
    version='0.0.1',
    author='Kunal Lokhande',
    author_email='kunallokhandea99@gmail.com',
    #install_requires=get_requirements('requirements.txt')
    install_requires=["scikit-learn","pandas","numpy"],    #..manual method
    packages=find_packages()
)