from setuptools import setup, find_packages

setup(
    name="matrix-gen",
    description="",
    version="0.0.1",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "dependency-injector",
        "matrix-sum @ https://github.com/yari61/otus-patterns-adapter-p1/tarball/master"
    ]
)
