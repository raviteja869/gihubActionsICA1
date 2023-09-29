from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here, e.g.,
        "tensorflow==2.4.0",
        "numpy==1.19.0",
        "pytest==6.2.0",
        "pytest-cov==2.10.0"
    ],
)

