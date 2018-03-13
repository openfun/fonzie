from .devstack import *

update_module_store_settings(MODULESTORE, doc_store_settings=DOC_STORE_CONFIG)

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
