from .base import *  # noqa

from decouple import config
from dj_database_url import parse as db_url

DEBUG = False

DATABASES = {
    "default": config("DATABASE_URL", default="sqlite://:memory:", cast=db_url)
}

# Speed up password hashing
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"
