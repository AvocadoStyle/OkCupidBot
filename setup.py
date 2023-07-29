from setuptools import setup, find_packages

requirements = ''
# Read requirements from requirements.txt file
with open('requirements.txt') as f:
    requirements = f.readlines()

# Remove newlines and comments from the requirements list
requirements = [line.strip() for line in requirements if not line.strip().startswith('#')]


setup(
    name='ok_cupid_tool',
    version='0.1.0',
    packages=find_packages(include=['OkCupidBot', 'OkCupidBot.*']),
    install_requires=requirements
)