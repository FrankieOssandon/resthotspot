ROOT_DIR = environ.Path(__file__) - 3  # djangohotspot/
APPS_DIR = ROOT_DIR.path('djangohotspot')  # path for django apps

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# allows you to define a function for unicode-supported Slug
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

DATABASES = {'default': env.db('DATABASE_URL', default='postgres:///djangohotspot'), }
# allows you to open and commit transaction when there are no exceptions. This could affect the performance negatively for traffic-heavy apps.
DATABASES['default']['ATOMIC_REQUESTS'] = True

EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
ADMIN_URL = env('DJANGO_ADMIN_URL', default=r'^admin/')

# add this object at the beginning of the list
PASSWORD_HASHERS = ['django.contrib.auth.hashers.Argon2PasswordHasher', (...)]

# base.py using below code

import os
import json

from django.core.exceptions import ImproperlyConfigured
with open(os.environ.get('MYSITE_CONFIG')) as f:
    configs = json.loads(f.read())


def get_env_var(setting, configs=configs):
    try:
        val = configs[setting]
        if val == 'True':
            val = True
        elif val == 'False':
            val = False
        return val
    except KeyError:
        error_msg = "ImproperlyConfigured: Set {0} environment      variable".format(setting)
        raise ImproperlyConfigured(error_msg)


# get secret key
SECRET_KEY = get_env_var("SECRET_KEY")
