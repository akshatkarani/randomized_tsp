import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="randomized_tsp", # Replace with your own username
    version="0.0.2",
    author="Akshat Karani",
    author_email="akshatkarani@gmail.com",
    description="Randomized algorithms for Travelling Salesman Problem",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akshatkarani/randomized_tsp",
    packages=setuptools.find_packages(),
    keywords=['travelling salesman problem', 'tsp', 'randomized algorithm'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
