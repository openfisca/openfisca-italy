#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='OpenFisca-Italy',
    version='0.0.1',
    author='OpenFisca Team',
    author_email='contact@openfisca.org',
    description=u'OpenFisca tax and benefit system for Italy',
    keywords='benefit microsimulation social tax',
    license='http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    url='https://github.com/openfisca/openfisca-italy',
    include_package_data=True,  # Will read MANIFEST.in
    install_requires=[
        'OpenFisca-Core >= 23.1.2, < 24.0'],
    extras_require={
        'test': [
            'flake8 >= 3.4.0, < 3.5.0',
            'flake8-print',
            'nose']},
    packages=find_packages(),
    test_suite='nose.collector')
