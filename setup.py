from setuptools import setup, find_packages


VERSION = '0.0.9'
DESCRIPTION = 'Pygame Essentials'

# Setting up
setup(
    name="pygess_py",
    version=VERSION,
    author="Abhijay 'CraftyRyte' Bidari",
    author_email="craftyryte2011@gmail.com",
    license="The Unlicense",
    description=DESCRIPTION,
    long_description="J",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pygame'],
    keywords=['python', 'pygame', "essentials"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities"
    ],
    python_requires=">=3.10"
)