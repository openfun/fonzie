from docker_run_production import *


DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

PIPELINE_ENABLED = False
STATICFILES_STORAGE = 'openedx.core.storage.DevelopmentStorage'

STATIC_ROOT = '/data/static/lms'
STATIC_URL = '/static/'
MEDIA_ROOT = '/data/media'
LOG_DIR = '/data/log'

FEATURES['ENABLE_DISCUSSION_SERVICE'] = False

ALLOWED_HOSTS = ["*"]

LOGGING['handlers'].update(
    local={'class': 'logging.NullHandler'},
    tracking={'class': 'logging.NullHandler'},
)

INSTALLED_APPS += (
    'fonzie',
)

ROOT_URLCONF = 'lms.urls'

# Django Rest Framework (aka DRF)
REST_FRAMEWORK = {
    'ALLOWED_VERSIONS': ('1.0', ),
    'DEFAULT_VERSION': '1.0',
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
}
