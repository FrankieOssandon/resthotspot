WSGI_APPLICATION = 'config.wsgi.application'
ROOT_URLCONF = 'config.urls'

# In our example, config.uwsgi file will look like this:
# view sourceprint?

import os
import sys

from django.core.wsgi import get_wsgi_application
app_path = os.path.dirname(os.path.abspath(__file__)).replace('/config', '')
sys.path.append(os.path.join(app_path, 'djangohotspot'))

if os.environ.get('DJANGO_SETTINGS_MODULE') == 'config.settings.production':
    from raven.contrib.django.raven_compat.middleware.wsgi import Sentry

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

application = get_wsgi_application()
if os.environ.get('DJANGO_SETTINGS_MODULE') == 'config.settings.production':
    application = Sentry(application)
