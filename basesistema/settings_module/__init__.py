# uwsgi.py and urls.py files
# Because we’ve split the main settings file into dedicated files with configuration for each environment, we need to
# point a file which will be used by default when it’s not clearly indicated. In urls.py file we define the 4xx and
# 5xx pages. We also add debug toolbar here.
# Move uwsgi.py and urls.py files from djangohotspot/djangohotspot catalogue to config module and add following
# changes to config.settings

WSGI_APPLICATION = 'config.wsgi.application'
ROOT_URLCONF = 'config.urls'
