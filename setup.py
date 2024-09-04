from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    page_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='image_processing',
    version='0.0.1',
    author='jorgemaciel',
    author_email='jorge.maciel.jr@gmail.com',
    description='App for Image processing',
    long_description=page_description,
    long_description_content_type=['text/plain', 'text/markdown', 'text/x-rst'],
    url='https://github.com/jorgemaciel/image-processing-package',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.9'
)