from setuptools import setup

with open("README.md","r")as fh:
    long_description = fh.read()

setup(
    name="animal-classifier",
    version="1.0.2",
    description="It classify the cat or dog images",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Vinay Garg",
    author_email="xvinay28x@gmail.com",
    url="https://github.com/xvinay28x/animal_classifier_library",
    install_requires=["tensorflow"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ]
    
)