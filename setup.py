from setuptools import setup, find_packages


VERSION = '0.2.2'
DESCRIPTION = 'Pygame Essentials'
LONG_DESCRIPTION = "This is a library that makes developing in pygame simple for beginners. It has classes like BasicEntity, RectEntity, BasicMovingEntity etc. These 'templates' help beginners create their first games with ease. These templates are kept highly customizable and have a high scope for custom logic. This library currently (as of v0.1.1) contains only Entity classes and a master object list."

# Setting up
setup(
    name="pygess_py",
    version=VERSION,
    author="Abhijay 'CraftyRyte' Bidari",
    author_email="craftyryte2011@gmail.com",
    license="The Unlicense",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
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