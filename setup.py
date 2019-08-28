from setuptools import setup, find_packages

setup(
    name='decocli',
    version='0.1',
    url='https://github.com/HyeockJinKim/DecoCLI',
    license='MIT',
    author='HyeockJin Kim',
    author_email='kherootz@gmail.com',
    description='tools for python CLI using decorator',
    keywords=['CLI', 'decorator'],
    python_requires='>=3.5',
    packages=find_packages(exclude=['test']),
    long_description=open('README.md').read(),
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
