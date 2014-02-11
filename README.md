# django-test-utils

A collection of utilities for testing Django apps.

## Installation

Currently this application is in pre-alpha, and should be installed directly
from the git repository:

    pip install -e git+git://github.com/kamni/django-test-utils#egg=django-test-utils

## Usage

Currently there is a make_user function in model_utils.py. Any parameters that
you would pass to the User.objects.create method, you can pass to make_user;
however, if no parameters are passed then make_user will simply generate sane
defaults.

By default, all users created by the make_user function will be non-superuser,
non-staff users.  The default password for users is "test1234".

Examples:

    user = make_user()

    user = make_user(first_name="Warren", last_name="Piece", password="password")

    user = make_user(is_staff=True, is_superuser=True)