from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'Pygame Essentials'

# Setting up
setup(
    name="pygess-py",
    version=VERSION,
    author="Abhijay 'CraftyRyte' Bidari",
    author_email="<craftyryte2011@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pygame'],
    keywords=['python', 'pygame', "essentials"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)