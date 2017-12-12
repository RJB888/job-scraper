"""."""

from setuptools import setup

setup(

    name='scraper',
    description='job scraper',
    package_dir={'': 'src'},
    author='Robert Bronson',
    author_email='robert.j.bronson@gmail.com',
    py_modules=['scraper',
    install_requires=[requests, BS4],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'tox'],
        'development': ['ipython']
    },
    entry_points={}

)
