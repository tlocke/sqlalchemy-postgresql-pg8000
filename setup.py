import os
import re

from setuptools import setup

v = open(
    os.path.join(os.path.dirname(__file__),
    'sqlalchemy_postgresql_pg8000', '__init__.py'))
VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(v.read()).group(1)
v.close()

readme = os.path.join(os.path.dirname(__file__), 'README.rst')


setup(
    name='sqlalchemy_postgresql_pg8000',
    version=VERSION,
    description="PostgreSQL pg8000 dialect for SQLAlchemy",
    long_description=open(readme).read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Database :: Front-Ends',],
    keywords='SQLAlchemy PostgreSQL pg8000',
    author='Tony Locke',
    author_email='tlocke@tlocke.org.uk',
    license='MIT',
    packages=['sqlalchemy_postgresql_pg8000'],
    include_package_data=True,
    tests_require=['nose >= 0.11'],
    test_suite="run_tests.setup_py_test",
    zip_safe=False,
    entry_points={
        'sqlalchemy.dialects': [
            'postgresql = '
            'sqlalchemy_postgresql_pg8000.pg8000:PGDialect_pg8000',
            'postgresql.pg8000 = '
            'sqlalchemy_postgresql_pg8000.pg8000:PGDialect_pg8000',]})
