from setuptools import setup, find_packages

setup(
    name='CodeRunner',
    version='0.4',
    description='CodeRunner in a sandboxing environment',
    keyword='CodeRunner',
    url='http://github.com/storborg/funniest',
    author='Nguyen Hoang Son',
    author_email='nguyenhoangson@example.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['subprocess32'],
    zip_safe=False)
