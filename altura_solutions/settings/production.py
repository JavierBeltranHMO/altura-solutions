from .base import *

DEBUG = False

STORAGES["staticfiles"][
    "BACKEND"
] = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

ALLOWED_HOSTS = ["localhost", "165.22.133.102", "altura-solutions.duckdns.org"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}

cwd = os.getcwd()
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache",
    }
}

import sentry_sdk

sentry_sdk.init(
    dsn="https://2e81bb4a7be1870ae55204d15b026a4a@o4509918350934016.ingest.us.sentry.io/4509918352703488",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

# settings/base.py o settings/production.py
from django.contrib.staticfiles.storage import ManifestStaticFilesStorage

STATIC_ROOT = os.path.join(BASE_DIR, "static")


class IgnoreMissingManifestFilesStorage(ManifestStaticFilesStorage):
    def post_process(self, *args, **kwargs):
        for item in super().post_process(*args, **kwargs):
            try:
                yield item
            except ValueError as e:
                if "could not be found" in str(e):
                    continue
                else:
                    raise


STATICFILES_STORAGE = (
    "altura_solutions.settings.production.IgnoreMissingManifestFilesStorage"
)

try:
    from .local import *
except ImportError:
    pass
