import setuptools
import os


setuptools.setup(
    name='social_science_ai'
    , version='0.0.3'
    , author='Nick Oh'
    , author_email="S.H.Oh1@lse.ac.uk"
    , description="AI/ML toolkits for social scientists"
    , long_description="AI/ML toolkits for social scientists"
    , long_description_content_type="text/markdown"
    , install_requires = [
        "numpy",
        "matplotlib", 
        "scipy",  
        "pandas"
    ]
    , packages=setuptools.find_packages()
    , classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)