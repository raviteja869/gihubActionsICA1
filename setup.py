from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here, e.g.,
        # 'numpy==1.21.0',
        numpy==1.21.0
        pandas==1.3.0
        pytest==6.2.4

    ],
)
