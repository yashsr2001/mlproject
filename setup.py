from setuptools import find_packages, setup

setup(
    name="my-project",
    version="0.1.0",
    description="A short description of the project",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        # Add your dependencies here
    ],
)