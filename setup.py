from setuptools import setup, find_packages

setup(
    name='stackoverflow',
    version='1.0',
    description='StackOverflow-lite where users can ask questions and be answered',
    url='https://github.com/deathsparrow101/stackoverflow',
    author='Nicholas Barkote',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: All',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages()
)
