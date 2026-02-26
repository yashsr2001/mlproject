from setuptools import find_packages, setup # type: ignore


def get_requirements(file_path):
    with open(file_path) as f:
        requirements = f.read().splitlines()
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name="mlproject",
    version="0.1.0",
    description="End-to-end machine learning project structure",
    author="Yash",
    author_email="yashrevankar17@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=get_requirements('requirements.txt')
)