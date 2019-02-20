import setuptools, os

long_description = '''
# Rhino-subs
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
    version="0.0.3",
	package_data=find_stubs("Rhino-stubs"),
    packages=['Rhino-stubs'],
    author="Robert McNeel & Associates",
    author_email="steve@mcneel.com",
    description="Stubs for RhinoCommon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ],
)
