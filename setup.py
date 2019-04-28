#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='cmsplugin_gallery',
    version='1.1.8',
    author='Piotr Kilczuk',
    author_email='piotr@tymaszweb.pl',
    url='http://github.com/centralniak',
    description = 'DjangoCMS image gallery plugin with drag&drop '
                  'reordering in admin, support for thumbnails and '
                  'jQueryTOOLS overlay.',
    packages=['cmsplugin_gallery'],
    provides=['cmsplugin_gallery'],
    include_package_data=True,
    install_requires = [
        'django-cms>=3.2.0',
        'django-inline-ordering>=0.1.1',
        'easy-thumbnails',
        'django-filer>=1.2.4',
    ],
    test_suite='tests.settings.run',
)
