from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)-> List[str]:
    '''this will return the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        for x in requirements:
            requirements=[x.replace('\n','') for x in requirements]
            if '-e .' in requirements:
                requirements.remove('-e .')
    return requirements



setup(
    name='mlpropject'
    version='0.0.1',
    author='parveen'
    author_email='parveen133012@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.tx')
)