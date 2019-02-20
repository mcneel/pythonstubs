import setuptools, os

long_description = '''
# GH_Util-stubs
Stubs for GH_Util
'''

def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for f in files:
            stubs.append(os.path.relpath(os.path.join(root, f), package))
    return {package: stubs}

setuptools.setup(
    name="GH_Util-stubs",
    version="0.0.4",
	package_data=find_stubs("GH_Util-stubs"),
    packages=['GH_Util-stubs'],
    author="Robert McNeel & Associates",
    author_email="steve@mcneel.com",
    description="Stubs for GH_Util",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mcneel/pythonstubs",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ],
)
