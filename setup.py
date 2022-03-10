from pkg_resources import parse_requirements
from setuptools import setup

install_reqs = parse_requirements('requirements.txt')

setup(
    name='Bot-Moe',
    version='1.0.0',
    packages=['src', 'src.RoleManager'],
    url='',
    license='MIT',
    author='Max DeVos',
    author_email='devosmaxwell@gmail.com',
    description='Basic Bot for Gaming Discord Server'
)
