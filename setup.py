"""A setuptools for photosorter application
"""

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='photosorter',  # Required
    version='0.1.3',  # Required
    description='A application for sorting and renaming photos',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/bryndav/photosorter',  # Optional
    author='David Bryngelsson',  # Optional
    author_email='d.bryngelsson@gmail.com',  # Optional
    keywords='image sorting',  # Optional
    packages=find_packages(where='photosorter'),  # Required
    python_requires='>=2.7, <11',
    install_requires=['pillow'],  # Optional
    entry_points={  # Optional
        'console_scripts': [
            'sort=photosorter:main',
        ],
    }
)
