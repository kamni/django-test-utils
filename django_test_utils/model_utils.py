"""
Useful functions for commonly used Django models
"""
from django.contrib.auth.models import Group, Permission, User
from django.utils import timezone

from django_test_utils.random_generators import random_name


PASSWORD = 'test1234'

def TestUser(first_name=None, last_name=None, email=None, username=None,
             password=PASSWORD, is_staff=False, is_superuser=False, 
             is_active=True, date_joined=None, last_login=None,
             groups=None, user_permissions=None):
    """
    Creates and returns a Django User for the purposes of testing.  You may
    specify any parameters that a Django User model may have with this method
    (e.g., first_name, last_name, etc.). If a particular value for a required 
    field is not specified, this method generates a sane default value.
    
    :param first_name: string, first name of the User
    :param last_name: string, last name of the User
    :param email: string in email format, email address of the User
    :param password: string, what the User's password will be set to
    :param is_staff: boolean, makes the User a Django staff member if True
    :param is_superuser: boolean, makes the User a Django superuser if True
    :param is_active: boolean, whether the User can log in
    :param date_joined: datetime, when the User joined the site
    :param last_login: datetime, last time the User logged in, should be 
            greater than or equal to date_joined
    :param groups: list, names of Django Groups this User should belong to
    :param user_permissions: list, codenames of Django Permissions this User
            should have
    
    :return: a Django User object
    """
    tmp_fn, tmp_ln = random_name()
    first_name = first_name or tmp_fn
    last_name = last_name or tmp_ln
    
    # if username not specified, iterate until we get a unique username
    if not username:
        suffix = 0
        not_unique = True
        while not_unique:
            suffix += 1
            username = ("%s%s%d" % (first_name, last_name, suffix)).lower()
            not_unique = User.objects.filter(username=username) 
    
    user =  User.objects.create(email=email or "%s@foo.com" % username,
                                username=username,
                                first_name=first_name,
                                last_name=last_name,
                                is_staff=is_staff,
                                is_superuser=is_superuser,
                                is_active=is_active,
                                date_joined=date_joined or timezone.now(),
                                last_login=last_login or timezone.now())
    user.set_password(password)
    user.save()
    
    if groups:
        for group in groups:
            g = Group.objects.get(name=group)
            user.groups.add(g)
    if user_permissions:
        for perm in user_permissions:
            p = Permission.objects.get(codename=perm)
            user.user_permissions.add(p)
    
    return user

