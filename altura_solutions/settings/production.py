from .base import *

DEBUG = False

STORAGES["staticfiles"][
    "BACKEND"
] = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

ALLOWED_HOSTS = ["localhost", "", ""]

DATABASES = {
    "default":{
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "altura_solutions",
        "USER": "altura_solutions",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}

cwd = os.getcwd()
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache",
    }
}

try:
    from .local import *
except ImportError:
    pass
