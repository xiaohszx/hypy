from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hypy',
    version='0.2.0',
    description='Multiplataform Hyper-V Manager using Python and FreeRDP',
    long_description=long_description,
    url='https://github.com/avanzzzi/hypy',
    author='Gabriel Avanzi, Eduardo Mendes',
    author_email='avanzzzi@gmail.com',
    license='GNU General Public License v3.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Systems Administration',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3'
    ],
    keywords='hyper-v freerdp winrm multiplatform',
    packages=find_packages(),
    install_requires=[
        'pywinrm',
        'click',
        'asciitree',
        'paramiko',
        'colorama'
    ],
    package_data={'hypy': ['hypy.conf.example']},
    entry_points={
        'console_scripts': [
            'hypy=hypy.hypy:main'
        ]
    }
)
