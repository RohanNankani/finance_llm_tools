from setuptools import setup, find_packages

setup(
    name="finance_tools",
    version="0.1",
    packages=find_packages(),  # Automatically finds and includes all subpackages
    install_requires=[
        "requests", 
    ],
    author="Rohan Nankani",
    author_email="rohan.nankani2021@example.com",
    description="A wrapper for the finance API clients and tools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)