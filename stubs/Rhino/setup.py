import setuptools
import os

long_description = '''
# Rhino-stubs
Stubs for RhinoCommon
'''


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for f in files:
            stubs.append(os.path.relpath(os.path.join(root, f), package))
    return {package: stubs}


setuptools.setup(
    name="Rhino-stubs",
    version="7.0.19239",
    package_data=find_stubs("Rhino-stubs"),
    packages=['Rhino-stubs'],
    author="Robert McNeel & Associates",
    author_email="steve@mcneel.com",
    description="Stubs for RhinoCommon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mcneel/pythonstubs",
    install_requires=['Grasshopper-stubs', 'GH_Util-stubs', 'GH_IO-stubs'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ],
)
