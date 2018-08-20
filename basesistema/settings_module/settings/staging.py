# Configuring test settings, start with turning debugging off:

DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = False

# Store sent mails in memory. They are available in django.core.mail.outbox:

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# Set the cache:

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# Set the password hasher to speed up the tests:

PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher', ]

# If you use Django templates, you can set them to be stored in memory:

TEMPLATES[0]['OPTIONS']['loaders'] = [
    ['django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
     'django.template.loaders.app_directories.Loader', ], ], ]
