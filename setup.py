from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='sphinx-comment-box',
    version='1.0.0',
    description='Add a comment area to sphinx webpages using HTML Comment Box.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/sasmlange/sphinx-comment-box',
    author='Maximilian Lange',
    author_email='maxhlange@gmail.com',
    license='MIT',
    packages=['sphinx-comment-box'],
    install_requires=["docutils"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2 Licence",
        "Operating System :: OS Independent",
    ],
)
