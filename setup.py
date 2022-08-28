import setuptools
from pkg_resources import parse_requirements

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hyperplane-definitions",
    version="0.0.1",
    author="Hyperplane",
    author_email="adam@hyperplane.cloud",
    description="Constant values across the platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='This code is property of Hyperplane, all rights reserved',
    url="https://tons.ai",
    project_urls={
        "Bug Tracker": "https://github.com/hyperplane-cloud/hyperplane-definitions/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    install_reqs = parse_requirements('python/requirements.txt'),
    python_requires=">=3.6",
)