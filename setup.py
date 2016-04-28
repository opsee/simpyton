from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='simpyton',
    version='0.0.1',
    description='Ties HTTP service models to endpoints so you get the responses you want.',
    long_description=readme,
    author='dan compton',
    author_email='dan@opsee.com',
    url='https://github.com/opsee/simpyton',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
