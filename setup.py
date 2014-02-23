import os
from setuptools import setup, find_packages

ROOT = os.path.abspath(os.path.dirname(__file__))

base_config = {'name': 'django_test_utils',
               'version': '0.0.2',
               'description': 'A collection of utilities for testing Django apps.',
               'long_description': open(os.path.join(ROOT, 'README.md')).read(),
               'author': 'J Leadbetter',
               'author_email': 'codemonkey@jleadbetter.com',
               'url': 'http://bitbucket.org/kamni/django-test-utils',
               'license': 'Affero GPL v3',
               'packages': find_packages(),
               'include_package_data': True,
               'zip_safe': False,
               'install_requires': ['Django>=1.5'],
               'classifiers': ['Development Status :: 2 - Pre-Alpha',
                               'Environment :: Web Environment',
                               'Framework :: Django',
                               'Intended Audience :: Developers',
                               'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
                               'Programming Language :: Python :: 2 :: Only']
              }

setup(**base_config)