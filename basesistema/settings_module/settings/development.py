from .base import *

# debug toolbar
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INSTALLED_APPS += ['debug_toolbar', ]
DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': ['debug_toolbar.panels.redirects.RedirectsPanel', ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# allowed IP addresses
INTERNAL_IPS = ['127.0.0.1']

# django extensions
INSTALLED_APPS += ['django_extensions', ]
