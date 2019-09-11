import os
import setuptools

long_description = '''
# Eto-stubs
Stubs for Eto
'''


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for f in files:
            stubs.append(os.path.relpath(os.path.join(root, f), package))
    return {package: stubs}


setuptools.setup(
    name="Eto-stubs",
    version="2.5.1",
    package_data=find_stubs("Eto-stubs"),
    packages=['Eto-stubs'],
    author="Robert McNeel & Associates",
    author_email="steve@mcneel.com",
    description="Stubs for Eto",
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
