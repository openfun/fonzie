from .docker_run_production import *


DEBUG = True

PIPELINE_ENABLED = False

STATICFILES_STORAGE = "openedx.core.storage.DevelopmentStorage"

STATIC_ROOT = "/edx/app/edxapp/data/static"
STATIC_URL = "/static/"
MEDIA_ROOT = "/edx/app/edxapp/data/media"
LOG_DIR = "/data/log"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
SECRET_KEY = "foo"

ALLOWED_HOSTS = ["*"]

LOGGING["handlers"].update(
    local={"class": "logging.NullHandler"},
    tracking={"class": "logging.NullHandler"},
)

INSTALLED_APPS += ("fonzie",)

ROOT_URLCONF = "fonzie.urls.lms_root"

# Disable CourseTalk service (student course reviewing)
COURSE_REVIEWS_TOOL_PROVIDER_FRAGMENT_NAME = None
COURSE_REVIEWS_TOOL_PROVIDER_PLATFORM_KEY = None

# Django Rest Framework (aka DRF)
REST_FRAMEWORK = {
    "ALLOWED_VERSIONS": ("1.0",),
    "DEFAULT_VERSION": "1.0",
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication"
    ],
}

SIMPLE_JWT = {
    "ALGORITHM": "HS256",
    "SIGNING_KEY": "ThisIsAnExampleKeyForDevPurposeOnly",
    "USER_ID_FIELD": "username",
    "USER_ID_CLAIM": "username",
}

FEATURES["ENABLE_DISCUSSION_SERVICE"] = False

FEATURES["AUTOMATIC_AUTH_FOR_TESTING"] = True
FEATURES["RESTRICT_AUTOMATIC_AUTH"] = False

FEATURES["ENABLE_GRADE_DOWNLOADS"] = True
FEATURES["ALLOW_COURSE_STAFF_GRADE_DOWNLOADS"] = True
FEATURES["ENABLE_ASYNC_ANSWER_DISTRIBUTION"] = False
FEATURES["ENABLE_INSTRUCTOR_BACKGROUND_TASKS"] = False

GRADES_DOWNLOAD = {
    "STORAGE_CLASS": "django.core.files.storage.FileSystemStorage",
    "STORAGE_KWARGS": {
        "location": "/data/export",
        "base_url": "/api/v1.0/acl/report",
    },
}
