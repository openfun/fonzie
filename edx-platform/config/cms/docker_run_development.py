from docker_run_production import *


DEBUG = True

REQUIRE_DEBUG = True

STATICFILES_STORAGE = "openedx.core.storage.DevelopmentStorage"

PIPELINE_ENABLED = False

EMAIL_BACKEND = config(
    "EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

ALLOWED_HOSTS = ["*"]

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

MEDIA_ROOT = "/edx/app/edxapp/data"
STATIC_ROOT = "/edx/app/edxapp/data/static/studio"
