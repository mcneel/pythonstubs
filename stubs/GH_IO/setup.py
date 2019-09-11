import setuptools
import os

long_description = '''
# GH_IO-stubs
Stubs for GH_IO
'''


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for f in files:
            stubs.append(os.path.relpath(os.path.join(root, f), package))
    return {package: stubs}


setuptools.setup(
    name="GH_IO-stubs",
    version="7.0.19250",
    package_data=find_stubs("GH_IO-stubs"),
    packages=['GH_IO-stubs'],
    author="Robert McNeel & Associates",
    author_email="steve@mcneel.com",
    description="Stubs for GH_IO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mcneel/pythonstubs",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ],
)
