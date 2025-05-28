'''
This setup.py file is essential part of packaging and 
distributinng Python Project. It is used by setuptools
(or distutils in older Python versions) to define the configuration
of your project, such as its metadata, dependencies and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open('req.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirement.txt file not found")

    return requirement_lst

print(get_requirements())

setup(
    name="NeworkSecurity",
    version="0.0.1",
    author="Aryan Diwakar",
    author_email="diwakararyan2547@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)